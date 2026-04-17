# Untitled Entry

- entry_type: `paper_candidate`
- slug: `r-b12-b14-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g), together with Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1, and William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026).`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `Closing R(B12, B14) would already support a compact note on unresolved almost-diagonal book Ramsey numbers.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short-medium`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `69`
- single_solve_to_paper_fraction: `0.7`
- title_theorem_strength: `moderate`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
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
- packaging_risk: `moderate`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/r-b12-b14-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the B_{n-2} versus B_n book line.`

## question
Either prove that every graph on 53 vertices contains B12 or its complement contains B14 and thus show R(B12, B14) = 53, or construct a 53-vertex graph avoiding B12 whose complement avoids B14 and thus show R(B12, B14) = 54.

## canonical_statement
Determine the exact value of R(B12, B14).

## intended_statement
Either prove that every graph on 53 vertices contains B12 or its complement contains B14 and thus show R(B12, B14) = 53, or construct a 53-vertex graph avoiding B12 whose complement avoids B14 and thus show R(B12, B14) = 54.

## pre_solve_gate_reason
The target is still a one-gap exact endpoint in a named near-diagonal family, with bounded post-solve residue and no evidence of absorption by the exact B_{n-1} versus B_n theorem.

## micro_paper_assessment
Pass, though less forcefully than the top slot. The family anchor is still strong enough that one clean solve would plausibly carry almost all of the resulting note.

## hypothetical_title
The Exact Value of R(B12, B14)

## hypothetical_abstract
We determine the book Ramsey number R(B12, B14). Existing work leaves this almost-diagonal case in the one-gap window 53 <= R(B12, B14) <= 54. Our result closes another small residue on the recent B_{n-2} versus B_n frontier.

## single_solve_paper_explanation
The exact value would still be the honest title theorem, and the surrounding paper would stay short. Because the family framework is already standardized by recent book-Ramsey work, the post-solve packaging is mostly limited to the proof or witness and a short discussion of adjacent solved cases. That keeps the solve-to-paper fraction at the lower edge of the preferred band.

## broader_theorem_nonimplication_note
The exact B_{n-1} versus B_n theorem gives R(B13, B14) = 55 but does not imply R(B12, B14). For this pair, the current almost-diagonal source supplies the lower bound only, while the older general upper-bound machinery still leaves a one-gap residue.

## literature_gap
Current public sources support only the one-gap window 53 <= R(B12, B14) <= 54, and the bounded 2026-04-14 audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B12, B14)

## publication_packet_frontier_basis
Current public sources leave this pair in the one-gap window 53 <= R(B12, B14) <= 54. The lower bound comes from the 2025 almost-diagonal theorem, while the best public upper bound still comes from the DS1.17 general book inequality rather than a dedicated exact argument.

## publication_packet_near_paper_reason
The note stays short once the exact value is known. After the solve, the remaining work is mostly the proof or witness, a short comparison with the neighboring exact case R(B13, B14) = 55, and a brief explanation of why the exact B_{n-1} versus B_n line does not subsume the target.

## publication_packet_literature_scope
DS1.17 Section 5.3(g), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Wesley 2026 Theorem 2 and appendix benchmarks, and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14, plus local 2026-04-15 attempt-registry conflict checks.

## publication_packet_artifact_requirements
Either a proof that every 53-vertex graph forces B12 or a complement B14, or one explicit 53-vertex witness graph avoiding B12 whose complement avoids B14.

## paper_shape
A one-theorem exact-value note on the B_{n-2} versus B_n book line.

## transfer_kit

### usable_lemmas
- Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 53 <= R(B12, B14).
- DS1.17 Section 5.3(g) gives R(B12, B14) <= 2(12 + 14 + 1) = 54.
- Wesley 2026 and the survey give the exact neighboring value R(B13, B14) = 55.

### toy_example
The exact case R(B13, B14) = 55 is the nearest solved off-diagonal benchmark above the target.

### known_obstruction
A proof of 53 must eliminate every 53-vertex critical graph compatible with the current lower bound, while a proof of 54 needs one explicit 53-vertex witness graph avoiding B12 whose complement avoids B14.

### prior_work_stop_sentence
Current sources stop at the one-gap window 53 <= R(B12, B14) <= 54.

### recommended_first_attack
Begin from the 2025 almost-diagonal lower-bound templates and compare them to the exact neighboring B13 versus B14 line, looking for a short structural obstruction before any witness search.

### paper_if_solved
The paper would be a short exact-value note on a fresh almost-diagonal book Ramsey case.
