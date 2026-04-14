# Working Packet: The Exact Value of R(B6, B6)

- slug: `r-b6-b6-diagonal-book-ramsey`
- title: Determine the exact value of R(B6, B6)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `86`
- single-solve-to-paper fraction: `0.84`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 6-page book graph B6.

## novelty_notes
- frontier basis: Recent family results leave the diagonal case at 25 <= R(B6, B6) <= 26, and 25 = 3^2 + 4^2 so the standard exactness shortcut does not settle it. This makes the case a genuine open one-step slice inside an active family rather than a disguised corollary.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A clean exact solve would already provide the paper's theorem statement, proof, and computational or structural core. The remaining packaging would be a short family-context section and a compact certificate or contradiction record.
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
- assessment: Pass. This is a narrow, stable, current frontier slice with strong family anchor and low editorial overhead.

## likely_paper_shape
- note title: The Exact Value of R(B6, B6)
- hypothetical title: The Exact Value of R(B6, B6)
- paper shape: A one-theorem exact-value note for a diagonal book Ramsey number left at a one-step interval.
- publication if solved: An exact determination of R(B6, B6) would support a short note closing another one-step diagonal book Ramsey gap in the recent family table.
- minimal artifact requirements: Either a monochromatic-book-free coloring of K25 or a proof that every coloring of K26 forces a monochromatic B6, with a compact verification artifact.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B6, B6). The current literature leaves this parameter in the interval 25 <= R(B6, B6) <= 26. Our result closes one of the sharp one-step gaps remaining in the recent diagonal book Ramsey table.

## single_solve_explanation
The exact value itself would already be the paper's title theorem. The surrounding family story is cheap because recent papers have already organized the diagonal-book landscape into exact cases and one-step exceptions. After the solve, little remains beyond presenting the proof or extremal coloring cleanly.

## broader_theorem_nonimplication
The family theorem stops at 25 <= R(B6, B6) <= 26, and the usual exactness shortcut does not fire because 25 is a sum of two squares. No broader result located in the bounded audit closes the remaining step automatically.

## literature_gap
Current public sources stop at 25 <= R(B6, B6) <= 26.

## transfer_kit
- lemma: Pchelintsev, Rath, and Angeltveit (2025), Theorem 1, implies R(B6, B6) >= 25.
- lemma: The same theorem implies R(B6, B6) <= 26.
- lemma: The note after Theorem 1 gives exactness when 4n + 1 is not a sum of two squares, but this does not settle n = 6 because 25 = 3^2 + 4^2.
- lemma: The 2026 Wesley paper provides recent lower-bound constructions and confirms that book Ramsey lower-bound technology is still actively advancing.
- toy example: The exact solved case R(B8, B8) = 33 is a nearby diagonal-book benchmark showing the intended paper shape after an exact closure.
- known obstruction: A lower-bound proof needs a K25 coloring with no monochromatic B6, while an upper-bound proof must show that every K26 coloring already creates a B6 in one color.
- prior-work stop sentence: Current sources stop at 25 <= R(B6, B6) <= 26.
- recommended first attack: Begin from the recent constructive lower-bound templates for books and test whether a K25 critical coloring can survive the monochromatic common-neighbor constraints forced by the B6 target.
- paper if solved: The paper would be a short exact-value note on a diagonal book Ramsey number currently trapped in a one-step interval.

## bounded_source_list
- Maksim V. Pchelintsev, Peter Rath, and Sebastian Angeltveit, "New lower and upper bounds on Ramsey numbers" (Electronic Journal of Combinatorics 32(4) (2025), #P4.64), Theorem 1 and the note immediately following it, which imply 25 <= R(B6, B6) <= 26; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026), 114913) as independent recent family context and bounded 2026-04-14 web checks that did not reveal a later exact closure.
- 2025 EJC P4.64 Theorem 1 and note, the 2026 Wesley paper for independent family context, plus bounded 2026-04-14 exact-notation and recent-status web checks.
- artifacts/r-b6-b6-diagonal-book-ramsey/record.md
- artifacts/r-b6-b6-diagonal-book-ramsey/status.json
