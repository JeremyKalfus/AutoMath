# Working Packet: The Exact Value of R(B4, B6)

- slug: `r-b4-b6-book-ramsey`
- title: Determine the exact value of R(B4, B6)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.86`

## statement
Determine the least n such that every graph on n vertices contains a copy of B4 or its complement contains a copy of B6.

## novelty_notes
- frontier basis: Current checked public sources support only 21 <= R(B4, B6) <= 22.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem, family framing, and nearby exact book values are already in place. What remains after the solve is mainly the decisive witness or forcing contradiction, one short comparison paragraph with neighboring exact values, and routine verification.
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
- assessment: Lane-eligible. The exact theorem slice is stable, the family anchor is strong, and one clean solve would already supply most of a legitimate short paper packet.

## likely_paper_shape
- note title: The Exact Value of R(B4, B6)
- hypothetical title: The Exact Value of R(B4, B6)
- paper shape: A one-theorem exact-value note on the smallest fresh B_{n-2} versus B_n book Ramsey residue outside current repo memory.
- publication if solved: Closing the one-gap case R(B4, B6) would already read like the title theorem of a short note on the almost-diagonal book Ramsey line.
- minimal artifact requirements: Either a 21-vertex graph avoiding B4 whose complement avoids B6, or a forcing proof that every 21-vertex graph contains B4 or its complement contains B6.

## hypothetical_abstract
We determine the two-color Ramsey number R(B4, B6), where Bk denotes the k-page book graph. Existing checked sources leave this almost-diagonal case in the one-gap corridor 21 <= R(B4, B6) <= 22. Our result closes a compact unresolved point on the B_{n-2} versus B_n book Ramsey line with a certificate small enough for a short stand-alone note.

## single_solve_explanation
This candidate passes the 70-90% paper test because the exact title theorem is already visible and the surrounding book-Ramsey narrative is standard. After a solve, the note would mainly need the decisive critical graph or forcing argument, a brief comparison with nearby exact values such as R(B5, B6) = 23 and R(B6, B7) = 27, and a short verification appendix. It is not just a curiosity because it is the smallest fresh one-gap almost-diagonal book case not already parked in repo memory.

## broader_theorem_nonimplication
The checked 2025 source gives only the lower bound from the general B_{n-2} versus B_n lemma, while DS1.17 gives only the generic upper bound 22. Wesley's 2026 paper settles the adjacent B_{n-1} versus B_n line up to n <= 20, but that does not determine the B_{n-2} versus B_n slice at (4, 6).

## literature_gap
Publicly checked sources stop at 21 <= R(B4, B6) <= 22.

## transfer_kit
- lemma: Lemma 1 of the 2025 source gives 21 <= R(B4, B6).
- lemma: DS1.17 Section 5.3(g) gives the generic upper bound R(B4, B6) <= 22.
- lemma: Table 1 of the 2025 source records nearby exact values R(B5, B6) = 23 and R(B6, B7) = 27.
- toy example: The exact solved neighbor R(B5, B6) = 23 is the nearest completed model for how a short off-diagonal book Ramsey note is packaged.
- known obstruction: Any 21-vertex witness must simultaneously suppress a 4-page book in one color and a 6-page book in the complement, so a few high-codegree spine edges may control the whole configuration.
- prior-work stop sentence: Current checked sources stop at the one-gap window 21 <= R(B4, B6) <= 22.
- recommended first attack: Start from a 20-vertex lower-bound construction on the B_{n-2} versus B_n line and test whether any 21st vertex can be added before attempting a global forcing proof at 21.
- paper if solved: The paper would be a short exact-value note closing the smallest fresh almost-diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Lemma 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 21 <= R(B4, B6); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g), which gives the generic book upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B4, B6) <= 22; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), checked as a recent outside-source status update and not found to settle this exact pair; plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Lemma 1 and Table 1, DS1.17 Section 5.3(g) and Table IXa, Wesley 2026 as a recent outside-source status check, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b4-b6-book-ramsey/record.md
- artifacts/r-b4-b6-book-ramsey/status.json
