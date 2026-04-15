# Working Packet: A Residual Weight-36 Circulant Weighing Matrix Case at Order 117

- slug: `circulant-weighing-matrix-117-36`
- title: circulant-weighing-matrix-117-36
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `66`
- single-solve-to-paper fraction: `0.7`

## statement
Determine whether there exists a circulant weighing matrix of order 117 and weight 36.

## novelty_notes
- frontier basis: CW(117,36) appears in the residual weight-36 list that remains after the Arasu-Gordon-Zhang eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A decisive result would drop directly into a short note because the frontier basis and proof ingredients are already standardized in the source. The only serious question is how computational the final certificate becomes.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Viable residual-case note if solved, but not lane-eligible because the most plausible proof still looks too certificate-driven.

## likely_paper_shape
- note title: A Residual Weight-36 Circulant Weighing Matrix Case at Order 117
- hypothetical title: On the Existence of CW(117,36)
- paper shape: A one-theorem residual-case note for one surviving weight-36 circulant weighing-matrix parameter.
- publication if solved: A construction or nonexistence proof for CW(117,36) would support a short residual-case note inside the current weight-36 circulant weighing-matrix frontier.
- minimal artifact requirements: Either an explicit CW(117,36) first row or a compact orbit-exhaust/nonexistence certificate.

## hypothetical_abstract
We determine the existence status of the circulant weighing matrix CW(117,36). The current Strassler/Gordon frontier leaves this parameter in the short residual weight-36 list that survives the published multiplier eliminations. An exact resolution would therefore read as a standalone residual-case paper, but the likely route still appears certificate-heavy.

## single_solve_explanation
The solve itself would already provide most of the paper because the literature has isolated the parameter and supplied the multiplier framework. What would remain is a bounded writeup of the residual frontier and the exact argument or computation. The lane penalty comes from the likely dependence on a nontrivial exhaustive orbit check.

## broader_theorem_nonimplication
The published multiplier and contracted-multiplier theory still leaves CW(117,36) in the residual table, so it is not already implied by the broader known theory.

## literature_gap
The post-elimination residual weight-36 frontier still contains CW(117,36), with no later resolution surfaced in the bounded curation pass.

## transfer_kit
- lemma: Theorem 2.1 supplies the self-conjugacy obstruction on folded intersection numbers.
- lemma: Theorem 2.2 turns the existence problem into a union-of-orbits problem under multiplier action.
- lemma: Lemma 1 converts the orbit data into concrete folded equations.
- lemma: Theorem 4.1 supplies contracted multipliers for hard residual cases.
- toy example: The hand-checkable cases eliminated earlier in the Arasu-Gordon-Zhang paper are the template for converting orbit tables into exact contradictions.
- known obstruction: The published multiplier filters still leave genuine residue for CW(117,36), so a finish likely needs additional orbit pruning or exhaustive checking.
- prior-work stop sentence: The current Gordon residual list still contains CW(117,36) as an open weight-36 case.
- recommended first attack: Use the contracted-multiplier framework to enumerate the folded-equation residue for n = 117 and see whether every surviving orbit pattern can be excluded by a short exact check.
- paper if solved: If solved exactly, the paper would be a residual-case note on the order-117 weight-36 circulant weighing-matrix problem.

## bounded_source_list
- Daniel M. Gordon, Circulant Weighing Matrices (La Jolla Combinatorics Repository / Jupyter Book, 2022; GitHub dataset release visible as May 16, 2025), together with K.T. Arasu, Daniel M. Gordon, and Yiran Zhang, "New Nonexistence Results on Circulant Weighing Matrices" (arXiv:1908.08447, consulted via arXiv/ar5iv on 2026-04-15), especially Section 5 / Table 10 listing the surviving open weight-36 cases including CW(117,36).
- Tan's update of Strassler's table, Arasu-Gordon-Zhang, and Gordon's maintained CW repository.
- artifacts/circulant-weighing-matrix-117-36/record.md
- artifacts/circulant-weighing-matrix-117-36/status.json
