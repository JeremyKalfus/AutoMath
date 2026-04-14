# Determine the exact value of R(B21, B21)

- entry_type: `paper_candidate`
- slug: `r-b21-b21-diagonal-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 85 <= R(B21, B21) <= 86 and the exact neighboring almost-diagonal value R(B20, B21) = 83; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)) as a recent family-status and citation check; plus bounded 2026-04-14 exact-statement, family-level, canonical-source, and recent-status web checks that did not reveal a later exact determination.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B21, B21) could still support a short note because the public frontier remains a one-step diagonal book Ramsey gap with an adjacent exact benchmark.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `70`
- single_solve_to_paper_fraction: `0.72`
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
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b21-b21-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a diagonal book Ramsey number that remains tightly framed by the recent book-Ramsey literature.`

## question
Is R(B21, B21) equal to 85 or 86?

## canonical_statement
Determine the exact value of R(B21, B21).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B21.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this exact tuple, slug, title, or canonical-source anchor. The bounded audit recovered the 85-86 interval and neighboring exact almost-diagonal value from the 2025 lemma, and the 2026 family-status source did not show a later closure.

## micro_paper_assessment
Pass. The theorem slice is stable, the adjacent exact comparison point helps the story, and one clean solve would still look like most of a short paper.

## hypothetical_title
The Exact Value of R(B21, B21)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B21, B21). Previous work left this number in the interval 85 <= R(B21, B21) <= 86. Our result closes the remaining one-step gap for this diagonal book pair.

## single_solve_paper_explanation
This target remains inside the strict micro-paper lane because one successful solve would already produce the title theorem, the decisive endpoint resolution, and almost all of the note's literature comparison. The family anchor is still strong and the theorem slice does not drift under the most plausible proof routes. The main downgrade relative to B19 and B20 is only a modest increase in certificate compactness risk.

## broader_theorem_nonimplication_note
The current broad diagonal-book results still stop at the interval 85 <= R(B21, B21) <= 86, and the nearby exact theorem R(B20, B21) = 83 does not determine the diagonal case. A proof here would therefore remain the honest headline result rather than a generic corollary.

## literature_gap
Current public sources stop at 85 <= R(B21, B21) <= 86.

## publication_packet_title
The Exact Value of R(B21, B21)

## publication_packet_frontier_basis
Current public sources leave the diagonal book Ramsey number at 85 <= R(B21, B21) <= 86. The frontier is still a single endpoint with the exact almost-diagonal value R(B20, B21) = 83 nearby.

## publication_packet_near_paper_reason
If the endpoint 85 versus 86 is settled, the note already has a clean title theorem, a direct comparison with the recent almost-diagonal exact case, and a compact family narrative. The residue after the solve is limited to polishing the decisive witness or forcing argument.

## publication_packet_literature_scope
2025 EJC Lemma 1 for the one-step interval and adjacent exact benchmark, Wesley (2026) for recent family status, and bounded 2026-04-14 exact-statement and status searches.

## publication_packet_artifact_requirements
Either an explicit 85-vertex coloring avoiding monochromatic B21 or a compact proof that every 86-vertex coloring forces B21.

## paper_shape
A one-theorem exact-value note for a diagonal book Ramsey number that remains tightly framed by the recent book-Ramsey literature.

## transfer_kit

### usable_lemmas
- Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 85 <= R(B21, B21) <= 86.
- The same lemma gives the exact neighboring almost-diagonal value R(B20, B21) = 83.
- The 2025 paper controls monochromatic books through common-neighborhood counts on candidate spine edges.
- Wesley (2026) provides recent lower-bound constructions and family-level status without closing the diagonal n = 21 case.

### toy_example
The exact almost-diagonal case R(B20, B21) = 83 is the nearest solved benchmark for the intended theorem shape.

### known_obstruction
The critical diagonal colorings can still be highly structured, so the final argument may need to rule out a small family of block-circulant or polycirculant extremals rather than a single witness.

### prior_work_stop_sentence
Current public sources stop at 85 <= R(B21, B21) <= 86.

### recommended_first_attack
Start from the published polycirculant lower-bound architecture and combine it with common-neighborhood forcing to test whether every 85-vertex near-extremal coloring necessarily creates a B21 after any one-vertex extension.

### paper_if_solved
The paper would be a short exact-value note closing another one-step diagonal book Ramsey gap.
