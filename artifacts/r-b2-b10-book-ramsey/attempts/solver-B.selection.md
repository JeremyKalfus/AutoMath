# Determine the exact value of R(B2, B10)

- entry_type: `paper_candidate`
- slug: `r-b2-b10-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1 and Appendix A, together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 5.3, William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), and bounded exact-term, alternate-notation, and recent-status web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Resolving the one-gap window for R(B2, B10) would already support a standalone short note in the small-book Ramsey program.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `82`
- single_solve_to_paper_fraction: `0.79`
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
- working_packet_path: `artifacts/r-b2-b10-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on a small off-diagonal book Ramsey number.`

## question
Is R(B2, B10) = 25 or 26?

## canonical_statement
Determine the exact value of R(B2, B10).

## intended_statement
Either prove that every graph on 25 vertices contains B2 or has a complement containing B10 and thus show R(B2, B10) = 25, or construct a 25-vertex graph with no B2 and no complement B10 and thus show R(B2, B10) = 26.

## pre_solve_gate_reason
The 2025 books-and-wheels paper narrows the pair to 25 <= R(B2, B10) <= 26 and records a concrete lower-bound witness; no later exact-resolution paper surfaced in the bounded 2026-04-13 audit.

## micro_paper_assessment
Pass. This is a narrow one-gap residue in a named exact-value family, with enough surrounding structure that one solve would already read like a complete note.

## hypothetical_title
The Exact Value of R(B2, B10)

## hypothetical_abstract
We determine the exact Ramsey number R(B2, B10) for book graphs. Current literature narrows this value to the one-gap window 25 <= R(B2, B10) <= 26 using explicit lower-bound constructions and flag-algebra upper bounds. Our theorem converts that narrow unresolved residue into an exact entry in the small-book Ramsey table and sharpens one of the cleanest remaining B2-versus-Bn cases.

## single_solve_paper_explanation
A sharp determination of R(B2, B10) is already the title theorem and the main body of the paper. The published witness, family context, and neighboring solved instances do most of the setup work in advance, so what remains after the solve is mostly exposition and a compact extremal appendix. The solve-to-paper distance is therefore short.

## broader_theorem_nonimplication_note
Known exact and asymptotic book results cover diagonal or near-diagonal families and large-parameter ranges; they do not imply the exact small asymmetric pair R(B2, B10).

## literature_gap
The 2025 books-and-wheels paper leaves 25 <= R(B2, B10) <= 26, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B2, B10)

## publication_packet_frontier_basis
The 2025 books-and-wheels paper records 25 <= R(B2, B10) <= 26 and supplies a 24-vertex witness, DS1.18 still treats the small-book table as incomplete in this zone, Wesley's 2026 lower-bounds paper improves book lower bounds but does not report an exact solution for this pair, and bounded exact-term plus recent-status searches on 2026-04-13 did not surface a later exact-resolution paper.

## publication_packet_near_paper_reason
This is already a one-gap exact target with a published critical witness and a mature family backdrop. After the solve, the note would mainly need the forcing proof or new 25-vertex obstruction and a short comparison with nearby B2-versus-Bn values.

## publication_packet_literature_scope
Lidicky-McKinley-Pfender-Van Overberghe 2025, DS1.18 Section 5.3, Wesley 2026, and bounded 2026-04-13 exact-statement, alternate-notation, and recent-status searches for R(B2, B10).

## publication_packet_artifact_requirements
Either a proof that every 25-vertex graph contains B2 or has complement containing B10, or one explicit 25-vertex graph avoiding both.

## paper_shape
A one-theorem exact-value note on a small off-diagonal book Ramsey number.

## transfer_kit

### usable_lemmas
- Lidicky-McKinley-Pfender-Van Overberghe 2025 proves R(B2, B10) <= 26.
- The same paper gives a published 24-vertex construction establishing R(B2, B10) >= 25.
- The same table records the exact neighboring value R(B2, B8) = 21 and the still-open but tighter window 22 <= R(B2, B9) <= 24, giving immediate local comparison points.

### toy_example
The sequence around the target now reads R(B2, B8) = 21, 22 <= R(B2, B9) <= 24, and 25 <= R(B2, B10) <= 26.

### known_obstruction
Any proof of R(B2, B10) = 25 must eliminate every 25th-vertex extension of the known 24-vertex witness class, while a proof of R(B2, B10) = 26 needs one explicit 25-vertex graph avoiding both B2 and complement B10.

### prior_work_stop_sentence
Current sources leave R(B2, B10) in the one-gap window 25 <= R(B2, B10) <= 26.

### recommended_first_attack
Use the published 24-vertex obstruction as the base case and classify whether any 25th-vertex attachment can preserve both forbidden configurations.

### paper_if_solved
The paper would be a short exact-value note on a one-gap B2-versus-B10 book Ramsey problem.
