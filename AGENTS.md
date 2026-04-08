# Goal

Continuously hunt for one Lean-verified exact proof or disproof of a very niche, simple, still-open math problem that GPT-5.4 could plausibly solve.

# Repo layout

- `ledger.md`: append-only human-readable log of what the harness did.
- `queue.json`: current batch of exactly 5 curated problem dossiers.
- `failed_problems.json`: problems that failed solve/verify and should not be re-curated.
- `selected_problem.md`: the active problem copied from the queue.
- `prompts/`: the 4 stage prompts.
- `artifacts/<slug>/`: per-problem work files created on demand.
- `run_once.sh`: one full cycle.
- `run_continuous.sh`: repeat cycles until stopped.

# Workflow

1. Curate a queue of 5 problems with web search ON.
2. Pick the next non-failed problem from the queue.
3. Solve it in a fresh no-web context.
4. Verify it in a fresh skeptical context that begins with a bounded rediscovery / prior-art search.
5. Run Lean only if verification says the candidate is genuinely strong and not a rediscovery.
6. Treat any non-Lean exact-looking positive result as a `CANDIDATE`, not a final success.
7. If Lean fully verifies a frontier-novel exact intended statement, stop the harness.
8. If verification finds a rediscovery, move the problem aside so it is not curated again.
9. Otherwise add the problem to `failed_problems.json`, remove it from the queue, and continue later.

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
- `EXACT` is reserved for an exact intended statement or exact intended disproof that has been fully checked in Lean. Before Lean completes, the strongest positive proof classification is `CANDIDATE`.
- A non-Lean explicit disproof may still be labeled `COUNTEREXAMPLE`, but it does not stop the harness until the exact instance-level result is also checked through the Lean stage.
- `REDISCOVERY` means the exact intended statement appears solved or directly implied in existing literature; the current run may still contain a correct proof, but it does not count as frontier-novel success, and Lean should not be used as a stop condition for rediscoveries.
- Do not start solve with SAT, ILP, CP-SAT, brute force, or generic optimization unless the problem is explicitly marked `search-heavy` OR two reasoning strategies have already failed.
- Before any nontrivial code, the solver must write a reasoning section in `artifacts/<slug>/record.md`.
- Minimal code only: checker, falsifier, tiny experiment, witness verification, or later exact search justified by the reasoning stage.
- Verification begins with a bounded rediscovery / prior-art search before proof checking.
- Curation must explicitly downrank or reject likely rediscoveries, downrank search-heavy problems, and prefer reasoning-friendly ones.
- If a specific instance is extracted from a broader open family, curation must check whether an earlier theorem, proposition, example, observation, corollary, or sufficient condition in the same source already settles that exact instance.
- Solve and Lean must run with web search disabled. Verification may use limited web only for the first rediscovery pass.
- Be conservative about claim types.
- Keep the ledger updated in plain English.
