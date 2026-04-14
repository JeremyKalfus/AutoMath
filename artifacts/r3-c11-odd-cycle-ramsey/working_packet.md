# Working Packet: The Exact Value of R(C11, C11, C11)

- slug: `r3-c11-odd-cycle-ramsey`
- title: Determine the exact value of R(C11, C11, C11)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.74`

## statement
Either prove that every 3-coloring of K41 contains a monochromatic C11, or construct a 3-coloring of K41 with no monochromatic C11 and thus show R(C11, C11, C11) >= 42.

## novelty_notes
- frontier basis: The January 6, 2026 survey states that the Bondy-Erdos prediction would give R(Cn, Cn, Cn) = 4n - 3 for odd n and still singles out C9 as the first open case; the UCSD Erdos page still presents the three-color odd-cycle family as open at the family level; bounded exact-statement, alternate-notation, and recent-status searches run on 2026-04-13 did not surface a later exact paper settling the diagonal C11 case.
- why still open: (not recorded)
- attempted conflict check: The refreshed 2026-04-13 exclusion sweep found no archived conflicting AutoMath mathematical status for the exact C11 diagonal odd-cycle problem.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The predicted value 41 and the family story are already fixed. Once the exact C11 value is settled, the remaining paper work is mainly a compact extremal discussion and placement relative to the solved C7 case and the first-open C9 frontier.
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
- assessment: Pass. This is no longer the first open odd-cycle slice, but it still has a stable theorem statement, a named conjectural value, and a plausible standalone short-note shape.

## likely_paper_shape
- note title: The Exact Value of R(C11, C11, C11)
- hypothetical title: The Exact Value of R(C11, C11, C11)
- paper shape: A one-theorem exact-value note for a bounded diagonal three-color odd-cycle Ramsey number.
- publication if solved: A sharp exact C11 resolution would still support a real short odd-cycle Ramsey note because the family conjecture and open-problem framing are already standard.
- minimal artifact requirements: Either a proof that every 3-coloring of K41 contains a monochromatic C11, or one explicit 41-vertex coloring with no monochromatic C11.

## hypothetical_abstract
We determine the exact three-color Ramsey number R(C11, C11, C11). The current Ramsey survey records the Bondy-Erdos prediction R(Cn, Cn, Cn) = 4n - 3 for odd n only as a sufficiently-large theorem and a bounded conjectural program, with C9 listed as the first open case. Our theorem settles another bounded odd-cycle residue in that diagonal three-color family.

## single_solve_explanation
If C11 is settled exactly, the resulting theorem is already the note's main contribution. The post-solve work is mostly packaging: a short account of the critical coloring pattern and comparison with existing odd-cycle theory. This is weaker than the first-open C9 slice, but it still stays inside the 70-90 percent paper window because the mathematical burden is concentrated in one exact bounded theorem.

## broader_theorem_nonimplication
The published odd-cycle theorem covers only sufficiently large odd n, and the family-level open-problem pages still phrase the three-color odd-cycle exact program as unresolved. No bounded theorem located in the audit settles C11 directly.

## literature_gap
The current accessible survey and family-level problem pages do not report an exact value for R(C11, C11, C11).

## transfer_kit
- lemma: DS1.18 states that if the Bondy-Erdos odd-cycle prediction holds then R(Cn, Cn, Cn) = 4n - 3 for odd n.
- lemma: The survey records the exact solved predecessor R(C7, C7, C7) = 25.
- lemma: The UCSD Erdos problem page still states the family-level three-color cycle inequality r(Cn, Cn, Cn) <= 4n - 3 as an open problem framework for odd cycles.
- toy example: The nearest exact odd-cycle benchmark still visible in the survey is R(C7, C7, C7) = 25, while the conjectural C11 target is 41.
- known obstruction: An upper-bound proof must rule out 40-vertex blowup-style odd-cycle constructions, while a disproof must exhibit one explicit 41-vertex coloring without a monochromatic C11.
- prior-work stop sentence: The current accessible survey does not report an exact value for R(C11, C11, C11).
- recommended first attack: Use the standard odd-cycle blowup lower-bound pattern as a template and seek a 41-vertex stability theorem forcing a monochromatic C11 in every extension.
- paper if solved: The paper would be a short exact-value note on a bounded diagonal three-color odd-cycle Ramsey number.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 6.3.1, together with the UCSD Erdos problem page for three-color cycle Ramsey numbers and bounded exact-term, alternate-notation, and recent-status web checks performed on 2026-04-13.
- Radziszowski DS1.18 Section 6.3.1, the UCSD Erdos three-color cycle problem page, and bounded 2026-04-13 exact-statement, alternate-notation, and recent-status searches for the diagonal C11 case.
- artifacts/r3-c11-odd-cycle-ramsey/record.md
- artifacts/r3-c11-odd-cycle-ramsey/status.json
