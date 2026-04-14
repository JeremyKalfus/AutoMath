# Is every 7-regular Ramanujan graph globally rigid in R^2?

- entry_type: `paper_candidate`
- slug: `ramanujan-7-global-rigidity`
- worker_role: `solver-B`
- canonical_source: `Sebastian M. Cioaba, Sean Dewar, Georg Grasegger, and Xiaofeng Gu, "Graph Rigidity Properties of Ramanujan Graphs" (Electronic Journal of Combinatorics 30(3), 2023).`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing the k = 7 case would settle one of the two remaining open degrees in the exact-all-orders Ramanujan global-rigidity question and would make a credible short note.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `80`
- single_solve_to_paper_fraction: `0.77`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `moderate`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `small`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `high`
- packaging_risk: `moderate`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/ramanujan-7-global-rigidity/working_packet.md`
- paper_shape: `A finite-residue completion note combining the 2023 asymptotic theorem with exact treatment of the unresolved 7-regular small orders.`

## question
Does every 7-regular Ramanujan graph have global rigidity in the plane, or does a counterexample exist among the unresolved small orders?

## canonical_statement
Determine whether all 7-regular Ramanujan graphs are globally rigid in R^2.

## intended_statement
Either prove that every 7-regular Ramanujan graph is globally rigid in R^2 or exhibit a 7-regular Ramanujan graph that is not globally rigid in R^2.

## pre_solve_gate_reason
The 2023 source reduces the open k = 7 case to a finite small-order residue and explicitly notes that only orders 16, 18, and 20 remain to be checked.

## micro_paper_assessment
Pass, but less clean than the top two entries: the theorem slice is stable and near-paper, though the residue likely needs certified computation rather than a purely conceptual proof.

## hypothetical_title
Global Rigidity of 7-Regular Ramanujan Graphs

## hypothetical_abstract
We settle the remaining exact-degree question for planar global rigidity of 7-regular Ramanujan graphs. A 2023 theorem proved the statement for sufficiently large order and reduced the unresolved residue to finitely many small orders; we complete that residue analysis. This determines whether every 7-regular Ramanujan graph is globally rigid in R^2.

## single_solve_paper_explanation
The current paper already contains the asymptotic theorem and the finite-reduction observation, so the unresolved residue is sharply isolated. If the small orders all work, the note is a finite-residue completion paper; if one fails, the note is a compact counterexample paper. In both cases the one exact solve contributes most of the final paper.

## broader_theorem_nonimplication_note
The 2023 theorem proves the statement only for sufficiently large order and explicitly says the exact all-orders k = 7 case still requires checking the 16-, 18-, and 20-vertex residues.

## literature_gap
The literature proves all sufficiently large 7-regular Ramanujan graphs are globally rigid in R^2 but does not settle the all-orders statement because the small orders 16, 18, and 20 remain unresolved.

## publication_packet_title
Global Rigidity of 7-Regular Ramanujan Graphs

## publication_packet_frontier_basis
Cioaba-Dewar-Grasegger-Gu prove all sufficiently large 7-regular Ramanujan graphs are globally rigid and record that the all-orders statement remains open only through finitely many small orders.

## publication_packet_near_paper_reason
The asymptotic theory, motivation, and computational tables are already published; after the solve, the paper mostly needs the residue analysis or counterexample and a short integration with the 2023 theorem.

## publication_packet_literature_scope
The 2023 Ramanujan rigidity paper, exact-statement searches for the k = 7 problem, finite-order residue information inside Section 6, and bounded post-2023 status checks that did not surface a completed k = 7 resolution.

## publication_packet_artifact_requirements
Either a full argument or certified computation showing every 7-regular Ramanujan graph of orders 16, 18, and 20 is globally rigid, or one explicit non-globally-rigid 7-regular Ramanujan counterexample.

## paper_shape
A finite-residue completion note combining the 2023 asymptotic theorem with exact treatment of the unresolved 7-regular small orders.

## transfer_kit

### usable_lemmas
- The 2023 paper proves every 7-regular Ramanujan graph with more than 22 vertices is globally rigid in R^2.
- Its open-problems section records that any 7-regular counterexample must have more than 14 vertices and that only orders 16, 18, and 20 remain to be checked.
- The paper already supplies the connectivity and spectral machinery linking Ramanujan bounds to global rigidity.

### toy_example
The already-checked orders up to 14 provide the smallest verified side of the finite residue and show how the computational certification is meant to look.

### known_obstruction
The remaining proof burden may collapse into explicit finite enumeration of 7-regular Ramanujan graphs at three small orders rather than a new conceptual theorem.

### prior_work_stop_sentence
The 2023 Ramanujan rigidity paper stops with the exact k = 7 all-orders case unresolved and notes that only the 16-, 18-, and 20-vertex residues remain.

### recommended_first_attack
Exploit the paper's finite-reduction tables directly and certify the 16-, 18-, and 20-vertex cases one order at a time, prioritizing structural pruning before any exhaustive generation.

### paper_if_solved
The paper would be a short finite-residue completion note for the exact k = 7 Ramanujan global-rigidity problem.
