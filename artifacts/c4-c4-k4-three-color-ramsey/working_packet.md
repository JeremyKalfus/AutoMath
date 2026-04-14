# Working Packet: The Exact Value of R(C4, C4, K4)

- slug: `c4-c4-k4-three-color-ramsey`
- title: Determine the exact value of R(C4, C4, K4)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `83`
- single-solve-to-paper fraction: `0.81`

## statement
Either prove that every 3-edge-coloring of K20 contains a first-color C4, a second-color C4, or a third-color K4 and thus show R(C4, C4, K4) = 20, or construct a 3-edge-coloring of K20 avoiding those targets and thus show R(C4, C4, K4) = 21.

## novelty_notes
- frontier basis: DS1.17 records the current one-gap window 20 <= R(C4, C4, K4) <= 21. The 2012 small-graph paper organized the surrounding C4/K4-e/K4 landscape, and the 2025 C4 upper-bound paper still relies on R(C4, C4, K4) <= 21 as input for its later multicolor bounds, indicating the exact case remains open.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The problem already has a mature literature shell: the exact statement is canonical, the gap is one, and the surrounding family is active enough that a closure immediately improves a reusable benchmark. After a solve, the note would mainly need the extremal coloring or forcing argument, a short comparison with adjacent C4/K4 cases, and perhaps a compact critical-graph discussion.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Pass. This is a stable one-gap multicolor Ramsey residue with a named family anchor, low novelty-check cost, and a clear short-note paper packet if solved.

## likely_paper_shape
- note title: The Exact Value of R(C4, C4, K4)
- hypothetical title: The Exact Value of R(C4, C4, K4)
- paper shape: A one-theorem exact-value note closing the smallest remaining one-gap C4/C4/K4 three-color case.
- publication if solved: Closing the one-gap case R(C4, C4, K4) would already read as the title theorem of a genuine short note on multicolor Ramsey numbers involving quadrilaterals.
- minimal artifact requirements: Either a complete 3-color forcing proof on 20 vertices or one explicit 20-vertex extremal coloring avoiding two quadrilateral colors and one K4 color.

## hypothetical_abstract
We determine the three-color Ramsey number R(C4, C4, K4). Existing work leaves this multicolor quadrilateral case in the one-gap window 20 <= R(C4, C4, K4) <= 21. Our result closes a natural benchmark problem in the C4-versus-clique line and sharpens an input that is reused in later upper-bound arguments.

## single_solve_explanation
The exact value is already the honest title theorem. The surrounding literature has already done most of the framing work, so a successful solve would leave only a short exposition of the extremal coloring or forcing mechanism and a comparison with nearby C4/K4 cases. That is close to the ideal 70-90% micro-paper profile.

## broader_theorem_nonimplication
No known general theorem already collapses this to a broader formula: the available C4 multicolor results give asymptotics or concrete upper-bound machinery, but not an exact evaluation of the small triple (C4, C4, K4). A shortest proof might illuminate a wider pattern, yet the honest frontier claim would still remain this exact one-gap case.

## literature_gap
Current public sources support only the one-gap window 20 <= R(C4, C4, K4) <= 21, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: DS1.17 Section 6.3.3(a) records the current bounds 20 <= R(C4, C4, K4) <= 21.
- lemma: The 2025 C4 upper-bound paper explicitly uses R(C4, C4, K4) <= 21 as known input in Case #6, so the upper bound is still current in the post-DS1 literature.
- lemma: The 2012 three-color small-graph paper proves exact neighboring values such as R(C4, C4, K4-e) = 16 and develops transfer lemmas among K4-e and K3+e variants around this triple.
- toy example: The exact value R(C4, C4, K4-e) = 16 is the smallest nearby worked case showing how two quadrilateral colors interact with a nearly-complete clique color.
- known obstruction: Any proof of 20 must rule out every 20-vertex critical coloring compatible with the known one-gap window, while a proof of 21 needs a single explicit 20-vertex 3-coloring with no first-color C4, no second-color C4, and no third-color K4.
- prior-work stop sentence: Current sources stop at the one-gap window 20 <= R(C4, C4, K4) <= 21.
- recommended first attack: Start from the known 20-vertex lower-bound colorings implicit in the survey line and try a bounded critical-coloring census with symmetry reduction, using the exact 2025 upper-bound input structure to force C4 creation under any extension.
- paper if solved: The paper would be a short exact-value note closing the smallest surviving one-gap C4/C4/K4 benchmark.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 6.3.3(a); Janusz Dybizbański, Tomasz Dzido, and Luis Boza, "Three color Ramsey numbers for graphs with at most 4 vertices" (Electronic Journal of Combinatorics 19(4), 2012), especially the C4/K4-e/K4 section; Luis Boza and Stanisław P. Radziszowski, "Some upper bounds on Ramsey numbers involving C4" (Discussiones Mathematicae Graph Theory 45, 2025), Case #6; and bounded exact-term, alternate-notation, canonical-source, source-internal, outside-source, and recent-status web checks performed on 2026-04-13.
- DS1.17 Section 6.3.3(a), Dybizbański-Dzido-Boza 2012, Boza-Radziszowski 2025, and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, outside-source, and recent-status searches for R(C4, C4, K4).
- artifacts/c4-c4-k4-three-color-ramsey/record.md
- artifacts/c4-c4-k4-three-color-ramsey/status.json
