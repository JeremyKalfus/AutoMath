# Working Packet: The Exact Value of R(4,6)

- slug: `r-4-6-classical-ramsey`
- title: Determine the exact value of R(4,6)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `67`
- single-solve-to-paper fraction: `0.63`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red K_4 or a blue K_6.

## novelty_notes
- frontier basis: Current public sources leave R(4,6) in the interval 36 <= R(4,6) <= 40, so the theorem slice is stable but not yet tightly compressed.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A full exact solve would still produce a publishable title theorem immediately. What keeps it out of the micro-paper lane is the likely size of the residual census and the weaker compactness of the decisive certificate.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: moderate
- assessment: Outside the strict lane. The family anchor is excellent, but the exact gap is too wide and the likely solve packet too large for one-shot micro-paper mode.

## likely_paper_shape
- note title: The Exact Value of R(4,6)
- hypothetical title: The Exact Value of R(4,6)
- paper shape: A computational exact-value note in classical Ramsey theory centered on one off-diagonal complete-graph parameter.
- publication if solved: An exact determination of R(4,6) would still be a real classical Ramsey note, but it no longer fits the strict one-shot micro-paper lane.
- minimal artifact requirements: Either an explicit 36- to 39-vertex (4,6)-avoiding coloring with verification or a structural classification forcing K_4 or K_6 by 40 vertices.

## hypothetical_abstract
We determine the classical Ramsey number R(4,6). Publicly available results place this number in the interval 36 <= R(4,6) <= 40. Our result closes the remaining gap for this off-diagonal complete-graph Ramsey parameter.

## single_solve_explanation
This target still has a legitimate paper shape because an exact solve would obviously be the title theorem. It fails the strict micro-paper test because the current interval is wider, the expected computation is heavier, and the final certificate is unlikely to stay compact. More than lightweight editorial residue remains after the solve itself.

## broader_theorem_nonimplication
No current general theorem implies the exact endpoint; the literature still separates explicit lower-bound constructions from upper-bound counting arguments. The issue is not theorem-slice drift but computational bulk.

## literature_gap
Current public sources stop at 36 <= R(4,6) <= 40.

## transfer_kit
- lemma: Exoo (2012) gives a lower-bound construction proving R(4,6) >= 36.
- lemma: McKay-Radziszowski (1997) derive subgraph-counting identities that yielded the published upper bound R(4,6) <= 41.
- lemma: Current status surfaces report the improved upper bound R(4,6) <= 40.
- lemma: Neighborhood decomposition reduces any hypothetical extremal graph to coupled constraints involving smaller Ramsey graph classes such as (3,6)- and (4,5)-graphs.
- toy example: The exact values R(3,6) = 18 and R(4,5) = 25 are the natural neighborhood-level benchmark cases used inside the standard decomposition.
- known obstruction: The main obstruction is the large family of near-extremal candidate graphs that survive simple degree and counting tests.
- prior-work stop sentence: Current public sources stop at 36 <= R(4,6) <= 40.
- recommended first attack: Exploit neighborhood decomposition and subgraph-counting identities to prune degree patterns before attempting any exhaustive extension search.
- paper if solved: The paper would be a computational exact-value note for an off-diagonal complete-graph Ramsey number.

## bounded_source_list
- Geoffrey Exoo, "On the Ramsey Number R(4,6)" (Electronic Journal of Combinatorics 19(1) (2012)) for the lower bound R(4,6) >= 36; Brendan McKay and Stanislaw Radziszowski, "Subgraph Counting Identities and Ramsey Numbers" (Journal of Combinatorial Theory, Series B 69 (1997)) for the earlier published upper bound 41; together with bounded 2026-04-14 survey-status checking reporting the current upper bound 40.
- Exoo (2012) for the lower bound, McKay-Radziszowski (1997) for subgraph-counting upper-bound machinery, and bounded 2026-04-14 survey/status checking.
- artifacts/r-4-6-classical-ramsey/record.md
- artifacts/r-4-6-classical-ramsey/status.json
