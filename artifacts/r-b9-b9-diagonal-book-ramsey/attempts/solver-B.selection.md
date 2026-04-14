# Determine the exact value of R(B9, B9)

- entry_type: `paper_candidate`
- slug: `r-b9-b9-diagonal-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `Maksim V. Pchelintsev, Peter Rath, and Sebastian Angeltveit, "New lower and upper bounds on Ramsey numbers" (Electronic Journal of Combinatorics 32(4) (2025), #P4.64), Theorem 1 and the note immediately following it, which imply 37 <= R(B9, B9) <= 38; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026), 114913) as independent recent family context and bounded 2026-04-14 web checks that did not reveal a later exact closure.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B9, B9) would support a clean short note closing another one-step diagonal book Ramsey interval in the active recent table.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `82`
- single_solve_to_paper_fraction: `0.81`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
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
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b9-b9-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a diagonal book Ramsey number currently trapped in a one-step gap.`

## question
Is R(B9, B9) equal to 37 or 38?

## canonical_statement
Determine the exact value of R(B9, B9).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 9-page book graph B9.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior mathematical status or near-duplicate slug for R(B9, B9) in the thin memory files, selected_problem.md, PROOFS.md, or artifact directory names. The bounded 2026-04-14 literature check found the interval 37 <= R(B9, B9) <= 38 in the 2025 EJC source, the 2026 Wesley paper as recent family context, and no later exact closure.

## micro_paper_assessment
Pass. The interval is tiny, the family anchor is strong, and a single exact solve would already carry most of the paper.

## hypothetical_title
The Exact Value of R(B9, B9)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B9, B9). Recent work leaves this parameter in the interval 37 <= R(B9, B9) <= 38. Our result closes a remaining one-step gap in the current exact table for small diagonal book Ramsey numbers.

## single_solve_paper_explanation
The exact value would already be the honest title theorem of the note. The family is current and structured enough that the post-solve writing burden is light. This keeps the solve-to-publication distance inside the strict micro-paper lane.

## broader_theorem_nonimplication_note
The best general diagonal-book theorem only narrows the case to two adjacent values, and the non-sum-of-two-squares exactness shortcut does not apply because 37 is a sum of two squares. No broader published result located in the bounded search decides the case.

## literature_gap
Current public sources stop at 37 <= R(B9, B9) <= 38.

## publication_packet_title
The Exact Value of R(B9, B9)

## publication_packet_frontier_basis
The recent diagonal-book theorem leaves a one-step gap 37 <= R(B9, B9) <= 38, and 37 = 1^2 + 6^2 so the available exactness shortcut again does not resolve the case. The slice is therefore still frontier-novel and paper-shaped if closed exactly.

## publication_packet_near_paper_reason
If the exact value is found, the witness or forcing argument is already almost the entire paper. Only a short literature paragraph and the final certificate packaging remain.

## publication_packet_literature_scope
2025 EJC P4.64 Theorem 1 and note, the 2026 Wesley paper, plus bounded 2026-04-14 exact-notation and recent-status web checks.

## publication_packet_artifact_requirements
Either a monochromatic-book-free coloring of K37 or a proof that every coloring of K38 forces a monochromatic B9, together with a compact verification artifact.

## paper_shape
A one-theorem exact-value note for a diagonal book Ramsey number currently trapped in a one-step gap.

## transfer_kit

### usable_lemmas
- Pchelintsev, Rath, and Angeltveit (2025), Theorem 1, implies R(B9, B9) >= 37.
- The same theorem implies R(B9, B9) <= 38.
- The note after Theorem 1 leaves the case unresolved because 37 is a sum of two squares.
- The 2026 Wesley paper shows the family is still seeing new constructive lower-bound input, supporting the relevance of an exact closure.

### toy_example
The exact value R(B8, B8) = 33 from the same recent family paper is the closest solved diagonal benchmark.

### known_obstruction
A lower-bound proof must realize a K37 coloring avoiding monochromatic B9, while an upper-bound proof must rule out all such critical colorings.

### prior_work_stop_sentence
Current sources stop at 37 <= R(B9, B9) <= 38.

### recommended_first_attack
Use the recent book-Ramsey constructions as a starting point and look for a rigid common-neighbor profile that either extends to K37 or proves impossible at K38.

### paper_if_solved
The paper would be a short exact-value note closing a one-step diagonal-book Ramsey gap.
