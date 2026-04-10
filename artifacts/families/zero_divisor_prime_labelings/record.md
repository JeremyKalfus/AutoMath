# Family Record: zero_divisor_prime_labelings

## family_statement_lock

- Active `family_slug`: `zero_divisor_prime_labelings`.
- Active dossier path: `campaigns/zero_divisor_prime_labelings.md`.
- Active family artifact path: `artifacts/families/zero_divisor_prime_labelings`.
- Locked family statements for this pass:
  - `F25(p) := Γ(Z_p × Z_25)` for odd prime `p`.
  - `F2(p) := Γ(Z_p × Z_p × Z_2)` for odd prime `p`.
- Locked theorem target for this generalize pass:
  - keep `zp_zp_z2_three_interface_lead_theorem` as the exact publication spine on the full ring family `F2(p)`;
  - treat the `F25` line as companion structural evidence until a quantified bounded-spill arithmetic theorem and a ring-level wrapper theorem are closed.
- Local files read in this pass:
  - `AGENTS.md`
  - `selected_problem.md`
  - `campaigns/zero_divisor_prime_labelings.md`
  - `artifacts/families/zero_divisor_prime_labelings/record.md`
  - `artifacts/families/zero_divisor_prime_labelings/status.json`
  - `PROOFS.md`
  - `artifacts/z5-z25-prime-zero-divisor-graph/record.md`
  - `artifacts/z13-z25-prime-zero-divisor-graph/record.md`
  - `artifacts/z17-z25-prime-zero-divisor-graph/record.md`
  - `artifacts/z5-z5-z2-prime-zero-divisor-graph/record.md`
  - `artifacts/z13-z13-z2-prime-zero-divisor-graph/record.md`
  - `lean/AutoMath/Families/ZeroDivisorRingBridges.lean`
  - `lean/AutoMath/Families/ZeroDivisorReductions.lean`
- Seed artifact count opened in this pass: `5`.
- Local search only: yes.
- Web usage in this pass: none.

## existing_instance_inventory

- Lean-backed exact baseline from `PROOFS.md`:
  - `F25(3)`, `F25(5)`, `F25(7)`.
  - `F2(5)`, `F2(7)`.
- Opened feeder records that materially drive this pass:
  - `F25(5)` supplies the stable four-class support graph on the actual ring:
    support classes `A,B,C,D` with exact edge families `A-C`, `B-B`, `B-C`, `B-D`.
  - `F25(13)` is the first honest failure of the old upper-half-only `C` rule:
    `|C| = 12`, but the upper half of `{1,...,84}` contributes only `10` primes, so the repair uses the spill primes `37,41` and sends their doubles `74,82` to `D`.
  - `F25(17)` shows that the same repair is not merely a `p = 13` patch:
    `|C| = 16`, the upper half of `{1,...,104}` contributes only `12` primes, and the spill extends to `37,41,43,47` with doubles `74,82,86,94` moved to `D`.
  - `F2(5)` supplies the clean six-class hinge reduction:
    once the singleton class `C` gets label `1`, the only live arithmetic interfaces are `A-B`, `A-F`, and `B-E`.
  - `F2(13)` is the first zero-slack six-class feeder:
    the nontrivial `{2,3}`-smooth labels up to `193` are exactly `24`, matching `|A ∪ E| = 24`.
- Lean-backed family facts read in this pass:
  - `f25_ring_support_partition_lemma`
  - `f25_ring_support_adjacency_lemma`
  - `f2_ring_support_partition_lemma`
  - `f2_ring_support_adjacency_lemma`
  - `f2_ring_nonhinge_edge_reduction`
  - `f2_ring_three_interface_reduction`
  - `zp_zp_z2_three_interface_lead_theorem`
  - `singleton_one_lemma`
  - `three_interface_pack_lemma`
- Inventory verdict:
  - the `F2` line already has one exact Lean-backed theorem slice on the full ring family;
  - the `F25` line already has an exact ring-to-support bridge, but it still lacks the quantified arithmetic package needed to promote the four-class line to a second theorem slice.

## shared_structure

- Common decomposition / invariant:
  - zero-product adjacency is controlled by support patterns in the coordinates, so each family graph is a blowup of a tiny support graph;
  - vertices inside one support class have identical neighborhoods, so once a class label set is fixed, any bijection inside that class preserves all adjacency constraints.
- Common decomposition / construction:
  1. classify each nonzero zero-divisor by support type;
  2. prove the support-class adjacency table from the ring law;
  3. transport the full graph to a classwise coprimality problem;
  4. solve only the remaining arithmetic interfaces.
- `F25(p)` support graph:
  - support classes `A,B,C,D` with sizes `20,4,p-1,4(p-1)`;
  - exact edge families `A-C`, `B-B`, `B-C`, `B-D`;
  - role split:
    `B` is a sparse clique barrier,
    `C` is the prime block whose factors must stay out of `A ∪ B`,
    `D` is constrained only against `B`.
- `F2(p)` support graph:
  - support classes `A,B,C,D,E,F` with sizes `p-1,p-1,1,(p-1)^2,p-1,p-1`;
  - exact edge families `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`;
  - role split:
    `C` is the hinge singleton,
    `C = 1` makes `A-C`, `B-C`, and `C-D` automatic,
    `D` becomes free,
    and the arithmetic core collapses to `A-B`, `A-F`, and `B-E`.
- Shared proof template extracted from the seeds:
  - ring-to-support bridge first;
  - support-graph reduction second;
  - interval arithmetic only last.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  - the support-class partitions for both families;
  - the support-class adjacency bridges on the actual ring families;
  - the reduction from the full graph to a bounded list of interface checks;
  - on the `F2` line, the hinge move `C = 1` and the exact reduction to `A-B`, `A-F`, and `B-E`;
  - on the `F2` line, the structural corollary `f2_ring_nonhinge_edge_reduction`, which isolates all non-hinge edges into the three live interfaces.
- Steps that plausibly scale but are not yet closed as family lemmas:
  - on the `F25` line, keeping a fixed sparse barrier set on `B`;
  - on the `F25` line, allowing a bounded spill subset of below-half primes in `C` whose nontrivial multiples land in `D` rather than `A ∪ B`;
  - on the `F25` line, proving that the spill from `B` plus the doubled spill from `C` always fits inside the fixed `20`-slot reservoir `A`;
  - on the `F2` line, turning the structural reduction into a stronger arithmetic corollary beyond the exact reduction theorem.
- Steps that remain instance-specific:
  - the explicit spill-prime choices `37,41` for `F25(13)`;
  - the explicit spill-prime choices `37,41,43,47` for `F25(17)`;
  - the repeated barrier choice `B = {1,19,23,29}` on the inspected `F25` feeders;
  - the exact zero-slack `{2,3}`-smooth split used at `F2(13)`.
- Strongest plausible theorem slice:
  - the full ring-level three-interface reduction for `F2(p)` after fixing `C = 1`.
- Smallest likely counterexample or obstruction:
  - there is still no preserved graph-level counterexample for either active family;
  - the smallest closed obstruction is template-level, not graph-level:
    the old subtemplate “all `C` labels lie above half the interval” fails first at `F25(13)`;
  - the smallest likely next obstructions to the open arithmetic extensions are
    `z19-z25-prime-zero-divisor-graph` on the four-class line and
    `z17-z17-z2-prime-zero-divisor-graph` on the six-class arithmetic-broadening line.

## candidate_theorem_slices

- Slice A: exact ring-level three-interface reduction on `F2(p)`.
  - For odd prime `p`, once the singleton support class `C` in `Γ(Z_p × Z_p × Z_2)` is labeled `1`, every zero-product edge between nonzero zero-divisor vertices is discharged by checking only `A-B`, `A-F`, and `B-E`.
- Slice B: exact ring-level support bridge on `F25(p)`.
  - For odd prime `p`, every nonzero zero-divisor in `Γ(Z_p × Z_25)` lands in exactly one of `A,B,C,D`, and zero product occurs exactly on the support pairs `A-C`, `B-B`, `B-C`, `B-D`.
- Slice C: refined four-class sufficient-condition theorem.
  - For odd prime `p`, `Γ(Z_p × Z_25)` is prime whenever the interval `{1,...,5p+19}` admits class sets of sizes `20,4,p-1,4(p-1)` with:
    `B` pairwise coprime,
    `D` cross-coprime to `B`,
    and every nontrivial multiple of a `C` prime kept out of `A ∪ B`;
    the inspected feeders show the honest version must allow a bounded spill subset of below-half `C` primes.
- Slice D: first-template-failure theorem on the companion line.
  - The old upper-half-prime-only `C` rule fails first at `p = 13`, even though the graph-level prime-labeling program survives after refinement.
- Slice E: arithmetic corollary on the six-class line.
  - Try to turn the `F2(13)` zero-slack witness into a bounded-range theorem for a fixed smooth-prime support set, but no quantified supply lemma is closed yet.

## chosen_slice

- Strongest honest slice: Slice A.
- Proposed theorem slice:
  - for odd prime `p`, the full ring family `Γ(Z_p × Z_p × Z_2)` admits an exact reduction to the three interfaces `A-B`, `A-F`, and `B-E` once the singleton class `C` is fixed to label `1`;
  - this is the ring-level theorem `zp_zp_z2_three_interface_lead_theorem`, not merely an abstract support-graph observation.
- Why this is the strongest honest slice:
  - the full ring-level bridge is closed in Lean on the `F2` line;
  - the proof uses only the genuinely scalable part of the family structure;
  - it avoids overclaiming on the still-open arithmetic supply problems;
  - the companion `F25` line is structurally exact, but its quantified bounded-spill arithmetic has not yet been promoted to a theorem.
- Strongest plausible next slice:
  - a refined `F25` sufficient-condition theorem with a fixed sparse barrier on `B` and an explicit bounded spill rule for the `C` block.

## reusable_lemmas

- Reusable abstract support lemmas already available:
  - `support_decomposition_F25`
  - `support_decomposition_F2`
  - `classwise_template_lemma`
  - `zp_z25_support_template_reduction`
  - `zp_zp_z2_support_template_reduction_of_singleton_one`
- Reusable family lemmas already closed on the `F2` side:
  - `singleton_one_lemma`
  - `three_interface_pack_lemma`
  - `f2_ring_support_partition_lemma`
  - `f2_ring_support_adjacency_lemma`
  - `f2_ring_nonhinge_edge_reduction`
  - `f2_ring_three_interface_reduction`
  - `zp_zp_z2_three_interface_lead_theorem`
- Reusable structural lemmas already closed on the `F25` side:
  - `f25_ring_support_partition_lemma`
  - `f25_ring_support_adjacency_lemma`
- Reusable lemmas still needed for the next companion closure:
  - a quantified `F25` spill-budget lemma for the `C` block;
  - a fixed-barrier reservoir lemma showing that the `B` spill plus the doubled `C` spill still fits inside `A`;
  - a ring-level wrapper theorem converting those arithmetic hypotheses into a clean family theorem on `Γ(Z_p × Z_25)`.

## proof_plan

Main proof path:

1. State the publication spine on the full ring family `F2(p)`, not on a quotient support graph.
2. Use `f2_ring_support_partition_lemma` to place every nonzero zero-divisor into exactly one of `A,B,C,D,E,F`.
3. Use `f2_ring_support_adjacency_lemma` to identify the only zero-product support interfaces.
4. Use `f2_ring_nonhinge_edge_reduction` to show that every zero-product edge avoiding the hinge singleton `C` already lies on `A-B`, `A-F`, or `B-E`.
5. Use `singleton_one_lemma` to discharge every edge touching `C` once `C` is fixed to label `1`.
6. Package Steps 4 and 5 through `f2_ring_three_interface_reduction` or directly through `zp_zp_z2_three_interface_lead_theorem`.
7. Use the exact feeders `F2(5)`, `F2(7)`, and `F2(13)` only as realization evidence for the theorem slice, not as substitutes for the theorem.

Fallback path:

1. If a second theorem unit is needed before the companion arithmetic closes, state the exact `F25` ring bridge itself as a structural theorem:
   every nonzero zero-divisor lies in exactly one of `A,B,C,D`, and every zero-product edge lies on `A-C`, `B-B`, `B-C`, or `B-D`.
2. Pair that structural theorem with the smallest honest obstruction to the old arithmetic program:
   the upper-half-only `C` rule fails first at `p = 13`.
3. Treat the verified `p = 17` feeder as continuation evidence for the refined spill template, not as a quantified theorem.
4. Do not claim an all-odd-primes `F25` prime-labeling theorem until the spill-budget and reservoir lemmas are written explicitly.

## fallback_counterexample_plan

- There is still no preserved graph-level counterexample for either active family.
- The current honest obstruction theorem is arithmetic-template level:
  - on the `F25` line, the old upper-half-prime-only `C` subtemplate fails first at `p = 13`;
  - on the `F2` line, the next likely arithmetic obstruction to broadening the current story is `z17-z17-z2-prime-zero-divisor-graph`, where the naive `{2,3}`-smooth reservoir should no longer have slack.
- Smallest likely counterexample or obstruction for the next pass:
  - `z19-z25-prime-zero-divisor-graph` for the current open bounded-spill `F25` arithmetic package;
  - `z17-z17-z2-prime-zero-divisor-graph` for any naive attempt to extend the `F2` arithmetic story without refining the support-prime reservoir.
- Counterexample handling rule:
  - if either feeder fails, record it as a counterexample to the arithmetic template under test, not to graph primality unless an actual non-prime witness is found.

## next_best_feeder_instances

- `z19-z25-prime-zero-divisor-graph`
  - smallest next four-class discriminator after the verified `F25(17)` continuation;
  - maximally tests whether the bounded-spill `C` template keeps scaling once the structural bridge is already fixed.
- `z17-z17-z2-prime-zero-divisor-graph`
  - smallest next six-class discriminator after the zero-slack `F2(13)` feeder;
  - maximally distinguishes between “the support-prime set must enlarge beyond `{2,3}`” and “the current six-class arithmetic can still be repaired without changing the structural theorem”.
- Feeder verdict for this pass:
  - no new feeder is required to justify the chosen exact slice itself;
  - the next feeders are only for discriminating the two open arithmetic extensions.

## publication_value

- Proposed theorem slice from this pass:
  - the exact ring-level three-interface reduction `zp_zp_z2_three_interface_lead_theorem` for `Γ(Z_p × Z_p × Z_2)`.
- Best generalized companion template still open:
  - an `F25` bounded-spill sufficient-condition theorem in which the `C` block may use a bounded number of below-half primes, provided their nontrivial multiples stay out of `A ∪ B` and the barrier spill from `B` still fits inside `A`.
- One strongest path forward:
  - keep the publication spine on the exact `F2` slice and close the quantified bounded-spill lemmas on the `F25` side so the companion line becomes a second theorem unit.
- One fallback path:
  - publish one-sided on the exact `F2` theorem slice and use the `F25` line only as exact structural evidence plus honest breakpoint analysis at `p = 13` and `p = 17`.
- Honest publication verdict:
  - `publication_status = SLICE_EXACT`;
  - not `PAPER_READY`, because the campaign still lacks a second closed family-level ingredient on the `F25` line.
