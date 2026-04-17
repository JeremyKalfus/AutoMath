# Untitled Entry

- entry_type: `paper_candidate`
- slug: `r-b15-b15-diagonal-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Lemma 1, together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026, 114913).`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `An exact determination of R(B15, B15) would still read as the title theorem of a short note because the public frontier is already a one-step diagonal book Ramsey gap.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `76`
- single_solve_to_paper_fraction: `0.75`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `moderate`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/r-b15-b15-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a larger diagonal book Ramsey number.`

## question
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 15-page book graph B15.

## canonical_statement
Determine the exact value of R(B15, B15).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 15-page book graph B15.

## pre_solve_gate_reason
This remains a one-gap exact-value target in a standardized family, and a solution would still be the honest title theorem with only modest certificate-size risk.

## micro_paper_assessment
Eligible but slightly weaker than the smaller one-step cases. The family anchor remains strong and the gap is one step, though the larger order modestly increases certificate and packaging risk.

## hypothetical_title
The Exact Value of R(B15, B15)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B15, B15). Previous work placed this number in the interval 61 <= R(B15, B15) <= 62. Our result closes the remaining one-step gap for a larger diagonal book pair.

## single_solve_paper_explanation
This target still passes the paper test because the public frontier is a one-step exact-value problem in a standard family. After the solve, the note mainly needs the main witness or forcing proof and a concise literature comparison. The only downgrade versus the top slot is a modest risk that the larger order produces a slightly bulkier certificate.

## broader_theorem_nonimplication_note
Known diagonal-book results still only provide the generic one-step interval, and the recent 2026 lower-bound paper does not settle n = 15. Exact neighboring cases such as R(B14, B15) = 59 do not force the diagonal endpoint.

## literature_gap
Current public sources stop at 61 <= R(B15, B15) <= 62.

## publication_packet_title
The Exact Value of R(B15, B15)

## publication_packet_frontier_basis
Current public sources leave the diagonal book Ramsey number at 61 <= R(B15, B15) <= 62, so the remaining frontier is already one endpoint wide.

## publication_packet_near_paper_reason
If the endpoint is settled, the note already has its title theorem, family placement, and main extremal artifact. The residue after the solve is mostly a compact proof write-up rather than additional theorem building.

## publication_packet_literature_scope
Lidický-McKinley-Pfender-Van Overberghe 2025, Wesley 2026, source-internal neighboring exact values, and bounded exact-statement, alternate-notation, outside-source, and recent-status checks through 2026-04-14, plus local 2026-04-15 attempt-registry conflict checks.

## publication_packet_artifact_requirements
Either an explicit 61-vertex coloring avoiding monochromatic B15 or a compact proof that every 62-vertex coloring forces B15.

## paper_shape
A one-theorem exact-value note for a larger diagonal book Ramsey number.

## transfer_kit

### usable_lemmas
- Lidicky-McKinley-Pfender-Van Overberghe 2025, Lemma 1, gives 61 <= R(B15, B15) <= 62.
- The same lemma gives the exact neighboring almost-diagonal value R(B14, B15) = 59.
- Wesley 2026 provides recent diagonal and almost-diagonal lower-bound constructions that confirm ongoing frontier activity in the family.
- The same 2025 paper records exact smaller diagonal benchmarks such as R(B8, B8) = 33.

### toy_example
The exact neighboring almost-diagonal case R(B14, B15) = 59 is the nearest solved model for a compact write-up in the same corridor.

### known_obstruction
At this order, symmetric lower-bound colorings may still be numerous, so the main risk is a larger family of critical 61-vertex constructions rather than theorem-scope drift.

### prior_work_stop_sentence
Current sources stop at 61 <= R(B15, B15) <= 62.

### recommended_first_attack
Start from the 4n + 1 diagonal lower-bound template at order 61 and combine common-neighborhood counting with symmetry reduction to test whether any 62-vertex extension can avoid a monochromatic B15.

### paper_if_solved
The paper would be a short exact-value note settling a larger diagonal book Ramsey number.
