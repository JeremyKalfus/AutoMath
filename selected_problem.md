# Zero-divisor prime labelings family campaign

- entry_type: `family_campaign`
- slug: `family-zero_divisor_prime_labelings`
- family_slug: `zero_divisor_prime_labelings`
- family_name: `Prime labelings of zero-divisor graph families`
- campaign_priority: `1`
- dossier_path: `campaigns/zero_divisor_prime_labelings.md`
- artifact_dir: `artifacts/families/zero_divisor_prime_labelings`
- publication_status: `SLICE_CANDIDATE`

## family_statement
Work from the active campaign dossier at `campaigns/zero_divisor_prime_labelings.md` and the family artifact path `artifacts/families/zero_divisor_prime_labelings`.

## theorem_slice_hint
Start with a support-template theorem for Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2), then pressure-test p = 11 as the next feeder.

## theorem_slice_target
Paired support-template reduction theorems for Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2), with the second family reduced to three coprimality interfaces after fixing the singleton class to label 1.

## fallback_target
A smallest-template-failure obstruction: most likely at Γ(Z_11 × Z_11 × Z_2) for the current F2 smooth-reservoir pattern, or at Γ(Z_13 × Z_25) if the verified F25 template first becomes tight one prime later.

## next_blocker
Package the verified Γ(Z_11 × Z_25) feeder into the family writeup, preserve the completed Lean reduction skeletons, and then test the parallel F2(11) line or the next tight F25(13) line.

## why_now
The repo already has a cluster of Lean-backed exact instances with repeated support-class decompositions and reusable label roles.

## strongest_honest_claim
The strongest honest slice is now a paired support-template reduction program backed by a verified new feeder: for odd prime p, prime labelability of Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2) reduces to explicit classwise coprimality partitions on tiny support graphs, and the Γ(Z_p × Z_25) template has now survived the decisive p = 11 test. The structural reductions are clear from the Lean-backed exact seeds and the verified p = 11 witness; the remaining uncertainty is arithmetic closure for the parallel Γ(Z_p × Z_p × Z_2) line and the next tight Γ(Z_p × Z_25) follow-up at p = 13.

## next_action
promote_verified_f25_p11_into_theorem_slice_writeup_then_run_f2_p11_or_f25_p13

## seed_instances
- z3-z25-prime-zero-divisor-graph
- z5-z25-prime-zero-divisor-graph
- z7-z25-prime-zero-divisor-graph
- z5-z5-z2-prime-zero-divisor-graph
- z5-z5-z3-prime-zero-divisor-graph
- z7-z7-z2-prime-zero-divisor-graph
- z2-power-8-prime-zero-divisor-graph

## next_feeder_instances
- z11-z11-z2-prime-zero-divisor-graph
- z13-z25-prime-zero-divisor-graph
- z13-z13-z2-prime-zero-divisor-graph
