#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"
cd "$ROOT"

CYCLE_LOG_PATH="$ROOT/artifacts/_logs/lean_queue_cycle.log"
STOP_MARKER="$ROOT/.stop_lean_queue"
SLEEP_SECONDS="${AUTOMATH_LEAN_SLEEP_SECONDS:-300}"

mkdir -p "$ROOT/artifacts" "$ROOT/artifacts/_logs"
[[ -f "$ROOT/ledger.md" ]] || printf '# Ledger\n' >"$ROOT/ledger.md"

append_ledger() {
  printf -- "- %s\n" "$1" >>"$ROOT/ledger.md"
}

append_cycle_log() {
  printf -- "%s\n" "$1" | tee -a "$CYCLE_LOG_PATH"
}

while [[ ! -f "$STOP_MARKER" ]]; do
  message="lean-queue cycle started at $(date '+%Y-%m-%d %H:%M:%S %Z')."
  append_ledger "$message"
  append_cycle_log "[run_lean_queue] $message"
  if ./run_lean_queue_once.sh; then
    message="lean-queue cycle finished at $(date '+%Y-%m-%d %H:%M:%S %Z')."
    append_ledger "$message"
    append_cycle_log "[run_lean_queue] $message"
  else
    message="lean-queue cycle ended with an error at $(date '+%Y-%m-%d %H:%M:%S %Z')."
    append_ledger "$message"
    append_cycle_log "[run_lean_queue] $message"
  fi
  if [[ -f "$STOP_MARKER" ]]; then
    append_cycle_log "[run_lean_queue] stop marker detected after the lean-queue cycle; stopping the continuous runner."
    break
  fi
  message="lean-queue cycle sleeping for ${SLEEP_SECONDS} seconds."
  append_ledger "$message"
  append_cycle_log "[run_lean_queue] $message"
  sleep "$SLEEP_SECONDS"
done
