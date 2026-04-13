# Working Packet: The Conference Graph of Order 85

- slug: `conference-graph-order-85`
- title: Does a conference graph of order 85 exist?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `False`
- paper leverage score: `62`
- single-solve-to-paper fraction: `0.88`

## statement
Resolve the exact order-85 conference graph case by either constructing an srg(85,42,20,21) or proving nonexistence.

## novelty_notes
- frontier basis: Reference tables still isolate order 85 as the smallest open conference case.
- why still open: The 2011 strongly-regular-graph table still lists srg(85,42,20,21) among the unknown parameter sets up to 100 vertices, and the bounded follow-up search did not reveal a later resolution.
- attempted conflict check: Repo memory contains a different conference-family rediscovery at order 66, but no exact match or near-duplicate for order 85 appeared in failed_problems, queue, selected_problem, campaigns, PROOFS, or artifact statuses.
- rediscovery risk: low-medium

## proof_sketch
- attack style: exact existence/nonexistence via automorphism pruning, spectral restrictions, and explicit construction or obstruction
- likely route: An exact yes or no answer would instantly determine the theorem and verification sections of the note.
- verifier focus: For existence, verify the adjacency matrix against the strongly regular parameters; for nonexistence, preserve the full orbit-matrix or obstruction chain.

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Park: excellent title theorem, but the likely proof route remains too search-heavy for the strict micro-paper lane.

## likely_paper_shape
- note title: The Conference Graph of Order 85
- hypothetical title: The Conference Graph of Order 85
- paper shape: A single exact existence paper or a single exact nonexistence paper for one canonical open parameter set.
- publication if solved: An exact existence or nonexistence result for the smallest open conference case is automatically a paper.
- minimal artifact requirements: Either a certified adjacency matrix or a complete nonexistence obstruction chain with orbit-matrix verification.

## hypothetical_abstract
We resolve the existence question for the smallest open conference-graph parameter set by settling srg(85,42,20,21). Using the known conference-matrix equivalence and automorphism-pruning framework, we either construct a graph with the required parameters or prove nonexistence. The paper payoff is immediate, but the present route still looks too search-heavy for the strict micro-paper lane.

## single_solve_explanation
If the construction or nonexistence proof were in hand, the note would be essentially complete: the title, theorem, and verification format are already fixed. The problem is parked only because the current likely route still depends on substantial computation or orbit pruning rather than on a compact human-readable residue. So the issue is closability style, not paper leverage.

## broader_theorem_nonimplication
The literature still lists the exact parameter set itself as open rather than as a corollary of a broader strongly regular graph theorem, so there is no known umbrella implication closing it.

## literature_gap
Available reference tables still stop with srg(85,42,20,21) unresolved among the small conference parameters.

## transfer_kit
- lemma: Translate the question immediately into the symmetric conference-matrix formulation.
- lemma: Use the existing strongly regular graph feasibility and automorphism constraints before any search-heavy case split.
- lemma: Verification of a positive certificate is tiny once a candidate adjacency matrix is proposed.
- toy example: Small Paley conference graphs such as the order-9 case give the positive-model template for what a certified construction should look like.
- known obstruction: Orbit-matrix pruning and nonexistence arguments can balloon into bulky computation if no compact structural obstruction appears early.
- prior-work stop sentence: Reference tables still stop with the exact order-85 conference case unresolved.
- recommended first attack: Push the automorphism and spectral restrictions as far as possible before allowing any construction or orbit search.
- paper if solved: The paper would be a single existence-or-nonexistence note on the smallest open conference parameter set, with a very short verification section.

## bounded_source_list
- Makhnev et al., "Strongly regular graphs with non-trivial automorphisms" (Discrete Mathematics 311, 2011), cross-checked against recent conference-graph reference summaries.
- The 2011 strongly regular graph table, conference-graph summaries, and one bounded follow-up search.
- artifacts/conference-graph-order-85/record.md
- artifacts/conference-graph-order-85/status.json
