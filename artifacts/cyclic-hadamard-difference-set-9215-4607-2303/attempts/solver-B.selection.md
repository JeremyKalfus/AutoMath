# Does the cyclic group C_9215 admit a (9215,4607,2303)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-hadamard-difference-set-9215-4607-2303`
- worker_role: `solver-B`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (9215,4607,2303) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" talk slides (ArasuFest, August 3, 2019), cyclic-Hadamard slide listing 9215 among the seven small open cases.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Settling the cyclic Hadamard case v = 9215 would plausibly yield a focused note removing another named survivor from the sub-10000 open list.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `79`
- single_solve_to_paper_fraction: `0.78`
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
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/cyclic-hadamard-difference-set-9215-4607-2303/working_packet.md`
- paper_shape: `A short note eliminating or constructing the cyclic Hadamard case (9215,4607,2303).`

## question
Does the cyclic group C_9215 admit a (9215,4607,2303)-difference set?

## canonical_statement
Determine whether the cyclic group C_9215 admits a (9215,4607,2303)-difference set.

## intended_statement
Determine whether the cyclic group C_9215 admits a (9215,4607,2303)-difference set.

## pre_solve_gate_reason
The exact parameter set is source-anchored in the canonical cyclic Hadamard open table, still appears in Gordon's 2019 small-open-case slide and a 2026 status slide repeating the same seven survivors, has no attempt-registry conflict, and remains theorem-stable because the exact cyclic case is already the honest title theorem if solved.

## micro_paper_assessment
This remains lane-eligible because the exact case is source-anchored and theorem-stable, and one clean solve would still look like the title theorem of a short note. It ranks below the top three only because the publication packet feels slightly less crisp at current audit depth.

## hypothetical_title
The cyclic Hadamard difference-set case (9215,4607,2303).

## hypothetical_abstract
We determine whether the cyclic group C_9215 admits a (9215,4607,2303)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, Gordon's 2019 La Jolla Repository slides still retain 9215 among the seven small unresolved cases below 10000, and a 2026 status slide repeats the same seven values. A resolution would therefore support a short note whose title theorem is exactly this residual cyclic Hadamard case.

## single_solve_paper_explanation
The literature already packages the frontier as a named residual table entry, so solving the exact case would supply the paper's core mathematical contribution immediately. What remains is a bounded writeup and the final literature note. Because the theorem slice is exact and family-labeled, the result would already look like the title theorem of a short note.

## broader_theorem_nonimplication_note
The canonical 2004 table and the 2019 and 2026 status sources still leave 9215 unresolved while nearby cyclic Hadamard cases are marked as eliminated. The surfaced literature therefore does not already imply the exact 9215 statement via a broader theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 and Gordon's 2019 cyclic-Hadamard slide both leave (9215,4607,2303) unresolved, and bounded 2026 status checks still present 9215 among the same seven sub-10000 survivors without a later exact settlement.

## publication_packet_title
On the Cyclic Hadamard Difference-Set Case (9215,4607,2303)

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 5 isolates (9215,4607,2303) as open, Gordon's 2019 La Jolla Repository slides still list 9215 among the seven small open cyclic Hadamard cases, and a 2026 status slide repeats the same seven values.

## publication_packet_near_paper_reason
A direct resolution would immediately close one of the canonical residual cases in a classical open family. Beyond the solve, only bounded exposition and literature positioning remain.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, Hong-Yeop Song's 2026 status slide repeating the same seven v < 10000 cases, the local attempt/source/paper/search memory, and bounded exact-tuple web searches that did not surface a later exact settlement.

## publication_packet_artifact_requirements
A proof or disproof for the cyclic group of order 9215, the decisive multiplier or character-sum obstruction exploiting 5-, 19-, and 97-quotients together with n = 2^8 * 3^2, and a short literature note explaining why 9215 remains outside the current eliminations.

## paper_shape
A short note eliminating or constructing the cyclic Hadamard case (9215,4607,2303).

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 5 isolates (9215,4607,2303) as an open cyclic Hadamard case.
- The same table shows nearby cyclic Hadamard cases already eliminated by Lander theorems, clarifying the residual frontier.
- Gordon's 2019 slides still list 9215 among the seven small open cyclic Hadamard cases below 10000, and a 2026 status slide repeats the same seven values.
- Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.

### toy_example
Compare 9215 with the nearby excluded case 8463 from the same 2004 table to see where the standard eliminators stop and the unresolved residue begins.

### known_obstruction
Existing cyclic Hadamard restrictions already eliminate several nearby values, so any proof for 9215 must use finer arithmetic than the standard textbook filters.

### prior_work_stop_sentence
The literature surface used here stops at listing (9215,4607,2303) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.

### recommended_first_attack
Exploit 5-, 19-, and 97-quotient profile constraints together with n = 2^8 * 3^2 and multiplier or character-sum conditions in the cyclic group of order 9215.

### paper_if_solved
If solved exactly, the paper would be a short note removing the cyclic Hadamard case (9215,4607,2303) from the small-open-case list.
