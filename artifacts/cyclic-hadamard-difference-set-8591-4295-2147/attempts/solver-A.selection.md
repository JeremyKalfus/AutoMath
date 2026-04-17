# Does the cyclic group C_8591 admit a (8591,4295,2147)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-hadamard-difference-set-8591-4295-2147`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (8591,4295,2147) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" talk slides (ArasuFest, August 3, 2019), cyclic-Hadamard slide listing 8591 among the seven small open cases.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Settling the smallest untouched surviving cyclic Hadamard case v = 8591 would plausibly yield a focused note removing one of the five remaining unattempted residual cases below 10000.`
- publication_if_solved_score: `solve_is_basically_the_paper`
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
- working_packet_path: `artifacts/cyclic-hadamard-difference-set-8591-4295-2147/working_packet.md`
- paper_shape: `A short note eliminating or constructing the cyclic Hadamard case (8591,4295,2147).`

## question
Does the cyclic group C_8591 admit a (8591,4295,2147)-difference set?

## canonical_statement
Determine whether the cyclic group C_8591 admits a (8591,4295,2147)-difference set.

## intended_statement
Determine whether the cyclic group C_8591 admits a (8591,4295,2147)-difference set.

## pre_solve_gate_reason
The exact parameter set is source-anchored in the canonical cyclic Hadamard open table, still appears in Gordon's 2019 small-open-case slide and a 2026 status slide repeating the same seven survivors, has no attempt-registry conflict, and remains theorem-stable because the exact cyclic case is already the honest title theorem if solved.

## micro_paper_assessment
This is a clean micro-paper lane target: exact, source-anchored, theorem-stable, and already framed by the literature as a surviving residual case. It is the best untouched slot because it is the smallest remaining open cyclic Hadamard case after hard-skipping previously attempted 3439 and 4355.

## hypothetical_title
The cyclic Hadamard difference-set case (8591,4295,2147).

## hypothetical_abstract
We determine whether the cyclic group C_8591 admits a (8591,4295,2147)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, Gordon's 2019 La Jolla Repository slides still retain 8591 among the seven small unresolved cases below 10000, and a 2026 status slide repeats the same seven values. A resolution would therefore stand as the title theorem of a short note removing the smallest untouched residual case from the cyclic Hadamard landscape below 10000.

## single_solve_paper_explanation
The literature already packages the frontier as a named residual table entry, so solving the exact case would supply the paper's core mathematical contribution immediately. Little beyond a careful writeup, a bounded prior-art note, and the decisive arithmetic certificate would remain. Because the group is uniquely cyclic and the family label is canonical, the honest paper title does not need to drift after the solve.

## broader_theorem_nonimplication_note
Table 5 explicitly leaves 8591 open after nearby Lander eliminations, Gordon's 2019 slide still lists 8591 among seven survivors, and the surfaced 2026 status material repeats the same unresolved list. The surfaced literature therefore does not already settle the exact 8591 case by a broader published theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 and Gordon's 2019 cyclic-Hadamard slide both leave (8591,4295,2147) unresolved, and bounded 2026 status checks still present 8591 among the same seven sub-10000 survivors without a later case-specific settlement.

## publication_packet_title
On the Cyclic Hadamard Difference-Set Case (8591,4295,2147)

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 5 isolates (8591,4295,2147) as open, Gordon's 2019 La Jolla Repository slides still list 8591 among the seven small open cyclic Hadamard cases, and a 2026 status slide repeats the same seven values.

## publication_packet_near_paper_reason
One exact solve would already remove a named survivor from a canonical residual list in a classical family. Beyond the solve, only bounded exposition, the literature note, and a compact arithmetic certificate remain.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, Hong-Yeop Song's 2026 status slide repeating the same seven v < 10000 cases, the local attempt/source/paper/search memory, and bounded exact-tuple web searches that did not surface a later exact settlement.

## publication_packet_artifact_requirements
A proof or disproof for the cyclic group of order 8591, the decisive character-sum or multiplier obstruction using 11- and 71-quotient data together with n = 2^2 * 3 * 179, and a short literature note explaining why 8591 remains outside the current eliminations.

## paper_shape
A short note eliminating or constructing the cyclic Hadamard case (8591,4295,2147).

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 5 isolates (8591,4295,2147) as an open cyclic Hadamard case.
- The same table shows neighboring cyclic Hadamard cases already eliminated by Lander theorems, clarifying the exact residual frontier.
- Gordon's 2019 slides still list 8591 among the seven small open cyclic Hadamard cases below 10000, and a 2026 status slide repeats the same seven values.
- Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.

### toy_example
Compare 8591 with the nearby excluded case 8463 from the same 2004 table to see exactly where the off-the-shelf Lander eliminations stop.

### known_obstruction
Existing cyclic Hadamard restrictions already dispose of several nearby values, so any proof for 8591 must exploit finer arithmetic than the standard textbook eliminators.

### prior_work_stop_sentence
The literature surface used here stops at listing (8591,4295,2147) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.

### recommended_first_attack
Exploit 11- and 71-quotient profile constraints together with n = 2^2 * 3 * 179 and multiplier or character-sum conditions in the cyclic group of order 8591.

### paper_if_solved
If solved exactly, the paper would be a short note removing the cyclic Hadamard case (8591,4295,2147) from the small-open-case list.
