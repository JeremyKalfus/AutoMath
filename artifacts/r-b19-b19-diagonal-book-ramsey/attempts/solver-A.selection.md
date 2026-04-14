# Determine the exact value of R(B19, B19)

- entry_type: `paper_candidate`
- slug: `r-b19-b19-diagonal-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 77 <= R(B19, B19) <= 78; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)) as a recent family-status and citation check; and bounded 2026-04-14 exact-statement, alternate-notation, canonical-source, and recent-status web checks that did not reveal a later exact determination.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B19, B19) would still read as the title theorem of a short note because the public frontier is already a one-step diagonal book Ramsey gap.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `74`
- single_solve_to_paper_fraction: `0.73`
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
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b19-b19-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a diagonal book Ramsey number just beyond the previously queued small diagonal range.`

## question
Is R(B19, B19) equal to 77 or 78?

## canonical_statement
Determine the exact value of R(B19, B19).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B19.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this exact tuple, slug, title, or canonical-source anchor. The bounded audit recovered the 77-78 interval from the 2025 lemma and did not surface a later exact closure in 2026-status searches.

## micro_paper_assessment
Pass. This is the strongest unattempted continuation of the current diagonal-book micro-paper lane that still keeps the theorem statement stable and paper-shaped.

## hypothetical_title
The Exact Value of R(B19, B19)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B19, B19). Previous work placed this number in the interval 77 <= R(B19, B19) <= 78. Our result closes the remaining one-step gap for this diagonal book pair.

## single_solve_paper_explanation
This target clears the 70-90% paper test because the public frontier is already one endpoint wide in a standard family. A successful solve would already provide the title theorem, the main literature comparison, and the decisive construction or forcing argument. The residue after the solve is mostly short write-up and placement beside nearby solved almost-diagonal cases.

## broader_theorem_nonimplication_note
The broad diagonal-book theory only narrows the problem to a one-step interval and does not decide the endpoint at n = 19. Nearby exact almost-diagonal values do not collapse the diagonal case.

## literature_gap
Current public sources stop at 77 <= R(B19, B19) <= 78.

## publication_packet_title
The Exact Value of R(B19, B19)

## publication_packet_frontier_basis
Current public sources leave the diagonal book Ramsey number at 77 <= R(B19, B19) <= 78. The family is already publication-legible, so settling the endpoint would itself be the main theorem of a short note.

## publication_packet_near_paper_reason
If the endpoint 77 versus 78 is settled, the note already has its title theorem, its literature comparison, and its main artifact. What remains after the solve is mainly compact exposition rather than a second theorem program.

## publication_packet_literature_scope
2025 EJC Lemma 1 for the one-step interval and neighboring exact almost-diagonal values, 2026 Wesley for recent book-Ramsey frontier context, and bounded 2026-04-14 exact-statement, synonym, and status searches.

## publication_packet_artifact_requirements
Either an explicit 77-vertex coloring avoiding monochromatic B19 or a compact proof that every 78-vertex coloring forces B19.

## paper_shape
A one-theorem exact-value note for a diagonal book Ramsey number just beyond the previously queued small diagonal range.

## transfer_kit

### usable_lemmas
- Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 77 <= R(B19, B19) <= 78.
- The same lemma gives the exact neighboring almost-diagonal value R(B18, B19) = 75.
- The 2025 paper's proof setup reduces book forcing to common-neighborhood counts along a spine edge.
- Wesley (2026) confirms that recent lower-bound constructions continue to populate this family without reporting an exact closure for B19.

### toy_example
The exact neighboring almost-diagonal case R(B18, B19) = 75 is the nearest solved benchmark for the intended theorem shape.

### known_obstruction
Structured near-extremal colorings persist in the diagonal-book family, so any upper-bound proof must rule out a nontrivial but still compact critical class.

### prior_work_stop_sentence
Current public sources stop at 77 <= R(B19, B19) <= 78.

### recommended_first_attack
Exploit the common-neighborhood spine count used throughout the book-Ramsey literature and test whether every 77-vertex near-extremal coloring extends to a forced B19 on one additional vertex.

### paper_if_solved
The paper would be a short exact-value note settling a one-step diagonal book Ramsey gap.
