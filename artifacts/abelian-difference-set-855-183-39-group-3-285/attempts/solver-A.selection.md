# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-855-183-39-group-3-285`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (855,183,39) in group [3,285].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle the exact Table 2 row (855,183,39) in the group C_3 x C_285.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `low`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.79`
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
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/abelian-difference-set-855-183-39-group-3-285/working_packet.md`
- paper_shape: `A short exact-group residual-row note from the multiplier-conjecture survey.`

## question
Does the abelian group C_3 x C_285 admit a (855,183,39)-difference set?

## canonical_statement
Determine whether the abelian group C_3 x C_285 admits a (855,183,39)-difference set.

## intended_statement
Determine whether the abelian group C_3 x C_285 admits a (855,183,39)-difference set.

## pre_solve_gate_reason
The exact row is source-anchored in Table 2, local memory shows no prior attempt on this canonical problem key, and the bounded exact-tuple, alternate-notation, and recent-status web sweeps on 2026-04-15 did not surface a later settlement or a broader theorem already forcing the [3,285] case.

## micro_paper_assessment
Cleanest surviving lane-eligible packet in this run: exact row, strong family anchor, no local attempt conflict, and bounded novelty audit came back quiet enough to justify the strict lane.

## hypothetical_title
On the (855,183,39) Difference-Set Problem in C_3 x C_285

## hypothetical_abstract
We determine whether the abelian group C_3 x C_285 admits a (855,183,39)-difference set. Gordon and Schmidt isolate this exact row in Table 2 of their multiplier-conjecture survey among the smallest open cases. A decisive proof would therefore remove a named residual case with only light expository work beyond the proof itself.

## single_solve_paper_explanation
The source already isolates an exact title theorem, so solving this one row would contribute nearly all of the mathematics of a short note. What would remain is a brief explanation of the Table 2 context and the decisive orbit or quotient argument. The target is not just a curiosity because it removes an explicit residual row in a canonical open-case table. The bounded web sweep also did not expose a broader published theorem that already settles the [3,285] case.

## broader_theorem_nonimplication_note
The survey still lists the exact [3,285] row as open, and the bounded 2026-04-15 exact-tuple, group-notation, and recent-status searches did not surface any later theorem directly forcing or forbidding this specific group case.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing the exact row (855,183,39) in group [3,285] as open; the bounded 2026-04-15 web sweep did not surface a later direct settlement.

## publication_packet_title
On the (855,183,39) Difference-Set Problem in C_3 x C_285

## publication_packet_frontier_basis
Gordon-Schmidt 2016 Table 2 isolates the exact [3,285] row as open, the bounded 2026-04-15 web sweep surfaced no later direct settlement, and the local attempt registry does not contain this canonical problem key.

## publication_packet_near_paper_reason
An exact solve would already read like the title theorem of a short paper because the canonical source isolates the row and only light framing around the Table 2 residual list would remain.

## publication_packet_literature_scope
Gordon-Schmidt 2016 Table 2 together with bounded exact-tuple, alternate-notation, and recent-status web searches on 2026-04-15 and local attempt-registry memory.

## publication_packet_artifact_requirements
A proof or disproof in C_3 x C_285, the decisive orbit or quotient constraints used, and a short explanation of why the row survives the survey machinery.

## paper_shape
A short exact-group residual-row note from the multiplier-conjecture survey.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt 2016 explicitly isolate the exact group row [3,285], so the theorem slice stays narrow and source-faithful.
- For (855,183,39), the order n = k - lambda = 144 = 2^4 * 3^2, and Table 2 records the multiplier-conjecture prime data attached to the row.
- The decomposition C_3 x C_285 = C_3^2 x C_5 x C_19 gives immediate quotient tests on the 3-part, 5-part, and 19-part images of any hypothetical difference set.

### toy_example
Project a hypothetical set to the 19-part quotient and test whether any multiplier-fixed orbit partition can sum to 183 while matching lambda = 39.

### known_obstruction
The row already survives the survey's standard multiplier filters, so any proof must sharpen the quotient or orbit bookkeeping beyond what Table 2 records.

### prior_work_stop_sentence
Gordon-Schmidt 2016 list (855,183,39) in group [3,285] as open in Table 2.

### recommended_first_attack
Exploit the C_3^2 x C_5 x C_19 decomposition and test whether the recorded multiplier information forces an orbit partition incompatible with total size 183 and lambda = 39.

### paper_if_solved
If solved exactly, the paper would be a short residual-row note on the Table 2 case (855,183,39) in C_3 x C_285.
