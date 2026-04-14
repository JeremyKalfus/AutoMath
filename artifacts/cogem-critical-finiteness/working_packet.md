# Working Packet: Vertex-Critical Graphs in the Co-Gem-Free Class

- slug: `cogem-critical-finiteness`
- title: Are there only finitely many k-vertex-critical co-gem-free graphs for each k?
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `64`
- single-solve-to-paper fraction: `0.61`

## statement
Either prove finiteness of k-vertex-critical P_4 + P_1-free graphs for every fixed k or produce an infinite family for some k >= 5.

## novelty_notes
- frontier basis: The 2022 paper reduces the global H-free finiteness landscape to H = P_4 + lP_1, and the 2025 follow-up resolves several (co-gem, H)-free subfamilies while leaving the pure co-gem-free case open.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath attempt or near-duplicate for the co-gem-free vertex-critical finiteness problem.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A solution would be publishable, but unlike the top-ranked entries it would still require significant structural exposition and probably a longer case analysis before the paper becomes tight.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: high
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: low
- exact gap from source: broad
- assessment: Fail for the strict lane: strong family anchor, but the exact gap is broad and the post-solve packaging load is likely too large for one-shot publication mode.

## likely_paper_shape
- note title: Vertex-Critical Graphs in the Co-Gem-Free Class
- hypothetical title: Vertex-Critical Graphs in the Co-Gem-Free Class
- paper shape: A structural classification or infinite-family construction note in the H-free vertex-critical program.
- publication if solved: A full co-gem-free finiteness theorem would be a meaningful result in the H-free critical-graph program, but it is farther from one-shot paper readiness than the top queue entries.
- minimal artifact requirements: Either a structural proof yielding a bound on the order of k-vertex-critical co-gem-free graphs for each fixed k, or an explicit infinite family with chromatic-critical certification.

## hypothetical_abstract
We determine whether the co-gem-free class contains only finitely many k-vertex-critical graphs for each fixed k. Previous work reduced the unresolved H-free finiteness landscape to H = P_4 + lP_1 and recent 2025 work settled several co-gem-free subfamilies, leaving the pure co-gem-free case open. Our result either completes this smallest remaining base family or shows that an infinite obstruction family exists.

## single_solve_explanation
A complete positive or negative resolution would certainly be publishable. It misses the strict micro-paper lane because the expected proof likely needs more structural infrastructure and a larger exposition section than a compact last-case completion note. The solve would be important, but not obviously 70-90 percent of the finished paper.

## broader_theorem_nonimplication
The 2022 and 2025 papers settle only proper subfamilies and explicitly leave the pure co-gem-free case unresolved, so no broader published theorem already forces the answer.

## literature_gap
After resolving (gem, co-gem)-free and several other co-gem-free subclasses, the remaining open base family in this line is H = P_4 + lP_1, starting with co-gem-free graphs.

## transfer_kit
- lemma: The 2022 Abuadas-Cameron-Hoang-Sawada paper reduces the remaining H-free finiteness landscape to H = P_4 + lP_1.
- lemma: That same paper proves the (gem, co-gem)-free restriction is finite and characterizes it via complete graphs and clique expansions of C_5.
- lemma: The 2025 Beaton-Cameron paper resolves all order-4 forbidden extra-constraint cases inside the co-gem-free world, sharpening but not closing the base case.
- toy example: Clique expansions of C_5 from the (gem, co-gem)-free classification are the cleanest small models showing how critical graphs can persist inside co-gem-flavored classes.
- known obstruction: The base co-gem-free class is much broader than the already-resolved subfamilies, so any positive proof must survive after the extra forbidden-pattern leverage is removed.
- prior-work stop sentence: Current papers resolve several co-gem-free subfamilies but still leave the pure co-gem-free finiteness question open.
- recommended first attack: Start from the known structural decompositions of co-gem-free graphs and try to force either bounded order or a reproducible inflation mechanism for vertex-critical examples.
- paper if solved: The paper would be a structural finiteness note in the H-free critical-graph program, but it is not a strict micro-paper target.

## bounded_source_list
- Tala Abuadas, Ben Cameron, Chinh T. Hoang, and Joe Sawada, "Vertex-critical (P3 + lP1)-free and vertex-critical (gem, co-gem)-free graphs" (2022 preprint), together with Iain Beaton and Ben Cameron, "Vertex-critical graphs in co-gem-free graphs" (Theoretical Computer Science 1042, 2025).
- The 2022 preprint locating P_4 + lP_1 as the remaining open family, the 2025 co-gem-free subfamily paper, exact-statement searches on co-gem-free vertex-critical finiteness, and bounded 2026 status checks that did not surface a full resolution.
- artifacts/cogem-critical-finiteness/record.md
- artifacts/cogem-critical-finiteness/status.json
