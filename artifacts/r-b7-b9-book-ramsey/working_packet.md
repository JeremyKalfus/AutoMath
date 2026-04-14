# Working Packet: The Exact Value of R(B7, B9)

- slug: `r-b7-b9-book-ramsey`
- title: Determine the exact value of R(B7, B9)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.79`

## statement
Determine the least n such that every graph on n vertices contains a copy of B7 or its complement contains a copy of B9.

## novelty_notes
- frontier basis: Current checked public sources support only 33 <= R(B7, B9) <= 34.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem and the family framing are already in place. What remains after the solve is mainly the decisive witness or forcing contradiction, a short positioning paragraph using nearby exact values, and routine verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible, but behind the two smaller fresh cases. The exact theorem slice is stable and paper-shaped, though the certificate looks slightly less compact.

## likely_paper_shape
- note title: The Exact Value of R(B7, B9)
- hypothetical title: The Exact Value of R(B7, B9)
- paper shape: A one-theorem exact-value note on a medium-small almost-diagonal book Ramsey residue.
- publication if solved: Closing the one-gap case R(B7, B9) would already support a short note on the almost-diagonal book Ramsey line, although the certificate is less compact than the very smallest fresh cases.
- minimal artifact requirements: Either a 33-vertex graph avoiding B7 whose complement avoids B9, or a forcing proof that every 33-vertex graph contains B7 or its complement contains B9.

## hypothetical_abstract
We determine the two-color Ramsey number R(B7, B9). Existing checked sources leave this almost-diagonal case in the one-gap corridor 33 <= R(B7, B9) <= 34. Our result closes a finite unresolved point on the B_{n-2} versus B_n book Ramsey line just above the smallest fresh residues.

## single_solve_explanation
This candidate still passes the 70-90% paper test because an exact solve would itself be the honest title theorem and the surrounding family context is already present. After the solve, the note would mainly need the decisive proof or witness, one comparison paragraph with nearby exact values such as R(B7, B8) = 31 and R(B8, B8) = 33, and routine verification. It is weaker than the smallest fresh cases only because the extremal object is a bit larger.

## broader_theorem_nonimplication
The checked 2025 source gives only the lower bound from the general B_{n-2} versus B_n lemma, while DS1.17 gives only the generic upper bound 34. Wesley's 2026 exact formula for the adjacent B_{n-1} versus B_n line does not determine the B_{n-2} versus B_n slice at (7, 9).

## literature_gap
Publicly checked sources stop at 33 <= R(B7, B9) <= 34.

## transfer_kit
- lemma: Lemma 1 of the 2025 source gives 33 <= R(B7, B9).
- lemma: DS1.17 Section 5.3(g) gives the generic upper bound R(B7, B9) <= 34.
- lemma: Table 1 of the 2025 source records nearby exact values R(B6, B8) = 29, R(B7, B8) = 31, and R(B8, B8) = 33.
- toy example: The exact solved neighbor R(B7, B8) = 31 is the nearest completed off-diagonal benchmark directly below the target.
- known obstruction: At 33 vertices, even a one-gap residue may hide a more global extremal configuration, so the critical witness may be less transparent than in the very smallest cases.
- prior-work stop sentence: Current checked sources stop at the one-gap window 33 <= R(B7, B9) <= 34.
- recommended first attack: Start from a 32-vertex lower-bound construction on the almost-diagonal book line and test whether any 33rd vertex can be added before attempting a forcing proof at 33.
- paper if solved: The paper would be a short exact-value note on an unresolved almost-diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Lemma 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 33 <= R(B7, B9); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g), which gives the generic book upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B7, B9) <= 34; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), checked as a recent outside-source status update and not found to settle this exact pair; plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Lemma 1 and Table 1, DS1.17 Section 5.3(g) and Table IXa, Wesley 2026 as a recent outside-source status check, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b7-b9-book-ramsey/record.md
- artifacts/r-b7-b9-book-ramsey/status.json
