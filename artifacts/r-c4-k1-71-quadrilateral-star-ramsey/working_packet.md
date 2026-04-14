# Working Packet: The Exact Value of R(C4, K1,71)

- slug: `r-c4-k1-71-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,71)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `68`
- single-solve-to-paper fraction: `0.72`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,71; equivalently determine R(C4, W71).

## novelty_notes
- frontier basis: Current checked public sources support only 80 <= R(C4, K1,71) = R(C4, W71) <= 81.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the exact theorem itself is already enough to anchor a paper. What remains after the solve is mainly the witness or forcing contradiction at 80 vertices, a brief comparison with nearby exact values, and routine verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible but weaker than the smaller queue entries. The family anchor stays strong and the residual gap is still one, but the likely certificate is larger and the paper packet is correspondingly less compact.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,71)
- hypothetical title: The Exact Value of R(C4, K1,71)
- paper shape: A one-theorem exact-value note on a larger one-gap quadrilateral-star residue with direct wheel reformulation.
- publication if solved: Closing the one-gap case R(C4, K1,71) = R(C4, W71) would still support a short exact-value note on the quadrilateral-star family.
- minimal artifact requirements: Either an 80-vertex C4-free graph with maximum degree at most 70, or a proof that every 80-vertex C4-free graph has a vertex of degree at least 71.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,71), equivalently R(C4, W71). Checked public sources currently leave this case in the one-gap corridor 80 <= R(C4, K1,71) <= 81. Our result closes a finite quadrilateral-star residue whose proof can be preserved in a short exact-value note.

## single_solve_explanation
This candidate remains paper-shaped because the one-gap closure would still be the dominant theorem and the surrounding prose is routine. After the solve, the note would mainly need the 80-vertex witness or forcing proof, a short explanation of the lower-bound transfer from exact values near 78-80, and a brief comparison with neighboring exact points. The main drawback is only the larger certificate size.

## broader_theorem_nonimplication
The known exact prime-power formulas and older exact wheel cases do not cover n = 71. The 2024 source records only 80/81 here, and the bounded 2026 exact-term and alternate-notation search did not reveal any later exact-value article for this case.

## literature_gap
Publicly checked sources stop at 80 <= R(C4, K1,71) = R(C4, W71) <= 81.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,71) <= 81 in the small-values table.
- lemma: Boza 2024 Proposition 12 proves R(C4, K1,71) >= 80.
- lemma: Boza 2024 Theorem 9 is the transfer mechanism behind that lower bound.
- lemma: Zhang-Broersma-Chen 2014 give the equivalence R(C4, W71) = R(C4, K1,71).
- toy example: The exact neighbor R(C4, K1,70) = 79 is the cleanest solved case directly below the target.
- known obstruction: Any 80-vertex witness must remain C4-free while keeping the maximum degree at most 70, so the graph must stay in a very narrow near-extremal regime where small local overlaps can force a C4.
- prior-work stop sentence: Current checked sources stop at the one-gap window 80 <= R(C4, K1,71) = R(C4, W71) <= 81.
- recommended first attack: Start from the exact n = 70 neighborhood and test whether a one-vertex extension survives the C4-free degree cap, using the q = 8 polarity-graph structure as the natural baseline before attempting a universal forcing proof at 80 vertices.
- paper if solved: The paper would be a short exact-value note settling another one-gap quadrilateral-star Ramsey case.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table, Theorem 9, Proposition 12, and Remark 13, which together leave f(71) = R(C4, K1,71) in the one-gap corridor 80 <= f(71) <= 81; together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014), which gives R(C4, Wn) = R(C4, K1,n) for n >= 6; together with the 2022 paper "Bounds for two multicolor Ramsey numbers concerning quadrilaterals" and the Erdos Problems page #552 as recent family-status surfaces, plus bounded 2026-04-14 exact-term and alternate-notation web checks on R(C4, K1,71) and R(C4, W71) that did not surface a later exact closure.
- Boza 2024 small-values table, Theorem 9, Proposition 12, and Remark 13; Zhang-Broersma-Chen 2014; the 2022 quadrilateral-bounds paper; Erdos Problems #552; and bounded 2026-04-14 exact-term and alternate-notation web checks.
- artifacts/r-c4-k1-71-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-71-quadrilateral-star-ramsey/status.json
