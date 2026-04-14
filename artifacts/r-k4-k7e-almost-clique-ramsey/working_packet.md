# Working Packet: On the Exact Value of R(K4, K7-e)

- slug: `r-k4-k7e-almost-clique-ramsey`
- title: Determine the exact value of R(K4, K7-e)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `46`
- single-solve-to-paper fraction: `0.5`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red K4 or a blue K7-e.

## novelty_notes
- frontier basis: The checked sources only pin the parameter inside the interval 37 <= R(K4, K7-e) <= 52.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the value were settled, the theorem would still headline a standard Ramsey note. But the remaining interval is far from tiny, so too much of the eventual paper still resides in the search rather than the single solve.
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
- search-heavy: True
- certificate compactness: low
- exact gap from source: moderate
- assessment: Not lane-eligible. The family is fine, but the residual computational burden is too large to satisfy the one-shot paper test.

## likely_paper_shape
- note title: On the Exact Value of R(K4, K7-e)
- hypothetical title: The Exact Value of R(K4, K7-e)
- paper shape: A computational exact-value note for a classical-versus-almost-clique Ramsey number.
- publication if solved: An exact value for R(K4, K7-e) would still yield a legitimate short note in a classical family, but not in the strict micro-paper sense targeted here.
- minimal artifact requirements: A decisive lower-bound coloring or exhaustive upper-bound elimination with reproducible verification.

## hypothetical_abstract
We determine the Ramsey number R(K4, K7-e). The bounded literature audit for this run leaves the parameter between 37 and 52. Our result closes that interval in the classical one-edge Ramsey family.

## single_solve_explanation
An exact solve would still give the title theorem of a short note. The family anchor is clear and the statement is stable. The target misses the micro-paper lane because the gap is still large enough that the final solve would likely be a substantial computational campaign rather than one compact decisive argument.

## broader_theorem_nonimplication
The lower-bound construction source and the older upper-bound source leave a genuine interval, and the bounded recent search did not uncover a theorem collapsing the case to an immediate corollary.

## literature_gap
The sources checked here expose only 37 <= R(K4, K7-e) <= 52.

## transfer_kit
- lemma: The bounded search recovered an explicit lower-bound construction showing R(K4, K7-e) >= 37.
- lemma: The older upper-bound paper surfaced in search gives R(K4, K7-e) <= 52.
- lemma: The one-edge Ramsey literature supplies monotonicity constraints from neighboring complete and almost-complete cases.
- toy example: Smaller exact almost-clique Ramsey values in the surrounding literature serve as the intended proof style if this interval were ever closed sharply.
- known obstruction: Both endpoints appear to require heavy computation or structured search, and there is no evidence from the bounded audit that a small human-readable reduction already exists.
- prior-work stop sentence: The bounded audit for this run found only 37 <= R(K4, K7-e) <= 52.
- recommended first attack: Attempt to improve the upper side using triangle-count and gluing inequalities before investing in a full lower-bound search.
- paper if solved: The paper would be a standard exact-value note in a classical almost-clique Ramsey family.

## bounded_source_list
- Greg Exoo's lower-bound constructions page for one-edge Ramsey numbers, surfaced in bounded search and reporting R(K4, K7-e) > 36; the 1998 European Journal of Combinatorics upper-bound paper surfaced in bounded search with R(K4, K7-e) <= 52; and bounded exact-statement, alternate-notation, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact value.
- Greg Exoo lower-bound constructions, an older upper-bound source surfaced by bounded search, and bounded 2026-04-14 exact-term, alternate-notation, outside-source, and recent-status checks.
- artifacts/r-k4-k7e-almost-clique-ramsey/record.md
- artifacts/r-k4-k7e-almost-clique-ramsey/status.json
