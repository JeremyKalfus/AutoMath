# Working Packet: The Exact Value of R(C10, C10, C10)

- slug: `r3-c10-even-cycle-ramsey`
- title: Determine the exact value of R(C10, C10, C10)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `85`
- single-solve-to-paper fraction: `0.82`

## statement
Either prove that every 3-coloring of K20 contains a monochromatic C10, or construct a 3-coloring of K20 with no monochromatic C10 and thus show R(C10, C10, C10) >= 21.

## novelty_notes
- frontier basis: The January 6, 2026 survey says R3(C2m) = 4m is known only for sufficiently large m and identifies C10 as the first open case; the Benevides-Skokan paper proves the large-even-cycle formula only beyond a threshold; bounded exact-statement, alternate-notation, and recent-status searches run on 2026-04-13 did not surface a later exact-resolution paper for C10.
- why still open: (not recorded)
- attempted conflict check: The refreshed 2026-04-13 exclusion sweep found no archived conflicting AutoMath mathematical status for the exact C10 diagonal even-cycle problem.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The conjectural target 20, the solved C8 benchmark, and the large-even-cycle framework are already in place. Once C10 is settled, the note mostly needs the sharp forcing proof or the critical coloring plus a short comparison to the established large-n theory.
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
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass. This is a first-open named residue in a flagship exact-value family, and one clean solve would already be the whole short paper.

## likely_paper_shape
- note title: The Exact Value of R(C10, C10, C10)
- hypothetical title: The Exact Value of R(C10, C10, C10)
- paper shape: A one-theorem exact-value note on the first open diagonal three-color even-cycle Ramsey number.
- publication if solved: Settling the first open three-color even-cycle diagonal case would already supply the title theorem of a short cycle-Ramsey note.
- minimal artifact requirements: Either a proof that every 3-coloring of K20 contains a monochromatic C10, or one explicit 20-vertex coloring with no monochromatic C10.

## hypothetical_abstract
We determine the exact three-color Ramsey number R(C10, C10, C10). The current Ramsey survey states that the formula R(C2m, C2m, C2m) = 4m is known only for sufficiently large m and identifies C10 as the first open diagonal even-cycle case. Our theorem closes the smallest remaining bounded even-cycle residue in the three-color diagonal family.

## single_solve_explanation
If the exact C10 value is determined, the theorem is already the note's title result. The family conjecture, the large-n exact theorem, and the solved C8 benchmark already provide the narrative scaffolding. What remains after the solve is mainly exposition, a compact extremal discussion, and documentation of the critical coloring pattern.

## broader_theorem_nonimplication
Benevides and Skokan prove the diagonal even-cycle formula only for sufficiently large even n, so the bounded C10 instance is not already covered by the published large-n theorem.

## literature_gap
The January 6, 2026 Ramsey survey identifies C10 as the first open diagonal three-color even-cycle case and records only the lower bound 20.

## transfer_kit
- lemma: DS1.18 records the general lower bound R3(C2m) >= 4m for all m >= 2 and says C10 is the first open diagonal even-cycle case.
- lemma: The survey records the exact benchmark R(C8, C8, C8) = 16.
- lemma: Benevides and Skokan prove that R(Cn, Cn, Cn) = 2n for all sufficiently large even n, supplying the large-scale stability model but not the bounded C10 case.
- toy example: The nearest solved diagonal even-cycle benchmark is R(C8, C8, C8) = 16, while the conjectural C10 target is 20.
- known obstruction: Any upper-bound proof must eliminate 19-vertex extremal three-color templates based on even-cycle blowups, while a disproof must produce one explicit 20-vertex coloring with no monochromatic C10.
- prior-work stop sentence: The January 6, 2026 Ramsey survey identifies C10 as the first open diagonal three-color even-cycle case.
- recommended first attack: Start from the standard 19-vertex lower-bound construction and prove a 20-vertex stability theorem forcing a monochromatic C10 in every extension.
- paper if solved: The paper would be a short exact-value note on the first open diagonal three-color even-cycle Ramsey number.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 6.3.1, together with Fabrico S. Benevides and Jozef Skokan, "The 3-colored Ramsey number of even cycles" (Journal of Combinatorial Theory, Series B, 2009), and bounded exact-term, alternate-notation, and recent-status web checks performed on 2026-04-13.
- Radziszowski DS1.18 Section 6.3.1, Benevides-Skokan 2009, and bounded 2026-04-13 exact-statement, alternate-notation, and recent-status searches for the diagonal C10 case.
- artifacts/r3-c10-even-cycle-ramsey/record.md
- artifacts/r3-c10-even-cycle-ramsey/status.json
