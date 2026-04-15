# Working Packet: A Residual Weight-36 Circulant Weighing Matrix Case at Order 180

- slug: `circulant-weighing-matrix-180-36`
- title: circulant-weighing-matrix-180-36
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `57`
- single-solve-to-paper fraction: `0.64`

## statement
Determine whether there exists a circulant weighing matrix of order 180 and weight 36.

## novelty_notes
- frontier basis: CW(180,36) remains in the explicit residual weight-36 list after the currently published eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The frontier basis is clear, but the likely certificate is heavier and the editorial cleanup less bounded than for the smaller residual cases.
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
- assessment: Still paper-shaped if solved, but outside the strict lane because the expected certificate bulk and computation cost are too high.

## likely_paper_shape
- note title: A Residual Weight-36 Circulant Weighing Matrix Case at Order 180
- hypothetical title: On the Existence of CW(180,36)
- paper shape: A residual-case note for a larger weight-36 circulant weighing-matrix parameter, if the certificate can be kept under control.
- publication if solved: A construction or nonexistence proof for CW(180,36) would support a residual-case note on one of the larger surviving weight-36 circulant weighing-matrix parameters.
- minimal artifact requirements: Either an explicit CW(180,36) first row or a robust nonexistence certificate excluding all multiplier-compatible orbit patterns.

## hypothetical_abstract
We study the existence of the circulant weighing matrix CW(180,36). This parameter remains on the current residual weight-36 frontier after the published multiplier and contracted-multiplier eliminations. Any exact resolution would still make a legitimate finite-frontier note, but the likely proof burden is heavier than for the smaller residual entries.

## single_solve_explanation
The solve would still provide the central theorem, because the surrounding frontier is already finite and source-anchored. What remains after the solve is mainly packaging and certificate presentation, not a new theorem program. Even so, the expected computational weight is high enough that this is not a preferred micro-paper lane target.

## broader_theorem_nonimplication
The residual-table status in the current Gordon/Arasu-Zhang source chain shows that CW(180,36) is not already settled by the broader published multiplier framework.

## literature_gap
The present Gordon/Arasu-Zhang residual weight-36 frontier still includes CW(180,36), and the bounded curation audit found no later settlement hit.

## transfer_kit
- lemma: Theorem 2.1 gives the self-conjugacy obstruction for folded intersection numbers.
- lemma: Theorem 2.2 gives multiplier-fixed orbit decompositions.
- lemma: Lemma 1 provides the folded intersection equations that constrain any candidate CW(180,36).
- lemma: Theorem 4.1 gives contracted multipliers for the residual open cases.
- toy example: The earlier hand-eliminated cases in Arasu-Gordon-Zhang show the standard pipeline from multiplier orbits to exact contradiction.
- known obstruction: CW(180,36) already survives the published multiplier reductions, so a final proof likely needs a comparatively large orbit-exhaust certificate or a new arithmetic insight.
- prior-work stop sentence: The current Gordon residual list still contains CW(180,36) as an unresolved weight-36 case.
- recommended first attack: Compute the contracted-multiplier orbit table for n = 180 and see whether the surviving folded-equation residue can be killed by a certificate-first exhaustive check with reusable symmetry reductions.
- paper if solved: If solved exactly, the paper would be a residual-case note for the order-180 weight-36 circulant weighing-matrix problem.

## bounded_source_list
- Daniel M. Gordon, Circulant Weighing Matrices (La Jolla Combinatorics Repository / Jupyter Book, 2022; GitHub dataset release visible as May 16, 2025), together with K.T. Arasu, Daniel M. Gordon, and Yiran Zhang, "New Nonexistence Results on Circulant Weighing Matrices" (arXiv:1908.08447, consulted via arXiv/ar5iv on 2026-04-15), especially Section 5 / Table 10 listing the surviving open weight-36 cases including CW(180,36).
- Tan's update of Strassler's table, Arasu-Gordon-Zhang, and Gordon's maintained CW repository.
- artifacts/circulant-weighing-matrix-180-36/record.md
- artifacts/circulant-weighing-matrix-180-36/status.json
