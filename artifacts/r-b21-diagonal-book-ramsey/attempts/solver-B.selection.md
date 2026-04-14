# Determine the exact value of R(B21, B21)

- entry_type: `paper_candidate`
- slug: `r-b21-diagonal-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), item 5.3(f); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1 and Appendix A; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026); and bounded exact-term, alternate-notation, canonical-source, and recent-status web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Settling this final small-range diagonal residue would already support a standalone short note in the book Ramsey program.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `low`
- paper_leverage_score: `79`
- single_solve_to_paper_fraction: `0.78`
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
- novelty_check_cost: `low`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b21-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on a diagonal book Ramsey number outside the standard exact criteria.`

## question
Is R(B21, B21) = 85 or 86?

## canonical_statement
Determine the exact value of R(B21, B21).

## intended_statement
Either prove that every graph on 85 vertices contains B21 or has a complement containing B21 and thus show R(B21, B21) = 85, or construct a 85-vertex graph with no B21 and no complement B21 and thus show R(B21, B21) = 86.

## pre_solve_gate_reason
The local thin-memory sweep shows no prior attempt on this tuple, the published diagonal framework gives the sharp one-gap window 85 <= R(B21, B21) <= 86, and the bounded 2026-04-13 audit did not surface a later exact-resolution paper.

## micro_paper_assessment
Pass. The gap is tiny, the theorem slice is stable, and one exact solve would already constitute most of a publishable note.

## hypothetical_title
The Exact Value of R(B21, B21)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B21, B21). Current diagonal criteria leave only the one-gap window 85 <= R(B21, B21) <= 86 because 4n + 1 = 85 is a sum of two squares and not a prime power. Our result closes one of the clean remaining diagonal residues in the exact theory of book Ramsey numbers.

## single_solve_paper_explanation
The exact diagonal value at n = 21 would itself be the title theorem. The family scaffolding, comparison cases, and reason the standard number-theoretic machinery fails are already available in the literature, so the remaining paper work after a solve is mostly contextual exposition and a compact extremal discussion.

## broader_theorem_nonimplication_note
The known diagonal exact criteria do not settle n = 21 because 85 = 2^2 + 9^2 and is not a prime power. A successful proof would still naturally center on this exact diagonal case rather than collapsing into a broader already-known theorem.

## literature_gap
Current public sources support only the one-gap diagonal window 85 <= R(B21, B21) <= 86, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B21, B21)

## publication_packet_frontier_basis
DS1.17 records the exact diagonal criteria tied to prime powers and sums of two squares. The 2025 paper proves 4n + 1 <= R(Bn, Bn) <= 4n + 2 for 4 <= n <= 21 and covers n = 21 in that one-gap framework, while Wesley 2026 improves lower bounds for books but does not report an exact diagonal closure at n = 21.

## publication_packet_near_paper_reason
This is again a mature one-gap diagonal packet rather than a campaign target. Once n = 21 is settled, the note mainly needs the short explanation of why 85 lies outside the standard exact criteria and the argument that closes the two-point window.

## publication_packet_literature_scope
DS1.17 item 5.3(f), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1 and Appendix A, Wesley 2026, and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, and recent-status searches for R(B21, B21).

## publication_packet_artifact_requirements
Either a proof that every 85-vertex graph contains B21 or has complement containing B21, or one explicit 85-vertex graph avoiding B21 in both colors.

## paper_shape
A one-theorem exact-value note on a diagonal book Ramsey number outside the standard exact criteria.

## transfer_kit

### usable_lemmas
- Lidický-McKinley-Pfender-Van Overberghe 2025 proves 4n + 1 <= R(Bn, Bn) <= 4n + 2 for all 4 <= n <= 21, hence 85 <= R(B21, B21) <= 86.
- DS1.17 item 5.3(f) gives the exact diagonal criterion R(Bn, Bn) = 4n + 2 when 4n + 1 is a prime power.
- The same item gives the upper criterion R(Bn, Bn) <= 4n + 1 when 4n + 1 is not a sum of two squares, which does not apply here because 85 is representable as a sum of two squares.

### toy_example
The diagonal family already resolves n = 20 exactly because 81 is a prime power, while n = 21 remains open because 85 escapes both standard exact criteria.

### known_obstruction
Any proof of R(B21, B21) = 85 must exclude every 85-vertex extremal template compatible with the known lower-bound machinery, while a proof of R(B21, B21) = 86 requires one explicit 85-vertex witness avoiding B21 in both a graph and its complement.

### prior_work_stop_sentence
Current sources stop at the one-gap diagonal window 85 <= R(B21, B21) <= 86.

### recommended_first_attack
Push the published diagonal lower-bound templates against degree-common-neighborhood constraints on 85 vertices and force a 21-page book in one color.

### paper_if_solved
The paper would be a short exact-value note closing another diagonal book Ramsey residue outside the standard criteria.
