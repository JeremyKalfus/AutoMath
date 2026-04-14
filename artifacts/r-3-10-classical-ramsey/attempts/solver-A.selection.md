# Determine the exact value of R(3,10)

- entry_type: `paper_candidate`
- slug: `r-3-10-classical-ramsey`
- worker_role: `solver-A`
- canonical_source: `Geoffrey Exoo, "On Two Classical Ramsey Numbers of the Form R(3, n)" (SIAM Journal on Discrete Mathematics 2 (1989)) for the lower bound R(3,10) >= 40; Vigleik Angeltveit, "R(3,10) <= 41" (manuscript listed in 2024 status updates) for the current upper bound; together with Stanislaw Radziszowski, "Small Ramsey Numbers" revision 18 (January 6, 2026) and the Leaps in Bounds Ramsey constant page as bounded current-status checks; plus bounded 2026-04-14 exact-statement and recent-status searches that did not reveal a later exact determination.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(3,10) would plausibly be the title theorem of a short note because the public frontier is already compressed to a one-step classical Ramsey gap.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `88`
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
- working_packet_path: `artifacts/r-3-10-classical-ramsey/working_packet.md`
- paper_shape: `A one-theorem classical Ramsey note closing a one-step off-diagonal gap by either a final lower-bound witness or a final forcing upper bound.`

## question
Is R(3,10) equal to 40 or 41?

## canonical_statement
Determine the exact value of R(3,10).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains either a red triangle or a blue K_10.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this tuple, slug, or title. The bounded audit recovered the current interval 40 <= R(3,10) <= 41 from the primary lower and upper sources and the 2026 survey/status surfaces did not show a later closure.

## micro_paper_assessment
Pass. This is the cleanest fresh tuple found in the bounded curation sweep: a stable theorem slice, a one-step exact gap, strong family anchor, and low post-solve editorial drag.

## hypothetical_title
The Exact Value of R(3,10)

## hypothetical_abstract
We determine the classical Ramsey number R(3,10). Previous work left this parameter in the interval 40 <= R(3,10) <= 41. Our result closes the remaining one-step gap for the smallest currently exposed off-diagonal triangle-versus-clique case of this form.

## single_solve_paper_explanation
This target clears the 70-90% paper test because one exact solve already gives the note's title theorem, main artifact, and complete comparison with prior bounds. The theorem slice is stable: the honest statement after a successful proof is still exactly R(3,10), not a broader ambient theorem. Residual work is limited to polishing the witness verification or forcing argument and writing a short context section.

## broader_theorem_nonimplication_note
The current literature only provides the lower witness at 40 and the upper bound 41. No broader published theorem collapses the exact endpoint automatically, so the exact 40-versus-41 decision would remain the headline theorem rather than a corollary.

## literature_gap
Current public sources stop at 40 <= R(3,10) <= 41.

## publication_packet_title
The Exact Value of R(3,10)

## publication_packet_frontier_basis
Current public sources leave the classical off-diagonal Ramsey number in the interval 40 <= R(3,10) <= 41, so the live frontier is a single unresolved endpoint.

## publication_packet_near_paper_reason
If the endpoint 40 versus 41 is settled, the note already has its title theorem, its complete literature comparison, and its decisive artifact. What remains after the solve is mostly compression of the computational or structural argument into publishable form.

## publication_packet_literature_scope
Exoo (1989) for the 40-vertex lower bound, Angeltveit (2024) for the 41 upper bound, Radziszowski revision 18 (2026) and Leaps in Bounds for current-status confirmation, and bounded 2026-04-14 exact-statement and recent-status searches.

## publication_packet_artifact_requirements
Either an explicit 40-vertex triangle-free graph with independence number 9 or a compact proof that every triangle-free graph on 41 vertices has independence number at least 10.

## paper_shape
A one-theorem classical Ramsey note closing a one-step off-diagonal gap by either a final lower-bound witness or a final forcing upper bound.

## transfer_kit

### usable_lemmas
- Exoo (1989) provides a 40-vertex lower-bound construction showing R(3,10) >= 40.
- Angeltveit (2024) gives the current upper bound R(3,10) <= 41.
- The standard equivalence reformulates the problem as classifying triangle-free graphs on 40 or 41 vertices with independence number below 10.
- The R(3,k) computational toolkit based on e(3,k,n) tables and one-vertex extension arguments remains the natural forcing framework for the upper-bound side.

### toy_example
The exact value R(3,9) = 36 is the nearest solved benchmark of the same triangle-versus-clique shape.

### known_obstruction
Near-extremal triangle-free graphs can be highly structured and almost regular, so the final step may require ruling out a small family of hard residual graphs rather than handling a single sporadic example.

### prior_work_stop_sentence
Current public sources stop at 40 <= R(3,10) <= 41.

### recommended_first_attack
Push the upper-bound side first by combining degree restrictions and one-vertex extension over the known triangle-free extremal families at the 40-vertex boundary.

### paper_if_solved
The paper would be a short classical Ramsey note closing a one-step off-diagonal exact gap.
