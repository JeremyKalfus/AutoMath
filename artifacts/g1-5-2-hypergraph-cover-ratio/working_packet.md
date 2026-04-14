# Working Packet: The Exact Value of g_1(5,2)

- slug: `g1-5-2-hypergraph-cover-ratio`
- title: Determine the exact value of g_1(5,2)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `91`
- single-solve-to-paper fraction: `0.86`

## statement
Prove that every 5-uniform hypergraph with nu^(2)=1 satisfies tau^(2) <= 6, or produce a 5-uniform hypergraph with nu^(2)=1 and tau^(2)=7.

## novelty_notes
- frontier basis: Parker's 2025 paper reduces the problem to the exact two-point gap 6 <= g_1(5,2) <= 7 and explicitly identifies it as the first remaining open case in the m = 2 line.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: Once the endpoint is fixed, the introduction, notation, hierarchy placement, and ambient framework are already in the literature. What remains is mainly the sharp proof or the sharp counterexample and a short comparison paragraph.
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
- assessment: Best current slot. The frontier is a two-point exact-value gap inside an established hierarchy, the theorem slice is stable, and one exact solve would already deliver most of a short publishable note.

## likely_paper_shape
- note title: The Exact Value of g_1(5,2)
- hypothetical title: The Exact Value of g_1(5,2)
- paper shape: A one-theorem exact-value note for the first unresolved m = 2 parameter in the generalized Tuza hierarchy.
- publication if solved: Settling g_1(5,2) would close the first remaining exact m = 2 case in the Aharoni-Zerbib hierarchy and already read like the title theorem of a short hypergraph note.
- minimal artifact requirements: Either a sharp upper-bound proof showing tau^(2) <= 6 whenever nu^(2)=1 in a 5-uniform hypergraph, or one explicit 5-uniform witness with tau^(2)=7 together with verification.

## hypothetical_abstract
We determine the exact value of g_1(5,2), the sharp ratio parameter for 5-uniform hypergraphs with 2-matching number 1. Parker's 2025 paper reduced the problem to the two-point gap 6 <= g_1(5,2) <= 7, and we close that gap. This settles the first remaining exact case in the m = 2 branch of the Aharoni-Zerbib program.

## single_solve_explanation
The surrounding framework and nearly sharp bounds are already published. If the sharp value is 6, the note is an exact upper-bound completion; if the sharp value is 7, the note is an extremal-construction paper. In either direction, the one solve is already most of the paper.

## broader_theorem_nonimplication
Parker's theorem stops exactly at 6 <= g_1(5,2) <= 7, and neither endpoint is forced by the broader Aharoni-Zerbib theory or by the 2025 argument.

## literature_gap
The literature currently proves only that 6 <= g_1(5,2) <= 7 and does not determine which endpoint is sharp.

## transfer_kit
- lemma: Parker 2025 proves the exact frontier bound 6 <= g_1(5,2) <= 7.
- lemma: The lower bound comes from the unique symmetric 2-(11,5,2) design, which already provides a concrete extremal template.
- lemma: The Aharoni-Zerbib framework supplies the ambient definition of g_1(k,m) and explains why exact determination of g_1(5,2) is the first open m = 2 case.
- toy example: The unique symmetric 2-(11,5,2) design is the smallest worked witness already used in the literature to certify the lower side.
- known obstruction: Any proof that g_1(5,2)=6 must rule out one extra 2-cover beyond the design-based lower-bound pattern, while any proof that g_1(5,2)=7 must beat Parker's sharpened upper-bound machinery.
- prior-work stop sentence: Parker's 2025 paper improves the upper bound but stops at the unresolved two-point gap 6 <= g_1(5,2) <= 7.
- recommended first attack: Exploit the nu^(2)=1 overlap structure and refine Parker's case analysis around the 2-(11,5,2) extremal pattern to force a six-set transversal.
- paper if solved: The paper would be a short exact-value note closing the first unresolved m = 2 parameter in the generalized Tuza hierarchy.

## bounded_source_list
- Alex Parker, "New bounds on a generalization of Tuza's conjecture" (Electronic Journal of Combinatorics 32(2) (2025)), together with the Aharoni-Zerbib framework for g_1(k,m), source-internal theorem checks, exact-statement and alternate-notation searches on 2026-04-13 to 2026-04-14, and bounded recent-status checks that did not surface a later resolution.
- Aharoni-Zerbib framework, Parker 2025, source-internal theorem checks, and bounded 2026-04-13 to 2026-04-14 exact-statement and recent-status searches.
- artifacts/g1-5-2-hypergraph-cover-ratio/record.md
- artifacts/g1-5-2-hypergraph-cover-ratio/status.json
