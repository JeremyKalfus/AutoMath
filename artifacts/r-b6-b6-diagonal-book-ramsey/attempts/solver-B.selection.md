# Determine the exact value of R(B6, B6)

- entry_type: `paper_candidate`
- slug: `r-b6-b6-diagonal-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `Maksim V. Pchelintsev, Peter Rath, and Sebastian Angeltveit, "New lower and upper bounds on Ramsey numbers" (Electronic Journal of Combinatorics 32(4) (2025), #P4.64), Theorem 1 and the note immediately following it, which imply 25 <= R(B6, B6) <= 26; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026), 114913) as independent recent family context and bounded 2026-04-14 web checks that did not reveal a later exact closure.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B6, B6) would support a short note closing another one-step diagonal book Ramsey gap in the recent family table.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `86`
- single_solve_to_paper_fraction: `0.84`
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
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b6-b6-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a diagonal book Ramsey number left at a one-step interval.`

## question
Is R(B6, B6) equal to 25 or 26?

## canonical_statement
Determine the exact value of R(B6, B6).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 6-page book graph B6.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior mathematical status or near-duplicate slug for the exact diagonal case R(B6, B6) across the thin memory files, selected_problem.md, PROOFS.md, and artifact directory names. The bounded 2026-04-14 literature check found only the 2025 EJC interval 25 <= R(B6, B6) <= 26, plus the 2026 Wesley paper as current family context, and no later exact value.

## micro_paper_assessment
Pass. This is a narrow, stable, current frontier slice with strong family anchor and low editorial overhead.

## hypothetical_title
The Exact Value of R(B6, B6)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B6, B6). The current literature leaves this parameter in the interval 25 <= R(B6, B6) <= 26. Our result closes one of the sharp one-step gaps remaining in the recent diagonal book Ramsey table.

## single_solve_paper_explanation
The exact value itself would already be the paper's title theorem. The surrounding family story is cheap because recent papers have already organized the diagonal-book landscape into exact cases and one-step exceptions. After the solve, little remains beyond presenting the proof or extremal coloring cleanly.

## broader_theorem_nonimplication_note
The family theorem stops at 25 <= R(B6, B6) <= 26, and the usual exactness shortcut does not fire because 25 is a sum of two squares. No broader result located in the bounded audit closes the remaining step automatically.

## literature_gap
Current public sources stop at 25 <= R(B6, B6) <= 26.

## publication_packet_title
The Exact Value of R(B6, B6)

## publication_packet_frontier_basis
Recent family results leave the diagonal case at 25 <= R(B6, B6) <= 26, and 25 = 3^2 + 4^2 so the standard exactness shortcut does not settle it. This makes the case a genuine open one-step slice inside an active family rather than a disguised corollary.

## publication_packet_near_paper_reason
A clean exact solve would already provide the paper's theorem statement, proof, and computational or structural core. The remaining packaging would be a short family-context section and a compact certificate or contradiction record.

## publication_packet_literature_scope
2025 EJC P4.64 Theorem 1 and note, the 2026 Wesley paper for independent family context, plus bounded 2026-04-14 exact-notation and recent-status web checks.

## publication_packet_artifact_requirements
Either a monochromatic-book-free coloring of K25 or a proof that every coloring of K26 forces a monochromatic B6, with a compact verification artifact.

## paper_shape
A one-theorem exact-value note for a diagonal book Ramsey number left at a one-step interval.

## transfer_kit

### usable_lemmas
- Pchelintsev, Rath, and Angeltveit (2025), Theorem 1, implies R(B6, B6) >= 25.
- The same theorem implies R(B6, B6) <= 26.
- The note after Theorem 1 gives exactness when 4n + 1 is not a sum of two squares, but this does not settle n = 6 because 25 = 3^2 + 4^2.
- The 2026 Wesley paper provides recent lower-bound constructions and confirms that book Ramsey lower-bound technology is still actively advancing.

### toy_example
The exact solved case R(B8, B8) = 33 is a nearby diagonal-book benchmark showing the intended paper shape after an exact closure.

### known_obstruction
A lower-bound proof needs a K25 coloring with no monochromatic B6, while an upper-bound proof must show that every K26 coloring already creates a B6 in one color.

### prior_work_stop_sentence
Current sources stop at 25 <= R(B6, B6) <= 26.

### recommended_first_attack
Begin from the recent constructive lower-bound templates for books and test whether a K25 critical coloring can survive the monochromatic common-neighbor constraints forced by the B6 target.

### paper_if_solved
The paper would be a short exact-value note on a diagonal book Ramsey number currently trapped in a one-step interval.
