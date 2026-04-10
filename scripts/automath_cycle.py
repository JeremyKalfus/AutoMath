#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
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
LEDGER = ROOT / "ledger.md"
QUEUE = ROOT / "queue.json"
FAILED = ROOT / "failed_problems.json"
SELECTED = ROOT / "selected_problem.md"
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
PARALLEL_WORKER_WAIT_TIMEOUT = int(os.environ.get("AUTOMATH_PARALLEL_WORKER_WAIT_TIMEOUT", "90"))
WORKTREE_REMOVE_TIMEOUT = int(os.environ.get("AUTOMATH_WORKTREE_REMOVE_TIMEOUT", "30"))


def now_str() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def today_str() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d")


def ensure_state() -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    FAMILY_ARTIFACTS.mkdir(parents=True, exist_ok=True)
    if not LEDGER.exists():
        LEDGER.write_text("# Ledger\n", encoding="utf-8")
    if not QUEUE.exists():
        QUEUE.write_text("[]\n", encoding="utf-8")
    if not FAILED.exists():
        FAILED.write_text("[]\n", encoding="utf-8")
    if not SELECTED.exists():
        SELECTED.write_text("# Selected Problem\n\nNo problem selected yet.\n", encoding="utf-8")


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
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


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


def failed_slug_set() -> set[str]:
    return {slug for slug in (slug_of(item) for item in load_json(FAILED, [])) if slug}


def queue_has_usable() -> bool:
    failed = failed_slug_set()
    queue = load_json(QUEUE, [])
    return any(isinstance(item, dict) and item.get("slug") and item["slug"] not in failed for item in queue)


def wait_for_usable_queue(attempts: int = 5, sleep_seconds: int = 2) -> bool:
    for _ in range(attempts):
        if queue_has_usable():
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
        "family_slug",
        "family_name",
        "campaign_priority",
        "canonical_source",
        "open_status_checked_on",
        "dossier_path",
        "artifact_dir",
        "attack_style",
        "curation_confidence",
        "publication_status",
        "campaign_affinity",
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
        "strongest_honest_claim",
        "next_action",
    ]:
        add_text_section(lines, key, entry.get(key))

    for list_key in ["definitions", "seed_instances", "publication_targets", "next_feeder_instances", "red_flags", "publication_red_flags"]:
        values = entry.get(list_key) or []
        if not values:
            continue
        lines.append(f"## {list_key}")
        for item in values:
            lines.append(f"- {item}")
        lines.append("")

    SELECTED.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def load_campaign_manifest() -> list[dict]:
    data = load_json(CAMPAIGN_MANIFEST, [])
    return data if isinstance(data, list) else []


def campaign_status_path(campaign: dict) -> pathlib.Path:
    return ROOT / campaign["artifact_dir"] / "status.json"


def campaign_record_path(campaign: dict) -> pathlib.Path:
    return ROOT / campaign["artifact_dir"] / "record.md"


def load_campaign_status(campaign: dict) -> dict:
    path = campaign_status_path(campaign)
    ensure_publication_defaults(path)
    return load_json(path, {})


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


def add_queue_entry(entries: list[dict], seen: set[str], failed: set[str], entry: dict | None) -> bool:
    if not entry:
        return False
    slug = entry.get("slug")
    if not slug or slug in seen or slug in failed:
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
    primary_feeders = list(primary.get("recommended_feeders", []))
    secondary_feeders = list(secondary.get("recommended_feeders", [])) if secondary else []

    add_queue_entry(entries, seen, failed, campaign_queue_entry(primary))
    while len(entries) < 3 and primary_feeders:
        add_queue_entry(entries, seen, failed, feeder_queue_entry(primary, primary_feeders.pop(0)))

    if secondary is not None:
        add_queue_entry(entries, seen, failed, campaign_queue_entry(secondary))
        while len(entries) < 5 and secondary_feeders:
            add_queue_entry(entries, seen, failed, feeder_queue_entry(secondary, secondary_feeders.pop(0)))
            break

    while len(entries) < 5 and primary_feeders:
        add_queue_entry(entries, seen, failed, feeder_queue_entry(primary, primary_feeders.pop(0)))

    while len(entries) < 5 and secondary_feeders:
        add_queue_entry(entries, seen, failed, feeder_queue_entry(secondary, secondary_feeders.pop(0)))

    if len(entries) != 5:
        return False
    write_json(QUEUE, entries)
    render_selected_problem(entries[0])
    append_ledger("Queue was empty or exhausted, so it was locally reseeded from active publication campaigns before any broad web curation.")
    return True


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
            ):
                return item
    for item in queue:
        if isinstance(item, dict) and item.get("slug") and item["slug"] not in failed:
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


def remove_problem_from_queue(slug: str) -> None:
    queue = load_json(QUEUE, [])
    write_json(QUEUE, [item for item in queue if not (isinstance(item, dict) and item.get("slug") == slug)])


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
        "or JSON output schemas. Follow the prompt below exactly."
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

    def terminate_process_group(proc: subprocess.Popen, sig: signal.Signals) -> None:
        try:
            os.killpg(proc.pid, sig)
        except ProcessLookupError:
            pass

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
                terminate_process_group(proc, signal.SIGKILL)
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


def render_queue_selection(entry: dict) -> pathlib.Path:
    render_selected_problem(entry)
    status_path = ROOT / "artifacts" / entry["slug"] / "status.json"
    ensure_publication_defaults(status_path)
    return status_path


def find_queue_entry_by_slug(slug: str) -> dict | None:
    for item in load_json(QUEUE, []):
        if isinstance(item, dict) and item.get("slug") == slug:
            return item
    return None


def next_campaign_feeder_entry(campaign: dict) -> dict | None:
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
    seen: set[str] = set()
    for slug in candidates:
        if not slug or slug in seen or slug in failed:
            continue
        seen.add(slug)
        queued = find_queue_entry_by_slug(slug)
        if queued is not None:
            return queued
        for feeder in campaign.get("recommended_feeders", []):
            if isinstance(feeder, dict) and feeder.get("slug") == slug:
                return feeder_queue_entry(campaign, feeder)
    return None


def run_curation_if_needed() -> bool:
    if queue_has_usable():
        return True
    if seed_campaign_queue():
        return True
    append_ledger("Queue was empty or exhausted, so web curation started.")
    rc = run_stage(ROOT, "curate", PROMPTS / "curate_batch.prompt.md", "on", CURATION_TIMEOUT, preferred_effort("high"), "default")
    if wait_for_usable_queue():
        if rc == 124:
            append_ledger("Curation hit its time budget but still produced a usable queue.")
        elif rc != 0:
            append_ledger("Curation ended oddly but still produced a usable queue.")
        return True
    if rc == 124:
        append_ledger("Curation timed out before producing a usable queue, so this cycle ended cleanly.")
    elif rc != 0:
        append_ledger("Curation had an infrastructure failure before producing a usable queue, so this cycle ended cleanly.")
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
    campaigns = active_campaigns()
    primary = find_campaign(active_campaign_slug) if active_campaign_slug else None
    if primary is None and campaigns:
        primary = campaigns[0]
    strongest_status = strongest_publication_status(campaigns) if campaigns else "NONE"
    strongest_claim = status_or_manifest(primary, "strongest_honest_claim") if primary else "(none)"
    theorem_target = status_or_manifest(primary, "theorem_slice_target") if primary else "(none)"
    next_blocker = status_or_manifest(primary, "next_blocker", status_or_manifest(primary, "next_action")) if primary else "(none)"
    next_feeders = status_or_manifest(primary, "next_feeder_instances", []) if primary else []
    next_decisive_feeder = next_feeders[0] if next_feeders else "(none listed)"
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

    def seed_checkout(self) -> None:
        required_paths = [
            ROOT / "AGENTS.md",
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
        for path in required_paths:
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
        )
        append_ledger(f"Parallel publication worker started for {self.campaign['family_slug']} in isolated git worktree.")
        return True

    def finish(self) -> str:
        if self.proc is None:
            return "not_started"
        try:
            returncode = self.proc.wait(timeout=PARALLEL_WORKER_WAIT_TIMEOUT)
        except subprocess.TimeoutExpired:
            self.proc.kill()
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
            append_ledger(
                f"Parallel publication worker for {self.campaign['family_slug']} exceeded the cleanup wait budget; "
                "the manager killed it, treated the worker as infrastructure-failed, and continued."
            )
            self._remove_worktree()
            return "infra_failed"
        if returncode == 0:
            sync_tree(self.worktree / self.campaign["dossier_path"], ROOT / self.campaign["dossier_path"])
            sync_tree(self.worktree / self.campaign["artifact_dir"], ROOT / self.campaign["artifact_dir"])
            append_ledger(f"Parallel publication worker finished cleanly for {self.campaign['family_slug']} and synced stable dossier/artifact updates back.")
            outcome = "clean"
        else:
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


def maybe_start_parallel_worker(primary_slug: str, allow_parallel: bool) -> ParallelWorker | None:
    if not allow_parallel or not git_worktree_supported():
        return None
    campaigns = [c for c in active_campaigns() if c["family_slug"] != primary_slug]
    if not campaigns:
        return None
    worker = ParallelWorker(campaigns[0])
    if worker.start():
        return worker
    return None


def maybe_run_campaign_lean(campaign: dict) -> None:
    status_path = campaign_status_path(campaign)
    ensure_publication_defaults(status_path)
    if status_value(status_path, "lean_ready") is not True:
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


def run_campaign_flow(campaign: dict, allow_parallel: bool) -> int:
    status_path = render_campaign_selection(campaign)
    append_ledger(f"publication mode selected active family campaign {campaign['family_slug']}.")
    worker = maybe_start_parallel_worker(campaign["family_slug"], allow_parallel)
    worker_status = "not_used" if worker is None else "running"

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

    maybe_run_campaign_lean(campaign)

    ensure_publication_defaults(status_path)
    if (
        campaign.get("family_slug") == "zero_divisor_prime_labelings"
        and not publication_stop_ready(status_path)
    ):
        feeder_entry = next_campaign_feeder_entry(campaign)
        if feeder_entry is not None:
            append_ledger(
                f"Publication mode is advancing {campaign['family_slug']} through its decisive feeder {feeder_entry['slug']}."
            )
            run_feeder_entry(feeder_entry, emit_summary=False)

    if worker is not None:
        worker_status = worker.finish()

    ensure_publication_defaults(status_path)
    if publication_stop_ready(status_path):
        STOP_MARKER.write_text("", encoding="utf-8")
        append_ledger(f"Publication-ready stop marker set after campaign {campaign['family_slug']} reached PAPER_READY.")
    else:
        append_ledger(f"Campaign {campaign['family_slug']} remains active with publication status {status_value(status_path, 'publication_status') or 'NONE'}.")
    write_publication_summary(campaign["family_slug"], worker_status)
    return 0


def run_instance_lean(entry: dict, status_path: pathlib.Path) -> None:
    if status_value(status_path, "lean_ready") is not True:
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
    family_slug = status_value(status_path, "family_affinity") or entry.get("campaign_affinity")
    if not family_slug:
        return
    campaign = find_campaign(str(family_slug))
    if campaign is None:
        return
    render_campaign_selection(campaign)
    run_stage(
        ROOT,
        f"generalize_{campaign['family_slug']}",
        PROMPTS / "generalize_family.prompt.md",
        "off",
        GENERALIZE_TIMEOUT,
        preferred_effort("xhigh"),
        "tuned_openai",
    )
    run_stage(
        ROOT,
        "publication_audit",
        PROMPTS / "publication_audit.prompt.md",
        "on",
        PUBLICATION_AUDIT_TIMEOUT,
        preferred_effort("xhigh"),
        "tuned_openai",
    )
    maybe_run_campaign_lean(campaign)


def run_feeder_entry(entry: dict, emit_summary: bool = True) -> int:
    if entry.get("entry_type") == "family_campaign" and entry.get("family_slug"):
        campaign = find_campaign(entry["family_slug"])
        if campaign is not None:
            return run_campaign_flow(campaign, allow_parallel=False)

    status_path = render_queue_selection(entry)
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

    run_affiliated_generalize(entry, status_path)
    render_queue_selection(entry)
    run_stage(
        ROOT,
        "publication_audit",
        PROMPTS / "publication_audit.prompt.md",
        "on",
        PUBLICATION_AUDIT_TIMEOUT,
        preferred_effort("xhigh"),
        "tuned_openai",
    )
    ensure_publication_defaults(status_path)

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
    campaigns = active_campaigns()
    if campaigns:
        return run_campaign_flow(campaigns[0], allow_parallel=allow_parallel)
    append_ledger("No active family campaign was available, so publication mode fell back to feeder curation.")
    return run_feeder_cycle()


def main() -> int:
    parser = argparse.ArgumentParser(description="AutoMath cycle manager")
    parser.add_argument("--mode", choices=["publication", "feeder"], default="publication")
    parser.add_argument("--campaign")
    parser.add_argument("--worker", action="store_true")
    args = parser.parse_args()

    ensure_state()
    append_cycle_log(f"[automath_cycle] {args.mode} cycle started at {now_str()}.")
    try:
        if args.mode == "publication":
            max_parallel = int(os.environ.get("AUTOMATH_MAX_PARALLEL_WORKERS", "3"))
            allow_parallel = (not args.worker) and max_parallel > 1
            return run_publication_cycle(args.campaign, allow_parallel)
        return run_feeder_cycle()
    finally:
        append_cycle_log(f"[automath_cycle] {args.mode} cycle finished at {now_str()}.")


if __name__ == "__main__":
    raise SystemExit(main())
