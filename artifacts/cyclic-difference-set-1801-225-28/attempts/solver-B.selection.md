# Does the cyclic group C_1801 admit a (1801,225,28)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-1801-225-28`
- worker_role: `solver-B`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the open cyclic row (1801,225,28) among the possible cases with 150 <= k <= 300 and gcd(v,n)=1.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `Settling the exact cyclic Table 3 row (1801,225,28) would likely produce a short residual-case note with only light framing beyond the proof.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `83`
- single_solve_to_paper_fraction: `0.72`
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
- working_packet_path: `artifacts/cyclic-difference-set-1801-225-28/working_packet.md`
- paper_shape: `A compact residual-case note on one untouched Table 3 cyclic row.`

## question
Does the cyclic group C_1801 admit a (1801,225,28)-difference set?

## canonical_statement
Determine whether the cyclic group C_1801 admits a (1801,225,28)-difference set.

## intended_statement
Determine whether the cyclic group C_1801 admits a (1801,225,28)-difference set.

## pre_solve_gate_reason
The row is source-anchored, attempt-registry clear, and the bounded exact and alternate-notation search on 2026-04-15 surfaced no later direct settlement.

## micro_paper_assessment
Lane-eligible. The row is exact, source-anchored, and compact enough that a single successful solve would plausibly deliver most of a short paper.

## hypothetical_title
On the cyclic (1801,225,28) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_1801 admits a (1801,225,28)-difference set. Baumert and Gordon isolate this tuple in Table 3 among the surviving cyclic cases with 150 <= k <= 300 and gcd(v,n)=1. A direct solution would already be close to paper-complete because the source table supplies a ready-made frontier basis and only light packaging remains.

## single_solve_paper_explanation
This row is a stable exact theorem slice from a canonical residual table. A clean solution would supply the theorem, the proof, and the main novelty claim in one move. After that, the note would mostly need bounded exposition and source comparison.

## broader_theorem_nonimplication_note
No surfaced later theorem, proposition, example, or repository note explicitly settles (1801,225,28), and the source already spends the standard eliminations before isolating the row.

## literature_gap
Baumert-Gordon 2004 Table 3 lists the cyclic row (1801,225,28) as possible, and the bounded 2026-04-15 exact-statement and alternate-notation search found no later direct settlement.

## publication_packet_title
The Cyclic (1801,225,28) Difference-Set Case

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 3 isolates (1801,225,28) as an exact surviving cyclic row, and the bounded 2026-04-15 exact-tuple and alternate-notation search surface did not expose a later settlement.

## publication_packet_near_paper_reason
The exact row is already a crisp title theorem, and the likely remaining work after a solve is just short contextual framing.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 3 and Sections 2-3, the current La Jolla Difference Set Repository surface, the bounded exact and alternate-notation web queries run on 2026-04-15, and the local attempt registry.

## publication_packet_artifact_requirements
A proof or disproof for C_1801, the decisive multiplier-orbit or contracted-coefficient contradiction, and a short explanation of why the tuple survives Table 3.

## paper_shape
A compact residual-case note on one untouched Table 3 cyclic row.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 3 isolates (1801,225,28) as an exact surviving cyclic row.
- Section 2 records the necessary conditions already exhausted before the tuple reaches Table 3.
- Theorem 3.1 gives contracted coefficient equations for cyclic difference sets.
- Theorem 3.2 gives the multiplier-orbit framework for cyclic rows with n = 197.

### toy_example
Check whether a 197-multiplier orbit decomposition in Z/1801Z can realize k = 225 while satisfying the contracted coefficient equations.

### known_obstruction
The source table has already removed the easy arithmetic contradictions, so a proof must sharpen multiplier or contraction structure rather than recycle standard tests.

### prior_work_stop_sentence
Baumert-Gordon 2004 stops at listing (1801,225,28) as a remaining possible cyclic case in Table 3.

### recommended_first_attack
Use Theorem 3.2 to pin down multiplier orbits for n = 197 and then test them against Theorem 3.1's contracted coefficient identities.

### paper_if_solved
If solved exactly, the paper would be a short residual-case note on the cyclic Table 3 row (1801,225,28).
