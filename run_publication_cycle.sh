#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"
cd "$ROOT"

if [[ -f "$HOME/.elan/env" ]]; then
  # shellcheck source=/dev/null
  source "$HOME/.elan/env"
fi

python3 "$ROOT/scripts/automath_cycle.py" --mode publication "$@"

