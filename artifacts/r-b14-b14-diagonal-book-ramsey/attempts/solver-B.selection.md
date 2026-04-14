# Determine the exact value of R(B14, B14)

- entry_type: `paper_candidate`
- slug: `r-b14-b14-diagonal-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), Table 3 giving the diagonal lower bound R(B14, B14) >= 57; together with Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving R(B14, B14) <= 58; and bounded 2026-04-14 exact-statement and alternate-notation web checks that did not reveal a later exact determination.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(B14, B14) would read as the title theorem of a short note because the public frontier is already a one-step diagonal book Ramsey gap.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `81`
- single_solve_to_paper_fraction: `0.79`
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
- working_packet_path: `artifacts/r-b14-b14-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a diagonal book Ramsey number with a fresh recent lower-bound construction.`

## question
Is R(B14, B14) equal to 57 or 58?

## canonical_statement
Determine the exact value of R(B14, B14).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B14.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this exact tuple, slug, or title. The bounded audit recovered the 57-58 interval from the 2026 lower-bound paper and the 2025 Lemma 1 upper bound, and it did not surface a later exact closure.

## micro_paper_assessment
Pass. This is one of the cleanest untouched recent diagonal book gaps because the lower endpoint is freshly constructed and the upper endpoint is already established.

## hypothetical_title
The Exact Value of R(B14, B14)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B14, B14). Previous work left this number in the interval 57 <= R(B14, B14) <= 58. Our result closes the remaining one-step gap for a diagonal book pair with a recent explicit lower-bound construction.

## single_solve_paper_explanation
This target passes the 70-90% paper test because the public frontier is one endpoint wide and the family is already publication-legible. A successful solve would already provide the title theorem, the main literature comparison, and the main artifact. The remaining work is just compact write-up rather than a second theorem campaign.

## broader_theorem_nonimplication_note
The available broad diagonal-book theorem only gives the one-step interval 4n + 1 <= R(B_n, B_n) <= 4n + 2, and the recent 2026 lower-bound paper improves constructions without fixing the diagonal endpoint at n = 14. Nearby exact values such as R(B13, B14) = 55 do not determine R(B14, B14).

## literature_gap
Current public sources stop at 57 <= R(B14, B14) <= 58.

## publication_packet_title
The Exact Value of R(B14, B14)

## publication_packet_frontier_basis
Current public sources leave the diagonal book Ramsey number at 57 <= R(B14, B14) <= 58. The lower endpoint is supported by a recent explicit construction, so the remaining frontier is a clean one-step exact-value problem.

## publication_packet_near_paper_reason
If the endpoint 57 versus 58 is settled, the paper already has its title theorem and its natural literature comparison. What remains is mainly the critical construction or forcing argument and a short placement beside the nearby diagonal and almost-diagonal book values.

## publication_packet_literature_scope
2026 Wesley Table 3 for the lower bound, 2025 EJC Lemma 1 for the upper bound and family context, and bounded 2026-04-14 exact-statement, synonym, and citation searches.

## publication_packet_artifact_requirements
Either an explicit 57-vertex coloring avoiding monochromatic B14 or a compact proof that every 58-vertex coloring forces B14.

## paper_shape
A one-theorem exact-value note for a diagonal book Ramsey number with a fresh recent lower-bound construction.

## transfer_kit

### usable_lemmas
- Wesley (2026), Table 3, gives the explicit lower bound R(B14, B14) >= 57.
- Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives the upper bound R(B14, B14) <= 58.
- The same 2025 lemma gives the exact neighboring almost-diagonal value R(B13, B14) = 55.
- The same family already contains exact smaller diagonal values such as R(B8, B8) = 33.

### toy_example
The exact neighboring almost-diagonal case R(B13, B14) = 55 is the nearest solved benchmark for how the forcing side of the packet can look.

### known_obstruction
Recent lower-bound constructions show that highly structured diagonal critical graphs persist at this size, so any upper-bound proof must eliminate a small but nontrivial family of 57-vertex candidates.

### prior_work_stop_sentence
Current sources stop at 57 <= R(B14, B14) <= 58.

### recommended_first_attack
Use the 2026 block-circulant lower-bound witness as the base critical template and analyze whether any one-vertex extension necessarily creates a monochromatic B14 by common-neighborhood counting on the spine.

### paper_if_solved
The paper would be a short exact-value note settling a recently sharpened diagonal book Ramsey gap.
