# Determine the exact value of R(C4, C4, K4)

- entry_type: `paper_candidate`
- slug: `c4-c4-k4-three-color-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 6.3.3(a); Janusz Dybizbański, Tomasz Dzido, and Luis Boza, "Three color Ramsey numbers for graphs with at most 4 vertices" (Electronic Journal of Combinatorics 19(4), 2012), especially the C4/K4-e/K4 section; Luis Boza and Stanisław P. Radziszowski, "Some upper bounds on Ramsey numbers involving C4" (Discussiones Mathematicae Graph Theory 45, 2025), Case #6; and bounded exact-term, alternate-notation, canonical-source, source-internal, outside-source, and recent-status web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing the one-gap case R(C4, C4, K4) would already read as the title theorem of a genuine short note on multicolor Ramsey numbers involving quadrilaterals.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `83`
- single_solve_to_paper_fraction: `0.81`
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
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/c4-c4-k4-three-color-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note closing the smallest remaining one-gap C4/C4/K4 three-color case.`

## question
Is R(C4, C4, K4) = 20 or 21?

## canonical_statement
Determine the exact value of R(C4, C4, K4).

## intended_statement
Either prove that every 3-edge-coloring of K20 contains a first-color C4, a second-color C4, or a third-color K4 and thus show R(C4, C4, K4) = 20, or construct a 3-edge-coloring of K20 avoiding those targets and thus show R(C4, C4, K4) = 21.

## pre_solve_gate_reason
The thin-memory sweep found no prior attempt on this exact triple, DS1.17 still records the one-gap window 20 <= R(C4, C4, K4) <= 21, the 2025 C4 upper-bound paper still cites 21 as the active upper bound, and the bounded 2026-04-13 audit did not surface a later exact-resolution paper.

## micro_paper_assessment
Pass. This is a stable one-gap multicolor Ramsey residue with a named family anchor, low novelty-check cost, and a clear short-note paper packet if solved.

## hypothetical_title
The Exact Value of R(C4, C4, K4)

## hypothetical_abstract
We determine the three-color Ramsey number R(C4, C4, K4). Existing work leaves this multicolor quadrilateral case in the one-gap window 20 <= R(C4, C4, K4) <= 21. Our result closes a natural benchmark problem in the C4-versus-clique line and sharpens an input that is reused in later upper-bound arguments.

## single_solve_paper_explanation
The exact value is already the honest title theorem. The surrounding literature has already done most of the framing work, so a successful solve would leave only a short exposition of the extremal coloring or forcing mechanism and a comparison with nearby C4/K4 cases. That is close to the ideal 70-90% micro-paper profile.

## broader_theorem_nonimplication_note
No known general theorem already collapses this to a broader formula: the available C4 multicolor results give asymptotics or concrete upper-bound machinery, but not an exact evaluation of the small triple (C4, C4, K4). A shortest proof might illuminate a wider pattern, yet the honest frontier claim would still remain this exact one-gap case.

## literature_gap
Current public sources support only the one-gap window 20 <= R(C4, C4, K4) <= 21, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(C4, C4, K4)

## publication_packet_frontier_basis
DS1.17 records the current one-gap window 20 <= R(C4, C4, K4) <= 21. The 2012 small-graph paper organized the surrounding C4/K4-e/K4 landscape, and the 2025 C4 upper-bound paper still relies on R(C4, C4, K4) <= 21 as input for its later multicolor bounds, indicating the exact case remains open.

## publication_packet_near_paper_reason
The problem already has a mature literature shell: the exact statement is canonical, the gap is one, and the surrounding family is active enough that a closure immediately improves a reusable benchmark. After a solve, the note would mainly need the extremal coloring or forcing argument, a short comparison with adjacent C4/K4 cases, and perhaps a compact critical-graph discussion.

## publication_packet_literature_scope
DS1.17 Section 6.3.3(a), Dybizbański-Dzido-Boza 2012, Boza-Radziszowski 2025, and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, outside-source, and recent-status searches for R(C4, C4, K4).

## publication_packet_artifact_requirements
Either a complete 3-color forcing proof on 20 vertices or one explicit 20-vertex extremal coloring avoiding two quadrilateral colors and one K4 color.

## paper_shape
A one-theorem exact-value note closing the smallest remaining one-gap C4/C4/K4 three-color case.

## transfer_kit

### usable_lemmas
- DS1.17 Section 6.3.3(a) records the current bounds 20 <= R(C4, C4, K4) <= 21.
- The 2025 C4 upper-bound paper explicitly uses R(C4, C4, K4) <= 21 as known input in Case #6, so the upper bound is still current in the post-DS1 literature.
- The 2012 three-color small-graph paper proves exact neighboring values such as R(C4, C4, K4-e) = 16 and develops transfer lemmas among K4-e and K3+e variants around this triple.

### toy_example
The exact value R(C4, C4, K4-e) = 16 is the smallest nearby worked case showing how two quadrilateral colors interact with a nearly-complete clique color.

### known_obstruction
Any proof of 20 must rule out every 20-vertex critical coloring compatible with the known one-gap window, while a proof of 21 needs a single explicit 20-vertex 3-coloring with no first-color C4, no second-color C4, and no third-color K4.

### prior_work_stop_sentence
Current sources stop at the one-gap window 20 <= R(C4, C4, K4) <= 21.

### recommended_first_attack
Start from the known 20-vertex lower-bound colorings implicit in the survey line and try a bounded critical-coloring census with symmetry reduction, using the exact 2025 upper-bound input structure to force C4 creation under any extension.

### paper_if_solved
The paper would be a short exact-value note closing the smallest surviving one-gap C4/C4/K4 benchmark.
