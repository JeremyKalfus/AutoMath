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

monitor_artifact_slugs() {
  local base="$1"
  python3 - "$base" <<'PY'
import json
import re
import sys
from pathlib import Path

base = Path(sys.argv[1])
seen = set()


def emit(slug):
    if not slug or slug in seen:
        return
    seen.add(slug)
    print(slug)


manifest = base / "campaigns" / "manifest.json"
if manifest.exists():
    try:
        data = json.loads(manifest.read_text())
    except Exception:
        data = []
    if isinstance(data, list):
        for campaign in data:
            if not isinstance(campaign, dict):
                continue
            for slug in campaign.get("seed_instances", []):
                emit(slug)

queue_path = base / "queue.json"
if queue_path.exists():
    try:
        queue = json.loads(queue_path.read_text())
    except Exception:
        queue = []
    if isinstance(queue, list):
        for item in queue:
            if not isinstance(item, dict):
                continue
            if item.get("entry_type") in {"paper_candidate", "feeder_instance"}:
                emit(item.get("slug"))
            for key in ["seed_instances", "next_feeder_instances"]:
                for slug in item.get(key, []):
                    emit(slug)

selected = base / "selected_problem.md"
if selected.exists():
    text = selected.read_text()
    match = re.search(r"^- slug: `([^`]+)`", text, flags=re.M)
    if match:
        slug = match.group(1)
        if not slug.startswith("family-"):
            emit(slug)
    for block_key in ["seed_instances", "next_feeder_instances"]:
        block = re.search(rf"^## {re.escape(block_key)}\n((?:- .+\n)*)", text, flags=re.M)
        if block:
            for line in block.group(1).splitlines():
                if line.startswith("- "):
                    emit(line[2:].strip())
PY
}

seed_monitor_checkout() {
  local items=(
    AGENTS.md
    ONE_SHOT_PUBLICATION_REDESIGN_PLAN.md
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
  done < <(monitor_artifact_slugs "$ROOT")
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

  while IFS= read -r slug; do
    [[ -n "$slug" ]] || continue
    sync_item "$WORKTREE/artifacts/$slug" "$ROOT/artifacts/$slug"
  done < <(monitor_artifact_slugs "$WORKTREE")
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
  AUTOMATH_MAX_PARALLEL_WORKERS="${AUTOMATH_MAX_PARALLEL_WORKERS:-5}" ./run_publication_cycle.sh
)

sync_monitor_results_back

printf 'Publication monitor cycle complete.\n'
printf 'Summary: %s\n' "$ROOT/artifacts/families/summary.md"
