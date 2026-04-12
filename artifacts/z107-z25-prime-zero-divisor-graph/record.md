# Solve Record: z107-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_107 × Z_25) prime?`
- Active slug: `z107-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_107 × Z_25)` admits a prime labeling, meaning a bijection from its `554` vertices to `{1,2,...,554}` such that adjacent vertices receive coprime labels.
- This solve pass is locked to the exact feeder instance `Z_107 × Z_25`, not to the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_107` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the standard four support classes for the `Γ(Z_p × Z_25)` campaign:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_107^×}`, size `106`.
  - `D = {(a,5t) : a ∈ Z_107^×, t ∈ {1,2,3,4}}`, size `424`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 107` and `bd = 0 mod 25`.
- Because `107` is prime, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions and ambiguities locked for solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - labels may be permuted within each support class because vertices in the same class have identical neighborhoods;
  - no missing definitions remain that block the exact instance.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 107` are therefore forced:
  - `A-C = 20 · 106 = 2120`;
  - `B-B = 6`;
  - `B-C = 4 · 106 = 424`;
  - `B-D = 4 · 424 = 1696`.
- Total predicted edge count: `2120 + 6 + 424 + 1696 = 4246`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.

## approach_B

- Construction / extremal route by switching fully into the late complementary-support regime.
- The small-prime spill strategy from `p = 13,17,19` is no longer the natural front here: at `p = 107`, `|C| = 106`, so manually tracking spill primes and all their multiples is the wrong invariant.
- The cleaner late-regime invariant is:
  - put `A` on the fixed `{2,3}`-supported reservoir
    `A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`;
  - put `B` on the pairwise-coprime high barrier
    `{1,293,307,311}`;
  - choose `C` from labels whose prime support avoids both `{2,3}` and the barrier primes.
- For this instance, take
  `C_lab = {n : 2 <= n <= 329, gcd(n,6)=1, n ∉ {293,307,311}}`.
- Count check for `C_lab`:
  - in `1,...,329`, the numbers coprime to `6` are exactly the residues `1` and `5 mod 6`;
  - since `329 = 6·54 + 5`, there are `2·54 + 2 = 110` such numbers in `1,...,329`;
  - removing `1`, `293`, `307`, and `311` leaves exactly `106` labels, matching `|C|`.
- Why this `C` choice is structurally clean:
  - every `A0` label has prime support contained in `{2,3}`;
  - every `C_lab` label is coprime to `6`, so it is coprime to every label in `A0`;
  - the only possible common factor with a `B` label could be `293`, `307`, or `311`, and those three labels were explicitly removed from `C_lab`.
- Why the high barrier works at `p = 107`:
  - the active interval is `{1,...,554}`;
  - `2·293 = 586`, `2·307 = 614`, and `2·311 = 622`, all above `554`;
  - therefore the only labels in the interval divisible by `293`, `307`, or `311` are the barrier labels themselves.
- So with `B = {1,293,307,311}`, the `B-D` interface is automatically safe once `D` is defined as the complement.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,106,424`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For the chosen late-regime data:
   - `A0` is supported only on primes `2` and `3`;
   - `B = {1,293,307,311}` is pairwise coprime;
   - every `C_lab` label is coprime to `6` and is not divisible by `293`, `307`, or `311`;
   - every label in the complement of `A0 ∪ B ∪ C_lab` is automatically coprime to `293`, `307`, and `311` because the only interval multiples of those primes are the barrier labels themselves.
7. Therefore any classwise bijection from `A,B,C,D` onto `A0`, `B`, `C_lab`, and the residual complement gives a prime labeling.

## chosen_plan

- Reuse the stable four-class support decomposition from the active campaign.
- Abandon prime-only language on `C` for this large instance and use complementary support instead.
- Freeze `A` at the campaign's fixed `A0` reservoir and `B` at the high barrier `{1,293,307,311}`.
- Define `C` by the exact admissibility criterion `2 <= n <= 329`, `gcd(n,6)=1`, and `n ∉ {293,307,311}`.
- Let `D` absorb the remaining labels in `{1,...,554}`.
- Only after this reasoning closes, use one tiny checker to verify the explicit class partition against the actual ring graph.

## self_checks

- After statement lock:
  - the exact target remains the feeder instance `Γ(Z_107 × Z_25)`;
  - the label interval length `554` matches the vertex count `20 + 4 + 106 + 424`.
- After Approach A:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the support graph still collapses the problem to three arithmetic interfaces.
- After Approach B:
  - `C_lab` has exactly `106` labels, so the class size matches without search;
  - `A0`, `B`, and `C_lab` are pairwise disjoint for structural reasons, not by accident;
  - the high barriers lie above half the interval, so `D` automatically avoids all nontrivial barrier multiples.
- After choosing the plan:
  - this remains reasoning-first because the witness is dictated by classwise support avoidance and a direct count, not by optimization;
  - minimal code is justified only as final witness verification on a large but explicit class partition.

## code_used

- Minimal code was used only after the reasoning and explicit classwise construction were fixed.
- A tiny local checker `check_witness.py` enumerates the `554` nonzero zero-divisors of `Z_107 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,554}`, and tests `gcd = 1` on every edge.
- The checker instantiates the exact solve-stage construction:
  - `A` labeled by `A0`;
  - `B` labeled by `{1,293,307,311}`;
  - `C` labeled by the sorted set `C_lab = {2 <= n <= 329 : gcd(n,6)=1} \\ {293,307,311}`;
  - `D` labeled by the residual complement.
- Result after running the checker:
  - `vertex_count = 554`
  - `edge_count = 4246`
  - `edge_type_counts = {A-C: 2120, B-B: 6, B-C: 424, B-D: 1696}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels
    `A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`
    on `A` in any order;
  - put the labels `{1,293,307,311}` on `B` in any order;
  - put the labels
    `C_lab = {n : 2 <= n <= 329, gcd(n,6)=1, n ∉ {293,307,311}}`
    on `C` in any order;
  - put the remaining `424` labels in `{1,...,554}` on `D` in any order.
- Why this works:
  - `B-B` edges:
    `1,293,307,311` are pairwise coprime.
  - `A-C` and `B-C` edges:
    every `C_lab` label is coprime to `6`, hence coprime to every `A0` label, and none is divisible by `293`, `307`, or `311`, hence each is also coprime to every `B` label.
  - `B-D` edges:
    the only numbers in `{1,...,554}` divisible by `293`, `307`, or `311` are the barrier labels themselves, which lie in `B`, not `D`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with a direct complementary-support prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the classwise reduction to `A-C`, `B-B`, `B-C`, `B-D`; the fixed `{2,3}`-smooth reservoir `A0`; and the high-barrier idea that once `B` uses primes above half the interval, `D` automatically avoids their multiples.
  - what part does not:
    the exact cutoff `329` and the exact late barrier data `{293,307,311}` are still finite-instance arithmetic choices in this record;
    the solve pass does not yet package a quantified post-`97` theorem.
  - what theorem slice is suggested:
    a post-`97` high-barrier complementary-support slice for `Γ(Z_p × Z_25)` in which `A` stays on `A0`, `B` is a pairwise-coprime barrier above half the interval, and `C` is chosen from labels avoiding the prime support of `A ∪ B`.
  - what one or two next feeder instances would help most:
    `Γ(Z_109 × Z_25)` and `Γ(Z_113 × Z_25)`, because they continue the same fixed-barrier regime up to the natural half-interval boundary for the prime `293`.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still instance-level evidence, but it is much closer to a paper-shaped claim than the earlier small-spill feeders because the witness is now governed by a clean complementary-support pattern rather than ad hoc spill bookkeeping.
- Solve-stage verdict:
  - `classification = CANDIDATE`, not `EXACT`, because Lean is still off.

## family_affinity

- Family affinity is very high.
- This feeder sits exactly on the live `Γ(Z_p × Z_25)` publication line and probes the post-`97` regime where the frozen `C0` window no longer suffices.
- The solve package is not a random exact win: it reuses the campaign's fixed `A0` reservoir and the late high-barrier logic while showing that the complementary-support viewpoint still closes a large exact instance.

## generalization_signal

- Generalization signal is strong.
- Relative to the frozen `p <= 97` window, the main new lesson is that the same high-barrier set `{1,293,307,311}` still works beyond `p = 97` once `C` is allowed to expand beyond the old fixed window and is defined instead by support avoidance.
- The honest scalable core is:
  choose `A` from labels supported only on `{2,3}`, choose `B` from pairwise-coprime labels above half the interval, and choose `C` from the complementary-support labels that avoid the prime support of `A ∪ B`.
- What remains open is the cleanest quantified theorem statement for how far this exact barrier data persists before a new barrier shift is needed.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact interface graph `A-C`, `B-B`, `B-C`, `B-D`;
  3. freeze `A` on a small `{2,3}`-supported reservoir `A0`;
  4. choose `B` as a pairwise-coprime barrier set above half the active interval;
  5. choose `C` from labels whose prime support avoids the prime support of `A ∪ B`;
  6. assign the residual complement to `D`.
- Relative to the earlier `p = 13,17,19` feeders, the reusable gain is conceptual:
  the controlling invariant is complementary support, not prime-only spill arithmetic.

## candidate_theorem_slice

- Candidate theorem slice:
  a late-range `Γ(Z_p × Z_25)` sufficient-condition theorem saying that if
  - `A` is labeled by a fixed `{2,3}`-supported reservoir `A0`,
  - `B` is labeled by a pairwise-coprime set of barriers lying above half the active interval,
  - `C` is labeled by `p - 1` integers in `{1,...,5p+19}` whose prime support avoids the support of `A ∪ B`,
  then the residual complement labels `D`, and the graph is prime.
- The present `p = 107` witness suggests that the specific late data
  `A0` and `B = {1,293,307,311}`
  may support a real post-`97` finite slice, but this solve pass does not claim that slice as a theorem yet.

## smallest_param_shift_to_test

- The smallest next parameter shift worth testing is `p = 109`.
- Reason:
  `p = 107` already shows that the old fixed high barriers can survive well past the preserved `p = 97` window once `C` is unfrozen, so the next honest discriminator is the next odd prime in the same half-barrier regime.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still one solve-stage exact feeder with no Lean closure and no packaged quantified theorem.
- It is publication-relevant because it changes the family story after `p = 97`:
  the frozen-window boundary is not a graph boundary, and the same late high-barrier logic still yields a large exact candidate once `C` is allowed to be a genuine complementary-support block.
- The likely publishable unit is not the single `p = 107` instance by itself.
  It is a post-`97` theorem slice or corollary explaining when a fixed high-barrier complementary-support construction continues to work.

## likely_failure_points

- The structural failure point would be a missed edge type in the support decomposition, though that would contradict the already stable `F25` ring bridge pattern.
- The arithmetic failure point would be accidentally including a label in `C_lab` divisible by `293`, `307`, or `311`.
- A second arithmetic failure point would be miscounting `|C_lab|`; the solve record relies on the exact count `106`.
- Publication-wise, the main weakness is that the record isolates a strong post-`97` pattern but does not yet package the largest honest finite range for that pattern.

## what_verify_should_check

- Recompute the `554` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `4246` edges.
- Check that
  `A0`,
  `{1,293,307,311}`,
  `C_lab = {2 <= n <= 329 : gcd(n,6)=1} \\ {293,307,311}`,
  and the residual complement
  are disjoint and cover exactly `{1,...,554}`.
- Check coprimality on every actual edge from the ring graph.
- Audit whether the same barrier data really continues to work at the next two primes `109` and `113`, or whether `107` is only a one-instance continuation.

## verify_rediscovery

- PASS 1 used a bounded live-web audit aimed at the exact instance notation `Γ(Z_107 × Z_25)`, alternate `Z_107 × Z_25` / `Z_25 × Z_107` notation, the family notation `Γ(Z_p × Z_25)` and `Γ(Z_p × Z_(q^2))`, and the current canonical published source `On Prime Labelings of Zero-Divisor Graphs` by Fox and Mooney.
- The bounded search did not uncover an earlier theorem, proposition, example, observation, or corollary settling the exact instance `Γ(Z_107 × Z_25)`.
- The strongest prior-art hit was the 2025 Fox-Mooney paper, which treats nearby zero-divisor prime-labeling families and still lists `Γ(Z_p × Z_(q^2))` as an open conjectural line rather than a solved theorem family. Since `25 = 5^2`, that source cuts against rediscovery rather than establishing it.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The solve record stays locked to the exact graph-theoretic claim: `Γ(Z_107 × Z_25)` admits a prime labeling on all `554` nonzero zero-divisors.
- The proof uses the full zero-divisor graph of the ring, not a quotient graph, orbit graph, reduced support graph, or weaker sufficient proxy. The support classes `A,B,C,D` are used only as a partition of the actual vertex set.
- The labeling claim is exact: a bijection onto `{1,2,...,554}` with coprime labels on every adjacent pair.
- I did not find wrong-theorem drift, quantifier drift, or a mismatch between the prose claim and the checked witness.

## verify_proof

- I recomputed the vertex partition from the ring definition and recovered the same class sizes `|A| = 20`, `|B| = 4`, `|C| = 106`, `|D| = 424`.
- I independently recomputed the edge set from the ring multiplication law and recovered exactly the four claimed edge interfaces `A-C`, `B-B`, `B-C`, and `B-D`, with counts `2120`, `6`, `424`, and `1696`, for total `4246`.
- Given that exact interface graph, the proof does reduce correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the proposed label sets:
  - every `A0` label is `2,3`-smooth, while every `C_lab` label satisfies `gcd(n,6) = 1`;
  - `B = {1,293,307,311}` is pairwise coprime;
  - the only multiples of `293`, `307`, or `311` in `{1,...,554}` are the barrier labels themselves, so no `D` label can share a factor with `B`.
- First incorrect step found: none.

## verify_adversarial

- I reran `artifacts/z107-z25-prime-zero-divisor-graph/check_witness.py`.
- It reported `vertex_count = 554`, `edge_count = 4246`, `edge_type_counts = {'A-C': 2120, 'B-B': 6, 'B-C': 424, 'B-D': 1696}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also checked independently that `A0`, `B`, `C_lab`, and the residual `D` labels are disjoint and cover exactly `{1,...,554}`.
- I separately checked the arithmetic interfaces directly and found no bad `A-C`, `B-C`, `B-B`, or `B-D` pairs.
- No hidden edge type or computational mismatch appeared.

## verify_theorem_worthiness

- This is stronger than an isolated exact curiosity. The verified witness supports the active post-`97` campaign claim that the `Γ(Z_p × Z_25)` line can survive after the old frozen `C0` window ends, provided `C` is chosen by complementary support rather than by a rigid prime-only block.
- The part that visibly scales is structural:
  - the four-class support decomposition;
  - the reduction to the interfaces `A-C`, `B-B`, `B-C`, `B-D`;
  - the fixed `A0` reservoir;
  - the high-barrier principle that if the nontrivial `B` labels lie above half the interval, then `D` automatically avoids their multiples.
- The part that does not yet scale honestly is the finite arithmetic packaging:
  - the exact cutoff `329` for `C_lab`;
  - the specific barrier set `{293,307,311}`;
  - the unproved range over which the same barrier data keeps working.
- The best honest publication status is still `SLICE_CANDIDATE`, not `INSTANCE_ONLY`, because this feeder directly strengthens a live family theorem slice rather than standing alone.
- The smallest parameter shift that most cleanly tests the claimed template is `p = 109`: it is the next odd prime, it stays in the same `293 > (5p+19)/2` barrier regime, and it tests whether `p = 107` is genuinely part of a post-`97` continuation rather than a one-off arithmetic coincidence.

## verify_verdict

- `VERIFIED`
- The exact feeder survives skeptical verification.
- The honest mathematical status remains `classification = CANDIDATE`, not `EXACT`, because Lean has not formalized the instance.
- The honest publication interpretation is: verified post-`97` feeder evidence for the active `Γ(Z_p × Z_25)` campaign, with real slice leverage but no closed theorem-range statement yet.

## minimal_repair_if_any

- No repair to the witness or proof was needed.
- The only conservative repair is status discipline: keep the run at `classification = CANDIDATE` and `publication_status = SLICE_CANDIDATE` pending generalization and any later Lean packaging.
