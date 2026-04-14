# Working Packet: The Exact Value of R(B2, B4)

- slug: `r-b2-b4-book-ramsey`
- title: Determine the exact value of R(B2, B4)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `41`
- single-solve-to-paper fraction: `0.48`

## statement
Determine the least n such that every graph on n vertices contains a copy of B2 or its complement contains a copy of B4.

## novelty_notes
- frontier basis: Current checked sources support only 13 <= R(B2, B4) <= 14, but the theorem slice is too fragile to trust as a publication-ready micro-paper target.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If genuinely frontier-novel and then solved, the title theorem would be immediate. It fails the lane because the likely output could collapse into a tiny remark, and the rediscovery surface for such a small case is unresolved.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: weak
- family anchor strength: moderate
- publication narrative strength: weak
- editorial overhead: moderate
- immediate corollary headroom: none
- isolated exact-case risk: high
- broader-theorem implication risk: unresolved
- theorem-slice stability: unclear
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Not lane-eligible. The candidate is too small, too exposed to rediscovery, and too likely to collapse into a remark rather than a dependable short paper.

## likely_paper_shape
- note title: The Exact Value of R(B2, B4)
- hypothetical title: The Exact Value of R(B2, B4)
- paper shape: A tiny exact-value remark unless a stronger narrative survives the novelty audit.
- publication if solved: An exact closure of R(B2, B4) could still be note-shaped if genuinely open, but under the present audit it looks too exposed to rediscovery and too slight to trust as a micro-paper target.
- minimal artifact requirements: Either a 13-vertex graph avoiding B2 whose complement avoids B4, or a forcing proof that every 13-vertex graph contains B2 or its complement contains B4.

## hypothetical_abstract
We determine the two-color Ramsey number R(B2, B4). Existing checked sources leave this tiny almost-diagonal case in the corridor 13 <= R(B2, B4) <= 14. If genuinely open, the result would still be exact and self-contained, but the rediscovery surface and paper-shape risk are both high.

## single_solve_explanation
If the case is frontier-novel, one solve would immediately produce the whole theorem. Almost nothing would remain beyond the proof or witness and a brief contextual paragraph. It fails the strict lane because the likely publication packet is too slight and the novelty check cost is too high for a case this small.

## broader_theorem_nonimplication
The checked 2025 source gives only the lower bound and DS1.17 gives only the generic upper bound 14. Even so, the problem is so small that older exact settlement or a broader overlooked observation remains a serious risk.

## literature_gap
Current checked public sources support only 13 <= R(B2, B4) <= 14, but the exact-status audit is not strong enough to treat the case as a reliable micro-paper target.

## transfer_kit
- lemma: Lemma 1 of the 2025 source gives 13 <= R(B2, B4).
- lemma: DS1.17 Section 5.3(g) gives the generic upper bound R(B2, B4) <= 14.
- lemma: The 2025 source provides exact nearby book values that show the ambient family notation and methods.
- toy example: The exact solved case R(B2, B8) = 21 in the 2025 source shows the family packaging, although it is not directly adjacent.
- known obstruction: The main obstruction is not proof size but paper-shape and rediscovery risk: a tiny exact value can easily already exist as a forgotten remark.
- prior-work stop sentence: Current checked sources support only the corridor 13 <= R(B2, B4) <= 14, but the bounded audit does not certify it as a safe frontier target.
- recommended first attack: Do not solve first; first discharge the exact old-literature risk with a dedicated exact-tuple sweep, and only then test whether a 12-vertex lower-bound construction extends to 13 vertices.
- paper if solved: If the case survives a stricter novelty audit, the paper would be a tiny exact-value note on a very small book Ramsey residue.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Lemma 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 13 <= R(B2, B4); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g), which gives the generic book upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B2, B4) <= 14; plus bounded family-level web checks on 2026-04-14 that did not surface a later exact closure but did not fully clear the rediscovery surface for such a tiny case.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Lemma 1, DS1.17 Section 5.3(g), and bounded 2026-04-14 family-level web checks.
- artifacts/r-b2-b4-book-ramsey/record.md
- artifacts/r-b2-b4-book-ramsey/status.json
