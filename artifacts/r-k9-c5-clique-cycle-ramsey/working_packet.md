# Working Packet: The Exact Value of R(K9, C5)

- slug: `r-k9-c5-clique-cycle-ramsey`
- title: Determine the exact value of R(K9, C5)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `58`
- single-solve-to-paper fraction: `0.62`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red K9 or a blue C5.

## novelty_notes
- frontier basis: Current public sources leave this clique-versus-cycle Ramsey number at 33 <= R(K9, C5) <= 36. The family anchor is classical, but the solve-to-paper distance is materially longer than for the surviving one-step candidates.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A future exact solve would still matter, but the present interval is wide enough that the eventual proof may not stay compact. That residual risk pushes it outside the strict micro-paper lane.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail for the strict lane. Strong family anchor, but too much residual solve-to-paper distance remains after curation.

## likely_paper_shape
- note title: The Exact Value of R(K9, C5)
- hypothetical title: The Exact Value of R(K9, C5)
- paper shape: A classical exact-value clique-versus-cycle note, but not a clean one-shot packet at the present interval size.
- publication if solved: An exact determination of R(K9, C5) would be publishable in the classical clique-versus-cycle literature, but the current gap is still too wide for a strict one-shot micro-paper.
- minimal artifact requirements: A compact extremal coloring or forcing argument collapsing the interval 33-36 to a single value.

## hypothetical_abstract
We determine the Ramsey number R(K9, C5). Previous work bounded this number between 33 and 36. Our result closes the remaining finite gap for this clique-versus-cycle pair.

## single_solve_explanation
This is a real classical exact-value target, but it fails the strict paper-fraction test because the frontier interval is still four values wide. Even a successful solve may need a broader structural argument or larger certificate packet before the note feels short and self-contained.

## broader_theorem_nonimplication
The exact neighboring value R(K8, C5) = 29 and general clique-versus-odd-cycle methods do not force the exact endpoint for K9 versus C5. The bounded audit did not surface a broader theorem settling 33, 34, 35, or 36 automatically.

## literature_gap
Current public sources stop at 33 <= R(K9, C5) <= 36.

## transfer_kit
- lemma: Lidicky-Pfender (2021), Theorem 7, gives the upper bound R(K9, C5) <= 36.
- lemma: The same source records the lower bound R(K9, C5) >= 33.
- lemma: Lidicky-Pfender (2021), Theorem 1, gives the exact neighboring value R(K8, C5) = 29.
- lemma: Balanced multipartite lower-bound constructions and standard monotonicity provide nearby comparison points without fixing the exact endpoint.
- toy example: The exact smaller case R(K8, C5) = 29 is the closest solved model for the intended theorem shape.
- known obstruction: Clique-versus-odd-cycle problems can preserve dense multipartite critical graphs over several consecutive orders, making a short exact proof less likely than the raw interval size suggests.
- prior-work stop sentence: Current sources stop at 33 <= R(K9, C5) <= 36.
- recommended first attack: Test whether the balanced multipartite lower-bound pattern is rigid enough that every 33-vertex extremal must resemble a blow-up of the K8/C5 witness; otherwise the target is probably too wide for the lane.
- paper if solved: The paper would be a classical exact-value note on a clique-versus-cycle Ramsey number, but it is not currently close enough to one-shot publication mode.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 7, giving 33 <= R(K9, C5) <= 36; together with bounded 2026-04-14 recent-status web checks that did not reveal a later exact determination.
- 2021 Lidicky-Pfender Theorem 7, Theorem 1 as nearby exact context, and bounded 2026-04-14 recent-status web checks.
- artifacts/r-k9-c5-clique-cycle-ramsey/record.md
- artifacts/r-k9-c5-clique-cycle-ramsey/status.json
