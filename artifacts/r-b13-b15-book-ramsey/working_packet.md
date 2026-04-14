# Working Packet: The Exact Value of R(B13, B15)

- slug: `r-b13-b15-book-ramsey`
- title: Determine the exact value of R(B13, B15)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `69`
- single-solve-to-paper fraction: `0.74`

## statement
Determine the least n such that every graph on n vertices contains a copy of B13 or its complement contains a copy of B15.

## novelty_notes
- frontier basis: Current checked public sources support only 57 <= R(B13, B15) <= 58.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the exact title theorem and the almost-diagonal family framing are already present. What remains after the solve is mainly the decisive witness or forcing contradiction, one comparison paragraph with the exact adjacent line, and routine verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible. The family anchor is still strong and the theorem slice is stable, although the witness scale is large enough to reduce certificate compactness relative to the smallest cases.

## likely_paper_shape
- note title: The Exact Value of R(B13, B15)
- hypothetical title: The Exact Value of R(B13, B15)
- paper shape: A one-theorem exact-value note on a larger but still one-gap almost-diagonal book Ramsey residue.
- publication if solved: Closing the one-gap case R(B13, B15) would still yield a viable short note on the almost-diagonal book Ramsey line.
- minimal artifact requirements: Either a 57-vertex graph avoiding B13 whose complement avoids B15, or a forcing proof that every 57-vertex graph contains B13 or its complement contains B15.

## hypothetical_abstract
We determine the two-color Ramsey number R(B13, B15). Existing checked sources leave this almost-diagonal pair in the one-gap corridor 57 <= R(B13, B15) <= 58. Our result closes a bounded unresolved point on the B_{n-2} versus B_n book Ramsey line and yields a self-contained short note with a single decisive theorem.

## single_solve_explanation
This candidate still passes the 70-90% paper test because the exact solution would itself be the honest title theorem, and the remaining writing is ordinary book-Ramsey packaging rather than new mathematics. After the solve, the paper would mainly need the critical graph or forcing argument, a short comparison with exact adjacent values such as R(B14, B15) = 59 and R(B15, B16) = 63, and a brief verification appendix. It is not just a curiosity because it sits directly on the named almost-diagonal family line rather than as an isolated extracted instance.

## broader_theorem_nonimplication
The known exact shortcut mentioned in the 2025 source settles R(B_{n-2}, B_n) only when n is congruent to 2 mod 3, and here n = 15. The adjacent exact family R(B_{n-1}, B_n) = 4n - 1 for 4 <= n <= 21 also does not settle the slice (13, 15).

## literature_gap
Publicly checked sources stop at 57 <= R(B13, B15) <= 58.

## transfer_kit
- lemma: Theorem 1 of the 2025 source gives the lower bound R(B13, B15) >= 57.
- lemma: DS1 gives the generic upper bound R(B13, B15) <= 58.
- lemma: Theorem 1 also gives the adjacent exact values R(B14, B15) = 59 and R(B15, B16) = 63.
- toy example: The exact solved adjacent case R(B14, B15) = 59 is the nearest family-level model for how the almost-diagonal line is packaged in a short note.
- known obstruction: Any 57-vertex witness must simultaneously suppress 13-page books in one color and 15-page books in the complement, so the obstruction is likely controlled by a narrow band of allowed common-neighborhood counts.
- prior-work stop sentence: Current checked sources stop at the one-gap window 57 <= R(B13, B15) <= 58.
- recommended first attack: Start from the 56-vertex 2-polycirculant lower-bound family behind Theorem 1 and test whether a 57th vertex can be added before attempting a global forcing proof at 57.
- paper if solved: The paper would be a short exact-value note on a larger unresolved almost-diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 57 <= R(B13, B15); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1, version posted Sep. 6, 2024), which gives the generic upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B13, B15) <= 58; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), checked as a recent outside-source status update and not found to settle this exact pair; plus bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Theorem 1 and note following it, DS1 for the generic upper-bound surface, Wesley 2026 as a recent outside-source status check, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b13-b15-book-ramsey/record.md
- artifacts/r-b13-b15-book-ramsey/status.json
