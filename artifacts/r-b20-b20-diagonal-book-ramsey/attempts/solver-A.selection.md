# Determine the exact value of R(B20, B20)

- entry_type: `paper_candidate`
- slug: `r-b20-b20-diagonal-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 81 <= R(B20, B20) <= 82; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)) as a recent family-status and citation check; and bounded 2026-04-14 exact-statement, alternate-notation, canonical-source, and recent-status web checks that did not reveal a later exact determination.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B20, B20) would still plausibly support a short note because the public frontier remains a one-step diagonal book Ramsey gap.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `73`
- single_solve_to_paper_fraction: `0.74`
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
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b20-b20-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a diagonal book Ramsey number at the edge of the strongest current micro-paper lane.`

## question
Is R(B20, B20) equal to 81 or 82?

## canonical_statement
Determine the exact value of R(B20, B20).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B20.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this exact tuple, slug, title, or canonical-source anchor. The bounded audit recovered the 81-82 interval from the 2025 lemma and did not surface a later exact closure in 2026-status searches.

## micro_paper_assessment
Pass. The theorem slice is stable and paper-shaped, though the certificate risk is slightly higher than for B19.

## hypothetical_title
The Exact Value of R(B20, B20)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B20, B20). Previous work left this number in the interval 81 <= R(B20, B20) <= 82. Our result closes the remaining one-step gap for this diagonal book pair.

## single_solve_paper_explanation
This target still meets the 70% paper threshold because one clean solve would already determine the exact value in a family with an established literature frame. The solve would contribute the title theorem, the main comparison, and the decisive artifact. The main risk is only that the certificate may be a little less compact than for B19.

## broader_theorem_nonimplication_note
The broad diagonal-book theory still leaves a one-step interval and does not fix the endpoint at n = 20. Exact almost-diagonal information nearby does not settle the diagonal slice.

## literature_gap
Current public sources stop at 81 <= R(B20, B20) <= 82.

## publication_packet_title
The Exact Value of R(B20, B20)

## publication_packet_frontier_basis
Current public sources leave the diagonal book Ramsey number at 81 <= R(B20, B20) <= 82. The remaining frontier is again a single endpoint in a standard family.

## publication_packet_near_paper_reason
If the endpoint 81 versus 82 is settled, the note already has a natural title theorem and a clean comparison with the recently sharpened diagonal-book record. The remaining work is mostly polishing the decisive witness or forcing proof.

## publication_packet_literature_scope
2025 EJC Lemma 1 for the one-step interval and exact almost-diagonal comparison point, 2026 Wesley for recent family context, and bounded 2026-04-14 exact-statement, synonym, and status searches.

## publication_packet_artifact_requirements
Either an explicit 81-vertex coloring avoiding monochromatic B20 or a compact proof that every 82-vertex coloring forces B20.

## paper_shape
A one-theorem exact-value note for a diagonal book Ramsey number at the edge of the strongest current micro-paper lane.

## transfer_kit

### usable_lemmas
- Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 81 <= R(B20, B20) <= 82.
- The same lemma gives the exact neighboring almost-diagonal value R(B19, B20) = 79.
- The 2025 paper's method counts copies of B_k through common neighborhoods of candidate spine edges.
- Wesley (2026) confirms that recent lower-bound constructions continue to sharpen book-Ramsey gaps without reporting an exact closure for B20.

### toy_example
The exact neighboring almost-diagonal case R(B19, B20) = 79 is the closest solved benchmark for the intended theorem shape.

### known_obstruction
The diagonal-book critical graphs at this size can still carry substantial symmetry, so an upper-bound proof must exclude a structured candidate class rather than a single sporadic witness.

### prior_work_stop_sentence
Current public sources stop at 81 <= R(B20, B20) <= 82.

### recommended_first_attack
Use common-neighborhood forcing on candidate spine edges, anchored by the exact R(B19, B20) = 79 comparison point, to show that every 81-vertex near-extremal coloring collapses when extended.

### paper_if_solved
The paper would be a short exact-value note settling another one-step diagonal book Ramsey gap.
