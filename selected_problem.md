# Does every 5-regular pseudograph contain a {4,1}-factor?

- entry_type: `paper_candidate`
- slug: `five-regular-pseudograph-4-1-factor`
- family_name: `Regular graph {a,b}-factors`
- canonical_source: `Maria Axenovich and Jonathan Rollin, "Brooks type results for conflict-free colorings and {a,b}-factors in graphs" (Discrete Mathematics 338, 2015), plus Douglas West's regular-subgraph problem summary.`
- open_status_checked_on: `2026-04-12`
- attack_style: `minimal-counterexample plus cut/parity analysis through the mod-3 edge-label reformulation`
- curation_confidence: `medium-high`
- publication_status: `SLICE_CANDIDATE`
- campaign_affinity: `none`
- publication_if_solved: `A full resolution of the smallest unresolved Akbari-Kano-type odd-degree case would already read like a short standalone paper.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `91`
- single_solve_to_paper_fraction: `0.86`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `small`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low-medium`
- formalization_overhead: `low-medium`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `excellent`
- working_packet_path: `artifacts/five-regular-pseudograph-4-1-factor/working_packet.md`
- paper_shape: `One exact theorem or counterexample package, with a brief structural section around the mod-3 reformulation and a short obstruction discussion.`

## question
Is every 5-regular pseudograph guaranteed to have a spanning subgraph in which every vertex has degree 4 or 1?

## canonical_statement
Every 5-regular pseudograph contains a {4,1}-factor.

## intended_statement
Resolve the exact 5-regular pseudograph case, either by proving every such pseudograph has a {4,1}-factor or by exhibiting a genuine counterexample.

## theorem_slice_hint
Exploit the mod-3 edge-label equivalence and rule out reducible local configurations in a vertex-minimal counterexample.

## why_reasoning_friendly
The statement is crisp, parity-heavy, and already has a known equivalent reformulation, so the search surface is much closer to a direct proof than to a campaign.

## why_low_token
The object is tiny to state, the verifier is just local degree bookkeeping, and the mod-3 formulation keeps the proof surface narrow.

## verifier_hint
For a positive solve, verify the spanning subgraph degrees directly; for a negative solve, preserve the exact counterexample and the argument excluding every {4,1}-factor.

## lean_hint
If the theorem closes, formalize only the local degree bookkeeping and the reformulation needed for the final statement; do not front-load Lean.

## rediscovery_risk
low-medium

## why_still_appears_open
The 2015 paper explicitly leaves the r = 5, t = 1 case open after disproving the broader odd-r conjecture, and the bounded status sweep surfaced only summary material still pointing to the same residue.

## why_this_could_be_publishable
It is a named-conjecture residue with a clean yes-or-no endpoint, tiny verifier, and immediate title theorem if solved.

## pre_solve_gate_reason
The 2015 paper isolates this exact residue after the larger odd-degree failures, so one solve is already most of a paper with no feeder ladder.

## micro_paper_assessment
Pass: this is a named-conjecture residue with a strong title theorem, low editorial overhead, and a direct note narrative once solved.

## hypothetical_title
The {4,1}-Factor Problem for 5-Regular Pseudographs

## hypothetical_abstract
We settle the 5-regular pseudograph case of the Akbari-Kano {1,4}-factor problem. Using the mod-3 edge-label reformulation and a minimal-counterexample analysis, we either prove that every 5-regular pseudograph admits a {4,1}-factor or isolate a genuine minimal obstruction. This closes the smallest surviving odd-degree residue after the 2015 counterexamples and leaves only routine framing and formal sealing.

## single_solve_paper_explanation
The source already supplies the broader conjectural frame and the negative larger-odd-degree background, so the remaining narrative is almost forced. Once the 5-regular residue is solved, the paper mainly needs a short introduction, the exact proof or obstruction, and one brief discussion of how the 2015 reformulation pinpoints the last odd-degree gap. No feeder ladder or second theorem program is needed.

## broader_theorem_nonimplication_note
The 2015 paper disproves the broader odd-r conjecture for larger odd degrees but explicitly isolates the 5-regular pseudograph case as the remaining residue; those broader counterexamples do not settle this exact low-degree endpoint.

## literature_gap
Prior work reaches the reformulation, proves counterexamples for larger odd r, and then stops with the exact 5-regular pseudograph {4,1}-factor case still open.

## publication_packet_title
The {4,1}-Factor Problem for 5-Regular Pseudographs

## publication_packet_frontier_basis
The 2015 source narrows the odd-degree landscape to this last 5-regular pseudograph residue after larger odd-degree failures.

## publication_packet_near_paper_reason
A proof or counterexample would directly close the named low-degree residue and would already determine the title theorem and core proof section of the paper.

## publication_packet_literature_scope
The 2015 source, the mod-3 reformulation it records, and one bounded later-status check.

## publication_packet_artifact_requirements
Either a structural proof or a minimal counterexample, together with a tiny checker for the {4,1}-factor or the equivalent edge-labeling certificate.

## paper_shape
One exact theorem or counterexample package, with a brief structural section around the mod-3 reformulation and a short obstruction discussion.

## transfer_kit

### usable_lemmas
- Use the 2015 equivalence between a {4,1}-factor and an edge-labeling by {1,2} with every vertex-sum 0 modulo 3.
- The 2015 counterexamples for larger odd degrees mean any proof can focus on the isolated 5-regular residue rather than a broad odd-degree program.
- Minimal-counterexample reductions can stay local because the certificate is only degree bookkeeping on a spanning subgraph or its mod-3 label image.

### toy_example
K_6 is a sanity-check model: deleting any perfect matching leaves a spanning 4-regular subgraph, so the positive certificate format is completely explicit on the smallest simple 5-regular graph.

### known_obstruction
Naive induction on odd degree is false because larger odd-degree cases already admit counterexamples.

### prior_work_stop_sentence
After the broader odd-degree failures, prior work stops at the exact 5-regular pseudograph {4,1}-factor case.

### recommended_first_attack
Work in the mod-3 edge-label language and force a vertex-minimal counterexample to contain a reducible cut or parity configuration.

### paper_if_solved
The paper would be a one-theorem note closing the last low-degree odd residue, with the mod-3 reformulation as the short setup section.

## definitions
- A {4,1}-factor is a spanning subgraph in which each vertex has degree either 4 or 1.
- A pseudograph may contain loops and multiple edges.
- The 2015 source reformulates the problem as an edge-labeling by {1,2} with vertex-sums 0 modulo 3.

## publication_red_flags
- The freshest explicit open-status signal is a summary page rather than a dedicated follow-up paper.
- A negative answer would need a carefully minimized obstruction rather than a raw machine witness.
