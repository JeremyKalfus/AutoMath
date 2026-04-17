# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-2869-240-20`
- worker_role: `solver-B`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the exact cyclic row (2869,240,20) among the possible cases with 150 <= k <= 300 and gcd(v,n) = 1.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `Settling the cyclic (2869,240,20) row would plausibly support a short exact-case note closing one of the Baumert-Gordon Table 3 survivors.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `79`
- single_solve_to_paper_fraction: `0.75`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `moderate`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-2869-240-20/working_packet.md`
- paper_shape: `An exact Table 3 residual-case note driven by a compact multiplier-orbit or contraction obstruction.`

## question
Does the cyclic group C_2869 admit a (2869,240,20)-difference set?

## canonical_statement
Determine whether the cyclic group C_2869 admits a (2869,240,20)-difference set.

## intended_statement
Determine whether the cyclic group C_2869 admits a (2869,240,20)-difference set.

## pre_solve_gate_reason
The row is source-anchored, unattempted locally, and bounded exact-tuple and alternate-notation searches surfaced no direct later settlement; the solve still looks like the honest title theorem rather than a corollary of a broader reframing.

## micro_paper_assessment
Usable lane survivor. The case is exact and source-anchored, with a plausible one-shot route to a short residual-case paper.

## hypothetical_title
On the cyclic (2869,240,20) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_2869 admits a (2869,240,20)-difference set. Baumert and Gordon isolate this tuple in Table 3 among the remaining cyclic cases with 150 <= k <= 300 and gcd(v,n) = 1. A direct solution would settle an exact residual row and supply the main contribution of a short note.

## single_solve_paper_explanation
The literature already packages the row as an exact survivor, so a clean proof or disproof is most of the publishable object. What remains after the solve is mainly concise framing inside Table 3 and a short explanation of the method. That keeps the solve-to-paper distance inside the intended micro-paper band.

## broader_theorem_nonimplication_note
The source row survives the standard small-parameter screens, and the bounded exact-row plus alternate-notation searches on 2026-04-15 did not surface a later theorem explicitly settling (2869,240,20).

## literature_gap
Baumert-Gordon 2004 stops at listing (2869,240,20) as a remaining cyclic Table 3 case, and the bounded 2026-04-15 follow-up surfaced no direct later settlement of the exact tuple.

## publication_packet_title
The Cyclic (2869,240,20) Difference-Set Case

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 3 isolates (2869,240,20) as an exact surviving cyclic row with gcd(v,n) = 1, and bounded 2026-04-15 exact-row and alternate-notation searches surfaced no direct later settlement.

## publication_packet_near_paper_reason
A direct solution would already settle the advertised row and leave only short source placement and proof exposition.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 3 and Sections 2-3, bounded exact-row and alternate-notation web searches on 2026-04-15, family-level status checks against the Baumert-Gordon citation surface and Gordon's difference-set web presence, and the local attempt registry.

## publication_packet_artifact_requirements
A proof or disproof for C_2869, the decisive contracted-coefficient or multiplier-orbit contradiction, and a short note positioning the row among the surviving Table 3 cases.

## paper_shape
An exact Table 3 residual-case note driven by a compact multiplier-orbit or contraction obstruction.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 3 isolates (2869,240,20) as an exact surviving cyclic row with gcd(v,n) = 1.
- Section 2 records the necessary conditions already exhausted before the tuple reaches Table 3.
- Theorem 3.1 gives the contracted coefficient equations for every divisor w of v.
- Theorem 3.2 gives multiplier-orbit equalities whenever the prime powers of n = 220 generate a common residue modulo a divisor of v.

### toy_example
Try contraction modulo w = 41 or w = 69 and test whether the Theorem 3.1 count equations are compatible with orbits forced by 2-, 5-, or 11-power multipliers from n = 220.

### known_obstruction
The easy cyclic filters are already exhausted in the source table, so any nonexistence proof has to exploit a sharper contraction or multiplier orbit pattern.

### prior_work_stop_sentence
Baumert-Gordon 2004 stops at listing (2869,240,20) as a remaining possible cyclic case in Table 3.

### recommended_first_attack
Search for a divisor of 2869 where powers of 2, 5, or 11 induce a useful w-multiplier, then intersect the orbit equalities with the contracted-count equations from Theorem 3.1.

### paper_if_solved
If solved exactly, the paper would be a short residual-case note on the cyclic Table 3 row (2869,240,20).
