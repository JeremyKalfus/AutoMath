# Working Packet: The Exact Value of GR(4, K4, 2)

- slug: `gr4-k4-at-most-two-colors`
- title: Determine the exact value of GR(4, K4, 2)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.73`

## statement
Determine the least n such that every 4-edge-coloring of K_n contains a copy of K4 using at most 2 colors.

## novelty_notes
- frontier basis: Current public sources support only 15 <= GR(4, K4, 2) <= 17.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The exact statement is already clean and title-worthy, while the surrounding family context and neighboring exact values are already available in the same source. After a solve, the remaining write-up would mostly be the extremal coloring or forcing proof and a short comparison with GR(3, K4, 2) and GR(4, K4, 3).
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
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
- assessment: Lane-eligible. The parameter is small, the statement is stable, and one exact closure would already carry most of the editorial burden of a short paper.

## likely_paper_shape
- note title: The Exact Value of GR(4, K4, 2)
- hypothetical title: The Exact Value of GR(4, K4, 2)
- paper shape: A one-theorem exact-value note in the small generalized Ramsey-number family.
- publication if solved: An exact determination of GR(4, K4, 2) would already support a compact note in the newly initiated small generalized Ramsey program.
- minimal artifact requirements: Either an explicit 4-coloring on 14, 15, or 16 vertices meeting the lower endpoint, or a complete forcing certificate for the upper endpoint.

## hypothetical_abstract
We determine GR(4, K4, 2), the least n such that every 4-edge-coloring of K_n contains a copy of K4 using at most two colors. The current published bounds leave this parameter in the interval 15 <= GR(4, K4, 2) <= 17. Our result closes one of the smallest unresolved cases in the generalized small Ramsey program initiated in recent work.

## single_solve_explanation
If solved exactly, this would still be the honest title theorem of the note rather than a corollary. The surrounding paper would need only the sharp extremal certificate, a concise explanation of the method, and a short positioning paragraph relative to the exact nearby values GR(3, K4, 2) = 10 and GR(4, K4, 3) = 10. The target is not just a curiosity because it sits inside a named recent program whose authors explicitly began charting these small generalized parameters.

## broader_theorem_nonimplication
The 2025 paper gives only the corridor 15-17 for this exact tuple, and the available project materials describe methods rather than a theorem collapsing the case. The bounded 2026 status check did not reveal a later paper that settles this exact value.

## literature_gap
Publicly checked sources stop at 15 <= GR(4, K4, 2) <= 17.

## transfer_kit
- lemma: Table 1 of the 2025 paper gives the bounds 15 <= GR(4, K4, 2) <= 17.
- lemma: The same table records the exact benchmark GR(3, K4, 2) = 10.
- lemma: The same source also gives GR(4, K4, 3) = 10, showing that the family already has nearby exact anchors.
- toy example: The exact value GR(4, K4, 3) = 10 is the smallest same-clique, same-color-count benchmark in the paper.
- known obstruction: Extremal colorings can mimic highly symmetric multipartite or circulant patterns, so a naive search may produce many near-miss colorings before a decisive obstruction appears.
- prior-work stop sentence: Current checked sources stop at 15 <= GR(4, K4, 2) <= 17.
- recommended first attack: Run bottom-up generation or SAT-style pruning on 4-colorings of K15 and K16 while exploiting the at-most-two-colors-on-K4 reformulation as a local constraint.
- paper if solved: The paper would be a short exact-value note in the small generalized Ramsey-number program.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1 and Section 3, which give 15 <= GR(4, K4, 2) <= 17 and describe the lower-bound and upper-bound machinery; together with the 2024 arXiv preprint version and the authors' project page, plus bounded exact-statement and recent-status web checks on 2026-04-14 that did not reveal a later exact determination.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Table 1 and Section 3, the 2024 arXiv/preprint version, the project page hosting certificates and constructions, and bounded 2026-04-14 exact-term and recent-status web checks.
- artifacts/gr4-k4-at-most-two-colors/record.md
- artifacts/gr4-k4-at-most-two-colors/status.json
