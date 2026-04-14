# Working Packet: The Exact Value of R(C4, K1,42)

- slug: `r-c4-k1-42-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,42)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `88`
- single-solve-to-paper fraction: `0.89`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,42; equivalently determine R(C4, W42).

## novelty_notes
- frontier basis: Current checked public sources support only 49 <= R(C4, K1,42) = R(C4, W42) <= 50.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem, the wheel-equivalent formulation, and the comparison points from nearby exact values are already in place. What remains after the solve is mainly the decisive witness or forcing contradiction, a short comparison paragraph with adjacent exact cases, and routine verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. The gap is only one, the family anchor is classical, the theorem slice is stable, and one clean solve would already supply almost the whole paper.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,42)
- hypothetical title: The Exact Value of R(C4, K1,42)
- paper shape: A one-theorem exact-value note on a smallest fresh one-gap quadrilateral-star Ramsey residue, with the wheel reformulation available for framing.
- publication if solved: Closing the one-gap case R(C4, K1,42) = R(C4, W42) would already read like the title theorem of a short note on quadrilateral-star Ramsey numbers.
- minimal artifact requirements: Either a 49-vertex C4-free graph with maximum degree at most 41, or a proof that every 49-vertex C4-free graph has a vertex of degree at least 42.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,42), equivalently R(C4, W42). Checked public sources currently leave this case in the one-gap corridor 49 <= R(C4, K1,42) <= 50. Our result closes a compact unresolved quadrilateral-star Ramsey case with a certificate small enough for a short stand-alone note.

## single_solve_explanation
This candidate passes the 70-90% paper test because the note is already title-shaped before any new mathematics is added. After a solve, the paper mainly needs the critical 49-vertex witness or the forcing proof at 49 vertices, plus a short comparison with neighboring exact values such as R(C4, K1,41) = 49 and R(C4, K1,43) = 51. It is not just a tiny curiosity because it sits on a named classical family that still has an explicitly open general status surface.

## broader_theorem_nonimplication
The published exact formulas check the prime-power surfaces n = q^2 and n = q^2 + 1, plus several q^2 - t neighborhoods, and the 2015 wheel paper settles selected cases up to n <= 44. The checked sources do not include n = 42 among those exact formulas or enumerated exact wheel cases, and the 2026 bounded search did not reveal a later paper closing it.

## literature_gap
Publicly checked sources stop at 49 <= R(C4, K1,42) = R(C4, W42) <= 50.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,42) <= 50 in the small-values table.
- lemma: Boza 2024 Remark 13 gives the generic lower bound R(C4, K1,n) >= n + ceil(sqrt(n)) for 2 <= n <= 82, hence R(C4, K1,42) >= 49.
- lemma: Zhang-Broersma-Chen 2014 prove R(C4, Wn) = R(C4, K1,n) for n >= 6.
- lemma: The same Boza 2024 table gives nearby exact anchors R(C4, K1,41) = 49 and R(C4, K1,43) = 51.
- toy example: The adjacent exact value R(C4, K1,41) = 49 is the cleanest nearby model for how a one-gap quadrilateral-star note can close.
- known obstruction: Any 49-vertex witness must be C4-free while keeping maximum degree at most 41, so the configuration must be very dense but still avoid repeated common-neighbor patterns.
- prior-work stop sentence: Current checked sources stop at the one-gap window 49 <= R(C4, K1,42) = R(C4, W42) <= 50.
- recommended first attack: Start from the q = 7 polarity-graph neighborhood and test whether a 49-vertex C4-free graph can be tuned to keep every degree at most 41 before attempting a forcing argument at 49 vertices.
- paper if solved: The paper would be a short exact-value note closing a smallest fresh quadrilateral-star Ramsey residue.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table and Remark 13, which together leave f(42) = R(C4, K1,42) in the one-gap corridor 49 <= f(42) <= 50; together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014), which gives the equivalence R(C4, Wn) = R(C4, K1,n) for n >= 6 and Parsons-type upper-bound surface; together with Yali Wu, Yongqi Sun, and Stanislaw Radziszowski, "Wheel and star-critical Ramsey numbers for quadrilateral" (Discrete Applied Mathematics 186, 2015), checked as the canonical older exact-value surface up to n <= 44 and not found to settle n = 42; together with the 2022 paper "Bounds for two multicolor Ramsey numbers concerning quadrilaterals" as a recent family-status surface, the Erdos Problems page #552 last edited 2026-02-01 as a recent discussion surface for the still-open family, and bounded 2026-04-14 exact-term and alternate-notation web checks on R(C4, K1,42) and R(C4, W42) that did not surface a later exact closure.
- Boza 2024 small-values table, Proposition 12, and Remark 13; Zhang-Broersma-Chen 2014 for the star-wheel equivalence and upper-bound surface; Wu-Sun-Radziszowski 2015 as the older exact-value wheel surface; the 2022 quadrilateral-bounds paper and Erdos Problems #552 as recent family-status surfaces; plus bounded 2026-04-14 exact-term and alternate-notation web checks.
- artifacts/r-c4-k1-42-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-42-quadrilateral-star-ramsey/status.json
