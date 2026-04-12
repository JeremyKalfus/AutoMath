# Working Packet: 1-11-representability of graphs on 9 vertices

- slug: `all-9-vertex-graphs-1-11-representable`
- title: Are all graphs on 9 vertices 1-11-representable?
- publication status: `SLICE_CANDIDATE`
- packet quality: `strong`

## statement
Resolve the first unresolved finite slice by proving that every 9-vertex graph is 1-11-representable, or by producing the first 9-vertex counterexample with a rigorous certificate.

## novelty_notes
- frontier basis: The canonical 2025 paper proves the universal statement through 8 vertices and explicitly points to the 9-vertex slice as the next natural unresolved finite frontier.
- why still open: The 2025 paper still states that it is unknown whether every graph is 1-11-representable, proves only the up-to-8-vertex slice, and its concluding discussion explicitly identifies the 9-vertex frontier as the next natural target; bounded web search found no later 9-vertex resolution.
- attempted conflict check: The repo exclusion sweep found no existing AutoMath artifact, queue entry, or failed problem near the 1-11-representability 9-vertex slice.
- rediscovery risk: medium

## proof_sketch
- attack style: use the 2024-2025 structural toolbox first, then only bounded exhaustive search on the remaining 9-vertex non-word-representable cases
- likely route: Settling the 9-vertex slice would already be a self-contained finite-classification note or first-obstruction paper with a very short path from solve to writeup.
- verifier focus: Positive solutions should preserve explicit 1-11 words for each reduced isomorphism class or a general construction; negative solutions need a complete obstruction certificate for the claimed 9-vertex graph.

## likely_paper_shape
- note title: 1-11-representability of graphs on 9 vertices
- paper shape: A smallest-unresolved finite-slice note with structural reductions, a compact classification table, and explicit representing words or a minimal obstruction.
- publication if solved: Settling the 9-vertex slice would already be a finite-classification note, either as a complete positive census or as a first minimal counterexample paper.
- minimal artifact requirements: Either explicit representing words for the reduced 9-vertex frontier or a certified minimal obstruction, plus a compact two-letter subword checker.

## bounded_source_list
- Mohammed Alshammari, Sergey Kitaev, Chaoliang Tang, Tianyi Tao, and Junchi Zhang, "On 1-11-representability and multi-1-11-representability of graphs" (Utilitas Mathematica 122, 2025), together with Futorny-Kitaev-Pyatkin, "New Tools to Study 1-11-Representation of Graphs" (Graphs and Combinatorics 40, 2024).
- Canonical 2025 1-11-representability paper, the adjacent 2024 toolbox paper, and one bounded outside-status check for a later 9-vertex census result.
- artifacts/all-9-vertex-graphs-1-11-representable/record.md
- artifacts/all-9-vertex-graphs-1-11-representable/status.json
