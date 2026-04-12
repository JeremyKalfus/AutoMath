# Family Record Attempt: zero_divisor_prime_labelings / obstruction_boundary

## family_statement_lock

- Sidecar mode is active from `selected_problem.md`.
- Active `entry_type`: `family_campaign`.
- Active `family_slug`: `zero_divisor_prime_labelings`.
- Active `family_name`: `Prime labelings of zero-divisor graph families`.
- Dossier path: `campaigns/zero_divisor_prime_labelings.md`.
- Canonical family artifact path used as input only: `artifacts/families/zero_divisor_prime_labelings`.
- Durable sidecar outputs for this pass:
  - `artifacts/families/zero_divisor_prime_labelings/attempts/obstruction_boundary.md`
  - `artifacts/families/zero_divisor_prime_labelings/attempts/obstruction_boundary.json`
- Locked family statements:
  - `F25(p) := Gamma(Z_p x Z_25)` for odd prime `p`.
  - `F2(p) := Gamma(Z_p x Z_p x Z_2)` for odd prime `p`.
- Locked theorem target for this sidecar:
  - keep `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice` as the closed paper core;
  - test whether the finite-range `F25` complementary-support corollary through `59 <= p <= 97` is already forced by the preserved fixed data;
  - because the direct finite-range corollary is still not preserved in repo state as its own theorem, isolate the first sharp exact obstruction / overclaim boundary instead of widening the headline.
- Bounded local inputs actually used in this pass:
  - `AGENTS.md`;
  - `selected_problem.md`;
  - `campaigns/zero_divisor_prime_labelings.md`;
  - canonical `artifacts/families/zero_divisor_prime_labelings/record.md`;
  - canonical `artifacts/families/zero_divisor_prime_labelings/status.json`;
  - `PROOFS.md`;
  - theorem windows in `lean/AutoMath/Families/ZeroDivisorPublicationSlice.lean`, `lean/AutoMath/Families/ZeroDivisorRingBridges.lean`, `lean/AutoMath/Families/ZeroDivisorF25FrozenWrapper.lean`, and `artifacts/families/zero_divisor_prime_labelings/lean/ZeroDivisorF25FrozenWrapperBoundary.lean`;
  - five seed artifacts:
    `z7-z25-prime-zero-divisor-graph`,
    `z7-z7-z2-prime-zero-divisor-graph`,
    `z13-z25-prime-zero-divisor-graph`,
    `z17-z25-prime-zero-divisor-graph`,
    and
    `z13-z13-z2-prime-zero-divisor-graph`.
- Local evidence gap:
  - no standalone local seed record for `z71-z25-prime-zero-divisor-graph`, `z97-z25-prime-zero-divisor-graph`, or `z101-z25-prime-zero-divisor-graph` is present in this worktree;
  - for those three boundary points, this sidecar uses the preserved canonical family record/status and `selected_problem.md` as read-only evidence.
- Bounded-read policy check:
  - local-only pass;
  - five seed artifacts opened, inside the requested target and hard cap;
  - local search was used only to jump to exact theorem windows and record sections;
  - no web was used.

## existing_instance_inventory

- Lean-backed exact seeds preserved in `PROOFS.md`:
  - `F25(3)`, `F25(5)`, and `F25(7)`;
  - `F2(5)` and `F2(7)`;
  - `z5-z5-z3` and `z2-power-8` remain background template evidence, not the live publication axis.
- Opened early exact seeds and what they contribute:
  - `z7-z25`:
    the stable four-class decomposition `A,B,C,D`, the exact edge families `A-C`, `B-B`, `B-C`, `B-D`, and the original no-spill large-prime `C` template.
  - `z7-z7-z2`:
    the stable six-class decomposition `A,B,C,D,E,F`, the hinge move `C = 1`, and the exact reduction to the three interfaces `A-B`, `A-F`, and `B-E`.
- Opened feeder artifacts and what changes at the first real boundaries:
  - `z13-z25`:
    the old upper-half-prime-only `C` rule already fails, but the graph still labels after allowing the spill primes `37,41` and sending their doubles to `D`.
  - `z17-z25`:
    the `p = 13` repair is not isolated; the same support proof survives with four spill primes `37,41,43,47`.
  - `z13-z13-z2`:
    the six-class line survives its first zero-slack point, with exactly `24` nontrivial `{2,3}`-smooth labels filling `A union E`.
- Lean-theorem inventory from the opened windows:
  - `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`;
  - `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_eq_96`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_ge_C_size_of_p_le_97`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_available_of_p_ge_59`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.frozen_wrapper_boundary_31_37`;
  - artifact-local mirrors
    `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f25_frozen_wrapper_boundary`,
    `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f25_fixedC0_card_eq_96`,
    `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f25_fixedC0_card_ge_C_size_of_p_le_97`,
    and
    `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`.
- Preserved canonical boundary evidence not reopened as standalone local seed records:
  - `p = 71` is the smallest preserved obstruction to strict prime-only `F25` wording;
  - `p = 97` is the last value where the fixed counted window `|C0| = 96` can still match `|C| = p - 1`;
  - `p = 101` is the first preserved post-window feeder, showing the graph can still label after changing the barrier data, so `97` is only a fixed-window boundary.
- Inventory conclusion:
  - the paired structural slice is already exact;
  - the `F2` arm is already exact at theorem-slice level;
  - the `F25` arm has one exact local arithmetic boundary theorem (`31/37`), one strongest plausible late finite-range upgrade (`59 <= p <= 97`), and two preserved overclaim boundaries (`p = 71`, `p = 101`) that must not be promoted to graph counterexamples.

## shared_structure

- Common decomposition / invariant / construction:
  classify each nonzero zero-divisor by coordinate-support type, prove that zero product is exactly support-graph adjacency, and then exploit the fact that vertices in one support class have identical neighborhoods.
- `F25(p)` support classes and exact interfaces:
  - `A = {(0,u) : 5 does not divide u}`, size `20`;
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`;
  - `C = {(a,0) : a in Z_p^x}`, size `p - 1`;
  - `D = {(a,5t) : a in Z_p^x, t in {1,2,3,4}}`, size `4(p - 1)`;
  - exact interfaces: only `A-C`, `B-B`, `B-C`, and `B-D`.
- `F2(p)` support classes and exact interfaces:
  - `A = (*,0,0)`;
  - `B = (0,*,0)`;
  - `C = (0,0,1)`;
  - `D = (*,*,0)`;
  - `E = (*,0,1)`;
  - `F = (0,*,1)`;
  - exact interfaces: only `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, and `C-D`.
- Shared proof template extracted from the seeds:
  1. prove the support partition;
  2. prove ring adjacency equals support adjacency;
  3. assign labels classwise so only support-adjacent interfaces matter;
  4. trivialize one large part of the graph by a single invariant move;
  5. let the remaining unconstrained class absorb the residual labels.
- Family-specific reusable constructions:
  - `F2`:
    set the singleton class `C` to label `1`, after which the whole proof collapses to the three cross-coprime interfaces `A-B`, `A-F`, and `B-E`;
  - `F25`:
    keep `A` in a low-support reservoir, choose a sparse pairwise-coprime barrier on `B`, choose `C` from labels whose prime support avoids the support of `A union B`, and let `D` absorb the complement.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  - the support decompositions;
  - the ring-to-support reduction on both family lines;
  - the exact `F2` hinge move `C = 1` and the three-interface reduction theorem;
  - the generic `F25` high-barrier wrapper once admissible `A`, `B`, `C`, and `D` label sets are supplied;
  - the counted fixed-window facts `|C0| = 96`, `p - 1 <= |C0|` for `p <= 97`, and `C0` support avoidance with respect to `{2,3}` and the late barrier primes `293,307,311`.
- Steps that are still open as theorem packaging rather than raw arithmetic:
  - choose a `(p - 1)`-subset of `fixedC0Finset`;
  - package that subset as the injective `C`-class input expected by `zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`;
  - turn the fixed-data skeleton into one referee-facing finite-range corollary for odd primes `59 <= p <= 97`.
- Steps that are visibly instance-specific:
  - the no-spill prime choice in `z7-z25`;
  - the two spill primes `37,41` in `z13-z25`;
  - the four spill primes `37,41,43,47` in `z17-z25`;
  - the zero-slack exact count of `24` nontrivial `{2,3}`-smooth labels at `p = 13` on the `F2` line;
  - the fixed late data
    `A0`,
    `B = {1,293,307,311}`,
    and
    `C0 = {n : 2 <= n <= 291 and gcd(n,6)=1}`;
  - the preserved strict-prime-only obstruction at `p = 71`;
  - the preserved post-window retuning at `p = 101`.
- Strongest plausible theorem slice:
  the fixed-data complementary-support corollary for odd primes `59 <= p <= 97`, derived from `|C0| = 96` plus the checked wrapper skeleton.
- Smallest likely counterexample or obstruction:
  - no graph-level counterexample is supported by the opened evidence;
  - the first sharp exact obstruction theorem preserved locally is
    `family_zero_divisor_prime_labelings_f25_frozen_wrapper_boundary`, equivalently `frozen_wrapper_boundary_31_37`, where the stricter frozen front fits through `p = 31` and first overflows at `p = 37`;
  - the smallest preserved overclaim boundary in the later prime-only language is `p = 71`;
  - the first preserved fixed-window boundary for the counted `C0` theorem is `p = 101`.

## candidate_theorem_slices

- Slice A:
  the exact paired structural theorem
  `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`.
- Slice B:
  the exact obstruction-boundary theorem
  `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f25_frozen_wrapper_boundary`,
  mirroring
  `AutoMath.Families.ZeroDivisorF25FrozenWrapper.frozen_wrapper_boundary_31_37`.
- Slice C:
  the finite-range `F25` complementary-support corollary for odd primes `59 <= p <= 97`, obtained from the fixed data `A0`, `B = {1,293,307,311}`, and any `(p - 1)`-subset of `C0`.
- Slice D:
  a template-level negative slice saying the stricter prime-only `F25` headline is already too strong by preserved `p = 71`, even though no graph non-primality is supported there.
- Slice E:
  a post-`97` variable-barrier complementary-support slice suggested by preserved `p = 101`, but not yet quantified.

## chosen_slice

- Chosen exact slice for this obstruction-boundary sidecar:
  keep `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice` as the closed paper core, and pair it with
  `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f25_frozen_wrapper_boundary`
  as the first sharp exact overclaim boundary on the stricter frozen `F25` front.
- Strongest plausible but still unclosed upgrade:
  the finite-range complementary-support `F25` corollary through `59 <= p <= 97`.
- Why this is the strongest honest choice in this sidecar:
  - Slice A is exact and already parameterized on both active family lines;
  - Slice B is also exact and is the cleanest preserved local obstruction theorem;
  - Slice C still depends on a subset-selection / injection statement that is not yet preserved as its own theorem in repo state;
  - Slice D and Slice E are honest boundary narratives, but not stronger closed theorems than Slice B.
- Why broader language would overclaim:
  - `z13-z25` and `z17-z25` show that the old no-spill front is not the family theorem;
  - preserved `p = 71` blocks strict prime-only wording;
  - preserved `p = 101` shows the fixed `C0` window stops at `97` without implying graph failure beyond it.

## reusable_lemmas

- Closed structural lemmas already carrying publication weight:
  - `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`;
  - `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`.
- Closed exact obstruction / boundary lemmas already preserved locally:
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.frozen_wrapper_boundary_31_37`;
  - `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f25_frozen_wrapper_boundary`.
- Fixed-window `F25` scaffold lemmas already preserved:
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_eq_96`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_ge_C_size_of_p_le_97`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_available_of_p_ge_59`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_support_avoids_two_three`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_support_avoids_high_barrier_293_307_311`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`;
  - artifact-local mirrors of the same fixed-window facts in `AutoMath.Families.ZeroDivisorPrimeLabelings`.
- Missing next reusable lemma family:
  - a finitary subset-selection / injection lemma that takes
    `p - 1 <= fixedC0Finset.card`,
    chooses a `(p - 1)`-subset of `fixedC0Finset`,
    and packages it as the actual `C`-class labeling input expected by the fixed-window wrapper skeleton.

## proof_plan

- Main proof path for this sidecar:
  1. Present `zero_divisor_prime_labelings_paired_exact_slice` as the closed theorem core.
  2. Present `family_zero_divisor_prime_labelings_f25_frozen_wrapper_boundary` as the first sharp exact obstruction theorem: the preserved frozen `F25` front fits at `p = 31`, has exact spill `19` there, has exact spill `22` at `p = 37`, and first exceeds the `20` labels of `A` at `p = 37`.
  3. Use the opened `z7`, `z13`, and `z17` `F25` seeds to explain why that obstruction is only to the stricter frozen front, not to graph prime-labelability itself: after `p = 13`, the family already survives by complementary-support refinement.
  4. Use the opened `z7-z7-z2` and `z13-z13-z2` seeds together with `zp_zp_z2_three_interface_lead_theorem` to keep the `F2` arm fixed and exact.
  5. Preserve the late fixed-window theorem surface only as next scaffold: `|C0| = 96`, `p - 1 <= |C0|` for `p <= 97`, and the graph-faithful wrapper skeleton.
- Strongest path forward beyond this sidecar:
  prove the missing subset-selection / injection lemma from `fixedC0Finset` into the actual `C` block and then upgrade the campaign to the finite-range `59 <= p <= 97` complementary-support corollary.
- Fallback path:
  1. If that finite-range corollary still is not packaged cleanly, stop at the exact paired slice plus the exact `31/37` obstruction theorem.
  2. Use preserved `p = 71` only to forbid stricter prime-only wording.
  3. Use preserved `p = 101` only to mark the end of the fixed `C0` window.
  4. Reopen feeder work only if the wrapper-language corollary still stalls after that packaging attempt.

## fallback_counterexample_plan

- No graph-level counterexample theorem is supported by the opened evidence.
- Best generalized conjecture / template if the finite-range corollary is still treated as open:
  for every odd prime `p` with `59 <= p <= 97`, the fixed data `A0`, `B = {1,293,307,311}`, and any `(p - 1)`-subset of
  `C0 = {n : 2 <= n <= 291 and gcd(n,6)=1}`
  should satisfy the `F25` graph-faithful wrapper hypotheses.
- Smallest exact negative theorem already available:
  `family_zero_divisor_prime_labelings_f25_frozen_wrapper_boundary`.
- Smallest preserved template-level obstructions after that:
  - `p = 71` blocks strict prime-only `F25` language;
  - `p = 101` blocks extending the fixed counted `C0` theorem past `p = 97`.
- Do not claim graph non-primality at `p = 37`, `p = 71`, or `p = 101`; the evidence supports only arithmetic / wrapper-language boundaries.

## next_best_feeder_instances

- `z103-z25-prime-zero-divisor-graph`:
  the smallest next discriminator for whether the post-`97` variable-barrier complementary-support regime begins immediately after the preserved fixed-window boundary.
- `z107-z25-prime-zero-divisor-graph`:
  the next smallest follow-up if `z103` still leaves ambiguity between a stable post-window template and a one-off barrier retuning.
- No further `F2` feeder is needed for this sidecar because the `F2` theorem slice is already exact in Lean.

## publication_value

- Best honest publication unit from this sidecar:
  the exact paired structural slice together with the exact `31/37` obstruction theorem for the stricter frozen `F25` front.
- Why this has publication value:
  - it cleanly separates what is already exact from what is still only a live upgrade target;
  - it gives one sharp local obstruction theorem instead of a vague warning;
  - it preserves the later `p = 71` and `p = 101` boundaries as overclaim boundaries rather than mislabeling them as graph counterexamples.
- Why this is not yet `PAPER_READY`:
  - the first referee-facing direct `F25` corollary through `59 <= p <= 97` is still not preserved as its own theorem;
  - the preserved `p = 71` and `p = 101` boundaries are carried canonically, not from reopened standalone local seed artifacts in this worktree;
  - the publication core is exact, but the next direct family claim is still one lemma short.
- Honest publication posture for this sidecar:
  `publication_status = SLICE_EXACT`, not `PAPER_READY`.
