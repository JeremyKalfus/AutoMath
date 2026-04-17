# Working Packet: The Smallest Open Exponent-Sensitive Abelian Difference-Set Case

- slug: `abelian-difference-set-243-121-60-group-3-9-9`
- title: abelian-difference-set-243-121-60-group-3-9-9
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `86`
- single-solve-to-paper fraction: `0.84`

## statement
Determine whether the abelian group of type [3,9,9] admits a (243,121,60)-difference set.

## novelty_notes
- frontier basis: Gordon's 2019 survey isolates (243,121,60) in the group [3,9,9] as the smallest remaining exact case in the question of whether difference-set existence depends only on the exponent of the ambient abelian group.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The surrounding narrative is already written by the source: the nearby yes/no comparison cases are known, the unresolved slice is explicitly named, and the final note only needs the exact construction or obstruction for this one group.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: This is a strong micro-paper candidate: one exact solve settles a named smallest-open case with a direct structural narrative and no feeder ladder.

## likely_paper_shape
- note title: The Smallest Open Exponent-Sensitive Abelian Difference-Set Case
- hypothetical title: On (243,121,60)-Difference Sets in C3 x C9 x C9
- paper shape: A one-theorem note settling the smallest open group-specific abelian difference-set case at parameters (243,121,60).
- publication if solved: A construction or nonexistence proof would settle the smallest open abelian difference-set case in which exponent-based heuristics still leave one exact group unresolved.
- minimal artifact requirements: Either an explicit subset of C3 x C9 x C9 certifying a (243,121,60)-difference set, or a compact group-specific nonexistence proof using quotient, character, or multiplier structure.

## hypothetical_abstract
We determine whether the abelian group C3 x C9 x C9 admits a (243,121,60)-difference set. Gordon's La Jolla Difference Set Repository survey identifies this as the smallest open case in the question of whether difference-set existence depends only on the exponent of the ambient abelian group. The result therefore closes a source-explicit frontier slice with little remaining packaging beyond the decisive argument and the comparison to the already-settled sibling groups.

## single_solve_explanation
This target is already paper-shaped because the literature singles it out as the smallest open exact case in a natural structural question, not as a stray tuple. A solve would immediately furnish the title theorem and the main novelty claim. What remains after the solve is only the short comparison table, notation, and a concise proof or witness presentation.

## broader_theorem_nonimplication
The known nearby examples only show that exponent does not determine existence in some larger cases and that the sibling group [3,3,3,9] is impossible; they do not decide the exact [3,9,9] group.

## literature_gap
Prior work stops at the statement that (243,121,60) is open for the group [3,9,9] even though the sibling group [3,3,3,9] is already ruled out and other comparison examples at order 324 are known.

## transfer_kit
- lemma: The group-ring criterion from Gordon's 2019 talk: D is a difference set exactly when D D^{-1} = n + lambda G.
- lemma: The character criterion from the same talk: for every nontrivial character chi, one must have |chi(D)|^2 = n, while the trivial character gives k^2.
- lemma: The comparison point recorded on the same slide: the sibling group [3,3,3,9] does not admit a (243,121,60)-difference set.
- lemma: The order-324 comparison examples in Gordon's talk show that existence can vary across abelian groups with nearby structural data, so a group-specific proof is mathematically meaningful rather than purely incidental.
- toy example: Use the order-324 yes/no comparison pair from Gordon's slide 37 as the worked model for how group structure can change existence at fixed parameters.
- known obstruction: The nearest sibling group [3,3,3,9] is already impossible, so any existence proof for [3,9,9] must exploit genuinely group-specific structure rather than parameter counts alone.
- prior-work stop sentence: The source literature still lists the group [3,9,9] as the smallest open exact case for parameters (243,121,60).
- recommended first attack: Exploit the subgroup chain C3 < C9 in the two large coordinates, pass to quotient profiles, and test whether the character values forced by a putative difference set can coexist with the known obstruction pattern from the sibling group.
- paper if solved: If solved exactly, the paper would be a one-theorem note resolving the smallest open group-specific exponent-sensitivity case for abelian difference sets.

## bounded_source_list
- Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the slide listing the smallest open exact group-specific case (243,121,60) in [3,9,9], together with the same talk's group-ring and character criteria slides.
- Gordon's 2019 LJDSR talk, together with the cited Lopez-Sanchez nonexistence result for [3,3,3,9] and the Davis-Jedwab and Jedwab comparison examples at order 324.
- artifacts/abelian-difference-set-243-121-60-group-3-9-9/record.md
- artifacts/abelian-difference-set-243-121-60-group-3-9-9/status.json
