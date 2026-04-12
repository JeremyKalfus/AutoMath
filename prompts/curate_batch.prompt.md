Read `AGENTS.md` first.

This is the CURATION stage.
Use web search.

Goal:
Write `queue.json` as a one-shot-publication queue of exactly 5 dossiers.
The queue may contain both:

- `entry_type = "paper_candidate"`
- `entry_type = "family_campaign"`
- `entry_type = "feeder_instance"`

The harness is no longer optimizing for mathematically interesting slow-burn families by default.
Optimize for:

- `solve -> publication distance`
- probability that one strong solve is already 70-90% of a paper
- exact theorem/result-pair plausibility
- sharp obstruction / minimal-counterexample plausibility
- low novelty-check cost
- low formalization overhead
- verifier tractability
- rediscovery resistance
- tiny proof object size

Phase 2 rubric requirement:

- Do not leave the publication-distance rubric implicit.
- Every `paper_candidate` must carry explicit normalized rubric fields so the manager can rank it without guessing from prose.
- If a candidate does not clearly pass the pre-solve paper test, do not smuggle it in as a paper candidate.

Hard limits:

- max 20 searches total
- max 8 minutes of curation effort
- stop early once 5 acceptable entries are secured
- do not keep browsing after a valid queue has been found
- at or before the budget boundary, stop browsing and immediately write `queue.json` and `selected_problem.md` before any closing prose

Pre-search exclusion sweep:
Before any web search, build an exclusion set from cheap local memory.
Check, if present and inexpensive to read:

- `failed_problems.json`
- `queue.json`
- `selected_problem.md`
- `ledger.md`
- `PROOFS.md`
- `campaigns/`
- `campaigns/manifest.json`
- artifact directory names and cheap status summaries if available
- any `attempted_problems.json`, `rediscoveries.json`, `candidate_problems.json`, or similar memory file

Treat a problem as ALREADY ATTEMPTED if it appears under any prior non-`NEW` status, including:

- `FAILED`
- `PARTIAL`
- `VARIANT`
- `CANDIDATE`
- `COUNTEREXAMPLE`
- `REDISCOVERY`
- `EXACT`

Hard skip any exact or near-duplicate attempted problem, not just failed ones.
Near-duplicate means any of:

- same slug
- same exact title
- same exact parameter tuple / instance
- same canonical-source anchor
- same intended statement up to trivial rewording, reordered tuple, or notation change

When uncertain whether a candidate is just a rephrasing of an earlier attempt, skip it.

Default policy:

- Prefer `paper_candidate` entries.
- Use `family_campaign` only when the family theorem is already very close to closure.
- Use `feeder_instance` only when solving that feeder would directly shorten the path to a paper rather than build a long campaign ladder.
- Up to 1 queue entry may be `family_campaign` unless the user explicitly restores campaign-first behavior.
- At least 4 of the 5 queue entries should be `paper_candidate` or feeder/problem entries whose solve would be nearly paper-shaped immediately.
- Reject or heavily downrank any target that visibly needs multiple feeder wins before publication.

Priority order:

1. `paper_candidate` targets where one solve is already most of a paper
2. exact theorem/result pairs, sharp obstructions, minimal counterexamples, and tiny structural lemmas with immediate applications
3. only then near-paper family campaigns
4. feeder instances only if they directly collapse the publication gap

Diversity control:

- Do not let all 5 queued items collapse into one literature vein unless that vein clearly dominates on solve-to-publication distance.
- At most 2 queued items may come from the same narrow source family unless each is independently paper-shaped if solved.
- Sample at least 3 distinct literature veins during discovery unless one-shot publication evidence is overwhelmingly stronger in a smaller set.

Search protocol under the 20-search cap:

1. Discovery pass:
   - first 4 to 6 searches must sample at least 3 distinct families or literature veins
2. Triage pass:
   - next 3 to 4 searches reduce to at most 8 candidates
3. Audit pass:
   - use remaining searches only on the strongest candidates and stop as soon as 5 survive

Use varied query shapes:

- family-level search for small open instances
- exact-instance search using exact notation / tuple / title
- alternate-notation / reordered-tuple / synonym search
- canonical-source search
- source-internal theorem / proposition / example / observation / corollary / sufficient-condition search
- outside-source status search
- recent status / citation / discussion search when the source is a paper or discussion page

Required publication audit for each final queued candidate:

- exact-instance search
- alternate-notation / synonym search
- canonical-source search
- theorem / proposition / example / observation / corollary / sufficient-condition check inside the canonical source
- one independent outside-source status search
- one recent status / citation / discussion search when appropriate
- attempted-problem conflict check against repo memory
- explicit `why_still_appears_open`
- explicit `why_this_could_be_publishable`
- explicit `publication_if_solved`
- explicit `publication_if_solved_score`
- explicit `solve_to_publication_distance`
- explicit `single_pass_proof_plausibility`
- explicit `novelty_check_cost`
- explicit `formalization_overhead`
- explicit `packaging_risk`
- explicit `needs_feeder_ladder`
- explicit `paper_shape`
- explicit `pre_solve_gate`
- explicit `pre_solve_gate_reason`

Normalized rubric values for `paper_candidate` entries:

- `publication_if_solved_score`:
  - `instant_paper`
  - `standalone_short_paper`
  - `paper_with_light_packaging`
  - `paper_with_moderate_packaging`
  - `paper_with_heavy_packaging`
- `solve_to_publication_distance`:
  - `tiny`
  - `short`
  - `short-medium`
  - `medium`
  - `long`
- `single_pass_proof_plausibility`:
  - `very_high`
  - `high`
  - `medium-high`
  - `medium`
  - `medium-low`
  - `low`
- `novelty_check_cost`:
  - `very_low`
  - `low`
  - `medium`
  - `high`
- `formalization_overhead`:
  - `very_low`
  - `low`
  - `low-medium`
  - `medium`
  - `high`
- `packaging_risk`:
  - `very_low`
  - `low`
  - `medium`
  - `high`
- `needs_feeder_ladder`:
  - `yes`
  - `no`
- `pre_solve_gate`:
  - `pass`
  - `fail`

`pre_solve_gate` rule:

- Mark `pass` only if solving the candidate would already be 70-90% of a paper.
- That means:
  - no feeder ladder is required,
  - the remaining publication distance is at worst `short-medium`,
  - and the result is already close to a standalone theorem, obstruction, minimal counterexample, or tiny structural note.
- If that test is not clearly met, mark `fail` and downrank or exclude the candidate.

Hard rediscovery rule:

- If a specific instance is extracted from a broader open family, you MUST check whether the same source already contains an earlier theorem, proposition, example, observation, corollary, or sufficient condition that settles that exact instance.
- Do not trust only a concluding-question sentence.
- Reject or strongly downrank candidates when:
  - the exact instance already appears in an example or theorem
  - the status is family-open but instance-specific status is unclear
  - the only evidence of openness is vague
  - the instance is likely already implied by a general sufficient condition

Strong preferences:

- crisp exact statements
- publication-worthy exact theorem/result targets
- sharp obstructions and minimal counterexamples
- tiny structural lemmas with immediate applications
- low prerequisite depth
- verifier-friendly problems
- reasoning-friendly problems
- no huge brute-force-first path
- plausible low-overhead formal sealing
- diversity across the queue

Hard reject if any of these hold:

- broad asymptotic conjecture
- heavy machinery dominates
- stale or unclear open status
- likely already solved
- only realistic path is huge brute force / generic SAT / ILP / optimization
- no clear verifier
- intended statement is ambiguous
- clearly already attempted in this repo
- duplicate / near-duplicate of any queued, selected, solved, rediscovered, candidate, variant, partial, counterexample, or failed problem
- solving it still leaves a long path to publication
- it needs a feeder ladder before becoming paper-shaped
- it is easy to solve but expensive to package into a paper

Every final queue entry must include:

- `entry_type`
- `title`
- `slug`
- `question`
- `family_name`
- `named_conjecture`
- `canonical_source`
- `open_status_checked_on`
- `canonical_statement`
- `intended_statement`
- `definitions`
- `attack_style`
- `generalization_potential`
- `proof_template_reuse_score`
- `publishability_score`
- `theorem_slice_hint`
- `campaign_affinity`
- `publication_red_flags`
- `publication_if_solved`
- `publication_if_solved_score`
- `solve_to_publication_distance`
- `single_pass_proof_plausibility`
- `novelty_check_cost`
- `formalization_overhead`
- `packaging_risk`
- `needs_feeder_ladder`
- `paper_shape`
- `pre_solve_gate`
- `pre_solve_gate_reason`
- `why_reasoning_friendly`
- `why_low_token`
- `verifier_hint`
- `lean_hint`
- `rediscovery_risk`
- `why_still_appears_open`
- `why_this_could_be_publishable`
- `attempted_conflict_check`
- `curation_confidence`
- `publication_status`

Status guidance at curation time:

- direct paper candidate with a real theorem/result shape: `SLICE_CANDIDATE`
- near-paper exact feeder or obstruction with immediate packaging value: `NONE` or `INSTANCE_ONLY`
- suspected rediscovery: do not queue it

Queue-writing requirements:

- `queue.json` must contain exactly 5 entries
- at least 4 entries should be `paper_candidate` entries with `pre_solve_gate = "pass"` unless the web evidence honestly fails to support that many
- no placeholder prose
- write `selected_problem.md` for the highest-priority first entry
- preserve bounded behavior
- do not silently fall back to campaign-first choices if one-shot paper candidates are weak; instead prefer honest rejection and a thinner queueing rationale within the 5-entry constraint
