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
Package the refined F25(13) C-block gain into the theorem-slice writeup, then run Γ(Z_13 × Z_13 × Z_2) as the next decisive zero-slack p = 13 pressure test.

## theorem_slice_target
Checked reusable theorem-slice reductions for the zero-divisor campaign: `zp_z25_support_template_reduction` for the four-class family and `zp_zp_z2_support_template_reduction_of_singleton_one`, factored through `three_interface_pack_lemma`, for the six-class family after setting C = 1.

## fallback_target
If the arithmetic corollaries do not close, preserve the honest theorem-slice plus template-obstruction results: the old upper-half-prime-only C program on Γ(Z_p × Z_25) fails at p = 13, and any failure at Γ(Z_13 × Z_13 × Z_2) should be recorded as a failure of the current smooth-reservoir template rather than of graph primality itself.

## next_blocker
The checked Lean reductions are still abstract support-template theorems rather than family-specific support decompositions from the ring law, and the six-class p = 13 feeder Γ(Z_13 × Z_13 × Z_2) still has to decide whether the current arithmetic story is a real theorem slice or only a promising scaffold.

## why_now
The repo already has a cluster of Lean-backed exact instances with repeated support-class decompositions and reusable label roles.

## strongest_honest_claim
The zero-divisor campaign now has paired verified p = 11 feeders on both active lines, a verified p = 13 feeder on the four-class Γ(Z_p × Z_25) line, checked Lean names for the abstract support-template reductions `zp_z25_support_template_reduction` and `zp_zp_z2_support_template_reduction_of_singleton_one`, and checked reusable family lemmas `singleton_one_lemma` and `three_interface_pack_lemma` on the Γ(Z_p × Z_p × Z_2) line. The strongest honest slice is that prime labelability of Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2) reduces to explicit classwise coprimality partitions on tiny support graphs, that the second family's actual support graph A-B, A-C, A-F, B-C, B-E, C-D collapses to the three parameter-sensitive interfaces A-B, A-F, and B-E after setting C = 1, and that the first p = 13 four-class stress test survives once the C block is refined to allow two doubled-prime exceptions into D. What remains is to formalize the actual support decompositions from ring structure and decide the six-class zero-slack feeder Γ(Z_13 × Z_13 × Z_2).

## next_action
formalize_actual_support_decomposition_lemmas_and_family_reduction_statements_then_run_z13_z13_z2

## seed_instances
- z3-z25-prime-zero-divisor-graph
- z5-z25-prime-zero-divisor-graph
- z7-z25-prime-zero-divisor-graph
- z5-z5-z2-prime-zero-divisor-graph
- z5-z5-z3-prime-zero-divisor-graph
- z7-z7-z2-prime-zero-divisor-graph
- z2-power-8-prime-zero-divisor-graph

## next_feeder_instances
- z13-z13-z2-prime-zero-divisor-graph
- z17-z25-prime-zero-divisor-graph
