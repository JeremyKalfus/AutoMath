# Solve Record: z101-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_101 × Z_25) prime?`
- Active slug: `z101-z25-prime-zero-divisor-graph`.
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_101 × Z_25)` admits a prime labeling, meaning a bijection from its `524` vertices to `{1,2,...,524}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_101 × Z_25`, while extracting only reusable structure that is honestly visible from this one instance.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_101` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the standard four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_101^×}`, size `100`.
  - `D = {(a,5t) : a ∈ Z_101^×, t ∈ {1,2,3,4}}`, size `400`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 101` and `bd = 0 mod 25`.
- Because `101` is prime, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - labels may be permuted inside each support class once the classwise label sets are fixed, because vertices in the same class have identical neighborhoods.
- Ambiguities, conventions, or missing definitions:
  - none block the solve;
  - the family dossier already fixes the standard zero-divisor graph convention and the support-class notation.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is the same as in the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 101` are therefore forced:
  - `A-C = 20 · 100 = 2000`;
  - `B-B = 6`;
  - `B-C = 4 · 100 = 400`;
  - `B-D = 4 · 400 = 1600`.
- Total predicted edge count: `2000 + 6 + 400 + 1600 = 4006`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Brief self-check after Approach A:
  - vertex count check: `20 + 4 + 100 + 400 = 524`;
  - no new graph-theoretic obstruction appears at `p = 101`, because the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`.

## approach_B

- Construction / extremal route using the later high-barrier complementary-support wrapper rather than the earlier low-barrier spill template.
- Fix the campaign's frozen low-support reservoir
  `A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
- Every label in `A0` is `{2,3}`-smooth, so any `C` label whose prime support avoids `{2,3}` is automatically coprime to every label in `A`.
- For `B`, choose the zero-spill barrier set
  `B = {1,263,269,271}`.
- Why these are the right barrier labels:
  - `263,269,271` are distinct primes;
  - `524 < 2·263`, `524 < 2·269`, and `524 < 2·271`;
  - hence any label in `{1,...,524}` divisible by one of `263,269,271` must equal that barrier prime itself.
- Therefore `B-D` will be automatic as long as `D` avoids those three barrier labels.
- This suggests choosing `C` entirely from labels whose prime support avoids `{2,3,263,269,271}`.
- A clean exact choice is:
  `C = {n ∈ {1,...,311} : gcd(n,6) = 1} \ {1,263,269,271}`.
- Count check for this `C`:
  - `311 = 6·51 + 5`;
  - in each full block of six integers, exactly two are coprime to `6`;
  - so `|{n ∈ {1,...,311} : gcd(n,6)=1}| = 2·51 + 2 = 104`;
  - removing `1,263,269,271` leaves exactly `104 - 4 = 100 = |C|`.
- Support-avoidance check for this `C`:
  - `gcd(n,6)=1` excludes prime divisors `2` and `3`;
  - because `2·263 > 311`, `2·269 > 311`, and `2·271 > 311`, any element of `{1,...,311}` divisible by one of `263,269,271` must be exactly that prime;
  - excluding `263,269,271` therefore excludes all barrier-prime support as well.
- Then let `D` be the residual complement of `A ∪ B ∪ C` inside `{1,...,524}`.
- Brief self-check after Approach B:
  - the construction uses the exact family wrapper language now active in the repo;
  - the barrier clique has zero spill because every nontrivial multiple of `263`, `269`, or `271` exceeds `524`;
  - the proposed `C` set has exactly the required size `100`.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,100,400`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A` has prime support contained in `{2,3}` and every label on `C` avoids prime divisors `2` and `3`, then all `A-C` edges are valid.
4. If the four labels on `B` are `1` together with three distinct primes, then `B-B` is valid.
5. If every label on `C` also avoids the three barrier primes used on `B`, then all `B-C` edges are valid.
6. If the three nontrivial barrier primes lie above half the active interval `{1,...,524}`, then any interval label outside `B` is automatically coprime to every label on `B`, so all `B-D` edges are valid once `D` avoids the barrier set.
7. Therefore any classwise partition of `{1,...,524}` with
   - `A = A0`,
   - `B = {1,263,269,271}`,
   - `C` avoiding prime support `{2,3,263,269,271}`,
   - `D` the residual complement,
   gives a prime labeling.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Abandon the old low-barrier spill language, because at `p = 101` the later high-barrier wrapper is strictly cleaner and already matches the family theorem surface.
- Fix `A = A0` and `B = {1,263,269,271}`.
- Choose `C` by a counted support-avoidance rule, not by a hand-picked prime list:
  `C = {n ≤ 311 : gcd(n,6)=1} \ {1,263,269,271}`.
- Let `D` be the remaining labels.
- Only after that exact reasoning is fixed, use one tiny checker to validate the witness against the full ring graph.
- Brief self-check after choosing the plan:
  - this remains reasoning-first because the class sets are forced by the support graph and elementary divisibility, not by search;
  - minimal code is justified only as post-construction witness verification.

## self_checks

- Statement lock:
  - the exact target is the feeder instance `Γ(Z_101 × Z_25)`;
  - the label interval length `524` matches the vertex count.
- Structural reduction:
  - no edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the graph again collapses to three arithmetic interfaces.
- Construction:
  - `A0` has size `20`;
  - `B = {1,263,269,271}` is pairwise coprime;
  - the proposed `C` set has size exactly `100`;
  - every `C` label avoids prime support `{2,3,263,269,271}`.
- Final witness:
  - `A`, `B`, and `C` are disjoint;
  - the remaining complement has size `400`, exactly `|D|`;
  - no nontrivial multiple of `263`, `269`, or `271` can occur in `D`;
  - every label in `A ∪ B` is coprime to every label in `C`.

## code_used

- Minimal code was used only after the reasoning and classwise witness were fixed.
- A tiny local checker `check_witness.py` enumerates the `524` nonzero zero-divisors of `Z_101 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,524}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 524`
  - `edge_count = 4006`
  - `edge_type_counts = {A-C: 2000, B-B: 6, B-C: 400, B-D: 1600}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the fixed reservoir
    `A = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`
    on the `20` vertices of support class `A` in any order;
  - put
    `B = {1,263,269,271}`
    on the `4` vertices of support class `B` in any order;
  - put
    `C = {n ∈ {1,...,311} : gcd(n,6)=1} \ {1,263,269,271}`
    on the `100` vertices of support class `C` in any order;
  - put the remaining `400` labels in `{1,...,524}` on support class `D` in any order.
- Why this works:
  - `B-B` edges:
    `1,263,269,271` are pairwise coprime.
  - `A-C` edges:
    every label on `A` is `{2,3}`-smooth, while every label on `C` is coprime to `6`, so every `A` label is coprime to every `C` label.
  - `B-C` edges:
    every label on `C` avoids prime support `263,269,271`, so it is coprime to every nontrivial label on `B`, and also to `1`.
  - `B-D` edges:
    the only interval labels divisible by `263`, `269`, or `271` are those barrier labels themselves, because each lies above half the interval; since `D` is the complement of `A ∪ B ∪ C`, it contains none of them.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit high-barrier complementary-support witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the fixed `A0` reservoir; the zero-spill high-barrier idea on `B`; and the wrapper-language condition that `C` need only avoid the prime support of `A0` and the barrier primes.
  - what part does not:
    this record does not prove a quantified family theorem producing `p - 1` support-avoiding `C` labels for all odd primes; it only proves that the construction works at `p = 101`.
  - what theorem slice is suggested:
    a high-barrier complementary-support sufficient-condition theorem for `Γ(Z_p × Z_25)` with fixed `A = A0`, barrier set `B = {1,b1,b2,b3}` above half the interval, and `C` chosen from labels whose prime support avoids `{2,3,b1,b2,b3}`.
  - what one or two next feeder instances would help most:
    `Γ(Z_103 × Z_25)` first, then `Γ(Z_107 × Z_25)`, because they probe whether the same post-`97` high-barrier support-avoidance package keeps working beyond this first reopened boundary case.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is closer to a paper-shaped claim than the earlier spill-style feeders because it lands directly inside the exact wrapper language already preserved by the family campaign.

## family_affinity

- Family affinity is very high.
- This feeder sits exactly on the active `Γ(Z_p × Z_25)` publication line and tests the next honest boundary after the preserved finite-range story through `p = 97`.
- The main campaign value is that the instance closes in the high-barrier complementary-support language already used by the exact family wrapper theorem.

## generalization_signal

- Generalization signal is strong.
- The witness no longer needs ad hoc below-half spill bookkeeping. At `p = 101`, the clean high-barrier regime works:
  - `A` is frozen as `A0`;
  - `B` is a zero-spill barrier clique above half the interval;
  - `C` is counted by support avoidance rather than by a prime-only threshold.
- The honest family question suggested here is not graph structure but arithmetic supply:
  for which odd primes `p` can one produce `p - 1` labels avoiding the prime support of `A0` and a chosen three-prime high barrier?

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. fix `A = A0`, where every label is `{2,3}`-smooth;
  3. choose `B = {1,b1,b2,b3}` with distinct primes above half the interval;
  4. choose `C` from labels whose prime support avoids `{2,3,b1,b2,b3}`;
  5. assign the residual complement to `D`;
  6. invoke the support-graph reduction to discharge the full graph.
- Relative to the earlier `p = 13,17,19,23` feeders, the reusable gain here is conceptual:
  the witness is better phrased in the exact wrapper language of support avoidance than in terms of low-barrier spill arithmetic.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, if there exist distinct primes `b1,b2,b3` with `5p+19 < 2b_i` for each `i`, and if the interval `{1,...,5p+19}` contains `p - 1` labels whose prime support avoids `{2,3,b1,b2,b3}`, then taking
  - `A = A0`,
  - `B = {1,b1,b2,b3}`,
  - `C` as any such support-avoiding set of size `p - 1`,
  - `D` as the complement,
  yields a prime labeling of `Γ(Z_p × Z_25)`.
- The present feeder shows that this wrapper-language slice is not empty beyond the preserved `59 ≤ p ≤ 97` window.

## smallest_param_shift_to_test

- The smallest next parameter shift to test is `p = 103`.
- Reason:
  `p = 101` is the first reopened post-`97` boundary probe, so `p = 103` is the next clean discriminator for whether the same high-barrier complementary-support package persists without repair.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder with no rediscovery audit in this pass and no Lean closure.
- It is publication-relevant because it gives a strong exact witness in the same language as the already checked family wrapper theorem, rather than in an obsolete local template.
- The likely publishable unit is still a theorem slice or finite-range corollary about support-avoiding `C` supply, not the single `p = 101` instance by itself.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the stable `Γ(Z_p × Z_25)` decomposition.
- The arithmetic failure point would be a mislabeled `C` element carrying prime support `2`, `3`, `263`, `269`, or `271`.
- Another failure point would be a mistaken count of the support-avoiding set `C`.
- Publication-wise, the main weakness is that the witness does not yet prove the family-level `C`-supply lemma it suggests.

## what_verify_should_check

- Recompute the `524` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `4006` edges.
- Check that
  - `A = A0`,
  - `B = {1,263,269,271}`,
  - `C = {n ≤ 311 : gcd(n,6)=1} \ {1,263,269,271}`,
  are disjoint and have sizes `20,4,100`.
- Check that the remaining complement has size `400`.
- Check coprimality on every actual edge from the ring graph.
- In the bounded rediscovery pass, audit not only the exact `p = 101` instance but also whether any existing wrapper-language sufficient-condition theorem already implies this high-barrier complementary-support witness.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact tuple, alternate notation, the ambient family notation, and the current canonical source on prime-labeled zero-divisor graphs.
- Exact-instance searches on `Γ(Z_101 × Z_25)` and ASCII variants such as `Z_101 x Z_25` did not reveal an earlier theorem, proposition, example, observation, or corollary settling this exact case within budget.
- I rechecked the canonical source `On Prime Labelings of Zero-Divisor Graphs` (Congressus Numerantium 236, 2025). Within the bounded source-level audit, it still treats the ambient `Γ(Z_p × Z_{q^2})` line as conjectural rather than already closed, and I did not find a same-source theorem / proposition / example / observation / corollary covering `Z_25`, `p = 101`, or a directly implying published sufficient condition.
- One bounded recent-status query also did not produce a later paper, citation trail, or discussion establishing the exact `p = 101, q = 5` instance within budget.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The solve record answers the exact graph-theoretic statement named in the title and canonical question: whether the full simple zero-divisor graph `Γ(Z_101 × Z_25)` admits a prime labeling on all `524` nonzero zero-divisors.
- There is no wrong-theorem drift to a support graph, quotient graph, partial labeling, or weaker proxy statement. The support decomposition is used only as a reduction for the full graph.
- The feeder framing in `selected_problem.md` is campaign metadata, not a change in theorem content, so the mathematical claim remains faithful to the intended instance.

## verify_proof

- I independently recomputed the zero-divisor partition from the ring definition and recovered class sizes `|A| = 20`, `|B| = 4`, `|C| = 100`, `|D| = 400`, so the label interval `{1,...,524}` is the correct target.
- I independently recomputed the exact edge pattern and obtained only `A-C`, `B-B`, `B-C`, and `B-D`, with counts `2000`, `6`, `400`, and `1600`, for total `4006` edges.
- Given that support graph, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the displayed witness:
  - every label on `A` is `{2,3}`-smooth and every label on `C` satisfies `gcd(n,6) = 1`, so all `A-C` edges are valid;
  - `B = {1,263,269,271}` is pairwise coprime;
  - the only labels up to `524` divisible by `263`, `269`, or `271` are those primes themselves, so once `D` is the complement of `A ∪ B ∪ C`, every `B-D` edge is automatically coprime.
- First incorrect step found: none.

## verify_adversarial

- I reran `artifacts/z101-z25-prime-zero-divisor-graph/check_witness.py`.
- It reported `vertex_count = 524`, `edge_count = 4006`, `edge_type_counts = {'A-C': 2000, 'B-B': 6, 'B-C': 400, 'B-D': 1600}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran an independent computation outside the artifact checker to confirm:
  - the four label classes are disjoint and cover exactly `{1,...,524}`;
  - `|C| = 100` for `C = {n ≤ 311 : gcd(n,6)=1} \\ {1,263,269,271}`;
  - the only multiples of the barrier primes inside `{1,...,524}` are `263`, `269`, and `271` themselves;
  - there is no hidden edge type beyond `A-C`, `B-B`, `B-C`, `B-D`.
- I did not find a counterexample edge, a count mismatch, or a hidden divisibility obstruction.

## verify_theorem_worthiness

- This witness is structurally aligned with a real family statement: it uses the same four-class support reduction and the same high-barrier complementary-support wrapper language already active in the `Γ(Z_p × Z_25)` campaign.
- What scales is the structural reduction: classify by support, reduce to the three interfaces, freeze `A = A0`, use a four-label high barrier on `B`, and ask only for a size `p - 1` complementary-support block for `C`.
- What does not yet scale is the arithmetic existence step. This record proves only that one such `C` block exists at `p = 101`; it does not prove a quantified `C`-supply lemma or a new finite-range corollary beyond the preserved campaign boundary.
- The best honest publication role for this artifact is therefore still `INSTANCE_ONLY`. It is useful feeder evidence for a future wrapper-language `C`-supply statement, but it is not itself a theorem slice.
- The smallest next parameter shift that most tests the claimed template is `Γ(Z_103 × Z_25)`, because it is the immediate post-`101` boundary probe for whether the same support-avoidance package keeps working without repair.

## verify_verdict

- `VERIFIED`
- No rediscovery was established within the bounded prior-art pass, the claim matches the exact intended instance, and the explicit witness survived skeptical recomputation.
- The classification remains `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- None. No conservative repair was needed.
