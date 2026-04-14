# Working Packet: The Exact Value of R(K7, K4-e)

- slug: `r-k7-k4e-almost-clique-ramsey`
- title: Determine the exact value of R(K7, K4-e)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.82`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red K7 or a blue K4-e.

## novelty_notes
- frontier basis: The 2021 SDP paper leaves this almost-clique Ramsey number at 28 <= R(K7, K4-e) <= 29. The interval is already paper-shaped because it is a single unresolved binary endpoint with standard notation and a classical family anchor.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact value is settled, the note is nearly complete: state the exact value, present the extremal construction or forcing proof, and briefly place it in the K_m versus K_n-e table. No feeder campaign is required.
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
- assessment: Pass. The gap is only one step, the family is classical, and the post-solve editorial residue is minimal.

## likely_paper_shape
- note title: The Exact Value of R(K7, K4-e)
- hypothetical title: The Exact Value of R(K7, K4-e)
- paper shape: A one-theorem exact-value note for a one-step almost-complete Ramsey gap.
- publication if solved: An exact determination of R(K7, K4-e) would read as the title theorem of a short note because the public frontier is a single unresolved step in a well-established almost-clique Ramsey table.
- minimal artifact requirements: Either an explicit red-blue coloring of K28 with no red K7 and no blue K4-e, or a compact proof that every coloring of K29 forces one of them.

## hypothetical_abstract
We determine the Ramsey number R(K7, K4-e). Current public bounds leave this number at 28 <= R(K7, K4-e) <= 29 after the 2021 semidefinite-programming improvement on the upper side. Our result closes the remaining one-step gap in the two-color almost-clique family.

## single_solve_explanation
This is already the honest title theorem of a short paper: an exact endpoint in a named Ramsey family. After the solve, almost everything else is lightweight packaging around a single construction or obstruction proof. There is no need for a broader theorem program to make the result publishable.

## broader_theorem_nonimplication
The standard inclusion K4-e subset K4 and classical monotonicity only sandwich the value; they do not collapse the endpoint. No broader theorem located in the bounded audit forces 28 or 29 automatically.

## literature_gap
Current public sources stop at 28 <= R(K7, K4-e) <= 29.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 7, gives the upper bound R(K7, K4-e) <= 29.
- lemma: The same theorem table records the matching known lower bound R(K7, K4-e) >= 28 from earlier literature.
- lemma: Subgraph monotonicity gives R(K7, K4-e) <= R(K7, K4), which helps frame the upper side without deciding the exact value.
- lemma: The Dynamic Survey identifies this as a live entry in the almost-complete graph Ramsey tables rather than an isolated curiosity.
- toy example: At the lower endpoint, the literature already certifies a 28-vertex coloring avoiding both a red K7 and a blue K4-e.
- known obstruction: A lower-bound proof needs a very dense blue graph with no K4-e, while an upper-bound proof must show that any attempt to avoid blue K4-e inevitably creates a red K7 one vertex later.
- prior-work stop sentence: Current sources stop at 28 <= R(K7, K4-e) <= 29.
- recommended first attack: Use the 2021 SDP constraints to restrict local blue neighborhoods, then push a case split on whether the blue graph is forced to be too sparse to avoid a red K7.
- paper if solved: The paper would be a short exact-value note in the two-color almost-clique Ramsey family.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 7, which gives 28 <= R(K7, K4-e) <= 29 and cites the earlier lower-bound source for 28; together with the 2024 revision of Radziszowski's Dynamic Survey "Small Ramsey Numbers" as family context and bounded 2026-04-14 exact-notation and recent-status web checks that did not reveal a later exact closure.
- 2021 Lidicky-Pfender theorem table, Dynamic Survey family context, and bounded 2026-04-14 exact-notation and recent-status web checks.
- artifacts/r-k7-k4e-almost-clique-ramsey/record.md
- artifacts/r-k7-k4e-almost-clique-ramsey/status.json
