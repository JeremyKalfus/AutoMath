# Working Packet: The Exact Value of R(3, K11-e)

- slug: `r3-k11-minus-edge`
- title: Determine the exact value of R(3, K11-e)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `73`
- single-solve-to-paper fraction: `0.68`

## statement
Determine the exact value of R(3, K11-e) within the current range 42 <= R(3, K11-e) <= 45 by either proving the sharp upper bound or producing a larger triangle-free critical graph.

## novelty_notes
- frontier basis: Goedgebeur and Radziszowski establish R(3, K10-e) = 37 and record 42 <= R(3, K11-e) <= 45, while the January 6, 2026 survey still lists only bounds for J11.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath slug, title, exact tuple, or source-anchor duplicate for the exact J11 Ramsey problem.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact J11 value were fixed, the surrounding J_k story is already well developed and the note could focus on the last missing computations and the final critical-graph analysis. The problem is that the artifact packet would likely be larger than the best one-shot publication targets.
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
- exact gap from source: small
- assessment: Fail for the strict lane. The theorem would be real and publishable, but the expected search and certification burden is too high relative to the cleanest one-shot paper packets.

## likely_paper_shape
- note title: The Exact Value of R(3, K11-e)
- hypothetical title: The Exact Value of R(3, K11-e)
- paper shape: A computational exact-value note for the smallest open R(3, Kk-e) parameter after k = 10.
- publication if solved: Fixing the first open K_k-e value after the solved J10 case would produce a legitimate exact-value Ramsey paper, but the computational certificate is likely too bulky for the strict micro-paper lane.
- minimal artifact requirements: A full certified elimination of triangle-free critical graphs on the relevant orders, or one explicit larger critical graph improving the lower bound.

## hypothetical_abstract
We determine the exact two-color Ramsey number R(3, K11-e). Goedgebeur and Radziszowski's 2013 paper and the January 6, 2026 Ramsey survey leave only the range 42 <= R(3, K11-e) <= 45. Our result closes the next exact case in the R(3, Kk-e) hierarchy after the solved K10-e entry.

## single_solve_explanation
The exact theorem would clearly be the title result, and the literature already supplies the context, prior bounds, and computational framework. However, the solve is likely to require a substantial certification appendix or machine-verification packet. That pushes the target outside the cleanest 70-90% micro-paper zone even though the exact theorem is publishable.

## broader_theorem_nonimplication
The latest survey still lists only the range 42 <= R(3, J11) <= 45, so no broader published theorem has collapsed the exact J11 case.

## literature_gap
Goedgebeur and Radziszowski give the range 42 <= R(3, K11-e) <= 45, and the January 6, 2026 survey still reports only bounds for J11.

## transfer_kit
- lemma: Goedgebeur and Radziszowski prove R(3, K10-e) = 37 and summarize the Jk framework via triangle-free critical graphs.
- lemma: Their Table 1 records the range 42 <= R(3, J11) <= 45, and the January 6, 2026 survey still retains that bounded gap.
- lemma: The deficiency method and exact e(3, Jk, n) computations from the 2013 paper reduce the J11 problem to finitely many critical graph configurations.
- toy example: The solved predecessor J10 = K10-e with exact value 37 is the nearest fully resolved benchmark for the J11 computation.
- known obstruction: The likely route is heavy triangle-free graph generation plus critical-graph elimination, so even a successful solve may come with a large machine certificate.
- prior-work stop sentence: The January 6, 2026 Ramsey survey still lists only 42 <= R(3, K11-e) <= 45.
- recommended first attack: Reuse the deficiency and neighbor-gluing framework from the 2013 J10 paper to force stronger lower bounds on e(3, J11, n) at the orders 42-45 before any full generation pass.
- paper if solved: The paper would be a computational exact-value Ramsey note closing the first open Jk case after J10.

## bounded_source_list
- Jan Goedgebeur and Stanislaw P. Radziszowski, "The Ramsey Number R(3, K10-e) and Computational Bounds for R(3, G)" (Electronic Journal of Combinatorics 20(4), 2013), together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Dynamic Survey DS1.18, revision dated January 6, 2026), Sections 3.1 and 8.2.
- Goedgebeur-Radziszowski 2013, Radziszowski DS1.18 January 6, 2026, and bounded 2026-04-13 web searches for R(3,K11-e), R(3,J11), and recent-status signals.
- artifacts/r3-k11-minus-edge/record.md
- artifacts/r3-k11-minus-edge/status.json
