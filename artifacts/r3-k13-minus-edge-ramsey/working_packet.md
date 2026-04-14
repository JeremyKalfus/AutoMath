# Working Packet: On the Exact Value of R(3, K13-e)

- slug: `r3-k13-minus-edge-ramsey`
- title: Determine the exact value of R(3, K13-e)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `66`
- single-solve-to-paper fraction: `0.63`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red triangle or a blue copy of K13-e.

## novelty_notes
- frontier basis: The 2013 Goedgebeur-Radziszowski table records 55 <= R(3, K13-e) <= 62, and the January 6, 2026 Dynamic Survey still lists this corridor rather than an exact value.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact value is settled, the family context, monotonicity comparisons, and prior computational framework are already available. The main missing ingredient is the decisive extremal certificate or impossibility proof at the sharp endpoint.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: small
- assessment: Best fresh slot found after excluding previously attempted local targets, but still outside the strict lane. The family anchor is good and the theorem slice is stable, yet the remaining search burden is too large for a clean 70-90% paper solve.

## likely_paper_shape
- note title: On the Exact Value of R(3, K13-e)
- hypothetical title: The Exact Value of R(3, K13-e)
- paper shape: A one-theorem exact-value note in the triangle-versus-almost-clique family, centered on one missing-edge target.
- publication if solved: An exact determination of R(3, K13-e) would support a recognizable short computational Ramsey note, but the remaining search and certification burden is still heavier than the strict micro-paper lane prefers.
- minimal artifact requirements: Either an explicit triangle-free graph on n-1 vertices whose complement avoids K13-e at the sharp lower endpoint, or a full nonexistence certificate forcing the sharp upper endpoint.

## hypothetical_abstract
We determine the Ramsey number R(3, K13-e), where K13-e denotes the 13-vertex complete graph with one missing edge. Goedgebeur and Radziszowski left this parameter in the interval 55 <= R(3, K13-e) <= 62. Our result closes that gap for the next unsolved triangle-versus-almost-clique parameter beyond the exact J10 case.

## single_solve_explanation
An exact value would still be the honest title theorem of a short note because the family is standard and the prior computational framework is already in place. The note would mainly consist of the sharp witness or sharp upper-bound certification plus a short comparison to the J10-J16 table. The reason it misses the strict lane is that the remaining computational residue is not obviously tiny.

## broader_theorem_nonimplication
The known monotonicity chain R(3, 12) <= R(3, K13-e) <= R(3, 13) only traps the number inside a seven-value interval, and the 2013 paper does not extract an endpoint. The bounded 2026 audit did not uncover a later general theorem collapsing this case.

## literature_gap
Public sources checked in this run still support only 55 <= R(3, K13-e) <= 62.

## transfer_kit
- lemma: Goedgebeur and Radziszowski (2013) give the current public interval 55 <= R(3, K13-e) <= 62.
- lemma: Their Table 1 places R(3, K13-e) between the neighboring complete-clique bounds R(3, 12) and R(3, 13).
- lemma: The same paper records a circulant lower-bound witness for the 54-vertex case used to establish the lower side.
- lemma: The January 6, 2026 Dynamic Survey still reports bounds rather than an exact value.
- toy example: The exact solved neighbor R(3, K10-e) = 37 from the same 2013 paper gives the intended proof-and-certificate model for a finished note.
- known obstruction: Any sharp lower-bound witness beyond the published circulant construction may need genuinely noncirculant structure, while the upper-bound route requires exhaustive exclusion over a large triangle-free search space.
- prior-work stop sentence: The public literature checked here stops at 55 <= R(3, K13-e) <= 62.
- recommended first attack: Push the e(3, J13, n) deficiency analysis and neighbor-gluing machinery beyond the published range while running targeted noncirculant searches at 55-61.
- paper if solved: The paper would be a compact exact-value note in the triangle-versus-almost-clique corridor.

## bounded_source_list
- Jan Goedgebeur and Stanislaw P. Radziszowski, "The Ramsey Number R(3, K10-e) and Computational Bounds for R(3,G)" (Electronic Journal of Combinatorics 20(4) (2013), #P19), especially Table 1 and Theorem 2; Radziszowski's Dynamic Survey "Small Ramsey Numbers" revision #18 (January 6, 2026); and bounded exact-statement, alternate-notation, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact determination.
- Goedgebeur-Radziszowski 2013, Radziszowski DS1 revision #18 (2026), and bounded 2026-04-14 exact-term, synonym, outside-source, and recent-status searches.
- artifacts/r3-k13-minus-edge-ramsey/record.md
- artifacts/r3-k13-minus-edge-ramsey/status.json
