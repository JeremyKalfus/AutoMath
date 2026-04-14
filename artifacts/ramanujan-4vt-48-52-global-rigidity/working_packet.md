# Working Packet: The 48- and 52-Vertex Residue for 4-Regular Vertex-Transitive Ramanujan Graphs

- slug: `ramanujan-4vt-48-52-global-rigidity`
- title: Do any 4-regular vertex-transitive Ramanujan graphs on 48 or 52 vertices fail global rigidity?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.79`

## statement
Either prove that every 4-regular vertex-transitive Ramanujan graph on 48 or 52 vertices is globally rigid in R^2, thereby sharpening the 53-vertex threshold from Theorem 3, or exhibit a non-globally-rigid Ramanujan graph at one of those two orders.

## novelty_notes
- frontier basis: Cioaba-Dewar-Grasegger-Gu prove every 4-regular vertex-transitive Ramanujan graph is globally rigid in R^2 once the order is at least 53 and note that the only cases left to check are 48 and 52 vertices.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath slug, title, source anchor, or near-duplicate attempt for the exact 48/52-vertex residue in the 4-regular vertex-transitive Ramanujan rigidity problem.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The literature already provides the global theorem, the small-order computations up to 47 vertices, and the structural reason only 48 and 52 remain; after the solve, the paper mostly needs the residue certification and the threshold update.
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
- certificate compactness: low
- exact gap from source: tiny
- assessment: Pass: the theorem slice is stable, the residue is tiny and explicit, and one exact solve would already read like the main theorem of a short bound-sharpening note.

## likely_paper_shape
- note title: The 48- and 52-Vertex Residue for 4-Regular Vertex-Transitive Ramanujan Graphs
- hypothetical title: The 48- and 52-Vertex Residue for 4-Regular Vertex-Transitive Ramanujan Graphs
- paper shape: A finite-residue sharpening note that either lowers the 53-vertex threshold or supplies the exact exceptional order.
- publication if solved: Resolving the 48/52-vertex residue would sharpen the exact bound in the 2023 Ramanujan rigidity theorem and would naturally support a short finite-residue note.
- minimal artifact requirements: Either a certified check that every 48- and 52-vertex 4-regular vertex-transitive Ramanujan graph is globally rigid in R^2, or one explicit Ramanujan counterexample at one of those two orders.

## hypothetical_abstract
We resolve the only remaining finite residue in the 4-regular vertex-transitive Ramanujan global-rigidity problem. Cioaba, Dewar, Grasegger, and Gu proved in 2023 that every such graph of order at least 53 is globally rigid in R^2 and reduced the remaining uncertainty to orders 48 and 52. We determine whether those two orders contain any non-globally-rigid examples and thereby sharpen the exact threshold.

## single_solve_explanation
The ambient theorem and the reduction to two explicit orders are already published. If both orders are positive, the note is a clean threshold-improvement paper; if one order fails, the note is a compact exceptional-example paper. In either direction, the residue solve supplies almost the whole paper.

## broader_theorem_nonimplication
The later 2024 rigidity paper characterizes global rigidity for general 4-regular graphs via connectivity properties, but it does not classify which 4-regular vertex-transitive Ramanujan graphs occur at orders 48 and 52 or whether they satisfy that characterization.

## literature_gap
The literature proves the 4-regular vertex-transitive Ramanujan statement for orders at least 53 and for all checked orders up to 47, but leaves exactly the 48- and 52-vertex residue unresolved.

## transfer_kit
- lemma: Theorem 3 of the 2023 source proves every 4-regular vertex-transitive Ramanujan graph with at least 53 vertices is globally rigid in R^2.
- lemma: The same source checks all 4-regular vertex-transitive Ramanujan graphs up to 47 vertices and isolates 48 and 52 as the only unresolved orders.
- lemma: The 2024 paper on four-regular extremal rigidity shows that a 4-regular graph is 2-vertex globally rigid exactly when it is 4-vertex-connected and essentially 6-edge-connected, giving a compact certification target for any candidate graph.
- toy example: The non-rigid and rigid-but-not-globally-rigid 4-regular vertex-transitive Ramanujan examples displayed in the 2023 paper show the obstruction pattern below the unresolved 48/52 residue.
- known obstruction: Known small non-rigid examples force any surviving unresolved case to follow the one-4-clique-per-vertex divisibility pattern, which is why only orders divisible by 4 remain.
- prior-work stop sentence: The 2023 Ramanujan rigidity paper proves the >=53 case and then states that the only cases left to check are 48 and 52 vertices.
- recommended first attack: Use the Royle-Holt vertex-transitive graph data and the 2024 four-regular connectivity characterization to certify the 48- and 52-vertex Ramanujan candidates one order at a time.
- paper if solved: The paper would be a short finite-residue note sharpening the exact threshold in the 4-regular vertex-transitive Ramanujan global-rigidity theorem.

## bounded_source_list
- Sebastian M. Cioaba, Sean Dewar, Georg Grasegger, and Xiaofeng Gu, "Graph Rigidity Properties of Ramanujan Graphs" (Electronic Journal of Combinatorics 30(3), 2023).
- The 2023 Ramanujan rigidity paper, the 2024 four-regular rigidity paper giving a connectivity characterization for 4-regular global rigidity, 2026-04-13 exact-statement and alternate-notation searches on the 48/52 residue, source-internal theorem checks, and bounded 2024-2026 status searches that did not surface a completed resolution.
- artifacts/ramanujan-4vt-48-52-global-rigidity/record.md
- artifacts/ramanujan-4vt-48-52-global-rigidity/status.json
