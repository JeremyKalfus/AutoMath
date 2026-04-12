Read `AGENTS.md` and `selected_problem.md` first.
If `selected_problem.md` includes `handoff_memo_path`, read that memo immediately after `selected_problem.md` and treat it as the binding scope authority for allowed files, stop condition, and output path.
If `selected_problem.md` includes `working_packet_path`, read that file immediately after `selected_problem.md`.

This is the PUBLICATION_AUDIT stage.
Limited web is allowed.

Purpose:
Judge theorem-worthiness and publication-worthiness, not just correctness.

This stage may run after:

- `verify`
- `generalize`

First detect whether the selected entry is:

- a `family_campaign`, in which case work under `artifacts/families/<family_slug>/`
- a `paper_candidate` or `feeder_instance`, in which case work under `artifacts/<slug>/`

Read the relevant `record.md`, `status.json`, and the campaign dossier if one exists.
If `selected_problem.md` includes `attempt_output_markdown` and `attempt_output_json`, treat this as a sidecar audit:

- read the canonical dossier / artifact record / status as inputs only;
- if the sidecar output files already exist, continue from them instead of restarting from scratch;
- write the audited markdown/json outputs to those sidecar paths instead of the canonical files;
- do not mutate canonical dossier or canonical `record.md` / `status.json` in this sidecar mode.

Read budget:

- target 3 to 6 local files total after `selected_problem.md`
- hard cap 8 local files unless the canonical source itself forces one extra pinpoint check
- prefer the working packet, local artifact record/status, and one canonical source anchor over broad repo rereads
- do not replay long ledger history during publication audit

Bounded-audit policy:

- Keep the literature pass narrow and claim-specific.
- Prefer the exact family statement, theorem slice wording, canonical source, and one independent status source over broad wandering.
- Use only the minimum web needed to answer the prior-art and publication-worthiness questions honestly.
- For a `paper_candidate`, use the narrow one-shot audit by default:
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

Questions you must answer explicitly:

- Is the strongest honest claim stronger than “here is an example”?
- If this is a `paper_candidate`, would solving it already be 70-90% of a paper?
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here?
- Is the proof structural or merely instance-specific?
- Would this survive a referee asking “what is the theorem?”
- Is the claim still too dependent on hand-picked small cases?
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit?
- For a `paper_candidate`, would Lean directly seal the packet, or would it only be optional polish / later archival formalization?

Prior-art / rediscovery audit requirements:

- `paper_candidate` narrow audit:
  - exact statement search
  - alternate notation search
  - canonical source search
  - theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source
  - one outside-source status search
- broader audit only when needed:
  - one recent citation / discussion / follow-up check when appropriate

Then update the relevant `record.md` with these sections:

- `publication_prior_art_audit`
- `publication_statement_faithfulness`
- `publication_theorem_worthiness`
- `publication_publishability`
- `publication_packet_audit`
- `strongest_honest_claim`
- `paper_title_hint`
- `next_action`

Update the relevant `status.json` with:

- `publication_status`
- `publication_confidence`
- `strongest_honest_claim`
- `paper_title_hint`
- `theorem_slice_target`
- `fallback_target`
- `next_blocker`
- `next_feeder_instances`
- `campaign_health`
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
- `FAMILY_CANDIDATE`
- `PAPER_READY`

Interpretation rules:

- Lean-backed exact instance but still just an example: `INSTANCE_ONLY`
- one-shot candidate with a clear theorem/result packet but light remaining writeup or formal sealing: usually `SLICE_CANDIDATE`
- rediscovery: `REDISCOVERY`
- strong but not fully closed theorem slice: `SLICE_CANDIDATE`
- fully proved nontrivial slice: `SLICE_EXACT`
- plausible family theorem not yet closed: `FAMILY_CANDIDATE`
- strongest honest claim looks genuinely publishable: `PAPER_READY`

Be conservative.
Do not confuse “mathematically correct” with “publishable theorem”.
For one-shot candidates, do not let the audit sprawl into a mini-survey; the goal is a cheap honest packet check, not broad literature accumulation.
For one-shot candidates, set `lean_ready = true` only when Lean is the shortest remaining path to a sealed publication packet; otherwise keep Lean off and explain why in `lean_gate_reason`.
