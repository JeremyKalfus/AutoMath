# Determine the exact value of R(B9, B11)

- entry_type: `paper_candidate`
- slug: `r-b9-b11-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g) and Table IXa; Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1 and appendix witness tables; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), Theorem 2 and appendix benchmarks; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `Closing R(B9, B11) would already support a compact exact-value note on the smallest fresh B_{n-2} versus B_n book Ramsey residue not already parked in canonical memory.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `88`
- single_solve_to_paper_fraction: `0.88`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
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
- working_packet_path: `artifacts/r-b9-b11-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the smallest fresh almost-diagonal book Ramsey residue.`

## question
Is R(B9, B11) = 41 or 42?

## canonical_statement
Determine the exact value of R(B9, B11).

## intended_statement
Either prove that every graph on 41 vertices contains B9 or its complement contains B11 and thus show R(B9, B11) = 41, or construct a 41-vertex graph avoiding B9 whose complement avoids B11 and thus show R(B9, B11) = 42.

## pre_solve_gate_reason
The thin-memory sweep found no prior mathematical status on this exact pair in queue.json, selected_problem memory, paper_memory, search_memory, or failed_problems. The 2025 almost-diagonal theorem gives 41 <= R(B9, B11), DS1.17 Section 5.3(g) still leaves the general upper bound R(B9, B11) <= 42, Wesley 2026 settles the adjacent line R(B10, B11) = 43 without collapsing this case, and the bounded 2026-04-14 exact-term and alternate-notation audit did not surface a later exact closure.

## micro_paper_assessment
Pass. This is the smallest fresh one-gap almost-diagonal book Ramsey target left outside canonical repo memory, with a strong family anchor and an immediate neighboring exact value that gives the note a real paper shape instead of a curiosity shape.

## hypothetical_title
The Exact Value of R(B9, B11)

## hypothetical_abstract
We determine the book Ramsey number R(B9, B11). Existing public sources leave this almost-diagonal case in the one-gap window 41 <= R(B9, B11) <= 42. Our result closes the smallest fresh unresolved point adjacent to the exact neighboring value R(B10, B11) = 43 on the B_{n-2} versus B_n line.

## single_solve_paper_explanation
One exact solve is already the honest title theorem. The literature shell is recent and explicit, so little remains beyond the proof or witness, a short comparison paragraph, and routine exposition around the neighboring exact benchmark. That places the solve-to-paper fraction at the top end of the target band.

## broader_theorem_nonimplication_note
Wesley 2026 proves the exact line R(B_{n-1}, B_n) = 4n - 1 for n <= 20, which gives R(B10, B11) = 43, but that theorem does not determine R(B9, B11). DS1.17 still supplies only the generic upper bound 42 for the target pair.

## literature_gap
Current public sources support only 41 <= R(B9, B11) <= 42, and the bounded 2026-04-14 exact-term and alternate-notation audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B9, B11)

## publication_packet_frontier_basis
Current public sources leave this pair in the one-gap window 41 <= R(B9, B11) <= 42. The lower bound comes from the 2025 almost-diagonal book theorem, the upper bound still comes from the DS1.17 general book inequality, and the latest 2026 exact progress closes the adjacent B10 versus B11 pair rather than this B_{n-2} versus B_n residue.

## publication_packet_near_paper_reason
If this one-gap case is closed, almost all of the note is already determined: exact statement, forcing proof or 41-vertex witness, one comparison with the neighboring exact value R(B10, B11) = 43, and a short paragraph explaining why the broader B_{n-1} versus B_n theorem does not settle the target. That is already the title theorem and most of the editorial payload.

## publication_packet_literature_scope
DS1.17 Section 5.3(g) and Table IXa, Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1 and appendix witness tables, Wesley 2026 Theorem 2 and appendix benchmarks, plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches on 2026-04-14.

## publication_packet_artifact_requirements
Either a proof that every 41-vertex graph forces B9 or a complement B11, or one explicit 41-vertex witness graph avoiding B9 whose complement avoids B11.

## paper_shape
A one-theorem exact-value note on the smallest fresh almost-diagonal book Ramsey residue.

## transfer_kit

### usable_lemmas
- Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 41 <= R(B9, B11).
- DS1.17 Section 5.3(g) gives R(B9, B11) <= 2(9 + 11 + 1) = 42.
- Wesley 2026 gives the adjacent exact benchmark R(B10, B11) = 43 via the solved B_{n-1} versus B_n line.

### toy_example
The neighboring exact case R(B10, B11) = 43 is the nearest solved off-diagonal benchmark directly above the target.

### known_obstruction
A proof of 41 must eliminate every 41-vertex critical configuration compatible with the current lower-bound template, while a proof of 42 needs one explicit 41-vertex witness extending the known 40-vertex paradigm.

### prior_work_stop_sentence
Current sources stop at the one-gap window 41 <= R(B9, B11) <= 42.

### recommended_first_attack
Start from the 2025 almost-diagonal lower-bound template at 40 vertices and test whether any 41st vertex can be added before attempting a global forcing proof at 41.

### paper_if_solved
The paper would be a short exact-value note closing the smallest fresh almost-diagonal book Ramsey case.
