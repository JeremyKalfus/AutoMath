# Determine the exact value of R(B16, B16)

- entry_type: `paper_candidate`
- slug: `r-b16-diagonal-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), item 5.3(f); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1 and Appendix A; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026); and bounded exact-term, alternate-notation, canonical-source, and recent-status web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing this one-gap diagonal residue would already read as the title theorem of a genuine short note on book Ramsey numbers.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `low`
- paper_leverage_score: `85`
- single_solve_to_paper_fraction: `0.82`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
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
- working_packet_path: `artifacts/r-b16-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on a diagonal book Ramsey number left outside the standard number-theoretic criteria.`

## question
Is R(B16, B16) = 65 or 66?

## canonical_statement
Determine the exact value of R(B16, B16).

## intended_statement
Either prove that every graph on 65 vertices contains B16 or has a complement containing B16 and thus show R(B16, B16) = 65, or construct a 65-vertex graph with no B16 and no complement B16 and thus show R(B16, B16) = 66.

## pre_solve_gate_reason
The local thin-memory sweep shows no prior attempt on this exact tuple, the published diagonal framework gives the sharp one-gap window 65 <= R(B16, B16) <= 66, and the bounded 2026-04-13 audit did not surface a later exact-resolution paper.

## micro_paper_assessment
Pass. This is a stable one-gap diagonal residue in a named family, with a clean story, low novelty-check cost, and very short solve-to-paper distance.

## hypothetical_title
The Exact Value of R(B16, B16)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B16, B16). Existing diagonal criteria leave the case n = 16 in the one-gap window 65 <= R(B16, B16) <= 66 because 4n + 1 = 65 is a sum of two squares but not a prime power. Our result closes a clean residual diagonal case in the book Ramsey table and sharpens the current boundary of the exact theory.

## single_solve_paper_explanation
The exact n = 16 diagonal value is already the honest title theorem. The surrounding paper infrastructure is unusually mature: the diagonal one-gap framework is published, the standard exact criteria are known, and the residue is a single named case with an immediate table update. After a solve, only light exposition and comparison with the existing exact diagonal cases remain.

## broader_theorem_nonimplication_note
The published diagonal exact criteria do not already settle n = 16 because 4n + 1 = 65 is neither a prime power nor excluded by the sum-of-two-squares obstruction. A shortest proof may use more structure than the published criteria, but the honest theorem would still remain this exact diagonal residue rather than a generic corollary of a known broader statement.

## literature_gap
Current public sources support only the one-gap window 65 <= R(B16, B16) <= 66, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B16, B16)

## publication_packet_frontier_basis
DS1.17 records the diagonal criteria R(Bn, Bn) = 4n + 2 when 4n + 1 is a prime power and R(Bn, Bn) <= 4n + 1 when 4n + 1 is not a sum of two squares. The 2025 paper proves 4n + 1 <= R(Bn, Bn) <= 4n + 2 for 4 <= n <= 21 and provides the lower-bound construction framework covering n = 16, while Wesley 2026 improves book lower bounds without reporting an exact closure of the n = 16 diagonal case.

## publication_packet_near_paper_reason
The family theorem, the two standard exact criteria, and the narrow one-gap residue are already in place. If the exact value at n = 16 is settled, the remaining paper work is mostly a compact explanation of why 65 escapes the standard criteria and how the forcing or obstruction closes the gap.

## publication_packet_literature_scope
DS1.17 item 5.3(f), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1 and Appendix A, Wesley 2026, and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, and recent-status searches for R(B16, B16).

## publication_packet_artifact_requirements
Either a proof that every 65-vertex graph contains B16 or has complement containing B16, or one explicit 65-vertex graph avoiding B16 in both colors.

## paper_shape
A one-theorem exact-value note on a diagonal book Ramsey number left outside the standard number-theoretic criteria.

## transfer_kit

### usable_lemmas
- Lidický-McKinley-Pfender-Van Overberghe 2025 proves 4n + 1 <= R(Bn, Bn) <= 4n + 2 for all 4 <= n <= 21, hence 65 <= R(B16, B16) <= 66.
- DS1.17 item 5.3(f) records the exact criterion R(Bn, Bn) = 4n + 2 when 4n + 1 is a prime power.
- The same item records that if 4n + 1 is not a sum of two integer squares, then R(Bn, Bn) <= 4n + 1, explaining why many neighboring diagonal cases are exact while n = 16 is not covered.

### toy_example
The nearby diagonal cases resolved by number-theoretic criteria provide the worked comparison: n = 17 is exact because 69 is not a sum of two squares, while n = 16 remains undecided because 65 = 1^2 + 8^2.

### known_obstruction
Any proof of R(B16, B16) = 65 must eliminate every 65-vertex extremal template compatible with the published lower-bound constructions, while a proof of R(B16, B16) = 66 needs one explicit 65-vertex witness avoiding B16 in both a graph and its complement.

### prior_work_stop_sentence
Current sources stop at the one-gap diagonal window 65 <= R(B16, B16) <= 66.

### recommended_first_attack
Start from the published block-circulant and polycirculant lower-bound templates and prove that any 65-vertex extension necessarily creates a spine with at least 16 common neighbors in one color.

### paper_if_solved
The paper would be a short exact-value note closing a diagonal book Ramsey residue left open by the standard number-theoretic criteria.
