# Working Packet: The Exact Value of R(B24, B24)

- slug: `r-b24-b24-diagonal-book-ramsey`
- title: Determine the exact value of R(B24, B24)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `60`
- single-solve-to-paper fraction: `0.65`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B24.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 97 <= R(B24, B24) <= 98. The theorem statement remains stable, but the likely witness or forcing packet is no longer especially compact.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 97 versus 98 is settled, the result still has a real paper shape because the family and theorem statement are clean. It misses the strict lane because too much editorial compression and certificate cleanup may remain after the solve.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: none
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: low
- exact gap from source: small
- assessment: Outside the strict lane. The family anchor is real, but the expected solve-to-paper fraction is too low for the current objective.

## likely_paper_shape
- note title: The Exact Value of R(B24, B24)
- hypothetical title: The Exact Value of R(B24, B24)
- paper shape: A one-theorem exact-value note candidate with clear family anchor but too much residual packaging risk for the strict lane.
- publication if solved: An exact determination of R(B24, B24) could still be written as a short note, but it no longer looks like the best micro-paper lane available.
- minimal artifact requirements: Either an explicit 97-vertex coloring avoiding monochromatic B24 or a forcing proof that every 98-vertex coloring contains B24.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B24, B24). Previously available results left this number in the interval 97 <= R(B24, B24) <= 98. Our result closes the remaining one-step gap for this larger diagonal book pair.

## single_solve_explanation
This target has a plausible one-theorem note shape, since the public frontier is still just one endpoint wide. It fails the strict micro-paper gate because the solve no longer looks close enough to a nearly finished packet; too much certificate compression and write-up risk remain. That makes it a backup queue slot rather than a preferred live target.

## broader_theorem_nonimplication
The available broad diagonal-book theorem still stops at the one-step interval and does not fix the endpoint at n = 24. The main concern is not prior implication but diminishing packet compactness.

## literature_gap
Current public sources stop at 97 <= R(B24, B24) <= 98.

## transfer_kit
- lemma: The classical diagonal-book bounds summarized in Wesley (2026) leave R(B24, B24) in the one-step interval 97 <= R(B24, B24) <= 98.
- lemma: Wesley (2026) identifies block-circulant and Paley-type graphs as the key lower-bound witness architecture for diagonal book problems.
- lemma: The 2025 paper's scoring rule counts books through common neighborhoods on a spine edge, giving the natural forcing template for any upper-bound attempt.
- lemma: Recent smaller book-Ramsey exact values show that the family is mathematically coherent even when the later diagonal cases become harder to package.
- toy example: The exact neighboring family benchmark most useful here is the recent R(B19, B20) = 79 almost-diagonal case, which shows the intended note shape even though it is smaller.
- known obstruction: The main obstruction is that the witness family at this size is likely broad enough that the final certificate becomes less publication-compact than the strict lane wants.
- prior-work stop sentence: Current public sources stop at 97 <= R(B24, B24) <= 98.
- recommended first attack: Probe whether the known diagonal lower-bound architectures on 97 vertices admit only a tiny set of extension types, then try to force a B24 on every such extension by common-neighborhood counting.
- paper if solved: The paper would still be an exact-value note, but it is no longer a top-priority micro-paper target under the current lane.

## bounded_source_list
- Classical diagonal book Ramsey bounds summarized in William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), introduction, together with Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)) for recent family context; and bounded 2026-04-14 exact-statement, alternate-notation, canonical-source, and recent-status web checks that did not reveal a later exact determination beyond the interval 97 <= R(B24, B24) <= 98.
- Classical diagonal-book interval summarized in Wesley (2026), recent family context from the 2025 EJC paper, and bounded 2026-04-14 exact-statement, synonym, and status searches.
- artifacts/r-b24-b24-diagonal-book-ramsey/record.md
- artifacts/r-b24-b24-diagonal-book-ramsey/status.json
