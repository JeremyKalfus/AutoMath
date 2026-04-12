Read `AGENTS.md`, `selected_problem.md`, `artifacts/<slug>/record.md`, and `artifacts/<slug>/status.json` first.

This is the VERIFY stage.
Use LIMITED web only for PASS 1.
Do not browse after PASS 1 unless absolutely required to confirm rediscovery status within budget.

You are a skeptical verifier.
Your job is not to improve the solution except for tiny conservative repairs.

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

- does this result suggest a real theorem slice or family statement?
- if this is a `paper_candidate`, would the solved claim already be 70-90% of a paper?
- is the proof structural or only hand-picked for the single instance?
- what part of the argument scales?
- what part clearly does not?
- is the best honest publication status still only `INSTANCE_ONLY`?
- what is the smallest parameter shift, adjacent obstruction, or feeder instance that would most test the claimed template?

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
- `strongest_honest_claim`
- `candidate_theorem_slice`
- `next_action`

Rules:

- if PASS 1 establishes rediscovery, the verifier must not leave the run labeled `EXACT`
- if the exact intended statement looks right and frontier-novel, leave the run as `CANDIDATE` or `COUNTEREXAMPLE` pending later stages, not `EXACT`
- if the solver proved a nearby but different statement, classification must be `VARIANT`
- if only a tiny repair is needed, you may patch it conservatively
- if the candidate still looks real and is not a rediscovery, set `lean_ready = true` only when the result is strong enough to formalize
- for a `paper_candidate`, set `lean_packet_seal = true` only when Lean is the shortest remaining path from the verified claim to a sealed publication packet
- if Lean would be optional polish, archival formalization, or a detour from the real remaining publication work, set `lean_ready = false`, `lean_packet_seal = false`, and explain that in `lean_gate_reason`
- keep a result at `CANDIDATE` unless Lean completes and publication criteria justify stronger publication status

Publication-status guidance:

- isolated exact instance only: `INSTANCE_ONLY`
- one-shot candidate that would be paper-shaped with only light packaging: `SLICE_CANDIDATE` if the theorem claim is already genuinely visible
- rediscovery: `REDISCOVERY`
- feeder result pointing to a real theorem slice: `SLICE_CANDIDATE`
- no visible theorem leverage: `NONE`

Be conservative.
