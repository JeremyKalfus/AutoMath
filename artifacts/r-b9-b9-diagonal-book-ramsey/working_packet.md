# Working Packet: The Exact Value of R(B9, B9)

- slug: `r-b9-b9-diagonal-book-ramsey`
- title: Determine the exact value of R(B9, B9)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.78`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B9.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 37 <= R(B9, B9) <= 38. The surrounding book family already has several exact neighboring values, so the remaining gap is sharply localized.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 37 versus 38 is settled, the result already reads like the title theorem of a short exact-value note. The remaining work is mainly to present the extremal coloring or forcing proof and compare it with nearby exact book values such as R(B8, B8) and R(B8, B9).
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass, but behind the top slot. The family anchor is excellent and the gap is one step, though there is a moderate chance that a successful proof suggests a broader diagonal-book pattern.

## likely_paper_shape
- note title: The Exact Value of R(B9, B9)
- hypothetical title: The Exact Value of R(B9, B9)
- paper shape: A one-theorem exact-value note for a diagonal book Ramsey number.
- publication if solved: An exact determination of R(B9, B9) would plausibly support a short note because the diagonal book family is standard and the current public interval is one step wide.
- minimal artifact requirements: Either a 37-vertex coloring of K_37 avoiding monochromatic B9, or a compact proof that every 38-vertex coloring forces B9.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B9, B9). Previous work placed this number in the interval 37 <= R(B9, B9) <= 38. Our result closes the remaining one-step gap in the diagonal book family.

## single_solve_explanation
This target passes the paper test because the frontier is already a one-step exact-value problem in a standard family with clear notation and nearby solved cases. After the solve, the note mostly needs the witness or forcing argument and a short comparison with adjacent book numbers. The editorial residue is small relative to the solve.

## broader_theorem_nonimplication
Lemma 1 sandwiches all diagonal book values B_n between 4n + 1 and 4n + 2 for 4 <= n <= 21, but it does not decide the endpoint for n = 9. The bounded audit did not reveal a broader published theorem that already fixes 37 or 38 for this exact n.

## literature_gap
Current public sources stop at 37 <= R(B9, B9) <= 38.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2024), Lemma 1, gives 37 <= R(B9, B9) <= 38.
- lemma: The same source gives the exact off-diagonal neighboring value R(B8, B9) = 35.
- lemma: The same source gives the exact smaller diagonal value R(B8, B8) = 33.
- lemma: The same source records multiple exact near-diagonal book values, showing that short exact endpoint notes are already the standard publication shape in this family.
- toy example: The exact neighboring diagonal case R(B8, B8) = 33 is the closest worked model for how a diagonal book exact-value proof packet can look.
- known obstruction: Book-avoiding colorings can remain highly structured and polycirculant, so an exact proof must eliminate the last 37-vertex critical patterns without expanding into a broad family campaign.
- prior-work stop sentence: Current sources stop at 37 <= R(B9, B9) <= 38.
- recommended first attack: Use the exact B8/B8 and B8/B9 extremal patterns as local templates, then test whether any 37-vertex candidate can preserve the necessary spine-neighborhood restrictions in both colors.
- paper if solved: The paper would be a short exact-value note for a diagonal book Ramsey number with immediate comparison to neighboring exact book values.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (2024 preprint), Lemma 1 giving 4n + 1 <= R(B_n, B_n) <= 4n + 2 for 4 <= n <= 21, hence 37 <= R(B9, B9) <= 38; together with bounded 2026-04-14 recent-status web checks that did not reveal a later exact determination.
- 2024 books-wheels-generalizations paper for Lemma 1 and nearby exact book values, plus bounded 2026-04-14 recent-status web checks.
- artifacts/r-b9-b9-diagonal-book-ramsey/record.md
- artifacts/r-b9-b9-diagonal-book-ramsey/status.json
