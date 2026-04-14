# Working Packet: On the Exact Value of R(K4-e, K8)

- slug: `r-k4e-k8-almost-clique-ramsey`
- title: Determine the exact value of R(K4-e, K8)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `58`
- single-solve-to-paper fraction: `0.57`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red copy of K4-e or a blue copy of K8.

## novelty_notes
- frontier basis: The checked sources expose a live exact-value corridor bounded below by 36 and above by 45, with no exact settlement found in the bounded 2026 search.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the value were determined, the result would still be the note's title theorem inside a standard family. However, too much of the eventual paper would still sit inside the search and verification machinery rather than the single final theorem statement.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: moderate
- assessment: Not lane-eligible. The family is standard and the theorem slice is stable, but the interval is too wide and the proof burden is too computational for a one-shot micro-paper target.

## likely_paper_shape
- note title: On the Exact Value of R(K4-e, K8)
- hypothetical title: The Exact Value of R(K4-e, K8)
- paper shape: A one-theorem exact-value note for a complete-versus-almost-complete Ramsey number.
- publication if solved: An exact determination of R(K4-e, K8) would likely support a conventional short Ramsey note, but the current interval is too wide for the strict micro-paper lane.
- minimal artifact requirements: A sharp lower-bound coloring at the endpoint or a complete upper-bound exclusion proof, together with machine-checkable verification of the extremal objects.

## hypothetical_abstract
We determine the Ramsey number R(K4-e, K8), where K4-e is the four-vertex complete graph with one missing edge. The checked literature leaves this parameter between 36 and 45. Our result closes that interval in a standard almost-clique Ramsey family.

## single_solve_explanation
A sharp endpoint would indeed furnish the main theorem of a short note. The surrounding family context is already standard, so the write-up after a solve would be manageable. The target still fails the strict lane because the remaining interval is too wide and the solve is likely to be dominated by extensive computation.

## broader_theorem_nonimplication
The 2022 lower-bound paper reports only the lower endpoint, while the 2009 triangle-count argument gives only an upper endpoint. The bounded audit did not find a later general theorem forcing equality at either end.

## literature_gap
The sources checked here expose only 36 <= R(K4-e, K8) <= 45.

## transfer_kit
- lemma: Goedgebeur and Van Overberghe (2022) report the lower bound 36 <= R(K4-e, K8).
- lemma: Lin and Mackey (2009) report the upper bound R(K4-e, K8) <= 45.
- lemma: The one-edge Ramsey family already has exact nearby values and lower-bound constructions based on structured colorings.
- toy example: The smaller solved one-edge cases in the 2022 paper illustrate the desired extremal-construction style for a successful note.
- known obstruction: The remaining gap is wide enough that a sharp result is unlikely to emerge from a tiny certificate; either endpoint will likely require a substantial computation or a nontrivial new reduction.
- prior-work stop sentence: The bounded audit for this run found only the interval 36 <= R(K4-e, K8) <= 45.
- recommended first attack: Try to tighten the upper side first by adapting triangle-count and gluing arguments before investing in a broad lower-bound search.
- paper if solved: The paper would be an exact-value Ramsey note for a complete-versus-almost-complete pair.

## bounded_source_list
- Jan Goedgebeur and Steven Van Overberghe, "New bounds for Ramsey numbers R(Kk-e, Kl-e)" (Discrete Applied Mathematics 307 (2022)), whose abstract reports the lower bound 36 <= R(K4-e, K8); Andrew Lin and John Mackey, "Counting triangles in some Ramsey graphs" (RIT technical report, 2009), which reports R(K4-e, K8) <= 45; and bounded exact-statement, alternate-notation, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact value.
- Goedgebeur-Van Overberghe 2022, Lin-Mackey 2009, and bounded 2026-04-14 exact-term, alternate-notation, outside-source, and recent-status searches.
- artifacts/r-k4e-k8-almost-clique-ramsey/record.md
- artifacts/r-k4e-k8-almost-clique-ramsey/status.json
