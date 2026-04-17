# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-816-326-130-group-2-408`
- worker_role: `solver-B`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (816,326,130) in group [2,408].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle the exact Table 2 row (816,326,130) in C_2 x C_408.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `78`
- single_solve_to_paper_fraction: `0.76`
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
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/abelian-difference-set-816-326-130-group-2-408/working_packet.md`
- paper_shape: `A short exact-group residual-row note from the multiplier-conjecture survey.`

## question
Does the abelian group C_2 x C_408 admit a (816,326,130)-difference set?

## canonical_statement
Determine whether the abelian group C_2 x C_408 admits a (816,326,130)-difference set.

## intended_statement
Determine whether the abelian group C_2 x C_408 admits a (816,326,130)-difference set.

## pre_solve_gate_reason
The row is exact and locally fresh, and the bounded exact/alternate-notation web sweep surfaced no direct later settlement.

## micro_paper_assessment
Lane-eligible, though slightly less crisp than the top rows because the likely proof path looks more technical on the 2-primary side.

## hypothetical_title
On the (816,326,130) Difference-Set Problem in C_2 x C_408

## hypothetical_abstract
We determine whether the abelian group C_2 x C_408 admits a (816,326,130)-difference set. Gordon and Schmidt list this exact row as open in Table 2 of their multiplier-conjecture survey. Because the theorem slice is already exact and the bounded status sweep found no direct later settlement, the solve itself would form the core of a short note.

## single_solve_paper_explanation
The source table already isolates the exact group row, so a proof or disproof would carry most of the mathematical weight of the paper. What remains would be brief framing and proof presentation. No feeder ladder is needed.

## broader_theorem_nonimplication_note
The row survives the survey's general multiplier machinery and appears as its own exact group entry; no broader published theorem surfaced in the bounded audit that automatically settles C_2 x C_408.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing (816,326,130) in [2,408] as open; bounded exact and alternate-notation web sweeps on 2026-04-15 found no direct later settlement.

## publication_packet_title
On the (816,326,130) Difference-Set Problem in C_2 x C_408

## publication_packet_frontier_basis
Gordon-Schmidt 2016 Table 2 isolates the exact [2,408] row as open, and local attempt/source memory shows no prior run on this exact statement.

## publication_packet_near_paper_reason
One exact solve would directly resolve the row named in the survey table, so the post-solve workload is only light exposition and context.

## publication_packet_literature_scope
Gordon-Schmidt 2015/2016 Table 2, bounded exact-statement and alternate-notation web sweeps on 2026-04-15, and local attempt/source registry checks.

## publication_packet_artifact_requirements
A proof or disproof in C_2 x C_408, the decisive quotient or orbit argument, and a short explanation of the surviving multiplier obstruction.

## paper_shape
A short exact-group residual-row note from the multiplier-conjecture survey.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt 2016 isolate the exact [2,408] row in Table 2, fixing the target theorem.
- For (816,326,130), the order is n = 196 = 2^2 x 7^2, so the main multiplier pressure on the odd side comes from the prime 7.
- The group C_2 x C_408 decomposes as C_2 x C_8 x C_3 x C_17, giving natural projections to the odd quotients and the 2-primary component.

### toy_example
Project to the C_17 quotient and test whether a 7-multiplier-fixed orbit partition can realize total size 326.

### known_obstruction
The standard multiplier filters do not already kill the row, so a successful proof must sharpen orbit or quotient bookkeeping beyond the published table.

### prior_work_stop_sentence
Gordon-Schmidt 2016 list (816,326,130) in group [2,408] as open in Table 2.

### recommended_first_attack
Exploit the C_2 x C_8 x C_3 x C_17 decomposition and compare 7-multiplier orbit sizes with the allowed odd-quotient occupancies.

### paper_if_solved
If solved exactly, the paper would be a short residual-row note on the Table 2 case (816,326,130) in C_2 x C_408.
