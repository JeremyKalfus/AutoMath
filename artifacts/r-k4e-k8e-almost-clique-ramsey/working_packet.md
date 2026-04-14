# Working Packet: The Exact Value of R(K4-e, K8-e)

- slug: `r-k4e-k8e-almost-clique-ramsey`
- title: Determine the exact value of R(K4-e, K8-e)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.73`

## statement
Determine the least n such that every red-blue coloring of K_n contains a red K4-e or a blue K8-e.

## novelty_notes
- frontier basis: Current public sources still leave R(K4-e, K8-e) in a six-value interval, but the same survey section shows that the neighboring smaller almost-clique cases have already been pinned down exactly. This creates a real table-level frontier rather than a disconnected curiosity.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the interval is closed exactly, the result already supports a short paper. The remaining work is mostly the decisive proof or extremal coloring plus a brief comparison with the exact neighboring almost-clique entries.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Pass, but below the top slot. The family anchor is real and the packaging is light, though the interval is wider than the best candidate.

## likely_paper_shape
- note title: The Exact Value of R(K4-e, K8-e)
- hypothetical title: The Exact Value of R(K4-e, K8-e)
- paper shape: A one-theorem exact-value note for a small almost-clique Ramsey pair.
- publication if solved: An exact value for R(K4-e, K8-e) would support a compact note sharpening the two-color almost-clique Ramsey table at the first unsolved point after several neighboring exact entries.
- minimal artifact requirements: Either a forcing proof at the correct threshold or one explicit extremal coloring at n-1 vertices together with a compact certificate.

## hypothetical_abstract
We determine the two-color Ramsey number R(K4-e, K8-e). Current survey data leaves this almost-clique parameter in the interval 32 <= R(K4-e, K8-e) <= 37. Our result closes a small remaining gap in the exact table for Ramsey numbers involving complete graphs with one edge removed.

## single_solve_explanation
The exact value itself would be the paper's title theorem. The result is not just a tiny curiosity because it sits on a named and systematically tracked almost-clique Ramsey line with exact neighboring anchors. After the solve, only light contextual packaging is needed.

## broader_theorem_nonimplication
Known monotonicity and general almost-clique inequalities bound the value but do not determine it. The survey still lists a genuine interval rather than a value already forced by a broader theorem.

## literature_gap
Current public sources stop at 32 <= R(K4-e, K8-e) <= 37.

## transfer_kit
- lemma: DS1.17 Table IIIa records 32 <= R(K4-e, K8-e) <= 37.
- lemma: The same section records exact neighboring almost-clique values such as R(K4-e, K6-e) = 17 and R(K4-e, K7-e) = 28.
- lemma: DS1.17 notes that all (K4-e, K6-e)-graphs were enumerated and that the critical graph for R(K4-e, K7-e) is unique, giving concrete nearby structural anchors.
- toy example: The exact predecessor R(K4-e, K7-e) = 28 provides the smallest nontrivial same-family benchmark for extension or obstruction arguments.
- known obstruction: A lower-bound advance needs an explicit coloring suppressing both almost-cliques, while an upper-bound proof must rule out a comparatively sparse missing-edge structure on both sides at once.
- prior-work stop sentence: Current sources stop at 32 <= R(K4-e, K8-e) <= 37.
- recommended first attack: Exploit the known exact neighboring almost-clique cases and try to extend their critical configurations before considering any wider search.
- paper if solved: The paper would be a short exact-value note on a small unresolved almost-clique Ramsey number.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Table IIIa in Section 3.1, which records 32 <= R(K4-e, K8-e) <= 37, together with the survey discussion of neighboring exact almost-clique cases and bounded 2026-04-14 survey/web checks that did not reveal a later exact closure.
- DS1.17 Table IIIa and its Section 3.1 commentary, plus bounded 2026-04-14 survey/web checks.
- artifacts/r-k4e-k8e-almost-clique-ramsey/record.md
- artifacts/r-k4e-k8e-almost-clique-ramsey/status.json
