#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/automath-supervisor.XXXXXX")"
SOAK_CYCLES="${AUTOMATH_SUPERVISOR_SOAK_CYCLES:-5}"

cleanup() {
  rm -rf "$TMP"
}
trap cleanup EXIT

STUB="$TMP/heartbeat_stub.py"
cat >"$STUB" <<'PY'
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import tempfile
import time


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat()


def write_json_atomic(path: pathlib.Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as tmp:
        tmp.write(json.dumps(payload, indent=2) + "\n")
        tmp.flush()
        os.fsync(tmp.fileno())
        tmp_path = pathlib.Path(tmp.name)
    os.replace(tmp_path, path)


def build_heartbeat(stage: str, state: str) -> dict:
    pid = os.getpid()
    return {
        "run_id": os.environ.get("AUTOMATH_RUN_ID"),
        "cycle_id": os.environ.get("AUTOMATH_CYCLE_ID"),
        "state": state,
        "stage": stage,
        "active_slug": None,
        "manager_pid": pid,
        "manager_pgid": os.getpgid(0),
        "stage_child_pid": pid,
        "stage_child_pgid": os.getpgid(0),
        "stdout_log": None,
        "last_heartbeat_at": now_iso(),
        "last_stdout_mtime": None,
        "active_workers": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["healthy", "wedge"], required=True)
    parser.add_argument("--stage", default="stub_stage")
    parser.add_argument("--duration", type=float, default=3.0)
    parser.add_argument("--interval", type=float, default=0.4)
    args = parser.parse_args()

    heartbeat_path = pathlib.Path(os.environ["AUTOMATH_HEARTBEAT_PATH"])
    if args.mode == "healthy":
        deadline = time.monotonic() + args.duration
        while time.monotonic() < deadline:
            write_json_atomic(heartbeat_path, build_heartbeat(args.stage, "stage_running"))
            time.sleep(args.interval)
        write_json_atomic(heartbeat_path, build_heartbeat(args.stage, "stage_finished"))
        return 0

    write_json_atomic(heartbeat_path, build_heartbeat(args.stage, "stage_running"))
    time.sleep(args.duration)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
PY
chmod +x "$STUB"

setup_case() {
  local case_dir="$1"
  rm -rf "$case_dir"
  mkdir -p "$case_dir/artifacts/_runtime/main_publication" "$case_dir/artifacts/_logs/stalls"
}

run_supervisor_case() {
  local case_dir="$1"
  local child_cmd="$2"
  shift 2
  (
    export AUTOMATH_ARTIFACTS_ROOT="$case_dir/artifacts"
    export AUTOMATH_LOGS_ROOT="$case_dir/artifacts/_logs"
    export AUTOMATH_RUNTIME_ROOT="$case_dir/artifacts/_runtime/main_publication"
    export AUTOMATH_LEASE_PATH="$case_dir/artifacts/_runtime/main_publication/lease.json"
    export AUTOMATH_LEASE_LOCK_PATH="$case_dir/artifacts/_runtime/main_publication/lease.lock"
    export AUTOMATH_HEARTBEAT_PATH="$case_dir/artifacts/_runtime/main_publication/heartbeat.json"
    export AUTOMATH_EVENTS_PATH="$case_dir/artifacts/_logs/events.jsonl"
    export AUTOMATH_STALLS_DIR="$case_dir/artifacts/_logs/stalls"
    export AUTOMATH_RUNNER_HEARTBEAT_SECS=1
    export AUTOMATH_RUNNER_STALE_LEASE_SECS=2
    export AUTOMATH_RUNNER_STALL_SECS=2
    export AUTOMATH_RUNNER_KILL_GRACE_SECS=1
    export AUTOMATH_ENABLE_STOP_HARNESS=0
    export AUTOMATH_SLEEP_SECONDS=0
    export AUTOMATH_SUPERVISOR_CHILD_CMD="$child_cmd"
    python3 "$ROOT/scripts/publication_supervisor.py" "$@"
  ) >"$case_dir/stdout.log" 2>"$case_dir/stderr.log"
}

assert_event() {
  local events_path="$1"
  local event_name="$2"
  python3 - "$events_path" "$event_name" <<'PY'
import json
import pathlib
import sys

events_path = pathlib.Path(sys.argv[1])
event_name = sys.argv[2]
rows = []
if events_path.exists():
    rows = [json.loads(line) for line in events_path.read_text().splitlines() if line.strip()]
if not any(row.get("event") == event_name for row in rows):
    raise SystemExit(f"missing event {event_name} in {events_path}")
PY
}

assert_no_stalls() {
  local stalls_dir="$1"
  if find "$stalls_dir" -type f -name '*.json' -print -quit | grep -q .; then
    echo "unexpected stall salvage in $stalls_dir" >&2
    return 1
  fi
}

assert_has_stall() {
  local stalls_dir="$1"
  if ! find "$stalls_dir" -type f -name '*.json' -print -quit | grep -q .; then
    echo "expected stall salvage in $stalls_dir" >&2
    return 1
  fi
}

assert_cycle_terminals() {
  local events_path="$1"
  python3 - "$events_path" <<'PY'
import json
import pathlib
import sys
from collections import defaultdict

events_path = pathlib.Path(sys.argv[1])
rows = [json.loads(line) for line in events_path.read_text().splitlines() if line.strip()]
started = defaultdict(int)
terminal = defaultdict(int)
for row in rows:
    cycle_id = row.get("cycle_id")
    if not cycle_id:
        continue
    event = row.get("event")
    if event == "cycle_started":
        started[cycle_id] += 1
    if event in {"cycle_finished", "cycle_errored", "cycle_stalled"}:
        terminal[cycle_id] += 1
for cycle_id, count in started.items():
    if count != 1:
        raise SystemExit(f"cycle {cycle_id} has {count} cycle_started events")
    if terminal[cycle_id] != 1:
        raise SystemExit(f"cycle {cycle_id} has {terminal[cycle_id]} terminal events")
PY
}

seed_stale_lease() {
  local case_dir="$1"
  python3 - "$case_dir" <<'PY'
import datetime as dt
import json
import pathlib
import sys

case_dir = pathlib.Path(sys.argv[1])
runtime = case_dir / "artifacts" / "_runtime" / "main_publication"
runtime.mkdir(parents=True, exist_ok=True)
old = (dt.datetime.now().astimezone() - dt.timedelta(seconds=30)).isoformat()
lease = {
    "run_id": "stale-run",
    "pid": 999999,
    "pgid": 999999,
    "started_at": old,
    "last_heartbeat_at": old,
    "mode": "continuous",
    "cwd": str(case_dir),
}
(runtime / "lease.json").write_text(json.dumps(lease, indent=2) + "\n", encoding="utf-8")
(runtime / "lease.lock").write_text("stale\n", encoding="utf-8")
(runtime / "heartbeat.json").write_text(json.dumps({"last_heartbeat_at": old}, indent=2) + "\n", encoding="utf-8")
PY
}

case_live="$TMP/live_refusal"
setup_case "$case_live"
(
  run_supervisor_case "$case_live" "python3 '$STUB' --mode healthy --stage single_flight_stub --duration 4" --mode once
) &
FIRST_PID=$!
sleep 1
set +e
run_supervisor_case "$case_live" "python3 '$STUB' --mode healthy --stage second_runner_stub --duration 1" --mode once
RC=$?
set -e
if [[ "$RC" -eq 0 ]]; then
  echo "expected second runner to fail fast on live lease" >&2
  exit 1
fi
wait "$FIRST_PID"
assert_event "$case_live/artifacts/_logs/events.jsonl" "lease_refused"
assert_cycle_terminals "$case_live/artifacts/_logs/events.jsonl"

case_stale="$TMP/stale_reclaim"
setup_case "$case_stale"
seed_stale_lease "$case_stale"
run_supervisor_case "$case_stale" "python3 '$STUB' --mode healthy --stage stale_reclaim_stub --duration 1.5" --mode once
assert_event "$case_stale/artifacts/_logs/events.jsonl" "lease_reclaimed"
assert_event "$case_stale/artifacts/_logs/events.jsonl" "cycle_finished"
assert_cycle_terminals "$case_stale/artifacts/_logs/events.jsonl"
assert_no_stalls "$case_stale/artifacts/_logs/stalls"

case_healthy="$TMP/healthy_heartbeat"
setup_case "$case_healthy"
run_supervisor_case "$case_healthy" "python3 '$STUB' --mode healthy --stage healthy_stub --duration 2.5" --mode once
assert_event "$case_healthy/artifacts/_logs/events.jsonl" "lease_acquired"
assert_event "$case_healthy/artifacts/_logs/events.jsonl" "cycle_finished"
assert_cycle_terminals "$case_healthy/artifacts/_logs/events.jsonl"
assert_no_stalls "$case_healthy/artifacts/_logs/stalls"

case_wedge="$TMP/forced_wedge"
setup_case "$case_wedge"
set +e
run_supervisor_case "$case_wedge" "python3 '$STUB' --mode wedge --stage wedge_stub --duration 10" --mode once
RC=$?
set -e
if [[ "$RC" -eq 0 ]]; then
  echo "expected forced wedge case to exit nonzero after watchdog kill" >&2
  exit 1
fi
assert_event "$case_wedge/artifacts/_logs/events.jsonl" "cycle_stalled"
assert_event "$case_wedge/artifacts/_logs/events.jsonl" "stage_killed"
assert_cycle_terminals "$case_wedge/artifacts/_logs/events.jsonl"
assert_has_stall "$case_wedge/artifacts/_logs/stalls"

if [[ "$SOAK_CYCLES" =~ ^[1-9][0-9]*$ ]]; then
  case_soak="$TMP/soak"
  setup_case "$case_soak"
  run_supervisor_case "$case_soak" "python3 '$STUB' --mode healthy --stage soak_stub --duration 0.6 --interval 0.2" --mode n-cycles --cycles "$SOAK_CYCLES"
  assert_cycle_terminals "$case_soak/artifacts/_logs/events.jsonl"
fi

printf 'Supervisor watchdog smoke tests passed.\n'
