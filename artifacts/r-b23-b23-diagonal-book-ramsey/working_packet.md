# Working Packet: The Exact Value of R(B23, B23)

- slug: `r-b23-b23-diagonal-book-ramsey`
- title: Determine the exact value of R(B23, B23)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `61`
- single-solve-to-paper fraction: `0.67`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B23.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 93 <= R(B23, B23) <= 94. The slice is stable, but the expected witness or forcing certificate is less compact than for smaller diagonal cases.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 93 versus 94 is settled, the result still has a plausible short-note title theorem. What keeps it out of the strict micro-paper lane is that the solve looks closer to 65-70% of the eventual packet than to a cleaner 70-90%.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: low
- exact gap from source: small
- assessment: Borderline but outside the strict lane. The theorem slice is stable, yet the projected certificate compactness is too weak for a confident micro-paper recommendation.

## likely_paper_shape
- note title: The Exact Value of R(B23, B23)
- hypothetical title: The Exact Value of R(B23, B23)
- paper shape: A one-theorem exact-value note candidate whose proof packet now looks less compact than the top queue slots.
- publication if solved: An exact determination of R(B23, B23) could still be written as a short note, but it is no longer clearly in the strongest micro-paper lane.
- minimal artifact requirements: Either an explicit 93-vertex coloring avoiding monochromatic B23 or a forcing proof that every 94-vertex coloring contains B23.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B23, B23). Previous work left this number in the interval 93 <= R(B23, B23) <= 94. Our result closes the remaining one-step gap for this diagonal book pair.

## single_solve_explanation
This target still has a legitimate paper shape because the public frontier is a one-step exact endpoint. However, it fails the strict micro-paper gate because the likely proof or certificate no longer looks compact enough to make the solve alone feel like 70-90% of the final note. More cleanup and presentation risk remain than in the top queue slots.

## broader_theorem_nonimplication
The broad diagonal-book theory does not decide the endpoint at n = 23, so a solve would still be a real theorem rather than a trivial corollary. The risk is not prior implication but weaker packet compactness.

## literature_gap
Current public sources stop at 93 <= R(B23, B23) <= 94.

## transfer_kit
- lemma: The classical diagonal-book bounds summarized in Wesley (2026) leave R(B23, B23) in the one-step interval 93 <= R(B23, B23) <= 94.
- lemma: Wesley (2026) points to Paley-type and block-circulant lower-bound architectures as the dominant witness style for diagonal book problems.
- lemma: The 2025 paper's counting setup for books turns forcing proofs into constraints on common neighborhoods of spine edges.
- lemma: Recent smaller exact book-Ramsey cases confirm that the family remains publication-legible even when the exact endpoint is not yet known.
- toy example: The recent exact almost-diagonal case R(B20, B21) = 83 is the nearest audited template for how a one-theorem note in this family reads.
- known obstruction: The key obstruction is packet bulk: the critical-coloring family is likely larger and less compressible than in the smaller diagonal cases.
- prior-work stop sentence: Current public sources stop at 93 <= R(B23, B23) <= 94.
- recommended first attack: Try to show that any 93-vertex near-extremal coloring modeled on the known diagonal lower-bound architectures forces a B23 after a one-vertex extension by common-neighborhood accumulation.
- paper if solved: The paper would be a short exact-value note, but the solve alone may not feel as close to a finished packet as in the stronger queue slots.

## bounded_source_list
- Classical diagonal book Ramsey bounds summarized in William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), introduction, together with Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)) for recent family context; and bounded 2026-04-14 exact-statement, alternate-notation, canonical-source, and recent-status web checks that did not reveal a later exact determination beyond the interval 93 <= R(B23, B23) <= 94.
- Classical diagonal-book interval summarized in Wesley (2026), recent family context from the 2025 EJC paper, and bounded 2026-04-14 exact-statement, synonym, and status searches.
- artifacts/r-b23-b23-diagonal-book-ramsey/record.md
- artifacts/r-b23-b23-diagonal-book-ramsey/status.json
