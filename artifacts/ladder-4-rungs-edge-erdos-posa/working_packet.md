# Working Packet: The edge-Erdos-Posa property for the 4-rung ladder

- slug: `ladder-4-rungs-edge-erdos-posa`
- title: Does the ladder with 4 rungs have the edge-Erdos-Posa property?
- publication status: `SLICE_CANDIDATE`
- packet quality: `excellent`

## statement
Settle the smallest unresolved ladder case by proving that the 4-rung ladder has the edge-Erdos-Posa property, or by constructing a genuine counterexample graph not ruled out by the condensed-wall barrier.

## novelty_notes
- frontier basis: The canonical 2024 ladder paper proves the 3-rung positive case and the 14-rung negative barrier, while explicitly leaving the 4-rung case open as the smallest unresolved ladder instance.
- why still open: The canonical 2024 paper explicitly asks whether ladders with 4 to 13 rungs have the edge-Erdos-Posa property, and the bounded later-status search surfaced no follow-up resolution for the 4-rung case.
- attempted conflict check: The exclusion sweep over failed_problems.json, queue.json, selected_problem.md, ledger.md, PROOFS.md, campaigns/, campaign manifests, and artifact slugs found no prior AutoMath attempt or near-duplicate around ladder edge-Erdos-Posa cases.
- rediscovery risk: low-medium

## proof_sketch
- attack style: extend the 3-rung positive proof and isolate the first extra obstruction pattern, or build the first non-condensed-wall counterexample
- likely route: A yes-or-no resolution of the 4-rung case is already a complete smallest-open-case note with built-in context from the 3-rung theorem and the 14-rung obstruction.
- verifier focus: For a positive solve, verify the hitting/packing theorem against the exact 4-rung ladder definition; for a negative solve, preserve an explicit host graph family together with a checked obstruction argument.

## likely_paper_shape
- note title: The edge-Erdos-Posa property for the 4-rung ladder
- paper shape: A smallest-open-case theorem or counterexample note for a fixed pattern H, with one structural section and one consequence section.
- publication if solved: A resolution of the 4-rung ladder case is already a standalone note because the 2024 paper leaves ladders with 4 to 13 rungs explicitly open.
- minimal artifact requirements: Either a proof that the 4-rung ladder has the edge-Erdos-Posa property or an explicit counterexample family, together with a compact packing/hitting verification writeup.

## bounded_source_list
- Raphael Steck and Arthur Ulmer, "On the Edge-Erdos-Posa Property of Ladders" (Graphs and Combinatorics 40, 2024).
- Canonical 2024 ladder paper plus one bounded later-status search for a follow-up on the 4-rung case.
- artifacts/ladder-4-rungs-edge-erdos-posa/record.md
- artifacts/ladder-4-rungs-edge-erdos-posa/status.json
