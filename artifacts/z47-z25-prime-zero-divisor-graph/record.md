# Solve Record: z47-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_47 × Z_25) prime?`
- Active slug: `z47-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_47 × Z_25)` admits a prime labeling, meaning a bijection from its `254` vertices to `{1,2,...,254}` such that adjacent vertices receive coprime labels.
- This solve pass is locked to the exact feeder instance `Z_47 × Z_25`, not to a full theorem for `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_47` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the standard four support classes for the `Γ(Z_p × Z_25)` family:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_47^×}`, size `46`.
  - `D = {(a,5t) : a ∈ Z_47^×, t ∈ {1,2,3,4}}`, size `184`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 47` and `bd = 0 mod 25`.
- Because `Z_47` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - once a classwise label set is fixed, labels may be assigned inside `A`, `C`, and `D` in any order because vertices there have identical neighborhoods; labels on `B` may also be permuted because `B` is a `K_4` and the chosen `B` labels are pairwise coprime.

## approach_A

Structural / invariant route through the support graph.

- The support decomposition is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- The edge counts are therefore forced:
  - `A-C = 20 · 46 = 920`;
  - `B-B = 6`;
  - `B-C = 4 · 46 = 184`;
  - `B-D = 4 · 184 = 736`.
- Total predicted edge count: `920 + 6 + 184 + 736 = 1846`.
- So the exact graph again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- This route also exposes why the old frozen wrapper `B = {1,19,23,29}` is no longer the right solve path here:
  - with `N = 254`, its forced spill into `A` is
    `(⌊254/19⌋ - 1) + (⌊254/23⌋ - 1) + (⌊254/29⌋ - 1) = 12 + 10 + 7 = 29`;
  - but `|A| = 20`, so that wrapper is impossible before one even starts choosing `C`.
- Therefore any honest `p = 47` attempt must move the barrier upward; the structural graph stays the same, but the arithmetic interface on `B` cannot stay frozen.

## approach_B

Construction / extremal route by reusing the moved sparse barrier.

- The family record already preserves that the moved barrier `B = {1,43,47,53}` survives at `p = 37,41,43`.
- At `p = 47`, the same barrier still has controlled spill:
  - nontrivial multiples of `43` in `{1,...,254}` are `86,129,172,215`;
  - nontrivial multiples of `47` are `94,141,188,235`;
  - nontrivial multiples of `53` are `106,159,212`.
- These spill sets are pairwise disjoint because `43·47`, `43·53`, and `47·53` all exceed `254`.
- Hence the moved barrier forces exactly `4 + 4 + 3 = 11` labels into `A`, which fits inside the fixed `20` slots of `A`.
- Put those `11` forced spill labels into `A`, and fill the remaining `9` `A`-slots with labels using only the small factor palette `{2,3,5}`:
  `2,3,4,5,6,8,9,10,12`.
- Then every label in `A ∪ B` has prime factors contained in
  `{2,3,5,43,47,53}`.
- So any prime label assigned to `C` only needs to avoid that six-prime palette.
- Up to `254`, the primes avoiding `{2,3,5,43,47,53}` are:
  `7,11,13,17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251`.
- This gives a candidate pool of `48` primes for `C`, while only `46` are needed.
- One explicit choice is to put on `C` the `46` primes
  `7,11,13,17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239`,
  leaving `241` and `251` unused by `C`.
- The residual labels then go to `D`.
- This route is extremal in the right sense: it squeezes the barrier spill into the fixed `20` slots of `A`, controls the full factor palette on `A ∪ B`, and then counts a prime pool for `C` with slack `2`.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,46,184`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For the moved barrier `B = {1,43,47,53}`, it is sufficient that:
   - every nontrivial multiple of `43`, `47`, or `53` in `{1,...,254}` lies in `A`;
   - every label on `A` uses only prime factors from `{2,3,5,43,47,53}`;
   - every label on `C` is a prime outside `{2,3,5,43,47,53}`.
7. Under those conditions, the three arithmetic obligations above are automatic, so any classwise partition of `{1,...,254}` satisfying them yields a prime labeling.

## chosen_plan

- Keep the standard four-class support proof unchanged.
- Reject the frozen wrapper immediately because its spill count already exceeds `20`.
- Reuse the campaign-preserved moved barrier `B = {1,43,47,53}`.
- Put its `11` forced spill labels into `A`, complete `A` with `2,3,4,5,6,8,9,10,12`, and choose `46` primes for `C` from the `48`-prime complementary pool.
- Only after the full witness is fixed on paper should a tiny checker be used, if needed, to verify the bookkeeping against the actual ring graph.

## self_checks

- After statement lock:
  - the target remains the exact feeder `Γ(Z_47 × Z_25)`;
  - the vertex count `20 + 4 + 46 + 184 = 254` matches the label interval.
- After Approach A:
  - the support graph is still exactly the campaign template `A-C`, `B-B`, `B-C`, `B-D`;
  - the old wrapper `B = {1,19,23,29}` really is impossible here because its forced spill is `29 > 20`.
- After Approach B:
  - the moved barrier `B = {1,43,47,53}` spills only `11` labels into `A`;
  - the chosen `A` palette uses only the six primes `{2,3,5,43,47,53}`;
  - the complementary prime pool for `C` has size `48`, so there is genuine slack `2`.
- After choosing the plan:
  - this is still reasoning-first because the witness is dictated by support reduction plus explicit divisibility bookkeeping, not by optimization search;
  - minimal code, if used at all, will be only post-construction witness verification.
- After code:
  - the tiny checker reported `254` vertices and `1846` edges with edge-type counts `A-C = 920`, `B-B = 6`, `B-C = 184`, `B-D = 736`;
  - the labeling is a bijection onto `{1,...,254}` and no edge had a gcd violation.

## code_used

- A tiny local checker [check_witness.py](/Users/jeremykalfus/CodingProjects/AutoMath/.worktrees/z47-z25-prime-zero-divisor-graph-1775947265/artifacts/z47-z25-prime-zero-divisor-graph/check_witness.py) was used only after the explicit class partition was fixed.
- The checker enumerates the `254` nonzero zero-divisors of `Z_47 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,254}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 254`
  - `edge_count = 1846`
  - `edge_type_counts = {A-C: 920, B-B: 6, B-C: 184, B-D: 736}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

Current best reasoning-stage candidate witness:

- Put the labels `1,43,47,53` on `B` in any order.
- Put the labels `2,3,4,5,6,8,9,10,12,86,94,106,129,141,159,172,188,212,215,235` on `A` in any order.
- Put the labels
  `7,11,13,17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239`
  on `C` in any order.
- Put the remaining `184` labels on `D`.

Why this should work:

- `B-B` edges:
  `1,43,47,53` are pairwise coprime.
- `A-C` and `B-C` edges:
  every label in `C` is a prime outside the factor palette `{2,3,5,43,47,53}` used by `A ∪ B`, so every label on `A ∪ B` is coprime to every label on `C`.
- `B-D` edges:
  every nontrivial multiple of `43`, `47`, or `53` up to `254` was deliberately placed in `A`, so no label in `D` shares a factor with `43`, `47`, or `53`.
- There are no other edge types.
- The checker confirmed that this bookkeeping matches the actual ring graph exactly for this instance.

Strong-result extraction:

- What part of the argument scales:
  the four-class support reduction, the classwise proof skeleton, the idea that `A` is a fixed reservoir, and the moved sparse-barrier strategy where one controls the full factor palette on `A ∪ B` and then fills `C` from the complementary prime pool.
- What part does not yet scale automatically:
  the existence of a good moved barrier and the exact complementary prime count are still proved here by instance arithmetic, not by a closed theorem.
- What theorem slice is suggested:
  a sufficient-condition theorem for `Γ(Z_p × Z_25)` saying that if `{1,...,5p+19}` admits a pairwise-coprime barrier `B = {1,q_1,q_2,q_3}` whose spill fits in `A` and leaves at least `p-1` primes outside the full factor palette of `A ∪ B`, then the four-interface bridge theorem gives a prime labeling.
- What one or two next feeder instances would help most:
  `Γ(Z_53 × Z_25)` first, because it is the next campaign-designated pressure test after `p = 47`; and, if that survives, `Γ(Z_59 × Z_25)` as the next check that the same barrier philosophy still leaves prime-pool slack.
- Whether the current package is still just an instance or already closer to a paper-shaped claim:
  it is still an instance-level solve package, but it is closer to a paper-shaped claim because it extends the preserved moved-barrier story from `p = 37,41,43` to one more parameter without changing the structural proof.

## family_affinity

- Family affinity is high.
- This feeder is explicitly the first post-`43` discriminator for whether the same moved barrier `B = {1,43,47,53}` still works one step later.
- The argument directly strengthens the live publication-mode companion target for `Γ(Z_p × Z_25)` rather than producing an isolated one-off witness.

## generalization_signal

- Generalization signal is strong but not closed.
- The old frozen wrapper is now decisively irrelevant at this parameter, while the moved-barrier strategy still appears viable.
- The reusable signal is not “these exact labels work”; it is “a barrier can move upward to shrink spill, while `A ∪ B` is tracked by a controlled factor palette and `C` is filled from the complementary prime pool.”
- What is still missing is a quantified existence lemma for such a barrier and a theorem-level lower bound for the complementary prime pool.

## proof_template_reuse

- Reusable proof template:
  1. partition the nonzero zero-divisors into `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. choose a pairwise-coprime barrier on `B`;
  4. place all of its nontrivial multiples into the fixed reservoir `A`;
  5. choose the remaining `A` labels from a deliberately small factor palette;
  6. choose `C` from primes outside that full palette;
  7. assign the residual complement to `D`.
- Relative to the earlier `p = 13,17` feeders, the reusable shift is that the argument is now naturally phrased as a moved-barrier plus factor-palette design, not just a small-spill repair of the old barrier.

## candidate_theorem_slice

- Candidate slice:
  if `N = 5p + 19` admits a pairwise-coprime barrier `B = {1,q_1,q_2,q_3}` whose nontrivial multiples occupy at most the `20` labels of `A`, and if one can choose the remaining `A` labels so that at least `p - 1` primes in `{1,...,N}` remain outside the resulting factor palette of `A ∪ B`, then `Γ(Z_p × Z_25)` is prime by the exact four-interface support theorem.

## smallest_param_shift_to_test

- The smallest next parameter shift to test is `p = 53`.
- Reason: `p = 47` is the current first discriminator after the preserved `p = 43` success, so the next honest pressure test is whether the same moved-barrier design still survives at `p = 53`.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet.
- It is still a single solve-stage feeder instance, without prior-art audit in this pass and without Lean closure.
- Its publication value is that it strengthens the companion theorem direction: the right family statement is increasingly clearly an existential moved-barrier plus controlled-factor-palette theorem, not a frozen-wrapper theorem.

## likely_failure_points

- A hidden support-edge mistake would invalidate the classwise reduction, though that would contradict the now-stable family structure.
- The main arithmetic risk is forgetting a nontrivial multiple of `43`, `47`, or `53` and accidentally leaving it in `D`.
- A second arithmetic risk is accidentally putting into `A ∪ B` a label divisible by one of the chosen `C` primes.
- The publication-facing weakness is that the current argument is still instance arithmetic, not yet a quantified theorem about barrier existence or prime-pool size.

## what_verify_should_check

- Recompute the `254` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the support-edge counts `A-C = 920`, `B-B = 6`, `B-C = 184`, `B-D = 736`, total `1846`.
- Check that the displayed classwise label sets are disjoint and cover exactly `{1,...,254}`.
- Check directly that every actual edge of the ring graph receives coprime labels.
- Audit whether the intended publication interpretation should remain `INSTANCE_ONLY` or be promoted only after the family dossier absorbs this feeder.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact tuple `Γ(Z_47 × Z_25)`, ASCII variants such as `Z_47 x Z_25`, alternate family notation such as `Γ(Z_p × Z_(q^2))`, the canonical 2025 source `On prime labelings of zero-divisor graphs`, and a same-source theorem / conjecture check.
- Exact-instance and alternate-notation searches did not reveal an earlier theorem, proposition, example, observation, or corollary settling this exact `p = 47, q = 5` case within budget.
- The canonical source check cut against rediscovery rather than supporting it: the Combinatorial Press paper `On prime labelings of zero-divisor graphs` still lists the ambient family `Γ(Z_p × Z_(q^2))` as open in Conjecture `4.4`, while the nearby settled same-source cases I recovered were different families such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))`.
- One bounded recent status / discussion search did not surface a later publication closing either the exact `Γ(Z_47 × Z_25)` instance or the whole `Γ(Z_p × Z_(q^2))` family within budget.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The solve record is aimed at the exact intended statement: existence of a prime labeling for the full simple zero-divisor graph `Γ(Z_47 × Z_25)` on the `254` nonzero zero-divisors, with labels bijectively covering `{1,...,254}`.
- There is no wrong-theorem drift to a support graph, induced subgraph, or partial labeling. The support classes are used only as a reduction device for the exact graph.
- I did make one tiny wording repair in the setup section: only `A`, `C`, and `D` have identical neighborhoods. The `B` labels can still be permuted, but for the different reason that `B` induces `K_4` and the chosen barrier labels are pairwise coprime.
- With that repair, the claimed result matches the intended instance exactly.

## verify_proof

- I recomputed the vertex partition directly from the ring definition and recovered `|A| = 20`, `|B| = 4`, `|C| = 46`, and `|D| = 184`, for total `254` vertices.
- I independently recomputed the exact edge set and again obtained only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `920`, `6`, `184`, and `736`, for total `1846` edges.
- Given that support graph, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly:
  - every `C` label is a prime outside the factor palette `{2,3,5,43,47,53}` used by `A ∪ B`, so all `A-C` and `B-C` edges are coprime;
  - `B = {1,43,47,53}` is pairwise coprime;
  - the nontrivial multiples up to `254` of `43`, `47`, and `53` are exactly `86,129,172,215`, `94,141,188,235`, and `106,159,212`, all placed in `A`, not `D`.
- First incorrect step found: none after the wording repair above. The proof is still instance-specific arithmetic bookkeeping, but the witness argument itself is correct.

## verify_adversarial

- I reran `artifacts/z47-z25-prime-zero-divisor-graph/check_witness.py`. It again reported `vertex_count = 254`, `edge_count = 1846`, `edge_type_counts = {'A-C': 920, 'B-B': 6, 'B-C': 184, 'B-D': 736}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran independent checks outside the artifact checker to confirm:
  - the four class label sets are disjoint and cover exactly `{1,...,254}`;
  - there is no hidden edge type beyond `A-C`, `B-B`, `B-C`, and `B-D`;
  - no residual `D` label is divisible by `43`, `47`, or `53`;
  - no label in `A ∪ B` shares a nontrivial gcd with any chosen `C` prime.
- I did not find a hidden edge, a mislabeled vertex, or a divisibility obstruction breaking the witness.

## verify_theorem_worthiness

- This is still an instance result, not a closed theorem slice by itself. The part that clearly scales is the four-class support reduction together with the moved sparse-barrier / controlled-factor-palette design.
- Relative to the preserved positive feeders at `p = 37, 41, 43`, this instance matters because the same moved barrier `B = {1,43,47,53}` still works at `p = 47`, and the complementary prime pool for `C` still has slack `2`.
- What does not yet scale automatically is the quantified arithmetic side: there is still no preserved theorem proving existence of a suitable moved barrier or guaranteeing enough primes outside the full factor palette of `A ∪ B`.
- The best honest publication status for this artifact is therefore `SLICE_CANDIDATE`, not `PAPER_READY`, because it is feeder evidence that points to a real theorem slice rather than a disconnected one-off.
- The smallest next discriminator for the claimed template is `Γ(Z_53 × Z_25)`, which tests whether the same moved-barrier design survives the next parameter shift after `p = 47`.

## verify_verdict

- `VERIFIED`
- No rediscovery was established in the bounded prior-art pass, the claim matches the intended instance after a tiny wording repair, and the explicit witness survived independent skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- Repaired one sentence in the setup section: only `A`, `C`, and `D` have identical neighborhoods; `B` is handled separately because it is a clique with pairwise-coprime labels.
