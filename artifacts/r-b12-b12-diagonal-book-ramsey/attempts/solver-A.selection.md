# Determine the exact value of R(B12, B12)

- entry_type: `paper_candidate`
- slug: `r-b12-b12-diagonal-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 49 <= R(B12, B12) <= 50; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), used as a bounded recent-status and citation check that did not report an exact closure for B12; and bounded 2026-04-14 exact-statement and alternate-notation web checks that did not reveal a later exact determination.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B12, B12) would read as the title theorem of a short note because the public frontier is already a one-step diagonal book Ramsey gap.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `82`
- single_solve_to_paper_fraction: `0.8`
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
- working_packet_path: `artifacts/r-b12-b12-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a diagonal book Ramsey number.`

## question
Is R(B12, B12) equal to 49 or 50?

## canonical_statement
Determine the exact value of R(B12, B12).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B12.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this exact tuple, slug, or title. The bounded audit recovered the 49-50 interval from Lemma 1, checked alternate notation and recent-status sources, and did not surface a later exact closure.

## micro_paper_assessment
Pass. This is a clean one-step diagonal book Ramsey gap with a strong family anchor, low editorial residue, and no detected broader theorem that already collapses the endpoint.

## hypothetical_title
The Exact Value of R(B12, B12)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B12, B12). Previous work placed this number in the interval 49 <= R(B12, B12) <= 50. Our result closes the remaining one-step gap for a standard diagonal book pair.

## single_solve_paper_explanation
This target passes the 70-90% paper test because the public frontier is already one endpoint wide in a named classical family. Once the exact value is known, the note mostly needs the extremal coloring or forcing argument and a short comparison with nearby exact book values. There is no feeder ladder between the solve and the paper-shaped claim.

## broader_theorem_nonimplication_note
The currently available broad diagonal-book result only sandwiches R(B_n, B_n) between 4n + 1 and 4n + 2 for 4 <= n <= 21. Exact off-diagonal values such as R(B11, B12) = 47 and smaller diagonal values such as R(B8, B8) = 33 do not force the endpoint for n = 12.

## literature_gap
Current public sources stop at 49 <= R(B12, B12) <= 50.

## publication_packet_title
The Exact Value of R(B12, B12)

## publication_packet_frontier_basis
Current public sources leave the diagonal book Ramsey number at 49 <= R(B12, B12) <= 50. That is already a one-step finite frontier in a standard family with exact neighboring book values and explicit lower-bound constructions.

## publication_packet_near_paper_reason
If the endpoint 49 versus 50 is settled, the note already has its title theorem, the core literature comparison, and a compact frontier claim. What remains is mainly the extremal coloring or forcing proof, plus a brief comparison with nearby diagonal and almost-diagonal book values.

## publication_packet_literature_scope
2025 EJC paper Lemma 1 for the one-step interval and nearby exact values, 2026 Wesley book-Ramsey lower-bound paper as a recent-status check, and bounded 2026-04-14 exact-statement, synonym, and citation searches.

## publication_packet_artifact_requirements
Either an explicit 49-vertex coloring avoiding monochromatic B12 or a compact proof that every 50-vertex coloring forces B12.

## paper_shape
A one-theorem exact-value note for a diagonal book Ramsey number.

## transfer_kit

### usable_lemmas
- Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 49 <= R(B12, B12) <= 50.
- The same lemma gives the exact neighboring almost-diagonal value R(B11, B12) = 47.
- The same paper records the exact smaller diagonal benchmark R(B8, B8) = 33.
- Wesley (2026) gives recent lower-bound progress and exact lower constructions for nearby diagonal book cases, but does not report an exact closure for B12.

### toy_example
The exact neighboring diagonal case R(B8, B8) = 33 is a direct model for how a short diagonal-book exact-value note can look.

### known_obstruction
Diagonal book critical graphs can remain highly structured and polycirculant, so any upper-bound proof must eliminate the last 49-vertex critical family without expanding into a broader campaign.

### prior_work_stop_sentence
Current sources stop at 49 <= R(B12, B12) <= 50.

### recommended_first_attack
Start from the Lemma 1 lower-bound construction at order 49 and test whether every one-vertex extension forces a monochromatic B12, while tracking common-neighborhood restrictions along candidate spine edges.

### paper_if_solved
The paper would be a short exact-value note settling one diagonal book Ramsey number.
