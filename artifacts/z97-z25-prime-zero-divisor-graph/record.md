# Solve Record: z97-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_97 × Z_25) prime?`
- Active slug: `z97-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_97 × Z_25)` admits a prime labeling, meaning a bijection from its `504` vertices to `{1,2,...,504}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_97 × Z_25`, while extracting only reusable structure that is directly justified by the same argument.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_97` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_97^×}`, size `96`.
  - `D = {(a,5t) : a ∈ Z_97^×, t ∈ {1,2,3,4}}`, size `384`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 97` and `bd = 0 mod 25`.
- Because `Z_97` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions and ambiguities locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - prime labeling means a bijection onto `{1,...,504}`;
  - once a classwise label set is chosen, labels may be permuted within each support class because vertices in the same support class have the same neighborhood;
  - no blocking definition gap remains after importing the campaign's four-class notation.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 97` are therefore forced:
  - `A-C = 20 · 96 = 1920`;
  - `B-B = 6`;
  - `B-C = 4 · 96 = 384`;
  - `B-D = 4 · 384 = 1536`.
- Total predicted edge count: `1920 + 6 + 384 + 1536 = 3846`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.

## approach_B

- Construction / extremal route in the live complementary-support wrapper language.
- The late-regime `F25` theorem slice already suggests abandoning the old prime-only / bounded-spill `C` bookkeeping here:
  - at `p = 97`, `|C| = 96`, so a construction that tries to micromanage exceptional multiples of many large primes is no longer the clean regime;
  - the fixed `A0` plus high-barrier / complementary-support wrapper is now the right structural fit.
- Use the fixed `A` reservoir from the wrapper theorem:
  - `A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
- Choose a high barrier set
  - `B = {1,293,307,311}`.
- Why these barrier labels are well chosen:
  - `293,307,311` are distinct primes;
  - each lies above half the active interval because `504 < 2·293`;
  - therefore each barrier prime has zero spill in `{1,...,504}`: its only multiple in the interval is itself.
- Define the `C` label reservoir by a fixed complementary-support window:
  - `C0 = {n : 2 ≤ n ≤ 291 and gcd(n,6) = 1}`.
- Count of this reservoir:
  - among `1,...,291`, the numbers not divisible by `2` or `3` are
    `291 - ⌊291/2⌋ - ⌊291/3⌋ + ⌊291/6⌋ = 291 - 145 - 97 + 48 = 97`;
  - removing `1` leaves `|C0| = 96`.
- So for the exact instance `p = 97`, take `C = C0`.
- Every `c ∈ C` is automatically coprime to every `a ∈ A0` because all prime divisors of `c` avoid `2` and `3`.
- Every `c ∈ C` is automatically coprime to every barrier prime in `B` because each `c ≤ 291 < 293`, so no `c` is divisible by `293`, `307`, or `311`.
- Let `D` be the residual complement
  - `D = {1,...,504} \ (A0 ∪ B ∪ C)`.
- Then
  - `|D| = 504 - 20 - 4 - 96 = 384`,
  exactly the required size for the support class `D`.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,96,384`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A` uses only prime support from `{2,3}` and every label on `C` avoids `2` and `3`, then all `A-C` edges are valid.
4. If `B = {1,b1,b2,b3}` with distinct primes `bi > 504/2`, then all distinct labels in `B` are pairwise coprime and every label in `D` is coprime to every label in `B`.
5. If every label in `C` also avoids the barrier primes `b1,b2,b3`, then all `B-C` edges are valid.
6. Therefore any partition of `{1,...,504}` into class label sets satisfying those support-avoidance conditions gives a prime labeling of `Γ(Z_97 × Z_25)`.
7. The chosen data
   `A = A0`, `B = {1,293,307,311}`, `C = {2 ≤ n ≤ 291 : gcd(n,6)=1}`, `D = {1,...,504} \ (A ∪ B ∪ C)`
   satisfy exactly those conditions.

## chosen_plan

- Use the exact four-class support reduction from Approach A.
- Solve the arithmetic only in the late complementary-support language from Approach B, not by reviving the older spill-prime bookkeeping.
- Keep `A` fixed at `A0`, choose three barrier primes above both `291` and `504/2`, and take `C` from a low complementary-support window where avoidance of `{2,3}` is transparent.
- Avoid code unless a hidden counting or divisibility ambiguity appears after the full class partition is written down.

## self_checks

- After statement lock:
  - the target is still the exact feeder instance `Γ(Z_97 × Z_25)`;
  - the vertex count `20 + 4 + 96 + 384 = 504` matches the active label interval.
- After Approach A:
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`;
  - no new graph-theoretic obstruction appears at `p = 97`.
- After Approach B:
  - `293,307,311` are all larger than `252`, so the barrier really is zero-spill on `{1,...,504}`;
  - the `C` window `2..291` lies strictly below the smallest barrier prime, so `B-C` coprimality is automatic once `gcd(c,6)=1`;
  - the count `|C| = 96` matches `|Z_97^×|`.
- After choosing the plan:
  - the argument is still reasoning-first because the witness is defined by simple arithmetic sets, not by search;
  - no code is needed because the partition sizes and coprimality interfaces all admit direct hand checks.

## code_used

- No code used.
- Reason:
  the class partition is explicit, the key counts are closed-form inclusion-exclusion counts, and the coprimality obligations reduce to immediate support-avoidance facts.

## result

- Current best solve-stage candidate:
  - put the fixed reservoir
    `A = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`
    on the support class `A`;
  - put `B = {1,293,307,311}` on the support class `B`;
  - put
    `C = {n : 2 ≤ n ≤ 291 and gcd(n,6) = 1}`
    on the support class `C`;
  - put the residual complement
    `D = {1,...,504} \ (A ∪ B ∪ C)`
    on the support class `D`.
- Why this works:
  - `B-B` edges:
    `1,293,307,311` are pairwise coprime because the non-unit labels are distinct primes.
  - `A-C` edges:
    every label in `A` has prime support contained in `{2,3}`, while every label in `C` avoids `2` and `3`.
  - `B-C` edges:
    every `c ∈ C` satisfies `c < 293`, so it cannot be divisible by `293`, `307`, or `311`; coprimality with `1` is automatic.
  - `B-D` edges:
    each barrier prime is greater than `504/2`, so any multiple of `293`, `307`, or `311` in `{1,...,504}` is just itself; since `D` excludes `B`, every `d ∈ D` is automatically coprime to every label in `B`.
  - there are no other edge types.
- Therefore the intended statement appears true for this exact feeder instance.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support reduction, the fixed `A0` reservoir, the zero-spill high-barrier `B` mechanism, and the complementary-support criterion for `C`.
  - what part does not yet scale automatically:
    the exact size of a low complementary-support window large enough to supply `p - 1` labels still needs a preserved counting corollary; the present window closes `p = 97` but does not by itself settle arbitrarily larger `p`.
  - what theorem slice is suggested:
    a finite-range complementary-support slice in the exact wrapper language, using a fixed `A0`, a fixed high barrier `B`, and a counted low window for `C`.
  - what one or two next feeder instances would help most:
    `Γ(Z_101 × Z_25)` is the immediate next stress test because the present `C` window is exactly saturated at `96` labels; if more feeder evidence is needed beyond that, `Γ(Z_103 × Z_25)` would distinguish “slightly wider window” from “new regime change”.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still solve-stage instance evidence, but it is substantially closer to a paper-shaped claim because the same argument exposes a clean finite-range theorem slice rather than a one-off ad hoc witness.

## family_affinity

- Family affinity is very high.
- This instance lies exactly on the live `Γ(Z_p × Z_25)` complementary-support wrapper line named by the campaign status.
- Unlike the early small-spill feeders, this solve directly tests the current publication-facing theorem language rather than an older repair heuristic.

## generalization_signal

- Generalization signal is strong.
- The exact `z97` construction does not depend on delicate exceptional multiples of individual `C` primes; it uses a clean support-avoidance reservoir
  `C0 = {2 ≤ n ≤ 291 : gcd(n,6)=1}`
  of size `96`.
- That immediately suggests a finite-range corollary:
  for odd primes `59 ≤ p ≤ 97`, the same fixed data
  `A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`
  and
  `B = {1,293,307,311}`
  still fit inside `{1,...,5p+19}`, still satisfy the high-barrier hypothesis, and leave a `C` reservoir of size at least `p - 1` by taking any `(p - 1)`-subset of `C0`.
- The honest new boundary signal is that this specific `C0` window is exactly saturated at `p = 97`.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. use the ring bridge to reduce the graph to the interfaces `A-C`, `B-B`, `B-C`, `B-D`;
  3. freeze `A` at the fixed `{2,3}`-smooth reservoir `A0`;
  4. choose `B = {1,b1,b2,b3}` with distinct barrier primes above half the active interval;
  5. choose `C` from a complementary-support set whose prime divisors avoid `2,3,b1,b2,b3`;
  6. let `D` be the residual complement.
- Relative to the earlier `p = 13,17,19` records, the reusable gain is conceptual:
  the late regime can be handled by support-avoidance alone, without tracking spill multiples of individual `C` primes.

## candidate_theorem_slice

- Candidate slice:
  for every odd prime `p` with `59 ≤ p ≤ 97`, let `N = 5p + 19`, set
  - `A = A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`,
  - `B = {1,293,307,311}`,
  - `C0 = {n : 2 ≤ n ≤ 291 and gcd(n,6) = 1}`,
  - choose any subset `C ⊆ C0` of size `p - 1`,
  - let `D = {1,...,N} \ (A ∪ B ∪ C)`.
  Then the exact ring bridge plus the checked complementary-support wrapper show that `Γ(Z_p × Z_25)` is prime.
- This is not claimed closed yet here because solve did not formalize or audit the whole range, but the argument visible in this instance is already range-uniform.

## smallest_param_shift_to_test

- The smallest next parameter shift to test is `p = 101`.
- Reason:
  the current low complementary-support window `C0 = {2 ≤ n ≤ 291 : gcd(n,6)=1}` has exactly `96` labels, so it closes `p = 97` exactly and no further.
  Even the rounder window `{2 ≤ n ≤ 300 : gcd(n,6)=1}` has only `99` labels, so `p = 101` is the first place where a genuinely new `C`-supply move is required.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage feeder with no verify pass and no Lean closure on the exact instance or the extracted finite range.
- It is publication-relevant because it lands directly in the live wrapper language and suggests a nontrivial finite-range slice rather than only one more isolated witness.
- The likely publishable unit is not the lone `p = 97` instance but the finite-range complementary-support corollary it points to, on top of the already checked structural wrapper.

## likely_failure_points

- A structural failure point would be a missed support-class edge type, though that would contradict the now-stable `F25` ring bridge.
- An arithmetic failure point would be an incorrect count for `|C0|`; that count should be rechecked explicitly in verify.
- Another arithmetic failure point would be forgetting that `B` must lie inside the active label interval for the extracted finite-range slice; that is why the natural lower endpoint is `p = 59`, not smaller.
- Publication-wise, the main risk is overclaiming the finite-range slice before the range-uniform argument is audited carefully and, if desired, mirrored into Lean.

## what_verify_should_check

- Recompute the `504` vertices directly from the ring definition and confirm the support-class sizes `20,4,96,384`.
- Recompute the exact edge set and confirm that only `A-C`, `B-B`, `B-C`, and `B-D` occur, with total `3846` edges.
- Check that
  `A0`,
  `B = {1,293,307,311}`,
  `C = {2 ≤ n ≤ 291 : gcd(n,6)=1}`,
  and
  `D = {1,...,504} \ (A ∪ B ∪ C)`
  are pairwise disjoint and cover exactly `{1,...,504}`.
- Recheck the inclusion-exclusion count `|C| = 96`.
- Recheck that `293,307,311` are prime and all exceed `252`.
- If verify wants a bounded adversarial check, a tiny checker is justified only as witness verification, not as discovery.
- If the exact instance verifies, the next family task should be to package the finite-range `59 ≤ p ≤ 97` corollary before reopening feeder search.

## verify_rediscovery

- PASS 1 used a bounded web audit centered on the exact instance notation, ASCII variants, the broader `Γ(Z_p × Z_(q^2))` family notation, the canonical Fox-Mooney source, and theorem/proposition/example/observation/corollary checks inside that source.
- Exact-instance searches on `Γ(Z_97 × Z_25)` and `Gamma(Z_97 x Z_25)` with `prime labeling` and `zero-divisor graph` did not reveal an earlier theorem, proposition, example, or corollary settling this exact case within budget.
- The canonical 2025 paper `On prime labelings of zero-divisor graphs` is directly relevant, but its nearby solved statements concern other families such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))`. Its open-problem discussion still leaves the ambient `Γ(Z_p × Z_(q^2))` line conjectural/open rather than already settled.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The solve record matches the intended statement exactly: existence of a prime labeling for the full simple zero-divisor graph `Γ(Z_97 × Z_25)` on all `504` nonzero zero-divisors, using a bijection to `{1,...,504}`.
- There is no drift to a quotient graph, support graph, partial labeling, or weaker sufficient proxy. The support decomposition is used only to certify the exact graph.
- The extra family discussion is clearly secondary. The actual solved claim remains the exact feeder instance, not a parameterized theorem.

## verify_proof

- I recomputed the zero-divisor partition from the ring law and recovered the claimed support classes:
  - `|A| = 20`,
  - `|B| = 4`,
  - `|C| = 96`,
  - `|D| = 384`,
  totaling `504`.
- I independently recomputed adjacency from coordinatewise zero product and again obtained only the edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `1920`, `6`, `384`, and `1536`, total `3846`.
- Given that edge pattern, the proof correctly reduces to three arithmetic obligations:
  - every label on `A` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime and every label on `C` is coprime to them;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the displayed witness:
  - `A0` consists entirely of `{2,3}`-smooth labels;
  - `C = {2 ≤ n ≤ 291 : gcd(n,6) = 1}` has size exactly `96`, so every `c ∈ C` avoids `2` and `3`;
  - `B = {1,293,307,311}` is pairwise coprime because the non-unit labels are distinct primes;
  - each of `293,307,311` exceeds `504/2`, so its only multiple in `{1,...,504}` is itself, and `D` excludes those three labels.
- First incorrect step found: none.

## verify_adversarial

- No artifact checker existed, so I ran an independent bounded witness check directly from the ring definition.
- The recomputation confirmed:
  - the four label classes are pairwise disjoint and cover exactly `{1,...,504}`;
  - `293`, `307`, and `311` are prime;
  - the only edge classes in the actual graph are `A-C`, `B-B`, `B-C`, and `B-D`;
  - there are zero gcd violations across all required interfaces.
- I also stress-checked the two places most likely to hide a mistake:
  - the `C` count is exactly `96`, not merely at least `96`;
  - the barrier argument is genuinely zero-spill on `{1,...,504}`, since the only interval multiples of `293`, `307`, and `311` are the numbers themselves.
- I did not find a counterexample edge, a mislabeled reservoir count, or a hidden divisibility obstruction.

## verify_theorem_worthiness

- This feeder does suggest a real theorem slice, not only an isolated instance. The same fixed data `A0`, `B = {1,293,307,311}`, and `C0 = {2 ≤ n ≤ 291 : gcd(n,6)=1}` already give a uniform finite-range template through the checked endpoint `p = 97`.
- What scales structurally:
  - the four-class support decomposition;
  - the reduction to the interfaces `A-C`, `B-B`, `B-C`, `B-D`;
  - the fixed high-barrier `B` mechanism;
  - the fixed complementary-support reservoir `C0`.
- What does not yet scale automatically:
  - any extension beyond `p = 97`, because this `C0` reservoir has exactly `96` labels and is exhausted at the present endpoint;
  - a quantified family lemma proving the full finite range rather than just this instance-level feeder.
- The best honest publication status is therefore `SLICE_CANDIDATE`, not `INSTANCE_ONLY`: this verified feeder materially sharpens the live campaign's finite-range wrapper claim. It is not `PAPER_READY`, because neither the finite range nor the ring-to-support family package is formalized yet.
- The smallest parameter shift that most tests the claimed template is `Γ(Z_101 × Z_25)`, since `p = 101` is the first odd prime for which the present `C0` reservoir is too small.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- No rediscovery was established in the bounded prior-art pass, the solve claim matches the intended exact statement, and the explicit witness survived skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.
- `lean_ready = true`

## minimal_repair_if_any

- None. No conservative repair to the proof or witness was needed.
