# Solve Record: z23-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_23 × Z_25) prime?`
- Active slug: `z23-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_23 × Z_25)` admits a prime labeling, meaning a bijection from its `134` vertices to `{1,2,...,134}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_23 × Z_25`, not the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_23` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_23^×}`, size `22`.
  - `D = {(a,5t) : a ∈ Z_23^×, t ∈ {1,2,3,4}}`, size `88`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 23` and `bd = 0 mod 25`.
- Because `Z_23` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - vertices inside `A`, `C`, and `D` have identical neighborhoods, so labels may be permuted inside those classes once the class label sets are fixed;
  - the four `B` vertices form a `K_4`, so any permutation of a pairwise-coprime `B` label set also preserves the witness.
- Ambiguities or missing definitions:
  - none that block the solve; the campaign dossier already fixes the standard zero-divisor graph convention and the four support classes.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 23` are therefore forced:
  - `A-C = 20 · 22 = 440`;
  - `B-B = 6`;
  - `B-C = 4 · 22 = 88`;
  - `B-D = 4 · 88 = 352`.
- Total predicted edge count: `440 + 6 + 88 + 352 = 886`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Brief self-check after Approach A:
  - vertex count check: `20 + 4 + 22 + 88 = 134`;
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`, so no new graph-theoretic obstruction appears at `p = 23`.

## approach_B

- Construction / extremal route using a fixed barrier set and a cleaner prime threshold.
- Keep the same sparse barrier set on `B`:
  `B = {1,19,23,29}`.
- Its nontrivial multiples up to `134` are exactly:
  - for `19`: `38,57,76,95,114,133`;
  - for `23`: `46,69,92,115`;
  - for `29`: `58,87,116`.
- Those `13` forced spill labels fit inside the fixed `20` slots of `A`.
- The key arithmetic observation at `p = 23` is that `|C| = 22` and there are exactly `22` primes in `(29,134]`:
  `31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131`.
- So unlike the earlier `p = 13,17,19` bookkeeping, no repaired half-interval spill is needed here: just label `C` by all primes greater than `29`.
- Put on `A` the `13` nontrivial multiples of `19,23,29` together with `7` harmless fillers:
  `A = {2,3,4,5,6,7,8,38,46,57,58,69,76,87,92,95,114,115,116,133}`.
- Why this is enough:
  - every label in `A ∪ B` is either at most `29` or a multiple of one of `19,23,29`;
  - every label in `C` is a prime strictly greater than `29`;
  - therefore no label in `A ∪ B` is divisible by any prime in `C`, so all `A-C` and `B-C` edges are automatically coprime;
  - every nontrivial multiple of `19`, `23`, or `29` has been forced into `A`, so `D` is automatically coprime to `B`.
- One explicit classwise partition suggested by this reasoning is:
  - `C = {31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131}`;
  - `B = {1,19,23,29}`;
  - `A = {2,3,4,5,6,7,8,38,46,57,58,69,76,87,92,95,114,115,116,133}`;
  - `D` gets the remaining `88` labels.
- Brief self-check after Approach B:
  - `|C| = 22` matches the number of primes in `(29,134]` exactly;
  - the forced barrier spill from `B` has size `13`, leaving `7` free `A` slots;
  - none of the chosen `A ∪ B` labels is divisible by any chosen `C` prime.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,22,88`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For this instance, it is sufficient to choose:
   - `B = {1,19,23,29}`;
   - `A` containing every nontrivial multiple of `19`, `23`, and `29` in `{1,...,134}`;
   - `C` equal to all primes in `(29,134]`;
   - `D` as the remaining complement.
7. Under that choice, every `A ∪ B` label avoids all `C` prime factors, every pair in `B` is coprime, and every `D` label avoids the barrier primes `19,23,29`.
8. Therefore any partition of `{1,...,134}` into class label sets satisfying those obligations gives a prime labeling.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Preserve the successful sparse barrier set `B = {1,19,23,29}`.
- Abandon the old solve-stage heuristic "all `C` primes must lie above half the interval" and instead use the cleaner condition "all `C` primes lie above the largest barrier prime `29`."
- Only after fixing the full explicit witness, use one tiny checker to validate the class partition against the ring definition.
- Brief self-check after choosing the plan:
  - this remains reasoning-first because the witness is dictated by the support reduction and divisibility structure, not by search;
  - minimal code is justified only as post-construction witness verification.

## self_checks

- Statement lock:
  - the exact target is the feeder instance `Γ(Z_23 × Z_25)`;
  - the label interval length `134` matches the vertex count.
- Structural reduction:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the full graph again collapses to three arithmetic interfaces.
- Construction:
  - the barrier spill from `B` has size `13`;
  - the prime pool `(29,134]` has size `22`, exactly `|C|`;
  - the chosen `A` fillers `2,3,4,5,6,7,8` add no new conflict with `C`.
- Final witness:
  - `A`, `B`, and `C` are disjoint and have sizes `20,4,22`;
  - the remaining complement has size `88`, exactly `|D|`;
  - every nontrivial multiple of `19`, `23`, or `29` lies in `A`, not `D`;
  - every label in `A ∪ B` is coprime to every label in `C`.

## code_used

- Minimal code was used only after the reasoning and explicit class partition were fixed.
- A tiny local checker `check_witness.py` enumerates the `134` nonzero zero-divisors of `Z_23 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,134}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 134`
  - `edge_count = 886`
  - `edge_type_counts = {A-C: 440, B-B: 6, B-C: 88, B-D: 352}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131` on `C` in any order;
  - put the labels `1,19,23,29` on `B` in any order;
  - put the labels `2,3,4,5,6,7,8,38,46,57,58,69,76,87,92,95,114,115,116,133` on `A` in any order;
  - put the remaining `88` labels
    `9,10,11,12,13,14,15,16,17,18,20,21,22,24,25,26,27,28,30,32,33,34,35,36,39,40,42,44,45,48,49,50,51,52,54,55,56,60,62,63,64,65,66,68,70,72,74,75,77,78,80,81,82,84,85,86,88,90,91,93,94,96,98,99,100,102,104,105,106,108,110,111,112,117,118,119,120,121,122,123,124,125,126,128,129,130,132,134`
    on `D` in any order.
- Why this works:
  - `B-B` edges: `1,19,23,29` are pairwise coprime.
  - `A-C` and `B-C` edges: every label on `C` is a prime `> 29`, while every label on `A ∪ B` is either at most `29` or a multiple of `19`, `23`, or `29`; hence no `A ∪ B` label shares a prime factor with any `C` label.
  - `B-D` edges: every nontrivial multiple of `19`, `23`, and `29` up to `134` was deliberately placed in `A`, so no label in `D` is divisible by any nontrivial label on `B`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; the fixed barrier set `B = {1,19,23,29}`; and the cleaner rule that `C` only needs primes above the barrier threshold `29`, not necessarily above half the whole interval.
  - what part does not yet scale:
    the family still needs a quantified counting lemma proving simultaneously that
    1. there are at least `p - 1` primes in `(29,5p+19]`, and
    2. the total spill of nontrivial multiples of `19,23,29` inside `{1,...,5p+19}` still fits inside the fixed `20` slots of `A`.
  - what theorem slice is suggested:
    a barrier-threshold sufficient-condition theorem for `Γ(Z_p × Z_25)` using `B = {1,19,23,29}`, `A` as the barrier-multiple reservoir, and `C` chosen from primes greater than `29`.
  - what one or two next feeder instances would help most:
    `Γ(Z_29 × Z_25)` and `Γ(Z_31 × Z_25)`, because they are the next boundary cases for the proposed barrier-threshold slice:
    at `p = 29`, the count of primes in `(29,164]` is exactly `28 = p - 1`, and at `p = 31`, the barrier spill already rises to `19` of the `20` available `A` slots.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is materially closer to a paper-shaped claim because it suggests a cleaner family slice than the earlier half-interval spill formulation.

## family_affinity

- Family affinity is high.
- This feeder sits directly on the active `Γ(Z_p × Z_25)` campaign line and strengthens the live publication program more than a random exact win would.
- The main value is not only that `p = 23` survives, but that it survives via a cleaner structural arithmetic package than the one currently emphasized in the earlier exact feeders.

## generalization_signal

- Generalization signal is strong.
- At `p = 23`, the old "upper-half prime" viewpoint is no longer the natural invariant. The cleaner invariant is that `C` can be built from primes above the fixed barrier threshold `29`.
- This suggests a sharper campaign question:
  for which odd primes `p` do the two finite counts
  - `#{primes in (29,5p+19]}` and
  - `#{nontrivial multiples of 19,23,29 in [1,5p+19]}`
  jointly force a witness?
- That is a real theorem-slice direction, not merely another isolated label list.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. fix the sparse barrier set `B = {1,19,23,29}`;
  4. put every nontrivial multiple of `19`, `23`, and `29` into `A`;
  5. choose `C` from primes greater than `29`;
  6. fill the remaining `A` slots with labels not divisible by any chosen `C` prime;
  7. assign the residual complement to `D`.
- Relative to the earlier `p = 13,17,19` records, the reusable gain is conceptual:
  the proof surface is better phrased in terms of a fixed barrier threshold at `29` than in terms of a moving half-interval cutoff.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, `Γ(Z_p × Z_25)` is prime whenever the interval `{1,...,5p+19}` admits
  - `p - 1` primes greater than `29`, and
  - no more than `20` nontrivial multiples of `19`, `23`, and `29`,
  because then one may take
  - `B = {1,19,23,29}`,
  - `A` to be all those barrier multiples plus arbitrary safe fillers,
  - `C` to be any `p - 1` primes from `(29,5p+19]`,
  - `D` to be the remaining complement.
- The present feeder is the first clean instance where this barrier-threshold formulation is easier to state than the earlier repaired spill language.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on the four-class line is `p = 29`.
- Reason:
  it is the next odd prime after `23`, and it is an exact boundary case for the proposed slice because the interval `(29,164]` contains exactly `28 = p - 1` candidate `C` primes while the `A` reservoir still has only `3` free slots after absorbing the fixed barrier spill.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder with no bounded rediscovery audit in this pass and no Lean closure.
- It is publication-relevant because it exposes a cleaner candidate theorem slice than the one previously highlighted by the four-class campaign notes.
- The likely publishable unit is not the single `p = 23` witness itself, but a theorem or sharply delimited slice built around the fixed barrier threshold `29` together with explicit counting lemmas for the `C` prime pool and the `A` spill reservoir.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the now-stable `Γ(Z_p × Z_25)` support reduction.
- The arithmetic failure point would be a missed nontrivial multiple of `19`, `23`, or `29` left in `D`.
- Another arithmetic failure point would be accidentally putting into `A ∪ B` a label divisible by one of the chosen `C` primes.
- Publication-wise, the main weakness is that the new barrier-threshold slice is still an observed pattern here, not yet a proved all-`p` counting theorem.

## what_verify_should_check

- Recompute the `134` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `886` edges.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,134}`.
- Check coprimality on every actual edge from the ring graph.
- In the bounded rediscovery pass, audit not only the exact `p = 23` instance but also whether any existing sufficient-condition theorem for `Γ(Z_p × Z_25)` already implies the barrier-threshold slice suggested here.
- If verification passes, promote the clean `C = {primes > 29}` formulation into the family generalization dossier before any exact-instance Lean work.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact tuple `Γ(Z_23 × Z_25)`, ASCII variants such as `Z_23 x Z_25`, the broader family notation `Γ(Z_p × Z_(q^2))`, the canonical source itself, and a later-status check for follow-up closure.
- Exact-instance and alternate-notation searches did not reveal an earlier theorem, proposition, example, observation, or corollary settling this exact `p = 23, q = 5` case.
- The canonical source check again pointed to the 2025 Combinatorial Press paper `On prime labelings of zero-divisor graphs`. In that source, nearby solved cases include families such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))`, while the ambient family `Γ(Z_p × Z_(q^2))` is still presented as Conjecture `4.4`, not as a theorem implying `Γ(Z_23 × Z_25)`.
- The bounded later-status check did not produce a newer published closure of either the exact `p = 23, q = 5` instance or the full `Γ(Z_p × Z_(q^2))` line.
- Verdict for PASS 1: no rediscovery established.

## verify_faithfulness

- The claimed result matches the exact intended graph-theoretic statement: the full simple zero-divisor graph `Γ(Z_23 × Z_25)` on its `134` nonzero zero-divisors admits a prime labeling by `{1,...,134}`.
- There is no wrong-theorem drift to a support graph, quotient graph, or partial labeling. The support classes are used only as a reduction device for the exact graph.
- The classwise "any order" language is faithful here: labels may be permuted freely inside `A`, `C`, and `D` because those classes have uniform neighborhoods, while `B` is handled separately by the fact that its four labels are pairwise coprime on a `K_4`.

## verify_proof

- I recomputed the vertex partition directly from the ring definition and again recovered `|A| = 20`, `|B| = 4`, `|C| = 22`, and `|D| = 88`, for total `134` vertices.
- I independently recomputed the edge set and again obtained only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `440`, `6`, `88`, and `352`, for total `886` edges.
- Given that support graph, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly. The displayed `A`, `B`, and `C` sets are disjoint, cover the required class sizes, and leave exactly `88` labels for `D`. Direct gcd checks found no bad pair on `A-C`, `B-B`, `B-C`, or `B-D`.
- The key arithmetic sentence in the solve record is valid: every label in `A ∪ B` is either at most `29` or divisible by one of `19`, `23`, `29`, whereas every label in `C` is a prime strictly greater than `29`; hence no `C`-prime divides any label in `A ∪ B`.
- First incorrect step found: none.

## verify_adversarial

- I reran `artifacts/z23-z25-prime-zero-divisor-graph/check_witness.py`. It again reported `vertex_count = 134`, `edge_count = 886`, `edge_type_counts = {'A-C': 440, 'B-B': 6, 'B-C': 88, 'B-D': 352}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran independent checks outside the artifact checker to confirm:
  - the four class label sets are disjoint and cover exactly `{1,...,134}`;
  - the complement assigned to `D` has size `88`;
  - there is no hidden edge type beyond `A-C`, `B-B`, `B-C`, and `B-D`;
  - no nontrivial multiple of `19`, `23`, or `29` lands in `D`.
- I did not find a candidate counterexample edge, a mislabeled vertex, or a computational mismatch between the ring graph and the arithmetic witness.

## verify_theorem_worthiness

- This is still not a standalone theorem slice. On its own, it remains one verified feeder instance.
- It does, however, materially strengthen the live `Γ(Z_p × Z_25)` campaign because the witness closes with the cleaner barrier-threshold formulation `C = {primes > 29}` rather than the earlier repaired half-interval language.
- The structural part that scales is the four-class support reduction together with the fixed sparse barrier set `B = {1,19,23,29}` and the rule that `A` absorbs all nontrivial multiples of those barrier labels.
- The part that does not yet scale automatically is the quantified counting lemma: one still needs a family proof guaranteeing enough primes above `29` for `C` and enough room in the `20` `A`-slots for the barrier spill.
- The best honest publication status is therefore `SLICE_CANDIDATE`, not `PAPER_READY`, because this feeder points to a real theorem slice but does not itself prove the slice.
- The smallest next discriminator for the claimed template is `Γ(Z_29 × Z_25)`, the next odd-prime boundary case for the barrier-threshold package.

## verify_verdict

- `VERIFIED`
- No rediscovery was established, the claim matches the intended instance exactly, and the explicit witness survived skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- None. No conservative repair was needed.
