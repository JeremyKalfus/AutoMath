# Working Packet: The C_4 union C_5 Decomposition of K_9

- slug: `k9-c4-c5-decomposition`
- title: Does K_9 decompose into four copies of C_4 union C_5?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `94`
- single-solve-to-paper fraction: `0.9`

## statement
Either construct a full 4-copy edge decomposition of K_9 into C_4 union C_5 blocks or prove that no such decomposition exists.

## novelty_notes
- frontier basis: The 2018 spectrum theorem handles the odd-order congruence class for unions of two cycles and explicitly carves out the single unresolved exception G = C_4 union C_5 at v = 9.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath mathematical attempt, slug conflict, or near-duplicate for the exact K_9 decomposition into C_4 union C_5, and the bounded curation audit did not surface a post-2018 resolution of the exceptional case.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The theorem statement, motivation, and artifact format are all fixed by the source; after the solve, little remains beyond a short reminder of the general spectrum theorem and a polished certificate.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass: this is a lone named exception to a finished spectrum theorem, the theorem surface is fully stable, and one exact solve would already read like a referee-ready short note.

## likely_paper_shape
- note title: The C_4 union C_5 Decomposition of K_9
- hypothetical title: The C_4 union C_5 Decomposition of K_9
- paper shape: A single exceptional-case completion note for a nearly complete decomposition spectrum.
- publication if solved: Settling the lone excluded C_4 union C_5 case at v = 9 would already be the title theorem of a short completion note for a nearly finished G-design spectrum.
- minimal artifact requirements: Either four explicit edge-disjoint C_4 union C_5 blocks covering E(K_9) or a complete obstruction argument ruling out such a partition.

## hypothetical_abstract
We settle the unique exceptional order left open in the spectrum for complete-graph decompositions into the disconnected graph C_4 union C_5. We either exhibit four edge-disjoint copies of C_4 union C_5 whose union is K_9 or prove that the exceptional order is genuinely impossible. Because the 2018 source already resolves the surrounding spectrum, this one exact result supplies almost the entire paper.

## single_solve_explanation
This is the cleanest possible spectrum-completion target: the literature already proves the ambient theorem and singles out one explicit unresolved exception. If K_9 can be decomposed, the note is a short exceptional-case completion with a four-block certificate; if not, it is a short obstruction note explaining why the lone exception is real. Either way, the solve itself is essentially the title theorem and the main body.

## broader_theorem_nonimplication
The canonical source explicitly excludes G = C_4 union C_5 at v = 9 from its general existence theorem, so the broader published result stops one step short of this exact case rather than implying it.

## literature_gap
The 2018 spectrum theorem covers the relevant congruence class for unions of two cycles except for the single excluded case G = C_4 union C_5 with v = 9.

## transfer_kit
- lemma: The graph C_4 union C_5 has 9 vertices and 9 edges, so K_9 would require exactly four blocks because |E(K_9)| = 36.
- lemma: The 2018 source proves the surrounding complete-graph decomposition spectrum for unions of two cycles and isolates this exact exceptional case rather than a broad unresolved family.
- lemma: Any positive certificate is tiny: four explicit 2-regular spanning subgraphs, each splitting into one 4-cycle and one 5-cycle.
- toy example: The arithmetic sanity check is already the smallest worked model: on 9 labeled vertices, each candidate block must be a spanning 2-regular graph with one 4-cycle and one 5-cycle, and four such blocks must partition all 36 edges of K_9.
- known obstruction: Because every block is spanning and disconnected, the 4-cycle and 5-cycle pieces must mesh across all four colors without reusing any edge, creating very tight local incidence constraints on only nine vertices.
- prior-work stop sentence: The 2018 decomposition paper proves the general spectrum around this case and then stops at the single excluded exception G = C_4 union C_5 with v = 9.
- recommended first attack: Rephrase the problem as a 4-edge-coloring of K_9 into spanning 2-regular color classes, each forced to have component sizes 4 and 5, and use vertex-incidence bookkeeping to complete or obstruct the partition.
- paper if solved: The paper would be a short exceptional-case completion of a nearly finished G-design spectrum, centered on one theorem and one compact decomposition or obstruction certificate.

## bounded_source_list
- Darryn Bryant, Daniel Horsley, Bill Wang, and Marco Buratti, "Decomposing the complete graph and the complete graph minus a 1-factor into copies of a graph G where G is the union of two disjoint cycles" (Electronic Journal of Combinatorics 25, 2018).
- The 2018 two-cycle decomposition paper, exact-statement and alternate-notation checks for the K_9 exception, and a bounded 2026 status search for later follow-up on the exceptional case.
- artifacts/k9-c4-c5-decomposition/record.md
- artifacts/k9-c4-c5-decomposition/status.json
