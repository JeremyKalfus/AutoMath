# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-495-247-123-group-3-165`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (495,247,123) in group [3,165].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `Settling the exact [3,165] row would plausibly yield a short note closing a named open Table 2 case from the multiplier-conjecture survey.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `82`
- single_solve_to_paper_fraction: `0.8`
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
- working_packet_path: `artifacts/abelian-difference-set-495-247-123-group-3-165/working_packet.md`
- paper_shape: `An exact survey-table closure note for the abelian [3,165] case.`

## question
Does the abelian group of type [3,165] admit a (495,247,123)-difference set?

## canonical_statement
Determine whether the abelian group of type [3,165] admits a (495,247,123)-difference set.

## intended_statement
Determine whether the abelian group of type [3,165] admits a (495,247,123)-difference set.

## pre_solve_gate_reason
The exact group-specific row is source-anchored in Table 2, has no attempted-problem conflict in local memory, and the bounded tuple-plus-group audit surfaced no later exact settlement.

## micro_paper_assessment
Lane-eligible. The theorem slice is stable, the source anchor is explicit, and one decisive solve would already look like the title theorem of a short note.

## hypothetical_title
On the abelian [3,165] (495,247,123) difference-set case

## hypothetical_abstract
We determine whether the abelian group of type [3,165] admits a (495,247,123)-difference set. Gordon and Schmidt isolate this exact group-specific row in Table 2 of their multiplier-conjecture survey after the standard eliminations. A direct solution would close a named residual case with only light packaging beyond the proof itself.

## single_solve_paper_explanation
The survey already supplies the family anchor, the exact statement, and the frontier basis. Once the [3,165] case is settled, the remaining paper work is mostly a concise introduction, a clean proof presentation, and a short comparison with the neighboring Table 2 rows. No feeder ladder or second theorem program is needed.

## broader_theorem_nonimplication_note
The source isolates the exact group [3,165], not merely the parameter triple, and the bounded audit surfaced no broader published theorem settling this precise group-specific row.

## literature_gap
Gordon-Schmidt Table 2 stops at listing the exact open row (495,247,123) in group [3,165]; the bounded 2026-04-15 audit found no later exact-resolution hit for that statement.

## publication_packet_title
The Abelian [3,165] (495,247,123) Difference-Set Case

## publication_packet_frontier_basis
The multiplier-conjecture survey still isolates (495,247,123) in the exact group [3,165] as an open Table 2 row, and the bounded 2026-04-15 audit found no later exact-row resolution.

## publication_packet_near_paper_reason
If solved, the main theorem is already the note: one exact survey-table closure with a short multiplier-orbit argument and brief source-to-proof bridge.

## publication_packet_literature_scope
Survey Table 2, bounded exact-tuple and group-notation web checks on 2026-04-15, and attempted-problem conflict checks against local memory surfaces.

## publication_packet_artifact_requirements
A proof or disproof in the exact group [3,165], a clean multiplier-orbit or character contradiction, and a short writeup tying the argument back to the survey row.

## paper_shape
An exact survey-table closure note for the abelian [3,165] case.

## transfer_kit

### usable_lemmas
- Survey Table 2 isolates the exact open row (495,247,123) in group [3,165] after the survey's eliminations.
- The survey's multiplier-conjecture framework turns any candidate difference set into unions of multiplier orbits inside the stated group type.
- Character-theoretic divisibility constraints from the survey sharply restrict quotient images and intersection numbers for admissible sets.
- The exact group decomposition [3,165] gives a small subgroup lattice for contraction and orbit bookkeeping.

### toy_example
Project a hypothetical set in the group [3,165] onto its 3-part or 5-part quotient and test whether a 247-element split can coexist with the induced multiplier orbits.

### known_obstruction
The same multiplier machinery that leaves this row open already kills many neighboring cases, so any surviving configuration must satisfy a very narrow orbit profile.

### prior_work_stop_sentence
Gordon and Schmidt stop at listing (495,247,123) in the exact group [3,165] as an open Table 2 row.

### recommended_first_attack
Exploit the 5- and 11-parts of 165 to force multiplier orbits, then intersect those orbit counts with the required 247-point total in the exact group [3,165].

### paper_if_solved
If solved, the paper would be a short exact-case note closing the survey's [3,165] row.
