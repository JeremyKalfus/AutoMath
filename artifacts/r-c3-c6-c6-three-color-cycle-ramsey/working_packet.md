# Working Packet: The Exact Value of R(C3, C6, C6)

- slug: `r-c3-c6-c6-three-color-cycle-ramsey`
- title: Determine the exact value of R(C3, C6, C6)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `61`
- single-solve-to-paper fraction: `0.68`

## statement
Determine the least n such that every 3-coloring of E(K_n) contains either a color-1 triangle or a color-2 C6 or a color-3 C6.

## novelty_notes
- frontier basis: Current public sources leave this three-color cycle Ramsey number at 15 <= R(C3, C6, C6) <= 18. The family is classical, but the interval is wider than the surviving micro-paper slots above it.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: An exact solve would still matter, but the gap is wide enough that the eventual proof package could become more elaborate than a true one-shot micro-paper. That residual risk pushes it out of the strict lane.
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
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail for the strict lane. The target is classical and real, but the proof risk and remaining editorial residue are still too large relative to the best surviving slots.

## likely_paper_shape
- note title: The Exact Value of R(C3, C6, C6)
- hypothetical title: The Exact Value of R(C3, C6, C6)
- paper shape: A classical small-cycle exact-value note, but with too much residual proof risk for the strict lane.
- publication if solved: An exact determination would likely still be publishable as a short note, but the current gap is wide enough that one solve may not finish enough of the paper for the strict micro-paper lane.
- minimal artifact requirements: A compact extremal coloring or forcing proof that closes the 15-18 interval, ideally with a clear structural explanation.

## hypothetical_abstract
We determine the three-color Ramsey number R(C3, C6, C6). Previous work bounded this number between 15 and 18. Our result closes the remaining finite gap for this triangle-versus-even-cycle configuration.

## single_solve_explanation
This candidate fails the strict lane not because the result would be unpublishable, but because the remaining interval is still wide enough that a successful solve may require a longer and less self-contained proof package. That weakens the 70-90% paper fraction.

## broader_theorem_nonimplication
Known asymptotic and parity-based cycle theorems do not fix the exact endpoint here, but neither does the bounded audit suggest a uniquely sharp small-slice narrative after the solve.

## literature_gap
Current public sources stop at 15 <= R(C3, C6, C6) <= 18.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 8, gives the upper bound R(C3, C6, C6) <= 18.
- lemma: The same theorem records the lower bound 15 <= R(C3, C6, C6).
- lemma: The exact value R(C3, C5, C5) = 17 from the same paper gives a nearby solved comparison case.
- lemma: The Dynamic Survey supplies the standard surrounding cycle-Ramsey context.
- toy example: The exact neighboring case R(C3, C5, C5) = 17 is the closest solved model for this family.
- known obstruction: The triangle color can force dense local behavior that interacts awkwardly with the two even-cycle colors, making a short exact proof less likely than the interval size first suggests.
- prior-work stop sentence: Current sources stop at 15 <= R(C3, C6, C6) <= 18.
- recommended first attack: Start with the 2021 SDP local profiles and test whether the absence of a monochromatic C6 in two colors forces enough triangle density to collapse the interval.
- paper if solved: The paper would be a classical exact-value note on a small three-color cycle Ramsey number, but probably not as compact as the top queue entries.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 8, which gives 15 <= R(C3, C6, C6) <= 18; together with the 2024 revision of Radziszowski's Dynamic Survey "Small Ramsey Numbers" as family context and bounded 2026-04-14 recent-status web checks during curation that did not reveal a later exact closure.
- 2021 Lidicky-Pfender Theorem 8, Dynamic Survey family context, and bounded 2026-04-14 recent-status web checks.
- artifacts/r-c3-c6-c6-three-color-cycle-ramsey/record.md
- artifacts/r-c3-c6-c6-three-color-cycle-ramsey/status.json
