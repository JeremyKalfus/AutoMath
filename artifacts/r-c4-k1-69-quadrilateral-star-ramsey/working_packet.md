# Working Packet: The Exact Value of R(C4, K1,69)

- slug: `r-c4-k1-69-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,69)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `72`
- single-solve-to-paper fraction: `0.75`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,69; equivalently determine R(C4, W69).

## novelty_notes
- frontier basis: Current checked public sources support only 78 <= R(C4, K1,69) = R(C4, W69) <= 79.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem is already paper-ready even though the witness scale is somewhat larger. What remains after the solve is mainly the decisive witness or forcing contradiction at 78 vertices, a short comparison with the exact neighbor R(C4, K1,68) = 77 and the exact point R(C4, K1,70) = 79, and routine verification.
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
- assessment: Lane-eligible. The gap is still just one, the theorem slice is stable, and the family anchor remains strong, though the certificate is less compact than for the smaller queue entries.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,69)
- hypothetical title: The Exact Value of R(C4, K1,69)
- paper shape: A one-theorem exact-value note on a larger but still one-gap quadrilateral-star residue.
- publication if solved: Closing the one-gap case R(C4, K1,69) = R(C4, W69) would still be enough for a short exact-value note on the quadrilateral-star line.
- minimal artifact requirements: Either a 78-vertex C4-free graph with maximum degree at most 68, or a proof that every 78-vertex C4-free graph has a vertex of degree at least 69.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,69), equivalently R(C4, W69). Checked public sources currently leave this case in the one-gap corridor 78 <= R(C4, K1,69) <= 79. Our result closes another unresolved quadrilateral-star point with a single decisive finite certificate.

## single_solve_explanation
This candidate remains within the micro-paper lane because one exact closure would still be the dominant mathematical content of the paper. After the solve, the note would mainly need the 78-vertex witness or the forcing proof, a short discussion of the transfer argument behind the lower bound, and brief comparison with adjacent exact values. The main penalty relative to the smaller cases is witness size, not lack of a paper narrative.

## broader_theorem_nonimplication
The checked exact formulas cover only special prime-power surfaces and small special neighborhoods, not the case n = 69. The 2024 source itself records only 78/79 here, and the bounded 2026 searches in both star and wheel notation did not reveal a later exact-value paper.

## literature_gap
Publicly checked sources stop at 78 <= R(C4, K1,69) = R(C4, W69) <= 79.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,69) <= 79 in the small-values table.
- lemma: Boza 2024 Proposition 12 proves R(C4, K1,69) >= 78.
- lemma: Boza 2024 Theorem 9 is the transfer mechanism behind that lower bound.
- lemma: The same Boza 2024 table gives exact adjacent anchors R(C4, K1,68) = 77 and R(C4, K1,70) = 79.
- toy example: The exact solved neighbor R(C4, K1,68) = 77 is the nearest template below the target.
- known obstruction: Any 78-vertex witness must be C4-free while capping the maximum degree at 68, so the graph must stay close to the polarity-graph density barrier without creating repeated common-neighbor pairs.
- prior-work stop sentence: Current checked sources stop at the one-gap window 78 <= R(C4, K1,69) = R(C4, W69) <= 79.
- recommended first attack: Start from the exact n = 68 case and test whether a one-vertex extension can be blocked or realized, using the q = 8 polarity-graph neighborhood as the structural baseline before attempting a global forcing proof at 78 vertices.
- paper if solved: The paper would be a short exact-value note on a larger one-gap quadrilateral-star Ramsey case.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table, Theorem 9, Proposition 12, and Remark 13, which together leave f(69) = R(C4, K1,69) in the one-gap corridor 78 <= f(69) <= 79; together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014), which gives R(C4, Wn) = R(C4, K1,n) for n >= 6; together with the 2022 paper "Bounds for two multicolor Ramsey numbers concerning quadrilaterals" and the Erdos Problems page #552 as recent family-status surfaces, plus bounded 2026-04-14 exact-term and alternate-notation web checks on R(C4, K1,69) and R(C4, W69) that did not surface a later exact closure.
- Boza 2024 small-values table, Theorem 9, Proposition 12, and Remark 13; Zhang-Broersma-Chen 2014; the 2022 quadrilateral-bounds paper; Erdos Problems #552; and bounded 2026-04-14 exact-term and alternate-notation web checks.
- artifacts/r-c4-k1-69-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-69-quadrilateral-star-ramsey/status.json
