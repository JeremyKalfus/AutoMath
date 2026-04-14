# Working Packet: The Exact Value of R(3,12)

- slug: `r-3-12-classical-ramsey`
- title: Determine the exact value of R(3,12)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `58`
- single-solve-to-paper fraction: `0.52`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red triangle or a blue K_12.

## novelty_notes
- frontier basis: Current public sources leave R(3,12) in the interval 53 <= R(3,12) <= 59, so the theorem slice is stable but materially wider than the preferred one-step or two-step micro-paper targets.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A full exact solve would still produce an immediate title theorem. What remains too large for the micro-paper lane is the expected extension census, witness management, and verification burden across a six-value window.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: moderate
- assessment: Fail for the lane. Strong family anchor, but the exact gap is too wide and the remaining solve packet too bulky.

## likely_paper_shape
- note title: The Exact Value of R(3,12)
- hypothetical title: The Exact Value of R(3,12)
- paper shape: A computational exact-value note in the classical R(3,k) program, but with a larger remaining gap than the preferred queue slots.
- publication if solved: An exact determination of R(3,12) would still be publishable as a classical Ramsey note, but the current gap is too wide for the strict micro-paper objective.
- minimal artifact requirements: Either a new explicit lower-bound witness at the exact frontier or a structural proof closing the full 53-59 interval from above.

## hypothetical_abstract
We determine the classical Ramsey number R(3,12). Existing public sources place this parameter in the interval 53 <= R(3,12) <= 59. Our result closes the current gap in the triangle-versus-clique sequence at k = 12.

## single_solve_explanation
This target still has a real paper shape because an exact value in the R(3,k) sequence is automatically theorem-grade. It fails the micro-paper screen because the current interval is too wide and the likely solve would leave a large verification and exposition burden. The solve would be meaningful, but not close enough to a finished note after one pass.

## broader_theorem_nonimplication
No broader theorem currently forces the exact endpoint at k = 12; the literature still records only separate lower and upper information. The issue is distance to closure, not hidden prior implication.

## literature_gap
Current public sources stop at 53 <= R(3,12) <= 59.

## transfer_kit
- lemma: Current survey/status surfaces record the interval 53 <= R(3,12) <= 59.
- lemma: Exoo's 1993 announcement marks the classical lower-bound improvement line for R(3,12).
- lemma: The standard reformulation turns the problem into triangle-free graph classification with independence number below 12.
- lemma: The R(3,k) extension methodology based on e(3,k,n) values remains the natural attack surface for tightening the upper side.
- toy example: The exact value R(3,9) = 36 is the nearest clean solved benchmark of the same family, and R(3,10) is the freshest one-step frontier in the same sequence.
- known obstruction: The main obstacle is the scale of the triangle-free graph search space across the remaining six-value window.
- prior-work stop sentence: Current public sources stop at 53 <= R(3,12) <= 59.
- recommended first attack: Update and tighten the e(3,12,n) table first, then attack the upper side through one-vertex extension from the best surviving triangle-free catalogs.
- paper if solved: The paper would be a classical R(3,k) exact-value note, but not a strict micro-paper.

## bounded_source_list
- Geoffrey Exoo, "Announcement: On the Ramsey Numbers R(4,6), R(5,6) and R(3,12)" (Ars Combinatoria 35 (1993)) for the lower-bound line; together with bounded 2026-04-14 survey-status checking that still reports the interval 53 <= R(3,12) <= 59.
- Exoo's 1993 lower-bound announcement and bounded 2026-04-14 survey/status checking.
- artifacts/r-3-12-classical-ramsey/record.md
- artifacts/r-3-12-classical-ramsey/status.json
