# Determine the exact value of R(P10, P10, P10)

- entry_type: `paper_candidate`
- slug: `r3-p10-three-color-path-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, revision dated June 7, 2024), Section 6.4.1, together with Janusz Dybizbanski, Tomasz Dzido, and Stanislaw Radziszowski, "On Some Three-Color Ramsey Numbers for Paths" (Discrete Applied Mathematics, 2016), and bounded exact-term and alternate-notation web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Settling the first open diagonal three-color path case would already read as the title theorem of a short Ramsey note rather than as feeder evidence.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `88`
- single_solve_to_paper_fraction: `0.85`
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
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r3-p10-three-color-path-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the first open diagonal three-color path Ramsey number.`

## question
Is R(P10, P10, P10) = 18?

## canonical_statement
Determine the exact value of R(P10, P10, P10).

## intended_statement
Either prove that every 3-coloring of K18 contains a monochromatic P10, or construct a 3-coloring of K18 with no monochromatic P10 and thus show R(P10, P10, P10) >= 19.

## pre_solve_gate_reason
The survey still says the exact diagonal path values are known only through P9 and that P10 is the first open case, so one sharp resolution already determines the honest note-sized theorem.

## micro_paper_assessment
Pass. This is the first open diagonal case in a named exact-value family, and one clean solve would already look like the paper rather than a feeder lemma.

## hypothetical_title
The Exact Value of R(P10, P10, P10)

## hypothetical_abstract
We determine the exact three-color Ramsey number R(P10, P10, P10). The current Ramsey survey records exact diagonal path values only through P9 and identifies P10 as the first open case, while the 2016 paper of Dybizbanski, Dzido, and Radziszowski settles only P8 and P9. Our theorem closes the first unresolved bounded diagonal path instance and fixes the smallest remaining test of the Faudree-Schelp formula in the three-color diagonal setting.

## single_solve_paper_explanation
If the exact P10 value is determined, the resulting theorem is already the title and core payload of the note. The family formula, the benchmark cases P8 and P9, and the expected target 18 are already standard inputs. What remains after the solve is mostly exposition, extremal-coloring discussion, and a short comparison with the last solved diagonal cases.

## broader_theorem_nonimplication_note
The asymptotic three-color path formula only applies for large n, and the 2016 path paper stops at P9. No broader published theorem visible in the bounded audit settles the exact diagonal P10 case.

## literature_gap
The June 7, 2024 Ramsey survey records exact diagonal three-color path values only through P9 and states that P10 is the first open case.

## publication_packet_title
The Exact Value of R(P10, P10, P10)

## publication_packet_frontier_basis
The June 7, 2024 survey states that exact diagonal three-color path values are known only through P9 and that P10 is the first open case; the 2016 path paper settles only P8 and P9; bounded exact-term and alternate-notation searches run on 2026-04-13 did not surface a later exact-resolution paper for P10.

## publication_packet_near_paper_reason
The conjectural value 18, the neighboring exact benchmarks, and the asymptotic family formula are already in place. Once the exact P10 value is settled, what remains is mostly a short extremal discussion and comparison with P8 and P9.

## publication_packet_literature_scope
Radziszowski DS1.17 Section 6.4.1, Dybizbanski-Dzido-Radziszowski 2016, and bounded 2026-04-13 exact-statement and alternate-notation searches for the diagonal P10 case.

## publication_packet_artifact_requirements
Either a proof that every 3-coloring of K18 contains a monochromatic P10, or one explicit 18-vertex coloring with no monochromatic P10.

## paper_shape
A one-theorem exact-value note on the first open diagonal three-color path Ramsey number.

## transfer_kit

### usable_lemmas
- DS1.17 records the asymptotic formula R(Pn, Pn, Pn) = 2n - 2 + (n mod 2) for large n and says P10 is the first open diagonal case.
- The same survey records the exact predecessor values R(P8, P8, P8) = 14 and R(P9, P9, P9) = 17.
- The 2016 path paper proves that if R(C2m, C2m, C2m) = 4m then R(P2m+1, P2m+1, P2m+1) = 4m + 1, clarifying where transfer from cycle methods is available and where it is not.

### toy_example
The nearest solved diagonal path values are R(P8, P8, P8) = 14 and R(P9, P9, P9) = 17, while the conjectural P10 target is 18.

### known_obstruction
Any upper-bound proof must eliminate 17-vertex three-color templates with all monochromatic components shorter than P10, while a disproof must exhibit one explicit 18-vertex coloring without a monochromatic P10.

### prior_work_stop_sentence
The June 7, 2024 Ramsey survey states that P10 is the first open diagonal three-color path case.

### recommended_first_attack
Start from the conjectural 17-vertex extremal block template and prove that every 18th-vertex extension forces a monochromatic P10 via a stability analysis.

### paper_if_solved
The paper would be a short exact-value note closing the first open diagonal three-color path Ramsey number.
