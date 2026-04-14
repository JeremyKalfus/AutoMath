# Determine the exact value of R(B4, B4)

- entry_type: `paper_candidate`
- slug: `r-b4-b4-diagonal-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Maksim V. Pchelintsev, Peter Rath, and Sebastian Angeltveit, "New lower and upper bounds on Ramsey numbers" (Electronic Journal of Combinatorics 32(4) (2025), #P4.64), Theorem 1 and the note immediately following it, which imply 17 <= R(B4, B4) <= 18; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026), 114913) as independent recent family context and bounded 2026-04-14 web checks that did not reveal a later exact closure.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B4, B4) would already be the title theorem of a short note closing the first still-open diagonal book Ramsey case after the recent one-step family bounds.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `88`
- single_solve_to_paper_fraction: `0.86`
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
- working_packet_path: `artifacts/r-b4-b4-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem note settling the first unresolved small diagonal book Ramsey number left at a one-step interval.`

## question
Is R(B4, B4) equal to 17 or 18?

## canonical_statement
Determine the exact value of R(B4, B4).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 4-page book graph B4.

## pre_solve_gate_reason
The thin-memory exclusion sweep over memory/search_memory.json, memory/paper_memory.json, failed_problems.json, queue.json, selected_problem.md, PROOFS.md, and artifact directory names found no prior mathematical status or near-duplicate slug for the exact diagonal case R(B4, B4). The bounded 2026-04-14 literature check found the 2025 EJC theorem giving 17 <= R(B4, B4) <= 18, the 2026 Wesley paper as recent independent family activity, and no later exact determination.

## micro_paper_assessment
Pass. This is a stable one-step exact gap in a named active family, and a clean solve would already look like a real short paper rather than a curiosity.

## hypothetical_title
The Exact Value of R(B4, B4)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B4, B4). Recent bounds leave this parameter in the sharp interval 17 <= R(B4, B4) <= 18, with neither the existing lower-bound constructions nor the standard sum-of-two-squares shortcut deciding the case. Our result closes the first unresolved small diagonal book case left by the recent family bounds.

## single_solve_paper_explanation
One exact solve would already be the honest main theorem of the paper. The family anchor is strong because diagonal book Ramsey numbers are currently being tightened systematically, and this is the smallest unresolved one-step case in that recent line. After the solve, only short contextual packaging and the verification artifact remain.

## broader_theorem_nonimplication_note
The recent family theorem only gives 4n + 1 <= R(Bn, Bn) <= 4n + 2, and the known exactness shortcut applies only when 4n + 1 is not a sum of two squares. Here 17 is a sum of two squares, so no broader published criterion found in the bounded audit already settles the case.

## literature_gap
Current public sources stop at 17 <= R(B4, B4) <= 18.

## publication_packet_title
The Exact Value of R(B4, B4)

## publication_packet_frontier_basis
The 2025 EJC paper compresses the diagonal book case to the sharp interval 17 <= R(B4, B4) <= 18, and the usual sum-of-two-squares exactness shortcut does not resolve 17 because 17 = 1^2 + 4^2. This leaves a genuine one-step frontier rather than a case already collapsed by a broader criterion.

## publication_packet_near_paper_reason
If the exact value is found, the decisive proof or critical coloring is already almost the whole note. What remains is a short contextual paragraph about recent diagonal-book progress, a compact verification artifact, and a brief comparison with neighboring exact diagonal cases.

## publication_packet_literature_scope
2025 EJC P4.64 Theorem 1 and follow-up note, the 2026 Wesley Discrete Mathematics paper for recent family context, plus bounded 2026-04-14 exact-notation and status web checks.

## publication_packet_artifact_requirements
Either an explicit B4-free red-blue coloring of K17 or a proof that every coloring of K18 contains a monochromatic B4, together with a compact verification certificate.

## paper_shape
A one-theorem note settling the first unresolved small diagonal book Ramsey number left at a one-step interval.

## transfer_kit

### usable_lemmas
- Pchelintsev, Rath, and Angeltveit (2025), Theorem 1, implies the lower bound R(B4, B4) >= 17.
- The same theorem gives the upper bound R(B4, B4) <= 18.
- The note after Theorem 1 states that R(Bn, Bn) = 4n + 1 when 4n + 1 is not a sum of two squares; this does not apply here because 17 = 1^2 + 4^2.
- The 2026 Wesley paper confirms that diagonal and near-diagonal book Ramsey numbers remain an active lower-bound frontier, so the family narrative is current.

### toy_example
The exact solved neighbor R(B8, B8) = 33 shows how a single diagonal-book closure in this family already supports a compact standalone note.

### known_obstruction
A lower-bound proof must exhibit a 2-coloring of K17 with no monochromatic B4, while an upper-bound proof must eliminate every such critical coloring at order 17.

### prior_work_stop_sentence
Current sources stop at 17 <= R(B4, B4) <= 18.

### recommended_first_attack
Start from the recent block-circulant and search-guided lower-bound constructions for book Ramsey numbers and analyze whether the K17 critical pattern can be completed or ruled out by a tight neighborhood case split.

### paper_if_solved
The paper would be a concise exact-value note closing the first unresolved small diagonal book Ramsey case left at a one-step interval.
