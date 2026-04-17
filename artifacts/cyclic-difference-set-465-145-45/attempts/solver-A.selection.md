# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-465-145-45`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 1 listing the two remaining open cyclic cases with k <= 150; status rechecked against Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), Table 2.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle one of the two residual cyclic difference-set cases left open by Baumert-Gordon for k <= 150 and still listed as open in Gordon-Schmidt's 2015 status table.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `tiny`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `88`
- single_solve_to_paper_fraction: `0.84`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `moderate`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-465-145-45/working_packet.md`
- paper_shape: `A short cyclic-difference-set note whose title theorem is exactly the resolution of the (465,145,45) case.`

## question
Does the cyclic group of order 465 admit a (465,145,45)-difference set?

## canonical_statement
Determine whether the cyclic group C_465 admits a (465,145,45)-difference set.

## intended_statement
Determine whether the cyclic group C_465 admits a (465,145,45)-difference set.

## pre_solve_gate_reason
The case is source-anchored, explicitly residual, still surfaced as open in a later status survey, and solving it would already read like the title theorem of a short note.

## micro_paper_assessment
Lane-eligible. This is a small, stable, source-anchored residual theorem whose exact resolution would itself be the paper.

## hypothetical_title
On Cyclic (465,145,45) Difference Sets

## hypothetical_abstract
We determine whether the cyclic group of order 465 admits a (465,145,45)-difference set. Baumert and Gordon left this parameter among the final two open cyclic cases with k <= 150, and Gordon and Schmidt still listed it as open in their 2015 multiplier survey. The result therefore closes a canonical residual case in the small-parameter cyclic difference-set literature with only light contextual packaging.

## single_solve_paper_explanation
The literature already isolates this tuple as a named residual case, so an exact proof would supply essentially all of the mathematics of the paper. What remains after the solve is bounded exposition: restate the old elimination pipeline, explain why those tests stop at 465, and present the decisive new argument. That is comfortably inside the 70-90% micro-paper band.

## broader_theorem_nonimplication_note
The 2004 paper eliminates four of the six k <= 150 cyclic survivors using the standard Schutzenberger, BRC, Yamamoto, Lander, Mann, and cyclotomic filters, yet leaves (465,145,45) open; the 2015 survey still records [465] as open, so no broader published theorem surfaced in this audit that already settles the exact cyclic case.

## literature_gap
Prior work stops at listing C_465 with parameters (465,145,45) as an unresolved cyclic difference-set case in Baumert-Gordon 2004 and Gordon-Schmidt 2015.

## publication_packet_title
The Cyclic (465,145,45) Difference-Set Problem

## publication_packet_frontier_basis
Baumert-Gordon 2004 leaves (465,145,45) as one of only two open cyclic cases with k <= 150, and Gordon-Schmidt 2015 still lists [465] among the smallest open difference-set parameters.

## publication_packet_near_paper_reason
One exact solution would remove a canonical residual case with cheap rediscovery surface and would need only a short introduction explaining the prior necessary-condition pipeline.

## publication_packet_literature_scope
Baumert-Gordon 2004 for the residual source table and standard cyclic tests; Gordon-Schmidt 2015 for later open-status confirmation and multiplier-theorem context; the La Jolla Difference Set Repository only as a status cross-check surface.

## publication_packet_artifact_requirements
A human-checkable existence construction in C_465 or a compact nonexistence proof using multiplier, orbit, or cyclotomic congruence arguments, together with a brief audit that the standard published tests did not already exclude the case.

## paper_shape
A short cyclic-difference-set note whose title theorem is exactly the resolution of the (465,145,45) case.

## transfer_kit

### usable_lemmas
- For any difference set, the parameter identity (v - 1)lambda = k(k - 1) fixes the tuple and prevents silent statement drift.
- Baumert-Gordon 2004 use the standard cyclic necessary-condition package: Schutzenberger, Bruck-Chowla-Ryser, Yamamoto, Mann, and Lander-style tests.
- Their Section 3 records the contracted-coefficient equations for theta[w](x), giving the sum, square-sum, and correlation constraints for any divisor w of v.
- Gordon-Schmidt 2015 organize multiplier-theorem tools for residual open cases and identify the relevant prime divisors of n that a successful proof would likely have to force as multipliers or obstruct as nonmultipliers.

### toy_example
Use the classical cyclic (7,3,1)-difference set in C_7 to illustrate how a cyclic difference set is encoded by a short polynomial theta(x) and then reduced modulo divisors w of v.

### known_obstruction
The standard published small-parameter filters already failed to eliminate (465,145,45), so any final proof must go beyond the stock table-building tests.

### prior_work_stop_sentence
Baumert and Gordon leave (465,145,45) open in Table 1, and Gordon-Schmidt still list [465] as open in Table 2 of their 2015 survey.

### recommended_first_attack
Try to force a new multiplier in C_465 from the prime divisors of n = 100, then run the contracted-multiplier orbit equations at a divisor w of 465 to show that no admissible coefficient vector can exist.

### paper_if_solved
If solved exactly, the paper would be a short note settling one of the last tiny cyclic small-parameter cases that survived the classical necessary-condition program.
