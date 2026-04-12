# Solve Record: z61-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_61 × Z_25) prime?`
- Active slug: `z61-z25-prime-zero-divisor-graph`.
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_61 × Z_25)` admits a prime labeling, meaning a bijection from its `324` vertices to `{1,2,...,324}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_61 × Z_25`, not to the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_61` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_61^×}`, size `60`.
  - `D = {(a,5t) : a ∈ Z_61^×, t ∈ {1,2,3,4}}`, size `240`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 61` and `bd = 0 mod 25`.
- Because `Z_61` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - once a classwise label set is fixed, labels may be permuted inside `A`, `C`, and `D` because vertices in those classes have identical neighborhoods; labels on `B` may also be permuted because `B` induces `K_4` and the only internal requirement there is pairwise coprimality.
- Ambiguities or missing definitions:
  - none that block the solve; the family dossier already fixes the four support classes and the standard simple zero-divisor graph convention.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 61` are therefore forced:
  - `A-C = 20 · 60 = 1200`;
  - `B-B = 6`;
  - `B-C = 4 · 60 = 240`;
  - `B-D = 4 · 240 = 960`.
- Total predicted edge count: `1200 + 6 + 240 + 960 = 2406`.
- Therefore the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.

## approach_B

- Construction / extremal / contradiction route.
- First test the older low-barrier package `B = {1,19,23,29}` against the fixed `20`-slot reservoir `A`.
- If that barrier is used at `p = 61`, then every nontrivial multiple of `19`, `23`, and `29` up to `324` must stay out of `D`, hence must be absorbed elsewhere.
- Those forced spill counts are:
  - multiples of `19`: `38,57,76,95,114,133,152,171,190,209,228,247,266,285,304,323`, count `16`;
  - multiples of `23`: `46,69,92,115,138,161,184,207,230,253,276,299,322`, count `13`;
  - multiples of `29`: `58,87,116,145,174,203,232,261,290,319`, count `10`.
- These sets are disjoint because `19·23`, `19·29`, and `23·29` all exceed `324`.
- So the old barrier would force `16 + 13 + 10 = 39` labels away from `D`, which already exceeds the `20` slots of `A`.
- Hence the earlier fixed low barrier is not just inconvenient here; it is structurally incompatible with the current `A` reservoir.
- The natural repair is the later campaign regime: choose a zero-spill high barrier on `B`, with all nontrivial barrier labels above `324/2 = 162`.
- Take
  `B = {1,163,167,173}`.
- Then `163`, `167`, and `173` are pairwise coprime primes, and each exceeds `162`, so no nontrivial multiple of any nontrivial `B` label lies in `{1,...,324}`.
- Thus `B-D` becomes automatic with zero spill.
- With `B` fixed this way, choose `A` from a small smooth palette supported only on the primes `2,3,5,7`:
  `A = {2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,21,24,25,27,28}`.
- Every label in `A` is therefore coprime to any number whose prime factors all lie outside `{2,3,5,7}`.
- For `C`, use the complementary prime pool:
  every prime in `{11,12,...,324}` except the barrier primes `163,167,173`.
- There are `59` such primes, so one more harmless label is still needed to reach `|C| = 60`.
- Add the composite `121 = 11^2`.
- This does not create any new conflict because `121` is also coprime to every label in `A ∪ B`.
- So the candidate `C` block is:
  all primes in `[11,324]` other than `163,167,173`, together with `121`.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,60,240`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
4. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. If every nontrivial label on `B` is greater than half the interval, then `B-D` is automatic because there are no nontrivial multiples of those barrier labels left in the interval.
7. If `A` is chosen from a fixed `2,3,5,7`-smooth palette and `C` is chosen from labels whose prime factors avoid `{2,3,5,7,163,167,173}`, then `A-C` and `B-C` are automatic.
8. Therefore any partition of `{1,...,324}` into class label sets satisfying those conditions gives a prime labeling of the full graph.

## chosen_plan

- Reject the old low barrier `B = {1,19,23,29}` because its forced spill count `39` already exceeds the fixed `20` slots of `A`.
- Use the zero-spill high-barrier regime instead:
  - `B = {1,163,167,173}`;
  - `A` is the fixed `2,3,5,7`-smooth palette of size `20`;
  - `C` is the complementary prime pool, plus one composite supplement `121`;
  - `D` is the remaining complement.
- Only after fixing that full classwise partition, use one tiny checker to validate the witness directly against the ring graph.

## self_checks

- After statement lock:
  - the exact target remains the feeder instance `Γ(Z_61 × Z_25)`;
  - the vertex count `20 + 4 + 60 + 240 = 324` matches the intended label interval.
- After Approach A:
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`;
  - no new edge family appears at `p = 61`;
  - the predicted edge count is `2406`.
- After Approach B:
  - the old low barrier really fails on counting grounds, because its forced spill count is `39 > 20`;
  - the high barrier `163,167,173` gives genuine zero spill since all three exceed `162`;
  - the complementary prime pool contributes `59` clean `C` labels, so exactly one additional nonconflicting composite label is needed.
- After choosing the plan:
  - every label in `A` is `2,3,5,7`-smooth;
  - every nontrivial label in `B` is a prime exceeding half the interval;
  - the supplement `121` is coprime to every label in `A ∪ B`.

## code_used

- No code was used to generate the construction.
- After the reasoning and classwise partition were fixed, a tiny local checker `check_witness.py` was used for witness verification only.
- The checker enumerates the `324` nonzero zero-divisors of `Z_61 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,324}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 324`
  - `edge_count = 2406`
  - `edge_type_counts = {A-C: 1200, B-B: 6, B-C: 240, B-D: 960}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `1,163,167,173` on `B` in any order;
  - put the labels `2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,21,24,25,27,28` on `A` in any order;
  - put on `C` all primes in `[11,324]` except `163,167,173`, together with `121`;
  - put the remaining `240` labels on `D`.
- Why this should work:
  - `B-B` edges:
    `1,163,167,173` are pairwise coprime.
  - `B-D` edges:
    `163`, `167`, and `173` exceed half the interval, so they have no nontrivial multiples in `{1,...,324}`; hence every label outside `B` is automatically coprime to every nontrivial `B` label.
  - `A-C` and `B-C` edges:
    every label in `A` is supported only on the primes `2,3,5,7`;
    every nontrivial label in `B` is one of `163,167,173`;
    every label in `C` is either a prime at least `11` different from `163,167,173`, or the square `121`;
    therefore every `C` label is coprime to every label in `A ∪ B`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit classwise prime-labeling witness.
- The tiny checker confirmed that witness on the full ring graph, not just on the support graph summary.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the exact reduction to `A-C`, `B-B`, `B-C`, `B-D`; the zero-spill principle for barriers above half the interval; and the use of a fixed small-factor palette on `A` against a complementary `C` block.
  - what part does not yet scale:
    the exact supply statement for `C` is still not theoremically closed; at `p = 61`, the pure complementary prime pool supplies only `59 = (p - 1) - 1` labels, so one extra harmless non-prime label `121` is still needed.
  - what theorem slice is suggested:
    a zero-spill high-barrier / complementary-support theorem for `Γ(Z_p × Z_25)` in which `B` is chosen above half the interval, `A` is a fixed small smooth reservoir, and `C` is allowed to use a complementary pool of labels with prime support outside that reservoir, not necessarily only primes.
  - what one or two next feeder instances would help most:
    `Γ(Z_67 × Z_25)` as the next immediate continuation of the zero-spill high-barrier regime, and `Γ(Z_59 × Z_25)` as the nearest backward comparison point if the family dossier needs the exact transition from prime-only `C` to "prime pool plus one supplement."
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is closer to a paper-shaped claim because it isolates a cleaner zero-spill family mechanism and exposes the first precise place where the pure prime-pool version appears one label short.

## family_affinity

- Family affinity is very high.
- This feeder sits directly on the active `Γ(Z_p × Z_25)` campaign line and tests the later zero-spill high-barrier regime rather than the earlier bounded-spill repair.
- The value is not just another exact witness: it pressures the campaign's live publication question about whether the `F25` arithmetic closure should be phrased in terms of complementary prime pools or a broader complementary-support pool.

## generalization_signal

- Generalization signal is strong.
- The decisive new fact at `p = 61` is not graph-theoretic but arithmetic:
  the old low barrier is now impossible for reservoir-size reasons, while the zero-spill high barrier works immediately.
- The second signal is sharper:
  a pure complementary prime pool appears to miss `|C|` by exactly one label here, yet a single square `121` closes the gap without creating any new conflict.
- That suggests the honest live family slice may need to permit a tiny complementary-support supplement rather than insisting that `C` be purely prime.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. choose `B` as a pairwise-coprime high barrier above half the interval so `B-D` is automatic;
  4. choose `A` from a fixed smooth palette with controlled prime support;
  5. choose `C` from labels whose prime factors avoid the support of `A ∪ B`;
  6. assign the residual complement to `D`.
- Relative to the earlier `p = 23` barrier-threshold package, the reusable gain here is that the theorem surface no longer depends on absorbing barrier spill inside `A`; the only live burden is now the size of the complementary-support pool for `C`.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, `Γ(Z_p × Z_25)` is prime whenever `{1,...,5p+19}` contains
  - a four-label pairwise-coprime barrier set `B = {1,b_1,b_2,b_3}` with each `b_i > (5p + 19)/2`,
  - a fixed `20`-label reservoir `A` whose prime support lies in a prescribed small set such as `{2,3,5,7}`,
  - and a complementary set `C` of `p - 1` labels whose prime factors avoid both that small support set and the barrier primes.
- The `p = 61` feeder suggests the theorem should allow `C` to contain a tiny number of composite supplements such as `121`, not only primes.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this line is `p = 67`.
- Reason:
  `p = 61` appears to be the first visible point where the zero-spill high-barrier regime remains clean but the pure complementary prime pool is one label short, so the next odd prime should test whether one supplement remains enough or whether the support pool needs a broader redesign.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage feeder instance with no bounded rediscovery pass in this turn and no Lean closure.
- It is publication-relevant because it isolates a sharper family-level arithmetic decision:
  whether the live `Γ(Z_p × Z_25)` theorem slice should be phrased as a complementary prime-pool theorem or as a slightly broader complementary-support theorem.
- That is a real paper-shaping distinction, not just another isolated label list.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the stable `Γ(Z_p × Z_25)` reduction already used throughout the campaign.
- The arithmetic failure point would be an incorrect count of the complementary prime pool, especially the claim that it contributes exactly `59` labels here.
- Another arithmetic failure point would be overlooking a shared factor between the supplement `121` and some label in `A ∪ B`.
- Publication-wise, the main weakness is that the "one harmless supplement" phenomenon is still observed only at this instance and is not yet a quantified family lemma.

## what_verify_should_check

- Recompute the `324` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `2406` edges.
- Check that the chosen `A`, `B`, and `C` label sets are disjoint and have sizes `20`, `4`, and `60`.
- Check that `C` really consists of exactly the `59` primes in `[11,324]` excluding `163,167,173`, together with `121`.
- Check coprimality on every actual edge from the ring graph.
- In the later bounded rediscovery pass, audit not only the exact instance but also whether any existing family sufficient condition already permits a non-prime supplement in the `C` block.

## verify_rediscovery

- PASS 1 used a bounded live web audit on the exact notation `Γ(Z_61 × Z_25)`, ASCII variants such as `Gamma(Z_61 x Z_25)`, broader family searches for `Γ(Z_p × Z_25)` and `Γ(Z_p × Z_(q^2))`, the canonical source `On prime labelings of zero-divisor graphs`, and a same-source theorem / proposition / example / conjecture check.
- Exact-instance and alternate-notation searches did not reveal an earlier theorem, proposition, example, observation, or corollary explicitly settling the `p = 61, q = 5` case within budget.
- The canonical source check was the Combinatorial Press paper `On prime labelings of zero-divisor graphs`, published online on `2025-11-21`. In that source, nearby solved families include cases such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))`, but the broader family `Γ(Z_p × Z_(q^2))` is still posed there as Conjecture `4.4`, not as a theorem implying `Γ(Z_61 × Z_25)`.
- A bounded follow-up status search did not uncover a later paper or discussion closing that conjectural family or explicitly exhibiting `Γ(Z_61 × Z_25)`.
- Verdict for PASS 1: rediscovery was not established within the bounded audit.

## verify_faithfulness

- The solve record is aimed at the exact intended statement: existence of a prime labeling for the full simple zero-divisor graph `Γ(Z_61 × Z_25)` on the `324` nonzero zero-divisors, with labels bijectively covering `{1,...,324}`.
- There is no wrong-theorem drift to a support graph, induced subgraph, proxy sufficient condition, or partial labeling. The support decomposition is used only as a reduction device for the exact graph.
- One sentence needed tightening during verification: the four vertices of `B` do not literally have identical neighborhoods in the simple graph, because each misses itself inside the `B` clique. That does not affect the witness, since any permutation of the four chosen `B` labels still preserves validity exactly when those four labels are pairwise coprime.
- With that wording repair, the claimed result matches the intended exact instance and should remain classified as `CANDIDATE`, not `VARIANT` and not `EXACT`.

## verify_proof

- I recomputed the vertex partition directly from the ring definition and recovered `|A| = 20`, `|B| = 4`, `|C| = 60`, and `|D| = 240`, for total `324` vertices.
- I independently recomputed the exact edge set and again obtained only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `1200`, `6`, `240`, and `960`, for total `2406` edges.
- Given that support graph, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly. There are `66` primes up to `324`, so the `C` block really does contain exactly `59` primes in `[11,324]` after removing `163`, `167`, and `173`, and the supplement `121` is coprime to every label in `A ∪ B`.
- The zero-spill claim on `B` is correct: because `163`, `167`, and `173` are all greater than `324/2`, no nontrivial multiple of any of them remains in `{1,...,324}`, so every `D` label is automatically coprime to every nontrivial `B` label.
- First incorrect step found: none after the neighborhood wording repair above. The proof is still hand-built instance arithmetic, but the witness argument itself is correct.

## verify_adversarial

- I reran `artifacts/z61-z25-prime-zero-divisor-graph/check_witness.py`. It again reported `vertex_count = 324`, `edge_count = 2406`, `edge_type_counts = {'A-C': 1200, 'B-B': 6, 'B-C': 240, 'B-D': 960}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran independent checks outside the artifact checker to confirm:
  - the four class label sets are disjoint and cover exactly `{1,...,324}`;
  - the only edge types are `A-C`, `B-B`, `B-C`, and `B-D`;
  - every `A-C`, `B-C`, and `B-D` gcd constraint is satisfied, and no `D` label shares a factor with `163`, `167`, or `173`;
  - the supplement `121` does not introduce a hidden common factor with any label in `A ∪ B`.
- I did not find a hidden edge type, a mislabeled vertex, or a divisibility obstruction breaking the witness.

## verify_theorem_worthiness

- This is still an instance result, not a theorem slice by itself. The structural part that scales is the four-class support reduction together with the zero-spill barrier idea: choose the nontrivial `B` labels above half the interval so `B-D` becomes automatic.
- The part that does not yet scale automatically is the arithmetic supply statement for the `C` block. At `p = 61`, the pure complementary prime pool is one label short, and the current repair is a hand-picked composite supplement `121`.
- Relative to the earlier bounded-spill feeders, this does materially sharpen the family campaign. The old low barrier `B = {1,19,23,29}` is no longer viable because its forced spill count is `39 > 20`, while the high-barrier route works immediately and isolates a cleaner family-level question about complementary-support rather than bounded spill.
- The best honest publication status for this artifact is `SLICE_CANDIDATE`, not `INSTANCE_ONLY`, because it is still feeder evidence but it directly tests the live family theorem surface and exposes the first concrete point where a pure prime-pool statement appears too rigid.
- The smallest parameter shift that would best test the claimed template is `Γ(Z_59 × Z_25)` as a backward comparison to locate whether the one-supplement phenomenon starts exactly here; the next forward continuation is `Γ(Z_67 × Z_25)`.

## verify_verdict

- `VERIFIED`
- No rediscovery was established in the bounded prior-art pass, the claim matches the intended instance after a tiny wording repair, and the explicit witness survived independent skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- Repaired one sentence in the definitions section: only `A`, `C`, and `D` have identical neighborhoods; `B` is handled instead by the fact that it is a `K_4` with pairwise-coprime labels.
