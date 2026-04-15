# Working Packet: The Three-Color Ramsey Number of C10

- slug: `r3-c10-triple-cycle`
- title: Determine the exact value of R(C10, C10, C10)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `82`
- single-solve-to-paper fraction: `0.78`

## statement
Determine the least N such that every 3-coloring of the edges of K_N contains a monochromatic 10-cycle.

## novelty_notes
- frontier basis: The 2026 dynamic survey states that Dzido's conjecture R_3(C_{2m}) = 4m is open first at C10, while exact values are recorded through C8 and large even-cycle asymptotics are already known.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If C10 is settled exactly, the note already has a named conjectural backdrop, a natural target value 20, and a crisp first-open-case narrative. Little more than a proof, a sharp lower construction or obstruction, and short context would remain.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Lane-eligible. This is a small exact theorem with a strong family anchor, an honest short-note title, and low post-solve editorial drag.

## likely_paper_shape
- note title: The Three-Color Ramsey Number of C10
- hypothetical title: The Three-Color Ramsey Number of C10
- paper shape: A single-theorem note settling the first unresolved even-cycle case in the three-color cycle Ramsey program.
- publication if solved: An exact determination of R(C10, C10, C10) would plausibly be publishable as a short note on the first unresolved even-cycle case in the three-color cycle-Ramsey line.
- minimal artifact requirements: Either a proof that every 3-coloring of K20 contains a monochromatic C10, or a 19-vertex coloring with no monochromatic C10 showing the natural target 20 fails.

## hypothetical_abstract
We determine the three-color Ramsey number R(C10, C10, C10). The current checked literature presents C10 as the first unresolved even-cycle case after the exact small table and the large-n exact theorem for even cycles. Resolving this case would give a compact stand-alone contribution anchored to the long-running conjecture R_3(C_{2m}) = 4m.

## single_solve_explanation
A proof of the exact value would itself be the title theorem of a short note. The remaining work would mostly be exposition: stating the first-open-case context, recording the sharp construction or forcing argument, and comparing with the exact C8 benchmark and the large-n theorem. That is comfortably within the 70-90% paper band.

## broader_theorem_nonimplication
The checked sources only give the exact even-cycle formula for sufficiently large n, not for all even n, and the survey explicitly names C10 as the first unresolved case. So a broader published theorem does not already force the exact C10 value.

## literature_gap
Prior work reaches exact three-color cycle values through C8 and a large-n exact theorem for even cycles, but the 2026 survey still identifies R(C10, C10, C10) as the first open even-cycle case.

## transfer_kit
- lemma: Radziszowski's 2026 survey records Dzido's conjecture that R_3(C_{2m}) = 4m for all m >= 3.
- lemma: The same survey records exact three-color cycle values through C8, giving the nearest solved benchmark R(C8, C8, C8) = 16.
- lemma: The same section records that R(C_n, C_n, C_n) = 2n for large even n, so the ambient asymptotic picture is already exact.
- lemma: The survey explicitly identifies R(C10, C10, C10) as the first open even-cycle case.
- toy example: The exact neighboring benchmark R(C8, C8, C8) = 16 is already recorded in the survey's small-cycle table.
- known obstruction: The current packet does not expose a published exact forcing argument for C10, so either a new structural argument or a sharp critical coloring analysis is still needed.
- prior-work stop sentence: Current checked sources solve the small table through C8 and the large even-cycle regime, but still leave R(C10, C10, C10) open.
- recommended first attack: Exploit the natural target value 20 and analyze whether a 19-vertex critical coloring can be excluded by combining the small exact cycle table with even-cycle forcing patterns.
- paper if solved: If solved exactly, the paper would be a short note closing the first open even-cycle case in the three-color cycle Ramsey line.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics Dynamic Survey DS1 revision 18, 2026), Section 6.3.1(b), citing T. Dzido's 2005 conjecture R_3(C_{2m}) = 4m for m >= 3, the exact table through C8, and the large-n even-cycle theorem of Benevides and Skokan; bounded 2026 exact-statement, alternate-notation, and recent-status searches in this run did not surface a later exact closure of R(C10, C10, C10).
- Radziszowski 2026 survey Section 6.3.1(b), the Dzido even-cycle conjecture, the exact table through C8, the large-n Benevides-Skokan theorem, and bounded 2026 status searches run here.
- artifacts/r3-c10-triple-cycle/record.md
- artifacts/r3-c10-triple-cycle/status.json
