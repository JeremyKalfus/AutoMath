# Working Packet: The Exact Value of R(P10, P10, P10)

- slug: `r3-p10-three-color-path-ramsey`
- title: Determine the exact value of R(P10, P10, P10)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `88`
- single-solve-to-paper fraction: `0.85`

## statement
Either prove that every 3-coloring of K18 contains a monochromatic P10, or construct a 3-coloring of K18 with no monochromatic P10 and thus show R(P10, P10, P10) >= 19.

## novelty_notes
- frontier basis: The January 6, 2026 survey states that exact diagonal three-color path values are known only through P9 and that P10 is the first open case; the 2016 path paper settles only P8 and P9; bounded exact-statement, alternate-notation, and recent-status searches run on 2026-04-13 did not surface a later exact-resolution paper for P10.
- why still open: (not recorded)
- attempted conflict check: The refreshed 2026-04-13 exclusion sweep found no archived conflicting AutoMath mathematical status for the exact P10 diagonal path problem.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The conjectural value 18, the neighboring exact benchmarks, and the asymptotic family formula are already in place. Once the exact P10 value is settled, what remains is mostly a short extremal discussion, a compact critical-coloring analysis, and comparison with P8 and P9.
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
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass. This is the first open diagonal case in a named exact-value family, and one clean solve would already look like the paper rather than a feeder lemma.

## likely_paper_shape
- note title: The Exact Value of R(P10, P10, P10)
- hypothetical title: The Exact Value of R(P10, P10, P10)
- paper shape: A one-theorem exact-value note on the first open diagonal three-color path Ramsey number.
- publication if solved: Settling the first open diagonal three-color path case would already read as the title theorem of a short Ramsey note rather than as feeder evidence.
- minimal artifact requirements: Either a proof that every 3-coloring of K18 contains a monochromatic P10, or one explicit 18-vertex coloring with no monochromatic P10.

## hypothetical_abstract
We determine the exact three-color Ramsey number R(P10, P10, P10). The current Ramsey survey records exact diagonal path values only through P9 and identifies P10 as the first open case, while the 2016 paper of Dybizbanski, Dzido, and Radziszowski settles only P8 and P9. Our theorem closes the first unresolved bounded diagonal path instance and fixes the smallest remaining test of the Faudree-Schelp formula in the three-color diagonal setting.

## single_solve_explanation
If the exact P10 value is determined, the resulting theorem is already the title and core payload of the note. The family formula, the benchmark cases P8 and P9, and the expected target 18 are already standard inputs. What remains after the solve is mostly exposition, extremal-coloring discussion, and a short comparison with the last solved diagonal cases.

## broader_theorem_nonimplication
The asymptotic three-color path formula only applies for large n, and the 2016 path paper stops at P9. No broader published theorem visible in the bounded audit settles the exact diagonal P10 case.

## literature_gap
The January 6, 2026 Ramsey survey records exact diagonal three-color path values only through P9 and states that P10 is the first open case.

## transfer_kit
- lemma: DS1.18 records the asymptotic formula R(Pn, Pn, Pn) = 2n - 2 + (n mod 2) for large n and says P10 is the first open diagonal case.
- lemma: The same survey records the exact predecessor values R(P8, P8, P8) = 14 and R(P9, P9, P9) = 17.
- lemma: The 2016 path paper proves that if R(C2m, C2m, C2m) = 4m then R(P2m+1, P2m+1, P2m+1) = 4m + 1, clarifying where transfer from cycle methods is available and where it is not.
- toy example: The nearest solved diagonal path values are R(P8, P8, P8) = 14 and R(P9, P9, P9) = 17, while the conjectural P10 target is 18.
- known obstruction: Any upper-bound proof must eliminate 17-vertex three-color templates with all monochromatic components shorter than P10, while a disproof must exhibit one explicit 18-vertex coloring without a monochromatic P10.
- prior-work stop sentence: The January 6, 2026 Ramsey survey states that P10 is the first open diagonal three-color path case.
- recommended first attack: Start from the conjectural 17-vertex extremal block template and prove that every 18th-vertex extension forces a monochromatic P10 via a stability analysis.
- paper if solved: The paper would be a short exact-value note closing the first open diagonal three-color path Ramsey number.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 6.4.1, together with Janusz Dybizbanski, Tomasz Dzido, and Stanislaw Radziszowski, "On Some Three-Color Ramsey Numbers for Paths" (Discrete Applied Mathematics, 2016), and bounded exact-term, alternate-notation, and recent-status web checks performed on 2026-04-13.
- Radziszowski DS1.18 Section 6.4.1, Dybizbanski-Dzido-Radziszowski 2016, and bounded 2026-04-13 exact-statement, alternate-notation, and recent-status searches for the diagonal P10 case.
- artifacts/r3-p10-three-color-path-ramsey/record.md
- artifacts/r3-p10-three-color-path-ramsey/status.json
