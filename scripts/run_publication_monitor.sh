#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
WORKTREE_NAME="${AUTOMATH_MONITOR_WORKTREE_NAME:-publication-monitor}"
WORKTREE="$ROOT/.worktrees/$WORKTREE_NAME"

sync_item() {
  local src="$1"
  local dst="$2"
  if [[ ! -e "$src" ]]; then
    return
  fi
  mkdir -p "$(dirname "$dst")"
  if [[ -d "$src" ]]; then
    rm -rf "$dst"
    cp -R "$src" "$dst"
  else
    cp "$src" "$dst"
  fi
}

seed_monitor_checkout() {
  local items=(
    AGENTS.md
    PROOFS.md
    ledger.md
    queue.json
    failed_problems.json
    selected_problem.md
    prompts
    campaigns
    scripts
    run_once.sh
    run_publication_cycle.sh
    run_feeder_cycle.sh
    run_n_cycles.sh
    run_continuous.sh
    lean/AutoMath.lean
    lean/AutoMath
    artifacts/families
  )

  for item in "${items[@]}"; do
    sync_item "$ROOT/$item" "$WORKTREE/$item"
  done

  while IFS= read -r slug; do
    [[ -n "$slug" ]] || continue
    sync_item "$ROOT/artifacts/$slug" "$WORKTREE/artifacts/$slug"
  done < <(
    python3 - <<'PY'
import json
from pathlib import Path

manifest = Path("campaigns/manifest.json")
if manifest.exists():
    data = json.loads(manifest.read_text())
    seen = set()
    for campaign in data:
        for slug in campaign.get("seed_instances", []):
            if slug not in seen:
                print(slug)
                seen.add(slug)
PY
  )
}

sync_monitor_results_back() {
  local items=(
    ledger.md
    queue.json
    selected_problem.md
    PROOFS.md
    campaigns
    artifacts/families
    artifacts/_logs/cycle.log
    artifacts/_logs/codex_capabilities.json
  )

  for item in "${items[@]}"; do
    sync_item "$WORKTREE/$item" "$ROOT/$item"
  done
}

if ! git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf 'run_publication_monitor.sh requires a git worktree-capable repository.\n' >&2
  exit 1
fi

mkdir -p "$ROOT/.worktrees"
if [[ ! -e "$WORKTREE/.git" && ! -f "$WORKTREE/.git" ]]; then
  git -C "$ROOT" worktree add --detach "$WORKTREE" HEAD >/dev/null
fi

seed_monitor_checkout

(
  cd "$WORKTREE"
  AUTOMATH_MAX_PARALLEL_WORKERS="${AUTOMATH_MAX_PARALLEL_WORKERS:-3}" ./run_publication_cycle.sh
)

sync_monitor_results_back

printf 'Publication monitor cycle complete.\n'
printf 'Summary: %s\n' "$ROOT/artifacts/families/summary.md"
