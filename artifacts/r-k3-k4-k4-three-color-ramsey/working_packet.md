# Working Packet: The Exact Value of R(K3, K4, K4)

- slug: `r-k3-k4-k4-three-color-ramsey`
- title: Determine the exact value of R(K3, K4, K4)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `81`
- single-solve-to-paper fraction: `0.8`

## statement
Determine the least n such that every 3-coloring of E(K_n) contains either a color-1 K3, a color-2 K4, or a color-3 K4.

## novelty_notes
- frontier basis: Current public sources leave the three-color clique Ramsey number at 21 <= R(K3, K4, K4) <= 22. The live frontier is therefore a single unresolved binary endpoint with standard notation and clear table value.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: Once the endpoint is fixed, the paper is almost entirely the proof or critical coloring. The surrounding exposition is routine because the question is already in standard Ramsey notation and needs little setup.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: moderate
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass. The family anchor is a bit lighter than the two-color cases, but the one-step gap and compact theorem statement keep it inside the micro-paper lane.

## likely_paper_shape
- note title: The Exact Value of R(K3, K4, K4)
- hypothetical title: The Exact Value of R(K3, K4, K4)
- paper shape: A one-theorem exact-value note for a one-step three-color clique Ramsey number.
- publication if solved: An exact determination of R(K3, K4, K4) would support a compact note because the public frontier is already a one-step gap with a clean three-color statement.
- minimal artifact requirements: Either an explicit 21-vertex 3-coloring with no monochromatic K3, K4, K4 in the designated colors or a proof that every 3-coloring of K22 forces one of them.

## hypothetical_abstract
We determine the three-color Ramsey number R(K3, K4, K4). The best public bounds after the 2021 semidefinite-programming improvement are 21 <= R(K3, K4, K4) <= 22. Our result closes the remaining one-step gap and completes this small three-color clique entry.

## single_solve_explanation
The exact value is already the full story here, not a feeder lemma. Because the gap is one step, a successful lower-bound construction or one-vertex forcing proof would contribute most of the eventual paper. The remaining work is mainly exposition and a compact extremal certificate.

## broader_theorem_nonimplication
General multicolor clique bounds do not decide 21 versus 22, and no broader theorem located in the bounded audit collapses this case automatically.

## literature_gap
Current public sources stop at 21 <= R(K3, K4, K4) <= 22.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 8, gives the upper bound R(K3, K4, K4) <= 22.
- lemma: The same theorem table records the known lower bound R(K3, K4, K4) >= 21 from earlier literature.
- lemma: Standard color-merging monotonicity gives easy sanity bounds from adjacent three-color clique entries without deciding the exact endpoint.
- lemma: The 2021 paper's SDP framework is explicitly designed to extract small-graph local constraints for Ramsey extremal colorings.
- toy example: The literature already certifies the existence of a 21-vertex coloring avoiding a monochromatic K3 in one color and K4 in each of the other two colors.
- known obstruction: A lower-bound construction must balance two different K4-avoidance conditions while also avoiding a triangle in the third color, which sharply restricts local color densities.
- prior-work stop sentence: Current sources stop at 21 <= R(K3, K4, K4) <= 22.
- recommended first attack: Start from the SDP upper-bound profile and classify allowed colored neighborhood types around a vertex; then attempt a constrained extension search from the 21-vertex lower-bound side.
- paper if solved: The paper would be a concise exact-value note on a small three-color clique Ramsey number.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 8, which gives 21 <= R(K3, K4, K4) <= 22; together with bounded 2026-04-14 exact-notation and recent-status web checks that did not reveal a later exact closure.
- 2021 Lidicky-Pfender theorem table plus bounded 2026-04-14 exact-notation and recent-status web checks.
- artifacts/r-k3-k4-k4-three-color-ramsey/record.md
- artifacts/r-k3-k4-k4-three-color-ramsey/status.json
