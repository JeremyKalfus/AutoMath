# Working Packet: The Ramsey Number R(3, K10-2K2)

- slug: `r3-k10-minus-2k2-triangle-ramsey`
- title: Determine the exact value of R(3, K10-2K2)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `71`
- single-solve-to-paper fraction: `0.71`

## statement
Determine the least N such that every triangle-free graph on N vertices has K10-2K2 in its complement.

## novelty_notes
- frontier basis: The 2013 EJC paper gives 31 <= R(3, K10-2K2) <= 33 and calls this case the hardest among the surviving order-10 graph cases; the 2026 survey still treats the graph-on-10-vertices program as not fully closed.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved, the paper is already clear: one exact triangle-Ramsey number in a tightly bounded surviving family. The downside is that the work is likely computation-first rather than compact-argument-first.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: small
- assessment: Not lane-eligible. The gap is tight and the statement is strong, but the likely search burden is too heavy.

## likely_paper_shape
- note title: The Ramsey Number R(3, K10-2K2)
- hypothetical title: The Ramsey Number R(3, K10-2K2)
- paper shape: A single-case triangle-Ramsey computation note with a tight 31-33 corridor.
- publication if solved: An exact determination of R(3, K10-2K2) would be publishable as a focused computational Ramsey note on one of the surviving 10-vertex triangle-Ramsey cases.
- minimal artifact requirements: Either a proof that every triangle-free graph on 33 vertices forces K10-2K2 in the complement at a smaller threshold, or a 32-vertex witness improving the lower bound above 31.

## hypothetical_abstract
We determine the triangle Ramsey number R(3, K10-2K2). The current checked literature narrows this case to the interval 31 <= R(3, K10-2K2) <= 33 and singles it out as one of the hard unresolved 10-vertex cases. An exact closure would therefore support a short, focused computational note in the R(3,G) program.

## single_solve_explanation
An exact solve would provide the title theorem and most of the finished note because the literature corridor is already tight. But the remaining burden is likely substantial certificate handling and graph-generation bookkeeping, which is why it does not clear the strict micro-paper lane.

## broader_theorem_nonimplication
The 2013 paper explicitly leaves the case unresolved, and the checked 2026 survey does not advertise a later theorem settling it. So no broader published result currently collapses this exact claim.

## literature_gap
Checked sources stop at the 31-33 interval from Goedgebeur-Radziszowski, with no later exact closure surfaced in the bounded 2026 status check.

## transfer_kit
- lemma: Goedgebeur and Radziszowski (2013) prove 31 <= R(3, K10-2K2) <= 33.
- lemma: The same paper explicitly conjectures that the exact value is 31.
- lemma: The same paper solves the nearby cases R(3, K10-K3-e) = 31 and R(3, K10-P3-e) = 31.
- lemma: The 2026 survey confirms that the broader R(3,G) program for graphs on 10 vertices was not fully closed by 2013.
- toy example: The 2013 paper's exact neighboring benchmarks R(3, K10-K3-e) = 31 and R(3, K10-P3-e) = 31 are the closest solved comparators.
- known obstruction: The original authors report that improving the upper bound further looked computationally infeasible with their methods, which is a warning that brute-force continuation may not be cheap.
- prior-work stop sentence: Current checked sources still give only 31 <= R(3, K10-2K2) <= 33.
- recommended first attack: Revisit the 31-33 corridor with newer maximal triangle-free generation and critical-graph filtering, targeting the conjectured value 31 first.
- paper if solved: If solved exactly, the paper would be a focused computational note closing one of the surviving 10-vertex triangle-Ramsey cases.

## bounded_source_list
- Jan Goedgebeur and Stanisław P. Radziszowski, "The Ramsey Number R(3, K10-e) and Computational Bounds for R(3,G)" (Electronic Journal of Combinatorics 20(4), 2013), especially Theorem 3(a) establishing 31 <= R(3, K10-2K2) <= 33 and explicitly conjecturing the value 31; together with Stanisław P. Radziszowski's 2026 dynamic survey summary that the graph-on-10-vertices R(3,G) program still has unresolved cases and that the 2013 paper solved only three of them; bounded 2026 exact-statement, alternate-notation, and recent-status searches in this run did not surface a later exact closure.
- Goedgebeur-Radziszowski 2013, the 2026 dynamic survey on small Ramsey numbers, and bounded 2026 status searches run here.
- artifacts/r3-k10-minus-2k2-triangle-ramsey/record.md
- artifacts/r3-k10-minus-2k2-triangle-ramsey/status.json
