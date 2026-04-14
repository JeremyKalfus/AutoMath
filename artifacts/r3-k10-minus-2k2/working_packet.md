# Working Packet: The Exact Value of R(3, K10-2K2)

- slug: `r3-k10-minus-2k2`
- title: Determine the exact value of R(3, K10-2K2)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `71`
- single-solve-to-paper fraction: `0.66`

## statement
Determine the exact value of R(3, K10-2K2) within the current range 31 <= R(3, K10-2K2) <= 33 by either proving the sharp upper bound or producing a larger triangle-free critical graph.

## novelty_notes
- frontier basis: Goedgebeur and Radziszowski prove only 31 <= R(3, K10-2K2) <= 33 and describe it as the hardest remaining open 10-vertex case in their computational study.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath slug, title, exact tuple, or source-anchor duplicate for the exact K10-2K2 Ramsey problem.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact value were fixed, the note could be sharply framed around one stubborn 10-vertex residue. But the heavy computational artifact requirements and the source's infeasibility warning make this a weaker fit for the strict micro-paper lane.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: small
- assessment: Fail for the strict lane. The exact statement is real, but the source literature itself warns that the remaining residue is computationally stubborn and unlikely to produce a compact publication packet.

## likely_paper_shape
- note title: The Exact Value of R(3, K10-2K2)
- hypothetical title: The Exact Value of R(3, K10-2K2)
- paper shape: A computational exact-value note for one remaining 10-vertex triangle Ramsey case.
- publication if solved: The exact theorem would be publishable as a finite-gap Ramsey note on one of the remaining 10-vertex graphs, but the source itself describes the case as unusually computation-heavy.
- minimal artifact requirements: A complete certified elimination of triangle-free critical graphs at orders 31-33, or one explicit larger critical graph improving the lower bound.

## hypothetical_abstract
We determine the exact Ramsey number R(3, K10-2K2). Goedgebeur and Radziszowski's 2013 computational study leaves only the bounds 31 <= R(3, K10-2K2) <= 33 and identifies this graph as the hardest remaining open 10-vertex case in their family. Our theorem closes that final bounded gap for this specific near-complete graph.

## single_solve_explanation
An exact determination would indeed be the whole paper, because the surrounding computational context is already in place. The problem is that the solve is likely to consist mostly of expensive elimination and certification rather than a compact transfer-friendly argument. That makes it honest as a paper but weaker as a micro-paper target.

## broader_theorem_nonimplication
The 2013 paper still records only 31 <= R(3, K10-2K2) <= 33 and the latest survey does not replace that with an exact value, so no broader theorem has settled the case.

## literature_gap
Goedgebeur and Radziszowski establish only 31 <= R(3, K10-2K2) <= 33 and explicitly leave the exact value open.

## transfer_kit
- lemma: Goedgebeur and Radziszowski prove 31 <= R(3, K10-2K2) <= 33 in Theorem 3.
- lemma: The same paper notes that all remaining unresolved 10-vertex cases have Ramsey number at least 31, so the residue is bounded and explicit.
- lemma: Their degree-sequence and neighbor-gluing computations already reduce the search space enough to improve the trivial upper bound from 37 to 33.
- toy example: The two sibling 10-vertex cases R(3, K10-K3-e) and R(3, K10-P3-e) are solved exactly at 31 in the same paper, giving the nearest successful benchmark.
- known obstruction: The authors report that K10-2K2 appears significantly more difficult than J10 and that further upper-bound improvement looked computationally infeasible with their algorithms.
- prior-work stop sentence: Goedgebeur and Radziszowski leave the case with bounds 31 <= R(3, K10-2K2) <= 33.
- recommended first attack: Exploit the solved sibling cases at value 31 to prune candidate critical graphs and then revisit the 32- and 33-vertex elimination with stronger structural filters before any exhaustive generation.
- paper if solved: The paper would be a computational note settling one stubborn remaining 10-vertex triangle Ramsey case.

## bounded_source_list
- Jan Goedgebeur and Stanislaw P. Radziszowski, "The Ramsey Number R(3, K10-e) and Computational Bounds for R(3, G)" (Electronic Journal of Combinatorics 20(4), 2013), Theorem 3 and surrounding discussion, together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Dynamic Survey DS1.18, revision dated January 6, 2026), Section 8.2.
- Goedgebeur-Radziszowski 2013 Theorem 3, Radziszowski DS1.18 January 6, 2026 cumulative remarks, and bounded 2026-04-13 web searches for R(3,K10-2K2) and recent-status signals.
- artifacts/r3-k10-minus-2k2/record.md
- artifacts/r3-k10-minus-2k2/status.json
