#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"
cd "$ROOT"

SLEEP_SECONDS="${AUTOMATH_SLEEP_SECONDS:-300}"
CYCLE_LOG_PATH="$ROOT/artifacts/_logs/cycle.log"

usage() {
  cat <<'EOF'
Usage: ./run_n_cycles.sh <positive-integer>

Runs AutoMath for a fixed number of publication-first cycles.
`run_once.sh` now defaults to publication mode; exact-instance feeder mode remains available via `./run_feeder_cycle.sh`.
Any `.stop_harness` marker is deferred until the requested cycle count completes.
Set AUTOMATH_SLEEP_SECONDS to override the default 300-second pause between cycles.
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

if [[ $# -ne 1 || ! "$1" =~ ^[1-9][0-9]*$ ]]; then
  usage >&2
  exit 1
fi

TARGET_CYCLES="$1"

mkdir -p "$ROOT/artifacts" "$ROOT/artifacts/_logs"
[[ -f "$ROOT/ledger.md" ]] || printf '# Ledger\n' >"$ROOT/ledger.md"

append_ledger() {
  printf -- "- %s\n" "$1" >>"$ROOT/ledger.md"
}

append_cycle_log() {
  printf -- "%s\n" "$1" | tee -a "$CYCLE_LOG_PATH"
}

completed_cycles=0
deferred_stop_marker=0
while (( completed_cycles < TARGET_CYCLES )); do
  cycle_number=$((completed_cycles + 1))
  if [[ -f "$ROOT/.stop_harness" ]]; then
    rm -f "$ROOT/.stop_harness"
    deferred_stop_marker=1
    message="bounded publication run deferred an existing stop marker before cycle ${cycle_number}/${TARGET_CYCLES} so the requested run could continue."
    append_ledger "$message"
    append_cycle_log "[run_n_cycles] $message"
  fi

  cycle_started_at="$(date '+%Y-%m-%d %H:%M:%S %Z')"
  message="bounded publication run cycle ${cycle_number}/${TARGET_CYCLES} started at ${cycle_started_at}."
  append_ledger "$message"
  append_cycle_log "[run_n_cycles] $message"
  if ./run_once.sh; then
    message="bounded publication run cycle ${cycle_number}/${TARGET_CYCLES} finished at $(date '+%Y-%m-%d %H:%M:%S %Z')."
    append_ledger "$message"
    append_cycle_log "[run_n_cycles] $message"
  else
    message="bounded publication run cycle ${cycle_number}/${TARGET_CYCLES} ended with an error at $(date '+%Y-%m-%d %H:%M:%S %Z')."
    append_ledger "$message"
    append_cycle_log "[run_n_cycles] $message"
  fi

  if [[ -f "$ROOT/.stop_harness" ]]; then
    rm -f "$ROOT/.stop_harness"
    deferred_stop_marker=1
    message="bounded publication run deferred a stop marker raised during cycle ${cycle_number}/${TARGET_CYCLES} until the requested run completes."
    append_ledger "$message"
    append_cycle_log "[run_n_cycles] $message"
  fi

  completed_cycles=$cycle_number

  if (( completed_cycles < TARGET_CYCLES )); then
    message="cycle sleeping for ${SLEEP_SECONDS} seconds."
    append_ledger "$message"
    append_cycle_log "[run_n_cycles] $message"
    sleep "$SLEEP_SECONDS"
  fi
done

message="bounded publication run completed ${completed_cycles}/${TARGET_CYCLES} requested cycle(s)."
append_ledger "$message"
append_cycle_log "[run_n_cycles] $message"
if (( deferred_stop_marker == 1 )); then
  : >"$ROOT/.stop_harness"
  message="bounded publication run restored the deferred stop marker after completing ${completed_cycles}/${TARGET_CYCLES} requested cycle(s)."
  append_ledger "$message"
  append_cycle_log "[run_n_cycles] $message"
fi
