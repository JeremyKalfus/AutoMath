# Working Packet: 3-Regular Subgraphs of 4-Regular Pseudographs

- slug: `four-regular-pseudograph-three-regular-subgraph`
- title: Does every 4-regular pseudograph contain a 3-regular subgraph?
- publication status: `NONE`
- packet quality: `adequate`
- micro-paper eligible: `False`
- paper leverage score: `67`
- single-solve-to-paper fraction: `0.74`

## statement
Resolve the pseudograph case by proving every 4-regular pseudograph contains a 3-regular subgraph, or by giving a minimal counterexample; equivalently, close the remaining ordered-(3,1)-colorable pseudograph characterization problem.

## novelty_notes
- frontier basis: The summary packet places the pseudograph extension directly on the boundary of a settled simple-graph theorem and a remaining ordered-(3,1)-coloring gap.
- why still open: The 2016 summary explicitly states that the simple-graph case is settled while the 4-regular pseudograph question remains open, and bounded search did not surface a later resolution.
- attempted conflict check: The repo exclusion sweep found no prior attempt on this pseudograph 4-regular subgraph problem or on the ordered-(3,1)-coloring statement.
- rediscovery risk: medium

## proof_sketch
- attack style: ordered-(3,1)-coloring reformulation plus edge-cut reductions and minimal counterexample analysis
- likely route: A clean solve would immediately determine the title theorem and most of the proof body, but the source-faithful boundary still needs tightening first.
- verifier focus: A positive witness is a degree-3 subgraph or ordered (3,1)-coloring; a negative solution must explain the exact obstruction and statement boundary.

## micro_paper_test
- title theorem strength: strong
- family anchor strength: moderate
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: unresolved
- search-heavy: False
- certificate compactness: high
- exact gap from source: small
- assessment: Park: the theorem is paper-shaped, but broader-theorem risk and statement-faithfulness ambiguity keep it out of the strict micro-paper lane until refreshed.

## likely_paper_shape
- note title: 3-Regular Subgraphs of 4-Regular Pseudographs
- hypothetical title: 3-Regular Subgraphs of 4-Regular Pseudographs
- paper shape: A single theorem or counterexample paper, built around the ordered-(3,1)-coloring equivalence and a short obstruction section.
- publication if solved: The pseudograph extension of a classical 4-regular theorem is already paper-shaped as a standalone yes/no result.
- minimal artifact requirements: Either a short structural proof or a minimal counterexample, together with an explicit ordered-(3,1)-coloring / degree-check certificate.

## hypothetical_abstract
We investigate the pseudograph extension of the classical 4-regular-to-3-regular subgraph theorem. Via the ordered-(3,1)-coloring reformulation, we either prove that every 4-regular pseudograph admits the required degree-3 substructure or isolate a minimal obstruction. The statement is paper-shaped, but the current packet still needs a sharper source-faithfulness lock before it belongs in the strict micro-paper lane.

## single_solve_explanation
If the exact statement is locked cleanly, one solve would likely yield most of a short note because the reformulation, motivation, and verifier are already present. What remains uncertain today is not the paper shape but the exact theorem surface and whether a broader existing result already shadows part of it. That unresolved risk is why this dossier is parked rather than front-ranked.

## broader_theorem_nonimplication
The current bounded packet does not yet completely rule out that the settled simple-graph theorem or the ordered-coloring reformulation already hides a broader implication affecting the pseudograph statement, so that risk remains unresolved.

## literature_gap
Available summary material says the simple-graph case is settled and the pseudograph extension remains open, but the exact source-faithful boundary still needs sharpening.

## transfer_kit
- lemma: Use Bernshteyn's ordered-(3,1)-coloring reformulation to move between the subgraph language and a local edge-coloring certificate.
- lemma: The simple-graph case is already settled, so any pseudograph proof should isolate exactly where loops or multiplicities enter the obstruction.
- lemma: The verifier is purely local degree bookkeeping once the exact formulation is fixed.
- toy example: Start with the settled simple-graph boundary case as the worked example and then inspect how the first loop or multiple-edge move breaks the same argument.
- known obstruction: The current packet still hides statement-faithfulness risk: the exact 3-regular-subgraph formulation may be narrower or broader than a casual reading suggests.
- prior-work stop sentence: Available summary sources say the simple-graph theorem is known, while the 4-regular pseudograph extension remains open.
- recommended first attack: Refresh the exact statement against the reformulation first, then attack a minimal pseudograph counterexample in the ordered-(3,1)-coloring language.
- paper if solved: If the statement locks cleanly, the paper would be a short extension-or-obstruction note sitting exactly one step beyond the settled simple-graph theorem.

## bounded_source_list
- Fields Institute talk page "(3,1)-colorings of 4-regular graphs" (2016), summarizing Bernshteyn's 2014 reformulation and the remaining ordered-(3,1)-coloring gap.
- The 2014 reformulation, the 2016 summary page, and one bounded later-status search.
- artifacts/four-regular-pseudograph-three-regular-subgraph/record.md
- artifacts/four-regular-pseudograph-three-regular-subgraph/status.json
