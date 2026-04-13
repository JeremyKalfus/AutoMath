#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
import pathlib
import re
import shutil
import signal
import subprocess
import tempfile
import time
from dataclasses import dataclass


ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"
ARTIFACTS = ROOT / "artifacts"
LOGS = ARTIFACTS / "_logs"
SUMMARY_PATH = ARTIFACTS / "summary.md"
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
STOP_MARKER = ROOT / ".stop_harness"
CAPABILITIES_CACHE = LOGS / "codex_capabilities.json"

PUBLICATION_STATUS_RANK = {
    "NONE": 0,
    "INSTANCE_ONLY": 1,
    "REDISCOVERY": 2,
    "SLICE_CANDIDATE": 3,
    "SLICE_EXACT": 4,
    "PAPER_READY": 5,
}

CURATION_TIMEOUT = int(os.environ.get("AUTOMATH_CURATION_TIMEOUT", "660"))
SOLVE_TIMEOUT = int(os.environ.get("AUTOMATH_SOLVE_TIMEOUT", "2700"))
VERIFY_TIMEOUT = int(os.environ.get("AUTOMATH_VERIFY_TIMEOUT", "720"))
PUBLICATION_AUDIT_TIMEOUT = int(os.environ.get("AUTOMATH_PUBLICATION_AUDIT_TIMEOUT", "1200"))
LEAN_TIMEOUT = int(os.environ.get("AUTOMATH_LEAN_TIMEOUT", "1800"))
SOLVE_CONCURRENCY = int(os.environ.get("AUTOMATH_SOLVE_CONCURRENCY", "2"))
CANDIDATE_INFRA_COOLDOWN = int(os.environ.get("AUTOMATH_CANDIDATE_INFRA_COOLDOWN", "21600"))
SALVAGE_TAIL_LINES = int(os.environ.get("AUTOMATH_SALVAGE_TAIL_LINES", "80"))


def now_str() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat()


def today_str() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d")


def ensure_state() -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    if not RUNTIME_STATE.exists():
        RUNTIME_STATE.write_text("{}\n", encoding="utf-8")
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


def update_runtime_candidate_state(slug: str, **updates) -> None:
    state = load_runtime_state()
    candidates = state.setdefault("candidates", {})
    candidate_state = candidates.setdefault(slug, {})
    for key, value in updates.items():
        if value is None:
            candidate_state.pop(key, None)
        else:
            candidate_state[key] = value
    write_json(RUNTIME_STATE, state)


def runtime_candidate_state(slug: str) -> dict:
    state = load_runtime_state()
    candidates = state.get("candidates", {})
    candidate_state = candidates.get(slug, {})
    return candidate_state if isinstance(candidate_state, dict) else {}


def ledger_tail(lines: int = 6) -> list[str]:
    if not LEDGER.exists():
        return []
    text = LEDGER.read_text(encoding="utf-8").splitlines()
    return text[-lines:]


def publication_summary_ledger_tail(lines: int = 6) -> list[str]:
    if not LEDGER.exists():
        return []
    text = LEDGER.read_text(encoding="utf-8").splitlines()
    blocked_phrases = (
        "campaign",
        "warm campaign",
        "warm family",
        "generalize" + " stage",
        "generalize timed out",
        "family" + " lean",
    )
    collected: list[str] = []
    for line in reversed(text):
        normalized = line.lower()
        if any(phrase in normalized for phrase in blocked_phrases):
            continue
        collected.append(line)
        if len(collected) >= lines:
            break
    return list(reversed(collected))


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


def failed_slug_set() -> set[str]:
    blocked: set[str] = set()
    for item in load_json(FAILED, []):
        if isinstance(item, dict):
            reason = str(item.get("reason") or "").upper()
            if reason.startswith("INFRA_"):
                continue
        slug = slug_of(item)
        if slug:
            blocked.add(slug)
    return blocked


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
    if data.get("classification") != "EXACT":
        return False
    if data.get("lean_complete") is not True:
        return False
    return bool(data.get("proof_artifacts_preserved") or data.get("lean_complete"))


@dataclass(frozen=True)
class StageRunResult:
    stage_name: str
    returncode: int
    stdout_log: pathlib.Path
    last_message: pathlib.Path
    timed_out: bool
    timeout_secs: int


@dataclass
class ParallelSolveWorker:
    entry: dict
    worker_role: str
    selection_file: pathlib.Path
    status_path: pathlib.Path
    stdout_log: pathlib.Path
    solve_ok: bool
    failure_reason: str | None
    stage_result: StageRunResult | None


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


def add_transfer_kit_section(lines: list[str], transfer_kit) -> None:
    if not isinstance(transfer_kit, dict):
        return
    if not any(value for value in transfer_kit.values()):
        return
    lines.extend(["## transfer_kit", ""])
    lemma_items = transfer_kit.get("lemmas") if isinstance(transfer_kit.get("lemmas"), list) else []
    if lemma_items:
        lines.append("### usable_lemmas")
        for item in lemma_items:
            lines.append(f"- {item}")
        lines.append("")
    for key in [
        "toy_example",
        "known_obstruction",
        "prior_work_stop_sentence",
        "recommended_first_attack",
        "paper_if_solved",
    ]:
        value = transfer_kit.get(key)
        if value:
            lines.append(f"### {key}")
            lines.append(str(value).strip())
            lines.append("")


def render_selected_problem(entry: dict, output_path: pathlib.Path = SELECTED) -> None:
    lines = [f"# {entry.get('title', 'Untitled Entry')}", ""]
    for key in [
        "entry_type",
        "slug",
        "worker_role",
        "canonical_source",
        "open_status_checked_on",
        "attempt_kind",
        "attack_style",
        "curation_confidence",
        "publication_status",
        "publication_if_solved",
        "publication_if_solved_score",
        "solve_to_publication_distance",
        "single_pass_proof_plausibility",
        "paper_leverage_score",
        "single_solve_to_paper_fraction",
        "title_theorem_strength",
        "family_anchor_strength",
        "publication_narrative_strength",
        "editorial_overhead",
        "immediate_corollary_headroom",
        "isolated_exact_case_risk",
        "broader_theorem_implication_risk",
        "search_heavy",
        "certificate_compactness",
        "transfer_kit_present",
        "exact_gap_from_source",
        "micro_paper_lane_eligible",
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
        "canonical_statement",
        "intended_statement",
        "why_now",
        "why_reasoning_friendly",
        "why_low_token",
        "verifier_hint",
        "lean_hint",
        "rediscovery_risk",
        "why_still_appears_open",
        "why_this_could_be_publishable",
        "pre_solve_gate_reason",
        "micro_paper_assessment",
        "hypothetical_title",
        "hypothetical_abstract",
        "single_solve_paper_explanation",
        "broader_theorem_nonimplication_note",
        "literature_gap",
        "publication_packet_title",
        "publication_packet_frontier_basis",
        "publication_packet_near_paper_reason",
        "publication_packet_literature_scope",
        "publication_packet_artifact_requirements",
        "context_budget",
        "paper_shape",
        "strongest_honest_claim",
        "attempt_output_markdown",
        "attempt_output_json",
        "stop_condition",
        "next_action",
    ]:
        add_text_section(lines, key, entry.get(key))

    add_transfer_kit_section(lines, entry.get("transfer_kit"))

    for list_key in ["definitions", "publication_targets", "red_flags", "publication_red_flags", "allowed_files"]:
        values = entry.get(list_key) or []
        if not values:
            continue
        lines.append(f"## {list_key}")
        for item in values:
            lines.append(f"- {item}")
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def sync_selected_problem_to_queue(queue_entries: list[dict] | None = None) -> None:
    entries = queue_entries if queue_entries is not None else load_json(QUEUE, [])
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("slug"):
            continue
        render_selected_problem(entry_with_working_packet(entry), SELECTED)
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

THEOREM_STRENGTH_RANK = {
    "strong": 0,
    "moderate": 1,
    "weak": 2,
}

OVERHEAD_RANK = {
    "low": 0,
    "moderate": 1,
    "high": 2,
}

HEADROOM_RANK = {
    "high": 0,
    "moderate": 1,
    "low": 2,
    "none": 3,
}

RISK_RANK = {
    "low": 0,
    "moderate": 1,
    "high": 2,
    "unresolved": 3,
}

COMPACTNESS_RANK = {
    "high": 0,
    "moderate": 1,
    "low": 2,
}

EXACT_GAP_RANK = {
    "tiny": 0,
    "small": 1,
    "moderate": 2,
    "broad": 3,
}

PAPER_CANDIDATE_REQUIRED_FIELDS = [
    "publication_if_solved",
    "publication_if_solved_score",
    "solve_to_publication_distance",
    "single_pass_proof_plausibility",
    "paper_leverage_score",
    "single_solve_to_paper_fraction",
    "title_theorem_strength",
    "family_anchor_strength",
    "publication_narrative_strength",
    "editorial_overhead",
    "immediate_corollary_headroom",
    "isolated_exact_case_risk",
    "broader_theorem_implication_risk",
    "search_heavy",
    "certificate_compactness",
    "transfer_kit_present",
    "exact_gap_from_source",
    "micro_paper_lane_eligible",
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
    "hypothetical_title",
    "hypothetical_abstract",
    "single_solve_paper_explanation",
    "broader_theorem_nonimplication_note",
    "literature_gap",
    "transfer_kit",
]

TRUE_VALUES = {"yes", "true", "pass", "1"}
FALSE_VALUES = {"no", "false", "fail", "0"}

SUBAGENT_CONTEXT_BUDGET = "1 candidate, at most 1 dossier, target 3-6 source files, and 1 explicit output file pair."
SOLVER_SIDECAR_ROLES = {"solver-A", "solver-B"}


def normalized_rank(value, mapping: dict[str, int], default: int) -> int:
    if value is None:
        return default
    text = str(value).strip().lower().replace(" ", "_")
    return mapping.get(text, default)


def normalized_float(value) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def normalized_int(value) -> int | None:
    if value is None:
        return None
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return None


def normalized_flag(value) -> bool | None:
    if value is None:
        return None
    text = str(value).strip().lower().replace(" ", "_")
    if text in TRUE_VALUES:
        return True
    if text in FALSE_VALUES:
        return False
    return None


def transfer_kit_complete(transfer_kit) -> bool:
    if not isinstance(transfer_kit, dict):
        return False
    lemmas = transfer_kit.get("lemmas")
    if not isinstance(lemmas, list):
        return False
    lemma_items = [str(item).strip() for item in lemmas if str(item).strip()]
    if len(lemma_items) < 2:
        return False
    for key in [
        "toy_example",
        "known_obstruction",
        "prior_work_stop_sentence",
        "recommended_first_attack",
        "paper_if_solved",
    ]:
        value = transfer_kit.get(key)
        if not isinstance(value, str) or not value.strip():
            return False
    return True


def candidate_cooldown_reason(slug: str) -> str | None:
    state = runtime_candidate_state(slug)
    cooldown_until = parse_status_timestamp(state.get("cooldown_until"))
    if cooldown_until is None:
        return None
    now = dt.datetime.now().astimezone()
    if now >= cooldown_until:
        return None
    failure_stage = state.get("last_infra_failure_stage") or "recent infrastructure failure"
    return f"{slug} is cooling down until {cooldown_until.isoformat()} after {failure_stage}"


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


def candidate_status_path(slug: str) -> pathlib.Path:
    return ROOT / "artifacts" / slug / "status.json"


def build_candidate_working_packet(entry: dict) -> str:
    slug = entry["slug"]
    packet_title = entry.get("publication_packet_title") or entry.get("hypothetical_title") or entry.get("title") or slug
    bounded_sources = [
        entry.get("canonical_source"),
        entry.get("publication_packet_literature_scope"),
        relative_display(ROOT / "artifacts" / slug / "record.md"),
        relative_display(ROOT / "artifacts" / slug / "status.json"),
    ]
    deduped_sources = [item for item in dict.fromkeys(str(x) for x in bounded_sources if x)]
    lines = [
        f"# Working Packet: {packet_title}",
        "",
        f"- slug: `{slug}`",
        f"- title: {entry.get('title', slug)}",
        f"- publication status: `{entry.get('publication_status', 'NONE')}`",
        f"- packet quality: `{entry.get('publication_packet_quality', 'unknown')}`",
        f"- micro-paper eligible: `{entry.get('micro_paper_lane_eligible', 'unknown')}`",
        f"- paper leverage score: `{entry.get('paper_leverage_score', 'unknown')}`",
        f"- single-solve-to-paper fraction: `{entry.get('single_solve_to_paper_fraction', 'unknown')}`",
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
        "## micro_paper_test",
        f"- title theorem strength: {entry.get('title_theorem_strength', '(not recorded)')}",
        f"- family anchor strength: {entry.get('family_anchor_strength', '(not recorded)')}",
        f"- publication narrative strength: {entry.get('publication_narrative_strength', '(not recorded)')}",
        f"- editorial overhead: {entry.get('editorial_overhead', '(not recorded)')}",
        f"- immediate corollary headroom: {entry.get('immediate_corollary_headroom', '(not recorded)')}",
        f"- isolated exact-case risk: {entry.get('isolated_exact_case_risk', '(not recorded)')}",
        f"- broader-theorem implication risk: {entry.get('broader_theorem_implication_risk', '(not recorded)')}",
        f"- search-heavy: {entry.get('search_heavy', '(not recorded)')}",
        f"- certificate compactness: {entry.get('certificate_compactness', '(not recorded)')}",
        f"- exact gap from source: {entry.get('exact_gap_from_source', '(not recorded)')}",
        f"- assessment: {entry.get('micro_paper_assessment', '(not recorded)')}",
        "",
        "## likely_paper_shape",
        f"- note title: {packet_title}",
        f"- hypothetical title: {entry.get('hypothetical_title', packet_title)}",
        f"- paper shape: {entry.get('paper_shape', '(not recorded)')}",
        f"- publication if solved: {entry.get('publication_if_solved', '(not recorded)')}",
        f"- minimal artifact requirements: {entry.get('publication_packet_artifact_requirements', '(not recorded)')}",
        "",
        "## hypothetical_abstract",
        str(entry.get("hypothetical_abstract") or "(not recorded)"),
        "",
        "## single_solve_explanation",
        str(entry.get("single_solve_paper_explanation") or "(not recorded)"),
        "",
        "## broader_theorem_nonimplication",
        str(entry.get("broader_theorem_nonimplication_note") or "(not recorded)"),
        "",
        "## literature_gap",
        str(entry.get("literature_gap") or "(not recorded)"),
        "",
        "## transfer_kit",
    ]
    transfer_kit = entry.get("transfer_kit")
    if transfer_kit_complete(transfer_kit):
        lines.extend([f"- lemma: {item}" for item in transfer_kit.get("lemmas", []) if str(item).strip()])
        lines.extend(
            [
                f"- toy example: {transfer_kit.get('toy_example')}",
                f"- known obstruction: {transfer_kit.get('known_obstruction')}",
                f"- prior-work stop sentence: {transfer_kit.get('prior_work_stop_sentence')}",
                f"- recommended first attack: {transfer_kit.get('recommended_first_attack')}",
                f"- paper if solved: {transfer_kit.get('paper_if_solved')}",
                "",
            ]
        )
    else:
        lines.extend(["- transfer kit is incomplete", ""])
    lines.extend(
        [
        "## bounded_source_list",
        ]
    )
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
                "paper_leverage_score": entry.get("paper_leverage_score"),
                "single_solve_to_paper_fraction": entry.get("single_solve_to_paper_fraction"),
                "micro_paper_lane_eligible": entry.get("micro_paper_lane_eligible"),
                "publication_if_solved": compact_text(entry.get("publication_if_solved"), 180),
                "why_this_could_be_publishable": compact_text(entry.get("why_this_could_be_publishable"), 180),
                "canonical_source": entry.get("canonical_source"),
                "working_packet_path": relative_display(packet_path),
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
    if not transfer_kit_complete(entry.get("transfer_kit")):
        return False, "transfer kit is missing required lemmas/examples/attack material"
    if normalized_flag(entry.get("pre_solve_gate")) is not True:
        reason = str(entry.get("pre_solve_gate_reason") or "").strip()
        return False, reason or "pre_solve_gate is not an explicit pass"
    if normalized_flag(entry.get("micro_paper_lane_eligible")) is not True:
        return False, "micro_paper_lane_eligible is not an explicit pass"
    if normalized_flag(entry.get("needs_feeder_ladder")) is True:
        return False, "paper candidate still requires a feeder ladder"
    single_fraction = normalized_float(entry.get("single_solve_to_paper_fraction"))
    if single_fraction is None or single_fraction < 0.70:
        return False, "single_solve_to_paper_fraction is below the micro-paper threshold"
    if normalized_rank(entry.get("title_theorem_strength"), THEOREM_STRENGTH_RANK, 99) > THEOREM_STRENGTH_RANK["moderate"]:
        return False, "title_theorem_strength is too weak for the micro-paper lane"
    if normalized_rank(entry.get("family_anchor_strength"), THEOREM_STRENGTH_RANK, 99) > THEOREM_STRENGTH_RANK["moderate"]:
        return False, "family_anchor_strength is too weak for the micro-paper lane"
    if normalized_rank(entry.get("publication_narrative_strength"), THEOREM_STRENGTH_RANK, 99) > THEOREM_STRENGTH_RANK["moderate"]:
        return False, "publication_narrative_strength is too weak for the micro-paper lane"
    if normalized_rank(entry.get("editorial_overhead"), OVERHEAD_RANK, 99) > OVERHEAD_RANK["moderate"]:
        return False, "editorial_overhead is too high for a micro-paper packet"
    if normalized_rank(entry.get("isolated_exact_case_risk"), RISK_RANK, 99) > RISK_RANK["moderate"]:
        return False, "isolated_exact_case_risk is too high for the micro-paper lane"
    if normalized_rank(entry.get("broader_theorem_implication_risk"), RISK_RANK, 99) > RISK_RANK["moderate"]:
        return False, "broader_theorem_implication_risk is still too high or unresolved"
    if normalized_rank(entry.get("certificate_compactness"), COMPACTNESS_RANK, 99) > COMPACTNESS_RANK["moderate"]:
        return False, "certificate_compactness is too weak for a compact note"
    search_heavy = normalized_flag(entry.get("search_heavy"))
    exact_gap_rank = normalized_rank(entry.get("exact_gap_from_source"), EXACT_GAP_RANK, 99)
    compactness_rank = normalized_rank(entry.get("certificate_compactness"), COMPACTNESS_RANK, 99)
    if search_heavy is True and not (
        exact_gap_rank <= EXACT_GAP_RANK["tiny"] and compactness_rank <= COMPACTNESS_RANK["high"]
    ):
        return False, "search-heavy targets are parked unless only a tiny human-readable residue remains"
    if normalized_rank(entry.get("publication_if_solved_score"), PUBLICATION_IF_SOLVED_SCORE_RANK, 99) > PUBLICATION_IF_SOLVED_SCORE_RANK["paper_with_light_packaging"]:
        return False, "publication_if_solved_score says the result is still too far from a paper"
    if normalized_rank(entry.get("solve_to_publication_distance"), PAPER_DISTANCE_RANK, 99) > PAPER_DISTANCE_RANK["short-medium"]:
        return False, "solve_to_publication_distance is too long for the one-shot gate"
    if normalized_rank(entry.get("publication_packet_quality"), PACKET_QUALITY_RANK, 99) > PACKET_QUALITY_RANK["strong"]:
        return False, "publication packet is not yet sharp enough for one-shot solve budget"
    return True, "pass"


def paper_candidate_available(entry: dict) -> tuple[bool, str]:
    gate_ok, gate_reason = paper_candidate_gate(entry)
    if not gate_ok:
        return False, gate_reason
    slug = entry.get("slug")
    if not slug:
        return False, "paper candidate is missing a slug"
    cooldown_reason = candidate_cooldown_reason(slug)
    if cooldown_reason is not None:
        return False, cooldown_reason
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
        available, _ = paper_candidate_available(item)
        if available:
            candidates.append(item)
    return candidates


def normalize_queue_for_scheduler() -> list[dict]:
    queue = load_json(QUEUE, [])
    if not isinstance(queue, list):
        return []
    valid_papers: list[dict] = []
    cooled_papers: list[dict] = []
    invalid_papers: list[dict] = []
    for item in queue:
        if not isinstance(item, dict):
            continue
        if item.get("entry_type") != "paper_candidate":
            continue
        available, reason = paper_candidate_available(item)
        if available:
            valid_papers.append(item)
        elif candidate_cooldown_reason(item.get("slug", "")) is not None:
            parked = dict(item)
            parked.setdefault("publication_lane_note", reason)
            cooled_papers.append(parked)
        else:
            invalid_papers.append(item)
    valid_papers.sort(key=paper_candidate_priority)
    cooled_papers.sort(key=paper_candidate_priority)
    normalized = valid_papers + cooled_papers + invalid_papers
    if normalized != queue:
        write_json(QUEUE, normalized)
    refresh_context_hygiene_surfaces(normalized)
    if normalized:
        sync_selected_problem_to_queue(normalized)
    return normalized


def publication_rank(status: str | None) -> int:
    if status is None:
        return -1
    return PUBLICATION_STATUS_RANK.get(status, -1)
def paper_candidate_priority(entry: dict) -> tuple[int, int, int, int, int, int, int, int, int, str]:
    leverage_score = -(normalized_int(entry.get("paper_leverage_score")) or 0)
    single_fraction = -(int(round((normalized_float(entry.get("single_solve_to_paper_fraction")) or 0.0) * 100)))
    title_strength = normalized_rank(entry.get("title_theorem_strength"), THEOREM_STRENGTH_RANK, 99)
    family_anchor = normalized_rank(entry.get("family_anchor_strength"), THEOREM_STRENGTH_RANK, 99)
    narrative_strength = normalized_rank(entry.get("publication_narrative_strength"), THEOREM_STRENGTH_RANK, 99)
    exact_gap = normalized_rank(entry.get("exact_gap_from_source"), EXACT_GAP_RANK, 99)
    distance = normalized_rank(entry.get("solve_to_publication_distance"), PAPER_DISTANCE_RANK, 5)
    packet_quality = normalized_rank(entry.get("publication_packet_quality"), PACKET_QUALITY_RANK, 99)
    plausibility = normalized_rank(entry.get("single_pass_proof_plausibility"), PLAUDIBILITY_RANK, 5)
    editorial_overhead = normalized_rank(entry.get("editorial_overhead"), OVERHEAD_RANK, 99)
    search_penalty = 1 if normalized_flag(entry.get("search_heavy")) is True else 0
    return (
        leverage_score,
        single_fraction,
        title_strength,
        family_anchor,
        narrative_strength,
        exact_gap,
        distance,
        packet_quality,
        plausibility + editorial_overhead + search_penalty,
        entry.get("slug", ""),
    )


def select_paper_candidate_entry() -> dict | None:
    candidates = usable_paper_candidates()
    if not candidates:
        return None
    candidates.sort(key=paper_candidate_priority)
    return candidates[0]


def render_candidate_attempt_selection(entry: dict, worker_role: str, output_path: pathlib.Path = SELECTED) -> pathlib.Path:
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
    render_selected_problem(attempt_entry, output_path)
    return output_json




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


def candidate_has_usable_solve_status(slug: str) -> bool:
    status_path = candidate_status_path(slug)
    if not status_path.exists():
        return False
    ensure_publication_defaults(status_path)
    normalize_candidate_pending_lean(status_path)
    return status_value(status_path, "classification") is not None


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


def read_tail_lines(path: pathlib.Path, lines: int = SALVAGE_TAIL_LINES) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8", errors="ignore").splitlines()[-lines:]


def artifact_partial_files(slug: str) -> list[str]:
    artifact_dir = ROOT / "artifacts" / slug
    if not artifact_dir.exists():
        return []
    files: list[str] = []
    for candidate in sorted(artifact_dir.rglob("*")):
        if not candidate.is_file():
            continue
        if "salvage" in candidate.parts:
            continue
        files.append(relative_display(candidate))
    return files[:60]


def strongest_recoverable_status(status_path: pathlib.Path) -> dict:
    if not status_path.exists():
        return {}
    ensure_publication_defaults(status_path)
    data = load_json(status_path, {})
    if not isinstance(data, dict):
        return {}
    return {
        key: data.get(key)
        for key in [
            "stage",
            "classification",
            "verify_verdict",
            "publication_status",
            "publication_confidence",
            "lean_ready",
            "lean_complete",
            "next_action",
        ]
        if data.get(key) is not None
    }


def salvage_candidate_failure(
    entry: dict,
    status_path: pathlib.Path,
    result: StageRunResult,
    *,
    failure_reason: str,
) -> pathlib.Path:
    slug = entry["slug"]
    salvage_dir = ROOT / "artifacts" / slug / "salvage"
    salvage_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "slug": slug,
        "title": entry.get("title"),
        "stage": result.stage_name,
        "failure_reason": failure_reason,
        "timed_out": result.timed_out,
        "timeout_secs": result.timeout_secs,
        "salvaged_on": now_iso(),
        "stdout_log": relative_display(result.stdout_log),
        "last_message_path": relative_display(result.last_message),
        "stdout_tail": read_tail_lines(result.stdout_log),
        "last_message": result.last_message.read_text(encoding="utf-8", errors="ignore").strip()
        if result.last_message.exists()
        else "",
        "strongest_recoverable_status": strongest_recoverable_status(status_path),
        "partial_artifacts": artifact_partial_files(slug),
    }
    json_path = salvage_dir / f"{result.stage_name}_last_failure.json"
    write_json(json_path, payload)
    lines = [
        f"# Salvage: {slug}",
        "",
        f"- stage: `{result.stage_name}`",
        f"- failure_reason: `{failure_reason}`",
        f"- timed_out: `{result.timed_out}`",
        f"- timeout_secs: `{result.timeout_secs}`",
        f"- salvaged_on: `{payload['salvaged_on']}`",
        f"- stdout_log: `{payload['stdout_log']}`",
        f"- last_message_path: `{payload['last_message_path']}`",
        "",
        "## strongest_recoverable_status",
        json.dumps(payload["strongest_recoverable_status"], indent=2) if payload["strongest_recoverable_status"] else "{}",
        "",
        "## partial_artifacts",
    ]
    lines.extend([f"- {item}" for item in payload["partial_artifacts"]])
    lines.extend(["", "## stdout_tail"])
    lines.extend(payload["stdout_tail"] or ["(no stdout tail captured)"])
    md_path = salvage_dir / f"{result.stage_name}_last_failure.md"
    md_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return json_path


def record_candidate_infra_failure(
    entry: dict,
    status_path: pathlib.Path,
    result: StageRunResult,
    *,
    failure_reason: str,
    rotate_queue: bool = True,
) -> None:
    slug = entry["slug"]
    failure_count = int(runtime_candidate_state(slug).get("infra_failure_count", 0)) + 1
    cooldown_seconds = CANDIDATE_INFRA_COOLDOWN * min(failure_count, 3)
    cooldown_until = (dt.datetime.now().astimezone() + dt.timedelta(seconds=cooldown_seconds)).isoformat()
    salvage_path = salvage_candidate_failure(entry, status_path, result, failure_reason=failure_reason)
    update_runtime_candidate_state(
        slug,
        infra_failure_count=failure_count,
        last_infra_failure_on=now_iso(),
        last_infra_failure_stage=result.stage_name,
        cooldown_until=cooldown_until,
        last_salvage_path=relative_display(salvage_path),
        last_failure_reason=failure_reason,
    )
    append_ledger(
        f"{slug} hit an infrastructure failure during {result.stage_name}; canonical salvage was written to "
        f"{relative_display(salvage_path)} and the slug is cooled down until {cooldown_until} instead of being archived as a mathematical failure."
    )
    if rotate_queue:
        rotate_problem_to_end(slug)


def run_stage(
    root: pathlib.Path,
    stage_name: str,
    prompt_file: pathlib.Path,
    search_mode: str,
    timeout_secs: int,
    reasoning_effort: str | None = None,
    transport_profile: str = "default",
    selection_file: pathlib.Path = SELECTED,
) -> StageRunResult:
    stamp = dt.datetime.now().strftime("%Y%m%dT%H%M%S")
    stdout_log = LOGS / f"{stamp}_{stage_name}.stdout.log"
    last_message = LOGS / f"{stamp}_{stage_name}.last.txt"
    preface = (
        "Work only inside this repository. Do not use skills, MCP, cloud tasks, "
        "or JSON output schemas. Follow the prompt below exactly. "
        f"The active selection file for this run is `{relative_display(selection_file)}`. Read that file first and "
        "treat it as the active selected-problem packet instead of repo-root `selected_problem.md` whenever they differ. "
        "If the active selection file specifies a handoff memo path, read that memo immediately after the active selection file "
        "and treat its allowed files, stop condition, output path, and context budget as the binding scope for this run."
    )
    if stage_name == "curate":
        preface += (
            " Respect the curation search and time budget. Do not narrate progress. "
            "Stop browsing once you have enough material and write queue.json and "
            "selected_problem.md before any closing message."
        )
    elif stage_name.startswith("verify") or stage_name == "publication_audit":
        preface += (
            " Use live web only inside the bounded prior-art or publication-status pass, "
            "then return to skeptical checking. Keep the audit bounded and update the status "
            "file before any closing message."
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
    return StageRunResult(
        stage_name=stage_name,
        returncode=returncode if not timed_out else 124,
        stdout_log=stdout_log,
        last_message=last_message,
        timed_out=timed_out,
        timeout_secs=timeout_secs,
    )


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


def render_queue_selection(
    entry: dict,
    worker_role: str | None = None,
    sidecar: bool = False,
    output_path: pathlib.Path = SELECTED,
) -> pathlib.Path:
    if sidecar and worker_role:
        return render_candidate_attempt_selection(entry, worker_role, output_path)
    entry = entry_with_working_packet(entry)
    rendered_entry = dict(entry)
    if worker_role:
        rendered_entry["worker_role"] = worker_role
    render_selected_problem(rendered_entry, output_path)
    status_path = candidate_status_path(entry["slug"])
    ensure_publication_defaults(status_path)
    return status_path


def find_queue_entry_by_slug(slug: str) -> dict | None:
    for item in load_json(QUEUE, []):
        if isinstance(item, dict) and item.get("slug") == slug:
            return item
    return None


def run_curation_if_needed(required_entry_type: str | None = None) -> bool:
    if queue_has_usable(required_entry_type=required_entry_type):
        normalize_queue_for_scheduler()
        return True
    if required_entry_type == "paper_candidate":
        append_ledger("Queue had no usable `paper_candidate`, so one-shot publication curation started.")
    else:
        append_ledger("Queue was empty or exhausted, so one-shot publication curation started.")
    result = run_stage(ROOT, "curate", PROMPTS / "curate_batch.prompt.md", "on", CURATION_TIMEOUT, preferred_effort("high"), "default")
    if wait_for_usable_queue(required_entry_type=required_entry_type):
        normalize_queue_for_scheduler()
        if result.returncode == 124:
            if required_entry_type == "paper_candidate":
                append_ledger("Curation hit its time budget but still produced a usable `paper_candidate` queue.")
            else:
                append_ledger("Curation hit its time budget but still produced a usable queue.")
        elif result.returncode != 0:
            if required_entry_type == "paper_candidate":
                append_ledger("Curation ended oddly but still produced a usable `paper_candidate` queue.")
            else:
                append_ledger("Curation ended oddly but still produced a usable queue.")
        return True
    if result.returncode == 124:
        if required_entry_type == "paper_candidate":
            append_ledger("Curation timed out before producing a usable `paper_candidate` queue, so this cycle ended cleanly.")
        else:
            append_ledger("Curation timed out before producing a usable queue, so this cycle ended cleanly.")
    elif result.returncode != 0:
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


def write_publication_summary(worker_status: str) -> None:
    refresh_context_hygiene_surfaces()
    paper_candidate = select_paper_candidate_entry()
    candidate_slug = paper_candidate["slug"] if paper_candidate else "(none queued)"
    candidate_title = paper_candidate["title"] if paper_candidate else "(none queued)"
    candidate_publication_if_solved = paper_candidate.get("publication_if_solved", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_publication_score = paper_candidate.get("publication_if_solved_score", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_pre_solve_gate = paper_candidate.get("pre_solve_gate", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_packet_quality = paper_candidate.get("publication_packet_quality", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_paper_leverage = paper_candidate.get("paper_leverage_score", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_single_fraction = paper_candidate.get("single_solve_to_paper_fraction", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_micro_lane = paper_candidate.get("micro_paper_lane_eligible", "(not recorded)") if paper_candidate else "(none queued)"
    candidate_status_path = (
        str((ROOT / "artifacts" / candidate_slug / "status.json").relative_to(ROOT))
        if paper_candidate
        else "(none)"
    )
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
        f"- Candidate paper leverage score: {candidate_paper_leverage}",
        f"- Candidate single-solve paper fraction: {candidate_single_fraction}",
        f"- Candidate micro-paper lane: {candidate_micro_lane}",
        f"- Solve timeout: `{SOLVE_TIMEOUT}` seconds",
        f"- Concurrent solve slots: `{SOLVE_CONCURRENCY}`",
        f"- xhigh usable in this environment: `{'yes' if supports_xhigh() else 'no'}`",
        "- Automatic stop condition: `publication_status = PAPER_READY`, `classification = EXACT`, and `lean_complete = true`",
        f"- Worker infra status this cycle: `{worker_status}`",
        f"- Summary path: `{SUMMARY_PATH.relative_to(ROOT)}`",
        f"- Candidate status path: `{candidate_status_path}`",
        "- Ledger tail:",
    ]
    summary_tail = publication_summary_ledger_tail(6)
    if summary_tail:
        summary_lines.extend([f"  {line}" for line in summary_tail])
    else:
        summary_lines.append("  - no recent micro-paper ledger entries available")
    SUMMARY_PATH.write_text("\n".join(summary_lines).rstrip() + "\n", encoding="utf-8")

    report_lines = [
        f"[publication_summary] queued paper candidate: {candidate_slug}",
        f"[publication_summary] candidate title: {candidate_title}",
        f"[publication_summary] candidate publication if solved: {candidate_publication_if_solved}",
        f"[publication_summary] candidate publication score: {candidate_publication_score}",
        f"[publication_summary] candidate packet quality: {candidate_packet_quality}",
        f"[publication_summary] candidate pre-solve gate: {candidate_pre_solve_gate}",
        f"[publication_summary] candidate paper leverage score: {candidate_paper_leverage}",
        f"[publication_summary] candidate single-solve paper fraction: {candidate_single_fraction}",
        f"[publication_summary] candidate micro-paper lane: {candidate_micro_lane}",
        f"[publication_summary] solve timeout seconds: {SOLVE_TIMEOUT}",
        f"[publication_summary] concurrent solve slots: {SOLVE_CONCURRENCY}",
        f"[publication_summary] worker infra: {worker_status}",
        f"[publication_summary] summary path: {SUMMARY_PATH.relative_to(ROOT)}",
        f"[publication_summary] status path: {candidate_status_path}",
        "[publication_summary] ledger tail:",
    ]
    if summary_tail:
        report_lines.extend([f"[publication_summary] {line}" for line in summary_tail])
    else:
        report_lines.append("[publication_summary] - no recent micro-paper ledger entries available")
    for line in report_lines:
        emit_status_line(line)




def should_run_instance_lean(entry: dict, status_path: pathlib.Path) -> tuple[bool, str]:
    if status_value(status_path, "lean_ready") is not True:
        return False, "Lean is not marked ready"
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
    result = run_stage(
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
            "Lean verified the exact intended statement in the AutoMath backend; archived to avoid rerunning this solved micro-paper candidate.",
            publication_status,
        )
        append_ledger(f"Lean verified the exact intended statement for {entry['slug']}; the solved micro-paper candidate was archived.")
        return
    if result.returncode == 124:
        append_ledger(f"Lean infrastructure timeout for {entry['slug']}; the instance stays archived only if later runs finish the exact proof.")
    elif result.returncode != 0:
        append_ledger(f"Lean infrastructure failure for {entry['slug']}; the candidate remains pending for a later micro-paper pass.")


def run_solve_stage(
    entry: dict,
    *,
    emit_summary: bool = True,
    artifact_only_worker: bool = False,
    worker_role: str | None = None,
    selection_file: pathlib.Path = SELECTED,
    queue_mutations: bool = True,
) -> tuple[pathlib.Path, bool, StageRunResult | None, str | None]:
    status_path = render_queue_selection(
        entry,
        worker_role=worker_role,
        sidecar=artifact_only_worker and bool(worker_role),
        output_path=selection_file,
    )
    append_ledger(f"started solving {entry['slug']}")

    result = run_stage(
        ROOT,
        f"solve_{entry['slug']}",
        PROMPTS / "solve_reasoning_first.prompt.md",
        "off",
        SOLVE_TIMEOUT,
        preferred_effort("high"),
        "tuned_openai",
        selection_file=selection_file,
    )
    if result.returncode != 0:
        if result.returncode == 124:
            append_ledger(f"Solve infrastructure failure for {entry['slug']}: the worker timed out before a real verdict.")
        else:
            append_ledger(f"Solve infrastructure failure for {entry['slug']}: the worker exited unexpectedly.")
        failure_reason = "solve_timeout" if result.returncode == 124 else "solve_nonzero_exit"
        if queue_mutations and not artifact_only_worker:
            record_candidate_infra_failure(
                entry,
                status_path,
                result,
                failure_reason=failure_reason,
                rotate_queue=True,
            )
        if emit_summary:
            write_publication_summary("infra_failed")
        return status_path, False, result, failure_reason

    normalize_candidate_pending_lean(status_path)
    if status_value(status_path, "classification") is None:
        append_ledger(f"Solve infrastructure failure for {entry['slug']}: no usable status verdict was written.")
        if queue_mutations and not artifact_only_worker:
            record_candidate_infra_failure(
                entry,
                status_path,
                result,
                failure_reason="solve_missing_status",
                rotate_queue=True,
            )
        if emit_summary:
            write_publication_summary("infra_failed")
        return status_path, False, result, "solve_missing_status"
    return status_path, True, result, None


def run_post_solve_pipeline(
    entry: dict,
    status_path: pathlib.Path,
    *,
    emit_summary: bool = True,
    selection_file: pathlib.Path = SELECTED,
) -> int:
    render_queue_selection(entry, output_path=selection_file)

    result = run_stage(
        ROOT,
        f"verify_{entry['slug']}",
        PROMPTS / "verify_skeptical.prompt.md",
        "on",
        VERIFY_TIMEOUT,
        preferred_effort("high"),
        "tuned_openai",
        selection_file=selection_file,
    )
    if result.returncode != 0:
        if result.returncode == 124:
            append_ledger(f"Verify infrastructure failure for {entry['slug']}: the worker timed out before a real verdict.")
        else:
            append_ledger(f"Verify infrastructure failure for {entry['slug']}: the worker exited unexpectedly.")
        record_candidate_infra_failure(
            entry,
            status_path,
            result,
            failure_reason="verify_timeout" if result.returncode == 124 else "verify_nonzero_exit",
            rotate_queue=True,
        )
        if emit_summary:
            write_publication_summary("infra_failed")
        return 0

    ensure_publication_defaults(status_path)
    normalize_candidate_pending_lean(status_path)
    classification = status_value(status_path, "classification")
    verify_verdict = status_value(status_path, "verify_verdict")
    publication_status = status_value(status_path, "publication_status") or "NONE"
    if classification == "REDISCOVERY":
        mark_rediscovery(entry, "Prior-art audit during verify found the exact statement already covered in the literature.")
        if emit_summary:
            write_publication_summary("not_used")
        return 0
    if verify_verdict is None:
        append_ledger(f"Verify infrastructure failure for {entry['slug']}: no verify verdict was written.")
        record_candidate_infra_failure(
            entry,
            status_path,
            result,
            failure_reason="verify_missing_status",
            rotate_queue=True,
        )
        if emit_summary:
            write_publication_summary("infra_failed")
        return 0

    render_queue_selection(entry, output_path=selection_file)
    result = run_stage(
        ROOT,
        "publication_audit",
        PROMPTS / "publication_audit.prompt.md",
        "on",
        PUBLICATION_AUDIT_TIMEOUT,
        preferred_effort("xhigh"),
        "tuned_openai",
        selection_file=selection_file,
    )
    if result.returncode != 0:
        if result.returncode == 124:
            append_ledger(f"Publication audit infrastructure failure for {entry['slug']}: the worker timed out before a real verdict.")
        else:
            append_ledger(f"Publication audit infrastructure failure for {entry['slug']}: the worker exited unexpectedly.")
        record_candidate_infra_failure(
            entry,
            status_path,
            result,
            failure_reason="publication_audit_timeout" if result.returncode == 124 else "publication_audit_nonzero_exit",
            rotate_queue=True,
        )
        if emit_summary:
            write_publication_summary("infra_failed")
        return 0
    ensure_publication_defaults(status_path)
    classification = status_value(status_path, "classification")
    verify_verdict = status_value(status_path, "verify_verdict")
    publication_status = status_value(status_path, "publication_status") or "NONE"

    if status_value(status_path, "lean_ready") is not True and classification not in {"CANDIDATE", "COUNTEREXAMPLE", "EXACT"}:
        mark_failed_problem(entry, str(verify_verdict), publication_status)
        if emit_summary:
            write_publication_summary("not_used")
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
            "Verified but not fully sealed micro-paper attempt archived so it does not immediately recycle into the queue.",
            publication_status,
        )
        append_ledger(
            f"Archived the verified-but-unsealed micro-paper attempt for {entry['slug']} so the queue can move on cleanly."
        )
    if publication_stop_ready(status_path):
        STOP_MARKER.write_text("", encoding="utf-8")
        append_ledger(f"Publication-ready stop marker set after {entry['slug']} reached PAPER_READY.")
    if emit_summary:
        write_publication_summary("not_used")
    return 0


def solve_worker_selection_path(slug: str, worker_role: str) -> pathlib.Path:
    return candidate_attempt_dir(slug) / f"{worker_role}.selection.md"


def run_parallel_solve_slot(entry: dict, worker_role: str) -> ParallelSolveWorker:
    selection_file = solve_worker_selection_path(entry["slug"], worker_role)
    status_path, solve_ok, stage_result, failure_reason = run_solve_stage(
        entry,
        emit_summary=False,
        artifact_only_worker=False,
        worker_role=worker_role,
        selection_file=selection_file,
        queue_mutations=False,
    )
    return ParallelSolveWorker(
        entry=entry,
        worker_role=worker_role,
        selection_file=selection_file,
        status_path=status_path,
        stdout_log=stage_result.stdout_log if stage_result is not None else LOGS / f"{worker_role}_{entry['slug']}.missing.log",
        solve_ok=solve_ok,
        failure_reason=failure_reason,
        stage_result=stage_result,
    )


def run_parallel_solve_batch(entries: list[dict]) -> list[ParallelSolveWorker]:
    workers: list[ParallelSolveWorker] = []
    launches = list(zip(entries[:SOLVE_CONCURRENCY], ["solver-A", "solver-B"]))
    for entry, worker_role in launches:
        append_ledger(
            f"Parallel solve launch: {worker_role} started {entry['slug']} with a {SOLVE_TIMEOUT}-second budget."
        )
    if not launches:
        return workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(launches)) as executor:
        future_map = {
            executor.submit(run_parallel_solve_slot, entry, worker_role): (entry, worker_role)
            for entry, worker_role in launches
        }
        for future in concurrent.futures.as_completed(future_map):
            worker = future.result()
            workers.append(worker)
            if worker.solve_ok:
                append_ledger(
                    f"Parallel solve finish: {worker.worker_role} completed {worker.entry['slug']} with a usable solve artifact; worker log at {relative_display(worker.stdout_log)}."
                )
                continue
            if worker.stage_result is not None and worker.failure_reason is not None:
                record_candidate_infra_failure(
                    worker.entry,
                    worker.status_path,
                    worker.stage_result,
                    failure_reason=worker.failure_reason,
                    rotate_queue=True,
                )
            append_ledger(
                f"Parallel solve finish: {worker.worker_role} completed {worker.entry['slug']} without a usable solve artifact; worker log at {relative_display(worker.stdout_log)}."
            )
    workers.sort(key=lambda item: item.worker_role)
    return workers


def solve_ready_queue_candidates() -> list[dict]:
    ready = [entry for entry in usable_paper_candidates() if candidate_has_usable_solve_status(entry["slug"])]
    ready.sort(key=paper_candidate_priority)
    return ready


def run_selected_entry(
    entry: dict,
    emit_summary: bool = True,
    artifact_only_worker: bool = False,
    worker_role: str | None = None,
    selection_file: pathlib.Path = SELECTED,
    stop_after: str | None = None,
) -> int:
    if candidate_has_usable_solve_status(entry["slug"]):
        status_path = candidate_status_path(entry["slug"])
        render_queue_selection(
            entry,
            worker_role=worker_role,
            sidecar=artifact_only_worker and bool(worker_role),
            output_path=selection_file,
        )
        append_ledger(f"Resuming {entry['slug']} from preserved solve artifacts instead of rerunning solve.")
    else:
        status_path, solve_ok, _, _ = run_solve_stage(
            entry,
            emit_summary=emit_summary,
            artifact_only_worker=artifact_only_worker,
            worker_role=worker_role,
            selection_file=selection_file,
        )
        if not solve_ok:
            return 0
    if stop_after == "solve":
        if emit_summary:
            write_publication_summary("not_used")
        return 0
    if artifact_only_worker:
        if emit_summary:
            write_publication_summary("not_used")
        return 0
    return run_post_solve_pipeline(entry, status_path, emit_summary=emit_summary, selection_file=selection_file)


def run_publication_cycle() -> int:
    if STOP_MARKER.exists():
        append_ledger("Stop marker already exists, so this cycle was skipped.")
        write_publication_summary("not_used")
        return 0
    if not run_curation_if_needed(required_entry_type="paper_candidate"):
        write_publication_summary("not_used")
        return 0
    normalize_queue_for_scheduler()
    ready_entries = solve_ready_queue_candidates()
    if ready_entries:
        entry = ready_entries[0]
        append_ledger(f"Publication mode resumed one-shot paper candidate {entry['slug']} from preserved solve artifacts.")
        return run_selected_entry(entry, emit_summary=True)
    entries = usable_paper_candidates()
    if not entries:
        append_ledger(
            "Publication mode found no queued `paper_candidate`, so it ended cleanly."
        )
        write_publication_summary("not_used")
        return 0
    solve_batch = entries[:SOLVE_CONCURRENCY]
    if len(solve_batch) > 1:
        append_ledger(
            "Publication mode launched a parallel solve batch for "
            + ", ".join(entry["slug"] for entry in solve_batch)
            + f" with {SOLVE_CONCURRENCY} concurrent slots and {SOLVE_TIMEOUT}-second per-solve budgets."
        )
    else:
        append_ledger(f"Publication mode selected one-shot paper candidate {solve_batch[0]['slug']}.")
    run_parallel_solve_batch(solve_batch)
    normalize_queue_for_scheduler()
    ready_entries = solve_ready_queue_candidates()
    if not ready_entries:
        append_ledger("Parallel solve batch ended without a queued candidate advancing past solve, so this cycle ended cleanly.")
        write_publication_summary("not_used")
        return 0
    entry = ready_entries[0]
    append_ledger(f"Publication mode advanced {entry['slug']} from solved status into verify/publication audit.")
    return run_selected_entry(entry, emit_summary=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="AutoMath cycle manager")
    parser.add_argument("--slug")
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--artifact-only-worker", action="store_true")
    parser.add_argument("--worker-role")
    parser.add_argument("--selection-file")
    parser.add_argument("--stop-after", choices=["solve"])
    args = parser.parse_args()

    ensure_state()
    append_cycle_log(f"[automath_cycle] publication cycle started at {now_str()}.")
    try:
        if args.slug:
            entry = find_queue_entry_by_slug(args.slug)
            if entry is None:
                append_ledger(f"Requested queued paper candidate {args.slug} was not found, so this cycle ended cleanly.")
                return 0
            return run_selected_entry(
                entry,
                emit_summary=not args.worker,
                artifact_only_worker=args.artifact_only_worker,
                worker_role=args.worker_role,
                selection_file=pathlib.Path(args.selection_file) if args.selection_file else SELECTED,
                stop_after=args.stop_after,
            )
        return run_publication_cycle()
    finally:
        append_cycle_log(f"[automath_cycle] publication cycle finished at {now_str()}.")


if __name__ == "__main__":
    raise SystemExit(main())
