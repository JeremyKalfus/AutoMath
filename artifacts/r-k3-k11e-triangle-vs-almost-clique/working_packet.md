# Working Packet: The Exact Value of R(K3, K11-e)

- slug: `r-k3-k11e-triangle-vs-almost-clique`
- title: Determine the exact value of R(K3, K11-e)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.72`

## statement
Determine the least n such that every red-blue coloring of K_n contains a red triangle or a blue K11-e.

## novelty_notes
- frontier basis: Current public sources leave the first post-K10 off-diagonal almost-clique case in the interval 42 <= R(K3, K11-e) <= 45. Because the earlier line is already exact for smaller almost-cliques, closing this case has a clear table-completion narrative.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved exactly, the result is already the main theorem. The remaining paper would be short: the proof or extremal coloring, a small verification appendix, and a comparison with the exact predecessor cases.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Pass. This is the first unresolved point after a string of exact predecessor cases, which gives it a strong small-table narrative.

## likely_paper_shape
- note title: The Exact Value of R(K3, K11-e)
- hypothetical title: The Exact Value of R(K3, K11-e)
- paper shape: A one-theorem note closing the first unresolved small off-diagonal triangle-versus-almost-clique case beyond the exact range.
- publication if solved: An exact determination of R(K3, K11-e) would support a concise note on the first unresolved entry after the known exact triangle-versus-almost-clique values up through K10-e.
- minimal artifact requirements: Either a proof that every coloring at the correct threshold forces a red triangle or a blue K11-e, or one explicit critical coloring on n-1 vertices with a compact verification certificate.

## hypothetical_abstract
We determine the two-color Ramsey number R(K3, K11-e). The current survey literature leaves this off-diagonal almost-clique parameter in the interval 42 <= R(K3, K11-e) <= 45. Our result closes the first unresolved entry after the exact range already known for smaller K_t-e targets in the triangle-versus-almost-clique line.

## single_solve_explanation
This exact solve would already be the honest title theorem of the paper. The family anchor is strong because the surrounding smaller cases are already exact, so the note has an immediate before-and-after story. After the solve, only light exposition remains.

## broader_theorem_nonimplication
General off-diagonal recurrences and monotonicity do not fix the value, and the survey still lists a true four-value interval. No broader theorem located in the bounded curation sweep collapses the exact case automatically.

## literature_gap
Current public sources stop at 42 <= R(K3, K11-e) <= 45.

## transfer_kit
- lemma: DS1.17 Table IIIb records 42 <= R(K3, K11-e) <= 45.
- lemma: The same survey section records exact predecessor values on this line through R(K3, K10-e) = 37.
- lemma: DS1.17 also notes that critical graphs for several earlier K3 versus K_t-e cases are known explicitly, providing nearby structural templates.
- toy example: The exact predecessor R(K3, K10-e) = 37 is the smallest same-family benchmark immediately below the target.
- known obstruction: A lower-bound improvement needs a triangle-free coloring whose complement still avoids K11-e, while an upper-bound proof must show that every triangle-free graph on the threshold already has complement containing K11-e.
- prior-work stop sentence: Current sources stop at 42 <= R(K3, K11-e) <= 45.
- recommended first attack: Start by extending exact K10-e critical configurations and test whether the missing-edge target creates a rigid neighborhood pattern before opening a broader search.
- paper if solved: The paper would be a short exact-value note closing the first unresolved small case on the K3 versus K_t-e line beyond the exact range.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Table IIIb in Section 3.1, which records 42 <= R(K3, K11-e) <= 45; together with the same section's exact predecessor data for K10-e and bounded 2026-04-14 survey/web checks that did not reveal a later exact closure.
- DS1.17 Table IIIb and Section 3.1 commentary, plus bounded 2026-04-14 survey/web checks.
- artifacts/r-k3-k11e-triangle-vs-almost-clique/record.md
- artifacts/r-k3-k11e-triangle-vs-almost-clique/status.json
