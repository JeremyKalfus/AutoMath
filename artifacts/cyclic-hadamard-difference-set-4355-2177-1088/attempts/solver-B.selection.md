# Does the cyclic group C_4355 admit a (4355,2177,1088)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-hadamard-difference-set-4355-2177-1088`
- worker_role: `solver-B`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (4355,2177,1088) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" slides (2019), cyclic-Hadamard slide listing 4355 among the seven small open cases.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Settling the cyclic Hadamard case v = 4355 would plausibly yield a focused note removing another named survivor from the sub-10000 open list.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.81`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `moderate`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `medium`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-hadamard-difference-set-4355-2177-1088/working_packet.md`
- paper_shape: `A short note eliminating or constructing the cyclic Hadamard case (4355,2177,1088).`

## question
Does the cyclic group C_4355 admit a (4355,2177,1088)-difference set?

## canonical_statement
Determine whether the cyclic group C_4355 admits a (4355,2177,1088)-difference set.

## intended_statement
Determine whether the cyclic group C_4355 admits a (4355,2177,1088)-difference set.

## pre_solve_gate_reason
The exact parameter set is source-anchored in the canonical cyclic Hadamard open table, survives into Gordon's 2019 small-open-case slide, has no local attempt conflict, and is theorem-stable because the exact cyclic case is already the honest title theorem if settled.

## micro_paper_assessment
This is a viable micro-paper lane target with strong family anchor and stable theorem slice. It is slightly less attractive than 3439 only because it is the second-smallest surviving cyclic Hadamard case rather than the smallest.

## hypothetical_title
The cyclic Hadamard difference-set case (4355,2177,1088).

## hypothetical_abstract
We determine whether the cyclic group C_4355 admits a (4355,2177,1088)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, and Gordon's 2019 La Jolla Repository slides still retain 4355 among the seven small unresolved cases below 10000. A resolution would therefore support a short paper whose title theorem is exactly this residual cyclic Hadamard case.

## single_solve_paper_explanation
The mathematical contribution is already packaged by the literature as a single residual case, so one exact solve would do almost all of the paper's substantive work. What remains is a bounded writeup and the final novelty note. Because the cyclic case is exact and family-labeled, the proof does not need feeder lemmas from a broader campaign to become paper-shaped.

## broader_theorem_nonimplication_note
The canonical 2004 open-case table and Gordon's 2019 slides both still leave 4355 unresolved while adjacent cyclic Hadamard cases are marked as eliminated. The surfaced literature therefore does not already imply the exact 4355 statement via a broader theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 leaves the exact cyclic Hadamard parameter set (4355,2177,1088) open, and Gordon's 2019 slides continue to list 4355 among the small surviving cases without a later case-specific resolution.

## publication_packet_title
On the Cyclic Hadamard Difference-Set Case (4355,2177,1088)

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 5 isolates (4355,2177,1088) as open, and Gordon's 2019 La Jolla Repository slides still retain 4355 among the seven small open cyclic Hadamard cases.

## publication_packet_near_paper_reason
A direct resolution would immediately close one of the canonical residual cases in a classical open family. Beyond the solve, only bounded exposition and literature positioning remain.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, the local attempt/source/paper/search memory, and bounded exact-tuple status searches that did not surface a later settlement.

## publication_packet_artifact_requirements
A proof or disproof for the cyclic group of order 4355, the decisive character-sum or multiplier obstruction on n = 1089, and a short literature note explaining why the case remains outside existing Lander-type eliminations.

## paper_shape
A short note eliminating or constructing the cyclic Hadamard case (4355,2177,1088).

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 5 isolates (4355,2177,1088) as an open cyclic Hadamard case.
- The same table marks several neighboring cyclic Hadamard cases as already excluded by Lander theorems, clarifying the exact residual frontier.
- Gordon's 2019 slides still list 4355 among the seven small open cyclic Hadamard cases below 10000.
- Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.

### toy_example
Compare 4355 with the neighboring excluded case 5775 from the same 2004 table to see how the exact residual case sits beyond the current theorem surface.

### known_obstruction
Existing cyclic Hadamard restrictions already dispose of many nearby values, so any proof for 4355 must exploit arithmetic information finer than the standard eliminators.

### prior_work_stop_sentence
The literature surface used here stops at listing (4355,2177,1088) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.

### recommended_first_attack
Exploit the square order n = 1089 = 3^2 * 11^2 together with multiplier and character-sum constraints in the cyclic group of order 4355.

### paper_if_solved
If solved exactly, the paper would be a short note removing the cyclic Hadamard case (4355,2177,1088) from the small-open-case list.
