# Does the cyclic group C_8835 admit a (8835,4417,2208)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-hadamard-difference-set-8835-4417-2208`
- worker_role: `solver-B`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (8835,4417,2208) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" talk slides (ArasuFest, August 3, 2019), cyclic-Hadamard slide listing 8835 among the seven small open cases.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Settling the cyclic Hadamard case v = 8835 would plausibly yield a focused note removing another named survivor from the sub-10000 open list.`
- publication_if_solved_score: `solve_is_basically_the_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `85`
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
- novelty_check_cost: `medium`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-hadamard-difference-set-8835-4417-2208/working_packet.md`
- paper_shape: `A short note eliminating or constructing the cyclic Hadamard case (8835,4417,2208).`

## question
Does the cyclic group C_8835 admit a (8835,4417,2208)-difference set?

## canonical_statement
Determine whether the cyclic group C_8835 admits a (8835,4417,2208)-difference set.

## intended_statement
Determine whether the cyclic group C_8835 admits a (8835,4417,2208)-difference set.

## pre_solve_gate_reason
The exact parameter set is source-anchored in the canonical cyclic Hadamard open table, still appears in Gordon's 2019 small-open-case slide and a 2026 status slide repeating the same seven survivors, has no attempt-registry conflict, and remains theorem-stable because the exact cyclic case is already the honest title theorem if solved.

## micro_paper_assessment
This is a viable micro-paper lane target with strong family anchor and stable theorem slice. It is especially attractive because n = 47^2 suggests a comparatively compact arithmetic certificate without changing the paper shape.

## hypothetical_title
The cyclic Hadamard difference-set case (8835,4417,2208).

## hypothetical_abstract
We determine whether the cyclic group C_8835 admits a (8835,4417,2208)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, Gordon's 2019 La Jolla Repository slides still retain 8835 among the seven small unresolved cases below 10000, and a 2026 status slide repeats the same seven values. A resolution would therefore support a short paper whose title theorem is exactly this residual cyclic Hadamard case.

## single_solve_paper_explanation
The mathematical contribution is already packaged by the literature as a single residual case, so one exact solve would do almost all of the paper's substantive work. What remains is a bounded writeup, the final novelty note, and the certificate details. Because the cyclic case is exact and family-labeled, the proof does not need feeder lemmas from a broader campaign to become paper-shaped.

## broader_theorem_nonimplication_note
The canonical 2004 table and the 2019 and 2026 status sources still leave 8835 unresolved while adjacent cyclic Hadamard cases are marked as eliminated. The surfaced literature therefore does not already imply the exact 8835 statement via a broader theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 and Gordon's 2019 cyclic-Hadamard slide both leave (8835,4417,2208) unresolved, and bounded 2026 status checks still present 8835 among the same seven sub-10000 survivors without a later exact settlement.

## publication_packet_title
On the Cyclic Hadamard Difference-Set Case (8835,4417,2208)

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 5 isolates (8835,4417,2208) as open, Gordon's 2019 La Jolla Repository slides still list 8835 among the seven small open cyclic Hadamard cases, and a 2026 status slide repeats the same seven values.

## publication_packet_near_paper_reason
One exact solve would already remove a named survivor from a canonical residual list in a classical family. The remaining work is mostly exposition, literature placement, and the final arithmetic certificate.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, Hong-Yeop Song's 2026 status slide repeating the same seven v < 10000 cases, the local attempt/source/paper/search memory, and bounded exact-tuple web searches that did not surface a later exact settlement.

## publication_packet_artifact_requirements
A proof or disproof for the cyclic group of order 8835, the decisive multiplier or character-sum obstruction exploiting 3-, 5-, 19-, and 31-quotients together with n = 47^2, and a short literature note explaining why 8835 remains outside the current eliminations.

## paper_shape
A short note eliminating or constructing the cyclic Hadamard case (8835,4417,2208).

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 5 isolates (8835,4417,2208) as an open cyclic Hadamard case.
- The same table shows neighboring cyclic Hadamard cases already eliminated by Lander theorems, clarifying the residual frontier.
- Gordon's 2019 slides still list 8835 among the seven small open cyclic Hadamard cases below 10000, and a 2026 status slide repeats the same seven values.
- Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.

### toy_example
Compare 8835 with the nearby excluded case 8463 from the same 2004 table to see how the open residue sits just beyond the currently available eliminators.

### known_obstruction
Existing cyclic Hadamard restrictions already remove several nearby values, so any proof for 8835 must exploit finer arithmetic data than the standard Lander-type exclusions.

### prior_work_stop_sentence
The literature surface used here stops at listing (8835,4417,2208) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.

### recommended_first_attack
Exploit 3-, 5-, 19-, and 31-quotient profile constraints together with the square order n = 47^2 and multiplier or character-sum conditions in the cyclic group of order 8835.

### paper_if_solved
If solved exactly, the paper would be a short note removing the cyclic Hadamard case (8835,4417,2208) from the small-open-case list.
