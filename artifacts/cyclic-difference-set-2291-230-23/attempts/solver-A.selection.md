# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-2291-230-23`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the exact cyclic row (2291,230,23) among the possible cases with 150 <= k <= 300 and gcd(v,n) = 1.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `Settling the cyclic (2291,230,23) row would plausibly support a short residual-case note on one exact Baumert-Gordon survivor.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short-medium`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `75`
- single_solve_to_paper_fraction: `0.71`
- title_theorem_strength: `moderate`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
- editorial_overhead: `moderate`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `moderate`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `moderate`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/cyclic-difference-set-2291-230-23/working_packet.md`
- paper_shape: `An exact cyclic residual-case note if solved, with slightly more framing and status-check burden than the top two slots.`

## question
Does the cyclic group C_2291 admit a (2291,230,23)-difference set?

## canonical_statement
Determine whether the cyclic group C_2291 admits a (2291,230,23)-difference set.

## intended_statement
Determine whether the cyclic group C_2291 admits a (2291,230,23)-difference set.

## pre_solve_gate_reason
The row is source-anchored and unattempted locally, and bounded exact-row, alternate-notation, and family-level status searches surfaced no direct later settlement; the packet now clears the strict 70 percent paper threshold, though only narrowly.

## micro_paper_assessment
Lane-eligible but not by much. The packet is exact and source-anchored, yet the solve-to-paper distance is a little longer than the top two candidates.

## hypothetical_title
On the cyclic (2291,230,23) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_2291 admits a (2291,230,23)-difference set. Baumert and Gordon isolate this tuple in Table 3 among the remaining cyclic cases with 150 <= k <= 300 and gcd(v,n) = 1. A direct solution would settle an exact residual row and provide the core content of a short note, with modest additional framing still required.

## single_solve_paper_explanation
This is still an honest exact theorem target rather than feeder work. If solved, the mathematical core of the note would already be present, and what remains is mostly careful source placement plus a bounded novelty discussion. The paper fraction is only barely in-band, which is why this ranks below the top two slots.

## broader_theorem_nonimplication_note
The source isolates the exact row after standard screens, and the bounded exact-row, alternate-notation, and family-level status searches on 2026-04-15 did not surface a later theorem explicitly settling (2291,230,23).

## literature_gap
Baumert-Gordon 2004 stops at listing (2291,230,23) as a remaining cyclic Table 3 case, and the bounded 2026-04-15 follow-up surfaced no direct later settlement for the exact tuple.

## publication_packet_title
The Cyclic (2291,230,23) Difference-Set Case

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 3 isolates (2291,230,23) as an exact surviving cyclic row with gcd(v,n) = 1, and bounded 2026-04-15 exact-row, alternate-notation, and family-level status searches surfaced no direct later settlement.

## publication_packet_near_paper_reason
A solve would still give a genuine residual-case title theorem, but this packet needs slightly more framing and broader-status caution than the top two slots.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 3 and Sections 2-3, bounded exact-row and alternate-notation web searches on 2026-04-15, family-level status checks against the Baumert-Gordon citation surface and Gordon's difference-set web presence, and the local attempt registry.

## publication_packet_artifact_requirements
A proof or disproof for C_2291, the decisive contracted-count or multiplier-orbit contradiction, and a short note locating the row inside the surviving Table 3 list.

## paper_shape
An exact cyclic residual-case note if solved, with slightly more framing and status-check burden than the top two slots.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 3 isolates (2291,230,23) as an exact surviving cyclic row with gcd(v,n) = 1.
- Section 2 records the necessary conditions already exhausted before the tuple reaches Table 3.
- Theorem 3.1 gives contracted coefficient equations for every divisor w of v.
- Theorem 3.2 gives multiplier-orbit equalities whenever the prime powers of n = 207 generate a common residue modulo a divisor of v.

### toy_example
Check whether contraction modulo w = 29 or w = 79 can satisfy Theorem 3.1 together with orbit equalities forced by powers of 3 or 23 from n = 207.

### known_obstruction
The standard cyclic necessary conditions have already been spent in the source table, so only sharper contraction or multiplier structure remains available.

### prior_work_stop_sentence
Baumert-Gordon 2004 stops at listing (2291,230,23) as a remaining possible cyclic case in Table 3.

### recommended_first_attack
Try a divisor of 2291 where powers of 3 or 23 generate a useful w-multiplier, then combine orbit equalities with the Theorem 3.1 contracted-count equations.

### paper_if_solved
If solved exactly, the paper would be a short residual-case note on the cyclic Table 3 row (2291,230,23).
