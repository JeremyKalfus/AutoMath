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
LEDGER = ROOT / "ledger.md"
QUEUE = ROOT / "queue.json"
FAILED = ROOT / "failed_problems.json"
SELECTED = ROOT / "selected_problem.md"
CAMPAIGN_MANIFEST = ROOT / "campaigns" / "manifest.json"
STOP_MARKER = ROOT / ".stop_harness"
CAPABILITIES_CACHE = LOGS / "codex_capabilities.json"

CURATION_TIMEOUT = int(os.environ.get("AUTOMATH_CURATION_TIMEOUT", "660"))
SOLVE_TIMEOUT = int(os.environ.get("AUTOMATH_SOLVE_TIMEOUT", "1200"))
VERIFY_TIMEOUT = int(os.environ.get("AUTOMATH_VERIFY_TIMEOUT", "720"))
GENERALIZE_TIMEOUT = int(os.environ.get("AUTOMATH_GENERALIZE_TIMEOUT", "1800"))
PUBLICATION_AUDIT_TIMEOUT = int(os.environ.get("AUTOMATH_PUBLICATION_AUDIT_TIMEOUT", "1200"))
LEAN_TIMEOUT = int(os.environ.get("AUTOMATH_LEAN_TIMEOUT", "1800"))


def now_str() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def today_str() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d")


def ensure_state() -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
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

    for list_key in ["definitions", "seed_instances", "publication_targets", "red_flags", "publication_red_flags"]:
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
        "why_now": campaign.get("why_now"),
        "seed_instances": campaign.get("seed_instances", []),
        "strongest_honest_claim": status.get("strongest_honest_claim"),
        "next_action": status.get("next_action"),
    }
    render_selected_problem(entry)
    return ROOT / campaign["artifact_dir"] / "status.json"


def select_queue_entry() -> dict | None:
    failed = failed_slug_set()
    for item in load_json(QUEUE, []):
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
    if isinstance(cached, dict) and "xhigh" in cached:
        return bool(cached["xhigh"])
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


def run_curation_if_needed() -> bool:
    if queue_has_usable():
        return True
    append_ledger("Queue was empty or exhausted, so curation started.")
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

    def finish(self) -> None:
        if self.proc is None:
            return
        returncode = self.proc.wait()
        if returncode == 0:
            sync_tree(self.worktree / self.campaign["dossier_path"], ROOT / self.campaign["dossier_path"])
            sync_tree(self.worktree / self.campaign["artifact_dir"], ROOT / self.campaign["artifact_dir"])
            append_ledger(f"Parallel publication worker finished cleanly for {self.campaign['family_slug']} and synced stable dossier/artifact updates back.")
        else:
            append_ledger(f"Parallel publication worker for {self.campaign['family_slug']} exited nonzero; manager kept the main worktree unchanged.")
        subprocess.run(["git", "worktree", "remove", "--force", str(self.worktree)], cwd=ROOT, check=False)


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

    if worker is not None:
        worker.finish()

    ensure_publication_defaults(status_path)
    if publication_stop_ready(status_path):
        STOP_MARKER.write_text("", encoding="utf-8")
        append_ledger(f"Publication-ready stop marker set after campaign {campaign['family_slug']} reached PAPER_READY.")
    else:
        append_ledger(f"Campaign {campaign['family_slug']} remains active with publication status {status_value(status_path, 'publication_status') or 'NONE'}.")
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


def run_feeder_cycle() -> int:
    if STOP_MARKER.exists():
        append_ledger("Stop marker already exists, so this cycle was skipped.")
        return 0

    if not run_curation_if_needed():
        return 0

    entry = select_queue_entry()
    if entry is None:
        append_ledger("No usable problem was available after curation checks, so this cycle ended cleanly.")
        return 0

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
        return 0

    normalize_candidate_pending_lean(status_path)
    if status_value(status_path, "classification") is None:
        append_ledger(f"Solve infrastructure failure for {entry['slug']}: no usable status verdict was written.")
        rotate_problem_to_end(entry["slug"])
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
        return 0

    ensure_publication_defaults(status_path)
    normalize_candidate_pending_lean(status_path)
    classification = status_value(status_path, "classification")
    verify_verdict = status_value(status_path, "verify_verdict")
    publication_status = status_value(status_path, "publication_status") or "NONE"
    if classification == "REDISCOVERY":
        mark_rediscovery(entry, "Prior-art audit during verify found the exact statement already covered in the literature.")
        return 0
    if verify_verdict is None:
        append_ledger(f"Verify infrastructure failure for {entry['slug']}: no verify verdict was written.")
        rotate_problem_to_end(entry["slug"])
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
        return 0

    run_instance_lean(entry, status_path)
    ensure_publication_defaults(status_path)
    if publication_stop_ready(status_path):
        STOP_MARKER.write_text("", encoding="utf-8")
        append_ledger(f"Publication-ready stop marker set after feeder result {entry['slug']} reached PAPER_READY.")
    return 0


def run_publication_cycle(explicit_campaign: str | None, allow_parallel: bool) -> int:
    if STOP_MARKER.exists():
        append_ledger("Stop marker already exists, so this cycle was skipped.")
        return 0
    if explicit_campaign:
        campaign = find_campaign(explicit_campaign)
        if campaign is None:
            append_ledger(f"Requested campaign {explicit_campaign} was not found, so this cycle ended cleanly.")
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
            max_parallel = int(os.environ.get("AUTOMATH_MAX_PARALLEL_WORKERS", "2"))
            allow_parallel = (not args.worker) and max_parallel > 1
            return run_publication_cycle(args.campaign, allow_parallel)
        return run_feeder_cycle()
    finally:
        append_cycle_log(f"[automath_cycle] {args.mode} cycle finished at {now_str()}.")


if __name__ == "__main__":
    raise SystemExit(main())
