Read `AGENTS.md`, `selected_problem.md`, the relevant `record.md`, the relevant `status.json`, and `PROOFS.md` if it exists.

This is the LEAN stage.
Do NOT browse the internet.

First detect whether the selected entry is:

- a `family_campaign`, in which case work under `artifacts/families/<family_slug>/`
- a `feeder_instance`, in which case work under `artifacts/<slug>/`

Only continue if the verified or generalized result is strong enough to formalize and the current classification is not `REDISCOVERY`.

Goal:
Formalize the strongest honest target, not a proxy.
That target may be:

- the exact intended statement
- a reusable lemma
- a theorem slice
- a family-supporting lemma used by the publication campaign

Rules:

- use the existing `lean/` AutoMath project as the official Lean/Lake backend
- keep problem-specific or family-specific Lean sources mirrored under the relevant artifact directory
- start with the exact theorem or lemma statement
- then write a proof skeleton
- then try a full proof only if feasible
- do not introduce new axioms
- do not use `sorry`, `admit`, or placeholders in the final claimed proof
- if Lean is available, run the build/check commands needed to confirm the file really checks
- when the real publication target is a theorem slice or reusable lemma, formalize that instead of spending all effort on yet another isolated instance

Append to the relevant `record.md`:

- `lean_statement`
- `lean_skeleton`
- `lean_result`
- `lean_blockers`

Update the relevant `status.json` with:

- `stage = "lean"`
- `lean_ready`
- `lean_complete`
- `classification`
- `confidence`
- `publication_status`
- `publication_confidence`
- `strongest_honest_claim`
- `theorem_slice_target`
- `fallback_target`
- `next_blocker`
- `next_feeder_instances`
- `campaign_health`
- `next_action`
- `proof_artifacts_preserved`

`PROOFS.md` policy:

- keep `PROOFS.md` as the exact-instance inventory
- update `PROOFS.md` only if a run really earns `classification = "EXACT"` with `lean_complete = true`
- do not remove existing exact wins
- exact-instance entries may still have `publication_status = INSTANCE_ONLY`

If and only if the run really earns `classification = "EXACT"` with `lean_complete = true`, also update `PROOFS.md` in the same run:

- keep exactly one section per solved slug using heading `## <slug>`
- if the slug already has a section, replace that section instead of duplicating it
- if `PROOFS.md` does not exist yet, create it with a short header
- include at least:
  - title
  - exact statement
  - verify verdict
  - publication status
  - Lean completion date in repo state
  - artifact directory
  - record file
  - status file
  - Lean backend file
  - mirrored Lean file(s)
  - main Lean theorem
  - explicit Lean theorem if present
  - axiom audit note if run
  - `lean4checker --fresh` note if unavailable

Important:

- update `PROOFS.md` before the final `status.json` write that flips the run to `EXACT`
- `EXACT` alone is not the global stop condition
- the automatic stop condition is `publication_status = PAPER_READY`

Classification / publication guidance:

- full formalization of the exact intended instance: `classification = EXACT`
- full formalization of a nontrivial theorem slice may still leave `classification` as the underlying exact or counterexample class, while `publication_status` becomes `SLICE_EXACT`
- use `PAPER_READY` only when the strongest honest campaign-level claim looks publishable and the proof artifacts are preserved

Be conservative.
