# Working Packet: The Exact Value of R(K5-e, K6-e)

- slug: `r-k5e-k6e-almost-clique-ramsey`
- title: Determine the exact value of R(K5-e, K6-e)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `52`
- single-solve-to-paper fraction: `0.58`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red K5-e or a blue K6-e.

## novelty_notes
- frontier basis: The 2021 SDP paper leaves this almost-clique Ramsey number at 31 <= R(K5-e, K6-e) <= 38. The family anchor is strong, but the solve-to-paper distance is materially longer than the top candidates.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A future exact solve would still matter, but the present gap is broad enough that the note would likely need more than one decisive ingredient or a heavy computational packet. That breaks the one-shot lane.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: high
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: low
- exact gap from source: broad
- assessment: Fail. Strong family anchor, but the frontier slice is too wide and too packaging-heavy for the strict micro-paper lane.

## likely_paper_shape
- note title: The Exact Value of R(K5-e, K6-e)
- hypothetical title: The Exact Value of R(K5-e, K6-e)
- paper shape: A classical almost-clique exact-value note, but not a true one-shot micro-paper at the current gap width.
- publication if solved: An exact determination would be publishable in a classical almost-clique table, but it is too far from one-shot paper readiness for the strict micro-paper objective.
- minimal artifact requirements: A substantial extremal construction or forcing argument compressing the interval 31-38 to a single value.

## hypothetical_abstract
We determine the Ramsey number R(K5-e, K6-e). Previous work bounded this number between 31 and 38. Our result closes the remaining finite gap in the two-color almost-clique family.

## single_solve_explanation
This fails the strict paper-fraction test because the current interval is still too broad. Even if progress is real, the route from solve to paper is not obviously a single short packet.

## broader_theorem_nonimplication
General almost-clique monotonicity and inclusion bounds do not settle the exact endpoint, but the bounded audit also did not indicate a compact one-theorem story at the current scale.

## literature_gap
Current public sources stop at 31 <= R(K5-e, K6-e) <= 38.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 7, gives the upper bound R(K5-e, K6-e) <= 38.
- lemma: The same theorem records the lower bound 31 <= R(K5-e, K6-e).
- lemma: The Dynamic Survey places the problem inside the classical almost-complete graph Ramsey tables.
- lemma: Subgraph monotonicity supplies immediate comparison bounds from complete-graph Ramsey numbers without determining the exact value.
- toy example: The exact smaller almost-clique values in the survey and the 2021 paper provide local calibration points, but none collapse this interval directly.
- known obstruction: Both forbidden graphs are dense enough that extremal colorings can remain highly structured over a long interval, which makes a compact exact proof unlikely.
- prior-work stop sentence: Current sources stop at 31 <= R(K5-e, K6-e) <= 38.
- recommended first attack: Before any search, inspect whether the 2021 SDP certificate isolates a narrow class of near-extremal degree profiles; otherwise this target is too wide for the lane.
- paper if solved: The paper would be an exact-value almost-clique Ramsey note, but it is not currently close enough to one-shot publication mode.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 7, which gives 31 <= R(K5-e, K6-e) <= 38; together with the 2024 revision of Radziszowski's Dynamic Survey "Small Ramsey Numbers" as family context and bounded 2026-04-14 recent-status web checks during curation that did not reveal a later exact closure.
- 2021 Lidicky-Pfender Theorem 7, Dynamic Survey family context, and bounded 2026-04-14 recent-status web checks.
- artifacts/r-k5e-k6e-almost-clique-ramsey/record.md
- artifacts/r-k5e-k6e-almost-clique-ramsey/status.json
