# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-1840051-2350-3`
- worker_role: `solver-B`
- canonical_source: `Daniel M. Gordon, "On difference sets with small lambda," Journal of Algebraic Combinatorics 55 (2022), especially Theorem 2, Theorems 3 and 4, and Table 4 on page 6, which lists the six remaining open abelian (v,k,3)-difference-set parameter sets after the source's eliminations.`
- open_status_checked_on: `2026-04-14`
- publication_status: `NONE`
- publication_if_solved: `A construction or nonexistence proof for an abelian (1840051,2350,3)-difference set would plausibly support a short note resolving another residual lambda = 3 case from Gordon's Table 4.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short-medium`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `68`
- single_solve_to_paper_fraction: `0.7`
- title_theorem_strength: `moderate`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/abelian-difference-set-1840051-2350-3/working_packet.md`
- paper_shape: `A one-theorem note resolving one residual abelian lambda = 3 difference-set parameter from Table 4.`

## question
Does there exist an abelian (1840051,2350,3)-difference set?

## canonical_statement
Determine whether there exists an abelian (1840051,2350,3)-difference set.

## intended_statement
Determine whether any abelian group of order 1840051 admits a (1840051,2350,3)-difference set.

## pre_solve_gate_reason
Thin repo memory shows no prior mathematical attempt for this exact tuple. The canonical-source audit confirms that Table 4 lists (1840051,2350,3) among the six remaining open lambda = 3 abelian difference-set cases after the source's eliminations. Bounded 2026-04-14 web checks on the exact tuple and family wording produced no later settlement hit beyond the canonical paper and generic reference pages.

## micro_paper_assessment
Borderline but still lane-eligible. The family anchor is clean and the post-solve packaging is light, though the larger parameter size modestly weakens closability compared with the top queue slot.

## hypothetical_title
On Abelian (1840051,2350,3)-Difference Sets

## hypothetical_abstract
We determine the existence status of abelian difference sets with parameters (1840051,2350,3). Gordon's 2022 analysis leaves this tuple in the final six-case lambda = 3 residual list after applying multiplier-orbit and quotient-multiplier obstructions together with the Lander and Mann tests. An exact resolution therefore yields a focused note rather than a broad campaign.

## single_solve_paper_explanation
The source already does the heavy framing work by collapsing the lambda = 3 search space to six residual tuples. If this exact tuple is resolved, the note mainly consists of recalling that frontier and presenting the decisive argument. That is enough to keep the solve close to paper-complete.

## broader_theorem_nonimplication_note
The source explicitly retains this tuple in Table 4 after its elimination theorems and standard tests have been applied. So the honest theorem slice remains the exact tuple, not a corollary of the published reductions.

## literature_gap
Gordon's Table 4 leaves (1840051,2350,3) unresolved as one of the six remaining abelian lambda = 3 parameter sets.

## publication_packet_title
An Abelian (1840051,2350,3)-Difference Set

## publication_packet_frontier_basis
Table 4 isolates (1840051,2350,3) inside a six-case lambda = 3 residual list surviving the source's elimination machinery.

## publication_packet_near_paper_reason
If this tuple is settled, the surrounding paper frame is already present in the source: explain why it survives Theorems 2-4 and the auxiliary tests, then present the final construction or obstruction. The remaining writeup is bounded and mostly expository.

## publication_packet_literature_scope
Gordon (2022), with the Lander and Mann background already referenced there.

## publication_packet_artifact_requirements
Either an explicit abelian group of order 1840051 carrying a (1840051,2350,3)-difference set, or a compact group-uniform nonexistence proof.

## paper_shape
A one-theorem note resolving one residual abelian lambda = 3 difference-set parameter from Table 4.

## transfer_kit

### usable_lemmas
- Theorem 2 gives the main multiplier-orbit contradiction template.
- Theorem 3 bounds cyclic multiplier groups by |M| <= k.
- Theorem 4 bounds contracted multiplier groups in cyclic quotients.
- Table 4 identifies (1840051,2350,3) as one of the source's remaining six lambda = 3 cases.

### toy_example
The source's short obstruction for (352,27,2) is the model example for the multiplier-orbit style of nonexistence proof that could still collapse this tuple.

### known_obstruction
Standard multiplier, quotient, Lander, and Mann eliminations already fail here, so any solution needs a sharper structural input than the source currently uses.

### prior_work_stop_sentence
After applying Theorems 2, 3, 4, the Lander tests, and the Mann test, Gordon's Table 4 still lists (1840051,2350,3) among the six remaining open abelian lambda = 3 cases.

### recommended_first_attack
Exploit the prime n = 2347 and the factorization of v to search for a single strong multiplier-orbit decomposition that forces impossible orbit counts in every abelian group type of order 1840051.

### paper_if_solved
If solved exactly, the paper would be a short note removing another residual lambda = 3 case from Gordon's finite frontier.
