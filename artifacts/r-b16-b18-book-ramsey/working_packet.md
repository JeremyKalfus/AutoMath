# Working Packet: The Exact Value of R(B16, B18)

- slug: `r-b16-b18-book-ramsey`
- title: Determine the exact value of R(B16, B18)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `63`
- single-solve-to-paper fraction: `0.7`

## statement
Determine the least n such that every graph on n vertices contains a copy of B16 or its complement contains a copy of B18.

## novelty_notes
- frontier basis: Current checked public sources support only 69 <= R(B16, B18) <= 70.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the gap is closed, the theorem already reads like the full title claim of a short note. What remains after the solve is mainly the decisive witness or forcing contradiction, one short comparison paragraph with the exact adjacent line, and routine verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible but weakest in the live queue. The family anchor remains strong and the theorem slice is stable, yet the larger witness scale compresses the certificate advantage.

## likely_paper_shape
- note title: The Exact Value of R(B16, B18)
- hypothetical title: The Exact Value of R(B16, B18)
- paper shape: A one-theorem exact-value note on a larger one-gap almost-diagonal book Ramsey residue where the title theorem still dominates the packet.
- publication if solved: Closing the one-gap case R(B16, B18) would still be enough for a short exact-value note on the almost-diagonal book Ramsey line.
- minimal artifact requirements: Either a 69-vertex graph avoiding B16 whose complement avoids B18, or a forcing proof that every 69-vertex graph contains B16 or its complement contains B18.

## hypothetical_abstract
We determine the two-color Ramsey number R(B16, B18). Existing checked sources leave this almost-diagonal pair in the one-gap corridor 69 <= R(B16, B18) <= 70. Our result closes a bounded unresolved point on the B_{n-2} versus B_n book Ramsey line with a single decisive theorem and minimal post-solve packaging.

## single_solve_explanation
This candidate is right at the lower edge of the 70-90% paper test, but it still clears the lane because the exact closure would itself be the title theorem and only routine packaging would remain. After the solve, the note would mainly need the critical graph or forcing argument, a brief comparison with nearby exact values such as R(B17, B18) = 71 and R(B16, B17) = 67, and a short verification appendix. The main weakness is certificate size, not lack of family anchor.

## broader_theorem_nonimplication
The known exact shortcut for R(B_{n-2}, B_n) when n is congruent to 2 mod 3 does not apply because n = 18. The adjacent exact family R(B_{n-1}, B_n) = 4n - 1 also does not determine the slice (16, 18).

## literature_gap
Publicly checked sources stop at 69 <= R(B16, B18) <= 70.

## transfer_kit
- lemma: Theorem 1 of the 2025 source gives the lower bound R(B16, B18) >= 69.
- lemma: DS1 gives the generic upper bound R(B16, B18) <= 70.
- lemma: Theorem 1 gives the nearby exact values R(B16, B17) = 67 and R(B17, B18) = 71.
- toy example: The exact adjacent case R(B17, B18) = 71 is the nearest solved family anchor directly above the target.
- known obstruction: Any 69-vertex witness must maintain a very narrow allowed codegree band so that neither color creates a large book around any spine edge.
- prior-work stop sentence: Current checked sources stop at the one-gap window 69 <= R(B16, B18) <= 70.
- recommended first attack: Start from the 68-vertex 2-polycirculant lower-bound family behind Theorem 1 and test whether any 69th vertex can be added before attempting a forcing proof at 69.
- paper if solved: The paper would be a short exact-value note on a larger unresolved almost-diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1, which gives 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and therefore 69 <= R(B16, B18); together with Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1, version posted Sep. 6, 2024), which gives the generic upper bound R(Bm, Bn) <= 2(m + n + 1) and therefore R(B16, B18) <= 70; plus William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), checked as a recent outside-source status update and not found to settle this exact pair; plus bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Theorem 1 and note following it, DS1 for the generic upper-bound surface, Wesley 2026 as a recent outside-source status check, and bounded 2026-04-14 exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks.
- artifacts/r-b16-b18-book-ramsey/record.md
- artifacts/r-b16-b18-book-ramsey/status.json
