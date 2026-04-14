# Determine the exact value of R(C4, K1,44)

- entry_type: `paper_candidate`
- status: `NEW`
- publication_status: `NONE`
- slug: `r-c4-k1-44-quadrilateral-star-ramsey`
- canonical_source: `Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table giving 51 <= R(C4, K1,44) <= 52 and Remark 13 giving the generic lower bound n + ceil(sqrt(n)); together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014) for the star-wheel equivalence surface; together with Wu, Sun, Zhang, and Radziszowski, "Ramsey Numbers of C4 versus Wheels and Stars" (Graphs and Combinatorics 31, 2015) and Zhang-Chen-Cheng, "Polarity Graphs and Ramsey Numbers for C4 versus Stars" (Discrete Mathematics 340, 2017) as older exact-family surfaces checked not to settle n = 44; plus bounded 2026-04-14 exact-term, wheel-notation, canonical-source, and recent-status searches that did not surface a later exact closure.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `Closing R(C4, K1,44) would already read like the title theorem of a short note on quadrilateral-star Ramsey numbers.`
- publication_if_solved_score: `short_note_ready`
- solve_to_publication_distance: `low`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `83`
- single_solve_to_paper_fraction: `0.84`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `false`
- certificate_compactness: `high`
- transfer_kit_present: `true`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `true`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- paper_shape: `A one-theorem exact-value note on a one-gap quadrilateral-star residue, with a short forcing-or-witness certificate and a nearby family comparison.`

## question
Is R(C4, K1,44) equal to 51 or 52?

## canonical_statement
Determine the exact value of R(C4, K1,44).

## intended_statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,44.

## pre_solve_gate_reason
The local exclusion sweep found no prior AutoMath slug, exact title, exact tuple, or canonical-source duplicate for n = 44. The bounded audit checked the exact statement, wheel notation, the Boza 2024 table plus Remark 13, the 2015 and 2017 exact-family papers, and recent 2025-2026 status surfaces; no later exact theorem for R(C4, K1,44) surfaced.

## micro_paper_assessment
Lane-eligible. The gap is only one, the family anchor is classical, the theorem slice is stable, and one clean solve would already supply most of the paper.

## hypothetical_title
The Exact Value of R(C4, K1,44)

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,44). Current checked public sources leave this case in the one-gap corridor 51 <= R(C4, K1,44) <= 52. Our result closes a compact unresolved quadrilateral-star point with a finite certificate small enough for a short stand-alone note.

## single_solve_paper_explanation
This candidate passes the 70-90% paper test because the decisive exact closure is already the main theorem. After a solve, the note mainly needs the 51-vertex witness or forcing contradiction, a short comparison with adjacent exact values, and routine checking. It is not just a tiny curiosity because it sits inside a classical named family with a modern explicit open-status surface.

## broader_theorem_nonimplication_note
The older exact-family papers close prime-power and polarity-driven parameter families, but their stated formulas do not include n = 44. Boza's 2024 source still leaves the one-gap corridor here, and the bounded 2026-04-14 checks did not reveal any later exact-value paper for this parameter.

## literature_gap
Current checked sources stop at 51 <= R(C4, K1,44) <= 52.

## publication_packet_title
The Exact Value of R(C4, K1,44)

## publication_packet_frontier_basis
Current checked public sources support only 51 <= R(C4, K1,44) <= 52.

## publication_packet_near_paper_reason
If the gap is closed, the title theorem and literature corridor are already in place. What remains after the solve is mainly the decisive 51-vertex witness or universal forcing proof, a short comparison with nearby exact values, and routine verification.

## publication_packet_literature_scope
Boza 2024 small-values table and Remark 13; Zhang-Broersma-Chen 2014 for the star-wheel equivalence; Wu-Sun-Zhang-Radziszowski 2015 and Zhang-Chen-Cheng 2017 for older exact-family surfaces; and bounded 2026-04-14 exact-term, wheel-notation, and recent-status checks.

## publication_packet_artifact_requirements
Either a 51-vertex C4-free graph with maximum degree at most 43, or a proof that every 51-vertex C4-free graph has a vertex of degree at least 44.

## transfer_kit

### usable_lemmas
- Boza 2024 records the upper bound R(C4, K1,44) <= 52 in the small-values table.
- Boza 2024 Remark 13 yields the lower bound R(C4, K1,44) >= 44 + ceil(sqrt(44)) = 51.
- The 2014 star-wheel equivalence lets any C4-versus-star exact closure be compared against the corresponding wheel surface.
- The 2015 and 2017 exact-family papers show nearby exact regimes while leaving n = 44 outside their closed formulas.

### toy_example
The adjacent exact point R(C4, K1,45) = 53 is the smallest nearby model for how a one-gap quadrilateral-star note can close.

### known_obstruction
Any 51-vertex witness must be C4-free while keeping maximum degree at most 43, so the graph must sit near the C4-free extremal density barrier without duplicated common-neighbor pairs.

### prior_work_stop_sentence
Current checked sources stop at the one-gap window 51 <= R(C4, K1,44) <= 52.

### recommended_first_attack
Exploit the extremal C4-free edge barrier at 51 vertices to try to force a degree-44 vertex before attempting a direct witness construction.

### paper_if_solved
The paper would be a short exact-value note closing a one-gap quadrilateral-star Ramsey residue.
