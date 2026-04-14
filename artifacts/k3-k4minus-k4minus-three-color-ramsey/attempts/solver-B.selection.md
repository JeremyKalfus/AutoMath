# Determine the exact value of R(K3, K4-e, K4-e)

- entry_type: `paper_candidate`
- slug: `k3-k4minus-k4minus-three-color-ramsey`
- worker_role: `solver-B`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 6.5(c); Luis Boza, Janusz Dybizbański, and Tomasz Dzido, "Three color Ramsey numbers for graphs with at most 4 vertices" (Electronic Journal of Combinatorics 19(4), 2012), together with its K3+e equivalence discussion; and bounded exact-term, alternate-notation, canonical-source, source-internal, outside-source, and recent-status web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing R(K3, K4-e, K4-e) would already support a standalone short note on small three-color Ramsey numbers for nearly complete four-vertex graphs.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `79`
- single_solve_to_paper_fraction: `0.78`
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
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/k3-k4minus-k4minus-three-color-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the smallest unresolved K3/J4/J4-type three-color case.`

## question
Is R(K3, K4-e, K4-e) = 21 or 22?

## canonical_statement
Determine the exact value of R(K3, K4-e, K4-e).

## intended_statement
Either prove that every 3-edge-coloring of K21 contains a first-color triangle or a second- or third-color copy of K4-e and thus show R(K3, K4-e, K4-e) = 21, or construct a 3-edge-coloring of K21 avoiding those targets and thus show R(K3, K4-e, K4-e) = 22.

## pre_solve_gate_reason
The thin-memory sweep found no prior attempt on this exact triple or its J4 notation alias, DS1.17 still records 21 <= R(K3, K4-e, K4-e) <= 22, and the bounded 2026-04-13 audit did not surface a later exact-resolution paper under either K4-e or J4 notation.

## micro_paper_assessment
Pass. This is a stable one-gap small-graph Ramsey residue with strong family anchor, low novelty-check cost, and minimal editorial overhead after a solve.

## hypothetical_title
The Exact Value of R(K3, K4-e, K4-e)

## hypothetical_abstract
We determine the three-color Ramsey number R(K3, K4-e, K4-e). Existing work leaves this case in the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22, equivalently 21 <= R(3, J4, J4) <= 22 in J4 notation. Our result closes a natural small-graph residue in the K3-versus-nearly-complete-four-vertex family.

## single_solve_paper_explanation
The exact value would already be the title theorem of the note, and the family context is standard enough that the paper would not need a long setup. Most of the eventual note would simply be the proof or extremal coloring plus a short comparison with the neighboring 2012 exact results. That keeps the solve-to-paper fraction inside the desired micro-paper band.

## broader_theorem_nonimplication_note
Known general relations among these small-graph Ramsey numbers do not force the exact value of R(K3, K4-e, K4-e); they only tie it to nearby variants such as the K3+e formulation. A proof might reveal a cleaner structural lemma, but it would still honestly be closing this exact one-gap J4/J4 survey entry rather than extracting a trivial corollary from an existing theorem.

## literature_gap
Current public sources support only the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22, and the bounded 2026-04-13 audit did not uncover a later exact determination under either K4-e or J4 notation.

## publication_packet_title
The Exact Value of R(K3, K4-e, K4-e)

## publication_packet_frontier_basis
DS1.17 lists the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22. The 2012 small-graph paper develops the K4-e / J4 three-color landscape and shows that the nearby variant with K3+e in place of K3 is equivalent to this same target, which reinforces that the exact unresolved slice is canonical rather than ad hoc.

## publication_packet_near_paper_reason
This is already a named survey-line residue with a tiny exact gap and cheap literature audit because both K4-e and J4 notations are standard. After a solve, the remaining paper work would mostly be a compact proof narrative, perhaps a short extremal-coloring census, and a discussion of how the K3+e equivalence fits around the exact value.

## publication_packet_literature_scope
DS1.17 Section 6.5(c), Dybizbański-Dzido-Boza 2012, and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, outside-source, and recent-status searches for R(K3, K4-e, K4-e) and R(3, J4, J4).

## publication_packet_artifact_requirements
Either a complete 3-color forcing proof on 21 vertices or one explicit 21-vertex extremal coloring avoiding a red K3 and blue/green K4-e.

## paper_shape
A one-theorem exact-value note on the smallest unresolved K3/J4/J4-type three-color case.

## transfer_kit

### usable_lemmas
- DS1.17 Section 6.5(c) records the current bounds 21 <= R(K3, K4-e, K4-e) <= 22.
- The 2012 small-graph paper proves that R(K3+e, K4-e, K4-e) = R(K3, K4-e, K4-e), providing an alternate-notation and nearby-variant transfer lemma.
- The same paper establishes exact adjacent cases such as R(C4, K4-e, K4-e) = 19 and R(K3, K4-e, K4) upper bounds, which help localize the small-graph landscape around the target.

### toy_example
The identity R(K3+e, K4-e, K4-e) = R(K3, K4-e, K4-e) is the smallest nearby worked example showing that tiny perturbations of the first forbidden graph need not change the exact value.

### known_obstruction
Any proof of 21 must eliminate every 21-vertex critical coloring consistent with the survey lower bound, while a proof of 22 requires one explicit 21-vertex coloring with no red triangle and no blue or green K4-e.

### prior_work_stop_sentence
Current sources stop at the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22.

### recommended_first_attack
Work in J4 notation and combine bounded critical-coloring generation with neighborhood splitting around a putative red-triangle-free color class, using the 2012 transfer lemmas to prune isomorphic K3+e variants.

### paper_if_solved
The paper would be a short exact-value note closing a canonical J4/J4 three-color Ramsey residue.
