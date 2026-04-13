Read `AGENTS.md` first.
Prefer `memory/paper_memory.json` and `memory/search_memory.json` over replaying broad repo history when they exist.

This is the CURATION stage.
Use web search.

Goal:
Write `queue.json` as a queue of exactly 5 `paper_candidate` dossiers, optimized for the MICRO-PAPER objective:

- the smallest frontier-novel exact claim where one clean solve is already about 70-90% of a publishable note
- exact theorem/result pairs, sharp obstructions, minimal counterexamples, and tiny structural slices with immediate applications
- small bounded targets only; do not drift into broad theorem hunting
- no reserve lane, no alternate fallback lane, and no feeder-instance queue slots

Core curation dimensions:

1. `closability`
2. `novelty`
3. `micro-paper leverage`

Required 70-90% paper test for every candidate:

1. If this statement were solved exactly, could it plausibly be the title theorem of a short note?
2. Would that one solve already provide about 70-90% of the eventual paper?
3. What would remain after the solve?
4. Why is the target not just a niche exact curiosity?
5. Why is it not already implied by a broader published result?

If you cannot write a plausible title and abstract that feel like a real short note, the candidate fails.

Lean policy during curation:

- Do not up-rank a candidate merely because it looks easy to formalize.
- Low `formalization_overhead` matters only when Lean would directly seal the publication packet after a successful solve.
- If Lean would be optional polish, later archival formalization, or a detour from the real paper packet, do not treat Lean-friendliness as a primary advantage.

Hard limits:

- max 20 searches total
- max 8 minutes of curation effort
- stop early once 5 acceptable entries are secured
- do not keep browsing after a valid queue has been found
- at or before the budget boundary, stop browsing and immediately write `queue.json` and `selected_problem.md` before any closing prose

Pre-search exclusion sweep:
Before any web search, build an exclusion set from cheap local memory.
Check, if present and inexpensive to read:

- `memory/search_memory.json`
- `memory/paper_memory.json`
- `failed_problems.json`
- `queue.json`
- `selected_problem.md`
- `PROOFS.md`
- artifact directory names and cheap status summaries if available
- any `attempted_problems.json`, `rediscoveries.json`, `candidate_problems.json`, or similar memory file
- `ledger.md` only if a conflict or ambiguity remains after the thin memory files

Treat a problem as ALREADY ATTEMPTED if it appears under any prior mathematical status, including:

- `FAILED`
- `PARTIAL`
- `VARIANT`
- `CANDIDATE`
- `COUNTEREXAMPLE`
- `REDISCOVERY`
- `EXACT`

Infrastructure failures are different:

- if local memory shows only a timeout / infra failure with salvaged artifacts and cooldown parking, do not treat that alone as a mathematical disqualification
- such targets may be reconsidered later, but only if they still fit the micro-paper lane and are not currently cooled down

Hard skip any exact or near-duplicate attempted problem, not just failed ones.
Near-duplicate means any of:

- same slug
- same exact title
- same exact parameter tuple / instance
- same canonical-source anchor
- same intended statement up to trivial rewording, reordered tuple, or notation change

When uncertain whether a candidate is just a rephrasing of an earlier attempt, skip it.

Local-read budget before web:

- target 4 to 6 local memory files
- hard cap 8 local files before the first web search
- do not roam through broad artifact history or large log files during curation

Default policy:

- Every queue slot must be a `paper_candidate`.
- Strongly downrank anything that needs a feeder ladder, a broad theorem-development program, or expensive post-solve packaging.
- Reject targets whose story depends on a future campaign rather than the one-shot solve itself.

Hard gate for `micro_paper_lane_eligible = true`:

- acceptable novelty risk after curation
- `broader_theorem_implication_risk` is not `high` and not `unresolved`
- `search_heavy = false`, or else the remaining residue is tiny and human-readable
- `isolated_exact_case_risk` is not `high`
- `transfer_kit_present = true`
- `title_theorem_strength` is at least `moderate`
- `family_anchor_strength` is at least `moderate`
- `publication_narrative_strength` is at least `moderate`
- `editorial_overhead` is not `high`
- `certificate_compactness` is acceptable
- `single_solve_to_paper_fraction >= 0.70`

Unknown on any load-bearing micro-paper field defaults to FAIL the lane.

Strong preferences inside the lane:

- `single_solve_to_paper_fraction` in `0.70-0.90`
- `title_theorem_strength = strong`
- `family_anchor_strength = strong`
- `publication_narrative_strength = strong`
- `editorial_overhead = low`
- `broader_theorem_implication_risk = low`
- `certificate_compactness = high`
- `paper_leverage_score` high

Negative archetypes to reject:

- tiny exact cases whose only appeal is that they are tiny
- problems where the solve is real but the paper story is weak
- isolated curiosities with no family anchor
- problems that are mainly finite census / exhaustive search / long certificate dumps
- extracted instances that may already be implied by broader known theorems
- problems where after one solve you still need two or three major new results before the note is paper-worthy
- cute observations that would likely stay a one-paragraph remark

Required dossier fields for every `paper_candidate`:

- `paper_leverage_score`
- `single_solve_to_paper_fraction`
- `title_theorem_strength`
- `family_anchor_strength`
- `publication_narrative_strength`
- `editorial_overhead`
- `immediate_corollary_headroom`
- `isolated_exact_case_risk`
- `broader_theorem_implication_risk`
- `search_heavy`
- `certificate_compactness`
- `transfer_kit_present`
- `exact_gap_from_source`
- `micro_paper_lane_eligible`
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
- `publication_packet_title`
- `publication_packet_frontier_basis`
- `publication_packet_near_paper_reason`
- `publication_packet_literature_scope`
- `publication_packet_artifact_requirements`
- `publication_packet_quality`
- `hypothetical_title`
- `hypothetical_abstract`
- `single_solve_paper_explanation`
- `broader_theorem_nonimplication_note`
- `literature_gap`
- `micro_paper_assessment`
- `transfer_kit`

Field conventions:

- `paper_leverage_score`: integer 0-100
- `single_solve_to_paper_fraction`: decimal in `[0,1]`
- `title_theorem_strength`: `weak`, `moderate`, `strong`
- `family_anchor_strength`: `weak`, `moderate`, `strong`
- `publication_narrative_strength`: `weak`, `moderate`, `strong`
- `editorial_overhead`: `low`, `moderate`, `high`
- `immediate_corollary_headroom`: `none`, `low`, `moderate`, `high`
- `isolated_exact_case_risk`: `low`, `moderate`, `high`
- `broader_theorem_implication_risk`: `low`, `moderate`, `high`, `unresolved`
- `search_heavy`: `true` or `false`
- `certificate_compactness`: `low`, `moderate`, `high`
- `transfer_kit_present`: `true` or `false`
- `exact_gap_from_source`: `tiny`, `small`, `moderate`, `broad`
- `micro_paper_lane_eligible`: `true` or `false`

Required publication packet payload:

- `hypothetical_title`: 1 sentence
- `hypothetical_abstract`: 3 sentences
- `single_solve_paper_explanation`: 2 to 4 sentences explaining why one solve yields most of the paper
- `broader_theorem_nonimplication_note`: specific note on why a broader theorem does not already settle it
- `literature_gap`: exact statement of where prior work stops

Required transfer kit payload:

- `lemmas`: 2 to 4 usable lemmas / proof ingredients from the source literature
- `toy_example`: 1 worked example or smallest nontrivial instance
- `known_obstruction`: 1 known obstruction or failure mode
- `prior_work_stop_sentence`: 1 exact sentence saying where prior work stops
- `recommended_first_attack`: 1 recommended first proof attack
- `paper_if_solved`: 1 sentence explaining what the paper would look like if solved

Search protocol under the 20-search cap:

1. Discovery pass:
   - first 4 to 6 searches must sample at least 3 distinct literature veins
2. Triage pass:
   - next 3 to 4 searches reduce to at most 8 candidates
3. Audit pass:
   - use remaining searches only on the strongest candidates and stop as soon as 5 survive

Use varied query shapes:

- family-level search for recent papers leaving exact gaps
- exact-statement search using exact notation / tuple / title
- alternate-notation / reordered-tuple / synonym search
- canonical-source search
- source-internal theorem / proposition / example / observation / corollary / sufficient-condition search
- outside-source status search
- recent status / citation / discussion search when the source is a paper or discussion page

Required bounded audit for each final queued candidate:

- exact-statement search
- alternate-notation / synonym search
- canonical-source search
- theorem / proposition / example / observation / corollary / sufficient-condition check inside the canonical source
- one independent outside-source status search
- one recent status / citation / discussion search when appropriate
- attempted-problem conflict check against repo memory

Output policy:

- `queue.json` must contain exactly 5 `paper_candidate` entries
- `selected_problem.md` must point to the highest-priority currently usable micro-paper candidate
- rank the queue by smallest honest `solve_to_publication_distance` and strongest paper packet quality, not by future theorem-program momentum
- if fewer than 5 honest micro-paper candidates survive, still write 5 `paper_candidate` entries but mark weak ones honestly with `micro_paper_lane_eligible = false`

Be conservative.
