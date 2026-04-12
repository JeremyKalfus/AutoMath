# Does the ladder with 4 rungs have the edge-Erdos-Posa property?

- entry_type: `paper_candidate`
- slug: `ladder-4-rungs-edge-erdos-posa`
- family_name: `Edge-Erdos-Posa property for fixed planar graphs`
- canonical_source: `Raphael Steck and Arthur Ulmer, "On the Edge-Erdos-Posa Property of Ladders" (Graphs and Combinatorics 40, 2024).`
- open_status_checked_on: `2026-04-12`
- attack_style: `extend the 3-rung positive proof and isolate the first extra obstruction pattern, or build the first non-condensed-wall counterexample`
- curation_confidence: `high`
- publication_status: `SLICE_CANDIDATE`
- campaign_affinity: `none`
- publication_if_solved: `A resolution of the 4-rung ladder case is already a standalone note because the 2024 paper leaves ladders with 4 to 13 rungs explicitly open.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `tiny`
- single_pass_proof_plausibility: `medium-high`
- novelty_check_cost: `low`
- formalization_overhead: `low-medium`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `excellent`
- working_packet_path: `artifacts/ladder-4-rungs-edge-erdos-posa/working_packet.md`
- paper_shape: `A smallest-open-case theorem or counterexample note for a fixed pattern H, with one structural section and one consequence section.`

## question
If H is the ladder with 4 rungs, must every graph either contain k edge-disjoint H-subdivisions or admit an edge set of size f(k) hitting all H-subdivisions?

## canonical_statement
Determine whether the ladder with 4 rungs has the edge-Erdos-Posa property.

## intended_statement
Settle the smallest unresolved ladder case by proving that the 4-rung ladder has the edge-Erdos-Posa property, or by constructing a genuine counterexample graph not ruled out by the condensed-wall barrier.

## theorem_slice_hint
Treat the 4-rung ladder as the smallest unresolved rung count, not as a broad ladder campaign; the whole note should pivot on one yes-or-no theorem.

## why_reasoning_friendly
The target graph H is tiny, the positive and negative sides are both crisp, and the canonical source already isolates the ladder-range gap rather than a sprawling family program.

## why_low_token
The statement is short, certificates are compact, and the proof surface is concentrated on one fixed pattern instead of a large parameter family.

## verifier_hint
For a positive solve, verify the hitting/packing theorem against the exact 4-rung ladder definition; for a negative solve, preserve an explicit host graph family together with a checked obstruction argument.

## lean_hint
Lean only after the combinatorial core is stable; formalization would mostly be finite graph bookkeeping around the exact ladder pattern and edge-hit definition.

## rediscovery_risk
low-medium

## why_still_appears_open
The canonical 2024 paper explicitly asks whether ladders with 4 to 13 rungs have the edge-Erdos-Posa property, and the bounded later-status search surfaced no follow-up resolution for the 4-rung case.

## why_this_could_be_publishable
It is a smallest-open-case yes/no theorem with immediate context from the 3-rung positive result and the 14-rung negative barrier.

## pre_solve_gate_reason
This is already the smallest unresolved exact ladder case left open in the canonical 2024 source, so one clean resolution is itself most of a paper with no feeder ladder.

## publication_packet_title
The edge-Erdos-Posa property for the 4-rung ladder

## publication_packet_frontier_basis
The canonical 2024 ladder paper proves the 3-rung positive case and the 14-rung negative barrier, while explicitly leaving the 4-rung case open as the smallest unresolved ladder instance.

## publication_packet_near_paper_reason
A yes-or-no resolution of the 4-rung case is already a complete smallest-open-case note with built-in context from the 3-rung theorem and the 14-rung obstruction.

## publication_packet_literature_scope
Canonical 2024 ladder paper plus one bounded later-status search for a follow-up on the 4-rung case.

## publication_packet_artifact_requirements
Either a proof that the 4-rung ladder has the edge-Erdos-Posa property or an explicit counterexample family, together with a compact packing/hitting verification writeup.

## paper_shape
A smallest-open-case theorem or counterexample note for a fixed pattern H, with one structural section and one consequence section.

## definitions
- A ladder with t rungs is the graph formed by two parallel paths with t matching edges between corresponding vertices.
- A graph H has the edge-Erdos-Posa property if there is a function f such that every graph G either contains k edge-disjoint subdivisions of H or an edge set of size at most f(k) meeting every subdivision of H.
- The 2024 source proves the property for the 3-rung ladder and shows that ladders with 14 or more rungs do not have it.

## publication_red_flags
- A negative answer would need a clean counterexample mechanism, not just an ad hoc gadget.
- If the positive proof merely replays the 3-rung argument with long case splits, packaging quality could slip.
