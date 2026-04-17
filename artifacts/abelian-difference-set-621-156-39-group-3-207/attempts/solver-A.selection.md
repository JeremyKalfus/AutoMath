# Does the abelian group C_3 x C_207 admit a (621,156,39)-difference set?

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-621-156-39-group-3-207`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (621,156,39) in group [3,207].`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `A proof of existence or nonexistence would settle the exact Table 2 row (621,156,39) in C_3 x C_207 and would already read like the title theorem of a short residual-row note.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `79`
- single_solve_to_paper_fraction: `0.77`
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
- working_packet_path: `artifacts/abelian-difference-set-621-156-39-group-3-207/working_packet.md`
- paper_shape: `A short exact-group residual-row note from the multiplier-conjecture survey.`

## question
Does the abelian group C_3 x C_207 admit a (621,156,39)-difference set?

## canonical_statement
Determine whether the abelian group C_3 x C_207 admits a (621,156,39)-difference set.

## intended_statement
Determine whether the abelian group C_3 x C_207 admits a (621,156,39)-difference set.

## pre_solve_gate_reason
Gordon-Schmidt Table 2 isolates the exact row [3,207], the local attempt registry shows no prior run on this canonical problem key, exact-tuple and alternate-notation web checks on 2026-04-15 surfaced no later settlement, and Gordon's current publications and repository pages surfaced no post-2016 resolution. The theorem slice is stable and one clean solve would already do most of the paper-shaped work.

## micro_paper_assessment
Lane-eligible. This is a stable exact theorem slice with a clear family anchor, low editorial overhead, and a solve-to-publication distance short enough for the strict micro-paper lane.

## hypothetical_title
On the nonexistence of a (621,156,39) difference set in C_3 x C_207

## hypothetical_abstract
We determine whether the abelian group C_3 x C_207 admits a (621,156,39)-difference set. Gordon and Schmidt isolate this exact row in Table 2 of their multiplier-conjecture survey. A decisive proof would remove a named residual case with only light post-solve framing left.

## single_solve_paper_explanation
The exact row is already isolated in the source literature, so the theorem statement does not need to be invented after the solve. One clean existence or nonexistence argument would therefore carry most of the mathematics and most of the paper narrative. What would remain is a short introduction, the proof writeup, and a brief comparison with the survey filters.

## broader_theorem_nonimplication_note
The bounded audit surfaced no broader published theorem that already removes the exact [3,207] group row; Gordon-Schmidt still lists it separately in Table 2, and the later web surface did not expose a newer discharge.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing the exact row (621,156,39) in group [3,207] as open; the bounded 2026-04-15 exact-tuple and alternate-notation sweep surfaced no later direct settlement.

## publication_packet_title
On the (621,156,39) Difference-Set Problem in C_3 x C_207

## publication_packet_frontier_basis
Gordon-Schmidt 2016 Table 2 still isolates the exact [3,207] row as open after the survey's multiplier-based eliminations.

## publication_packet_near_paper_reason
The source already supplies the exact title theorem, the literature stop line, and the family anchor. After a solve, what remains is mostly concise exposition of the decisive orbit or quotient contradiction and brief placement against Table 2.

## publication_packet_literature_scope
Gordon-Schmidt 2016 Table 2, Gordon's current publications page, Gordon's current La Jolla repository page, the local attempt registry, and bounded exact-tuple plus alternate-notation searches on 2026-04-15.

## publication_packet_artifact_requirements
A proof or disproof in C_3 x C_207, the decisive quotient-orbit argument, and a short explanation of why the row survives the published Table 2 filters.

## paper_shape
A short exact-group residual-row note from the multiplier-conjecture survey.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt 2016 isolate the exact group row [3,207] in Table 2, so the intended theorem is already source-anchored.
- For (621,156,39), the order is n = 117 = 3^2 * 13, and Table 2 records 13 as the natural multiplier-conjecture prime for the row.
- The decomposition C_3 x C_207 = C_3^3 x C_23 gives immediate 3-part and 23-part quotient tests for multiplier-fixed orbit counts.

### toy_example
Project to the C_23 quotient and test whether a 13-multiplier-fixed orbit partition can sum to 156 while respecting the lambda = 39 difference counts.

### known_obstruction
The row already survives the survey's standard multiplier machinery, so any proof must sharpen the quotient or orbit bookkeeping beyond Table 2.

### prior_work_stop_sentence
Gordon-Schmidt 2016 list (621,156,39) in group [3,207] as open in Table 2.

### recommended_first_attack
Exploit the C_3^3 x C_23 decomposition and test whether the recorded 13-multiplier information forces an orbit partition incompatible with total size 156 and lambda = 39.

### paper_if_solved
If solved exactly, the paper would be a short residual-row note on the Table 2 case (621,156,39) in C_3 x C_207.
