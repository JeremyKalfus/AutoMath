# Working Packet: The Exact Value of R(B13, B13)

- slug: `r-b13-b13-diagonal-book-ramsey`
- title: Determine the exact value of R(B13, B13)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `79`
- single-solve-to-paper fraction: `0.78`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B13.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 53 <= R(B13, B13) <= 54. This is already a one-step exact frontier in a standard family with exact neighboring book values.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 53 versus 54 is settled, the result already has the shape of a short exact-value paper. The only real residue is the critical coloring or forcing proof and a short comparison with nearby diagonal and almost-diagonal cases.
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
- assessment: Pass. This is a stable one-step diagonal book gap with low editorial residue and a clear short-note endpoint if solved.

## likely_paper_shape
- note title: The Exact Value of R(B13, B13)
- hypothetical title: The Exact Value of R(B13, B13)
- paper shape: A one-theorem exact-value note for a diagonal book Ramsey number.
- publication if solved: An exact determination of R(B13, B13) would read as the title theorem of a short note because the public frontier is already a one-step diagonal book Ramsey gap.
- minimal artifact requirements: Either an explicit 53-vertex coloring avoiding monochromatic B13 or a compact proof that every 54-vertex coloring forces B13.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B13, B13). Previous work placed this number in the interval 53 <= R(B13, B13) <= 54. Our result closes the remaining one-step gap for a standard diagonal book pair.

## single_solve_explanation
This target passes the 70-90% paper test because the public literature already isolates a single unresolved endpoint. Once the exact value is known, most of the paper is already determined: theorem statement, brief family context, and the main extremal or forcing artifact. No feeder ladder is needed.

## broader_theorem_nonimplication
The known diagonal-book theorem only yields the interval 4n + 1 <= R(B_n, B_n) <= 4n + 2, and the recent 2026 lower-bound paper does not close the case n = 13. Exact neighboring values such as R(B12, B13) = 51 do not decide the diagonal endpoint.

## literature_gap
Current public sources stop at 53 <= R(B13, B13) <= 54.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 53 <= R(B13, B13) <= 54.
- lemma: The same lemma gives the exact neighboring almost-diagonal value R(B12, B13) = 51.
- lemma: The same paper records the exact smaller diagonal benchmark R(B8, B8) = 33.
- lemma: Wesley (2026) gives recent book-Ramsey lower-bound progress but does not report an exact closure for B13.
- toy example: The exact neighboring almost-diagonal case R(B12, B13) = 51 is the closest solved model for a short proof packet in the same corridor.
- known obstruction: The diagonal family admits many structured lower-bound colorings, so the main difficulty is ruling out the last 53-vertex critical patterns without turning the note into a family-wide project.
- prior-work stop sentence: Current sources stop at 53 <= R(B13, B13) <= 54.
- recommended first attack: Analyze the Lemma 1 lower-bound construction at order 53 and test whether any extension to 54 vertices inevitably creates a monochromatic B13 through common-neighborhood growth around candidate spines.
- paper if solved: The paper would be a short exact-value note settling one diagonal book Ramsey number.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 53 <= R(B13, B13) <= 54; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), used as a bounded recent-status and citation check that did not report an exact closure for B13; and bounded 2026-04-14 exact-statement and alternate-notation web checks that did not reveal a later exact determination.
- 2025 EJC paper Lemma 1 for the one-step interval and nearby exact values, 2026 Wesley book-Ramsey paper as a recent-status check, and bounded 2026-04-14 exact-statement, synonym, and citation searches.
- artifacts/r-b13-b13-diagonal-book-ramsey/record.md
- artifacts/r-b13-b13-diagonal-book-ramsey/status.json
