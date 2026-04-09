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
A smallest-template-failure obstruction: most likely at Γ(Z_11 × Z_25) for the current F25 reservoir pattern, or at Γ(Z_13 × Z_13 × Z_2) if the F2 smooth-reservoir template survives p = 11 but becomes tight next.

## next_blocker
Formalize the support-template reductions as reusable Lean-ready family lemmas and then test whether the current arithmetic reservoir templates actually satisfy those hypotheses at p = 11.

## why_now
The repo already has a cluster of Lean-backed exact instances with repeated support-class decompositions and reusable label roles.

## strongest_honest_claim
The strongest honest slice is a paired support-template reduction program: for odd prime p, prime labelability of Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2) reduces to explicit classwise coprimality partitions on tiny support graphs. The structural reductions are clear from the Lean-backed exact seeds; the remaining uncertainty is arithmetic closure, with p = 11 the first decisive feeder and p = 13 the next tight follow-up.

## next_action
formalize_support_template_reduction_lemmas_then_run_p11_feeders_with_p13_tightness_check

## seed_instances
- z3-z25-prime-zero-divisor-graph
- z5-z25-prime-zero-divisor-graph
- z7-z25-prime-zero-divisor-graph
- z5-z5-z2-prime-zero-divisor-graph
- z5-z5-z3-prime-zero-divisor-graph
- z7-z7-z2-prime-zero-divisor-graph
- z2-power-8-prime-zero-divisor-graph

## next_feeder_instances
- z11-z25-prime-zero-divisor-graph
- z11-z11-z2-prime-zero-divisor-graph
- z13-z25-prime-zero-divisor-graph
- z13-z13-z2-prime-zero-divisor-graph
