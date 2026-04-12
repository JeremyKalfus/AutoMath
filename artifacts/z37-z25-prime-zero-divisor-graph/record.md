# Solve Record: z37-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_37 × Z_25) prime?`
- Active slug: `z37-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_37 × Z_25)` admits a prime labeling, meaning a bijection from its `204` vertices to `{1,2,...,204}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_37 × Z_25`, not the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_37` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_37^×}`, size `36`.
  - `D = {(a,5t) : a ∈ Z_37^×, t ∈ {1,2,3,4}}`, size `144`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 37` and `bd = 0 mod 25`.
- Because `Z_37` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - once a classwise label set is chosen, labels may be assigned inside `A`, `C`, and `D` in any order because those classes have identical neighborhoods;
  - the four `B` vertices form a `K_4`, so any permutation of a pairwise-coprime `B` label set preserves the witness.
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
- Edge counts at `p = 37` are therefore forced:
  - `A-C = 20 · 36 = 720`;
  - `B-B = 6`;
  - `B-C = 4 · 36 = 144`;
  - `B-D = 4 · 144 = 576`.
- Total predicted edge count: `720 + 6 + 144 + 576 = 1446`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Brief self-check after Approach A:
  - vertex count check: `20 + 4 + 36 + 144 = 204`;
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`, so the old `p = 37` campaign obstruction is not graph-theoretic by itself;
  - any failure at `p = 37` must come from arithmetic label allocation, not from a new edge family.

## approach_B

- Construction / extremal route by replacing the failing small barrier with a larger sparse barrier.
- The family sidecar already shows that the old fixed wrapper `B = {1,19,23,29}` cannot work here:
  - in `{1,...,204}`, the nontrivial multiples of `19`, `23`, and `29` occupy `22` labels;
  - but `A` has only `20` slots.
- That is only a template obstruction. It suggests moving the `B` clique to larger pairwise-coprime labels so its spill shrinks.
- A clean replacement is
  `B = {1,43,47,53}`.
- Its nontrivial multiples up to `204` are exactly:
  - for `43`: `86,129,172`;
  - for `47`: `94,141,188`;
  - for `53`: `106,159`.
- So this redesigned barrier produces only `8` forced spill labels, comfortably within the `20` slots of `A`.
- To keep `A-C` and `B-C` coprime, choose `C` from primes avoiding the prime factors used by `A ∪ B`.
- One explicit `36`-prime block is
  `C = {11,13,17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191}`.
- Put into `A` the `8` forced barrier multiples together with `12` smooth fillers whose prime factors lie only in `{2,3,5,7}`:
  `A = {2,3,4,5,6,7,8,9,10,12,14,15,86,94,106,129,141,159,172,188}`.
- Why this works structurally:
  - every label in `A ∪ B` has all prime factors in `{2,3,5,7,43,47,53}`;
  - every label in `C` is a prime outside that set;
  - therefore every `A-C` and `B-C` edge is automatically coprime;
  - every nontrivial multiple of `43`, `47`, or `53` has been forced into `A`, so `D` is automatically coprime to `B`.
- One explicit classwise partition suggested by this logic is:
  - `B = {1,43,47,53}`;
  - `C = {11,13,17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191}`;
  - `A = {2,3,4,5,6,7,8,9,10,12,14,15,86,94,106,129,141,159,172,188}`;
  - `D` gets the remaining `144` labels.
- Brief self-check after Approach B:
  - the redesigned barrier spill is `8`, so `A` still has `12` free filler slots;
  - the `C` block has exactly `36` labels, matching `|C|`;
  - no label in `A ∪ B` is divisible by any prime in the chosen `C` block.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,36,144`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
4. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. A sufficient arithmetic sublemma for this instance is:
   if `B = {1,43,47,53}`, every nontrivial multiple of `43`, `47`, or `53` in `{1,...,204}` lies in `A`, and every label in `A ∪ B` has prime factors only in `{2,3,5,7,43,47,53}` while every label in `C` is a prime outside that set, then all classwise coprimality obligations hold.
7. Therefore any partition of `{1,...,204}` into class label sets satisfying those obligations gives a prime labeling.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Treat the old `B = {1,19,23,29}` count failure at `p = 37` as a wrapper failure, not as evidence of graph-level non-primality.
- Replace the small barrier with a larger sparse barrier `B = {1,43,47,53}` whose spill fits inside `A`.
- Build `C` from primes deliberately disjoint from the prime-factor palette of `A ∪ B`.
- Use one tiny checker only after the full classwise partition is fixed.

## self_checks

- Statement lock:
  - the exact target is the feeder instance `Γ(Z_37 × Z_25)`;
  - the label interval length `204` matches the vertex count.
- Structural reduction:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the family sidecar's `p = 37` obstruction is therefore only an obstruction to one fixed wrapper.
- Barrier redesign:
  - the old fixed barrier spills `22` labels and therefore cannot fit in `A`;
  - the new barrier `43,47,53` spills only `8` labels.
- Prime block:
  - the chosen `C` block has exactly `36` primes;
  - every prime in `C` avoids the factor palette `{2,3,5,7,43,47,53}`.
- Final witness shape:
  - `A`, `B`, and `C` are disjoint and have sizes `20,4,36`;
  - the remaining complement has size `144`, exactly `|D|`;
  - every nontrivial multiple of `43`, `47`, or `53` lies in `A`, not in `D`.

## code_used

- A tiny local checker `check_witness.py` was used only after the reasoning and explicit class partition were fixed.
- The checker enumerates the `204` nonzero zero-divisors of `Z_37 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,204}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 204`
  - `edge_count = 1446`
  - `edge_type_counts = {A-C: 720, B-B: 6, B-C: 144, B-D: 576}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `1,43,47,53` on `B` in any order;
  - put the labels `11,13,17,19,23,29,31,37,41,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191` on `C` in any order;
  - put the labels `2,3,4,5,6,7,8,9,10,12,14,15,86,94,106,129,141,159,172,188` on `A` in any order;
  - put the remaining `144` labels on `D` in any order.
- Why this works:
  - `B-B` edges: `1,43,47,53` are pairwise coprime.
  - `A-C` and `B-C` edges: every label on `A ∪ B` has prime factors only in `{2,3,5,7,43,47,53}`, while every label on `C` is a prime outside that set.
  - `B-D` edges: every nontrivial multiple of `43`, `47`, and `53` up to `204` was deliberately placed in `A`, so no label in `D` is divisible by a nontrivial label on `B`.
  - there are no other edges by the support decomposition.
- Minimal-code confirmation:
  - the local checker recovered `204` vertices and `1446` edges with edge-type counts `A-C = 720`, `B-B = 6`, `B-C = 144`, `B-D = 576`;
  - it confirmed bijectivity onto `{1,...,204}` and found no edge with `gcd > 1`.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; the idea of choosing `B` as a large sparse pairwise-coprime barrier; and the classwise factor-separation rule “`A ∪ B` uses a small prime-factor palette, `C` uses disjoint primes.”
  - what part does not yet scale:
    the exact barrier choice `43,47,53`, the exact prime count for `C`, and the filler-count argument for `A` are still finite-instance arithmetic bookkeeping rather than a proved general lemma.
  - what theorem slice is suggested:
    a second-generation sufficient-condition slice for `Γ(Z_p × Z_25)` in which `B = {1,q_1,q_2,q_3}` is a large pairwise-coprime barrier with small multiple spill, `A` absorbs those multiples plus smooth fillers, and `C` is chosen from primes disjoint from the factor palette of `A ∪ B`.
  - what one or two next feeder instances would help most:
    `Γ(Z_41 × Z_25)` as the immediate next test of whether the same large-barrier template survives one more prime, and `Γ(Z_43 × Z_25)` as the next pressure point because the barrier prime `43` then sits exactly at the parameter boundary.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is materially closer to a paper-shaped claim because it shows the first fixed-wrapper obstruction at `p = 37` is not a graph-level breakpoint and instead points to a new family template.

## family_affinity

- Family affinity is high.
- This feeder sits exactly at the campaign's advertised first fixed-wrapper obstruction on the four-class `Γ(Z_p × Z_25)` line.
- The solve package matters because it distinguishes “the old wrapper breaks” from “the graph stops being prime,” and presently supports the former rather than the latter.

## generalization_signal

- Generalization signal is strong.
- The main new signal is not another small repair to the old `C` block. It is a different structural allocation:
  - move the `B` clique to larger pairwise-coprime labels;
  - force their few multiples into `A`;
  - keep `A`'s filler labels smooth;
  - let `C` use a large block of primes disjoint from that small factor palette.
- At `p = 37`, this replaces the campaign's old “threshold `29` barrier” viewpoint with a more flexible “large sparse barrier” viewpoint.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. choose a pairwise-coprime barrier set `B = {1,q_1,q_2,q_3}` whose nontrivial multiples in `{1,...,5p+19}` fit inside the `20` slots of `A`;
  4. place all those barrier multiples into `A`;
  5. fill the remaining `A` slots with labels using only a small excluded prime-factor palette;
  6. choose `C` as `p - 1` primes disjoint from that palette and from `{q_1,q_2,q_3}`;
  7. assign the residual complement to `D`.
- Relative to the earlier `p = 23,29,31` fixed-threshold story, the reusable gain is conceptual:
  the barrier itself can move upward to shrink spill, rather than staying frozen at `19,23,29`.

## candidate_theorem_slice

- Candidate slice:
  let `N = 5p + 19`.
  If there exist pairwise-coprime integers `q_1,q_2,q_3` in `{2,...,N}` such that
  - the nontrivial multiples of `q_1,q_2,q_3` in `{1,...,N}` occupy at most `20` labels, and
  - `{1,...,N}` contains at least `p - 1` primes disjoint from the prime-factor palette used by `A ∪ {1,q_1,q_2,q_3}`,
  then taking `B = {1,q_1,q_2,q_3}`, `A` as the barrier-multiple reservoir plus safe fillers, `C` from those primes, and `D` as the complement yields a prime labeling of `Γ(Z_p × Z_25)`.
- The present feeder suggests `q_1,q_2,q_3 = 43,47,53` as the first concrete test case for this larger-barrier slice.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on the four-class line is `p = 41`.
- Reason:
  the present `p = 37` construction no longer uses the old fixed wrapper, so the immediate campaign question is whether the same redesigned large-barrier template persists at the next odd prime.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder with no bounded rediscovery audit in this pass and no Lean closure.
- It is publication-relevant because it changes the meaning of the `p = 37` frontier:
  the first fixed-wrapper obstruction does not currently look like a graph-level obstruction.
- The likely publishable unit is not the single `p = 37` witness itself, but a theorem slice or smallest-breakpoint package showing when the old barrier must be replaced and when a larger sparse barrier still succeeds.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the now-stable `Γ(Z_p × Z_25)` support reduction.
- The arithmetic failure point would be a missed nontrivial multiple of `43`, `47`, or `53` left in `D`.
- Another arithmetic failure point would be accidentally placing into `A ∪ B` a label divisible by one of the chosen `C` primes.
- Publication-wise, the main weakness is that the new large-barrier template is still an observed construction here, not yet a proved family lemma.

## what_verify_should_check

- Recompute the `204` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `1446` edges.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,204}`.
- Check that every nontrivial multiple of `43`, `47`, and `53` up to `204` lies in `A ∪ B`.
- Check coprimality on every actual edge from the ring graph.
- In the bounded rediscovery pass, audit not only the exact `p = 37` instance but also whether any existing sufficient-condition theorem already implies this larger-barrier slice.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact instance `Γ(Z_37 × Z_25)`, ASCII and reordered variants such as `Z_37 x Z_25` and `Z_25 x Z_37`, the broader family notation `Γ(Z_p × Z_(q^2))`, and the most relevant recent source I found on prime labelings of zero-divisor graphs.
- Exact-instance and alternate-notation searches did not reveal an earlier theorem, proposition, example, observation, or corollary settling this exact `p = 37, q = 5` case.
- The canonical source check again pointed to the 2025 Combinatorial Press paper `On Prime Labelings of Zero-Divisor Graphs`. Within the bounded pass, that source did not exhibit `Γ(Z_37 × Z_25)` as a solved example, and its surrounding family discussion treats `Γ(Z_p × Z_(q^2))` as conjectural rather than proved.
- A bounded status-style follow-up within the same pass did not surface a newer published closure of either the exact `p = 37, q = 5` instance or the full `Γ(Z_p × Z_(q^2))` family.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The solve record remains faithful to the exact intended feeder statement: the full simple zero-divisor graph `Γ(Z_37 × Z_25)` on its `204` nonzero zero-divisors admits a prime labeling by `{1,...,204}`.
- The support classes `A,B,C,D` are used only as a reduction device for the exact graph. The claimed output is still a full labeling of all vertices, not merely a support-graph witness or a weaker sufficient condition detached from the instance.
- The record does not drift to a nearby statement. The ring, vertex set, adjacency rule, and label interval all match the selected dossier exactly.
- No wrong-theorem drift, quantifier drift, weakened proxy claim, or prose/computation mismatch was found.

## verify_proof

- I recomputed the vertex partition directly from the ring definition and again recovered `|A| = 20`, `|B| = 4`, `|C| = 36`, and `|D| = 144`, totaling `204`.
- I independently recomputed adjacency and again obtained only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `720`, `6`, `144`, and `576`, for total `1446` edges.
- Given that support graph, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly. The displayed `A`, `B`, and `C` sets are disjoint, have sizes `20,4,36`, and leave exactly `144` labels for `D`.
- The key barrier sentence is correct: the only nontrivial multiples of `43`, `47`, and `53` up to `204` are `86,129,172`, `94,141,188`, and `106,159`, and all eight were deliberately placed in `A`, so no `D` label is divisible by a nontrivial label in `B`.
- The factor-separation sentence is also correct: every label in `A ∪ B` has all prime factors in `{2,3,5,7,43,47,53}`, while every label in `C` is a prime outside that set, so every `A-C` and `B-C` edge is coprime.
- First incorrect step found: none.

## verify_adversarial

- I reran `artifacts/z37-z25-prime-zero-divisor-graph/check_witness.py`. It again reported `vertex_count = 204`, `edge_count = 1446`, `edge_type_counts = {'A-C': 720, 'B-B': 6, 'B-C': 144, 'B-D': 576}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran an independent arithmetic check outside the shipped checker to confirm:
  - the four class label sets are disjoint and cover exactly `{1,...,204}`;
  - the complement assigned to `D` has size `144`;
  - there is no hidden edge type beyond `A-C`, `B-B`, `B-C`, and `B-D`;
  - every nontrivial multiple of `43`, `47`, and `53` up to `204` lies in `A`, not in `D`;
  - every required pair on `A-C`, `B-B`, `B-C`, and `B-D` has gcd `1`.
- I did not find a broken edge, a missed divisibility obstruction, or a computation/prose mismatch that breaks the candidate witness.

## verify_theorem_worthiness

- This feeder suggests a real theorem slice rather than a bare isolated instance. The campaign-level gain is that the old fixed barrier `B = {1,19,23,29}` appears to fail at `p = 37` only as a wrapper by spill count, while a moved sparse barrier `B = {1,43,47,53}` still closes the exact graph.
- What clearly scales:
  - the four-class support reduction for `Γ(Z_p × Z_25)`;
  - the reduction to the interfaces `A-C`, `B-B`, `B-C`, and `B-D`;
  - the movable sparse-barrier idea for `B`;
  - the rule that `A` absorbs all nontrivial barrier multiples and `C` is chosen from primes disjoint from the factor palette of `A ∪ B`.
- What does not yet scale automatically:
  - the specific barrier choice `43,47,53`;
  - the supply count guaranteeing `p - 1` usable primes for `C`;
  - the general counting lemma showing when the barrier spill still fits in the `20` available `A` slots.
- The best honest publication status is therefore `SLICE_CANDIDATE`, not merely `INSTANCE_ONLY`: this verified feeder materially changes the family picture even though it does not yet prove the slice.
- The smallest next parameter shift that most tests the claimed template is `Γ(Z_41 × Z_25)`. The next pressure point after that is `Γ(Z_43 × Z_25)`, where one of the new barrier primes meets the parameter boundary.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- No rediscovery was established, the claim matches the intended instance exactly, and the explicit witness survived skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.
- `lean_ready = false`

## minimal_repair_if_any

- No repair to the witness was needed.
- The only conservative repair is classificatory: keep the artifact at `classification = CANDIDATE`, raise `publication_status` to `SLICE_CANDIDATE`, and defer Lean on the isolated instance until the movable-barrier slice is absorbed by `generalize`.
