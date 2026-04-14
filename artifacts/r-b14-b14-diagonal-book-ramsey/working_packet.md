# Working Packet: The Exact Value of R(B14, B14)

- slug: `r-b14-b14-diagonal-book-ramsey`
- title: Determine the exact value of R(B14, B14)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `81`
- single-solve-to-paper fraction: `0.79`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B14.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 57 <= R(B14, B14) <= 58. The lower endpoint is supported by a recent explicit construction, so the remaining frontier is a clean one-step exact-value problem.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 57 versus 58 is settled, the paper already has its title theorem and its natural literature comparison. What remains is mainly the critical construction or forcing argument and a short placement beside the nearby diagonal and almost-diagonal book values.
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
- assessment: Pass. This is one of the cleanest untouched recent diagonal book gaps because the lower endpoint is freshly constructed and the upper endpoint is already established.

## likely_paper_shape
- note title: The Exact Value of R(B14, B14)
- hypothetical title: The Exact Value of R(B14, B14)
- paper shape: A one-theorem exact-value note for a diagonal book Ramsey number with a fresh recent lower-bound construction.
- publication if solved: An exact determination of R(B14, B14) would read as the title theorem of a short note because the public frontier is already a one-step diagonal book Ramsey gap.
- minimal artifact requirements: Either an explicit 57-vertex coloring avoiding monochromatic B14 or a compact proof that every 58-vertex coloring forces B14.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B14, B14). Previous work left this number in the interval 57 <= R(B14, B14) <= 58. Our result closes the remaining one-step gap for a diagonal book pair with a recent explicit lower-bound construction.

## single_solve_explanation
This target passes the 70-90% paper test because the public frontier is one endpoint wide and the family is already publication-legible. A successful solve would already provide the title theorem, the main literature comparison, and the main artifact. The remaining work is just compact write-up rather than a second theorem campaign.

## broader_theorem_nonimplication
The available broad diagonal-book theorem only gives the one-step interval 4n + 1 <= R(B_n, B_n) <= 4n + 2, and the recent 2026 lower-bound paper improves constructions without fixing the diagonal endpoint at n = 14. Nearby exact values such as R(B13, B14) = 55 do not determine R(B14, B14).

## literature_gap
Current public sources stop at 57 <= R(B14, B14) <= 58.

## transfer_kit
- lemma: Wesley (2026), Appendix A / lower-bound table, gives the explicit lower bound R(B14, B14) >= 57.
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives the upper bound R(B14, B14) <= 58.
- lemma: The same 2025 lemma gives the exact neighboring almost-diagonal value R(B13, B14) = 55.
- lemma: The same family already contains exact smaller diagonal values such as R(B8, B8) = 33.
- toy example: The exact neighboring almost-diagonal case R(B13, B14) = 55 is the nearest solved benchmark for how the forcing side of the packet can look.
- known obstruction: Recent lower-bound constructions show that highly structured diagonal critical graphs persist at this size, so any upper-bound proof must eliminate a small but nontrivial family of 57-vertex candidates.
- prior-work stop sentence: Current sources stop at 57 <= R(B14, B14) <= 58.
- recommended first attack: Use the 2026 block-circulant lower-bound witness as the base critical template and analyze whether any one-vertex extension necessarily creates a monochromatic B14 by common-neighborhood counting on the spine.
- paper if solved: The paper would be a short exact-value note settling a recently sharpened diagonal book Ramsey gap.

## bounded_source_list
- William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), Appendix A / Table 3 giving the diagonal lower bound R(B14, B14) >= 57; together with Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving R(B14, B14) <= 58; and bounded 2026-04-14 exact-statement, alternate-notation, and recent-status web checks that did not reveal a later exact determination.
- 2026 Wesley Appendix A / lower-bound table, 2025 EJC Lemma 1 for the upper bound and family context, and bounded 2026-04-14 exact-statement, synonym, and citation-status searches.
- artifacts/r-b14-b14-diagonal-book-ramsey/record.md
- artifacts/r-b14-b14-diagonal-book-ramsey/status.json
