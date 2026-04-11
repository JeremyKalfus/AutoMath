# Family Record: zero_divisor_prime_labelings

## family_statement_lock

- Active `family_slug`: `zero_divisor_prime_labelings`.
- Dossier path: `campaigns/zero_divisor_prime_labelings.md`.
- Family artifact path: `artifacts/families/zero_divisor_prime_labelings`.
- Locked family statements for this PUBLICATION_AUDIT pass:
  - `F2(p) := Γ(Z_p × Z_p × Z_2)` for odd primes `p`;
  - `F25(p) := Γ(Z_p × Z_25)` for odd primes `p`.
- Locked theorem target from `selected_problem.md`:
  - keep `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem` fixed as the exact lead slice.
- Locked fallback target from `selected_problem.md`:
  - close a quantified bounded-spill plus barrier-reservoir wrapper on `Γ(Z_p × Z_25)`, or else package the first sharp repaired-wrapper obstruction theorem.
- Bounded local read log for this pass:
  - `AGENTS.md`;
  - `selected_problem.md`;
  - `campaigns/zero_divisor_prime_labelings.md`;
  - `artifacts/families/zero_divisor_prime_labelings/record.md`;
  - `artifacts/families/zero_divisor_prime_labelings/status.json`;
  - `PROOFS.md` at the exact sections for `z3-z25-prime-zero-divisor-graph`, `z5-z25-prime-zero-divisor-graph`, `z7-z25-prime-zero-divisor-graph`, `z5-z5-z2-prime-zero-divisor-graph`, and `z7-z7-z2-prime-zero-divisor-graph`;
  - `lean/AutoMath/Families/ZeroDivisorReductions.lean` at the exact sections for `singleton_one_lemma`, `three_interface_pack_lemma`, and `zp_zp_z2_support_template_reduction_of_singleton_one`;
  - `lean/AutoMath/Families/ZeroDivisorRingBridges.lean` at the exact sections for `f25_ring_support_partition_lemma`, `f25_ring_support_adjacency_lemma`, `f2_ring_support_partition_lemma`, `f2_ring_support_adjacency_lemma`, `f2_ring_nonhinge_edge_reduction`, `f2_ring_three_interface_reduction`, and `zp_zp_z2_three_interface_lead_theorem`;
  - exactly four seed artifacts:
    - `artifacts/z13-z25-prime-zero-divisor-graph/record.md`;
    - `artifacts/z17-z25-prime-zero-divisor-graph/record.md`;
    - `artifacts/z11-z11-z2-prime-zero-divisor-graph/record.md`;
    - `artifacts/z13-z13-z2-prime-zero-divisor-graph/record.md`.
- Deliberately not opened in this bounded pass:
  - `artifacts/z5-z5-z3-prime-zero-divisor-graph/record.md`;
  - `artifacts/z2-power-8-prime-zero-divisor-graph/record.md`.
  Reason: they support the campaign background but do not discriminate between the locked `F2` lead slice and the live `F25` wrapper question.
- Web use in this pass:
  - bounded and claim-specific only;
  - Fox-Mooney, `On Prime Labelings of Zero-Divisor Graphs`, as the canonical source check;
  - Axtell-Stickles-Warfel, `Zero-divisor graphs of direct products of commutative rings`, as the outside structural status check;
  - the `2026` follow-up paper `On properties and topological indices of the zero divisor graph for direct product of some commutative rings` as the recent status check.
- Statement-lock conclusion:
  - the lead `F2` slice is already closed exactly at ring level in Lean;
  - the `F25` ring-to-support bridge is also already preserved in Lean;
  - the remaining open campaign question is therefore not the structural bridge but the quantified arithmetic wrapper on the four-class `F25` line;
  - the `selected_problem.md` hint that `Γ(Z_17 × Z_25)` is the next unread stress test is stale relative to the preserved artifacts, because `z17-z25-prime-zero-divisor-graph` is already on disk as a verified feeder;
  - the smallest live four-class discriminator is now `z19-z25-prime-zero-divisor-graph`.

## existing_instance_inventory

- Lean-backed exact baseline from `PROOFS.md`:
  - `F25(3)`, `F25(5)`, `F25(7)`;
  - `F2(5)`, `F2(7)`.
- What the baseline exacts already lock in:
  - the four-class `F25` support geometry `A,B,C,D` with edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  - the six-class `F2` support geometry `A,B,C,D,E,F` with hinge class `C` and live interfaces `A-B`, `A-F`, `B-E` after setting `C = 1`.
- `F2` feeder chain read in this pass:
  - `F2(11)`:
    - gives the first clean count-based feeder for the naive `{2,3}`-smooth reservoir;
    - there are `21` nontrivial `{2,3}`-smooth labels up to `141`, one spare beyond the `20` labels needed for `A ∪ E`.
  - `F2(13)`:
    - closes the first zero-slack boundary of the same template;
    - there are exactly `24` nontrivial `{2,3}`-smooth labels up to `193`, exactly matching `|A ∪ E| = 24`.
- `F25` feeder chain read in this pass:
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
  - the `F2` line now supports a real exact theorem slice, not merely a feeder pattern;
  - the `F25` line now has repaired-wrapper feeder evidence through `p = 17`, but it still lacks a quantified theorem or a first sharp repaired-wrapper obstruction theorem.

## shared_structure

- Common decomposition / invariant / construction:
  - partition nonzero zero-divisors by coordinate-support type;
  - translate ring-level zero product into adjacency on a tiny support graph;
  - use classwise interchangeability, since vertices inside one support class have identical neighborhoods;
  - reduce the full graph-labeling problem to coprimality on a short list of support interfaces.
- Shared structure on `F2(p)`:
  - support classes and sizes:
    - `A = (*,0,0)`, size `p - 1`;
    - `B = (0,*,0)`, size `p - 1`;
    - `C = (0,0,1)`, size `1`;
    - `D = (*,*,0)`, size `(p - 1)^2`;
    - `E = (*,0,1)`, size `p - 1`;
    - `F = (0,*,1)`, size `p - 1`.
  - exact edge families:
    - `A-B`;
    - `A-C`;
    - `A-F`;
    - `B-C`;
    - `B-E`;
    - `C-D`.
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
    - `A-C`;
    - `B-B`;
    - `B-C`;
    - `B-D`.
  - common invariant:
    - `B` is a sparse pairwise-coprime barrier clique;
    - `C` is the prime-carrying block;
    - `A` is the fixed `20`-slot spill buffer;
    - `D` is the residual reservoir and also absorbs the nontrivial multiples of the below-half `C` exceptions.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  - the ring-to-support partition lemmas for `F2(p)` and `F25(p)`;
  - the ring-to-support adjacency lemmas for `F2(p)` and `F25(p)`;
  - classwise interchangeability inside each support class;
  - on `F2`, the hinge move `C = 1` and the reduction to the three live interfaces `A-B`, `A-F`, and `B-E`;
  - on `F25`, the fixed barrier-versus-reservoir skeleton with `|A| = 20` and `|B| = 4`.
- Steps that are still parameter-sensitive and not yet closed as family theorems:
  - on `F25`, a quantified supply law for `p - 1` prime labels on `C` allowing bounded below-half spill into `D`;
  - on `F25`, a compatibility lemma showing that barrier spill from `B` plus spill avoidance for `C` still fits inside the fixed `20` slots of `A`;
  - on `F2`, any attempt to go beyond the exact reduction theorem to a full all-odd-prime prime-labeling theorem.
- Steps that are instance-specific:
  - the explicit `{2,3}`-smooth witness lists in `F2(11)` and `F2(13)`;
  - the concrete prime choices on `C` in `F25(13)` and `F25(17)`;
  - the current barrier choice `B = {1,19,23,29}` on the four-class line.
- Strongest plausible theorem slice:
  - the exact ring-level theorem
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
  - sharp obstruction theorem on `F25` for the repaired wrapper:
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
  - `support_decomposition_F2`;
  - `singleton_one_lemma`;
  - `three_interface_pack_lemma`;
  - `f2_ring_support_partition_lemma`;
  - `f2_ring_support_adjacency_lemma`;
  - `f2_ring_nonhinge_edge_reduction`;
  - `f2_ring_three_interface_reduction`;
  - `zp_zp_z2_three_interface_lead_theorem`.
- Reusable companion setup already preserved on the four-class line:
  - `support_decomposition_F25`;
  - `f25_ring_support_partition_lemma`;
  - `f25_ring_support_adjacency_lemma`;
  - `zp_z25_support_template_reduction`.
- Next reusable lemma targets still needed for the open `F25` line:
  - a quantified small-spill lemma for choosing the `C` block;
  - a barrier-reservoir compatibility lemma showing that barrier spill plus `C`-spill avoidance still fits inside the fixed `20`-slot `A` buffer;
  - a wrapper theorem combining those arithmetic lemmas with the already-preserved ring-support bridge.

## proof_plan

- Main proof path for the chosen slice:
  1. classify each nonzero zero-divisor of `Γ(Z_p × Z_p × Z_2)` into the six support classes `A,B,C,D,E,F`;
  2. reduce any ring-level zero-product edge to one of `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, or `C-D`;
  3. assign label `1` to the singleton class `C`;
  4. discharge `A-C`, `B-C`, and `C-D` automatically via `singleton_one_lemma`;
  5. keep only the three nontrivial interfaces `A-B`, `A-F`, and `B-E`;
  6. conclude by `three_interface_pack_lemma` and
     `zp_zp_z2_three_interface_lead_theorem`.
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
  - then add the `F25` program only as the next open arithmetic wrapper problem, with preserved repaired feeders at `p = 13` and `p = 17`.
- Reusable lemmas:
  - the `F2` slice already has a paper-shaped lemma chain;
  - the `F25` side already has the ring-support bridge but still needs the quantified arithmetic lemmas.
- One strongest path forward:
  - publish around the exact `F2` slice now, then thicken the campaign by either closing the quantified `F25` bounded-spill theorem or sharply breaking it.
- One fallback path:
  - if the `F25` line does not close at `p = 19`, package the repaired-wrapper obstruction theorem rather than stretching to a broader positive theorem.
- Honest publication reading:
  - the campaign is beyond `INSTANCE_ONLY` because one real parameterized slice is exact and preserved;
  - the campaign is not `PAPER_READY` because the companion `F25` line still needs either a quantified bounded-spill theorem or a first sharp repaired-wrapper obstruction theorem.
- Current publication stance:
  - `publication_status = SLICE_EXACT` is honest for this family after the current PUBLICATION_AUDIT pass;
  - `proof_artifacts_preserved = true` is honest because the exact `F2` slice, the local seed chain, the `F25` bridge, and the live fallback targets are all preserved in-repo.

## publication_prior_art_audit

- Audit date:
  - `2026-04-11T15:03:19-04:00`.
- Claim locked for this bounded audit:
  - the exact publication anchor is the ring-level theorem
    `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`;
  - the live companion line is the still-open four-class wrapper program on `Γ(Z_p × Z_25)`.
- Exact-statement search:
  - I searched the direct family statements
    `prime labeling zero-divisor graph Γ(Z_p × Z_p × Z_2)` and
    `prime labeling zero-divisor graph Γ(Z_p × Z_25)`,
    together with the exact feeder notations `Γ(Z_13 × Z_13 × Z_2)`, `Γ(Z_13 × Z_25)`, and `Γ(Z_17 × Z_25)`.
  - Within the bounded pass, those searches surfaced Fox-Mooney as the controlling prime-labeling source plus structural zero-divisor-graph background, but no earlier paper or preprint stating the repo's exact three-interface reduction theorem and no published sufficient-condition theorem obviously subsuming it.
- Alternate-notation search:
  - I also searched the common alternate forms
    `Γ(Z_2 × Z_p × Z_p)`,
    `Γ(F_p × F_p × F_2)`,
    `Γ(Z_p × Z_p × Z_q)`,
    `Γ(Z_p × Z_(q^2))`,
    and `Z_p × Z_5^2`.
  - This was enough to catch the ambient conjectural lines and the common `q^2` notation for the four-class family.
  - Within budget, these searches again led back to Fox-Mooney or to structural direct-product papers rather than to an exact-match theorem slice.
- Canonical source search:
  - the controlling canonical source remains Fox-Mooney,
    `On Prime Labelings of Zero-Divisor Graphs`, published online `2025-11-21`;
  - inside that source, I checked the nearby theorem and open-problem entries most likely to subsume the current claims:
    - `Theorem 2.9` for `Γ(Z_2 × Z_2 × Z_p)`;
    - `Theorem 2.11` for `Γ(Z_3 × Z_3 × Z_p)`;
    - `Theorem 2.14` for `Γ(Z_p × Z_9)`;
    - `Theorem 2.15` for `Γ(Z_2 × Z_(p^2))`;
    - `Conjecture 4.3` for `Γ(Z_p × Z_p × Z_q)`;
    - `Conjecture 4.4` for `Γ(Z_p × Z_(q^2))`.
- Canonical-source implication check:
  - I did not find a theorem, proposition, example, corollary, observation, or sufficient-condition statement in Fox-Mooney that already implies the repo's exact ring-level three-interface theorem on `Γ(Z_p × Z_p × Z_2)`;
  - the same source still treats the ambient `Γ(Z_p × Z_p × Z_q)` and `Γ(Z_p × Z_(q^2))` lines as open, so the repo's lead claim remains a reduction theorem inside those open families rather than a repackaged published corollary.
- Outside-source status search:
  - I checked Axtell-Stickles-Warfel,
    `Zero-divisor graphs of direct products of commutative rings` (`2006`),
    as the structural outside source most likely to collapse the support decomposition to standard folklore.
  - It supplies direct-product zero-divisor-graph structure, but not prime-labeling results that settle either the exact `F2` reduction theorem or the current `Γ(Z_p × Z_25)` wrapper program.
- Recent citation / discussion / follow-up check:
  - I ran one recent follow-up search and found the `2026` structural paper
    `On properties and topological indices of the zero divisor graph for direct product of some commutative rings`, posted `2026-01-19`.
  - The bounded page check showed a structural and topological study of `Γ(Z_(p^m) × Z_(q^n))`, not a prime-labeling closure, and it did not reveal a later public paper closing Fox-Mooney `Conjecture 4.3` or `Conjecture 4.4`.
  - I did not find the repo's exact reduction theorem stated there or in any recent follow-up surfaced within budget.
- Prior-art verdict:
  - bounded audit does not establish rediscovery;
  - bounded audit also does not prove absolute novelty, but the exact `F2` slice still looks live rather than already absorbed by the canonical literature.

## publication_statement_faithfulness

- Is the strongest honest claim stronger than “here is an example”?
  - Yes.
  - The locked `F2` claim is a uniform theorem in the odd prime parameter `p`, not a finite list of examples.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here?
  - Yes.
  - The real theorem slice is the exact ring-level reduction theorem
    `zp_zp_z2_three_interface_lead_theorem`.
- Is the proof structural or merely instance-specific?
  - Structural on the locked `F2` line.
  - The theorem runs through support partition, adjacency reduction, the singleton hinge class, and the three live interfaces, not through hand-picked labels for each `p`.
- What the claim is not:
  - it is not a theorem that `Γ(Z_p × Z_p × Z_2)` is prime for all odd primes;
  - it is not a theorem on the full ambient family `Γ(Z_p × Z_p × Z_q)`;
  - it is not a quantified positive theorem yet on `Γ(Z_p × Z_25)`.
- Faithfulness check:
  - the theorem statement in Lean matches the honest paper-facing wording: once the singleton support class `C` is fixed to label `1`, only the three interfaces `A-B`, `A-F`, and `B-E` remain live;
  - the mirror theorem
    `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f2_slice`
    is preserved locally in the family artifact;
  - the feeder records `F2(11)`, `F2(13)`, `F25(13)`, and `F25(17)` are used only as evidence about scaling pressure, not as substitutes for the theorem.
- Dependence on hand-picked cases:
  - the exact `F2` theorem slice itself is not dependent on hand-picked small cases;
  - the broader publication package still partly is, because the `F25` side remains backed by repaired feeders rather than a closed quantified theorem.

## publication_theorem_worthiness

- Is the strongest honest claim stronger than “here is an example”?
  - Yes.
  - It compresses the full ring graph into a structural three-interface theorem slice valid for every odd prime `p`.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here?
  - Yes.
  - The honest unit is a parameterized theorem slice, not a full family theorem.
- Is the proof structural or merely instance-specific?
  - Structural on the lead `F2` line.
  - The proof runs through support partition, adjacency reduction, singleton hinge, and a three-interface pack lemma, not through a hand-crafted witness for each `p`.
- Would this survive a referee asking “what is the theorem?”
  - Yes, provided the headline theorem is kept exactly at the reduction-theorem level.
  - No, if the paper tries to advertise a stronger all-odd-prime prime-labeling theorem that the repo does not yet prove.
- Is the claim still too dependent on hand-picked small cases?
  - The exact `F2` slice is not.
  - The overall campaign narrative still is, because the companion `F25` story is presently a feeder-supported open wrapper program rather than a theorem.
- Is the generalization route strong enough to merit campaign priority?
  - Yes.
  - The `F25` line already has preserved ring-to-support bridge lemmas and repaired feeders through `p = 17`, so the next test `p = 19` is a genuine theorem-mass discriminator rather than another random exact.
- Theorem-worthiness verdict:
  - `SLICE_EXACT` is justified;
  - `FAMILY_CANDIDATE` would overstate what is actually closed today;
  - `PAPER_READY` would be premature.

## publication_publishability

- Publication reading:
  - the lead `F2` result is theorem-worthy and likely non-rediscovered within the bounded audit;
  - it is also stronger than an instance note because it is an exact uniform reduction theorem.
- Why it is not `PAPER_READY` yet:
  - on its own, the `F2` theorem still reads like a sharp reduction lemma unless the paper frames it against a larger closed theorem, a stronger corollary, or a companion obstruction / wrapper result;
  - the natural companion line `Γ(Z_p × Z_25)` is still missing either a quantified bounded-spill / barrier-reservoir theorem or a first sharp repaired-wrapper obstruction theorem.
- Referee test:
  - a referee asking “what is the theorem?” can be answered cleanly for the `F2` slice;
  - a referee asking “why is this enough for a paper rather than a strong lemma?” still has a live objection until the `F25` side closes positively or obstructively.
- Honest publication outcome:
  - the family is beyond `INSTANCE_ONLY`;
  - the family is not a rediscovery on the current bounded evidence;
  - the family is not yet `PAPER_READY`;
  - the strongest honest status remains `SLICE_EXACT`.
- Best publishable shape now:
  - either a short-note paper centered on the exact `F2` reduction theorem plus a persuasive open-program section, or preferably;
  - a thicker paper package that pairs the exact `F2` slice with a closed positive or obstruction theorem on the four-class `F25` line.

## strongest_honest_claim

- As of `2026-04-11T15:03:19-04:00`, the strongest honest family claim is still the preserved exact Lean theorem
  `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`,
  mirrored by
  `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f2_slice`:
  for every odd prime `p`, if the singleton support class `C` in `Γ(Z_p × Z_p × Z_2)` receives label `1` and the three live interfaces `A-B`, `A-F`, and `B-E` are pairwise coprime, then every zero-product edge between nonzero zero-divisor vertices is automatically labeled by coprime integers.
- Publication reading:
  - this is a genuine parameterized theorem slice and is stronger than “here is an example”;
  - it is not yet a theorem that `Γ(Z_p × Z_p × Z_2)` itself is prime for all odd `p`;
  - it sits naturally inside Fox-Mooney `Conjecture 4.3` rather than closing it;
  - the refreshed bounded prior-art pass did not reveal an earlier source already stating this exact reduction theorem;
  - this audit confirms preserved source artifacts in-repo, but it did not freshly re-run `lake` in this pass.

## paper_title_hint

- `A Three-Interface Reduction Theorem for Prime Labelings of Γ(Z_p × Z_p × Z_2)`

## next_action

- Keep `zp_zp_z2_three_interface_lead_theorem` fixed as the exact publication anchor and do not broaden the headline claim beyond that reduction theorem.
- Do not spend the next cycle reopening the `F2` bridge: the preserved exact slice is already the right anchor.
- Treat the `Γ(Z_17 × Z_25)` hint in `selected_problem.md` as stale relative to the preserved artifacts: that feeder is already on disk and already part of the family evidence.
- Move the next family cycle to the four-class `Γ(Z_p × Z_25)` arithmetic wrapper above the already-preserved ring-support bridge.
- Either prove the quantified small-spill plus barrier-reservoir theorem from the preserved `p = 13` and `p = 17` feeders, or run `z19-z25-prime-zero-divisor-graph` as the first sharp repaired-wrapper discriminator, with `z23-z25-prime-zero-divisor-graph` next if `p = 19` survives.
- If the wrapper closes, package that theorem beside the exact `F2` slice.
- If the wrapper breaks, package the first sharp repaired-wrapper obstruction theorem instead of stretching to an all-`p` claim.

## lean_statement

- Lean target kept fixed for this pass:
  `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`.
- Exact statement formalized and preserved:
  for every odd prime `p`, if a labeling on `F2RingElem p` assigns label `1` to every vertex in the singleton support class `C`, and is coprime across the three live interfaces `A-B`, `A-F`, and `B-E`, then every zero-product edge between nonzero zero-divisor vertices of `Γ(Z_p × Z_p × Z_2)` receives coprime labels.
- Artifact-local mirror kept fixed:
  `artifacts/families/zero_divisor_prime_labelings/lean/ZeroDivisorF2Slice.lean`
  under theorem
  `AutoMath.Families.ZeroDivisorPrimeLabelings.family_zero_divisor_prime_labelings_f2_slice`.

## lean_skeleton

- Proof skeleton kept fixed rather than broadened:
  1. `f2_ring_support_partition_lemma` classifies every nonzero zero-divisor into one of `A,B,C,D,E,F`;
  2. `f2_ring_support_adjacency_lemma` converts ring multiplication-zero into the abstract support adjacency relation;
  3. `f2_support_edge_cases` enumerates the only possible support-interface edge shapes;
  4. `f2_ring_nonhinge_edge_reduction` shows that once neither endpoint lies in `C`, only the three live interfaces remain;
  5. `ZeroDivisorReductions.zp_zp_z2_support_template_reduction_of_singleton_one` discharges the `C`-touching edges automatically from `label = 1` on `C`;
  6. `f2_ring_three_interface_reduction` packages the ring-level reduction;
  7. `zp_zp_z2_three_interface_lead_theorem` is the publication-facing exact slice.
- Conservative Lean choice for this pass:
  no new broader theorem was introduced, because the strongest honest family target was already the checked three-interface slice and the open blocker is on the `F25` arithmetic wrapper, not on the `F2` ring bridge.

## lean_result

- Fresh local rerun attempt in this audit:
  - `cd lean && lake build AutoMath.Families.ZeroDivisorRingBridges`
  - result on `2026-04-11`: failed before proof checking because the local Lean toolchain attempted network dependency resolution and could not resolve `github.com` in this environment.
- Preserved formal evidence still present in-repo:
  - source theorem chain at `lean/AutoMath/Families/ZeroDivisorRingBridges.lean` with the named bridge and lead theorems intact;
  - compiled backend artifacts already present at
    `lean/.lake/build/lib/lean/AutoMath/Families/ZeroDivisorRingBridges.olean` and
    `lean/.lake/build/lib/lean/AutoMath/Families/ZeroDivisorRingBridges.ilean`;
  - artifact-local mirror theorem preserved at
    `artifacts/families/zero_divisor_prime_labelings/lean/ZeroDivisorF2Slice.lean`.
- Outcome:
  - this pass confirms preservation of the exact `F2` slice and its formal artifact chain, not a fresh clean-room rerun;
  - no new axioms, `sorry`, `admit`, or placeholders were introduced in this pass.
- Classification consequence:
  - keep family `classification = CANDIDATE`;
  - keep `publication_status = SLICE_EXACT`;
  - do not touch `PROOFS.md`, because this run did not earn a new exact-instance `EXACT` result.

## lean_blockers

- No Lean blocker remains on the locked `F2` theorem slice itself.
- The live campaign blocker is unchanged:
  the four-class `Γ(Z_p × Z_25)` line still lacks either
  - a quantified small-spill / barrier-reservoir wrapper theorem, or
  - a first sharp repaired-wrapper obstruction theorem.
- Because that blocker is outside the currently checked `F2` slice, this LEAN pass stops after preserving the checked theorem and mirror.
