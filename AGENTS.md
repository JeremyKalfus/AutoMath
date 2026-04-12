# Project context
You are working in AutoMath, an automated method for finding niche open math problems and turning the smallest frontier claims into publishable papers.

# Goal

The main objective is now one-shot publication mode:

- find the smallest frontier claim where a single strong solve is already 70-90% of a paper
- prefer exact theorem/result pairs, sharp obstructions, minimal counterexamples, and tiny structural lemmas with immediate applications
- heavily downrank any target that needs a feeder ladder, broad campaign buildup, or expensive post-solve packaging before becoming paper-shaped
- stop automatically only when the strongest honest claim reaches `publication_status = PAPER_READY`

The exact-instance engine is still available, but only when the exact solve itself is already near-publication.
Campaign mode is secondary and should be used only when a family theorem is already very close to closure.

# Repo layout

- `ledger.md`: append-only human-readable log of what the harness did.
- `queue.json`: current batch of exactly 5 curated dossiers. Entries may now be `paper_candidate`, `family_campaign`, or `feeder_instance`.
- `failed_problems.json`: problems that failed, rediscoveries, archived exacts, and other do-not-recur memory.
- `selected_problem.md`: the currently active queue entry or family campaign brief.
- `memory/`: thin canonical memory surfaces, especially `paper_memory.json` for near-paper packets and `search_memory.json` for attempted/rejected targets.
- `campaigns/`: active campaign dossiers plus campaign manifest/state.
- `prompts/`: stage prompts for `curate`, `solve`, `verify`, `generalize`, `publication_audit`, and `lean`.
- `artifacts/<slug>/`: per-instance work files.
- `artifacts/families/<family_slug>/`: durable family-campaign work files.
- `lean/`: the official AutoMath Lean backend, including reusable family-supporting lemmas.
- `run_once.sh`: one publication-oriented cycle by default.
- `run_n_cycles.sh`: bounded repeated cycles.
- `run_continuous.sh`: repeated cycles until stopped.

# Workflow

AutoMath now has 6 conceptual stages:

1. `curate`
2. `solve`
3. `verify`
4. `generalize`
5. `publication_audit`
6. `lean`

One-shot publication rules:

1. Prefer a `paper_candidate` whose solve would already be most of a paper before considering any family campaign.
2. Curation must optimize for `solve -> publication distance`, not just solve difficulty.
3. Any target that needs a feeder ladder before becoming paper-shaped should be downranked hard.
4. Any campaign that keeps producing solved feeders without shrinking the publication gap should be deprioritized.
5. Use `publication_audit` to decide whether the strongest honest claim is instance-only, slice-level, family-level, rediscovered, or genuinely paper-ready.
6. Use Lean only when it directly seals a near-publication packet; do not let formalization overhead dominate early selection.
7. `EXACT` alone is not a stop condition.
8. Stop automatically only when `publication_status = PAPER_READY` and the relevant proof/formal artifacts are preserved.
9. If verification finds rediscovery, archive it and do not treat it as a frontier success.
10. If a chosen one-shot path fails, do not silently fall back to campaign-first behavior or broad curation; record the blocker clearly and wait for the next explicit selection step.

Parallel policy:

- One manager thread/worktree orchestrates the run.
- If the repo is under Git, isolated workers may run in dedicated worktrees.
- Use subagents or isolated workers only for narrowly scoped tasks with strict context budgets and clear write ownership.
- Merge back only stable dossier and artifact updates.
- Allowed narrow worker roles are:
  - `curation-scout`
  - `novelty-scout`
  - `solver-A`
  - `solver-B`
  - `packet-auditor`
- Do not ask a worker to absorb the whole repo or wander across unrelated campaigns.
- Every worker should receive a short handoff memo containing:
  - exact statement
  - why publishable if solved
  - allowed files
  - stop condition
  - output path
- Default worker context budget:
  - 1 candidate or campaign
  - at most 1 dossier
  - target 3 to 6 source files
  - 1 explicit output file pair
- Write ownership:
  - the manager owns canonical queue files and canonical `record.md` / `status.json`
  - solver workers write only candidate-local sidecar attempt artifacts
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
  - `FAMILY_CANDIDATE`
  - `PAPER_READY`
- Candidate selection should strongly prefer:
  - exact theorem/result pairs,
  - sharp obstruction theorems,
  - minimal counterexamples,
  - tiny structural lemmas with immediate applications,
  - narrow claims with cheap rediscovery surfaces.
- Candidate selection should strongly penalize:
  - feeder ladders,
  - broad family programs with expensive packaging,
  - mathematically easy instances that are still far from publication after the solve,
  - targets with high novelty-check cost or high formalization overhead.
- `EXACT` is reserved for an exact intended statement or exact intended disproof fully checked in Lean.
- Before Lean completes, the strongest positive proof classification is `CANDIDATE`.
- A non-Lean explicit disproof may still be labeled `COUNTEREXAMPLE`, but it does not stop the harness on its own.
- A Lean-backed exact instance may still have `publication_status = INSTANCE_ONLY`.
- `REDISCOVERY` means the exact intended statement is already solved or directly implied in prior art; it never counts as a frontier-novel publication win.
- Do not start solve with SAT, ILP, CP-SAT, brute force, or generic optimization unless the problem is explicitly marked `search-heavy` or two reasoning strategies have already failed.
- Before any nontrivial code, write the reasoning section in the relevant `record.md`.
- Minimal code only: checker, falsifier, tiny experiment, witness verification, or later exact search justified by the reasoning stage.
- Verification begins with a bounded rediscovery / prior-art search before proof checking.
- Curation must explicitly downrank likely rediscoveries, search-heavy targets, feeder-ladder targets, and any target whose solve still leaves a long path to publication.
- If a specific instance is extracted from a broader open family, curation must check whether an earlier theorem, proposition, example, observation, corollary, or sufficient condition already settles that exact instance.
- Solve and most family generalization must run with web disabled. Verification may use limited web for the bounded rediscovery pass. Publication audit may use limited web.
- Be conservative about claim types and theorem scope.
- Keep the ledger updated in plain English.
- Discard worker outputs that do not honestly shorten solve-to-publication distance.
- Prefer thin memory surfaces over replaying large ledgers when orienting future runs.
