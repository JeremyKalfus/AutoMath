# Working Packet: A Residual Weight-36 Circulant Weighing Matrix Case at Order 112

- slug: `circulant-weighing-matrix-112-36`
- title: circulant-weighing-matrix-112-36
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `69`
- single-solve-to-paper fraction: `0.72`

## statement
Determine whether there exists a circulant weighing matrix of order 112 and weight 36.

## novelty_notes
- frontier basis: CW(112,36) is one of the explicitly surviving weight-36 cases in the post-elimination Strassler/Gordon frontier.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The paper frame is already present in the source because the residual table and multiplier tools are in place. A decisive resolution would mainly need the exact certificate and a brief explanation of how it interacts with the known orbit structure.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Publication-shaped but not lane-eligible because the shortest plausible route still appears search-heavy and certificate-driven.

## likely_paper_shape
- note title: A Residual Weight-36 Circulant Weighing Matrix Case at Order 112
- hypothetical title: On the Existence of CW(112,36)
- paper shape: A one-theorem residual-case note for a surviving weight-36 circulant weighing-matrix parameter.
- publication if solved: A construction or nonexistence proof for CW(112,36) would support a residual-case note on the current weight-36 circulant weighing-matrix frontier.
- minimal artifact requirements: Either an explicit CW(112,36) first row or a compact orbit-exhaust/nonexistence certificate.

## hypothetical_abstract
We determine the existence status of the circulant weighing matrix CW(112,36). The current Gordon update to Strassler's table leaves this parameter on the short residual weight-36 list after the available multiplier eliminations. Any exact resolution would therefore yield a self-contained residual-case note, although the likely proof route still looks computational.

## single_solve_explanation
A solution would already provide the core theorem, because the literature has compressed the surrounding context to a finite residual frontier. Only brief packaging would remain: restating the frontier, fixing notation, and presenting the decisive certificate. The risk is that the certificate may still depend on a moderately heavy exhaustive orbit search.

## broader_theorem_nonimplication
The residual-table framing in the Arasu-Gordon-Zhang paper and Gordon repository shows that current published multiplier theory has not already absorbed CW(112,36) into a broader theorem.

## literature_gap
The post-2019 residual weight-36 list still includes CW(112,36), with no later resolution surfaced in the bounded curation audit.

## transfer_kit
- lemma: Theorem 2.1 gives the self-conjugacy obstruction on folded intersection numbers.
- lemma: Theorem 2.2 gives multiplier-fixed translates and orbit decompositions for candidate supports.
- lemma: Lemma 1 supplies the exact folded equations that must be satisfied before any exhaustive check.
- lemma: Theorem 4.1 is the contracted-multiplier tool the source uses for residual open cases without easy hand proofs.
- toy example: The paper's smaller hand-eliminated cases illustrate how orbit tables and folded equations can collapse an open CW(n,36)-style parameter to a finite contradiction.
- known obstruction: This parameter survives the currently published multiplier filters, so a proof must sharpen those filters or finish the remaining narrowed search.
- prior-work stop sentence: The current Strassler/Gordon frontier still lists CW(112,36) as unresolved after the published eliminations.
- recommended first attack: Build the contracted-multiplier orbit table specific to n = 112 and test whether the surviving folded-equation solutions can all be killed by a short bounded exhaust.
- paper if solved: If solved exactly, the paper would be a residual-case note for the order-112 weight-36 circulant weighing-matrix problem.

## bounded_source_list
- Daniel M. Gordon, Circulant Weighing Matrices (La Jolla Combinatorics Repository / Jupyter Book, 2022; GitHub dataset release visible as May 16, 2025), together with K.T. Arasu, Daniel M. Gordon, and Yiran Zhang, "New Nonexistence Results on Circulant Weighing Matrices" (arXiv:1908.08447, consulted via arXiv/ar5iv on 2026-04-15), especially Section 5 / Table 10 listing the surviving open weight-36 cases including CW(112,36).
- Tan's update of Strassler's table, the Arasu-Gordon-Zhang elimination paper, and the Gordon repository snapshot.
- artifacts/circulant-weighing-matrix-112-36/record.md
- artifacts/circulant-weighing-matrix-112-36/status.json
