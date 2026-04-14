# Working Packet: The Exact Value of R(C4, K1,54)

- slug: `r-c4-k1-54-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,54)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `80`
- single-solve-to-paper fraction: `0.82`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,54.

## novelty_notes
- frontier basis: Current checked public sources support only 62 <= R(C4, K1,54) <= 63.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the title theorem already defines the note. What remains after the solve is mainly the decisive 62-vertex witness or forcing proof, a brief comparison with nearby exact cases, and routine verification.
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
- assessment: Lane-eligible. The family anchor is strong, the theorem slice is stable, and the gap is only one, though the packet is a bit less sharp than the Proposition 12 cases.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,54)
- hypothetical title: The Exact Value of R(C4, K1,54)
- paper shape: A one-theorem exact-value note on a mid-size one-gap quadrilateral-star residue.
- publication if solved: Closing the one-gap case R(C4, K1,54) would still produce a credible short exact-value note on the quadrilateral-star family.
- minimal artifact requirements: Either a 62-vertex C4-free graph with maximum degree at most 53, or a proof that every 62-vertex C4-free graph has a vertex of degree at least 54.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,54). Checked public sources currently leave this case in the one-gap corridor 62 <= R(C4, K1,54) <= 63. Our result closes a finite quadrilateral-star residue whose proof can be recorded as a short exact-value note.

## single_solve_explanation
This candidate still qualifies because the exact one-gap closure would remain the honest title theorem of the note. After a solve, the paper mainly needs the decisive 62-vertex witness or forcing contradiction, a short comparison with nearby exact points, and routine verification. The main penalty relative to the top queue entries is that the lower bound comes from the generic Remark 13 surface rather than a sharper proposition.

## broader_theorem_nonimplication
The checked exact-family papers settle q^2, q^2+1, and a few special q^2-t cases, but 54 is not one of those listed parameters. The 2024 source itself leaves only the corridor 62/63 here, and the bounded 2026 exact-term and alternate-notation searches did not reveal a later exact-value paper.

## literature_gap
Publicly checked sources stop at 62 <= R(C4, K1,54) <= 63.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,54) <= 63 in the small-values table.
- lemma: Boza 2024 Remark 13 implies R(C4, K1,54) >= 54 + ceil(sqrt(54)) = 62.
- lemma: The 2017 polarity-graph paper gives several nearby exact families but not n = 54, clarifying the true gap location.
- lemma: The same Boza 2024 table places n = 53 and n = 55 immediately on either side of the target corridor.
- toy example: The neighboring case n = 53 is the nearest lower one-gap model for expected packaging.
- known obstruction: Any 62-vertex witness must be C4-free while keeping maximum degree at most 53, forcing a dense near-extremal configuration without repeated common-neighbor patterns.
- prior-work stop sentence: Current checked sources stop at the one-gap window 62 <= R(C4, K1,54) <= 63.
- recommended first attack: Start from the generic n + ceil(sqrt(n)) lower-bound regime at n = 54 and try to prove that every 62-vertex C4-free graph must cross the degree-54 threshold.
- paper if solved: The paper would be a short exact-value note on a mid-size quadrilateral-star Ramsey residue.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table and Remark 13, which together leave f(54) = R(C4, K1,54) in the one-gap corridor 62 <= f(54) <= 63; together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014) for the star-wheel equivalence surface; together with Wu, Sun, Zhang, and Radziszowski, "Ramsey Numbers of C4 versus Wheels and Stars" (Graphs and Combinatorics 31, 2015) and Zhang-Chen-Cheng, "Polarity Graphs and Ramsey Numbers for C4 versus Stars" (Discrete Mathematics 340, 2017) as older exact-family surfaces checked not to settle n = 54; together with the 2022 paper "Bounds for two multicolor Ramsey numbers concerning quadrilaterals" and the Erdos Problems page #552 as recent family-status surfaces; plus bounded 2026-04-14 exact-term and alternate-notation web checks on R(C4, K1,54) that did not surface a later exact closure.
- Boza 2024 small-values table and Remark 13; Zhang-Broersma-Chen 2014 for the star-wheel surface; Wu-Sun-Zhang-Radziszowski 2015 and Zhang-Chen-Cheng 2017 for older exact-family surfaces; the 2022 quadrilateral-bounds paper; Erdos Problems #552; and bounded 2026-04-14 exact-term and alternate-notation web checks.
- artifacts/r-c4-k1-54-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-54-quadrilateral-star-ramsey/status.json
