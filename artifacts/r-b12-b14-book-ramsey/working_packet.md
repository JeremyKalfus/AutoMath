# Working Packet: The Exact Value of R(B12, B14)

- slug: `r-b12-b14-book-ramsey`
- title: Determine the exact value of R(B12, B14)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `69`
- single-solve-to-paper fraction: `0.7`

## statement
Either prove that every graph on 53 vertices contains B12 or its complement contains B14 and thus show R(B12, B14) = 53, or construct a 53-vertex graph avoiding B12 whose complement avoids B14 and thus show R(B12, B14) = 54.

## novelty_notes
- frontier basis: Current public sources leave this pair in the one-gap window 53 <= R(B12, B14) <= 54. The lower bound comes from the 2025 almost-diagonal theorem, while the best public upper bound still comes from the DS1.17 general book inequality rather than a dedicated exact argument.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The note stays short once the exact value is known. After the solve, the remaining work is mostly the proof or witness, a short comparison with the neighboring exact case R(B13, B14) = 55, and a brief explanation of why the exact B_{n-1} versus B_n line does not subsume the target.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass, though less forcefully than the top slot. The family anchor is still strong enough that one clean solve would plausibly carry almost all of the resulting note.

## likely_paper_shape
- note title: The Exact Value of R(B12, B14)
- hypothetical title: The Exact Value of R(B12, B14)
- paper shape: A one-theorem exact-value note on the B_{n-2} versus B_n book line.
- publication if solved: Closing R(B12, B14) would already support a compact note on unresolved almost-diagonal book Ramsey numbers.
- minimal artifact requirements: Either a proof that every 53-vertex graph forces B12 or a complement B14, or one explicit 53-vertex witness graph avoiding B12 whose complement avoids B14.

## hypothetical_abstract
We determine the book Ramsey number R(B12, B14). Existing work leaves this almost-diagonal case in the one-gap window 53 <= R(B12, B14) <= 54. Our result closes another small residue on the recent B_{n-2} versus B_n frontier.

## single_solve_explanation
The exact value would still be the honest title theorem, and the surrounding paper would stay short. Because the family framework is already standardized by recent book-Ramsey work, the post-solve packaging is mostly limited to the proof or witness and a short discussion of adjacent solved cases. That keeps the solve-to-paper fraction at the lower edge of the preferred band.

## broader_theorem_nonimplication
The exact B_{n-1} versus B_n theorem gives R(B13, B14) = 55 but does not imply R(B12, B14). For this pair, the current almost-diagonal source supplies the lower bound only, while the older general upper-bound machinery still leaves a one-gap residue.

## literature_gap
Current public sources support only the one-gap window 53 <= R(B12, B14) <= 54, and the bounded 2026-04-14 audit did not uncover a later exact determination.

## transfer_kit
- lemma: Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 53 <= R(B12, B14).
- lemma: DS1.17 Section 5.3(g) gives R(B12, B14) <= 2(12 + 14 + 1) = 54.
- lemma: Wesley 2026 and the survey give the exact neighboring value R(B13, B14) = 55.
- toy example: The exact case R(B13, B14) = 55 is the nearest solved off-diagonal benchmark above the target.
- known obstruction: A proof of 53 must eliminate every 53-vertex critical graph compatible with the current lower bound, while a proof of 54 needs one explicit 53-vertex witness graph avoiding B12 whose complement avoids B14.
- prior-work stop sentence: Current sources stop at the one-gap window 53 <= R(B12, B14) <= 54.
- recommended first attack: Begin from the 2025 almost-diagonal lower-bound templates and compare them to the exact neighboring B13 versus B14 line, looking for a short structural obstruction before any witness search.
- paper if solved: The paper would be a short exact-value note on a fresh almost-diagonal book Ramsey case.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), Theorem 2 and appendix benchmarks; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14.
- DS1.17 Section 5.3(g), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Wesley 2026 Theorem 2 and appendix benchmarks, plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches on 2026-04-14.
- artifacts/r-b12-b14-book-ramsey/record.md
- artifacts/r-b12-b14-book-ramsey/status.json
