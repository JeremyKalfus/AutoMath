# Solve Record: z89-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_89 × Z_25) prime?`
- Active slug: `z89-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_89 × Z_25)` admits a prime labeling, meaning a bijection from its `464` vertices to `{1,2,...,464}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_89 × Z_25`, not to a full all-`p` family theorem.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_89` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the usual four support classes for `Γ(Z_p × Z_25)`:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_89^×}`, size `88`.
  - `D = {(a,5t) : a ∈ Z_89^×, t ∈ {1,2,3,4}}`, size `352`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 89` and `bd = 0 mod 25`.
- Because `Z_89` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Ambiguities and conventions locked here:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - once classwise label sets are fixed, labels may be permuted within each support class because vertices in the same class have identical neighborhoods.

## approach_A

- Structural / invariant approach through the support graph.
- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 89` are therefore forced:
  - `A-C = 20 · 88 = 1760`;
  - `B-B = 6`;
  - `B-C = 4 · 88 = 352`;
  - `B-D = 4 · 352 = 1408`.
- Total predicted edge count: `1760 + 6 + 352 + 1408 = 3526`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.

## approach_B

- Construction / extremal approach using a high barrier with complementary support, rather than the older low-`p` spill bookkeeping.
- The old barrier pattern `B = {1,19,23,29}` is no longer viable here:
  - with `N = 464`, the nontrivial multiples of `19`, `23`, and `29` below `N` already far exceed the fixed `20` slots of `A`.
- So the correct large-`p` move is to make `B` spill-free:
  - choose `B = {1,449,457,461}`;
  - the three nontrivial barrier labels satisfy `449,457,461 > N/2 = 232`, so none has a nontrivial multiple in `{1,...,464}`;
  - they are pairwise coprime, so `B` is a valid `K_4` label set.
- Fix `A` inside a tiny prime-support reservoir:
  - let
    `A = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`;
  - every label in this set is `2,3`-smooth, so every prime divisor of an `A` label is in `{2,3}`.
- Now define the candidate `C` pool by the complementary coprimality condition:
  - let
    `S = {n ∈ {1,...,464} : gcd(n,6) = 1 and n ∉ {1,449,457,461}}`;
  - the count is
    `|S| = 464 - floor(464/2) - floor(464/3) + floor(464/6) - 4 = 464 - 232 - 154 + 77 - 4 = 151`.
- Since `|C| = 88` and `151 > 88`, there is ample room to choose `88` labels for `C` from `S`.
- A concrete choice is to take the first `88` elements of `S` in increasing order:
  `5,7,11,13,17,19,23,25,29,31,35,37,41,43,47,49,53,55,59,61,65,67,71,73,77,79,83,85,89,91,95,97,101,103,107,109,113,115,119,121,125,127,131,133,137,139,143,145,149,151,155,157,161,163,167,169,173,175,179,181,185,187,191,193,197,199,203,205,209,211,215,217,221,223,227,229,233,235,239,241,245,247,251,253,257,259,263,265`.
- Let `D` receive the remaining `352` labels.
- Why this solves the arithmetic interfaces:
  - every label in `A` has prime support contained in `{2,3}`;
  - every label in `C` is coprime to `6`, hence to every label in `A`;
  - the only labels divisible by `449`, `457`, or `461` in the interval are those labels themselves, already placed in `B`;
  - therefore every label in `C ∪ D` is coprime to every nontrivial label in `B`.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,88,352`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For this instance, it is sufficient to choose:
   - `A` from labels whose prime factors lie in `{2,3}`;
   - `B = {1,q_1,q_2,q_3}` with `q_i > 232` pairwise coprime;
   - `C` from labels coprime to `6q_1q_2q_3`;
   - `D` as the remaining complement.
7. Under that choice, every `A-C`, `B-C`, `B-B`, and `B-D` coprimality obligation is automatic.
8. Therefore any partition of `{1,...,464}` into class label sets satisfying those conditions gives a prime labeling.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Abandon the earlier low-barrier spill template because its forced multiples no longer fit into `A`.
- Use a spill-free high barrier on `B`, fixed `2,3`-smooth labels on `A`, and a large complementary pool for `C`.
- Only after the full classwise partition was fixed, use one tiny bounded checker command to confirm the concrete witness against the ring graph.

## self_checks

- After statement lock:
  - the target remains the exact feeder instance `Γ(Z_89 × Z_25)`;
  - the label interval length `464` matches `20 + 4 + 88 + 352`.
- After Approach A:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the full graph again collapses to three arithmetic interfaces.
- After Approach B:
  - the old low-barrier reservoir idea is genuinely impossible here because its spill already exceeds the `20` `A` slots;
  - `449`, `457`, and `461` are each above half the interval, so `B` has no nontrivial spill at all;
  - the complementary pool size `151` is comfortably larger than the needed `88`.
- After the concrete witness was fixed:
  - `A`, `B`, and `C` are disjoint and have sizes `20,4,88`;
  - the remaining complement has size `352`, exactly `|D|`;
  - every actual edge in the instantiated ring graph was checked to have coprime labels.

## code_used

- Minimal code was used only after the reasoning and explicit class partition were fixed.
- A one-off bounded local checker command instantiated the above `A`, `B`, and `C` sets, assigned the complement to `D`, enumerated the `464` nonzero zero-divisors of `Z_89 × Z_25`, generated edges directly from the ring multiplication rule, checked bijectivity onto `{1,...,464}`, and tested `gcd = 1` on every edge.
- Result after running that checker:
  - `vertex_count = 464`
  - `edge_count = 3526`
  - `edge_type_counts = {A-C: 1760, B-B: 6, B-C: 352, B-D: 1408}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108` on `A` in any order;
  - put the labels `1,449,457,461` on `B` in any order;
  - put the labels
    `5,7,11,13,17,19,23,25,29,31,35,37,41,43,47,49,53,55,59,61,65,67,71,73,77,79,83,85,89,91,95,97,101,103,107,109,113,115,119,121,125,127,131,133,137,139,143,145,149,151,155,157,161,163,167,169,173,175,179,181,185,187,191,193,197,199,203,205,209,211,215,217,221,223,227,229,233,235,239,241,245,247,251,253,257,259,263,265`
    on `C` in any order;
  - put the remaining `352` labels on `D` in any order.
- Why this works:
  - `B-B` edges:
    `1,449,457,461` are pairwise coprime.
  - `A-C` edges:
    every `A` label is `2,3`-smooth, every `C` label is coprime to `6`, so each cross gcd is `1`.
  - `B-C` edges:
    every `C` label avoids the factors `449`, `457`, and `461`, and the only labels in the interval carrying those factors are the three barrier labels themselves.
  - `B-D` edges:
    for the same reason, no `D` label is divisible by `449`, `457`, or `461`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; the idea of taking `A` from a fixed tiny prime-support reservoir; and the complementary-support move of choosing `B` so high that it has no spill at all.
  - what part does not yet scale:
    the argument still needs an arithmetic supply lemma guaranteeing three pairwise-coprime labels above half the interval and at least `p - 1` labels in the complementary coprime pool for general `p`.
  - what theorem slice is suggested:
    a high-barrier complementary-support theorem for large enough `Γ(Z_p × Z_25)`, distinct from the earlier low-`p` barrier-spill slice.
  - what one or two next feeder instances would help most:
    `Γ(Z_97 × Z_25)` as the immediate next feeder on the same large-`p` regime, and `Γ(Z_101 × Z_25)` as the next stress test after that.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is closer to a paper-shaped claim than the earlier hand-tuned spill records because the proof surface is now a clean large-parameter template rather than finite spill bookkeeping.

## family_affinity

- Family affinity is high.
- This feeder sits directly on the active `Γ(Z_p × Z_25)` campaign line and tests the wrapper-style high-barrier regime named in the family hint.
- The main value is not only that `p = 89` appears to survive, but that it survives by a cleaner large-`p` construction than the earlier small-spill exact records.

## generalization_signal

- Generalization signal is strong.
- The exact instance suggests a second arithmetic regime on the four-class line:
  - low and medium `p` are handled by barrier spill absorbed into `A`;
  - larger `p` can instead choose `B` above half the interval, making the barrier spill disappear entirely.
- In that large-`p` regime, `A` can be fixed inside a tiny smooth reservoir and `C` can be drawn from a much larger complementary set of labels coprime to that reservoir.
- This is a real theorem-slice signal, not just another isolated witness list.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. fix `A` inside a small prime-support set such as the `2,3`-smooth labels;
  4. choose `B = {1,q_1,q_2,q_3}` with pairwise-coprime `q_i > (5p+19)/2`;
  5. choose `C` from labels coprime to `6q_1q_2q_3`;
  6. assign the residual complement to `D`.
- Relative to the earlier `p = 13,17,19,23` records, the reusable gain is conceptual:
  the barrier itself no longer needs an `A`-reservoir accounting argument once it sits above half the interval.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, let `N = 5p + 19`. If one can choose
  - `20` distinct labels in `{1,...,N}` whose prime divisors lie in `{2,3}`,
  - three pairwise-coprime labels `q_1,q_2,q_3` in `(N/2,N]`,
  - and at least `p - 1` labels in `{1,...,N}` coprime to `6q_1q_2q_3`,
  then taking
  - `A` as those `20` smooth labels,
  - `B = {1,q_1,q_2,q_3}`,
  - `C` as any `p - 1` labels from that coprime pool,
  - `D` as the remaining complement,
  yields a prime labeling of `Γ(Z_p × Z_25)`.
- The present feeder realizes this slice at `p = 89` with `q_1,q_2,q_3 = 449,457,461`.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this line is `p = 97`.
- Reason:
  `z89` appears to be the first preserved high-barrier complementary-support witness in this worktree, so `z97` is the next honest check that this large-`p` regime is not a single-instance accident.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder with no rediscovery audit in this pass and no Lean closure.
- It is publication-relevant because it suggests a new family theorem slice on the same campaign line:
  a large-`p` complementary-support regime that looks cleaner than the earlier finite spill arguments.
- The likely publishable unit is still the family reduction together with a quantified high-barrier supply lemma, not the single `p = 89` witness by itself.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the stable `Γ(Z_p × Z_25)` reduction already used across the campaign.
- The arithmetic failure point would be an incorrect count of the complementary pool `|S|`.
- Another arithmetic failure point would be using a barrier label at or below half the interval, which would reintroduce nontrivial multiples into `D`.
- Publication-wise, the main weakness is that the current argument still uses an instance-specific choice of large barrier labels rather than a closed family supply theorem.

## what_verify_should_check

- Recompute the `464` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `3526` edges.
- Check that the chosen `A`, `B`, and `C` label sets are disjoint, have sizes `20,4,88`, and leave exactly `352` labels for `D`.
- Recheck that `449`, `457`, and `461` are pairwise coprime and exceed `232`, so they have no nontrivial multiples in the interval.
- Recheck the pool count `|S| = 151`.
- Run the bounded exact-instance checker on the explicit witness and confirm `edge_coprime_ok = 1`.

## verify_rediscovery

- PASS 1 used a bounded live web audit with the required query types: exact-instance notation `Γ(Z_89 × Z_25)` / `Gamma(Z_89 x Z_25)`, alternate notation `Z_89 x Z_(5^2)` and family notation `Γ(Z_p × Z_(q^2))`, the canonical source title `On prime labelings of zero-divisor graphs`, theorem/corollary checks inside that source, and one later-status query.
- Exact-instance and alternate-notation searches did not surface a paper, theorem, proposition, example, observation, or corollary settling the exact case `Γ(Z_89 × Z_25)`.
- The canonical source was Fox-Mooney, `On prime labelings of zero-divisor graphs` (Combinatorial Press, published online `2025-11-21`, https://combinatorialpress.com/cn-articles/volume-236/on-prime-labelings-of-zero-divisor-graphs/). In that paper, nearby solved families include `Γ(Z_p × Z_4)`, `Γ(Z_p × Z_9)`, and `Γ(Z_2 × Z_(p^2))`, while the broader family `Γ(Z_p × Z_(q^2))` is still stated as Conjecture `4.4`, not as a theorem that would imply `q = 5`.
- The bounded later-status query did not reveal a newer published closure of either the exact `p = 89, q = 5` instance or the full `Γ(Z_p × Z_(q^2))` family.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The solve record matches the intended exact mathematical claim: existence of a prime labeling of the full simple zero-divisor graph `Γ(Z_89 × Z_25)` on all `464` nonzero zero-divisors.
- There is no drift to a proxy support graph, quotient graph, partial labeling, or weakened claim. The support classes are used only as a reduction device for the exact ring graph.
- The classwise `any order` language is faithful here:
  - inside `A`, `C`, and `D`, vertices have identical neighborhoods within the exact graph;
  - inside `B`, the only internal edges are the `K_4` edges among distinct `B` vertices, and the chosen four `B` labels are pairwise coprime, so any permutation within `B` still works.
- The only repair needed is conservative metadata, not mathematics: the solve-stage status had `lean_ready = true`, which is too aggressive for a not-yet-formalized feeder instance.

## verify_proof

- I recomputed the vertex partition directly from the ring definition and recovered `|A| = 20`, `|B| = 4`, `|C| = 88`, and `|D| = 352`, for total `464` vertices.
- I independently recomputed the exact edge set and again obtained only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `1760`, `6`, `352`, and `1408`, for total `3526` edges.
- Given that support graph, the proof reduces correctly to the three arithmetic obligations claimed in the solve record:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly. The displayed `A`, `B`, and `C` sets are disjoint, have sizes `20,4,88`, and leave exactly `352` labels for `D`.
- I rechecked the key arithmetic facts:
  - `449`, `457`, and `461` are pairwise coprime and all exceed `N/2 = 232`, so none has a nontrivial multiple in `{1,...,464}`;
  - the complementary pool `S = {n ≤ 464 : gcd(n,6) = 1 and n ∉ {1,449,457,461}}` has size `151`;
  - the chosen `C` set is a subset of `S`, so every `A-C` and `B-C` gcd is `1`;
  - since the only multiples of `449`, `457`, and `461` in the interval are the labels themselves, every `B-D` gcd is also `1`.
- First incorrect step found: none.

## verify_adversarial

- There was no saved checker script in the artifact, so I reran an independent one-off exact-instance command that:
  - enumerated the `464` nonzero zero-divisors of `Z_89 × Z_25`;
  - rebuilt the edge set from the ring multiplication rule;
  - assigned the displayed `A`, `B`, and `C` label sets and the residual complement to `D`;
  - checked bijectivity onto `{1,...,464}`;
  - checked `gcd = 1` on every edge.
- That command returned:
  - `vertex_count = 464`
  - `class_counts = {A: 20, B: 4, C: 88, D: 352}`
  - `edge_count = 3526`
  - `edge_types = {A-C: 1760, B-B: 6, B-C: 352, B-D: 1408}`
  - `bad_edges = 0`
- I also tried to break the witness by checking the interfaces directly at the label-set level. All pairwise gcd checks on `A-C`, `B-C`, `B-B`, and `B-D` passed.
- I did not find a hidden edge type, mislabeled vertex class, duplicate label, or computational mismatch between the explicit witness and the actual ring graph.

## verify_theorem_worthiness

- This is still not a theorem slice by itself. On its own, it remains one verified feeder instance.
- It does have real slice leverage, though, because the proof is structural rather than purely hand-picked: it reuses the four-class support reduction and tests the live high-barrier complementary-support wrapper rather than a disconnected one-off trick.
- The part of the argument that scales is clear:
  - the support decomposition `A,B,C,D`;
  - reduction to the interfaces `A-C`, `B-B`, `B-C`, and `B-D`;
  - fixing `A` inside a small `2,3`-smooth reservoir;
  - choosing nontrivial `B` labels above half the interval so the barrier has no spill;
  - choosing `C` from a complementary pool avoiding the prime support of `A ∪ B`.
- The part that still does not scale automatically is also clear:
  - a quantified supply lemma is still needed to guarantee three suitable high barrier labels and at least `p - 1` complementary labels for general `p`;
  - the barrier-clique packaging still has to be turned into a final paper-facing theorem rather than repeated feeder arithmetic.
- The best honest publication status is therefore `SLICE_CANDIDATE`, not `PAPER_READY`, because this feeder materially supports the live family slice but does not itself prove the parameterized theorem.
- The smallest next parameter shift that most directly tests the claimed template is `Γ(Z_97 × Z_25)`.

## verify_verdict

- `VERIFIED`
- No rediscovery was established, the claim matches the intended instance exactly, no incorrect proof step was found, and the explicit witness survived skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- No mathematical repair to the witness was needed.
- Conservative metadata repair only:
  - downgrade `lean_ready` to `false`;
  - keep the run at `classification = CANDIDATE` during verify.
