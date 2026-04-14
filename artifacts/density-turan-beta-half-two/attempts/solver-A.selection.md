# Is beta(1/2,2) equal to 1/50 in the density version of Turan's theorem?

- entry_type: `paper_candidate`
- slug: `density-turan-beta-half-two`
- worker_role: `solver-A`
- canonical_source: `Douglas West, "Density Version of Turan's Theorem" problem page, summarizing Erdos, Faudree, Rousseau, and Schelp's 1990 conjecture that beta(1/2,2) = 1/50.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Resolving the Erdos-Faudree-Rousseau-Schelp half-set threshold exactly would already be the title theorem of a short extremal graph note.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium_low`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.78`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `moderate`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `moderate`
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
- working_packet_path: `artifacts/density-turan-beta-half-two/working_packet.md`
- paper_shape: `A single sharp threshold theorem for one named local-density extremal constant.`

## question
In a triangle-free n-vertex graph, is 1/50 the sharp forcing threshold for the edge density induced by every n/2-vertex subset?

## canonical_statement
Determine whether beta(1/2,2) = 1/50.

## intended_statement
Either prove that every triangle-free graph with all n/2-subsets inducing more than n^2/50 edges contains a triangle, or construct a sharper triangle-free extremal family showing that 1/50 is not the correct threshold.

## pre_solve_gate_reason
The source literature isolates one exact constant, provides an explicit lower-bound construction, and frames the result as a standalone extremal threshold rather than a feeder instance.

## micro_paper_assessment
Pass, but less crisp than the K_9 decomposition exception: the target is exact and paper-shaped, though the proof could lean on heavier extremal machinery than the final note length suggests.

## hypothetical_title
The Half-Set Density Threshold in Triangle-Free Graphs

## hypothetical_abstract
We resolve the Erdos-Faudree-Rousseau-Schelp problem asking whether beta(1/2,2) equals 1/50. We either prove that 1/50 is the sharp half-set density threshold forcing a triangle or exhibit a triangle-free extremal construction with a strictly larger value. Since the lower-bound family and the exact conjectural constant are already fixed in the literature, the solve itself would provide the main theorem and most of the note.

## single_solve_paper_explanation
This candidate already has a crisp title theorem and an obvious paper packet: one exact constant, one lower-bound construction, and one sharp upper bound or counterexample. The argument may use broader extremal tools, but the honest headline remains the half-set threshold because that exact constant is the published target. After the solve, what remains is mostly contextual framing and sharpening the extremal discussion.

## broader_theorem_nonimplication_note
The published background provides lower bounds and general inequalities for beta(alpha,r), but the exact half-set triangle-free constant beta(1/2,2) is explicitly posed as an open problem rather than a corollary of a broader theorem.

## literature_gap
The canonical source records the lower bound beta(1/2,2) >= 1/50 from blowups of C_5 or the Petersen graph and leaves the matching upper bound open.

## publication_packet_title
The Half-Set Density Threshold in Triangle-Free Graphs

## publication_packet_frontier_basis
West's page records the exact conjecture beta(1/2,2) = 1/50 and notes the matching lower-bound construction via blowups of C_5 or the Petersen graph.

## publication_packet_near_paper_reason
The paper architecture is fixed in advance: define beta(alpha,2), recall the standard lower bound, and prove the exact upper bound or produce a sharper construction.

## publication_packet_literature_scope
The 1990 EFRS problem as summarized by West, exact-statement and alternate-notation searches for beta(1/2,2), and bounded later-status checks for a settled sharp constant.

## publication_packet_artifact_requirements
Either a sharp upper-bound proof with a stability argument or a new triangle-free construction beating the 1/50 benchmark.

## paper_shape
A single sharp threshold theorem for one named local-density extremal constant.

## transfer_kit

### usable_lemmas
- The lower bound beta(1/2,2) >= 1/50 comes from balanced blowups of C_5 and also from the Petersen graph construction highlighted on the canonical problem page.
- The problem is already isolated at one exact parameter pair alpha = 1/2, r = 2, so the theorem statement does not depend on resolving the whole beta(alpha,r) landscape.
- Any sharp result naturally packages with a stability discussion around the known lower-bound examples.

### toy_example
Balanced blowups of C_5 provide the standard model example: they are triangle-free and witness the 1/50 lower bound on half-set induced density.

### known_obstruction
The known lower-bound constructions are highly symmetric and locally dense on large subsets, so naive averaging arguments do not force triangles at the conjectured threshold.

### prior_work_stop_sentence
The published problem record gives the lower bound beta(1/2,2) >= 1/50 and stops before proving the matching upper bound.

### recommended_first_attack
Use a stability-first extremal approach centered on near blowups of C_5 or Petersen-type examples, then convert the structural control into a sharp half-set upper bound.

### paper_if_solved
The paper would be a short sharp-threshold extremal note built around one exact constant, one extremal family section, and one proof section.
