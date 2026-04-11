Read `AGENTS.md` and `selected_problem.md` first.

This is the PUBLICATION_AUDIT stage.
Limited web is allowed.

Purpose:
Judge theorem-worthiness and publication-worthiness, not just correctness.

This stage may run after:

- `verify`
- `generalize`

First detect whether the selected entry is:

- a `family_campaign`, in which case work under `artifacts/families/<family_slug>/`
- a `feeder_instance`, in which case work under `artifacts/<slug>/`

Read the relevant `record.md`, `status.json`, and the campaign dossier if one exists.
If `selected_problem.md` includes `attempt_kind`, `attempt_output_markdown`, and `attempt_output_json`, treat this as a sidecar proof-attempt audit:

- read the canonical family dossier, record, and status as inputs only;
- write the audited markdown/json outputs to those attempt paths instead of the canonical family files;
- do not mutate the canonical family dossier, canonical family `record.md`, or canonical family `status.json` in this sidecar mode.

Bounded-audit policy:

- Keep the literature pass narrow and claim-specific.
- Prefer the exact family statement, theorem slice wording, canonical source, and one independent status source over broad wandering.
- Use only the minimum web needed to answer the prior-art and publication-worthiness questions honestly.
- Update `record.md` and `status.json` before any closing message.
- In sidecar proof-attempt mode, update only the attempt output markdown/json files before any closing message.

Run these passes in order:

1. `prior_art_audit`
2. `statement_faithfulness_audit`
3. `theorem_worthiness_audit`
4. `publishability_audit`

Questions you must answer explicitly:

- Is the strongest honest claim stronger than “here is an example”?
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here?
- Is the proof structural or merely instance-specific?
- Would this survive a referee asking “what is the theorem?”
- Is the claim still too dependent on hand-picked small cases?
- Is the generalization route strong enough to merit campaign priority?

Prior-art / rediscovery audit requirements:

- exact statement search
- alternate notation search
- canonical source search
- theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source
- one outside-source status search
- one recent citation / discussion / follow-up check when appropriate

Then update the relevant `record.md` with these sections:

- `publication_prior_art_audit`
- `publication_statement_faithfulness`
- `publication_theorem_worthiness`
- `publication_publishability`
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
- rediscovery: `REDISCOVERY`
- strong but not fully closed theorem slice: `SLICE_CANDIDATE`
- fully proved nontrivial slice: `SLICE_EXACT`
- plausible family theorem not yet closed: `FAMILY_CANDIDATE`
- strongest honest claim looks genuinely publishable: `PAPER_READY`

Be conservative.
Do not confuse “mathematically correct” with “publishable theorem”.
