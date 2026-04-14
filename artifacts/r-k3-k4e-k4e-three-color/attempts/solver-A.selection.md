# Determine the exact value of R(K3, K4-e, K4-e)

- entry_type: `paper_candidate`
- slug: `r-k3-k4e-k4e-three-color`
- worker_role: `solver-A`
- canonical_source: `Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 6.5 and Table XVI; the older references cited there for the lower and upper bounds; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `Closing R(K3, K4-e, K4-e) would already support a compact 3-color exact-value note on a one-gap small Ramsey entry involving the first noncomplete 4-vertex graph.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `87`
- single_solve_to_paper_fraction: `0.84`
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
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-k3-k4e-k4e-three-color/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a one-gap multicolor Ramsey number with a missing-edge clique target.`

## question
Is R(K3, K4-e, K4-e) = 21 or 22?

## canonical_statement
Determine the exact value of R(K3, K4-e, K4-e).

## intended_statement
Either prove that every 3-coloring of K21 contains a color-1 triangle or a color-2 or color-3 copy of K4-e and thus show R(K3, K4-e, K4-e) = 21, or construct a 3-coloring of K21 avoiding all three forbidden patterns and thus show R(K3, K4-e, K4-e) = 22.

## pre_solve_gate_reason
The thin-memory sweep found no prior mathematical status on this exact 3-color target in the repo memory files. DS1.17 still records the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22 in Section 6.5 and Table XVI, and the bounded exact-term and alternate-notation search on 2026-04-14 did not surface a newer exact closure.

## micro_paper_assessment
Pass. The theorem slice is stable, the exact window is only one step wide, and the family anchor is strong enough for a genuine short note.

## hypothetical_title
The Exact Value of R(K3, K4-e, K4-e)

## hypothetical_abstract
We determine the 3-color Ramsey number R(K3, K4-e, K4-e). Existing public sources leave this parameter in the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22. Our result closes a compact unresolved point in the small multicolor K4-e table.

## single_solve_paper_explanation
One exact solve would already be the honest main theorem of the note. Because the current literature state is already compressed to a one-gap window, almost all of the remaining paper is the decisive proof or witness and routine contextualization. The result is clearly paper-shaped rather than a remark.

## broader_theorem_nonimplication_note
General multicolor Ramsey inequalities do not determine this one-gap K4-e instance, and the survey still lists only the narrow 21/22 window. No broader theorem located in the bounded audit collapsed the exact target to an immediate corollary.

## literature_gap
Current public sources support only 21 <= R(K3, K4-e, K4-e) <= 22, and the bounded 2026-04-14 exact-term and alternate-notation audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(K3, K4-e, K4-e)

## publication_packet_frontier_basis
Current public sources leave this three-color number in the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22. The target has a clear family anchor in small multicolor Ramsey numbers involving K4-e, and no later exact determination surfaced in the bounded audit.

## publication_packet_near_paper_reason
The exact value would itself be the title theorem. The note would need only the proof or witness, a short verification appendix for the extremal coloring if the upper endpoint is correct, and a brief comparison to adjacent K4-e multicolor entries already tabulated in the survey.

## publication_packet_literature_scope
DS1.17 Section 6.5 and Table XVI, the lower- and upper-bound references cited there, plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches on 2026-04-14.

## publication_packet_artifact_requirements
Either a proof that every 3-coloring of K21 forces one forbidden pattern, or one explicit 3-coloring of K21 avoiding K3 in one color and K4-e in the other two colors.

## paper_shape
A one-theorem exact-value note for a one-gap multicolor Ramsey number with a missing-edge clique target.

## transfer_kit

### usable_lemmas
- DS1.17 Table XVI records the lower bound R(K3, K4-e, K4-e) >= 21.
- The same survey table records the upper bound R(K3, K4-e, K4-e) <= 22.
- By symmetry of the last two colors, any extremal coloring may be normalized up to swapping the two K4-e colors.

### toy_example
The 21-vertex lower-bound coloring cited through DS1.17 is the smallest nontrivial witness template directly below the target threshold.

### known_obstruction
Any exact upper-bound proof must control triangle creation in one color while simultaneously blocking every almost-clique on four vertices in the other two colors.

### prior_work_stop_sentence
Current sources stop at the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22.

### recommended_first_attack
Begin from the cited 21-vertex extremal coloring and perform a disciplined extension analysis, using color-symmetry reductions before any heavier exhaustive branch search.

### paper_if_solved
The paper would be a short exact-value note on a one-gap 3-color Ramsey number involving K4-e.
