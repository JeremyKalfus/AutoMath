# Working Packet: Recolourability of 4-Chromatic (2K2, K4)-Free Graphs

- slug: `2k2-k4-recolourable`
- title: Are all 4-chromatic (2K2, K4)-free graphs recolourable?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `88`
- single-solve-to-paper fraction: `0.82`

## statement
Either prove that every 4-chromatic (2K2, K4)-free graph is recolourable or construct a 4-chromatic (2K2, K4)-free graph with a frozen 5-colouring or disconnected recolouring graph.

## novelty_notes
- frontier basis: Belavadia-Cameron-Hildred prove all neighboring pair-forbidden cases and explicitly identify the 4-chromatic (2K2, K4)-free class as the sole remaining dichotomy gap.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath slug, title, source anchor, or near-duplicate attempt for the exact 4-chromatic (2K2, K4)-free recolourability question.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The frontier already arrives as one named residual case in a near-complete classification; after the solve, the paper mainly needs the proof or counterexample and a short recap of the surrounding results.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: small
- assessment: Pass: this is a stable named last-case completion problem with a compact success certificate and immediate dichotomy leverage.

## likely_paper_shape
- note title: Recolourability of 4-Chromatic (2K2, K4)-Free Graphs
- hypothetical title: Recolourability of 4-Chromatic (2K2, K4)-Free Graphs
- paper shape: A dichotomy-completion note whose main theorem settles the unique unresolved pair-forbidden recolourability class.
- publication if solved: Settling this question would close the last remaining recolourability case for pairs of forbidden four-vertex induced subgraphs and would naturally support a short dichotomy-completion note.
- minimal artifact requirements: Either a structural recolouring proof for every 4-chromatic (2K2, K4)-free graph, or one explicit counterexample carrying a frozen 5-colouring or disconnected R_5(G).

## hypothetical_abstract
We settle the last open recolourability question for graph classes defined by forbidding two induced subgraphs on four vertices. Specifically, we determine whether every 4-chromatic (2K2, K4)-free graph is recolourable. Combined with the 2024-2025 classification of the neighboring cases, this yields the full dichotomy in the four-vertex-pair setting.

## single_solve_explanation
The surrounding classification is already in print and the literature isolates this exact leftover case. A positive solution finishes the dichotomy; a negative solution produces the missing obstruction class. Either way, the solved claim is already the paper's main theorem.

## broader_theorem_nonimplication
The 2025 source proves recolourability for several neighboring classes but explicitly stops at the 4-chromatic (2K2, K4)-free case, so no broader published theorem currently subsumes it.

## literature_gap
The only unresolved four-vertex-pair recolourability case identified in the 2025 source is whether all 4-chromatic (2K2, K4)-free graphs are recolourable.

## transfer_kit
- lemma: Belavadia-Cameron-Hildred prove every 3-chromatic 2K2-free graph is recolourable.
- lemma: The same paper identifies the 4-chromatic (2K2, K4)-free class as the only remaining open case in the pair-forbidden four-vertex setting.
- lemma: The class is already known to be 4-colourable, so the open problem is about recolouring connectivity rather than chromatic feasibility.
- toy example: The 2025 paper highlights the small 4-chromatic examples D2 and F2 carrying frozen 5-colourings in the wider 2K2-free world, giving the first nontrivial objects to compare against the extra K4-free restriction.
- known obstruction: Frozen 5-colourings already occur in nearby 2K2-free classes, so any positive proof must show that the K4-free restriction eliminates exactly those obstruction mechanisms.
- prior-work stop sentence: The 2025 Frozen Colourings paper proves all neighboring cases and then stops at the lone open question of whether all 4-chromatic (2K2, K4)-free graphs are recolourable.
- recommended first attack: Exploit the K4-free restriction on the local structure around any putative frozen 5-colouring and try to force a recolouring move via a minimal-counterexample argument built on the 3-chromatic machinery.
- paper if solved: The paper would be a short dichotomy-completion note for recolourability under two forbidden induced subgraphs on four vertices.

## bounded_source_list
- Manoj Belavadia, Kathie Cameron, and Elias Hildred, "Frozen Colourings in 2K2-Free Graphs" (Electronic Journal of Combinatorics 32(2), 2025).
- The 2025 Frozen Colourings paper, the 2024-2025 pair-forbidden recolourability papers it cites, 2026-04-13 exact-statement and alternate-notation searches on the (2K2, K4)-free case, source-internal theorem checks, and bounded 2025-2026 status searches that did not surface a later resolution.
- artifacts/2k2-k4-recolourable/record.md
- artifacts/2k2-k4-recolourable/status.json
