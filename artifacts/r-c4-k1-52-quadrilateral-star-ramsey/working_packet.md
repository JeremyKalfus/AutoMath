# Working Packet: The Exact Value of R(C4, K1,52)

- slug: `r-c4-k1-52-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,52)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `75`
- single-solve-to-paper fraction: `0.76`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,52.

## novelty_notes
- frontier basis: Current checked public sources support only 60 <= R(C4, K1,52) <= 61.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The paper packet is already close to complete because the open corridor is a single integer and the lower-bound source is explicit. After a solve, only the final witness-or-forcing proof and a compact comparison paragraph would still be missing.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible, but slightly weaker than n = 44 and n = 46 because the narrative is more corridor-closing than stand-alone family-shaping. Still, one exact solve would already produce most of a publishable short note.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,52)
- hypothetical title: The Exact Value of R(C4, K1,52)
- paper shape: A short exact-value note on a one-gap quadrilateral-star residue whose lower bound is already source-extracted by a recent recursive proposition.
- publication if solved: Closing R(C4, K1,52) would plausibly stand as a short exact-value note in the quadrilateral-star family.
- minimal artifact requirements: Either a 60-vertex C4-free graph with maximum degree at most 51, or a proof that every 60-vertex C4-free graph has a vertex of degree at least 52.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,52). Current checked public sources leave the exact value in the one-gap corridor 60 <= R(C4, K1,52) <= 61. The result closes a narrow residue in a classical family with a proof packet compact enough for a brief note.

## single_solve_explanation
This candidate passes the 70-90% paper test because the exact closure itself is the main theorem and almost all of the technical content. After the solve, the remaining work is limited to certificate presentation, literature placement, and routine verification. The family anchor is still strong enough to keep the note from reading like an isolated tiny anecdote.

## broader_theorem_nonimplication
The older exact-family papers and Boza's 2024 recursion-based lower bounds do not decide whether the upper bound 61 is sharp. The checked web searches did not reveal any later theorem or survey entry resolving this exact parameter.

## literature_gap
Current checked sources stop at 60 <= R(C4, K1,52) <= 61.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,52) <= 61 in the small-values table.
- lemma: Boza 2024 Proposition 12 proves the lower bound R(C4, K1,52) >= 60.
- lemma: Boza 2024 Theorem 9 is the recursive input behind that lower bound.
- lemma: The 2014 star-wheel equivalence converts this target into the wheel notation R(C4, W53).
- toy example: The adjacent exact point R(C4, K1,50) = 58 provides a nearby solved model below the open case.
- known obstruction: Any 60-vertex witness must be C4-free with maximum degree at most 51, leaving little degree slack and forcing tight control of common-neighbor intersections.
- prior-work stop sentence: Current checked sources stop at the one-gap window 60 <= R(C4, K1,52) <= 61.
- recommended first attack: Push the recursive lower-bound machinery together with a 60-vertex extremal-degree count to see whether the upper bound can be forced down to 60.
- paper if solved: The paper would be a short exact-value note closing the n = 52 quadrilateral-star corridor.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table giving 60 <= R(C4, K1,52) <= 61 and Proposition 12 deriving the lower bound f(52) >= 60 from Theorem 9 and exact values at 60 and 61; together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014) for the star-wheel equivalence surface; together with Wu, Sun, Zhang, and Radziszowski, "Ramsey Numbers of C4 versus Wheels and Stars" (Graphs and Combinatorics 31, 2015) and Zhang-Chen-Cheng, "Polarity Graphs and Ramsey Numbers for C4 versus Stars" (Discrete Mathematics 340, 2017) as older exact-family surfaces checked not to settle n = 52; plus bounded 2026-04-14 exact-term, wheel-notation, canonical-source, and recent-status searches that did not surface a later exact closure.
- Boza 2024 small-values table, Theorem 9, and Proposition 12; Zhang-Broersma-Chen 2014 for the star-wheel equivalence; Wu-Sun-Zhang-Radziszowski 2015 and Zhang-Chen-Cheng 2017 for older exact-family surfaces; and bounded 2026-04-14 exact-term, wheel-notation, and recent-status checks.
- artifacts/r-c4-k1-52-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-52-quadrilateral-star-ramsey/status.json
