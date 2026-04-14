# Working Packet: The Exact Value of R(C4, K1,51)

- slug: `r-c4-k1-51-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,51)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `77`
- single-solve-to-paper fraction: `0.78`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,51.

## novelty_notes
- frontier basis: Current checked public sources support only 59 <= R(C4, K1,51) <= 60.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The exact corridor is already one-gap and the lower bound is explained cleanly in the source. A single solve would therefore contribute almost all of the content needed for a short note, with only proof presentation and comparison to nearby exact values remaining.
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
- assessment: Lane-eligible. The corridor is one-gap, the lower bound is already source-supported by a named proposition, and one exact solve would leave only light packaging.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,51)
- hypothetical title: The Exact Value of R(C4, K1,51)
- paper shape: A one-theorem exact-value note on a one-gap quadrilateral-star case whose lower bound already comes from a recent recursive proposition.
- publication if solved: Closing R(C4, K1,51) would plausibly support a short note on one-gap residues in the quadrilateral-star family.
- minimal artifact requirements: Either a 59-vertex C4-free graph with maximum degree at most 50, or a proof that every 59-vertex C4-free graph has a vertex of degree at least 51.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,51). Current checked public sources leave this parameter in the one-gap corridor 59 <= R(C4, K1,51) <= 60. Closing this gap yields a compact title theorem inside a classical family and requires only a small witness or forcing certificate.

## single_solve_explanation
This candidate passes the 70-90% paper test because the literature already isolates the exact gap and explains the lower-bound mechanism. After the solve, the note would mainly need the decisive witness or contradiction together with a short discussion of the recursive lower-bound provenance. The family anchor is strong enough that the result reads like a legitimate short note rather than a one-paragraph curiosity.

## broader_theorem_nonimplication
Boza's Proposition 12 explains why the lower bound reaches 59, but neither that proposition nor the older exact-family papers settles whether the upper bound 60 is sharp. The checked 2025-2026 searches did not reveal any later paper collapsing the whole band that contains n = 51.

## literature_gap
Current checked sources stop at 59 <= R(C4, K1,51) <= 60.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,51) <= 60 in the small-values table.
- lemma: Boza 2024 Proposition 12 proves the lower bound R(C4, K1,51) >= 59.
- lemma: Boza 2024 Theorem 9 is the recursive device feeding the lower bound in Proposition 12.
- lemma: The 2014 star-wheel equivalence converts the same target into the wheel notation R(C4, W52).
- toy example: The adjacent exact point R(C4, K1,50) = 58 is the nearest solved value immediately below this one-gap residue.
- known obstruction: Any 59-vertex witness must be C4-free with maximum degree at most 50, so the witness has to live very close to the extremal C4-free density ceiling.
- prior-work stop sentence: Current checked sources stop at the one-gap window 59 <= R(C4, K1,51) <= 60.
- recommended first attack: Try to combine the recursive lower-bound mechanism from Theorem 9 with a sharpened extremal argument at 59 vertices to rule out all degree-50 complements.
- paper if solved: The paper would be a short exact-value note closing the n = 51 quadrilateral-star one-gap corridor.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table giving 59 <= R(C4, K1,51) <= 60 and Proposition 12 deriving the lower bound f(51) >= 59 from Theorem 9 and the exact values f(59), f(60), and f(61); together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014) for the star-wheel equivalence surface; together with Wu, Sun, Zhang, and Radziszowski, "Ramsey Numbers of C4 versus Wheels and Stars" (Graphs and Combinatorics 31, 2015) and Zhang-Chen-Cheng, "Polarity Graphs and Ramsey Numbers for C4 versus Stars" (Discrete Mathematics 340, 2017) as older exact-family surfaces checked not to settle n = 51; plus bounded 2026-04-14 exact-term, wheel-notation, canonical-source, and recent-status searches that did not surface a later exact closure.
- Boza 2024 small-values table, Theorem 9, and Proposition 12; Zhang-Broersma-Chen 2014 for the star-wheel equivalence; Wu-Sun-Zhang-Radziszowski 2015 and Zhang-Chen-Cheng 2017 for older exact-family surfaces; and bounded 2026-04-14 exact-term, wheel-notation, and recent-status checks.
- artifacts/r-c4-k1-51-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-51-quadrilateral-star-ramsey/status.json
