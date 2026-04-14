# Determine the exact value of R(K7, K4-e)

- entry_type: `paper_candidate`
- slug: `r-k7-k4e-almost-clique-ramsey`
- worker_role: `solver-B`
- canonical_source: `Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 7, which gives 28 <= R(K7, K4-e) <= 29 and cites the earlier lower-bound source for 28; together with the 2024 revision of Radziszowski's Dynamic Survey "Small Ramsey Numbers" as family context and bounded 2026-04-14 exact-notation and recent-status web checks that did not reveal a later exact closure.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(K7, K4-e) would read as the title theorem of a short note because the public frontier is a single unresolved step in a well-established almost-clique Ramsey table.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.82`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-k7-k4e-almost-clique-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a one-step almost-complete Ramsey gap.`

## question
Is R(K7, K4-e) equal to 28 or 29?

## canonical_statement
Determine the exact value of R(K7, K4-e).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains either a red K7 or a blue K4-e.

## pre_solve_gate_reason
The thin-memory sweep found no prior AutoMath attempt under this exact tuple or title. The bounded web audit found the 2021 interval 28 <= R(K7, K4-e) <= 29 and no later exact determination in the 2026-04-14 search budget.

## micro_paper_assessment
Pass. The gap is only one step, the family is classical, and the post-solve editorial residue is minimal.

## hypothetical_title
The Exact Value of R(K7, K4-e)

## hypothetical_abstract
We determine the Ramsey number R(K7, K4-e). Current public bounds leave this number at 28 <= R(K7, K4-e) <= 29 after the 2021 semidefinite-programming improvement on the upper side. Our result closes the remaining one-step gap in the two-color almost-clique family.

## single_solve_paper_explanation
This is already the honest title theorem of a short paper: an exact endpoint in a named Ramsey family. After the solve, almost everything else is lightweight packaging around a single construction or obstruction proof. There is no need for a broader theorem program to make the result publishable.

## broader_theorem_nonimplication_note
The standard inclusion K4-e subset K4 and classical monotonicity only sandwich the value; they do not collapse the endpoint. No broader theorem located in the bounded audit forces 28 or 29 automatically.

## literature_gap
Current public sources stop at 28 <= R(K7, K4-e) <= 29.

## publication_packet_title
The Exact Value of R(K7, K4-e)

## publication_packet_frontier_basis
The 2021 SDP paper leaves this almost-clique Ramsey number at 28 <= R(K7, K4-e) <= 29. The interval is already paper-shaped because it is a single unresolved binary endpoint with standard notation and a classical family anchor.

## publication_packet_near_paper_reason
If the exact value is settled, the note is nearly complete: state the exact value, present the extremal construction or forcing proof, and briefly place it in the K_m versus K_n-e table. No feeder campaign is required.

## publication_packet_literature_scope
2021 Lidicky-Pfender theorem table, Dynamic Survey family context, and bounded 2026-04-14 exact-notation and recent-status web checks.

## publication_packet_artifact_requirements
Either an explicit red-blue coloring of K28 with no red K7 and no blue K4-e, or a compact proof that every coloring of K29 forces one of them.

## paper_shape
A one-theorem exact-value note for a one-step almost-complete Ramsey gap.

## transfer_kit

### usable_lemmas
- Lidicky-Pfender (2021), Theorem 7, gives the upper bound R(K7, K4-e) <= 29.
- The same theorem table records the matching known lower bound R(K7, K4-e) >= 28 from earlier literature.
- Subgraph monotonicity gives R(K7, K4-e) <= R(K7, K4), which helps frame the upper side without deciding the exact value.
- The Dynamic Survey identifies this as a live entry in the almost-complete graph Ramsey tables rather than an isolated curiosity.

### toy_example
At the lower endpoint, the literature already certifies a 28-vertex coloring avoiding both a red K7 and a blue K4-e.

### known_obstruction
A lower-bound proof needs a very dense blue graph with no K4-e, while an upper-bound proof must show that any attempt to avoid blue K4-e inevitably creates a red K7 one vertex later.

### prior_work_stop_sentence
Current sources stop at 28 <= R(K7, K4-e) <= 29.

### recommended_first_attack
Use the 2021 SDP constraints to restrict local blue neighborhoods, then push a case split on whether the blue graph is forced to be too sparse to avoid a red K7.

### paper_if_solved
The paper would be a short exact-value note in the two-color almost-clique Ramsey family.
