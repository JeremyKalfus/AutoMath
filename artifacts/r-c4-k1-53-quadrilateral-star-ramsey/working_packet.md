# Working Packet: The Exact Value of R(C4, K1,53)

- slug: `r-c4-k1-53-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,53)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.86`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,53.

## novelty_notes
- frontier basis: Current checked public sources support only 61 <= R(C4, K1,53) <= 62.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the note already has a clear title theorem and a very short comparison corridor. What remains after the solve is mainly the decisive 61-vertex witness or forcing proof, a short discussion of the adjacent cases, and routine verification.
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
- assessment: Lane-eligible. The theorem slice is stable, the gap is only one, and one solve would already account for most of a publishable note.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,53)
- hypothetical title: The Exact Value of R(C4, K1,53)
- paper shape: A one-theorem exact-value note on a one-gap quadrilateral-star residue with a direct lower-bound transfer already in hand.
- publication if solved: Closing the one-gap case R(C4, K1,53) would already support a compact exact-value note on the quadrilateral-star line.
- minimal artifact requirements: Either a 61-vertex C4-free graph with maximum degree at most 52, or a proof that every 61-vertex C4-free graph has a vertex of degree at least 53.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,53). Checked public sources currently leave this case in the one-gap corridor 61 <= R(C4, K1,53) <= 62. Our result closes a compact unresolved quadrilateral-star point with a single decisive finite certificate.

## single_solve_explanation
This target still clears the 70-90% paper threshold because the exact closure is itself the paper's dominant mathematical content. After a solve, the note mainly needs the 61-vertex witness or forcing contradiction, a brief comparison with the adjacent points n = 52 and n = 54, and ordinary verification. The narrative remains strong because the family is classical and the gap is explicitly recorded in a current source.

## broader_theorem_nonimplication
The older exact-family formulas cover prime-power points and a few special q^2-t neighborhoods, but they do not list n = 53. The 2024 table keeps this case at 61/62, and the bounded 2026 exact-term and alternate-notation searches did not expose a later exact closure.

## literature_gap
Publicly checked sources stop at 61 <= R(C4, K1,53) <= 62.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,53) <= 62 in the small-values table.
- lemma: Boza 2024 Proposition 12 proves R(C4, K1,53) >= 61.
- lemma: Boza 2024 Theorem 9 is the transfer mechanism behind the lower bound.
- lemma: The same Boza 2024 table places the adjacent cases n = 52 and n = 54 in neighboring one-gap corridors.
- toy example: The adjacent one-gap case n = 52 is the cleanest nearby model for the expected proof packaging.
- known obstruction: Any 61-vertex witness must be C4-free while keeping maximum degree at most 52, so the graph must be dense enough to be extremal while still avoiding duplicated common-neighbor patterns.
- prior-work stop sentence: Current checked sources stop at the one-gap window 61 <= R(C4, K1,53) <= 62.
- recommended first attack: Push the Proposition 12 transfer argument one step further into a 61-vertex forcing analysis before attempting a direct extremal witness search.
- paper if solved: The paper would be a short exact-value note closing another one-gap quadrilateral-star residue.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table and Proposition 12, which together leave f(53) = R(C4, K1,53) in the one-gap corridor 61 <= f(53) <= 62; together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014) for the star-wheel equivalence surface; together with Wu, Sun, Zhang, and Radziszowski, "Ramsey Numbers of C4 versus Wheels and Stars" (Graphs and Combinatorics 31, 2015) and Zhang-Chen-Cheng, "Polarity Graphs and Ramsey Numbers for C4 versus Stars" (Discrete Mathematics 340, 2017) as older exact-family surfaces checked not to settle n = 53; together with the 2022 paper "Bounds for two multicolor Ramsey numbers concerning quadrilaterals" and the Erdos Problems page #552 as recent family-status surfaces; plus bounded 2026-04-14 exact-term and alternate-notation web checks on R(C4, K1,53) that did not surface a later exact closure.
- Boza 2024 small-values table and Proposition 12; Zhang-Broersma-Chen 2014 for the star-wheel surface; Wu-Sun-Zhang-Radziszowski 2015 and Zhang-Chen-Cheng 2017 for older exact-family surfaces; the 2022 quadrilateral-bounds paper; Erdos Problems #552; and bounded 2026-04-14 exact-term and alternate-notation web checks.
- artifacts/r-c4-k1-53-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-53-quadrilateral-star-ramsey/status.json
