# Zero-divisor prime labelings family campaign

- entry_type: `family_campaign`
- slug: `family-zero_divisor_prime_labelings`
- family_slug: `zero_divisor_prime_labelings`
- family_name: `Prime labelings of zero-divisor graph families`
- campaign_priority: `1`
- dossier_path: `campaigns/zero_divisor_prime_labelings.md`
- artifact_dir: `artifacts/families/zero_divisor_prime_labelings`
- publication_status: `SLICE_EXACT`

## family_statement
Work from the active campaign dossier at `campaigns/zero_divisor_prime_labelings.md` and the family artifact path `artifacts/families/zero_divisor_prime_labelings`.

## theorem_slice_hint
Package the paired p = 13 gains into the theorem-slice writeup, then run Γ(Z_17 × Z_25) as the next four-class stress test while formalizing the missing ring-to-support bridge lemmas.

## theorem_slice_target
Keep `zp_zp_z2_three_interface_lead_theorem` fixed as the exact lead slice and present it only as a ring-level reduction theorem for `Γ(Z_p × Z_p × Z_2)`, with support partition and adjacency reduction as setup and the singleton hinge plus three live interfaces as the theorem.

## fallback_target
Add paper-scale theorem mass on `Γ(Z_p × Z_25)` by closing the quantified bounded-spill plus barrier-reservoir wrapper if possible; otherwise package the first sharp repaired-wrapper obstruction theorem, with `p = 19` as the next discriminator and `p = 23` next if `p = 19` survives.

## next_blocker
The exact `F2` slice is real but not paper-ready on its own. The live blocker is still the four-class `Γ(Z_p × Z_25)` line: despite the preserved bridge lemmas `f25_ring_support_partition_lemma` and `f25_ring_support_adjacency_lemma`, the repo still needs either a quantified small-spill / barrier-reservoir theorem or a first sharp repaired-wrapper obstruction theorem.

## why_now
The repo already has a cluster of Lean-backed exact instances with repeated support-class decompositions and reusable label roles.

## strongest_honest_claim
The strongest honest current family claim is the exact Lean-backed theorem slice `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`: for every odd prime `p`, if the singleton support class `C` in `Γ(Z_p × Z_p × Z_2)` receives label `1` and the three live interfaces `A-B`, `A-F`, and `B-E` are pairwise coprime, then every zero-product edge between nonzero zero-divisor vertices is automatically labeled by coprime integers. This is a real parameterized reduction theorem, but it is not yet a theorem that `Γ(Z_p × Z_p × Z_2)` is prime for all odd `p`.

## next_action
Keep `zp_zp_z2_three_interface_lead_theorem` fixed as the exact publication anchor and do not broaden the headline claim beyond that slice. Move the next family cycle to the `Γ(Z_p × Z_25)` arithmetic wrapper on top of the preserved bridge; if the quantified spill route still does not close cleanly, run `z19-z25-prime-zero-divisor-graph` as the first sharp repaired-wrapper discriminator, then `z23-z25-prime-zero-divisor-graph` if needed.

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
- z23-z25-prime-zero-divisor-graph
