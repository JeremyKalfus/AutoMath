# Working Packet: The Exact Value of R(B16, B16)

- slug: `r-b16-b16-book-ramsey`
- title: Determine the exact value of R(B16, B16)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `63`
- single-solve-to-paper fraction: `0.68`

## statement
Determine the least n such that every graph on n vertices contains a copy of B16 or its complement contains a copy of B16.

## novelty_notes
- frontier basis: Current checked public sources support only 65 <= R(B16, B16) <= 66.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved, the result would still stand as the note's title theorem inside the diagonal book family. It misses the strict lane because the larger critical size makes a one-pass proof less plausible and raises the chance that the packet would need more technical cleanup after the solve.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Borderline but not lane-eligible. The theorem slice is stable and the family anchor is good, but the solve-to-paper fraction is a little too low for strict one-shot publication mode.

## likely_paper_shape
- note title: The Exact Value of R(B16, B16)
- hypothetical title: The Exact Value of R(B16, B16)
- paper shape: A one-theorem exact-value note on a larger diagonal book Ramsey residue.
- publication if solved: An exact closure of R(B16, B16) would still support a short diagonal-book note, but the solve looks less likely to be a single clean pass than the stricter lane prefers.
- minimal artifact requirements: A 65-vertex extremal witness or a compact forcing proof at 65 vertices, together with explicit verification of the relevant common-neighbor bounds.

## hypothetical_abstract
We determine the diagonal Ramsey number R(B16, B16) for the 16-page book graph. Current checked literature leaves the value in the interval 65 <= R(B16, B16) <= 66, and the available prime-power exactness theorem does not apply because 65 is not a prime power. Our result closes one more unresolved diagonal case in the finite small-book regime.

## single_solve_explanation
A clean exact solve would still give a legitimate title theorem and most of the final note. The family context and near-neighbor comparisons already exist, so the paper would mostly need the decisive certificate and a short positioning paragraph. It fails the strict micro-paper lane because the larger extremal size makes the solve less likely to remain compact enough to occupy 70-90% of the total effort.

## broader_theorem_nonimplication
The checked infinite exact family covers prime-power values of 4n + 1 only, and 65 is not among them. The checked 2025 source gives only the one-gap corridor 65-66 for this exact n and no source-internal theorem, proposition, or example collapses it.

## literature_gap
Publicly checked sources stop at 65 <= R(B16, B16) <= 66.

## transfer_kit
- lemma: Theorem 1 of the 2025 source gives 65 <= R(B16, B16) <= 66.
- lemma: The 2022 source explains the diagonal exactness mechanism for prime-power cases and therefore clarifies why n = 16 remains outside the solved family.
- lemma: The checked literature provides nearby exact diagonal or almost-diagonal book benchmarks for comparison once an exact value is found.
- toy example: The nearby resolved prime-power diagonal case n = 20 gives the model exact value R(B20, B20) = 82 in the checked family literature.
- known obstruction: Even a 65-vertex witness would likely need globally coordinated structure, so the certificate may resist the compact critical-graph descriptions that make the smallest one-gap cases attractive.
- prior-work stop sentence: Current checked sources stop at the one-gap window 65 <= R(B16, B16) <= 66.
- recommended first attack: Begin with a symmetry-driven extremal ansatz and test whether diagonal common-neighbor constraints force a 65-vertex critical graph into a small family of candidate configurations.
- paper if solved: The paper would be a short exact-value note on a larger unresolved diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1, which gives 65 <= R(B16, B16) <= 66; and Shyam Narayanan and Tian Zhang, "Ramsey numbers of fans and large books" (Electronic Journal of Combinatorics 29(1), 2022), whose prime-power diagonal exactness result does not settle n = 16 because 4n + 1 = 65 is not a prime power; together with bounded exact-statement, alternate-notation, source-internal, outside-source, and recent-status web checks on 2026-04-14 that did not reveal a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Narayanan-Zhang 2022 for the prime-power diagonal exactness mechanism, and bounded 2026-04-14 exact-term, alternate-notation, source-internal, outside-source, and recent-status web checks.
- artifacts/r-b16-b16-book-ramsey/record.md
- artifacts/r-b16-b16-book-ramsey/status.json
