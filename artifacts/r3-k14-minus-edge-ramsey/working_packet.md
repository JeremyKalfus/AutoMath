# Working Packet: On the Exact Value of R(3, K14-e)

- slug: `r3-k14-minus-edge-ramsey`
- title: Determine the exact value of R(3, K14-e)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `44`
- single-solve-to-paper fraction: `0.47`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red triangle or a blue copy of K14-e.

## novelty_notes
- frontier basis: The public sources checked here still expose the parameter only through the interval 59 <= R(3, K14-e) <= 71.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A solve would still headline the note if it happened. But too much of the final paper would depend on a large computational search and extensive verification, so the exact solve is not close enough to a paper-shaped packet for this curation lane.
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
- certificate compactness: low
- exact gap from source: moderate
- assessment: Not lane-eligible. This is a standard open exact parameter, but it is much too search-heavy for one-shot publication mode.

## likely_paper_shape
- note title: On the Exact Value of R(3, K14-e)
- hypothetical title: The Exact Value of R(3, K14-e)
- paper shape: A computational exact-value note in the triangle-versus-almost-clique family, but at a parameter that is already beyond the easy corridor.
- publication if solved: An exact determination of R(3, K14-e) would be publishable in the standard Ramsey literature, but the remaining campaign is too large for the strict micro-paper objective.
- minimal artifact requirements: A sharp lower-bound construction or exhaustive upper-bound elimination, both at substantially larger orders than the best fresh queue slots above.

## hypothetical_abstract
We determine the Ramsey number R(3, K14-e). The bounded literature audit for this run leaves the value between 59 and 71. Our result would close another open case in the triangle-versus-almost-clique table.

## single_solve_explanation
If solved exactly, the theorem would certainly be the title result of a short computational note. The family anchor is not the problem. The problem is that the path to the solve still looks too large to qualify as a strict micro-paper target.

## broader_theorem_nonimplication
The 2013 table and the 2026 Dynamic Survey still report only a nontrivial interval, and the bounded audit did not reveal a later theorem forcing one endpoint.

## literature_gap
Public sources checked in this run still support only 59 <= R(3, K14-e) <= 71.

## transfer_kit
- lemma: Goedgebeur and Radziszowski (2013) report the interval 59 <= R(3, K14-e) <= 71.
- lemma: The 2026 Dynamic Survey still lists bounds rather than an exact value.
- lemma: Monotonicity places R(3, K14-e) between neighboring complete-clique triangle Ramsey numbers.
- toy example: The exact solved case R(3, K10-e) = 37 is the nearby model for what a finished note in this family looks like.
- known obstruction: At this order the remaining search appears too large for a compact certificate, and the lower-bound side may require constructions beyond the structured families already published.
- prior-work stop sentence: The public literature checked here stops at 59 <= R(3, K14-e) <= 71.
- recommended first attack: Only revisit this target if stronger e(3, J14, n) lower-bound technology or a new constructive family materially shrinks the interval first.
- paper if solved: The paper would be a conventional exact-value note in the triangle-versus-almost-clique literature.

## bounded_source_list
- Jan Goedgebeur and Stanislaw P. Radziszowski, "The Ramsey Number R(3, K10-e) and Computational Bounds for R(3,G)" (Electronic Journal of Combinatorics 20(4) (2013), #P19), especially Table 1 and Theorem 2; Radziszowski's Dynamic Survey "Small Ramsey Numbers" revision #18 (January 6, 2026); and bounded exact-statement, alternate-notation, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact determination.
- Goedgebeur-Radziszowski 2013, Radziszowski DS1 revision #18 (2026), and bounded 2026-04-14 exact-term, alternate-notation, outside-source, and recent-status searches.
- artifacts/r3-k14-minus-edge-ramsey/record.md
- artifacts/r3-k14-minus-edge-ramsey/status.json
