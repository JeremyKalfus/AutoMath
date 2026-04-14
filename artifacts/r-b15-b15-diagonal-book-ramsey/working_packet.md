# Working Packet: The Exact Value of R(B15, B15)

- slug: `r-b15-b15-diagonal-book-ramsey`
- title: Determine the exact value of R(B15, B15)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.75`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 15-page book graph B15.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 61 <= R(B15, B15) <= 62, so the remaining frontier is already one endpoint wide.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint is settled, the note already has its title theorem, family placement, and main extremal artifact. The residue after the solve is mostly a compact proof write-up rather than additional theorem building.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Eligible but slightly weaker than the smaller one-step cases. The family anchor remains strong and the gap is one step, though the larger order modestly increases certificate and packaging risk.

## likely_paper_shape
- note title: The Exact Value of R(B15, B15)
- hypothetical title: The Exact Value of R(B15, B15)
- paper shape: A one-theorem exact-value note for a larger diagonal book Ramsey number.
- publication if solved: An exact determination of R(B15, B15) would still read as the title theorem of a short note because the public frontier is already a one-step diagonal book Ramsey gap.
- minimal artifact requirements: Either an explicit 61-vertex coloring avoiding monochromatic B15 or a compact proof that every 62-vertex coloring forces B15.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B15, B15). Previous work placed this number in the interval 61 <= R(B15, B15) <= 62. Our result closes the remaining one-step gap for a larger diagonal book pair.

## single_solve_explanation
This target still passes the paper test because the public frontier is a one-step exact-value problem in a standard family. After the solve, the note mainly needs the main witness or forcing proof and a concise literature comparison. The only downgrade versus the top slot is a modest risk that the larger order produces a slightly bulkier certificate.

## broader_theorem_nonimplication
Known diagonal-book results still only provide the generic one-step interval, and the recent 2026 lower-bound paper does not settle n = 15. Exact neighboring cases such as R(B14, B15) = 59 do not force the diagonal endpoint.

## literature_gap
Current public sources stop at 61 <= R(B15, B15) <= 62.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe 2025, Lemma 1, gives 61 <= R(B15, B15) <= 62.
- lemma: The same lemma gives the exact neighboring almost-diagonal value R(B14, B15) = 59.
- lemma: Wesley 2026 provides recent diagonal and almost-diagonal lower-bound constructions that confirm ongoing frontier activity in the family.
- lemma: The same 2025 paper records exact smaller diagonal benchmarks such as R(B8, B8) = 33.
- toy example: The exact neighboring almost-diagonal case R(B14, B15) = 59 is the nearest solved model for a compact write-up in the same corridor.
- known obstruction: At this order, symmetric lower-bound colorings may still be numerous, so the main risk is a larger family of critical 61-vertex constructions rather than theorem-scope drift.
- prior-work stop sentence: Current sources stop at 61 <= R(B15, B15) <= 62.
- recommended first attack: Start from the 4n + 1 diagonal lower-bound template at order 61 and combine common-neighborhood counting with symmetry reduction to test whether any 62-vertex extension can avoid a monochromatic B15.
- paper if solved: The paper would be a short exact-value note settling a larger diagonal book Ramsey number.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1, together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026), 114913), and bounded exact-statement, alternate-notation, outside-source, and recent-status checks through 2026-04-14.
- Lidicky-McKinley-Pfender-Van Overberghe 2025, Wesley 2026, source-internal neighboring exact values, and bounded 2026-04-14 exact-term, synonym, outside-source, and recent-status checks.
- artifacts/r-b15-b15-diagonal-book-ramsey/record.md
- artifacts/r-b15-b15-diagonal-book-ramsey/status.json
