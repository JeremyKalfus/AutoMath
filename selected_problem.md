# Are all graphs on 9 vertices 1-11-representable?

- entry_type: `paper_candidate`
- slug: `all-9-vertex-graphs-1-11-representable`
- canonical_source: `Mohammed Alshammari, Sergey Kitaev, Chaoliang Tang, Tianyi Tao, and Junchi Zhang, "On 1-11-representability and multi-1-11-representability of graphs" (Utilitas Mathematica 122, 2025), together with Futorny-Kitaev-Pyatkin, "New Tools to Study 1-11-Representation of Graphs" (Graphs and Combinatorics 40, 2024).`
- open_status_checked_on: `2026-04-12`
- attack_style: `use the 2024-2025 structural toolbox first, then only bounded exhaustive search on the remaining 9-vertex non-word-representable cases`
- curation_confidence: `medium`
- publication_status: `SLICE_CANDIDATE`
- publication_if_solved: `Settling the 9-vertex slice would already be a finite-classification note, either as a complete positive census or as a first minimal counterexample paper.`
- publication_if_solved_score: `paper_with_light_packaging`
- solve_to_publication_distance: `short-medium`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `86`
- single_solve_to_paper_fraction: `0.76`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `moderate`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- search_heavy: `True`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `low-medium`
- packaging_risk: `medium`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/all-9-vertex-graphs-1-11-representable/working_packet.md`
- paper_shape: `A smallest-unresolved finite-slice note with structural reductions, a compact classification table, and explicit representing words or a minimal obstruction.`

## question
Does every graph with 9 vertices admit a 1-11 representation, or is there a minimal 9-vertex obstruction?

## canonical_statement
It is unknown whether every graph is 1-11-representable; the 2025 paper proves all graphs on at most 8 vertices are 1-11-representable and explicitly points toward the 9-vertex slice.

## intended_statement
Resolve the first unresolved finite slice by proving that every 9-vertex graph is 1-11-representable, or by producing the first 9-vertex counterexample with a rigorous certificate.

## why_reasoning_friendly
The problem has a rich reduction toolbox, a sharply bounded finite frontier, and a natural minimal-counterexample flavor.

## why_low_token
The theorem statement is tiny, witnesses are explicit words, and any remaining residue is a finite census rather than an open-ended family.

## verifier_hint
Positive solutions should preserve explicit 1-11 words for each reduced isomorphism class or a general construction; negative solutions need a complete obstruction certificate for the claimed 9-vertex graph.

## lean_hint
Only formalize after a human-readable certificate style is fixed; the right backend object is a checker for two-letter subword constraints, not a large search proof.

## rediscovery_risk
medium

## why_still_appears_open
The 2025 paper still states that it is unknown whether every graph is 1-11-representable, proves only the up-to-8-vertex slice, and identifies the 9-vertex frontier as the next natural target; bounded follow-up search found no later 9-vertex resolution.

## why_this_could_be_publishable
It is exactly the kind of smallest unresolved finite slice that can become a clean note or a minimal-counterexample paper with low novelty-check cost.

## pre_solve_gate_reason
The 9-vertex slice is already a self-contained smallest unresolved finite classification, so a full settlement would itself be most of a paper without a feeder ladder.

## micro_paper_assessment
Pass: this is a smallest unresolved finite slice with a strong title theorem, explicit family anchor, and only a tiny human-readable search residue.

## hypothetical_title
1-11-Representability of Graphs on 9 Vertices

## hypothetical_abstract
We settle the first unresolved finite slice of the 1-11-representability program by classifying graphs on 9 vertices. Using the 2024-2025 structural toolbox and a bounded residue analysis, we either prove that every 9-vertex graph is 1-11-representable or isolate a first obstruction with a compact certificate. The result converts the universal conjecture into a sharper frontier statement and needs only light packaging beyond the solve.

## single_solve_paper_explanation
The source already fixes the natural headline theorem: the 9-vertex slice is the first omitted finite case after the complete 8-vertex classification. Once the slice is settled, the rest of the paper is mostly a short literature frame, a compact certificate table or obstruction description, and one or two immediate remarks on how the 9-vertex frontier interacts with the broader conjecture. The residue is small enough that even a computational component can stay human-readable.

## broader_theorem_nonimplication_note
The 2025 paper proves the up-to-8-vertex theorem and adjacent structural tools, but it does not imply the 9-vertex slice; bounded follow-up checks found no broader theorem settling the omitted case.

## literature_gap
Prior work proves 1-11-representability through 8 vertices and develops the nearby toolbox, but stops before the 9-vertex slice.

## publication_packet_title
1-11-Representability of Graphs on 9 Vertices

## publication_packet_frontier_basis
The canonical 2025 paper proves the universal statement through 8 vertices and explicitly points to the 9-vertex slice as the next natural finite frontier.

## publication_packet_near_paper_reason
Settling the 9-vertex slice would already be a self-contained finite-classification note or first-obstruction paper with a short path from solve to writeup.

## publication_packet_literature_scope
The canonical 2025 1-11-representability paper, the adjacent 2024 toolbox paper, and one bounded outside-status check for a later 9-vertex census result.

## publication_packet_artifact_requirements
Either explicit representing words for the reduced 9-vertex frontier or a certified minimal obstruction, plus a compact two-letter subword checker.

## paper_shape
A smallest-unresolved finite-slice note with structural reductions, a compact classification table, and explicit representing words or a minimal obstruction.

## transfer_kit

### usable_lemmas
- Use the 2024-2025 structural toolbox to reduce from arbitrary 9-vertex graphs to the non-word-representable residue first.
- The 2025 paper already proves the complete 8-vertex slice, so all induction and minimal-counterexample rhetoric can start at 9 vertices.
- Representing words are explicit finite certificates, so any surviving residue can be documented class by class without long certificate dumps.

### toy_example
The full 8-vertex classification from the 2025 source is the immediate toy model: it shows exactly what a positive finite-slice note and certificate table should look like one step lower.

### known_obstruction
If the positive route survives only by machine census, the packet risks turning into a search dump unless the residue stays tiny and the certificates stay compact.

### prior_work_stop_sentence
The source proves the 1-11-representability theorem through 8 vertices and then stops at the 9-vertex frontier.

### recommended_first_attack
Use the structural reductions to isolate the few 9-vertex classes not already handled by word-representability and only then run bounded certificate search.

### paper_if_solved
The paper would be a finite-slice classification note with a short structural reduction section and either a compact certificate table or a first obstruction section.

## definitions
- A graph is 1-11-representable if a word witnesses edges by allowing at most one occurrence of consecutive equal letters and non-edges by forcing at least two.
- Word-representable graphs are exactly the 0-11-representable graphs.
- The 2025 source proves all graphs on at most 8 vertices are 1-11-representable and singles out the 9-vertex slice as the next frontier.

## publication_red_flags
- This can drift into a brute-force census if the structural reductions are not used aggressively.
- If all 9-vertex graphs are representable, the paper still needs a concise certificate strategy rather than a raw machine dump.
