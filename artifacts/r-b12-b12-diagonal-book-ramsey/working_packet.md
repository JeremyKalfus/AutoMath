# Working Packet: The Exact Value of R(B12, B12)

- slug: `r-b12-b12-diagonal-book-ramsey`
- title: Determine the exact value of R(B12, B12)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `82`
- single-solve-to-paper fraction: `0.8`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B12.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 49 <= R(B12, B12) <= 50. That is already a one-step finite frontier in a standard family with exact neighboring book values and explicit lower-bound constructions.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 49 versus 50 is settled, the note already has its title theorem, the core literature comparison, and a compact frontier claim. What remains is mainly the extremal coloring or forcing proof, plus a brief comparison with nearby diagonal and almost-diagonal book values.
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
- assessment: Pass. This is a clean one-step diagonal book Ramsey gap with a strong family anchor, low editorial residue, and no detected broader theorem that already collapses the endpoint.

## likely_paper_shape
- note title: The Exact Value of R(B12, B12)
- hypothetical title: The Exact Value of R(B12, B12)
- paper shape: A one-theorem exact-value note for a diagonal book Ramsey number.
- publication if solved: An exact determination of R(B12, B12) would read as the title theorem of a short note because the public frontier is already a one-step diagonal book Ramsey gap.
- minimal artifact requirements: Either an explicit 49-vertex coloring avoiding monochromatic B12 or a compact proof that every 50-vertex coloring forces B12.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B12, B12). Previous work placed this number in the interval 49 <= R(B12, B12) <= 50. Our result closes the remaining one-step gap for a standard diagonal book pair.

## single_solve_explanation
This target passes the 70-90% paper test because the public frontier is already one endpoint wide in a named classical family. Once the exact value is known, the note mostly needs the extremal coloring or forcing argument and a short comparison with nearby exact book values. There is no feeder ladder between the solve and the paper-shaped claim.

## broader_theorem_nonimplication
The currently available broad diagonal-book result only sandwiches R(B_n, B_n) between 4n + 1 and 4n + 2 for 4 <= n <= 21. Exact off-diagonal values such as R(B11, B12) = 47 and smaller diagonal values such as R(B8, B8) = 33 do not force the endpoint for n = 12.

## literature_gap
Current public sources stop at 49 <= R(B12, B12) <= 50.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 49 <= R(B12, B12) <= 50.
- lemma: The same lemma gives the exact neighboring almost-diagonal value R(B11, B12) = 47.
- lemma: The same paper records the exact smaller diagonal benchmark R(B8, B8) = 33.
- lemma: Wesley (2026) gives recent lower-bound progress and exact lower constructions for nearby diagonal book cases, but does not report an exact closure for B12.
- toy example: The exact neighboring diagonal case R(B8, B8) = 33 is a direct model for how a short diagonal-book exact-value note can look.
- known obstruction: Diagonal book critical graphs can remain highly structured and polycirculant, so any upper-bound proof must eliminate the last 49-vertex critical family without expanding into a broader campaign.
- prior-work stop sentence: Current sources stop at 49 <= R(B12, B12) <= 50.
- recommended first attack: Start from the Lemma 1 lower-bound construction at order 49 and test whether every one-vertex extension forces a monochromatic B12, while tracking common-neighborhood restrictions along candidate spine edges.
- paper if solved: The paper would be a short exact-value note settling one diagonal book Ramsey number.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 49 <= R(B12, B12) <= 50; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), used as a bounded recent-status and citation check that did not report an exact closure for B12; and bounded 2026-04-14 exact-statement and alternate-notation web checks that did not reveal a later exact determination.
- 2025 EJC paper Lemma 1 for the one-step interval and nearby exact values, 2026 Wesley book-Ramsey lower-bound paper as a recent-status check, and bounded 2026-04-14 exact-statement, synonym, and citation searches.
- artifacts/r-b12-b12-diagonal-book-ramsey/record.md
- artifacts/r-b12-b12-diagonal-book-ramsey/status.json
