# Working Packet: The Exact Value of GR(3, K5, 2)

- slug: `gr-3-k5-2-generalized-ramsey`
- title: Determine the exact value of GR(3, K5, 2)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `63`
- single-solve-to-paper fraction: `0.67`

## statement
Determine the minimum N such that every 3-edge-coloring of KN contains a copy of K5 using at most 2 colors; current public bounds leave N in {20, 21, 22, 23}.

## novelty_notes
- frontier basis: Current public sources leave this parameter in the four-value window 20 <= GR(3, K5, 2) <= 23. The family is genuinely frontier-facing, but the current gap is not yet as compressed as the top-ranked queue entries.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A complete exact determination would still give a natural title theorem. However, the paper would need more proof-management and possibly more extremal-coloring discussion than the one-gap candidates, so the solve-to-paper fraction falls below the preferred range.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: moderate
- assessment: Borderline fail for the strict lane. The family anchor is real, but the current interval is still wide enough that the one-solve-to-paper fraction is less clearly in the target 0.70-0.90 band.

## likely_paper_shape
- note title: The Exact Value of GR(3, K5, 2)
- hypothetical title: The Exact Value of GR(3, K5, 2)
- paper shape: A one-theorem generalized-Ramsey exact-value note, but with a wider residual interval than the preferred lane.
- publication if solved: An exact determination of GR(3, K5, 2) could still support a short note, but the wider current gap makes the solve-to-paper fraction less clearly inside the strict micro-paper lane.
- minimal artifact requirements: Either a proof that every 3-coloring of K20 forces a 2-colored K5, or explicit extremal colorings at the boundary orders together with verification.

## hypothetical_abstract
We determine the generalized Ramsey number GR(3, K5, 2), the minimum N such that every 3-edge-coloring of KN contains a copy of K5 using at most two colors. Existing public sources leave the value in the interval 20 <= GR(3, K5, 2) <= 23. Our result closes one of the first unresolved exact parameters in the newly initiated finite generalized-Ramsey table.

## single_solve_explanation
If solved exactly, this statement would still be the honest main theorem of a short note. The reason it falls outside the strict lane is not lack of publishability but the wider remaining interval and the resulting higher proof-management risk before curation. It is therefore a credible reserve-quality candidate but not a preferred live target.

## broader_theorem_nonimplication
The 2025 paper provides an explicit 19-vertex witness and a 23-vertex upper bound, but no broader theorem located in the bounded audit implies the exact value. The issue is not immediate rediscovery, but the wider gap and potentially less compact decisive certificate.

## literature_gap
Current public sources support only 20 <= GR(3, K5, 2) <= 23, and the bounded 2026-04-14 exact-term and alternate-notation audit did not uncover a later exact determination.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe 2025, Table 1, gives 20 <= GR(3, K5, 2) <= 23.
- lemma: The same paper exhibits a concrete 19-vertex lower-bound coloring built from three circulant graphs.
- lemma: Their generalized-Ramsey scoring framework reduces the search to K5 counting in unions of two color classes.
- toy example: The paper's explicit 19-vertex coloring with three isomorphic circulant color classes is the smallest worked example directly under the target threshold.
- known obstruction: A decisive proof must control K5 formation across all three unions of two color classes, which is a broader certificate-management task than in the best one-gap candidates.
- prior-work stop sentence: Current sources stop at the interval 20 <= GR(3, K5, 2) <= 23.
- recommended first attack: Exploit the explicit 19-vertex circulant witness and test extension rigidity under the paper's two-color-class reduction before allowing any larger computational census.
- paper if solved: The paper would be a short exact-value note on an early small generalized Ramsey parameter, but it is less cleanly one-shot than the preferred queue leaders.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels and generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1 and generalized-Ramsey method discussion; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Table 1 and generalized-Ramsey method discussion, plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches on 2026-04-14.
- artifacts/gr-3-k5-2-generalized-ramsey/record.md
- artifacts/gr-3-k5-2-generalized-ramsey/status.json
