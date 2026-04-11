# Family Record: zero_divisor_prime_labelings

## family_statement_lock

- Active `family_slug`: `zero_divisor_prime_labelings`.
- Dossier path: `campaigns/zero_divisor_prime_labelings.md`.
- Family artifact path: `artifacts/families/zero_divisor_prime_labelings`.
- Locked family statements for this GENERALIZE pass:
  - `F2(p) := Γ(Z_p × Z_p × Z_2)` for odd primes `p`;
  - `F25(p) := Γ(Z_p × Z_25)` for odd primes `p`.
- Locked theorem target from `selected_problem.md`:
  - keep `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem` as the exact lead slice.
- Locked fallback target from `selected_problem.md`:
  - close a quantified bounded-spill plus barrier-reservoir wrapper on `Γ(Z_p × Z_25)`, or else package the first sharp repaired-wrapper obstruction theorem.
- Bounded local read log for this pass:
  - `AGENTS.md`;
  - `selected_problem.md`;
  - `campaigns/zero_divisor_prime_labelings.md`;
  - `artifacts/families/zero_divisor_prime_labelings/record.md`;
  - `artifacts/families/zero_divisor_prime_labelings/status.json`;
  - `PROOFS.md` at the exact sections for `z3-z25`, `z5-z25`, `z7-z25`, `z5-z5-z2`, and `z7-z7-z2`;
  - `lean/AutoMath/Families/ZeroDivisorRingBridges.lean` at the exact sections for
    `f25_ring_support_partition_lemma`,
    `f25_ring_support_adjacency_lemma`,
    `f2_ring_three_interface_reduction`,
    and
    `zp_zp_z2_three_interface_lead_theorem`;
  - exactly six seed records:
    - `artifacts/z13-z25-prime-zero-divisor-graph/record.md`;
    - `artifacts/z17-z25-prime-zero-divisor-graph/record.md`;
    - `artifacts/z5-z5-z2-prime-zero-divisor-graph/record.md`;
    - `artifacts/z7-z7-z2-prime-zero-divisor-graph/record.md`;
    - `artifacts/z11-z11-z2-prime-zero-divisor-graph/record.md`;
    - `artifacts/z13-z13-z2-prime-zero-divisor-graph/record.md`.
- Web use in this pass: none.
- Statement lock conclusion:
  - the lead `F2` slice is already closed exactly at ring level in Lean;
  - the live generalization problem is now purely on the four-class `F25` arithmetic wrapper, not on the ring-to-support bridge.

## existing_instance_inventory

- Lean-backed exact baseline from `PROOFS.md`:
  - `F25(3)`, `F25(5)`, `F25(7)`;
  - `F2(5)`, `F2(7)`.
- `F2` seed chain read in this pass:
  - `F2(5)`:
    - fixes the six support classes `A,B,C,D,E,F`;
    - shows the hinge move `C = 1`;
    - reduces the graph to the three live interfaces `A-B`, `A-F`, and `B-E`.
  - `F2(7)`:
    - keeps the same six-class decomposition and same interface list;
    - realizes the template with `A ∪ E` using only `{2,3}`-smooth labels and `B ∪ F` avoiding `2` and `3`.
  - `F2(11)`:
    - gives the first clean count-based feeder for the naive `{2,3}`-smooth reservoir;
    - there are `21` nontrivial `{2,3}`-smooth labels up to `141`, one spare beyond the `20` labels needed for `A ∪ E`.
  - `F2(13)`:
    - closes the first zero-slack boundary of the same template;
    - there are exactly `24` nontrivial `{2,3}`-smooth labels up to `193`, exactly matching `|A ∪ E| = 24`.
- `F25` seed chain visible from `PROOFS.md` plus the read seed records:
  - `F25(3)`, `F25(5)`, and `F25(7)` already sit on the same four support classes `A,B,C,D` with edge pattern `A-C`, `B-B`, `B-C`, `B-D`.
  - `F25(13)`:
    - the old upper-half-only `C` rule fails for the first time;
    - the repaired witness uses below-half `C` primes `37` and `41`;
    - the only new forbidden labels are their doubles `74` and `82`, and those are pushed into `D`;
    - the fixed barrier `B = {1,19,23,29}` creates six spill labels into `A`.
  - `F25(17)`:
    - the same support geometry persists unchanged;
    - the repaired witness now tolerates four below-half `C` primes `37,41,43,47`;
    - their only interval spill labels are `74,82,86,94`, again pushed into `D`;
    - the same barrier `B = {1,19,23,29}` now creates nine spill labels into `A`.
- Inventory conclusion:
  - the `F2` line now supports a closed exact theorem slice, not merely a feeder pattern;
  - the `F25` line supports a stable repaired template through `p = 17`, but still lacks a quantified family theorem or a sharp obstruction theorem.

## shared_structure

- Common decomposition / invariant / construction across the campaign:
  - partition nonzero zero-divisors by coordinate-support type;
  - translate ring-level zero product into adjacency on a tiny support graph;
  - use classwise interchangeability, since vertices inside one support class have identical neighborhoods;
  - reduce the exact graph-labeling problem to coprimality on a short list of support interfaces.
- Shared structure on `F2(p)`:
  - support classes and sizes:
    - `A = (*,0,0)`, size `p - 1`;
    - `B = (0,*,0)`, size `p - 1`;
    - `C = (0,0,1)`, size `1`;
    - `D = (*,*,0)`, size `(p - 1)^2`;
    - `E = (*,0,1)`, size `p - 1`;
    - `F = (0,*,1)`, size `p - 1`.
  - exact edge families:
    - `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`.
  - common invariant:
    - `C` is the singleton hinge;
    - once `C` gets label `1`, the edges `A-C`, `B-C`, and `C-D` are automatic;
    - the entire `D` block becomes free;
    - the only live arithmetic interfaces are `A-B`, `A-F`, and `B-E`.
- Shared structure on `F25(p)`:
  - support classes and sizes:
    - `A = {(0,u) : u in Z_25^x and 5 does not divide u}`, size `20`;
    - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`;
    - `C = {(a,0) : a in Z_p^x}`, size `p - 1`;
    - `D = {(a,5t) : a in Z_p^x, t in {1,2,3,4}}`, size `4(p - 1)`.
  - exact edge families:
    - `A-C`, `B-B`, `B-C`, `B-D`.
  - common invariant:
    - `B` is a sparse pairwise-coprime barrier clique;
    - `C` is the prime-carrying block;
    - `A` is the fixed `20`-slot spill buffer;
    - `D` is the residual reservoir and also absorbs the nontrivial multiples of the below-half `C` exceptions.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  - the support partitions for `F2(p)` and `F25(p)`;
  - the ring-to-support adjacency reductions already preserved in `ZeroDivisorRingBridges.lean`;
  - classwise interchangeability inside each support class;
  - on `F2`, the hinge move `C = 1` and the reduction to the three live interfaces `A-B`, `A-F`, and `B-E`;
  - on `F25`, the fixed barrier-versus-reservoir skeleton with `|A| = 20` and `|B| = 4`.
- Steps that are still parameter-sensitive and not yet closed as family theorems:
  - on `F2`, any attempt to go beyond the exact reduction theorem to a full all-odd-prime prime-labeling theorem;
  - on `F25`, a quantified supply law for `p - 1` prime labels on `C` allowing bounded below-half spill into `D`;
  - on `F25`, a compatibility lemma showing that barrier spill from `B` plus spill avoidance for `C` still fits inside the fixed `20` slots of `A`.
- Steps that are instance-specific:
  - the explicit `{2,3}`-smooth witness lists in `F2(5)`, `F2(7)`, `F2(11)`, and `F2(13)`;
  - the concrete prime choices on `C` in `F25(13)` and `F25(17)`;
  - the current barrier choice `B = {1,19,23,29}` on the four-class line.
- Strongest plausible theorem slice:
  - the exact ring-level three-interface theorem
    `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`.
- Smallest likely counterexample or obstruction:
  - already proved template obstruction:
    - the old upper-half-only `C` wrapper on `F25` breaks first at `p = 13`;
  - next live repaired-wrapper discriminator:
    - `z19-z25-prime-zero-divisor-graph`;
  - next one if `p = 19` survives:
    - `z23-z25-prime-zero-divisor-graph`.

## candidate_theorem_slices

- Slice A:
  - exact ring-level theorem on `F2(p)`:
    once the singleton support class `C` gets label `1`, coprimality on `A-B`, `A-F`, and `B-E` forces coprimality on every zero-product edge.
- Slice B:
  - sufficient-condition corollary on `F2(p)`:
    if `{1,...,p^2 + 2p - 2}` contains `2(p - 1)` labels supported on a fixed small prime set `S` and another `2(p - 1)` labels avoiding every prime in `S`, then `Γ(Z_p × Z_p × Z_2)` is prime after setting `C = 1`.
- Slice C:
  - sufficient-condition theorem on `F25(p)`:
    if `{1,...,5p + 19}` admits a `C` block of `p - 1` prime labels whose nontrivial interval multiples stay out of `A ∪ B`, together with a four-label pairwise-coprime barrier on `B` whose spill still fits in `A`, then `Γ(Z_p × Z_25)` is prime.
- Slice D:
  - sharp obstruction theorem on `F25` for the discarded old wrapper:
    the upper-half-only `C` subtemplate fails first at `p = 13`, even though the graph itself remains prime after repair.
- Slice E:
  - repaired-wrapper obstruction theorem on `F25`:
    if the bounded-spill picture fails next, the first honest place to package that failure is `p = 19`, not a vague "small primes only" statement.

## chosen_slice

- Chosen slice:
  - Slice A.
- Proposed theorem slice:
  - For every odd prime `p`, if a labeling of `Γ(Z_p × Z_p × Z_2)` assigns label `1` to the singleton support class `C` and is coprime across `A-B`, `A-F`, and `B-E`, then every zero-product edge between nonzero zero-divisor vertices is automatically labeled by coprime integers.
- Why this is the strongest honest slice now:
  - it is already preserved exactly as
    `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`;
  - it is uniform in `p`;
  - it uses only the genuinely scalable support partition, adjacency reduction, singleton hinge, and three live interfaces;
  - it matches the exact lead target in `selected_problem.md`.
- Overclaim boundary:
  - this is not a theorem that `Γ(Z_p × Z_p × Z_2)` is prime for all odd primes;
  - this is not a theorem on the full ambient family `Γ(Z_p × Z_p × Z_q)`;
  - this pass does not claim a quantified positive theorem on `Γ(Z_p × Z_25)`.

## reusable_lemmas

- Reusable lemmas already supporting the chosen slice:
  - `f2_ring_support_partition_lemma`;
  - `f2_ring_support_adjacency_lemma`;
  - `support_decomposition_F2`;
  - `singleton_one_lemma`;
  - `three_interface_pack_lemma`;
  - `f2_ring_nonhinge_edge_reduction`;
  - `f2_ring_three_interface_reduction`;
  - `zp_zp_z2_three_interface_lead_theorem`.
- Reusable companion setup already preserved on the four-class line:
  - `support_decomposition_F25`;
  - `f25_ring_support_partition_lemma`;
  - `f25_ring_support_adjacency_lemma`;
  - `zp_z25_support_template_reduction`;
  - the dossier-level arithmetic templates
    `pairwise_coprime_clique_lemma`,
    `classwise_template_lemma`,
    and
    `forbidden_multiples_reservoir_lemma`.
- Next reusable lemma targets still needed for the open `F25` line:
  - a quantified small-spill lemma for choosing the `C` block;
  - a barrier-reservoir compatibility lemma showing the total spill still fits inside the fixed `20`-slot `A` buffer;
  - a wrapper theorem combining those arithmetic lemmas with the already-preserved ring-support bridge.

## proof_plan

- Main proof path for the chosen slice:
  1. classify each nonzero zero-divisor of `Γ(Z_p × Z_p × Z_2)` into the six support classes `A,B,C,D,E,F`;
  2. reduce any ring-level zero-product edge to one of `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, or `C-D`;
  3. assign label `1` to the singleton class `C`;
  4. discharge `A-C`, `B-C`, and `C-D` automatically;
  5. keep only the three nontrivial interfaces `A-B`, `A-F`, and `B-E`;
  6. conclude by `zp_zp_z2_three_interface_lead_theorem`.
- One strongest path forward:
  - keep the exact `F2` slice fixed as the publication anchor;
  - use `F2(5)`, `F2(7)`, `F2(11)`, and `F2(13)` only as feeder evidence that the same mechanism is stable from loose to zero-slack arithmetic;
  - spend the next campaign cycle on the `F25` arithmetic wrapper, not on reopening the already-preserved structural bridge.
- One fallback path:
  - if the quantified `F25` wrapper still does not close, do not broaden the `F2` claim;
  - instead package the first sharp repaired-wrapper obstruction theorem on the four-class line.

## fallback_counterexample_plan

- Best generalized conjecture / template on the unresolved `F25` line:
  - `Γ(Z_p × Z_25)` should be prime whenever `{1,...,5p + 19}` admits:
    - a `C` block of `p - 1` prime labels with only bounded below-half spill, and every nontrivial interval multiple of a `C`-prime kept out of `A ∪ B` and absorbed by `D`;
    - a four-label pairwise-coprime barrier set on `B`;
    - enough room in `A` to absorb every nontrivial multiple of the barrier labels.
- Strongest preserved obstruction:
  - the old upper-half-only `C` wrapper already fails at `p = 13`;
  - this is a template obstruction, not a graph-level non-primality claim.
- Smallest likely counterexample or obstruction for the repaired wrapper:
  - `p = 19` is the first live place where the repaired bounded-spill picture is likely to fail sharply enough to package;
  - if `p = 19` survives, then `p = 23` is the next discriminator.
- Fallback theorem shape:
  - a first sharp repaired-wrapper obstruction theorem for `Γ(Z_p × Z_25)`, phrased at the template level rather than as a claim that the graph family itself is non-prime.

## next_best_feeder_instances

- `z19-z25-prime-zero-divisor-graph`
  - smallest post-`17` stress test for the repaired four-class wrapper;
  - best discriminator between a real bounded-spill family mechanism and a still-local repair.
- `z23-z25-prime-zero-divisor-graph`
  - immediate follow-up if `p = 19` survives;
  - best next test of whether spill growth still fits the fixed `20`-slot `A` buffer.
- No further `F2` feeder is needed before the next publication decision:
  - the exact slice is already fixed there;
  - the unresolved discriminator is entirely on the `F25` line.

## publication_value

- Proposed theorem slice:
  - `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`.
- Proof plan:
  - package the `F2` family section as support partition plus adjacency bridge plus singleton hinge plus three-interface theorem;
  - then add the `F25` program only as the next open arithmetic wrapper problem, with preserved exact feeders at `p = 13` and `p = 17`.
- One strongest path forward:
  - publish around the exact `F2` slice now, then thicken the campaign by either closing the quantified `F25` bounded-spill theorem or sharply breaking it.
- One fallback path:
  - if the `F25` line does not close at `p = 19`, package the repaired-wrapper obstruction theorem rather than stretching to a broader positive theorem.
- Honest publication reading:
  - the campaign is beyond `INSTANCE_ONLY` because one real parameterized slice is exact and preserved;
  - the campaign is not `PAPER_READY` because the companion `F25` line still needs either a quantified bounded-spill theorem or a first sharp repaired-wrapper obstruction theorem.
- Current publication stance:
  - `publication_status = SLICE_EXACT` is honest for this family after the current GENERALIZE pass;
  - `proof_artifacts_preserved = true` is honest because the exact `F2` slice, the local seed chain, the `F25` bridge, and the live fallback targets are all preserved in-repo.

## publication_prior_art_audit

- Exact-statement search:
  - searched the exact family line `Γ(Z_p × Z_p × Z_2)` with `prime labeling`, `zero-divisor graph`, and the repo's three-interface wording;
  - searched the companion four-class line `Γ(Z_p × Z_25)` and alternate square notation `Γ(Z_p × Z_(5^2))` with `prime labeling`;
  - within budget, no earlier primary-source statement matching the repo's exact ring-level three-interface theorem or a quantified `F25` wrapper surfaced.
- Alternate-notation search:
  - searched `Γ(Z_2 × Z_p × Z_p)` and `Γ(F_p × F_p × F_2)` with `prime labeling`;
  - within budget, no public statement of the exact `F2` slice surfaced.
- Canonical source search:
  - the controlling source remains Fox and Mooney, `On Prime Labelings of Zero-Divisor Graphs`, published online `2025-11-21`;
  - inside that source, nearby families are solved, but the ambient lines `Γ(Z_p × Z_p × Z_q)` and `Γ(Z_p × Z_(q^2))` are still posed as Conjectures `4.3` and `4.4`;
  - within the canonical source, no theorem / proposition / example / corollary / observation / sufficient-condition statement already settles the repo's exact `F2` slice or the open `F25` wrapper.
- Outside-source status search:
  - checked the older direct-product structural literature through Axtell, Stickles, and Warfel, `Zero-divisor graphs of direct products of commutative rings` (`2006`);
  - that source treats background zero-divisor-graph structure for direct products, not prime labelings, so the support-partition / adjacency bridge should be treated as setup rather than as the novelty claim.
- Recent discussion / follow-up check:
  - checked the AMS Special Session abstract `On Prime Labelings of Zero-Divisor Graphs`, dated `2025-03-09`;
  - within budget, no later public citation / discussion / follow-up closing Conjectures `4.3` or `4.4` surfaced.
- Prior-art verdict:
  - no rediscovery is established within the bounded audit;
  - novelty confidence is only `medium`, because the literature pass was intentionally narrow and claim-specific.

## publication_statement_faithfulness

- The strongest honest claim is not `Γ(Z_p × Z_p × Z_2)` is prime for all odd primes `p`.
- The strongest honest claim is the exact ring-level reduction theorem
  `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`:
  once the singleton support class `C` gets label `1`, the only live arithmetic obligations are the three interfaces `A-B`, `A-F`, and `B-E`, and those suffice to discharge every zero-product edge.
- This is faithful to the intended graph-level object:
  - the theorem is still about the full zero-divisor graph on nonzero zero-divisor vertices;
  - the support classes are proof scaffolding, not a substitute quotient graph.
- The companion `Γ(Z_p × Z_25)` line remains outside the strongest claim:
  - it has real feeder evidence and a preserved ring-support bridge;
  - it does not yet have a closed quantified theorem or sharp obstruction theorem.
- Referee-facing statement check:
  - this would survive the question `what is the theorem?` only when presented as a reduction theorem slice, not as a full closure of the ambient family.

## publication_theorem_worthiness

- Is the strongest honest claim stronger than `here is an example`?
  - Yes. It is uniform in the parameter `p` and is not tied to any one witness instance.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here?
  - Yes. There is a real exact theorem slice on `F2(p) = Γ(Z_p × Z_p × Z_2)`.
  - Not yet on `F25(p) = Γ(Z_p × Z_25)`: that line is still feeder-backed and theorem-candidate only.
- Is the proof structural or merely instance-specific?
  - On the `F2` slice, the proof is structural: support partition, ring-to-support adjacency reduction, singleton hinge, and three live interfaces.
  - On the `F25` line, the current arithmetic evidence is still too instance-dependent.
- Would this survive a referee asking `what is the theorem?`
  - Yes for the exact `F2` reduction theorem.
  - No for any broader combined-family claim beyond that exact slice.
- Is the claim still too dependent on hand-picked small cases?
  - The exact `F2` slice is not.
  - The live `F25` route still is, because its current strength comes from feeders at `p = 13` and `p = 17` plus an unclosed wrapper conjecture.
- Is the generalization route strong enough to merit campaign priority?
  - Yes. The `F25` line now has preserved bridge lemmas, a known first break of the old wrapper at `p = 13`, and a repaired feeder surviving at `p = 17`, so it is still the correct next publication target.

## publication_publishability

- Conservative verdict:
  - `publication_status = SLICE_EXACT` remains honest.
  - `publication_status = PAPER_READY` would be an overclaim.
- Why it is not `INSTANCE_ONLY`:
  - the family now contains a real exact parameterized theorem slice, not merely isolated exact examples.
- Why it is not `PAPER_READY`:
  - the current exact slice is substantial enough for a theorem section, but still thin as a standalone publication claim;
  - the campaign still needs paper-scale mass on the four-class `Γ(Z_p × Z_25)` line, either as a quantified bounded-spill theorem or as a first sharp repaired-wrapper obstruction theorem;
  - bounded prior-art checking did not prove novelty beyond doubt, so publication confidence should be kept at `medium`.
- Honest publication reading:
  - this is structural and theorem-worthy;
  - it is not yet a complete paper package.
- Campaign priority reading:
  - keep the campaign hot, because the open `F25` line is now the only live blocker between a real slice result and a paper-shaped family story.

## strongest_honest_claim

- The strongest honest current family claim is the exact Lean-backed theorem slice
  `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`:
  for every odd prime `p`, if the singleton support class `C` in `Γ(Z_p × Z_p × Z_2)` receives label `1` and the three live interfaces `A-B`, `A-F`, and `B-E` are pairwise coprime, then every zero-product edge between nonzero zero-divisor vertices is automatically labeled by coprime integers.
- This is a real parameterized reduction theorem.
- It is not yet a theorem that `Γ(Z_p × Z_p × Z_2)` is prime for all odd primes `p`.

## paper_title_hint

- `A Three-Interface Reduction Theorem for Prime Labelings of Γ(Z_p × Z_p × Z_2)`

## next_action

- Keep `zp_zp_z2_three_interface_lead_theorem` fixed as the exact publication anchor.
- Do not broaden the headline claim beyond that exact slice.
- Spend the next family cycle on the four-class `Γ(Z_p × Z_25)` wrapper:
  - try to close the quantified bounded-spill / barrier-reservoir theorem;
  - if it still will not close cleanly, run `z19-z25-prime-zero-divisor-graph` as the first sharp repaired-wrapper discriminator, then `z23-z25-prime-zero-divisor-graph` if needed.

## lean_statement

- Selected Lean target:
  - `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`.
- Exact family-facing statement formalized in this stage:
  - for every odd prime `p`, if a labeling on the nonzero zero-divisor vertices of `Γ(Z_p × Z_p × Z_2)` assigns label `1` to the singleton support class `C` and is coprime on the three live interfaces `A-B`, `A-F`, and `B-E`, then every zero-product edge is automatically labeled by coprime integers.
- Artifact-local mirror preserved for the family dossier:
  - `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f2_slice`
    in `artifacts/families/zero_divisor_prime_labelings/lean/ZeroDivisorF2Slice.lean`.
- Overclaim boundary:
  - this is not a theorem that `Γ(Z_p × Z_p × Z_2)` is prime for all odd primes `p`;
  - this Lean pass does not claim a quantified positive theorem on `Γ(Z_p × Z_25)`.

## lean_skeleton

- The proof skeleton for the closed `F2` slice is:
  1. use `f2_ring_support_partition_lemma` to place each endpoint of a zero-product edge into one of the six support classes `A,B,C,D,E,F`;
  2. use `f2_ring_support_adjacency_lemma` and `support_decomposition_F2` to reduce ring-level adjacency to the finite support-edge list;
  3. use the singleton hinge hypothesis `hC1` to discharge every edge touching `C`, namely `A-C`, `B-C`, and `C-D`;
  4. use `f2_ring_nonhinge_edge_reduction` to show that every remaining zero-product edge lies on one of the three live interfaces `A-B`, `A-F`, or `B-E`, together with reversals;
  5. finish by the abstract support-template wrapper
     `ZeroDivisorReductions.zp_zp_z2_support_template_reduction_of_singleton_one`.
- The artifact-local mirror theorem keeps the same statement and closes by a direct invocation of
  `zp_zp_z2_three_interface_lead_theorem`.

## lean_result

- Backend check:
  - `cd lean && lake build AutoMath.Families.ZeroDivisorRingBridges` succeeded in the current repo state.
- Artifact-local mirror check:
  - `cd lean && lake env lean ../artifacts/families/zero_divisor_prime_labelings/lean/ZeroDivisorF2Slice.lean` succeeded in the current repo state.
- Honest Lean-stage verdict:
  - the current family Lean target is already fully formalized and checked;
  - no new axioms, `sorry`, `admit`, or placeholders were introduced in this pass;
  - the strongest honest family claim stays the exact theorem slice `zp_zp_z2_three_interface_lead_theorem`;
  - `classification = CANDIDATE` remains conservative and `publication_status = SLICE_EXACT` remains the honest publication-facing status.

## lean_blockers

- No Lean blocker remains on the closed `F2` theorem slice itself.
- The live blocker is unchanged and belongs to the four-class `Γ(Z_p × Z_25)` line:
  - the repo still lacks either a quantified small-spill / barrier-reservoir family theorem or a first sharp repaired-wrapper obstruction theorem on the repaired wrapper.
- Because that `F25` line is still open, this campaign is not yet `PAPER_READY`.
