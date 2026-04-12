# Does every 2-colored cocktail party graph admit a cover by two monochromatic diameter-2 subsets?

- entry_type: `paper_candidate`
- slug: `cocktail-party-two-monochromatic-diameter-2-cover`
- family_name: `Low-diameter monochromatic covers in edge-colored graphs`
- canonical_source: `Andras Gyarfas and Gabor N. Sarkozy, "2-Reachable Subsets in Two-Colored Graphs" (Graphs and Combinatorics 42, 2026), which states and relaxes the English-McCourt-Mattes-Phillips conjecture.`
- open_status_checked_on: `2026-04-12`
- attack_style: `tighten the 2-reachable argument to internal diameter 2 via critical-pair analysis and blow-up-of-C5 obstruction control`
- curation_confidence: `high`
- publication_status: `SLICE_CANDIDATE`
- campaign_affinity: `none`
- publication_if_solved: `Solving the original diameter-2 cocktail-party conjecture would read as a direct short follow-up to the 2026 relaxed theorem.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `tiny`
- single_pass_proof_plausibility: `medium-high`
- novelty_check_cost: `low`
- formalization_overhead: `low-medium`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `excellent`
- working_packet_path: `artifacts/cocktail-party-two-monochromatic-diameter-2-cover/working_packet.md`
- paper_shape: `One conjecture-resolution note: statement, structural proof or counterexample, and a short discussion of Ryser-style diameter bounds.`

## question
In every red-blue coloring of the cocktail party graph on an even number of vertices, can the vertex set be covered by two monochromatic diameter-2 subsets?

## canonical_statement
In every 2-coloring of the edges of the cocktail party graph G^c, there exist A,B covering V(G^c) such that A and B are monochromatic diameter-2 subsets.

## intended_statement
Upgrade the 2026 relaxed 2-reachable cover theorem to the original diameter-2 conjecture, or exhibit a minimal colored cocktail-party counterexample.

## theorem_slice_hint
Treat the exact cocktail-party conjecture as the main theorem, not as a stepping stone to full f(2,2)=3 for all alpha=2 graphs.

## why_reasoning_friendly
The host graph is rigid, the color structure is binary, and the gap from 2-reachable to diameter 2 is conceptually narrow rather than campaign-sized.

## why_low_token
The object definition is short, certificates are simple vertex covers in two colors, and the conjecture has a tight yes-or-no endpoint.

## verifier_hint
A positive witness is a pair of color classes with direct internal diameter checks; a negative result needs a fully specified 2-coloring family with provable failure of every two-set cover.

## lean_hint
If solved positively, only formalize the fixed graph family and diameter-2 cover predicate after the combinatorial proof stabilizes.

## rediscovery_risk
low-medium

## why_still_appears_open
The canonical 2026 paper states the diameter-2 cocktail-party conjecture explicitly, proves only the relaxed 2-reachable version, and the bounded recent-status search surfaced no later diameter-2 resolution.

## why_this_could_be_publishable
It is a direct upgrade from a very recent paper's main relaxed theorem to the original exact conjecture.

## pre_solve_gate_reason
The 2026 source already isolates the exact open conjecture and proves a nearby relaxation, so one strong solve would already be most of a standalone paper.

## publication_packet_title
Two monochromatic diameter-2 covers in 2-colored cocktail party graphs

## publication_packet_frontier_basis
The canonical 2026 source states the exact diameter-2 cocktail-party conjecture and proves only the relaxed 2-reachable version, so the diameter-2 claim itself remains the frontier object.

## publication_packet_near_paper_reason
A proof or counterexample would directly resolve the named conjecture left open by the 2026 relaxation paper, so the theorem statement, motivation, and comparison section are already essentially fixed.

## publication_packet_literature_scope
Canonical 2026 cocktail-party/2-reachable paper plus one bounded outside-status check for a later diameter-2 resolution.

## publication_packet_artifact_requirements
One rigorous proof or explicit colored counterexample family, a short skeptical verification note, and a direct diameter-2 cover checker for any positive witness.

## paper_shape
One conjecture-resolution note: statement, structural proof or counterexample, and a short discussion of Ryser-style diameter bounds.

## definitions
- The cocktail party graph is obtained from a complete graph on an even number of vertices by deleting a perfect matching.
- A diameter-2 subset in color i is a vertex set whose induced color-i subgraph has distance at most 2 between every pair of its vertices.
- The 2026 source proves the relaxed version where the distance-2 witness may pass through vertices outside the subset.

## publication_red_flags
- The gap between external 2-reachability and internal diameter 2 can hide subtle obstruction configurations.
- A negative answer would need a very explicit coloring family, not an isolated small example.
