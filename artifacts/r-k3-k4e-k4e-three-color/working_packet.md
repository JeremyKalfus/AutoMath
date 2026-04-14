# Working Packet: The Exact Value of R(K3, K4-e, K4-e)

- slug: `r-k3-k4e-k4e-three-color`
- title: Determine the exact value of R(K3, K4-e, K4-e)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `87`
- single-solve-to-paper fraction: `0.84`

## statement
Either prove that every 3-coloring of K21 contains a color-1 triangle or a color-2 or color-3 copy of K4-e and thus show R(K3, K4-e, K4-e) = 21, or construct a 3-coloring of K21 avoiding all three forbidden patterns and thus show R(K3, K4-e, K4-e) = 22.

## novelty_notes
- frontier basis: Current public sources leave this three-color number in the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22. The target has a clear family anchor in small multicolor Ramsey numbers involving K4-e, and no later exact determination surfaced in the bounded audit.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The exact value would itself be the title theorem. The note would need only the proof or witness, a short verification appendix for the extremal coloring if the upper endpoint is correct, and a brief comparison to adjacent K4-e multicolor entries already tabulated in the survey.
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
- assessment: Pass. The theorem slice is stable, the exact window is only one step wide, and the family anchor is strong enough for a genuine short note.

## likely_paper_shape
- note title: The Exact Value of R(K3, K4-e, K4-e)
- hypothetical title: The Exact Value of R(K3, K4-e, K4-e)
- paper shape: A one-theorem exact-value note for a one-gap multicolor Ramsey number with a missing-edge clique target.
- publication if solved: Closing R(K3, K4-e, K4-e) would already support a compact 3-color exact-value note on a one-gap small Ramsey entry involving the first noncomplete 4-vertex graph.
- minimal artifact requirements: Either a proof that every 3-coloring of K21 forces one forbidden pattern, or one explicit 3-coloring of K21 avoiding K3 in one color and K4-e in the other two colors.

## hypothetical_abstract
We determine the 3-color Ramsey number R(K3, K4-e, K4-e). Existing public sources leave this parameter in the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22. Our result closes a compact unresolved point in the small multicolor K4-e table.

## single_solve_explanation
One exact solve would already be the honest main theorem of the note. Because the current literature state is already compressed to a one-gap window, almost all of the remaining paper is the decisive proof or witness and routine contextualization. The result is clearly paper-shaped rather than a remark.

## broader_theorem_nonimplication
General multicolor Ramsey inequalities do not determine this one-gap K4-e instance, and the survey still lists only the narrow 21/22 window. No broader theorem located in the bounded audit collapsed the exact target to an immediate corollary.

## literature_gap
Current public sources support only 21 <= R(K3, K4-e, K4-e) <= 22, and the bounded 2026-04-14 exact-term and alternate-notation audit did not uncover a later exact determination.

## transfer_kit
- lemma: DS1.17 Table XVI records the lower bound R(K3, K4-e, K4-e) >= 21.
- lemma: The same survey table records the upper bound R(K3, K4-e, K4-e) <= 22.
- lemma: By symmetry of the last two colors, any extremal coloring may be normalized up to swapping the two K4-e colors.
- toy example: The 21-vertex lower-bound coloring cited through DS1.17 is the smallest nontrivial witness template directly below the target threshold.
- known obstruction: Any exact upper-bound proof must control triangle creation in one color while simultaneously blocking every almost-clique on four vertices in the other two colors.
- prior-work stop sentence: Current sources stop at the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22.
- recommended first attack: Begin from the cited 21-vertex extremal coloring and perform a disciplined extension analysis, using color-symmetry reductions before any heavier exhaustive branch search.
- paper if solved: The paper would be a short exact-value note on a one-gap 3-color Ramsey number involving K4-e.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 6.5 and Table XVI; the older references cited there for the lower and upper bounds; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14.
- DS1.17 Section 6.5 and Table XVI, the lower- and upper-bound references cited there, plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches on 2026-04-14.
- artifacts/r-k3-k4e-k4e-three-color/record.md
- artifacts/r-k3-k4e-k4e-three-color/status.json
