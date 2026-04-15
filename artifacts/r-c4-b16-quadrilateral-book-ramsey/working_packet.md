# Working Packet: The Exact Value of R(C4, B16)

- slug: `r-c4-b16-quadrilateral-book-ramsey`
- title: Determine the exact value of R(C4, B16)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `65`
- single-solve-to-paper fraction: `0.67`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains the 16-page book B16.

## novelty_notes
- frontier basis: Current checked public sources give exact values through n = 14 and the explicit upper bound R(C4, B16) <= 27, with no later exact closure surfaced in the bounded search.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The family is named and active, and an exact closure would be a real theorem. But the source-backed gap remains broader than the queue should prefer for one-shot publication mode.
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
- assessment: Not lane-eligible. The candidate is fresh and structurally clean, but the publication packet is not yet tight enough.

## likely_paper_shape
- note title: The Exact Value of R(C4, B16)
- hypothetical title: The Exact Value of R(C4, B16)
- paper shape: A small exact-value note on quadrilateral versus books, if the threshold can be forced at the current upper endpoint.
- publication if solved: An exact determination of R(C4, B16) could support a short note, but the current literature packet is still too loose for the strict micro-paper lane.
- minimal artifact requirements: Either a proof that every 27-vertex graph contains C4 or its complement contains B16, or a new lower construction showing the 2022 upper endpoint is not sharp.

## hypothetical_abstract
We determine the Ramsey number R(C4, B16). Current checked sources provide an explicit upper bound of 27 and exact values for smaller ordinary books, but do not appear to settle the 16-page case. Any exact closure would add a compact new theorem to the quadrilateral-book Ramsey literature.

## single_solve_explanation
This is still a plausible short-note theorem if solved exactly, because the named family and small parameter keep the statement readable. But the lack of a source-tight lower corridor means a solve would not automatically supply 70-90% of the final paper. Extra packaging would be needed to explain why this isolated value is the right ordinary-book residue to emphasize.

## broader_theorem_nonimplication
The 2022 exact families do not include n = 16, and the 2025 broader book-graph preprint does not advertise an ordinary-book theorem that forces this exact case. The bounded 2026-04-14 searches did not reveal a later exact-value paper for R(C4, B16).

## literature_gap
Checked sources stop at exact values for r(C4, B_n) through n = 14 together with the explicit upper bound R(C4, B16) <= 27 and nearby exact family values such as R(C4, B18) = 29.

## transfer_kit
- lemma: Li-Lin-Peng 2022 yields R(C4, B16) <= 27 from its upper-bound theorem at (m, t) = (5, 3).
- lemma: The same paper reports that prior work already determines r(C4, B_n) exactly for 1 <= n <= 14.
- lemma: The same paper gives the exact neighboring family point R(C4, B18) = 29.
- lemma: The 2025 quadrilateral-versus-book-graph preprint confirms the family remains active without surfacing an exact ordinary-book closure at n = 16.
- toy example: The exact case R(C4, B18) = 29 is the nearest higher ordinary-book benchmark visible in the checked literature.
- known obstruction: The current packet lacks a sharp lower-bound theorem at n = 16, so the solve has to create both the decisive exact step and part of the surrounding justification.
- prior-work stop sentence: Current checked sources give R(C4, B16) <= 27 and nearby exact family values, but do not appear to settle the exact ordinary-book case n = 16.
- recommended first attack: Test whether the 2022 counting argument can already force the upper endpoint 27 once specialized tightly to B16.
- paper if solved: If solved exactly, the paper would be a brief note pinning down one small ordinary-book residue in the quadrilateral-book family.

## bounded_source_list
- Tianyu Li, Qizhong Lin, and Xing Peng, "Ramsey numbers of the quadrilateral versus books" (Journal of Graph Theory 103(2), 2022), especially the upper-bound theorem r(C4, B_{(m-1)^2+(t-2)}) <= m^2 + t for m >= 4 and 0 <= t <= m-1, which yields R(C4, B16) <= 27; together with the same paper's quoted older exact-value surface through n = 14 and its exact family special case R(C4, B18) = 29; together with Chunyang Dou, Tianyu Li, Qizhong Lin, and Xing Peng, "The Ramsey number of the 4-cycle versus a book graph" (preprint, 2025) as a recent family-status check; plus bounded 2026-04-14 exact-statement, alternate-notation, canonical-source, and recent-status searches that did not surface a later exact closure.
- Li-Lin-Peng 2022 for the ordinary book case and upper-bound theorem; the quoted exact-value surface through n = 14; the neighboring exact family point R(C4, B18) = 29; the 2025 generalization as a recent status check; and bounded 2026-04-14 exact-term and alternate-notation searches.
- artifacts/r-c4-b16-quadrilateral-book-ramsey/record.md
- artifacts/r-c4-b16-quadrilateral-book-ramsey/status.json
