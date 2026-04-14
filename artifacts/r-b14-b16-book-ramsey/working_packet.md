# Working Packet: The Exact Value of R(B14, B16)

- slug: `r-b14-b16-book-ramsey`
- title: Determine the exact value of R(B14, B16)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `66`
- single-solve-to-paper fraction: `0.72`

## statement
Determine the least n such that every graph on n vertices contains a copy of B14 or its complement contains a copy of B16.

## novelty_notes
- frontier basis: Current checked public sources support only 61 <= R(B14, B16) <= 62.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the exact theorem and family anchor are already present. What remains after the solve is mainly the decisive witness or forcing contradiction, one short comparison paragraph with adjacent exact cases, and routine verification.
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
- assessment: Lane-eligible. The family anchor stays strong and the theorem slice is stable, though the certificate is less compact than for the smallest live cases.

## likely_paper_shape
- note title: The Exact Value of R(B14, B16)
- hypothetical title: The Exact Value of R(B14, B16)
- paper shape: A one-theorem exact-value note on a one-gap almost-diagonal book Ramsey residue of moderate witness size.
- publication if solved: Closing the one-gap case R(B14, B16) would still support a short note on the almost-diagonal book Ramsey line.
- minimal artifact requirements: Either a 61-vertex graph avoiding B14 whose complement avoids B16, or a forcing proof that every 61-vertex graph contains B14 or its complement contains B16.

## hypothetical_abstract
We determine the two-color Ramsey number R(B14, B16). Existing checked sources leave this almost-diagonal pair in the one-gap corridor 61 <= R(B14, B16) <= 62. Our result closes another bounded unresolved point on the B_{n-2} versus B_n book Ramsey line with a single decisive theorem.

## single_solve_explanation
This candidate remains paper-shaped because solving the exact one-gap residue would itself furnish the title theorem and the note would not need further mathematical buildup. After the solve, the paper would mainly need the critical graph or forcing argument, a brief comparison with exact adjacent values such as R(B15, B16) = 63 and R(B14, B15) = 59, and a short verification appendix. The main cost is that the witness scale is larger than the smallest cases, not that the statement lacks a paper narrative.

## broader_theorem_nonimplication
The known exact shortcut for R(B_{n-2}, B_n) when n is congruent to 2 mod 3 does not apply because n = 16. The adjacent exact line R(B_{n-1}, B_n) = 4n - 1 likewise does not determine the slice (14, 16).

## literature_gap
Publicly checked sources stop at 61 <= R(B14, B16) <= 62.

## transfer_kit
- lemma: Theorem 1 of the 2025 source gives the lower bound R(B14, B16) >= 61.
- lemma: DS1 gives the generic upper bound R(B14, B16) <= 62.
- lemma: Theorem 1 gives the nearby exact values R(B14, B15) = 59 and R(B15, B16) = 63.
- toy example: The exact adjacent case R(B15, B16) = 63 is the closest solved family anchor directly above the target.
- known obstruction: Any 61-vertex witness must keep common-neighborhood counts below the thresholds that generate 14-page books in one color and 16-page books in the complement, so the feasible codegree profile is likely narrow.
- prior-work stop sentence: Current checked sources stop at the one-gap window 61 <= R(B14, B16) <= 62.
- recommended first attack: Start from the 60-vertex lower-bound family promised by Theorem 1 and test whether any 61st vertex can be inserted before attempting a forcing proof at 61.
- paper if solved: The paper would be a short exact-value note on another unresolved almost-diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 61 <= R(B14, B16); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1, version posted Sep. 6, 2024), which gives the generic upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B14, B16) <= 62; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), checked as a recent outside-source status update and not found to settle this exact pair; plus bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Theorem 1 and note following it, DS1 for the generic upper-bound surface, Wesley 2026 as a recent outside-source status check, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b14-b16-book-ramsey/record.md
- artifacts/r-b14-b16-book-ramsey/status.json
