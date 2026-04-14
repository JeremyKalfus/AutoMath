# Working Packet: The Exact Value of R4(C6)

- slug: `r4-c6-four-color-cycle-ramsey`
- title: Determine the exact value of R4(C6)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `77`
- single-solve-to-paper fraction: `0.71`

## statement
Determine the exact value of R4(C6) in the current range 18 <= R4(C6) <= 20 by proving the sharp upper bound and matching it with a critical coloring, or by improving the lower bound and then sealing the exact upper bound.

## novelty_notes
- frontier basis: Radziszowski DS1.17 lists 18 <= R4(C6) <= 20, while the 2013 hexagon paper proves only mixed four-color bounds such as 18 <= R(C6, C6, H1, H2) <= 20 with H_i in {C4, C6}; bounded 2026-04-13 primary-source web checks found no later exact diagonal resolution.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no archived conflicting AutoMath mathematical status for the exact four-color hexagon problem; the matching slug and artifact directory belong to the current live dossier rather than to a retired attempt.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The note would have a crisp one-line theorem, a tiny numerical range, and a short discussion of critical colorings. Once the exact diagonal value is pinned down, only the final proof packet and a comparison to the mixed-case 2013 bounds remain.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Pass with some caution. The gap is small and the family anchor is strong, but the final proof may still need a more explicit critical-coloring packet than the cycle and path diagonal cases above.

## likely_paper_shape
- note title: The Exact Value of R4(C6)
- hypothetical title: The Exact Value of R4(C6)
- paper shape: A short exact-value note for the four-color Ramsey number of the hexagon.
- publication if solved: Closing the four-color hexagon gap would produce a real exact-value note in a named multicolor cycle family, with most of the surrounding exposition already supplied by the current bounds literature.
- minimal artifact requirements: A sharp upper-bound proof at the exact value N together with a matching (N-1)-vertex four-coloring avoiding monochromatic C6.

## hypothetical_abstract
We determine the four-color Ramsey number R4(C6). The publicly accessible Ramsey survey revision of June 7, 2024 leaves only the range 18 <= R4(C6) <= 20, and the 2013 paper on four-color hexagons resolves several related mixed tuples without settling the diagonal case. Our theorem closes the remaining bounded gap for the first unresolved four-color even-cycle hexagon value.

## single_solve_explanation
If the exact diagonal hexagon value is fixed, the theorem already provides the paper title and main payload. The remaining work is mainly the presentation of the critical coloring and a short comparison with the mixed-case four-color bounds. This is close to the lower edge of the target band, but still acceptable because the parameter range is tiny and the surrounding literature already frames the note.

## broader_theorem_nonimplication
The general multicolor even-cycle results in the survey are asymptotic or coarse, and the 2013 four-color hexagon paper only treats mixed tuples, so no broader published theorem currently settles the diagonal R4(C6) case.

## literature_gap
The June 7, 2024 Ramsey survey lists only 18 <= R4(C6) <= 20 and does not report an exact value.

## transfer_kit
- lemma: Radziszowski DS1.17 records the current diagonal bound 18 <= R4(C6) <= 20.
- lemma: The same survey records the exact neighboring value R5(C6) = 26.
- lemma: Wang, Xu, and Xie show that 18 <= R(C6, C6, H1, H2) <= 20 when H1 and H2 are each isomorphic to C4 or C6, which gives usable local structure around the diagonal case.
- toy example: The mixed four-color cases around C6 already sit in the same 18-20 band, so any diagonal argument can be benchmarked against those near-neighbor hexagon tuples.
- known obstruction: Any exact proof must either classify or decisively rule out 17-, 18-, or 19-vertex critical four-color hexagon colorings, which may require a compact but nontrivial extremal packet.
- prior-work stop sentence: The June 7, 2024 Ramsey survey lists only 18 <= R4(C6) <= 20 and does not report an exact value.
- recommended first attack: Exploit the mixed-tuple 2013 hexagon bounds to constrain diagonal critical colorings, then perform a stability analysis around 19-vertex witnesses before any heavier search.
- paper if solved: The paper would be a short exact-value contribution on multicolor Ramsey numbers for cycles, centered on the diagonal four-color hexagon case.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, revision dated June 7, 2024), Section 6.3.2, together with Wang-Xu-Xie, "On the Four Color Ramsey Numbers for Hexagons" (Ars Combinatoria 111, 2013), and bounded 2026-04-13 primary-source web checks.
- Radziszowski DS1.17 Section 6.3.2, Wang-Xu-Xie 2013 on four-color hexagons, and bounded 2026-04-13 searches for R4(C6), R_4(C6), and recent multicolor-cycle status signals.
- artifacts/r4-c6-four-color-cycle-ramsey/record.md
- artifacts/r4-c6-four-color-cycle-ramsey/status.json
