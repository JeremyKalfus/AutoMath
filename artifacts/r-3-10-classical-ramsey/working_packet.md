# Working Packet: The Exact Value of R(3,10)

- slug: `r-3-10-classical-ramsey`
- title: Determine the exact value of R(3,10)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `88`
- single-solve-to-paper fraction: `0.84`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red triangle or a blue K_10.

## novelty_notes
- frontier basis: Current public sources leave the classical off-diagonal Ramsey number in the interval 40 <= R(3,10) <= 41, so the live frontier is a single unresolved endpoint.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 40 versus 41 is settled, the note already has its title theorem, its complete literature comparison, and its decisive artifact. What remains after the solve is mostly compression of the computational or structural argument into publishable form.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Pass. This is the cleanest fresh tuple found in the bounded curation sweep: a stable theorem slice, a one-step exact gap, strong family anchor, and low post-solve editorial drag.

## likely_paper_shape
- note title: The Exact Value of R(3,10)
- hypothetical title: The Exact Value of R(3,10)
- paper shape: A one-theorem classical Ramsey note closing a one-step off-diagonal gap by either a final lower-bound witness or a final forcing upper bound.
- publication if solved: An exact determination of R(3,10) would plausibly be the title theorem of a short note because the public frontier is already compressed to a one-step classical Ramsey gap.
- minimal artifact requirements: Either an explicit 40-vertex triangle-free graph with independence number 9 or a compact proof that every triangle-free graph on 41 vertices has independence number at least 10.

## hypothetical_abstract
We determine the classical Ramsey number R(3,10). Previous work left this parameter in the interval 40 <= R(3,10) <= 41. Our result closes the remaining one-step gap for the smallest currently exposed off-diagonal triangle-versus-clique case of this form.

## single_solve_explanation
This target clears the 70-90% paper test because one exact solve already gives the note's title theorem, main artifact, and complete comparison with prior bounds. The theorem slice is stable: the honest statement after a successful proof is still exactly R(3,10), not a broader ambient theorem. Residual work is limited to polishing the witness verification or forcing argument and writing a short context section.

## broader_theorem_nonimplication
The current literature only provides the lower witness at 40 and the upper bound 41. No broader published theorem collapses the exact endpoint automatically, so the exact 40-versus-41 decision would remain the headline theorem rather than a corollary.

## literature_gap
Current public sources stop at 40 <= R(3,10) <= 41.

## transfer_kit
- lemma: Exoo (1989) provides a 40-vertex lower-bound construction showing R(3,10) >= 40.
- lemma: Angeltveit (2024) gives the current upper bound R(3,10) <= 41.
- lemma: The standard equivalence reformulates the problem as classifying triangle-free graphs on 40 or 41 vertices with independence number below 10.
- lemma: The R(3,k) computational toolkit based on e(3,k,n) tables and one-vertex extension arguments remains the natural forcing framework for the upper-bound side.
- toy example: The exact value R(3,9) = 36 is the nearest solved benchmark of the same triangle-versus-clique shape.
- known obstruction: Near-extremal triangle-free graphs can be highly structured and almost regular, so the final step may require ruling out a small family of hard residual graphs rather than handling a single sporadic example.
- prior-work stop sentence: Current public sources stop at 40 <= R(3,10) <= 41.
- recommended first attack: Push the upper-bound side first by combining degree restrictions and one-vertex extension over the known triangle-free extremal families at the 40-vertex boundary.
- paper if solved: The paper would be a short classical Ramsey note closing a one-step off-diagonal exact gap.

## bounded_source_list
- Geoffrey Exoo, "On Two Classical Ramsey Numbers of the Form R(3, n)" (SIAM Journal on Discrete Mathematics 2 (1989)) for the lower bound R(3,10) >= 40; Vigleik Angeltveit, "R(3,10) <= 41" (manuscript listed in 2024 status updates) for the current upper bound; together with Stanislaw Radziszowski, "Small Ramsey Numbers" revision 18 (January 6, 2026) and the Leaps in Bounds Ramsey constant page as bounded current-status checks; plus bounded 2026-04-14 exact-statement and recent-status searches that did not reveal a later exact determination.
- Exoo (1989) for the 40-vertex lower bound, Angeltveit (2024) for the 41 upper bound, Radziszowski revision 18 (2026) and Leaps in Bounds for current-status confirmation, and bounded 2026-04-14 exact-statement and recent-status searches.
- artifacts/r-3-10-classical-ramsey/record.md
- artifacts/r-3-10-classical-ramsey/status.json
