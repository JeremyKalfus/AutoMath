# Working Packet: The Exact Value of R(B5, B7)

- slug: `r-b5-b7-book-ramsey`
- title: Determine the exact value of R(B5, B7)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `82`
- single-solve-to-paper fraction: `0.84`

## statement
Determine the least n such that every graph on n vertices contains a copy of B5 or its complement contains a copy of B7.

## novelty_notes
- frontier basis: Current checked public sources support only 25 <= R(B5, B7) <= 26.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem and the surrounding almost-diagonal book narrative are already in place. What remains after the solve is mainly the decisive witness or forcing contradiction, one short comparison paragraph with nearby exact values, and routine verification.
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
- assessment: Lane-eligible. The exact theorem slice is stable, broader-family nonimplication is specific, and one solve would already carry most of a genuine short note.

## likely_paper_shape
- note title: The Exact Value of R(B5, B7)
- hypothetical title: The Exact Value of R(B5, B7)
- paper shape: A one-theorem exact-value note on a one-gap almost-diagonal book Ramsey residue.
- publication if solved: Closing the one-gap case R(B5, B7) would already support a short exact-value note on the almost-diagonal book Ramsey line.
- minimal artifact requirements: Either a 25-vertex graph avoiding B5 whose complement avoids B7, or a forcing proof that every 25-vertex graph contains B5 or its complement contains B7.

## hypothetical_abstract
We determine the two-color Ramsey number R(B5, B7). Existing checked sources leave this almost-diagonal case in the one-gap corridor 25 <= R(B5, B7) <= 26. Our result closes another compact unresolved point on the B_{n-2} versus B_n book Ramsey line with a certificate small enough for a short note.

## single_solve_explanation
This candidate passes the 70-90% paper test because the exact theorem would already be the honest title theorem and the family framing is standard. After a solve, the paper would mainly need the decisive witness or forcing proof, a short comparison with neighboring exact values such as R(B6, B7) = 27, and a routine verification appendix. It is not merely a tiny curiosity because it sits on a named one-gap family line rather than an ad hoc isolated instance.

## broader_theorem_nonimplication
The checked 2025 source gives only the lower bound from the general B_{n-2} versus B_n lemma, while DS1.17 gives only the generic upper bound 26. Wesley 2026 independently confirms the lower bound 25 but does not provide an exact closure for R(B5, B7), and nearby exact pairs such as R(B5, B6) and R(B6, B7) do not determine it.

## literature_gap
Publicly checked sources stop at 25 <= R(B5, B7) <= 26.

## transfer_kit
- lemma: Lemma 1 of the 2025 source gives 25 <= R(B5, B7).
- lemma: DS1.17 Section 5.3(g) gives the generic upper bound R(B5, B7) <= 26.
- lemma: Wesley 2026 records an independent lower bound R(B5, B7) >= 25 without closing the pair.
- toy example: The exact solved neighbor R(B6, B7) = 27 is the nearest completed model directly above the target on the same book line.
- known obstruction: Any 25-vertex witness must control common-neighbor counts on both colors at once, so the extremal obstruction may be concentrated around a small number of candidate spine edges.
- prior-work stop sentence: Current checked sources stop at the one-gap window 25 <= R(B5, B7) <= 26.
- recommended first attack: Begin from a 24-vertex lower-bound construction on the B_{n-2} versus B_n line and test whether any 25th vertex can be inserted before attempting a forcing proof at 25.
- paper if solved: The paper would be a short exact-value note on an unresolved almost-diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Lemma 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 25 <= R(B5, B7); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g), which gives the generic book upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B5, B7) <= 26; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), which explicitly notes an independent lower bound R(B5, B7) >= 25 but does not close the exact pair; plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Lemma 1 and Table 1, DS1.17 Section 5.3(g) and Table IXa, Wesley 2026 as an independent recent-status check, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b5-b7-book-ramsey/record.md
- artifacts/r-b5-b7-book-ramsey/status.json
