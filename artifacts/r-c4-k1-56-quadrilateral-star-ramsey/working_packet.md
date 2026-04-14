# Working Packet: The Exact Value of R(C4, K1,56)

- slug: `r-c4-k1-56-quadrilateral-star-ramsey`
- title: Determine the exact value of R(C4, K1,56)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `63`
- single-solve-to-paper fraction: `0.68`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains K1,56.

## novelty_notes
- frontier basis: Current checked public sources support only 64 <= R(C4, K1,56) <= 65.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The corridor is still just one integer wide, so a solve would contribute most of the mathematics. However, the paper packet is weaker than for the top candidates because the lower bound is only generic and the honest title theorem could more easily be absorbed into a broader interval result.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: unclear
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Not lane-eligible under the strict gate. The gap is tiny, but theorem-slice stability is unclear and the single-solve-to-paper fraction falls below the preferred 0.70 threshold.

## likely_paper_shape
- note title: The Exact Value of R(C4, K1,56)
- hypothetical title: The Exact Value of R(C4, K1,56)
- paper shape: A possible exact-value note on a one-gap quadrilateral-star residue, but with a shakier title-theorem slice than the stronger candidates above.
- publication if solved: Closing R(C4, K1,56) could plausibly support a short exact-value note, but the paper packet is less robust than for the stronger one-gap residues above.
- minimal artifact requirements: Either a 64-vertex C4-free graph with maximum degree at most 55, or a proof that every 64-vertex C4-free graph has a vertex of degree at least 56.

## hypothetical_abstract
We determine the Ramsey number R(C4, K1,56). Current checked public sources leave the exact value in the one-gap corridor 64 <= R(C4, K1,56) <= 65. The result would close a bounded residue in the quadrilateral-star family, although the surrounding paper narrative is weaker than for the strongest queue entries.

## single_solve_explanation
This candidate narrowly misses the strongest micro-paper lane because, although the exact gap is only one, the likely best proof could collapse into a broader observation about a short interval of parameters. After the solve, more narrative work may be needed to justify why this exact parameter deserves to be the title theorem rather than a corollary. It remains a usable reserve dossier inside the same family, but not a top-lane target.

## broader_theorem_nonimplication
The checked literature does not presently imply n = 56, but the generic shape of the lower bound and the surrounding exact values make it more plausible that a future proof would naturally settle several nearby parameters at once. That raises theorem-slice risk even though no existing paper currently closes this specific case.

## literature_gap
Current checked sources stop at 64 <= R(C4, K1,56) <= 65.

## transfer_kit
- lemma: Boza 2024 records the upper bound R(C4, K1,56) <= 65 in the small-values table.
- lemma: Boza 2024 Remark 13 yields the generic lower bound R(C4, K1,56) >= 56 + ceil(sqrt(56)) = 64.
- lemma: The 2014 star-wheel equivalence converts the same target into the wheel notation R(C4, W57).
- lemma: The 2015 and 2017 family papers leave n = 56 outside their published exact formulas.
- toy example: The adjacent exact value R(C4, K1,55) = 64 is the nearest solved point immediately below the open corridor.
- known obstruction: Any 64-vertex witness must be C4-free with maximum degree at most 55, so any lower-bound construction must be both dense and highly collision-averse in common neighborhoods.
- prior-work stop sentence: Current checked sources stop at the one-gap window 64 <= R(C4, K1,56) <= 65.
- recommended first attack: Try to lift the exact construction at n = 55 or the degree-forcing method behind nearby solved cases before investing in any broad interval conjecture.
- paper if solved: If solved cleanly and without broader theorem drift, the paper would be a short exact-value note on the n = 56 quadrilateral-star case.

## bounded_source_list
- Luis Boza, "Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph" (arXiv:2409.12770, 2024), especially the small-values table giving 64 <= R(C4, K1,56) <= 65 and Remark 13 giving the generic lower bound n + ceil(sqrt(n)); together with Yanbo Zhang, Hajo Broersma, and Yaojun Chen, "A remark on star-C4 and wheel-C4 Ramsey numbers" (EJGTA 2(2), 2014) for the star-wheel equivalence surface; together with Wu, Sun, Zhang, and Radziszowski, "Ramsey Numbers of C4 versus Wheels and Stars" (Graphs and Combinatorics 31, 2015) and Zhang-Chen-Cheng, "Polarity Graphs and Ramsey Numbers for C4 versus Stars" (Discrete Mathematics 340, 2017) as older exact-family surfaces checked not to settle n = 56; plus bounded 2026-04-14 exact-term, wheel-notation, canonical-source, and recent-status searches that did not surface a later exact closure.
- Boza 2024 small-values table and Remark 13; Zhang-Broersma-Chen 2014 for the star-wheel equivalence; Wu-Sun-Zhang-Radziszowski 2015 and Zhang-Chen-Cheng 2017 for older exact-family surfaces; and bounded 2026-04-14 exact-term, wheel-notation, and recent-status checks.
- artifacts/r-c4-k1-56-quadrilateral-star-ramsey/record.md
- artifacts/r-c4-k1-56-quadrilateral-star-ramsey/status.json
