# Determine the exact value of R(K4-e, K4-e, K4-e; 3)

- entry_type: `paper_candidate`
- slug: `r-k4e-k4e-k4e-three-uniform-hypergraph-ramsey`
- worker_role: `solver-A`
- canonical_source: `Bernard Lidicky and Florian Pfender, "Semidefinite Programming and Ramsey Numbers" (SIAM J. Discrete Math. 35(4) (2021)), Theorem 9, which gives 13 <= R(K4-e, K4-e, K4-e; 3) <= 14; together with bounded 2026-04-14 survey and recent-status web checks during curation that did not reveal a later exact determination.`
- open_status_checked_on: `2026-04-14`
- publication_if_solved: `An exact determination of R(K4-e, K4-e, K4-e; 3) would read as the title theorem of a short note because the public frontier is already a one-step 3-uniform hypergraph gap.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `81`
- single_solve_to_paper_fraction: `0.81`
- title_theorem_strength: `strong`
- family_anchor_strength: `moderate`
- publication_narrative_strength: `strong`
- editorial_overhead: `moderate`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-k4e-k4e-k4e-three-uniform-hypergraph-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note closing a one-step 3-uniform missing-edge Ramsey gap.`

## question
Is R(K4-e, K4-e, K4-e; 3) equal to 13 or 14?

## canonical_statement
Determine the exact 3-uniform hypergraph Ramsey number R(K4-e, K4-e, K4-e; 3).

## intended_statement
Determine the least n such that every 3-coloring of the triples of an n-element set contains a monochromatic 3-uniform K4-e in one of the three colors.

## pre_solve_gate_reason
The thin-memory exclusion sweep found no prior AutoMath attempt under this exact hypergraph tuple or title. The bounded curation audit located the 2021 one-step interval and no later exact closure in the capped web pass.

## micro_paper_assessment
Pass. This is the cleanest untouched one-step gap found after the exclusion sweep, and one exact solve would already account for most of a publishable note.

## hypothetical_title
The Exact Value of R(K4-e, K4-e, K4-e; 3)

## hypothetical_abstract
We determine the 3-uniform hypergraph Ramsey number R(K4-e, K4-e, K4-e; 3). Previous work placed this number in the interval 13 <= R(K4-e, K4-e, K4-e; 3) <= 14. Our result closes the remaining one-step gap for the three-color missing-edge K4 family.

## single_solve_paper_explanation
This already has the shape of a short paper because the frontier is a single endpoint. Once the exact value is established, the note mostly writes itself around one extremal construction or one forcing argument. The surrounding context is already small and sharply localized.

## broader_theorem_nonimplication_note
The 2021 paper improves the upper bound but does not subsume this exact endpoint into a broader published theorem. No stronger general theorem surfaced in the bounded audit that would force 13 or 14 automatically.

## literature_gap
Current public sources stop at 13 <= R(K4-e, K4-e, K4-e; 3) <= 14.

## publication_packet_title
The Exact Value of R(K4-e, K4-e, K4-e; 3)

## publication_packet_frontier_basis
Current public sources leave this 3-color 3-uniform Ramsey number at 13 <= R(K4-e, K4-e, K4-e; 3) <= 14. The gap is already one step after the 2021 SDP improvement.

## publication_packet_near_paper_reason
If the endpoint 13 versus 14 is settled, the main theorem, motivation, and frontier comparison are already in place. The remaining work is mainly a compact extremal coloring or forcing proof, plus a short explanation of how it fits next to the nearby exact 3-uniform cases.

## publication_packet_literature_scope
2021 Lidicky-Pfender Theorem 9 for the current bounds, nearby 2021 Theorem 10 as local-method context, and bounded 2026-04-14 survey/recent-status web checks.

## publication_packet_artifact_requirements
Either an explicit 13-vertex 3-coloring of triples avoiding monochromatic K4-e in all colors, or a compact proof that every 3-coloring on 14 vertices forces one.

## paper_shape
A one-theorem exact-value note closing a one-step 3-uniform missing-edge Ramsey gap.

## transfer_kit

### usable_lemmas
- Lidicky-Pfender (2021), Theorem 9, gives the upper bound R(K4-e, K4-e, K4-e; 3) <= 14.
- The same theorem records the lower bound 13 <= R(K4-e, K4-e, K4-e; 3) from earlier literature.
- Lidicky-Pfender (2021), Theorem 10, shows the neighboring exact value R(K4-e, K5; 3) = 12 and provides a local-model template for turning a sharp SDP certificate into an exact finite proof.
- The 2021 paper explicitly frames these as fixed-size hypergraph Ramsey questions accessible to exact finite analysis rather than asymptotic machinery.

### toy_example
The exact neighboring case R(K4-e, K5; 3) = 12 from the same paper is the closest worked example of the intended proof style.

### known_obstruction
Any lower-bound construction must coordinate three colors on triples while suppressing every monochromatic K4-e, and any upper-bound proof must rule out the last 13-vertex critical configuration family.

### prior_work_stop_sentence
Current sources stop at 13 <= R(K4-e, K4-e, K4-e; 3) <= 14.

### recommended_first_attack
Interrogate the sharp 2021 SDP profile for forbidden 6- and 7-vertex traces, then attempt a constrained completion or uniqueness argument on the putative 13-vertex extremals.

### paper_if_solved
The paper would be a short exact-value note closing the remaining one-step gap for the three-color 3-uniform K4-e Ramsey number.
