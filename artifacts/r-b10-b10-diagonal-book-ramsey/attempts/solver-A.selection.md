# Untitled Entry

- entry_type: `paper_candidate`
- slug: `r-b10-b10-diagonal-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Maksim V. Pchelintsev, Peter Rath, and Sebastian Angeltveit, "New lower and upper bounds on Ramsey numbers" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1 and the note immediately following it, together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026, 114913).`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `An exact determination of R(B10, B10) would support a compact note because the remaining gap is a single unresolved step in the recent diagonal-book Ramsey table.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `80`
- single_solve_to_paper_fraction: `0.8`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
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
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/r-b10-b10-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on a diagonal book Ramsey number left at a one-step interval.`

## question
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 10-page book graph B10.

## canonical_statement
Determine the exact value of R(B10, B10).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 10-page book graph B10.

## pre_solve_gate_reason
This is a source-anchored one-gap exact-value packet with a stable theorem slice, low broader-theorem risk, and bounded post-solve residue.

## micro_paper_assessment
Strong lane fit. This is a one-step diagonal-book gap with clear family anchor and low editorial residue after the solve, though the certificate may be slightly less compact than the top slot.

## hypothetical_title
The Exact Value of R(B10, B10)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B10, B10). Current public sources leave this value in the interval 41 <= R(B10, B10) <= 42. Our result closes another one-step gap in the recent diagonal-book Ramsey table.

## single_solve_paper_explanation
The exact value would still be the honest title theorem of a short note. The family story is already present in recent literature, so one solve gets most of the way to publication. The only real residue is clean presentation of the proof or extremal construction.

## broader_theorem_nonimplication_note
The existing family theorem leaves a genuine two-value gap, and the known exactness shortcut does not apply because 41 is a sum of two squares. No broader result found in the bounded audit implies the answer already.

## literature_gap
Current public sources stop at 41 <= R(B10, B10) <= 42.

## publication_packet_title
The Exact Value of R(B10, B10)

## publication_packet_frontier_basis
Recent literature leaves the exact value at 41 <= R(B10, B10) <= 42, and 41 is a sum of two squares, so the standard diagonal-book exactness shortcut does not settle the lower endpoint.

## publication_packet_near_paper_reason
Once the endpoint is settled, the proof or critical coloring is already the main theorem and nearly all of the note. Only clean exposition and verification of the decisive witness or forcing argument remain.

## publication_packet_literature_scope
Pchelintsev-Rath-Angeltveit 2025 Theorem 1 and note after Theorem 1, Wesley 2026, and bounded exact-notation, alternate-notation, source-internal, outside-source, and recent-status checks through 2026-04-14, plus local 2026-04-15 attempt-registry conflict checks.

## publication_packet_artifact_requirements
Either a monochromatic-book-free coloring of K41 or a proof that every coloring of K42 contains a monochromatic B10, with a compact verification certificate.

## paper_shape
A one-theorem exact-value note on a diagonal book Ramsey number left at a one-step interval.

## transfer_kit

### usable_lemmas
- Pchelintsev-Rath-Angeltveit 2025, Theorem 1, implies R(B10, B10) >= 41.
- The same theorem implies R(B10, B10) <= 42.
- The note after Theorem 1 does not force exactness here because 41 is a sum of two squares.
- Wesley 2026 supplies recent constructive family context confirming that the diagonal-book line remains active.

### toy_example
The exact solved neighbor R(B8, B8) = 33 illustrates the intended paper form after a diagonal-book exact closure.

### known_obstruction
A lower-bound proof requires a K41 coloring avoiding monochromatic B10, while an upper-bound proof must eliminate every such critical coloring at that order.

### prior_work_stop_sentence
Current sources stop at 41 <= R(B10, B10) <= 42.

### recommended_first_attack
Try to extend the current constructive templates to K41 and, in parallel, extract forced common-neighbor inequalities that could make K42 unavoidable.

### paper_if_solved
The paper would be a concise exact-value note on a one-step diagonal-book Ramsey gap.
