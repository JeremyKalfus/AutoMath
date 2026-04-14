# Working Packet: The Exact Value of R(P11, P11, P11)

- slug: `r3-p11-three-color-path-ramsey`
- title: Determine the exact value of R(P11, P11, P11)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `61`
- single-solve-to-paper fraction: `0.66`

## statement
Either prove that every 3-coloring of K21 contains a monochromatic P11, or construct a 3-coloring of K21 with no monochromatic P11 and thus show R(P11, P11, P11) >= 22.

## novelty_notes
- frontier basis: The January 6, 2026 survey still leaves diagonal path cases beyond P9 unresolved, and bounded exact-statement, alternate-notation, and recent-status checks run on 2026-04-13 did not surface a later exact-resolution paper for P11.
- why still open: (not recorded)
- attempted conflict check: The refreshed 2026-04-13 exclusion sweep found no archived conflicting AutoMath mathematical status for the exact P11 diagonal path problem.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved by a path-specific argument, the result would still look like a short exact-value note. However, the literature already advertises a direct transfer from C10 to P11, which threatens theorem-slice stability.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: high
- theorem-slice stability: unclear
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail for the strict lane. The result may still be publishable if solved directly, but the theorem slice is not stable enough because the honest paper could collapse into a stronger C10-to-P11 transfer theorem or an exact C10 result.

## likely_paper_shape
- note title: The Exact Value of R(P11, P11, P11)
- hypothetical title: The Exact Value of R(P11, P11, P11)
- paper shape: Potentially a short exact-value note, but with unstable theorem packaging because cycle-to-path transfer may dominate the proof.
- publication if solved: A direct exact determination of the diagonal P11 value could support a short note, but the most plausible proof route may reframe the paper around the even-cycle case C10 instead.
- minimal artifact requirements: Either a proof that every 3-coloring of K21 contains a monochromatic P11, or one explicit 21-vertex coloring with no monochromatic P11.

## hypothetical_abstract
We determine the exact three-color Ramsey number R(P11, P11, P11). The current Ramsey survey leaves all diagonal path cases beyond P9 unresolved, and the 2016 path paper isolates a direct implication from the conjectural C10 even-cycle case to the odd-path value 21. Our theorem would settle one more bounded diagonal path instance, although the surrounding proof architecture may force a broader cycle-based framing.

## single_solve_explanation
A direct path-specific solve would still carry most of a short note. The problem is not mathematical insignificance but packaging stability: the most natural proof route may first resolve C10 or a stronger transfer theorem, making P11 a corollary rather than the honest title theorem. For that reason the single-solve-to-paper fraction falls below the micro-paper lane threshold.

## broader_theorem_nonimplication
No published theorem found in the bounded audit already settles P11 exactly, but the literature explicitly flags a route from exact even-cycle results to this odd-path value, so broader-theorem implication risk is high.

## literature_gap
The current accessible survey does not list an exact value for R(P11, P11, P11).

## transfer_kit
- lemma: DS1.18 records the large-n diagonal path formula and says exact diagonal values are known only through P9.
- lemma: The survey notes that the conjectured equality R(C2m, C2m, C2m) = 4m would imply R(P2m+1, P2m+1, P2m+1) = 4m + 1.
- lemma: The 2016 path paper proves this cycle-to-path implication and settles only the benchmark odd-path cases P8 and P9.
- toy example: If C10 were known to equal 20, the transfer statement highlighted in the 2016 paper would immediately predict R(P11, P11, P11) = 21.
- known obstruction: A direct P11 proof risks collapsing into an exact C10 theorem or a stronger transfer statement, undermining the stability of P11 as the honest title theorem.
- prior-work stop sentence: The current accessible survey does not list an exact value for R(P11, P11, P11).
- recommended first attack: Only pursue this slice if a path-specific stability argument can be isolated without first proving the exact C10 even-cycle case.
- paper if solved: If solved by a genuinely path-specific argument, the paper could be a short exact-value note, but the honest framing may shift to a broader cycle-based theorem.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 6.4.1, together with Janusz Dybizbanski, Tomasz Dzido, and Stanislaw Radziszowski, "On Some Three-Color Ramsey Numbers for Paths" (Discrete Applied Mathematics, 2016), and bounded exact-term, alternate-notation, and recent-status web checks performed on 2026-04-13.
- Radziszowski DS1.18 Section 6.4.1, Dybizbanski-Dzido-Radziszowski 2016, and bounded 2026-04-13 exact-statement, alternate-notation, and recent-status searches for the diagonal P11 case.
- artifacts/r3-p11-three-color-path-ramsey/record.md
- artifacts/r3-p11-three-color-path-ramsey/status.json
