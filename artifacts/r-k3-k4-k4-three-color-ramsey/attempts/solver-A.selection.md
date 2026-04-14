# Determine the exact value of R(K3, K4, K4)

- entry_type: `paper_candidate`
- slug: `r-k3-k4-k4-three-color-ramsey`
- worker_role: `solver-A`
- canonical_source: `Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 8, which gives 21 <= R(K3, K4, K4) <= 22; together with bounded 2026-04-14 exact-notation and recent-status web checks that did not reveal a later exact closure.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(K3, K4, K4) would support a compact note because the public frontier is already a one-step gap with a clean three-color statement.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `81`
- single_solve_to_paper_fraction: `0.8`
- title_theorem_strength: `strong`
- family_anchor_strength: `moderate`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
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
- working_packet_path: `artifacts/r-k3-k4-k4-three-color-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a one-step three-color clique Ramsey number.`

## question
Is R(K3, K4, K4) equal to 21 or 22?

## canonical_statement
Determine the exact value of R(K3, K4, K4).

## intended_statement
Determine the least n such that every 3-coloring of E(K_n) contains either a color-1 K3, a color-2 K4, or a color-3 K4.

## pre_solve_gate_reason
The thin-memory sweep found no prior AutoMath attempt under this exact tuple or title. The bounded web audit found the 2021 interval 21 <= R(K3, K4, K4) <= 22 and no later exact determination in the 2026-04-14 search budget.

## micro_paper_assessment
Pass. The family anchor is a bit lighter than the two-color cases, but the one-step gap and compact theorem statement keep it inside the micro-paper lane.

## hypothetical_title
The Exact Value of R(K3, K4, K4)

## hypothetical_abstract
We determine the three-color Ramsey number R(K3, K4, K4). The best public bounds after the 2021 semidefinite-programming improvement are 21 <= R(K3, K4, K4) <= 22. Our result closes the remaining one-step gap and completes this small three-color clique entry.

## single_solve_paper_explanation
The exact value is already the full story here, not a feeder lemma. Because the gap is one step, a successful lower-bound construction or one-vertex forcing proof would contribute most of the eventual paper. The remaining work is mainly exposition and a compact extremal certificate.

## broader_theorem_nonimplication_note
General multicolor clique bounds do not decide 21 versus 22, and no broader theorem located in the bounded audit collapses this case automatically.

## literature_gap
Current public sources stop at 21 <= R(K3, K4, K4) <= 22.

## publication_packet_title
The Exact Value of R(K3, K4, K4)

## publication_packet_frontier_basis
Current public sources leave the three-color clique Ramsey number at 21 <= R(K3, K4, K4) <= 22. The live frontier is therefore a single unresolved binary endpoint with standard notation and clear table value.

## publication_packet_near_paper_reason
Once the endpoint is fixed, the paper is almost entirely the proof or critical coloring. The surrounding exposition is routine because the question is already in standard Ramsey notation and needs little setup.

## publication_packet_literature_scope
2021 Lidicky-Pfender theorem table plus bounded 2026-04-14 exact-notation and recent-status web checks.

## publication_packet_artifact_requirements
Either an explicit 21-vertex 3-coloring with no monochromatic K3, K4, K4 in the designated colors or a proof that every 3-coloring of K22 forces one of them.

## paper_shape
A one-theorem exact-value note for a one-step three-color clique Ramsey number.

## transfer_kit

### usable_lemmas
- Lidicky-Pfender (2021), Theorem 8, gives the upper bound R(K3, K4, K4) <= 22.
- The same theorem table records the known lower bound R(K3, K4, K4) >= 21 from earlier literature.
- Standard color-merging monotonicity gives easy sanity bounds from adjacent three-color clique entries without deciding the exact endpoint.
- The 2021 paper's SDP framework is explicitly designed to extract small-graph local constraints for Ramsey extremal colorings.

### toy_example
The literature already certifies the existence of a 21-vertex coloring avoiding a monochromatic K3 in one color and K4 in each of the other two colors.

### known_obstruction
A lower-bound construction must balance two different K4-avoidance conditions while also avoiding a triangle in the third color, which sharply restricts local color densities.

### prior_work_stop_sentence
Current sources stop at 21 <= R(K3, K4, K4) <= 22.

### recommended_first_attack
Start from the SDP upper-bound profile and classify allowed colored neighborhood types around a vertex; then attempt a constrained extension search from the 21-vertex lower-bound side.

### paper_if_solved
The paper would be a concise exact-value note on a small three-color clique Ramsey number.
