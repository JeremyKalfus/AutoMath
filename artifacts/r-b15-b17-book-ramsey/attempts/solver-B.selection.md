# Determine the exact value of R(B15, B17)

- entry_type: `paper_candidate`
- slug: `r-b15-b17-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), Theorem 2 and appendix benchmarks; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `Closing R(B15, B17) would already support a short exact-value note on the unresolved almost-diagonal book Ramsey strip.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `75`
- single_solve_to_paper_fraction: `0.76`
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
- working_packet_path: `artifacts/r-b15-b17-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the almost-diagonal book Ramsey line.`

## question
Is R(B15, B17) = 65 or 66?

## canonical_statement
Determine the exact value of R(B15, B17).

## intended_statement
Either prove that every graph on 65 vertices contains B15 or its complement contains B17 and thus show R(B15, B17) = 65, or construct a 65-vertex graph avoiding B15 whose complement avoids B17 and thus show R(B15, B17) = 66.

## pre_solve_gate_reason
The thin-memory sweep found no prior mathematical status on this exact pair in queue.json, paper_memory, search_memory, or failed_problems. The 2025 book-Ramsey theorem gives 65 <= R(B15, B17), DS1.17 Section 5.3(g) gives R(B15, B17) <= 66, Wesley 2026 settles the adjacent line R(B16, B17) = 67 without determining this pair, and the bounded 2026-04-14 exact-term and alternate-notation audit did not surface a later exact closure.

## micro_paper_assessment
Pass. This remains a one-gap exact target on a recent family frontier, and the solve would already carry most of the note's mathematical and editorial content.

## hypothetical_title
The Exact Value of R(B15, B17)

## hypothetical_abstract
We determine the book Ramsey number R(B15, B17). Existing public sources leave this almost-diagonal pair in the one-gap window 65 <= R(B15, B17) <= 66. Our result removes another clean frontier residue from the B_{n-2} versus B_n book Ramsey line.

## single_solve_paper_explanation
The exact value would already be the central theorem of the note. Family framing, old upper-bound technology, and the recent lower-bound source are already available, so the solve does most of the real work. The remaining editorial load is small enough for the micro-paper lane.

## broader_theorem_nonimplication_note
The known exact theorem for R(B_{n-1}, B_n) gives R(B16, B17) = 67 but does not settle R(B15, B17). For n = 17, public sources still leave only the one-gap interval 65 <= R(B15, B17) <= 66.

## literature_gap
Current public sources support only 65 <= R(B15, B17) <= 66, and the bounded 2026-04-14 exact-term and alternate-notation audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B15, B17)

## publication_packet_frontier_basis
Public sources leave this pair in the one-gap window 65 <= R(B15, B17) <= 66. The 2025 theorem provides the lower bound, DS1.17 continues to provide only the general upper bound, and Wesley 2026 resolves the adjacent B16 versus B17 case rather than this one.

## publication_packet_near_paper_reason
The write-up after a successful solve is short and standard: exact statement, forcing proof or extremal graph, one comparison with the solved R(B16, B17) benchmark, and a brief discussion of why the broader almost-diagonal line remains open. That is enough for a clean note.

## publication_packet_literature_scope
DS1.17 Section 5.3(g), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Wesley 2026 Theorem 2 and appendix benchmarks, plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches on 2026-04-14.

## publication_packet_artifact_requirements
Either a proof that every 65-vertex graph forces B15 or a complement B17, or one explicit 65-vertex witness graph avoiding B15 whose complement avoids B17.

## paper_shape
A one-theorem exact-value note on the almost-diagonal book Ramsey line.

## transfer_kit

### usable_lemmas
- Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 65 <= R(B15, B17).
- DS1.17 Section 5.3(g) gives R(B15, B17) <= 2(15 + 17 + 1) = 66.
- Wesley 2026 gives the adjacent exact benchmark R(B16, B17) = 67.

### toy_example
The neighboring exact case R(B16, B17) = 67 is the nearest solved comparison immediately above the target.

### known_obstruction
A 66-proof needs a 65-vertex avoiding graph, while a 65-proof must show that the structured lower-bound templates fail to extend one more vertex.

### prior_work_stop_sentence
Current sources stop at the one-gap window 65 <= R(B15, B17) <= 66.

### recommended_first_attack
Treat the 65-vertex witness question as the first branch, because a failed extension search would immediately sharpen the case for a forcing proof at 65.

### paper_if_solved
The paper would be a short exact-value note on an unresolved almost-diagonal book Ramsey pair.
