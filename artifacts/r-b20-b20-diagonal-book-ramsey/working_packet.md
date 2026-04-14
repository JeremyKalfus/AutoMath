# Working Packet: The Exact Value of R(B20, B20)

- slug: `r-b20-b20-diagonal-book-ramsey`
- title: Determine the exact value of R(B20, B20)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `73`
- single-solve-to-paper fraction: `0.74`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B20.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 81 <= R(B20, B20) <= 82. The remaining frontier is again a single endpoint in a standard family.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 81 versus 82 is settled, the note already has a natural title theorem and a clean comparison with the recently sharpened diagonal-book record. The remaining work is mostly polishing the decisive witness or forcing proof.
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
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Pass. The theorem slice is stable and paper-shaped, though the certificate risk is slightly higher than for B19.

## likely_paper_shape
- note title: The Exact Value of R(B20, B20)
- hypothetical title: The Exact Value of R(B20, B20)
- paper shape: A one-theorem exact-value note for a diagonal book Ramsey number at the edge of the strongest current micro-paper lane.
- publication if solved: An exact determination of R(B20, B20) would still plausibly support a short note because the public frontier remains a one-step diagonal book Ramsey gap.
- minimal artifact requirements: Either an explicit 81-vertex coloring avoiding monochromatic B20 or a compact proof that every 82-vertex coloring forces B20.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B20, B20). Previous work left this number in the interval 81 <= R(B20, B20) <= 82. Our result closes the remaining one-step gap for this diagonal book pair.

## single_solve_explanation
This target still meets the 70% paper threshold because one clean solve would already determine the exact value in a family with an established literature frame. The solve would contribute the title theorem, the main comparison, and the decisive artifact. The main risk is only that the certificate may be a little less compact than for B19.

## broader_theorem_nonimplication
The broad diagonal-book theory still leaves a one-step interval and does not fix the endpoint at n = 20. Exact almost-diagonal information nearby does not settle the diagonal slice.

## literature_gap
Current public sources stop at 81 <= R(B20, B20) <= 82.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 81 <= R(B20, B20) <= 82.
- lemma: The same lemma gives the exact neighboring almost-diagonal value R(B19, B20) = 79.
- lemma: The 2025 paper's method counts copies of B_k through common neighborhoods of candidate spine edges.
- lemma: Wesley (2026) confirms that recent lower-bound constructions continue to sharpen book-Ramsey gaps without reporting an exact closure for B20.
- toy example: The exact neighboring almost-diagonal case R(B19, B20) = 79 is the closest solved benchmark for the intended theorem shape.
- known obstruction: The diagonal-book critical graphs at this size can still carry substantial symmetry, so an upper-bound proof must exclude a structured candidate class rather than a single sporadic witness.
- prior-work stop sentence: Current public sources stop at 81 <= R(B20, B20) <= 82.
- recommended first attack: Use common-neighborhood forcing on candidate spine edges, anchored by the exact R(B19, B20) = 79 comparison point, to show that every 81-vertex near-extremal coloring collapses when extended.
- paper if solved: The paper would be a short exact-value note settling another one-step diagonal book Ramsey gap.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 81 <= R(B20, B20) <= 82; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)) as a recent family-status and citation check; and bounded 2026-04-14 exact-statement, alternate-notation, canonical-source, and recent-status web checks that did not reveal a later exact determination.
- 2025 EJC Lemma 1 for the one-step interval and exact almost-diagonal comparison point, 2026 Wesley for recent family context, and bounded 2026-04-14 exact-statement, synonym, and status searches.
- artifacts/r-b20-b20-diagonal-book-ramsey/record.md
- artifacts/r-b20-b20-diagonal-book-ramsey/status.json
