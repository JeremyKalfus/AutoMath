# Solve Record: z41-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_41 × Z_25) prime?`
- Active slug: `z41-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_41 × Z_25)` admits a prime labeling, meaning a bijection from its `224` vertices to `{1,2,...,224}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_41 × Z_25`, not to a full all-prime theorem for `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_41` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the same four support classes used on the `Γ(Z_p × Z_25)` campaign line:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_41^×}`, size `40`.
  - `D = {(a,5t) : a ∈ Z_41^×, t ∈ {1,2,3,4}}`, size `160`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 41` and `bd = 0 mod 25`.
- Because `Z_41` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - vertices inside `A`, `C`, and `D` have identical neighborhoods, so labels may be permuted inside those classes once the class label sets are fixed;
  - the four `B` vertices form a `K_4`, so any permutation of a pairwise-coprime `B` label set also preserves the witness.
- Ambiguities or missing definitions:
  - none that block the solve; the campaign notation already fixes the support classes and graph convention.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 41` are therefore forced:
  - `A-C = 20 · 40 = 800`;
  - `B-B = 6`;
  - `B-C = 4 · 40 = 160`;
  - `B-D = 4 · 160 = 640`.
- Total predicted edge count: `800 + 6 + 160 + 640 = 1606`.
- Therefore the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Brief self-check after Approach A:
  - vertex count check: `20 + 4 + 40 + 160 = 224`;
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`, so no new graph-theoretic obstruction appears at `p = 41`.

## approach_B

- Construction / extremal route by moving the barrier clique instead of trying to preserve the old wrapper.
- The old fixed barrier `B = {1,19,23,29}` is no longer viable at `p = 41`:
  - the nontrivial multiples of `19` up to `224` contribute `10` labels;
  - the nontrivial multiples of `23` contribute `8` labels;
  - the nontrivial multiples of `29` contribute `6` labels;
  - total spill `24` exceeds the fixed `20` slots of `A`.
- So the right extremal move is not a graph-level contradiction; it is to move the sparse barrier to larger primes whose spill fits inside `A`.
- A clean candidate is
  `B = {1,43,47,53}`.
- Its nontrivial multiples up to `224` are exactly:
  - for `43`: `86,129,172,215`;
  - for `47`: `94,141,188`;
  - for `53`: `106,159,212`.
- That is only `10` forced spill labels, so half of `A` remains free.
- For the `C` block, exclude the prime palette
  `{2,3,5,7,11,43,47,53}`.
- Up to `224`, the remaining primes are exactly the `40` labels
  `13,17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223`.
- Hence `C` can be filled exactly by that 40-prime set.
- Use the other `10` slots of `A` for tiny fillers built only from the excluded small primes:
  `2,3,4,5,6,7,8,9,10,11`.
- One explicit classwise partition suggested by this reasoning is:
  - `B = {1,43,47,53}`;
  - `A = {2,3,4,5,6,7,8,9,10,11,86,94,106,129,141,159,172,188,212,215}`;
  - `C = {13,17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223}`;
  - `D` gets the remaining `160` labels.
- Why this is enough:
  - every label in `C` is prime and none of those primes divides any label in `A ∪ B`;
  - `1,43,47,53` are pairwise coprime;
  - every label divisible by `43`, `47`, or `53` beyond the barrier itself has been forced into `A`, so no label in `D` shares a nontrivial factor with `B`.
- Brief self-check after Approach B:
  - `|C| = 40` exactly matches the size required for the `C` class;
  - the barrier spill from `43,47,53` has size `10`, leaving `10` free `A` slots;
  - the chosen `A` fillers use only excluded small primes, so `A-C` coprimality is automatic.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,40,160`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For this instance it is sufficient to choose a pairwise-coprime barrier set `B`, place every nontrivial multiple of its nontrivial labels into `A`, choose `C` from primes disjoint from the factor palette used by `A ∪ B`, and let `D` be the remaining complement.
7. Therefore any partition of `{1,...,224}` into class label sets satisfying those obligations gives a prime labeling of `Γ(Z_41 × Z_25)`.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Start by proving that the old fixed wrapper `B = {1,19,23,29}` fails by spill count at `p = 41`.
- Replace it with the moved sparse barrier `B = {1,43,47,53}`.
- Fill `A` by the ten forced barrier multiples together with ten tiny excluded-palette fillers.
- Fill `C` by the 40 primes outside the excluded palette `{2,3,5,7,11,43,47,53}`.
- Only after fixing that explicit class partition, use one tiny checker to validate the witness against the ring definition.
- Brief self-check after choosing the plan:
  - this remains reasoning-first because the construction is dictated by support reduction and divisibility bookkeeping, not by optimization search;
  - minimal code is justified only as post-construction witness verification.

## self_checks

- Statement lock:
  - the exact target is the feeder instance `Γ(Z_41 × Z_25)`;
  - the label interval length `224` matches the vertex count.
- Structural reduction:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the full graph again collapses to three arithmetic interfaces.
- Construction:
  - the old barrier `19,23,29` now fails by count because its spill is `24 > 20`;
  - the moved barrier `43,47,53` has spill size `10`;
  - the excluded palette leaves exactly `40` usable primes for `C`.
- Final witness:
  - `A`, `B`, and `C` are disjoint and have sizes `20,4,40`;
  - the remaining complement has size `160`, exactly `|D|`;
  - every nontrivial multiple of `43`, `47`, and `53` lies in `A`, not `D`;
  - every label in `A ∪ B` is coprime to every label in `C`.

## code_used

- No code was used before the reasoning and explicit class partition were fixed.
- After the witness was fully specified, a tiny local checker `check_witness.py` was used only for witness verification.
- The checker enumerates the `224` nonzero zero-divisors of `Z_41 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,224}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 224`
  - `edge_count = 1606`
  - `edge_type_counts = {A-C: 800, B-B: 6, B-C: 160, B-D: 640}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `1,43,47,53` on `B` in any order;
  - put the labels `2,3,4,5,6,7,8,9,10,11,86,94,106,129,141,159,172,188,212,215` on `A` in any order;
  - put the labels `13,17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223` on `C` in any order;
  - put the remaining `160` labels
    `12,14,15,16,18,20,21,22,24,25,26,27,28,30,32,33,34,35,36,38,39,40,42,44,45,46,48,49,50,51,52,54,55,56,57,58,60,62,63,64,65,66,68,69,70,72,74,75,76,77,78,80,81,82,84,85,87,88,90,91,92,93,95,96,98,99,100,102,104,105,108,110,111,112,114,115,116,117,118,119,120,121,122,123,124,125,126,128,130,132,133,134,135,136,138,140,142,143,144,145,146,147,148,150,152,153,154,155,156,158,160,161,162,164,165,166,168,169,170,171,174,175,176,177,178,180,182,183,184,185,186,187,189,190,192,194,195,196,198,200,201,202,203,204,205,206,207,208,209,210,213,214,216,217,218,219,220,221,222,224`
    on `D` in any order.
- Why this works:
  - `B-B` edges: `1,43,47,53` are pairwise coprime.
  - `A-C` and `B-C` edges: every label on `C` is prime, and none of those primes divides any label in `A ∪ B` because `A ∪ B` uses only the excluded palette `{2,3,5,7,11,43,47,53}`.
  - `B-D` edges: every label divisible by `43`, `47`, or `53` beyond the barrier itself has been forced into `A`, so no label in `D` shares a nontrivial factor with `B`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; the sparse-barrier viewpoint; and the factor-palette rule “build `A ∪ B` from an excluded palette, then take `C` from the complementary prime pool.”
  - what part does not yet scale:
    the moved sparse barrier itself is still hand-chosen here, and there is not yet a proved family lemma guaranteeing, for each `p`, a barrier with spill at most `20` together with `p - 1` available complementary primes.
  - what theorem slice is suggested:
    a movable sparse-barrier sufficient-condition theorem for `Γ(Z_p × Z_25)`: if `{1,...,5p+19}` contains a pairwise-coprime barrier `B = {1,q_1,q_2,q_3}` whose spill fits inside the `20` labels of `A`, and if there are `p - 1` primes disjoint from the factor palette of `A ∪ B`, then the graph is prime.
  - what one or two next feeder instances would help most:
    `Γ(Z_43 × Z_25)` as the immediate pressure point for the same moved barrier, and then `Γ(Z_47 × Z_25)` if `p = 43` still survives.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is closer to a paper-shaped claim because it supports the live family narrative that the right invariant is a movable sparse barrier, not the frozen `19,23,29` wrapper.

## family_affinity

- Family affinity is high.
- This feeder sits directly on the active `Γ(Z_p × Z_25)` campaign line and was explicitly selected as the next discriminator after the wrapper obstruction regime.
- The main value is not only that `p = 41` appears to survive, but that it survives via the same moved sparse barrier `B = {1,43,47,53}` that the family record already treats as the next live redesign.

## generalization_signal

- Generalization signal is strong.
- The strongest local signal is that the campaign's structural shift survives at `p = 41`: the frozen barrier `19,23,29` now fails by count, but the graph still appears prime after moving the barrier upward.
- The honest generalization message is:
  the companion theorem candidate on the `Γ(Z_p × Z_25)` line should be phrased in terms of movable sparse barriers and complementary prime palettes, not in terms of one permanently frozen barrier.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. choose a sparse pairwise-coprime barrier `B = {1,q_1,q_2,q_3}`;
  4. put every nontrivial multiple of `q_1,q_2,q_3` into `A`;
  5. fill the remaining `A` slots from a small excluded factor palette;
  6. choose `C` from `p - 1` primes outside that palette;
  7. let `D` be the complement.
- Relative to the earlier `p = 23` barrier-threshold formulation, the reusable gain here is that the barrier can move while the classwise proof surface stays the same.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, `Γ(Z_p × Z_25)` is prime whenever the interval `{1,...,5p+19}` admits
  - a pairwise-coprime barrier `B = {1,q_1,q_2,q_3}` whose nontrivial multiples occupy at most `20` labels,
  - a `20`-label class `A` containing all those barrier multiples and otherwise using only a controlled excluded factor palette,
  - and a `C` block of `p - 1` primes outside that palette.
- The present feeder suggests that the live family theorem should be stated at this movable-barrier level rather than at the earlier fixed `29`-threshold level.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on the four-class line is `p = 43`.
- Reason:
  `p = 41` appears to survive with the moved barrier `43,47,53`, so `p = 43` is the next honest pressure point for whether this same redesign persists one more odd prime.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder with no rediscovery pass in this artifact and no Lean closure.
- It is publication-relevant because it is a campaign-directed discriminator that appears to preserve the moved sparse-barrier story beyond the first wrapper obstruction.
- The likely publishable unit is still a family-level sparse-barrier theorem or a bounded obstruction/result package, not the single `p = 41` witness by itself.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the now-stable `Γ(Z_p × Z_25)` reduction.
- The arithmetic failure point would be a missed label in `D` divisible by `43`, `47`, or `53`.
- Another arithmetic failure point would be an overlooked `A ∪ B` label divisible by one of the chosen `C` primes.
- Publication-wise, the main weakness is that the barrier move is still an observed redesign, not yet a theorem with quantified existence.

## what_verify_should_check

- Recompute the `224` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `1606` edges.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,224}`.
- Check coprimality on every actual edge from the ring graph.
- Audit whether the local family record's `p = 37` redesign with barrier `43,47,53` is faithfully preserved elsewhere, since this worktree's family record references it but the exact feeder artifact is not present here.
- If verification passes, promote this as evidence for the movable sparse-barrier companion slice before any exact-instance Lean work.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact instance, alternate notation, the broader `Γ(Z_p × Z_25)` family phrasing, and the most relevant canonical recent source on prime labelings of zero-divisor graphs.
- Exact-instance searches on `Γ(Z_41 × Z_25)` and `Z_41 × Z_25` with `zero-divisor graph` and `prime labeling` did not surface an earlier theorem, proposition, example, observation, or corollary settling this case.
- Family-level searches on `Γ(Z_p × Z_25)` and `Z_p × Z_(5^2)` with `prime labeling` also did not produce a published theorem directly implying the exact `p = 41` instance within budget.
- The bounded source check returned the 2025 article `On Prime Labelings of Zero-Divisor Graphs` as the main nearby literature item. Within budget, that source did not establish this exact instance or an all-`p` theorem covering it.
- Verdict for PASS 1: no rediscovery established within the allowed audit budget.

## verify_faithfulness

- The claimed result matches the exact graph question in `selected_problem.md`: whether the full zero-divisor graph `Γ(Z_41 × Z_25)` admits a prime labeling.
- The proof target is still the simple graph on all nonzero zero-divisors of `Z_41 × Z_25`, with adjacency defined by coordinatewise zero product and labels a bijection onto `{1,...,224}`.
- The record does extract family meaning, but it does not replace the exact instance with a weaker support-level proxy or claim that the whole `Γ(Z_p × Z_25)` line is already settled.
- Wrong-theorem drift, quantifier drift, and definition drift were not found.

## verify_proof

- I recomputed the vertex partition from the ring definition and recovered the exact support classes `A,B,C,D` with sizes `20,4,40,160`.
- I also recomputed the edge pattern directly from the ring law and recovered only `A-C`, `B-B`, `B-C`, and `B-D`, with counts `800, 6, 160, 640`, hence total edge count `1606`.
- Given that exact support graph, the proof correctly reduces to three obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the displayed label sets:
  - `C` consists of 40 primes, none dividing any label in `A ∪ B`;
  - `B = {1,43,47,53}` is pairwise coprime;
  - every nontrivial multiple of `43`, `47`, and `53` up to `224` is in `A`, and none remains in `D`.
- First incorrect step found: none.

## verify_adversarial

- I reran `artifacts/z41-z25-prime-zero-divisor-graph/check_witness.py`.
- It reported `vertex_count = 224`, `edge_count = 1606`, `edge_type_counts = {'A-C': 800, 'B-B': 6, 'B-C': 160, 'B-D': 640}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- Independently of that checker, I verified that the four displayed label classes are disjoint, cover exactly `{1,...,224}`, and satisfy:
  - `A ∪ B` coprime to `C`;
  - `B` pairwise coprime;
  - `B` coprime to all labels in `D`.
- I also checked the main attack surface named in the solve record: no label in `D` is divisible by `43`, `47`, or `53`.
- No hidden edge type, missed divisibility obstruction, or computational mismatch appeared.

## verify_theorem_worthiness

- This is not only an isolated exact win. It strengthens the live `Γ(Z_p × Z_25)` companion story by showing that the graph still appears prime at `p = 41` after the frozen wrapper `B = {1,19,23,29}` has already failed by spill count.
- The structural part that scales is clear:
  - the four-class support decomposition;
  - the reduction to interfaces `A-C`, `B-B`, `B-C`, `B-D`;
  - the spill-count viewpoint for a four-label barrier;
  - the complementary-prime-palette construction for `C`.
- The part that does not yet scale is the existence theorem:
  - the moved barrier `B = {1,43,47,53}` is still hand-chosen here;
  - there is no proved family lemma yet guaranteeing such a barrier and enough compatible primes for every later `p`.
- The best honest publication status is therefore not `INSTANCE_ONLY`; it is `SLICE_CANDIDATE`, because this feeder directly sharpens a real companion theorem candidate while still falling well short of a theorem or paper-ready package.
- The smallest parameter shift that most tests the template is still `p = 43`, since `p = 41` survives with the moved barrier and `p = 43` is the next immediate pressure point for whether the same redesign persists.

## verify_verdict

- `VERIFIED`
- The exact `Γ(Z_41 × Z_25)` witness survives skeptical local verification, and no rediscovery was established within the bounded PASS 1 audit.
- The run must remain below `EXACT`: the result is a verified exact feeder with theorem-slice relevance, not a Lean-closed theorem.

## minimal_repair_if_any

- No repair was needed.
