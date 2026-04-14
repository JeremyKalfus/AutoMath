# Working Packet: List Edge Coloring of Graphs on at Most 10 Vertices

- slug: `all-10-vertex-graphs-list-edge-coloring`
- title: Does every graph on at most 10 vertices satisfy the List Edge Coloring Conjecture?
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `66`
- single-solve-to-paper fraction: `0.67`

## statement
Either prove that chi'_ell(G) = chi'(G) for every graph on at most 10 vertices or produce a first 10-vertex counterexample together with an explicit obstructing list assignment.

## novelty_notes
- frontier basis: The 2018 paper computes many small cases and reduces the unresolved residue to specific 10-vertex zero-sum regular class-1 graphs rather than proving the whole 10-vertex slice.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath mathematical attempt, slug conflict, or near-duplicate for the exact 10-vertex List Edge Coloring Conjecture slice.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A completed 10-vertex classification would have a clear note format, but the amount of residue bookkeeping still makes the packet heavier than the lane prefers.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: high
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail for the strict lane: exact and stable, but still too search-heavy and editorially bulky relative to the desired one-shot paper packet.

## likely_paper_shape
- note title: List Edge Coloring of Graphs on at Most 10 Vertices
- hypothetical title: List Edge Coloring of Graphs on at Most 10 Vertices
- paper shape: A finite-slice classification note with a residue table of exceptional 10-vertex graphs and either explicit colorings or one counterexample.
- publication if solved: A complete 10-vertex slice for list edge coloring would be publishable, but the packet remains too census-heavy for the strict micro-paper lane.
- minimal artifact requirements: Either explicit list-edge-coloring certificates for each remaining 10-vertex residue class or a concrete 10-vertex counterexample with a witness list assignment and checker.

## hypothetical_abstract
We settle the 10-vertex finite slice of the List Edge Coloring Conjecture. Building on the 2018 computational reduction to zero-sum regular class-1 graphs, we either prove that every graph on at most 10 vertices satisfies chi'_ell = chi' or isolate a first 10-vertex counterexample with an explicit obstructing list assignment. The theorem is real and stable, but the remaining packet still has too much census flavor to be a top micro-paper target.

## single_solve_explanation
If the exact 10-vertex slice were settled, the paper would be legitimate and mostly determined in advance. The problem is that the residual workload is still more table-like than theorem-like, so the solve does not compress the packet as sharply as the best single-exception candidates do. This makes it an honest but low-priority paper candidate rather than a preferred micro-paper lane target.

## broader_theorem_nonimplication
The 2018 paper resolves many nearby cases but stops with a specific 10-vertex residue, so the exact finite slice is not currently implied by a broader published theorem.

## literature_gap
The 2018 computation reduces the unresolved part of the 10-vertex slice to specific zero-sum regular class-1 graphs and stops before proving the full 10-vertex conjecture.

## transfer_kit
- lemma: The 2018 paper computes the list chromatic index for many small graphs and reduces the unresolved 10-vertex work to zero-sum regular class-1 cases.
- lemma: The paper reports that all regular even graphs up to 10 vertices and all regular class-2 graphs up to 10 vertices are already handled.
- lemma: Any negative resolution would have a compact witness form: one 10-vertex graph together with an explicit obstructing list assignment.
- toy example: The already settled small regular and bipartite cases in the 2018 source provide the toy model for what a positive certificate table looks like.
- known obstruction: The zero-sum regular class-1 residue resists the main sign-based method, so the remaining work risks becoming a finite census rather than a short structural proof.
- prior-work stop sentence: The 2018 computation stops after reducing the 10-vertex problem to specific zero-sum regular class-1 graphs.
- recommended first attack: Push the 2018 reduction one step further to isolate the smallest genuinely unresolved residue before doing any bounded exact computation.
- paper if solved: The paper would be a finite-slice classification note with a residue table and either explicit colorings or one explicit counterexample.

## bounded_source_list
- M. C. de Carvalho, C. L. Lucchesi, U. S. Souza, and M. Stiebitz, "Computing the list chromatic index of graphs" (Journal of Combinatorial Theory, Series B 130, 2018).
- The 2018 computation paper, exact-statement searches for a settled 10-vertex slice, and bounded later-status checks for the remaining zero-sum cases.
- artifacts/all-10-vertex-graphs-list-edge-coloring/record.md
- artifacts/all-10-vertex-graphs-list-edge-coloring/status.json
