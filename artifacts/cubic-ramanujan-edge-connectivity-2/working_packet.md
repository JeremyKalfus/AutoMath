# Working Packet: Cubic Ramanujan Graphs of Edge-Connectivity Two

- slug: `cubic-ramanujan-edge-connectivity-2`
- title: Are there only finitely many cubic Ramanujan graphs with edge-connectivity 2?
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `69`
- single-solve-to-paper fraction: `0.66`

## statement
Either prove that only finitely many cubic Ramanujan graphs have edge-connectivity 2 or construct an infinite family of cubic Ramanujan graphs with edge-connectivity 2.

## novelty_notes
- frontier basis: The 2023 paper proves the edge-connectivity-1 case is finite and explicitly leaves the edge-connectivity-2 cubic case open after exhibiting many 20-vertex examples.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath slug, title, source anchor, or near-duplicate attempt for the cubic Ramanujan edge-connectivity-2 finiteness question.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A resolution would still be publishable, but the source itself points to a broad persistence phenomenon with many 20-vertex examples, so the route looks more like a compact program than a one-shot residue closure.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: small
- assessment: Fail for the strict lane: the statement is crisp and publishable, but the 20-vertex density of examples makes the likely route too search-heavy and program-like for the one-shot micro-paper objective.

## likely_paper_shape
- note title: Cubic Ramanujan Graphs of Edge-Connectivity Two
- hypothetical title: Cubic Ramanujan Graphs of Edge-Connectivity Two
- paper shape: A cubic-Ramanujan finiteness note, likely mixing structure and computation.
- publication if solved: A complete finiteness or infinitude theorem for cubic Ramanujan graphs of edge-connectivity 2 would be publishable, but it is less tightly micro-paper-shaped than the top four entries.
- minimal artifact requirements: Either a theorem forcing an absolute size bound on cubic edge-connectivity-2 Ramanujan graphs together with verification of the remaining small cases, or an explicit infinite family with spectral certification.

## hypothetical_abstract
We determine whether the family of cubic Ramanujan graphs with edge-connectivity 2 is finite. The 2023 Ramanujan rigidity paper showed that the edge-connectivity-1 case is finite and reported many small edge-connectivity-2 examples, leaving the global finiteness question open. We resolve that question by proving either finiteness with an explicit bound or infinitude via a concrete family.

## single_solve_explanation
A full finiteness or infinitude theorem would certainly be a paper. The target fails the strict lane because the known 20-vertex census already shows a large persistent family, so the shortest plausible route now looks like a structural-plus-computational campaign rather than one compact solve. That keeps the publication value real while making the solve-to-paper distance longer than the top four entries.

## broader_theorem_nonimplication
The 2023 paper proves only the edge-connectivity-1 case and explicitly says it leaves the edge-connectivity-2 cubic case open.

## literature_gap
After proving no cubic Ramanujan graph with edge-connectivity 1 exists above 20 vertices, the 2023 paper still leaves open whether edge-connectivity-2 cubic Ramanujan graphs form a finite family.

## transfer_kit
- lemma: The 2023 paper proves cubic Ramanujan graphs with edge-connectivity 1 are completely bounded and absent above 20 vertices.
- lemma: The same paper records 85,046 cubic Ramanujan graphs on 20 vertices with edge-connectivity 2, showing the phenomenon is real but still localized in known computations.
- lemma: The open-problem discussion explicitly conjectures finiteness for the edge-connectivity-2 cubic case.
- toy example: The 20-vertex edge-connectivity-2 cubic Ramanujan examples in the 2023 paper are the smallest concrete models for testing any finiteness mechanism.
- known obstruction: Unlike the cut-edge case, the edge-connectivity-2 class already has 85,046 examples on 20 vertices, so a proof of finiteness must explain a genuinely persistent but apparently bounded phenomenon.
- prior-work stop sentence: The 2023 paper proves finiteness for the edge-connectivity-1 cubic case and then leaves the edge-connectivity-2 cubic case open.
- recommended first attack: Look for a spectral obstruction to 2-edge cuts whose strength grows with order, starting from the decomposition patterns seen in the computed 20-vertex examples.
- paper if solved: The paper would be a cubic-Ramanujan finiteness note, but it sits outside the preferred micro-paper lane.

## bounded_source_list
- Sebastian M. Cioaba, Sean Dewar, Georg Grasegger, and Xiaofeng Gu, "Graph Rigidity Properties of Ramanujan Graphs" (Electronic Journal of Combinatorics 30(3), 2023), especially the open-question discussion after Proposition 36.
- The 2023 Ramanujan rigidity paper, 2026-04-13 exact-statement and alternate-notation searches on the edge-connectivity-2 finiteness question, the source's open-problem discussion, and bounded 2024-2026 status searches that did not surface a resolution.
- artifacts/cubic-ramanujan-edge-connectivity-2/record.md
- artifacts/cubic-ramanujan-edge-connectivity-2/status.json
