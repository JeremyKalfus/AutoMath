# Determine the exact value of R(B11, B13)

- entry_type: `paper_candidate`
- slug: `r-b11-b13-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3 items (g)-(h); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), Theorem 2 and appendix benchmarks; and bounded exact-term and alternate-notation web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing R(B11, B13) would already support a compact exact-value note on the unresolved B_{n-2} versus B_n book Ramsey line.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `83`
- single_solve_to_paper_fraction: `0.83`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b11-b13-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the almost-diagonal book Ramsey line.`

## question
Is R(B11, B13) = 49 or 50?

## canonical_statement
Determine the exact value of R(B11, B13).

## intended_statement
Either prove that every graph on 49 vertices contains B11 or its complement contains B13 and thus show R(B11, B13) = 49, or construct a 49-vertex graph avoiding B11 whose complement avoids B13 and thus show R(B11, B13) = 50.

## pre_solve_gate_reason
The thin-memory sweep found no prior attempt on this exact pair. The 2025 book-Ramsey paper gives 49 <= R(B11, B13), DS1.17 item 5.3.g gives R(B11, B13) <= 50, Wesley 2026 settles the adjacent line R(B12, B13) = 51 but not this pair, and the bounded exact-term and alternate-notation searches on 2026-04-13 did not surface a later exact closure.

## micro_paper_assessment
Pass. This is a one-gap frontier case with a strong family anchor and a natural exact neighbor, so a single clean solve would already look like a finished short paper.

## hypothetical_title
The Exact Value of R(B11, B13)

## hypothetical_abstract
We determine the book Ramsey number R(B11, B13). Existing public bounds leave this almost-diagonal case in the one-gap window 49 <= R(B11, B13) <= 50. Our result closes a natural unresolved point adjacent to the exact neighboring value R(B12, B13) = 51.

## single_solve_paper_explanation
An exact value for this pair is already the whole point of the paper. The family scaffolding is recent and explicit, so the remaining work after the solve is small: present the proof or witness, compare with the neighboring exact case, and document the frontier gap that just got removed. That keeps the solve-to-paper distance short.

## broader_theorem_nonimplication_note
The exact line R(B_{n-1}, B_n) = 4n - 1 does not imply anything exact for R(B_{n-2}, B_n). For n = 13, the public record still gives only 49 <= R(B11, B13) <= 50.

## literature_gap
Current public sources support only 49 <= R(B11, B13) <= 50, and the bounded 2026-04-13 exact-term and alternate-notation audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B11, B13)

## publication_packet_frontier_basis
Current public sources leave this pair in the one-gap window 49 <= R(B11, B13) <= 50. The lower bound is explicitly covered by the 2025 theorem, the upper bound still comes from DS1.17 item 5.3.g, and the most recent 2026 book-Ramsey paper closes the adjacent B12 versus B13 case rather than this one.

## publication_packet_near_paper_reason
The write-up after a successful solve is short and standard: exact statement, forcing proof or extremal graph, one comparison with the solved R(B12, B13) benchmark, and a brief discussion of why the broader almost-diagonal line remains open. That is enough for a clean note.

## publication_packet_literature_scope
DS1.17 Section 5.3, Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Wesley 2026 Theorem 2 and appendix benchmarks, plus bounded exact-term and alternate-notation web searches on 2026-04-13.

## publication_packet_artifact_requirements
Either a proof that every 49-vertex graph forces B11 or a complement B13, or one explicit 49-vertex witness graph avoiding B11 whose complement avoids B13.

## paper_shape
A one-theorem exact-value note on the almost-diagonal book Ramsey line.

## transfer_kit

### usable_lemmas
- Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 49 <= R(B11, B13).
- DS1.17 item 5.3.g gives R(B11, B13) <= 2(11 + 13 + 1) = 50.
- DS1.17 item 5.3.e and Wesley 2026 together give the adjacent exact benchmark R(B12, B13) = 51.

### toy_example
The neighboring exact case R(B12, B13) = 51 is a worked benchmark on the same family corridor.

### known_obstruction
A proof of 49 must force B11 against B13 at the threshold, while a proof of 50 needs a 49-vertex witness that extends the current lower-bound template by one more layer.

### prior_work_stop_sentence
Current sources stop at the one-gap window 49 <= R(B11, B13) <= 50.

### recommended_first_attack
Try to extend the 48-vertex almost-diagonal lower-bound constructions from the 2025 repository and treat nonextendability as the first forcing target.

### paper_if_solved
The paper would be a short exact-value note on an unresolved one-gap book Ramsey pair.
