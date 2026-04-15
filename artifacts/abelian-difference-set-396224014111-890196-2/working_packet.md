# Working Packet: An Abelian (396224014111,890196,2)-Difference Set

- slug: `abelian-difference-set-396224014111-890196-2`
- title: abelian-difference-set-396224014111-890196-2
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `49`
- single-solve-to-paper fraction: `0.6`

## statement
Determine whether any abelian group of order 396224014111 admits a (396224014111,890196,2)-difference set.

## novelty_notes
- frontier basis: Table 3 retains this tuple in the finite residual list of abelian lambda = 2 cases left open after Gordon's eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The frontier basis is clear, but the parameter size makes both the proof and the final certificate unwieldy relative to the strict micro-paper objective.
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
- assessment: Not lane-eligible. The family anchor is real, but the likely proof burden and packaging cost are too high for the current micro-paper objective.

## likely_paper_shape
- note title: An Abelian (396224014111,890196,2)-Difference Set
- hypothetical title: On Abelian (396224014111,890196,2)-Difference Sets
- paper shape: A residual-case note on one exact biplane parameter from Table 3, if it could be closed cleanly.
- publication if solved: A construction or nonexistence proof for an abelian (396224014111,890196,2)-difference set would plausibly support a note on another residual Table 3 biplane parameter, but it is far from the preferred closability regime.
- minimal artifact requirements: Either an explicit abelian group of order 396224014111 carrying a (396224014111,890196,2)-difference set, or a compact group-uniform nonexistence proof.

## hypothetical_abstract
We consider the existence of abelian difference sets with parameters (396224014111,890196,2). Gordon's Table 3 leaves this tuple in the finite residual biplane frontier after the current elimination methods are exhausted. Any resolution would be mathematically meaningful, but it is not well aligned with the one-shot micro-paper lane because the likely proof and certificate burden are too heavy.

## single_solve_explanation
A solve would still leave a recognizable note because the exact frontier is already source-anchored. But compared with the smaller residual cases, the supporting exposition and certificate management would be heavier, and the proof itself looks materially less closeable. That keeps the solve outside the preferred 70-90% paper band.

## broader_theorem_nonimplication
The source explicitly keeps this tuple in Table 3 after applying its available elimination methods, so it is not already implied by the broader published theory.

## literature_gap
Gordon's Table 3 leaves (396224014111,890196,2) unresolved as one of the remaining abelian biplane cases.

## transfer_kit
- lemma: Theorem 2 gives the main multiplier-orbit obstruction template.
- lemma: Theorem 4 supplies the quotient-multiplier bound emphasized in the biplane discussion.
- lemma: The biplane section states that Table 3 records the remaining open lambda = 2 cases.
- lemma: The source's residual-list framing means the honest theorem slice is the exact tuple itself.
- toy example: The source's short nonexistence proof for (352,27,2) is still the model example for a compact biplane obstruction argument.
- known obstruction: This tuple already survives all eliminations used in the source, so only a sharper arithmetic or character-theoretic obstruction is likely to finish it cleanly.
- prior-work stop sentence: Gordon's Table 3 still lists (396224014111,890196,2) among the remaining open abelian lambda = 2 cases.
- recommended first attack: Test whether a single large prime divisor of v combined with a prime divisor of n can force an orbit-size contradiction stronger than the source's current Theorem 2 analysis across all abelian group types of order v.
- paper if solved: If solved exactly, the paper would be a residual-case note on one surviving biplane parameter, but it is not a preferred micro-paper target.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda," Journal of Algebraic Combinatorics 55 (2022), especially the biplane discussion on page 6 and Table 3 on page 6, which lists the remaining open abelian (v,k,2)-difference-set parameter sets for k <= 10^10.
- Gordon (2022) and the earlier biplane computations cited there.
- artifacts/abelian-difference-set-396224014111-890196-2/record.md
- artifacts/abelian-difference-set-396224014111-890196-2/status.json
