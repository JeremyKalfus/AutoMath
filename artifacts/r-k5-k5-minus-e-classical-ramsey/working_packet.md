# Working Packet: The Ramsey Number R(K5, K5-e)

- slug: `r-k5-k5-minus-e-classical-ramsey`
- title: Determine the exact value of R(K5, K5-e)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `False`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.73`

## statement
Determine the least N such that every graph on N vertices contains K5 or its complement contains K5 with one edge deleted.

## novelty_notes
- frontier basis: The 2026 dynamic survey records R(K5, K5-e) as one of the last two unsolved entries from Hendry's 5-vertex table, with range 30 to 33.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved, the result would plainly be a real paper. The problem is not paper shape but solve style: the likely burden is large-scale computation, certification, or deep extremal search.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: small
- assessment: Not lane-eligible. The publication value is undeniable, but the probable search and certification load is too high for the strict one-shot micro-paper lane.

## likely_paper_shape
- note title: The Ramsey Number R(K5, K5-e)
- hypothetical title: The Ramsey Number R(K5, K5-e)
- paper shape: A classical exact-value Ramsey note with substantial computational or certificate burden.
- publication if solved: An exact determination of R(K5, K5-e) would be publishable immediately as a classical small-Ramsey note or computational paper.
- minimal artifact requirements: A proof forcing K5 or co-(K5-e) in every graph on N vertices at the sharp threshold, together with critical colorings or certificates at N-1.

## hypothetical_abstract
We determine the classical small Ramsey number R(K5, K5-e). The current checked survey still lists this as one of the two surviving open entries from Hendry's 5-vertex table, with bounds 30 <= R(K5, K5-e) <= 33. Any exact closure would therefore be immediately paper-shaped and historically well anchored.

## single_solve_explanation
An exact solve would already be most of the finished paper because the statement is classical, stable, and historically important. What keeps it out of the strict micro-paper lane is that the likely proof is computationally expensive, with bulky certification rather than a compact reasoning-first packet.

## broader_theorem_nonimplication
The 2026 survey still lists R(K5, K5-e) as open, which rules out any known broader theorem already forcing the exact value. The open interval 30 to 33 itself is the current frontier summary.

## literature_gap
Checked sources stop at the range 30 <= R(K5, K5-e) <= 33, with no exact closure surfaced in this run's bounded status audit.

## transfer_kit
- lemma: Radziszowski's 2026 survey records the current bounds 30 <= R(K5, K5-e) <= 33.
- lemma: The same survey states that only R(K5, K5-e) and R(5,5) remain open from Hendry's 5-vertex table.
- lemma: The same section records nearby exact solved cases such as R(K5, K5-P3) = 25.
- lemma: The survey's historical summary shows that the surrounding 5-vertex landscape is otherwise largely closed.
- toy example: A nearby exact benchmark in the same small-graph landscape is R(K5, K5-P3) = 25.
- known obstruction: The open interval is small, but likely closing it requires heavy search or exhaustive critical-coloring certification rather than a light structural argument.
- prior-work stop sentence: Current checked sources still give only 30 <= R(K5, K5-e) <= 33.
- recommended first attack: Treat the 30-33 corridor as a critical-graph generation problem and try to kill the top endpoint first with modern maximal-Ramsey graph enumeration.
- paper if solved: If solved exactly, the paper would be a classical exact-value Ramsey note closing one of the last surviving 5-vertex table entries.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics Dynamic Survey DS1 revision 18, 2026), Section 5.12 and Section 3.1, recording that after decades of progress on Hendry's table only R(K5, K5-e) and R(5,5) remain open, with 30 <= R(K5, K5-e) <= 33; bounded 2026 exact-statement, alternate-notation, and recent-status searches in this run did not surface a later exact closure.
- Radziszowski 2026 survey, the historical Hendry table context, nearby solved 5-vertex cases from the same survey, and bounded 2026 status searches run here.
- artifacts/r-k5-k5-minus-e-classical-ramsey/record.md
- artifacts/r-k5-k5-minus-e-classical-ramsey/status.json
