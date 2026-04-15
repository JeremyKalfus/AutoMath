# Working Packet: A Residual Weight-36 Circulant Weighing Matrix Case at Order 140

- slug: `circulant-weighing-matrix-140-36`
- title: circulant-weighing-matrix-140-36
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `62`
- single-solve-to-paper fraction: `0.67`

## statement
Determine whether there exists a circulant weighing matrix of order 140 and weight 36.

## novelty_notes
- frontier basis: CW(140,36) is explicitly retained in the post-elimination residual weight-36 list.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The family narrative is still clear, but compared with the smaller residual orders the final certificate is likelier to be bulkier and the writeup less sharp.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: none
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: tiny
- assessment: Residual-case publishable if solved, but not lane-eligible because the likely proof and certificate footprint are too heavy.

## likely_paper_shape
- note title: A Residual Weight-36 Circulant Weighing Matrix Case at Order 140
- hypothetical title: On the Existence of CW(140,36)
- paper shape: A residual-case note for a larger weight-36 circulant weighing-matrix parameter.
- publication if solved: A construction or nonexistence proof for CW(140,36) would support a residual-case note on one of the larger surviving weight-36 circulant weighing-matrix parameters.
- minimal artifact requirements: Either an explicit CW(140,36) first row or a nonexistence certificate robust enough to exclude all surviving orbit patterns.

## hypothetical_abstract
We consider the existence of the circulant weighing matrix CW(140,36). The parameter remains on the current residual weight-36 frontier after the available multiplier-based eliminations. A resolution would still yield a finite-frontier note, but the solve looks less compact than for the smallest residual cases.

## single_solve_explanation
A solution would still deliver a real paper-shaped contribution because the frontier is already source-anchored and finite. However, for this larger order the decisive argument is more likely to come with a longer computational appendix or certificate. That extra bulk moves it outside the preferred micro-paper lane.

## broader_theorem_nonimplication
The current residual-table status shows that no published general multiplier theorem has yet absorbed CW(140,36).

## literature_gap
The present Gordon/Arasu-Zhang residual weight-36 frontier still includes CW(140,36), and the bounded curation audit found no later settlement hit.

## transfer_kit
- lemma: Theorem 2.1 gives the self-conjugacy obstruction on folded intersection numbers.
- lemma: Theorem 2.2 gives multiplier-fixed orbit decompositions for candidate supports.
- lemma: Lemma 1 turns the support decomposition into explicit folded equations.
- lemma: Theorem 4.1 provides contracted multipliers for hard residual cases.
- toy example: The paper's earlier hand eliminations remain the model for reducing an open parameter to orbit tables and folded contradictions.
- known obstruction: CW(140,36) survives the currently published multiplier filters, so a finish probably requires a larger exact orbit search or a sharper structural obstruction.
- prior-work stop sentence: The current Gordon residual list still contains CW(140,36) as an unresolved weight-36 case.
- recommended first attack: Derive the contracted-multiplier orbit table for n = 140 and test whether the folded-equation residue collapses under a bounded exact search with reusable certificate output.
- paper if solved: If solved exactly, the paper would be a residual-case note for the order-140 weight-36 circulant weighing-matrix problem.

## bounded_source_list
- Daniel M. Gordon, Circulant Weighing Matrices (La Jolla Combinatorics Repository / Jupyter Book, 2022; GitHub dataset release visible as May 16, 2025), together with K.T. Arasu, Daniel M. Gordon, and Yiran Zhang, "New Nonexistence Results on Circulant Weighing Matrices" (arXiv:1908.08447, consulted via arXiv/ar5iv on 2026-04-15), especially Section 5 / Table 10 listing the surviving open weight-36 cases including CW(140,36).
- Tan's update of Strassler's table, Arasu-Gordon-Zhang, and Gordon's maintained CW repository.
- artifacts/circulant-weighing-matrix-140-36/record.md
- artifacts/circulant-weighing-matrix-140-36/status.json
