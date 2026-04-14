# Working Packet: The Exact Value of R(C12, C12, C12)

- slug: `r3-c12-even-cycle-ramsey`
- title: Determine the exact value of R(C12, C12, C12)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `73`
- single-solve-to-paper fraction: `0.72`

## statement
Either prove that every 3-coloring of K24 contains a monochromatic C12, or construct a 3-coloring of K24 with no monochromatic C12 and thus show R(C12, C12, C12) >= 25.

## novelty_notes
- frontier basis: The January 6, 2026 survey records R3(C2m) = 4m only for sufficiently large m and lists C10 as the first open diagonal case; the Benevides-Skokan paper proves the even-cycle formula only beyond a threshold; bounded exact-statement, alternate-notation, and recent-status searches run on 2026-04-13 did not surface a later exact-resolution paper for C12.
- why still open: (not recorded)
- attempted conflict check: The refreshed 2026-04-13 exclusion sweep found no archived conflicting AutoMath mathematical status for the exact C12 diagonal even-cycle problem.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The conjectural value 24, the C8 benchmark, and the large-even-cycle theory are already known. Once C12 is resolved, the note mostly needs a compact forcing proof or a critical coloring together with a short comparison to C10 and the large-n theorem.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Pass. This is not the first open even-cycle slice, but it still has a stable exact theorem statement and a note-sized publication packet if solved sharply.

## likely_paper_shape
- note title: The Exact Value of R(C12, C12, C12)
- hypothetical title: The Exact Value of R(C12, C12, C12)
- paper shape: A one-theorem exact-value note for a bounded diagonal three-color even-cycle Ramsey number.
- publication if solved: A clean exact resolution of the diagonal C12 case would still support a genuine short cycle-Ramsey paper because the conjectural target and family backdrop are already standard.
- minimal artifact requirements: Either a proof that every 3-coloring of K24 contains a monochromatic C12, or one explicit 24-vertex coloring with no monochromatic C12.

## hypothetical_abstract
We determine the exact three-color Ramsey number R(C12, C12, C12). The current Ramsey survey records the diagonal even-cycle formula only for sufficiently large lengths and leaves bounded cases beginning at C10 unresolved. Our theorem settles another concrete even-cycle residue in the diagonal three-color family and fixes the predicted value 24 at the smallest even parameter beyond the first-open case.

## single_solve_explanation
If the exact C12 value is determined, the theorem already carries most of the note because the family conjecture, lower-bound pattern, and comparison benchmarks are already established. What remains is a short extremal discussion and the presentation of the critical coloring or structural obstruction. This is weaker than C10 but still inside the target paper window.

## broader_theorem_nonimplication
The published even-cycle theorem applies only for sufficiently large even n, so the bounded diagonal C12 case is not already implied by the large-n result.

## literature_gap
The current accessible survey does not list an exact value for R(C12, C12, C12).

## transfer_kit
- lemma: DS1.18 records the lower bound R3(C2m) >= 4m for all m >= 2.
- lemma: The same survey records the exact benchmark R(C8, C8, C8) = 16 and says C10 is the first open even-cycle case.
- lemma: Benevides and Skokan prove R(Cn, Cn, Cn) = 2n for all sufficiently large even n, giving the large-scale structural model but not the bounded C12 case.
- toy example: The nearest exact diagonal even-cycle benchmark is R(C8, C8, C8) = 16, while the conjectural C12 target is 24.
- known obstruction: An upper-bound proof must eliminate 23-vertex extremal templates with no monochromatic C12, while a disproof must exhibit one explicit 24-vertex coloring of that type.
- prior-work stop sentence: The current accessible survey does not list an exact value for R(C12, C12, C12).
- recommended first attack: Treat the 23-vertex lower-bound pattern as the unique near-extremal template and prove that any 24-vertex extension forces a monochromatic C12.
- paper if solved: The paper would be a short exact-value note on a bounded diagonal three-color even-cycle Ramsey number.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 6.3.1, together with Fabrico S. Benevides and Jozef Skokan, "The 3-colored Ramsey number of even cycles" (Journal of Combinatorial Theory, Series B, 2009), and bounded exact-term, alternate-notation, and recent-status web checks performed on 2026-04-13.
- Radziszowski DS1.18 Section 6.3.1, Benevides-Skokan 2009, and bounded 2026-04-13 exact-statement, alternate-notation, and recent-status searches for the diagonal C12 case.
- artifacts/r3-c12-even-cycle-ramsey/record.md
- artifacts/r3-c12-even-cycle-ramsey/status.json
