# Determine the exact value of R(B8, B10)

- entry_type: `paper_candidate`
- slug: `r-b8-b10-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g); William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), abstract-level status check; and bounded exact-term, canonical-source, outside-source, and recent-status web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Closing the one-gap case R(B8, B10) would already read as the title theorem of a short note on almost-diagonal book Ramsey numbers.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `76`
- single_solve_to_paper_fraction: `0.76`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
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
- working_packet_path: `artifacts/r-b8-b10-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on an almost-diagonal book Ramsey residue.`

## question
Is R(B8, B10) = 37 or 38?

## canonical_statement
Determine the exact value of R(B8, B10).

## intended_statement
Either prove that every graph on 37 vertices contains B8 or its complement contains B10 and thus show R(B8, B10) = 37, or construct a 37-vertex graph avoiding B8 whose complement avoids B10 and thus show R(B8, B10) = 38.

## pre_solve_gate_reason
The thin-memory sweep found no prior attempt on this exact pair, the 2025 book-Ramsey paper gives the lower bound 37 <= R(B8, B10), DS1.17 Section 5.3(g) still yields the upper bound R(B8, B10) <= 38, and the bounded 2026-04-13 exact-term and outside-source checks did not surface a later exact determination.

## micro_paper_assessment
Pass. This is a fresh one-gap exact-value residue with a strong family anchor, a cheap novelty audit, and a short-note packet if solved.

## hypothetical_title
The Exact Value of R(B8, B10)

## hypothetical_abstract
We determine the book Ramsey number R(B8, B10). Existing work leaves this almost-diagonal case in the one-gap window 37 <= R(B8, B10) <= 38. Our result closes a natural residue in the recent book-Ramsey program around the almost-diagonal family R(B_{n-2}, B_n).

## single_solve_paper_explanation
The exact value is already the honest title theorem, and the surrounding literature has done most of the setup. A successful solve would leave only the proof or explicit witness, a compact comparison with neighboring solved book pairs, and a short remark on the boundary of the known family theorems. That is comfortably inside the 70-90% micro-paper band.

## broader_theorem_nonimplication_note
Known exact families settle R(B_{n-1}, B_n) and many diagonal cases, but they do not settle R(B_{n-2}, B_n) for n = 10. The recent 2026 follow-up advertises infinite-family progress only for the second case, so the B8/B10 slice is not already forced by a broader published theorem.

## literature_gap
Current public sources support only the one-gap window 37 <= R(B8, B10) <= 38, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## publication_packet_title
The Exact Value of R(B8, B10)

## publication_packet_frontier_basis
The 2025 book-Ramsey paper implies the current lower bound 37 <= R(B8, B10) through its almost-diagonal theorem, while the older Rousseau-Sheehan upper-bound mechanism recorded in DS1.17 still gives R(B8, B10) <= 38. The sampled 2026 Wesley follow-up advertises new lower bounds for several book pairs and an infinite-family result for R(B_{n-1}, B_n), but it does not advertise an exact resolution of R(B8, B10).

## publication_packet_near_paper_reason
This is already a canonical one-gap residue inside a named exact-value program. After a solve, the note would mainly need the extremal witness or forcing proof, a short comparison with the adjacent exact case R(B9, B10) = 39, and a brief comment on why the known infinite-family theorems stop short of B8 versus B10.

## publication_packet_literature_scope
Lidicky-McKinley-Pfender-Van Overberghe 2025, DS1.17 Section 5.3(g), Wesley 2026 abstract-level status check, and bounded 2026-04-13 exact-term, canonical-source, outside-source, and recent-status searches for R(B8, B10).

## publication_packet_artifact_requirements
Either a proof that every 37-vertex graph forces B8 or a complement B10, or one explicit 37-vertex witness graph showing the threshold is 38.

## paper_shape
A one-theorem exact-value note on an almost-diagonal book Ramsey residue.

## transfer_kit

### usable_lemmas
- Theorem 1 of the 2025 book-Ramsey paper gives the lower bound 37 <= R(B8, B10).
- DS1.17 Section 5.3(g) gives the generic upper bound R(Bm, Bn) <= 2(m + n + 1); for (m, n) = (8, 10) this is R(B8, B10) <= 38.
- The same 2025 paper proves the neighboring exact value R(B9, B10) = 39, which gives a local benchmark one step closer to the diagonal.

### toy_example
The exact case R(B9, B10) = 39 is the nearest solved almost-diagonal example showing how the 4n - 1 line behaves one notch above the target.

### known_obstruction
A proof of 37 must eliminate every 37-vertex critical graph allowed by the current lower bound, while a proof of 38 needs a single 37-vertex graph avoiding B8 with complement avoiding B10.

### prior_work_stop_sentence
Current sources stop at the one-gap window 37 <= R(B8, B10) <= 38.

### recommended_first_attack
Exploit the 2025 lower-bound construction paradigm and test whether any 37-vertex extension survives the B8 and complement-B10 constraints, using SAT modulo symmetries or tightly pruned block-circulant search only as a certificate generator after a structural setup.

### paper_if_solved
The paper would be a short exact-value note closing an almost-diagonal book Ramsey residue.
