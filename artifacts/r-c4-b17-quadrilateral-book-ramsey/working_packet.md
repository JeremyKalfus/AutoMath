# Working Packet: The Exact Value of R(C4, B17)

- slug: `r-c4-b17-quadrilateral-book-ramsey`
- title: Determine the exact value of R(C4, B17)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `68`
- single-solve-to-paper fraction: `0.69`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains the 17-page book B17.

## novelty_notes
- frontier basis: Current checked public sources give exact values through n = 14, the 2022 theorem yields R(C4, B17) <= 28, and no later exact closure surfaced in the bounded 2026-04-14 search.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved exactly, the note would already have a legitimate title theorem and a classical family anchor. However, the current literature packet still lacks the sort of tight source-backed corridor that would make the solve itself 70-90% of the eventual paper.
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
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: moderate
- assessment: Not lane-eligible. The family anchor is strong and the theorem slice is stable, but the packet is not source-tight enough for a one-shot micro-paper solve.

## likely_paper_shape
- note title: The Exact Value of R(C4, B17)
- hypothetical title: The Exact Value of R(C4, B17)
- paper shape: A single-theorem exact-value note on a small quadrilateral-book residue, with a compact proof if the threshold can be forced sharply.
- publication if solved: An exact determination of R(C4, B17) would be publishable as a short note on quadrilateral-book Ramsey numbers, but the current packet is not yet close enough to paper-ready for the strict micro-paper lane.
- minimal artifact requirements: Either a proof that every 28-vertex graph contains C4 or its complement contains B17, or a sharp lower construction showing the upper bound is not tight.

## hypothetical_abstract
We determine the Ramsey number R(C4, B17). Current checked sources give a modern exact-family framework for quadrilateral-book Ramsey numbers and yield the explicit upper bound R(C4, B17) <= 28, but do not appear to settle this exact case. An exact closure would turn one bounded unresolved point in a named family into a short stand-alone note.

## single_solve_explanation
This target is close to paper-shaped because the honest title theorem would still be the exact candidate itself, not merely a corollary. But it misses the strict micro-paper lane because the current source-backed frontier is not yet one-step sharp, so a solve would still need some extra context-building and lower-bound packaging. That keeps the single-solve-to-paper fraction just below the required threshold.

## broader_theorem_nonimplication
The 2022 paper proves exact values for infinitely many ordinary book parameters and quotes exact values up to n = 14, but its stated exact families do not include n = 17. The 2025 generalization studies the broader book-graph setting and does not advertise a direct exact closure of R(C4, B17).

## literature_gap
Checked sources stop at the combination of exact values for r(C4, B_n) through n = 14, the explicit upper bound R(C4, B17) <= 28 from the 2022 theorem, and nearby exact family points such as R(C4, B18) = 29.

## transfer_kit
- lemma: Li-Lin-Peng 2022 gives the upper-bound theorem r(C4, B_{(m-1)^2+(t-2)}) <= m^2 + t for m >= 4 and 0 <= t <= m-1, which yields R(C4, B17) <= 28 at (m, t) = (5, 4).
- lemma: The same 2022 paper states that prior work already determines the exact values of r(C4, B_n) for 1 <= n <= 14.
- lemma: The same 2022 paper records the exact special case R(C4, B18) = 29 via its prime-power family.
- lemma: The 2025 quadrilateral-versus-book-graph generalization shows the family remains active without surfacing an exact ordinary-book closure at n = 17.
- toy example: The exact neighboring case R(C4, B18) = 29 is the closest family benchmark just above the target.
- known obstruction: The current checked literature does not yet expose a sharp lower-bound corridor for n = 17, so an exact solve needs either a fresh lower construction or a forcing proof tight at 28.
- prior-work stop sentence: Current checked sources give R(C4, B17) <= 28 and nearby exact family values, but do not appear to settle the exact case n = 17.
- recommended first attack: Try to force the upper endpoint 28 first by adapting the common-neighbor counting from the 2022 quadrilateral-versus-books argument and comparing against the exact n = 18 benchmark.
- paper if solved: If solved exactly, the paper would be a short quadrilateral-book exact-value note centered on one small unresolved ordinary-book case.

## bounded_source_list
- Tianyu Li, Qizhong Lin, and Xing Peng, "Ramsey numbers of the quadrilateral versus books" (Journal of Graph Theory 103(2), 2022), especially the abstracted upper-bound theorem r(C4, B_{(m-1)^2+(t-2)}) <= m^2 + t for m >= 4 and 0 <= t <= m-1, which yields R(C4, B17) <= 28; together with the same paper's quoted prior-art surface giving exact values for r(C4, B_n) for 1 <= n <= 14 and its exact family special case R(C4, B18) = 29; together with Chunyang Dou, Tianyu Li, Qizhong Lin, and Xing Peng, "The Ramsey number of the 4-cycle versus a book graph" (preprint, 2025) as a recent family-status check; plus bounded 2026-04-14 exact-statement, alternate-notation, canonical-source, and recent-status searches that did not surface a later exact closure.
- Li-Lin-Peng 2022 for the ordinary book case and its upper-bound theorem; the quoted older exact small-n surface up to n = 14; the exact neighboring special case R(C4, B18) = 29; the 2025 quadrilateral-versus-book-graph generalization as a recent status check; and bounded 2026-04-14 exact-term and alternate-notation searches.
- artifacts/r-c4-b17-quadrilateral-book-ramsey/record.md
- artifacts/r-c4-b17-quadrilateral-book-ramsey/status.json
