# Solve Record: z43-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Gamma(Z_43 x Z_25) prime?`
- Active slug: `z43-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_43 × Z_25)` admits a prime labeling, meaning a bijection from its `234` vertices to `{1,2,...,234}` such that adjacent vertices receive coprime labels.
- This solve pass is locked to the exact feeder instance `Z_43 × Z_25`, not to a full all-`p` theorem.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_43` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the standard four support classes for `F25(p) = Γ(Z_p × Z_25)`:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_43^×}`, size `42`.
  - `D = {(a,5t) : a ∈ Z_43^×, t ∈ {1,2,3,4}}`, size `168`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 43` and `bd = 0 mod 25`.
- Because `Z_43` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both second coordinates are multiples of `5`.
- Ambiguities, conventions, or missing definitions:
  - use the simple zero-divisor graph, so there are no loops;
  - exclude `(0,0)` from the vertex set;
  - once class label sets are fixed, labels may be permuted inside `A`, `C`, and `D` because those classes have uniform neighborhoods;
  - the four vertices of `B` form a `K_4`, so any permutation of a pairwise-coprime `B` label set also preserves the witness.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- The forced edge counts at `p = 43` are:
  - `A-C = 20 · 42 = 840`;
  - `B-B = 6`;
  - `B-C = 4 · 42 = 168`;
  - `B-D = 4 · 168 = 672`.
- Total predicted edge count: `840 + 6 + 168 + 672 = 1686`.
- Therefore the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.

## approach_B

- Construction / extremal route by minimizing the factor palette of `A ∪ B`.
- The campaign already says the fixed wrapper `B = {1,19,23,29}` is obsolete beyond `p = 31`. At `p = 43` its spill is even worse:
  - the nontrivial multiples of `19`, `23`, and `29` in `{1,...,234}` form a set of size `27`, which cannot fit inside the `20` labels of `A`.
- So the right starting point is the second-generation moved barrier already preserved at `p = 37` and `p = 41`:
  - take `B = {1,43,47,53}`.
- Its nontrivial multiples inside `{1,...,234}` are exactly
  `86,94,106,129,141,159,172,188,212,215`,
  so its spill size is only `10`.
- Put those ten forced spill labels in `A`, and fill the remaining ten `A` slots with labels whose prime factors stay inside a tiny palette:
  - choose fillers `2,3,4,5,6,7,8,9,11,13`.
- Then every prime factor appearing in `A ∪ B` lies in
  `{2,3,5,7,11,13,43,47,53}`.
- So any prime outside that palette is automatically coprime to every label in `A ∪ B`.
- In `{1,...,234}`, the primes outside that palette are exactly
  `17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233`.
- That list has size exactly `42 = |C|`, so it can serve as the full `C` block.
- One explicit classwise partition suggested by this reasoning is:
  - `B = {1,43,47,53}`;
  - `A = {2,3,4,5,6,7,8,9,11,13,86,94,106,129,141,159,172,188,212,215}`;
  - `C = {17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233}`;
  - `D` gets the remaining `168` labels.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,42,168`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For this instance, it is sufficient to choose a pairwise-coprime barrier `B` whose nontrivial multiples all lie in `A`, then choose `C` as primes outside the factor palette of `A ∪ B`, and finally let `D` be the remaining complement.
7. Therefore any partition of `{1,...,234}` into class label sets satisfying those obligations gives a prime labeling.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Reject the old fixed wrapper `B = {1,19,23,29}` immediately, because its spill count is already `27 > 20`.
- Use the moved sparse barrier `B = {1,43,47,53}`.
- Keep `A` on the controlled factor palette `{2,3,5,7,11,13,43,47,53}`.
- Take `C` to be exactly the `42` primes in `{1,...,234}` outside that factor palette.
- Only after the full witness is fixed, use one tiny checker to validate the explicit class partition against the ring definition.

## self_checks

- After statement lock:
  - the exact target remains the feeder instance `Γ(Z_43 × Z_25)`;
  - the label interval length `234` matches the vertex count `20 + 4 + 42 + 168`.
- After Approach A:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the exact graph again collapses to three arithmetic interfaces.
- After Approach B:
  - the old fixed wrapper is genuinely impossible here as a wrapper because its spill is `27`, not merely near the boundary `20`;
  - the moved barrier `B = {1,43,47,53}` has spill only `10`;
  - the chosen `A` fillers keep the factor palette small enough to leave exactly `42` available primes for `C`.
- After choosing the plan:
  - this remains reasoning-first because the witness is dictated by support reduction and factor-palette bookkeeping, not by optimization search;
  - minimal code is justified only as post-construction witness verification.

## code_used

- Minimal code was used only after the reasoning and explicit class partition were fixed.
- A tiny local checker `check_witness.py` enumerates the `234` nonzero zero-divisors of `Z_43 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,234}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 234`
  - `edge_count = 1686`
  - `edge_type_counts = {A-C: 840, B-B: 6, B-C: 168, B-D: 672}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `1,43,47,53` on `B` in any order;
  - put the labels `2,3,4,5,6,7,8,9,11,13,86,94,106,129,141,159,172,188,212,215` on `A` in any order;
  - put the labels `17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233` on `C` in any order;
  - put the remaining `168` labels on `D`.
- Why this works:
  - `B-B` edges: `1,43,47,53` are pairwise coprime.
  - `A-C` and `B-C` edges: every label on `C` is a prime outside the factor palette of `A ∪ B`, so every label on `A ∪ B` is coprime to every label on `C`.
  - `B-D` edges: every nontrivial multiple of `43`, `47`, or `53` up to `234` was deliberately placed in `A`, so no label in `D` is divisible by a nontrivial label on `B`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; the barrier/reservoir/prime-block viewpoint; and the second-generation move of pushing the barrier to larger primes so the spill into `A` shrinks.
  - what part does not yet scale:
    the existence of a good barrier and a large enough prime pool is still finite arithmetic bookkeeping, not yet a proved general lemma;
    at `p = 43` the witness is explicit, but there is still no quantified theorem saying a suitable barrier always exists.
  - what theorem slice is suggested:
    a movable sparse-barrier sufficient-condition theorem for `Γ(Z_p × Z_25)`:
    if `{1,...,5p+19}` admits a pairwise-coprime barrier `B = {1,q_1,q_2,q_3}` whose nontrivial multiples fit inside the `20` labels of `A` and still leaves `p - 1` primes disjoint from the factor palette of `A ∪ B`, then the four-interface bridge theorem closes the full graph.
  - what one or two next feeder instances would help most:
    `Γ(Z_47 × Z_25)` as the next pressure test for the moved barrier line, and `Γ(Z_53 × Z_25)` as the first case where one current barrier prime itself would need to be reconsidered if the same template is pushed further.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still instance-level evidence, but it is closer to a paper-shaped claim than `p = 37` alone because the moved sparse-barrier redesign now appears to survive beyond its first two preserved checkpoints.

## family_affinity

- Family affinity is high.
- This instance is not a random exact feeder: it is the next campaign-designated pressure test after the preserved moved-barrier successes at `p = 37` and `p = 41`.
- The main family value is that `p = 43` still closes when the barrier prime `43` is no longer “comfortably below” the parameter line, so the second-generation template is not obviously a one-step accident.

## generalization_signal

- Generalization signal is strong.
- At `p = 43`, the right invariant is not “choose `C` above a threshold,” but “keep the factor palette of `A ∪ B` small enough that the remaining primes fill `C`.”
- The witness suggests the movable sparse-barrier program should be formulated in terms of:
  - barrier spill count into the fixed `20` slots of `A`; and
  - residual prime-pool count outside the factor palette of `A ∪ B`.
- That is a publication-mode signal because it points to a referee-facing sufficient-condition theorem rather than to another isolated label list.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. choose a pairwise-coprime barrier `B = {1,q_1,q_2,q_3}`;
  4. force every nontrivial multiple of `q_1,q_2,q_3` into `A`;
  5. choose `A` fillers that keep the factor palette of `A ∪ B` deliberately small;
  6. let `C` be any set of `p - 1` primes outside that factor palette;
  7. assign the remaining complement to `D`.
- Relative to the earlier `p = 13,17,19,23` records, the reusable gain here is conceptual:
  the solve no longer depends on a half-interval or fixed-threshold prime block;
  it depends on factor-palette control under a movable sparse barrier.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, `Γ(Z_p × Z_25)` is prime whenever `{1,...,5p+19}` admits
  - a pairwise-coprime barrier `B = {1,q_1,q_2,q_3}` whose nontrivial multiples occupy at most `20` labels;
  - an `A` filler set whose prime factors stay inside a controlled palette disjoint from the chosen `C` primes;
  - a set `C` of `p - 1` primes disjoint from the factor palette of `A ∪ B`.
- The `p = 43` feeder suggests that the family theorem should be phrased in terms of factor palettes, not just barrier thresholds or below-half spill language.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this line is `p = 47`.
- Reason:
  `p = 43` survives while using the same moved barrier that already worked at `p = 37` and `p = 41`, so `p = 47` is the next honest pressure point for whether this exact barrier still has enough prime-pool slack.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder, with no bounded rediscovery audit in this pass and no Lean closure.
- It is publication-relevant because it sharpens the live `F25` companion target:
  the fixed wrapper is decisively dead here, but the moved sparse-barrier route still survives.
- The likely publishable unit is still a movable sparse-barrier sufficient-condition theorem, or else a bounded theorem/result pair describing exactly where a chosen barrier works and where it first fails.

## likely_failure_points

- The structural failure point would be a missed edge type in the support decomposition, though that would contradict the now-stable `F25` support graph.
- The arithmetic failure point would be a missed nontrivial multiple of `43`, `47`, or `53` left in `D`.
- Another arithmetic failure point would be accidentally placing in `A ∪ B` a label divisible by one of the chosen `C` primes.
- Publication-wise, the main weakness is that the moved-barrier arithmetic is still a preserved pattern, not yet a proved theorem with quantified hypotheses.

## what_verify_should_check

- Recompute the `234` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `1686` edges.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,234}`.
- Check coprimality on every actual edge from the ring graph.
- Audit whether any existing family-level sufficient-condition theorem already implies this `p = 43` case.
- If verification passes, treat this as strong feeder evidence for the movable sparse-barrier theorem before any exact-instance Lean work.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact tuple `Γ(Z_43 × Z_25)`, ASCII variants such as `Gamma(Z_43 x Z_25)`, the family notation `Γ(Z_p × Z_(q^2))`, the canonical 2025 source on prime labelings of zero-divisor graphs, same-source theorem / proposition / example / corollary checks, and one recent status check.
- Exact-instance and alternate-notation searches did not reveal an earlier theorem, proposition, example, observation, or corollary settling the exact `p = 43, q = 5` case within budget.
- The canonical source check was the Fox-Mooney paper `On prime labelings of zero-divisor graphs`, published online by Combinatorial Press on `2025-11-21`. In that source, nearby solved families include cases such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))`, while the ambient family `Γ(Z_p × Z_(q^2))` is still left open as Conjecture `4.4`, not closed by a theorem implying `Γ(Z_43 × Z_25)`.
- Verdict for PASS 1: no rediscovery established within the bounded audit.

## verify_faithfulness

- The solve record is aimed at the exact intended statement: existence of a prime labeling for the full simple zero-divisor graph `Γ(Z_43 × Z_25)` on the `234` nonzero zero-divisors, with labels bijectively covering `{1,...,234}`.
- There is no wrong-theorem drift to a support graph, induced subgraph, or partial labeling. The support classes `A,B,C,D` are used only as a reduction device for the exact graph.
- The campaign-level theorem-slice language is clearly separated from the solved claim. The verified mathematical content here is still the single feeder instance, not the full movable sparse-barrier theorem.
- Faithfulness verdict: the claimed result matches the intended statement exactly.

## verify_proof

- I recomputed the zero-divisor partition directly from the ring definition and recovered `|A| = 20`, `|B| = 4`, `|C| = 42`, and `|D| = 168`, for total `234` vertices.
- I independently rederived the exact edge set and again obtained only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `840`, `6`, `168`, and `672`, for total `1686` edges.
- Given that support graph, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly. The `C` labels are all prime and avoid the factor palette `{2,3,5,7,11,13,43,47,53}` of `A ∪ B`. The nontrivial multiples of `43`, `47`, and `53` inside `{1,...,234}` are exactly `86,94,106,129,141,159,172,188,212,215`, all deliberately placed in `A`, so no `D` label violates a `B-D` edge.
- First incorrect step found: none. The proof remains finite instance arithmetic rather than a general theorem, but the witness argument itself is correct.

## verify_adversarial

- I reran `artifacts/z43-z25-prime-zero-divisor-graph/check_witness.py`. It again reported `vertex_count = 234`, `edge_count = 1686`, `edge_type_counts = {'A-C': 840, 'B-B': 6, 'B-C': 168, 'B-D': 672}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran independent checks outside the artifact checker to confirm:
  - `A`, `B`, and `C` have sizes `20`, `4`, and `42`, and the complement `D` has size `168`;
  - the four class label sets are disjoint and cover exactly `{1,...,234}`;
  - every `C` label is prime and avoids the factor palette of `A ∪ B`;
  - no `D` label shares a nontrivial common factor with `43`, `47`, or `53`.
- I explicitly checked the barrier-spill boundary: the next possible multiple `5·47 = 235` lies just outside the label interval, so the claimed spill list inside `{1,...,234}` is complete.
- I did not find a hidden edge type, a mislabeled vertex, or a divisibility obstruction breaking the witness.

## verify_theorem_worthiness

- This remains an instance result, not a theorem slice by itself. The structural part that scales is the already-live four-class ring reduction for `Γ(Z_p × Z_25)`.
- The genuinely new feeder value at `p = 43` is that the moved sparse barrier `B = {1,43,47,53}` still works even when `43` itself has moved into the barrier set, while the frozen wrapper `B = {1,19,23,29}` is now decisively impossible here because its spill is `27 > 20`.
- The part that does not yet scale automatically is the finite arithmetic existence argument for the barrier and prime pool. This record still hand-picks the barrier, the `A` fillers, and the full `C` prime block rather than proving a quantified companion theorem.
- The best honest publication status for this artifact is therefore `SLICE_CANDIDATE`, not `INSTANCE_ONLY`, because it is functioning as a live pressure test for a real family theorem slice. It is still far from `PAPER_READY`.
- The smallest next discriminator for the claimed template is `Γ(Z_47 × Z_25)`, which tests whether the same moved sparse-barrier line survives one more parameter shift before the barrier must be redesigned again.

## verify_verdict

- `VERIFIED`
- No rediscovery was established in the bounded prior-art pass, the claim matches the intended exact instance, and the explicit witness survived both the artifact checker and independent skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed for this instance and the publication-facing gain is still feeder evidence rather than a closed theorem.

## minimal_repair_if_any

- No mathematical repair was needed.
- Conservative handling note: keep the theorem-slice language as campaign guidance only; the verified claim in this artifact is the exact `p = 43` feeder instance.
