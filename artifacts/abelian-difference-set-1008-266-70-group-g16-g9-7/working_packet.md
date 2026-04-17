# Working Packet: The (1008,266,70) Difference-Set Case in Groups of Type [G16,G9,7]

- slug: `abelian-difference-set-1008-266-70-group-g16-g9-7`
- title: Does an abelian group of type [G16,G9,7] admit a (1008,266,70)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `82`
- single-solve-to-paper fraction: `0.78`

## statement
Determine whether any abelian group with Gordon's Table-2 type [G16,G9,7] admits a (1008,266,70)-difference set.

## novelty_notes
- frontier basis: Gordon's 2019 Lander-conjecture slide still lists 1008 266 70 196 [G16,G9,7] among the small exact open rows.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If this row is settled, almost all of the paper is already determined: cite the exact frontier line from Gordon's slide, recall the standard orbit and character setup, and present the decisive obstruction or construction. Little remains beyond certificate checking and tight exposition.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. The row is source-anchored, exact, and small enough that one clean proof would already read like the theorem statement of a short note. The likely proof routes stay attached to the [G16,G9,7] quotient structure instead of obviously collapsing into a broader published theorem.

## likely_paper_shape
- note title: The (1008,266,70) Difference-Set Case in Groups of Type [G16,G9,7]
- hypothetical title: On the (1008,266,70) Difference-Set Problem for Abelian Groups of Type [G16,G9,7]
- paper shape: A one-theorem note settling one named small open Lander-conjecture row in a fixed abelian group type.
- publication if solved: A construction or nonexistence proof for the [G16,G9,7] row would support a short note resolving one named small open Lander-conjecture residue.
- minimal artifact requirements: Either an explicit difference set in an abelian group of type [G16,G9,7], or a compact nonexistence proof uniform in that group type.

## hypothetical_abstract
We determine whether any abelian group of type [G16,G9,7] admits a (1008,266,70)-difference set. Gordon's 2019 survey slide isolates this exact row as one of the smallest remaining open cases attached to Lander's conjecture, so the published frontier for the problem is already crisp. An exact obstruction or construction would therefore give the title theorem of a short stand-alone note rather than a feeder result in a broader campaign.

## single_solve_explanation
This target is already paper-shaped before any new proof work because the exact group type and parameter triple are named on a canonical open-problem slide. Solving it would contribute the title theorem, the core proof, and the main novelty claim in one move. The only material left would be a short frontier recap, certificate presentation, and routine verification packaging.

## broader_theorem_nonimplication
The Leung-Ma-Schmidt theorem cited on the same Lander-conjecture slide proves the conjecture only when n is a power of a prime greater than 3. Here n = 196 = 2^2 * 7^2, so the published theorem does not dispose of the [G16,G9,7] row and Gordon still lists it as open in 2019.

## literature_gap
Gordon's 2019 Lander-conjecture slide still lists the exact row 1008 266 70 196 [G16,G9,7] as open.

## transfer_kit
- lemma: A difference set D in G satisfies the group-ring identity D D^(-1) = n + lambda G, so exact coefficient counts in quotients are admissible obstruction data.
- lemma: For every nontrivial character chi of G, a difference set must satisfy |chi(D)|^2 = n, giving a fixed character-sum target for obstruction arguments.
- lemma: Some translate of D is fixed by all multipliers, so any usable multiplier information converts the problem into an orbit-union problem.
- lemma: Gordon's 2019 slide names 1008 266 70 196 [G16,G9,7] as an exact open Lander-conjecture residue.
- toy example: The same 2019 slide deck highlights the nearby group-sensitive contrast at v = 243, where [3,3,3,9] is settled negative while [3,9,9] stays open, illustrating how a fixed group type can support a genuine title theorem.
- known obstruction: Any proof has to respect the noncyclic Sylow-7 issue that makes this a Lander-conjecture row in the first place, so a successful argument must use the [G16,G9,7] local structure rather than generic parameter counting alone.
- prior-work stop sentence: Gordon's 2019 Lander-conjecture slide stops at listing 1008 266 70 196 [G16,G9,7] as an open exact row.
- recommended first attack: Translate to a multiplier-normalized representative if possible, then push quotient-profile constraints through the 7-part and the 2-part of [G16,G9,7] until only a tiny orbit system remains.
- paper if solved: If solved exactly, the paper would be a short note settling one named small open Lander-conjecture case in a fixed abelian group type.

## bounded_source_list
- Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the Lander-conjecture slide listing the exact open row 1008 266 70 196 [G16,G9,7] with p = 7.
- Gordon's 2019 slide deck for the exact row, together with the standard group-ring and character criteria cited in that talk and a bounded freshness check against Gordon's current repository and publications pages.
- artifacts/abelian-difference-set-1008-266-70-group-g16-g9-7/record.md
- artifacts/abelian-difference-set-1008-266-70-group-g16-g9-7/status.json
