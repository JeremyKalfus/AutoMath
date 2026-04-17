#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"
cd "$ROOT"

SUPERVISOR_ARGS=()
CHILD_ARGS=()

for arg in "$@"; do
  case "$arg" in
    --verbose|-v) SUPERVISOR_ARGS+=("$arg") ;;
    *) CHILD_ARGS+=("$arg") ;;
  esac
done

if ((${#SUPERVISOR_ARGS[@]})) && ((${#CHILD_ARGS[@]})); then
  exec python3 "$ROOT/scripts/publication_supervisor.py" --mode continuous "${SUPERVISOR_ARGS[@]}" -- "${CHILD_ARGS[@]}"
elif ((${#SUPERVISOR_ARGS[@]})); then
  exec python3 "$ROOT/scripts/publication_supervisor.py" --mode continuous "${SUPERVISOR_ARGS[@]}" --
elif ((${#CHILD_ARGS[@]})); then
  exec python3 "$ROOT/scripts/publication_supervisor.py" --mode continuous -- "${CHILD_ARGS[@]}"
else
  exec python3 "$ROOT/scripts/publication_supervisor.py" --mode continuous --
fi
