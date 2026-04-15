# Working Packet: The Exact Value of R(C4, B15)

- slug: `r-c4-b15-quadrilateral-book-ramsey`
- title: Determine the exact value of R(C4, B15)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `63`
- single-solve-to-paper fraction: `0.64`

## statement
Determine the least N such that every graph on N vertices contains a C4 or its complement contains the 15-page book B15.

## novelty_notes
- frontier basis: Current checked sources give exact values through n = 14 and the explicit upper bound R(C4, B15) <= 26, with no later exact closure surfaced in the bounded search.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: This is the smallest fresh ordinary-book case above the quoted exact range, so a clean exact closure would be easy to state and easy to benchmark. The weak point is that the current packet is not yet sharp enough for one-shot publication mode.
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
- assessment: Not lane-eligible. The case is fresh and small, but the literature gap is still too broad for the strict 70-90% paper test.

## likely_paper_shape
- note title: The Exact Value of R(C4, B15)
- hypothetical title: The Exact Value of R(C4, B15)
- paper shape: A short exact-value note on the smallest currently fresh ordinary-book case just above the exact range quoted in the 2022 source.
- publication if solved: An exact determination of R(C4, B15) would be a legitimate short note, but it does not clear the stricter one-shot micro-paper threshold on the current packet.
- minimal artifact requirements: Either a proof that every 26-vertex graph contains C4 or its complement contains B15, or a new lower construction showing the upper bound is not sharp.

## hypothetical_abstract
We determine the Ramsey number R(C4, B15). Current checked sources quote exact values for the quadrilateral-versus-book Ramsey numbers up to n = 14 and yield the explicit upper bound R(C4, B15) <= 26, but do not appear to settle this next case. Any exact closure would add a compact new point to the ordinary-book slice of the family.

## single_solve_explanation
The main reason this falls short of the micro-paper lane is not that the statement is weak, but that the packet is still one theorem too loose. A solve would need to do more than just close a source-isolated gap; it would also need to justify why n = 15 is the right ordinary-book residue to publish on its own. That lowers the solve-to-paper fraction below the required range.

## broader_theorem_nonimplication
The published exact families quoted in the 2022 paper do not include n = 15, and the 2025 broader preprint does not advertise a direct exact closure of this ordinary-book case. The bounded 2026-04-14 searches did not reveal a later theorem settling R(C4, B15).

## literature_gap
Checked sources stop at exact values for r(C4, B_n) through n = 14 together with the explicit upper bound R(C4, B15) <= 26 and nearby exact family values such as R(C4, B18) = 29.

## transfer_kit
- lemma: Li-Lin-Peng 2022 yields R(C4, B15) <= 26 from its upper-bound theorem at (m, t) = (5, 2).
- lemma: The same paper quotes prior exact values of r(C4, B_n) for 1 <= n <= 14.
- lemma: The same paper gives the exact family point R(C4, B18) = 29.
- lemma: The 2025 generalization confirms that quadrilateral-versus-book Ramsey problems remain active without surfacing an exact ordinary-book closure at n = 15.
- toy example: The quoted exact range through n = 14 is the smallest benchmark, while the exact family point R(C4, B18) = 29 gives the nearest higher exact value.
- known obstruction: The checked sources do not currently pin R(C4, B15) into a one-step corridor, so a solve would have to create a sharper packet than the current literature provides.
- prior-work stop sentence: Current checked sources give R(C4, B15) <= 26 and exact values only through n = 14 for the ordinary-book slice.
- recommended first attack: Specialize the 2022 quadrilateral-versus-books counting argument to B15 and test whether the natural upper endpoint 26 can already be forced.
- paper if solved: If solved exactly, the paper would be a short note closing the first fresh ordinary-book case above the exact range quoted in the 2022 source.

## bounded_source_list
- Tianyu Li, Qizhong Lin, and Xing Peng, "Ramsey numbers of the quadrilateral versus books" (Journal of Graph Theory 103(2), 2022), especially the upper-bound theorem r(C4, B_{(m-1)^2+(t-2)}) <= m^2 + t for m >= 4 and 0 <= t <= m-1, which yields R(C4, B15) <= 26; together with the same paper's quoted prior-art exact values through n = 14 and exact family special case R(C4, B18) = 29; together with Chunyang Dou, Tianyu Li, Qizhong Lin, and Xing Peng, "The Ramsey number of the 4-cycle versus a book graph" (preprint, 2025) as a recent family-status check; plus bounded 2026-04-14 exact-statement, alternate-notation, canonical-source, and recent-status searches that did not surface a later exact closure.
- Li-Lin-Peng 2022 for the upper-bound theorem and quoted exact small-n surface; the exact family point R(C4, B18) = 29; the 2025 generalization as a recent status check; and bounded 2026-04-14 exact-term and alternate-notation searches.
- artifacts/r-c4-b15-quadrilateral-book-ramsey/record.md
- artifacts/r-c4-b15-quadrilateral-book-ramsey/status.json
