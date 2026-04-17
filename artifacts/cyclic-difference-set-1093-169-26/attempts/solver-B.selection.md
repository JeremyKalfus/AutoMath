# Does the cyclic group C_1093 admit a (1093,169,26)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-1093-169-26`
- worker_role: `solver-B`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the open cyclic row (1093,169,26) among the possible cases with 150 <= k <= 300 and gcd(v,n)=1.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Settling the exact cyclic row (1093,169,26) would likely yield a short residual-case note because the source already isolates the title theorem and the family anchor.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `77`
- single_solve_to_paper_fraction: `0.74`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
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
- working_packet_path: `artifacts/cyclic-difference-set-1093-169-26/working_packet.md`
- paper_shape: `A short residual-case note closing one open Table 3 cyclic parameter row.`

## question
Does the cyclic group C_1093 admit a (1093,169,26)-difference set?

## canonical_statement
Determine whether the cyclic group C_1093 admits a (1093,169,26)-difference set.

## intended_statement
Determine whether the cyclic group C_1093 admits a (1093,169,26)-difference set.

## pre_solve_gate_reason
The local memory surfaces show no exact or near-duplicate attempt on this tuple. Baumert-Gordon 2004 Table 3 still isolates (1093,169,26), and the bounded 2026-04-15 exact-tuple, alternate-notation, and Gordon-site sweeps surfaced no later direct settlement; the prime-order ambient group keeps the honest theorem slice clean rather than pushing it toward a broader ambient claim.

## micro_paper_assessment
Clean second lane candidate: exact row, quiet novelty surface, and a prime-order ambient group that keeps the paper packet tight.

## hypothetical_title
On the cyclic (1093,169,26) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_1093 admits a (1093,169,26)-difference set. Baumert and Gordon isolate this tuple in Table 3 as one of the remaining cyclic possibilities with 150 <= k <= 300 and gcd(v,n)=1. A decisive proof would close an exact residual case with only light post-solve exposition remaining.

## single_solve_paper_explanation
The statement is already paper-shaped before any new mathematics begins because the source table singles it out as an exact survivor. A one-pass proof would contribute both the central theorem and most of the eventual narrative. What would remain after the solve is only a compact explanation of how this row sits among the few surviving cyclic tuples.

## broader_theorem_nonimplication_note
No surfaced later theorem settled (1093,169,26) as a corollary of a broader cyclic classification result; the later multiplier-theorem surface that explicitly advertises sibling eliminations did not expose this tuple as already resolved.

## literature_gap
Baumert-Gordon 2004 Table 3 lists the cyclic parameter row (1093,169,26) as possible, and the bounded 2026-04-15 exact-tuple, alternate-notation, and Gordon-site searches surfaced no later direct settlement of that exact row.

## publication_packet_title
On the Cyclic (1093,169,26) Difference-Set Problem

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 3 lists the exact cyclic row (1093,169,26) as open, and the bounded 2026-04-15 later-source sweep did not reveal a direct discharge.

## publication_packet_near_paper_reason
The exact statement is already fixed by the source table and already reads like the title theorem of a short note. After a solve, only concise framing and comparison to the remaining Table 3 survivors would be left.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 3 and Sections 2-3, the later multiplier-theorem surface on sibling rows, the Gordon web surface, and the local attempt and search registries.

## publication_packet_artifact_requirements
A proof or disproof for C_1093, the decisive multiplier or cyclotomic argument, and a short explanation of why the standard Table 3 eliminations stop short of this row.

## paper_shape
A short residual-case note closing one open Table 3 cyclic parameter row.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 3 isolates (1093,169,26) as a surviving cyclic case.
- Section 2 of Baumert-Gordon records the standard necessary conditions already exhausted on neighboring tuples, so the remaining task is inherently a residual-case argument rather than a full fresh census.
- Theorem 3.1 and Theorem 3.2 in Baumert-Gordon provide contracted coefficient identities and multiplier-orbit constraints that are directly reusable in a row-specific proof.

### toy_example
Because 1093 is prime, model a putative set by the orbit partition of nonzero residues under a candidate multiplier coming from n = 143 = 11 * 13 and test whether the orbit sizes can sum to k = 169.

### known_obstruction
The stock arithmetic tests already fail to eliminate this tuple, so any proof must sharpen the multiplier or cyclotomic residue analysis beyond the published table construction.

### prior_work_stop_sentence
Baumert-Gordon 2004 Table 3 lists (1093,169,26) as a remaining possible cyclic case, and the bounded 2026-04-15 search surfaced no later direct settlement.

### recommended_first_attack
Exploit the prime-order ambient group and force 11- and 13-multiplier orbit structures on F_1093^x, then compare the allowed orbit partitions with k = 169 and lambda = 26.

### paper_if_solved
If solved exactly, the paper would be a short note closing the Table 3 cyclic row (1093,169,26).
