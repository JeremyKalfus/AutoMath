# Working Packet: The Exact Value of R(C4, K1,46)

- slug: `r-c4-k1-46-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,46)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `79`
- single-solve-to-paper fraction: `0.8`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,46.

## novelty_notes
- frontier basis: Current checked public sources support only 53 <= R(C4, K1,46) <= 54.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The literature already isolates a one-gap corridor, so a single forcing proof or a 53-vertex witness would supply the central theorem. After the solve, only a concise proof write-up and a comparison to the solved adjacent values are still needed.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. The corridor is one-gap, the narrative is still title-theorem sized, and the likely remaining post-solve work is editorial rather than mathematical.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,46)
- hypothetical title: The Exact Value of R(C4, K1,46)
- paper shape: A compact exact-value note closing a one-gap quadrilateral-star case immediately adjacent to an exact solved value.
- publication if solved: Closing R(C4, K1,46) would plausibly stand as the title theorem of a short note on one-gap quadrilateral-star Ramsey values.
- minimal artifact requirements: Either a 53-vertex C4-free graph with maximum degree at most 45, or a proof that every 53-vertex C4-free graph has a vertex of degree at least 46.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,46). Current checked public sources leave this parameter in the one-gap corridor 53 <= R(C4, K1,46) <= 54. The resulting certificate is compact enough that the exact closure would already form the core of a short note on quadrilateral-star Ramsey numbers.

## single_solve_explanation
This candidate passes the 70-90% paper test because one exact closure already gives the title theorem and almost all of the mathematical substance. After the solve, what remains is mainly the decisive witness or forcing contradiction, plus a short comparison to the nearby exact values R(C4, K1,45) and R(C4, K1,47). The family anchor keeps it from being just a tiny isolated curiosity.

## broader_theorem_nonimplication
The older C4-versus-star formulas do not cover n = 46, and the literature still records only the one-gap corridor. A broader theorem could exist, but the current checked sources do not imply this instance and do not advertise a general result settling it.

## literature_gap
Current checked sources stop at 53 <= R(C4, K1,46) <= 54.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,46) <= 54 in the small-values table.
- lemma: Boza 2024 Remark 13 yields the lower bound R(C4, K1,46) >= 46 + ceil(sqrt(46)) = 53.
- lemma: The 2014 star-wheel equivalence converts the same target into the wheel notation R(C4, W47).
- lemma: The 2015 and 2017 family papers leave n = 46 outside their closed exact regimes.
- toy example: The adjacent exact point R(C4, K1,45) = 53 gives the nearest solved model for a one-gap closure at this scale.
- known obstruction: Any 53-vertex witness must be C4-free with maximum degree at most 45, so the construction has very little slack against the extremal C4-free density limit.
- prior-work stop sentence: Current checked sources stop at the one-gap window 53 <= R(C4, K1,46) <= 54.
- recommended first attack: Start from the exact value at n = 45 and test whether the extremal-degree argument upgrades to force a degree-46 vertex on 53 vertices.
- paper if solved: The paper would be a short exact-value note closing the n = 46 quadrilateral-star residue.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table giving 53 <= R(C4, K1,46) <= 54 and Remark 13 giving the generic lower bound n + ceil(sqrt(n)); together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014) for the star-wheel equivalence surface; together with Wu, Sun, Zhang, and Radziszowski, "Ramsey Numbers of C4 versus Wheels and Stars" (Graphs and Combinatorics 31, 2015) and Zhang-Chen-Cheng, "Polarity Graphs and Ramsey Numbers for C4 versus Stars" (Discrete Mathematics 340, 2017) as older exact-family surfaces checked not to settle n = 46; plus bounded 2026-04-14 exact-term, wheel-notation, canonical-source, and recent-status searches that did not surface a later exact closure.
- Boza 2024 small-values table and Remark 13; Zhang-Broersma-Chen 2014 for the star-wheel equivalence; Wu-Sun-Zhang-Radziszowski 2015 and Zhang-Chen-Cheng 2017 for older exact-family surfaces; and bounded 2026-04-14 exact-term, wheel-notation, and recent-status checks.
- artifacts/r-c4-k1-46-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-46-quadrilateral-star-ramsey/status.json
