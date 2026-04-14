# Working Packet: The Exact Value of R(C14, C14, C14)

- slug: `r3-c14-even-cycle-ramsey`
- title: Determine the exact value of R(C14, C14, C14)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.7`

## statement
Either prove that every 3-coloring of K28 contains a monochromatic C14, or construct a 3-coloring of K28 with no monochromatic C14 and thus show R(C14, C14, C14) >= 29.

## novelty_notes
- frontier basis: Radziszowski DS1.17 records R3(C2m) = 4m only for sufficiently large m and says the first open case is C10; bounded 2026-04-13 primary-source web checks found no later exact diagonal paper settling C14.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no archived conflicting AutoMath mathematical status for the exact C14 three-color even-cycle problem; the matching slug and artifact directory belong to the current live dossier rather than to a retired attempt.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The conjectural target 28 is fixed, the exact C8 benchmark is known, and the large-even-cycle theory already explains why the family matters. Once C14 is resolved, the note mainly needs the forcing proof or the extremal coloring plus a short comparison with the solved smaller even-cycle case.
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
- certificate compactness: high
- exact gap from source: moderate
- assessment: Pass. This is not the first open even-cycle slice, but it still has a stable theorem statement, a named conjectural value, and a clean exact-note narrative without a feeder ladder.

## likely_paper_shape
- note title: The Exact Value of R(C14, C14, C14)
- hypothetical title: The Exact Value of R(C14, C14, C14)
- paper shape: A one-theorem exact-value note for a bounded diagonal three-color even-cycle Ramsey number.
- publication if solved: A clean exact resolution of the diagonal C14 case would still support a genuine short cycle-Ramsey paper because the conjectural target and large-n framework are already standard.
- minimal artifact requirements: Either a proof that every 3-coloring of K28 contains a monochromatic C14, or one explicit 28-vertex coloring with no monochromatic C14.

## hypothetical_abstract
We determine the exact three-color Ramsey number R(C14, C14, C14). The publicly accessible Ramsey survey revision of June 7, 2024 records the diagonal even-cycle formula only for sufficiently large lengths and states that C10 is the first open case, leaving C14 unresolved. Our theorem fixes another bounded even-cycle residue and tests the diagonal value 28 predicted by the standard 4m pattern.

## single_solve_explanation
If the C14 value is determined exactly, the resulting theorem would already carry most of the note because the expected value and the family narrative are already standard. Only a short extremal discussion and comparison with the solved C8 case remain after the main solve. This just clears the micro-paper threshold because the target is bounded and title-sized, though weaker than the first-open C9 case.

## broader_theorem_nonimplication
The large-even-cycle theorem cited in the survey applies only for sufficiently large m and does not collapse the bounded C14 diagonal case to a previously solved theorem.

## literature_gap
The June 7, 2024 Ramsey survey records the diagonal even-cycle formula only for sufficiently large lengths and does not list an exact value for R(C14, C14, C14).

## transfer_kit
- lemma: Radziszowski DS1.17 records that R3(C2m) = 4m for all sufficiently large m.
- lemma: The same survey records the exact solved benchmark R(C8, C8, C8) = 16.
- lemma: The survey states that the first open diagonal even-cycle case is R3(C10), so later bounded even-cycle residues such as C14 remain open but clearly anchored to the same formula.
- toy example: The nearest publicly solved diagonal even-cycle benchmark is R(C8, C8, C8) = 16, while the conjectural C14 target is 28.
- known obstruction: An upper-bound proof must eliminate the standard 27-vertex blowup-style constructions avoiding long monochromatic even cycles, while a disproof must exhibit one explicit 28-vertex witness.
- prior-work stop sentence: The June 7, 2024 Ramsey survey does not list an exact value for R(C14, C14, C14).
- recommended first attack: Start from the 27-vertex lower-bound pattern behind the 4m conjecture and prove that any 28-vertex perturbation forces a monochromatic C14 by a stability argument.
- paper if solved: The paper would be a short exact-value note on a bounded diagonal three-color even-cycle Ramsey number.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, revision dated June 7, 2024), Section 6.3.1, together with the Benevides-Skokan large-even-cycle result cited there and bounded 2026-04-13 primary-source web checks.
- Radziszowski DS1.17 Section 6.3.1, the large-even-cycle exact theorem cited there, and bounded 2026-04-13 searches for R(C14,C14,C14), R3(C14), and recent status signals.
- artifacts/r3-c14-even-cycle-ramsey/record.md
- artifacts/r3-c14-even-cycle-ramsey/status.json
