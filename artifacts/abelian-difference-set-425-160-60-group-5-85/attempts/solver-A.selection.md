# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-425-160-60-group-5-85`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (425,160,60) in group [5,85].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle the exact Table 2 row (425,160,60) in the group C_5 x C_85.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `82`
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
- working_packet_path: `artifacts/abelian-difference-set-425-160-60-group-5-85/working_packet.md`
- paper_shape: `A short exact-group residual-row note from the multiplier-conjecture survey.`

## question
Does the abelian group C_5 x C_85 admit a (425,160,60)-difference set?

## canonical_statement
Determine whether the abelian group C_5 x C_85 admits a (425,160,60)-difference set.

## intended_statement
Determine whether the abelian group C_5 x C_85 admits a (425,160,60)-difference set.

## pre_solve_gate_reason
The source isolates one exact group row, local attempt memory shows no conflict, and exact plus alternate-notation web searches surfaced no later settled statement for this row.

## micro_paper_assessment
Lane-eligible: exact title theorem, stable slice, low packaging burden, and acceptable novelty risk after bounded local and web audit.

## hypothetical_title
On the (425,160,60) Difference-Set Problem in C_5 x C_85

## hypothetical_abstract
We determine whether the abelian group C_5 x C_85 admits a (425,160,60)-difference set. Gordon and Schmidt isolate this exact group row in Table 2 of their multiplier-conjecture survey among the smallest unresolved non-Paley cases. A decisive proof would likely constitute the main theorem of a short note, and bounded exact plus alternate-notation searches in this run surfaced no later paper settling the row.

## single_solve_paper_explanation
The source already supplies the title theorem, the family anchor, and the literature gap. An exact proof or disproof would therefore contribute most of the mathematics of the eventual paper. What remains after the solve is mainly a short introduction, a comparison with the published multiplier filters, and clean exposition of the decisive argument.

## broader_theorem_nonimplication_note
Within the canonical survey, the [5,85] row survives the paper's earlier general multiplier theorems and is listed separately in Table 2, while the bounded exact and alternate-notation searches in this run surfaced no later source closing this exact group case.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 marking (425,160,60) in group [5,85] as open; bounded exact and alternate-notation searches on 2026-04-15 did not surface a later settled paper for this row.

## publication_packet_title
On the (425,160,60) Difference-Set Problem in C_5 x C_85

## publication_packet_frontier_basis
Gordon-Schmidt 2016 Table 2 lists the exact [5,85] row as open, local attempt memory has no matching canonical problem key, and bounded exact plus alternate-notation web searches on 2026-04-15 surfaced no later paper settling this row.

## publication_packet_near_paper_reason
One clean proof or disproof would already provide the title theorem, with only residual-list framing and brief comparison to the published multiplier filters left to write.

## publication_packet_literature_scope
Gordon-Schmidt 2016 Table 2; Dan Gordon's live difference-set database page; bounded exact and alternate-notation web searches on 2026-04-15; local attempt-registry memory.

## publication_packet_artifact_requirements
A proof or disproof in C_5 x C_85, together with the decisive orbit or quotient contradiction or explicit construction data and a short explanation of why the row survives the published multiplier filters.

## paper_shape
A short exact-group residual-row note from the multiplier-conjecture survey.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt 2016 isolate the exact [5,85] row in Table 2, fixing the theorem slice in one group.
- For (425,160,60), the order n = 100 = 2^2 * 5^2, so 2 is the first multiplier-conjecture prime and dyadic orbit structure is the natural first pressure point.
- The decomposition C_5 x C_85 = C_5^2 x C_17 gives immediate quotient maps to C_17 and to the 5-primary part, so orbit sizes can be checked against k = 160.

### toy_example
Project to the C_17 quotient and test whether a 2-multiplier-fixed orbit partition can realize total size 160 while preserving lambda = 60.

### known_obstruction
The standard multiplier machinery in the survey does not already eliminate the row, so any proof must sharpen quotient or orbit bookkeeping beyond the published filters.

### prior_work_stop_sentence
Gordon-Schmidt 2016 list (425,160,60) in group [5,85] as open in Table 2.

### recommended_first_attack
Exploit the C_5^2 x C_17 decomposition under the putative 2-multiplier action and look for a contradiction in the allowed orbit sizes or quotient image counts.

### paper_if_solved
If solved exactly, the paper would be a short residual-row note on the Table 2 case (425,160,60) in C_5 x C_85.
