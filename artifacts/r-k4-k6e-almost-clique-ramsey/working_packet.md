# Working Packet: The Exact Value of R(K4, K6-e)

- slug: `r-k4-k6e-almost-clique-ramsey`
- title: Determine the exact value of R(K4, K6-e)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `72`
- single-solve-to-paper fraction: `0.74`

## statement
Determine the least n such that every red-blue coloring of K_n contains either a red K_4 or a blue K_6-e.

## novelty_notes
- frontier basis: The 2021 SDP paper leaves this almost-clique Ramsey number at 30 <= R(K4, K6-e) <= 32, so the family anchor is strong but the interval is wider than the best one-step candidates.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A clean exact solve would still deliver most of a short paper because the main theorem is already identifiable and the literature context is standard. The extra residue is that a three-value gap may require a longer argument or a more elaborate certificate.
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
- assessment: Lowest-ranked eligible slot. The family is standard and the theorem slice is stable, but the three-value interval makes the final packet less compact than the higher one-step or two-point entries.

## likely_paper_shape
- note title: The Exact Value of R(K4, K6-e)
- hypothetical title: The Exact Value of R(K4, K6-e)
- paper shape: A short exact-value note in the almost-complete two-color Ramsey table, with a slightly wider gap than the top queue slots.
- publication if solved: An exact determination of R(K4, K6-e) would likely still support a short note because the family is standard and the current public interval is only three values wide.
- minimal artifact requirements: Either a 30- or 31-vertex extremal coloring that avoids red K4 and blue K6-e at the correct threshold, or a forcing proof that closes the remaining interval.

## hypothetical_abstract
We determine the Ramsey number R(K4, K6-e). Current public sources place this value in the interval 30 <= R(K4, K6-e) <= 32 after the 2021 semidefinite-programming improvement of the upper bound. Our result closes this remaining finite gap in the two-color almost-clique family.

## single_solve_explanation
This still passes the paper test because an exact closure of a named small Ramsey interval would already be the title theorem. The remaining writing would mainly organize the case analysis or extremal construction. The gap is not as tight as the top queue entries, so the solve-to-paper distance is a bit longer.

## broader_theorem_nonimplication
Standard monotonicity and inclusion relations do not decide the exact endpoint here, and the bounded audit did not locate a broader theorem forcing the interval to collapse.

## literature_gap
Current public sources stop at 30 <= R(K4, K6-e) <= 32.

## transfer_kit
- lemma: Lidicky-Pfender 2021, Theorem 7, gives the upper bound R(K4, K6-e) <= 32.
- lemma: The same theorem table records the known lower bound R(K4, K6-e) >= 30 from prior literature.
- lemma: Inclusion K6-e subset K6 gives a classical comparison bound from the complete-graph side without deciding the exact value.
- lemma: The Dynamic Survey places this problem in the standard K_m versus K_n-e tables, giving ready-made surrounding context for a short note.
- toy example: The current lower side is already witnessed by a 30-vertex coloring avoiding a red K4 and a blue K6-e.
- known obstruction: Blue K6-e is dense enough that local neighborhood arguments can become delicate, while red K4 avoidance still permits many near-critical configurations.
- prior-work stop sentence: Current sources stop at 30 <= R(K4, K6-e) <= 32.
- recommended first attack: Push the 2021 SDP inequalities into a neighborhood classification argument and see whether the 30-vertex lower-bound templates can survive one or two extension steps.
- paper if solved: The paper would be a short exact-value note extending the current almost-clique Ramsey tables.

## bounded_source_list
- Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM Journal on Discrete Mathematics 35(4) (2021)), Theorem 7, together with Radziszowski's 2024 Dynamic Survey family context and bounded exact-notation, source-internal, outside-source, and recent-status checks through 2026-04-14.
- Lidicky-Pfender 2021, Radziszowski's Dynamic Survey, and bounded 2026-04-14 exact-notation, source-internal, outside-source, and recent-status checks.
- artifacts/r-k4-k6e-almost-clique-ramsey/record.md
- artifacts/r-k4-k6e-almost-clique-ramsey/status.json
