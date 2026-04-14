# Working Packet: The Exact Value of R(B10, B10)

- slug: `r-b10-b10-diagonal-book-ramsey`
- title: Determine the exact value of R(B10, B10)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `80`
- single-solve-to-paper fraction: `0.8`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 10-page book graph B10.

## novelty_notes
- frontier basis: Recent literature leaves the exact value at 41 <= R(B10, B10) <= 42, and 41 is a sum of two squares, so the standard diagonal-book exactness shortcut does not settle the lower endpoint.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint is settled, the proof or critical coloring is already the main theorem. The surrounding family story, exact table placement, and comparison benchmarks are already present in the literature.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
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
- assessment: Strong lane fit. This is a one-step diagonal-book gap with clear family anchor and low editorial residue after the solve, though the certificate may be slightly less compact than the top slot.

## likely_paper_shape
- note title: The Exact Value of R(B10, B10)
- hypothetical title: The Exact Value of R(B10, B10)
- paper shape: A one-theorem exact-value note on a diagonal book Ramsey number left at a one-step interval.
- publication if solved: An exact determination of R(B10, B10) would support a compact note because the remaining gap is a single unresolved step in the recent diagonal-book Ramsey table.
- minimal artifact requirements: Either a monochromatic-book-free coloring of K41 or a proof that every coloring of K42 contains a monochromatic B10, with a compact verification certificate.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B10, B10). Current public sources leave this value in the interval 41 <= R(B10, B10) <= 42. Our result closes another one-step gap in the recent diagonal-book Ramsey table.

## single_solve_explanation
The exact value would still be the honest title theorem of a short note. The family story is already present in recent literature, so one solve gets most of the way to publication. The only real residue is clean presentation of the proof or extremal construction.

## broader_theorem_nonimplication
The existing family theorem leaves a genuine two-value gap, and the known exactness shortcut does not apply because 41 is a sum of two squares. No broader result found in the bounded audit implies the answer already.

## literature_gap
Current public sources stop at 41 <= R(B10, B10) <= 42.

## transfer_kit
- lemma: Pchelintsev-Rath-Angeltveit 2025, Theorem 1, implies R(B10, B10) >= 41.
- lemma: The same theorem implies R(B10, B10) <= 42.
- lemma: The note after Theorem 1 does not force exactness here because 41 is a sum of two squares.
- lemma: Wesley 2026 supplies recent constructive family context confirming that the diagonal-book line remains active.
- toy example: The exact solved neighbor R(B8, B8) = 33 illustrates the intended paper form after a diagonal-book exact closure.
- known obstruction: A lower-bound proof requires a K41 coloring avoiding monochromatic B10, while an upper-bound proof must eliminate every such critical coloring at that order.
- prior-work stop sentence: Current sources stop at 41 <= R(B10, B10) <= 42.
- recommended first attack: Try to extend the current constructive templates to K41 and, in parallel, extract forced common-neighbor inequalities that could make K42 unavoidable.
- paper if solved: The paper would be a concise exact-value note on a one-step diagonal-book Ramsey gap.

## bounded_source_list
- Maksim V. Pchelintsev, Peter Rath, and Sebastian Angeltveit, "New lower and upper bounds on Ramsey numbers" (Electronic Journal of Combinatorics 32(4) (2025), #P4.64), Theorem 1 and the note immediately following it, together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026), 114913), and bounded exact-notation, alternate-notation, source-internal, outside-source, and recent-status checks through 2026-04-14.
- Pchelintsev-Rath-Angeltveit 2025, Wesley 2026, and bounded 2026-04-14 exact-statement, synonym, source-internal, outside-source, and recent-status checks.
- artifacts/r-b10-b10-diagonal-book-ramsey/record.md
- artifacts/r-b10-b10-diagonal-book-ramsey/status.json
