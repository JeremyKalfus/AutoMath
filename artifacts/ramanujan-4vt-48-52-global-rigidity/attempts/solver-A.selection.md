# Do any 4-regular vertex-transitive Ramanujan graphs on 48 or 52 vertices fail global rigidity?

- entry_type: `paper_candidate`
- slug: `ramanujan-4vt-48-52-global-rigidity`
- worker_role: `solver-A`
- canonical_source: `Sebastian M. Cioaba, Sean Dewar, Georg Grasegger, and Xiaofeng Gu, "Graph Rigidity Properties of Ramanujan Graphs" (Electronic Journal of Combinatorics 30(3), 2023).`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Resolving the 48/52-vertex residue would sharpen the exact bound in the 2023 Ramanujan rigidity theorem and would naturally support a short finite-residue note.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.79`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/ramanujan-4vt-48-52-global-rigidity/working_packet.md`
- paper_shape: `A finite-residue sharpening note that either lowers the 53-vertex threshold or supplies the exact exceptional order.`

## question
Is every 4-regular vertex-transitive Ramanujan graph on 48 or 52 vertices globally rigid in R^2, or does one of those two remaining orders contain a non-globally-rigid example?

## canonical_statement
Determine whether any 4-regular vertex-transitive Ramanujan graph on 48 or 52 vertices is not globally rigid in R^2.

## intended_statement
Either prove that every 4-regular vertex-transitive Ramanujan graph on 48 or 52 vertices is globally rigid in R^2, thereby sharpening the 53-vertex threshold from Theorem 3, or exhibit a non-globally-rigid Ramanujan graph at one of those two orders.

## pre_solve_gate_reason
The 2023 source reduces the unresolved 4-regular vertex-transitive Ramanujan case to exactly two orders, 48 and 52, after checking all smaller orders and proving the >=53 theorem.

## micro_paper_assessment
Pass: the theorem slice is stable, the residue is tiny and explicit, and one exact solve would already read like the main theorem of a short bound-sharpening note.

## hypothetical_title
The 48- and 52-Vertex Residue for 4-Regular Vertex-Transitive Ramanujan Graphs

## hypothetical_abstract
We resolve the only remaining finite residue in the 4-regular vertex-transitive Ramanujan global-rigidity problem. Cioaba, Dewar, Grasegger, and Gu proved in 2023 that every such graph of order at least 53 is globally rigid in R^2 and reduced the remaining uncertainty to orders 48 and 52. We determine whether those two orders contain any non-globally-rigid examples and thereby sharpen the exact threshold.

## single_solve_paper_explanation
The ambient theorem and the reduction to two explicit orders are already published. If both orders are positive, the note is a clean threshold-improvement paper; if one order fails, the note is a compact exceptional-example paper. In either direction, the residue solve supplies almost the whole paper.

## broader_theorem_nonimplication_note
The later 2024 rigidity paper characterizes global rigidity for general 4-regular graphs via connectivity properties, but it does not classify which 4-regular vertex-transitive Ramanujan graphs occur at orders 48 and 52 or whether they satisfy that characterization.

## literature_gap
The literature proves the 4-regular vertex-transitive Ramanujan statement for orders at least 53 and for all checked orders up to 47, but leaves exactly the 48- and 52-vertex residue unresolved.

## publication_packet_title
The 48- and 52-Vertex Residue for 4-Regular Vertex-Transitive Ramanujan Graphs

## publication_packet_frontier_basis
Cioaba-Dewar-Grasegger-Gu prove every 4-regular vertex-transitive Ramanujan graph is globally rigid in R^2 once the order is at least 53 and note that the only cases left to check are 48 and 52 vertices.

## publication_packet_near_paper_reason
The literature already provides the global theorem, the small-order computations up to 47 vertices, and the structural reason only 48 and 52 remain; after the solve, the paper mostly needs the residue certification and the threshold update.

## publication_packet_literature_scope
The 2023 Ramanujan rigidity paper, the 2024 four-regular rigidity paper giving a connectivity characterization for 4-regular global rigidity, exact-order searches on the 48/52 residue, and bounded 2024-2026 status checks that did not surface a completed resolution.

## publication_packet_artifact_requirements
Either a certified check that every 48- and 52-vertex 4-regular vertex-transitive Ramanujan graph is globally rigid in R^2, or one explicit Ramanujan counterexample at one of those two orders.

## paper_shape
A finite-residue sharpening note that either lowers the 53-vertex threshold or supplies the exact exceptional order.

## transfer_kit

### usable_lemmas
- Theorem 3 of the 2023 source proves every 4-regular vertex-transitive Ramanujan graph with at least 53 vertices is globally rigid in R^2.
- The same source checks all 4-regular vertex-transitive Ramanujan graphs up to 47 vertices and isolates 48 and 52 as the only unresolved orders.
- The 2024 paper on four-regular extremal rigidity shows that a 4-regular graph is 2-vertex globally rigid exactly when it is 4-vertex-connected and essentially 6-edge-connected, giving a compact certification target for any candidate graph.

### toy_example
The non-rigid and rigid-but-not-globally-rigid 4-regular vertex-transitive Ramanujan examples displayed in the 2023 paper show the obstruction pattern below the unresolved 48/52 residue.

### known_obstruction
Known small non-rigid examples force any surviving unresolved case to follow the one-4-clique-per-vertex divisibility pattern, which is why only orders divisible by 4 remain.

### prior_work_stop_sentence
The 2023 Ramanujan rigidity paper proves the >=53 case and then states that the only cases left to check are 48 and 52 vertices.

### recommended_first_attack
Use the Royle-Holt vertex-transitive graph data and the 2024 four-regular connectivity characterization to certify the 48- and 52-vertex Ramanujan candidates one order at a time.

### paper_if_solved
The paper would be a short finite-residue note sharpening the exact threshold in the 4-regular vertex-transitive Ramanujan global-rigidity theorem.
