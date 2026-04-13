Read `AGENTS.md`, the active selection file, `artifacts/<slug>/record.md`, and `artifacts/<slug>/status.json` first.
Unless the manager preface names another file, the active selection file is `selected_problem.md`.
If the active selection file includes `handoff_memo_path`, read that memo immediately after the active selection file and treat it as the binding scope authority for allowed files, stop condition, and output path.
If the active selection file includes `working_packet_path`, read that file immediately after the active selection file.

This is the VERIFY stage.
Use LIMITED web only for PASS 1.
Do not browse after PASS 1 unless absolutely required to confirm rediscovery status within budget.

You are a skeptical verifier.
Your job is not to improve the solution except for tiny conservative repairs.

Sidecar attempt mode:

- if the active selection file includes `attempt_output_markdown` and `attempt_output_json`, treat this as a sidecar verification run
- read the canonical artifact `record.md` / `status.json` as baseline context only
- if the sidecar output files already exist, read them first and keep writing there
- write the durable verification record and status to those sidecar output paths instead of the canonical artifact files
- do not mutate canonical artifact files in this sidecar mode

Read budget:

- target 3 to 6 local files total after the active selection file
- hard cap 8 local files unless one exact faithfulness check forces one more supporting source
- prefer the working packet, local artifact record/status, and one canonical source anchor over broad repo rereads
- do not roam through broad logs or unrelated artifacts during verify

Run 5 passes in this exact order:

PASS 1: `rediscovery_audit`

- allowed LIMITED web
- budget:
  - max 8 searches
  - max 6 minutes
  - stop early if rediscovery is clearly established
- search patterns must include:
  1. exact instance notation / parameter tuple
  2. alternate notation / reordered parameters / family notation
  3. the canonical source itself
  4. theorem / proposition / example / observation / corollary checks inside the same source
  5. one recent citation / status / discussion check if needed
- decide whether the exact intended statement is already solved, directly implied, or explicitly exhibited in prior art
- if rediscovery is found, set:
  - `verify_verdict = "REDISCOVERY"`
  - `classification = "REDISCOVERY"`
  - `publication_status = "REDISCOVERY"`
  - `lean_ready = false`
  - `next_action = "archive_as_rediscovery"`

PASS 2: `faithfulness`

- does the claimed result match the intended statement exactly?
- look for wrong-theorem drift, quantifier drift, changed definitions, weaker proxy statements, or mismatch between prose and the actual solved claim

PASS 3: `proof_correctness`

- find the first incorrect step, or say none found
- look for hidden assumptions, missing cases, unjustified leaps, or handwaving

PASS 4: `adversarial_check`

- if code or a checker exists, rerun it
- if there is a candidate construction or counterexample, try to break it
- check that any computation really supports the mathematical claim

PASS 5: `theorem_worthiness`

- assess exactness
- assess novelty
- assess reproducibility
- assess Lean readiness
- assess paper leverage
- distinguish “true but still publication-distant” from “one solve away from a paper packet”
- explicitly answer:
  - would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  - what percentage of the paper would one solve already provide?
  - what title theorem is actually visible?
  - what part of the argument scales?
  - what part clearly does not?
  - is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`?

Then update `artifacts/<slug>/record.md` with these sections:

- `verify_rediscovery`
- `verify_faithfulness`
- `verify_proof`
- `verify_adversarial`
- `verify_theorem_worthiness`
- `verify_verdict`
- `minimal_repair_if_any`

Update `artifacts/<slug>/status.json` with:

- `stage = "verify"`
- `verify_verdict`
- `classification`
- `confidence`
- `lean_ready`
- `lean_packet_seal`
- `lean_gate_reason`
- `publication_status`
- `publication_confidence`
- `single_solve_to_paper_fraction`
- `title_theorem_strength`
- `publication_narrative_strength`
- `micro_paper_assessment`
- `strongest_honest_claim`
- `candidate_theorem_slice`
- `next_action`

Rules:

- if PASS 1 establishes rediscovery, the verifier must not leave the run labeled `EXACT`
- if the exact intended statement looks right and frontier-novel, leave the run as `CANDIDATE` or `COUNTEREXAMPLE` pending later stages, not `EXACT`
- if the solver proved a nearby but different statement, classification must be `VARIANT`
- if only a tiny repair is needed, you may patch it conservatively
- if the candidate still looks real and is not a rediscovery, set `lean_ready = true` only when the result is strong enough to formalize
- set `lean_packet_seal = true` only when Lean is the shortest remaining path from the verified claim to a sealed publication packet
- if Lean would be optional polish, archival formalization, or a detour from the real remaining publication work, set `lean_ready = false`, `lean_packet_seal = false`, and explain that in `lean_gate_reason`
- keep a result at `CANDIDATE` unless Lean completes and publication criteria justify stronger publication status

Publication-status guidance:

- isolated exact instance only: `INSTANCE_ONLY`
- one-shot candidate with a clear theorem/result packet and genuinely small remaining gap: `SLICE_CANDIDATE`
- rediscovery: `REDISCOVERY`
- no visible theorem leverage: `NONE`

Be conservative.
A result can be exact yet still fail the micro-paper test.
