# Are all 4-chromatic (2K2, K4)-free graphs recolourable?

- entry_type: `paper_candidate`
- slug: `2k2-k4-recolourable`
- worker_role: `solver-A`
- canonical_source: `Manoj Belavadia, Kathie Cameron, and Elias Hildred, "Frozen Colourings in 2K2-Free Graphs" (Electronic Journal of Combinatorics 32(2), 2025).`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Settling this question would close the last remaining recolourability case for pairs of forbidden four-vertex induced subgraphs and would naturally support a short dichotomy-completion note.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `88`
- single_solve_to_paper_fraction: `0.82`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `small`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/2k2-k4-recolourable/working_packet.md`
- paper_shape: `A dichotomy-completion note whose main theorem settles the unique unresolved pair-forbidden recolourability class.`

## question
Does every 4-chromatic graph with no induced 2K2 and no induced K4 have connected recolouring graphs R_l(G) for all l > chi(G)?

## canonical_statement
Determine whether all 4-chromatic (2K2, K4)-free graphs are recolourable.

## intended_statement
Either prove that every 4-chromatic (2K2, K4)-free graph is recolourable or construct a 4-chromatic (2K2, K4)-free graph with a frozen 5-colouring or disconnected recolouring graph.

## pre_solve_gate_reason
The 2025 source explicitly isolates this as the only open case remaining for recolourability when two graphs on four vertices are forbidden.

## micro_paper_assessment
Pass: this is a stable named last-case completion problem with a compact success certificate and immediate dichotomy leverage.

## hypothetical_title
Recolourability of 4-Chromatic (2K2, K4)-Free Graphs

## hypothetical_abstract
We settle the last open recolourability question for graph classes defined by forbidding two induced subgraphs on four vertices. Specifically, we determine whether every 4-chromatic (2K2, K4)-free graph is recolourable. Combined with the 2025 classification of the neighboring cases, this yields the full dichotomy in the four-vertex-pair setting.

## single_solve_paper_explanation
The literature already supplies the surrounding classification and isolates this exact leftover case. A positive solution immediately finishes the dichotomy; a negative solution immediately supplies the missing obstruction class. Either way, the solved claim is already the paper's main theorem.

## broader_theorem_nonimplication_note
The 2025 source proves recolourability for several neighboring classes but explicitly stops at the 4-chromatic (2K2, K4)-free case, so no broader published theorem currently subsumes it.

## literature_gap
The only unresolved four-vertex-pair recolourability case identified in the 2025 source is whether all 4-chromatic (2K2, K4)-free graphs are recolourable.

## publication_packet_title
Recolourability of 4-Chromatic (2K2, K4)-Free Graphs

## publication_packet_frontier_basis
Belavadia-Cameron-Hildred prove all 3-chromatic 2K2-free graphs are recolourable and explicitly identify the 4-chromatic (2K2, K4)-free case as the sole remaining dichotomy gap.

## publication_packet_near_paper_reason
The frontier already comes packaged as one named open case in a near-complete dichotomy; after the solve, the paper mainly needs the proof, one extremal example if negative, and a short recap of the surrounding results.

## publication_packet_literature_scope
The 2025 Frozen Colourings paper, the earlier pair-forbidden recolourability classification it cites, exact-syntax searches on the (2K2, K4)-free case, and bounded 2026 status checks that did not surface a later resolution.

## publication_packet_artifact_requirements
Either a structural recolouring proof for every 4-chromatic (2K2, K4)-free graph, or one explicit counterexample carrying a frozen 5-colouring or disconnected R_5(G).

## paper_shape
A dichotomy-completion note whose main theorem settles the unique unresolved pair-forbidden recolourability class.

## transfer_kit

### usable_lemmas
- Belavadia-Cameron-Hildred prove every 3-chromatic 2K2-free graph is recolourable.
- The same paper identifies the 4-chromatic (2K2, K4)-free class as the only remaining open case in the pair-forbidden four-vertex setting.
- The class is known to be 4-colourable, so the open problem is not about chromatic feasibility but about recolouring connectivity.

### toy_example
The 2025 paper highlights the small 4-chromatic examples D2 and F2 carrying frozen 5-colourings in the wider 2K2-free world, giving the first nontrivial objects to compare against the extra K4-free restriction.

### known_obstruction
Frozen 5-colourings already occur in nearby 2K2-free classes, so any positive proof must show that the K4-free restriction eliminates exactly those obstruction mechanisms.

### prior_work_stop_sentence
The 2025 Frozen Colourings paper proves all neighboring cases and then stops at the lone open question of whether all 4-chromatic (2K2, K4)-free graphs are recolourable.

### recommended_first_attack
Exploit the K4-free restriction on the local structure around any putative frozen 5-colouring and try to force a recolouring move by combining the 3-chromatic recolouring machinery with a minimal-counterexample argument.

### paper_if_solved
The paper would be a short dichotomy-completion note for recolourability under two forbidden induced subgraphs on four vertices.
