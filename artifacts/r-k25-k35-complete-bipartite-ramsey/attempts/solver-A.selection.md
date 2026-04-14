# Determine the exact value of R(K2,5, K3,5)

- entry_type: `paper_candidate`
- slug: `r-k25-k35-complete-bipartite-ramsey`
- worker_role: `solver-A`
- canonical_source: `Mohammad Ghebleh, Salem Al-Yakoob, Ali Kanso, and Dragan Stevanovic, "Reinforcement learning for graph theory, II. Small Ramsey numbers" (The Art of Discrete and Applied Mathematics 8(1) (2025)), abstract giving R(K_{2,5}, K_{3,5}) >= 22; together with Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 7, giving R(K3,5, K2,5) <= 23; and bounded 2026-04-14 recent-status web checks that did not reveal a later exact determination.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(K2,5, K3,5) would read as the title theorem of a short note because the public frontier is already a one-step mixed complete-bipartite Ramsey gap.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.84`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-k25-k35-complete-bipartite-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note closing a one-step mixed bipartite Ramsey gap.`

## question
Is R(K2,5, K3,5) equal to 22 or 23?

## canonical_statement
Determine the exact value of R(K2,5, K3,5).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains either a red K2,5 or a blue K3,5.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this exact tuple, reversed tuple, slug, or title. The bounded curation audit recovered the 2025 lower bound 22 and the 2021 upper bound 23, and it did not surface a later exact closure.

## micro_paper_assessment
Pass. This is the cleanest untouched one-step graph Ramsey gap found in the bounded curation pass, and one exact solve would already account for most of a short publishable note.

## hypothetical_title
The Exact Value of R(K2,5, K3,5)

## hypothetical_abstract
We determine the two-color Ramsey number R(K2,5, K3,5). Previous work left this number in the interval 22 <= R(K2,5, K3,5) <= 23. Our result closes the remaining one-step gap for this mixed complete-bipartite pair.

## single_solve_paper_explanation
This target cleanly passes the 70-90% paper test because the public frontier is already one endpoint wide. Once the exact value is known, the note is mostly a short extremal construction or forcing proof together with a minimal literature comparison. There is no feeder ladder between the solve and the paper-shaped claim.

## broader_theorem_nonimplication_note
Known exact results for neighboring bipartite pairs such as R(K3,4, K3,4) and R(K3,5, K3,5) do not force the mixed pair R(K2,5, K3,5). The bounded audit did not uncover a broader theorem that collapses the 22 versus 23 endpoint automatically.

## literature_gap
Current public sources stop at 22 <= R(K2,5, K3,5) <= 23.

## publication_packet_title
The Exact Value of R(K2,5, K3,5)

## publication_packet_frontier_basis
Current public sources leave this mixed complete-bipartite Ramsey number at 22 <= R(K2,5, K3,5) <= 23. That is already a one-step finite frontier after the 2025 lower-bound improvement and the 2021 SDP upper bound.

## publication_packet_near_paper_reason
If the endpoint 22 versus 23 is settled, the note already has its title theorem, main comparison with prior work, and exact frontier claim. What remains is mainly a compact critical coloring or a short forcing argument, plus a brief placement beside the nearby exact bipartite cases.

## publication_packet_literature_scope
2025 Ghebleh-Al-Yakoob-Kanso-Stevanovic abstract-level lower-bound source, 2021 Lidicky-Pfender Theorem 7 for the upper bound, nearby exact bipartite Ramsey values from the 2022 bounds paper, and bounded 2026-04-14 recent-status web checks.

## publication_packet_artifact_requirements
Either an explicit 22-vertex coloring avoiding red K2,5 and blue K3,5, or a compact proof that every 23-vertex coloring forces one of them.

## paper_shape
A one-theorem exact-value note closing a one-step mixed bipartite Ramsey gap.

## transfer_kit

### usable_lemmas
- Ghebleh et al. (2025) provide the current lower bound R(K2,5, K3,5) >= 22.
- By symmetry of two-color Ramsey numbers, Lidicky-Pfender (2021), Theorem 7, gives the upper bound R(K2,5, K3,5) = R(K3,5, K2,5) <= 23.
- The 2022 small-Ramsey bounds paper records the exact neighboring value R(K3,4, K3,4) = 25, giving a nearby solved model in the same complete-bipartite corridor.
- The same 2022 paper records the exact neighboring value R(K3,5, K3,5) = 33, showing the family is publication-legible through exact finite endpoint papers.

### toy_example
The exact case R(K3,4, K3,4) = 25 is the nearest solved mixed-bipartite benchmark for how a finite exact-value note in this family can look.

### known_obstruction
A lower-bound coloring can stay dense while suppressing K2,5 in one color and K3,5 in the other, so any upper-bound proof must rule out the last 22-vertex critical configuration family without drifting into a broad census.

### prior_work_stop_sentence
Current sources stop at 22 <= R(K2,5, K3,5) <= 23.

### recommended_first_attack
Start from the 2025 lower-bound construction and test whether every extension by one new vertex forces either a red K2,5 or a blue K3,5, while tracking degree-pattern restrictions suggested by the 2021 SDP upper bound.

### paper_if_solved
The paper would be a short exact-value note closing a one-step mixed complete-bipartite Ramsey gap.
