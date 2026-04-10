# Family Record: zero_divisor_prime_labelings

## family_statement_lock

- Active family slug: `zero_divisor_prime_labelings`.
- Active dossier: `campaigns/zero_divisor_prime_labelings.md`.
- Family artifact path: `artifacts/families/zero_divisor_prime_labelings`.
- Locked family statements for this pass:
  - `F25(p) := Γ(Z_p × Z_25)` for odd prime `p`, with support classes
    `A,B,C,D` of sizes `20,4,p-1,4(p-1)`.
  - `F2(p) := Γ(Z_p × Z_p × Z_2)` for odd prime `p`, with support classes
    `A,B,C,D,E,F` of sizes `p-1,p-1,1,(p-1)^2,p-1,p-1`.
- Locked theorem target for this generalize pass:
  - paired support-template reduction theorems;
  - for `F25(p)`, reduce prime labelability to classwise coprimality conditions on the four support classes `A,B,C,D`;
  - for `F2(p)`, state the theorem on the actual support graph
    `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`, then reduce it to the three parameter-sensitive interfaces `A-B`, `A-F`, `B-E` after setting `C = 1`.
- Bounded-read set used in this pass:
  - dossier `campaigns/zero_divisor_prime_labelings.md`;
  - current family files `artifacts/families/zero_divisor_prime_labelings/record.md` and `status.json`;
  - `PROOFS.md`;
  - seed artifacts `z5-z25`, `z7-z25`, `z13-z25`, `z5-z5-z2`, `z7-z7-z2`, and `z11-z11-z2`.
- Strongest plausible theorem slice at this stage:
  - structural reductions first;
  - arithmetic corollaries second;
  - no all-odd-prime closure claim yet.

## existing_instance_inventory

- Lean-backed exact family seeds preserved in `PROOFS.md`:
  - `F25(3)`, `F25(5)`, `F25(7)`;
  - `F2(5)`, `F2(7)`.
- Verified feeder evidence preserved in the dossier/current family state:
  - `F25(11)`;
  - `F25(13)`;
  - `F2(11)`.
- `F25(p)` line from the opened seed artifacts:
  - `F25(5)` already uses the full four-class template:
    `C = {11,23,29,31}` as a large-prime block,
    `B = {1,37,41,43}` as a pairwise-coprime barrier,
    `A` absorbing the small forbidden set,
    and `D` receiving the clean complement.
  - `F25(7)` keeps the same proof shape:
    `C` uses six primes above half the interval,
    `B = {1,11,13,17}`,
    and `A` absorbs the eight extra multiples forced by `B`.
  - `F25(13)` preserves the same structural graph but forces the first arithmetic refinement:
    the old upper-half-prime-only `C` subtemplate fails because `[43,84]` has only `10` primes for `12` `C` slots;
    the verified repair is to use `37` and `41` below half and send their doubles `74,82` to `D`,
    while keeping the sparse barrier `B = {1,19,23,29}` and placing its spill labels `38,46,57,58,69,76` into `A`.
- `F2(p)` line from the opened seed artifacts:
  - `F2(5)` already exhibits the hinge move `C = 1`, after which only `A-B`, `A-F`, and `B-E` matter;
    its arithmetic realization uses powers of `2` on `A`, `{3,5}`-smooth odd labels on `B`, labels avoiding `3,5` on `E`, and odd labels on `F`.
  - `F2(7)` shows the cleaner scalable template:
    `C = 1`,
    `A ∪ E` supported on primes `{2,3}`,
    `B` large primes greater than `3`,
    and `F` odd labels avoiding `3`.
  - `F2(11)` is the decisive verified feeder on this line:
    the same `C = 1` reduction survives with `A ∪ E` filled by the `21` nontrivial `{2,3}`-smooth labels up to `141`,
    leaving one spare beyond the required `20`,
    and it records that the naive `{2,3}`-smooth count becomes exactly tight at `p = 13` with `24` available labels for `24` required slots.
  - `F2(13)` is now also a verified feeder on this line:
    the same `C = 1` reduction survives at the first zero-slack boundary,
    with `A ∪ E` using all `24` nontrivial `{2,3}`-smooth labels up to `193`
    and `B ∪ F` packed into a complement block coprime to `6`.
- Inventory conclusion:
  - both active family lines share stable support decompositions and stable proof skeletons;
  - the four-class arithmetic line already survives its first `p = 13` test, but only after a refined small-spill `C` block;
  - the six-class arithmetic line now also survives its first zero-slack test `F2(13)`;
  - the next honest arithmetic discriminator is the first post-`13` four-class stress test `F25(17)`.

## shared_structure

- Common decomposition / invariant:
  - in both families, adjacency depends only on coordinate support, so the full zero-divisor graph is a blowup of a tiny support graph;
  - vertices inside a fixed support class have identical neighborhoods, so any bijection inside a class preserves adjacency and all coprimality obligations.
- Common decomposition / construction:
  - classify the nonzero zero-divisors by support type;
  - prove the exact support-graph edge pattern from the ring law;
  - partition the label interval by support classes;
  - check only adjacent class pairs and any clique class.
- `F25(p)` support graph:
  - exact edge families are `A-C`, `B-B`, `B-C`, `B-D`;
  - `B` is the unique clique class;
  - `C` only constrains `A ∪ B`;
  - `D` only constrains `B`.
- `F2(p)` support graph:
  - exact edge families are `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`;
  - `C` is the unique hinge vertex;
  - once `C = 1`, the edges touching `C` become automatic and the whole `D` class becomes free;
  - only `A-B`, `A-F`, and `B-E` remain parameter-sensitive.
- Shared proof template extracted from the seeds:
  1. prove the support decomposition;
  2. invoke a classwise template lemma for support blowups;
  3. isolate the tiny family-specific support graph;
  4. solve the remaining arithmetic interface problem without search-heavy machinery.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  - the support decompositions `support_decomposition_F25` and `support_decomposition_F2`;
  - the classwise-template principle that only adjacent support classes matter once the partition is fixed;
  - for `F25(p)`, the reduction to three interface obligations plus the `B` clique;
  - for `F2(p)`, the `C = 1` hinge reduction and the three-interface packing problem.
- Parameter-sensitive arithmetic burdens:
  - choose `p - 1` `C` labels for `F25(p)` while keeping every nontrivial multiple of any `C` prime out of `A ∪ B`;
  - choose a four-label pairwise-coprime barrier set on `B` whose extra multiples fit inside the `20` `A` slots;
  - count enough labels for `A ∪ E` in `F2(p)` supported on a fixed small prime set;
  - choose `B ∪ F` as a sufficiently large complement block avoiding that prime support.
- Steps that are still instance-specific in the current evidence:
  - the exact prime lists used on `C` in the finite `F25` witnesses;
  - the exact barrier sets used on `B` in the four-class line;
  - the exact splits of the smooth reservoir between `A` and `E` in the six-class line;
  - the particular doubled-prime exceptions `37,41` used in `F25(13)`.
- Smallest honest obstruction already visible:
  - the unchanged upper-half-prime-only `F25` `C` program fails at `p = 13`;
  - this is a theorem about the old arithmetic subtemplate, not about graph non-primality.
- Smallest likely unresolved obstruction:
  - post-`13` scaling of the refined small-spill `F25` `C` program, because the paired `p = 13` checkpoint is now closed and the next honest question is whether the repaired four-class arithmetic is genuinely stable.

## candidate_theorem_slices

- Slice A: paired structural reductions.
  - For odd prime `p`, `F25(p)` is prime whenever `{1,...,5p+19}` can be partitioned into sets `L_A,L_B,L_C,L_D` of sizes `20,4,p-1,4(p-1)` such that:
    `L_B` is pairwise coprime,
    every label in `L_C` is coprime to every label in `L_A ∪ L_B`,
    and every label in `L_D` is coprime to every label in `L_B`.
  - For odd prime `p`, `F2(p)` is prime whenever `{1,...,p^2+2p-2}` can be partitioned into sets `L_A,L_B,{1},L_D,L_E,L_F` of sizes `p-1,p-1,1,(p-1)^2,p-1,p-1` such that every `L_A-L_B`, `L_A-L_F`, and `L_B-L_E` pair is cross-coprime.
- Slice B: four-class refined arithmetic corollary.
  - A sufficient-condition theorem for `F25(p)` using a size-`p-1` `C` block with bounded below-half exceptions whose nontrivial multiples are sent to `D`, together with a sparse four-label barrier set on `B`.
- Slice C: six-class smooth-reservoir corollary.
  - A sufficient-condition theorem for `F2(p)` saying that after `C = 1`, it is enough to place `2(p-1)` labels on `A ∪ E` supported on a fixed small prime set `S` and `2(p-1)` labels on `B ∪ F` avoiding all primes in `S`.
- Slice D: obstruction slice.
  - The unchanged upper-half-prime-only `F25` `C` program already fails at `p = 13`, even though `F25(13)` itself remains prime after a refined `C` block.

## chosen_slice

- Strongest honest slice for this pass:
  - Slice A, the paired structural reductions.
- Chosen theorem-slice statement:
  - `Γ(Z_p × Z_25)` and `Γ(Z_p × Z_p × Z_2)` each reduce to explicit classwise coprimality allocations on tiny support graphs;
  - on the second family, the actual support graph is
    `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`,
    and after fixing `C = 1` only `A-B`, `A-F`, and `B-E` remain arithmetic.
- Why this is the strongest honest slice:
  - it is already supported by Lean-backed exact seeds and verified feeders on both active lines;
  - it packages the reusable mechanism shared by the exact proofs;
  - it does not pretend that the current arithmetic corollaries are closed for all odd primes.
- Arithmetic refinement preserved alongside the chosen slice:
  - on the `F25` line, the honest theorem upgrade is that the old upper-half-prime-only `C` rule is obsolete and the right local template is a small-spill `C` block;
  - on the `F2` line, the honest upgraded claim is that the naive `{2,3}`-smooth program now survives through the first zero-slack case `p = 13`, while still lacking a family-level supply lemma.

## reusable_lemmas

- Structural lemmas already worth treating as durable family assets:
  - `support_decomposition_F25`;
  - `classwise_template_lemma`;
  - `pairwise_coprime_clique_lemma`;
  - `forbidden_multiples_reservoir_lemma`;
  - `support_decomposition_F2`;
  - `singleton_one_lemma`;
  - `three_interface_pack_lemma`.
- Wrapper-level theorem names already aligned with the dossier:
  - `zp_z25_support_template_reduction`;
  - `zp_zp_z2_support_template_reduction_of_singleton_one`.
- Arithmetic lemmas that should be isolated next if the slice is to strengthen:
  - `small_spill_C_block_lemma`:
    choose `p - 1` labels for `C` in `F25(p)` while allowing a bounded number of below-half primes whose nontrivial multiples are diverted to `D`;
  - `sparse_barrier_set_lemma`:
    choose four pairwise-coprime `B` labels whose extra multiples fit inside the fixed `20` `A` slots;
  - `smooth_reservoir_count_lemma`:
    count enough `S`-smooth labels in `{1,...,p^2+2p-2}` for `A ∪ E`;
  - `coprime_complement_pack_lemma`:
    fill `B ∪ F` with labels avoiding the prime support used on `A ∪ E`.

## proof_plan

- Main proof path:
  1. Formalize the actual zero-divisor support decompositions for `F25(p)` and `F2(p)` from the ring law.
  2. State one classwise template lemma for support blowups and instantiate it on the four-class and six-class support graphs.
  3. On the `F2` line, factor the family statement through `singleton_one_lemma` and `three_interface_pack_lemma`.
  4. On the `F25` line, preserve the refined `p = 13` witness as evidence for the small-spill `C` corollary, not as a proof of a full odd-prime range.
  5. Promote the paired structural reductions as the main theorem slice and the finite arithmetic witness families as corollaries/examples.
- Strongest path forward:
  - formalize the actual support-decomposition lemmas first, because once they are on disk the paired structural slice becomes a clean paper section even before the `p = 13` six-class arithmetic question is resolved.
- Fallback path:
  - if the arithmetic corollaries still do not close, preserve the structural slice as the main theorem and package the first arithmetic failures as template-obstruction results rather than graph-level non-primality claims.

## fallback_counterexample_plan

- Do not claim a graph counterexample unless an actual non-prime instance is proved.
- Strongest obstruction theorem already available:
  - the unchanged upper-half-prime-only `C` program for `F25(p)` fails first at `p = 13`, because `[43,84]` contains only `10` primes for `12` required `C` slots.
- Strongest likely next obstruction:
  - the naive `F2` `{2,3}`-smooth reservoir at `p = 13`;
  - if the explicit packing fails there, preserve the result as the first failure of that arithmetic template, not as a theorem that `Γ(Z_13 × Z_13 × Z_2)` is non-prime.
- Minimal data to preserve if the fallback path is triggered:
  - the exact template statement being tested;
  - the exact counting or divisibility obstruction;
  - the distinction between template failure and graph failure;
  - any refined replacement template suggested by the failed feeder.

## next_best_feeder_instances

- `z17-z25-prime-zero-divisor-graph`
  - next decisive feeder;
  - it is the smallest post-`13` four-class test of whether the refined small-spill `C` strategy scales beyond the first two-exception case seen at `p = 13`.

## publication_value

- The campaign is stronger than a stack of isolated exacts because it now preserves:
  - a shared support-graph explanation on both active family lines;
  - Lean-backed exact seeds on both lines;
  - verified `p = 11` feeders on both lines;
  - paired verified `p = 13` feeders showing both that the right `F25` arithmetic slice is the refined small-spill version and that the current six-class `{2,3}`-smooth template survives exactly at zero slack.
- The strongest honest publication value right now is:
  - a paired theorem-slice program centered on support-template reductions;
  - a paired `p = 13` arithmetic package on the two active lines;
  - a sharply localized next discriminator on the four-class line.
- The honest publication verdict remains:
  - `publication_status = SLICE_CANDIDATE`;
  - not `SLICE_EXACT`, because the actual support decompositions still need family-level formal packaging and the current Lean results are still abstract support theorems rather than ring-level family wrappers;
  - not `PAPER_READY`, because the bridge lemmas and the first post-`13` four-class stress test have not yet been absorbed into the theorem narrative.

## publication_prior_art_audit

- Exact-statement search on the family phrases
  `prime labeling zero-divisor graph Z_p x Z_25`
  and
  `prime labeling zero-divisor graph Z_p x Z_p x Z_2`
  did not produce an existing theorem already settling the current paired claim.
- Alternate-notation search matters on the four-class line because
  `Z_p × Z_25 ≅ Z_(25p)` when `p ≠ 5`.
  The closest canonical hit was Fox and Mooney, `On prime labelings of zero-divisor graphs` (Combinatorial Press, 2025), which proves nearby families such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))` and leaves the broader lines `Γ(Z_p × Z_(q^2))` and `Γ(Z_p × Z_p × Z_q)` as conjectural/open rather than solved.
- Canonical-source theorem/proposition/example/corollary/observation scan:
  no statement in that 2025 source already settles `Γ(Z_p × Z_25)` or `Γ(Z_p × Z_p × Z_2)` as currently targeted here.
  The closest family-level status is conjectural, not resolved.
- Outside-source status search:
  independent structural literature already studies zero-divisor graphs of `Z_(p^2 q)` and direct products of three finite fields, so the support decompositions themselves should be treated as standard graph scaffolding rather than the main novelty of a paper claim.
- Recent follow-up check:
  recent adjacent labeling work on graceful labelings of `Γ(Z_(p^2 q))` shows the `p^2 q` zero-divisor family is still an active publication venue, but that follow-up does not settle prime labeling.
- Prior-art verdict:
  not a rediscovery at the graph-prime-labeling level;
  the real rediscovery risk is only if this campaign tries to sell the support decomposition alone as new.

## publication_statement_faithfulness

- The strongest honest claim is stronger than `here is an example`, because the repo now preserves a reusable family-level proof template supported by multiple exact seeds, verified feeders, and checked abstract wrapper lemmas.
- However, the current checked Lean statements are abstract support-template wrappers, not yet the actual zero-divisor family theorems.
  Until the family support-decomposition lemmas are formalized, the sentence
  `we proved paired reduction theorems for Γ(Z_p × Z_25) and Γ(Z_p × Z_p × Z_2)`
  is still too strong.
- The faithful current statement is:
  once the actual support decompositions are written down, prime labelability of these two families reduces to tiny coprimality interface problems;
  on the four-class line, the verified `p = 13` feeder already shows the old upper-half-prime-only `C` rule is not the right theorem statement and must be replaced by a small-spill version;
  on the six-class line, the verified `p = 13` feeder shows the naive `{2,3}`-smooth template remains alive exactly at zero slack.
- Because the underlying support decompositions are largely standard in the zero-divisor-graph literature, any publication claim must center on the prime-labeling reduction and the arithmetic package, not on the existence of the support classes themselves.

## publication_theorem_worthiness

- There is a real parameterized theorem slice here, not just isolated exacts:
  a paired reduction theorem on two infinite families plus a genuine obstruction/refinement theorem for the obsolete `F25` upper-half-prime-only `C` program.
- The proof package is partly structural and partly unfinished.
  The support-graph/interface logic is structural;
  the arithmetic corollaries still lean on hand-picked finite feeders and one unresolved post-`13` discriminator `F25(17)`.
- A referee asking `what is the theorem?` can be answered only if the paper is stated as a reduction or sufficient-condition theorem.
  The current evidence does not yet support a closed graph-level classification or a full all-odd-prime slice.
- The claim is still too dependent on small cases for anything stronger than `SLICE_CANDIDATE`.
  The exact and verified instances identify the right statement shape, but they do not by themselves close the family theorem.
- The generalization route is still strong enough to merit campaign priority.
  The closest known prime-labeling paper leaves neighboring lines open, and this repo now has family-specific structural and arithmetic evidence rather than unrelated one-off exacts.

## publication_publishability

- Current publishability verdict:
  not paper ready.
- Best honest near-term paper shape:
  a short paired reduction paper or section whose main theorem is the support-template reduction, with the exact/feeders and the `F25(13)` refinement story as applications.
- To survive review, the writeup still needs two missing ingredients:
  checked family support-decomposition lemmas tying the abstract Lean wrappers to the actual zero-divisor graphs;
  and a clear decision on whether the refined four-class arithmetic extends cleanly past `p = 13`.
- If the bridge lemmas are formalized and `F25(17)` succeeds, the status can move toward `SLICE_EXACT`.
- If `F25(17)` fails, the campaign can still yield a publishable smaller obstruction theorem, but only if the failure is packaged as a theorem about the refined arithmetic template rather than about graph non-primality.

## strongest_honest_claim

- The strongest honest post-audit claim is a paired theorem-slice candidate, not a closed theorem:
  the repo has exact seeds, verified feeders, and checked abstract Lean wrapper lemmas indicating that prime labelability of `Γ(Z_p × Z_25)` and `Γ(Z_p × Z_p × Z_2)` should reduce to explicit coprimality allocations on tiny support graphs, with the second family collapsing to `A-B`, `A-F`, and `B-E` after setting `C = 1`.
  The `F25` line also now has verified `p = 13` evidence that the old upper-half-prime-only `C` program is false as a template and must be replaced by a small-spill version, while the `F2` line now has verified `p = 13` evidence that the naive `{2,3}`-smooth six-class template survives exactly at zero slack.
  But the actual support-decomposition lemmas for the families are not yet formalized, and the decisive post-`13` arithmetic stress test `F25(17)` is still unresolved, so this is not yet a proved publication theorem.

## paper_title_hint

- `Support-template reductions for prime labelings in two zero-divisor graph families`

## next_action

- `formalize_actual_support_decomposition_lemmas_and_family_reduction_statements_then_run_z13_z13_z2`

## lean_statement

- Current Lean target for this pass:
  - the reusable family lemma
    `AutoMath.Families.ZeroDivisorReductions.three_interface_pack_lemma`,
    with the campaign wrapper
    `AutoMath.Families.ZeroDivisorReductions.zp_zp_z2_support_template_reduction_of_singleton_one`
    now factoring through it.
- Exact theorem statement checked in the official Lean backend:
  - for predicates `A,B,C,D,E,F : V → Prop`, an adjacency relation `Adj`, and a label map `label : V → Nat`,
    if every edge of `Adj` lies in one of the six actual support-graph families
    `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`,
    if all `A-B`, `A-F`, and `B-E` label pairs are coprime,
    and if every vertex in the hinge class `C` has label `1`,
    then every adjacent pair has coprime labels.
- Honest scope:
  - this is the right current theorem-slice skeleton for the six-class family line;
  - it is still an abstract support-template statement, not yet the actual family theorem for
    `Γ(Z_p × Z_p × Z_2)` derived from zero-divisor structure.

## lean_skeleton

- Proof skeleton used:
  1. case-split on the twelve-way support-graph disjunction supplied by `hAdj`;
  2. discharge the parameter-sensitive branches `A-B`, `A-F`, and `B-E` directly from `hAB`, `hAF`, and `hBE`;
  3. discharge the hinge branches `A-C`, `B-C`, and `C-D` through `singleton_one_lemma`;
  4. route the wrapper theorem
     `zp_zp_z2_support_template_reduction_of_singleton_one`
     through `three_interface_pack_lemma`.
- Reason this is the strongest honest Lean target in the current bounded scope:
  - it packages the actual six-class support graph named by the family dossier;
  - it cleanly isolates the three remaining arithmetic interfaces after `C = 1`;
  - it avoids pretending that the missing family support decompositions have already been formalized.

## lean_result

- Lean files carrying the checked target:
  - `lean/AutoMath/Families/ZeroDivisorReductions.lean`
  - `artifacts/families/zero_divisor_prime_labelings/lean/AutoMath/Families/ZeroDivisorReductions.lean`
- Mirrored-file check:
  - the family mirror matches the official backend file byte-for-byte.
- Check run:
  - `cd lean && lake build AutoMath.Families.ZeroDivisorReductions`
- Result:
  - the targeted family module checked successfully.
- Honest Lean verdict for this campaign pass:
  - the current theorem-slice skeleton is now honestly checked in Lean;
  - the campaign does not earn `EXACT`, so `PROOFS.md` is unchanged;
  - the publication claim still stops at `SLICE_CANDIDATE`, not `SLICE_EXACT`.

## lean_blockers

- Remaining blockers after this Lean pass:
  - no checked family support-decomposition lemma yet derives the actual `F25(p)` or `F2(p)` support graphs from the zero-divisor families themselves;
  - the checked Lean surface still lives at the abstract support-template level rather than the ring-specific family-theorem level;
  - the decisive post-`13` four-class feeder `F25(17)` remains unresolved, so the arithmetic story is still not closed.
