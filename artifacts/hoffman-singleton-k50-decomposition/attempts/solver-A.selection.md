# Does K_50 decompose into 7 copies of the Hoffman-Singleton graph?

- entry_type: `paper_candidate`
- slug: `hoffman-singleton-k50-decomposition`
- worker_role: `solver-A`
- canonical_source: `Douglas West, "Hoffman-Singleton Decomposition of K_50" open problem page, summarizing Meszka and Siagiova's five-copy packing result.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `A full decomposition or impossibility proof would already be the title theorem of a short graph-decomposition note centered on a named exceptional graph.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium-low`
- paper_leverage_score: `80`
- single_solve_to_paper_fraction: `0.82`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `small`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `medium`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/hoffman-singleton-k50-decomposition/working_packet.md`
- paper_shape: `A single exact decomposition theorem or exact obstruction theorem for one named exceptional graph.`

## question
Can the complete graph K_50 be edge-decomposed into seven pairwise edge-disjoint copies of the Hoffman-Singleton graph?

## canonical_statement
Determine whether K_50 decomposes into 7 copies of the Hoffman-Singleton graph.

## intended_statement
Either construct a full 7-copy edge decomposition of K_50 into Hoffman-Singleton graphs or prove that no such decomposition exists.

## pre_solve_gate_reason
The statement is exact, stable, already partially narrowed by a five-copy packing, and one clean completion or obstruction would supply almost the whole paper.

## micro_paper_assessment
Pass: the exact theorem is stable, the residual gap is concrete, and a single completion-or-obstruction result would already read like a short standalone paper rather than a feeder instance.

## hypothetical_title
A Hoffman-Singleton Decomposition of K_50

## hypothetical_abstract
We settle the exact decomposition problem asking whether K_50 splits into seven edge-disjoint Hoffman-Singleton graphs. Starting from the known packing of five copies, we either complete the decomposition by analyzing the 14-regular residual graph or prove that the final completion is impossible. Because the theorem statement is already fixed and the certificates are tiny, the solve itself would constitute most of a finished note.

## single_solve_paper_explanation
This target already has a referee-facing title theorem: either K_50 does decompose into seven Hoffman-Singleton graphs or it does not. The source literature gives a concrete partial foothold, so the remaining work is not a broad campaign but the exact completion or obstruction of the last gap. After the solve, what remains is mainly exposition of the five-copy precursor and a polished certificate.

## broader_theorem_nonimplication_note
Known general decomposition results do not force a decomposition into a specific exceptional strongly regular graph, and the best cited partial result stops at five edge-disjoint copies rather than settling the full seven-copy question.

## literature_gap
The cited partial result yields five edge-disjoint Hoffman-Singleton copies in K_50, and the exact seven-copy decomposition question remains open there.

## publication_packet_title
A Hoffman-Singleton Decomposition of K_50

## publication_packet_frontier_basis
West's problem page records the exact decomposition question and the known partial result of five edge-disjoint copies.

## publication_packet_near_paper_reason
The title, theorem statement, and verification format are fixed in advance; after the solve, little remains beyond proof cleanup and a short discussion of the five-copy precursor.

## publication_packet_literature_scope
The West open-problem page, the Hoffman-Singleton graph background, and the cited five-copy packing result.

## publication_packet_artifact_requirements
Either seven explicit edge-disjoint copies whose union is K_50 or a complete obstruction argument ruling out the final two copies.

## paper_shape
A single exact decomposition theorem or exact obstruction theorem for one named exceptional graph.

## transfer_kit

### usable_lemmas
- The Hoffman-Singleton graph has 50 vertices and 175 edges, so exactly seven copies are needed because 7 x 175 = |E(K_50)| = 1225.
- Each Hoffman-Singleton copy is 7-regular, so a packing of five copies leaves a 14-regular residual graph on the same vertex set.
- Meszka and Siagiova already produced five edge-disjoint copies, so the live residue is the exact structure of the leftover 14-regular complement.

### toy_example
The arithmetic sanity check 7 x 175 = 1225 and the existing five-copy packing together give the smallest nontrivial worked model: the problem is already reduced to understanding the residual 14-regular complement.

### known_obstruction
The two missing copies must fit globally and simultaneously, so local edge choices can fail because the residual graph must itself split into two Hoffman-Singleton copies.

### prior_work_stop_sentence
The cited partial result finds five edge-disjoint Hoffman-Singleton copies in K_50 and stops short of settling the full seven-copy decomposition.

### recommended_first_attack
Analyze the residual graph left by a five-copy packing and test whether its spectrum, local structure, or automorphisms can force or forbid a decomposition into two further Hoffman-Singleton copies.

### paper_if_solved
The paper would be a short exact decomposition note with one theorem, one certificate section, and a brief comparison to the known five-copy packing.
