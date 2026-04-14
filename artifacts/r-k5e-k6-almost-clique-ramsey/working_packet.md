# Working Packet: On the Exact Value of R(K5-e, K6)

- slug: `r-k5e-k6-almost-clique-ramsey`
- title: Determine the exact value of R(K5-e, K6)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `49`
- single-solve-to-paper fraction: `0.52`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red copy of K5-e or a blue copy of K6.

## novelty_notes
- frontier basis: Current bounded-source evidence exposes a live interval 43 <= R(K5-e, K6) <= 59 rather than an exact value.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved exactly, the result would still be the main theorem of a short note in a standard family. The remaining work after the solve would mostly be certificate presentation and comparison to nearby one-edge values. The problem is that the solve itself still looks too large.
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
- search-heavy: True
- certificate compactness: low
- exact gap from source: moderate
- assessment: Not lane-eligible. The theorem slice is stable, but the remaining residue is much too large for the intended one-shot publication mode.

## likely_paper_shape
- note title: On the Exact Value of R(K5-e, K6)
- hypothetical title: The Exact Value of R(K5-e, K6)
- paper shape: A computational exact-value note in a one-edge Ramsey family.
- publication if solved: A sharp value for R(K5-e, K6) would still be publishable as a conventional Ramsey note, but it sits well outside the intended one-shot micro-paper lane.
- minimal artifact requirements: A sharp lower-bound coloring or a full upper-bound exclusion proof, together with exhaustive verification.

## hypothetical_abstract
We determine the Ramsey number R(K5-e, K6). The bounded literature audit for this run leaves the parameter between 43 and 59. Our result closes that gap for a standard complete-versus-almost-complete Ramsey pair.

## single_solve_explanation
A successful exact solve would still yield a recognizable title theorem. The family anchor is strong enough that the final paper shape is not in doubt. This slot remains outside the target lane because the current gap is too wide and the likely proof is too computation-heavy.

## broader_theorem_nonimplication
The checked 2022 source only improves the lower side, while the older upper-bound source remains far away. The bounded recent search did not reveal a later theorem collapsing the interval.

## literature_gap
The sources checked here expose only 43 <= R(K5-e, K6) <= 59.

## transfer_kit
- lemma: Goedgebeur and Van Overberghe (2022) report the lower bound 43 <= R(K5-e, K6).
- lemma: The older upper-bound literature surfaced in this run gives R(K5-e, K6) <= 59.
- lemma: The one-edge Ramsey family provides standard monotonicity comparisons with exact smaller cases.
- toy example: The exact value R(J5, J6) = 37 from the 2022 paper is a nearby solved model inside the same literature vein.
- known obstruction: The current interval is wide enough that either endpoint likely needs significant computation, and the final certificate is unlikely to remain compact.
- prior-work stop sentence: The bounded audit for this run found only 43 <= R(K5-e, K6) <= 59.
- recommended first attack: Exploit the newer circulant lower-bound templates while first checking whether upper-bound gluing methods from smaller one-edge cases extend at all.
- paper if solved: The paper would be a standard exact-value note in the one-edge Ramsey family.

## bounded_source_list
- Jan Goedgebeur and Steven Van Overberghe, "New bounds for Ramsey numbers R(Kk-e, Kl-e)" (Discrete Applied Mathematics 307 (2022)), whose abstract reports 43 <= R(K5-e, K6); the 1998 European Journal of Combinatorics upper-bound paper surfaced in bounded search with R(K5-e, K6) <= 59; and bounded exact-statement, alternate-notation, outside-source, and recent-status web checks on 2026-04-14 that did not surface a later exact value.
- Goedgebeur-Van Overberghe 2022, a 1998 upper-bound source surfaced by exact-statement search, and bounded 2026-04-14 exact-term, alternate-notation, outside-source, and recent-status checks.
- artifacts/r-k5e-k6-almost-clique-ramsey/record.md
- artifacts/r-k5e-k6-almost-clique-ramsey/status.json
