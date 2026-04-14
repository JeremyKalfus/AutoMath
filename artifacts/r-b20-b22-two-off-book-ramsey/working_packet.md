# Working Packet: The Exact Value of R(B20, B22)

- slug: `r-b20-b22-two-off-book-ramsey`
- title: Determine the exact value of R(B20, B22)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `49`
- single-solve-to-paper fraction: `0.55`

## statement
Determine the least N such that every graph on N vertices contains a red copy of B20 or its complement contains a blue copy of B22.

## novelty_notes
- frontier basis: The proved two-off lower pattern stops at n = 21, and the available older exact upper surface does not cover n = 22.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If an exact closure were obtained cleanly, the resulting paper could still be written as a short continuation of the two-off line. But compared with the leading candidate, too much theorem-shape uncertainty remains before solve.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: low
- isolated exact-case risk: high
- broader-theorem implication risk: unresolved
- theorem-slice stability: fragile
- search-heavy: True
- certificate compactness: low
- exact gap from source: broad
- assessment: Not lane-eligible. The family anchor is decent, but the gap from source is too broad and the solve-to-publication distance is too large.

## likely_paper_shape
- note title: The Exact Value of R(B20, B22)
- hypothetical title: The Exact Value of R(B20, B22)
- paper shape: Potentially a one-case continuation note, but only if the proof is unexpectedly clean and the theorem does not immediately reframe as a broader construction theorem.
- publication if solved: A clean exact determination could still be publishable as a one-case continuation of the two-off book line, but only with significant pattern justification.
- minimal artifact requirements: A Ramsey-(B20,B22) witness at the best candidate order or a universal forcing proof at the exact threshold.

## hypothetical_abstract
We determine the Ramsey number R(B20, B22). The current checked literature proves the lower-line pattern only up to n = 21 and does not cheaply certify a sharp corridor for the first uncovered even case n = 22. Any exact closure would therefore need heavier contextual packaging than the leading one-gap candidates.

## single_solve_explanation
This candidate fails the 70-90% test because even a successful solve would leave too much packaging uncertainty. The note would need extra work to explain why this specific pair matters and why the result is not simply a stepping stone toward a broader two-off theorem. That is outside the strict micro-paper lane.

## broader_theorem_nonimplication
The 2025 source explicitly leaves extension of the two-off pattern beyond n = 21 open, and the older exact upper-bound condition n ≡ 2 (mod 3) does not cover n = 22. So direct implication is not known, but the risk of broader theorem drift remains high.

## literature_gap
Checked sources prove only the two-off lower pattern through n <= 21 and do not cheaply certify a sharp exact corridor for R(B20, B22).

## transfer_kit
- lemma: EJC 2025 Theorem 1 proves 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21.
- lemma: The same paper notes an older exact upper bound R(B_{n-2}, B_n) <= 4n - 3 when n ≡ 2 (mod 3), which does not apply at n = 22.
- lemma: Section 4.2.1 records that extending the construction pattern further looked plausible but became computationally expensive.
- lemma: The 2026 lower-bound paper supplies modern construction tools but not a sharp theorem for this exact tuple.
- toy example: The proved neighboring two-off behavior at n = 20 or 21 is the nearest available structural template.
- known obstruction: There is no cheap theorem-level upper corridor here, so any progress likely depends on search-heavy witness construction or expensive upper-bound machinery.
- prior-work stop sentence: Current checked sources stop with the two-off lower theorem at n <= 21 and do not certify a sharp exact corridor for (20,22).
- recommended first attack: Do not prioritize this during live solve; if revisited, start with a search for highly symmetric Ramsey-(B20,B22) witnesses to see whether a compact pattern emerges.
- paper if solved: If solved exactly, the paper would need to be framed as a cautious continuation of the two-off book Ramsey pattern beyond the 2025 theorem range.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), especially Theorem 1 proving 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and Section 4.2.1 discussing extension beyond that range; together with the same paper's note that earlier work already gave R(B_{n-2}, B_n) <= 4n - 3 when n ≡ 2 (mod 3), which does not cover n = 22; and the 2026 paper "Lower bounds for book Ramsey numbers" for surrounding construction infrastructure.
- EJC 2025 Theorem 1 and Section 4.2.1, plus the cited older upper-bound surface and the 2026 lower-bound paper.
- artifacts/r-b20-b22-two-off-book-ramsey/record.md
- artifacts/r-b20-b22-two-off-book-ramsey/status.json
