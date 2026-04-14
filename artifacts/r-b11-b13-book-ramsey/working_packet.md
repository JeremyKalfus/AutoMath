# Working Packet: The Exact Value of R(B11, B13)

- slug: `r-b11-b13-book-ramsey`
- title: Determine the exact value of R(B11, B13)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `70`
- single-solve-to-paper fraction: `0.74`

## statement
Determine the least n such that every graph on n vertices contains a copy of B11 or its complement contains a copy of B13.

## novelty_notes
- frontier basis: Current checked public sources support only 49 <= R(B11, B13) <= 50.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem and local family narrative are already present. What remains after the solve is mainly the decisive witness or forcing contradiction, one comparison paragraph with adjacent exact cases, and routine verification.
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
- assessment: Lane-eligible, though near the back of the queue because the certificate is larger than the smaller almost-diagonal residues. The theorem slice remains stable and paper-shaped.

## likely_paper_shape
- note title: The Exact Value of R(B11, B13)
- hypothetical title: The Exact Value of R(B11, B13)
- paper shape: A one-theorem exact-value note on a larger one-gap almost-diagonal book Ramsey residue.
- publication if solved: Closing the one-gap case R(B11, B13) would still yield a viable short note on the almost-diagonal book Ramsey line.
- minimal artifact requirements: Either a 49-vertex graph avoiding B11 whose complement avoids B13, or a forcing proof that every 49-vertex graph contains B11 or its complement contains B13.

## hypothetical_abstract
We determine the two-color Ramsey number R(B11, B13). Existing checked sources leave this almost-diagonal case in the one-gap corridor 49 <= R(B11, B13) <= 50. Our result closes a bounded unresolved point on the B_{n-2} versus B_n book Ramsey line and yields a short note centered on a single exact theorem.

## single_solve_explanation
This candidate passes the 70-90% paper test because the title theorem is already visible and the post-solve work is mostly expository packaging rather than additional mathematics. After the solve, the note would mainly need the decisive witness or forcing proof, a short comparison with the adjacent exact values R(B11, B12) = 47 and R(B12, B13) = 51, and a routine verification appendix. It remains paper-shaped because it is an exact unresolved slice on a named family line rather than an isolated census fact.

## broader_theorem_nonimplication
Known exact formulas in the checked sources cover the adjacent B_{n-1} versus B_n line and some diagonal cases, but not the B_{n-2} versus B_n slice at n = 13. Wesley 2026 strengthens nearby lower bounds and exact adjacent cases, yet still does not determine R(B11, B13).

## literature_gap
Publicly checked sources stop at 49 <= R(B11, B13) <= 50.

## transfer_kit
- lemma: Lemma 1 of the 2025 source gives 49 <= R(B11, B13).
- lemma: DS1.17 Section 5.3(g) gives the generic upper bound R(B11, B13) <= 50.
- lemma: Wesley 2026 proves adjacent exact values on the B_{n-1} versus B_n line up to n <= 20, including local anchors around this case, without settling R(B11, B13).
- lemma: The 2025 source reduces book counting to common-neighborhood counts along candidate spine edges, giving a direct forcing template.
- toy example: The exact solved neighbor R(B12, B13) = 51 is the nearest completed almost-diagonal comparison directly above the target.
- known obstruction: Any 49-vertex witness must suppress very large common-neighborhood counts in both colors, so the extremal obstruction may be governed by a small set of highly constrained spine edges.
- prior-work stop sentence: Current checked sources stop at the one-gap window 49 <= R(B11, B13) <= 50.
- recommended first attack: Start from a 48-vertex polycirculant lower-bound construction on the Lemma 1 family line and test whether any 49th vertex can be added before attempting a forcing proof at 49.
- paper if solved: The paper would be a short exact-value note on a larger almost-diagonal book Ramsey case with immediate family context.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Lemma 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 49 <= R(B11, B13); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g), which gives the generic book upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B11, B13) <= 50; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), which settles the adjacent family R(B_{n-1}, B_n) = 4n - 1 for n <= 20 and sharpens the nearby exact picture without closing this pair; plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Lemma 1 and proof discussion, DS1.17 Section 5.3(g), Wesley 2026 Theorem 2 and nearby exact book values, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b11-b13-book-ramsey/record.md
- artifacts/r-b11-b13-book-ramsey/status.json
