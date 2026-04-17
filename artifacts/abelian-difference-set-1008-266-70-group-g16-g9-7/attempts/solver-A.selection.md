# Does an abelian group of type [G16,G9,7] admit a (1008,266,70)-difference set?

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-1008-266-70-group-g16-g9-7`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the Lander-conjecture slide listing the exact open row 1008 266 70 196 [G16,G9,7] with p = 7.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A construction or nonexistence proof for the [G16,G9,7] row would support a short note resolving one named small open Lander-conjecture residue.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `82`
- single_solve_to_paper_fraction: `0.78`
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
- working_packet_path: `artifacts/abelian-difference-set-1008-266-70-group-g16-g9-7/working_packet.md`
- paper_shape: `A one-theorem note settling one named small open Lander-conjecture row in a fixed abelian group type.`

## question
Does an abelian group of type [G16,G9,7] admit a (1008,266,70)-difference set?

## canonical_statement
Determine whether any abelian group with Gordon's Table-2 type [G16,G9,7] admits a (1008,266,70)-difference set.

## intended_statement
Determine whether any abelian group with Gordon's Table-2 type [G16,G9,7] admits a (1008,266,70)-difference set.

## pre_solve_gate_reason
The authoritative local attempt registry is clear on this exact row, and the bounded 2026-04-15 audit kept the frontier narrow: the exact tuple search returned no later direct settlement, the alternate-notation search surfaced Gordon's 2019 slide, and the current repository and publications pages did not expose a newer source closing the [G16,G9,7] case. The theorem slice stays tied to the exact group type because the cited Leung-Ma-Schmidt theorem only covers n a prime power greater than 3, while here n = 196.

## micro_paper_assessment
Lane-eligible. The row is source-anchored, exact, and small enough that one clean proof would already read like the theorem statement of a short note. The likely proof routes stay attached to the [G16,G9,7] quotient structure instead of obviously collapsing into a broader published theorem.

## hypothetical_title
On the (1008,266,70) Difference-Set Problem for Abelian Groups of Type [G16,G9,7]

## hypothetical_abstract
We determine whether any abelian group of type [G16,G9,7] admits a (1008,266,70)-difference set. Gordon's 2019 survey slide isolates this exact row as one of the smallest remaining open cases attached to Lander's conjecture, so the published frontier for the problem is already crisp. An exact obstruction or construction would therefore give the title theorem of a short stand-alone note rather than a feeder result in a broader campaign.

## single_solve_paper_explanation
This target is already paper-shaped before any new proof work because the exact group type and parameter triple are named on a canonical open-problem slide. Solving it would contribute the title theorem, the core proof, and the main novelty claim in one move. The only material left would be a short frontier recap, certificate presentation, and routine verification packaging.

## broader_theorem_nonimplication_note
The Leung-Ma-Schmidt theorem cited on the same Lander-conjecture slide proves the conjecture only when n is a power of a prime greater than 3. Here n = 196 = 2^2 * 7^2, so the published theorem does not dispose of the [G16,G9,7] row and Gordon still lists it as open in 2019.

## literature_gap
Gordon's 2019 Lander-conjecture slide still lists the exact row 1008 266 70 196 [G16,G9,7] as open.

## publication_packet_title
The (1008,266,70) Difference-Set Case in Groups of Type [G16,G9,7]

## publication_packet_frontier_basis
Gordon's 2019 Lander-conjecture slide still lists 1008 266 70 196 [G16,G9,7] among the small exact open rows.

## publication_packet_near_paper_reason
If this row is settled, almost all of the paper is already determined: cite the exact frontier line from Gordon's slide, recall the standard orbit and character setup, and present the decisive obstruction or construction. Little remains beyond certificate checking and tight exposition.

## publication_packet_literature_scope
Gordon's 2019 slide deck for the exact row, together with the standard group-ring and character criteria cited in that talk and a bounded freshness check against Gordon's current repository and publications pages.

## publication_packet_artifact_requirements
Either an explicit difference set in an abelian group of type [G16,G9,7], or a compact nonexistence proof uniform in that group type.

## paper_shape
A one-theorem note settling one named small open Lander-conjecture row in a fixed abelian group type.

## transfer_kit

### usable_lemmas
- A difference set D in G satisfies the group-ring identity D D^(-1) = n + lambda G, so exact coefficient counts in quotients are admissible obstruction data.
- For every nontrivial character chi of G, a difference set must satisfy |chi(D)|^2 = n, giving a fixed character-sum target for obstruction arguments.
- Some translate of D is fixed by all multipliers, so any usable multiplier information converts the problem into an orbit-union problem.
- Gordon's 2019 slide names 1008 266 70 196 [G16,G9,7] as an exact open Lander-conjecture residue.

### toy_example
The same 2019 slide deck highlights the nearby group-sensitive contrast at v = 243, where [3,3,3,9] is settled negative while [3,9,9] stays open, illustrating how a fixed group type can support a genuine title theorem.

### known_obstruction
Any proof has to respect the noncyclic Sylow-7 issue that makes this a Lander-conjecture row in the first place, so a successful argument must use the [G16,G9,7] local structure rather than generic parameter counting alone.

### prior_work_stop_sentence
Gordon's 2019 Lander-conjecture slide stops at listing 1008 266 70 196 [G16,G9,7] as an open exact row.

### recommended_first_attack
Translate to a multiplier-normalized representative if possible, then push quotient-profile constraints through the 7-part and the 2-part of [G16,G9,7] until only a tiny orbit system remains.

### paper_if_solved
If solved exactly, the paper would be a short note settling one named small open Lander-conjecture case in a fixed abelian group type.
