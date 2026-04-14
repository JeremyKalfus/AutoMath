# Working Packet: The Exact Value of R(3,13)

- slug: `r-3-13-classical-ramsey`
- title: Determine the exact value of R(3,13)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `49`
- single-solve-to-paper fraction: `0.44`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red triangle or a blue K_13.

## novelty_notes
- frontier basis: The dynamic survey records 60 <= R(3,13) <= 68, so the theorem slice is stable but the residual band is much wider than the micro-paper target.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A full exact solve would still produce the headline theorem immediately. The reason this slot remains weak is that both the solve residue and the novelty audit are too large relative to the capped curation budget.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: high
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: broad
- assessment: Fail. The family anchor is strong, but the exact gap is broad and the capped audit never became tuple-specific enough to justify live solve priority.

## likely_paper_shape
- note title: The Exact Value of R(3,13)
- hypothetical title: The Exact Value of R(3,13)
- paper shape: A computational exact-value note in the classical off-diagonal Ramsey sequence, with a materially wider frontier band than the preferred lane.
- publication if solved: An exact determination of R(3,13) would still support a real short Ramsey note, but it sits well outside the micro-paper lane.
- minimal artifact requirements: Either an exact new lower-bound witness near the survey upper edge or a strong upper-bound classification collapsing the entire 60-68 band.

## hypothetical_abstract
We determine the classical Ramsey number R(3,13). The dynamic survey records the current interval 60 <= R(3,13) <= 68. Our result closes the next unresolved gap in the triangle-versus-clique sequence beyond k = 12.

## single_solve_explanation
An exact value for R(3,13) would still be the title theorem of a real note, so the family anchor is not the problem. The issue is that the present interval is broad, the likely computation is heavy, and this curation pass did not complete a tuple-specific freshness audit. That combination pushes the one-solve-to-paper fraction well below the micro-paper threshold.

## broader_theorem_nonimplication
The survey still lists only numerical lower and upper bounds; no general theorem collapses the exact endpoint automatically. The concern here is not theorem-slice drift but frontier width and incomplete bounded audit.

## literature_gap
The DS1.17 survey records 60 <= R(3,13) <= 68.

## transfer_kit
- lemma: DS1.17 Table Ia records the current survey interval 60 <= R(3,13) <= 68.
- lemma: The standard equivalence rewrites the problem as classifying triangle-free graphs with independence number below 13.
- lemma: The e(3,k,n) table and one-vertex extension machinery remain the natural forcing framework for the upper-bound side.
- lemma: Nearby exact cases such as R(3,9) = 36 and the tighter frontier at R(3,10) illustrate the same proof architecture on smaller instances.
- toy example: R(3,9) = 36 is the nearest clean solved benchmark in the same family.
- known obstruction: The surviving triangle-free search space is much larger than in the one-step R(3,10) and four-value R(3,11) settings.
- prior-work stop sentence: The DS1.17 survey records 60 <= R(3,13) <= 68.
- recommended first attack: Do not hand this off directly; first complete a tuple-specific exact-status audit, then tighten the upper side through updated e(3,13,n) tables.
- paper if solved: The paper would be an exact-value note in the classical R(3,k) line, but it is not a credible micro-paper target today.

## bounded_source_list
- Stanislaw Radziszowski, "Small Ramsey Numbers" DS1.17 (June 7, 2024), Table Ia, which records 60 <= R(3,13) <= 68; together with a bounded 2026-04-14 family-level web scan that did not surface a later exact announcement, but without a tuple-specific exact-statement audit under the capped search budget.
- Radziszowski DS1.17 Table Ia plus bounded 2026-04-14 family-level search only.
- artifacts/r-3-13-classical-ramsey/record.md
- artifacts/r-3-13-classical-ramsey/status.json
