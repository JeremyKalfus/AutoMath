# Family Record: zero_divisor_prime_labelings

## family_statement_lock

- Active `entry_type`: `family_campaign`.
- Active `family_slug`: `zero_divisor_prime_labelings`.
- Active `family_name`: `Prime labelings of zero-divisor graph families`.
- Dossier path: `campaigns/zero_divisor_prime_labelings.md`.
- Canonical family artifact path: `artifacts/families/zero_divisor_prime_labelings`.
- This pass is canonical `generalize`, not sidecar mode. `selected_problem.md` does not specify `attempt_kind`, `attempt_output_markdown`, or `attempt_output_json`.
- Locked family statements:
  - `F25(p) := Γ(Z_p × Z_25)` for odd prime `p`.
  - `F2(p) := Γ(Z_p × Z_p × Z_2)` for odd prime `p`.
- Closed paper core already preserved in Lean:
  - `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`.
- Current theorem target for this pass:
  - keep the paired exact slice as the closed paper core;
  - push only the direct finite-range `F25` corollary for odd primes `59 <= p <= 97` by combining
    `AutoMath.Families.ZeroDivisorF25FrozenWrapper.exists_fixedC0_subset_card_eq_C_size_of_p_le_97`
    with one missing injection / extension theorem into
    `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`.
- Bounded local inputs used:
  - `AGENTS.md`;
  - `selected_problem.md`;
  - `campaigns/zero_divisor_prime_labelings.md`;
  - canonical family `record.md` and `status.json`;
  - `PROOFS.md`;
  - theorem windows in
    `lean/AutoMath/Families/ZeroDivisorPublicationSlice.lean`,
    `lean/AutoMath/Families/ZeroDivisorF25FrozenWrapper.lean`,
    and
    `lean/AutoMath/Families/ZeroDivisorRingBridges.lean`;
  - six seed artifacts:
    `z13-z25-prime-zero-divisor-graph`,
    `z17-z25-prime-zero-divisor-graph`,
    `z71-z25-prime-zero-divisor-graph`,
    `z97-z25-prime-zero-divisor-graph`,
    `z101-z25-prime-zero-divisor-graph`,
    and
    `z13-z13-z2-prime-zero-divisor-graph`.
- Bounded-read verdict:
  - local-only pass;
  - six seed artifacts opened, within the target bound;
  - no web used.

## existing_instance_inventory

- Lean-backed exact seeds preserved in `PROOFS.md`:
  - `F25(3)`, `F25(5)`, and `F25(7)` are Lean-verified exact instances with `publication_status = INSTANCE_ONLY`;
  - `F2(5)` and `F2(7)` are Lean-verified exact instances with `publication_status = INSTANCE_ONLY`.
- Seed artifacts opened in this pass and what they contribute:
  - `z13-z25`:
    the first exact failure of the old upper-half-prime-only `C` rule; the graph still labels once `37` and `41` are admitted into `C` and their doubles are pushed out of `A ∪ B`.
  - `z17-z25`:
    the same small-spill pattern survives one more step with four spill primes `37,41,43,47`, showing the `p = 13` repair is not isolated.
  - `z13-z13-z2`:
    the `F2` line survives its first zero-slack boundary; once `C = 1`, the full `{2,3}`-smooth reservoir on `A ∪ E` closes exactly at `p = 13`.
  - `z71-z25`:
    the strict prime-only high-barrier `C` wording fails first here; one complementary-support label `25` repairs the exact instance without changing the support proof.
  - `z97-z25`:
    the fixed late data
    `A0`,
    `B = {1,293,307,311}`,
    and
    `C0 = {n : 2 <= n <= 291 and gcd(n,6)=1}`
    give an exact endpoint with `|C0| = 96 = p - 1`.
  - `z101-z25`:
    the graph still labels after the `C0` window ends, but only after changing the barrier set to `B = {1,263,269,271}` and changing the `C` pool, so `p = 101` is a frozen-window boundary, not a graph boundary.
- Inventory conclusion:
  - the paired structural slice is already exact in Lean;
  - the `F2` arm is already a closed theorem slice, not a live feeder problem;
  - the live `F25` story has three preserved layers:
    early spill-repair evidence at `p = 13,17`,
    a frozen exact window ending at `p = 97`,
    and a reopened post-window continuation signal at `p = 101`;
  - no preserved graph-level counterexample is supported by the opened evidence.

## shared_structure

- Common decomposition / invariant / construction:
  classify each nonzero zero-divisor by coordinate-support type, prove that support type determines the neighborhood pattern, reduce the full ring graph to a tiny support graph, and satisfy the exact graph by classwise coprimality conditions.
- `F25(p)` support classes and exact interfaces:
  - classes:
    `A = {(0,u) : 5 ∤ u}`,
    `B = {(0,5),(0,10),(0,15),(0,20)}`,
    `C = {(a,0) : a ∈ Z_p^×}`,
    `D = {(a,5t) : a ∈ Z_p^×, t ∈ {1,2,3,4}}`;
  - interfaces:
    only `A-C`, `B-B`, `B-C`, and `B-D`.
- `F2(p)` support classes and exact interfaces:
  - classes:
    `A = (*,0,0)`,
    `B = (0,*,0)`,
    `C = (0,0,1)`,
    `D = (*,*,0)`,
    `E = (*,0,1)`,
    `F = (0,*,1)`;
  - interfaces:
    only `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, and `C-D`.
- Shared proof template:
  1. prove the support partition from the ring law;
  2. prove that ring adjacency equals support adjacency;
  3. assign each support class to a label reservoir with the needed coprimality support;
  4. let the unconstrained residual class absorb the remaining interval labels.
- Family-specific structural takeaways:
  - `F2`:
    set the singleton class `C` to label `1`; then `A-C`, `B-C`, and `C-D` are automatic, and only the interfaces `A-B`, `A-F`, and `B-E` remain.
  - `F25`:
    freeze `A` in a low-support reservoir, place a pairwise-coprime high barrier on `B`, choose `C` from labels whose prime support avoids the support carried by `A ∪ B`, and let `D` absorb the residual interval complement.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  - the support decompositions and ring-to-support reductions;
  - the `F2` hinge move `C = 1` and the resulting three-interface reduction;
  - the `F25` high-barrier complementary-support wrapper language;
  - the fixed-window `C0` counting and support-avoidance lemmas through `p <= 97`;
  - the checked subset-selection theorem producing an actual `(p - 1)`-element sub-finset of `fixedC0Finset`.
- Steps that still need theorem packaging:
  - convert a chosen `(p - 1)`-element subset `S ⊆ fixedC0Finset` into an actual injective `C`-class labeling;
  - extend that classwise `C` labeling to a total label function on the full graph with `D` as the residual complement;
  - state the direct `59 <= p <= 97` corollary as a clean ring-faithful theorem.
- Steps that are instance-specific:
  - spill primes `37,41` at `p = 13`;
  - spill primes `37,41,43,47` at `p = 17`;
  - the one-label complementary-support repair `25` at `p = 71`;
  - the frozen endpoint data
    `A0`,
    `B = {1,293,307,311}`,
    and
    `C0`
    at `p = 97`;
  - the changed barrier set `B = {1,263,269,271}` and changed `C` pool at `p = 101`.
- Strongest plausible theorem slice:
  the direct fixed-window `F25` corollary for odd primes `59 <= p <= 97`, with fixed
  `A0`,
  fixed
  `B = {1,293,307,311}`,
  and any `(p - 1)`-subset of
  `C0`.
- Smallest likely counterexample or obstruction:
  - no graph-level counterexample is supported by current evidence;
  - the smallest preserved obstruction to strict prime-only `F25` wording is `p = 71`;
  - the smallest preserved obstruction to extending the frozen `C0` window is `p = 101`.

## candidate_theorem_slices

- Slice A:
  the exact paired structural theorem
  `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`.
- Slice B:
  the exact `F2` lead theorem
  `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`.
- Slice C:
  the direct fixed-window `F25` corollary for odd primes `59 <= p <= 97`, obtained from `A0`, `B = {1,293,307,311}`, `C0`, and one missing injection / extension theorem.
- Slice D:
  a template-boundary slice saying that strict prime-only high-barrier `C` wording already fails at `p = 71`, and the frozen `C0` window ends at `p = 101`, without claiming graph non-primality.
- Slice E:
  a post-`97` complementary-support continuation theorem in the same high-barrier regime, but only at `FAMILY_CANDIDATE` level until the support-avoiding `C` supply is quantified.

## chosen_slice

- Strongest honest closed slice:
  keep `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice` as the exact publication core.
- Strongest honest live upgrade target:
  the direct fixed-window `F25` corollary for odd primes `59 <= p <= 97`.
- Why this is the right slice:
  - every supply ingredient except one injection / extension package is already preserved in Lean;
  - it stops exactly before the first preserved fixed-window failure at `p = 101`;
  - it is stronger than an instance list and weaker than any unjustified post-`97` family theorem.
- What is not honest yet:
  - an all-odd-primes theorem for `Γ(Z_p × Z_25)`;
  - a quantified post-`97` continuation theorem;
  - any graph-level counterexample claim from `p = 71` or `p = 101`.

## reusable_lemmas

- Structural lemmas already supporting family reuse:
  - `support_decomposition_F25`;
  - `support_decomposition_F2`;
  - `classwise_template_lemma`;
  - `pairwise_coprime_clique_lemma`;
  - `forbidden_multiples_reservoir_lemma`;
  - `singleton_one_lemma`;
  - `three_interface_pack_lemma`.
- Lean-checked family theorems already available:
  - `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`;
  - `AutoMath.Families.ZeroDivisorRingBridges.zp_zp_z2_three_interface_lead_theorem`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`.
- Fixed-window `F25` lemmas already closed:
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_card_eq_96`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.exists_fixedC0_subset_card_eq_C_size_of_p_le_97`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_available_of_p_ge_59`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_support_avoids_two_three`;
  - `AutoMath.Families.ZeroDivisorF25FrozenWrapper.fixedC0_support_avoids_high_barrier_293_307_311`.
- Missing reusable lemma family:
  - a `C`-class packaging lemma turning
    `S ⊆ fixedC0Finset`
    with
    `S.card = p - 1`
    into an injective labeling of the `C` support class;
  - a residual-extension lemma showing that the remaining interval labels furnish the required `D` class data after `A`, `B`, and `C` are fixed.

## proof_plan

- Main proof path:
  1. State the direct finite-range corollary for odd prime `p` with `59 <= p <= 97`.
  2. Use
     `AutoMath.Families.ZeroDivisorF25FrozenWrapper.exists_fixedC0_subset_card_eq_C_size_of_p_le_97`
     to obtain `S ⊆ fixedC0Finset` with `S.card = p - 1`.
  3. Use `|C| = p - 1` to build an explicit equivalence between the `C` support-class vertices and the chosen finite set `S`.
  4. Freeze `A = A0` and `B = {1,293,307,311}`, label `C` by `S`, and define `D` from the residual interval complement.
  5. Prove injectivity and the `D`-class interval / barrier-exclusion hypotheses for that total labeling.
  6. Use
     `fixedC0_available_of_p_ge_59`,
     `fixedC0_support_avoids_two_three`,
     and
     `fixedC0_support_avoids_high_barrier_293_307_311`
     to discharge the wrapper side conditions.
  7. Invoke
     `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`.
  8. Present the paired exact slice as the closed paper core and this `59 <= p <= 97` result as the first direct `F25` corollary.
- Strongest path forward:
  formalize the `C`-class injection / extension theorem before opening any new feeder.
- Fallback path:
  1. Freeze the publication claim at the paired exact slice plus the exact `F2` lead theorem.
  2. Preserve the fixed-window `F25` supply and subset-selection lemmas as reusable infrastructure even if the direct corollary remains unwrapped.
  3. Use `p = 71` only as the smallest counterexample to strict prime-only template wording.
  4. Use `p = 101` only as the first frozen-window boundary.
  5. If extra evidence becomes necessary before the packaging theorem closes, move next to `z109` and `z113`, not to unrelated feeders.

## fallback_counterexample_plan

- No graph-level counterexample theorem is supported by the opened evidence.
- The honest negative statements are template-level:
  - `p = 71` is the smallest preserved counterexample to the strict prime-only high-barrier `C` formulation;
  - `p = 101` is the first preserved counterexample to the claim that the frozen `C0` window alone extends beyond `97`.
- If the fixed-window corollary still does not close:
  - preserve those as wording boundaries, not graph non-primality claims;
  - treat the unresolved obstruction as the missing injection / extension theorem, not as a failure of the support reduction itself.

## next_best_feeder_instances

- `z109-z25-prime-zero-divisor-graph`:
  the next odd prime after the already-preserved post-`97` continuation evidence named by the current family status, and still inside the same `293 > (5p + 19)/2` high-barrier regime.
- `z113-z25-prime-zero-divisor-graph`:
  the last odd prime in that same `293`-above-half regime, so it maximally discriminates genuine continuation from a boundary artifact.
- No new `F2` feeder is needed right now:
  the live blocker is entirely the `F25` injection / extension packaging.

## publication_value

- The campaign already owns a real paper core:
  the paired exact support-reduction theorem is stronger than a pile of exact feeders.
- The opened seed inventory cleanly separates scalable structure from local arithmetic:
  - `F2` is structurally closed once `C = 1`;
  - `z13` and `z17` explain the early spill-repair narrative;
  - `z71` kills prime-only overclaiming;
  - `z97` is the fixed-window endpoint;
  - `z101` shows the window boundary is not a graph boundary.
- Best honest publication status remains `SLICE_EXACT`, not `PAPER_READY`:
  the exact paired slice is closed, but the first direct `F25` corollary still needs one small but real packaging theorem.

## publication_prior_art_audit

- Bounded live-web audit on `2026-04-12` stayed claim-specific:
  exact searches on `prime labeling zero-divisor graph Z_p x Z_25` and `prime labeling zero-divisor graph Z_p x Z_p x Z_2`,
  alternate notation searches on `Γ(Z_p × Z_(q^2))`, `Γ(Z_p × Z_p × Z_q)`, `Z_p × Z_25`, and `Z_p × Z_p × Z_2`,
  the canonical Fox-Mooney paper,
  one outside-source status sweep,
  and one recent discussion / follow-up check.
- Exact-statement search did not surface an earlier theorem, proposition, example, corollary, observation, or sufficient-condition statement already settling either active subfamily
  `Γ(Z_p × Z_25)` or
  `Γ(Z_p × Z_p × Z_2)`
  within the bounded search budget.
- Alternate-notation search again pointed either back to the canonical source or to no direct closure within budget.
  In particular, the bounded pass did not find an independent published theorem for the `q = 5` case of
  `Γ(Z_p × Z_(q^2))`
  or the `q = 2` case of
  `Γ(Z_p × Z_p × Z_q)`.
- Canonical-source search:
  the canonical source remains Fox and Mooney, `On Prime Labelings of Zero-Divisor Graphs` (`2025`).
  Inside that paper, nearby positive theorems cover other families such as
  `Γ(Z_p × Z_4)`,
  `Γ(Z_p × Z_9)`,
  and
  `Γ(Z_2 × Z_(p^2))`,
  but the ambient families containing the active campaign still appear as open Conjectures `4.3` and `4.4`.
- Canonical-source theorem / proposition / example / corollary / observation / sufficient-condition check:
  within the canonical paper, the bounded inspection did not find a theorem, proposition, example, corollary, observation, or sufficient-condition statement that already implies the paired support-reduction slice closed here, the direct fixed-window `59 <= p <= 97` `F25` corollary, or an earlier exact closure of the `q = 5` / `q = 2` subfamilies.
- One outside-source status search:
  a bounded outside-canonical sweep on the exact title, family notation, and nearby zero-divisor-graph labeling terms surfaced discussion listings and adjacent labeling papers, but it did not surface a later independent prime-labeling paper already closing
  `Γ(Z_p × Z_25)`,
  `Γ(Z_p × Z_p × Z_2)`,
  or the specific fixed-window `59 <= p <= 97` corollary target.
- One recent citation / discussion / follow-up check:
  the topic is still publicly discussed in recent meeting materials, including Brad Fox's `IWOGL 2026` abstract, but the bounded `2026-04-12` sweep did not reveal a later published follow-up already resolving the active subfamilies.
- Caution:
  absence of hits is not proof of novelty.
  It only means the bounded rediscovery / status audit did not find an earlier closure.
- Prior-art verdict:
  rediscovery is not established in this bounded audit.

## publication_statement_faithfulness

- Is the strongest honest claim stronger than `here is an example`:
  yes.
  The closed headline is the Lean-checked paired support-reduction slice, which is quantified in the prime parameter and is not just a list of feeder instances.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here:
  yes.
  The real closed slice is
  `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`,
  and the real live upgrade target is the direct fixed-window `Γ(Z_p × Z_25)` corollary for odd primes `59 <= p <= 97`.
- Is the proof structural or merely instance-specific:
  the strongest closed claim is structural.
  It works by ring-to-support partition, support-adjacency reduction, and classwise coprimality packaging rather than by one hand-picked witness.
  The unfinished direct `F25` corollary still needs one packaging step from counted `C0` supply to an actual total labeling, so that upgrade is not yet fully structural end to end.
- Would this survive a referee asking `what is the theorem?`:
  yes, if the paper headline stays at the paired support-reduction theorem plus the exact `F2` lead theorem.
  No, if the paper headline overclaims a direct all-primes `F25` existence theorem or a post-`97` continuation theorem.
- Is the claim still too dependent on hand-picked small cases:
  the closed paired slice is not.
  The live direct `F25` upgrade still partly is, because the finite-range story is supported by fixed-window data and preserved feeder boundaries until the injection / extension theorem is written.
- Is the generalization route strong enough to merit campaign priority:
  yes.
  The canonical source still leaves the ambient families open, the repo already owns a real exact slice, and only one small but real theorem-packaging step blocks the first direct `F25` corollary.
- Faithfulness verdict:
  the campaign already has a real referee-facing slice theorem, but the honest paper headline must remain the support-reduction slice until the direct `F25` corollary is actually closed.

## publication_theorem_worthiness

- There is a real theorem here, not just feeder evidence.
  The paired slice converts repeated exact-instance structure into a parameterized ring-faithful reduction theorem.
- The strongest honest claim is stronger than an example because it explains the whole proof architecture:
  support partition,
  support-adjacency equivalence,
  and classwise coprimality discharge on a tiny support graph.
- The proof is genuinely structural for the closed slice.
  The `F2` arm is already a clean three-interface theorem once the singleton support class gets label `1`.
  The `F25` arm is already an exact graph-faithful wrapper theorem under explicit support-avoidance hypotheses.
- A referee asking `what is the theorem?` would get a coherent answer today:
  a paired support-reduction theorem for two open zero-divisor prime-labeling families, together with a closed direct `F2` lead theorem and a sharply delimited direct `F25` corollary target.
- A referee could still object that the `F25` side stops one theorem step short of the paper's strongest likely headline.
  That objection is valid, and it is exactly why the campaign is not yet `PAPER_READY`.
- The claim is no longer fatally dependent on hand-picked small cases, but the strongest direct graph-primality statement still is.
  The closed slice is structural;
  the next direct `F25` corollary still depends on the missing injection / extension package.
- The generalization route is strong enough to keep campaign priority.
  This is the shortest path from preserved exact wins to a paper-worthy theorem slice, and broad fresh curation would be a weaker use of effort.
- Theorem-worthiness verdict:
  real theorem slice,
  real campaign priority,
  still one paper-facing step short of `PAPER_READY`.

## publication_publishability

- Conservative publication verdict:
  keep `publication_status = SLICE_EXACT`.
- Why not `INSTANCE_ONLY`:
  the strongest honest claim is a parameterized Lean-checked slice theorem, not a single graph instance.
- Why not `REDISCOVERY`:
  the bounded prior-art audit did not establish an earlier exact closure or a directly implying published theorem.
- Why not `SLICE_CANDIDATE`:
  the paired support-reduction slice is already closed in Lean and is nontrivial.
- Why not `FAMILY_CANDIDATE`:
  the strongest honest closed claim is a finished theorem slice, not merely a plausible broader family theorem.
- Why not `PAPER_READY`:
  the current closed theorem is structural and worthwhile, but the paper still lacks the first direct referee-facing `F25` corollary that turns the support machinery into a clean new family prime-labeling theorem.
  A referee could still ask whether the paper proves more than an exact reduction package plus curated feeder evidence.
- Honest publishable shape right now:
  a theorem-slice paper centered on paired support-reduction theorems, with the exact `F2` lead theorem already closed and the direct finite-range `F25` corollary as the decisive upgrade target.
- Campaign-priority verdict:
  keep this family active.
  Do not wander to unrelated curation while the `F25` injection / extension package remains the only live blocker.

## strongest_honest_claim

- As of `2026-04-12T03:55:30-0400`, the strongest honest family claim remains the Lean-checked paired structural theorem
  `AutoMath.Families.ZeroDivisorPublicationSlice.zero_divisor_prime_labelings_paired_exact_slice`.
- The bounded prior-art audit did not establish rediscovery:
  Fox-Mooney's `2025` canonical source still leaves the ambient families
  `Γ(Z_p × Z_p × Z_q)`
  and
  `Γ(Z_p × Z_(q^2))`
  open as Conjectures `4.3` and `4.4`,
  and the bounded outside-source sweep did not surface an independent closure of the active `q = 2` or `q = 5` subfamilies.
- What is exact here is the reduction slice, not a direct all-primes graph-primality theorem.
  The `F2` arm is already a closed three-interface lead theorem once `C = 1`,
  while the `F25` arm is an exact graph-faithful wrapper theorem under the checked high-barrier complementary-support hypotheses.
- The first direct `F25` publication upgrade remains the finite-range corollary for odd primes `59 <= p <= 97`.
  That claim is still blocked only by packaging a chosen `(p - 1)`-element subset of `fixedC0Finset` into an injective `C`-class labeling and extending it to a total label function compatible with
  `AutoMath.Families.ZeroDivisorF25FrozenWrapper.zp_z25_fixed_C0_high_barrier_wrapper_graph_skeleton_of_p_le_97`.
- Therefore the honest publication label remains `SLICE_EXACT` rather than `PAPER_READY`.

## paper_title_hint

- `Paired Support-Reduction Theorems for Prime Labelings of Two Zero-Divisor Graph Families`

## next_action

- Keep the paper headline fixed at the paired support-reduction slice.
- Formalize the `C`-class injection / extension package needed for the direct finite-range `Γ(Z_p × Z_25)` corollary for odd primes `59 <= p <= 97`.
- Rerun `publication_audit` immediately after that theorem packaging closes.
- Only if the packaging still stalls should feeder work resume at
  `z109-z25-prime-zero-divisor-graph`
  and
  `z113-z25-prime-zero-divisor-graph`
  as post-`97` continuation tests rather than as new paper headlines.
