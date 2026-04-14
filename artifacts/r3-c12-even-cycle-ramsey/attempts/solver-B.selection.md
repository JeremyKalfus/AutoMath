# Determine the exact value of R(C12, C12, C12)

- entry_type: `paper_candidate`
- slug: `r3-c12-even-cycle-ramsey`
- worker_role: `solver-B`
- canonical_source: `Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 6.3.1.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing the next even-cycle value after the already-preserved C10 residue would still yield a clean exact-value Ramsey note with an established family narrative.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `80`
- single_solve_to_paper_fraction: `0.75`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `small`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r3-c12-even-cycle-ramsey/working_packet.md`
- paper_shape: `A one-theorem note giving the exact three-color Ramsey number for a single even cycle length.`

## question
Is R(C12, C12, C12) = 24?

## canonical_statement
Determine the exact value of R(C12, C12, C12).

## intended_statement
Either prove that every 3-coloring of K24 contains a monochromatic C12, or construct a 3-coloring of K24 with no monochromatic C12 and thus show R(C12, C12, C12) >= 25.

## pre_solve_gate_reason
The latest survey still records the three-color even-cycle exact program as unresolved beyond the smaller cases and does not list a later exact determination for C12.

## micro_paper_assessment
Pass. The exact statement is bounded, the family anchor is strong, and the paper would still be title-theorem-shaped after one successful solve.

## hypothetical_title
The Exact Value of R(C12, C12, C12)

## hypothetical_abstract
We determine the exact three-color Ramsey number R(C12, C12, C12). The January 6, 2026 Ramsey survey still presents the three-color even-cycle formula as unresolved in bounded small cases and does not list a later exact value for C12. Our theorem fixes one concrete even-cycle residue in the exact multicolor Ramsey table.

## single_solve_paper_explanation
The solve itself would be the note. Standard lower-bound constructions and the conjectural family formula already explain why C12 matters, so after the exact argument is found, only brief packaging remains. The candidate passes the paper test because it is a named exact-cycle slice with immediate table-level consequences rather than an isolated curiosity.

## broader_theorem_nonimplication_note
Known large-n even-cycle theorems and conjectural formulas do not automatically settle the exact C12 case, and the survey still treats bounded small even cycles separately from the asymptotic regime.

## literature_gap
Radziszowski's January 6, 2026 survey does not list an exact value for R(C12, C12, C12) while still presenting the three-color even-cycle formula only as a conjectural small-case guide.

## publication_packet_title
The Exact Value of R(C12, C12, C12)

## publication_packet_frontier_basis
Radziszowski's January 6, 2026 survey states the three-color even-cycle conjectural formula and does not report an exact resolution of the C12 case.

## publication_packet_near_paper_reason
The even-cycle formula, its lower-bound constructions, and the exact-value table already supply the narrative spine. Once C12 is settled, the remaining work is a short proof presentation and a comparison with the smaller verified cycle lengths.

## publication_packet_literature_scope
Radziszowski DS1.18 Section 6.3.1, the survey's references to Dzido and later three-color cycle papers, and bounded 2026-04-13 web searches for R(C12,C12,C12), R_3(C12), and recent-status signals.

## publication_packet_artifact_requirements
Either a proof that every 3-coloring of K24 contains a monochromatic C12, or one explicit 24-vertex three-coloring with no monochromatic C12.

## paper_shape
A one-theorem note giving the exact three-color Ramsey number for a single even cycle length.

## transfer_kit

### usable_lemmas
- Radziszowski's January 6, 2026 survey records the conjectural three-color even-cycle formula R(C2n, C2n, C2n) = 4n.
- The same survey records the first bounded open even-cycle residue earlier in the line and does not list an exact determination for C12.
- The survey's lower-bound discussion supplies the standard 4n-type extremal template that motivates 24 as the sharp target.

### toy_example
The candidate sits one step beyond the already-studied C10 residue and uses the same conjectural target value pattern 4n, here equal to 24.

### known_obstruction
Any upper-bound proof has to eliminate near-extremal 24-vertex colorings built from standard cycle-avoiding templates, while any negative result needs one explicit 24-vertex witness with no monochromatic C12.

### prior_work_stop_sentence
Radziszowski's January 6, 2026 survey does not report an exact value for R(C12, C12, C12) in the three-color even-cycle table.

### recommended_first_attack
Exploit the known 4n lower-bound construction and look for a stability argument showing that any 24th vertex or any extra cross-edge density forces a monochromatic 12-cycle.

### paper_if_solved
The paper would be a short exact-value note for one bounded three-color even-cycle Ramsey number.
