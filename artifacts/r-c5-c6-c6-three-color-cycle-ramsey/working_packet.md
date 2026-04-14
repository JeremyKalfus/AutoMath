# Working Packet: The Exact Value of R(C5, C6, C6)

- slug: `r-c5-c6-c6-three-color-cycle-ramsey`
- title: Determine the exact value of R(C5, C6, C6)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.74`

## statement
Determine the least n such that every 3-coloring of E(K_n) contains either a color-1 C5 or a color-2 C6 or a color-3 C6.

## novelty_notes
- frontier basis: Current public sources leave this multicolor cycle Ramsey number at 15 <= R(C5, C6, C6) <= 17. The 2021 SDP upper bound compressed the problem to a very small finite interval.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A clean exact closure would already provide the note's main theorem and most of its motivation. The remaining work would be a compact construction or exclusion argument and a brief comparison with neighboring small cycle values.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
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
- assessment: Pass, but behind the top slot. The gap is slightly wider and the surrounding story is weaker than the one-step hypergraph candidate, yet one exact solve would still be most of a short paper.

## likely_paper_shape
- note title: The Exact Value of R(C5, C6, C6)
- hypothetical title: The Exact Value of R(C5, C6, C6)
- paper shape: A short exact-value note for a small three-color cycle Ramsey number.
- publication if solved: An exact determination of R(C5, C6, C6) would likely support a short note because it closes a small finite multicolor cycle gap in a standard family.
- minimal artifact requirements: Either a 15- or 16-vertex extremal coloring matching the exact lower side, or a proof that the next complete graph forces one of the target cycles.

## hypothetical_abstract
We determine the three-color Ramsey number R(C5, C6, C6). Previous work placed this number in the interval 15 <= R(C5, C6, C6) <= 17. Our result closes the remaining finite gap for this small cycle configuration.

## single_solve_explanation
This target still passes the 70-90% paper test because an exact closure would genuinely be the title theorem. After the solve, the remaining work is mostly expository cleanup and presentation of the extremal coloring or forcing proof. The gap is small enough that no feeder ladder is needed.

## broader_theorem_nonimplication
Known asymptotic cycle-Ramsey theorems and monotonicity statements do not force the exact finite endpoint here. The 2021 SDP improvement narrows the interval but does not settle 15 versus 16 versus 17.

## literature_gap
Current public sources stop at 15 <= R(C5, C6, C6) <= 17.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 8, gives the upper bound R(C5, C6, C6) <= 17.
- lemma: The same theorem records the known lower bound 15 <= R(C5, C6, C6).
- lemma: The 2024 Dynamic Survey supplies the standard cycle-Ramsey notation and nearby finite values as context.
- lemma: The 2021 paper treats this as a finite exact-bound problem accessible to SDP-driven local obstruction analysis.
- toy example: The neighboring exact three-color cycle number R(C3, C5, C5) = 17 from the same 2021 paper is the closest solved comparison point.
- known obstruction: A lower-bound construction must avoid an odd cycle in one color and even cycles in the other two simultaneously, while an upper-bound proof must control several near-bipartite local structures.
- prior-work stop sentence: Current sources stop at 15 <= R(C5, C6, C6) <= 17.
- recommended first attack: Extract local forbidden-pattern data from the 2021 SDP certificate and test whether any 15- or 16-vertex critical coloring can extend consistently under cycle-parity constraints.
- paper if solved: The paper would be a short exact-value note for a small three-color cycle Ramsey number with a compact extremal analysis.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 8, which gives 15 <= R(C5, C6, C6) <= 17; together with the 2024 revision of Radziszowski's Dynamic Survey "Small Ramsey Numbers" as family context and bounded 2026-04-14 recent-status web checks during curation that did not reveal a later exact closure.
- 2021 Lidicky-Pfender Theorem 8, the 2024 Dynamic Survey for surrounding Ramsey context, and bounded 2026-04-14 recent-status web checks.
- artifacts/r-c5-c6-c6-three-color-cycle-ramsey/record.md
- artifacts/r-c5-c6-c6-three-color-cycle-ramsey/status.json
