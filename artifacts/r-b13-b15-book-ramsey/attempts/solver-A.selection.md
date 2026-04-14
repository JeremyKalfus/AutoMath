# Determine the exact value of R(B13, B15)

- entry_type: `paper_candidate`
- slug: `r-b13-b15-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3 items (g)-(h); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), Theorem 2 and appendix benchmarks; and bounded exact-term and alternate-notation web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing R(B13, B15) would already support a short exact-value note on the unresolved almost-diagonal book Ramsey strip.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `79`
- single_solve_to_paper_fraction: `0.8`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
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
- working_packet_path: `artifacts/r-b13-b15-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the almost-diagonal book Ramsey line.`

## question
Is R(B13, B15) = 57 or 58?

## canonical_statement
Determine the exact value of R(B13, B15).

## intended_statement
Either prove that every graph on 57 vertices contains B13 or its complement contains B15 and thus show R(B13, B15) = 57, or construct a 57-vertex graph avoiding B13 whose complement avoids B15 and thus show R(B13, B15) = 58.

## pre_solve_gate_reason
The thin-memory sweep found no prior attempt on this exact pair. The 2025 book-Ramsey paper gives 57 <= R(B13, B15), DS1.17 item 5.3.g gives R(B13, B15) <= 58, Wesley 2026 settles the adjacent line R(B14, B15) = 59 but not this pair, and the bounded exact-term and alternate-notation searches on 2026-04-13 did not surface a later exact closure.

## micro_paper_assessment
Pass. This is still a one-gap frontier statement with a strong family anchor and low editorial overhead, so one solve would already do most of the publication work.

## hypothetical_title
The Exact Value of R(B13, B15)

## hypothetical_abstract
We determine the book Ramsey number R(B13, B15). Existing public sources leave this almost-diagonal pair in the one-gap window 57 <= R(B13, B15) <= 58. Our result removes a clean frontier residue from the B_{n-2} versus B_n book Ramsey line.

## single_solve_paper_explanation
The exact determination would itself be the note's main theorem. Because the relevant bounds, neighboring exact values, and family notation are already in the literature, very little feeder work remains after the solve. The post-solve burden is essentially proof presentation plus a concise contextual paragraph.

## broader_theorem_nonimplication_note
The known exact theorem for R(B_{n-1}, B_n) does not settle R(B_{n-2}, B_n). For n = 15, public sources still leave only the one-gap interval 57 <= R(B13, B15) <= 58.

## literature_gap
Current public sources support only 57 <= R(B13, B15) <= 58, and the bounded 2026-04-13 exact-term and alternate-notation audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B13, B15)

## publication_packet_frontier_basis
Public sources leave this pair in the one-gap window 57 <= R(B13, B15) <= 58. The 2025 theorem provides the lower bound, DS1.17 continues to provide only the general upper bound, and Wesley 2026 resolves the adjacent B14 versus B15 case rather than this one.

## publication_packet_near_paper_reason
This target stays paper-shaped after the solve because the exact statement is already crisp and the family story is already written by the surrounding literature. Once the proof or witness exists, the remaining paper is mostly exposition and one comparison paragraph.

## publication_packet_literature_scope
DS1.17 Section 5.3, Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Wesley 2026 Theorem 2 and appendix benchmarks, plus bounded exact-term and alternate-notation web searches on 2026-04-13.

## publication_packet_artifact_requirements
Either a proof that every 57-vertex graph forces B13 or a complement B15, or one explicit 57-vertex witness graph avoiding B13 whose complement avoids B15.

## paper_shape
A one-theorem exact-value note on the almost-diagonal book Ramsey line.

## transfer_kit

### usable_lemmas
- Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 57 <= R(B13, B15).
- DS1.17 item 5.3.g gives R(B13, B15) <= 2(13 + 15 + 1) = 58.
- Wesley 2026 gives the adjacent exact benchmark R(B14, B15) = 59.

### toy_example
The neighboring exact case R(B14, B15) = 59 is the nearest solved comparison immediately above the target.

### known_obstruction
The main obstruction is extending the present 56-vertex lower-bound architecture to 57 vertices; failure there would strongly suggest an upper-bound forcing proof at 57.

### prior_work_stop_sentence
Current sources stop at the one-gap window 57 <= R(B13, B15) <= 58.

### recommended_first_attack
Use the 2025 polycirculant templates as a witness-extension problem first, then pivot to a threshold forcing argument only if every structured 57-vertex extension fails.

### paper_if_solved
The paper would be a short exact-value note closing a one-gap almost-diagonal book Ramsey case.
