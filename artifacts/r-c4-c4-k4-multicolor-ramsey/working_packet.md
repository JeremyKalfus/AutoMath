# Working Packet: The Exact Value of R(C4, C4, K4)

- slug: `r-c4-c4-k4-multicolor-ramsey`
- title: Determine the exact value of R(C4, C4, K4)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `88`
- single-solve-to-paper fraction: `0.86`

## statement
Determine the least n such that every 3-coloring of E(K_n) contains either a color-1 C4, a color-2 C4, or a color-3 K4.

## novelty_notes
- frontier basis: Current public sources leave this multicolor Ramsey number at 20 <= R(C4, C4, K4) <= 21. The 2021 semidefinite-programming paper narrows the upper side but does not settle the lower endpoint.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved exactly, the proof or critical coloring is almost the entire paper. The surrounding literature and motivation are already in place, so the remaining work is mainly proof presentation, a compact extremal certificate, and one short discussion paragraph.
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
- assessment: Pass. This is the cleanest one-step gap found in the bounded audit, with strong family anchor and low editorial residue after a solve.

## likely_paper_shape
- note title: The Exact Value of R(C4, C4, K4)
- hypothetical title: The Exact Value of R(C4, C4, K4)
- paper shape: A one-theorem exact-value note closing a one-step multicolor C4/K4 Ramsey gap.
- publication if solved: An exact determination of R(C4, C4, K4) would be the title theorem of a compact note because the live frontier gap is a single unresolved step after the 2021 upper-bound improvement.
- minimal artifact requirements: Either an explicit (C4, C4, K4; 20)-coloring or a proof that every 3-coloring of K20 already forces one of the forbidden monochromatic subgraphs; in either direction the certificate must be compact and human-checkable.

## hypothetical_abstract
We determine the 3-color Ramsey number R(C4, C4, K4). Earlier work gave 19 <= R(C4, C4, K4) <= 22, and semidefinite programming later reduced the upper bound to 21. Our result closes the remaining one-step gap and identifies the exact threshold for forcing two monochromatic quadrilaterals or a monochromatic K4.

## single_solve_explanation
This target already has the right paper shape because the frontier is a one-step exact-value gap. Once the exact lower or upper endpoint is proved, most of the note is finished: statement, motivation, and context are already supplied by the prior literature. What remains is mainly polishing the proof or presenting the extremal coloring cleanly.

## broader_theorem_nonimplication
Known asymptotic or monotonicity statements for multicolor C4-Ramsey numbers do not force the finite endpoint 20 or 21. The 2021 SDP result improves only the upper side and does not imply exactness.

## literature_gap
Current public sources stop at 20 <= R(C4, C4, K4) <= 21.

## transfer_kit
- lemma: Xu-Shao-Radziszowski (2008), Theorem 3, gives the constructive lower bound R(C4, C4, K4) >= 19.
- lemma: Xu-Shao-Radziszowski (2008), Table 1, records the pre-2021 interval 19 <= R(C4, C4, K4) <= 22.
- lemma: Lidicky-Pfender (2021), Theorem 8, improves the upper bound to R(C4, C4, K4) <= 21.
- lemma: The product-coloring lower-bound method highlighted in the 2008 paper remains a concrete template for extremal constructions in this family.
- toy example: The exact coloring in Xu-Shao-Radziszowski proving a (C4, C4, K4; 18)-coloring is the smallest concrete extremal instance immediately below the current live gap.
- known obstruction: A lower-bound attack must build a 20-vertex 3-coloring simultaneously avoiding two monochromatic C4 copies in different colors and a monochromatic K4 in the third color; an upper-bound attack must exclude every such coloring.
- prior-work stop sentence: Current sources stop at 20 <= R(C4, C4, K4) <= 21.
- recommended first attack: Exploit the 2021 SDP profile to extract forbidden local patterns, then combine that with a structured extension search from the known 18-vertex lower-bound coloring.
- paper if solved: The paper would be a concise exact-value note closing the last one-step gap for this specific multicolor quadrilateral/clique Ramsey number.

## bounded_source_list
- Xiaodong Xu, Zehui Shao, and Stanislaw P. Radziszowski, "Bounds on Some Ramsey Numbers Involving Quadrilateral" (2008), Theorem 3 and Table 1, which give 19 <= R(C4, C4, K4) <= 22; together with Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 8, which improves the upper bound to 21; plus bounded 2026-04-14 exact-notation and recent-status web checks that did not reveal a later exact closure.
- 2008 Xu-Shao-Radziszowski for the lower bound and early table, 2021 Lidicky-Pfender for the tightened upper bound, plus bounded 2026-04-14 exact-notation and recent-status web checks.
- artifacts/r-c4-c4-k4-multicolor-ramsey/record.md
- artifacts/r-c4-c4-k4-multicolor-ramsey/status.json
