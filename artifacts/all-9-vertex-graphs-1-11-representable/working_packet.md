# Working Packet: 1-11-Representability of Graphs on 9 Vertices

- slug: `all-9-vertex-graphs-1-11-representable`
- title: Are all graphs on 9 vertices 1-11-representable?
- publication status: `SLICE_CANDIDATE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `86`
- single-solve-to-paper fraction: `0.76`

## statement
Resolve the first unresolved finite slice by proving that every 9-vertex graph is 1-11-representable, or by producing the first 9-vertex counterexample with a rigorous certificate.

## novelty_notes
- frontier basis: The canonical 2025 paper proves the universal statement through 8 vertices and explicitly points to the 9-vertex slice as the next natural finite frontier.
- why still open: The 2025 paper still states that it is unknown whether every graph is 1-11-representable, proves only the up-to-8-vertex slice, and identifies the 9-vertex frontier as the next natural target; bounded follow-up search found no later 9-vertex resolution.
- attempted conflict check: The repo exclusion sweep found no existing AutoMath artifact, queue entry, or failed problem near the 1-11-representability 9-vertex slice.
- rediscovery risk: medium

## proof_sketch
- attack style: use the 2024-2025 structural toolbox first, then only bounded exhaustive search on the remaining 9-vertex non-word-representable cases
- likely route: Settling the 9-vertex slice would already be a self-contained finite-classification note or first-obstruction paper with a short path from solve to writeup.
- verifier focus: Positive solutions should preserve explicit 1-11 words for each reduced isomorphism class or a general construction; negative solutions need a complete obstruction certificate for the claimed 9-vertex graph.

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- search-heavy: True
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass: this is a smallest unresolved finite slice with a strong title theorem, explicit family anchor, and only a tiny human-readable search residue.

## likely_paper_shape
- note title: 1-11-Representability of Graphs on 9 Vertices
- hypothetical title: 1-11-Representability of Graphs on 9 Vertices
- paper shape: A smallest-unresolved finite-slice note with structural reductions, a compact classification table, and explicit representing words or a minimal obstruction.
- publication if solved: Settling the 9-vertex slice would already be a finite-classification note, either as a complete positive census or as a first minimal counterexample paper.
- minimal artifact requirements: Either explicit representing words for the reduced 9-vertex frontier or a certified minimal obstruction, plus a compact two-letter subword checker.

## hypothetical_abstract
We settle the first unresolved finite slice of the 1-11-representability program by classifying graphs on 9 vertices. Using the 2024-2025 structural toolbox and a bounded residue analysis, we either prove that every 9-vertex graph is 1-11-representable or isolate a first obstruction with a compact certificate. The result converts the universal conjecture into a sharper frontier statement and needs only light packaging beyond the solve.

## single_solve_explanation
The source already fixes the natural headline theorem: the 9-vertex slice is the first omitted finite case after the complete 8-vertex classification. Once the slice is settled, the rest of the paper is mostly a short literature frame, a compact certificate table or obstruction description, and one or two immediate remarks on how the 9-vertex frontier interacts with the broader conjecture. The residue is small enough that even a computational component can stay human-readable.

## broader_theorem_nonimplication
The 2025 paper proves the up-to-8-vertex theorem and adjacent structural tools, but it does not imply the 9-vertex slice; bounded follow-up checks found no broader theorem settling the omitted case.

## literature_gap
Prior work proves 1-11-representability through 8 vertices and develops the nearby toolbox, but stops before the 9-vertex slice.

## transfer_kit
- lemma: Use the 2024-2025 structural toolbox to reduce from arbitrary 9-vertex graphs to the non-word-representable residue first.
- lemma: The 2025 paper already proves the complete 8-vertex slice, so all induction and minimal-counterexample rhetoric can start at 9 vertices.
- lemma: Representing words are explicit finite certificates, so any surviving residue can be documented class by class without long certificate dumps.
- toy example: The full 8-vertex classification from the 2025 source is the immediate toy model: it shows exactly what a positive finite-slice note and certificate table should look like one step lower.
- known obstruction: If the positive route survives only by machine census, the packet risks turning into a search dump unless the residue stays tiny and the certificates stay compact.
- prior-work stop sentence: The source proves the 1-11-representability theorem through 8 vertices and then stops at the 9-vertex frontier.
- recommended first attack: Use the structural reductions to isolate the few 9-vertex classes not already handled by word-representability and only then run bounded certificate search.
- paper if solved: The paper would be a finite-slice classification note with a short structural reduction section and either a compact certificate table or a first obstruction section.

## bounded_source_list
- Mohammed Alshammari, Sergey Kitaev, Chaoliang Tang, Tianyi Tao, and Junchi Zhang, "On 1-11-representability and multi-1-11-representability of graphs" (Utilitas Mathematica 122, 2025), together with Futorny-Kitaev-Pyatkin, "New Tools to Study 1-11-Representation of Graphs" (Graphs and Combinatorics 40, 2024).
- The canonical 2025 1-11-representability paper, the adjacent 2024 toolbox paper, and one bounded outside-status check for a later 9-vertex census result.
- artifacts/all-9-vertex-graphs-1-11-representable/record.md
- artifacts/all-9-vertex-graphs-1-11-representable/status.json
