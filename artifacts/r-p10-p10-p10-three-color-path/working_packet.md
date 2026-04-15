# Working Packet: The Three-Color Ramsey Number of P10

- slug: `r-p10-p10-p10-three-color-path`
- title: Determine the exact value of R(P10, P10, P10)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `79`
- single-solve-to-paper fraction: `0.75`

## statement
Determine the least N such that every 3-coloring of the edges of K_N contains a monochromatic path on 10 vertices.

## novelty_notes
- frontier basis: The 2026 survey records the Faudree-Schelp formula as exact for n <= 9 and asymptotically true for large n, with P10 marked as the first unresolved diagonal case.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If R(P10, P10, P10) is settled, the note already has a named conjecture, exact solved neighbors, and a natural target value 18. The post-solve paper work would mostly be lightweight positioning.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Lane-eligible. The theorem slice is stable, the family is classical, and one exact solve would already amount to most of a real short note.

## likely_paper_shape
- note title: The Three-Color Ramsey Number of P10
- hypothetical title: The Three-Color Ramsey Number of P10
- paper shape: A first-open-case exact note for the diagonal three-color path formula.
- publication if solved: An exact determination of R(P10, P10, P10) would support a short note on the first unresolved diagonal three-color path case.
- minimal artifact requirements: Either a proof that every 3-coloring of K18 contains a monochromatic P10, or a 17-vertex coloring with no monochromatic P10 disproving the expected value.

## hypothetical_abstract
We determine the three-color Ramsey number R(P10, P10, P10). The current checked literature makes P10 the first unresolved diagonal case after exact values through P9 and the known asymptotic formula for large n. This gives a compact and natural short-note target tied directly to the classical Faudree-Schelp conjecture.

## single_solve_explanation
A single exact solve would provide the title theorem, the main result, and most of the narrative. What would remain is mostly a brief comparison with the exact P9 value and the conjectured general formula. That is a near-ideal micro-paper shape.

## broader_theorem_nonimplication
The asymptotic path theorem only covers sufficiently large n, and the survey explicitly isolates P10 as the first unresolved diagonal case. So no broader published theorem currently collapses the exact P10 claim.

## literature_gap
Current checked sources give exact diagonal three-color path values through P9 and the asymptotic formula for large n, but still leave R(P10, P10, P10) open.

## transfer_kit
- lemma: Radziszowski's 2026 survey records the Faudree-Schelp conjecture R(P_n, P_n, P_n) = 2n - 2 + (n mod 2).
- lemma: The same survey records the exact values R_3(P8) = 14 and R_3(P9) = 17 from Dzido-Dybczyński-Radziszowski.
- lemma: The same section records that the diagonal three-color path formula is exact for all sufficiently large n.
- lemma: The survey explicitly identifies P10 as the first unresolved diagonal case.
- toy example: The exact neighboring benchmark R(P9, P9, P9) = 17 is already recorded in the checked survey.
- known obstruction: The current packet does not expose a published exact small-n forcing argument at n = 10, so the gap between the exact small table and the asymptotic theorem still has to be bridged directly.
- prior-work stop sentence: Current checked sources settle the diagonal three-color path formula through P9 and for large n, but not for P10.
- recommended first attack: Try to force the conjectured value 18 by adapting the exact P9 critical-coloring analysis to 17-vertex colorings and exploiting the strong path-vs-cycle transfer heuristics in the survey.
- paper if solved: If solved exactly, the paper would be a short note determining the first open diagonal three-color path Ramsey number.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics Dynamic Survey DS1 revision 18, 2026), Section 6.4, citing the Faudree-Schelp conjecture R(P_n, P_n, P_n) = 2n - 2 + (n mod 2), the exact table through P9 from Dzido-Dybczyński-Radziszowski, and the large-n theorem of Gyárfás-Ruszinkó-Sárközy-Szemerédi; bounded 2026 exact-statement, alternate-notation, and recent-status searches in this run did not surface a later exact closure of R(P10, P10, P10).
- Radziszowski 2026 survey Section 6.4, the Faudree-Schelp conjecture, the exact small-n path table through P9, the Gyárfás-Ruszinkó-Sárközy-Szemerédi asymptotic theorem, and bounded 2026 status searches run here.
- artifacts/r-p10-p10-p10-three-color-path/record.md
- artifacts/r-p10-p10-p10-three-color-path/status.json
