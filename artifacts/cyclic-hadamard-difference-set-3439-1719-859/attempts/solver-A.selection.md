# Does the cyclic group C_3439 admit a (3439,1719,859)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-hadamard-difference-set-3439-1719-859`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), Table 5 listing (3439,1719,859) as open among the cyclic Hadamard cases up to v = 10000; status rechecked against Daniel M. Gordon, "The La Jolla Difference Set Repository" slides (2019), cyclic-Hadamard slide listing 3439 among the seven small open cases.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Settling the smallest surviving cyclic Hadamard case v = 3439 would plausibly yield a focused note removing one of the seven residual cases below 10000.`
- publication_if_solved_score: `solve_is_basically_the_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `88`
- single_solve_to_paper_fraction: `0.84`
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
- working_packet_path: `artifacts/cyclic-hadamard-difference-set-3439-1719-859/working_packet.md`
- paper_shape: `A short note eliminating or constructing the smallest surviving cyclic Hadamard case below 10000.`

## question
Does the cyclic group C_3439 admit a (3439,1719,859)-difference set?

## canonical_statement
Determine whether the cyclic group C_3439 admits a (3439,1719,859)-difference set.

## intended_statement
Determine whether the cyclic group C_3439 admits a (3439,1719,859)-difference set.

## pre_solve_gate_reason
The exact parameter set is source-anchored in a canonical open table, survives into Gordon's 2019 small-open-case slide, has no attempt-registry conflict, and is theorem-stable because the cyclic group and parameter triple are already the honest title theorem if solved.

## micro_paper_assessment
This is a clean micro-paper lane target: exact, source-anchored, theorem-stable, and already framed by the literature as a residual case whose direct resolution would look like a short paper. The main remaining risk is ordinary novelty checking rather than paper shape.

## hypothetical_title
The cyclic Hadamard difference-set case (3439,1719,859).

## hypothetical_abstract
We determine whether the cyclic group C_3439 admits a (3439,1719,859)-difference set. Baumert and Gordon list this exact parameter set as open in their 2004 table of cyclic Hadamard survivors, and Gordon's 2019 La Jolla Repository slides still retain 3439 among the seven small unresolved cases below 10000. A resolution would therefore stand as the title theorem of a short note removing one explicit residual case from the cyclic Hadamard landscape.

## single_solve_paper_explanation
The literature already packages the frontier as a named residual table entry, so solving the exact case would supply the core mathematical contribution immediately. Little beyond a careful writeup, a bounded prior-art note, and the proof certificate would remain. Because the group is uniquely cyclic and the family label is already canonical, the honest paper title does not need to drift after the solve.

## broader_theorem_nonimplication_note
The canonical 2004 table explicitly leaves 3439 open while marking six nearby cases as already eliminated by Lander's theorems, and the 2019 slides still list 3439 as unresolved. The surfaced literature therefore does not already collapse this case into a broader published theorem.

## literature_gap
Baumert-Gordon 2004 Table 5 leaves the exact cyclic Hadamard parameter set (3439,1719,859) open, and Gordon's 2019 slides continue to list 3439 among the small surviving cases without a later exact settlement.

## publication_packet_title
On the Cyclic Hadamard Difference-Set Case (3439,1719,859)

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 5 isolates (3439,1719,859) as open, and Gordon's 2019 La Jolla Repository slides still list 3439 among the seven small open cyclic Hadamard cases.

## publication_packet_near_paper_reason
One exact solve would already remove a named residual case from a standard open-case table in a classical family. The remaining work is mostly exposition, literature placement, and a compact arithmetic certificate.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 5, Gordon's 2019 La Jolla Difference Set Repository slides on cyclic Hadamard cases, the local attempt/source/paper/search memory, and bounded exact-tuple status searches that did not surface a later settlement.

## publication_packet_artifact_requirements
A proof or disproof for the cyclic group of order 3439, the decisive character-sum or multiplier obstruction on n = 860, and a short literature note explaining why 3439 remains outside the already eliminated neighboring cases.

## paper_shape
A short note eliminating or constructing the smallest surviving cyclic Hadamard case below 10000.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 5 isolates (3439,1719,859) as an open cyclic Hadamard case.
- The same table shows six nearby cyclic Hadamard cases already eliminated by specific theorems from Lander's book, so the remaining case sits just beyond current off-the-shelf eliminations.
- Gordon's 2019 slides still list 3439 among the seven small open cyclic Hadamard cases below 10000.
- Any cyclic difference set must satisfy the standard group-ring and character equations D D^(-1) = n + lambda G and |chi(D)|^2 = n for nontrivial characters.

### toy_example
Compare 3439 with the neighboring excluded case 4623 from the same 2004 table to see exactly where existing Lander-type eliminations stop.

### known_obstruction
The standard cyclic Hadamard restrictions already kill several nearby cases, so any proof for 3439 must exploit a finer arithmetic obstruction rather than replaying the textbook eliminations.

### prior_work_stop_sentence
The literature surface used here stops at listing (3439,1719,859) as an exact open cyclic Hadamard case and does not provide a later case-specific resolution.

### recommended_first_attack
Exploit the factorization n = 860 = 2^2 * 5 * 43 together with multiplier and character-sum constraints in the cyclic group of order 3439.

### paper_if_solved
If solved exactly, the paper would be a short note removing the cyclic Hadamard case (3439,1719,859) from the small-open-case list.
