#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import pathlib
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time


ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"
ARTIFACTS = ROOT / "artifacts"
LOGS = ARTIFACTS / "_logs"
FAMILY_ARTIFACTS = ARTIFACTS / "families"
FAMILY_SUMMARY = FAMILY_ARTIFACTS / "summary.md"
RUNTIME_STATE = LOGS / "runtime_state.json"
LEDGER = ROOT / "ledger.md"
PROOFS = ROOT / "PROOFS.md"
QUEUE = ROOT / "queue.json"
FAILED = ROOT / "failed_problems.json"
SELECTED = ROOT / "selected_problem.md"
AGENTS_FILE = ROOT / "AGENTS.md"
MEMORY_DIR = ROOT / "memory"
PAPER_MEMORY = MEMORY_DIR / "paper_memory.json"
SEARCH_MEMORY = MEMORY_DIR / "search_memory.json"
CAMPAIGN_MANIFEST = ROOT / "campaigns" / "manifest.json"
STOP_MARKER = ROOT / ".stop_harness"
CAPABILITIES_CACHE = LOGS / "codex_capabilities.json"

PUBLICATION_STATUS_RANK = {
    "NONE": 0,
    "INSTANCE_ONLY": 1,
    "REDISCOVERY": 2,
    "SLICE_CANDIDATE": 3,
    "SLICE_EXACT": 4,
    "FAMILY_CANDIDATE": 5,
    "PAPER_READY": 6,
}

CURATION_TIMEOUT = int(os.environ.get("AUTOMATH_CURATION_TIMEOUT", "660"))
SOLVE_TIMEOUT = int(os.environ.get("AUTOMATH_SOLVE_TIMEOUT", "1200"))
VERIFY_TIMEOUT = int(os.environ.get("AUTOMATH_VERIFY_TIMEOUT", "720"))
GENERALIZE_TIMEOUT = int(os.environ.get("AUTOMATH_GENERALIZE_TIMEOUT", "1800"))
PUBLICATION_AUDIT_TIMEOUT = int(os.environ.get("AUTOMATH_PUBLICATION_AUDIT_TIMEOUT", "1200"))
LEAN_TIMEOUT = int(os.environ.get("AUTOMATH_LEAN_TIMEOUT", "1800"))
PROOF_ATTEMPT_TIMEOUT = int(os.environ.get("AUTOMATH_PROOF_ATTEMPT_TIMEOUT", "1800"))
PARALLEL_WORKER_WAIT_TIMEOUT = int(os.environ.get("AUTOMATH_PARALLEL_WORKER_WAIT_TIMEOUT", "90"))
WORKTREE_REMOVE_TIMEOUT = int(os.environ.get("AUTOMATH_WORKTREE_REMOVE_TIMEOUT", "30"))
PARALLEL_FEEDER_WORKERS = int(os.environ.get("AUTOMATH_PARALLEL_FEEDER_WORKERS", "3"))
PARALLEL_PROOF_ATTEMPTS = int(os.environ.get("AUTOMATH_PARALLEL_PROOF_ATTEMPTS", "2"))
PUBLICATION_AUDIT_MIN_INTERVAL = int(os.environ.get("AUTOMATH_PUBLICATION_AUDIT_MIN_INTERVAL", "1800"))
FRONTIER_REFRESH_MIN_INTERVAL = int(os.environ.get("AUTOMATH_FRONTIER_REFRESH_MIN_INTERVAL", "1800"))
PROOF_ATTEMPT_MIN_INTERVAL = int(os.environ.get("AUTOMATH_PROOF_ATTEMPT_MIN_INTERVAL", "3600"))
SECONDARY_WORKER_MIN_INTERVAL = int(os.environ.get("AUTOMATH_SECONDARY_WORKER_MIN_INTERVAL", "1800"))
SECONDARY_WORKER_FAILURE_BACKOFF = int(os.environ.get("AUTOMATH_SECONDARY_WORKER_FAILURE_BACKOFF", "3600"))
RECENT_AFFILIATED_ARTIFACT_LIMIT = int(os.environ.get("AUTOMATH_RECENT_AFFILIATED_ARTIFACT_LIMIT", "12"))

CAMPAIGN_LEAN_SURFACE_HINTS = {
    "zero_divisor_prime_labelings": [
        ROOT / "lean" / "AutoMath" / "Families" / "ZeroDivisorSupports.lean",
        ROOT / "lean" / "AutoMath" / "Families" / "ZeroDivisorReductions.lean",
        ROOT / "lean" / "AutoMath" / "Families" / "ZeroDivisorRingBridges.lean",
        ROOT / "artifacts" / "families" / "zero_divisor_prime_labelings" / "lean",
    ],
    "cnbc_quintic_nonexistence": [
        ROOT / "lean" / "AutoMath" / "Families" / "CNBCQuinticRouteI.lean",
        ROOT / "artifacts" / "families" / "cnbc_quintic_nonexistence" / "lean",
    ],
}


def now_str() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat()


def today_str() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d")


def ensure_state() -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    FAMILY_ARTIFACTS.mkdir(parents=True, exist_ok=True)
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    if not RUNTIME_STATE.exists():
        RUNTIME_STATE.write_text("{}\n", encoding="utf-8")
    try:
        subprocess.run(
            ["git", "worktree", "prune"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except Exception:
        pass
    cleanup_stale_worker_processes()
    if not LEDGER.exists():
        LEDGER.write_text("# Ledger\n", encoding="utf-8")
    if not QUEUE.exists():
        QUEUE.write_text("[]\n", encoding="utf-8")
    if not FAILED.exists():
        FAILED.write_text("[]\n", encoding="utf-8")
    if not SELECTED.exists():
        SELECTED.write_text("# Selected Problem\n\nNo problem selected yet.\n", encoding="utf-8")
    if not PAPER_MEMORY.exists():
        PAPER_MEMORY.write_text("{}\n", encoding="utf-8")
    if not SEARCH_MEMORY.exists():
        SEARCH_MEMORY.write_text("{}\n", encoding="utf-8")


def append_ledger(message: str) -> None:
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(f"- {message}\n")


def append_cycle_log(message: str) -> None:
    with (LOGS / "cycle.log").open("a", encoding="utf-8") as fh:
        fh.write(f"{message}\n")


def load_json(path: pathlib.Path, default):
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def write_json(path: pathlib.Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, indent=2) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")


def write_stable_memory_json(path: pathlib.Path, data: dict) -> None:
    existing = load_json(path, {})
    if isinstance(existing, dict):
        existing_core = {k: v for k, v in existing.items() if k != "generated_on"}
        new_core = {k: v for k, v in data.items() if k != "generated_on"}
        if existing_core == new_core and existing.get("generated_on"):
            data = dict(data)
            data["generated_on"] = existing["generated_on"]
    write_json(path, data)


def compact_text(value, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 3)].rstrip() + "..."


def load_runtime_state() -> dict:
    data = load_json(RUNTIME_STATE, {})
    return data if isinstance(data, dict) else {}


def update_runtime_campaign_state(family_slug: str, **updates) -> None:
    state = load_runtime_state()
    campaigns = state.setdefault("campaigns", {})
    campaign_state = campaigns.setdefault(family_slug, {})
    for key, value in updates.items():
        if value is None:
            campaign_state.pop(key, None)
        else:
            campaign_state[key] = value
    write_json(RUNTIME_STATE, state)


def runtime_campaign_state(family_slug: str) -> dict:
    state = load_runtime_state()
    campaigns = state.get("campaigns", {})
    campaign_state = campaigns.get(family_slug, {})
    return campaign_state if isinstance(campaign_state, dict) else {}


def ledger_tail(lines: int = 6) -> list[str]:
    if not LEDGER.exists():
        return []
    text = LEDGER.read_text(encoding="utf-8").splitlines()
    return text[-lines:]


def emit_status_line(message: str) -> None:
    print(message)
    append_cycle_log(message)


def slug_of(item) -> str | None:
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        return item.get("slug")
    return None


def within_root(path: pathlib.Path) -> bool:
    try:
        path.resolve().relative_to(ROOT)
        return True
    except ValueError:
        return False


def iter_signature_files(path: pathlib.Path) -> list[pathlib.Path]:
    if path.is_file():
        return [path]
    if not path.exists():
        return []
    files: list[pathlib.Path] = []
    for candidate in sorted(path.rglob("*")):
        if candidate.is_file() and ".git" not in candidate.parts:
            files.append(candidate)
    return files


def path_signature(paths: list[pathlib.Path]) -> str:
    digest = hashlib.sha256()
    seen: set[str] = set()
    for original in paths:
        path = original.resolve() if original.exists() else original
        key = str(path)
        if key in seen:
            continue
        seen.add(key)
        label = path.relative_to(ROOT) if within_root(path) else path
        if not path.exists():
            digest.update(f"MISSING:{label}\n".encode("utf-8"))
            continue
        files = iter_signature_files(path)
        if not files:
            digest.update(f"EMPTY:{label}\n".encode("utf-8"))
            continue
        for file_path in files:
            rel = file_path.relative_to(ROOT) if within_root(file_path) else file_path
            digest.update(f"FILE:{rel}\n".encode("utf-8"))
            digest.update(hashlib.sha256(file_path.read_bytes()).digest())
    return digest.hexdigest()


def kill_process_group(proc: subprocess.Popen, sig: signal.Signals = signal.SIGKILL) -> None:
    try:
        os.killpg(proc.pid, sig)
    except ProcessLookupError:
        pass


def listed_worktree_paths() -> set[pathlib.Path]:
    try:
        result = subprocess.run(
            ["git", "worktree", "list", "--porcelain"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except Exception:
        return set()
    if result.returncode != 0:
        return set()
    worktrees: set[pathlib.Path] = set()
    for line in result.stdout.splitlines():
        if line.startswith("worktree "):
            worktrees.add(pathlib.Path(line.removeprefix("worktree ")).resolve())
    return worktrees


def cleanup_stale_worker_processes() -> None:
    worktrees_root = (ROOT / ".worktrees").resolve()
    active_worktrees = listed_worktree_paths()
    try:
        result = subprocess.run(
            ["ps", "-axo", "pid=,command="],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except Exception:
        return
    if result.returncode != 0:
        return
    worktree_pattern = re.escape(str(worktrees_root)) + r"/([^/\s]+)"
    killed: list[int] = []
    for line in result.stdout.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        parts = stripped.split(maxsplit=1)
        if len(parts) != 2:
            continue
        pid_text, command = parts
        if str(worktrees_root) not in command:
            continue
        match = re.search(worktree_pattern, command)
        if match is None:
            continue
        worktree_path = (worktrees_root / match.group(1)).resolve()
        if worktree_path in active_worktrees:
            continue
        try:
            pid = int(pid_text)
        except ValueError:
            continue
        if pid == os.getpid():
            continue
        try:
            os.kill(pid, signal.SIGKILL)
            killed.append(pid)
        except ProcessLookupError:
            continue
        except PermissionError:
            continue
    if killed:
        append_ledger(
            f"Cleaned up {len(killed)} stale worker process(es) from removed git worktrees before starting the next cycle."
        )


def failed_slug_set() -> set[str]:
    return {slug for slug in (slug_of(item) for item in load_json(FAILED, [])) if slug}


def queue_has_usable(required_entry_type: str | None = None) -> bool:
    if required_entry_type == "paper_candidate":
        return bool(usable_paper_candidates())
    failed = failed_slug_set()
    queue = load_json(QUEUE, [])
    return any(
        isinstance(item, dict)
        and item.get("slug")
        and item["slug"] not in failed
        and (required_entry_type is None or item.get("entry_type") == required_entry_type)
        for item in queue
    )


def wait_for_usable_queue(required_entry_type: str | None = None, attempts: int = 5, sleep_seconds: int = 2) -> bool:
    for _ in range(attempts):
        if queue_has_usable(required_entry_type=required_entry_type):
            return True
        time.sleep(sleep_seconds)
    return False


def status_value(path: pathlib.Path, key: str):
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    return data.get(key)


def normalize_candidate_pending_lean(path: pathlib.Path) -> None:
    if not path.exists():
        return
    data = load_json(path, {})
    if data.get("classification") == "EXACT" and not data.get("lean_complete", False):
        data["classification"] = "CANDIDATE"
        data.setdefault("next_action", "run Lean on the exact intended statement")
    write_json(path, data)


def publication_stop_ready(path: pathlib.Path) -> bool:
    if not path.exists():
        return False
    data = load_json(path, {})
    if data.get("publication_status") != "PAPER_READY":
        return False
    return bool(data.get("proof_artifacts_preserved") or data.get("lean_complete"))


def ensure_publication_defaults(path: pathlib.Path) -> None:
    if not path.exists():
        return
    data = load_json(path, {})
    changed = False
    if "publication_status" not in data:
        classification = data.get("classification")
        if classification == "REDISCOVERY":
            data["publication_status"] = "REDISCOVERY"
        elif classification == "EXACT":
            data["publication_status"] = "INSTANCE_ONLY"
        else:
            data["publication_status"] = "NONE"
        changed = True
    if "publication_confidence" not in data:
        data["publication_confidence"] = data.get("confidence", "medium")
        changed = True
    if changed:
        write_json(path, data)


def parse_status_timestamp(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value)
    except ValueError:
        return None


def add_text_section(lines: list[str], heading: str, value) -> None:
    if value is None:
        return
    text = str(value).strip()
    if not text:
        return
    lines.extend([f"## {heading}", text, ""])


def render_selected_problem(entry: dict) -> None:
    lines = [f"# {entry.get('title', 'Untitled Entry')}", ""]
    for key in [
        "entry_type",
        "slug",
        "worker_role",
        "family_slug",
        "family_name",
        "campaign_priority",
        "canonical_source",
        "open_status_checked_on",
        "dossier_path",
        "artifact_dir",
        "attempt_kind",
        "attack_style",
        "curation_confidence",
        "publication_status",
        "campaign_affinity",
        "publication_if_solved",
        "publication_if_solved_score",
        "solve_to_publication_distance",
        "single_pass_proof_plausibility",
        "novelty_check_cost",
        "formalization_overhead",
        "write_scope",
        "packaging_risk",
        "needs_feeder_ladder",
        "pre_solve_gate",
        "publication_packet_quality",
        "handoff_memo_path",
        "working_packet_path",
        "paper_shape",
    ]:
        value = entry.get(key)
        if value is None:
            continue
        if isinstance(value, (list, dict)):
            rendered = json.dumps(value)
        else:
            rendered = str(value)
        lines.append(f"- {key}: `{rendered}`")
    lines.append("")

    for key in [
        "question",
        "family_statement",
        "canonical_statement",
        "intended_statement",
        "theorem_slice_hint",
        "theorem_slice_target",
        "fallback_target",
        "next_blocker",
        "why_now",
        "why_reasoning_friendly",
        "why_low_token",
        "verifier_hint",
        "lean_hint",
        "rediscovery_risk",
        "why_still_appears_open",
        "why_this_could_be_publishable",
        "pre_solve_gate_reason",
        "publication_packet_title",
        "publication_packet_frontier_basis",
        "publication_packet_near_paper_reason",
        "publication_packet_literature_scope",
        "publication_packet_artifact_requirements",
        "context_budget",
        "paper_shape",
        "strongest_honest_claim",
        "attempt_goal",
        "attempt_output_markdown",
        "attempt_output_json",
        "stop_condition",
        "next_action",
    ]:
        add_text_section(lines, key, entry.get(key))

    for list_key in ["definitions", "seed_instances", "publication_targets", "next_feeder_instances", "red_flags", "publication_red_flags", "allowed_files"]:
        values = entry.get(list_key) or []
        if not values:
            continue
        lines.append(f"## {list_key}")
        for item in values:
            lines.append(f"- {item}")
        lines.append("")

    SELECTED.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def sync_selected_problem_to_queue(queue_entries: list[dict] | None = None) -> None:
    entries = queue_entries if queue_entries is not None else load_json(QUEUE, [])
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("slug"):
            continue
        render_selected_problem(entry_with_working_packet(entry))
        return
    SELECTED.write_text("# Selected Problem\n\nNo problem selected yet.\n", encoding="utf-8")


PAPER_DISTANCE_RANK = {
    "tiny": 0,
    "short": 1,
    "short-medium": 2,
    "medium": 3,
    "long": 4,
    "very_long": 5,
}

PLAUDIBILITY_RANK = {
    "very_high": 0,
    "high": 1,
    "medium-high": 2,
    "medium": 3,
    "medium-low": 4,
    "low": 5,
}

PUBLICATION_IF_SOLVED_SCORE_RANK = {
    "instant_paper": 0,
    "standalone_short_paper": 1,
    "paper_with_light_packaging": 2,
    "paper_with_moderate_packaging": 3,
    "paper_with_heavy_packaging": 4,
}

COST_RANK = {
    "very_low": 0,
    "low": 1,
    "low-medium": 2,
    "medium": 3,
    "medium-high": 4,
    "high": 5,
    "very_high": 6,
}

PACKET_QUALITY_RANK = {
    "excellent": 0,
    "strong": 1,
    "adequate": 2,
    "weak": 3,
}

PAPER_CANDIDATE_REQUIRED_FIELDS = [
    "publication_if_solved",
    "publication_if_solved_score",
    "solve_to_publication_distance",
    "single_pass_proof_plausibility",
    "novelty_check_cost",
    "formalization_overhead",
    "packaging_risk",
    "needs_feeder_ladder",
    "paper_shape",
    "pre_solve_gate",
    "pre_solve_gate_reason",
    "publication_packet_title",
    "publication_packet_frontier_basis",
    "publication_packet_near_paper_reason",
    "publication_packet_literature_scope",
    "publication_packet_artifact_requirements",
    "publication_packet_quality",
]

TRUE_VALUES = {"yes", "true", "pass", "1"}
FALSE_VALUES = {"no", "false", "fail", "0"}

SUBAGENT_CONTEXT_BUDGET = "1 candidate or campaign, at most 1 dossier, target 3-6 source files, and 1 explicit output file pair."
SOLVER_SIDECAR_ROLES = {"solver-A", "solver-B"}
FAMILY_ATTEMPT_ROLES = {
    "direct_family_proof": "solver-A",
    "obstruction_boundary": "solver-B",
}


def normalized_rank(value, mapping: dict[str, int], default: int) -> int:
    if value is None:
        return default
    text = str(value).strip().lower().replace(" ", "_")
    return mapping.get(text, default)


def normalized_flag(value) -> bool | None:
    if value is None:
        return None
    text = str(value).strip().lower().replace(" ", "_")
    if text in TRUE_VALUES:
        return True
    if text in FALSE_VALUES:
        return False
    return None


def missing_fields(entry: dict, fields: list[str]) -> list[str]:
    missing: list[str] = []
    for field in fields:
        value = entry.get(field)
        if value in (None, "", []):
            missing.append(field)
    return missing


def dedupe_paths(paths: list[pathlib.Path]) -> list[pathlib.Path]:
    seen: set[str] = set()
    deduped: list[pathlib.Path] = []
    for path in paths:
        key = str(path)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(path)
    return deduped


def relative_display(path: pathlib.Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def candidate_working_packet_path(slug: str) -> pathlib.Path:
    return ROOT / "artifacts" / slug / "working_packet.md"


def build_candidate_working_packet(entry: dict) -> str:
    slug = entry["slug"]
    packet_title = entry.get("publication_packet_title") or entry.get("title") or slug
    bounded_sources = [
        entry.get("canonical_source"),
        entry.get("publication_packet_literature_scope"),
        relative_display(ROOT / "artifacts" / slug / "record.md"),
        relative_display(ROOT / "artifacts" / slug / "status.json"),
    ]
    if isinstance(entry.get("campaign_affinity"), str) and entry.get("campaign_affinity"):
        campaign = find_campaign(entry["campaign_affinity"])
        if campaign is not None:
            bounded_sources.extend(
                [
                    relative_display(ROOT / campaign["dossier_path"]),
                    relative_display(campaign_status_path(campaign)),
                ]
            )
    deduped_sources = [item for item in dict.fromkeys(str(x) for x in bounded_sources if x)]
    lines = [
        f"# Working Packet: {packet_title}",
        "",
        f"- slug: `{slug}`",
        f"- title: {entry.get('title', slug)}",
        f"- publication status: `{entry.get('publication_status', 'NONE')}`",
        f"- packet quality: `{entry.get('publication_packet_quality', 'unknown')}`",
        "",
        "## statement",
        str(entry.get("intended_statement") or entry.get("canonical_statement") or entry.get("question") or ""),
        "",
        "## novelty_notes",
        f"- frontier basis: {entry.get('publication_packet_frontier_basis', '(not recorded)')}",
        f"- why still open: {entry.get('why_still_appears_open', '(not recorded)')}",
        f"- attempted conflict check: {entry.get('attempted_conflict_check', '(not recorded)')}",
        f"- rediscovery risk: {entry.get('rediscovery_risk', '(not recorded)')}",
        "",
        "## proof_sketch",
        f"- attack style: {entry.get('attack_style', '(not recorded)')}",
        f"- likely route: {entry.get('publication_packet_near_paper_reason', '(not recorded)')}",
        f"- verifier focus: {entry.get('verifier_hint', '(not recorded)')}",
        "",
        "## likely_paper_shape",
        f"- note title: {packet_title}",
        f"- paper shape: {entry.get('paper_shape', '(not recorded)')}",
        f"- publication if solved: {entry.get('publication_if_solved', '(not recorded)')}",
        f"- minimal artifact requirements: {entry.get('publication_packet_artifact_requirements', '(not recorded)')}",
        "",
        "## bounded_source_list",
    ]
    lines.extend([f"- {item}" for item in deduped_sources])
    lines.append("")
    return "\n".join(lines)


def ensure_candidate_working_packet(entry: dict) -> pathlib.Path:
    path = candidate_working_packet_path(entry["slug"])
    text = build_candidate_working_packet(entry)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")
    return path


def entry_with_working_packet(entry: dict) -> dict:
    if entry.get("entry_type") != "paper_candidate" or not entry.get("slug"):
        return entry
    enriched = dict(entry)
    enriched["working_packet_path"] = relative_display(ensure_candidate_working_packet(entry))
    return enriched


def thin_failed_entry(item) -> dict:
    if isinstance(item, str):
        return {
            "slug": item,
            "reason": "ATTEMPTED",
            "title": item,
            "notes": "Legacy archived attempt preserved before thin search memory existed.",
            "checked_on": None,
            "publication_status": None,
        }
    if not isinstance(item, dict):
        return {
            "slug": str(item),
            "reason": "ATTEMPTED",
            "title": str(item),
            "notes": "Unstructured archived attempt.",
            "checked_on": None,
            "publication_status": None,
        }
    return {
        "slug": item.get("slug") or "(missing slug)",
        "reason": item.get("reason") or "ATTEMPTED",
        "title": item.get("title") or item.get("slug") or "(untitled)",
        "notes": compact_text(item.get("notes") or item.get("reason") or "Archived attempt."),
        "checked_on": item.get("checked_on"),
        "publication_status": item.get("publication_status"),
    }


def refresh_search_memory() -> None:
    failed = load_json(FAILED, [])
    normalized = [thin_failed_entry(item) for item in failed]
    summary = {
        "generated_on": now_iso(),
        "count": len(normalized),
        "recent_attempts": normalized[-40:],
    }
    write_stable_memory_json(SEARCH_MEMORY, summary)


def refresh_paper_memory(queue_entries: list[dict] | None = None) -> None:
    entries = queue_entries if queue_entries is not None else load_json(QUEUE, [])
    packets: list[dict] = []
    for entry in entries:
        if not isinstance(entry, dict) or entry.get("entry_type") != "paper_candidate":
            continue
        packet_path = ensure_candidate_working_packet(entry)
        packets.append(
            {
                "slug": entry.get("slug"),
                "title": entry.get("title"),
                "publication_status": entry.get("publication_status", "NONE"),
                "publication_packet_title": entry.get("publication_packet_title"),
                "publication_packet_quality": entry.get("publication_packet_quality"),
                "publication_if_solved": compact_text(entry.get("publication_if_solved"), 180),
                "why_this_could_be_publishable": compact_text(entry.get("why_this_could_be_publishable"), 180),
                "canonical_source": entry.get("canonical_source"),
                "working_packet_path": relative_display(packet_path),
            }
        )
    campaign_summaries: list[dict] = []
    for campaign in active_campaigns()[:3]:
        status = load_campaign_status(campaign)
        campaign_summaries.append(
            {
                "family_slug": campaign["family_slug"],
                "publication_status": status.get("publication_status", campaign.get("publication_status", "NONE")),
                "strongest_honest_claim": compact_text(status.get("strongest_honest_claim") or campaign.get("theorem_slice_hint"), 220),
                "next_blocker": compact_text(status.get("next_blocker") or status.get("next_action") or "", 180),
            }
        )
    exact_wins = [
        item
        for item in (thin_failed_entry(entry) for entry in load_json(FAILED, []))
        if item.get("reason") == "EXACT"
    ]
    summary = {
        "generated_on": now_iso(),
        "queued_publication_packets": packets,
        "near_paper_campaigns": campaign_summaries,
        "exact_wins": exact_wins[-20:],
    }
    write_stable_memory_json(PAPER_MEMORY, summary)


def refresh_context_hygiene_surfaces(queue_entries: list[dict] | None = None) -> None:
    entries = queue_entries if queue_entries is not None else load_json(QUEUE, [])
    for entry in entries:
        if isinstance(entry, dict) and entry.get("entry_type") == "paper_candidate" and entry.get("slug"):
            ensure_candidate_working_packet(entry)
    refresh_search_memory()
    refresh_paper_memory(entries)


def candidate_attempt_dir(slug: str) -> pathlib.Path:
    return ROOT / "artifacts" / slug / "attempts"


def candidate_attempt_paths(slug: str, worker_role: str) -> tuple[pathlib.Path, pathlib.Path]:
    attempt_dir = candidate_attempt_dir(slug)
    return attempt_dir / f"{worker_role}.md", attempt_dir / f"{worker_role}.json"


def candidate_handoff_path(slug: str, worker_role: str) -> pathlib.Path:
    return candidate_attempt_dir(slug) / f"{worker_role}.handoff.md"


def family_attempt_handoff_path(campaign: dict, attempt_kind: str) -> pathlib.Path:
    return campaign_attempt_dir(campaign) / f"{attempt_kind}.handoff.md"


def candidate_allowed_paths(entry: dict) -> list[pathlib.Path]:
    slug = entry["slug"]
    working_packet = ensure_candidate_working_packet(entry)
    paths: list[pathlib.Path] = [
        AGENTS_FILE,
        PAPER_MEMORY,
        SEARCH_MEMORY,
        working_packet,
        ROOT / "artifacts" / slug / "record.md",
        ROOT / "artifacts" / slug / "status.json",
    ]
    family_slug = entry.get("campaign_affinity")
    if isinstance(family_slug, str) and family_slug:
        campaign = find_campaign(family_slug)
        if campaign is not None:
            paths.extend(
                [
                    ROOT / campaign["dossier_path"],
                    campaign_record_path(campaign),
                    campaign_status_path(campaign),
                ]
            )
    return dedupe_paths(paths)[:6]


def family_attempt_allowed_paths(campaign: dict) -> list[pathlib.Path]:
    paths: list[pathlib.Path] = [
        AGENTS_FILE,
        PAPER_MEMORY,
        SEARCH_MEMORY,
        ROOT / campaign["dossier_path"],
        campaign_record_path(campaign),
        campaign_status_path(campaign),
    ]
    if PROOFS.exists():
        paths.append(PROOFS)
    for slug in campaign.get("seed_instances", [])[:1]:
        paths.extend(
            [
                ROOT / "artifacts" / slug / "record.md",
                ROOT / "artifacts" / slug / "status.json",
            ]
        )
    return dedupe_paths(paths)[:6]


def write_handoff_memo(
    path: pathlib.Path,
    *,
    worker_role: str,
    exact_statement: str,
    why_publishable: str,
    allowed_files: list[pathlib.Path],
    stop_condition: str,
    output_path: str,
) -> None:
    lines = [
        f"# {worker_role} handoff",
        "",
        f"- role: `{worker_role}`",
        f"- exact statement: {exact_statement}",
        f"- why publishable if solved: {why_publishable}",
        f"- stop condition: {stop_condition}",
        f"- output path: `{output_path}`",
        "- allowed files:",
    ]
    for allowed in allowed_files:
        lines.append(f"  - `{relative_display(allowed)}`")
    lines.extend(
        [
            "",
            f"- context budget: {SUBAGENT_CONTEXT_BUDGET}",
            "",
            "Do not broaden scope beyond these files unless the stated stop condition would otherwise be impossible to satisfy honestly.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def paper_candidate_gate(entry: dict) -> tuple[bool, str]:
    missing = missing_fields(entry, PAPER_CANDIDATE_REQUIRED_FIELDS)
    if missing:
        return False, f"missing required paper-candidate fields: {', '.join(missing)}"
    if normalized_flag(entry.get("pre_solve_gate")) is not True:
        reason = str(entry.get("pre_solve_gate_reason") or "").strip()
        return False, reason or "pre_solve_gate is not an explicit pass"
    if normalized_flag(entry.get("needs_feeder_ladder")) is True:
        return False, "paper candidate still requires a feeder ladder"
    if normalized_rank(entry.get("publication_if_solved_score"), PUBLICATION_IF_SOLVED_SCORE_RANK, 99) > PUBLICATION_IF_SOLVED_SCORE_RANK["paper_with_light_packaging"]:
        return False, "publication_if_solved_score says the result is still too far from a paper"
    if normalized_rank(entry.get("solve_to_publication_distance"), PAPER_DISTANCE_RANK, 99) > PAPER_DISTANCE_RANK["short-medium"]:
        return False, "solve_to_publication_distance is too long for the one-shot gate"
    if normalized_rank(entry.get("publication_packet_quality"), PACKET_QUALITY_RANK, 99) > PACKET_QUALITY_RANK["strong"]:
        return False, "publication packet is not yet sharp enough for one-shot solve budget"
    return True, "pass"


def usable_paper_candidates() -> list[dict]:
    failed = failed_slug_set()
    candidates: list[dict] = []
    for item in load_json(QUEUE, []):
        if not isinstance(item, dict):
            continue
        slug = item.get("slug")
        if not slug or slug in failed or item.get("entry_type") != "paper_candidate":
            continue
        gate_ok, _ = paper_candidate_gate(item)
        if gate_ok:
            candidates.append(item)
    return candidates


def normalize_queue_for_scheduler() -> list[dict]:
    queue = load_json(QUEUE, [])
    if not isinstance(queue, list):
        return []
    valid_papers: list[dict] = []
    invalid_papers: list[dict] = []
    others: list[dict] = []
    for item in queue:
        if not isinstance(item, dict):
            continue
        if item.get("entry_type") != "paper_candidate":
            others.append(item)
            continue
        gate_ok, _ = paper_candidate_gate(item)
        if gate_ok:
            valid_papers.append(item)
        else:
            invalid_papers.append(item)
    valid_papers.sort(key=paper_candidate_priority)
    normalized = valid_papers + invalid_papers + others
    if normalized != queue:
        write_json(QUEUE, normalized)
    refresh_context_hygiene_surfaces(normalized)
    if valid_papers:
        render_selected_problem(entry_with_working_packet(valid_papers[0]))
    return normalized


def campaign_is_near_closure(campaign: dict | str) -> tuple[bool, str]:
    if isinstance(campaign, str):
        campaign_record = find_campaign(campaign)
        if campaign_record is None:
            return False, f"campaign {campaign!r} is not present in campaigns/manifest.json"
        campaign = campaign_record
    status = load_campaign_status(campaign)
    if normalized_flag(status.get("near_closure")) is True:
        return True, "campaign explicitly marks itself near closure"
    publication_status = status.get("publication_status", campaign.get("publication_status", "NONE"))
    if publication_rank(publication_status) < publication_rank("SLICE_EXACT"):
        return False, f"campaign publication_status={publication_status} is still below SLICE_EXACT"
    blocker = str(status.get("next_blocker") or status.get("next_action") or "").strip()
    if not blocker:
        return True, "campaign is slice-exact and has no blocker text recorded"
    return True, "campaign is already slice-exact or better, so campaign mode is still justified"


def load_campaign_manifest() -> list[dict]:
    data = load_json(CAMPAIGN_MANIFEST, [])
    return data if isinstance(data, list) else []


def campaign_status_path(campaign: dict) -> pathlib.Path:
    return ROOT / campaign["artifact_dir"] / "status.json"


def campaign_record_path(campaign: dict) -> pathlib.Path:
    return ROOT / campaign["artifact_dir"] / "record.md"


def campaign_attempt_dir(campaign: dict) -> pathlib.Path:
    return ROOT / campaign["artifact_dir"] / "attempts"


def campaign_attempt_paths(campaign: dict, attempt_kind: str) -> tuple[pathlib.Path, pathlib.Path]:
    attempt_dir = campaign_attempt_dir(campaign)
    return attempt_dir / f"{attempt_kind}.md", attempt_dir / f"{attempt_kind}.json"


def load_campaign_status(campaign: dict) -> dict:
    path = campaign_status_path(campaign)
    ensure_publication_defaults(path)
    return load_json(path, {})


def affiliated_artifact_slugs(campaign: dict, limit: int = RECENT_AFFILIATED_ARTIFACT_LIMIT) -> list[str]:
    scored: list[tuple[float, str]] = []
    for status_path in ARTIFACTS.glob("*/status.json"):
        if status_path.parent.parent.name == "families":
            continue
        data = load_json(status_path, {})
        if data.get("family_affinity") != campaign["family_slug"]:
            continue
        if not (
            data.get("verify_verdict") == "VERIFIED"
            or data.get("classification") in {"EXACT", "COUNTEREXAMPLE", "REDISCOVERY"}
        ):
            continue
        record_path = status_path.parent / "record.md"
        mtime = status_path.stat().st_mtime
        if record_path.exists():
            mtime = max(mtime, record_path.stat().st_mtime)
        scored.append((mtime, status_path.parent.name))
    scored.sort(reverse=True)
    seen: set[str] = set()
    slugs: list[str] = []
    for _, slug in scored:
        if slug in seen:
            continue
        seen.add(slug)
        slugs.append(slug)
        if len(slugs) >= limit:
            break
    return slugs


def campaign_frontier_slugs(campaign: dict) -> list[str]:
    status = load_campaign_status(campaign)
    slugs: list[str] = []
    decisive = status.get("next_decisive_feeder")
    if isinstance(decisive, str) and decisive:
        slugs.append(decisive)
    for slug in status.get("next_feeder_instances", []):
        if isinstance(slug, str) and slug:
            slugs.append(slug)
    deduped: list[str] = []
    seen: set[str] = set()
    for slug in slugs:
        if slug in seen:
            continue
        seen.add(slug)
        deduped.append(slug)
    return deduped


def attempt_output_files(campaign: dict, exclude_attempt_kind: str | None = None) -> list[pathlib.Path]:
    attempt_dir = campaign_attempt_dir(campaign)
    if not attempt_dir.exists():
        return []
    excluded: set[pathlib.Path] = set()
    if exclude_attempt_kind:
        excluded.update(campaign_attempt_paths(campaign, exclude_attempt_kind))
    files: list[pathlib.Path] = []
    for candidate in sorted(attempt_dir.glob("*")):
        if candidate.is_file() and candidate not in excluded:
            files.append(candidate)
    return files


def campaign_input_paths(campaign: dict, include_attempts: bool = True, exclude_attempt_kind: str | None = None) -> list[pathlib.Path]:
    status = load_campaign_status(campaign)
    paths: list[pathlib.Path] = [
        CAMPAIGN_MANIFEST,
        PROOFS,
        FAILED,
        ROOT / campaign["dossier_path"],
        campaign_record_path(campaign),
        campaign_status_path(campaign),
    ]
    if include_attempts:
        if exclude_attempt_kind is None:
            paths.append(campaign_attempt_dir(campaign))
        else:
            paths.extend(attempt_output_files(campaign, exclude_attempt_kind))
    paths.extend(CAMPAIGN_LEAN_SURFACE_HINTS.get(campaign["family_slug"], []))
    feeder_slugs: list[str] = []
    decisive = status.get("next_decisive_feeder")
    if isinstance(decisive, str) and decisive:
        feeder_slugs.append(decisive)
    for slug in status.get("next_feeder_instances", []):
        if isinstance(slug, str) and slug:
            feeder_slugs.append(slug)
    for slug in campaign.get("seed_instances", []):
        if isinstance(slug, str) and slug:
            feeder_slugs.append(slug)
    feeder_slugs.extend(affiliated_artifact_slugs(campaign))
    seen: set[str] = set()
    for slug in feeder_slugs[: max(10, RECENT_AFFILIATED_ARTIFACT_LIMIT)]:
        if slug in seen:
            continue
        seen.add(slug)
        artifact_dir = ROOT / "artifacts" / slug
        paths.extend([artifact_dir / "record.md", artifact_dir / "status.json"])
    return paths


def campaign_input_signature(campaign: dict) -> str:
    return path_signature(campaign_input_paths(campaign))


def proof_attempt_input_signature(campaign: dict, attempt_kind: str) -> str:
    return path_signature(campaign_input_paths(campaign, include_attempts=True, exclude_attempt_kind=attempt_kind))


def should_run_campaign_generalize(campaign: dict, signature: str) -> tuple[bool, str]:
    status = load_campaign_status(campaign)
    runtime = runtime_campaign_state(campaign["family_slug"])
    if publication_rank(status.get("publication_status")) < publication_rank("SLICE_EXACT"):
        return True, "campaign is below SLICE_EXACT"
    if not status.get("strongest_honest_claim"):
        return True, "campaign has no preserved strongest_honest_claim yet"
    if runtime.get("last_generalize_signature") != signature:
        return True, "campaign inputs changed"
    return False, "campaign inputs are unchanged and the slice is already stable"


def should_run_publication_audit(campaign: dict, signature: str) -> tuple[bool, str]:
    status = load_campaign_status(campaign)
    runtime = runtime_campaign_state(campaign["family_slug"])
    if publication_rank(status.get("publication_status")) < publication_rank("SLICE_EXACT"):
        return True, "campaign is below SLICE_EXACT"
    if runtime.get("last_publication_audit_signature") != signature:
        return True, "campaign inputs changed since the last publication audit"
    last_audit = parse_status_timestamp(runtime.get("last_publication_audit_on"))
    if last_audit is None:
        return True, "no prior publication audit timestamp was preserved"
    elapsed = (dt.datetime.now().astimezone() - last_audit).total_seconds()
    if elapsed >= PUBLICATION_AUDIT_MIN_INTERVAL:
        return True, "the publication audit freshness window expired"
    return False, "the current slice is stable and the last publication audit is still fresh"


def should_run_campaign_lean(campaign: dict, signature: str) -> tuple[bool, str]:
    status = load_campaign_status(campaign)
    if status.get("lean_ready") is not True:
        return False, "Lean is not ready for this family campaign"
    runtime = runtime_campaign_state(campaign["family_slug"])
    if status.get("lean_complete") is not True:
        return True, "Lean is not complete yet"
    if runtime.get("last_lean_signature") != signature:
        return True, "family Lean inputs changed"
    return False, "family Lean inputs are unchanged and the slice is already checked"


def should_start_secondary_worker(campaign: dict) -> tuple[bool, str]:
    near_closure, closure_reason = campaign_is_near_closure(campaign)
    if not near_closure:
        return False, closure_reason
    runtime = runtime_campaign_state(campaign["family_slug"])
    backoff_until = parse_status_timestamp(runtime.get("secondary_worker_backoff_until"))
    now = dt.datetime.now().astimezone()
    if backoff_until is not None and now < backoff_until:
        return False, "secondary worker is still in backoff after an infrastructure failure"
    status = load_campaign_status(campaign)
    if publication_rank(status.get("publication_status")) < publication_rank("SLICE_EXACT"):
        return True, "secondary campaign is not yet slice-stable"
    signature = campaign_input_signature(campaign)
    if runtime.get("last_secondary_worker_signature") != signature:
        return True, "secondary campaign inputs changed"
    last_attempt = parse_status_timestamp(runtime.get("last_secondary_worker_attempt_on"))
    if last_attempt is None:
        return True, "secondary campaign has not run yet"
    elapsed = (now - last_attempt).total_seconds()
    if elapsed >= SECONDARY_WORKER_MIN_INTERVAL:
        return True, "secondary worker interval expired"
    return False, "secondary campaign inputs are unchanged and still within its throttle window"


def frontier_is_exhausted(campaign: dict) -> bool:
    frontier = campaign_frontier_slugs(campaign)
    if frontier and all(feeder_artifact_is_preserved(slug) for slug in frontier):
        return True
    return next_campaign_feeder_entry(campaign) is None


def should_run_frontier_refresh(campaign: dict, signature: str) -> tuple[bool, str]:
    if not frontier_is_exhausted(campaign):
        return False, "the campaign still has an unpreserved live feeder frontier"
    runtime = runtime_campaign_state(campaign["family_slug"])
    if runtime.get("last_frontier_refresh_signature") != signature:
        return True, "the frontier is exhausted and campaign inputs changed"
    last_refresh = parse_status_timestamp(runtime.get("last_frontier_refresh_on"))
    if last_refresh is None:
        return True, "the frontier is exhausted and no prior frontier refresh was preserved"
    elapsed = (dt.datetime.now().astimezone() - last_refresh).total_seconds()
    if elapsed >= FRONTIER_REFRESH_MIN_INTERVAL:
        return True, "the frontier is exhausted and the refresh window expired"
    return False, "the frontier is exhausted but no new family input has appeared since the last refresh"


def proof_attempt_specs(campaign: dict) -> list[dict]:
    status = load_campaign_status(campaign)
    configured = status.get("proof_attempt_portfolio")
    if isinstance(configured, list):
        specs: list[dict] = []
        for item in configured:
            if not isinstance(item, dict):
                continue
            kind = item.get("kind")
            if not isinstance(kind, str) or not kind.strip():
                continue
            specs.append(
                {
                    "kind": kind,
                    "title": item.get("title") or f"{kind.replace('_', ' ').title()} for {campaign['family_slug']}",
                    "question": item.get("question") or item.get("attempt_goal") or f"Advance the {campaign['family_slug']} family campaign on the current frontier.",
                    "attempt_goal": item.get("attempt_goal")
                    or "push the strongest current family claim forward without mutating the canonical family dossier directly",
                }
            )
        if specs:
            return specs
    theorem_target = status.get("theorem_slice_target") or campaign.get("theorem_slice_target")
    blocker = status.get("next_blocker") or status.get("next_action") or campaign.get("current_blocker")
    fallback = status.get("fallback_target") or campaign.get("fallback_target")
    specs = [
        {
            "kind": "direct_family_proof",
            "title": f"Direct proof attempt for {campaign['family_slug']}",
            "question": f"Try to close the current family theorem target directly: {theorem_target or blocker}",
            "attempt_goal": "prove the strongest currently plausible quantified family statement or theorem slice directly from the preserved campaign evidence",
        }
    ]
    if fallback:
        specs.append(
            {
                "kind": "obstruction_boundary",
                "title": f"Boundary/obstruction attempt for {campaign['family_slug']}",
                "question": f"If the direct family theorem is too strong, isolate the first sharp obstruction or boundary theorem: {fallback}",
                "attempt_goal": "find the first sharp obstruction theorem, boundary case, or overclaim boundary if the direct family proof does not close cleanly",
            }
        )
    return specs


def should_run_proof_attempt(campaign: dict, attempt_kind: str, signature: str) -> tuple[bool, str]:
    runtime = runtime_campaign_state(campaign["family_slug"])
    signature_key = f"attempt_{attempt_kind}_signature"
    time_key = f"attempt_{attempt_kind}_on"
    if runtime.get(signature_key) != signature:
        return True, "campaign inputs changed for this proof attempt"
    last_attempt = parse_status_timestamp(runtime.get(time_key))
    if last_attempt is None:
        return True, "this proof attempt has not run yet"
    elapsed = (dt.datetime.now().astimezone() - last_attempt).total_seconds()
    if elapsed >= PROOF_ATTEMPT_MIN_INTERVAL:
        return True, "this proof attempt exceeded its backoff window"
    return False, "this proof attempt already ran on the current inputs"


def mark_generalize_success(campaign: dict, signature: str, frontier_refresh: bool = False) -> None:
    timestamp = now_iso()
    updates = {
        "last_generalize_signature": signature,
        "last_generalize_on": timestamp,
    }
    if frontier_refresh:
        updates["last_frontier_refresh_signature"] = signature
        updates["last_frontier_refresh_on"] = timestamp
    update_runtime_campaign_state(campaign["family_slug"], **updates)


def proof_attempt_budget(campaign: dict, allow_parallel: bool, reserved_slots: int) -> int:
    if not allow_parallel or not git_worktree_supported():
        return 0
    if publication_stop_ready(campaign_status_path(campaign)):
        return 0
    status = load_campaign_status(campaign)
    if not (
        frontier_is_exhausted(campaign)
        or publication_rank(status.get("publication_status")) >= publication_rank("SLICE_EXACT")
    ):
        return 0
    max_parallel = int(os.environ.get("AUTOMATH_MAX_PARALLEL_WORKERS", "5"))
    available_slots = max(0, max_parallel - 1 - reserved_slots)
    return min(PARALLEL_PROOF_ATTEMPTS, available_slots)


def find_campaign(family_slug: str) -> dict | None:
    for campaign in load_campaign_manifest():
        if campaign.get("family_slug") == family_slug:
            return campaign
    return None


def active_campaigns() -> list[dict]:
    ranked = []
    for campaign in load_campaign_manifest():
        if not campaign.get("active", False):
            continue
        status = load_campaign_status(campaign)
        publication_status = status.get("publication_status", campaign.get("publication_status", "NONE"))
        if publication_status == "PAPER_READY":
            continue
        ranked.append((campaign.get("priority", 999), campaign, status))
    ranked.sort(key=lambda item: item[0])
    result = []
    for _, campaign, status in ranked:
        merged = dict(campaign)
        merged.update(
            {
                "campaign_priority": campaign.get("priority", 999),
                "publication_status": status.get("publication_status", campaign.get("publication_status", "NONE")),
                "strongest_honest_claim": status.get("strongest_honest_claim"),
                "next_action": status.get("next_action"),
            }
        )
        result.append(merged)
    return result


def worker_required_paths() -> list[pathlib.Path]:
    return [
        AGENTS_FILE,
        MEMORY_DIR,
        ROOT / "PROOFS.md",
        ROOT / "ledger.md",
        ROOT / "selected_problem.md",
        ROOT / "prompts",
        ROOT / "campaigns",
        ROOT / "scripts",
        ROOT / "run_publication_cycle.sh",
        ROOT / "run_feeder_cycle.sh",
        ROOT / "lean" / "AutoMath.lean",
        ROOT / "lean" / "AutoMath",
    ]


def artifact_status_path(slug: str) -> pathlib.Path:
    return ROOT / "artifacts" / slug / "status.json"


def feeder_artifact_is_preserved(slug: str) -> bool:
    path = artifact_status_path(slug)
    if not path.exists():
        return False
    data = load_json(path, {})
    verify_verdict = data.get("verify_verdict")
    classification = data.get("classification")
    if verify_verdict == "VERIFIED":
        return True
    if classification in {"EXACT", "REDISCOVERY"}:
        return True
    return False


def publication_rank(status: str | None) -> int:
    if status is None:
        return -1
    return PUBLICATION_STATUS_RANK.get(status, -1)


def status_or_manifest(campaign: dict, key: str, default=None):
    status = load_campaign_status(campaign)
    if key in status and status.get(key) not in (None, "", []):
        return status.get(key)
    return campaign.get(key, default)


def campaign_queue_entry(campaign: dict) -> dict:
    return {
        "entry_type": "family_campaign",
        "title": campaign["title"],
        "slug": f"family-{campaign['family_slug']}",
        "family_slug": campaign["family_slug"],
        "family_name": campaign["family_name"],
        "campaign_affinity": campaign["family_slug"],
        "canonical_source": campaign["dossier_path"],
        "open_status_checked_on": today_str(),
        "question": f"Advance the active publication campaign {campaign['family_slug']} from its current theorem-slice blocker.",
        "canonical_statement": status_or_manifest(campaign, "theorem_slice_target", campaign.get("theorem_slice_hint")),
        "intended_statement": status_or_manifest(campaign, "strongest_honest_claim", campaign.get("theorem_slice_hint")),
        "attack_style": "family campaign",
        "generalization_potential": "high",
        "proof_template_reuse_score": "high",
        "publishability_score": "high",
        "theorem_slice_hint": campaign.get("theorem_slice_hint"),
        "theorem_slice_target": status_or_manifest(campaign, "theorem_slice_target"),
        "fallback_target": status_or_manifest(campaign, "fallback_target"),
        "next_blocker": status_or_manifest(campaign, "next_blocker", status_or_manifest(campaign, "next_action")),
        "next_feeder_instances": status_or_manifest(campaign, "next_feeder_instances", []),
        "publication_red_flags": [],
        "why_reasoning_friendly": campaign.get("why_now"),
        "why_low_token": "The dossier, family record, and exact inventory already exist locally.",
        "verifier_hint": "Use publication audit to test whether the current claim is really theorem-shaped rather than another instance.",
        "lean_hint": "Prefer reusable family lemmas or theorem-slice reductions over another isolated exact formalization.",
        "rediscovery_risk": "low-medium",
        "why_still_appears_open": "The family artifact still records a live blocker rather than a closed publication-grade theorem.",
        "why_this_could_be_publishable": status_or_manifest(campaign, "paper_title_hint", campaign.get("theorem_slice_hint")),
        "curation_confidence": "high",
        "publication_status": status_or_manifest(campaign, "publication_status", "NONE"),
        "strongest_honest_claim": status_or_manifest(campaign, "strongest_honest_claim"),
        "next_action": status_or_manifest(campaign, "next_action"),
        "seed_instances": campaign.get("seed_instances", []),
        "dossier_path": campaign["dossier_path"],
        "artifact_dir": campaign["artifact_dir"],
    }


def feeder_queue_entry(campaign: dict, feeder: dict) -> dict:
    return {
        "entry_type": "feeder_instance",
        "title": feeder["title"],
        "slug": feeder["slug"],
        "question": feeder["question"],
        "family_name": campaign["family_name"],
        "named_conjecture": feeder.get("named_conjecture", campaign["family_name"]),
        "campaign_affinity": campaign["family_slug"],
        "canonical_source": campaign["dossier_path"],
        "open_status_checked_on": today_str(),
        "canonical_statement": feeder.get("canonical_statement", feeder["question"]),
        "intended_statement": feeder.get("intended_statement", feeder["question"]),
        "definitions": feeder.get("definitions", []),
        "attack_style": feeder.get("attack_style", "campaign feeder"),
        "generalization_potential": feeder.get("generalization_potential", "high"),
        "proof_template_reuse_score": feeder.get("proof_template_reuse_score", "high"),
        "publishability_score": feeder.get("publishability_score", "high"),
        "theorem_slice_hint": feeder.get("theorem_slice_hint", status_or_manifest(campaign, "theorem_slice_target")),
        "publication_red_flags": feeder.get("publication_red_flags", []),
        "why_reasoning_friendly": feeder.get(
            "why_reasoning_friendly",
            "This is the next smallest parameter shift against an active theorem slice rather than a random fresh family.",
        ),
        "why_low_token": feeder.get(
            "why_low_token",
            "The campaign dossier and existing exact/partial cluster already provide the notation, proof template, and likely checks.",
        ),
        "verifier_hint": feeder.get(
            "verifier_hint",
            "Audit the instance against the active campaign theorem slice, not just the standalone exact claim.",
        ),
        "lean_hint": feeder.get(
            "lean_hint",
            "Prefer Lean only if the feeder either closes exactly or materially strengthens a family theorem slice.",
        ),
        "rediscovery_risk": feeder.get("rediscovery_risk", "medium"),
        "why_still_appears_open": feeder.get("why_still_appears_open", "No exact result for this feeder is currently preserved in repo memory."),
        "why_this_could_be_publishable": feeder.get(
            "why_this_could_be_publishable",
            "This feeder directly tests an active theorem slice instead of adding another unrelated exact instance.",
        ),
        "attempted_conflict_check": feeder.get(
            "attempted_conflict_check",
            "Local campaign reseeding did not find this slug in failed, exact, or rediscovery memory.",
        ),
        "curation_confidence": feeder.get("curation_confidence", "medium-high"),
        "publication_status": feeder.get("publication_status", "NONE"),
    }


def synthetic_feeder_entry(campaign: dict, slug: str) -> dict | None:
    zero_divisor = re.fullmatch(r"z(\d+)-z(\d+)(?:-z(\d+))?-prime-zero-divisor-graph", slug)
    if campaign["family_slug"] == "zero_divisor_prime_labelings" and zero_divisor:
        factors = [f"Z_{zero_divisor.group(1)}", f"Z_{zero_divisor.group(2)}"]
        if zero_divisor.group(3):
            factors.append(f"Z_{zero_divisor.group(3)}")
        ring = " x ".join(factors)
        feeder = {
            "slug": slug,
            "title": f"Is the zero-divisor graph Gamma({ring}) prime?",
            "question": f"Does the zero-divisor graph Gamma({ring}) admit a prime labeling?",
            "canonical_statement": f"Determine whether Gamma({ring}) is prime.",
            "intended_statement": (
                f"Use Gamma({ring}) as the next campaign-directed feeder on the live "
                f"{campaign['family_name']} line."
            ),
            "named_conjecture": campaign["family_name"],
            "attack_style": "campaign feeder synthesized from the active family status",
            "theorem_slice_hint": status_or_manifest(campaign, "theorem_slice_target"),
            "why_still_appears_open": "This feeder was promoted by the active family status, but no preserved queue entry exists yet.",
            "why_this_could_be_publishable": "It is the current discriminator named by the live family campaign rather than a broad exploratory one-off.",
        }
        return feeder_queue_entry(campaign, feeder)

    cnbc = re.fullmatch(r"c(\d+)-(\d+)-(\d+)-(\d+)-cnbc", slug)
    if campaign["family_slug"] == "cnbc_quintic_nonexistence" and cnbc:
        n, a, b, c = cnbc.groups()
        feeder = {
            "slug": slug,
            "title": f"Is the quintic circulant C_{n}({a},{b},{c}) a CNBC graph?",
            "question": f"Does the quintic circulant C_{n}({a},{b},{c}) admit a closed-neighborhood balanced coloring?",
            "canonical_statement": f"Determine whether C_{n}({a},{b},{c}) is CNBC.",
            "intended_statement": (
                f"Use C_{n}({a},{b},{c}) as the next family-directed discriminator for "
                f"{campaign['family_name']}."
            ),
            "named_conjecture": campaign["family_name"],
            "attack_style": "campaign feeder synthesized from the active family status",
            "theorem_slice_hint": status_or_manifest(campaign, "theorem_slice_target"),
            "why_still_appears_open": "This feeder was promoted by the active family status, but no preserved queue entry exists yet.",
            "why_this_could_be_publishable": "It is the current discriminator named by the live family campaign rather than a broad exploratory one-off.",
        }
        return feeder_queue_entry(campaign, feeder)

    return None


def find_feeder_entry_by_slug(slug: str, campaign: dict | None = None) -> dict | None:
    queued = find_queue_entry_by_slug(slug)
    if queued is not None:
        return queued
    search_campaigns = [campaign] if campaign is not None else load_campaign_manifest()
    for candidate_campaign in search_campaigns:
        for feeder in candidate_campaign.get("recommended_feeders", []):
            if isinstance(feeder, dict) and feeder.get("slug") == slug:
                return feeder_queue_entry(candidate_campaign, feeder)
        synthesized = synthetic_feeder_entry(candidate_campaign, slug)
        if synthesized is not None:
            return synthesized
    if campaign is None:
        for candidate_campaign in load_campaign_manifest():
            status = load_campaign_status(candidate_campaign)
            slugs = []
            decisive = status.get("next_decisive_feeder")
            if decisive:
                slugs.append(decisive)
            slugs.extend(status.get("next_feeder_instances", []))
            if slug in slugs:
                synthesized = synthetic_feeder_entry(candidate_campaign, slug)
                if synthesized is not None:
                    return synthesized
    return None


def add_queue_entry(entries: list[dict], seen: set[str], failed: set[str], entry: dict | None) -> bool:
    if not entry:
        return False
    slug = entry.get("slug")
    if not slug or slug in seen or slug in failed:
        return False
    if entry.get("entry_type") == "feeder_instance" and feeder_artifact_is_preserved(slug):
        return False
    entries.append(entry)
    seen.add(slug)
    return True


def seed_campaign_queue() -> bool:
    campaigns = active_campaigns()[:2]
    if not campaigns:
        return False
    failed = failed_slug_set()
    entries: list[dict] = []
    seen: set[str] = set()
    primary = campaigns[0]
    secondary = campaigns[1] if len(campaigns) > 1 else None
    primary_feeders = next_campaign_feeder_entries(primary, 4)
    secondary_feeders = next_campaign_feeder_entries(secondary, 2) if secondary else []

    add_queue_entry(entries, seen, failed, campaign_queue_entry(primary))
    while len(entries) < 3 and primary_feeders:
        add_queue_entry(entries, seen, failed, primary_feeders.pop(0))

    if secondary is not None:
        add_queue_entry(entries, seen, failed, campaign_queue_entry(secondary))
        while len(entries) < 5 and secondary_feeders:
            add_queue_entry(entries, seen, failed, secondary_feeders.pop(0))
            break

    while len(entries) < 5 and primary_feeders:
        add_queue_entry(entries, seen, failed, primary_feeders.pop(0))

    while len(entries) < 5 and secondary_feeders:
        add_queue_entry(entries, seen, failed, secondary_feeders.pop(0))

    if len(entries) != 5:
        return False
    write_json(QUEUE, entries)
    refresh_context_hygiene_surfaces(entries)
    render_selected_problem(entry_with_working_packet(entries[0]))
    append_ledger("Queue was empty or exhausted, so it was locally reseeded from active publication campaigns before any broad web curation.")
    return True


def paper_candidate_priority(entry: dict) -> tuple[int, int, int, int, int, int, int, str]:
    publication_if_solved = normalized_rank(entry.get("publication_if_solved_score"), PUBLICATION_IF_SOLVED_SCORE_RANK, 99)
    distance = normalized_rank(entry.get("solve_to_publication_distance"), PAPER_DISTANCE_RANK, 5)
    packet_quality = normalized_rank(entry.get("publication_packet_quality"), PACKET_QUALITY_RANK, 99)
    plausibility = normalized_rank(entry.get("single_pass_proof_plausibility"), PLAUDIBILITY_RANK, 5)
    novelty_cost = normalized_rank(entry.get("novelty_check_cost"), COST_RANK, 99)
    packaging = normalized_rank(entry.get("packaging_risk"), COST_RANK, 99)
    feeder_penalty = 1 if normalized_flag(entry.get("needs_feeder_ladder")) is True else 0
    return (distance, publication_if_solved, packet_quality, plausibility, novelty_cost, packaging, feeder_penalty, entry.get("slug", ""))


def select_paper_candidate_entry() -> dict | None:
    candidates = usable_paper_candidates()
    if not candidates:
        return None
    candidates.sort(key=paper_candidate_priority)
    return candidates[0]


def render_campaign_selection(campaign: dict) -> pathlib.Path:
    status = load_campaign_status(campaign)
    entry = {
        "title": campaign["title"],
        "entry_type": "family_campaign",
        "slug": f"family-{campaign['family_slug']}",
        "family_slug": campaign["family_slug"],
        "family_name": campaign["family_name"],
        "campaign_priority": campaign.get("priority", 999),
        "dossier_path": campaign["dossier_path"],
        "artifact_dir": campaign["artifact_dir"],
        "publication_status": status.get("publication_status", campaign.get("publication_status", "NONE")),
        "family_statement": f"Work from the active campaign dossier at `{campaign['dossier_path']}` and the family artifact path `{campaign['artifact_dir']}`.",
        "theorem_slice_hint": campaign.get("theorem_slice_hint"),
        "theorem_slice_target": status.get("theorem_slice_target", campaign.get("theorem_slice_target")),
        "fallback_target": status.get("fallback_target", campaign.get("fallback_target")),
        "next_blocker": status.get("next_blocker", campaign.get("current_blocker")),
        "next_feeder_instances": status.get(
            "next_feeder_instances",
            [item.get("slug") for item in campaign.get("recommended_feeders", []) if item.get("slug")],
        ),
        "why_now": campaign.get("why_now"),
        "seed_instances": campaign.get("seed_instances", []),
        "strongest_honest_claim": status.get("strongest_honest_claim"),
        "next_action": status.get("next_action"),
    }
    render_selected_problem(entry)
    return ROOT / campaign["artifact_dir"] / "status.json"


def render_candidate_attempt_selection(entry: dict, worker_role: str) -> pathlib.Path:
    entry = entry_with_working_packet(entry)
    output_markdown, output_json = candidate_attempt_paths(entry["slug"], worker_role)
    handoff_path = candidate_handoff_path(entry["slug"], worker_role)
    allowed_paths = candidate_allowed_paths(entry)
    stop_condition = (
        "Write only the sidecar attempt outputs and stop once you have a decisive solve/verify result "
        "or a clear blocker that does not shorten solve-to-publication distance."
    )
    write_handoff_memo(
        handoff_path,
        worker_role=worker_role,
        exact_statement=str(entry.get("intended_statement") or entry.get("canonical_statement") or entry.get("question") or entry.get("title")),
        why_publishable=str(entry.get("publication_if_solved") or entry.get("why_this_could_be_publishable") or "A strong solve would already be near-publication."),
        allowed_files=allowed_paths,
        stop_condition=stop_condition,
        output_path=f"{relative_display(output_markdown)}, {relative_display(output_json)}",
    )
    attempt_entry = dict(entry)
    attempt_entry.update(
        {
            "worker_role": worker_role,
            "attempt_kind": worker_role,
            "attempt_output_markdown": str(output_markdown.relative_to(ROOT)),
            "attempt_output_json": str(output_json.relative_to(ROOT)),
            "handoff_memo_path": str(handoff_path.relative_to(ROOT)),
            "write_scope": "attempt_sidecar_only",
            "stop_condition": stop_condition,
            "context_budget": SUBAGENT_CONTEXT_BUDGET,
            "allowed_files": [relative_display(path) for path in allowed_paths],
        }
    )
    render_selected_problem(attempt_entry)
    return output_json


def render_family_attempt_selection(campaign: dict, attempt: dict) -> None:
    status = load_campaign_status(campaign)
    output_markdown, output_json = campaign_attempt_paths(campaign, attempt["kind"])
    worker_role = FAMILY_ATTEMPT_ROLES.get(attempt["kind"], "solver-A")
    handoff_path = family_attempt_handoff_path(campaign, attempt["kind"])
    allowed_paths = family_attempt_allowed_paths(campaign)
    stop_condition = (
        "Write only the sidecar proof-attempt outputs and stop once you either sharpen the family theorem slice "
        "or identify a blocker that does not shorten solve-to-publication distance."
    )
    write_handoff_memo(
        handoff_path,
        worker_role=worker_role,
        exact_statement=str(status.get("theorem_slice_target", campaign.get("theorem_slice_target")) or campaign.get("theorem_slice_hint") or campaign["title"]),
        why_publishable=str(status.get("strongest_honest_claim") or campaign.get("theorem_slice_hint") or campaign["title"]),
        allowed_files=allowed_paths,
        stop_condition=stop_condition,
        output_path=f"{relative_display(output_markdown)}, {relative_display(output_json)}",
    )
    entry = {
        "title": attempt["title"],
        "entry_type": "family_campaign",
        "slug": f"family-{campaign['family_slug']}-{attempt['kind']}",
        "worker_role": worker_role,
        "family_slug": campaign["family_slug"],
        "family_name": campaign["family_name"],
        "campaign_priority": campaign.get("priority", 999),
        "dossier_path": campaign["dossier_path"],
        "artifact_dir": campaign["artifact_dir"],
        "attempt_kind": attempt["kind"],
        "publication_status": status.get("publication_status", campaign.get("publication_status", "NONE")),
        "question": attempt["question"],
        "attempt_goal": attempt["attempt_goal"],
        "theorem_slice_target": status.get("theorem_slice_target", campaign.get("theorem_slice_target")),
        "fallback_target": status.get("fallback_target", campaign.get("fallback_target")),
        "next_blocker": status.get("next_blocker", campaign.get("current_blocker")),
        "next_feeder_instances": status.get("next_feeder_instances", []),
        "seed_instances": campaign.get("seed_instances", []),
        "strongest_honest_claim": status.get("strongest_honest_claim"),
        "attempt_output_markdown": str(output_markdown.relative_to(ROOT)),
        "attempt_output_json": str(output_json.relative_to(ROOT)),
        "handoff_memo_path": str(handoff_path.relative_to(ROOT)),
        "write_scope": "attempt_sidecar_only",
        "stop_condition": stop_condition,
        "context_budget": SUBAGENT_CONTEXT_BUDGET,
        "allowed_files": [relative_display(path) for path in allowed_paths],
        "next_action": status.get("next_action"),
    }
    render_selected_problem(entry)


def find_proof_attempt(campaign: dict, attempt_kind: str) -> dict | None:
    for attempt in proof_attempt_specs(campaign):
        if attempt.get("kind") == attempt_kind:
            return attempt
    return None


def run_family_proof_attempt(campaign: dict, attempt_kind: str) -> int:
    attempt = find_proof_attempt(campaign, attempt_kind)
    if attempt is None:
        append_ledger(
            f"Requested proof attempt {attempt_kind} for family campaign {campaign['family_slug']} was not recognized, so the attempt ended cleanly."
        )
        return 0
    render_family_attempt_selection(campaign, attempt)
    signature = proof_attempt_input_signature(campaign, attempt_kind)
    update_runtime_campaign_state(
        campaign["family_slug"],
        **{
            f"attempt_{attempt_kind}_signature": signature,
            f"attempt_{attempt_kind}_on": now_iso(),
        },
    )
    rc = run_stage(
        ROOT,
        f"generalize_attempt_{campaign['family_slug']}_{attempt_kind}",
        PROMPTS / "generalize_family.prompt.md",
        "off",
        PROOF_ATTEMPT_TIMEOUT,
        preferred_effort("xhigh"),
        "tuned_openai",
    )
    if rc == 124:
        append_ledger(
            f"Family proof attempt {attempt_kind} for {campaign['family_slug']} hit its time budget and was left as a sidecar attempt artifact."
        )
    elif rc != 0:
        append_ledger(
            f"Family proof attempt {attempt_kind} for {campaign['family_slug']} exited unexpectedly and was left out of the canonical dossier."
        )
    return rc


def select_queue_entry(prefer_feeders: bool = False) -> dict | None:
    failed = failed_slug_set()
    queue = load_json(QUEUE, [])
    if prefer_feeders:
        for item in queue:
            if (
                isinstance(item, dict)
                and item.get("slug")
                and item["slug"] not in failed
                and item.get("entry_type") == "feeder_instance"
                and not feeder_artifact_is_preserved(item["slug"])
            ):
                return item
    for item in queue:
        if (
            isinstance(item, dict)
            and item.get("slug")
            and item["slug"] not in failed
            and not (item.get("entry_type") == "feeder_instance" and feeder_artifact_is_preserved(item["slug"]))
        ):
            return item
    return None


def rotate_problem_to_end(slug: str) -> None:
    queue = load_json(QUEUE, [])
    picked = None
    rest = []
    for item in queue:
        if picked is None and isinstance(item, dict) and item.get("slug") == slug:
            picked = item
        else:
            rest.append(item)
    if picked is not None:
        rest.append(picked)
    write_json(QUEUE, rest)
    refresh_context_hygiene_surfaces(rest)
    sync_selected_problem_to_queue(rest)


def remove_problem_from_queue(slug: str) -> None:
    queue = load_json(QUEUE, [])
    updated = [item for item in queue if not (isinstance(item, dict) and item.get("slug") == slug)]
    write_json(QUEUE, updated)
    refresh_context_hygiene_surfaces(updated)
    sync_selected_problem_to_queue(updated)


def mark_failed_problem(entry: dict, reason: str, publication_status: str | None = None) -> None:
    slug = entry["slug"]
    append_ledger(f"{slug} failed and was moved aside: {reason}")
    failed = load_json(FAILED, [])
    if slug not in {slug_of(item) for item in failed}:
        failed.append(
            {
                "slug": slug,
                "reason": reason,
                "title": entry.get("title"),
                "publication_status": publication_status or entry.get("publication_status", "NONE"),
                "checked_on": today_str(),
            }
        )
    write_json(FAILED, failed)
    refresh_search_memory()
    remove_problem_from_queue(slug)


def mark_rediscovery(entry: dict, notes: str) -> None:
    slug = entry["slug"]
    append_ledger(f"{slug} was reclassified as REDISCOVERY after the prior-art audit and was moved aside.")
    failed = load_json(FAILED, [])
    if slug not in {slug_of(item) for item in failed}:
        failed.append(
            {
                "slug": slug,
                "reason": "REDISCOVERY",
                "title": entry.get("title"),
                "notes": notes,
                "publication_status": "REDISCOVERY",
                "checked_on": today_str(),
            }
        )
    write_json(FAILED, failed)
    refresh_search_memory()
    remove_problem_from_queue(slug)


def archive_exact_instance(entry: dict, notes: str, publication_status: str = "INSTANCE_ONLY") -> None:
    slug = entry["slug"]
    failed = load_json(FAILED, [])
    if slug not in {slug_of(item) for item in failed}:
        failed.append(
            {
                "slug": slug,
                "reason": "EXACT",
                "title": entry.get("title"),
                "notes": notes,
                "publication_status": publication_status,
                "checked_on": today_str(),
            }
        )
    write_json(FAILED, failed)
    refresh_search_memory()
    remove_problem_from_queue(slug)


def archive_attempted_problem(entry: dict, reason: str, notes: str, publication_status: str | None = None) -> None:
    slug = entry["slug"]
    failed = load_json(FAILED, [])
    if slug not in {slug_of(item) for item in failed}:
        failed.append(
            {
                "slug": slug,
                "reason": reason,
                "title": entry.get("title"),
                "notes": notes,
                "publication_status": publication_status or entry.get("publication_status", "NONE"),
                "checked_on": today_str(),
            }
        )
    write_json(FAILED, failed)
    refresh_search_memory()
    remove_problem_from_queue(slug)


def transport_env(profile: str) -> tuple[dict, tempfile.TemporaryDirectory | None]:
    env = os.environ.copy()
    temp_home = None
    if profile != "tuned_openai":
        return env, temp_home
    auth_source = pathlib.Path.home() / ".codex" / "auth.json"
    if not auth_source.exists():
        return env, temp_home
    temp_home = tempfile.TemporaryDirectory()
    temp_home_path = pathlib.Path(temp_home.name)
    codex_home = temp_home_path / ".codex"
    codex_home.mkdir(parents=True, exist_ok=True)
    shutil.copy2(auth_source, codex_home / "auth.json")
    (codex_home / "config.toml").write_text(
        "\n".join(
            [
                'model = "gpt-5.4"',
                'model_provider = "openai-tuned"',
                'approval_policy = "never"',
                'sandbox_mode = "workspace-write"',
                'preferred_auth_method = "chatgpt"',
                'chatgpt_base_url = "https://chatgpt.com/backend-api/"',
                '[model_providers.openai-tuned]',
                'name = "OpenAI Tuned"',
                'base_url = "https://chatgpt.com/backend-api/codex"',
                'wire_api = "responses"',
                'requires_openai_auth = true',
                'stream_idle_timeout_ms = 900000',
                'stream_max_retries = 20',
                "",
            ]
        ),
        encoding="utf-8",
    )
    env["HOME"] = str(temp_home_path)
    return env, temp_home


def run_stage(root: pathlib.Path, stage_name: str, prompt_file: pathlib.Path, search_mode: str, timeout_secs: int,
              reasoning_effort: str | None = None, transport_profile: str = "default") -> int:
    stamp = dt.datetime.now().strftime("%Y%m%dT%H%M%S")
    stdout_log = LOGS / f"{stamp}_{stage_name}.stdout.log"
    last_message = LOGS / f"{stamp}_{stage_name}.last.txt"
    preface = (
        "Work only inside this repository. Do not use skills, MCP, cloud tasks, "
        "or JSON output schemas. Follow the prompt below exactly. "
        "If selected_problem.md specifies a handoff memo path, read that memo immediately after selected_problem.md "
        "and treat its allowed files, stop condition, output path, and context budget as the binding scope for this run."
    )
    if stage_name == "curate":
        preface += (
            " Respect the curation search and time budget. Do not narrate progress. "
            "Stop browsing once you have enough material and write queue.json and "
            "selected_problem.md before any closing message."
        )
    elif stage_name.startswith("generalize_"):
        preface += (
            " Stay bounded. Read the campaign dossier, the current family record/status, "
            "PROOFS.md when relevant, and only the most relevant seed artifacts named there "
            "(target 6 or fewer, hard cap 10 unless a final discriminator is necessary). "
            "Use local search only to jump to exact sections. Write the family record and "
            "status files before any closing message."
        )
    elif stage_name.startswith("verify") or stage_name == "publication_audit":
        preface += (
            " Use live web only inside the bounded prior-art or publication-status pass, "
            "then return to skeptical checking. Keep the audit bounded and update the status "
            "file before any closing message."
        )
    elif stage_name.startswith("lean_family_"):
        preface += (
            " Stay bounded to the active family dossier, family record/status, and current family Lean modules. "
            "Do not roam solved exact-instance artifact directories unless the family record explicitly names one as a necessary dependency. "
            "Prefer one reusable family lemma or one theorem-slice skeleton, update the family status file, and stop once the current Lean target is honestly checked."
        )

    prompt_text = preface + "\n\n" + prompt_file.read_text(encoding="utf-8")
    cmd = ["codex"]
    if search_mode == "on":
        cmd.append("--search")
    cmd.extend(
        [
            "exec",
            "--ephemeral",
            "-C",
            str(root),
            "-m",
            "gpt-5.4",
            "-s",
            "workspace-write",
            "-c",
            'approval_policy="never"',
            "--color",
            "never",
            "-o",
            str(last_message),
            "-",
        ]
    )
    if reasoning_effort:
        cmd.extend(["-c", f'model_reasoning_effort="{reasoning_effort}"'])

    env, temp_home = transport_env(transport_profile)

    timed_out = False
    returncode = 0

    with stdout_log.open("w", encoding="utf-8") as out:
        proc = subprocess.Popen(
            cmd,
            cwd=root,
            stdin=subprocess.PIPE,
            stdout=out,
            stderr=subprocess.STDOUT,
            text=True,
            env=env,
            start_new_session=True,
        )
        assert proc.stdin is not None
        proc.stdin.write(prompt_text)
        proc.stdin.close()

        deadline = time.monotonic() + timeout_secs
        while True:
            returncode = proc.poll()
            if returncode is not None:
                break
            if time.monotonic() >= deadline:
                timed_out = True
                kill_process_group(proc, signal.SIGKILL)
                proc.wait()
                out.write(f"\n[run_stage timeout after {timeout_secs} seconds]\n")
                returncode = 124
                break
            time.sleep(2)

    if temp_home is not None:
        temp_home.cleanup()
    return returncode if not timed_out else 124


def supports_xhigh() -> bool:
    cached = load_json(CAPABILITIES_CACHE, {})
    if isinstance(cached, dict) and cached.get("xhigh") is True:
        return True
    probe_cmd = [
        "codex",
        "exec",
        "-m",
        "gpt-5.4",
        "-s",
        "workspace-write",
        "-c",
        'approval_policy="never"',
        "-c",
        'model_reasoning_effort="xhigh"',
        "--color",
        "never",
        "-",
    ]
    try:
        result = subprocess.run(
            probe_cmd,
            cwd=ROOT,
            input="Reply with exactly: xhigh_ok\n",
            text=True,
            capture_output=True,
            timeout=120,
            check=False,
        )
        ok = result.returncode == 0 and "xhigh_ok" in result.stdout
    except Exception:
        ok = False
    write_json(CAPABILITIES_CACHE, {"xhigh": ok, "checked_on": today_str()})
    return ok


def preferred_effort(level: str) -> str:
    if level == "xhigh":
        return "xhigh" if supports_xhigh() else "high"
    return level


def render_queue_selection(entry: dict, worker_role: str | None = None, sidecar: bool = False) -> pathlib.Path:
    if sidecar and worker_role:
        return render_candidate_attempt_selection(entry, worker_role)
    entry = entry_with_working_packet(entry)
    render_selected_problem(entry)
    status_path = ROOT / "artifacts" / entry["slug"] / "status.json"
    ensure_publication_defaults(status_path)
    return status_path


def find_queue_entry_by_slug(slug: str) -> dict | None:
    for item in load_json(QUEUE, []):
        if isinstance(item, dict) and item.get("slug") == slug:
            return item
    return None


def next_campaign_feeder_entry(campaign: dict, excluded_slugs: set[str] | None = None) -> dict | None:
    status = load_campaign_status(campaign)
    failed = failed_slug_set()
    excluded = excluded_slugs or set()
    candidates: list[str] = []
    decisive = status.get("next_decisive_feeder")
    if decisive:
        candidates.append(decisive)
    candidates.extend(status.get("next_feeder_instances", []))
    candidates.extend(
        feeder.get("slug")
        for feeder in campaign.get("recommended_feeders", [])
        if isinstance(feeder, dict) and feeder.get("slug")
    )
    seen: set[str] = set()
    for slug in candidates:
        if not slug or slug in seen or slug in failed or slug in excluded or feeder_artifact_is_preserved(slug):
            continue
        seen.add(slug)
        entry = find_feeder_entry_by_slug(slug, campaign)
        if entry is not None:
            return entry
    return None


def next_campaign_feeder_entries(campaign: dict, limit: int) -> list[dict]:
    status = load_campaign_status(campaign)
    failed = failed_slug_set()
    candidates: list[str] = []
    decisive = status.get("next_decisive_feeder")
    if decisive:
        candidates.append(decisive)
    candidates.extend(status.get("next_feeder_instances", []))
    candidates.extend(
        feeder.get("slug")
        for feeder in campaign.get("recommended_feeders", [])
        if isinstance(feeder, dict) and feeder.get("slug")
    )
    entries: list[dict] = []
    seen: set[str] = set()
    for slug in candidates:
        if not slug or slug in seen or slug in failed or feeder_artifact_is_preserved(slug):
            continue
        seen.add(slug)
        entry = find_feeder_entry_by_slug(slug, campaign)
        if entry is not None:
            entries.append(entry)
        if len(entries) >= limit:
            break
    return entries


def run_curation_if_needed(required_entry_type: str | None = None) -> bool:
    if queue_has_usable(required_entry_type=required_entry_type):
        normalize_queue_for_scheduler()
        return True
    if required_entry_type == "paper_candidate":
        append_ledger("Queue had no usable `paper_candidate`, so one-shot publication curation started.")
    else:
        append_ledger("Queue was empty or exhausted, so one-shot publication curation started.")
    rc = run_stage(ROOT, "curate", PROMPTS / "curate_batch.prompt.md", "on", CURATION_TIMEOUT, preferred_effort("high"), "default")
    if wait_for_usable_queue(required_entry_type=required_entry_type):
        normalize_queue_for_scheduler()
        if rc == 124:
            if required_entry_type == "paper_candidate":
                append_ledger("Curation hit its time budget but still produced a usable `paper_candidate` queue.")
            else:
                append_ledger("Curation hit its time budget but still produced a usable queue.")
        elif rc != 0:
            if required_entry_type == "paper_candidate":
                append_ledger("Curation ended oddly but still produced a usable `paper_candidate` queue.")
            else:
                append_ledger("Curation ended oddly but still produced a usable queue.")
        return True
    if rc == 124:
        if required_entry_type == "paper_candidate":
            append_ledger("Curation timed out before producing a usable `paper_candidate` queue, so this cycle ended cleanly.")
        else:
            append_ledger("Curation timed out before producing a usable queue, so this cycle ended cleanly.")
    elif rc != 0:
        if required_entry_type == "paper_candidate":
            append_ledger("Curation had an infrastructure failure before producing a usable `paper_candidate` queue, so this cycle ended cleanly.")
        else:
            append_ledger("Curation had an infrastructure failure before producing a usable queue, so this cycle ended cleanly.")
    else:
        if required_entry_type == "paper_candidate":
            append_ledger("Curation finished without producing a usable `paper_candidate` queue, so this cycle ended cleanly.")
        else:
            append_ledger("Curation finished without producing a usable queue, so this cycle ended cleanly.")
    return False


def git_worktree_supported() -> bool:
    try:
        inside = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        return inside.returncode == 0 and inside.stdout.strip() == "true"
    except Exception:
        return False


def strongest_publication_status(campaigns: list[dict]) -> str:
    strongest = "NONE"
    for campaign in campaigns:
        status = load_campaign_status(campaign).get("publication_status", campaign.get("publication_status", "NONE"))
        if publication_rank(status) > publication_rank(strongest):
            strongest = status
    return strongest


def write_publication_summary(active_campaign_slug: str | None, worker_status: str) -> None:
    refresh_context_hygiene_surfaces()
    campaigns = active_campaigns()
    primary = find_campaign(active_campaign_slug) if active_campaign_slug else None
    if primary is None and campaigns:
        primary = campaigns[0]
    paper_candidate = select_paper_candidate_entry()
    strongest_status = strongest_publication_status(campaigns) if campaigns else "NONE"
    strongest_claim = status_or_manifest(primary, "strongest_honest_claim") if primary else "(none)"
    theorem_target = status_or_manifest(primary, "theorem_slice_target") if primary else "(none)"
    next_blocker = status_or_manifest(primary, "next_blocker", status_or_manifest(primary, "next_action")) if primary else "(none)"
    next_feeders = status_or_manifest(primary, "next_feeder_instances", []) if primary else []
    next_decisive_feeder = next_feeders[0] if next_feeders else "(none listed)"
    candidate_slug = paper_candidate["slug"] if paper_candidate else "(none queued)"
    candidate_title = paper_candidate["title"] if paper_candidate else "(none queued)"
    candidate_publication_if_solved = paper_candidate.get("publication_if_solved", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_publication_score = paper_candidate.get("publication_if_solved_score", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_pre_solve_gate = paper_candidate.get("pre_solve_gate", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_packet_quality = paper_candidate.get("publication_packet_quality", "(not recorded)") if paper_candidate else "(none queued)"
    lean_family_complete = any(
        bool(load_campaign_status(campaign).get("lean_complete"))
        or bool(load_campaign_status(campaign).get("lean_family_lemma_complete"))
        for campaign in campaigns
    )
    status_paths = [str(campaign_status_path(campaign).relative_to(ROOT)) for campaign in campaigns[:3]]
    summary_lines = [
        "# AutoMath Publication Summary",
        "",
        f"- Updated: `{now_str()}`",
        f"- Queued one-shot paper candidate: {candidate_slug}",
        f"- Candidate title: {candidate_title}",
        f"- Candidate publication if solved: {candidate_publication_if_solved}",
        f"- Candidate publication score: {candidate_publication_score}",
        f"- Candidate packet quality: {candidate_packet_quality}",
        f"- Candidate pre-solve gate: {candidate_pre_solve_gate}",
        f"- Active campaigns: {', '.join(c['family_slug'] for c in campaigns) if campaigns else '(none)'}",
        f"- Strongest current publication status: `{strongest_status}`",
        f"- Strongest honest claim: {strongest_claim}",
        f"- Active theorem-slice target: {theorem_target}",
        f"- Next blocker: {next_blocker}",
        f"- Next decisive feeder instance: {next_decisive_feeder}",
        f"- Next feeder instances: {', '.join(next_feeders) if next_feeders else '(none listed)'}",
        f"- Any Lean family lemma or slice complete: `{'yes' if lean_family_complete else 'no'}`",
        f"- xhigh usable in this environment: `{'yes' if supports_xhigh() else 'no'}`",
        f"- Isolated git worktrees feasible: `{'yes' if git_worktree_supported() else 'no'}`",
        "- Automatic stop condition: `publication_status = PAPER_READY` with preserved proof artifacts",
        f"- Worker infra status this cycle: `{worker_status}`",
        f"- Summary path: `{FAMILY_SUMMARY.relative_to(ROOT)}`",
        f"- Family status paths: {', '.join(status_paths) if status_paths else '(none)'}",
        "- Ledger tail:",
    ]
    summary_lines.extend([f"  {line}" for line in ledger_tail(6)])
    FAMILY_SUMMARY.write_text("\n".join(summary_lines).rstrip() + "\n", encoding="utf-8")

    report_lines = [
        f"[publication_summary] queued paper candidate: {candidate_slug}",
        f"[publication_summary] candidate title: {candidate_title}",
        f"[publication_summary] candidate publication if solved: {candidate_publication_if_solved}",
        f"[publication_summary] candidate publication score: {candidate_publication_score}",
        f"[publication_summary] candidate packet quality: {candidate_packet_quality}",
        f"[publication_summary] candidate pre-solve gate: {candidate_pre_solve_gate}",
        f"[publication_summary] active campaign: {primary['family_slug'] if primary else '(none)'}",
        f"[publication_summary] strongest publication_status: {strongest_status}",
        f"[publication_summary] strongest honest claim: {strongest_claim}",
        f"[publication_summary] theorem slice target: {theorem_target}",
        f"[publication_summary] next blocker: {next_blocker}",
        f"[publication_summary] next decisive feeder: {next_decisive_feeder}",
        f"[publication_summary] next feeders: {', '.join(next_feeders) if next_feeders else '(none listed)'}",
        f"[publication_summary] any Lean family lemma complete: {'yes' if lean_family_complete else 'no'}",
        f"[publication_summary] worker infra: {worker_status}",
        f"[publication_summary] summary path: {FAMILY_SUMMARY.relative_to(ROOT)}",
        f"[publication_summary] status paths: {', '.join(status_paths) if status_paths else '(none)'}",
        "[publication_summary] ledger tail:",
    ]
    report_lines.extend([f"[publication_summary] {line}" for line in ledger_tail(6)])
    for line in report_lines:
        emit_status_line(line)


def sync_tree(src: pathlib.Path, dst: pathlib.Path) -> None:
    if not src.exists():
        return
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


class ParallelWorker:
    def __init__(self, campaign: dict):
        self.campaign = campaign
        self.worktree = ROOT / ".worktrees" / f"{campaign['family_slug']}-{int(time.time())}"
        self.proc: subprocess.Popen | None = None
        self.started_signature: str | None = None

    def seed_checkout(self) -> None:
        for path in worker_required_paths():
            sync_tree(path, self.worktree / path.relative_to(ROOT))

        sync_tree(ROOT / self.campaign["artifact_dir"], self.worktree / self.campaign["artifact_dir"])
        for slug in self.campaign.get("seed_instances", []):
            sync_tree(ROOT / "artifacts" / slug, self.worktree / "artifacts" / slug)

    def start(self) -> bool:
        self.worktree.parent.mkdir(parents=True, exist_ok=True)
        add = subprocess.run(
            ["git", "worktree", "add", "--detach", str(self.worktree), "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if add.returncode != 0:
            append_ledger(f"Parallel worker setup failed for {self.campaign['family_slug']}; continuing sequentially.")
            return False
        self.seed_checkout()
        self.started_signature = campaign_input_signature(self.campaign)
        update_runtime_campaign_state(
            self.campaign["family_slug"],
            last_secondary_worker_attempt_on=now_iso(),
        )
        cmd = [
            str(self.worktree / "run_publication_cycle.sh"),
            "--campaign",
            self.campaign["family_slug"],
            "--worker",
        ]
        self.proc = subprocess.Popen(
            cmd,
            cwd=self.worktree,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
            env={**os.environ, "AUTOMATH_MAX_PARALLEL_WORKERS": "1"},
            start_new_session=True,
        )
        append_ledger(f"Parallel publication worker started for {self.campaign['family_slug']} in isolated git worktree.")
        return True

    def finish(self) -> str:
        if self.proc is None:
            return "not_started"
        try:
            returncode = self.proc.wait(timeout=PARALLEL_WORKER_WAIT_TIMEOUT)
        except subprocess.TimeoutExpired:
            kill_process_group(self.proc, signal.SIGKILL)
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
            failure_count = int(runtime_campaign_state(self.campaign["family_slug"]).get("secondary_worker_failures", 0)) + 1
            backoff_seconds = SECONDARY_WORKER_FAILURE_BACKOFF * min(failure_count, 3)
            backoff_until = (dt.datetime.now().astimezone() + dt.timedelta(seconds=backoff_seconds)).isoformat()
            update_runtime_campaign_state(
                self.campaign["family_slug"],
                secondary_worker_failures=failure_count,
                secondary_worker_backoff_until=backoff_until,
            )
            append_ledger(
                f"Parallel publication worker for {self.campaign['family_slug']} exceeded the cleanup wait budget; "
                "the manager killed it, treated the worker as infrastructure-failed, and continued."
            )
            self._remove_worktree()
            return "infra_failed"
        if returncode == 0:
            sync_tree(self.worktree / self.campaign["dossier_path"], ROOT / self.campaign["dossier_path"])
            sync_tree(self.worktree / self.campaign["artifact_dir"], ROOT / self.campaign["artifact_dir"])
            update_runtime_campaign_state(
                self.campaign["family_slug"],
                last_secondary_worker_signature=self.started_signature,
                secondary_worker_failures=0,
                secondary_worker_backoff_until=None,
            )
            append_ledger(f"Parallel publication worker finished cleanly for {self.campaign['family_slug']} and synced stable dossier/artifact updates back.")
            outcome = "clean"
        else:
            failure_count = int(runtime_campaign_state(self.campaign["family_slug"]).get("secondary_worker_failures", 0)) + 1
            backoff_seconds = SECONDARY_WORKER_FAILURE_BACKOFF * min(failure_count, 3)
            backoff_until = (dt.datetime.now().astimezone() + dt.timedelta(seconds=backoff_seconds)).isoformat()
            update_runtime_campaign_state(
                self.campaign["family_slug"],
                secondary_worker_failures=failure_count,
                secondary_worker_backoff_until=backoff_until,
            )
            append_ledger(f"Parallel publication worker for {self.campaign['family_slug']} exited nonzero; manager kept the main worktree unchanged.")
            outcome = "infra_failed"
        self._remove_worktree()
        return outcome

    def _remove_worktree(self) -> None:
        try:
            result = subprocess.run(
                ["git", "worktree", "remove", "--force", str(self.worktree)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=WORKTREE_REMOVE_TIMEOUT,
                check=False,
            )
        except subprocess.TimeoutExpired:
            append_ledger(
                f"Parallel publication worker cleanup timed out while removing the worktree for "
                f"{self.campaign['family_slug']}; the main manager continued without blocking."
            )
            return
        if result.returncode != 0:
            append_ledger(
                f"Parallel publication worker cleanup could not remove the worktree for "
                f"{self.campaign['family_slug']} cleanly; a later manual cleanup may be needed."
            )


class ParallelFeederWorker:
    def __init__(self, entry: dict):
        self.entry = entry
        self.slug = entry["slug"]
        self.worker_role = "solver-A"
        self.worktree = ROOT / ".worktrees" / f"{self.slug}-{int(time.time())}"
        self.proc: subprocess.Popen | None = None

    def seed_checkout(self) -> None:
        for path in worker_required_paths():
            sync_tree(path, self.worktree / path.relative_to(ROOT))

        campaign = find_campaign(self.entry.get("campaign_affinity", ""))
        if campaign is not None:
            sync_tree(ROOT / campaign["dossier_path"], self.worktree / campaign["dossier_path"])
            sync_tree(ROOT / campaign["artifact_dir"], self.worktree / campaign["artifact_dir"])
            for slug in campaign.get("seed_instances", [])[:6]:
                sync_tree(ROOT / "artifacts" / slug, self.worktree / "artifacts" / slug)

        artifact_dir = ROOT / "artifacts" / self.slug
        if artifact_dir.exists():
            sync_tree(artifact_dir, self.worktree / artifact_dir.relative_to(ROOT))
        attempt_dir = candidate_attempt_dir(self.slug)
        if attempt_dir.exists():
            sync_tree(attempt_dir, self.worktree / attempt_dir.relative_to(ROOT))

    def start(self) -> bool:
        self.worktree.parent.mkdir(parents=True, exist_ok=True)
        add = subprocess.run(
            ["git", "worktree", "add", "--detach", str(self.worktree), "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if add.returncode != 0:
            append_ledger(f"Parallel feeder worker setup failed for {self.slug}; continuing without that worker.")
            return False
        self.seed_checkout()
        cmd = [
            "python3",
            str(self.worktree / "scripts" / "automath_cycle.py"),
            "--mode",
            "feeder",
            "--slug",
            self.slug,
            "--worker",
            "--worker-role",
            self.worker_role,
            "--artifact-only-worker",
        ]
        self.proc = subprocess.Popen(
            cmd,
            cwd=self.worktree,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
            env={**os.environ, "AUTOMATH_MAX_PARALLEL_WORKERS": "1"},
            start_new_session=True,
        )
        append_ledger(f"Parallel feeder worker started for {self.slug} in isolated git worktree.")
        return True

    def finish(self) -> str:
        if self.proc is None:
            return "not_started"
        try:
            returncode = self.proc.wait(timeout=PARALLEL_WORKER_WAIT_TIMEOUT)
        except subprocess.TimeoutExpired:
            kill_process_group(self.proc, signal.SIGKILL)
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
            append_ledger(
                f"Parallel feeder worker for {self.slug} exceeded the cleanup wait budget; "
                "the manager killed it, treated the worker as infrastructure-failed, and continued."
            )
            self._remove_worktree()
            return "infra_failed"
        if returncode == 0:
            output_markdown, output_json = candidate_attempt_paths(self.slug, self.worker_role)
            handoff_path = candidate_handoff_path(self.slug, self.worker_role)
            synced = False
            worktree_markdown = self.worktree / output_markdown.relative_to(ROOT)
            worktree_json = self.worktree / output_json.relative_to(ROOT)
            worktree_handoff = self.worktree / handoff_path.relative_to(ROOT)
            if worktree_markdown.exists():
                sync_tree(worktree_markdown, output_markdown)
                synced = True
            if worktree_json.exists():
                sync_tree(worktree_json, output_json)
                synced = True
            if worktree_handoff.exists():
                sync_tree(worktree_handoff, handoff_path)
            if synced:
                append_ledger(
                    f"Parallel feeder worker finished cleanly for {self.slug} and synced only the sidecar solver outputs back."
                )
                outcome = "clean"
            else:
                append_ledger(
                    f"Parallel feeder worker for {self.slug} exited cleanly but produced no sidecar solver outputs, so the manager ignored it."
                )
                outcome = "infra_failed"
        else:
            append_ledger(f"Parallel feeder worker for {self.slug} exited nonzero; manager ignored its partial outputs.")
            outcome = "infra_failed"
        self._remove_worktree()
        return outcome

    def _remove_worktree(self) -> None:
        try:
            result = subprocess.run(
                ["git", "worktree", "remove", "--force", str(self.worktree)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=WORKTREE_REMOVE_TIMEOUT,
                check=False,
            )
        except subprocess.TimeoutExpired:
            append_ledger(
                f"Parallel feeder worker cleanup timed out while removing the worktree for "
                f"{self.slug}; the main manager continued without blocking."
            )
            return
        if result.returncode != 0:
            append_ledger(
                f"Parallel feeder worker cleanup could not remove the worktree for "
                f"{self.slug} cleanly; a later manual cleanup may be needed."
            )


class ParallelProofAttemptWorker:
    def __init__(self, campaign: dict, attempt: dict):
        self.campaign = campaign
        self.attempt = attempt
        self.attempt_kind = attempt["kind"]
        self.worker_role = FAMILY_ATTEMPT_ROLES.get(self.attempt_kind, "solver-A")
        self.worktree = ROOT / ".worktrees" / f"{campaign['family_slug']}-{self.attempt_kind}-{int(time.time())}"
        self.proc: subprocess.Popen | None = None
        self.started_signature: str | None = None

    def seed_checkout(self) -> None:
        for path in worker_required_paths():
            sync_tree(path, self.worktree / path.relative_to(ROOT))
        sync_tree(ROOT / self.campaign["dossier_path"], self.worktree / self.campaign["dossier_path"])
        sync_tree(ROOT / self.campaign["artifact_dir"], self.worktree / self.campaign["artifact_dir"])
        for slug in self.campaign.get("seed_instances", [])[:8]:
            sync_tree(ROOT / "artifacts" / slug, self.worktree / "artifacts" / slug)

    def start(self) -> bool:
        self.worktree.parent.mkdir(parents=True, exist_ok=True)
        add = subprocess.run(
            ["git", "worktree", "add", "--detach", str(self.worktree), "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if add.returncode != 0:
            append_ledger(
                f"Parallel proof attempt worker setup failed for {self.campaign['family_slug']}::{self.attempt_kind}; continuing without that worker."
            )
            return False
        self.seed_checkout()
        self.started_signature = proof_attempt_input_signature(self.campaign, self.attempt_kind)
        update_runtime_campaign_state(
            self.campaign["family_slug"],
            **{
                f"attempt_{self.attempt_kind}_signature": self.started_signature,
                f"attempt_{self.attempt_kind}_on": now_iso(),
            },
        )
        cmd = [
            "python3",
            str(self.worktree / "scripts" / "automath_cycle.py"),
            "--mode",
            "family_attempt",
            "--campaign",
            self.campaign["family_slug"],
            "--attempt-kind",
            self.attempt_kind,
            "--worker",
        ]
        self.proc = subprocess.Popen(
            cmd,
            cwd=self.worktree,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
            env={**os.environ, "AUTOMATH_MAX_PARALLEL_WORKERS": "1"},
            start_new_session=True,
        )
        append_ledger(
            f"Parallel proof attempt worker started for {self.campaign['family_slug']}::{self.attempt_kind} in isolated git worktree."
        )
        return True

    def finish(self) -> str:
        if self.proc is None:
            return "not_started"
        try:
            returncode = self.proc.wait(timeout=PARALLEL_WORKER_WAIT_TIMEOUT)
        except subprocess.TimeoutExpired:
            kill_process_group(self.proc, signal.SIGKILL)
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
            append_ledger(
                f"Parallel proof attempt worker for {self.campaign['family_slug']}::{self.attempt_kind} exceeded the cleanup wait budget; "
                "the manager killed it and continued without syncing sidecar attempt outputs."
            )
            self._remove_worktree()
            return "infra_failed"
        if returncode == 0:
            output_markdown, output_json = campaign_attempt_paths(self.campaign, self.attempt_kind)
            handoff_path = family_attempt_handoff_path(self.campaign, self.attempt_kind)
            synced = False
            worktree_markdown = self.worktree / output_markdown.relative_to(ROOT)
            worktree_json = self.worktree / output_json.relative_to(ROOT)
            worktree_handoff = self.worktree / handoff_path.relative_to(ROOT)
            if worktree_markdown.exists():
                sync_tree(worktree_markdown, output_markdown)
                synced = True
            if worktree_json.exists():
                sync_tree(worktree_json, output_json)
                synced = True
            if worktree_handoff.exists():
                sync_tree(worktree_handoff, handoff_path)
            if synced:
                append_ledger(
                    f"Parallel proof attempt worker finished cleanly for {self.campaign['family_slug']}::{self.attempt_kind} and synced sidecar attempt outputs back."
                )
                outcome = "clean"
            else:
                append_ledger(
                    f"Parallel proof attempt worker for {self.campaign['family_slug']}::{self.attempt_kind} exited cleanly but produced no sidecar attempt outputs, so the manager ignored it."
                )
                outcome = "infra_failed"
        else:
            append_ledger(
                f"Parallel proof attempt worker for {self.campaign['family_slug']}::{self.attempt_kind} exited nonzero; manager ignored its partial outputs."
            )
            outcome = "infra_failed"
        self._remove_worktree()
        return outcome

    def _remove_worktree(self) -> None:
        try:
            result = subprocess.run(
                ["git", "worktree", "remove", "--force", str(self.worktree)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=WORKTREE_REMOVE_TIMEOUT,
                check=False,
            )
        except subprocess.TimeoutExpired:
            append_ledger(
                f"Parallel proof attempt worker cleanup timed out while removing the worktree for "
                f"{self.campaign['family_slug']}::{self.attempt_kind}; the main manager continued without blocking."
            )
            return
        if result.returncode != 0:
            append_ledger(
                f"Parallel proof attempt worker cleanup could not remove the worktree for "
                f"{self.campaign['family_slug']}::{self.attempt_kind} cleanly; a later manual cleanup may be needed."
            )


def maybe_start_parallel_worker(primary_slug: str, allow_parallel: bool) -> ParallelWorker | None:
    if not allow_parallel or not git_worktree_supported():
        return None
    campaigns = [c for c in active_campaigns() if c["family_slug"] != primary_slug]
    if not campaigns:
        return None
    secondary = campaigns[0]
    should_start, reason = should_start_secondary_worker(secondary)
    if not should_start:
        append_ledger(
            f"Parallel publication worker was skipped for {secondary['family_slug']} because {reason}."
        )
        return None
    worker = ParallelWorker(secondary)
    if worker.start():
        return worker
    return None


def maybe_start_parallel_feeder_workers(
    campaign: dict,
    allow_parallel: bool,
    reserved_slots: int,
    proof_reserve: int = 0,
) -> list[ParallelFeederWorker]:
    if not allow_parallel or not git_worktree_supported():
        return []
    if publication_stop_ready(campaign_status_path(campaign)):
        return []
    max_parallel = int(os.environ.get("AUTOMATH_MAX_PARALLEL_WORKERS", "5"))
    available_slots = max(0, max_parallel - 1 - reserved_slots - proof_reserve)
    feeder_budget = min(PARALLEL_FEEDER_WORKERS, available_slots)
    if feeder_budget <= 0:
        return []
    workers: list[ParallelFeederWorker] = []
    for entry in next_campaign_feeder_entries(campaign, feeder_budget):
        worker = ParallelFeederWorker(entry)
        if worker.start():
            workers.append(worker)
    return workers


def maybe_start_parallel_proof_attempt_workers(
    campaign: dict,
    allow_parallel: bool,
    reserved_slots: int,
) -> list[ParallelProofAttemptWorker]:
    budget = proof_attempt_budget(campaign, allow_parallel, reserved_slots)
    if budget <= 0:
        return []
    workers: list[ParallelProofAttemptWorker] = []
    for attempt in proof_attempt_specs(campaign):
        if len(workers) >= budget:
            break
        signature = proof_attempt_input_signature(campaign, attempt["kind"])
        should_run, reason = should_run_proof_attempt(campaign, attempt["kind"], signature)
        if not should_run:
            append_ledger(
                f"Parallel proof attempt {campaign['family_slug']}::{attempt['kind']} was skipped because {reason}."
            )
            continue
        worker = ParallelProofAttemptWorker(campaign, attempt)
        if worker.start():
            workers.append(worker)
    return workers


def absorb_parallel_feeder_result(entry: dict, worker_role: str = "solver-A") -> bool:
    _, status_path = candidate_attempt_paths(entry["slug"], worker_role)
    if not status_path.exists():
        return False
    ensure_publication_defaults(status_path)
    data = load_json(status_path, {})
    classification = data.get("classification")
    verify_verdict = data.get("verify_verdict")
    publication_status = data.get("publication_status") or entry.get("publication_status", "NONE")
    if classification == "REDISCOVERY":
        mark_rediscovery(entry, "Prior-art audit during verify found the exact statement already covered in the literature.")
        return True
    if verify_verdict == "VERIFIED" and classification in {"CANDIDATE", "COUNTEREXAMPLE"}:
        archive_attempted_problem(
            entry,
            classification,
            f"Verified feeder evidence from sidecar {worker_role} was archived so publication mode can use it as campaign input without rerunning it as a fresh queue target.",
            publication_status,
        )
        append_ledger(f"Archived verified feeder evidence for {entry['slug']} after sidecar {worker_role} finished.")
        return True
    if classification == "EXACT" and data.get("lean_complete") is True:
        archive_exact_instance(
            entry,
            "Lean verified the exact intended statement in the AutoMath backend; archived to avoid rerunning this solved instance while publication campaigns continue.",
            publication_status,
        )
        append_ledger(f"Lean verified the exact intended statement for {entry['slug']} in sidecar {worker_role}; archived as feeder evidence.")
        return True
    append_ledger(
        f"Manager discarded sidecar {worker_role} output for {entry['slug']} because it did not honestly shorten solve-to-publication distance."
    )
    return False


def maybe_run_campaign_lean(campaign: dict, signature: str) -> None:
    should_run, reason = should_run_campaign_lean(campaign, signature)
    if not should_run:
        append_ledger(f"Lean was skipped for family campaign {campaign['family_slug']} because {reason}.")
        return
    render_campaign_selection(campaign)
    rc = run_stage(
        ROOT,
        f"lean_family_{campaign['family_slug']}",
        PROMPTS / "lean.prompt.md",
        "off",
        LEAN_TIMEOUT,
        preferred_effort("xhigh"),
        "default",
    )
    if rc == 124:
        append_ledger(f"Lean timed out on family campaign {campaign['family_slug']}; the family artifact remains active for later.")
    elif rc != 0:
        append_ledger(f"Lean exited unexpectedly on family campaign {campaign['family_slug']}; the family artifact remains active for later.")
    else:
        update_runtime_campaign_state(
            campaign["family_slug"],
            last_lean_signature=signature,
            last_lean_on=now_iso(),
        )


def run_campaign_flow(campaign: dict, allow_parallel: bool) -> int:
    near_closure, closure_reason = campaign_is_near_closure(campaign)
    if not near_closure:
        append_ledger(
            f"Campaign mode did not start for {campaign['family_slug']} because {closure_reason}."
        )
        write_publication_summary(campaign["family_slug"], "not_used")
        return 0
    status_path = render_campaign_selection(campaign)
    append_ledger(f"publication mode selected active family campaign {campaign['family_slug']}.")
    input_signature = campaign_input_signature(campaign)
    should_refresh, refresh_reason = should_run_frontier_refresh(campaign, input_signature)
    if should_refresh:
        rc = run_stage(
            ROOT,
            f"generalize_{campaign['family_slug']}",
            PROMPTS / "generalize_family.prompt.md",
            "off",
            GENERALIZE_TIMEOUT,
            preferred_effort("xhigh"),
            "tuned_openai",
        )
        if rc == 124:
            append_ledger(f"Frontier refresh timed out for family campaign {campaign['family_slug']}.")
        elif rc != 0:
            append_ledger(f"Frontier refresh exited unexpectedly for family campaign {campaign['family_slug']}.")
        else:
            input_signature = campaign_input_signature(campaign)
            mark_generalize_success(campaign, input_signature, frontier_refresh=True)
    else:
        append_ledger(
            f"Frontier refresh was skipped for family campaign {campaign['family_slug']} because {refresh_reason}."
        )

    worker = maybe_start_parallel_worker(campaign["family_slug"], allow_parallel)
    feeder_reserve = 1 if worker is not None else 0
    proof_reserve = proof_attempt_budget(campaign, allow_parallel, feeder_reserve)
    feeder_workers = maybe_start_parallel_feeder_workers(
        campaign,
        allow_parallel,
        reserved_slots=feeder_reserve,
        proof_reserve=proof_reserve,
    )
    proof_workers = maybe_start_parallel_proof_attempt_workers(
        campaign,
        allow_parallel,
        reserved_slots=feeder_reserve + len(feeder_workers),
    )
    new_feeder_signal = False
    new_attempt_signal = False
    infra_failed = False

    should_generalize, generalize_reason = should_run_campaign_generalize(campaign, input_signature)
    if should_generalize:
        rc = run_stage(
            ROOT,
            f"generalize_{campaign['family_slug']}",
            PROMPTS / "generalize_family.prompt.md",
            "off",
            GENERALIZE_TIMEOUT,
            preferred_effort("xhigh"),
            "tuned_openai",
        )
        if rc == 124:
            append_ledger(f"Generalize timed out for family campaign {campaign['family_slug']}.")
        elif rc != 0:
            append_ledger(f"Generalize exited unexpectedly for family campaign {campaign['family_slug']}.")
        else:
            input_signature = campaign_input_signature(campaign)
            mark_generalize_success(campaign, input_signature)
    else:
        append_ledger(
            f"Generalize was skipped for family campaign {campaign['family_slug']} because {generalize_reason}."
        )

    should_audit, audit_reason = should_run_publication_audit(campaign, input_signature)
    if should_audit:
        rc = run_stage(
            ROOT,
            "publication_audit",
            PROMPTS / "publication_audit.prompt.md",
            "on",
            PUBLICATION_AUDIT_TIMEOUT,
            preferred_effort("xhigh"),
            "tuned_openai",
        )
        if rc == 124:
            append_ledger(f"Publication audit timed out for family campaign {campaign['family_slug']}.")
        elif rc != 0:
            append_ledger(f"Publication audit exited unexpectedly for family campaign {campaign['family_slug']}.")
        else:
            update_runtime_campaign_state(
                campaign["family_slug"],
                last_publication_audit_on=now_iso(),
                last_publication_audit_signature=input_signature,
            )
    else:
        append_ledger(
            f"Publication audit was skipped for family campaign {campaign['family_slug']} because {audit_reason}."
        )

    maybe_run_campaign_lean(campaign, input_signature)

    ensure_publication_defaults(status_path)
    if (
        campaign.get("family_slug") == "zero_divisor_prime_labelings"
        and not publication_stop_ready(status_path)
    ):
        if feeder_workers or proof_workers:
            append_ledger(
                f"Sequential decisive feeder work was skipped for {campaign['family_slug']} because isolated feeder/proof attempt workers already used the active math budget this cycle."
            )
        else:
            feeder_entry = next_campaign_feeder_entry(campaign, {worker.slug for worker in feeder_workers})
            if feeder_entry is not None:
                append_ledger(
                    f"Publication mode is advancing {campaign['family_slug']} through its decisive feeder {feeder_entry['slug']}."
                )
                run_feeder_entry(feeder_entry, emit_summary=False)

    for feeder_worker in feeder_workers:
        outcome = feeder_worker.finish()
        if outcome == "clean":
            if absorb_parallel_feeder_result(feeder_worker.entry, feeder_worker.worker_role):
                new_feeder_signal = True
        else:
            infra_failed = True

    for proof_worker in proof_workers:
        outcome = proof_worker.finish()
        if outcome == "clean":
            new_attempt_signal = True
        else:
            infra_failed = True

    if new_feeder_signal or new_attempt_signal:
        if new_feeder_signal and new_attempt_signal:
            append_ledger(
                f"Parallel feeder and proof-attempt results changed the campaign input for {campaign['family_slug']}, so the canonical family generalize/audit pass is rerunning once to absorb them."
            )
        elif new_feeder_signal:
            append_ledger(
                f"Parallel feeder results changed the campaign input for {campaign['family_slug']}, so the family generalize/audit pass is rerunning once to absorb them."
            )
        else:
            append_ledger(
                f"Parallel proof-attempt results changed the campaign input for {campaign['family_slug']}, so the canonical family generalize/audit pass is rerunning once to absorb them."
            )
        render_campaign_selection(campaign)
        input_signature = campaign_input_signature(campaign)
        rc = run_stage(
            ROOT,
            f"generalize_{campaign['family_slug']}",
            PROMPTS / "generalize_family.prompt.md",
            "off",
            GENERALIZE_TIMEOUT,
            preferred_effort("xhigh"),
            "tuned_openai",
        )
        if rc == 0:
            input_signature = campaign_input_signature(campaign)
            mark_generalize_success(campaign, input_signature)
        rc = run_stage(
            ROOT,
            "publication_audit",
            PROMPTS / "publication_audit.prompt.md",
            "on",
            PUBLICATION_AUDIT_TIMEOUT,
            preferred_effort("xhigh"),
            "tuned_openai",
        )
        if rc == 0:
            update_runtime_campaign_state(
                campaign["family_slug"],
                last_publication_audit_on=now_iso(),
                last_publication_audit_signature=input_signature,
            )

    secondary_outcome = "not_used"
    if worker is not None:
        secondary_outcome = worker.finish()
        if secondary_outcome == "infra_failed":
            infra_failed = True

    worker_status = "infra_failed" if infra_failed else ("clean" if secondary_outcome == "clean" else "not_used")

    ensure_publication_defaults(status_path)
    if publication_stop_ready(status_path):
        STOP_MARKER.write_text("", encoding="utf-8")
        append_ledger(f"Publication-ready stop marker set after campaign {campaign['family_slug']} reached PAPER_READY.")
    else:
        append_ledger(f"Campaign {campaign['family_slug']} remains active with publication status {status_value(status_path, 'publication_status') or 'NONE'}.")
    write_publication_summary(campaign["family_slug"], worker_status)
    return 0


def should_run_instance_lean(entry: dict, status_path: pathlib.Path) -> tuple[bool, str]:
    if status_value(status_path, "lean_ready") is not True:
        return False, "Lean is not marked ready"
    if entry.get("entry_type") != "paper_candidate":
        return True, "non-paper candidate Lean remains allowed"
    if status_value(status_path, "lean_packet_seal") is not True:
        reason = status_value(status_path, "lean_gate_reason")
        if isinstance(reason, str) and reason.strip():
            return False, reason.strip()
        return False, "Lean is not marked as the direct packet-sealing step"
    gate_ok, gate_reason = paper_candidate_gate(entry)
    if not gate_ok:
        return False, gate_reason
    publication_status = status_value(status_path, "publication_status") or entry.get("publication_status") or "NONE"
    classification = status_value(status_path, "classification")
    if classification not in {"CANDIDATE", "COUNTEREXAMPLE", "EXACT"}:
        return False, f"classification={classification or 'NONE'} is not a Lean-sealable one-shot result"
    if publication_rank(publication_status) < publication_rank("SLICE_CANDIDATE"):
        return False, f"publication_status={publication_status} is not a paper-sealing state"
    distance = normalized_rank(entry.get("solve_to_publication_distance"), PAPER_DISTANCE_RANK, 99)
    if distance > PAPER_DISTANCE_RANK["short"] and publication_rank(publication_status) < publication_rank("SLICE_EXACT"):
        return False, "one-shot Lean is reserved for tiny/short packets unless the result is already slice-exact"
    return True, "Lean can directly help seal this one-shot packet"


def run_instance_lean(entry: dict, status_path: pathlib.Path) -> None:
    should_run, reason = should_run_instance_lean(entry, status_path)
    if not should_run:
        append_ledger(f"Lean was skipped for {entry['slug']} because {reason}.")
        return
    render_queue_selection(entry)
    rc = run_stage(
        ROOT,
        f"lean_{entry['slug']}",
        PROMPTS / "lean.prompt.md",
        "off",
        LEAN_TIMEOUT,
        preferred_effort("high"),
        "default",
    )
    normalize_candidate_pending_lean(status_path)
    classification = status_value(status_path, "classification")
    lean_complete = status_value(status_path, "lean_complete")
    publication_status = status_value(status_path, "publication_status") or "INSTANCE_ONLY"
    if classification == "EXACT" and lean_complete is True:
        archive_exact_instance(
            entry,
            "Lean verified the exact intended statement in the AutoMath backend; archived to avoid rerunning this solved instance while publication campaigns continue.",
            publication_status,
        )
        append_ledger(f"Lean verified the exact intended statement for {entry['slug']}; archived as feeder evidence without stopping the harness.")
        return
    if rc == 124:
        append_ledger(f"Lean infrastructure timeout for {entry['slug']}; the instance stays archived only if later runs finish the exact proof.")
    elif rc != 0:
        append_ledger(f"Lean infrastructure failure for {entry['slug']}; the instance remains pending or failed depending on later campaign use.")


def run_affiliated_generalize(entry: dict, status_path: pathlib.Path) -> None:
    if entry.get("entry_type") == "paper_candidate":
        return
    family_slug = status_value(status_path, "family_affinity") or entry.get("campaign_affinity")
    if not family_slug:
        return
    campaign = find_campaign(str(family_slug))
    if campaign is None:
        return
    near_closure, closure_reason = campaign_is_near_closure(campaign)
    if not near_closure:
        append_ledger(
            f"Affiliated campaign work was skipped for {campaign['family_slug']} because {closure_reason}."
        )
        return
    input_signature = campaign_input_signature(campaign)
    should_refresh, refresh_reason = should_run_frontier_refresh(campaign, input_signature)
    if should_refresh:
        render_campaign_selection(campaign)
        rc = run_stage(
            ROOT,
            f"generalize_{campaign['family_slug']}",
            PROMPTS / "generalize_family.prompt.md",
            "off",
            GENERALIZE_TIMEOUT,
            preferred_effort("xhigh"),
            "tuned_openai",
        )
        if rc == 0:
            input_signature = campaign_input_signature(campaign)
            mark_generalize_success(campaign, input_signature, frontier_refresh=True)
    else:
        append_ledger(
            f"Affiliated frontier refresh was skipped for family campaign {campaign['family_slug']} because {refresh_reason}."
        )
    render_campaign_selection(campaign)
    should_generalize, generalize_reason = should_run_campaign_generalize(campaign, input_signature)
    if should_generalize:
        rc = run_stage(
            ROOT,
            f"generalize_{campaign['family_slug']}",
            PROMPTS / "generalize_family.prompt.md",
            "off",
            GENERALIZE_TIMEOUT,
            preferred_effort("xhigh"),
            "tuned_openai",
        )
        if rc == 0:
            input_signature = campaign_input_signature(campaign)
            mark_generalize_success(campaign, input_signature)
    else:
        append_ledger(
            f"Affiliated generalize was skipped for family campaign {campaign['family_slug']} because {generalize_reason}."
        )
    should_audit, audit_reason = should_run_publication_audit(campaign, input_signature)
    if should_audit:
        rc = run_stage(
            ROOT,
            "publication_audit",
            PROMPTS / "publication_audit.prompt.md",
            "on",
            PUBLICATION_AUDIT_TIMEOUT,
            preferred_effort("xhigh"),
            "tuned_openai",
        )
        if rc == 0:
            update_runtime_campaign_state(
                campaign["family_slug"],
                last_publication_audit_on=now_iso(),
                last_publication_audit_signature=input_signature,
            )
    else:
        append_ledger(
            f"Affiliated publication audit was skipped for family campaign {campaign['family_slug']} because {audit_reason}."
        )
    maybe_run_campaign_lean(campaign, input_signature)


def run_feeder_entry(
    entry: dict,
    emit_summary: bool = True,
    artifact_only_worker: bool = False,
    worker_role: str | None = None,
) -> int:
    if entry.get("entry_type") == "family_campaign" and entry.get("family_slug"):
        campaign = find_campaign(entry["family_slug"])
        if campaign is not None:
            return run_campaign_flow(campaign, allow_parallel=False)

    status_path = render_queue_selection(
        entry,
        worker_role=worker_role,
        sidecar=artifact_only_worker and bool(worker_role),
    )
    append_ledger(f"started solving {entry['slug']}")

    rc = run_stage(
        ROOT,
        f"solve_{entry['slug']}",
        PROMPTS / "solve_reasoning_first.prompt.md",
        "off",
        SOLVE_TIMEOUT,
        preferred_effort("high"),
        "tuned_openai",
    )
    if rc != 0:
        if rc == 124:
            append_ledger(f"Solve infrastructure failure for {entry['slug']}: the worker timed out before a real verdict.")
        else:
            append_ledger(f"Solve infrastructure failure for {entry['slug']}: the worker exited unexpectedly.")
        rotate_problem_to_end(entry["slug"])
        if emit_summary:
            write_publication_summary(entry.get("campaign_affinity"), "infra_failed")
        return 0

    normalize_candidate_pending_lean(status_path)
    if status_value(status_path, "classification") is None:
        append_ledger(f"Solve infrastructure failure for {entry['slug']}: no usable status verdict was written.")
        rotate_problem_to_end(entry["slug"])
        if emit_summary:
            write_publication_summary(entry.get("campaign_affinity"), "infra_failed")
        return 0

    rc = run_stage(
        ROOT,
        f"verify_{entry['slug']}",
        PROMPTS / "verify_skeptical.prompt.md",
        "on",
        VERIFY_TIMEOUT,
        preferred_effort("high"),
        "tuned_openai",
    )
    if rc != 0:
        if rc == 124:
            append_ledger(f"Verify infrastructure failure for {entry['slug']}: the worker timed out before a real verdict.")
        else:
            append_ledger(f"Verify infrastructure failure for {entry['slug']}: the worker exited unexpectedly.")
        rotate_problem_to_end(entry["slug"])
        if emit_summary:
            write_publication_summary(entry.get("campaign_affinity"), "infra_failed")
        return 0

    ensure_publication_defaults(status_path)
    normalize_candidate_pending_lean(status_path)
    classification = status_value(status_path, "classification")
    verify_verdict = status_value(status_path, "verify_verdict")
    publication_status = status_value(status_path, "publication_status") or "NONE"
    if classification == "REDISCOVERY":
        mark_rediscovery(entry, "Prior-art audit during verify found the exact statement already covered in the literature.")
        if emit_summary:
            write_publication_summary(entry.get("campaign_affinity"), "not_used")
        return 0
    if verify_verdict is None:
        append_ledger(f"Verify infrastructure failure for {entry['slug']}: no verify verdict was written.")
        rotate_problem_to_end(entry["slug"])
        if emit_summary:
            write_publication_summary(entry.get("campaign_affinity"), "infra_failed")
        return 0

    if artifact_only_worker:
        if emit_summary:
            write_publication_summary(entry.get("campaign_affinity"), "not_used")
        return 0

    run_affiliated_generalize(entry, status_path)
    render_queue_selection(entry)
    rc = run_stage(
        ROOT,
        "publication_audit",
        PROMPTS / "publication_audit.prompt.md",
        "on",
        PUBLICATION_AUDIT_TIMEOUT,
        preferred_effort("xhigh"),
        "tuned_openai",
    )
    ensure_publication_defaults(status_path)
    classification = status_value(status_path, "classification")
    verify_verdict = status_value(status_path, "verify_verdict")
    publication_status = status_value(status_path, "publication_status") or "NONE"

    if status_value(status_path, "lean_ready") is not True and classification not in {"CANDIDATE", "COUNTEREXAMPLE", "EXACT"}:
        mark_failed_problem(entry, str(verify_verdict), publication_status)
        if emit_summary:
            write_publication_summary(entry.get("campaign_affinity"), "not_used")
        return 0

    run_instance_lean(entry, status_path)
    ensure_publication_defaults(status_path)
    classification = status_value(status_path, "classification")
    verify_verdict = status_value(status_path, "verify_verdict")
    publication_status = status_value(status_path, "publication_status") or "NONE"
    if verify_verdict == "VERIFIED" and classification in {"CANDIDATE", "COUNTEREXAMPLE"}:
        archive_attempted_problem(
            entry,
            classification,
            "Verified feeder evidence archived so publication mode can use it as campaign input without rerunning it as a fresh queue target.",
            publication_status,
        )
        append_ledger(
            f"Archived verified feeder evidence for {entry['slug']} so it remains campaign fuel without reentering the live queue."
        )
    if publication_stop_ready(status_path):
        STOP_MARKER.write_text("", encoding="utf-8")
        append_ledger(f"Publication-ready stop marker set after feeder result {entry['slug']} reached PAPER_READY.")
    if emit_summary:
        write_publication_summary(entry.get("campaign_affinity"), "not_used")
    return 0


def run_feeder_cycle() -> int:
    if STOP_MARKER.exists():
        append_ledger("Stop marker already exists, so this cycle was skipped.")
        return 0

    if not run_curation_if_needed():
        return 0

    entry = select_queue_entry(prefer_feeders=True)
    if entry is None:
        append_ledger("No usable problem was available after curation checks, so this cycle ended cleanly.")
        write_publication_summary(None, "not_used")
        return 0
    return run_feeder_entry(entry, emit_summary=True)


def run_publication_cycle(explicit_campaign: str | None, allow_parallel: bool) -> int:
    if STOP_MARKER.exists():
        append_ledger("Stop marker already exists, so this cycle was skipped.")
        write_publication_summary(explicit_campaign, "not_used")
        return 0
    if explicit_campaign:
        campaign = find_campaign(explicit_campaign)
        if campaign is None:
            append_ledger(f"Requested campaign {explicit_campaign} was not found, so this cycle ended cleanly.")
            write_publication_summary(None, "not_used")
            return 0
        return run_campaign_flow(campaign, allow_parallel=allow_parallel)
    if not run_curation_if_needed(required_entry_type="paper_candidate"):
        write_publication_summary(None, "not_used")
        return 0
    normalize_queue_for_scheduler()
    entry = select_paper_candidate_entry()
    if entry is None:
        append_ledger(
            "Publication mode found no queued `paper_candidate`, so it ended cleanly without silently falling back to campaign-first or feeder-first behavior."
        )
        write_publication_summary(None, "not_used")
        return 0
    append_ledger(
        f"Publication mode selected one-shot paper candidate {entry['slug']} instead of silently preferring a warm family campaign."
    )
    return run_feeder_entry(entry, emit_summary=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="AutoMath cycle manager")
    parser.add_argument("--mode", choices=["publication", "feeder", "family_attempt"], default="publication")
    parser.add_argument("--campaign")
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--slug")
    parser.add_argument("--attempt-kind")
    parser.add_argument("--artifact-only-worker", action="store_true")
    parser.add_argument("--worker-role")
    args = parser.parse_args()

    ensure_state()
    append_cycle_log(f"[automath_cycle] {args.mode} cycle started at {now_str()}.")
    try:
        if args.mode == "publication":
            max_parallel = int(os.environ.get("AUTOMATH_MAX_PARALLEL_WORKERS", "5"))
            allow_parallel = (not args.worker) and max_parallel > 1
            return run_publication_cycle(args.campaign, allow_parallel)
        if args.mode == "family_attempt":
            if not args.campaign or not args.attempt_kind:
                append_ledger("Family proof attempt mode requires both --campaign and --attempt-kind, so this attempt ended cleanly.")
                return 0
            campaign = find_campaign(args.campaign)
            if campaign is None:
                append_ledger(f"Requested campaign {args.campaign} was not found, so this family proof attempt ended cleanly.")
                return 0
            return run_family_proof_attempt(campaign, args.attempt_kind)
        if args.slug:
            entry = find_feeder_entry_by_slug(args.slug)
            if entry is None:
                append_ledger(f"Requested feeder {args.slug} was not found, so this feeder cycle ended cleanly.")
                return 0
            return run_feeder_entry(
                entry,
                emit_summary=not args.worker,
                artifact_only_worker=args.artifact_only_worker,
                worker_role=args.worker_role,
            )
        return run_feeder_cycle()
    finally:
        append_cycle_log(f"[automath_cycle] {args.mode} cycle finished at {now_str()}.")


if __name__ == "__main__":
    raise SystemExit(main())
