Read `AGENTS.md`, `selected_problem.md`, the relevant `record.md`, the relevant `status.json`, and `PROOFS.md` if it exists.
If `selected_problem.md` includes `handoff_memo_path`, read that memo immediately after `selected_problem.md` and treat it as the binding scope authority for allowed files, stop condition, and output path.

This is the LEAN stage.
Do NOT browse the internet.

First detect whether the selected entry is:

- a `family_campaign`, in which case work under `artifacts/families/<family_slug>/`
- a `paper_candidate` or `feeder_instance`, in which case work under `artifacts/<slug>/`

Only continue if the verified or generalized result is strong enough to formalize and the current classification is not `REDISCOVERY`.
For one-shot `paper_candidate` work, only continue when the current `status.json` makes it explicit that Lean is the direct packet-sealing step rather than optional polish.

Sidecar attempt mode:

- if `selected_problem.md` includes `attempt_output_markdown` and `attempt_output_json`, treat this as a sidecar Lean attempt
- read the canonical record/status as baseline context only
- if the sidecar output files already exist, continue from them instead of restarting from scratch
- write the durable Lean record/status to those sidecar output paths instead of the canonical artifact files
- do not mutate canonical artifact files in this sidecar mode

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
- if the selected entry is a `family_campaign`, stay bounded to the family dossier, family record/status, and current family Lean modules first
- for family campaigns, do not roam solved exact-instance artifact directories unless the family record explicitly names one as a dependency you still need
- start with the exact theorem or lemma statement
- then write a proof skeleton
- then try a full proof only if feasible
- for family campaigns, prefer one reusable lemma or one theorem-slice skeleton over a broad multi-file excursion
- for one-shot `paper_candidate` work, use Lean only if it is the shortest path from "solved claim" to "publication packet sealed"
- if a one-shot `paper_candidate` does not have `lean_packet_seal = true`, stop cleanly after recording that Lean was not the direct packet-sealing step
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
- `lean_packet_seal`
- `lean_gate_reason`
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
