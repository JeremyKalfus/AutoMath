# Project context
You are working in AutoMath, an automated method for finding niche open math problems and turning the smallest frontier-novel claims into publishable papers.

# Goal

The main objective is one-shot publication mode under the MICRO-PAPER objective.

Plain-English version:

- look for something super easy and niche where simple work on one exact claim would already yield a paper
- equivalently, find the smallest frontier claim where a single strong solve is already 70-90% of a paper
- prefer exact theorem/result pairs, sharp obstructions, minimal counterexamples, and tiny structural lemmas with immediate applications
- optimize for paper leverage rather than microscopic statement size
- heavily downrank any target that needs a feeder ladder, broad campaign buildup, or expensive post-solve packaging before becoming paper-shaped
- primary publication success is now entry into `lean_queue.json`: solve is done, verification is `VERIFIED`, significance is `PAPER_READY`, proof artifacts are preserved, and Lean is the only remaining gate
- Lean-complete `EXACT` is a second-tier formal seal, not the only kind of success

AutoMath is now a strict micro-paper lane only.
The active harness is exactly five stages: `curate`, `solve`, `verify`, `publication_audit`, and `lean`.

# Repo layout

- `ledger.md`: append-only human-readable log of what the harness did.
- `queue.json`: current batch of exactly 5 curated dossiers. Every live queue entry should be a `paper_candidate`.
- `failed_problems.json`: problems that failed, rediscoveries, archived exacts, and other do-not-recur memory.
- `lean_queue.json`: packets where solve, verification, significance audit, and artifact preservation are done; Lean is the only remaining gate.
- `lean_complete.json`: definitive list of publication-significant proofs AutoMath has found and proved in Lean.
- `archive/PROOFS.legacy.md` and `archive/lean_complete.instance_only_legacy.json`: historical Lean-complete exact-instance inventory; preserved for memory, not used as the current significant-proof registry.
- `selected_problem.md`: the currently active queue entry.
- `memory/`: thin canonical memory surfaces, especially `paper_memory.json` for near-paper packets and `search_memory.json` for attempted/rejected targets.
- `prompts/`: stage prompts for `curate`, `solve`, `verify`, `publication_audit`, and `lean`.
- `artifacts/<slug>/`: per-candidate work files.
- `lean/`: the official AutoMath Lean backend.
- `run_once.sh`: one publication-oriented cycle by default.
- `run_n_cycles.sh`: bounded repeated cycles.
- `run_continuous.sh`: repeated cycles until stopped.
- `run_lean_queue_once.sh`: one non-blocking Lean-queue cycle over `lean_queue.json`.
- `run_lean_queue_continuous.sh`: repeated Lean-queue cycles until stopped.

# Workflow

AutoMath now has 5 conceptual stages:

1. `curate`
2. `solve`
3. `verify`
4. `publication_audit`
5. `lean`

One-shot publication rules:

1. Every live run targets a `paper_candidate`.
2. In plain terms, prefer the smallest honest target where one clean solve would already read like the title theorem of a short paper.
3. Curation must optimize for `solve -> publication distance`, not just solve difficulty.
4. Any target that needs a feeder ladder before becoming paper-shaped should be downranked hard.
5. Use `publication_audit` to decide whether the strongest honest claim is instance-only, slice-level, rediscovered, or genuinely paper-ready.
6. The manager may run up to 2 concurrent solve workers on distinct queued `paper_candidate` slugs; solve is the only parallelized stage in the live harness.
7. The default solve budget is 45 minutes per candidate unless `AUTOMATH_SOLVE_TIMEOUT` is overridden explicitly.
8. Use Lean as a secondary formal-seal lane fed by `lean_queue.json`; do not let formalization overhead dominate early selection or block fresh curation/solve work.
9. `EXACT` alone is not a publication success condition; the solve must also be paper-shaped enough to audit as `PAPER_READY`.
10. Packets in `lean_queue.json` must leave the main queue and fresh discovery must continue even if Lean is still pending.
11. A Lean-complete `EXACT` result is the formal-seal tier, not the only tier that counts as a success.
12. If verification finds rediscovery, archive it and do not treat it as a frontier success.
13. No automatic fallbacks: if a chosen path fails, do not silently switch into campaign-building, feeder-ladder work, or another conceptually different lane. Record the blocker, preserve useful artifacts, and continue only through the same one-shot lane.
14. Infrastructure failures are not mathematical failures: salvage partial artifacts, cool the slug down, and do not archive it as though the theorem failed.

Parallel policy:

- One manager thread/worktree orchestrates the run.
- The manager may launch up to 2 isolated solve workers concurrently on distinct queued paper candidates.
- `verify` and `publication_audit` remain manager-serial even when solve runs in parallel.
- `lean` runs from `lean_queue.json` as a non-blocking secondary lane and should not prevent fresh curation/solve work.
- Use isolated workers only for narrowly scoped paper-candidate tasks with strict context budgets and clear write ownership.
- Merge back only stable dossier and artifact updates.
- Allowed narrow worker roles are:
  - `curation-scout`
  - `novelty-scout`
  - `solver-A`
  - `solver-B`
  - `packet-auditor`
- Do not ask a worker to absorb the whole repo or wander across unrelated dossiers.
- Every worker should receive a short handoff memo containing:
  - exact statement
  - why publishable if solved
  - allowed files
  - stop condition
  - output path
- Default worker context budget:
  - 1 candidate
  - at most 1 dossier
  - target 3 to 6 source files
  - 1 explicit output file pair
- Write ownership:
  - the manager owns canonical queue files and canonical `record.md` / `status.json`
  - parallel solve workers may write only candidate-local canonical solve artifacts for their assigned slug plus candidate-local helper files
  - sidecar solve workers, when used, write only candidate-local sidecar attempt artifacts
  - packet-auditor workers write only publication-packet sidecar artifacts
  - the manager alone decides whether a sidecar output is strong enough to absorb

# Core rules

- Reasoning first, code second.
- No silent fallbacks. If the intended path fails, stop that path, record the blocker, preserve useful artifacts, and do not automatically switch to a conceptually different mode.
- No unapproved concept drift. Do not make large objective-changing decisions beyond the user-specified one-shot-publication redesign without explicitly informing the user first.
- Harness classifications:
  - `NEW`
  - `UNSUITED`
  - `FAILED`
  - `PARTIAL`
  - `VARIANT`
  - `CANDIDATE`
  - `EXACT`
  - `COUNTEREXAMPLE`
  - `REDISCOVERY`
- Separate publication-facing status:
  - `NONE`
  - `INSTANCE_ONLY`
  - `REDISCOVERY`
  - `SLICE_CANDIDATE`
  - `SLICE_EXACT`
- `PAPER_READY`
- Candidate selection should strongly prefer:
  - exact theorem/result pairs,
  - sharp obstruction theorems,
  - minimal counterexamples,
  - tiny structural lemmas with immediate applications,
  - narrow claims with cheap rediscovery surfaces,
  - targets where one solve plausibly supplies the title theorem of a short paper.
- Candidate selection should strongly penalize:
  - feeder ladders,
  - broad theorem programs with expensive packaging,
  - mathematically easy instances that are still far from publication after the solve,
  - targets with high novelty-check cost or high formalization overhead,
  - tiny exact curiosities with weak paper narrative,
  - unresolved broader-theorem implication risk,
  - search-heavy targets unless only a tiny human-readable residue remains.
- Every `paper_candidate` should expose explicit micro-paper fields:
  - `paper_leverage_score`
  - `single_solve_to_paper_fraction`
  - `title_theorem_strength`
  - `family_anchor_strength`
  - `publication_narrative_strength`
  - `editorial_overhead`
  - `immediate_corollary_headroom`
  - `isolated_exact_case_risk`
  - `broader_theorem_implication_risk`
  - `search_heavy`
  - `certificate_compactness`
  - `transfer_kit_present`
  - `exact_gap_from_source`
  - `micro_paper_lane_eligible`
- Unknown on any load-bearing micro-paper field should default to FAIL the micro-paper lane until refreshed.
- Every micro-paper candidate must carry a transfer kit:
  - 2 to 4 usable lemmas or proof ingredients from the source literature
  - 1 toy worked example or smallest nontrivial instance
  - 1 known obstruction or failure mode
  - 1 exact sentence saying where prior work stops
  - 1 recommended first proof attack
  - 1 sentence explaining what the paper would look like if solved
- `EXACT` is reserved for an exact intended statement or exact intended disproof fully checked in Lean.
- Before Lean completes, the strongest positive proof classification is `CANDIDATE`.
- A non-Lean explicit disproof may still be labeled `COUNTEREXAMPLE`, but it does not stop the harness on its own.
- A Lean-backed exact instance may still have `publication_status = INSTANCE_ONLY`.
- `PAPER_READY` is the significance tier: the strongest honest claim already looks publishable on human mathematical standards even if Lean is still pending.
- `REDISCOVERY` means the exact intended statement is already solved or directly implied in prior art; it never counts as a frontier-novel publication win.
- Do not start solve with SAT, ILP, CP-SAT, brute force, or generic optimization unless the problem is explicitly marked `search-heavy` or two reasoning strategies have already failed.
- Before any nontrivial code, write the reasoning section in the relevant `record.md`.
- Minimal code only: checker, falsifier, tiny experiment, witness verification, or later exact search justified by the reasoning stage.
- Verification begins with a bounded rediscovery / prior-art search before proof checking.
- Curation must explicitly downrank likely rediscoveries, search-heavy targets, feeder-ladder targets, and any target whose solve still leaves a long path to publication.
- If a specific instance is extracted from a broader open family, curation must check whether an earlier theorem, proposition, example, observation, corollary, or sufficient condition already settles that exact instance.
- Solve runs with web disabled. Verification and publication audit may use limited web for bounded prior-art checking.
- Be conservative about claim types and theorem scope.
- Keep the ledger updated in plain English.
- Discard worker outputs that do not honestly shorten solve-to-publication distance.
- Prefer thin memory surfaces over replaying large ledgers when orienting future runs.
