Read `AGENTS.md`, the active selection file, the relevant `record.md`, the relevant `status.json`, and `PROOFS.md` if it exists.
Unless the manager preface names another file, the active selection file is `selected_problem.md`.
If the active selection file includes `handoff_memo_path`, read that memo immediately after the active selection file and treat it as the binding scope authority for allowed files, stop condition, and output path.
If the active selection file includes `working_packet_path`, read that file immediately after the active selection file.

This is the LEAN stage.
Do NOT browse the internet.

Work under `artifacts/<slug>/`.

Only continue if the verified result is strong enough to formalize, the current classification is not `REDISCOVERY`, and the packet is already marked HUMAN_READY.
This stage runs from the secondary `LEAN_QUEUE`, not the main discovery queue.
Only continue when the current `status.json` makes it explicit that Lean is the direct packet-sealing step rather than optional polish.

Sidecar attempt mode:

- if the active selection file includes `attempt_output_markdown` and `attempt_output_json`, treat this as a sidecar Lean attempt
- read the canonical record/status as baseline context only
- if the sidecar output files already exist, continue from them instead of restarting from scratch
- write the durable Lean record/status to those sidecar output paths instead of the canonical artifact files
- do not mutate canonical artifact files in this sidecar mode

Read budget:

- target 3 to 6 local files total after the active selection file
- hard cap 8 local files unless one exact theorem dependency must be opened explicitly
- prefer the working packet, local record/status, and only the minimal Lean modules needed for the current target
- do not reopen broad artifact history during Lean

Goal:
Formalize the strongest honest target, not a proxy.
That target may be:

- the exact intended statement
- a reusable lemma
- a theorem slice

Rules:

- use the existing `lean/` AutoMath project as the official Lean/Lake backend
- keep problem-specific Lean sources mirrored under the relevant artifact directory
- start with the exact theorem or lemma statement
- then write a proof skeleton
- then try a full proof only if feasible
- use Lean only if it is the shortest path from "solved claim" to "publication packet sealed"
- if the selected `paper_candidate` does not have `lean_packet_seal = true`, stop cleanly after recording that Lean was not the direct packet-sealing step
- do not introduce new axioms
- do not use `sorry`, `admit`, or placeholders in the final claimed proof
- if Lean is available, run the build/check commands needed to confirm the file really checks
- when the real publication target is a theorem slice or reusable lemma, formalize that instead of spending all effort on yet another isolated instance

Append to `record.md`:

- `lean_statement`
- `lean_skeleton`
- `lean_result`
- `lean_blockers`

Update `status.json` with:

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
- `candidate_theorem_slice`
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
- use `PAPER_READY` only when the strongest honest micro-paper claim looks publishable and the proof artifacts are preserved

Be conservative.
