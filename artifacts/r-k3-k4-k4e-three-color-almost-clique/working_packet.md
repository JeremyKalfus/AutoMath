# Working Packet: The Exact Value of R(K3, K4, K4-e)

- slug: `r-k3-k4-k4e-three-color-almost-clique`
- title: Determine the exact value of R(K3, K4, K4-e)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `60`
- single-solve-to-paper fraction: `0.63`

## statement
Determine the least n such that every 3-coloring of K_n contains a red K3, a blue K4, or a green K4-e.

## novelty_notes
- frontier basis: Current public sources still leave this mixed three-color almost-clique number unresolved in a comparatively wide interval. It is a real frontier slice, but less compressed than the better queue entries.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved exactly, the result would still be the main theorem. However, the proof burden and certificate size are likely to dominate more of the final note than is ideal for the strict micro-paper lane.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: moderate
- assessment: Fail for the strict lane. The theorem slice is stable, but the gap is wide enough that one solve would probably leave too much proof and packaging work.

## likely_paper_shape
- note title: The Exact Value of R(K3, K4, K4-e)
- hypothetical title: The Exact Value of R(K3, K4, K4-e)
- paper shape: A possible one-theorem multicolor note, but with enough residue that it misses the strict lane.
- publication if solved: An exact value here could still support a note, but the gap width and likely computational residue make it a weaker strict micro-paper target.
- minimal artifact requirements: Either a complete forcing proof or an explicit extremal 3-coloring with a nontrivial verification appendix.

## hypothetical_abstract
We determine the 3-color Ramsey number R(K3, K4, K4-e). Existing public sources leave this mixed clique and almost-clique parameter in the interval 31 <= R(K3, K4, K4-e) <= 40. Our result closes an unresolved small multicolor entry involving the first noncomplete four-vertex graph.

## single_solve_explanation
The exact value would still be a legitimate title theorem, but the solve-to-paper fraction is below the preferred band. Compared with the stronger queue entries, this target likely needs more computational verification and more exposition after the solve.

## broader_theorem_nonimplication
Known exact results for nearby small K4-e multicolor cases do not force this mixed K3/K4/K4-e parameter. The issue is not hidden implication but the wider interval and heavier likely residue.

## literature_gap
Current public sources stop at 31 <= R(K3, K4, K4-e) <= 40.

## transfer_kit
- lemma: DS1.17 Section 6.5 records 31 <= R(K3, K4, K4-e) <= 40.
- lemma: The same section records the tighter nearby case 21 <= R(K3, K4-e, K4-e) <= 22.
- lemma: Color symmetry between the last two colors reduces some case distinctions when constructing or ruling out extremal colorings.
- toy example: The exact smaller multicolor benchmark R(P3, K4-e, K4-e) = 11 illustrates the same almost-clique color role in a simpler setting.
- known obstruction: Any witness must simultaneously block a monochromatic triangle, a monochromatic K4, and a monochromatic K4-e across three colors, which tends to produce bulky verification artifacts.
- prior-work stop sentence: Current sources stop at 31 <= R(K3, K4, K4-e) <= 40.
- recommended first attack: Exploit color symmetry and the tighter K3/K4-e/K4-e companion case before attempting any broad computational exploration.
- paper if solved: The paper would be a small multicolor Ramsey note, but it is not the cleanest strict micro-paper option available.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 6.5, which records 31 <= R(K3, K4, K4-e) <= 40; together with bounded 2026-04-14 survey/web checks that did not reveal a later exact closure.
- DS1.17 Section 6.5 and bounded 2026-04-14 survey/web checks.
- artifacts/r-k3-k4-k4e-three-color-almost-clique/record.md
- artifacts/r-k3-k4-k4e-three-color-almost-clique/status.json
