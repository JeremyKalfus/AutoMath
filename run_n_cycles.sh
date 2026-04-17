#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"
cd "$ROOT"

usage() {
  cat <<'EOF'
Usage: ./run_n_cycles.sh [--verbose|-v] <positive-integer> [automath_cycle args...]

Runs AutoMath for a fixed number of publication-first cycles through the
authoritative publication supervisor.
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

SUPERVISOR_ARGS=()
TARGET_CYCLES=""
CHILD_ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --verbose|-v)
      SUPERVISOR_ARGS+=("$1")
      shift
      ;;
    --)
      shift
      CHILD_ARGS+=("$@")
      break
      ;;
    *)
      if [[ -z "$TARGET_CYCLES" ]]; then
        TARGET_CYCLES="$1"
      else
        CHILD_ARGS+=("$1")
      fi
      shift
      ;;
  esac
done

if [[ -z "$TARGET_CYCLES" || ! "$TARGET_CYCLES" =~ ^[1-9][0-9]*$ ]]; then
  usage >&2
  exit 1
fi

if ((${#SUPERVISOR_ARGS[@]})) && ((${#CHILD_ARGS[@]})); then
  exec python3 "$ROOT/scripts/publication_supervisor.py" --mode n-cycles --cycles "$TARGET_CYCLES" "${SUPERVISOR_ARGS[@]}" -- "${CHILD_ARGS[@]}"
elif ((${#SUPERVISOR_ARGS[@]})); then
  exec python3 "$ROOT/scripts/publication_supervisor.py" --mode n-cycles --cycles "$TARGET_CYCLES" "${SUPERVISOR_ARGS[@]}" --
elif ((${#CHILD_ARGS[@]})); then
  exec python3 "$ROOT/scripts/publication_supervisor.py" --mode n-cycles --cycles "$TARGET_CYCLES" -- "${CHILD_ARGS[@]}"
else
  exec python3 "$ROOT/scripts/publication_supervisor.py" --mode n-cycles --cycles "$TARGET_CYCLES" --
fi
