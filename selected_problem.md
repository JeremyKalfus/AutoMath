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
Package the paired p = 13 gains into the theorem-slice writeup, then run Γ(Z_17 × Z_25) as the next four-class stress test while formalizing the missing ring-to-support bridge lemmas.

## theorem_slice_target
Formalize the actual ring-level support partition and adjacency lemmas for Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2), then package the preserved abstract support-template reductions as the main theorem slice and present the paired verified p = 13 feeders as arithmetic checkpoints rather than a closed all-primes theorem.

## fallback_target
If the bridge lemmas close but the arithmetic still does not scale cleanly, preserve the structural reduction slice together with the paired p = 13 checkpoints and isolate the smallest broken arithmetic subtemplate instead of claiming a full family theorem.

## next_blocker
The main blocker is still the missing family-specific ring-to-support bridge lemmas; after that, the next publication-pressure arithmetic blocker is whether the refined four-class small-spill C program survives the first post-p = 13 stress test at Γ(Z_17 × Z_25).

## why_now
The repo already has a cluster of Lean-backed exact instances with repeated support-class decompositions and reusable label roles.

## strongest_honest_claim
The strongest honest publication-facing claim is a paired theorem-slice candidate, not a full family theorem: once the actual ring-to-support partition and adjacency lemmas are formalized, the preserved abstract support reductions on disk turn Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2) into tiny coprimality allocation problems. The paired verified p = 13 feeders show the slice is still alive on both lines, but they also show the arithmetic is not fully closed: Γ(Z_13 × Z_25) needs the refined small-spill C block, while Γ(Z_13 × Z_13 × Z_2) survives exactly at the first zero-slack boundary of the naive six-class template.

## next_action
formalize_f25_and_f2_ring_to_support_bridge_lemmas_then_run_z17_z25

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
- z17-z17-z2-prime-zero-divisor-graph
