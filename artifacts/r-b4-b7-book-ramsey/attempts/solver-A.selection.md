# Determine the exact value of R(B4, B7)

- entry_type: `paper_candidate`
- slug: `r-b4-b7-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1 and Appendix A, together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 5.3, William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), and bounded exact-term, alternate-notation, and recent-status web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing the remaining one-gap window for R(B4, B7) would already read as the title theorem of a short note on small book Ramsey numbers.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.81`
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
- novelty_check_cost: `low`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b4-b7-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on a narrow unresolved book Ramsey pair.`

## question
Is R(B4, B7) = 22 or 23?

## canonical_statement
Determine the exact value of R(B4, B7).

## intended_statement
Either prove that every graph on 22 vertices contains B4 or has a complement containing B7 and thus show R(B4, B7) = 22, or construct a 22-vertex graph with no B4 and no complement B7 and thus show R(B4, B7) = 23.

## pre_solve_gate_reason
The 2025 books-and-wheels paper leaves only the window 22 <= R(B4, B7) <= 23, and the 2026 lower-bounds paper did not upgrade this pair to an exact value, so one sharp resolution is already the note.

## micro_paper_assessment
Pass. This is a stable one-gap exact-value target inside a named family, and a single clean solve would already look like a complete short note.

## hypothetical_title
The Exact Value of R(B4, B7)

## hypothetical_abstract
We determine the exact Ramsey number R(B4, B7) for book graphs. The current small-Ramsey literature leaves only the one-gap window 22 <= R(B4, B7) <= 23 after the 2025 books-and-wheels paper established the lower and upper bounds. Our theorem closes one of the smallest unresolved off-diagonal book cases and sharpens the current small-book Ramsey table by an exact entry rather than another partial bound.

## single_solve_paper_explanation
The title theorem is already the whole mathematical payload once the pair is settled exactly. The literature already supplies the family context, nearby exact values, and explicit lower-bound templates, so the post-solve work is mainly exposition and a compact extremal appendix. This is comfortably inside the 70-90 percent paper window.

## broader_theorem_nonimplication_note
Known asymptotic and infinite-family book results concern large parameters, diagonal cases, or near-diagonal families such as R(Bn-1, Bn); they do not imply the exact small off-diagonal pair R(B4, B7).

## literature_gap
The 2025 books-and-wheels paper leaves the exact value of R(B4, B7) unresolved between 22 and 23, and no later exact resolution surfaced in the bounded 2026-04-13 audit.

## publication_packet_title
The Exact Value of R(B4, B7)

## publication_packet_frontier_basis
The 2025 books-and-wheels paper records the bounds 22 <= R(B4, B7) <= 23 and gives an explicit lower-bound construction, DS1.18 still lists the small-book family as partially unresolved in this range, Wesley's 2026 lower-bounds paper does not announce an exact value for this pair, and bounded exact-term plus recent-status searches on 2026-04-13 did not surface a later exact-resolution paper.

## publication_packet_near_paper_reason
The family context, neighboring solved small-book cases, and a concrete one-gap window are already in place. After a solve, the remaining work is mostly a short extremal discussion and documentation of the critical 22-vertex obstruction or forcing argument.

## publication_packet_literature_scope
Lidicky-McKinley-Pfender-Van Overberghe 2025, DS1.18 Section 5.3, Wesley 2026, and bounded 2026-04-13 exact-statement, alternate-notation, and recent-status searches for R(B4, B7).

## publication_packet_artifact_requirements
Either a proof that every 22-vertex graph contains B4 or has complement containing B7, or one explicit 22-vertex graph avoiding both.

## paper_shape
A one-theorem exact-value note on a narrow unresolved book Ramsey pair.

## transfer_kit

### usable_lemmas
- Lidicky-McKinley-Pfender-Van Overberghe 2025 proves the upper bound R(B4, B7) <= 23 by flag-algebra methods.
- The same paper provides an explicit 21-vertex lower-bound construction establishing R(B4, B7) >= 22.
- The same table records neighboring exact cases R(B3, B7) = 20 and R(B5, B6) = 23, giving immediate local benchmarks for any stability argument.

### toy_example
The adjacent solved cases R(B3, B7) = 20 and R(B5, B6) = 23 show that the B4-versus-B7 slice sits exactly at the edge of the already-charted small-book table.

### known_obstruction
Any proof of R(B4, B7) = 22 must rule out every 22-vertex extension of the known critical 21-vertex patterns, while a proof of R(B4, B7) = 23 must exhibit one explicit 22-vertex graph avoiding B4 and complement B7.

### prior_work_stop_sentence
Current sources leave R(B4, B7) in the one-gap window 22 <= R(B4, B7) <= 23.

### recommended_first_attack
Start from the published 21-vertex obstruction class and run a structural extendability analysis: prove that every 22nd-vertex extension creates either a B4 or a complement B7 unless a new 22-vertex witness exists.

### paper_if_solved
The paper would be a short exact-value note closing a one-gap off-diagonal book Ramsey number.
