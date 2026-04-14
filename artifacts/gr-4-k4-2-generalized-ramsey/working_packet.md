# Working Packet: The Exact Value of GR(4, K4, 2)

- slug: `gr-4-k4-2-generalized-ramsey`
- title: Determine the exact value of GR(4, K4, 2)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.74`

## statement
Determine the minimum N such that every 4-edge-coloring of K_N contains a copy of K_4 using at most two colors.

## novelty_notes
- frontier basis: Current public sources leave this parameter in the three-value window 15 <= GR(4, K4, 2) <= 17, and the small-parameter generalized-Ramsey program is recent enough that an exact closure still reads as a genuine title theorem.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The result would already be the central theorem of the note. The remaining work is mainly the extremal proof or witness classification and a short placement beside the exact nearby cases already solved in the same paper.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Eligible but not top-ranked. The family anchor is strong and the parameter is foundational, yet the interval is wider than the best one-step candidates and the note would need slightly more explanatory packaging.

## likely_paper_shape
- note title: The Exact Value of GR(4, K4, 2)
- hypothetical title: The Exact Value of GR(4, K4, 2)
- paper shape: A one-theorem exact-value note for a foundational small generalized Ramsey parameter.
- publication if solved: Closing GR(4, K4, 2) would already support a concise note on one of the first unresolved exact generalized small Ramsey numbers for clique-with-at-most-two-colors forcing.
- minimal artifact requirements: Either a proof that every 4-coloring of K15 forces a 2-colored K4, or an explicit extremal coloring on 15 or 16 vertices together with verification.

## hypothetical_abstract
We determine the generalized Ramsey number GR(4, K4, 2), the minimum N such that every 4-edge-coloring of K_N contains a copy of K_4 using at most two colors. Existing public sources leave the value in the interval 15 <= GR(4, K4, 2) <= 17. Our result closes one of the smallest unresolved exact parameters in the newly initiated finite generalized-Ramsey table.

## single_solve_explanation
An exact determination would already provide the paper's title theorem. Some exposition remains because the generalized notation is less standard than for ordinary two-color Ramsey numbers, but the literature base is small and explicit. This keeps the solve-to-paper fraction inside the target lane, albeit not at the very top.

## broader_theorem_nonimplication
The 2025 paper proves nearby exact cases GR(3, K4, 2) = 10 and GR(4, K4, 3) = 10, but neither determines the 4-color at-most-2-color threshold. No broader theorem found in the bounded audit collapses GR(4, K4, 2) to an immediate corollary.

## literature_gap
Current public sources support only 15 <= GR(4, K4, 2) <= 17, and the bounded 2026-04-14 exact-term and alternate-notation audit did not uncover a later exact determination.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe 2025, Table 1, gives 15 <= GR(4, K4, 2) <= 17.
- lemma: The same paper proves the exact nearby benchmarks GR(3, K4, 2) = 10 and GR(4, K4, 3) = 10.
- lemma: Their generalized-Ramsey scoring framework reduces the search to clique counting inside the graphs formed by unions of chosen color classes.
- toy example: Joining two arbitrary colors in the unique extremal coloring for GR(4, K4, 3) recovers the extremal picture for GR(3, K4, 2), giving a concrete toy model for the target family.
- known obstruction: An exact upper-bound proof must show that every 4-coloring at the target order already creates a K4 inside some union of two color classes, while a lower-bound witness must suppress such K4s across all six color pairs.
- prior-work stop sentence: Current sources stop at the interval 15 <= GR(4, K4, 2) <= 17.
- recommended first attack: Use the paper's two-color-class reduction and extend the exact GR(3, K4, 2) and GR(4, K4, 3) structures before allowing any wider computational sweep.
- paper if solved: The paper would be a concise exact-value note on a foundational small generalized Ramsey parameter.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), especially Table 1 and the generalized-Ramsey method discussion, together with bounded exact-statement, alternate-notation, canonical-source, outside-source, and recent-status checks through 2026-04-14.
- Lidicky-McKinley-Pfender-Van Overberghe 2025, source-internal nearby exact cases, and bounded 2026-04-14 exact-term, synonym, outside-source, and recent-status checks.
- artifacts/gr-4-k4-2-generalized-ramsey/record.md
- artifacts/gr-4-k4-2-generalized-ramsey/status.json
