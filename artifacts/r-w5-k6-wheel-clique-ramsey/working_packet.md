# Working Packet: The Exact Value of R(W5, K6)

- slug: `r-w5-k6-wheel-clique-ramsey`
- title: Determine the exact value of R(W5, K6)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `54`
- single-solve-to-paper fraction: `0.57`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red wheel W5 or a blue K6.

## novelty_notes
- frontier basis: Current public sources leave this wheel-versus-clique Ramsey number at 33 <= R(W5, K6) <= 36. The family is classical, but the solve-to-publication distance is still longer than the best surviving slots.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A future exact solve would still produce a legitimate note, but the remaining interval is wide enough that the proof could become structurally broader than the final theorem statement. That makes the target too packaging-heavy for the strict lane.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: high
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail. Real frontier, but not close enough to one-shot publication mode after the bounded curation audit.

## likely_paper_shape
- note title: The Exact Value of R(W5, K6)
- hypothetical title: The Exact Value of R(W5, K6)
- paper shape: A wheel-versus-clique exact-value note, but not a clean micro-paper at the current gap width.
- publication if solved: An exact determination of R(W5, K6) would be publishable as a classical wheel-versus-clique note, but it is too far from one-shot paper readiness for the strict lane.
- minimal artifact requirements: A short extremal coloring or a forcing proof collapsing the interval 33-36 to a single value.

## hypothetical_abstract
We determine the Ramsey number R(W5, K6). Previous work bounded this number between 33 and 36. Our result closes the remaining finite gap for this small wheel-versus-clique pair.

## single_solve_explanation
This fails the strict micro-paper test because the gap is still several values wide and the likely proof is not obviously local. Even if the result is publishable, the route from exact solve to short-note packet is longer and less certain than in the one-step slots above.

## broader_theorem_nonimplication
Known wheel results and deletion-based variants do not settle the full clique endpoint K6. The bounded audit did not uncover a broader theorem that already forces 33, 34, 35, or 36.

## literature_gap
Current public sources stop at 33 <= R(W5, K6) <= 36.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 7, gives the upper bound R(W5, K6) <= 36.
- lemma: The same source records the lower bound R(W5, K6) >= 33.
- lemma: The 2021 paper notes that some wheel upper bounds from the same table were later shown tight, which confirms the family is active but does not settle W5 versus K6.
- lemma: Older wheel-versus-almost-clique results for K6 with deleted stars show that weakening the blue clique target changes the value, so those broader-looking theorems do not imply the exact W5 versus K6 endpoint.
- toy example: The exact wheel values R(W5, W7) = 15 and R(W5, W9) = 18 from the 2024 books-and-wheels paper show the local family is paper-legible, but they do not collapse the clique side.
- known obstruction: Wheel avoidance interacts poorly with dense clique-avoiding multipartite constructions, so the remaining interval can hide several qualitatively different critical graph types.
- prior-work stop sentence: Current sources stop at 33 <= R(W5, K6) <= 36.
- recommended first attack: Start by testing whether every near-extremal lower-bound construction already contains a forced W5 once the blue graph is kept K6-free at order 33 or above; if not, the target is probably too wide for the lane.
- paper if solved: The paper would be a classical wheel-versus-clique exact-value note, but it is not currently close enough to one-shot publication mode.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 7, giving 33 <= R(W5, K6) <= 36; together with bounded 2026-04-14 recent-status web checks that did not reveal a later exact determination.
- 2021 Lidicky-Pfender Theorem 7, older wheel-versus-clique background cited there, and bounded 2026-04-14 recent-status web checks.
- artifacts/r-w5-k6-wheel-clique-ramsey/record.md
- artifacts/r-w5-k6-wheel-clique-ramsey/status.json
