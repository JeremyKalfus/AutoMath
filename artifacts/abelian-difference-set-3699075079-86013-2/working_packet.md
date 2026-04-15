# Working Packet: An Abelian (3699075079,86013,2)-Difference Set

- slug: `abelian-difference-set-3699075079-86013-2`
- title: abelian-difference-set-3699075079-86013-2
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `58`
- single-solve-to-paper fraction: `0.66`

## statement
Determine whether any abelian group of order 3699075079 admits a (3699075079,86013,2)-difference set.

## novelty_notes
- frontier basis: Table 3 places this tuple in the short residual list of abelian lambda = 2 cases left open after Gordon's eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If this tuple were settled, the paper frame would be compact and source-anchored. The main issue is that the solve itself looks materially harder than the top queue slots.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: none
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: low
- exact gap from source: tiny
- assessment: Not lane-eligible. The family anchor is good, but the parameter size and low proof plausibility weaken closability too much for the strict micro-paper lane.

## likely_paper_shape
- note title: An Abelian (3699075079,86013,2)-Difference Set
- hypothetical title: On Abelian (3699075079,86013,2)-Difference Sets
- paper shape: A residual-case note on one exact biplane parameter from Table 3.
- publication if solved: A construction or nonexistence proof for an abelian (3699075079,86013,2)-difference set would plausibly support a short note resolving another residual biplane case from Gordon's Table 3.
- minimal artifact requirements: Either an explicit abelian group of order 3699075079 carrying a (3699075079,86013,2)-difference set, or a compact group-uniform nonexistence proof.

## hypothetical_abstract
We determine the existence status of abelian difference sets with parameters (3699075079,86013,2). Gordon retains this tuple in Table 3 as one of the few residual biplane cases surviving the 2022 elimination framework. Any exact resolution would therefore make a finite-residual note, but current closability looks weaker than the top shortlist entries.

## single_solve_explanation
A decisive solve would still do most of the paper work because the frontier and background are already compressed into Table 3. But compared with the smaller residual tuples, more technical exposition and certificate handling would likely remain. That pushes the solve below the preferred micro-paper fraction.

## broader_theorem_nonimplication
The source explicitly preserves this tuple in Table 3 after applying its available elimination tools, so no broader published theorem in that paper already settles it.

## literature_gap
Gordon's Table 3 leaves (3699075079,86013,2) unresolved as one of the remaining abelian biplane cases.

## transfer_kit
- lemma: Theorem 2 gives the standard orbit-count obstruction framework.
- lemma: Theorem 4 is singled out as crucial for eliminating many residual biplane cases via quotient multipliers.
- lemma: The biplane section states that Table 3 contains the remaining open lambda = 2 cases.
- lemma: The source's discussion explains that many earlier cases were already eliminated computationally by Hughes and Dickey.
- toy example: The nonexistence proof for (352,27,2) remains the canonical short obstruction example in the source.
- known obstruction: This tuple already survives the current multiplier-based eliminations, so any proof must go beyond the source's present orbit-count and quotient-multiplier arguments.
- prior-work stop sentence: Gordon's Table 3 still lists (3699075079,86013,2) among the remaining open abelian lambda = 2 cases.
- recommended first attack: Use the factorization of v together with contracted multipliers for cyclic quotients to see whether every plausible abelian group type forces an orbit partition incompatible with k = 86013.
- paper if solved: If solved exactly, the paper would be a residual-case note for one surviving biplane parameter from Gordon's Table 3.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda," Journal of Algebraic Combinatorics 55 (2022), especially the biplane discussion on page 6 and Table 3 on page 6, which lists the remaining open abelian (v,k,2)-difference-set parameter sets for k <= 10^10.
- Gordon (2022) and the older biplane computations cited there.
- artifacts/abelian-difference-set-3699075079-86013-2/record.md
- artifacts/abelian-difference-set-3699075079-86013-2/status.json
