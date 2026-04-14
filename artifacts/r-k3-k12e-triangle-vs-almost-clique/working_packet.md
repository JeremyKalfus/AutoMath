# Working Packet: The Exact Value of R(K3, K12-e)

- slug: `r-k3-k12e-triangle-vs-almost-clique`
- title: Determine the exact value of R(K3, K12-e)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `71`
- single-solve-to-paper fraction: `0.7`

## statement
Determine the least n such that every red-blue coloring of K_n contains a red triangle or a blue K12-e.

## novelty_notes
- frontier basis: Current public sources leave the pair in the interval 49 <= R(K3, K12-e) <= 53. The case is naturally anchored by the same exact small almost-clique line as the K11-e case, though the narrative is weaker because it is no longer the first unresolved point.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A successful exact closure still gives the paper's main theorem. More contextual explanation would be needed than for the K11-e case, because this is the second unresolved point rather than the first gap after the exact range.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Pass, but barely. This remains paper-shaped if solved, though the narrative is weaker than for the first unresolved point on the line.

## likely_paper_shape
- note title: The Exact Value of R(K3, K12-e)
- hypothetical title: The Exact Value of R(K3, K12-e)
- paper shape: A one-theorem exact-value note on the next unresolved triangle-versus-almost-clique case after K11-e.
- publication if solved: An exact determination of R(K3, K12-e) could still support a short note, because the family narrative is already in place and the survey literature isolates a compact remaining interval.
- minimal artifact requirements: Either a forcing proof at the correct threshold or one explicit critical coloring on n-1 vertices with a compact verification certificate.

## hypothetical_abstract
We determine the Ramsey number R(K3, K12-e). Existing survey data leaves this off-diagonal almost-clique parameter in the interval 49 <= R(K3, K12-e) <= 53. Our result closes one more small unresolved entry on the triangle-versus-almost-clique line.

## single_solve_explanation
This exact solve can still support a short paper, but the leverage is slightly weaker than for the first unresolved K11-e case. The solve itself would still be the title theorem, and the rest of the note would mostly be proof, certificate, and comparison text.

## broader_theorem_nonimplication
The survey still lists only a five-value interval, so no known general theorem settles the case. The main risk is not hidden implication but reduced paper distinctness relative to the immediately preceding unresolved K11-e case.

## literature_gap
Current public sources stop at 49 <= R(K3, K12-e) <= 53.

## transfer_kit
- lemma: DS1.17 Table IIIb records 49 <= R(K3, K12-e) <= 53.
- lemma: The same section records exact predecessor values through R(K3, K10-e) = 37 and then the compact unresolved interval for K11-e.
- lemma: The survey's off-diagonal almost-clique references provide established construction methods for triangle-free critical graphs in the nearby exact range.
- toy example: The exact predecessor R(K3, K10-e) = 37 is the smallest same-family benchmark already pinned down completely.
- known obstruction: Any lower-bound construction must stay triangle-free while keeping the complement below K12-e, and any upper-bound proof must show that triangle-free structure at the threshold already forces a nearly complete complementary subgraph.
- prior-work stop sentence: Current sources stop at 49 <= R(K3, K12-e) <= 53.
- recommended first attack: Exploit the same construction family used on the exact smaller cases and test whether the K11-e extremal regime admits any extension to K12-e before widening the search.
- paper if solved: The paper would be a short exact-value note on another compact unresolved entry of the K3 versus K_t-e table.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Table IIIb in Section 3.1, which records 49 <= R(K3, K12-e) <= 53; together with the same section's exact predecessor data and bounded 2026-04-14 survey/web checks that did not reveal a later exact closure.
- DS1.17 Table IIIb and Section 3.1 commentary, plus bounded 2026-04-14 survey/web checks.
- artifacts/r-k3-k12e-triangle-vs-almost-clique/record.md
- artifacts/r-k3-k12e-triangle-vs-almost-clique/status.json
