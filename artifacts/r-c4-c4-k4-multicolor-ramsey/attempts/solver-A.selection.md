# Determine the exact value of R(C4, C4, K4)

- entry_type: `paper_candidate`
- slug: `r-c4-c4-k4-multicolor-ramsey`
- worker_role: `solver-A`
- canonical_source: `Xiaodong Xu, Zehui Shao, and Stanislaw P. Radziszowski, "Bounds on Some Ramsey Numbers Involving Quadrilateral" (2008), Theorem 3 and Table 1, which give 19 <= R(C4, C4, K4) <= 22; together with Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 8, which improves the upper bound to 21; plus bounded 2026-04-14 exact-notation and recent-status web checks that did not reveal a later exact closure.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(C4, C4, K4) would be the title theorem of a compact note because the live frontier gap is a single unresolved step after the 2021 upper-bound improvement.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `88`
- single_solve_to_paper_fraction: `0.86`
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
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-c4-c4-k4-multicolor-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note closing a one-step multicolor C4/K4 Ramsey gap.`

## question
Is R(C4, C4, K4) equal to 20 or 21?

## canonical_statement
Determine the exact value of R(C4, C4, K4).

## intended_statement
Determine the least n such that every 3-coloring of E(K_n) contains either a color-1 C4, a color-2 C4, or a color-3 K4.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this slug, title, or exact parameter tuple, and no artifact-name near-duplicate. The bounded web audit found the 2008 lower bound and 2021 upper bound, plus no later exact determination in the 2026-04-14 search budget.

## micro_paper_assessment
Pass. This is the cleanest one-step gap found in the bounded audit, with strong family anchor and low editorial residue after a solve.

## hypothetical_title
The Exact Value of R(C4, C4, K4)

## hypothetical_abstract
We determine the 3-color Ramsey number R(C4, C4, K4). Earlier work gave 19 <= R(C4, C4, K4) <= 22, and semidefinite programming later reduced the upper bound to 21. Our result closes the remaining one-step gap and identifies the exact threshold for forcing two monochromatic quadrilaterals or a monochromatic K4.

## single_solve_paper_explanation
This target already has the right paper shape because the frontier is a one-step exact-value gap. Once the exact lower or upper endpoint is proved, most of the note is finished: statement, motivation, and context are already supplied by the prior literature. What remains is mainly polishing the proof or presenting the extremal coloring cleanly.

## broader_theorem_nonimplication_note
Known asymptotic or monotonicity statements for multicolor C4-Ramsey numbers do not force the finite endpoint 20 or 21. The 2021 SDP result improves only the upper side and does not imply exactness.

## literature_gap
Current public sources stop at 20 <= R(C4, C4, K4) <= 21.

## publication_packet_title
The Exact Value of R(C4, C4, K4)

## publication_packet_frontier_basis
Current public sources leave this multicolor Ramsey number at 20 <= R(C4, C4, K4) <= 21. The 2021 semidefinite-programming paper narrows the upper side but does not settle the lower endpoint.

## publication_packet_near_paper_reason
If solved exactly, the proof or critical coloring is almost the entire paper. The surrounding literature and motivation are already in place, so the remaining work is mainly proof presentation, a compact extremal certificate, and one short discussion paragraph.

## publication_packet_literature_scope
2008 Xu-Shao-Radziszowski for the lower bound and early table, 2021 Lidicky-Pfender for the tightened upper bound, plus bounded 2026-04-14 exact-notation and recent-status web checks.

## publication_packet_artifact_requirements
Either an explicit (C4, C4, K4; 20)-coloring or a proof that every 3-coloring of K20 already forces one of the forbidden monochromatic subgraphs; in either direction the certificate must be compact and human-checkable.

## paper_shape
A one-theorem exact-value note closing a one-step multicolor C4/K4 Ramsey gap.

## transfer_kit

### usable_lemmas
- Xu-Shao-Radziszowski (2008), Theorem 3, gives the constructive lower bound R(C4, C4, K4) >= 19.
- Xu-Shao-Radziszowski (2008), Table 1, records the pre-2021 interval 19 <= R(C4, C4, K4) <= 22.
- Lidicky-Pfender (2021), Theorem 8, improves the upper bound to R(C4, C4, K4) <= 21.
- The product-coloring lower-bound method highlighted in the 2008 paper remains a concrete template for extremal constructions in this family.

### toy_example
The exact coloring in Xu-Shao-Radziszowski proving a (C4, C4, K4; 18)-coloring is the smallest concrete extremal instance immediately below the current live gap.

### known_obstruction
A lower-bound attack must build a 20-vertex 3-coloring simultaneously avoiding two monochromatic C4 copies in different colors and a monochromatic K4 in the third color; an upper-bound attack must exclude every such coloring.

### prior_work_stop_sentence
Current sources stop at 20 <= R(C4, C4, K4) <= 21.

### recommended_first_attack
Exploit the 2021 SDP profile to extract forbidden local patterns, then combine that with a structured extension search from the known 18-vertex lower-bound coloring.

### paper_if_solved
The paper would be a concise exact-value note closing the last one-step gap for this specific multicolor quadrilateral/clique Ramsey number.
