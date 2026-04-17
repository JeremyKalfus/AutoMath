# Does the cyclic group C_419 admit a (419,133,42)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-419-133-42`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 1 listing the open cyclic row (419,133,42) among the remaining cyclic cases with k <= 150.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `Settling the exact cyclic Table 1 row (419,133,42) would plausibly give the title theorem of a short residual-case note on one of the last small-k cyclic survivors.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `88`
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
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-419-133-42/working_packet.md`
- paper_shape: `A residual-case cyclic note centered on one of the last open k <= 150 rows.`

## question
Does the cyclic group C_419 admit a (419,133,42)-difference set?

## canonical_statement
Determine whether the cyclic group C_419 admits a (419,133,42)-difference set.

## intended_statement
Determine whether the cyclic group C_419 admits a (419,133,42)-difference set.

## pre_solve_gate_reason
The exact row is source-anchored, attempt-registry clear, and the bounded exact and alternate notation search on 2026-04-15 surfaced no later direct settlement.

## micro_paper_assessment
Lane-eligible. The row is exact, source-anchored, stable under proof-genericity stress, and a successful solve would already look like 70 to 90 percent of a short paper.

## hypothetical_title
On the cyclic (419,133,42) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_419 admits a (419,133,42)-difference set. Baumert and Gordon isolate this tuple in Table 1 as one of the remaining cyclic cases with k <= 150. A direct solution would already read like the title theorem of a short note, because the surrounding literature work is mostly just source placement and a compact proof packet.

## single_solve_paper_explanation
This target already has a clean residual-case narrative from a canonical source table. Solving the exact row would supply the core theorem, the main proof, and the novelty-bearing contribution in one step. What remains afterward is mostly bounded exposition rather than follow-on mathematics.

## broader_theorem_nonimplication_note
The source already spends the standard arithmetic, BRC, Mann, Yamamoto, and multiplier screens before isolating the row, and the bounded 2026-04-15 search surface did not reveal a later result explicitly covering (419,133,42).

## literature_gap
Baumert-Gordon 2004 Table 1 stops at listing (419,133,42) as an open cyclic row, and the bounded 2026-04-15 exact-statement and alternate-notation search found no later direct settlement.

## publication_packet_title
The Cyclic (419,133,42) Difference-Set Case

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 1 isolates (419,133,42) as an exact remaining cyclic row, and the bounded 2026-04-15 exact-tuple and alternate-notation search surface did not expose a later theorem, proposition, or repository note settling it.

## publication_packet_near_paper_reason
If solved, the exact row itself would already be the title theorem; only a short literature placement and concise proof packaging would remain.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 1 and Sections 2-3, the current La Jolla Difference Set Repository surface, the bounded exact and alternate-notation web queries run on 2026-04-15, and the local attempt registry.

## publication_packet_artifact_requirements
A proof or disproof for C_419, the decisive multiplier-orbit or p-adic contradiction, and a short explanation of why the row survives the source table.

## paper_shape
A residual-case cyclic note centered on one of the last open k <= 150 rows.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 1 isolates (419,133,42) as an exact remaining cyclic row.
- Section 2 records the necessary conditions already exhausted before the tuple reaches Table 1.
- Theorem 2.4 gives the p-adic multiplier obstruction available once a prime divisor of n is known to be a multiplier.
- Theorem 3.2 gives the contracted-multiplier framework that can force orbit-size contradictions in cyclic groups.

### toy_example
Test whether 7- or 13-multiplier orbits in Z/419Z can be combined to realize k = 133 without violating the source's contracted conditions.

### known_obstruction
The easy arithmetic tests are already spent, so any proof must exploit sharper multiplier-orbit or p-adic structure in the prime-order group.

### prior_work_stop_sentence
Baumert-Gordon 2004 stops at listing (419,133,42) as an open cyclic case in Table 1.

### recommended_first_attack
Use Theorem 3.2 with the prime divisors 7 and 13 of n = 91 to force incompatible orbit counts, then close with a counting contradiction.

### paper_if_solved
If solved exactly, the paper would be a short residual-case note on one of the last small-k open cyclic rows.
