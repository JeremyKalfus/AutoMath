# Working Packet: An Abelian (1840051,2350,3)-Difference Set

- slug: `abelian-difference-set-1840051-2350-3`
- title: abelian-difference-set-1840051-2350-3
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `68`
- single-solve-to-paper fraction: `0.7`

## statement
Determine whether any abelian group of order 1840051 admits a (1840051,2350,3)-difference set.

## novelty_notes
- frontier basis: Table 4 isolates (1840051,2350,3) inside a six-case lambda = 3 residual list surviving the source's elimination machinery.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If this tuple is settled, the surrounding paper frame is already present in the source: explain why it survives Theorems 2-4 and the auxiliary tests, then present the final construction or obstruction. The remaining writeup is bounded and mostly expository.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Borderline but still lane-eligible. The family anchor is clean and the post-solve packaging is light, though the larger parameter size modestly weakens closability compared with the top queue slot.

## likely_paper_shape
- note title: An Abelian (1840051,2350,3)-Difference Set
- hypothetical title: On Abelian (1840051,2350,3)-Difference Sets
- paper shape: A one-theorem note resolving one residual abelian lambda = 3 difference-set parameter from Table 4.
- publication if solved: A construction or nonexistence proof for an abelian (1840051,2350,3)-difference set would plausibly support a short note resolving another residual lambda = 3 case from Gordon's Table 4.
- minimal artifact requirements: Either an explicit abelian group of order 1840051 carrying a (1840051,2350,3)-difference set, or a compact group-uniform nonexistence proof.

## hypothetical_abstract
We determine the existence status of abelian difference sets with parameters (1840051,2350,3). Gordon's 2022 analysis leaves this tuple in the final six-case lambda = 3 residual list after applying multiplier-orbit and quotient-multiplier obstructions together with the Lander and Mann tests. An exact resolution therefore yields a focused note rather than a broad campaign.

## single_solve_explanation
The source already does the heavy framing work by collapsing the lambda = 3 search space to six residual tuples. If this exact tuple is resolved, the note mainly consists of recalling that frontier and presenting the decisive argument. That is enough to keep the solve close to paper-complete.

## broader_theorem_nonimplication
The source explicitly retains this tuple in Table 4 after its elimination theorems and standard tests have been applied. So the honest theorem slice remains the exact tuple, not a corollary of the published reductions.

## literature_gap
Gordon's Table 4 leaves (1840051,2350,3) unresolved as one of the six remaining abelian lambda = 3 parameter sets.

## transfer_kit
- lemma: Theorem 2 gives the main multiplier-orbit contradiction template.
- lemma: Theorem 3 bounds cyclic multiplier groups by |M| <= k.
- lemma: Theorem 4 bounds contracted multiplier groups in cyclic quotients.
- lemma: Table 4 identifies (1840051,2350,3) as one of the source's remaining six lambda = 3 cases.
- toy example: The source's short obstruction for (352,27,2) is the model example for the multiplier-orbit style of nonexistence proof that could still collapse this tuple.
- known obstruction: Standard multiplier, quotient, Lander, and Mann eliminations already fail here, so any solution needs a sharper structural input than the source currently uses.
- prior-work stop sentence: After applying Theorems 2, 3, 4, the Lander tests, and the Mann test, Gordon's Table 4 still lists (1840051,2350,3) among the six remaining open abelian lambda = 3 cases.
- recommended first attack: Exploit the prime n = 2347 and the factorization of v to search for a single strong multiplier-orbit decomposition that forces impossible orbit counts in every abelian group type of order 1840051.
- paper if solved: If solved exactly, the paper would be a short note removing another residual lambda = 3 case from Gordon's finite frontier.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda," Journal of Algebraic Combinatorics 55 (2022), especially Theorem 2, Theorems 3 and 4, and Table 4 on page 6, which lists the six remaining open abelian (v,k,3)-difference-set parameter sets after the source's eliminations.
- Gordon (2022), with the Lander and Mann background already referenced there.
- artifacts/abelian-difference-set-1840051-2350-3/record.md
- artifacts/abelian-difference-set-1840051-2350-3/status.json
