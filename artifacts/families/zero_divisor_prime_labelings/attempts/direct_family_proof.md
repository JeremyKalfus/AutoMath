# Family Record Attempt: zero_divisor_prime_labelings / direct_family_proof

## family_statement_lock

- Sidecar mode is active from `selected_problem.md`.
  This pass writes only to:
  `artifacts/families/zero_divisor_prime_labelings/attempts/direct_family_proof.md`
  and
  `artifacts/families/zero_divisor_prime_labelings/attempts/direct_family_proof.json`.
- Canonical inputs were treated as read-only:
  `campaigns/zero_divisor_prime_labelings.md`,
  `artifacts/families/zero_divisor_prime_labelings/record.md`,
  and
  `artifacts/families/zero_divisor_prime_labelings/status.json`.
- Locked family statements:
  - `F25(p) := Gamma(Z_p x Z_25)` for odd prime `p`.
  - `F2(p) := Gamma(Z_p x Z_p x Z_2)` for odd prime `p`.
- Closed publication core for this sidecar:
  `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`.
- Live theorem target for this pass:
  the finite-range `F25` complementary-support corollary for odd primes
  `59 <= p <= 97`, obtained by combining
  `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_ge_C_size_of_p_le_97`
  with
  `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`
  through an explicit subset-selection / injection theorem.
- Output intent:
  keep the paired theorem slice as exact,
  identify the strongest honest upgrade path,
  and isolate the smallest remaining blocker without widening the claim to an all-primes `F25` theorem.
- Local inputs used in this bounded pass:
  - `AGENTS.md`;
  - `selected_problem.md`;
  - `campaigns/zero_divisor_prime_labelings.md`;
  - the canonical family `record.md` and `status.json`;
  - `PROOFS.md`;
  - exact theorem windows in
    `lean/AutoMath/Families/ZeroDivisorPublicationSlice.lean`
    and
    `lean/AutoMath/Families/ZeroDivisorF25FrozenWrapper.lean`;
  - six seed artifacts:
    `z3-z25-prime-zero-divisor-graph`,
    `z5-z25-prime-zero-divisor-graph`,
    `z7-z25-prime-zero-divisor-graph`,
    `z5-z5-z2-prime-zero-divisor-graph`,
    `z7-z7-z2-prime-zero-divisor-graph`,
    and
    `z13-z25-prime-zero-divisor-graph`.
- Bounded-read check:
  - local-only pass;
  - no web used;
  - six seed artifacts opened, within the requested target and below the hard cap;
  - local search was used only to jump to exact theorem and artifact sections;
  - once the record could be filled honestly, exploration stopped and the sidecar outputs were rewritten.

## existing_instance_inventory

- Lean-backed exact baseline from `PROOFS.md`:
  - `F25(3)`, `F25(5)`, `F25(7)`;
  - `F2(5)`, `F2(7)`;
  - each preserved only as `publication_status = INSTANCE_ONLY`.
- Opened seed artifacts and what each contributes:
  - `z3-z25`:
    smallest exact `F25` seed; its witness already separates the graph into the same four structural roles later called `A,B,C,D`.
  - `z5-z25`:
    first clean four-class exact where the support graph is explicitly `A-C`, `B-B`, `B-C`, `B-D`, with `C` handled by sparse high primes and `B` by a pairwise-coprime barrier clique.
  - `z7-z25`:
    larger exact seed showing the same four-class template survives unchanged when the `C` block grows to size `6`.
  - `z5-z5-z2`:
    smallest exact `F2` seed; once the singleton class `C` gets label `1`, the only nontrivial interfaces are `A-B`, `A-F`, and `B-E`.
  - `z7-z7-z2`:
    larger exact `F2` seed confirming the same three-interface reduction with a free `D` class after `C = 1`.
  - `z13-z25`:
    first refined `F25` feeder; the old upper-half-prime-only `C` rule fails, but the graph still labels after admitting spill primes `37,41` and pushing their doubles into `D`.
- Exact Lean theorems opened locally:
  - `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_eq_96`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_ge_C_size_of_p_le_97`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_available_of_p_ge_59`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_support_avoids_two_three`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_support_avoids_high_barrier_293_307_311`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_high_barrier_complementary_support_wrapper_graph_of_injective`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.frozen_wrapper_boundary_31_37`.
- Preserved boundary facts taken from the read-only canonical family state and `selected_problem.md`:
  - `p = 71` is the smallest preserved obstruction to strict prime-only `F25` language;
  - `p = 101` is the first preserved boundary showing the fixed `C0` window stops at `97` without implying graph-level failure.
- Inventory conclusion:
  - the paired structural slice is already exact in Lean;
  - the `F2` arm is not the active blocker;
  - the `F25` arm already has the fixed-window size bound and the wrapper skeleton through `p <= 97`;
  - the only live gap is packaging `p - 1 <= |fixedC0Finset|` into the explicit `C`-class selection / injective-labeling input required by the fixed-window wrapper theorem.

## shared_structure

- Common decomposition / invariant / construction:
  classify each nonzero zero-divisor by coordinate-support type,
  prove that zero product is exactly support-graph adjacency,
  then assign labels classwise because vertices inside one support class have identical neighborhoods.
- `F25(p)` support classes:
  - `A = {(0,u) : 5 does not divide u}`, size `20`;
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`;
  - `C = {(a,0) : a in Z_p^x}`, size `p - 1`;
  - `D = {(a,5t) : a in Z_p^x, t in {1,2,3,4}}`, size `4(p - 1)`.
- `F25(p)` exact interfaces:
  only `A-C`, `B-B`, `B-C`, and `B-D`.
- `F2(p)` support classes:
  `A,B,C,D,E,F`.
- `F2(p)` exact interfaces:
  only `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, and `C-D`.
- Shared proof template:
  1. prove the support partition from the ring law;
  2. reduce graph coprimality to a tiny support graph;
  3. choose labels by class rather than by individual vertex;
  4. use classwise symmetry to lift the class labels to a full graph labeling.
- Construction that genuinely recurs:
  - on the `F2` line, put `1` on the singleton `C` class and let `D` absorb the leftovers;
  - on the `F25` line, keep `A` on a `{2,3}`-supported reservoir, keep `B` on a sparse barrier clique, choose `C` from labels whose prime support avoids both `{2,3}` and the barrier primes, then let `D` absorb the complement.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  - the support decompositions and ring-to-support bridge;
  - the `F2` hinge move `C = 1`;
  - the generic `F25` wrapper once admissible class label sets are supplied;
  - the fixed-window `C0` facts:
    `|C0| = 96`,
    `p - 1 <= |C0|` for `p <= 97`,
    and support-avoidance against `{2,3,293,307,311}`.
- Steps that are still open as theorem packaging:
  - extract a `(p - 1)`-element block from `fixedC0Finset`;
  - convert that block into the injective `C`-class labeling data expected by
    `zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`;
  - package the resulting graph-level corollary cleanly for odd primes
    `59 <= p <= 97`.
- Steps that are instance-specific:
  - the hand-picked above-half prime choices in the small exact seeds;
  - the spill primes `37,41` at `p = 13`;
  - the template-level obstruction at `p = 71`;
  - the fixed-window endpoint role of `p = 101`.
- Strongest plausible theorem slice beyond the exact paired core:
  the finite-range `F25` corollary for odd primes `59 <= p <= 97`.
- Smallest likely counterexample or obstruction:
  - no graph-level counterexample is supported by the opened local evidence;
  - the smallest honest obstruction is template-level:
    strict prime-only `F25` wording fails by `p = 71`;
  - the smallest preserved fixed-window boundary is `p = 101`,
    where the graph may still label but the frozen `C0` supply no longer covers `|C| = p - 1`.

## candidate_theorem_slices

- Slice A:
  the exact paired structural reduction theorem
  `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`.
- Slice B:
  the exact `F2` three-interface slice already packaged inside Slice A.
- Slice C:
  the exact graph-faithful `F25` wrapper
  `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_high_barrier_complementary_support_wrapper_graph_of_injective`.
- Slice D:
  the finite-range `F25` corollary for odd primes `59 <= p <= 97`,
  using fixed `A0`,
  fixed `B = {1,293,307,311}`,
  and a selected `(p - 1)`-subset of `C0`.
- Slice E:
  a negative template boundary:
  `p = 71` already rules out strict prime-only `F25` language,
  while `p = 101` marks the end of the fixed `C0` window rather than a graph-level failure.

## chosen_slice

- Strongest closed slice:
  keep
  `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`
  as the exact publication core.
- Strongest honest live upgrade:
  Slice D, the finite-range `F25` corollary for odd primes `59 <= p <= 97`.
- Proposed theorem slice:
  for every odd prime `p` with `59 <= p <= 97`,
  `Gamma(Z_p x Z_25)` should admit a prime labeling obtained by labeling
  `A` with the fixed `A0` set,
  `B` with `{1,293,307,311}`,
  `C` with some `(p - 1)`-element subset of
  `C0 = {n : 2 <= n <= 291 and gcd(n,6)=1}`,
  and `D` with the remaining labels in `{1,...,5p+19}`.
- Why this is the strongest honest slice:
  - it is strictly stronger than an instance-only claim;
  - every arithmetic ingredient except the subset-selection / injection packaging is already preserved locally;
  - it stops exactly at the first preserved fixed-window boundary.
- Why this slice is not yet claimed as closed:
  - the repo theorem surface already counts `C0`, but does not yet preserve the explicit selector / injection theorem feeding the fixed-window wrapper skeleton;
  - the current blocker is therefore packaging, not lack of arithmetic supply or lack of exact seeds.

## reusable_lemmas

- Reusable structural lemmas already carrying family weight:
  - `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`;
  - the support-decomposition and classwise-template lemmas named in the dossier;
  - the `F2` three-interface reduction theorem already packaged in the paired exact slice.
- Reusable fixed-window `F25` lemmas already preserved:
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_eq_96`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_ge_C_size_of_p_le_97`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_available_of_p_ge_59`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_support_avoids_two_three`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_support_avoids_high_barrier_293_307_311`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`.
- One missing reusable lemma family:
  - a subset-selection / injection theorem saying that,
    for odd prime `p` with `59 <= p <= 97`,
    the inequality `p - 1 <= fixedC0Finset.card` yields a selected `C` block of size `p - 1`
    and an injective classwise labeling compatible with the fixed-window wrapper skeleton.
- Secondary missing packaging lemma:
  - a complement-cardinality statement that the remaining labels in `{1,...,5p+19}` have size exactly `4(p - 1)` after removing the fixed `A` block, fixed `B` block, and chosen `C` block.

## proof_plan

- Main proof path:
  1. Present
     `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`
     as the closed paper core.
  2. Use
     `fixedC0_card_ge_C_size_of_p_le_97`
     to obtain enough `C` labels for every odd prime `59 <= p <= 97`.
  3. Prove the missing selector / injection lemma from `fixedC0Finset` into the `C` support class.
  4. Define `D` as the interval complement and prove it has the required size `4(p - 1)`.
  5. Apply
     `zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`
     to obtain the graph-level corollary.
- Strongest path forward:
  close the selector / injection packaging before reopening feeder search,
  because the exact paired theorem and the fixed-window arithmetic surface are already preserved.
- Fallback path:
  keep the publication claim frozen at the exact paired slice plus the fixed-window `F25` supply lemmas and wrapper skeleton,
  then use feeder work only to test the first post-window variable-barrier regime.

## fallback_counterexample_plan

- No graph-level counterexample theorem is supported by the opened evidence.
- The honest negative line is template-level:
  strict prime-only `F25` wording is already too strong by `p = 71`.
- If the finite-range corollary still does not close:
  - preserve `p = 71` only as the smallest obstruction to overstrong prime-only language;
  - preserve `p = 101` only as the first fixed-window boundary;
  - do not claim any failure of `Gamma(Z_p x Z_25)` itself from either fact.
- Smallest unresolved obstruction after the fixed-window slice:
  whether the post-`97` variable-barrier complementary-support template persists immediately at `p = 103` and `p = 107`.

## next_best_feeder_instances

- `z103-z25-prime-zero-divisor-graph`:
  first odd-prime feeder beyond the preserved fixed-window boundary;
  it best discriminates whether the variable-barrier complementary-support template restarts immediately after `p = 101`.
- `z107-z25-prime-zero-divisor-graph`:
  next smallest post-boundary discriminator if `z103` is inconclusive or looks too special.
- No new `F2` feeder is the right next move:
  the `F2` arm is already structurally exact and is not the current blocker.

## publication_value

- The campaign already owns a real theorem slice, not just exact feeder instances:
  the paired support-reduction theorem is Lean-checked and publication-facing.
- The direct value of this sidecar is to isolate one small missing theorem-packaging step:
  the selector / injection bridge from `fixedC0Finset` into the fixed-window `F25` wrapper.
- If that bridge closes, the campaign gains its first referee-facing direct `F25` corollary on a nontrivial finite prime range.
- If it does not, the current state is still publishable as an exact paired reduction theorem with an honest fixed-window frontier and a sharply bounded next-feeder plan.
