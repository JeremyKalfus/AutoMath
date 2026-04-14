# Working Packet: The Exact Value of R(K3, K4-e, K4-e)

- slug: `k3-k4minus-k4minus-three-color-ramsey`
- title: Determine the exact value of R(K3, K4-e, K4-e)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `79`
- single-solve-to-paper fraction: `0.78`

## statement
Either prove that every 3-edge-coloring of K21 contains a first-color triangle or a second- or third-color copy of K4-e and thus show R(K3, K4-e, K4-e) = 21, or construct a 3-edge-coloring of K21 avoiding those targets and thus show R(K3, K4-e, K4-e) = 22.

## novelty_notes
- frontier basis: DS1.17 lists the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22. The 2012 small-graph paper develops the K4-e / J4 three-color landscape and shows that the nearby variant with K3+e in place of K3 is equivalent to this same target, which reinforces that the exact unresolved slice is canonical rather than ad hoc.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: This is already a named survey-line residue with a tiny exact gap and cheap literature audit because both K4-e and J4 notations are standard. After a solve, the remaining paper work would mostly be a compact proof narrative, perhaps a short extremal-coloring census, and a discussion of how the K3+e equivalence fits around the exact value.
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
- assessment: Pass. This is a stable one-gap small-graph Ramsey residue with strong family anchor, low novelty-check cost, and minimal editorial overhead after a solve.

## likely_paper_shape
- note title: The Exact Value of R(K3, K4-e, K4-e)
- hypothetical title: The Exact Value of R(K3, K4-e, K4-e)
- paper shape: A one-theorem exact-value note on the smallest unresolved K3/J4/J4-type three-color case.
- publication if solved: Closing R(K3, K4-e, K4-e) would already support a standalone short note on small three-color Ramsey numbers for nearly complete four-vertex graphs.
- minimal artifact requirements: Either a complete 3-color forcing proof on 21 vertices or one explicit 21-vertex extremal coloring avoiding a red K3 and blue/green K4-e.

## hypothetical_abstract
We determine the three-color Ramsey number R(K3, K4-e, K4-e). Existing work leaves this case in the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22, equivalently 21 <= R(3, J4, J4) <= 22 in J4 notation. Our result closes a natural small-graph residue in the K3-versus-nearly-complete-four-vertex family.

## single_solve_explanation
The exact value would already be the title theorem of the note, and the family context is standard enough that the paper would not need a long setup. Most of the eventual note would simply be the proof or extremal coloring plus a short comparison with the neighboring 2012 exact results. That keeps the solve-to-paper fraction inside the desired micro-paper band.

## broader_theorem_nonimplication
Known general relations among these small-graph Ramsey numbers do not force the exact value of R(K3, K4-e, K4-e); they only tie it to nearby variants such as the K3+e formulation. A proof might reveal a cleaner structural lemma, but it would still honestly be closing this exact one-gap J4/J4 survey entry rather than extracting a trivial corollary from an existing theorem.

## literature_gap
Current public sources support only the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22, and the bounded 2026-04-13 audit did not uncover a later exact determination under either K4-e or J4 notation.

## transfer_kit
- lemma: DS1.17 Section 6.5(c) records the current bounds 21 <= R(K3, K4-e, K4-e) <= 22.
- lemma: The 2012 small-graph paper proves that R(K3+e, K4-e, K4-e) = R(K3, K4-e, K4-e), providing an alternate-notation and nearby-variant transfer lemma.
- lemma: The same paper establishes exact adjacent cases such as R(C4, K4-e, K4-e) = 19 and R(K3, K4-e, K4) upper bounds, which help localize the small-graph landscape around the target.
- toy example: The identity R(K3+e, K4-e, K4-e) = R(K3, K4-e, K4-e) is the smallest nearby worked example showing that tiny perturbations of the first forbidden graph need not change the exact value.
- known obstruction: Any proof of 21 must eliminate every 21-vertex critical coloring consistent with the survey lower bound, while a proof of 22 requires one explicit 21-vertex coloring with no red triangle and no blue or green K4-e.
- prior-work stop sentence: Current sources stop at the one-gap window 21 <= R(K3, K4-e, K4-e) <= 22.
- recommended first attack: Work in J4 notation and combine bounded critical-coloring generation with neighborhood splitting around a putative red-triangle-free color class, using the 2012 transfer lemmas to prune isomorphic K3+e variants.
- paper if solved: The paper would be a short exact-value note closing a canonical J4/J4 three-color Ramsey residue.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 6.5(c); Luis Boza, Janusz Dybizbański, and Tomasz Dzido, "Three color Ramsey numbers for graphs with at most 4 vertices" (Electronic Journal of Combinatorics 19(4), 2012), together with its K3+e equivalence discussion; and bounded exact-term, alternate-notation, canonical-source, source-internal, outside-source, and recent-status web checks performed on 2026-04-13.
- DS1.17 Section 6.5(c), Dybizbański-Dzido-Boza 2012, and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, outside-source, and recent-status searches for R(K3, K4-e, K4-e) and R(3, J4, J4).
- artifacts/k3-k4minus-k4minus-three-color-ramsey/record.md
- artifacts/k3-k4minus-k4minus-three-color-ramsey/status.json
