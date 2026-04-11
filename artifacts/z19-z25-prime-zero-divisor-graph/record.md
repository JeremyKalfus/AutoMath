# Solve Record: z19-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_19 × Z_25) prime?`
- Active slug: `z19-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_19 × Z_25)` admits a prime labeling, meaning a bijection from its `114` vertices to `{1,2,...,114}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_19 × Z_25`, not the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_19` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_19^×}`, size `18`.
  - `D = {(a,5t) : a ∈ Z_19^×, t ∈ {1,2,3,4}}`, size `72`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 19` and `bd = 0 mod 25`.
- Because `Z_19` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - once a classwise label set is chosen, labels may be assigned inside `A`, `C`, and `D` in any order because those classes have identical neighborhoods; labels may also be permuted inside `B` because `B` is a `K_4` and the chosen `B` labels are pairwise coprime.
- Ambiguities or missing definitions:
  - none that block the solve; the campaign notation and the earlier `F25` feeders already fix the support classes and graph convention.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is the same as in the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 19` are therefore forced:
  - `A-C = 20 · 18 = 360`;
  - `B-B = 6`;
  - `B-C = 4 · 18 = 72`;
  - `B-D = 4 · 72 = 288`.
- Total predicted edge count: `360 + 6 + 72 + 288 = 726`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Self-check after Approach A:
  - vertex count check: `20 + 4 + 18 + 72 = 114`;
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`, so no new graph-theoretic obstruction appears at `p = 19`.

## approach_B

- Construction / extremal route by continuing the refined bounded-spill `C` block from `p = 13` and `p = 17`.
- The pure upper-half-prime rule is still too small:
  - `|C| = 18`;
  - the interval `[58,114]` contains only the `14` primes
    `59,61,67,71,73,79,83,89,97,101,103,107,109,113`.
- So at least four below-half primes are needed again.
- The same spill quartet from `p = 17` still fits cleanly:
  - use `37,41,43,47`;
  - their nontrivial multiples in `{1,...,114}` are
    `74 = 2·37`, `111 = 3·37`, `82 = 2·41`, `86 = 2·43`, and `94 = 2·47`.
- Hence a candidate `C` block is
  `C = {37,41,43,47,59,61,67,71,73,79,83,89,97,101,103,107,109,113}`.
- Keep the stable sparse barrier set on `B`:
  `B = {1,19,23,29}`.
- Its nontrivial multiples up to `114` are:
  - for `19`: `38,57,76,95,114`;
  - for `23`: `46,69,92`;
  - for `29`: `58,87`.
- Those ten barrier-spill labels still fit inside the fixed `20` slots of `A`.
- One explicit classwise partition suggested by this reasoning is:
  - `C = {37,41,43,47,59,61,67,71,73,79,83,89,97,101,103,107,109,113}`;
  - `B = {1,19,23,29}`;
  - `A = {2,3,4,5,6,7,8,9,10,11,38,46,57,58,69,76,87,92,95,114}`;
  - `D` gets the remaining `72` labels.
- Self-check after Approach B:
  - the upper-half-only `C` subtemplate is short by exactly `4`, so the spill is structurally required;
  - the chosen four spill primes create only five extra forbidden labels for `A ∪ B`, namely `74,82,86,94,111`;
  - the barrier spill from `B` has size `10`, still leaving enough room in `A`;
  - none of the forced `A` labels is divisible by any chosen `C` prime.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,18,72`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. A sufficient arithmetic sublemma for this instance is:
   if `C` is labeled by primes whose nontrivial multiples in `{1,...,114}` all lie in `D`, and if the nontrivial multiples of the barrier set `B` all lie in `A`, then the classwise coprimality obligations are satisfied.
7. Therefore any partition of `{1,...,114}` into class label sets satisfying those obligations gives a prime labeling.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Keep the already successful sparse barrier set `B = {1,19,23,29}`.
- Extend the refined small-spill `C` strategy by reusing the same four below-half spill primes as at `p = 17`.
- Only after fixing an explicit witness, use one tiny checker to validate the class partition against the ring definition.
- Self-check after choosing the plan:
  - this remains reasoning-first because the witness is dictated by the support reduction and divisibility bookkeeping, not by search;
  - minimal code is justified only as post-construction witness verification.

## self_checks

- Statement lock:
  - the exact target is the feeder instance `Γ(Z_19 × Z_25)`;
  - the label interval length `114` matches the vertex count.
- Structural reduction:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the full graph again collapses to three arithmetic interfaces.
- Construction:
  - `C` needs exactly four spill primes below the half-interval cutoff;
  - their only extra forbidden labels are `74,82,86,94,111`;
  - the fixed `B` barrier still has spill size only `10`.
- Final witness:
  - `A`, `B`, and `C` are disjoint and have sizes `20,4,18`;
  - the remaining complement has size `72`, exactly `|D|`;
  - every nontrivial multiple of `19`, `23`, or `29` lies in `A`, not `D`;
  - every nontrivial multiple of a `C` prime lies in `D`, not in `A ∪ B`.

## code_used

- Minimal code was used only after the reasoning and explicit class partition were fixed.
- A tiny local checker `check_witness.py` enumerates the `114` nonzero zero-divisors of `Z_19 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,114}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 114`
  - `edge_count = 726`
  - `edge_type_counts = {A-C: 360, B-B: 6, B-C: 72, B-D: 288}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `37,41,43,47,59,61,67,71,73,79,83,89,97,101,103,107,109,113` on `C` in any order;
  - put the labels `1,19,23,29` on `B` in any order;
  - put the labels `2,3,4,5,6,7,8,9,10,11,38,46,57,58,69,76,87,92,95,114` on `A` in any order;
  - put the remaining `72` labels
    `12,13,14,15,16,17,18,20,21,22,24,25,26,27,28,30,31,32,33,34,35,36,39,40,42,44,45,48,49,50,51,52,53,54,55,56,60,62,63,64,65,66,68,70,72,74,75,77,78,80,81,82,84,85,86,88,90,91,93,94,96,98,99,100,102,104,105,106,108,110,111,112`
    on `D` in any order.
- Why this works:
  - `B-B` edges: `1,19,23,29` are pairwise coprime.
  - `A-C` and `B-C` edges: every label on `C` is prime, and the only extra forbidden labels below `114` are `74,82,86,94,111`; none is used on `A ∪ B`.
  - `B-D` edges: every nontrivial multiple of `19`, `23`, and `29` up to `114` is one of `38,46,57,58,69,76,87,92,95,114`, and all ten were deliberately placed in `A`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; the reuse of the sparse barrier set `B = {1,19,23,29}`; and the bounded-spill principle that below-half `C` primes are allowed when their nontrivial multiples are pushed into `D`.
  - what part does not yet scale:
    the exact count of admissible spill primes and the exact prime choices still depend on interval arithmetic in `{1,...,5p+19}`;
    there is still no closed family lemma proving that this spill budget always exists.
  - what theorem slice is suggested:
    a refined sufficient-condition theorem for `Γ(Z_p × Z_25)` allowing a bounded spill subset of below-half primes in `C`, provided all resulting nontrivial multiples stay out of `A ∪ B` and the fixed `B` barrier spill still fits inside `A`.
  - what one or two next feeder instances would help most:
    `Γ(Z_23 × Z_25)` as the next four-class arithmetic stress test, and `Γ(Z_17 × Z_17 × Z_2)` as the matching campaign discriminator on the parallel six-class line.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still instance-level evidence, but it is closer to a paper-shaped claim because the same refined four-spill `C` pattern now survives two consecutive post-`13` feeders rather than a single repaired case.

## family_affinity

- Family affinity is high.
- This feeder sits directly on the active `Γ(Z_p × Z_25)` campaign line and tests the still-open quantified bounded-spill arithmetic package rather than a one-off exact trick.
- The solve package strengthens the publication program because it shows the refined `C` strategy persists beyond the verified `p = 17` checkpoint.

## generalization_signal

- Generalization signal is strong but still arithmetic rather than theorem-level.
- At `p = 19`, the same sparse barrier set on `B` survives unchanged, and the same four spill primes `37,41,43,47` still suffice for `C`.
- The new phenomenon relative to `p = 17` is that `37` now contributes a second nontrivial multiple `111`, yet the witness still survives because those extra `C` multiples only need to stay out of `A ∪ B`, not out of the whole interval.
- The honest family signal is therefore:
  a small fixed spill set in `C` may continue to work even after some spill primes acquire more than one nontrivial multiple inside the label interval.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. choose a sparse pairwise-coprime barrier set on `B`;
  4. choose `p - 1` prime labels for `C`, allowing a bounded spill subset below half the interval;
  5. place every nontrivial multiple of the barrier labels into `A`;
  6. place every nontrivial multiple of a spill prime from `C` into `D`;
  7. assign the remaining complement to `D`.
- Relative to `p = 17`, the reusable gain is that the same four-spill pattern survives even when one spill prime contributes a third multiple inside the interval.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, `Γ(Z_p × Z_25)` is prime whenever `{1,...,5p+19}` admits
  - a four-element pairwise-coprime barrier set `B` whose nontrivial multiples occupy at most `20` labels;
  - a prime block `C` of size `p - 1` in which a bounded spill subset may lie below half the interval, provided all nontrivial multiples of `C` stay out of `A ∪ B`;
  - an `A` reservoir of size `20` large enough to absorb the full barrier spill from `B`.
- The present feeder suggests the theorem statement should not insist that each spill prime in `C` have only one nontrivial multiple in the interval.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on the four-class line is `p = 23`.
- Reason:
  `p = 19` still survives with the same four spill primes and the same barrier set, so the next honest discriminator is whether the spill budget remains stable once the interval expands to `{1,...,134}`.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder, with no rediscovery audit in this pass and no Lean closure.
- It is publication-relevant because it sharpens the family claim from
  “the `p = 17` four-spill continuation works”
  to
  “the same refined four-spill pattern also survives at `p = 19`, even after one spill prime acquires an additional nontrivial multiple.”
- The likely publishable unit is still a quantified bounded-spill theorem or a smallest-breakpoint theorem on the family line, not this single instance by itself.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the now-stable `F25` ring bridge.
- The arithmetic failure point would be a missed nontrivial multiple of `19`, `23`, or `29` left in `D`.
- Another arithmetic failure point would be an overlooked multiple of `37`, `41`, `43`, or `47` accidentally placed in `A ∪ B`.
- Publication-wise, the main weakness is that the spill-budget argument is still finite-instance bookkeeping rather than a proven parameterized counting lemma.

## what_verify_should_check

- Recompute the `114` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `726` edges.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,114}`.
- Check coprimality on every actual edge from the ring graph.
- Audit whether any existing sufficient-condition theorem for `Γ(Z_p × Z_25)` already implies this `p = 19` case.
- If verification passes, treat this as a strong feeder for generalization before any exact-instance Lean work.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact tuple `Γ(Z_19 × Z_25)`, ASCII variants such as `Z_19 x Z_25`, the family notation `Γ(Z_p × Z_(q^2))`, the canonical 2025 source on prime labelings of zero-divisor graphs, and a same-source theorem / conjecture check.
- Exact-instance and alternate-notation searches did not reveal an earlier theorem, proposition, example, observation, or corollary settling this exact `p = 19, q = 5` case within budget.
- The canonical source check was the paper `On prime labelings of zero-divisor graphs` from Combinatorial Press, published online on 2025-11-21. Inside that source, the nearby solved families I recovered were cases such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))`, while the ambient family `Γ(Z_p × Z_(q^2))` was still left open as Conjecture `4.4` rather than closed by a theorem implying `Γ(Z_19 × Z_25)`.
- Verdict for PASS 1: no rediscovery established within the bounded audit.

## verify_faithfulness

- The solve record is aimed at the exact intended statement: existence of a prime labeling for the full simple zero-divisor graph `Γ(Z_19 × Z_25)` on the `114` nonzero zero-divisors, with labels bijectively covering `{1,...,114}`.
- There is no wrong-theorem drift to a support graph, induced subgraph, or partial labeling. The support classes are only used as a reduction device for the exact graph.
- One sentence in the solve record needed tightening: the four `B` vertices do not literally have identical neighborhoods in the simple graph, because each misses itself inside the `B` clique. That does not change the claim, since any permutation of the chosen `B` labels still preserves the witness exactly when those four labels are pairwise coprime.
- With that wording repair, the claimed result matches the intended instance exactly.

## verify_proof

- I recomputed the vertex partition directly from the ring definition and recovered `|A| = 20`, `|B| = 4`, `|C| = 18`, and `|D| = 72`, for total `114` vertices.
- I independently recomputed the exact edge set and again obtained only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `360`, `6`, `72`, and `288`, for total `726` edges.
- Given that support graph, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly. No nontrivial multiple of any `C`-prime lands in `A ∪ B`, and every nontrivial multiple up to `114` of `19`, `23`, or `29` lands in `A`, not `D`.
- First incorrect step found: none after the neighborhood wording repair above. The proof package is still instance-level arithmetic bookkeeping, but the witness argument itself is correct.

## verify_adversarial

- I reran `artifacts/z19-z25-prime-zero-divisor-graph/check_witness.py`. It again reported `vertex_count = 114`, `edge_count = 726`, `edge_type_counts = {'A-C': 360, 'B-B': 6, 'B-C': 72, 'B-D': 288}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran independent checks outside the artifact checker to confirm:
  - the four class label sets are disjoint and cover exactly `{1,...,114}`;
  - the only edge types are `A-C`, `B-B`, `B-C`, and `B-D`;
  - each of `A`, `C`, and `D` really does have uniform neighborhoods, while `B` is instead a clique whose labels must merely stay pairwise coprime;
  - direct gcd checks on all required interfaces found no bad pair.
- I did not find a hidden edge type, a mislabeled vertex, or a divisibility obstruction breaking the witness.

## verify_theorem_worthiness

- This remains an instance result, not a theorem slice by itself. The structural part that scales is the four-class support reduction together with the fixed sparse barrier set `B = {1,19,23,29}`.
- The part that does not yet scale automatically is the finite arithmetic supply argument for the `C` block. The proof still hand-picks the spill primes `37,41,43,47` rather than deriving a quantified bounded-spill lemma.
- Relative to the verified `p = 17` feeder, this does strengthen the family campaign: the same four-spill pattern survives one more step on the `Γ(Z_p × Z_25)` line even though `37` now contributes two nontrivial multiples, `74` and `111`, inside the interval.
- The best honest publication status for this artifact is therefore `SLICE_CANDIDATE`, not `PAPER_READY`, because it is still only feeder evidence but it does point to a real family theorem slice.
- The smallest next discriminator for the claimed template is `Γ(Z_23 × Z_25)`, which tests whether the same bounded-spill arithmetic still survives once the interval expands from `{1,...,114}` to `{1,...,134}`.

## verify_verdict

- `VERIFIED`
- No rediscovery was established in the bounded prior-art pass, the claim matches the intended instance after a tiny wording repair, and the explicit witness survived independent skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- Repaired one sentence in the solve record: only `A`, `C`, and `D` have identical neighborhoods; `B` is handled instead by the fact that it is a `K_4` with pairwise-coprime labels.
