# Does the cyclic group C_1111 admit a (1111,186,31)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-1111-186-31`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the open cyclic row (1111,186,31) among the possible cases with 150 <= k <= 300 and gcd(v,n)=1.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `Settling the exact cyclic row (1111,186,31) would likely produce a short residual-case note because the source already isolates a stable exact title theorem and only light framing would remain.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `75`
- single_solve_to_paper_fraction: `0.71`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `moderate`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-1111-186-31/working_packet.md`
- paper_shape: `A short residual-case note closing one surviving Table 3 cyclic parameter row with a stable exact title theorem.`

## question
Does the cyclic group C_1111 admit a (1111,186,31)-difference set?

## canonical_statement
Determine whether the cyclic group C_1111 admits a (1111,186,31)-difference set.

## intended_statement
Determine whether the cyclic group C_1111 admits a (1111,186,31)-difference set.

## pre_solve_gate_reason
The attempt registry is clear on this exact cyclic row, Baumert-Gordon 2004 Table 3 isolates it as an open survivor, and the bounded 2026-04-15 exact-tuple plus alternate-notation searches surfaced no direct later settlement. The theorem slice is stable, the story is already paper-shaped if solved, and the remaining packaging looks light rather than campaign-like.

## micro_paper_assessment
Lane-eligible. The theorem slice is stable, the source anchor is exact, the single-solve-to-paper fraction clears the 0.70 gate, and the remaining writeup burden looks light rather than campaign-like.

## hypothetical_title
On the cyclic (1111,186,31) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_1111 admits a (1111,186,31)-difference set. Baumert and Gordon isolate this tuple in Table 3 among the remaining cyclic cases with 150 <= k <= 300 and gcd(v,n)=1. A definitive proof would largely complete a short residual-case note because the exact theorem slice is already fixed by the source table.

## single_solve_paper_explanation
The canonical source already isolates an exact cyclic residual row, so the solve itself would be the title theorem rather than just feeder evidence. The remaining work after the solve is limited to writing the multiplier or contraction argument cleanly and situating it against Table 3. That is close enough to the 70-90% paper threshold to keep the row in the strict micro-paper lane.

## broader_theorem_nonimplication_note
No surfaced broader theorem or later corollary explicitly discharges (1111,186,31), and the honest proof target remains this exact cyclic tuple rather than an obviously broader ambient classification statement.

## literature_gap
Baumert-Gordon 2004 Table 3 lists the cyclic parameter row (1111,186,31) as possible, and the bounded 2026-04-15 exact-tuple and alternate-notation sweep surfaced no direct later settlement.

## publication_packet_title
The Cyclic (1111,186,31) Difference-Set Case

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 3 isolates (1111,186,31) as one of the surviving cyclic rows with 150 <= k <= 300 and gcd(v,n)=1, and the bounded 2026-04-15 follow-up did not expose a direct later discharge.

## publication_packet_near_paper_reason
One decisive proof would already settle the exact theorem named in the title, with only bounded exposition on the published Table 3 filters and the decisive multiplier or contraction argument left to write up.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 3 and Sections 2-3, Gordon's current publications and repository web surface, the local attempt registry, and the bounded 2026-04-15 exact-tuple plus alternate-notation status sweep.

## publication_packet_artifact_requirements
A proof or disproof for C_1111, the decisive multiplier-orbit or contracted-residue contradiction, and a short literature note explaining why the tuple survives the published Table 3 filters.

## paper_shape
A short residual-case note closing one surviving Table 3 cyclic parameter row with a stable exact title theorem.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 3 isolates (1111,186,31) as an exact surviving cyclic row.
- Section 2 of Baumert-Gordon records the standard necessary conditions already exhausted at the table-building stage.
- Theorem 3.1 and Theorem 3.2 in Baumert-Gordon provide the contracted-coefficient and multiplier-orbit framework for a tuple-specific contradiction.
- For nontrivial characters of a cyclic difference set, the standard relation |chi(D)|^2 = n gives a fixed target value n = 155.

### toy_example
Project modulo 101 and modulo 11 and compare whether a candidate 31-multiplier orbit partition can realize k = 186 with n = 155.

### known_obstruction
The published Table 3 arithmetic filters already remove easy cases, so any exact proof must sharpen contraction or multiplier analysis rather than recycle standard admissibility tests.

### prior_work_stop_sentence
Baumert-Gordon 2004 Table 3 lists (1111,186,31) as a remaining possible cyclic case, and the bounded 2026-04-15 follow-up surfaced no later direct settlement.

### recommended_first_attack
Use the factorization 1111 = 11 * 101 and n = 155 = 5 * 31 to compare multiplier-orbit partitions against contractions modulo the two prime factors of v.

### paper_if_solved
If solved exactly, the paper would be a short residual-case note on the cyclic Table 3 row (1111,186,31).
