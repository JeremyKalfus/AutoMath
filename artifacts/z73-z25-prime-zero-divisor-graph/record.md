# Solve Record: z73-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Gamma(Z_73 x Z_25) prime?`
- Active slug: `z73-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_73 × Z_25)` admits a prime labeling, meaning a bijection from its `384` vertices to `{1,2,...,384}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_73 × Z_25`, not to a full family theorem.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_73` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the usual four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_73^×}`, size `72`.
  - `D = {(a,5t) : a ∈ Z_73^×, t ∈ {1,2,3,4}}`, size `288`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 73` and `bd = 0 mod 25`.
- Because `73` is prime, `ac = 0 mod 73` iff `a = 0` or `c = 0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions and ambiguities locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - labels are exactly `{1,...,384}`;
  - labels may be permuted inside each support class because vertices in the same class have the same neighborhood;
  - the family record already treats the late-regime headline as the fixed-`A₀` / high-barrier / complementary-support `C` slice, so this feeder is judged against that theorem shape rather than against the older strict prime-only `C` clause.
- Fixed reservoir used here:
  `A₀ = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
  Every element of `A₀` has prime support contained in `{2,3}`.

## approach_A

Structural / invariant route through the support graph.

- The support decomposition is unchanged from earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- The forced edge counts at `p = 73` are:
  - `A-C = 20 · 72 = 1440`;
  - `B-B = 6`;
  - `B-C = 4 · 72 = 288`;
  - `B-D = 4 · 288 = 1152`.
- Total predicted edge count: `1440 + 6 + 288 + 1152 = 2886`.
- Therefore the graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.

## approach_B

Construction / extremal route using the live fixed-`A₀` and complementary-support template.

- Let `N = 5p + 19 = 384`.
- Freeze `A = A₀`.
- Choose a high barrier above half the interval:
  `B = {1,193,197,199}`.
- This is attractive because each nontrivial barrier prime exceeds `N/2 = 192`, so:
  - the labels on `B` are pairwise coprime;
  - no nontrivial multiple of `193`, `197`, or `199` lies in `{1,...,384}`;
  - hence the entire `B-D` interface is zero-spill.
- For `C`, the strict prime-only complementary pool is almost enough but misses by exactly one:
  - `π(384) = 76`;
  - removing the forbidden primes `{2,3,193,197,199}` leaves `76 - 5 = 71` allowed primes;
  - but `|C| = 72`.
- So the clean late-regime candidate is to keep all `71` allowed primes and add one composite label whose prime support still avoids `{2,3,193,197,199}`.
- The smallest natural supplement is `25 = 5^2`.
  Its prime support is `{5}`, so it is coprime to every label in `A₀` and to every label in `B`.
- This gives the explicit candidate block
  `C = {5,7,11,13,17,19,23,25,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383}`.
- Then `D` is the residual complement of `A ∪ B ∪ C` in `{1,...,384}`.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,72,288`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For the chosen `A₀`, every label on `A` has prime support contained in `{2,3}`.
7. For the chosen high barrier `B = {1,193,197,199}`, every nontrivial barrier prime is above `N/2`, so no label in `D` can share a barrier prime factor with `B`.
8. Every label in the proposed `C` block has prime support avoiding `{2,3,193,197,199}`.
9. Therefore the classwise coprimality obligations hold, and any within-class bijection yields a prime labeling of `Γ(Z_73 × Z_25)`.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Switch fully to the live late-regime family template:
  `A = A₀`, a high barrier on `B`, and a complementary-support pool on `C`.
- First prove that the prime-only complementary-support pool is short by exactly one at `N = 384`.
- Then repair that shortage with the single composite label `25`, because its prime support still avoids the forbidden palette.
- Only after the explicit class partition is fixed, use one tiny checker to verify the witness directly against the ring graph.

## self_checks

- After statement lock:
  - the target remains the exact feeder instance `Γ(Z_73 × Z_25)`;
  - the label interval length `384` matches the vertex count `20 + 4 + 72 + 288`.
- After definitions:
  - the same support classes and the same ring-law adjacency criterion as earlier `F25` feeders are being used;
  - no hidden convention about loops, zero vertex, or label interval is left implicit.
- After Approach A:
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`;
  - there is no new edge family introduced by the larger prime `73`.
- After Approach B:
  - the late-regime arithmetic really is a one-supplement problem here: `71` allowed primes for `72` `C`-slots;
  - `25` is admissible because its only prime factor is `5`, outside `{2,3,193,197,199}`;
  - the chosen high barrier is zero-spill because `2 · 193 > 384`.
- After choosing the plan:
  - this is still reasoning-first, because the witness is forced by support decomposition plus finite divisibility counting rather than by search;
  - minimal code is justified only as post-construction witness verification.

## code_used

- Minimal code was used only after the reasoning and explicit classwise partition were fixed.
- A tiny checker `check_witness.py` enumerates the `384` nonzero zero-divisors of `Z_73 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,384}`, and tests `gcd = 1` on every edge.
- Checker result:
  - `vertex_count = 384`
  - `edge_count = 2886`
  - `edge_type_counts = {A-C: 1440, B-B: 6, B-C: 288, B-D: 1152}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

Current best solve-stage candidate:

- Put
  `A = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
- Put
  `B = {1,193,197,199}`.
- Put
  `C = {5,7,11,13,17,19,23,25,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383}`.
- Put the remaining `288` labels on `D` in any order.

Why this works:

- `B-B` edges:
  `1,193,197,199` are pairwise coprime.
- `A-C` edges:
  every label in `A` has prime support inside `{2,3}`, while every label in `C` has prime support avoiding `{2,3}`.
- `B-C` edges:
  every label in `C` avoids the barrier primes `193,197,199`; because those barrier primes exceed half the interval, the only multiples they could have in the interval are themselves, and those are not used in `C`.
- `B-D` edges:
  there are no nontrivial multiples of `193`, `197`, or `199` in `{1,...,384}`, so every `D`-label is automatically coprime to the nontrivial barrier labels.
- There are no other edges.

Strong-result extraction:

- The instance appears prime, with an explicit classwise witness verified by a tiny checker.
- What part of the argument scales:
  the four-class support decomposition, the fixed-`A₀` reservoir, the high-barrier zero-spill mechanism, and the broader complementary-support criterion for the `C` block.
- What part does not yet scale automatically:
  the arithmetic supply statement for how many complementary-support labels are available in `{1,...,5p+19}` and how many supplements beyond the prime-only pool are needed at each `p`.
- What theorem slice is suggested:
  a fixed-`A₀` / high-barrier / complementary-support theorem for `Γ(Z_p × Z_25)` in which `C` may use any labels whose prime support avoids `{2,3,b₁,b₂,b₃}`, not just primes.
- What one or two next feeder instances would help most:
  `z79-z25-prime-zero-divisor-graph` is the next discriminator for whether the one-supplement repair remains enough; if that still works cleanly, the next odd-prime step after it will test whether the same theorem shape persists without new hypotheses.
- Whether this package is still just an instance or closer to a paper-shaped claim:
  it is still only an instance-level candidate in solve, but it is materially closer to a paper-shaped claim because it matches the live family theorem shape rather than a discarded subtemplate.

## family_affinity

- Family affinity is high.
- This feeder sits exactly on the live `Γ(Z_p × Z_25)` publication line and tests the post-`z71` statement shape rather than a random exact instance.
- The witness supports the campaign move from a prime-only `C` clause to a complementary-support `C` clause.

## generalization_signal

- Generalization signal is strong.
- At `p = 73`, the fixed `A₀` reservoir and high barrier still work unchanged.
- The prime-only complementary pool is short by exactly one, yet the graph still labels after adding the single complementary-support label `25`.
- So the honest signal is not “the prime-only corollary keeps surviving.” It is “the broader complementary-support theorem shape survives another late-regime discriminator.”

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. freeze `A` on `A₀`, whose prime support is only `{2,3}`;
  4. choose `B = {1,b₁,b₂,b₃}` with the nontrivial barrier primes above half the interval;
  5. choose `C` from labels whose prime support avoids `{2,3,b₁,b₂,b₃}`;
  6. let `D` absorb the remaining interval.
- At `z73`, the only non-prime ingredient needed in `C` is a single supplementary label `25`, so the reusable feature is the support-avoidance condition, not primality of the `C` labels themselves.

## candidate_theorem_slice

- Candidate slice:
  for odd primes `p` with `5p + 19 ≥ 108`, if one can choose
  - `A = A₀`,
  - `B = {1,b₁,b₂,b₃}` with distinct primes `b₁,b₂,b₃ > (5p + 19)/2`,
  - `C` of size `p - 1` from labels in `{1,...,5p+19}` whose prime support avoids `{2,3,b₁,b₂,b₃}`,
  - and `D` as the residual complement,
  then all classwise coprimality obligations of the four-class reduction hold, so `Γ(Z_p × Z_25)` is prime.
- The `z73` feeder specifically suggests the one-supplement corollary where the prime-only pool is short by exactly one but one composite complementary-support label fills the gap.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this live theorem shape is `p = 79`.
- Reason:
  `z71` is the first preserved one-supplement late-regime case, and `z73` appears to confirm that the same repair is not isolated.
  The next untested campaign-designated discriminator is therefore `z79`.

## why_this_is_or_is_not_publishable

- This is not publishable by itself.
- It is still a solve-stage exact feeder with no bounded rediscovery audit in this artifact and no Lean closure.
- It is publication-relevant because it supports the live family headline:
  the fixed-`A₀` / high-barrier / complementary-support theorem is a better description of the `F25` line than the strict prime-only clause.
- So the right publication interpretation is:
  not a paper-ready result,
  but a strong feeder that narrows the theorem statement the paper should actually try to freeze.

## likely_failure_points

- A structural failure would mean the support decomposition omitted an edge type, but that would contradict the already stable `F25` support template.
- An arithmetic failure would mean some `C` label shares a forbidden prime factor with `A ∪ B`; the only non-prime `C` label is `25`, so this is easy to audit.
- Another arithmetic failure would mean a hidden multiple of `193`, `197`, or `199` lies in the interval, but `2 · 193 > 384` rules that out immediately.
- Publication-wise, the main weakness is that the argument is still instance-specific about the supplement count in `C`.

## what_verify_should_check

- Recompute the `384` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `2886` edges.
- Check that the four label classes are disjoint and cover exactly `{1,...,384}`.
- Check coprimality on every actual edge from the ring graph.
- Audit the exact instance against the current family theorem choice:
  verify that this really is evidence for the complementary-support `C` slice and not for the obsolete prime-only headline.
- In the later bounded rediscovery pass, ask not only whether `Γ(Z_73 × Z_25)` is already settled, but also whether any known sufficient-condition theorem already implies the fixed-`A₀` / complementary-support construction used here.

## verify_rediscovery

- PASS 1 used the full bounded budget on exact-instance notation, alternate notation, family notation, and the most relevant current source on zero-divisor prime labelings.
- Exact-instance and alternate-notation searches on `Γ(Z_73 × Z_25)`, `Gamma(Z_73 x Z_25)`, `Z_73 × Z_25` with `zero-divisor graph` and `prime labeling`, and `Γ(Z_p × Z_25)` / `Γ(Z_p × Z_(q^2))` with `prime labeling` did not produce a theorem, proposition, example, observation, or corollary settling this exact case within budget.
- The canonical-source check focused on Fox and Mooney, `On Prime Labelings of Zero-Divisor Graphs` (Combinatorial Press / Congressus Numerantium, 2025). Within that source I did not find `Z_25`, `Γ(Z_p × Z_25)`, `Γ(Z_73 × Z_25)`, or a same-source result directly implying this instance.
- The bounded title/source sweep instead reinforced the opposite prior-art signal: the ambient `Γ(Z_p × Z_(q^2))` line still appears to be treated there as open rather than already settled.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The solve artifact stays on the exact graph-level question `Γ(Z_73 × Z_25)` and does not drift to a quotient graph, a partial support graph, or a weaker sufficient condition detached from the actual ring graph.
- The proof target is still the exact intended feeder instance: a bijection from all `384` vertices to `{1,...,384}` with coprime labels on every actual edge.
- The family-level prose in the solve record is correctly framed as interpretation of the instance, not as a claim that a family theorem has already been proved.
- I found no wrong-theorem drift, quantifier drift, changed definition, or mismatch between the prose statement and the solved claim.

## verify_proof

- I re-derived the support decomposition from the ring law. The nonzero zero-divisors of `Z_73 × Z_25` split exactly into classes `A,B,C,D` of sizes `20,4,72,288`, totaling `384`.
- I rechecked adjacency from coordinatewise zero product. The only edge types are `A-C`, `B-B`, `B-C`, and `B-D`, with counts `1440`, `6`, `288`, and `1152`, total `2886`.
- Given that support graph, the solve reduction is correct: it is enough to prove
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the proposed label sets:
  - every label in `A` has prime support inside `{2,3}`;
  - every label in `C` has prime support avoiding `{2,3,193,197,199}`, including the lone composite supplement `25`;
  - `B = {1,193,197,199}` is pairwise coprime;
  - since `2·193 > 384`, `2·197 > 384`, and `2·199 > 384`, no label in `D` can share a nontrivial barrier prime with `B`.
- First incorrect step found: none.

## verify_adversarial

- I reran the provided checker `artifacts/z73-z25-prime-zero-divisor-graph/check_witness.py`. It reported `vertex_count = 384`, `edge_count = 2886`, `edge_type_counts = {'A-C': 1440, 'B-B': 6, 'B-C': 288, 'B-D': 1152}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran an independent one-off arithmetic check outside the checker to confirm that the four label sets are disjoint, cover exactly `{1,...,384}`, and satisfy the full interface conditions `A-C`, `B-B`, `B-C`, and `B-D`.
- The main place to break this witness would have been a hidden forbidden factor in `C` or an unseen multiple of `193`, `197`, or `199` in `D`; neither failure mode occurs.
- I did not find a computation/prose mismatch, a hidden edge type, or a fragile case split that invalidates the candidate witness.

## verify_theorem_worthiness

- This feeder does suggest a real theorem slice rather than a purely hand-picked one-off. The structural mechanism is exactly the live `Γ(Z_p × Z_25)` four-class reduction with fixed `A₀`, a high barrier on `B`, and a complementary-support `C` block.
- What clearly scales:
  - the ring-to-support decomposition into `A,B,C,D`;
  - the reduction to the interfaces `A-C`, `B-B`, `B-C`, and `B-D`;
  - the fixed-`A₀` idea and the high-barrier zero-spill mechanism;
  - the broader rule that `C` only needs prime support avoiding `{2,3,b₁,b₂,b₃}`, not literal primality of every `C` label.
- What does not yet scale automatically:
  - proving a general supply lemma for enough complementary-support labels in the `C` block;
  - controlling exactly how many composite supplements are needed as `p` grows;
  - turning the instance arithmetic into a referee-facing quantified theorem.
- Best honest publication status is not merely `INSTANCE_ONLY`. Because this verified feeder directly strengthens the live complementary-support slice, the conservative status is `SLICE_CANDIDATE`.
- The smallest next feeder that most tests the claimed template is `Γ(Z_79 × Z_25)`: it is the next campaign-designated late-regime discriminator after this `p = 73` confirmation of the one-supplement pattern.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- The exact intended statement appears to be correctly proved by the current explicit witness, and the bounded rediscovery pass did not establish that the instance is already settled in prior art.
- The harness classification must remain `CANDIDATE`, not `EXACT`, because Lean has not been completed.
- `lean_ready = true`

## minimal_repair_if_any

- None. No conservative patch to the mathematical content was needed.
