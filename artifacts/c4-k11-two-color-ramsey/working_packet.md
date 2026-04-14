# Working Packet: The Exact Value of R(C4, K11)

- slug: `c4-k11-two-color-ramsey`
- title: Determine the exact value of R(C4, K11)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `61`
- single-solve-to-paper fraction: `0.58`

## statement
Determine the least n such that every graph on n vertices contains either a C4 or an independent set of size 11, equivalently close the current window 40 <= R(C4, K11) <= 43.

## novelty_notes
- frontier basis: The 2022 computation paper sharpened classical R(C4, Kn) bounds and the 2025 C4 upper-bound paper further improved specific concrete upper bounds, including R(C4, K11) <= 43. The bounded 2026-04-13 audit did not surface a later exact determination beyond the current window 40 <= R(C4, K11) <= 43.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: This is unquestionably a real paper target because R(C4, Kn) is a classical line with strong citation gravity. But it fails the strict micro-paper lane: any solution is likely to need a larger computational packet, more verification overhead, and less compact exposition than the queue leaders.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: small
- assessment: Fail for the strict lane. The family anchor is excellent, but the target is too search-heavy and too certificate-large relative to the desired one-shot publication profile.

## likely_paper_shape
- note title: The Exact Value of R(C4, K11)
- hypothetical title: The Exact Value of R(C4, K11)
- paper shape: A computational exact-value note on a classical C4-versus-clique Ramsey number.
- publication if solved: An exact value of R(C4, K11) would clearly be publishable, but the residue is too search-heavy and too far from a finished micro-paper packet for this lane.
- minimal artifact requirements: Either a full computational proof closing the 40-43 window or one new lower-bound witness together with improved upper-bound exclusion.

## hypothetical_abstract
We determine the classical Ramsey number R(C4, K11). Existing work leaves this case in the range 40 <= R(C4, K11) <= 43 after recent improvements in the C4-versus-clique line. Our result sharpens one more exact entry in a longstanding classical family.

## single_solve_explanation
A solve would definitely yield a legitimate paper, but it would not be 70-90% of the final packet in the sense required by the lane. The likely need for larger computation, critical-graph verification, and a more substantial appendix keeps the editorial load noticeably higher than for the queue leaders.

## broader_theorem_nonimplication
The current C4-versus-clique theory gives asymptotic behavior and concrete computational bounds, not an exact formula forcing the n = 11 case. The target is stable, but its shortest plausible route is still computationally heavier than the micro-paper lane should prioritize.

## literature_gap
Current public sources leave R(C4, K11) unresolved in the range 40 <= R(C4, K11) <= 43, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: The 2022 computation paper advances the exact classical R(C4, Kn) line and provides the immediate pre-2025 context for n = 11.
- lemma: The 2025 C4 upper-bound paper reports the improved concrete bound R(C4, K11) <= 43.
- lemma: DS1.17 records the best currently known lower/upper data for cycle-versus-complete-graph numbers and places R(C4, K11) inside the current unresolved table.
- toy example: The smaller exact values and tight cases in the computed R(C4, Kn) table provide the worked comparison showing how extremal C4-free graphs control the exact threshold.
- known obstruction: Any exact closure must manage a large search space of C4-free graphs near the extremal density threshold, and certificates are unlikely to stay compact.
- prior-work stop sentence: Current sources stop at the range 40 <= R(C4, K11) <= 43.
- recommended first attack: Start from the 2022 computational framework for C4-free graphs and test whether the 2025 upper-bound improvements can be paired with a bounded critical-graph census at orders 40, 41, and 42.
- paper if solved: The paper would be a computational exact-value note in the classical R(C4, Kn) family.

## bounded_source_list
- Stanislav Dudek and Vojtěch Rödl, "On K_s-free subgraphs in K_s+k-free graphs and vertex Folkman numbers" (Combinatorica 31, 2011) for the classical lower-bound context; Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), cycle-versus-complete-graph section; Jan Goedgebeur, Jan Van Ceulebroeck, and Stanisław P. Radziszowski, "A Computation of Classical Ramsey Numbers of the Form R(C4, Kn)" (Journal of Graph Theory 101, 2022); Luis Boza and Stanisław P. Radziszowski, "Some upper bounds on Ramsey numbers involving C4" (Discussiones Mathematicae Graph Theory 45, 2025); and bounded exact-term, alternate-notation, canonical-source, source-internal, outside-source, and recent-status web checks performed on 2026-04-13.
- Dudek-Rödl 2011, DS1.17 cycle-versus-complete-graph section, Goedgebeur-Van Ceulebroeck-Radziszowski 2022, Boza-Radziszowski 2025, and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, outside-source, and recent-status searches for R(C4, K11).
- artifacts/c4-k11-two-color-ramsey/record.md
- artifacts/c4-k11-two-color-ramsey/status.json
