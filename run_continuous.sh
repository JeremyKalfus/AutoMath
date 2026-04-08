#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"
cd "$ROOT"

mkdir -p "$ROOT/artifacts" "$ROOT/artifacts/_logs"
[[ -f "$ROOT/ledger.md" ]] || printf '# Ledger\n' >"$ROOT/ledger.md"

append_ledger() {
  printf -- "- %s\n" "$1" >>"$ROOT/ledger.md"
}

while [[ ! -f "$ROOT/.stop_harness" ]]; do
  append_ledger "cycle started at $(date '+%Y-%m-%d %H:%M:%S %Z')."
  if ./run_once.sh; then
    append_ledger "cycle finished at $(date '+%Y-%m-%d %H:%M:%S %Z')."
  else
    append_ledger "cycle ended with an error at $(date '+%Y-%m-%d %H:%M:%S %Z')."
  fi
  [[ -f "$ROOT/.stop_harness" ]] && break
  append_ledger "cycle sleeping for 300 seconds."
  sleep 300
done
