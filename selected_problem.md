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
- publication_status: `SLICE_EXACT`
- campaign_affinity: `zero_divisor_prime_labelings`

## question
Advance the active publication campaign zero_divisor_prime_labelings from its current theorem-slice blocker.

## canonical_statement
Keep `zp_zp_z2_three_interface_lead_theorem` as the one-sided exact publication spine on the actual ring family `Γ(Z_p × Z_p × Z_2)`, and treat `Γ(Z_p × Z_25)` as companion structural evidence until a quantified bounded-spill theorem and ring-level wrapper promote it to a second honest slice.

## intended_statement
For odd prime p, the campaign has one exact Lean-backed ring-level theorem slice on Γ(Z_p × Z_p × Z_2): `f2_ring_support_partition_lemma`, `f2_ring_support_adjacency_lemma`, `f2_ring_nonhinge_edge_reduction`, `f2_ring_three_interface_reduction`, and `zp_zp_z2_three_interface_lead_theorem` show that every non-hinge zero-product edge already lies on A-B, A-F, or B-E, and that once the singleton support class C is fixed to label 1, every zero-product edge between nonzero zero-divisor vertices is discharged by those three interfaces. On the companion family Γ(Z_p × Z_25), the ring-level bridge is exact via `f25_ring_support_partition_lemma` and `f25_ring_support_adjacency_lemma`, but the quantified bounded-spill arithmetic theorem needed to promote that line to a second honest slice is still open.

## theorem_slice_hint
Package the paired p = 13 gains into the theorem-slice writeup, then run Γ(Z_17 × Z_25) as the next four-class stress test while formalizing the missing ring-to-support bridge lemmas.

## theorem_slice_target
Keep `zp_zp_z2_three_interface_lead_theorem` as the one-sided exact publication spine on the actual ring family `Γ(Z_p × Z_p × Z_2)`, and treat `Γ(Z_p × Z_25)` as companion structural evidence until a quantified bounded-spill theorem and ring-level wrapper promote it to a second honest slice.

## fallback_target
If the four-class companion arithmetic does not close quickly, publish strictly on the exact six-class reduction and use the `Γ(Z_p × Z_25)` side as companion evidence consisting of the exact structural bridge, the first failure of the upper-half-only `C` rule at `p = 13`, and the refined spill continuation at `p = 17`.

## next_blocker
No blocker remains on the exact `Γ(Z_p × Z_p × Z_2)` slice. The campaign is blocked on the companion `Γ(Z_p × Z_25)` line: close a quantified bounded-spill `C` lemma, close the barrier-reservoir lemma showing the spill still fits inside `A`, and then package those arithmetic hypotheses into a ring-level wrapper theorem.

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
A Three-Interface Reduction for Prime Labelings of Γ(Z_p × Z_p × Z_2), with Structural Companion Evidence for Γ(Z_p × Z_25)

## strongest_honest_claim
For odd prime p, the campaign has one exact Lean-backed ring-level theorem slice on Γ(Z_p × Z_p × Z_2): `f2_ring_support_partition_lemma`, `f2_ring_support_adjacency_lemma`, `f2_ring_nonhinge_edge_reduction`, `f2_ring_three_interface_reduction`, and `zp_zp_z2_three_interface_lead_theorem` show that every non-hinge zero-product edge already lies on A-B, A-F, or B-E, and that once the singleton support class C is fixed to label 1, every zero-product edge between nonzero zero-divisor vertices is discharged by those three interfaces. On the companion family Γ(Z_p × Z_25), the ring-level bridge is exact via `f25_ring_support_partition_lemma` and `f25_ring_support_adjacency_lemma`, but the quantified bounded-spill arithmetic theorem needed to promote that line to a second honest slice is still open.

## next_action
Use `f2_ring_nonhinge_edge_reduction` plus `singleton_one_lemma` as the paper-facing proof spine for `zp_zp_z2_three_interface_lead_theorem`, then close the quantified bounded-spill `Γ(Z_p × Z_25)` theorem and its ring-level wrapper; use `z19-z25-prime-zero-divisor-graph` and `z17-z17-z2-prime-zero-divisor-graph` only as discriminating feeders.

## seed_instances
- z3-z25-prime-zero-divisor-graph
- z5-z25-prime-zero-divisor-graph
- z7-z25-prime-zero-divisor-graph
- z5-z5-z2-prime-zero-divisor-graph
- z5-z5-z3-prime-zero-divisor-graph
- z7-z7-z2-prime-zero-divisor-graph
- z2-power-8-prime-zero-divisor-graph

## next_feeder_instances
- z19-z25-prime-zero-divisor-graph
- z17-z17-z2-prime-zero-divisor-graph
