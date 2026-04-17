# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-243-121-60-group-3-9-9`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the slide listing the smallest open exact group-specific case (243,121,60) in [3,9,9], together with the same talk's group-ring and character criteria slides.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A construction or nonexistence proof would settle the smallest open abelian difference-set case in which exponent-based heuristics still leave one exact group unresolved.`
- publication_if_solved_score: `solve_is_basically_the_paper`
- solve_to_publication_distance: `tiny`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `86`
- single_solve_to_paper_fraction: `0.84`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `moderate`
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
- working_packet_path: `artifacts/abelian-difference-set-243-121-60-group-3-9-9/working_packet.md`
- paper_shape: `A one-theorem note settling the smallest open group-specific abelian difference-set case at parameters (243,121,60).`

## question
Does the abelian group C3 x C9 x C9 admit a (243,121,60)-difference set?

## canonical_statement
Determine whether there exists a (243,121,60)-difference set in the abelian group C3 x C9 x C9.

## intended_statement
Determine whether the abelian group of type [3,9,9] admits a (243,121,60)-difference set.

## pre_solve_gate_reason
Thin local memory shows no prior AutoMath attempt for the exact [3,9,9] group case. The source-anchored audit identifies it as the smallest open instance in Gordon's 2019 talk, and no local duplicate tuple, title, or source-anchor conflict appears in the attempt registry.

## micro_paper_assessment
This is a strong micro-paper candidate: one exact solve settles a named smallest-open case with a direct structural narrative and no feeder ladder.

## hypothetical_title
On (243,121,60)-Difference Sets in C3 x C9 x C9

## hypothetical_abstract
We determine whether the abelian group C3 x C9 x C9 admits a (243,121,60)-difference set. Gordon's La Jolla Difference Set Repository survey identifies this as the smallest open case in the question of whether difference-set existence depends only on the exponent of the ambient abelian group. The result therefore closes a source-explicit frontier slice with little remaining packaging beyond the decisive argument and the comparison to the already-settled sibling groups.

## single_solve_paper_explanation
This target is already paper-shaped because the literature singles it out as the smallest open exact case in a natural structural question, not as a stray tuple. A solve would immediately furnish the title theorem and the main novelty claim. What remains after the solve is only the short comparison table, notation, and a concise proof or witness presentation.

## broader_theorem_nonimplication_note
The known nearby examples only show that exponent does not determine existence in some larger cases and that the sibling group [3,3,3,9] is impossible; they do not decide the exact [3,9,9] group.

## literature_gap
Prior work stops at the statement that (243,121,60) is open for the group [3,9,9] even though the sibling group [3,3,3,9] is already ruled out and other comparison examples at order 324 are known.

## publication_packet_title
The Smallest Open Exponent-Sensitive Abelian Difference-Set Case

## publication_packet_frontier_basis
Gordon's 2019 survey isolates (243,121,60) in the group [3,9,9] as the smallest remaining exact case in the question of whether difference-set existence depends only on the exponent of the ambient abelian group.

## publication_packet_near_paper_reason
The surrounding narrative is already written by the source: the nearby yes/no comparison cases are known, the unresolved slice is explicitly named, and the final note only needs the exact construction or obstruction for this one group.

## publication_packet_literature_scope
Gordon's 2019 LJDSR talk, together with the cited Lopez-Sanchez nonexistence result for [3,3,3,9] and the Davis-Jedwab and Jedwab comparison examples at order 324.

## publication_packet_artifact_requirements
Either an explicit subset of C3 x C9 x C9 certifying a (243,121,60)-difference set, or a compact group-specific nonexistence proof using quotient, character, or multiplier structure.

## paper_shape
A one-theorem note settling the smallest open group-specific abelian difference-set case at parameters (243,121,60).

## transfer_kit

### usable_lemmas
- The group-ring criterion from Gordon's 2019 talk: D is a difference set exactly when D D^{-1} = n + lambda G.
- The character criterion from the same talk: for every nontrivial character chi, one must have |chi(D)|^2 = n, while the trivial character gives k^2.
- The comparison point recorded on the same slide: the sibling group [3,3,3,9] does not admit a (243,121,60)-difference set.
- The order-324 comparison examples in Gordon's talk show that existence can vary across abelian groups with nearby structural data, so a group-specific proof is mathematically meaningful rather than purely incidental.

### toy_example
Use the order-324 yes/no comparison pair from Gordon's slide 37 as the worked model for how group structure can change existence at fixed parameters.

### known_obstruction
The nearest sibling group [3,3,3,9] is already impossible, so any existence proof for [3,9,9] must exploit genuinely group-specific structure rather than parameter counts alone.

### prior_work_stop_sentence
The source literature still lists the group [3,9,9] as the smallest open exact case for parameters (243,121,60).

### recommended_first_attack
Exploit the subgroup chain C3 < C9 in the two large coordinates, pass to quotient profiles, and test whether the character values forced by a putative difference set can coexist with the known obstruction pattern from the sibling group.

### paper_if_solved
If solved exactly, the paper would be a one-theorem note resolving the smallest open group-specific exponent-sensitivity case for abelian difference sets.
