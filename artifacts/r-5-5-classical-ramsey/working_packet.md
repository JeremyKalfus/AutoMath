# Working Packet: The Exact Value of R(5,5)

- slug: `r-5-5-classical-ramsey`
- title: Determine the exact value of R(5,5)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `64`
- single-solve-to-paper fraction: `0.58`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic K_5.

## novelty_notes
- frontier basis: Current public sources leave the diagonal classical Ramsey number R(5,5) in the interval 43 <= R(5,5) <= 46.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: Any exact solve would obviously be a headline theorem. It is not near-paper in the micro-paper sense because the decisive computational packet would still be large, difficult to compress, and expensive to verify.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: none
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: moderate
- assessment: Fail for the lane. The theorem is too important and too computation-heavy to behave like a small one-shot note.

## likely_paper_shape
- note title: The Exact Value of R(5,5)
- hypothetical title: The Exact Value of R(5,5)
- paper shape: A substantial computational exact-value paper around a famous diagonal classical Ramsey number.
- publication if solved: An exact determination of R(5,5) would be highly publishable, but it is too heavy and search-driven for the strict micro-paper lane.
- minimal artifact requirements: Either a full census or decisive nonexistence proof for all (5,5,42-45)-graphs, or a matching lower-bound construction at the exact frontier.

## hypothetical_abstract
We determine the diagonal classical Ramsey number R(5,5). Existing public sources place this famous parameter in the interval 43 <= R(5,5) <= 46. Our result closes the remaining gap for the smallest unresolved diagonal complete-graph Ramsey number after R(4,4).

## single_solve_explanation
This problem would unquestionably yield a paper if solved exactly, but it fails the micro-paper test for the opposite reason from a weak curiosity: the packet is too large, not too small. The likely solve requires a heavy computational campaign and a bulky verification layer. That makes the solve-to-paper distance longer than desired even though the title theorem is strong.

## broader_theorem_nonimplication
No broader published theorem settles the exact diagonal value; the literature still reports only separated lower and upper bounds. The barrier is computational scale, not theorem-slice instability.

## literature_gap
Current public sources stop at 43 <= R(5,5) <= 46.

## transfer_kit
- lemma: Exoo (1989) gives the lower-bound construction proving R(5,5) >= 43.
- lemma: Angeltveit-McKay (2018) prove the published upper bound R(5,5) <= 48.
- lemma: Current status surfaces report the improved upper bound R(5,5) <= 46.
- lemma: Recent exact work on nearby missing-edge variants, such as the exact result for R(K5, K5-e), demonstrates the relevant census-and-gluing methodology at the same local scale.
- toy example: The exact value R(4,4) = 18 is the nearest solved diagonal complete-graph benchmark, while R(K5, K5-e) = 30 gives a methodologically adjacent exact computation.
- known obstruction: The candidate graph census is extremely large, and verifying nonextendability across all surviving cases is the dominant obstacle.
- prior-work stop sentence: Current public sources stop at 43 <= R(5,5) <= 46.
- recommended first attack: Adapt recent missing-edge census and gluing techniques to the diagonal case, beginning with a full structural catalog of surviving (5,5,42)-graphs.
- paper if solved: The paper would be a substantial computational breakthrough note rather than a strict micro-paper.

## bounded_source_list
- Geoffrey Exoo, "A Lower Bound for R(5,5)" (Journal of Graph Theory 13 (1989)) for the lower bound R(5,5) >= 43; Vigleik Angeltveit and Brendan McKay, "R(5,5) <= 48" (Journal of Graph Theory 89 (2018)) as the last published upper-bound paper before the currently reported tighter bound; together with bounded 2026-04-14 survey-status checking that reports the current upper bound 46.
- Exoo (1989), Angeltveit-McKay (2018), and bounded 2026-04-14 survey/status checking.
- artifacts/r-5-5-classical-ramsey/record.md
- artifacts/r-5-5-classical-ramsey/status.json
