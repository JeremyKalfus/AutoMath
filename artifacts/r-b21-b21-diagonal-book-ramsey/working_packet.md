# Working Packet: The Exact Value of R(B21, B21)

- slug: `r-b21-b21-diagonal-book-ramsey`
- title: Determine the exact value of R(B21, B21)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `70`
- single-solve-to-paper fraction: `0.72`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B21.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 85 <= R(B21, B21) <= 86. The frontier is still a single endpoint with the exact almost-diagonal value R(B20, B21) = 83 nearby.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 85 versus 86 is settled, the note already has a clean title theorem, a direct comparison with the recent almost-diagonal exact case, and a compact family narrative. The residue after the solve is limited to polishing the decisive witness or forcing argument.
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
- assessment: Pass. The theorem slice is stable, the adjacent exact comparison point helps the story, and one clean solve would still look like most of a short paper.

## likely_paper_shape
- note title: The Exact Value of R(B21, B21)
- hypothetical title: The Exact Value of R(B21, B21)
- paper shape: A one-theorem exact-value note for a diagonal book Ramsey number that remains tightly framed by the recent book-Ramsey literature.
- publication if solved: An exact determination of R(B21, B21) could still support a short note because the public frontier remains a one-step diagonal book Ramsey gap with an adjacent exact benchmark.
- minimal artifact requirements: Either an explicit 85-vertex coloring avoiding monochromatic B21 or a compact proof that every 86-vertex coloring forces B21.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B21, B21). Previous work left this number in the interval 85 <= R(B21, B21) <= 86. Our result closes the remaining one-step gap for this diagonal book pair.

## single_solve_explanation
This target remains inside the strict micro-paper lane because one successful solve would already produce the title theorem, the decisive endpoint resolution, and almost all of the note's literature comparison. The family anchor is still strong and the theorem slice does not drift under the most plausible proof routes. The main downgrade relative to B19 and B20 is only a modest increase in certificate compactness risk.

## broader_theorem_nonimplication
The current broad diagonal-book results still stop at the interval 85 <= R(B21, B21) <= 86, and the nearby exact theorem R(B20, B21) = 83 does not determine the diagonal case. A proof here would therefore remain the honest headline result rather than a generic corollary.

## literature_gap
Current public sources stop at 85 <= R(B21, B21) <= 86.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 85 <= R(B21, B21) <= 86.
- lemma: The same lemma gives the exact neighboring almost-diagonal value R(B20, B21) = 83.
- lemma: The 2025 paper controls monochromatic books through common-neighborhood counts on candidate spine edges.
- lemma: Wesley (2026) provides recent lower-bound constructions and family-level status without closing the diagonal n = 21 case.
- toy example: The exact almost-diagonal case R(B20, B21) = 83 is the nearest solved benchmark for the intended theorem shape.
- known obstruction: The critical diagonal colorings can still be highly structured, so the final argument may need to rule out a small family of block-circulant or polycirculant extremals rather than a single witness.
- prior-work stop sentence: Current public sources stop at 85 <= R(B21, B21) <= 86.
- recommended first attack: Start from the published polycirculant lower-bound architecture and combine it with common-neighborhood forcing to test whether every 85-vertex near-extremal coloring necessarily creates a B21 after any one-vertex extension.
- paper if solved: The paper would be a short exact-value note closing another one-step diagonal book Ramsey gap.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 85 <= R(B21, B21) <= 86 and the exact neighboring almost-diagonal value R(B20, B21) = 83; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)) as a recent family-status and citation check; plus bounded 2026-04-14 exact-statement, family-level, canonical-source, and recent-status web checks that did not reveal a later exact determination.
- 2025 EJC Lemma 1 for the one-step interval and adjacent exact benchmark, Wesley (2026) for recent family status, and bounded 2026-04-14 exact-statement and status searches.
- artifacts/r-b21-b21-diagonal-book-ramsey/record.md
- artifacts/r-b21-b21-diagonal-book-ramsey/status.json
