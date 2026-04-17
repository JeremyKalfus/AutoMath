# Does the cyclic group C_645 admit a (645,161,40)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-645-161-40`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the open cyclic row (645,161,40) among the possible cases with 150 <= k <= 300 and gcd(v,n)=1.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Settling the exact cyclic row (645,161,40) would close one of the residual Table 3 cases and would already read like the title theorem of a short cleanup note in the cyclic difference-set lane.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `81`
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
- novelty_check_cost: `medium`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-645-161-40/working_packet.md`
- paper_shape: `A short residual-case note closing one open Table 3 cyclic parameter row.`

## question
Does the cyclic group C_645 admit a (645,161,40)-difference set?

## canonical_statement
Determine whether the cyclic group C_645 admits a (645,161,40)-difference set.

## intended_statement
Determine whether the cyclic group C_645 admits a (645,161,40)-difference set.

## pre_solve_gate_reason
The local attempt registry shows no exact or near-duplicate run on this tuple. Baumert-Gordon 2004 Table 3 still isolates (645,161,40) as an open cyclic case, and the bounded 2026-04-15 exact-tuple, alternate-notation, and Gordon-site sweeps surfaced no later direct settlement; the later multiplier-theorem surface explicitly discharges other Table 3 rows such as (419,133,42) and (1123,154,21), which lowers the risk that this row is already an unnoticed corollary.

## micro_paper_assessment
Best current lane survivor: exact row, stable theorem slice, strong family anchor, and a quiet enough novelty surface that one decisive solve would already supply most of a short note.

## hypothetical_title
On the cyclic (645,161,40) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_645 admits a (645,161,40)-difference set. Baumert and Gordon list this exact tuple as one of the surviving Table 3 cyclic cases with 150 <= k <= 300 and gcd(v,n)=1 after their standard eliminations. A definitive existence or nonexistence proof would therefore close a precise residual case rather than contribute only an isolated curiosity.

## single_solve_paper_explanation
This row is already source-anchored as a residual exact case, so the main theorem of the note is predetermined before any new work starts. One clean proof or disproof would do most of the mathematical work and most of the paper-shaping work at once. What remains after the solve is mainly a short literature recap and a comparison with neighboring Table 3 survivors.

## broader_theorem_nonimplication_note
The later multiplier-theorem surface explicitly advertises eliminations for some Table 3 rows, including (419,133,42) and (1123,154,21), but no surfaced broader theorem discharged (645,161,40); the tuple still behaves like an exact residual row rather than an already-implied corollary.

## literature_gap
Baumert-Gordon 2004 Table 3 lists the cyclic parameter row (645,161,40) as possible, and the bounded 2026-04-15 exact-tuple, alternate-notation, and Gordon-site searches surfaced no later direct settlement of that exact row.

## publication_packet_title
On the Cyclic (645,161,40) Difference-Set Problem

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 3 isolates the exact cyclic row (645,161,40) as one of the remaining possible cases with 150 <= k <= 300 and gcd(v,n)=1, and the bounded 2026-04-15 status sweep did not expose a later settlement.

## publication_packet_near_paper_reason
The source already fixes the exact title theorem, the family anchor, and the stop line in the literature. After one decisive proof or disproof, the remaining work is mostly brief context and a comparison with the few sibling Table 3 rows.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 3 and Sections 2-3, the later multiplier-theorem surface that explicitly eliminates some sibling rows, the Gordon web surface, and the local attempt and search registries.

## publication_packet_artifact_requirements
A proof or disproof for the cyclic group C_645, the decisive multiplier or contracted-residue argument, and a short explanation of why the standard Table 3 filters stop here.

## paper_shape
A short residual-case note closing one open Table 3 cyclic parameter row.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 3 isolates (645,161,40) as a surviving cyclic case, so the target theorem is source-anchored and exact.
- Section 2 of Baumert-Gordon records the standard necessary conditions already used to cull nearby tuples, including the Mann and Arasu-style filters, so any new proof can start from a sharply reduced residual case.
- Theorem 3.1 in Baumert-Gordon gives contracted coefficient equations for each divisor w of v, and Theorem 3.2 supplies multiplier-orbit constraints that can force contradictions once a candidate multiplier is fixed.

### toy_example
Contract a hypothetical set modulo 43 and modulo 15 and test whether the resulting coefficient vectors can satisfy the Table 3.1 equations with k = 161 and n = 121.

### known_obstruction
The routine arithmetic filters already leave this tuple alive, so any proof must go beyond the stock Table 3 eliminations and use sharper multiplier or contraction bookkeeping.

### prior_work_stop_sentence
Baumert-Gordon 2004 Table 3 lists (645,161,40) as a remaining possible cyclic case, and the bounded 2026-04-15 search surfaced no later direct settlement.

### recommended_first_attack
Exploit the prime square order n = 121 to force an 11-multiplier orbit structure, then compare the induced orbit sizes with contracted residue counts modulo 43 and modulo 15.

### paper_if_solved
If solved exactly, the paper would be a short residual-case note closing the cyclic Table 3 row (645,161,40).
