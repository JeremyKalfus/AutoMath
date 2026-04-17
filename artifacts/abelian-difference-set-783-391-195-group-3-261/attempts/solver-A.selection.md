# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-783-391-195-group-3-261`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), especially Table 1 listing the known (783,391,195) row in group [3,3,87] and Table 2 listing the open row in group [3,261].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle whether the exact abelian group C_3 x C_261 admits a (783,391,195)-difference set, despite the same parameters being realized in group type [3,3,87].`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `low`
- paper_leverage_score: `83`
- single_solve_to_paper_fraction: `0.82`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
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
- working_packet_path: `artifacts/abelian-difference-set-783-391-195-group-3-261/working_packet.md`
- paper_shape: `A short exact-group note separating the open [3,261] case from the known [3,3,87] case at the same parameters.`

## question
Does the abelian group C_3 x C_261 admit a (783,391,195)-difference set?

## canonical_statement
Determine whether the abelian group C_3 x C_261 admits a (783,391,195)-difference set.

## intended_statement
Determine whether the abelian group C_3 x C_261 admits a (783,391,195)-difference set.

## pre_solve_gate_reason
The source already isolates a sharp exact residue: Table 1 records the same parameters in group [3,3,87], while Table 2 leaves [3,261] open. The bounded exact-notation, alternate-notation, canonical-source, later-source, and current-database checks on 2026-04-15 surfaced no direct post-2015 settlement of the exact [3,261] row and no local attempt-registry conflict.

## micro_paper_assessment
Lane-eligible. The statement is exact, source-anchored, group-specific, and solving it would plausibly provide 80%+ of a short paper rather than a one-paragraph curiosity.

## hypothetical_title
On the (783,391,195) Difference-Set Problem in C_3 x C_261

## hypothetical_abstract
We determine whether the abelian group C_3 x C_261 admits a (783,391,195)-difference set. Gordon and Schmidt record the same parameters as known in group [3,3,87] but leave the exact group [3,261] open in Table 2 of their multiplier survey. A decisive construction or obstruction for C_3 x C_261 would therefore settle a clean residual group-type question and would already supply the main theorem of a short note.

## single_solve_paper_explanation
This target is already paper-shaped before solving: the source supplies the exact open statement, the nearby known row gives the natural comparison theorem, and the theorem slice is stable under the likely proof routes. After the solve, little remains beyond packaging the argument, stating why [3,261] differs from [3,3,87], and writing a short literature-positioning paragraph.

## broader_theorem_nonimplication_note
The same parameters already occur in another abelian type, so a generic parameter-level existence or nonexistence theorem would not automatically settle the [3,261] row. The bounded later-source check did not surface any broader post-2015 theorem deciding the exact group C_3 x C_261.

## literature_gap
Prior work surfaced here stops at Gordon-Schmidt 2015, which lists (783,391,195) as known in group [3,3,87] but still open in group [3,261]; the bounded 2026-04-15 outside-source check found no later direct settlement of the [3,261] case.

## publication_packet_title
On the (783,391,195) Difference-Set Problem in C_3 x C_261

## publication_packet_frontier_basis
Gordon-Schmidt 2015 explicitly separate the known [3,3,87] row from the open [3,261] row at the same parameters, so solving the [3,261] case would settle an exact residual group-type question rather than a vague family fragment.

## publication_packet_near_paper_reason
One exact solve already yields the note: state the split status at v = 783, give the obstruction or construction for C_3 x C_261, and explain why the known [3,3,87] realization does not transfer.

## publication_packet_literature_scope
Gordon-Schmidt 2015 Table 1 and Table 2, Gordon 2020 on small-lambda methods as a bounded later-source check, the current Dan Gordon difference-set index page, and local attempt-registry memory.

## publication_packet_artifact_requirements
A proof or disproof for C_3 x C_261, the orbit or quotient constraints used, and a short comparison with the known [3,3,87] realization.

## paper_shape
A short exact-group note separating the open [3,261] case from the known [3,3,87] case at the same parameters.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt Table 2 isolates the exact open row (783,391,195) in group [3,261], so the honest theorem can stay group-specific.
- Gordon-Schmidt Table 1 records the same parameters in group [3,3,87] with comment TPP(27), showing that the issue is the precise abelian type rather than mere parameter feasibility.
- The survey's multiplier framework reduces any proof to orbit decompositions under the unresolved multiplier candidates listed for the row.
- The decomposition C_3 x C_261 is naturally compatible with 9-part and 29-part quotients, giving immediate contracted-count tests.

### toy_example
Contract a hypothetical set to the 29-part quotient and compare the admissible orbit counts with the known [3,3,87] realization to see where the group-type obstruction first appears.

### known_obstruction
Because the same parameters are already realized in a different abelian type, any proof for [3,261] must exploit exact group structure and cannot stop at parameter-level tests.

### prior_work_stop_sentence
Gordon-Schmidt list (783,391,195) as known in [3,3,87] but open in [3,261].

### recommended_first_attack
Exploit the C_3 x C_9 x C_29 decomposition and test whether the survey's multiplier-orbit constraints are compatible with any lift from the 29-part quotient to C_3 x C_261.

### paper_if_solved
If solved exactly, the paper would be a short note resolving the remaining v = 783 group-type split between the known [3,3,87] case and the open [3,261] case.
