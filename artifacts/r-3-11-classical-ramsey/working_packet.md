# Working Packet: The Exact Value of R(3,11)

- slug: `r-3-11-classical-ramsey`
- title: Determine the exact value of R(3,11)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `71`
- single-solve-to-paper fraction: `0.68`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red triangle or a blue K_11.

## novelty_notes
- frontier basis: Current public sources place R(3,11) in the interval 47 <= R(3,11) <= 50, so the parameter remains classically visible but no longer one-step compressed.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A full exact solve would still provide the title theorem and family placement immediately. The reason it falls outside the strict micro-paper lane is that the likely computational residue is larger and the final packet is less compact than for the best one-step targets.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: small
- assessment: Borderline outside the lane. The theorem slice is stable and the family anchor is strong, but the current gap and expected census burden push the solve-to-paper fraction below the preferred threshold.

## likely_paper_shape
- note title: The Exact Value of R(3,11)
- hypothetical title: The Exact Value of R(3,11)
- paper shape: A one-theorem classical Ramsey note settling the next open off-diagonal R(3,k) parameter after the cleaner one-step case.
- publication if solved: An exact determination of R(3,11) would still support a legitimate short note in the classical R(3,k) sequence, but the solve packet is less compact than the strict micro-paper target.
- minimal artifact requirements: Either an explicit 47- to 49-vertex triangle-free witness meeting the extremal independence constraint or a classification proving the exact threshold by 50 vertices.

## hypothetical_abstract
We determine the classical Ramsey number R(3,11). Existing public bounds place this parameter in the interval 47 <= R(3,11) <= 50. Our result closes the current gap in the next unresolved off-diagonal triangle-versus-clique case after R(3,10).

## single_solve_explanation
A complete solve would still look like the title theorem of a real note because R(3,11) sits in a famous named sequence. However, it fails the strict micro-paper gate because the remaining range is not one-step and the honest proof packet likely needs a heavier census or extension computation. The solve would be most of a paper, but not as cleanly 70-90% as the top micro-paper standard.

## broader_theorem_nonimplication
No broader published theorem fixes the exact value of R(3,11); the literature still separates the lower-bound construction from the upper-bound computation. The risk is packet bulk, not immediate prior implication.

## literature_gap
Current public sources stop at 47 <= R(3,11) <= 50.

## transfer_kit
- lemma: Goedgebeur-Radziszowski (2013) proves the current upper bound R(3,11) <= 50.
- lemma: Exoo's November 2023 update reports a lower-bound construction showing R(3,11) >= 47.
- lemma: The problem is equivalent to classifying triangle-free graphs on up to 49 vertices with independence number below 11.
- lemma: The e(3,k,n) and one-vertex extension framework from the R(3,k) literature supplies the natural route for either proving 50 or improving the lower side.
- toy example: The exact value R(3,9) = 36 and the one-step frontier case R(3,10) in 40 or 41 provide the nearest benchmark shapes.
- known obstruction: The extremal triangle-free search space grows sharply past the R(3,10) scale, so the final packet may require a large residual census.
- prior-work stop sentence: Current public sources stop at 47 <= R(3,11) <= 50.
- recommended first attack: Sharpen the upper-bound side by extending the e(3,11,n) table and pruning candidate degree sequences before any full graph census.
- paper if solved: The paper would be a computational-exact note settling the next unresolved member of the classical R(3,k) sequence.

## bounded_source_list
- Jan Goedgebeur and Stanislaw Radziszowski, "New computational upper bounds for Ramsey numbers R(3,k)" (Electronic Journal of Combinatorics 20(1) (2013)) for the upper bound R(3,11) <= 50; Geoffrey Exoo's Ramsey constructions page with the November 2023 update reporting a new lower bound R(3,11) >= 47; together with bounded 2026-04-14 survey-status checking against Small Ramsey Numbers / current status surfaces.
- Goedgebeur-Radziszowski (2013) for the upper bound, Exoo's 2023 Ramsey update for the lower bound, and bounded 2026-04-14 survey/status checking.
- artifacts/r-3-11-classical-ramsey/record.md
- artifacts/r-3-11-classical-ramsey/status.json
