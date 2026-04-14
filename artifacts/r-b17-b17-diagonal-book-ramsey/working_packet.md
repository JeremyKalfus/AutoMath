# Working Packet: The Exact Value of R(B17, B17)

- slug: `r-b17-b17-diagonal-book-ramsey`
- title: Determine the exact value of R(B17, B17)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `73`
- single-solve-to-paper fraction: `0.72`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B17.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 69 <= R(B17, B17) <= 70. The gap is still only one step, but the larger size increases honest uncertainty about proof compactness.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 69 versus 70 is settled, the result still has a short-note title theorem and a clear literature slot. The residue after the solve is modest, but the certificate may be less compact than for the smaller diagonal cases above.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Pass, but as the weakest eligible slot. The theorem slice is stable and the gap is one step, though certificate compactness and proof plausibility are weaker than for the smaller diagonal cases.

## likely_paper_shape
- note title: The Exact Value of R(B17, B17)
- hypothetical title: The Exact Value of R(B17, B17)
- paper shape: A one-theorem exact-value note for a larger diagonal book Ramsey number, with more certificate risk than the top slots.
- publication if solved: An exact determination of R(B17, B17) would still plausibly support a short note because the public frontier is already a one-step diagonal book Ramsey gap.
- minimal artifact requirements: Either an explicit 69-vertex coloring avoiding monochromatic B17 or a compact proof that every 70-vertex coloring forces B17.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B17, B17). Previous work placed this number in the interval 69 <= R(B17, B17) <= 70. Our result closes the remaining one-step gap for a larger diagonal book pair.

## single_solve_explanation
This target still clears the 70% paper threshold because the frontier is already one endpoint wide in a standard family. After the solve, the note mostly needs the main witness or forcing proof and a short comparison with nearby cases. The only serious downside is a higher risk that the final certificate is bulkier than ideal.

## broader_theorem_nonimplication
The available broad diagonal-book theorem still only gives the generic one-step interval, and the 2026 lower-bound paper does not resolve n = 17. Exact neighboring values such as R(B16, B17) = 67 do not settle the diagonal endpoint.

## literature_gap
Current public sources stop at 69 <= R(B17, B17) <= 70.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 69 <= R(B17, B17) <= 70.
- lemma: The same lemma gives the exact neighboring almost-diagonal value R(B16, B17) = 67.
- lemma: Wesley (2026) shows that recent lower-bound methods continue to reach this size range in the book family, without reporting an exact closure for B17.
- lemma: The same 2025 paper records exact smaller diagonal benchmarks such as R(B8, B8) = 33.
- toy example: The exact neighboring almost-diagonal case R(B16, B17) = 67 is the closest solved benchmark for the intended theorem shape.
- known obstruction: The larger diagonal-book instances may admit many structured critical graphs, so the main risk is a less compact certificate even if the theorem statement itself stays stable.
- prior-work stop sentence: Current sources stop at 69 <= R(B17, B17) <= 70.
- recommended first attack: Exploit the exact R(B16, B17) = 67 boundary as a structural template, then test whether every 69-vertex lower-bound construction collapses under a one-vertex extension by forcing too many common neighbors on some spine.
- paper if solved: The paper would be a short exact-value note settling a larger diagonal book Ramsey number.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 69 <= R(B17, B17) <= 70; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), used as a bounded recent-status and citation check that did not report an exact closure for B17; and bounded 2026-04-14 exact-statement and alternate-notation web checks that did not reveal a later exact determination.
- 2025 EJC Lemma 1 for the one-step interval and family context, 2026 Wesley paper as a recent-status check, and bounded 2026-04-14 exact-statement, synonym, and citation searches.
- artifacts/r-b17-b17-diagonal-book-ramsey/record.md
- artifacts/r-b17-b17-diagonal-book-ramsey/status.json
