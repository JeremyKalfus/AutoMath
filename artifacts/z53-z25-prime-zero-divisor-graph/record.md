# Solve Record: z53-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_53 × Z_25) prime?`
- Active slug: `z53-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_53 × Z_25)` admits a prime labeling, meaning a bijection from its `284` vertices to `{1,2,...,284}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_53 × Z_25`, not the full family `Γ(Z_p × Z_25)`.
- Brief self-check:
  - the vertex-count formula `5p + 19` gives `5·53 + 19 = 284`, matching the intended label interval;
  - the problem is exact-instance solve, but it is being used to pressure the live `F25` arithmetic existence layer.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_53` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's standard four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`;
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`;
  - `C = {(a,0) : a ∈ Z_53^×}`, size `52`;
  - `D = {(a,5t) : a ∈ Z_53^×, t ∈ {1,2,3,4}}`, size `208`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 53` and `bd = 0 mod 25`.
- Because `Z_53` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - labels may be permuted freely inside `A`, `C`, and `D` once the class label sets are fixed, because those classes have uniform neighborhoods;
  - the four `B` vertices form a `K_4`, so any permutation of a pairwise-coprime `B` label set preserves the witness.
- Ambiguities or missing definitions:
  - none that block the solve; the campaign dossier already fixes the graph convention and the four support classes.
- Brief self-check:
  - `20 + 4 + 52 + 208 = 284`;
  - the only point needing care is to distinguish "uniform neighborhoods" for `A,C,D` from the `K_4` behavior of `B`.

## approach_A

- Structural / invariant route through the support graph.
- The exact support interfaces are unchanged from earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 53` are therefore forced:
  - `A-C = 20 · 52 = 1040`;
  - `B-B = 6`;
  - `B-C = 4 · 52 = 208`;
  - `B-D = 4 · 208 = 832`.
- Total predicted edge count: `1040 + 6 + 208 + 832 = 2086`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- The frozen-wrapper continuation from `p = 23` is already structurally ruled out here:
  - with `B = {1,19,23,29}`, the spill count is
    `(⌊284/19⌋ - 1) + (⌊284/23⌋ - 1) + (⌊284/29⌋ - 1) = 13 + 11 + 8 = 32`,
    which is far larger than the fixed `20` slots of `A`.
- Brief self-check:
  - the graph-theoretic part has no new phenomenon at `p = 53`;
  - the live difficulty is purely arithmetic and specifically concerns barrier choice plus prime-pool size.

## approach_B

- Construction / extremal route via the preserved moved-barrier pattern.
- Since the frozen wrapper `B = {1,19,23,29}` overflows badly, the solve should test the live moved-barrier direction rather than re-run a dead template.
- Reuse the preserved moved barrier suggested by the family record:
  `B = {1,43,47,53}`.
- These labels are pairwise coprime, and their nontrivial multiples inside `{1,...,284}` are exactly:
  - for `43`:
    `86 = 2·43`, `129 = 3·43`, `172 = 4·43`, `215 = 5·43`, `258 = 6·43`;
  - for `47`:
    `94 = 2·47`, `141 = 3·47`, `188 = 4·47`, `235 = 5·47`, `282 = 6·47`;
  - for `53`:
    `106 = 2·53`, `159 = 3·53`, `212 = 4·53`, `265 = 5·53`.
- So the full barrier spill has size `14`, leaving `6` free slots in `A`.
- The crucial factor-palette observation is:
  every barrier multiple above has prime factors drawn only from
  `{2,3,5,43,47,53}`.
  No cofactor larger than `6` occurs because
  `284/43 < 7`, `284/47 < 7`, and `284/53 < 6`.
- Therefore if the six filler labels of `A` are also chosen from the small palette `{2,3,5}`, then every label in `A ∪ B` has prime factors only in
  `{2,3,5,43,47,53}`.
- Take
  `A = {4,8,9,16,25,27,86,94,106,129,141,159,172,188,212,215,235,258,265,282}`.
- Then choose
  `C` to be all primes in `{1,...,284}` except
  `2,3,5,7,11,13,43,47,53`.
  Explicitly:
  `C = {17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283}`.
- This gives `|C| = 52`, exactly the required size.
- Why this arithmetic package should work:
  - every label in `A ∪ B` is composed only of the excluded primes `2,3,5,43,47,53`;
  - every label in `C` is a prime outside that palette;
  - hence every `A-C` and `B-C` edge is automatically coprime;
  - every nontrivial multiple of `43`, `47`, or `53` lies in `A`, so every `B-D` edge is also automatically coprime.
- Brief self-check:
  - the moved barrier consumes only `14` of the `20` `A`-slots;
  - the complementary prime pool has the exact required size `52`;
  - the construction uses the live family mechanism "barrier spill into `A`, prime-block spill into `D`" rather than an ad hoc search pattern.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,52,208`.
2. The exact support interfaces are `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For this instance, it is sufficient to ensure:
  - `B = {1,43,47,53}`;
  - every nontrivial multiple in `{1,...,284}` of `43`, `47`, or `53` lies in `A`;
  - every label in `A` has all prime factors in `{2,3,5,43,47,53}`;
  - `C` consists of `52` primes outside that factor palette.
7. Under those conditions, `A ∪ B` shares no prime factor with `C`, the `B` labels are pairwise coprime, and every label in `D` avoids the barrier primes `43,47,53`.
8. Therefore any classwise labeling by those four label sets is a prime labeling of `Γ(Z_53 × Z_25)`.

## chosen_plan

- Use the stable four-class support reduction from Approach A.
- Treat the frozen wrapper as a ruled-out comparison point, not as a live candidate.
- Commit to the moved barrier `B = {1,43,47,53}` from Approach B.
- Build `A` from the exact barrier spill plus six small palette fillers `4,8,9,16,25,27`.
- Put on `C` the complementary prime pool of size `52`.
- Only after the full class partition is fixed, use one tiny local checker to validate the witness directly against the ring definition.
- Brief self-check:
  - the plan is still reasoning-first because the checker is not discovering the witness;
  - the witness is already forced by spill count, factor palette, and prime-pool count before code is used.

## self_checks

- Statement lock:
  - the target remains the exact feeder instance `Γ(Z_53 × Z_25)`;
  - the label interval length `284` matches the vertex count.
- Structural reduction:
  - no edge type appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the arithmetic burden is exactly on `A ∪ B` versus `C`, inside `B`, and on `B` versus `D`.
- Extremal comparison:
  - the frozen wrapper has spill `32 > 20`, so a moved barrier is genuinely necessary here;
  - the moved barrier `43,47,53` has spill only `14`, leaving room for `6` filler labels in `A`.
- Explicit witness package:
  - `A`, `B`, and `C` are pairwise disjoint with sizes `20,4,52`;
  - the complement has size `208`, exactly `|D|`;
  - every label in `A ∪ B` factors only over `{2,3,5,43,47,53}`;
  - every label in `C` is a prime outside that factor palette.

## code_used

- Before any code, the full reasoning package, class partition, and intended witness were fixed in this record.
- Minimal code was then justified only for witness verification.
- A tiny local checker `check_witness.py`:
  - enumerate the `284` nonzero zero-divisors of `Z_53 × Z_25`;
  - generate edges directly from the ring multiplication rule;
  - assign the displayed classwise label sets to the support classes;
  - check bijectivity onto `{1,...,284}`;
  - test `gcd = 1` on every actual edge.
- Checker result:
  - `vertex_count = 284`;
  - `class_sizes = {A: 20, B: 4, C: 52, D: 208}`;
  - `edge_count = 2086`;
  - `edge_type_counts = {A-C: 1040, B-B: 6, B-C: 208, B-D: 832}`;
  - `label_bijection_ok = 1`;
  - `edge_coprime_ok = 1`.

## result

- Current best solve-stage candidate:
  - put the labels `1,43,47,53` on `B` in any order;
  - put the labels
    `4,8,9,16,25,27,86,94,106,129,141,159,172,188,212,215,235,258,265,282`
    on `A` in any order;
  - put the labels
    `17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283`
    on `C` in any order;
  - put the remaining `208` labels on `D`.
- Why this should work:
  - `B-B` edges:
    `1,43,47,53` are pairwise coprime;
  - `A-C` and `B-C` edges:
    every label in `A ∪ B` factors only over `{2,3,5,43,47,53}`, while every label in `C` is a prime outside that palette;
  - `B-D` edges:
    every nontrivial multiple of `43`, `47`, and `53` up to `284` was deliberately placed in `A`, so no label in `D` is divisible by any nontrivial barrier prime;
  - there are no other edges by the support decomposition.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support reduction, the moved-barrier idea, the two-spill packaging "barrier spill into `A`, prime-block spill into `D`", and the factor-palette viewpoint that `A ∪ B` only needs a small excluded prime set;
  - what part does not yet scale:
    the exact choice `43,47,53` and the complementary-prime count at `N = 284` are still instance-level arithmetic data, not a quantified existence lemma;
  - what theorem slice is suggested:
    a movable sparse-barrier / complementary prime-pool theorem for `Γ(Z_p × Z_25)` saying that if one can choose three pairwise-coprime barrier primes with spill fitting into the `20` `A`-slots and still leave `p - 1` primes outside the induced factor palette, then the four-interface bridge theorem closes the graph;
  - what one or two next feeder instances would help most:
    `Γ(Z_59 × Z_25)` first, to test whether the same moved barrier still leaves enough complementary primes, and then whichever smallest post-`59` feeder first forces either a new barrier or a true prime-pool obstruction;
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is much closer to a paper-shaped claim because it directly pressures the live existence-layer theorem rather than merely extending the old fixed-wrapper line.
- Brief self-check:
  - the checker confirms the full ring graph has exactly the predicted `2086` edges and no coprimality violation under the displayed witness;
  - the strongest honest solve-stage classification is still `CANDIDATE`, not `EXACT`, because Lean has not been run.

## family_affinity

- Family affinity is high.
- This feeder lands exactly on the current campaign blocker: the existence layer behind the sharpened two-spill `F25` companion theorem.
- The value is not just "another positive instance"; it tests whether the preserved moved-barrier route can still support a full `C` prime block at a much larger parameter than the frozen-wrapper boundary.

## generalization_signal

- Generalization signal is strong.
- The decisive new pattern at `p = 53` is not a half-interval prime count and not the frozen wrapper. It is a factor-palette split:
  - choose a barrier whose full spill forces only a small excluded palette in `A ∪ B`;
  - then fill `C` from the complementary prime pool.
- The honest family-level signal is:
  the paper-facing `F25` companion should likely be phrased as a movable sparse-barrier / complementary prime-pool theorem, not as persistence of any fixed wrapper.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact interfaces `A-C`, `B-B`, `B-C`, `B-D`;
  3. choose `B = {1,q_1,q_2,q_3}` with pairwise-coprime barrier primes;
  4. place every nontrivial in-interval multiple of `q_1,q_2,q_3` into `A`;
  5. choose any extra `A` fillers from the same small excluded factor palette;
  6. choose `C` as `p - 1` primes outside that palette;
  7. assign the complement to `D`.
- Reusable gain from this feeder:
  the complementary-prime-pool viewpoint is now explicit and concrete enough to state as the real arithmetic front end of the family theorem.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, let `N = 5p + 19`. If `{1,...,N}` admits a partition into class label sets `A_lab,B_lab,C_lab,D_lab` with
  - `|A_lab| = 20`,
  - `|B_lab| = 4`,
  - `|C_lab| = p - 1`,
  - `|D_lab| = 4(p - 1)`,
  - `B_lab = {1,q_1,q_2,q_3}` with `q_1,q_2,q_3` pairwise coprime primes,
  - every nontrivial multiple in `{1,...,N}` of `q_1,q_2,q_3` placed in `A_lab`,
  - every label in `A_lab` factoring only over a small excluded prime palette containing `q_1,q_2,q_3`,
  - `C_lab` consisting of `p - 1` primes outside that palette,
  then the four-interface bridge theorem yields a prime labeling of `Γ(Z_p × Z_25)`.
- This feeder suggests the theorem statement should emphasize "complementary prime pool outside the `A ∪ B` factor palette" rather than any fixed threshold such as `> 29`.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this live moved-barrier line is `p = 59`.
- Reason:
  the family dossier already names `z59-z25-prime-zero-divisor-graph` as the next discriminator if `z53-z25-prime-zero-divisor-graph` survives, and the real question is whether the same arithmetic package still leaves `58` complementary primes.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder with no bounded rediscovery audit in this pass and no Lean closure on the exact instance.
- It is publication-relevant because it directly sharpens the open arithmetic existence problem for the paper-facing `F25` companion theorem.
- The likely publishable unit is still a family-level theorem or obstruction/result pair, not the single `p = 53` witness by itself.
- If verification confirms this witness, the package is still not `PAPER_READY`, but it is clearly closer to a referee-facing family claim than a random exact-instance success.

## likely_failure_points

- A structural failure would mean an omitted edge type outside `A-C`, `B-B`, `B-C`, `B-D`, which would contradict the now-stable support reduction.
- An arithmetic failure would mean a missed barrier multiple of `43`, `47`, or `53` accidentally left in `D`.
- Another arithmetic failure would mean an `A` filler accidentally carrying a prime that was also placed in `C`.
- Publication-wise, the weak point is unchanged:
  the instance materially pressures the `F25` existence layer, but by itself it is not yet a referee-facing family theorem.

## verify_rediscovery

- PASS 1 ran on 2026-04-11 as a bounded web audit for the exact feeder statement `Γ(Z_53 × Z_25)` / `Gamma(Z_53 x Z_25)`, alternate family notation `Γ(Z_p × Z_{q^2})`, the canonical Fox-Mooney source, in-source theorem/proposition/example/corollary/conjecture checks, and one bounded follow-up status check.
- Exact-instance searches did not surface any published paper or database entry already stating that `Γ(Z_53 × Z_25)` is prime.
- The canonical source
  Fox-Mooney, "On prime labelings of zero-divisor graphs," Congressus Numerantium 236 (2025),
  proves nearby families such as `Γ(Z_p × Z_4)`, `Γ(Z_p × Z_9)`, and `Γ(Z_2 × Z_{p^2})`, but within the bounded in-source audit it does not settle the `q = 5` line.
- The same source explicitly leaves the ambient family `Γ(Z_p × Z_{q^2})` open via Conjecture 4.4, so the exact `Z_53 × Z_25` instance is not directly implied there.
- A bounded recent-status search found discussion of the 2025 paper, but no later primary-source resolution of the `Γ(Z_p × Z_{q^2})` family within budget.
- Rediscovery verdict: not established within the allowed PASS 1 budget.

## verify_faithfulness

- The claimed result matches the intended exact statement: a prime labeling of the full simple zero-divisor graph on the `284` nonzero zero-divisors of `Z_53 × Z_25`.
- The solve artifact works with the actual ring graph and the exact adjacency rule `(a,b) ~ (c,d)` iff `ac = 0 mod 53` and `bd = 0 mod 25`; it does not switch to a proxy graph or a weakened surrogate claim.
- The record keeps the instance-level claim separate from the family-level heuristic. The candidate theorem slice is presented as future leverage, not as something already proved here.
- I did not find quantifier drift, definition drift, or a mismatch between the prose claim and the object checked by the local witness verifier.

## verify_proof

- First incorrect step found: none.
- The structural reduction to the four support classes `A,B,C,D` and the edge interfaces `A-C`, `B-B`, `B-C`, `B-D` is coherent and matches the ring multiplication rules for `Z_53 × Z_25`.
- The key arithmetic obligations are also coherent:
  - `B = {1,43,47,53}` is pairwise coprime;
  - every label in `A ∪ B` factors only over `{2,3,5,43,47,53}`;
  - every label in `C` is a prime outside that palette;
  - every nontrivial multiple up to `284` of `43`, `47`, and `53` is placed in `A`, so no `D`-label is divisible by a nontrivial barrier prime.
- That is enough to justify every actual edge type:
  - `A-C` and `B-C` by palette separation;
  - `B-B` by pairwise coprimality inside `B`;
  - `B-D` by exclusion of barrier multiples from `D`.
- The proof is still an informal mathematical argument plus exhaustive computation, not a formal proof object. That limits the harness classification, but I did not find a mathematical break in the stated reasoning.

## verify_adversarial

- I reran `artifacts/z53-z25-prime-zero-divisor-graph/check_witness.py`. It reported:
  - `vertex_count = 284`
  - `class_sizes = {'A': 20, 'B': 4, 'C': 52, 'D': 208}`
  - `edge_count = 2086`
  - `edge_type_counts = {'A-C': 1040, 'B-B': 6, 'B-C': 208, 'B-D': 832}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`
- I also ran independent one-off arithmetic checks outside the checker logic to verify:
  - `A`, `B`, and `C` are disjoint and leave exactly `208` labels for `D`;
  - every `A` label has prime factors only in `{2,3,5,43,47,53}`;
  - no `C` label shares a prime factor with that palette;
  - no label left in `D` is divisible by `43`, `47`, or `53`;
  - the barrier spill union has the claimed size `14`.
- I did not find an adversarial break of the witness or a hidden computational mismatch.

## verify_theorem_worthiness

- This feeder does suggest a real theorem slice, not merely an isolated exact curiosity. At `p = 53`, the old frozen-wrapper package is genuinely dead by spill count, yet the moved sparse-barrier / complementary prime-pool mechanism still closes the exact instance.
- What clearly scales:
  - the support decomposition into `A,B,C,D`;
  - the exact interface reduction `A-C`, `B-B`, `B-C`, `B-D`;
  - the general bridge principle that any classwise partition with the right coprimality obligations yields a prime labeling;
  - the factor-palette viewpoint for `A ∪ B` versus the complementary prime pool for `C`.
- What does not yet scale automatically:
  - the exact barrier choice `43,47,53`;
  - the exact prime-count bookkeeping at `N = 284`;
  - any quantified lemma ensuring such a barrier/prime-pool partition for a general odd prime `p`.
- Best honest publication status is not merely `INSTANCE_ONLY`. This verified feeder directly strengthens the active `F25` campaign line and points to a concrete theorem slice, so the honest status is `SLICE_CANDIDATE`.
- The smallest next feeder that most tests the current template is `Γ(Z_59 × Z_25)`, since it is the next campaign-designated pressure point for the same moved-barrier arithmetic package.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- PASS 1 did not establish rediscovery, PASS 2 did not show statement drift, and PASS 3 through PASS 4 did not expose a mathematical or computational failure in the displayed witness.
- Because Lean has not been completed, the harness classification must remain `CANDIDATE`, not `EXACT`.
- `lean_ready = true`, but the campaign's next honest action is still `generalize` before any instance-level Lean work.

## minimal_repair_if_any

- None. No conservative mathematical patch was needed.
  the existence of good moved barriers and large enough complementary prime pools is still not quantified in theorem form.

## what_verify_should_check

- Recompute the `284` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `2086` edges.
- Check that the displayed `A`, `B`, and `C` sets are pairwise disjoint and cover `76` labels, so the complement has size `208`.
- Check coprimality on every actual edge from the ring graph.
- Check explicitly that the barrier spill of `43`, `47`, and `53` is exactly the `14` labels listed in `A`.
- In verify, audit whether any existing family theorem already implies this moved-barrier / complementary-prime-pool instance before treating it as frontier evidence.
