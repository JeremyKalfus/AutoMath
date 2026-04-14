# Working Packet: The Exact Value of GR(3, K5, 2)

- slug: `gr3-k5-at-most-two-colors`
- title: Determine the exact value of GR(3, K5, 2)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `62`
- single-solve-to-paper fraction: `0.61`

## statement
Determine the least n such that every 3-edge-coloring of K_n contains a copy of K5 using at most 2 colors.

## novelty_notes
- frontier basis: Current public sources support only 20 <= GR(3, K5, 2) <= 23.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved, the theorem would still head a real note in the same newly named family. The target misses the strict lane because the current interval remains a bit too wide and the likely proof would still lean on extensive search or symmetry-breaking.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: small
- assessment: Usable as a backup paper candidate but outside the strict lane. The family is legitimate, yet the remaining search residue is still larger than desired.

## likely_paper_shape
- note title: The Exact Value of GR(3, K5, 2)
- hypothetical title: The Exact Value of GR(3, K5, 2)
- paper shape: A computational exact-value note in the generalized small Ramsey family.
- publication if solved: An exact determination of GR(3, K5, 2) would still support a short note, but too much of the current residue still sits inside the search.
- minimal artifact requirements: Either an explicit extremal 3-coloring near the lower endpoint or a complete upper-bound exclusion proof with a machine-checkable certificate.

## hypothetical_abstract
We determine GR(3, K5, 2), the least n such that every 3-edge-coloring of K_n contains a K5 using at most two colors. The recent literature leaves this parameter between 20 and 23. Our result closes one of the first unresolved cases in the small generalized Ramsey program.

## single_solve_explanation
A sharp solve would still produce the note's title theorem, and the family context is already available from the 2025 source. However, the current range is still wide enough that the solve would likely require a substantial computational packet. That lowers the single-solve-to-paper fraction below the strict micro-paper target.

## broader_theorem_nonimplication
The 2025 source only provides the 20-23 corridor and nearby exact benchmarks for smaller tuples. No checked general theorem forces the K5 case from the exact K4 cases.

## literature_gap
Publicly checked sources stop at 20 <= GR(3, K5, 2) <= 23.

## transfer_kit
- lemma: Table 1 of the 2025 paper gives 20 <= GR(3, K5, 2) <= 23.
- lemma: The same source proves the exact benchmark GR(3, K4, 2) = 10.
- lemma: Section 3 describes the bottom-up, flag-algebra, and local-search toolkit used for nearby generalized cases.
- toy example: The exact lower-dimensional benchmark GR(3, K4, 2) = 10 gives the intended style for a finished generalized Ramsey note.
- known obstruction: The search space for 3-colorings of K_n with no two-colored K5 grows quickly, and symmetry can hide many near-extremal colorings.
- prior-work stop sentence: Current checked sources stop at 20 <= GR(3, K5, 2) <= 23.
- recommended first attack: Exploit the exact K4 case as a local forbidden-pattern subroutine and search for high-symmetry 3-colorings near n = 20, 21, and 22.
- paper if solved: The paper would be an exact-value note in the small generalized Ramsey family.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1 and Section 3, which give 20 <= GR(3, K5, 2) <= 23; together with the 2024 arXiv preprint version and the authors' project page, plus bounded exact-statement and recent-status web checks on 2026-04-14 that did not reveal a later exact determination.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Table 1 and Section 3, the 2024 preprint version, the project page, and bounded 2026-04-14 exact-term and recent-status web checks.
- artifacts/gr3-k5-at-most-two-colors/record.md
- artifacts/gr3-k5-at-most-two-colors/status.json
