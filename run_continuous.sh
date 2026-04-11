#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"
cd "$ROOT"

CYCLE_LOG_PATH="$ROOT/artifacts/_logs/cycle.log"
SLEEP_SECONDS="${AUTOMATH_SLEEP_SECONDS:-60}"

mkdir -p "$ROOT/artifacts" "$ROOT/artifacts/_logs"
[[ -f "$ROOT/ledger.md" ]] || printf '# Ledger\n' >"$ROOT/ledger.md"

append_ledger() {
  printf -- "- %s\n" "$1" >>"$ROOT/ledger.md"
}

append_cycle_log() {
  printf -- "%s\n" "$1" | tee -a "$CYCLE_LOG_PATH"
}

while [[ ! -f "$ROOT/.stop_harness" ]]; do
  message="publication cycle started at $(date '+%Y-%m-%d %H:%M:%S %Z')."
  append_ledger "$message"
  append_cycle_log "[run_continuous] $message"
  if ./run_once.sh; then
    message="publication cycle finished at $(date '+%Y-%m-%d %H:%M:%S %Z')."
    append_ledger "$message"
    append_cycle_log "[run_continuous] $message"
  else
    message="publication cycle ended with an error at $(date '+%Y-%m-%d %H:%M:%S %Z')."
    append_ledger "$message"
    append_cycle_log "[run_continuous] $message"
  fi
  if [[ -f "$ROOT/.stop_harness" ]]; then
    append_cycle_log "[run_continuous] stop marker detected after the publication cycle; stopping the continuous runner."
    break
  fi
  message="publication cycle sleeping for ${SLEEP_SECONDS} seconds."
  append_ledger "$message"
  append_cycle_log "[run_continuous] $message"
  sleep "$SLEEP_SECONDS"
done
