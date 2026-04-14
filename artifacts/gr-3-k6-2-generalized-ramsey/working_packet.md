# Working Packet: The Exact Value of GR(3, K6, 2)

- slug: `gr-3-k6-2-generalized-ramsey`
- title: Determine the exact value of GR(3, K6, 2)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `34`
- single-solve-to-paper fraction: `0.38`

## statement
Determine the least n such that every 3-edge-coloring of Kn contains a K6 using at most two colors, equivalently improve the current window 32 <= GR(3, K6, 2) <= 54 to an exact value.

## novelty_notes
- frontier basis: The 2025 paper records the first known bounds 32 <= GR(3, K6, 2) <= 54 in the newly introduced generalized small Ramsey family. The bounded 2026-04-13 exact-term and recent-status audit did not surface a later exact determination.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: This packet is not near-paper by current standards. Even if a solve arrived, too much of the final paper would still be devoted to heavy case closure, computational certification, and broader framing.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: weak
- family anchor strength: moderate
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: moderate
- isolated exact-case risk: high
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: broad
- assessment: Fail. This is a legitimate frontier problem, but it is much too broad, computation-heavy, and publication-distant for the strict one-shot micro-paper lane.

## likely_paper_shape
- note title: The Exact Value of GR(3, K6, 2)
- hypothetical title: The Exact Value of GR(3, K6, 2)
- paper shape: A broader exact-value paper in generalized Ramsey theory rather than a micro-note.
- publication if solved: An exact value would certainly be mathematically interesting, but this is not a micro-paper target under the current lane.
- minimal artifact requirements: A major exact proof closing the current 23-point window, likely together with substantial computational certification and extremal-coloring analysis.

## hypothetical_abstract
We determine the generalized Ramsey number GR(3, K6, 2), the least n such that every 3-coloring of Kn contains a K6 spanning at most two colors. Existing work gives only the broad interval 32 <= GR(3, K6, 2) <= 54. Our result would close the first exact K6 case in the generalized small Ramsey setting.

## single_solve_explanation
Even an exact solution here would not satisfy the desired 70-90 percent paper test. The current gap is too broad, the likely proof burden is heavy, and a large amount of supporting computation or structure would still need to be explained before the result became a clean short note. This is precisely the kind of target the micro-paper lane should downrank.

## broader_theorem_nonimplication
There is no known broad exact theorem in the new generalized Ramsey family that already settles the K6 case, but the problem remains too broad and certificate-heavy to be a disciplined micro-paper target.

## literature_gap
Current sources leave GR(3, K6, 2) unresolved in the interval 32 <= GR(3, K6, 2) <= 54, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: Lidický-McKinley-Pfender-Van Overberghe 2025 proves the lower bound GR(3, K6, 2) >= 32.
- lemma: The same paper proves the upper bound GR(3, K6, 2) <= 54.
- lemma: The same source solves smaller nearby generalized Ramsey cases including GR(3, K4, 2) = 10 and GR(4, K4, 3) = 10.
- toy example: The family already has exact low-order anchors such as GR(3, K4, 2) = 10, highlighting how far the K6 case still is from closure.
- known obstruction: The gap is wide enough that any exact attack is likely to require substantial computation or new structural theory rather than a compact single-certificate argument.
- prior-work stop sentence: Current sources stop at the interval 32 <= GR(3, K6, 2) <= 54.
- recommended first attack: Treat the published lower-bound coloring as a seed and first aim to compress the upper bound dramatically before considering any exact search.
- paper if solved: The paper would be a broader exact-value contribution in generalized Ramsey theory, not a micro-note.

## bounded_source_list
- Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1, together with bounded exact-term, alternate-notation, canonical-source, and recent-status web checks performed on 2026-04-13.
- Lidický-McKinley-Pfender-Van Overberghe 2025 Table 1 and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, and recent-status searches for GR(3, K6, 2).
- artifacts/gr-3-k6-2-generalized-ramsey/record.md
- artifacts/gr-3-k6-2-generalized-ramsey/status.json
