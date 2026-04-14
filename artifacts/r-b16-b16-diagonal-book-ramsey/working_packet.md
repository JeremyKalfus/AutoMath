# Working Packet: The Exact Value of R(B16, B16)

- slug: `r-b16-b16-diagonal-book-ramsey`
- title: Determine the exact value of R(B16, B16)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `75`
- single-solve-to-paper fraction: `0.74`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B16.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 65 <= R(B16, B16) <= 66. The lower endpoint is backed by an explicit recent construction, keeping the frontier narrow and publication-legible.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 65 versus 66 is settled, the note already has its title theorem, its literature comparison, and a natural main artifact. The residue after the solve is still only compact exposition and proof presentation.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Pass. This slot is slightly less compact than B14-B15, but it remains a stable one-step diagonal book gap with a clear paper packet if solved.

## likely_paper_shape
- note title: The Exact Value of R(B16, B16)
- hypothetical title: The Exact Value of R(B16, B16)
- paper shape: A one-theorem exact-value note for a diagonal book Ramsey number with explicit current lower-bound data.
- publication if solved: An exact determination of R(B16, B16) would still read as the title theorem of a short note because the public frontier is again a one-step diagonal book Ramsey gap with an explicit current lower-bound witness.
- minimal artifact requirements: Either an explicit 65-vertex coloring avoiding monochromatic B16 or a compact proof that every 66-vertex coloring forces B16.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B16, B16). Previous work placed this number in the interval 65 <= R(B16, B16) <= 66. Our result closes the remaining one-step gap for a diagonal book pair whose lower endpoint already has an explicit block-circulant witness.

## single_solve_explanation
This target passes the 70-90% paper test because the theorem statement is already the natural title theorem and the literature gap is exactly one endpoint wide. A successful solve would contribute the decisive witness or forcing argument and most of the note's narrative. What remains after the solve is mainly compact verification and framing, not a second results program.

## broader_theorem_nonimplication
The currently available broad diagonal-book results still stop at the generic one-step interval 4n + 1 <= R(B_n, B_n) <= 4n + 2. Wesley's 2026 paper improves lower bounds and gives an explicit 65-vertex witness here, but it does not determine whether 65 is sharp or 66 is forced.

## literature_gap
Current public sources stop at 65 <= R(B16, B16) <= 66.

## transfer_kit
- lemma: Wesley (2026), Appendix A / lower-bound table, gives the explicit lower bound R(B16, B16) >= 65.
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives the upper bound R(B16, B16) <= 66.
- lemma: The same 2025 lemma gives the exact neighboring almost-diagonal value R(B15, B16) = 63.
- lemma: The same family already contains exact smaller diagonal values such as R(B8, B8) = 33.
- toy example: The exact neighboring almost-diagonal case R(B15, B16) = 63 is the nearest solved benchmark for the intended theorem shape.
- known obstruction: The 2026 lower-bound witness shows that structured diagonal critical graphs still survive at order 65, so an upper-bound proof must rule out a nontrivial extension class rather than only a single sporadic graph.
- prior-work stop sentence: Current sources stop at 65 <= R(B16, B16) <= 66.
- recommended first attack: Start from Wesley's explicit 65-vertex block-circulant witness and test whether every one-vertex extension forces a monochromatic B16 via common-neighborhood counting on candidate spine edges.
- paper if solved: The paper would be a short exact-value note settling a one-step diagonal book Ramsey gap with an explicit lower-bound construction already in hand.

## bounded_source_list
- William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), Appendix A / lower-bound table giving R(B16, B16) >= 65; together with Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving R(B16, B16) <= 66; and bounded 2026-04-14 exact-statement, alternate-notation, and recent-status web checks that did not reveal a later exact determination.
- 2026 Wesley Appendix A / lower-bound table, 2025 EJC Lemma 1 for the upper bound and family context, and bounded 2026-04-14 exact-statement, synonym, and citation-status checks.
- artifacts/r-b16-b16-diagonal-book-ramsey/record.md
- artifacts/r-b16-b16-diagonal-book-ramsey/status.json
