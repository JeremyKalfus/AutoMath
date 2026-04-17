# Does the cyclic group C_1123 admit a (1123,154,21)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-1123-154-21`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the open cyclic row (1123,154,21) among the possible cases with 150 <= k <= 300 and gcd(v,n)=1.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `Settling the exact cyclic Table 3 row (1123,154,21) would plausibly yield a short residual-case note. The theorem slice is stable, the attempt registry is clear, and the bounded exact, alternate-notation, and recent-status search surface from 2026-04-15 exposed no direct later settlement.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `82`
- single_solve_to_paper_fraction: `0.8`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
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
- working_packet_path: `artifacts/cyclic-difference-set-1123-154-21/working_packet.md`
- paper_shape: `A short residual-case note closing one surviving Table 3 cyclic row.`

## question
Does the cyclic group C_1123 admit a (1123,154,21)-difference set?

## canonical_statement
Determine whether the cyclic group C_1123 admits a (1123,154,21)-difference set.

## intended_statement
Determine whether the cyclic group C_1123 admits a (1123,154,21)-difference set.

## pre_solve_gate_reason
The exact row is source-anchored, the attempt registry is clear, the theorem slice is stable, and the bounded exact, alternate-notation, and recent-status queries surfaced no direct later settlement. This is the cleanest unattempted cyclic Table 3 survivor under the current budget.

## micro_paper_assessment
Lane-eligible. This is a source-anchored, stable exact theorem target where one clean solve plausibly supplies most of a short paper.

## hypothetical_title
On the cyclic (1123,154,21) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_1123 admits a (1123,154,21)-difference set. Baumert and Gordon isolate this tuple in Table 3 as one of the surviving cyclic cases with 150 <= k <= 300 and gcd(v,n)=1, after the standard necessary conditions have already been applied. A direct solution would itself supply the main theorem of a short residual-case note.

## single_solve_paper_explanation
The source literature already packages this as an exact residual row rather than as a feeder instance. If the row is settled, the honest paper is immediately visible: state the exact cyclic case, give the contradiction or construction, and briefly position it inside Table 3. Very little campaign work remains beyond writing the proof cleanly and recording the literature boundary.

## broader_theorem_nonimplication_note
No surfaced broader theorem, proposition, or repository status page already settles (1123,154,21). Because the canonical source isolates the exact cyclic row and the bounded later search surfaced no direct discharge, the natural title theorem remains this row rather than an obvious broader folklore corollary.

## literature_gap
Baumert-Gordon 2004 Table 3 lists the cyclic row (1123,154,21) as possible, and the bounded 2026-04-15 exact, alternate-notation, and recent-status searches surfaced no direct later settlement.

## publication_packet_title
The Cyclic (1123,154,21) Difference-Set Case

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 3 isolates (1123,154,21) as an exact surviving cyclic row, and the current La Jolla Repository remains the live status surface while the bounded 2026-04-15 exact and alternate searches surfaced no direct later settlement.

## publication_packet_near_paper_reason
One exact solve would still read like the title theorem of a short note. What remains after the solve is mostly exposition: a compact literature paragraph and the final orbit or cyclotomic contradiction.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 3 and Sections 2-3, the current La Jolla Difference Set Repository web surface, the local attempt and search registries, and the bounded exact, alternate-notation, and recent-status query surface used on 2026-04-15.

## publication_packet_artifact_requirements
A proof or disproof for C_1123, the decisive multiplier-orbit or cyclotomic contradiction, and a short note explaining why Table 3 leaves this tuple alive after the standard tests.

## paper_shape
A short residual-case note closing one surviving Table 3 cyclic row.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 3 isolates (1123,154,21) as an exact surviving cyclic row.
- Section 2 of Baumert-Gordon records the standard necessary conditions already exhausted before the tuple reaches Table 3.
- Theorem 3.1 gives the contracted coefficient equations for theta[w], providing exact orbit-count constraints.
- Theorem 3.2 gives the multiplier-orbit framework for cyclic difference sets with n = 133.

### toy_example
Test whether a putative multiplier orbit partition for n = 133 can be reconciled with k = 154 and the contracted coefficient equations from Theorem 3.1.

### known_obstruction
The easy arithmetic filters have already been spent by the source table, so any proof must extract sharper multiplier or cyclotomic structure than the table itself records.

### prior_work_stop_sentence
Baumert-Gordon 2004 stops at listing (1123,154,21) as a remaining possible cyclic case in Table 3.

### recommended_first_attack
Start with Theorem 3.1 on contracted coefficients and combine it with Theorem 3.2 multiplier orbits to force an incompatible orbit-count pattern.

### paper_if_solved
If solved exactly, the paper would be a short residual-case note closing the cyclic Table 3 row (1123,154,21).
