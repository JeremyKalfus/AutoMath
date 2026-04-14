# Working Packet: The Exact Value of R(B19, B19)

- slug: `r-b19-b19-diagonal-book-ramsey`
- title: Determine the exact value of R(B19, B19)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `78`
- single-solve-to-paper fraction: `0.78`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B19.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 77 <= R(B19, B19) <= 78. The frontier is a single endpoint in a named family with the adjacent exact almost-diagonal value R(B18, B19) = 75 already available as a comparison point.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 77 versus 78 is settled, the note already has its title theorem, its literature comparison, and its central artifact. What remains after the solve is mostly polishing the decisive witness or forcing argument and presenting the short family-context paragraph.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Strong pass. This is the cleanest audited diagonal-book slice still open after the recent literature update, and one exact solve would already look like most of a publishable short paper.

## likely_paper_shape
- note title: The Exact Value of R(B19, B19)
- hypothetical title: The Exact Value of R(B19, B19)
- paper shape: A one-theorem exact-value note for the smallest currently exposed diagonal book Ramsey gap still left one step wide in the recent literature.
- publication if solved: An exact determination of R(B19, B19) would plausibly be the title theorem of a short note because the public frontier is a one-step diagonal book Ramsey gap with an immediate family benchmark beside it.
- minimal artifact requirements: Either an explicit 77-vertex coloring avoiding monochromatic B19 or a compact proof that every 78-vertex coloring forces B19.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B19, B19). Previous work left this number in the interval 77 <= R(B19, B19) <= 78. Our result closes the remaining one-step gap for this diagonal book pair.

## single_solve_explanation
This target clears the 70-90% paper test because one successful solve would already deliver the title theorem, the decisive comparison with the known almost-diagonal neighbor, and the main mathematical artifact. The residual work after the solve is light editorial packaging rather than another theorem. The family anchor is strong enough that the result reads like a real short note rather than a one-paragraph curiosity.

## broader_theorem_nonimplication
The current broad diagonal-book theory only supplies the interval 77 <= R(B19, B19) <= 78, while the nearby exact theorem R(B18, B19) = 75 does not determine the diagonal endpoint. Solving the n = 19 diagonal slice would therefore still be the honest title theorem, not a corollary of an existing broader published statement.

## literature_gap
Current public sources stop at 77 <= R(B19, B19) <= 78.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 77 <= R(B19, B19) <= 78.
- lemma: The same lemma gives the exact neighboring almost-diagonal value R(B18, B19) = 75.
- lemma: The 2025 paper controls books by counting common neighbors of candidate spine edges, which is the natural forcing mechanism for an upper-bound proof.
- lemma: Wesley (2026) confirms recent lower-bound architectures for book Ramsey numbers without reporting an exact diagonal closure at n = 19.
- toy example: The exact almost-diagonal case R(B18, B19) = 75 is the nearest solved benchmark for the intended theorem shape.
- known obstruction: Near-extremal diagonal-book colorings can retain substantial symmetry, so the upper-bound side may need to exclude a small structured class rather than a single sporadic witness.
- prior-work stop sentence: Current public sources stop at 77 <= R(B19, B19) <= 78.
- recommended first attack: Use common-neighborhood forcing on candidate spine edges, anchored by the exact R(B18, B19) = 75 benchmark and the published polycirculant lower-bound templates, to show that every 77-vertex near-extremal coloring collapses when extended.
- paper if solved: The paper would be a short exact-value note settling the smallest currently exposed diagonal book Ramsey gap in the recent literature.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 77 <= R(B19, B19) <= 78 and the exact neighboring almost-diagonal value R(B18, B19) = 75; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)) as a recent family-status and citation check; plus bounded 2026-04-14 exact-statement, family-level, canonical-source, and recent-status web checks that did not reveal a later exact determination.
- 2025 EJC Lemma 1 for the one-step diagonal interval and nearby exact benchmark, Wesley (2026) for recent book-Ramsey family status, and bounded 2026-04-14 exact-statement and status searches.
- artifacts/r-b19-b19-diagonal-book-ramsey/record.md
- artifacts/r-b19-b19-diagonal-book-ramsey/status.json
