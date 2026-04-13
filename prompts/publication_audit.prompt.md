Read `AGENTS.md` and the active selection file first.
Unless the manager preface names another file, the active selection file is `selected_problem.md`.
If the active selection file includes `handoff_memo_path`, read that memo immediately after the active selection file and treat it as the binding scope authority for allowed files, stop condition, and output path.
If the active selection file includes `working_packet_path`, read that file immediately after the active selection file.

This is the PUBLICATION_AUDIT stage.
Limited web is allowed.

Purpose:
Judge theorem-worthiness, publication-worthiness, and MICRO-PAPER leverage, not just correctness.
Default question: is this chosen one-shot candidate actually close to a paper, or did it only look attractive before audit?

This stage runs after `verify`.

Work under `artifacts/<slug>/`.
Read the relevant `record.md` and `status.json`.
If the active selection file includes `attempt_output_markdown` and `attempt_output_json`, treat this as a sidecar audit:

- read the canonical artifact record / status as inputs only
- if the sidecar output files already exist, continue from them instead of restarting from scratch
- write the audited markdown/json outputs to those sidecar paths instead of the canonical files
- do not mutate canonical `record.md` / `status.json` in this sidecar mode

Read budget:

- target 3 to 6 local files total after the active selection file
- hard cap 8 local files unless the canonical source itself forces one extra pinpoint check
- prefer the working packet, local artifact record/status, and one canonical source anchor over broad repo rereads
- do not replay long ledger history during publication audit

Bounded-audit policy:

- Keep the literature pass narrow and claim-specific.
- Prefer the exact statement, theorem-slice wording, canonical source, and one independent status source over broad wandering.
- Use only the minimum web needed to answer the prior-art and publication-worthiness questions honestly.
- Use the narrow one-shot audit by default:
  - exact statement search
  - alternate notation search
  - canonical source check
  - one outside-source status pass
  - stop there unless one of those checks creates a concrete ambiguity that must be resolved
- Update `record.md` and `status.json` before any closing message.
- In sidecar mode, update only the sidecar output markdown/json files before any closing message.

Run these passes in order:

1. `prior_art_audit`
2. `statement_faithfulness_audit`
3. `theorem_worthiness_audit`
4. `publishability_audit`
5. `micro_paper_audit`

Questions you must answer explicitly:

- Is the strongest honest claim stronger than “here is an example”?
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
- What percentage of the paper would one solve already provide?
- Is there a real title theorem, theorem slice, or counterexample theorem here?
- Is the proof structural or merely instance-specific?
- Would this survive a referee asking “what is the theorem?”
- Is the claim still too dependent on hand-picked small cases?
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit?
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program?
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization?

Prior-art / rediscovery audit requirements:

- exact statement search
- alternate notation search
- canonical source search
- theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source
- one outside-source status search
- one recent citation / discussion / follow-up check only when needed

Then update `record.md` with these sections:

- `publication_prior_art_audit`
- `publication_statement_faithfulness`
- `publication_theorem_worthiness`
- `publication_publishability`
- `publication_packet_audit`
- `micro_paper_audit`
- `strongest_honest_claim`
- `paper_title_hint`
- `next_action`

Update `status.json` with:

- `publication_status`
- `publication_confidence`
- `single_solve_to_paper_fraction`
- `title_theorem_strength`
- `publication_narrative_strength`
- `micro_paper_assessment`
- `strongest_honest_claim`
- `paper_title_hint`
- `candidate_theorem_slice`
- `publication_packet_quality`
- `lean_packet_seal`
- `lean_gate_reason`
- `next_action`
- `proof_artifacts_preserved`
- `lean_ready`

Publication status taxonomy:

- `NONE`
- `INSTANCE_ONLY`
- `REDISCOVERY`
- `SLICE_CANDIDATE`
- `SLICE_EXACT`
- `PAPER_READY`

Interpretation rules:

- Lean-backed exact instance but still just an example: `INSTANCE_ONLY`
- one-shot candidate with a clear theorem/result packet and genuinely small remaining gap: usually `SLICE_CANDIDATE`
- rediscovery: `REDISCOVERY`
- strong but not fully closed theorem slice: `SLICE_CANDIDATE`
- fully proved nontrivial slice: `SLICE_EXACT`
- strongest honest claim looks genuinely publishable: `PAPER_READY`

Stop-condition rule:

- do not treat `PAPER_READY` as honest unless the intended statement is exact and Lean-ready for sealing
- automatic stop still requires a Lean-complete exact result plus the paper-ready audit

Be conservative.
Do not confuse “mathematically correct” with “publishable theorem”.
For one-shot candidates, do not let the audit sprawl into a mini-survey; the goal is a cheap honest packet check, not broad literature accumulation.
