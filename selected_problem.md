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
Keep `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice` as the closed paper core. The active upgrade target is the direct finite-range `Γ(Z_p × Z_25)` corollary for odd primes `59 <= p <= 97`, using the checked subset-selection theorem `AutoMath.Families.ZeroDivisorF25FrozenWrapper.exists_fixedC0_subset_card_eq_C_size_of_p_le_97` plus one remaining injection / extension theorem into `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`.

## fallback_target
If that finite-range `F25` corollary still does not close, freeze the publication claim at the exact paired support-reduction theorem together with the exact `F2` lead theorem, the checked fixed-window `F25` supply and subset-selection lemmas, and the template boundaries `p = 71` (strict prime-only wording fails) and `p = 101` (the frozen `C0` window ends). Treat `z101`, `z103`, and `z107` only as preserved post-97 evidence, not as paper-headline theorems.

## next_blocker
Package a chosen `(p - 1)` element subset of `fixedC0Finset` as an actual injective `C`-class labeling and extend it to a total label function compatible with `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`.

## why_now
The repo already has a cluster of Lean-backed exact instances with repeated support-class decompositions and reusable label roles.

## strongest_honest_claim
As of 2026-04-12T03:41:09-0400, the strongest honest family claim remains the Lean-checked paired structural theorem `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`. The bounded prior-art audit did not establish rediscovery: Fox-Mooney 2025 still leaves the ambient families `Γ(Z_p × Z_p × Z_q)` and `Γ(Z_p × Z_(q^2))` open as Conjectures 4.3 and 4.4. What is exact here is the reduction slice, not a direct all-primes existence theorem: the `F2` arm closes every zero-product edge once `C = 1` and the interfaces `A-B`, `A-F`, and `B-E` are coprime, while the `F25` arm closes every zero-product edge under the checked high-barrier / complementary-support wrapper hypotheses. The first direct `F25` publication upgrade remains the finite-range `59 <= p <= 97` corollary, still blocked only by the injection / extension packaging from a chosen `(p - 1)` subset of `fixedC0Finset`.

## next_action
Keep the paper headline fixed at the paired support-reduction slice. Next formalize the `C`-class injection / extension package needed for the finite-range `59 <= p <= 97` `F25` corollary, then rerun `publication_audit`; only if that still stalls should feeder work move to `z109-z25-prime-zero-divisor-graph` and `z113-z25-prime-zero-divisor-graph` as post-97 continuation tests.

## seed_instances
- z3-z25-prime-zero-divisor-graph
- z5-z25-prime-zero-divisor-graph
- z7-z25-prime-zero-divisor-graph
- z5-z5-z2-prime-zero-divisor-graph
- z5-z5-z3-prime-zero-divisor-graph
- z7-z7-z2-prime-zero-divisor-graph
- z2-power-8-prime-zero-divisor-graph

## next_feeder_instances
- z109-z25-prime-zero-divisor-graph
- z113-z25-prime-zero-divisor-graph
