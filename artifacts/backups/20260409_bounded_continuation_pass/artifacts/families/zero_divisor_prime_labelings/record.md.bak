# Family Record: zero_divisor_prime_labelings

## family_statement_lock

- Active family slug: `zero_divisor_prime_labelings`.
- Active dossier: [campaigns/zero_divisor_prime_labelings.md](/Users/jeremykalfus/CodingProjects/AutoMath/campaigns/zero_divisor_prime_labelings.md).
- Family artifact path: [artifacts/families/zero_divisor_prime_labelings](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/families/zero_divisor_prime_labelings).
- Locked family statements for this pass:
  - `F25(p) := Γ(Z_p × Z_25)` for odd prime `p`, with vertex count `5p + 19`.
  - `F2(p) := Γ(Z_p × Z_p × Z_2)` for odd prime `p`, with vertex count `p^2 + 2p - 2`.
- Locked theorem target for this generalize pass:
  - paired support-template reduction theorems, not an all-odd-prime closure;
  - `F25(p)` reduced to four classwise label blocks `A,B,C,D`;
  - `F2(p)` reduced on the actual support graph `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`, with the edges touching `C` discharged automatically once the singleton class gets label `1`.
- The strongest honest current theorem target is therefore:
  - a reduction theorem for `F25(p)` on a four-class support blowup with one clique class `B`;
  - a reduction theorem for `F2(p)` on a six-class support blowup where only `A-B`, `A-F`, and `B-E` remain parameter-sensitive after setting `C = 1`.

## existing_instance_inventory

- Lean-backed exact seeds preserved in [PROOFS.md](/Users/jeremykalfus/CodingProjects/AutoMath/PROOFS.md):
  - `z3-z25-prime-zero-divisor-graph`: exact `F25(3)`.
  - `z5-z25-prime-zero-divisor-graph`: exact `F25(5)`.
  - `z7-z25-prime-zero-divisor-graph`: exact `F25(7)`.
  - `z5-z5-z2-prime-zero-divisor-graph`: exact `F2(5)`.
  - `z7-z7-z2-prime-zero-divisor-graph`: exact `F2(7)`.
- Verified non-Lean feeder evidence beyond `PROOFS.md`:
  - `z11-z25-prime-zero-divisor-graph`: verified `F25(11)`.
  - `z11-z11-z2-prime-zero-divisor-graph`: verified `F2(11)`.
- Exact inventory for `F25(p)`:
  - every seed uses the same four support roles
    `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, `|A| = 20`,
    `B = {(0,5),(0,10),(0,15),(0,20)}`, `|B| = 4`,
    `C = {(a,0) : a ∈ Z_p^×}`, `|C| = p - 1`,
    `D = {(a,5t) : a ∈ Z_p^×, t ∈ {1,2,3,4}}`, `|D| = 4(p - 1)`.
  - the `p = 3` record uses the names `N,M,U,W`, but it is the same template with `N = A`, `M = B`, `U = C`, `W = D`.
  - every seed has the same exact edge pattern:
    `A-C`, `B-B`, `B-C`, `B-D`, and no other edges.
  - repeated arithmetic pattern across `p = 5,7,11`:
    `C` gets a large-prime block,
    `B` gets a four-label pairwise-coprime barrier set,
    the bad multiples forced by `B` are dumped into `A`,
    and `D` gets the residual complement.
  - the verified `p = 11` feeder is the first decisive unsolved odd prime on this line and preserves the same proof shape with
    `C = {37,41,43,47,53,59,61,67,71,73}`,
    `B = {1,19,23,29}`,
    and the five extra barrier multiples `{38,46,57,58,69}` absorbed into `A`.
- Exact inventory for `F2(p)`:
  - every seed uses the same six support classes
    `A = (*,0,0)`,
    `B = (0,*,0)`,
    `C = (0,0,1)`,
    `D = (*,*,0)`,
    `E = (*,0,1)`,
    `F = (0,*,1)`.
  - multiplicities are
    `|A| = |B| = |E| = |F| = p - 1`,
    `|C| = 1`,
    `|D| = (p - 1)^2`.
  - every seed has the same exact edge pattern:
    `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`, and no other edges.
  - `F2(5)` uses `C = 1`, powers of `2` on `A`, odd `{3,5}`-smooth labels on `B`, labels avoiding `3,5` on `E`, and odd labels on `F`.
  - `F2(7)` and verified `F2(11)` use the cleaner shared pattern:
    `C = 1`,
    a `{2,3}`-smooth reservoir for `A ∪ E`,
    and labels coprime to `6` for `B ∪ F`.
- Inventory conclusion:
  - both active family lines have now survived the campaign-designated `p = 11` feeder;
  - the structural burden is settled enough for a family theorem slice;
  - the live uncertainty has moved to the first `p = 13` arithmetic redesign, not to the support decompositions themselves.

## shared_structure

- Common decomposition / invariant:
  - in both families, adjacency depends only on support type, so the zero-divisor graph is a blowup of a tiny support graph with parameter-dependent class sizes;
  - vertices inside one support class have identical neighborhoods, so any bijection within a class preserves adjacency and all coprimality obligations.
- Common decomposition / construction:
  - first classify the nonzero zero-divisors by coordinate support;
  - then replace the graph by a partition of the label interval into classwise blocks of the correct sizes;
  - then check only adjacent class pairs and any clique classes.
- `F25(p)` support graph:
  - `A` and `D` are independent;
  - `B` is the unique clique class;
  - `C` only sees `A ∪ B`;
  - `D` only sees `B`.
- `F2(p)` support graph:
  - actual edges are `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`;
  - `C` is the unique hinge vertex;
  - once `C` gets label `1`, the edges `A-C`, `B-C`, and `C-D` are automatic, `D` becomes completely free, and only the three genuinely constrained interfaces `A-B`, `A-F`, and `B-E` remain.
- Shared proof template:
  - support blowup lemma;
  - classwise partition lemma;
  - family-specific reduction to a tiny support graph;
  - arithmetic only after the structural reduction is fixed.
- Formal note preserved in this pass:
  - the local Lean singleton-one reduction theorem for `F2(p)` was corrected so the theorem statement now includes the actual `A-C` and `B-C` edge families instead of silently dropping them.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameter:
  - the support decompositions for `F25(p)` and `F2(p)`;
  - the classwise-template principle that only support classes matter once the partition is fixed;
  - the `F25(p)` reduction to the obligations `B-B`, `A-C`, `B-C`, and `B-D`;
  - the `F2(p)` hinge reduction `C = 1`, after which only `A-B`, `A-F`, and `B-E` remain arithmetic.
- Steps that are still instance-specific in the current seeds:
  - the exact prime lists used for the `C` block in `F25(5)`, `F25(7)`, and `F25(11)`;
  - the exact four-label barrier sets used on `B` in those `F25` seeds;
  - the precise partitions of the smooth reservoir between `A` and `E` in the `F2` seeds;
  - the exact coprime-to-`6` lists used on `B ∪ F` in `F2(7)` and `F2(11)`.
- Parameter-sensitive arithmetic facts now visible from the seeds:
  - `F25(11)` closes with the strict upper-half-prime strategy on `C`, because `|C| = 10` and the interval `[37,74]` already supplies `10` primes.
  - `F25(13)` is the first guaranteed obstruction to that unchanged subtemplate: `|C| = 12`, but `[43,84]` contains only `10` primes, so the pure "all `C` labels above half the interval" trick cannot survive unchanged.
  - `F2(11)` closes with a `{2,3}`-smooth reservoir because there are `21` nontrivial `{2,3}`-smooth labels up to `141`, while `|A ∪ E| = 20`.
  - `F2(13)` is the first tight smooth-reservoir test, not a proved failure: there are exactly `24` nontrivial `{2,3}`-smooth labels up to `193`, matching the required `|A ∪ E| = 24`.
- Smallest likely obstruction:
  - not an actual graph counterexample yet;
  - instead, the first honest obstruction is the failure of the unchanged `F25` upper-half-prime `C` subtemplate at `p = 13`;
  - on the `F2` side, `p = 13` is the first zero-slack arithmetic test for the naive `{2,3}`-smooth program.

## candidate_theorem_slices

- Slice 1: paired structural reduction theorems.
  - For odd prime `p`, `F25(p)` is prime whenever `{1,...,5p+19}` can be partitioned into `L_A,L_B,L_C,L_D` of sizes `20,4,p-1,4(p-1)` such that `L_B` is pairwise coprime, every element of `L_C` is coprime to every element of `L_A ∪ L_B`, and every element of `L_D` is coprime to every element of `L_B`.
  - For odd prime `p`, `F2(p)` is prime whenever `{1,...,p^2+2p-2}` can be partitioned into `L_A,L_B,{1},L_D,L_E,L_F` of sizes `p-1,p-1,1,(p-1)^2,p-1,p-1` such that every `L_A-L_B`, `L_A-L_F`, and `L_B-L_E` pair is coprime.
- Slice 2: `F25(p)` arithmetic sufficient-condition theorem.
  - If one can choose a `C` block of size `p - 1` with very small spill into `A ∪ B`, and a four-label pairwise-coprime barrier set `B` whose extra multiples occupy at most the `20` `A` slots, then `F25(p)` is prime.
  - This mechanism is now verified at `p = 11`.
- Slice 3: `F2(p)` arithmetic sufficient-condition theorem.
  - If one can choose a fixed small prime-support set `S`, place `2(p - 1)` nontrivial `S`-smooth labels on `A ∪ E`, place `2(p - 1)` labels coprime to every prime in `S` on `B ∪ F`, and set `C = 1`, then `F2(p)` is prime.
  - This mechanism is realized by `S = {2,3}` at `p = 7` and `p = 11`.
- Slice 4: smallest-template-obstruction theorem.
  - The unchanged `F25` upper-half-prime `C` strategy cannot extend to `p = 13`, because the interval `[43,84]` has only `10` primes while `|C| = 12`.
  - This would be a theorem about the current arithmetic subtemplate, not about non-primality of `Γ(Z_13 × Z_25)`.

## chosen_slice

- Strongest honest slice for this pass:
  - the paired structural reduction theorems in Slice 1.
- Why this is the right choice:
  - the proof is structural and now supported by five Lean-backed exact seeds plus verified `p = 11` feeders on both family lines;
  - it is stronger than a pile of exact examples because it packages the reusable family mechanism;
  - it does not require an unproved prime-counting theorem or an unproved smooth-counting asymptotic.
- Strongest arithmetic upgrade now honestly supported:
  - `F25(11)` shows the four-class arithmetic template survives its first decisive odd prime;
  - `F2(11)` shows the six-class smooth-reservoir template also survives its decisive odd prime;
  - the next real campaign frontier is therefore the paired `p = 13` step, where `F25` needs a refined `C` block and `F2` becomes exactly tight.
- Honest publication verdict:
  - stronger than `INSTANCE_ONLY`;
  - not yet a closed family theorem;
  - still `publication_status = SLICE_CANDIDATE`.

## reusable_lemmas

- Preserved structural lemmas:
  - `support_decomposition_F25`: classify `F25(p)` into `A,B,C,D` and prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`.
  - `classwise_template_lemma`: for a support blowup graph, any partition by classes works once every adjacent class pair is cross-coprime and every clique class is internally pairwise coprime.
  - `pairwise_coprime_clique_lemma`: the `B` class in `F25(p)` only needs four pairwise-coprime labels, independent of `p`.
  - `support_decomposition_F2`: classify `F2(p)` into `A,B,C,D,E,F` and prove the exact edge pattern `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`.
  - `singleton_one_lemma`: if the hinge class `C` gets label `1`, then every edge touching `C` is automatic and the entire `D` class becomes free.
  - `three_interface_pack_lemma`: after `C = 1` in `F2(p)`, only `A-B`, `A-F`, and `B-E` remain arithmetic.
- Next arithmetic lemmas worth isolating:
  - `large_prime_block_with_small_spill_lemma`: choose `p - 1` `C` labels for `F25(p)` while leaving enough labels for `A ∪ B`.
  - `sparse_barrier_set_lemma`: choose four pairwise-coprime `B` labels whose nontrivial multiples spill into at most `20` `A` slots.
  - `smooth_reservoir_count_lemma`: count `S`-smooth labels in `{1,...,p^2+2p-2}` sharply enough for `F2(p)`.
  - `coprime_complement_pack_lemma`: choose `B ∪ F` from labels avoiding the prime support used on `A ∪ E`.

## proof_plan

- Main proof path:
  1. Preserve the corrected structural reduction theorems for `F25(p)` and `F2(p)` as the family-level backbone.
  2. Package the classwise-template lemma once, then instantiate it separately for the four-class and six-class support graphs.
  3. Promote `z11-z25` and `z11-z11-z2` only as arithmetic witness instantiations of those reduction theorems, not as the theorem proof itself.
  4. Isolate two arithmetic corollaries, one for the `F25` large-prime-plus-barrier program and one for the `F2` smooth-reservoir-plus-coprime-complement program.
  5. Pressure-test both arithmetic corollaries at `p = 13`.
- One strongest path forward:
  - formalize the paired structural slice in Lean first, then test `z13-z25-prime-zero-divisor-graph` and `z13-z13-z2-prime-zero-divisor-graph` as the first post-`p = 11` arithmetic discriminators.
- One fallback path:
  - if the arithmetic side still does not close at `p = 13`, preserve the first exact failure of the current subtemplate as a theorem about the arithmetic program rather than claiming graph non-primality.

## fallback_counterexample_plan

- The likely fallback theorem is not "the graph is not prime."
- `F25` fallback:
  - preserve the first-template-obstruction theorem that the unchanged upper-half-prime `C` program already fails at `p = 13`;
  - if a refined `C` block with a few doubled primes rescues `F25(13)`, preserve that refinement explicitly rather than pretending the original subtemplate survived.
- `F2` fallback:
  - test whether the naive `{2,3}`-smooth program can be packed exactly at `p = 13`;
  - if it fails, preserve that as the smallest failure of the naive smooth-reservoir template, not as a non-primality claim for `Γ(Z_13 × Z_13 × Z_2)`.
- What to preserve if a feeder fails:
  - the corrected structural reduction theorem;
  - the exact arithmetic subtemplate being tested;
  - the minimal counting or divisibility obstruction;
  - the distinction between template failure and graph failure.

## next_best_feeder_instances

- `z13-z25-prime-zero-divisor-graph`
  - first arithmetic discriminator because the old upper-half-prime `C` block cannot survive unchanged there.
- `z13-z13-z2-prime-zero-divisor-graph`
  - first tight six-class discriminator because the naive `{2,3}`-smooth reservoir has zero slack there.

## publication_value

- The campaign is now materially stronger than a loose family slogan:
  - five Lean-backed exact seeds already preserve the structural backbone;
  - verified `F25(11)` and verified `F2(11)` show both active family lines survive the first decisive unsolved odd prime;
  - the next theorem-slice question is sharply localized at `p = 13`.
- The strongest honest publication value is:
  - a corrected paired support-template reduction program;
  - two verified `p = 11` campaign feeders, one on each family line;
  - an explicit first arithmetic obstruction for the unchanged `F25` subtemplate;
  - an explicit first zero-slack arithmetic test for the naive `F2` subtemplate.
- Honest current publication verdict:
  - not `PAPER_READY`;
  - not merely `INSTANCE_ONLY`;
  - correctly `publication_status = SLICE_CANDIDATE`.

## lean_statement

- Current Lean target for this pass:
  - a reusable family-supporting lemma, not a new exact instance.
- Exact theorem statement added to the official Lean backend:
  - `AutoMath.Families.ZeroDivisorReductions.singleton_one_lemma`
  - For predicates `A,B,C,D : V → Prop` and a label map `label : V → Nat`, if every vertex in the hinge class `C` has label `1`, then every edge of type `A-C`, `B-C`, or `C-D` is automatically labeled by a coprime pair.
- Honest scope:
  - this formalizes the reusable "edges touching `C` are automatic" step on the `F2(p)` line;
  - it does not yet formalize the full support decomposition from actual zero-divisors of `Z_p × Z_p × Z_2`.

## lean_skeleton

- Proof skeleton used:
  1. State the six edge families touching `C`: `A-C`, `C-A`, `B-C`, `C-B`, `C-D`, `D-C`.
  2. Case-split on that finite disjunction.
  3. In each branch, rewrite the relevant `C`-label to `1` using `hC1`.
  4. Discharge the coprimality goal by `simp`.
- Reason this is the right Lean target:
  - it is the smallest reusable lemma explicitly named by the family record;
  - it strengthens the checked family surface without pretending the full paired slice is already formalized from ring data.

## lean_result

- Lean file updated:
  - `lean/AutoMath/Families/ZeroDivisorReductions.lean`
- Mirrored family Lean file preserved under the family artifact after the check:
  - `artifacts/families/zero_divisor_prime_labelings/lean/AutoMath/Families/ZeroDivisorReductions.lean`
- Check run:
  - `lake build AutoMath.Families.ZeroDivisorReductions`
- Result:
  - the targeted family module checked successfully with the new `singleton_one_lemma`.
- Honest Lean verdict for the campaign after this pass:
  - the family now has a checked reusable singleton-one lemma on the official Lean surface;
  - the broader paired theorem slice remains structurally correct but not yet connected all the way to formal support decompositions of the actual zero-divisor families.

## lean_blockers

- Remaining blockers before the paired theorem slice can honestly be marked Lean-complete:
  - no checked support-decomposition lemma yet derives the `F25(p)` and `F2(p)` support graphs directly from the actual zero-divisor families;
  - the current theorem-slice wrappers still live at the abstract support-template level;
  - the next arithmetic frontier remains the paired `p = 13` audit, especially the refined `F25(13)` `C` block and the zero-slack `F2(13)` smooth-reservoir test.
