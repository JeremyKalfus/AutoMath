# Solve Record: z67-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_67 × Z_25) prime?`
- Active slug: `z67-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_67 × Z_25)` admits a prime labeling, meaning a bijection from its `354` vertices to `{1,2,...,354}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_67 × Z_25`, not to a quantified family statement.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_67` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the usual four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_67^×}`, size `66`.
  - `D = {(a,5t) : a ∈ Z_67^×, t ∈ {1,2,3,4}}`, size `264`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 67` and `bd = 0 mod 25`.
- Because `Z_67` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - once a classwise label set is fixed, labels may be permuted inside `A`, `C`, and `D` because those classes have uniform neighborhoods;
  - the four `B` vertices form a `K_4`, so any permutation of a pairwise-coprime `B` label set also preserves the witness.
- Ambiguities or missing definitions:
  - none that block the solve; the campaign notation already fixes the graph convention and support classes.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 67` are therefore forced:
  - `A-C = 20 · 66 = 1320`;
  - `B-B = 6`;
  - `B-C = 4 · 66 = 264`;
  - `B-D = 4 · 264 = 1056`.
- Total predicted edge count: `1320 + 6 + 264 + 1056 = 2646`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.

## approach_B

- Construction / extremal route using the late zero-spill regime rather than the old frozen-wrapper spill bookkeeping.
- Let `N = 5p + 19 = 354`, so `N / 2 = 177`.
- Put `A` on a fixed `2,3`-smooth palette:
  `A = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
- This gives `20` distinct labels, and every prime factor appearing on `A` is in the tiny palette `{2,3}`.
- Choose a zero-spill barrier on `B`:
  `B = {1,337,347,349}`.
- The three nontrivial barrier labels are distinct primes and satisfy `337,347,349 > 177`, so each has no nontrivial multiple inside `{1,...,354}`.
- Therefore the full `B-D` interface becomes automatic: the only multiples of `337`, `347`, and `349` in the interval are the labels themselves, and those labels are used on `B`, not on `D`.
- For `C`, take the complementary prime pool:
  all primes in `{1,...,354}` greater than `3`, excluding the three barrier primes `337,347,349`.
- Prime count check:
  - there are `71` primes in `{1,...,354}`;
  - therefore there are `69` primes greater than `3`;
  - removing the three barrier primes leaves exactly `66 = p - 1` primes for `C`.
- This makes `A-C` and `B-C` automatic:
  - every label on `A` has prime factors only in `{2,3}`;
  - every label on `C` is a prime greater than `3`;
  - every nontrivial label on `B` is one of the excluded barrier primes.
- The remaining labels may therefore go to `D` with no further arithmetic design.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,66,264`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For this instance, it is sufficient to choose:
   - `A` supported only on the prime palette `{2,3}`;
   - `B = {1,b1,b2,b3}` with distinct primes `bi > 177`;
   - `C` as the remaining primes greater than `3`;
   - `D` as the residual complement.
7. Under those choices, `A-C`, `B-C`, and `B-D` are automatic, so the classwise template closes.

## chosen_plan

- Use the zero-spill high-barrier route, not the older frozen-wrapper or moved-barrier templates.
- Fix `A` as a concrete `2,3`-smooth reservoir of size `20`.
- Fix `B = {1,337,347,349}` so the barrier side is completely zero-spill.
- Let `C` be exactly the remaining primes greater than `3`.
- Use one tiny checker only after the full class partition is fixed.

## self_checks

- After statement lock:
  - the target remains the exact feeder instance `Γ(Z_67 × Z_25)`;
  - the label interval length `354` matches the vertex count `20 + 4 + 66 + 264`.
- After Approach A:
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`;
  - no new graph-theoretic obstruction appears at `p = 67`.
- After Approach B:
  - there are at least `20` nontrivial `2,3`-smooth labels available below `354`;
  - there are many primes above `177`, so the high barrier is easy to choose;
  - the complementary prime pool is count-tight but sufficient: `69 - 3 = 66`.
- After choosing the plan:
  - this remains reasoning-first because the witness is dictated by support reduction and explicit counting, not by search;
  - code is used only as post-construction witness verification.
- After the checker:
  - the full ring graph has `354` vertices and `2646` edges with the predicted edge-type counts;
  - the displayed class partition is a bijection onto `{1,...,354}` and produces no gcd violation on any edge.

## code_used

- Minimal code was used only after the reasoning and explicit class partition were fixed.
- The tiny checker at `artifacts/z67-z25-prime-zero-divisor-graph/check_witness.py` enumerates the `354` nonzero zero-divisors of `Z_67 × Z_25`, generates edges directly from the ring multiplication rule, computes the classwise edge counts, checks bijectivity onto `{1,...,354}`, and tests coprimality on every edge.
- Result after running the checker:
  - `vertex_count = 354`
  - `edge_count = 2646`
  - `edge_type_counts = {A-C: 1320, B-B: 6, B-C: 264, B-D: 1056}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108` on `A` in any order;
  - put the labels `1,337,347,349` on `B` in any order;
  - put the labels `5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,353` on `C` in any order;
  - put the remaining `264` labels on `D` in any order.
- Why this works:
  - `B-B` edges: `1,337,347,349` are pairwise coprime.
  - `A-C` edges: every `A` label has all prime factors in `{2,3}`, while every `C` label is a prime greater than `3`.
  - `B-C` edges: every nontrivial `B` label is a barrier prime excluded from `C`.
  - `B-D` edges: each nontrivial barrier prime is greater than `354 / 2`, so it has no nontrivial multiple inside the label interval other than itself, and those labels are not in `D`.
  - there are no other edge types by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition;
    the zero-spill observation for barrier primes above half the interval;
    the idea of placing `A` on a tiny fixed factor palette and taking `C` from the complementary prime pool;
    the residual-complement treatment of `D`.
  - what part does not yet scale:
    this pass does not prove that every later odd prime admits three suitable barrier primes above `N/2` together with a complementary prime pool of size `p - 1`;
    the exact prime counts used here are still instance arithmetic.
  - what theorem slice is suggested:
    a late-range zero-spill `F25` slice:
    if `N = 5p + 19` admits a `20`-label `A` reservoir supported on `{2,3}`, three distinct barrier primes in `(N/2, N]`, and at least `p - 1` additional primes greater than `3` outside that barrier, then `Γ(Z_p × Z_25)` is prime.
  - what one or two next feeder instances would help most:
    `Γ(Z_71 × Z_25)` and `Γ(Z_73 × Z_25)`, because they are the nearest stress tests of the same zero-spill / complementary-prime-pool package.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still instance-level evidence, but it is much closer to a paper-shaped claim than the earlier small-spill feeders because the witness is governed by a clean late-regime theorem template rather than ad hoc spill placement.

## family_affinity

- Family affinity is very high.
- This feeder sits exactly on the campaign's live blocker: the zero-spill high-barrier / complementary-prime-pool route for `Γ(Z_p × Z_25)`.
- The main value is not only that `p = 67` appears to survive, but that it survives with the cleanest arithmetic package seen so far in the local records.

## generalization_signal

- Generalization signal is strong.
- At `p = 67`, the solve does not need frozen-wrapper spill bookkeeping and does not need moved-barrier spill bookkeeping either.
- The barrier side disappears completely once `B = {1,337,347,349}` is chosen, and the only remaining arithmetic question is prime-pool supply.
- The count is tight in a useful way:
  there are exactly `69 = (p - 1) + 3` primes greater than `3` in `{1,...,354}`, so after using three of them on the barrier, the remaining complementary prime pool has exactly the right size `66`.
- That makes this feeder a clean discriminator for the late zero-spill theorem slice, not just another positive instance.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. choose `A` as `20` labels whose prime factors lie in a tiny palette, here `{2,3}`;
  4. choose `B = {1,b1,b2,b3}` with distinct primes `bi > (5p + 19) / 2`;
  5. choose `C` from primes outside the `A` factor palette and outside `B`;
  6. put the remaining labels on `D`;
  7. close the exact graph by the classwise coprimality obligations alone.
- Relative to the earlier `F25` feeders, the reusable gain is that the proof surface now has no spill management on either `C` or `B`; the whole burden is pushed into explicit prime counting.

## candidate_theorem_slice

- Candidate theorem slice:
  let `N = 5p + 19` for an odd prime `p`.
  If
  - there are `20` distinct labels in `{2,...,N}` whose prime factors lie in `{2,3}`,
  - there exist three distinct primes `b1,b2,b3` with `N / 2 < bi ≤ N`,
  - and there are at least `p - 1` further primes greater than `3` in `{1,...,N}` outside `{b1,b2,b3}`,
  then taking
  - `A` as any `20` such `2,3`-smooth labels,
  - `B = {1,b1,b2,b3}`,
  - `C` as any `p - 1` of the remaining primes greater than `3`,
  - `D` as the complement,
  yields a prime labeling of `Γ(Z_p × Z_25)`.
- The present feeder is a clean instance of that slice, with equality in the complementary-prime-pool count.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this late zero-spill line is `p = 71`.
- Reason:
  it is the next odd prime after `67` and keeps the same proof template, so it is the nearest discriminator for whether the clean `{2,3}`-palette / zero-spill barrier route is genuinely stable.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage feeder with no verify-stage rediscovery audit in this pass and no Lean closure.
- It is publication-relevant because it exhibits a clean late-regime theorem shape:
  `A` on a fixed tiny factor palette,
  `B` as a zero-spill high barrier,
  `C` as a complementary prime pool,
  `D` as the residual sink.
- That is substantially closer to a paper-facing arithmetic corollary than the earlier repaired small-spill witnesses, but the publishable unit is still the theorem slice, not this single instance.

## likely_failure_points

- The structural failure point would be a missed edge type in the support decomposition, though that would contradict the now-stable `Γ(Z_p × Z_25)` bridge.
- The arithmetic failure point would be a mistaken prime count in `{1,...,354}`, since the `C` pool is used at exact size here.
- Another arithmetic failure point would be accidentally including a label with a prime factor greater than `3` in `A`, which would break the palette-separation argument.
- Publication-wise, the main weakness is unchanged:
  this pass does not prove the general existence theorem behind the zero-spill slice.

## what_verify_should_check

- Recompute the `354` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `2646` edges.
- Check that the displayed `A`, `B`, and `C` label sets are disjoint and have sizes `20,4,66`.
- Check that `C` is exactly the set of primes greater than `3` in `{1,...,354}` excluding `337,347,349`.
- Check that `337,347,349 > 354 / 2`, so `B-D` is genuinely zero-spill.
- Rerun `artifacts/z67-z25-prime-zero-divisor-graph/check_witness.py` and confirm bijectivity plus coprimality on every actual edge.
- In the bounded rediscovery pass later, audit not only the exact instance but also whether any existing sufficient-condition theorem already implies this late zero-spill slice.

## verify_rediscovery

PASS 1 used a bounded live web audit and then stopped browsing.

Search patterns covered:

- the exact instance notation `Gamma(Z_67 x Z_25)` and `Γ(Z_67 × Z_25)` with `prime labeling`
- reordered / alternate notation such as `Gamma(Z_25 x Z_67)` and the family form `Gamma(Z_p x Z_(5^2))`
- the canonical source by title: Fox-Mooney, `On prime labelings of zero-divisor graphs`
- same-source checks aimed at whether a theorem / proposition / example / observation / corollary there already settles the `q = 5^2` line or this exact `p = 67` instance
- one bounded recent-status sweep for later follow-up or citation-based closure

What the bounded pass found:

- the canonical Fox-Mooney paper is still the controlling source for this family within the search budget
- nearby solved families appear there, but the broader `Γ(Z_p × Z_(q^2))` line is still presented as open rather than closed
- no exact-instance hit for `Γ(Z_67 × Z_25)` was found
- no same-source theorem, proposition, example, observation, or corollary was found that already states or directly implies this exact `p = 67, q = 5` case
- no later public source within the bounded pass clearly exhibited this exact labeling or otherwise settled the instance

Rediscovery conclusion:

- rediscovery was not established within the bounded pass
- this artifact should not be reclassified as `REDISCOVERY`

## verify_faithfulness

The solve record is faithful to the intended exact graph statement.

- The local target is the exact feeder instance `Γ(Z_67 × Z_25)`, not a quantified family theorem.
- The solve record proves existence of a prime labeling for that exact graph by an explicit classwise bijection onto `{1,...,354}`.
- The vertex set, support classes `A,B,C,D`, and edge families `A-C`, `B-B`, `B-C`, `B-D` match the standard coordinatewise zero-product definition stated in the record.
- The argument does not drift to a weaker proxy such as only counting primes, only proving a sufficient family condition, or only checking a support abstraction without the actual ring graph.

No wrong-statement drift, quantifier drift, or definition mismatch was found.

## verify_proof

First incorrect step found: none.

Skeptical proof audit:

- The support decomposition is correct: nonzero zero-divisors are exactly the classes `A,B,C,D` with sizes `20,4,66,264`, totaling `354`.
- The edge pattern is correct: because `67` is prime, first-coordinate products vanish only when one first coordinate is `0`; in `Z_25`, nonzero products vanish only between multiples of `5`. That leaves exactly `A-C`, `B-B`, `B-C`, and `B-D`.
- The `A` palette is genuinely `{2,3}`-smooth, so every `A` label is coprime to every prime in `C`.
- The `B` labels `1,337,347,349` are pairwise coprime, so the `K_4` on `B` is valid.
- The `C` pool is exactly count-tight but sufficient: there are `69` primes greater than `3` up to `354`, and deleting the three barrier primes leaves exactly `66 = p - 1`.
- The barrier argument is sound: each nontrivial `B` prime is greater than `354/2`, so its only multiple in `{1,...,354}` is itself; since those three labels stay on `B`, every `B-D` gcd is `1`.

The proof is still instance-level arithmetic rather than a family theorem, but no hidden assumption or invalid inference was found in the exact-instance argument.

## verify_adversarial

PASS 4 reran the local checker and tried to break the explicit witness.

Checker rerun:

- `python3 artifacts/z67-z25-prime-zero-divisor-graph/check_witness.py`
- output:
  - `vertex_count = 354`
  - `edge_count = 2646`
  - `edge_type_counts = {A-C: 1320, B-B: 6, B-C: 264, B-D: 1056}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

Independent arithmetic checks:

- recomputed that there are exactly `69` primes greater than `3` in `{1,...,354}`
- confirmed that removing `337,347,349` leaves exactly `66` labels for `C`
- confirmed that `337,347,349 > 177 = 354/2`
- confirmed that the displayed `A`, `B`, and `C` sets are disjoint and leave exactly `264` residual labels for `D`

Adversarial conclusion:

- the natural failure mode was a hidden multiple of a barrier prime landing in `D`, but that attack fails because all three nontrivial barrier primes lie above the half-interval cutoff
- no counterexample to the displayed witness was found

## verify_theorem_worthiness

This feeder does suggest a real theorem slice, but the verified claim itself is still only an exact instance.

- What scales:
  the four-class support decomposition, the separation of obligations into `A-C`, `B-B`, `B-C`, `B-D`, the zero-spill barrier observation for primes above `N/2`, and the complementary-prime-pool formulation for `C`.
- What does not yet scale:
  the proof that the required prime counts and barrier choices always exist for later `p`; here that part is still exact-instance arithmetic at `N = 354`.
- Best honest publication reading:
  stronger than `INSTANCE_ONLY` because it materially sharpens the live `F25` campaign template, but still not a theorem slice on its own.
- Best honest publication status now:
  `SLICE_CANDIDATE`.
- Smallest next stress test:
  `Γ(Z_71 × Z_25)`, since it is the next odd prime and directly tests whether the same zero-spill complementary-prime-pool package survives beyond this count-tight feeder.

## verify_verdict

`VERIFIED`

- The bounded rediscovery pass did not establish prior-art closure of the exact instance.
- The solve record is faithful to the intended statement.
- No incorrect proof step was found.
- The explicit witness survives direct recomputation on the actual graph.
- Classification should remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

No repair was needed.
