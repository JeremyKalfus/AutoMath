# Working Packet: The Exact Value of R(C4, K3, K4)

- slug: `c4-k3-k4-three-color-ramsey`
- title: Determine the exact value of R(C4, K3, K4)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `66`
- single-solve-to-paper fraction: `0.67`

## statement
Determine the least n such that every 3-edge-coloring of Kn contains a first-color C4, a second-color K3, or a third-color K4, equivalently close the current window 27 <= R(C4, K3, K4) <= 29.

## novelty_notes
- frontier basis: DS1.17 lists 27 <= R(C4, K3, K4) <= 29. The 2025 C4 upper-bound paper still cites 29 as the active upper bound while improving several neighboring C4/clique cases, so the exact value remains open in the recent literature sampled during the bounded audit.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A solve would still close a named survey-line problem in an active C4-versus-clique vein. But because the gap has width two and the family contains many nearby small cases, the note would likely need more comparative discussion and perhaps a larger extremal-coloring appendix than the strict micro-paper lane should prefer.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail for the strict lane. The family anchor is real and the exact question is publishable if solved, but the solve-to-paper distance is longer than for the one-gap candidates.

## likely_paper_shape
- note title: The Exact Value of R(C4, K3, K4)
- hypothetical title: The Exact Value of R(C4, K3, K4)
- paper shape: A short exact-value note on a small three-color C4/clique Ramsey number.
- publication if solved: An exact value would still make a plausible short note in the C4-versus-clique program, but it is not as close to a finished micro-paper as the one-gap residues.
- minimal artifact requirements: Either a forcing proof on 27 or 28 vertices, or one explicit extremal coloring on 27 or 28 vertices depending on the exact value.

## hypothetical_abstract
We determine the three-color Ramsey number R(C4, K3, K4). Existing work leaves this C4-versus-clique case in the range 27 <= R(C4, K3, K4) <= 29, with the recent literature still using 29 as the best known upper bound. Our result sharpens the exact landscape for small multicolor Ramsey numbers involving quadrilaterals and cliques.

## single_solve_explanation
If solved, the theorem would indeed be the title theorem of a reasonable short paper. However, the surviving gap is wider than ideal and the surrounding note would probably need more critical-coloring discussion than the best queue entries. That pushes the paper fraction slightly below the strict micro-paper target.

## broader_theorem_nonimplication
The available C4 upper-bound machinery improves concrete cases but does not force the exact value of R(C4, K3, K4). A successful proof could illuminate a wider pattern, yet at present there is no known broader theorem making this a trivial corollary.

## literature_gap
Current public sources leave R(C4, K3, K4) unresolved in the range 27 <= R(C4, K3, K4) <= 29, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: DS1.17 Section 6.3.3(a) records 27 <= R(C4, K3, K4) <= 29.
- lemma: The 2025 C4 upper-bound paper explicitly lists R(C4, K3, K4) <= 29 as a concrete improved input.
- lemma: The same 2025 paper also records R(C4, K4, K4) <= 66 and uses recursive upper-bound constructions that can be specialized back to the K3/K4 case.
- toy example: The exact value R(C4, K3, K4-e) = 17 from the 2012 small-graph paper is the smallest nearby worked example with the same C4-plus-clique architecture.
- known obstruction: Any exact determination must control 27- and 28-vertex extremal colorings where one color is triangle-free and another avoids K4, which is a denser search space than the one-gap entries.
- prior-work stop sentence: Current sources stop at the interval 27 <= R(C4, K3, K4) <= 29.
- recommended first attack: Use the 2025 recursive C4 upper-bound framework together with a bounded enumeration of triangle-free second-color classes on 28 vertices to see whether the 29 upper bound can be pushed down by one or two.
- paper if solved: The paper would be a short exact-value note in the C4-versus-clique three-color line.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 6.3.3(a); Luis Boza and Stanisław P. Radziszowski, "Some upper bounds on Ramsey numbers involving C4" (Discussiones Mathematicae Graph Theory 45, 2025), which gives R(C4, K3, K4) <= 29; and bounded exact-term, alternate-notation, canonical-source, source-internal, outside-source, and recent-status web checks performed on 2026-04-13.
- DS1.17 Section 6.3.3(a), Boza-Radziszowski 2025, and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, outside-source, and recent-status searches for R(C4, K3, K4).
- artifacts/c4-k3-k4-three-color-ramsey/record.md
- artifacts/c4-k3-k4-three-color-ramsey/status.json
