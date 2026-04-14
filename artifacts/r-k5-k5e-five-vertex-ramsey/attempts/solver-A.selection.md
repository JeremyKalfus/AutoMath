# Determine the exact value of R(K5, K5-e)

- entry_type: `paper_candidate`
- slug: `r-k5-k5e-five-vertex-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.11, especially the summary at page 40 stating 30 <= R(K5, K5-e) <= 33; together with bounded 2026-04-14 web checks against the survey page and historical five-vertex-graph summaries that did not reveal a later exact closure.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(K5, K5-e) would already read like the title theorem of a short note on one of the last unresolved five-vertex graph Ramsey pairs.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `83`
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
- exact_gap_from_source: `small`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-k5-k5e-five-vertex-ramsey/working_packet.md`
- paper_shape: `A one-theorem note closing one of the last unresolved five-vertex graph Ramsey pairs.`

## question
Is R(K5, K5-e) equal to 30, 31, 32, or 33?

## canonical_statement
Determine the exact value of R(K5, K5-e).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a red K5 or a blue K5-e.

## pre_solve_gate_reason
The thin-memory sweep found no prior mathematical status or near-duplicate slug for this exact pair in memory/search_memory.json, memory/paper_memory.json, failed_problems.json, queue.json, selected_problem.md, PROOFS.md, or artifact directory names. DS1.17 still records only the narrow interval 30 <= R(K5, K5-e) <= 33, and the bounded 2026-04-14 web sweep surfaced historical discussion of this pair as still open but no later exact determination.

## micro_paper_assessment
Pass. This is a stable, still-open exact theorem slice with a strong family anchor and low editorial overhead.

## hypothetical_title
The Exact Value of R(K5, K5-e)

## hypothetical_abstract
We determine the two-color Ramsey number R(K5, K5-e). The current survey literature leaves this parameter in the interval 30 <= R(K5, K5-e) <= 33 and identifies it as one of the remaining unresolved five-vertex graph cases. Our result closes that gap and completes another exact entry in the five-vertex Ramsey table.

## single_solve_paper_explanation
One exact solve would already be the honest main theorem of the note. The family anchor is strong because this is not an isolated curiosity but one of the small residual five-vertex cases tracked by the survey literature. After the solve, very little remains beyond the proof or witness and a short contextual discussion.

## broader_theorem_nonimplication_note
General Ramsey recurrences and monotonicity only recover the interval and do not force a specific value. The survey still records a true multi-value gap rather than a case implicitly settled by a broader theorem.

## literature_gap
Current public sources stop at 30 <= R(K5, K5-e) <= 33.

## publication_packet_title
The Exact Value of R(K5, K5-e)

## publication_packet_frontier_basis
Current public survey data still leaves the pair in the interval 30 <= R(K5, K5-e) <= 33. It is explicitly highlighted as one of the remaining unsolved five-vertex graph cases, so an exact closure has an immediate paper frame.

## publication_packet_near_paper_reason
If the exact value is found, the decisive argument or extremal coloring is already the paper. What remains is a short literature paragraph, a compact verification artifact, and a comparison with the already solved neighboring five-vertex pairs.

## publication_packet_literature_scope
DS1.17 Section 5.11 plus bounded 2026-04-14 survey-page and five-vertex-summary web checks.

## publication_packet_artifact_requirements
Either a forcing proof at the correct threshold or one explicit extremal coloring on n-1 vertices together with a small verification certificate.

## paper_shape
A one-theorem note closing one of the last unresolved five-vertex graph Ramsey pairs.

## transfer_kit

### usable_lemmas
- DS1.17 records the current lower bound 30 <= R(K5, K5-e).
- DS1.17 records the current upper bound R(K5, K5-e) <= 33.
- The same survey isolates K5 versus K5-e as one of the remaining open five-vertex graph Ramsey pairs, so the surrounding family narrative is already in place.

### toy_example
The solved neighboring five-vertex case R(K5, W5) = 27 shows how a single exact closure in this table naturally supports a short standalone note.

### known_obstruction
Any proof of the upper endpoint must rule out all colorings at one threshold, while any lower-bound improvement needs an explicit extremal coloring suppressing a red K5 and a blue K5-e simultaneously.

### prior_work_stop_sentence
Current sources stop at 30 <= R(K5, K5-e) <= 33.

### recommended_first_attack
Start from the known lower-bound constructions cited by the survey and perform a tightly controlled extension analysis before allowing any broader computational campaign.

### paper_if_solved
The paper would be a concise exact-value note on one of the last unresolved five-vertex Ramsey pairs.
