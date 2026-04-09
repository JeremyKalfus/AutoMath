Read `AGENTS.md` first.

This is the CURATION stage.
Use web search.

Goal:
Write `queue.json` as a publication-oriented mixed queue of exactly 5 dossiers.
The queue may contain both:

- `entry_type = "family_campaign"`
- `entry_type = "feeder_instance"`

The harness is no longer optimizing for isolated one-off wins.
Optimize for:

- publication potential
- named family / named conjecture alignment
- theorem-slice plausibility
- generalization potential
- reusable proof-template potential
- verifier and Lean tractability
- rediscovery resistance
- diversity across families

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

Campaign-first policy:

- Up to 2 queue entries may be `family_campaign`.
- Remaining entries may be `feeder_instance`.
- Prefer feeder instances that strengthen an active campaign rather than random unrelated one-offs.
- If there is at least one active campaign with an unresolved theorem-slice blocker, at least 4 of the 5 queue entries must support active campaigns.
- In that case, at most 1 queue entry may be a broad unrelated candidate.
- If two family-campaign entries are queued, fill the remaining three slots with campaign feeders before considering unrelated problems.
- If a named family already has either:
  - 2 or more exact instances in repo memory, or
  - 1 exact instance plus 2 strong verified near-results,
  then prefer opening or extending a campaign instead of queueing yet another isolated instance from that family.

Priority order:

1. active publication campaigns already seeded from repo memory
2. feeder instances that discriminate between campaign theorem templates
3. only then fresh unrelated curation

Diversity control:

- Do not let all 5 queued items collapse into one paper or one narrow literature vein unless it is overwhelmingly stronger than the alternatives.
- At most 2 queued items may come from the same narrow source family unless that family is an active campaign.
- Sample at least 3 distinct source families or literature veins during discovery unless the campaign-first evidence is overwhelmingly stronger.

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
- publication-worthy theorem targets
- theorem-slice plausibility
- structural or family-level leverage
- low prerequisite depth
- verifier-friendly problems
- reasoning-friendly problems
- no huge brute-force-first path
- plausible Lean formalization
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

- new family campaign target with real theorem-slice traction: `SLICE_CANDIDATE`
- exact feeder instance with no family closure yet: `NONE` or `INSTANCE_ONLY`
- suspected rediscovery: do not queue it

Queue-writing requirements:

- `queue.json` must contain exactly 5 entries
- no placeholder prose
- write `selected_problem.md` for the highest-priority first entry
- preserve bounded behavior
