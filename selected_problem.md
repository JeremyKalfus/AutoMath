# Zero-divisor prime labelings family campaign

- entry_type: `family_campaign`
- slug: `family-zero_divisor_prime_labelings`
- family_slug: `zero_divisor_prime_labelings`
- family_name: `Prime labelings of zero-divisor graph families`
- canonical_source: `campaigns/zero_divisor_prime_labelings.md`
- open_status_checked_on: `2026-04-10`
- dossier_path: `campaigns/zero_divisor_prime_labelings.md`
- artifact_dir: `artifacts/families/zero_divisor_prime_labelings`
- attack_style: `family campaign`
- curation_confidence: `high`
- publication_status: `SLICE_CANDIDATE`
- campaign_affinity: `zero_divisor_prime_labelings`

## question
Advance the active publication campaign zero_divisor_prime_labelings from its current theorem-slice blocker.

## canonical_statement
Family-level bridge lemmas from the ring law into the checked support-template reductions for Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2), together with the paired verified p = 13 arithmetic checkpoints.

## intended_statement
The zero-divisor campaign now has paired verified p = 13 feeders on both active lines: Γ(Z_13 × Z_25) survives with a refined small-spill C block, and Γ(Z_13 × Z_13 × Z_2) survives the first zero-slack six-class test with the unrefined C = 1 plus {2,3}-smooth template. The Lean surface now also contains checked abstract support assets `support_decomposition_F25`, `support_decomposition_F2`, `classwise_template_lemma`, `zp_z25_support_template_reduction`, and `zp_zp_z2_support_template_reduction_of_singleton_one`. The main remaining gap is no longer whether the paired p = 13 frontier survives, but whether the actual ring-to-support bridge lemmas can be formalized cleanly enough to turn this feeder cluster into a paper-ready family theorem slice.

## theorem_slice_hint
Package the paired p = 13 gains into the theorem-slice writeup, then run Γ(Z_17 × Z_25) as the next four-class stress test while formalizing the missing ring-to-support bridge lemmas.

## theorem_slice_target
Family-level bridge lemmas from the ring law into the checked support-template reductions for Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2), together with the paired verified p = 13 arithmetic checkpoints.

## fallback_target
If the arithmetic corollaries do not yet close, preserve the structural slice plus the paired p = 13 arithmetic statement rather than overclaiming a full odd-prime theorem.

## next_blocker
The campaign still needs the actual ring-to-support bridge lemmas that connect the new Lean support module to the family rings themselves, and it still needs one post-p = 13 stress test on the refined four-class line to see how much p-range language is honest.

## why_reasoning_friendly
The repo already has a cluster of Lean-backed exact instances with repeated support-class decompositions and reusable label roles.

## why_low_token
The dossier, family record, and exact inventory already exist locally.

## verifier_hint
Use publication audit to test whether the current claim is really theorem-shaped rather than another instance.

## lean_hint
Prefer reusable family lemmas or theorem-slice reductions over another isolated exact formalization.

## rediscovery_risk
low-medium

## why_still_appears_open
The family artifact still records a live blocker rather than a closed publication-grade theorem.

## why_this_could_be_publishable
Support-template reductions and paired p = 13 feeders in two zero-divisor prime-labeling families

## strongest_honest_claim
The zero-divisor campaign now has paired verified p = 13 feeders on both active lines: Γ(Z_13 × Z_25) survives with a refined small-spill C block, and Γ(Z_13 × Z_13 × Z_2) survives the first zero-slack six-class test with the unrefined C = 1 plus {2,3}-smooth template. The Lean surface now also contains checked abstract support assets `support_decomposition_F25`, `support_decomposition_F2`, `classwise_template_lemma`, `zp_z25_support_template_reduction`, and `zp_zp_z2_support_template_reduction_of_singleton_one`. The main remaining gap is no longer whether the paired p = 13 frontier survives, but whether the actual ring-to-support bridge lemmas can be formalized cleanly enough to turn this feeder cluster into a paper-ready family theorem slice.

## next_action
formalize_ring_to_support_bridge_lemmas_then_run_z17_z25

## seed_instances
- z3-z25-prime-zero-divisor-graph
- z5-z25-prime-zero-divisor-graph
- z7-z25-prime-zero-divisor-graph
- z5-z5-z2-prime-zero-divisor-graph
- z5-z5-z3-prime-zero-divisor-graph
- z7-z7-z2-prime-zero-divisor-graph
- z2-power-8-prime-zero-divisor-graph

## next_feeder_instances
- z17-z25-prime-zero-divisor-graph
