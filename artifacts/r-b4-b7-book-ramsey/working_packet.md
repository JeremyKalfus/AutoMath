# Working Packet: The Exact Value of R(B4, B7)

- slug: `r-b4-b7-book-ramsey`
- title: Determine the exact value of R(B4, B7)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `86`
- single-solve-to-paper fraction: `0.88`

## statement
Determine the least n such that every graph on n vertices contains a copy of B4 or its complement contains a copy of B7.

## novelty_notes
- frontier basis: Current checked public sources support only 22 <= R(B4, B7) <= 23.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem, source table anchor, and local book-Ramsey comparison points are already in place. What remains after the solve is mainly the decisive witness or forcing contradiction, a brief comparison paragraph with nearby solved pairs, and routine verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. The theorem slice is stable, the family anchor is strong, and one clean solve would already provide nearly all of a credible short note.

## likely_paper_shape
- note title: The Exact Value of R(B4, B7)
- hypothetical title: The Exact Value of R(B4, B7)
- paper shape: A one-theorem exact-value note on a smallest fresh one-gap off-diagonal book Ramsey case outside current repo memory.
- publication if solved: Closing the one-gap case R(B4, B7) would already read like the title theorem of a short note on a concrete small-book Ramsey residue.
- minimal artifact requirements: Either a 22-vertex graph avoiding B4 whose complement avoids B7, or a forcing proof that every 22-vertex graph contains B4 or its complement contains B7.

## hypothetical_abstract
We determine the two-color Ramsey number R(B4, B7), where Bk denotes the k-page book graph. Existing checked sources leave this pair in the one-gap corridor 22 <= R(B4, B7) <= 23. Our result closes a compact unresolved book-Ramsey case with a certificate small enough for a short stand-alone note.

## single_solve_explanation
This candidate passes the 70-90% paper test because the exact title theorem is already visible and the surrounding narrative is standard once the last one-gap case is closed. After a solve, the note would mainly need the decisive critical graph or forcing argument, a short comparison with nearby exact values such as R(B5, B6) = 23 and R(B3, B7) = 20, and a verification appendix. It is not just a curiosity because it sits on the same named book-Ramsey surface as several recent exact determinations and still has a compact certificate size.

## broader_theorem_nonimplication
The exact formulas in Theorem 1 of the 2025 paper concern the adjacent B_{n-1} versus B_n line and the lower-bound family B_{n-2} versus B_n, not the off-diagonal slice (4, 7). The checked 2025 table gives only the one-gap window 22 <= R(B4, B7) <= 23, and the bounded recent-status check did not reveal a later theorem collapsing this specific pair.

## literature_gap
Publicly checked sources stop at 22 <= R(B4, B7) <= 23.

## transfer_kit
- lemma: Table 1 of the 2025 source gives the lower bound R(B4, B7) >= 22.
- lemma: Table 1 of the 2025 source gives the upper bound R(B4, B7) <= 23.
- lemma: The same 2025 source records nearby exact anchors R(B5, B6) = 23 and R(B3, B7) = 20.
- toy example: The exact solved neighbor R(B5, B6) = 23 is the cleanest nearby model for how a short off-diagonal book-Ramsey note is packaged.
- known obstruction: Any 22-vertex witness must keep every edge from supporting four same-color pages while also keeping every non-edge from supporting seven pages in the complement, so a few high-codegree spine pairs may control the whole configuration.
- prior-work stop sentence: Current checked sources stop at the one-gap window 22 <= R(B4, B7) <= 23.
- recommended first attack: Start from the 21-vertex lower-bound construction implicit behind the 2025 lower bound and test whether any 22nd vertex can be added before attempting a global forcing proof at 22.
- paper if solved: The paper would be a short exact-value note closing a smallest fresh off-diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1, which records the new lower bound 22 for R(B4, B7) and the new upper bound 23; together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1, version posted Sep. 6, 2024), used as the canonical survey surface for older book-Ramsey bounds and notation; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), checked as a recent outside-source status update and not found to settle this exact pair; plus bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Table 1 and surrounding discussion, DS1 as the canonical survey surface for book Ramsey notation and older bounds, Wesley 2026 as a recent outside-source status check, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b4-b7-book-ramsey/record.md
- artifacts/r-b4-b7-book-ramsey/status.json
