# Working Packet: The Exact Value of R(B2, B10)

- slug: `r-b2-b10-book-ramsey`
- title: Determine the exact value of R(B2, B10)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `77`
- single-solve-to-paper fraction: `0.79`

## statement
Determine the least n such that every graph on n vertices contains a copy of B2 or its complement contains a copy of B10.

## novelty_notes
- frontier basis: Current checked public sources support only 25 <= R(B2, B10) <= 26.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the paper already has a precise title theorem and a compact certificate scale. What remains after the solve is mainly the decisive witness or forcing contradiction, one comparison paragraph with nearby small-book values, and routine verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible, though less robust than the almost-diagonal line. The certificate size is excellent and one solve would still supply most of a real short note.

## likely_paper_shape
- note title: The Exact Value of R(B2, B10)
- hypothetical title: The Exact Value of R(B2, B10)
- paper shape: A one-theorem exact-value note on a one-gap book Ramsey pair with a very small witness scale.
- publication if solved: Closing the one-gap case R(B2, B10) would support a compact exact-value note on a sharply bounded small-book Ramsey pair.
- minimal artifact requirements: Either a 25-vertex graph avoiding B2 whose complement avoids B10, or a forcing proof that every 25-vertex graph contains B2 or its complement contains B10.

## hypothetical_abstract
We determine the two-color Ramsey number R(B2, B10). Existing checked sources leave this pair in the one-gap corridor 25 <= R(B2, B10) <= 26. Our result closes a sharply bounded small-book Ramsey case with a certificate compact enough for a short self-contained note.

## single_solve_explanation
This candidate still passes the 70-90% paper test because an exact closure would itself be the honest title theorem, and the remaining work is standard short-note packaging rather than additional mathematics. After the solve, the note would mainly need the decisive witness or forcing argument, a brief comparison with neighboring small-book pairs such as R(B2, B8) = 21 and the window for R(B2, B9), and a short verification appendix. The risk is that the story is slightly more special-purpose than the almost-diagonal family, but the one-gap status and tiny certificate scale keep it paper-shaped.

## broader_theorem_nonimplication
The exact family results highlighted in the 2025 source do not cover the highly asymmetric slice (2, 10). The checked source table and survey support only 25 <= R(B2, B10) <= 26, and the bounded recent-status check did not reveal a later paper settling this exact pair.

## literature_gap
Publicly checked sources stop at 25 <= R(B2, B10) <= 26.

## transfer_kit
- lemma: Table 1 of the 2025 source gives the lower bound R(B2, B10) >= 25.
- lemma: DS1 gives the generic upper bound R(B2, B10) <= 26.
- lemma: The 2025 source records the nearby exact anchor R(B2, B8) = 21.
- toy example: The exact value R(B2, B8) = 21 is the nearest solved comparison for how a short note on the B2 line is packaged.
- known obstruction: Any 25-vertex witness must avoid even a 2-page book in one color, so the obstruction may be driven by forbidding modest common-neighborhood counts while simultaneously suppressing a much larger complementary book.
- prior-work stop sentence: Current checked sources stop at the one-gap window 25 <= R(B2, B10) <= 26.
- recommended first attack: Exploit the very small B2 condition to derive a tight codegree framework first, and only then test whether a 25-vertex witness can exist.
- paper if solved: The paper would be a short exact-value note on a sharply bounded small-book Ramsey pair.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1, which records the new lower bound 25 for R(B2, B10) and cites the standing upper bound 26; together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1, version posted Sep. 6, 2024), which records the general book upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B2, B10) <= 26; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), checked as a recent outside-source status update and not found to settle this exact pair; plus bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Table 1 and surrounding book discussion, DS1 for the survey upper-bound surface, Wesley 2026 as a recent outside-source status check, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b2-b10-book-ramsey/record.md
- artifacts/r-b2-b10-book-ramsey/status.json
