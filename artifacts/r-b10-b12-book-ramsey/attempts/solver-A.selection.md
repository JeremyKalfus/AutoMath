# Determine the exact value of R(B10, B12)

- entry_type: `paper_candidate`
- slug: `r-b10-b12-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3 items (g)-(h); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), Theorem 2 and appendix benchmarks; and bounded exact-term and alternate-notation web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing R(B10, B12) would already support a compact exact-value note on the unresolved B_{n-2} versus B_n book Ramsey line just beyond the classical small table.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `86`
- single_solve_to_paper_fraction: `0.86`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
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
- working_packet_path: `artifacts/r-b10-b12-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the almost-diagonal book Ramsey line.`

## question
Is R(B10, B12) = 45 or 46?

## canonical_statement
Determine the exact value of R(B10, B12).

## intended_statement
Either prove that every graph on 45 vertices contains B10 or its complement contains B12 and thus show R(B10, B12) = 45, or construct a 45-vertex graph avoiding B10 whose complement avoids B12 and thus show R(B10, B12) = 46.

## pre_solve_gate_reason
The thin-memory sweep found no prior attempt on this exact pair. The 2025 book-Ramsey paper gives 45 <= R(B10, B12), DS1.17 item 5.3.g gives R(B10, B12) <= 46, Wesley 2026 settles the adjacent line R(B11, B12) = 47 but not this pair, and the bounded exact-term and alternate-notation searches on 2026-04-13 did not surface a later exact closure.

## micro_paper_assessment
Pass. This is a one-gap exact target on a live, recently updated family line, and solving it would already yield the title theorem and most of the content of a short note.

## hypothetical_title
The Exact Value of R(B10, B12)

## hypothetical_abstract
We determine the book Ramsey number R(B10, B12). Existing public bounds leave this almost-diagonal case in the one-gap window 45 <= R(B10, B12) <= 46. Our result closes a clean unresolved point on the B_{n-2} versus B_n line, adjacent to the recently settled B_{n-1} versus B_n family.

## single_solve_paper_explanation
One exact solve is already the honest title theorem. The surrounding family context, notation, and neighboring benchmarks are already in place in DS1.17, the 2025 book-Ramsey paper, and Wesley 2026, so little remains beyond the proof or witness, a short comparison paragraph, and routine exposition. That places the solve-to-paper fraction comfortably inside the target band.

## broader_theorem_nonimplication_note
Wesley 2026 proves R(B_{n-1}, B_n) = 4n - 1 for n <= 20, but that theorem does not determine R(B_{n-2}, B_n). For n = 12, DS1.17 still gives only the general upper bound 46, while the 2025 paper gives the lower bound 45.

## literature_gap
Current public sources support only 45 <= R(B10, B12) <= 46, and the bounded 2026-04-13 exact-term and alternate-notation audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B10, B12)

## publication_packet_frontier_basis
Current public sources leave this almost-diagonal book pair in the one-gap window 45 <= R(B10, B12) <= 46. The 2025 theorem supplies the lower bound, DS1.17 still routes the upper bound through the general book inequality, and Wesley 2026 closes the neighboring B_{n-1} versus B_n line without determining this B_{n-2} versus B_n case.

## publication_packet_near_paper_reason
If this one-gap case is closed, the note is almost finished immediately: state the exact value, give the forcing proof or extremal witness, compare to the adjacent solved B11 versus B12 case, and explain why the broader line still stops here. That is already the title theorem and most of the narrative.

## publication_packet_literature_scope
DS1.17 Section 5.3, Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Wesley 2026 Theorem 2 and appendix benchmarks, plus bounded exact-term and alternate-notation web searches on 2026-04-13.

## publication_packet_artifact_requirements
Either a proof that every 45-vertex graph forces B10 or a complement B12, or one explicit 45-vertex witness graph avoiding B10 whose complement avoids B12.

## paper_shape
A one-theorem exact-value note on the almost-diagonal book Ramsey line.

## transfer_kit

### usable_lemmas
- Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 45 <= R(B10, B12).
- DS1.17 item 5.3.g gives R(B10, B12) <= 2(10 + 12 + 1) = 46.
- Wesley 2026 gives the adjacent exact benchmark R(B11, B12) = 47 via the solved B_{n-1} versus B_n line.

### toy_example
The neighboring exact case R(B11, B12) = 47 is the smallest solved benchmark directly above the target on the same family corridor.

### known_obstruction
A proof of 45 must eliminate every 45-vertex critical configuration compatible with the known lower-bound constructions, while a proof of 46 needs one explicit 45-vertex witness extending the current 44-vertex lower-bound paradigm.

### prior_work_stop_sentence
Current sources stop at the one-gap window 45 <= R(B10, B12) <= 46.

### recommended_first_attack
Start from the 2025 polycirculant lower-bound construction at 44 vertices and test whether any 45-vertex extension survives before attempting a global forcing proof at 45.

### paper_if_solved
The paper would be a short exact-value note closing a one-gap almost-diagonal book Ramsey case.
