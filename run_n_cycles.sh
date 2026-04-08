#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"
cd "$ROOT"

SLEEP_SECONDS=300

usage() {
  cat <<'EOF'
Usage: ./run_n_cycles.sh <positive-integer>

Runs AutoMath for a fixed number of cycles, stopping early if .stop_harness appears.
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

completed_cycles=0
while (( completed_cycles < TARGET_CYCLES )) && [[ ! -f "$ROOT/.stop_harness" ]]; do
  cycle_number=$((completed_cycles + 1))
  append_ledger "bounded run cycle ${cycle_number}/${TARGET_CYCLES} started at $(date '+%Y-%m-%d %H:%M:%S %Z')."
  if ./run_once.sh; then
    append_ledger "bounded run cycle ${cycle_number}/${TARGET_CYCLES} finished at $(date '+%Y-%m-%d %H:%M:%S %Z')."
  else
    append_ledger "bounded run cycle ${cycle_number}/${TARGET_CYCLES} ended with an error at $(date '+%Y-%m-%d %H:%M:%S %Z')."
  fi

  completed_cycles=$cycle_number
  [[ -f "$ROOT/.stop_harness" ]] && break

  if (( completed_cycles < TARGET_CYCLES )); then
    append_ledger "cycle sleeping for ${SLEEP_SECONDS} seconds."
    sleep "$SLEEP_SECONDS"
  fi
done

if [[ -f "$ROOT/.stop_harness" ]]; then
  append_ledger "bounded run stopped early after ${completed_cycles} cycle(s) because the harness stop marker exists."
else
  append_ledger "bounded run completed ${completed_cycles}/${TARGET_CYCLES} requested cycle(s)."
fi
