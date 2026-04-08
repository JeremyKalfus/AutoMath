#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"
cd "$ROOT"

if [[ -f "$HOME/.elan/env" ]]; then
  # Make elan-managed Lean and Lake visible for the final stage when available.
  # shellcheck source=/dev/null
  source "$HOME/.elan/env"
fi

CURATION_TIMEOUT=660
SOLVE_TIMEOUT=1200
VERIFY_TIMEOUT=720
LEAN_TIMEOUT=600

mkdir -p "$ROOT/prompts" "$ROOT/artifacts" "$ROOT/artifacts/_logs"
[[ -f "$ROOT/ledger.md" ]] || printf '# Ledger\n' >"$ROOT/ledger.md"
[[ -f "$ROOT/queue.json" ]] || printf '[]\n' >"$ROOT/queue.json"
[[ -f "$ROOT/failed_problems.json" ]] || printf '[]\n' >"$ROOT/failed_problems.json"
[[ -f "$ROOT/selected_problem.md" ]] || printf '# Selected Problem\n\nNo problem selected yet.\n' >"$ROOT/selected_problem.md"

REPORT_TITLE="(none)"
REPORT_SLUG="(none)"
REPORT_OUTCOME="cycle ended before problem selection"
REPORT_LEAN_RAN="no"
REPORT_ARTIFACT_DIR="(none)"
REPORT_STATUS_PATH=""

append_ledger() {
  printf -- "- %s\n" "$1" >>"$ROOT/ledger.md"
}

print_cycle_report() {
  printf '\n=== Cycle Report ===\n'
  printf 'selected title: %s\n' "$REPORT_TITLE"
  printf 'selected slug: %s\n' "$REPORT_SLUG"
  printf 'final outcome: %s\n' "$REPORT_OUTCOME"
  printf 'lean ran: %s\n' "$REPORT_LEAN_RAN"
  printf 'artifact path: %s\n' "$REPORT_ARTIFACT_DIR"
  if [[ -n "$REPORT_STATUS_PATH" && -f "$REPORT_STATUS_PATH" ]]; then
    printf '\n=== status.json ===\n'
    cat "$REPORT_STATUS_PATH"
  fi
  printf '\n=== Ledger Tail ===\n'
  tail -n 30 "$ROOT/ledger.md" || true
}

trap print_cycle_report EXIT

queue_has_usable() {
  python3 - "$ROOT/queue.json" "$ROOT/failed_problems.json" <<'PY'
import json
import sys

queue_path, failed_path = sys.argv[1:3]

def load(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def slug_of(item):
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        return item.get("slug")
    return None

queue = load(queue_path)
failed = {slug for slug in (slug_of(item) for item in load(failed_path)) if slug}
usable = any(
    isinstance(item, dict) and item.get("slug") and item.get("slug") not in failed
    for item in queue
)
print("1" if usable else "0")
PY
}

render_selected_problem() {
  python3 - "$ROOT" <<'PY'
import json
import os
import sys

root = sys.argv[1]

with open(os.path.join(root, "queue.json"), "r", encoding="utf-8") as fh:
    queue = json.load(fh)
with open(os.path.join(root, "failed_problems.json"), "r", encoding="utf-8") as fh:
    failed_raw = json.load(fh)

failed = set()
for item in failed_raw:
    if isinstance(item, str):
        failed.add(item)
    elif isinstance(item, dict) and item.get("slug"):
        failed.add(item["slug"])

selected = None
for item in queue:
    if isinstance(item, dict) and item.get("slug") and item["slug"] not in failed:
        selected = item
        break

if selected is None:
    sys.exit(1)

def add_text(lines, heading, value):
    if value is None:
        return
    text = str(value).strip()
    if not text:
        return
    lines.append(f"## {heading}")
    lines.append(text)
    lines.append("")

lines = [f"# {selected.get('title', 'Untitled Problem')}", ""]
lines.append(f"- slug: `{selected.get('slug', '')}`")
if selected.get("canonical_source"):
    lines.append(f"- canonical_source: {selected['canonical_source']}")
if selected.get("open_status_checked_on"):
    lines.append(f"- open_status_checked_on: {selected['open_status_checked_on']}")
if selected.get("attack_style"):
    lines.append(f"- attack_style: `{selected['attack_style']}`")
if selected.get("curation_confidence"):
    lines.append(f"- curation_confidence: `{selected['curation_confidence']}`")
lines.append("")

add_text(lines, "question", selected.get("question"))
add_text(lines, "canonical_statement", selected.get("canonical_statement"))
add_text(lines, "intended_statement", selected.get("intended_statement"))

definitions = selected.get("definitions") or []
if definitions:
    lines.append("## definitions")
    for item in definitions:
        lines.append(f"- {item}")
    lines.append("")

add_text(lines, "why_reasoning_friendly", selected.get("why_reasoning_friendly"))
add_text(lines, "why_low_token", selected.get("why_low_token"))
add_text(lines, "verifier_hint", selected.get("verifier_hint"))
add_text(lines, "lean_hint", selected.get("lean_hint"))
add_text(lines, "rediscovery_risk", selected.get("rediscovery_risk"))
add_text(lines, "why_still_appears_open", selected.get("why_still_appears_open"))

red_flags = selected.get("red_flags") or []
if red_flags:
    lines.append("## red_flags")
    for item in red_flags:
        lines.append(f"- {item}")
    lines.append("")

selected_path = os.path.join(root, "selected_problem.md")
with open(selected_path, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines).rstrip() + "\n")

print(selected.get("slug", ""))
print(selected.get("title", ""))
PY
}

status_value() {
  python3 - "$1" "$2" <<'PY'
import json
import sys

path, key = sys.argv[1:3]
try:
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
except Exception:
    print("")
    raise SystemExit(0)

value = data.get(key)
if isinstance(value, bool):
    print("true" if value else "false")
elif value is None:
    print("")
else:
    print(value)
PY
}

rotate_problem_to_end() {
  local slug="$1"
  python3 - "$ROOT" "$slug" <<'PY'
import json
import os
import sys

root, slug = sys.argv[1:3]
queue_path = os.path.join(root, "queue.json")

with open(queue_path, "r", encoding="utf-8") as fh:
    queue = json.load(fh)
if not isinstance(queue, list):
    queue = []

picked = None
rest = []
for item in queue:
    if picked is None and isinstance(item, dict) and item.get("slug") == slug:
        picked = item
    else:
        rest.append(item)

if picked is not None:
    rest.append(picked)

with open(queue_path, "w", encoding="utf-8") as fh:
    json.dump(rest, fh, indent=2)
    fh.write("\n")
PY
}

mark_problem_failed() {
  local slug="$1"
  local reason="$2"
  append_ledger "${slug} failed and was moved aside: ${reason}"
  python3 - "$ROOT" "$slug" <<'PY'
import json
import os
import sys

root, slug = sys.argv[1:3]
failed_path = os.path.join(root, "failed_problems.json")
queue_path = os.path.join(root, "queue.json")

with open(failed_path, "r", encoding="utf-8") as fh:
    failed = json.load(fh)
if not isinstance(failed, list):
    failed = []

def slug_of(item):
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        return item.get("slug")
    return None

if slug not in {slug_of(item) for item in failed}:
    failed.append(slug)

with open(queue_path, "r", encoding="utf-8") as fh:
    queue = json.load(fh)
if not isinstance(queue, list):
    queue = []

queue = [item for item in queue if not (isinstance(item, dict) and item.get("slug") == slug)]

with open(failed_path, "w", encoding="utf-8") as fh:
    json.dump(failed, fh, indent=2)
    fh.write("\n")

with open(queue_path, "w", encoding="utf-8") as fh:
    json.dump(queue, fh, indent=2)
    fh.write("\n")
PY
}

mark_problem_rediscovery() {
  local slug="$1"
  local title="$2"
  local notes="$3"
  local checked_on="$4"
  python3 - "$ROOT" "$slug" "$title" "$notes" "$checked_on" <<'PY'
import json
import os
import sys

root, slug, title, notes, checked_on = sys.argv[1:6]
failed_path = os.path.join(root, "failed_problems.json")
queue_path = os.path.join(root, "queue.json")

with open(failed_path, "r", encoding="utf-8") as fh:
    failed = json.load(fh)
if not isinstance(failed, list):
    failed = []

def slug_of(item):
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        return item.get("slug")
    return None

if slug not in {slug_of(item) for item in failed}:
    failed.append(
        {
            "slug": slug,
            "reason": "REDISCOVERY",
            "title": title,
            "notes": notes,
            "checked_on": checked_on,
        }
    )

with open(queue_path, "r", encoding="utf-8") as fh:
    queue = json.load(fh)
if not isinstance(queue, list):
    queue = []

queue = [item for item in queue if not (isinstance(item, dict) and item.get("slug") == slug)]

with open(failed_path, "w", encoding="utf-8") as fh:
    json.dump(failed, fh, indent=2)
    fh.write("\n")

with open(queue_path, "w", encoding="utf-8") as fh:
    json.dump(queue, fh, indent=2)
    fh.write("\n")
PY
}

mark_problem_completed() {
  local slug="$1"
  local title="$2"
  local notes="$3"
  local checked_on="$4"
  python3 - "$ROOT" "$slug" "$title" "$notes" "$checked_on" <<'PY'
import json
import os
import sys

root, slug, title, notes, checked_on = sys.argv[1:6]
failed_path = os.path.join(root, "failed_problems.json")
queue_path = os.path.join(root, "queue.json")

with open(failed_path, "r", encoding="utf-8") as fh:
    failed = json.load(fh)
if not isinstance(failed, list):
    failed = []

def slug_of(item):
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        return item.get("slug")
    return None

if slug not in {slug_of(item) for item in failed}:
    failed.append(
        {
            "slug": slug,
            "reason": "EXACT",
            "title": title,
            "notes": notes,
            "checked_on": checked_on,
        }
    )

with open(queue_path, "r", encoding="utf-8") as fh:
    queue = json.load(fh)
if not isinstance(queue, list):
    queue = []

queue = [item for item in queue if not (isinstance(item, dict) and item.get("slug") == slug)]

with open(failed_path, "w", encoding="utf-8") as fh:
    json.dump(failed, fh, indent=2)
    fh.write("\n")

with open(queue_path, "w", encoding="utf-8") as fh:
    json.dump(queue, fh, indent=2)
    fh.write("\n")
PY
}

normalize_candidate_pending_lean() {
  local status_path="$1"
  python3 - "$status_path" <<'PY'
import json
import os
import sys

path = sys.argv[1]
if not os.path.exists(path):
    raise SystemExit(0)

with open(path, "r", encoding="utf-8") as fh:
    data = json.load(fh)

if data.get("classification") == "EXACT" and not data.get("lean_complete", False):
    data["classification"] = "CANDIDATE"
    if not data.get("next_action"):
        data["next_action"] = "run Lean on the exact intended statement"
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")
PY
}

run_stage() {
  local stage_name="$1"
  local prompt_file="$2"
  local search_mode="$3"
  local timeout_secs="$4"
  local reasoning_effort="${5:-}"
  local transport_profile="${6:-default}"
  python3 - "$ROOT" "$stage_name" "$prompt_file" "$search_mode" "$timeout_secs" "$reasoning_effort" "$transport_profile" <<'PY'
import datetime
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

root, stage_name, prompt_file, search_mode, timeout_secs, reasoning_effort, transport_profile = sys.argv[1:8]
timeout_secs = int(timeout_secs)
root_path = pathlib.Path(root)
logs_dir = root_path / "artifacts" / "_logs"
logs_dir.mkdir(parents=True, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
log_prefix = logs_dir / f"{stamp}_{stage_name}"
stdout_log = pathlib.Path(f"{log_prefix}.stdout.log")
last_message = pathlib.Path(f"{log_prefix}.last.txt")

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
elif stage_name.startswith("verify_"):
    preface += (
        " Use live web only for the bounded rediscovery pass, then return to "
        "skeptical proof checking without further browsing unless absolutely needed."
    )

prompt_text = preface + "\n\n" + pathlib.Path(prompt_file).read_text(encoding="utf-8")
cmd = ["codex"]
if search_mode == "on":
    cmd.append("--search")
cmd.extend(
    [
        "exec",
        "--ephemeral",
        "-C",
        root,
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

env = os.environ.copy()
temp_home = None
if transport_profile == "tuned_openai":
    auth_source = pathlib.Path.home() / ".codex" / "auth.json"
    if auth_source.exists():
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

lean_status_path = None
lean_artifact_dir = None
if stage_name.startswith("lean_"):
    slug = stage_name[len("lean_"):]
    lean_status_path = root_path / "artifacts" / slug / "status.json"
    lean_artifact_dir = root_path / "artifacts" / slug / "lean"


def lean_stage_completed() -> bool:
    if lean_status_path is None or lean_artifact_dir is None:
        return False
    if not lean_status_path.exists() or not lean_artifact_dir.exists():
        return False
    try:
        data = json.loads(lean_status_path.read_text(encoding="utf-8"))
    except Exception:
        return False
    if data.get("classification") != "EXACT" or not data.get("lean_complete", False):
        return False
    return any(lean_artifact_dir.glob("*.lean"))


timed_out = False
returncode = 0
with stdout_log.open("w", encoding="utf-8") as out:
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=out,
        stderr=subprocess.STDOUT,
        text=True,
        env=env,
    )
    assert proc.stdin is not None
    proc.stdin.write(prompt_text)
    proc.stdin.close()

    deadline = time.monotonic() + timeout_secs
    while True:
        returncode = proc.poll()
        if returncode is not None:
            break

        if lean_stage_completed():
            out.write(
                "\n[run_stage detected a completed Lean artifact and ended the worker early]\n"
            )
            out.flush()
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait()
            returncode = 0
            break

        if time.monotonic() >= deadline:
            timed_out = True
            proc.kill()
            proc.wait()
            out.write(f"\n[run_stage timeout after {timeout_secs} seconds]\n")
            returncode = 124
            break

        time.sleep(2)

if temp_home is not None:
    temp_home.cleanup()
sys.exit(returncode)
PY
}

if [[ -f "$ROOT/.stop_harness" ]]; then
  append_ledger "Stop marker already exists, so this cycle was skipped."
  REPORT_OUTCOME="stop marker already existed"
  exit 0
fi

if [[ "$(queue_has_usable)" != "1" ]]; then
  append_ledger "Queue was empty or exhausted, so curation started."
  curation_rc=0
  run_stage "curate" "$ROOT/prompts/curate_batch.prompt.md" "on" "$CURATION_TIMEOUT" "" "default" || curation_rc=$?

  if [[ "$(queue_has_usable)" == "1" ]]; then
    if [[ "$curation_rc" -eq 124 ]]; then
      append_ledger "Curation hit its time budget but still produced a usable queue."
    elif [[ "$curation_rc" -ne 0 ]]; then
      append_ledger "Curation ended oddly but still produced a usable queue."
    fi
  else
    if [[ "$curation_rc" -eq 124 ]]; then
      append_ledger "Curation timed out before producing a usable queue, so this cycle ended cleanly."
      REPORT_OUTCOME="curation timed out without a usable queue"
    elif [[ "$curation_rc" -ne 0 ]]; then
      append_ledger "Curation had an infrastructure failure before producing a usable queue, so this cycle ended cleanly."
      REPORT_OUTCOME="curation infrastructure failure without a usable queue"
    else
      append_ledger "Curation finished without producing a usable queue, so this cycle ended cleanly."
      REPORT_OUTCOME="curation finished without a usable queue"
    fi
    exit 0
  fi
fi

if [[ "$(queue_has_usable)" != "1" ]]; then
  append_ledger "No usable problem was available after curation checks, so this cycle ended cleanly."
  REPORT_OUTCOME="no usable problem after curation checks"
  exit 0
fi

if ! selection_output="$(render_selected_problem)"; then
  append_ledger "A usable queue existed but the selected problem could not be rendered, so this cycle ended cleanly."
  REPORT_OUTCOME="selected problem could not be rendered"
  exit 0
fi

current_slug="$(printf '%s\n' "$selection_output" | sed -n '1p')"
current_title="$(printf '%s\n' "$selection_output" | sed -n '2p')"
if [[ -z "$current_slug" ]]; then
  append_ledger "No active problem could be selected from the queue, so this cycle ended cleanly."
  REPORT_OUTCOME="no active problem could be selected"
  exit 0
fi

REPORT_TITLE="${current_title:-"(untitled)"}"
REPORT_SLUG="$current_slug"
REPORT_ARTIFACT_DIR="$ROOT/artifacts/${current_slug}"
REPORT_STATUS_PATH="$REPORT_ARTIFACT_DIR/status.json"
REPORT_OUTCOME="selected; solve pending"

append_ledger "started solving ${current_slug}"

solve_rc=0
run_stage "solve_${current_slug}" "$ROOT/prompts/solve_reasoning_first.prompt.md" "off" "$SOLVE_TIMEOUT" "high" "tuned_openai" || solve_rc=$?

status_path="$ROOT/artifacts/${current_slug}/status.json"
if [[ "$solve_rc" -ne 0 ]]; then
  if [[ "$solve_rc" -eq 124 ]]; then
    append_ledger "Solve infrastructure failure for ${current_slug}: the worker timed out before a real verdict."
    REPORT_OUTCOME="solve infrastructure timeout"
  else
    append_ledger "Solve infrastructure failure for ${current_slug}: the worker exited unexpectedly."
    REPORT_OUTCOME="solve infrastructure crash"
  fi
  rotate_problem_to_end "$current_slug"
  exit 0
fi

solve_classification="$(status_value "$status_path" "classification")"
if [[ -z "$solve_classification" ]]; then
  append_ledger "Solve infrastructure failure for ${current_slug}: no usable status verdict was written."
  REPORT_OUTCOME="solve infrastructure failure: missing status verdict"
  rotate_problem_to_end "$current_slug"
  exit 0
fi
normalize_candidate_pending_lean "$status_path"

verify_rc=0
run_stage "verify_${current_slug}" "$ROOT/prompts/verify_skeptical.prompt.md" "on" "$VERIFY_TIMEOUT" "" "tuned_openai" || verify_rc=$?

if [[ "$verify_rc" -ne 0 ]]; then
  if [[ "$verify_rc" -eq 124 ]]; then
    append_ledger "Verify infrastructure failure for ${current_slug}: the worker timed out before a real verdict."
    REPORT_OUTCOME="verify infrastructure timeout"
  else
    append_ledger "Verify infrastructure failure for ${current_slug}: the worker exited unexpectedly."
    REPORT_OUTCOME="verify infrastructure crash"
  fi
  rotate_problem_to_end "$current_slug"
  exit 0
fi

verify_verdict="$(status_value "$status_path" "verify_verdict")"
classification="$(status_value "$status_path" "classification")"
lean_ready="$(status_value "$status_path" "lean_ready")"
if [[ -z "$verify_verdict" ]]; then
  append_ledger "Verify infrastructure failure for ${current_slug}: no verify verdict was written."
  REPORT_OUTCOME="verify infrastructure failure: missing verify verdict"
  rotate_problem_to_end "$current_slug"
  exit 0
fi
normalize_candidate_pending_lean "$status_path"
classification="$(status_value "$status_path" "classification")"

if [[ "$classification" == "REDISCOVERY" ]]; then
  current_title="$(status_value "$status_path" "title")"
  append_ledger "${current_slug} was reclassified as REDISCOVERY after the prior-art audit and was moved aside."
  REPORT_OUTCOME="REDISCOVERY"
  mark_problem_rediscovery "$current_slug" "$current_title" "Prior-art audit during verify found the exact statement already covered in the literature." "$(date '+%Y-%m-%d')"
  exit 0
fi

if [[ "$lean_ready" != "true" ]]; then
  REPORT_OUTCOME="${classification:-unknown}/${verify_verdict}"
  mark_problem_failed "$current_slug" "${verify_verdict}"
  exit 0
fi

if ! command -v lake >/dev/null 2>&1; then
  append_ledger "Lean is unavailable on this machine, so Lean was skipped for ${current_slug}."
  normalize_candidate_pending_lean "$status_path"
  REPORT_OUTCOME="CANDIDATE (lean unavailable)"
  rotate_problem_to_end "$current_slug"
  exit 0
fi

lean_rc=0
REPORT_LEAN_RAN="yes"
run_stage "lean_${current_slug}" "$ROOT/prompts/lean.prompt.md" "off" "$LEAN_TIMEOUT" "" "default" || lean_rc=$?

if [[ "$lean_rc" -ne 0 ]]; then
  classification="$(status_value "$status_path" "classification")"
  lean_complete="$(status_value "$status_path" "lean_complete")"
  if [[ "$classification" == "EXACT" && "$lean_complete" == "true" ]]; then
    mark_problem_completed "$current_slug" "$current_title" "Lean verified the exact intended statement in the AutoMath backend; archived to avoid rerunning this solved instance." "$(date '+%Y-%m-%d')"
    : >"$ROOT/.stop_harness"
    append_ledger "Lean completed for ${current_slug} just before the wall-clock cutoff, so the exact result was preserved and the harness stopped."
    REPORT_OUTCOME="EXACT"
    exit 0
  fi
  if [[ "$lean_rc" -eq 124 ]]; then
    append_ledger "Lean infrastructure failure for ${current_slug}: the worker timed out, so the candidate was kept for later."
    REPORT_OUTCOME="lean infrastructure timeout"
  else
    append_ledger "Lean infrastructure failure for ${current_slug}: the worker exited unexpectedly, so the candidate was kept for later."
    REPORT_OUTCOME="lean infrastructure crash"
  fi
  normalize_candidate_pending_lean "$status_path"
  rotate_problem_to_end "$current_slug"
  exit 0
fi

classification="$(status_value "$status_path" "classification")"
lean_complete="$(status_value "$status_path" "lean_complete")"
if [[ "$classification" == "EXACT" && "$lean_complete" == "true" ]]; then
  mark_problem_completed "$current_slug" "$current_title" "Lean verified the exact intended statement in the AutoMath backend; archived to avoid rerunning this solved instance." "$(date '+%Y-%m-%d')"
  : >"$ROOT/.stop_harness"
  append_ledger "Lean verified the exact intended statement for ${current_slug}, so the harness stopped."
  REPORT_OUTCOME="EXACT"
  exit 0
fi

append_ledger "Lean did not finish an exact checked result for ${current_slug}, so the candidate was kept for later."
normalize_candidate_pending_lean "$status_path"
REPORT_OUTCOME="CANDIDATE (lean incomplete)"
rotate_problem_to_end "$current_slug"
