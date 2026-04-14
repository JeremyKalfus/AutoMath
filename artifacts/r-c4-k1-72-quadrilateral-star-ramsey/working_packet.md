# Working Packet: The Exact Value of R(C4, K1,72)

- slug: `r-c4-k1-72-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,72)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `69`
- single-solve-to-paper fraction: `0.72`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,72.

## novelty_notes
- frontier basis: Current checked public sources support only 81 <= R(C4, K1,72) <= 82.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem is still already paper-shaped even though the witness scale is larger. What remains after the solve is mainly the decisive 81-vertex witness or forcing contradiction, a short comparison with nearby exact values, and routine verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible but weaker than the smaller queue entries. The gap is still one and the theorem slice is stable, yet the larger certificate pushes the paper closer to the lower end of the target 70-90% band.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,72)
- hypothetical title: The Exact Value of R(C4, K1,72)
- paper shape: A one-theorem exact-value note on a larger but still one-gap quadrilateral-star residue.
- publication if solved: Closing the one-gap case R(C4, K1,72) would still support a short exact-value note on the quadrilateral-star family.
- minimal artifact requirements: Either a 81-vertex C4-free graph with maximum degree at most 71, or a proof that every 81-vertex C4-free graph has a vertex of degree at least 72.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,72). Checked public sources currently leave this case in the one-gap corridor 81 <= R(C4, K1,72) <= 82. Our result closes another unresolved quadrilateral-star point with a single decisive finite certificate.

## single_solve_explanation
This candidate barely but honestly remains inside the micro-paper lane because one exact closure would still dominate the paper. After the solve, the note would mainly need the 81-vertex witness or forcing proof, a brief comparison with the surrounding exact points, and routine verification. The main cost relative to the smaller cases is certificate size, not the absence of a paper narrative.

## broader_theorem_nonimplication
The checked exact-family papers do not list n = 72 among their closed prime-power or q^2 - t parameters, so the broader published formulas stop short of this case. The 2024 source retains only the corridor 81/82 here, and the bounded 2026 exact-term and alternate-notation searches did not reveal a later exact closure.

## literature_gap
Publicly checked sources stop at 81 <= R(C4, K1,72) <= 82.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,72) <= 82 in the small-values table.
- lemma: Boza 2024 Remark 13 implies R(C4, K1,72) >= 72 + ceil(sqrt(72)) = 81.
- lemma: The 2015 and 2017 exact-family papers settle several nearby structural families but not n = 72.
- lemma: The same Boza 2024 table gives the adjacent one-gap case n = 71 and the exact value at n = 73.
- toy example: The adjacent case n = 71 is the nearest one-gap template below the target.
- known obstruction: Any 81-vertex witness must be C4-free while keeping maximum degree at most 71, so the graph must remain extremely dense without creating repeated common-neighbor pairs.
- prior-work stop sentence: Current checked sources stop at the one-gap window 81 <= R(C4, K1,72) <= 82.
- recommended first attack: Use the exact value at n = 73 and the neighboring one-gap behavior at n = 71 to test whether every 81-vertex C4-free graph must already force a degree-72 vertex.
- paper if solved: The paper would be a short exact-value note on a larger quadrilateral-star residue.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table and Remark 13, which together leave f(72) = R(C4, K1,72) in the one-gap corridor 81 <= f(72) <= 82; together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014) for the star-wheel equivalence surface; together with Wu, Sun, Zhang, and Radziszowski, "Ramsey Numbers of C4 versus Wheels and Stars" (Graphs and Combinatorics 31, 2015) and Zhang-Chen-Cheng, "Polarity Graphs and Ramsey Numbers for C4 versus Stars" (Discrete Mathematics 340, 2017) as older exact-family surfaces checked not to settle n = 72; together with the 2022 paper "Bounds for two multicolor Ramsey numbers concerning quadrilaterals" and the Erdos Problems page #552 as recent family-status surfaces; plus bounded 2026-04-14 exact-term and alternate-notation web checks on R(C4, K1,72) that did not surface a later exact closure.
- Boza 2024 small-values table and Remark 13; Zhang-Broersma-Chen 2014 for the star-wheel surface; Wu-Sun-Zhang-Radziszowski 2015 and Zhang-Chen-Cheng 2017 for older exact-family surfaces; the 2022 quadrilateral-bounds paper; Erdos Problems #552; and bounded 2026-04-14 exact-term and alternate-notation web checks.
- artifacts/r-c4-k1-72-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-72-quadrilateral-star-ramsey/status.json
