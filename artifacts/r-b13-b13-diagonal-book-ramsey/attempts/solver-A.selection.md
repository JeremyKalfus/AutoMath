# Determine the exact value of R(B13, B13)

- entry_type: `paper_candidate`
- slug: `r-b13-b13-diagonal-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 53 <= R(B13, B13) <= 54; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), used as a bounded recent-status and citation check that did not report an exact closure for B13; and bounded 2026-04-14 exact-statement and alternate-notation web checks that did not reveal a later exact determination.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B13, B13) would read as the title theorem of a short note because the public frontier is already a one-step diagonal book Ramsey gap.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
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
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b13-b13-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a diagonal book Ramsey number.`

## question
Is R(B13, B13) equal to 53 or 54?

## canonical_statement
Determine the exact value of R(B13, B13).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B13.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this exact tuple, slug, or title. The bounded audit recovered the 53-54 interval from Lemma 1 and did not find any later exact closure in the 2026 recent-status search.

## micro_paper_assessment
Pass. This is a stable one-step diagonal book gap with low editorial residue and a clear short-note endpoint if solved.

## hypothetical_title
The Exact Value of R(B13, B13)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B13, B13). Previous work placed this number in the interval 53 <= R(B13, B13) <= 54. Our result closes the remaining one-step gap for a standard diagonal book pair.

## single_solve_paper_explanation
This target passes the 70-90% paper test because the public literature already isolates a single unresolved endpoint. Once the exact value is known, most of the paper is already determined: theorem statement, brief family context, and the main extremal or forcing artifact. No feeder ladder is needed.

## broader_theorem_nonimplication_note
The known diagonal-book theorem only yields the interval 4n + 1 <= R(B_n, B_n) <= 4n + 2, and the recent 2026 lower-bound paper does not close the case n = 13. Exact neighboring values such as R(B12, B13) = 51 do not decide the diagonal endpoint.

## literature_gap
Current public sources stop at 53 <= R(B13, B13) <= 54.

## publication_packet_title
The Exact Value of R(B13, B13)

## publication_packet_frontier_basis
Current public sources leave the diagonal book Ramsey number at 53 <= R(B13, B13) <= 54. This is already a one-step exact frontier in a standard family with exact neighboring book values.

## publication_packet_near_paper_reason
If the endpoint 53 versus 54 is settled, the result already has the shape of a short exact-value paper. The only real residue is the critical coloring or forcing proof and a short comparison with nearby diagonal and almost-diagonal cases.

## publication_packet_literature_scope
2025 EJC paper Lemma 1 for the one-step interval and nearby exact values, 2026 Wesley book-Ramsey paper as a recent-status check, and bounded 2026-04-14 exact-statement, synonym, and citation searches.

## publication_packet_artifact_requirements
Either an explicit 53-vertex coloring avoiding monochromatic B13 or a compact proof that every 54-vertex coloring forces B13.

## paper_shape
A one-theorem exact-value note for a diagonal book Ramsey number.

## transfer_kit

### usable_lemmas
- Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 53 <= R(B13, B13) <= 54.
- The same lemma gives the exact neighboring almost-diagonal value R(B12, B13) = 51.
- The same paper records the exact smaller diagonal benchmark R(B8, B8) = 33.
- Wesley (2026) gives recent book-Ramsey lower-bound progress but does not report an exact closure for B13.

### toy_example
The exact neighboring almost-diagonal case R(B12, B13) = 51 is the closest solved model for a short proof packet in the same corridor.

### known_obstruction
The diagonal family admits many structured lower-bound colorings, so the main difficulty is ruling out the last 53-vertex critical patterns without turning the note into a family-wide project.

### prior_work_stop_sentence
Current sources stop at 53 <= R(B13, B13) <= 54.

### recommended_first_attack
Analyze the Lemma 1 lower-bound construction at order 53 and test whether any extension to 54 vertices inevitably creates a monochromatic B13 through common-neighborhood growth around candidate spines.

### paper_if_solved
The paper would be a short exact-value note settling one diagonal book Ramsey number.
