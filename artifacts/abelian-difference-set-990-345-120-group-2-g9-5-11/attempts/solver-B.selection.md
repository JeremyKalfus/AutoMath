# Does an abelian group of type [2,G9,5,11] admit a (990,345,120)-difference set?

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-990-345-120-group-2-g9-5-11`
- worker_role: `solver-B`
- canonical_source: `Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the Lander-conjecture slide listing the exact open row 990 345 120 225 [2,G9,5,11] with p = 3,5.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A solution of the [2,G9,5,11] row would support a short note removing one small exact residue from Gordon's Lander-conjecture frontier.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `79`
- single_solve_to_paper_fraction: `0.76`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
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
- working_packet_path: `artifacts/abelian-difference-set-990-345-120-group-2-g9-5-11/working_packet.md`
- paper_shape: `A one-theorem note settling one named small open Lander-conjecture row in a fixed abelian group type.`

## question
Does an abelian group of type [2,G9,5,11] admit a (990,345,120)-difference set?

## canonical_statement
Determine whether any abelian group with Gordon's Lander-conjecture row [2,G9,5,11] admits a (990,345,120)-difference set.

## intended_statement
Determine whether any abelian group with Gordon's Lander-conjecture row [2,G9,5,11] admits a (990,345,120)-difference set.

## pre_solve_gate_reason
The attempt registry has no exact or near-duplicate match for the [2,G9,5,11] row. In the bounded 2026-04-15 audit, the exact tuple search produced no later direct settlement, the alternate-notation search pointed back to Gordon's 2019 slide, and Gordon's current repository and publications pages did not expose a newer paper closing this exact group-type case. The theorem slice remains stable because n = 225 = 3^2 * 5^2 lies outside the published prime-power range on the cited slide.

## micro_paper_assessment
Lane-eligible. The source anchor is explicit, the theorem slice is exact, and a clean proof would already determine the paper's title and core contribution. The remaining risk is only the usual bounded freshness caveat, not a structural packaging problem.

## hypothetical_title
On the (990,345,120) Difference-Set Problem for Abelian Groups of Type [2,G9,5,11]

## hypothetical_abstract
We determine whether any abelian group of type [2,G9,5,11] admits a (990,345,120)-difference set. Gordon's 2019 survey slide lists this exact row among the smallest open Lander-conjecture cases, giving a canonical source-anchored frontier statement. Resolving the row would therefore yield a compact note centered on one exact theorem rather than a broad programmatic advance.

## single_solve_paper_explanation
The row is already branded by a canonical source and does not need feeder instances to become paper-shaped. If one exact proof works, the result itself is the note's title theorem. What remains is only a light setup section and the presentation of the final obstruction or construction.

## broader_theorem_nonimplication_note
The published theorem cited on Gordon's Lander slide covers only the case where n is a power of a prime greater than 3. Here n = 225, so the exact group-type row is not swallowed by that theorem and is still listed as open in 2019.

## literature_gap
Gordon's 2019 Lander-conjecture slide still lists 990 345 120 225 [2,G9,5,11] as open.

## publication_packet_title
The (990,345,120) Difference-Set Case in Groups of Type [2,G9,5,11]

## publication_packet_frontier_basis
Gordon's 2019 Lander-conjecture slide still names 990 345 120 225 [2,G9,5,11] as a small exact open row.

## publication_packet_near_paper_reason
An exact settlement already furnishes the theorem statement, the novelty claim, and the main narrative frame. The remaining paper would mostly be a compact literature paragraph around Gordon's slide and the decisive certificate.

## publication_packet_literature_scope
Gordon's 2019 slide deck for the exact row, plus the bounded 2026-04-15 freshness check against the current difference-set repository and Gordon's publications page.

## publication_packet_artifact_requirements
Either an explicit difference set in an abelian group of type [2,G9,5,11], or a compact obstruction uniform in that exact type.

## paper_shape
A one-theorem note settling one named small open Lander-conjecture row in a fixed abelian group type.

## transfer_kit

### usable_lemmas
- A difference set must satisfy the group-ring identity D D^(-1) = n + lambda G, which lets quotient coefficient counts act as exact constraints.
- Every nontrivial character chi must satisfy |chi(D)|^2 = n, giving a rigid target for character-divisibility arguments.
- Some translate of D is fixed by all multipliers, so any available multiplier information reduces the search to orbit unions.
- Gordon's 2019 slide lists 990 345 120 225 [2,G9,5,11] as an exact open Lander-conjecture row.

### toy_example
The same slide deck's 243 example, where [3,3,3,9] is negative but [3,9,9] is open, shows that exact abelian group type can already support a paper-level theorem statement.

### known_obstruction
This row survives as a small Lander-conjecture residue because the noncyclic Sylow-3 and Sylow-5 structure is not disposed of by the published prime-power theorem.

### prior_work_stop_sentence
Gordon's 2019 Lander-conjecture slide stops at listing 990 345 120 225 [2,G9,5,11] as an open exact row.

### recommended_first_attack
Exploit simultaneous 3-local and 5-local orbit constraints after passing to a multiplier-normalized translate, aiming to force an impossible fiber profile in the [2,G9,5,11] decomposition.

### paper_if_solved
If solved exactly, the paper would be a short note settling one exact small open Lander-conjecture row.
