# Determine the exact value of R(C10, C10, C10)

- entry_type: `paper_candidate`
- slug: `r3-c10-even-cycle-ramsey`
- worker_role: `solver-B`
- canonical_source: `Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, revision dated June 7, 2024), Section 6.3.1, together with Fabrico S. Benevides and Jozef Skokan, "The 3-colored Ramsey number of even cycles" (Journal of Combinatorial Theory, Series B, 2009), and bounded exact-term and alternate-notation web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Settling the first open three-color even-cycle diagonal case would already supply the title theorem of a short cycle-Ramsey note.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
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
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r3-c10-even-cycle-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the first open diagonal three-color even-cycle Ramsey number.`

## question
Is R(C10, C10, C10) = 20?

## canonical_statement
Determine the exact value of R(C10, C10, C10).

## intended_statement
Either prove that every 3-coloring of K20 contains a monochromatic C10, or construct a 3-coloring of K20 with no monochromatic C10 and thus show R(C10, C10, C10) >= 21.

## pre_solve_gate_reason
The survey still names C10 as the first open diagonal three-color even-cycle case, and the large-n exact theorem does not settle this bounded slice.

## micro_paper_assessment
Pass. This is a first-open named residue in a flagship exact-value family, and one clean solve would already be the whole short paper.

## hypothetical_title
The Exact Value of R(C10, C10, C10)

## hypothetical_abstract
We determine the exact three-color Ramsey number R(C10, C10, C10). The current Ramsey survey states that the formula R(C2m, C2m, C2m) = 4m is known only for sufficiently large m and identifies C10 as the first open diagonal even-cycle case. Our theorem closes the smallest remaining bounded even-cycle residue in the three-color diagonal family.

## single_solve_paper_explanation
If the exact C10 value is determined, the theorem is already the note's title result. The family conjecture, the large-n exact theorem, and the solved C8 benchmark already provide the narrative scaffolding. What remains after the solve is mainly exposition, a compact extremal discussion, and documentation of the critical coloring pattern.

## broader_theorem_nonimplication_note
Benevides and Skokan prove the diagonal even-cycle formula only for sufficiently large even n, so the bounded C10 instance is not already covered by the published large-n theorem.

## literature_gap
The June 7, 2024 Ramsey survey identifies C10 as the first open diagonal three-color even-cycle case and records only the lower bound 20.

## publication_packet_title
The Exact Value of R(C10, C10, C10)

## publication_packet_frontier_basis
The June 7, 2024 survey says R3(C2m) = 4m is known only for sufficiently large m and identifies C10 as the first open case; the Benevides-Skokan paper proves the large-even-cycle formula only beyond a threshold; bounded 2026-04-13 exact-term and alternate-notation searches did not surface a later exact-resolution paper for C10.

## publication_packet_near_paper_reason
The conjectural target 20, the solved C8 benchmark, and the large-even-cycle framework are already in place. Once C10 is settled, the note mostly needs the sharp forcing proof or the critical coloring plus a short comparison to the established large-n theory.

## publication_packet_literature_scope
Radziszowski DS1.17 Section 6.3.1, Benevides-Skokan 2009, and bounded 2026-04-13 exact-statement and alternate-notation searches for the diagonal C10 case.

## publication_packet_artifact_requirements
Either a proof that every 3-coloring of K20 contains a monochromatic C10, or one explicit 20-vertex coloring with no monochromatic C10.

## paper_shape
A one-theorem exact-value note on the first open diagonal three-color even-cycle Ramsey number.

## transfer_kit

### usable_lemmas
- DS1.17 records the general lower bound R3(C2m) >= 4m for all m >= 2 and says C10 is the first open diagonal even-cycle case.
- The survey records the exact benchmark R(C8, C8, C8) = 16.
- Benevides and Skokan prove that R(Cn, Cn, Cn) = 2n for all sufficiently large even n, supplying the large-scale stability model but not the bounded C10 case.

### toy_example
The nearest solved diagonal even-cycle benchmark is R(C8, C8, C8) = 16, while the conjectural C10 target is 20.

### known_obstruction
Any upper-bound proof must eliminate 19-vertex extremal three-color templates based on even-cycle blowups, while a disproof must produce one explicit 20-vertex coloring with no monochromatic C10.

### prior_work_stop_sentence
The June 7, 2024 Ramsey survey identifies C10 as the first open diagonal three-color even-cycle case.

### recommended_first_attack
Start from the standard 19-vertex lower-bound construction and prove a 20-vertex stability theorem forcing a monochromatic C10 in every extension.

### paper_if_solved
The paper would be a short exact-value note on the first open diagonal three-color even-cycle Ramsey number.
