# Determine the exact value of R(B7, B7)

- entry_type: `paper_candidate`
- slug: `r-b7-b7-diagonal-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Maksim V. Pchelintsev, Peter Rath, and Sebastian Angeltveit, "New lower and upper bounds on Ramsey numbers" (Electronic Journal of Combinatorics 32(4) (2025), #P4.64), Theorem 1 and the note immediately following it, which imply 29 <= R(B7, B7) <= 30; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026), 114913) as independent recent family context and bounded 2026-04-14 web checks that did not reveal a later exact closure.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B7, B7) would already yield a compact note closing another one-step diagonal book Ramsey gap.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.83`
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
- working_packet_path: `artifacts/r-b7-b7-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem note determining one unresolved diagonal book Ramsey value at a one-step gap.`

## question
Is R(B7, B7) equal to 29 or 30?

## canonical_statement
Determine the exact value of R(B7, B7).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 7-page book graph B7.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior mathematical status or near-duplicate slug for R(B7, B7) in the thin memory files, selected_problem.md, PROOFS.md, or artifact directory names. The bounded 2026-04-14 literature check found only the 2025 interval 29 <= R(B7, B7) <= 30, the 2026 Wesley paper as recent family context, and no later exact determination.

## micro_paper_assessment
Pass. It is a stable one-step gap with current literature context and low packaging cost.

## hypothetical_title
The Exact Value of R(B7, B7)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B7, B7). Recent work leaves this value in the interval 29 <= R(B7, B7) <= 30. Our result closes another sharp diagonal-book gap and strengthens the exact small-book Ramsey table.

## single_solve_paper_explanation
A single exact solve would already supply the paper's title theorem and main body. The family narrative is already built in the recent literature, so the post-solve work is minimal. This is substantially closer to paper-ready than a broader campaign-style target.

## broader_theorem_nonimplication_note
The recent theorem bounds the value within one step but does not decide it, and the published exactness shortcut fails because 29 is a sum of two squares. No broader statement found in the bounded audit forces the answer.

## literature_gap
Current public sources stop at 29 <= R(B7, B7) <= 30.

## publication_packet_title
The Exact Value of R(B7, B7)

## publication_packet_frontier_basis
The recent diagonal-book theorem leaves R(B7, B7) at the one-step interval 29 <= R(B7, B7) <= 30, and 29 = 2^2 + 5^2 so the available exactness shortcut does not settle it. The remaining gap is therefore a genuine small frontier claim with immediate table value.

## publication_packet_near_paper_reason
Once the exact value is decided, the proof or witness is already almost the complete note. The rest is limited to a concise family summary and a small verification appendix.

## publication_packet_literature_scope
2025 EJC P4.64 Theorem 1 and note, the 2026 Wesley paper, plus bounded 2026-04-14 exact-notation and recent-status web checks.

## publication_packet_artifact_requirements
Either a B7-free coloring of K29 or a proof that every coloring of K30 forces a monochromatic B7, with a compact certificate.

## paper_shape
A one-theorem note determining one unresolved diagonal book Ramsey value at a one-step gap.

## transfer_kit

### usable_lemmas
- Pchelintsev, Rath, and Angeltveit (2025), Theorem 1, implies R(B7, B7) >= 29.
- The same theorem implies R(B7, B7) <= 30.
- The note after Theorem 1 explains why the non-sum-of-two-squares exactness criterion does not apply here, since 29 is a sum of two squares.
- The 2026 Wesley paper provides independent recent lower-bound progress for book Ramsey numbers and confirms that the family remains active.

### toy_example
The exact solved diagonal case R(B8, B8) = 33 is a nearby benchmark for what the final note would look like.

### known_obstruction
A lower-bound proof needs a K29 coloring avoiding monochromatic B7, while an upper-bound proof must rule out every such critical coloring.

### prior_work_stop_sentence
Current sources stop at 29 <= R(B7, B7) <= 30.

### recommended_first_attack
Test whether the recent constructive templates for diagonal books can be extended to K29, and if not, turn the failure pattern into a focused common-neighbor forcing argument for K30.

### paper_if_solved
The paper would be a concise exact-value note on another unresolved one-step diagonal book Ramsey number.
