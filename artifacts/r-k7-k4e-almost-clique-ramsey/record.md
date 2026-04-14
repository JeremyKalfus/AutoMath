## statement_lock

Active slug: `r-k7-k4e-almost-clique-ramsey`

Active title: `Determine the exact value of R(K7, K4-e)`

Locked intended statement:

- Determine the least `n` such that every red-blue coloring of `K_n` contains either a red `K7` or a blue `K4-e`.

Equivalent blue-graph formulation:

- Let `G` be the blue graph. Then `R(K7, K4-e) <= n` iff every `K4-e`-free graph `G` on `n` vertices has `alpha(G) >= 7`.
- Therefore the exact closure is:
- either prove every `K4-e`-free graph on `28` vertices has independence number at least `7`, which would give `R(K7, K4-e) = 28`,
- or exhibit a `K4-e`-free graph on `28` vertices with independence number at most `6`, which would give `R(K7, K4-e) = 29`.

Exact title theorem if this closes:

- `The Exact Value of R(K7, K4-e)`

Publication relevance:

- Yes. A successful exact solve here would still be about `0.82` of a paper by itself; the remaining work would mostly be packaging the forcing proof or explicit `28`-vertex witness, plus a short placement paragraph in the almost-clique Ramsey table.

## definitions

- `K4-e` means the `5`-edge graph obtained from `K4` by deleting one edge.
- Subgraph containment here is non-induced. In particular, a blue `K4` also counts as a blue `K4-e`.
- `alpha(G)` is the independence number of the blue graph `G`; a blue independent set of size `7` is exactly a red `K7`.
- For `v in V(G)`, `N(v)` is the blue neighborhood and `A(v) = V(G) \\ N[v]` is the blue anti-neighborhood.

Ambiguities and conventions that matter:

- The known literature lower bound `28 <= R(K7, K4-e)` only certifies a `27`-vertex avoiding coloring. It does not supply the `28`-vertex witness needed for `R = 29`.
- Because containment is non-induced, any local argument must forbid both blue diamonds and blue `K4`s automatically.
- The working packet points to an SDP-based upper bound `R(K7, K4-e) <= 29`, so the solve-stage burden is to close exactly one endpoint, not to re-prove the existing upper bound.

## approach_A

Structural / invariant route.

Set `G` to be a hypothetical `K4-e`-free graph with `alpha(G) <= 6` on as many vertices as possible. Then:

1. Local neighborhood rigidity.
   For any vertex `v`, the induced graph `G[N(v)]` cannot contain a path `x-y-z`.
   Otherwise the four vertices `v,x,y,z` span the five blue edges `vx, vy, vz, xy, yz`, which is a blue `K4-e`.
   Since `G[N(v)]` is `P3`-free, it is a disjoint union of cliques; and because a triangle in `N(v)` together with `v` gives a blue `K4`, all those cliques have size at most `2`.
   Therefore `G[N(v)]` is always a matching plus isolated vertices.

2. Degree cap from the independence budget.
   If `d(v) = |N(v)|`, and `N(v)` is a matching plus isolated vertices with `t` edges and `s` isolates, then `2t + s = d(v)` and `alpha(G[N(v)]) = t + s = d(v) - t >= ceil(d(v)/2)`.
   Because `alpha(G) <= 6`, we must have `alpha(G[N(v)]) <= 6`, hence `d(v) <= 12`.

3. Sharp form near the cap.
   If `d(v) = 12`, then `ceil(d(v)/2) = 6`, so `N(v)` must realize the minimum possible independence number. That forces `t = 6` and `s = 0`, so `G[N(v)] = 6K2`.
   If `d(v) = 11`, then `t + s <= 6` and `2t + s = 11`, which forces `t = 5`, `s = 1`. So `G[N(v)] = 5K2 + K1`.

4. Anti-neighborhood recursion.
   Any independent `6`-set in `A(v)` together with `v` would produce an independent `7`-set in `G`.
   Hence `alpha(G[A(v)]) <= 5` for every vertex `v`.

What this route gives rigorously:

- any `29`-vertex counterexample would have maximum blue degree at most `12`,
- every degree-`11` or degree-`12` neighborhood is forced into a near-perfect matching pattern,
- every anti-neighborhood sits inside the smaller subproblem " `K4-e`-free with independence at most `5` ".

Why it does not close the main claim by itself:

- the residual anti-neighborhood can still have size as large as `16`,
- I do not have, from the allowed local file budget alone, a proved sharp upper bound on the order of a `K4-e`-free graph with independence number `5`,
- so the recursion isolates the hard core but does not eliminate it.

## approach_B

Construction / extremal / contradiction route.

Try to decide between `28` and `29` by modeling a hypothetical lower-side witness on `28` vertices.

Observations:

- A blue witness for `R = 29` would have to be unusually dense while still avoiding every `4`-vertex set with `5` blue edges.
- Rephrased in the red graph `R = complement(G)`, every `4`-set must span at least `2` red edges, while `R` must avoid `K7`.
- That sounds like a clean contradiction setup, but the first coarse counts are too weak:
- averaging over `4`-sets only yields a mild lower bound on `e(R)`,
- the blue-side degree cap `Delta(G) <= 12` still permits too many blue edges for a Turan contradiction on the red side.

I also considered a direct constructive picture for the blue graph:

- maximal blue cliques have size at most `3`,
- each blue neighborhood is a matching plus isolates,
- so any extremal witness would have to look like a carefully glued system of edge-disjoint triangles and edges with unusually small independence number.

That is a useful mental model, but it does not become a proof without either:

- a classification of the allowable `16`-vertex anti-neighborhoods, or
- a bounded search over those templates.

Under the solve-stage rules, that search would be the main method rather than a minimal checker, so I am not treating it as justified code yet.

## lemma_graph

- Lemma 1: If `G` is `K4-e`-free and `v in V(G)`, then `G[N(v)]` is a matching plus isolates.
- Lemma 2: If additionally `alpha(G) <= 6`, then `d(v) <= 12` for every `v`.
- Lemma 3: If `d(v) = 12`, then `G[N(v)] = 6K2`; if `d(v) = 11`, then `G[N(v)] = 5K2 + K1`.
- Lemma 4: If `alpha(G) <= 6`, then `alpha(G[A(v)]) <= 5` for every `v`.
- Dependency flow: Lemma 1 -> Lemma 2 -> Lemma 3, and Lemma 2 + anti-neighborhood definition -> Lemma 4.
- Proof skeleton for the exact theorem:
- choose a strategically extreme vertex `v`,
- use Lemmas 1 to 4 to force the `N(v)` / `A(v)` split into a very rigid local template,
- then either classify the `A(v)` side sharply enough to contradict `|V(G)| = 29`, or construct a `28`-vertex witness that survives all local constraints.

## chosen_plan

Chosen path: keep the argument on the structural side and extract the strongest rigorous theorem-facing slice available without turning the run into a search project.

Reason for the choice:

- the current packet is already one endpoint away from a paper, so what matters most is an honest reduction that narrows the exact obstruction,
- the neighborhood / anti-neighborhood lemmas are clean, reusable, and actually proved,
- the construction route is still speculative unless I allow a nontrivial template search, which would violate the "reasoning first, minimal code" priority here.

## self_checks

- Statement lock check: the exact closure really is binary, `28` versus `29`, and the lower-bound endpoint language was corrected to the needed `28`-vertex witness versus known `27`-vertex witness.
- Definition check: I consistently treated `K4-e` as a non-induced forbidden subgraph, so blue `K4`s were not accidentally allowed.
- Approach A check: each local lemma only uses the forbidden `K4-e` pattern and the independence cap `alpha <= 6`.
- Approach B check: I did not overclaim any edge-count contradiction; the counting route was recorded as insufficient, not as a theorem.
- Code check: no code was used because any exact search here would no longer be a secondary checker.

## code_used

No code used.

Reason:

- The current output is a reasoning-first reduction.
- A bounded search on `28` or `29` vertices would be the primary solve mechanism, not a minimal checker or witness verifier.
- That would be a concept shift toward search-heavy work without a prior structural collapse.

## result

Best rigorous solve-stage result from this run:

> Proposition.
> Let `G` be a `K4-e`-free graph with `alpha(G) <= 6`.
> Then for every vertex `v`:
> 1. `G[N(v)]` is a matching plus isolated vertices.
> 2. `deg(v) <= 12`.
> 3. If `deg(v) = 12`, then `G[N(v)] = 6K2`.
> 4. If `deg(v) = 11`, then `G[N(v)] = 5K2 + K1`.
> 5. `alpha(G[A(v)]) <= 5`.

Proof.

- Part `1`: if `G[N(v)]` contained a path `x-y-z`, then the four vertices `v,x,y,z` would span the five edges `vx, vy, vz, xy, yz`, a `K4-e`. So `G[N(v)]` is `P3`-free, hence a disjoint union of cliques. A triangle in `N(v)` together with `v` would produce a blue `K4`, which contains a blue `K4-e`, so those cliques have size at most `2`.
- Part `2`: write `G[N(v)]` as `t` disjoint edges and `s` isolated vertices. Then `2t + s = deg(v)` and an independent set in `N(v)` is obtained by taking one endpoint from each edge and every isolate, so `alpha(G[N(v)]) = t + s >= ceil(deg(v)/2)`. Since `alpha(G) <= 6`, we get `deg(v) <= 12`.
- Parts `3` and `4`: solve the integer constraints above together with `t + s <= 6`.
- Part `5`: any independent `6`-set inside `A(v)` together with `v` would be an independent `7`-set in `G`, impossible.

Conservative solve conclusion:

- I did not close `R(K7, K4-e)`.
- I did isolate the remaining obstruction to a much narrower local template: any `29`-vertex counterexample must have all blue neighborhoods extremely close to perfect matchings, and every anti-neighborhood falls into the smaller "`alpha <= 5`" subproblem.

What part of the argument scales:

- the neighborhood-matching lemma,
- the degree cap `Delta(G) <= 2r` for `K4-e`-free graphs with `alpha(G) <= r`,
- the anti-neighborhood reduction `alpha(G[A(v)]) <= r-1`.

What part does not scale yet:

- the final classification of the residual anti-neighborhood,
- any exact contradiction at the `29`-vertex level,
- any explicit `28`-vertex witness for the lower side.

Suggested theorem slice from the current packet:

- "Local structure of extremal `K4-e`-free graphs with bounded independence number."

Immediate corollary / remark:

- Any proof that `R(K7, K4-e) = 28` can focus on the degree-`11` / degree-`12` bottleneck, because larger blue degree is already excluded in every hypothetical `29`-vertex counterexample.

Exact sentence for why the instance matters:

- This instance matters because closing `R(K7, K4-e)` would replace a one-line frontier interval in a standard Ramsey table by a complete exact theorem with almost no additional packaging overhead.

## family_affinity

Strong.

This reduction lives naturally in the `R(K_t, K4-e)` family:

- replacing `6` by `t-1` gives the same local proof template,
- the matching-neighborhood phenomenon is specific to the almost-clique target `K4-e`,
- the anti-neighborhood recursion is exactly the kind of family-stable ingredient that can be reused across nearby almost-clique instances.

## generalization_signal

Moderate but not yet publication-grade.

The reusable signal is:

- if `G` is `K4-e`-free with `alpha(G) <= r`, then every neighborhood is a matching plus isolates, hence `Delta(G) <= 2r`,
- and every anti-neighborhood has independence number at most `r-1`.

That is a real family-level template, but on its own it still looks too standard and too weak to be a micro-paper result.

## proof_template_reuse

Reusable proof template:

1. Translate `R(K_t, K4-e)` into a `K4-e`-free blue graph with `alpha <= t-1`.
2. Choose an extreme blue vertex.
3. Use the local `P3`-in-neighborhood obstruction to force `N(v)` into `K2` and `K1` components only.
4. Convert the neighborhood shape into a degree cap and a sharply smaller anti-neighborhood subproblem.
5. Spend the real effort only on the small residual configuration space.

This template should transfer to nearby `K_t` versus almost-clique endpoints, but the final residual classification remains the missing step here.

## candidate_theorem_slice

Candidate theorem slice:

- If `G` is a `K4-e`-free graph with `alpha(G) <= 6`, then `Delta(G) <= 12`, every degree-`12` neighborhood is exactly `6K2`, every degree-`11` neighborhood is exactly `5K2 + K1`, and every anti-neighborhood has independence number at most `5`.

Assessment:

- theorem-facing and exact,
- likely useful as a setup lemma in an eventual exact proof,
- still too thin by itself for the micro-paper lane.

## smallest_param_shift_to_test

The most useful next shifts are:

- the `alpha <= 5` residual problem on `16` vertices arising from `A(v)` when `deg(v) = 12`,
- the exact neighboring family value `R(K6, K4-e)`, because any sharp information there feeds directly into the anti-neighborhood recursion for the present `K7` case.

Among same-instance shifts, the sharpest immediate split is:

- degree-`12` neighborhood case versus degree-`11` neighborhood case in a hypothetical `29`-vertex counterexample.

## why_this_is_or_is_not_publishable

Current result: not publishable in the micro-paper lane.

Reason:

- the exact value `28` versus `29` remains open,
- the proved local slice is useful but probably standard-looking,
- there is no exact witness, no forcing proof, and no new family theorem with enough weight to stand as a note.

If the main claim closes:

- yes, the solve would already be roughly `70` to `90` percent of a paper,
- the title theorem would simply be the exact value statement,
- minimal remaining packaging would be the clean proof write-up, one paragraph locating the result in the almost-clique table, and one short remark on the lower or upper endpoint mechanism.

Current honesty check:

- this packet is still too thin for the micro-paper lane unless the exact endpoint itself closes.

## paper_shape_support

If the main claim closes, the smallest support needed for a paper-shaped packet is:

- the exact theorem statement `R(K7, K4-e) = 28` or `29`,
- one self-contained forcing argument on `28` vertices or one explicit `28`-vertex witness,
- the local proposition above as a supporting setup lemma or boundary remark,
- one sentence locating the result in the established almost-clique Ramsey table.

Natural corollary or boundary remark if closure happens:

- the solved value would pin down the entire `K7` versus `K4-e` entry exactly, removing the last one-step ambiguity left by the current public table entry.

## boundary_remark

Boundary remark:

- The current local constraints are strong enough to show that any `29`-vertex counterexample must concentrate in a very narrow degree window, but they are not strong enough to force a contradiction by crude averaging alone. In particular, the bottleneck has already moved from "general `29`-vertex coloring" to "classification of the residual `alpha <= 5` anti-neighborhood inside a degree-`11` or degree-`12` local template."

## likely_failure_points

- The local proposition may already be folklore in the `K4-e` / diamond-free Ramsey literature, so it should not be oversold.
- The main missing ingredient is a sharp classification of `K4-e`-free graphs with small independence number on the anti-neighborhood side.
- A direct construction attempt for `28` vertices is underconstrained without search.
- A direct contradiction attempt on `29` vertices is underpowered without a stronger extremal bound than the ones proved here.

## what_verify_should_check

- Check whether the neighborhood-matching proposition is already explicit in prior `K4-e` Ramsey or diamond-free graph literature.
- Check the endpoint language carefully: known lower bound `28 <= R(K7, K4-e)` means a `27`-vertex avoiding coloring, not the `28`-vertex witness needed for `R = 29`.
- If a future run uses code, verify that it stays in a genuinely bounded residual space such as the `16`-vertex anti-neighborhood case, rather than drifting into unconstrained brute force.
- Check whether any known exact value or sharp bound for `R(K6, K4-e)` immediately collapses the anti-neighborhood recursion used here.
