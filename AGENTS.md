# Project context
You are working in AutoMath, an automated method for finding niche open math problems and turning exact-instance discoveries into publishable theorem slices, family theorems, or publishable counterexample theorems.

# Goal

The exact-instance engine is still alive, but it is now feeder mode.
The main objective is publication mode:

- harvest exact wins, partials, and verified counterexamples
- turn them into active family campaigns
- push those campaigns toward theorem slices, reusable lemmas, family theorems, or paper-grade counterexample theorems
- stop automatically only when the strongest honest claim reaches `publication_status = PAPER_READY`

# Repo layout

- `ledger.md`: append-only human-readable log of what the harness did.
- `queue.json`: current batch of exactly 5 curated dossiers. Entries may now be `family_campaign` or `feeder_instance`.
- `failed_problems.json`: problems that failed, rediscoveries, archived exacts, and other do-not-recur memory.
- `selected_problem.md`: the currently active queue entry or family campaign brief.
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

Publication mode rules:

1. Prefer an active family campaign before broad fresh curation.
2. Use exact instances as feeder evidence, templates, and discriminating tests for campaigns.
3. After a strong feeder result, run `generalize` before `lean`.
4. Use `publication_audit` to decide whether the strongest honest claim is instance-only, slice-level, family-level, rediscovered, or genuinely paper-ready.
5. Use Lean for reusable lemmas, theorem slices, and family-supporting facts, not only isolated exact instances.
6. `EXACT` alone is not a stop condition.
7. Stop automatically only when `publication_status = PAPER_READY` and the relevant proof/formal artifacts are preserved.
8. If verification finds rediscovery, archive it and do not treat it as a frontier success.
9. If a campaign stalls, use feeder curation to strengthen that campaign before wandering to unrelated one-offs.

Parallel policy:

- One manager thread/worktree orchestrates the run.
- If the repo is under Git, isolated publication workers may run in dedicated worktrees.
- Merge back only stable dossier and artifact updates.

# Core rules

- Reasoning first, code second.
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
- `EXACT` is reserved for an exact intended statement or exact intended disproof fully checked in Lean.
- Before Lean completes, the strongest positive proof classification is `CANDIDATE`.
- A non-Lean explicit disproof may still be labeled `COUNTEREXAMPLE`, but it does not stop the harness on its own.
- A Lean-backed exact instance may still have `publication_status = INSTANCE_ONLY`.
- `REDISCOVERY` means the exact intended statement is already solved or directly implied in prior art; it never counts as a frontier-novel publication win.
- Do not start solve with SAT, ILP, CP-SAT, brute force, or generic optimization unless the problem is explicitly marked `search-heavy` or two reasoning strategies have already failed.
- Before any nontrivial code, write the reasoning section in the relevant `record.md`.
- Minimal code only: checker, falsifier, tiny experiment, witness verification, or later exact search justified by the reasoning stage.
- Verification begins with a bounded rediscovery / prior-art search before proof checking.
- Curation must explicitly downrank likely rediscoveries, search-heavy targets, and isolated one-offs that do not strengthen an active campaign.
- If a specific instance is extracted from a broader open family, curation must check whether an earlier theorem, proposition, example, observation, corollary, or sufficient condition already settles that exact instance.
- Solve and most family generalization must run with web disabled. Verification may use limited web for the bounded rediscovery pass. Publication audit may use limited web.
- Be conservative about claim types and theorem scope.
- Keep the ledger updated in plain English.
