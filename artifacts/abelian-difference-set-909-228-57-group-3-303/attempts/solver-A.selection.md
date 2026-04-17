# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-909-228-57-group-3-303`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (909,228,57) in group [3,303].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle the exact Table 2 row (909,228,57) in C_3 x C_303.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `80`
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
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/abelian-difference-set-909-228-57-group-3-303/working_packet.md`
- paper_shape: `A short exact-group residual-row note from the multiplier-conjecture survey.`

## question
Does the abelian group C_3 x C_303 admit a (909,228,57)-difference set?

## canonical_statement
Determine whether the abelian group C_3 x C_303 admits a (909,228,57)-difference set.

## intended_statement
Determine whether the abelian group C_3 x C_303 admits a (909,228,57)-difference set.

## pre_solve_gate_reason
The row is an exact unattempted survey residue, and the bounded exact/alternate-notation web sweep surfaced no direct later settlement.

## micro_paper_assessment
Lane-eligible. The target is a unique exact-row open case with low packaging burden and a stable short-note narrative.

## hypothetical_title
On the (909,228,57) Difference-Set Problem in C_3 x C_303

## hypothetical_abstract
We determine whether the abelian group C_3 x C_303 admits a (909,228,57)-difference set. Gordon and Schmidt list this exact row as open in Table 2 of their multiplier-conjecture survey. Since the bounded status sweep produced no direct later settlement and the theorem slice is already exact at source level, one clean solve would already deliver the core of a short note.

## single_solve_paper_explanation
The exact survey row already reads like a title theorem. Solving it would therefore contribute nearly all of the mathematics needed for publication. After the solve, only bounded exposition and context would remain.

## broader_theorem_nonimplication_note
The survey leaves [3,303] as a separate row after applying its general multiplier machinery, and no broader later theorem surfaced in the bounded audit that would automatically settle this exact group case.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing (909,228,57) in [3,303] as open; bounded exact and alternate-notation web sweeps on 2026-04-15 found no direct later settlement.

## publication_packet_title
On the (909,228,57) Difference-Set Problem in C_3 x C_303

## publication_packet_frontier_basis
Gordon-Schmidt 2016 Table 2 isolates the exact [3,303] row as open, with no local attempt-registry duplicate and no direct later hit in the bounded search sweep.

## publication_packet_near_paper_reason
A decisive proof would directly resolve the named residual row, leaving only light survey framing and proof exposition.

## publication_packet_literature_scope
Gordon-Schmidt 2015/2016 Table 2, bounded exact-statement and alternate-notation web sweeps on 2026-04-15, and local attempt/source registry checks.

## publication_packet_artifact_requirements
A proof or disproof in C_3 x C_303, the decisive multiplier-orbit or quotient argument, and a short explanation of why the row survived the published criteria.

## paper_shape
A short exact-group residual-row note from the multiplier-conjecture survey.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt 2016 isolate the exact [3,303] row in Table 2, fixing the theorem slice.
- For (909,228,57), the order is n = 171 = 3^2 x 19, so the key multiplier pressure comes from the prime 19 recorded against the row.
- The group C_3 x C_303 decomposes as C_3^2 x C_101, giving a natural large prime quotient whose orbit sizes can be compared against k = 228.

### toy_example
Project a hypothetical difference set to the C_101 quotient and test whether a 19-multiplier-fixed orbit structure can realize size 228.

### known_obstruction
The published multiplier filters do not already eliminate the row, so any proof must sharpen the quotient or orbit bookkeeping beyond the source table.

### prior_work_stop_sentence
Gordon-Schmidt 2016 list (909,228,57) in group [3,303] as open in Table 2.

### recommended_first_attack
Use the C_3^2 x C_101 decomposition and the 19-multiplier orbit structure to look for a contradiction in quotient occupancies or character sums.

### paper_if_solved
If solved exactly, the paper would be a short residual-row note on the Table 2 case (909,228,57) in C_3 x C_303.
