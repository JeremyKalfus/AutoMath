# Working Packet: One-factorizations of 9-regular graphs of order 12

- slug: `order-12-9-regular-one-factorization`
- title: Is every 9-regular graph on 12 vertices one-factorizable?
- publication status: `SLICE_CANDIDATE`
- packet quality: `strong`

## statement
Settle the smallest high-degree unresolved slice by classifying the nine nonisomorphic 9-regular graphs on 12 vertices with respect to one-factorizability, ideally proving all are one-factorizable or isolating minimal exceptions.

## novelty_notes
- frontier basis: The canonical 2005 classification paper leaves the degree-9 order-12 slice explicitly unresolved and records that only nine nonisomorphic base graphs remain in this slice.
- why still open: The canonical 2005 paper explicitly leaves degrees 7, 8, and 9 open for order 12, and the bounded later-status search surfaced no later paper resolving the degree-9 slice.
- attempted conflict check: The repo memory sweep found no earlier AutoMath attempt or near-duplicate on order-12 one-factorizations or degree-9 regular graph factorizations.
- rediscovery risk: medium

## proof_sketch
- attack style: near-complete-graph case split using perfect-matching structure, complement heuristics, and tiny exact verification on the nine degree-9 graphs
- likely route: A complete verdict on those nine graphs is already a finite exact-classification note with the statement, table, and verification format essentially predetermined.
- verifier focus: For a positive solve, store each factorization explicitly as nine perfect matchings; for a negative solve, preserve the complete obstruction search or structural proof for every one of the nine graphs.

## likely_paper_shape
- note title: One-factorizations of 9-regular graphs of order 12
- paper shape: A fixed-order exact classification note with a table of the nine graphs, factorization verdicts, and a short structural discussion.
- publication if solved: A complete degree-9 classification on order 12 is already a short exact-classification paper because the source explicitly leaves that slice open.
- minimal artifact requirements: An explicit factorization table or a complete obstruction argument for each of the nine graphs, together with a small perfect-matching decomposition checker.

## bounded_source_list
- Petteri Kaski and Patric R. J. Ostergard, "One-Factorizations of Regular Graphs of Order 12" (Electronic Journal of Combinatorics 12, 2005).
- Canonical 2005 order-12 one-factorization paper plus one bounded later-status search for a quiet degree-9 resolution.
- artifacts/order-12-9-regular-one-factorization/record.md
- artifacts/order-12-9-regular-one-factorization/status.json
