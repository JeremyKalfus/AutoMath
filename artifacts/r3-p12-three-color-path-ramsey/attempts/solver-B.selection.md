# Determine the exact value of R(P12, P12, P12)

- entry_type: `paper_candidate`
- slug: `r3-p12-three-color-path-ramsey`
- worker_role: `solver-B`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, revision dated June 7, 2024), Section 6.4.1, together with Dybizbański-Dzido-Radziszowski, "On some three-color Ramsey numbers for paths" (Discrete Applied Mathematics, 2016), and bounded 2026-04-13 web checks.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `An exact determination of the P12 diagonal path value would still be a standalone short Ramsey note because the formula, the neighboring solved cases, and the intended target are already fixed in the literature.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `79`
- single_solve_to_paper_fraction: `0.72`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `moderate`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r3-p12-three-color-path-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a bounded three-color path diagonal case beyond the currently solved P9 range.`

## question
Is R(P12, P12, P12) = 22?

## canonical_statement
Determine the exact value of R(P12, P12, P12).

## intended_statement
Either prove that every 3-coloring of K22 contains a monochromatic P12, or construct a 3-coloring of K22 with no monochromatic P12 and thus show R(P12, P12, P12) >= 23.

## pre_solve_gate_reason
The public survey still records only the exact range through P9 and identifies P10 as the first open case, so the P12 diagonal slice remains unresolved while retaining a clean exact-value-paper shape.

## micro_paper_assessment
Pass. The target is not the first open diagonal path case, but it still has a real title theorem, a named conjectural value, and a short-paper narrative that does not need a feeder ladder once the exact solve lands.

## hypothetical_title
The Exact Value of R(P12, P12, P12)

## hypothetical_abstract
We determine the exact three-color Ramsey number R(P12, P12, P12). The publicly accessible Ramsey survey revision of June 7, 2024 records exact diagonal path values only through P9 and states that P10 is the first open case, while the 2016 paper of Dybizbański, Dzido, and Radziszowski settles only P8 and P9. Our theorem fixes another bounded diagonal path residue and tests the Faudree-Schelp formula at n = 12.

## single_solve_paper_explanation
If P12 is settled exactly, the theorem is already the full paper spine because the family formula, neighboring exact cases, and expected value 22 are already on the table. The remaining work is short exposition, a comparison to P8 and P9, and the final extremal description. The case is slightly weaker than a first-open residue, but it still sits in the target 70-90% paper zone.

## broader_theorem_nonimplication_note
The large-n path theorem R(Pn, Pn, Pn) = 2n - 2 + (n mod 2) only applies asymptotically, and the cycle-to-path implication recorded in the literature addresses odd-path slices from even-cycle formulas rather than the even-path case P12.

## literature_gap
The June 7, 2024 Ramsey survey records exact diagonal three-color path values only through P9 and gives no exact value for R(P12, P12, P12).

## publication_packet_title
The Exact Value of R(P12, P12, P12)

## publication_packet_frontier_basis
Radziszowski DS1.17 records exact three-color path values only through P9 and states that P10 is the first open case; bounded 2026-04-13 web checks found no later exact paper settling the diagonal P12 value.

## publication_packet_near_paper_reason
The Faudree-Schelp conjectural formula gives the target 22, and the 2016 path paper already supplies the last publicly recorded exact cases P8 and P9. Once P12 is settled, the note mostly needs the forcing proof or the extremal coloring plus a short comparison to P8 and P9.

## publication_packet_literature_scope
Radziszowski DS1.17 Section 6.4.1, Dybizbański-Dzido-Radziszowski 2016, and bounded 2026-04-13 searches for R(P12,P12,P12), R3(P12), and recent path-Ramsey status signals.

## publication_packet_artifact_requirements
Either a proof that every 3-coloring of K22 contains a monochromatic P12, or one explicit 22-vertex coloring with no monochromatic P12.

## paper_shape
A one-theorem exact-value note for a bounded three-color path diagonal case beyond the currently solved P9 range.

## transfer_kit

### usable_lemmas
- Radziszowski DS1.17 records the asymptotic formula R(Pn, Pn, Pn) = 2n - 2 + (n mod 2) and attributes the all-n conjecture to Faudree and Schelp.
- The same survey records exact diagonal values through R3(P9) = 17.
- Dybizbański, Dzido, and Radziszowski prove that the even-cycle formula, when true, implies the odd-path formula R(P2m+1, P2m+1, P2m+1) = 4m + 1, which highlights that even-path cases need their own treatment.

### toy_example
The nearest publicly solved diagonal path cases are R(P8, P8, P8) = 14 and R(P9, P9, P9) = 17, while the conjectural P12 target is 22.

### known_obstruction
Any proof must control the usual three-color path-avoiding block templates on 22 vertices, while a disproof must produce one explicit 22-vertex witness with no monochromatic P12.

### prior_work_stop_sentence
The June 7, 2024 Ramsey survey records exact diagonal three-color path values only through P9 and gives no exact value for R(P12, P12, P12).

### recommended_first_attack
Begin with the extremal coloring patterns compatible with the Faudree-Schelp value 22 and perform a stability analysis showing that each 22-vertex near-extremal template already creates a monochromatic P12.

### paper_if_solved
The paper would be a short exact-value note on a bounded diagonal three-color path Ramsey number.
