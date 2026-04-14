# Working Packet: The Exact Value of R(B10, B12)

- slug: `r-b10-b12-book-ramsey`
- title: Determine the exact value of R(B10, B12)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `72`
- single-solve-to-paper fraction: `0.76`

## statement
Determine the least n such that every graph on n vertices contains a copy of B10 or its complement contains a copy of B12.

## novelty_notes
- frontier basis: Current checked public sources support only 45 <= R(B10, B12) <= 46.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem and family framing are already present. What remains after the solve is mainly the decisive witness or forcing contradiction, one comparison paragraph with adjacent exact cases, and routine verification.
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
- assessment: Lane-eligible. The family anchor remains strong and the theorem slice is stable, though the certificate is less compact than the smallest fresh cases.

## likely_paper_shape
- note title: The Exact Value of R(B10, B12)
- hypothetical title: The Exact Value of R(B10, B12)
- paper shape: A one-theorem exact-value note on a larger but still compact one-gap almost-diagonal book Ramsey residue.
- publication if solved: Closing the one-gap case R(B10, B12) would still support a clean short note on the almost-diagonal book Ramsey line.
- minimal artifact requirements: Either a 45-vertex graph avoiding B10 whose complement avoids B12, or a forcing proof that every 45-vertex graph contains B10 or its complement contains B12.

## hypothetical_abstract
We determine the two-color Ramsey number R(B10, B12). Existing checked sources leave this almost-diagonal case in the one-gap corridor 45 <= R(B10, B12) <= 46. Our result closes a bounded unresolved point on the B_{n-2} versus B_n book Ramsey line and yields a self-contained short note with a single decisive theorem.

## single_solve_explanation
This candidate still passes the 70-90% paper test because an exact solution would itself be the honest title theorem, and the remaining writing is standard book-Ramsey packaging rather than additional mathematics. After the solve, the paper would mainly need the critical graph or forcing argument, a brief comparison with the adjacent exact values R(B11, B12) = 47 and R(B12, B13) = 51, and a short verification appendix. It is not a niche curiosity because it sits on the same named almost-diagonal family line as the smaller one-gap residues.

## broader_theorem_nonimplication
Known exact formulas in the checked sources cover the adjacent B_{n-1} versus B_n line and some prime-power diagonal cases, but not the B_{n-2} versus B_n slice at n = 12. Wesley 2026 strengthens nearby lower bounds and exact adjacent cases, yet still does not determine R(B10, B12).

## literature_gap
Publicly checked sources stop at 45 <= R(B10, B12) <= 46.

## transfer_kit
- lemma: Lemma 1 of the 2025 source gives 45 <= R(B10, B12).
- lemma: DS1.17 Section 5.3(g) gives the generic upper bound R(B10, B12) <= 46.
- lemma: Wesley 2026 proves the adjacent exact value R(B11, B12) = 47 and therefore sharpens the local family picture without settling R(B10, B12).
- lemma: The 2025 source explains that counting copies of Bk reduces to common-neighborhood counts along spine edges, giving a concrete proof ingredient for forcing arguments.
- toy example: The exact solved neighbor R(B11, B12) = 47 is the nearest completed almost-diagonal comparison directly above the target.
- known obstruction: Any 45-vertex witness must simultaneously keep every edge from having at least 10 common neighbors in one color and at least 12 common non-neighbors in the other, so a few high-codegree spine edges may govern the whole obstruction.
- prior-work stop sentence: Current checked sources stop at the one-gap window 45 <= R(B10, B12) <= 46.
- recommended first attack: Start from a 44-vertex polycirculant lower-bound construction along the Lemma 1 family line and test whether any 45th vertex can be added before attempting a global forcing proof at 45.
- paper if solved: The paper would be a short exact-value note on a larger but still clean almost-diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Lemma 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 45 <= R(B10, B12); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g), which gives the generic book upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B10, B12) <= 46; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), which settles the adjacent family R(B_{n-1}, B_n) = 4n - 1 for n <= 20 and records nearby exact anchors without closing this pair; plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Lemma 1 and proof discussion, DS1.17 Section 5.3(g), Wesley 2026 Theorem 2 and surrounding results on adjacent book families, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b10-b12-book-ramsey/record.md
- artifacts/r-b10-b12-book-ramsey/status.json
