# Solve Record: z11-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_11 × Z_25) prime?`
- Active slug: `z11-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_11 × Z_25)` admits a prime labeling, meaning a bijection from its `74` vertices to `{1,2,...,74}` such that adjacent vertices receive coprime labels.
- This solve pass is locked to the exact feeder instance `Z_11 × Z_25`, not the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_11` and `b ∈ Z_25`.
- A nonzero zero-divisor in `Z_11 × Z_25` is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_11^×}`, size `10`.
  - `D = {(a,5t) : a ∈ Z_11^×, t ∈ {1,2,3,4}}`, size `40`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 11` and `bd = 0 mod 25`.
- Because `Z_11` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - once a classwise label set is chosen, labels may be assigned to vertices inside each class in any order because vertices in the same class have the same neighborhood.

## approach_A

Structural / invariant approach through the support graph.

- If `x,y ∈ A`, then their second coordinates are units mod `25`, so `xy` cannot have second coordinate `0`; hence there are no `A-A` edges.
- If `x ∈ A` and `y ∈ C`, then `0 * a = 0 mod 11` and `u * 0 = 0 mod 25`, so `A-C` is complete bipartite.
- If `x ∈ A` and `y ∈ B` or `D`, then the second-coordinate product is `u * 5t`, nonzero mod `25`, so there are no `A-B` or `A-D` edges.
- If `x,y ∈ B`, then both first coordinates are `0` and both second coordinates are nonzero multiples of `5`, so `B` induces `K_4`.
- If `x ∈ B` and `y ∈ C`, then `(0,5t)(a,0) = (0,0)`, so `B-C` is complete bipartite.
- If `x ∈ B` and `y ∈ D`, then again the first-coordinate product is `0`, while `5t * 5s = 0 mod 25`, so `B-D` is complete bipartite.
- If `x,y ∈ C`, or `x ∈ C` and `y ∈ D`, or `x,y ∈ D`, then both first coordinates are nonzero in `Z_11`, so their product is nonzero mod `11`; hence there are no such edges.

Therefore the only edge types are:

- `A-C`, with `20 * 10 = 200` edges.
- `B-B`, with `binom(4,2) = 6` edges.
- `B-C`, with `4 * 10 = 40` edges.
- `B-D`, with `4 * 40 = 160` edges.

This gives total edge count `200 + 6 + 40 + 160 = 406`, and reduces the labeling problem to three coprimality interfaces plus one clique condition.

Self-check after Approach A:

- Vertex count check: `20 + 4 + 10 + 40 = 74`, matching the instance size.
- Structural check: the support graph is exactly the campaign template `A-C`, `B-B`, `B-C`, `B-D`, and nothing else.

## approach_B

Construction / extremal / contradiction approach by sparse forbidden sets.

- Every vertex of `C` is adjacent to every vertex of `A ∪ B`, so the labels on `C` should create as few exclusions as possible on the `24` labels used there.
- Choose ten large primes for `C`:
  `37,41,43,47,53,59,61,67,71,73`.
- For the nine primes strictly larger than `37`, the only multiples in `{1,...,74}` are the primes themselves. For `37`, the only multiples are `37` and `74`.
- So any label set used on `A ∪ B` only has to avoid
  `{37,41,43,47,53,59,61,67,71,73,74}`.
- Next, `B` is a `4`-clique and is also adjacent to all of `D`, so the labels on `B` must be pairwise coprime and should forbid only a small set of multiples in `D`.
- Choose
  `B = {1,19,23,29}`.
- These labels are pairwise coprime. Their nontrivial multiples in `{1,...,74}` are:
  - for `19`: `38,57`;
  - for `23`: `46,69`;
  - for `29`: `58`.
- Therefore `D` only needs to avoid the five labels
  `{38,46,57,58,69}` beyond the `B` labels themselves.
- Since `A` has `20` slots and only needs to be coprime to the `C` labels, `A` can absorb those five obstructing multiples together with fifteen harmless labels.

One explicit classwise partition suggested by this logic is:

- `C = {37,41,43,47,53,59,61,67,71,73}`.
- `B = {1,19,23,29}`.
- `A = {2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,38,46,57,58,69}`.
- `D` gets the remaining `40` labels.

Self-check after Approach B:

- `B`-clique check: `1,19,23,29` are pairwise coprime.
- `C`-interface check: no label used on `A ∪ B` lies in `{37,41,43,47,53,59,61,67,71,73,74}`.
- `D`-interface check: if `A` absorbs `38,46,57,58,69`, then the complement avoids every nontrivial multiple of `19,23,29` up to `74`.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,10,40`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`, with no other edges.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. Therefore any partition of `{1,...,74}` into class label sets satisfying those three arithmetic obligations is a prime labeling.

## chosen_plan

- Use Approach A to lock the support graph exactly.
- Use Approach B to construct an explicit classwise labeling with tiny forbidden sets.
- Do not introduce search or optimization: the arithmetic constraints are sparse enough to resolve directly.
- After the full witness is written down, use one tiny checker only to validate the explicit labeling against the ring definition.

Self-check after chosen plan:

- This remains reasoning-first: the witness comes from the support decomposition and sparse-multiple arithmetic, not from brute force.
- Minimal code, if any, is justified only as witness verification after the construction is fixed.

## self_checks

- Statement-lock check: the target remains the exact feeder instance `Γ(Z_11 × Z_25)`.
- Counting check: the class decomposition forces `74` vertices and predicts `406` edges.
- Interface check: the argument only needs four obligations, namely `A-C`, `B-C`, `B-B`, and `B-D`.
- Arithmetic check: the key economy is that `C` consumes ten mostly singleton prime labels, while `B` forbids only five extra labels from `D`.
- Conservatism check: even if the witness survives direct checking, solve should still classify this as `CANDIDATE`, not `EXACT`, because Lean is off.

## code_used

- A tiny local witness checker was used only after the reasoning and explicit class partition were fixed.
- The checker enumerates the `74` nonzero zero-divisors of `Z_11 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,74}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 74`
  - `edge_count = 406`
  - `edge_type_counts = {A-C: 200, B-B: 6, B-C: 40, B-D: 160}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

Current best solve-stage candidate:

- Put the labels `37,41,43,47,53,59,61,67,71,73` on `C` in any order.
- Put the labels `1,19,23,29` on `B` in any order.
- Put the labels `2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,38,46,57,58,69` on `A` in any order.
- Put the remaining `40` labels
  `17,18,20,21,22,24,25,26,27,28,30,31,32,33,34,35,36,39,40,42,44,45,48,49,50,51,52,54,55,56,60,62,63,64,65,66,68,70,72,74`
  on `D` in any order.

Why this works:

- `B-B` edges:
  `1,19,23,29` are pairwise coprime.
- `A-C` and `B-C` edges:
  every label on `C` is prime. The only multiple of each chosen prime up to `74` is itself, except for `37`, whose only extra multiple is `74`. None of those forbidden labels appears on `A ∪ B`.
- `B-D` edges:
  every nontrivial multiple of `19,23,29` up to `74` is one of `38,46,57,58,69`, and those five labels were deliberately placed in `A`. So every `D` label is coprime to every label on `B`.
- There are no other edges by the support decomposition.

Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.

Strong-result extraction:

- What part of the argument scales:
  the four-class support decomposition, the reduction to three coprimality interfaces plus one clique condition, the use of a large-prime block for `C`, and the use of a sparse barrier set on `B` whose obstructing multiples are absorbed into `A`.
- What part does not yet scale automatically:
  the exact prime choices `37,41,43,47,53,59,61,67,71,73` and barrier set `1,19,23,29` are instance-tuned; a family theorem still needs a clean supply lemma guaranteeing enough large primes for `C` and a sparse enough barrier set for `B`.
- Suggested theorem slice:
  a sufficient-condition theorem for `Γ(Z_p × Z_25)` saying that if the label interval `{1,...,4p+30}` contains a block of `p-1` primes avoiding `A ∪ B` conflicts and a `4`-label barrier set whose nontrivial multiples fit inside the `20` available `A` slots, then the graph is prime.
- Highest-value next feeder instances:
  `Γ(Z_13 × Z_25)` to test whether the same large-prime plus sparse-barrier template still closes, and `Γ(Z_11 × Z_11 × Z_2)` to pressure-test the parallel family campaign at the same parameter.
- Current publication shape:
  this is still an instance-level package, but it is closer to a paper-shaped family claim because the proof is template-driven rather than ad hoc and cleanly identifies the two arithmetic lemmas still missing for a slice theorem.

Self-check after result:

- The witness is fully explicit and uses all labels `1` through `74` exactly once.
- The solve-stage classification should remain `CANDIDATE`; this is not yet Lean-complete and not yet a theorem slice.

## family_affinity

- Family affinity is high.
- This instance is the campaign-designated first decisive feeder for the `Γ(Z_p × Z_25)` slice.
- The proof reuses the exact campaign support graph `A,B,C,D` and strengthens confidence that the current template is structural rather than accidental.

## generalization_signal

- Generalization signal is strong but not complete.
- The `p=11` case shows that the current support-template logic survives the first unsolved odd-prime test in the campaign.
- The arithmetic bottleneck now looks explicit: one needs a family-level large-prime supply statement for `C` and a reusable sparse-barrier lemma for `B`.
- That is enough to justify `SLICE_CANDIDATE` at the publication level, but not a family theorem yet.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into classes `A,B,C,D`;
  2. prove the edge support graph `A-C`, `B-B`, `B-C`, `B-D`;
  3. assign `C` a block of large primes whose multiples barely touch the label interval;
  4. assign `B` a pairwise-coprime barrier set with few nontrivial multiples;
  5. dump those barrier multiples into `A`;
  6. give `D` the residual complement.
- This is directly reusable for later feeders and for a support-template theorem statement.

## candidate_theorem_slice

- Candidate slice: a sufficient-condition theorem for odd primes `p` such that `Γ(Z_p × Z_25)` is prime whenever the interval `{1,...,4p+30}` contains:
  - a set of `p-1` labels for `C` whose only conflicts with `A ∪ B` are themselves and a very small exceptional set;
  - a `4`-element pairwise-coprime barrier set for `B` whose nontrivial multiples outside `B` occupy at most `20` labels.
- The `p=11` witness provides a concrete nontrivial example of this slice mechanism.

## smallest_param_shift_to_test

- The smallest next parameter shift to test in this family is `p = 13`.
- Reason: `p=11` was the campaign’s first decisive unsolved odd prime; once it survives, `p=13` is the tightest next discriminator for whether the same reservoir logic keeps scaling.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still one exact instance, with no rediscovery audit and no family theorem closure.
- It is publication-relevant because it pressure-tests the active `Γ(Z_p × Z_25)` campaign exactly where the campaign said it should: the first unsolved-looking odd prime after the Lean-backed `p=3,5,7` cluster.
- The argument is unusually publication-useful for an instance because it isolates a family-shaped proof template and exposes the remaining slice lemmas very clearly.

## likely_failure_points

- The only structural failure point would be a mistaken support-graph classification, especially an omitted edge type.
- The only arithmetic failure point would be overlooking a multiple of `19`, `23`, or `29` in the claimed `D` set.
- The `C` block relies on the fact that the only extra conflict beyond the chosen primes themselves is `74 = 2 * 37`.
- Publication-wise, the main remaining weakness is that this is still an exact feeder and not yet a verified theorem slice or rediscovery-cleared frontier claim.

## what_verify_should_check

- Recompute the `74` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `406` edges.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,74}`.
- Check coprimality on every actual edge from the ring graph.
- In the bounded rediscovery pass, audit not only the exact instance but also whether an existing theorem or sufficient-condition result already implies this `p=11` case.
- If verification passes, treat this as an exact-feeder success that materially strengthens the `Γ(Z_p × Z_25)` slice campaign and should go to `generalize` before `lean`.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact instance, alternate notation, family notation, and theorem/proposition/example/observation/corollary checks inside the most relevant recent source I found.
- Exact-instance searches on `Γ(Z_11 × Z_25)`, `Z_11 × Z_25` with `zero-divisor graph`, and family searches on `Γ(Z_p × Z_25)` with `prime labeling` did not produce a paper, theorem, proposition, example, or corollary settling this exact case.
- I inspected the recent article `On Prime Labelings of Zero-Divisor Graphs` (Combinatorial Press, 2025) because it is directly on-topic. Within the bounded pass, I did not find `Z_25`, the family `Γ(Z_p × Z_25)`, or the exact `p = 11` instance there.
- I therefore did not establish that the exact intended statement is already solved, directly implied, or explicitly exhibited in prior art.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The solve record stays locked to the exact intended feeder statement: existence of a prime labeling for the full zero-divisor graph `Γ(Z_11 × Z_25)`.
- The graph definition used in solve matches the dossier: vertices are the nonzero zero-divisors of `Z_11 × Z_25`, the graph is simple, adjacency is coordinatewise zero product, and the labels are a bijection onto `{1,...,74}`.
- The proof does not drift to a quotient graph, an orbit graph, or a weaker sufficient condition. It supplies an explicit labeling for all `74` vertices.
- No wrong-theorem drift, quantifier drift, or mismatch between prose and the claimed target was found.

## verify_proof

- I recomputed the support decomposition from the ring definition. The nonzero zero-divisors split exactly into classes `A,B,C,D` of sizes `20,4,10,40`, totaling `74`.
- I independently recomputed adjacency. The only edge types are `A-C`, `B-B`, `B-C`, and `B-D`, with counts `200`, `6`, `40`, and `160`, total `406`.
- Given that edge pattern, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the proposed label sets:
  - `C = {37,41,43,47,53,59,61,67,71,73}` are primes, and within `{1,...,74}` the only extra multiple among them is `74 = 2·37`; none of these forbidden labels is used on `A ∪ B`;
  - `B = {1,19,23,29}` is pairwise coprime;
  - `D` omits every nontrivial multiple of `19`, `23`, and `29` up to `74`, namely `38,46,57,58,69`, because those labels were deliberately placed in `A`.
- First incorrect step found: none.

## verify_adversarial

- I reran the provided checker `artifacts/z11-z25-prime-zero-divisor-graph/check_witness.py`. It reported `vertex_count = 74`, `edge_count = 406`, `edge_type_counts = {'A-C': 200, 'B-B': 6, 'B-C': 40, 'B-D': 160}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran an independent one-off coverage check outside the checker logic to confirm that the four label sets are disjoint and cover exactly `{1,...,74}`.
- I did not find a hidden edge type, a missed divisibility obstruction, or a computation/prose mismatch that breaks the candidate witness.

## verify_theorem_worthiness

- This feeder does suggest a real theorem slice rather than a one-off curiosity. The structural part is the exact same four-class support graph already visible at `p = 3,5,7`, and `p = 11` is the first campaign-designated unsolved odd prime where the template had to survive a nontrivial increase in interval size.
- What clearly scales:
  - the support decomposition into `A,B,C,D`;
  - the reduction to the interfaces `A-C`, `B-B`, `B-C`, and `B-D`;
  - the classwise theorem that any bijection within a class is interchangeable once the label sets satisfy the arithmetic obligations.
- What does not yet scale automatically:
  - the exact prime block used on `C`;
  - the exact sparse barrier set used on `B`;
  - the missing family lemma guaranteeing those choices for general odd prime `p`.
- Best honest publication status is not merely `INSTANCE_ONLY`. Because this verified feeder directly strengthens an active family campaign and exposes a reusable support-template mechanism, the honest status is `SLICE_CANDIDATE`, not `SLICE_EXACT` and not `FAMILY_CANDIDATE`.
- The smallest next feeder that most tests the claimed template is `Γ(Z_13 × Z_25)`. It is the next parameter after the newly verified `p = 11` breakpoint and would show whether the same large-prime plus sparse-barrier reservoir logic still closes without redesign.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- The exact intended statement appears to be proved correctly by the current explicit witness, and the bounded rediscovery pass did not establish that this exact result is already in prior art.
- Because Lean has not been completed, the harness classification must remain `CANDIDATE`, not `EXACT`.
- `lean_ready = true`

## minimal_repair_if_any

- None. No conservative patch to the mathematical content was needed.
