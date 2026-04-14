# Working Packet: The Exact Value of R(K2,2,2, K2,2,2)

- slug: `r-k222-k222-octahedral-ramsey`
- title: Determine the exact value of R(K2,2,2, K2,2,2)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `58`
- single-solve-to-paper fraction: `0.63`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of K2,2,2 in one of the two colors.

## novelty_notes
- frontier basis: The 2021 SDP paper leaves the diagonal K2,2,2 Ramsey number at 30 <= R(K2,2,2, K2,2,2) <= 31. The gap is one step, but the narrative leverage is weaker than for the clique and almost-clique families.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved, most of the technical content of the paper would indeed be finished. The problem is not closability but story strength: the exact closure risks reading like a narrow census result unless the proof has a particularly clean extremal interpretation.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: weak
- editorial overhead: moderate
- immediate corollary headroom: none
- isolated exact-case risk: high
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Fail for the strict micro-paper lane. The one-step gap is attractive, but the family anchor and publication narrative are not strong enough to beat the top four candidates.

## likely_paper_shape
- note title: The Exact Value of R(K2,2,2, K2,2,2)
- hypothetical title: The Exact Value of R(K2,2,2, K2,2,2)
- paper shape: A narrow exact-value note, but with noticeably weaker story leverage than the top candidates.
- publication if solved: An exact determination would likely be publishable as a short computational or extremal note, but the narrative is less compelling than the top queue entries.
- minimal artifact requirements: Either an explicit 30-vertex coloring avoiding monochromatic K2,2,2 in both colors or a forcing proof at 31 with a short certificate.

## hypothetical_abstract
We determine the diagonal Ramsey number R(K2,2,2, K2,2,2). Current public sources leave this value at 30 <= R(K2,2,2, K2,2,2) <= 31 after the 2021 semidefinite-programming upper-bound improvement. Our result closes the remaining one-step gap for the octahedral graph family.

## single_solve_explanation
A solve would certainly provide the main theorem of a short note. However, compared with the stronger queue entries, more of the eventual paper value would have to come from a particularly elegant construction, uniqueness statement, or structural interpretation. Without that extra feature, the paper risks feeling like a narrow exact table entry.

## broader_theorem_nonimplication
No general theorem located in the bounded audit forces the 30 versus 31 endpoint automatically, but neither did the audit uncover especially strong surrounding narrative that would upgrade the result beyond a specialized exact case.

## literature_gap
Current public sources stop at 30 <= R(K2,2,2, K2,2,2) <= 31.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 7, gives the upper bound R(K2,2,2, K2,2,2) <= 31.
- lemma: The same theorem table records the known lower bound R(K2,2,2, K2,2,2) >= 30.
- lemma: The SDP method in the 2021 paper is explicitly designed to rule out small counterexamples by local density constraints.
- lemma: Diagonal symmetry means any exact proof can focus on a single family of critical colorings up to color reversal.
- toy example: The current lower-bound side already guarantees a 30-vertex coloring with no monochromatic K2,2,2.
- known obstruction: Even with a one-step interval, the likely proof may be highly computational, which raises the risk of a weak paper narrative despite exact closure.
- prior-work stop sentence: Current sources stop at 30 <= R(K2,2,2, K2,2,2) <= 31.
- recommended first attack: Look first for a uniqueness or strong structural classification of 30-vertex critical colorings; without that, the endpoint alone may not carry the paper.
- paper if solved: The paper would be a short exact-value note on the diagonal octahedral Ramsey number, ideally with a structural characterization of the extremal coloring.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 7, which gives 30 <= R(K2,2,2, K2,2,2) <= 31; together with bounded 2026-04-14 exact-notation and recent-status web checks that did not reveal a later exact closure.
- 2021 Lidicky-Pfender theorem table plus bounded 2026-04-14 exact-notation and recent-status web checks.
- artifacts/r-k222-k222-octahedral-ramsey/record.md
- artifacts/r-k222-k222-octahedral-ramsey/status.json
