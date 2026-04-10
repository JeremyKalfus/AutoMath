# Family Record: zero_divisor_prime_labelings

## family_statement_lock

- Active family slug: `zero_divisor_prime_labelings`.
- Active dossier: [campaigns/zero_divisor_prime_labelings.md](/Users/jeremykalfus/CodingProjects/AutoMath/campaigns/zero_divisor_prime_labelings.md).
- Family artifact path: [artifacts/families/zero_divisor_prime_labelings](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/families/zero_divisor_prime_labelings).
- Locked family statements for this pass:
  - `F25(p) := Γ(Z_p × Z_25)` for odd prime `p`.
  - `F2(p) := Γ(Z_p × Z_p × Z_2)` for odd prime `p`.
- Locked theorem target for this generalize pass:
  - not an all-odd-prime theorem;
  - not another isolated exact witness;
  - instead, paired support-template reduction theorems that turn each family into a small classwise coprimality allocation problem.
- The strongest honest current theorem target is therefore:
  - a reduction theorem for `F25(p)` on four support classes `A,B,C,D`;
  - a reduction theorem for `F2(p)` on six support classes `A,B,C,D,E,F`, with the singleton class `C` fixed to label `1`.

## existing_instance_inventory

- Lean-backed exact seeds preserved in [PROOFS.md](/Users/jeremykalfus/CodingProjects/AutoMath/PROOFS.md):
  - `z3-z25-prime-zero-divisor-graph`: exact `F25(3)` on `34` vertices.
  - `z5-z25-prime-zero-divisor-graph`: exact `F25(5)` on `44` vertices.
  - `z7-z25-prime-zero-divisor-graph`: exact `F25(7)` on `54` vertices.
  - `z5-z5-z2-prime-zero-divisor-graph`: exact `F2(5)` on `33` vertices.
  - `z7-z7-z2-prime-zero-divisor-graph`: exact `F2(7)` on `61` vertices.
- Exact inventory for `F25(p)`:
  - every seed uses the same four support classes
    `A = {(0,u) : u ∈ Z_25^x, 5 ∤ u}`, `|A| = 20`,
    `B = {(0,5),(0,10),(0,15),(0,20)}`, `|B| = 4`,
    `C = {(a,0) : a ∈ Z_p^x}`, `|C| = p - 1`,
    `D = {(a,5t) : a ∈ Z_p^x, t ∈ {1,2,3,4}}`, `|D| = 4(p - 1)`.
  - every seed uses the same edge pattern:
    `A-C`, `B-B`, `B-C`, `B-D`, and no other edges.
  - witness arithmetic across the solved exacts:
    `F25(3)` uses a two-vertex high-prime block on `C` and absorbs the forbidden multiples into the nonadjacent classes;
    `F25(5)` uses `C = {11,23,29,31}` and `B = {1,37,41,43}`;
    `F25(7)` uses six upper-half primes on `C` and `B = {1,11,13,17}`.
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
  - every seed uses the same edge pattern:
    `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`, and no other edges.
  - witness arithmetic across the solved exacts:
    `F2(5)` uses `C = 1`, powers of `2` on `A`, odd `3,5`-smooth labels on `B`, `3,5`-avoiding even labels on `E`, and odd labels on `F`;
    `F2(7)` uses `C = 1`, a `{2,3}`-smooth block on `A`, large primes on `B`, another `{2,3}`-smooth block on `E`, and labels avoiding `2,3` on `F`.
- The exact inventory already settles one major point:
  - the repeated proof burden is structural and classwise, not vertex-by-vertex.

## shared_structure

- Common decomposition / invariant:
  - in both families, adjacency is determined entirely by support type, so the zero-divisor graph is a blowup of a tiny support graph with parameter-dependent class sizes;
  - vertices inside a fixed support class have identical neighborhoods, so any bijection within a class preserves adjacency and coprimality requirements.
- Common decomposition / construction:
  - first prove the support-class partition from coordinatewise zero product;
  - then replace the full graph by a partition of `{1,...,N}` into class label blocks of the right sizes;
  - then check only the adjacent class pairs and any clique classes.
- `F25(p)` support graph:
  - `A` and `D` are independent and only interface indirectly;
  - `B` is the unique internal clique class;
  - `C` only sees `A ∪ B`;
  - `D` only sees `B`.
- `F2(p)` support graph:
  - `C` is the unique hinge vertex;
  - once `C` gets label `1`, the entire `D` block becomes free;
  - only three nontrivial cross-class interfaces remain: `A-B`, `A-F`, `B-E`.
- The shared proof template is therefore:
  - support blowup lemma;
  - classwise partition lemma;
  - family-specific adjacency check on a tiny support graph.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameter:
  - the support decompositions for `F25(p)` and `F2(p)`;
  - the fact that classwise label blocks are enough once support classes are fixed;
  - the `F25(p)` observation that the only internal constraint is the `K_4` on `B`;
  - the `F2(p)` observation that `C = 1` frees the whole `D` class;
  - the reduction of both families to finitely many cross-coprimality interfaces independent of the full graph size.
- Steps that are still instance-specific in the current exact proofs:
  - the concrete upper-half prime lists used for the `C` block in the solved `F25(p)` instances;
  - the exact barrier sets chosen for the `B` clique in the solved `F25(p)` instances;
  - the precise smooth-number reservoirs used for `A` and `E` in `F2(5)` and `F2(7)`;
  - the leftover label assignments into `D`, which are free only after the support reduction is established.
- The real parameter bottlenecks are arithmetic, not structural:
  - `F25(p)`: the `C` block has size `p - 1`, but `A ∪ B` has fixed size `24`, so the set of prime factors carried by `C` must stay sparse enough that `24` labels remain available for `A ∪ B`;
  - `F25(p)`: the clique labels on `B` must stay pairwise coprime while forbidding as few labels as possible from the large `D` reservoir;
  - `F2(p)`: after `C = 1`, one must still supply `2(p - 1)` labels for `A ∪ E` and `p - 1` labels for `F` with the right prime-support separation.
- Smallest likely obstructions if the current arithmetic templates break:
  - `F25(11)` is the first natural breakpoint for the current upper-half-prime plus sparse-barrier pattern;
  - `F2(11)` is the first place the smooth-reservoir heuristic must be counted rather than guessed;
  - if `F2(11)` survives, `F2(13)` is the first visibly tight smooth-reservoir test.

## candidate_theorem_slices

- Slice 1: `F25(p)` support-template reduction theorem.
  - For odd prime `p`, let `{1,...,5p+19}` be partitioned into `L_A,L_B,L_C,L_D` with sizes `20,4,p-1,4(p-1)`.
  - If `L_B` is pairwise coprime, every label in `L_C` is coprime to every label in `L_A ∪ L_B`, and every label in `L_D` is coprime to every label in `L_B`, then `Γ(Z_p × Z_25)` has a prime labeling.
- Slice 2: `F2(p)` support-template reduction theorem.
  - For odd prime `p`, let `{1,...,p^2 + 2p - 2}` be partitioned into `L_A,L_B,L_C,L_D,L_E,L_F` with sizes
    `p-1,p-1,1,(p-1)^2,p-1,p-1`.
  - If `L_C = {1}` and the only required cross-coprimality conditions
    `gcd(L_A,L_B) = 1`,
    `gcd(L_A,L_F) = 1`,
    `gcd(L_B,L_E) = 1`
    hold classwise, then `Γ(Z_p × Z_p × Z_2)` has a prime labeling.
- Slice 3: arithmetic corollary candidate for `F25(11)`.
  - Reuse Slice 1 with an upper-half prime block on `C`, a sparse pairwise-coprime clique block on `B`, and absorb all extra forbidden multiples into `A`.
  - This is plausible from the exact cluster, but not yet closed from current evidence.
- Slice 4: arithmetic corollary candidate for `F2(11)`.
  - Reuse Slice 2 with `C = 1`, a smooth block for `A ∪ E`, a prime block for `B`, and a residue class for `F` avoiding the prime support of `A`.
  - This matches the `p = 5,7` exacts but still needs a clean count argument.
- Slice 5: smallest-template-failure obstruction theorem.
  - If the structural reduction remains correct but the current arithmetic template first fails at `p = 11` or `p = 13`, preserve that as a theorem about the first failure of the naive reservoir pattern rather than as a claim that the graph itself is non-prime.

## chosen_slice

- Strongest honest slice for this pass:
  - the paired support-template reduction theorems in Slice 1 and Slice 2.
- Why this is the right choice:
  - the proof is structural and visible in all five Lean-backed exact seeds;
  - it is stronger than a pile of isolated exacts because it packages the reusable family mechanism;
  - it does not rely on any unproved prime-counting or smooth-counting claim.
- Explicit theorem target for `F25(p)`:
  - prime labelability reduces exactly to finding a classwise partition satisfying one clique constraint on `B`, one `C` versus `A ∪ B` coprimality condition, and one `D` versus `B` coprimality condition.
- Explicit theorem target for `F2(p)`:
  - prime labelability reduces exactly to fixing `C = 1`, after which only three cross-class interfaces remain: `A-B`, `A-F`, and `B-E`.
- Strongest plausible arithmetic upgrade after the chosen slice:
  - test `F25(11)` and `F2(11)` as the first nontrivial corollaries of the reduction theorems;
  - use `p = 13` only as the first tight follow-up, not as the next default target.

## reusable_lemmas

- `support_decomposition_F25`:
  classify the nonzero zero-divisors of `Z_p × Z_25` into `A,B,C,D` and prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`.
- `support_decomposition_F2`:
  classify the nonzero zero-divisors of `Z_p × Z_p × Z_2` into `A,B,C,D,E,F` and prove the exact edge pattern `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`.
- `classwise_template_lemma`:
  for a support blowup graph, any partition of the label interval by support classes works once every adjacent class pair is cross-coprime and every clique class is internally pairwise coprime.
- `pairwise_coprime_clique_lemma`:
  the `B` class in `F25(p)` only needs four pairwise-coprime labels, independent of `p`.
- `singleton_one_lemma`:
  if a singleton support class is adjacent to a large residual class, assigning label `1` to that singleton frees the entire residual class.
- `forbidden_multiples_reservoir_lemma`:
  once the prime support carried by a constrained class is fixed, the adjacent residual class only needs enough labels avoiding those prime factors, not a vertex-by-vertex witness.
- `three_interface_pack_lemma`:
  after `C = 1` in `F2(p)`, the family reduces to simultaneously satisfying exactly three cross-coprimality interfaces and no others.

## proof_plan

- Main proof path:
  1. Prove `support_decomposition_F25` and `support_decomposition_F2` directly from coordinatewise zero product.
  2. Prove `classwise_template_lemma` once for support-blowup graphs.
  3. Deduce Slice 1 by checking only the edge families `A-C`, `B-B`, `B-C`, `B-D`.
  4. Deduce Slice 2 by fixing `C = 1`, freeing `D`, and checking only `A-B`, `A-F`, `B-E`.
  5. Preserve the solved exact seeds only as evidence that the arithmetic side is plausible, not as part of the structural proof.
- One strongest path forward:
  - formalize the two reduction theorems first and only then test `p = 11` as a pure interval-partition feeder.
- One fallback path:
  - if the arithmetic closure does not scale at `p = 11`, keep the structural reduction theorems and reframe the result as the first honest failure of the current reservoir template.

## fallback_counterexample_plan

- The likely fallback theorem is not "non-prime graph" but "first failure of the naive arithmetic template."
- Smallest likely obstruction for `F25(p)`:
  - `F25(11)`, where the upper-half-prime `C` block and the sparse `B` clique barrier first need a real count argument rather than ad hoc packing.
- Smallest likely obstruction for `F2(p)`:
  - `F2(11)` if the current smooth-reservoir heuristic already under-supplies one of `A,E,F`;
  - `F2(13)` if `p = 11` survives, because the smooth-reservoir count becomes visibly tight there.
- What to preserve if a feeder fails:
  - the exact structural reduction theorem;
  - the explicit arithmetic template that was being tested;
  - the minimal counting or divisibility obstruction;
  - the distinction between template failure and actual non-primality of the graph family.

## next_best_feeder_instances

- `z11-z25-prime-zero-divisor-graph`
  - first discriminator for whether the `F25(p)` upper-half-prime plus sparse-barrier template actually satisfies Slice 1 beyond the solved exact cluster.
- `z11-z11-z2-prime-zero-divisor-graph`
  - first discriminator for whether the `F2(p)` smooth-reservoir and prime-block split really satisfies Slice 2 beyond `p = 5,7`.
- `z13-z25-prime-zero-divisor-graph`
  - next tight follow-up only after the `p = 11` verdict is clean.
- `z13-z13-z2-prime-zero-divisor-graph`
  - first visibly tight follow-up for the smooth-reservoir side if `p = 11` survives.

## publication_value

- The campaign is already stronger than `INSTANCE_ONLY` because five Lean-backed exacts now share two family-level support templates.
- The strongest honest present publication value is:
  - paired reduction theorems that package the structural heart of the exact proofs;
  - a clear arithmetic feeder program at `p = 11`, with `p = 13` as the next tight discriminator;
  - reusable family lemmas that are Lean-ready even though the family theorems are not yet Lean-complete.
- Honest current publication verdict:
  - the campaign is not `PAPER_READY`;
  - the campaign is stronger than a conjectural family slogan;
  - the right present label remains `publication_status = SLICE_CANDIDATE`.
