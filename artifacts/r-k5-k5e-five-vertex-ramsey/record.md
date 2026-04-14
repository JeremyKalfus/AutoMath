# Solve Record: Determine the exact value of R(K5, K5-e)

## statement_lock
- Active slug: `r-k5-k5e-five-vertex-ramsey`.
- Active title: `Determine the exact value of R(K5, K5-e)`.
- Locked target: determine the least `N` such that every red-blue coloring of `K_N` contains a red `K5` or a blue `K5-e`.
- Equivalent graph form: let `J5 := K5-e`. Then `R(K5, J5) = m + 1`, where `m` is the largest order of a graph `G` with `alpha(G) <= 4` and no subgraph `J5`.
- Under the current interval `30 <= R(K5, J5) <= 33`, the graph-form witness size is `m in {29, 30, 31, 32}`.
- If this closes, the exact title theorem would be: `The Exact Value of R(K5, K5-e)`.

## definitions
- Write `J5 := K5-e` and `J4 := K4-e`.
- A critical lower-bound witness is a graph `G` on `m` vertices with `alpha(G) <= 4` and `J5`-free.
- In the original coloring language, `G` is the blue graph and `G^c` is the red graph.
- Because `J5` contains a `K4`, every `J5`-free graph is automatically `K5`-free.
- A successful exact solve would already be about `0.78` of a paper by the packet's own estimate: one theorem, one proof or one explicit witness certificate, and only light packaging remain.

## approach_A
- Structural / invariant route: work inside a hypothetical critical witness `G` with `alpha(G) <= 4` and no `J5`.
- Lemma A1: for every vertex `v`, the neighborhood graph `G[N(v)]` is `J4`-free.
- Reason: if `N(v)` contained a `J4`, then adjoining `v` would produce a `J5`.
- Consequence: `G[N(v)]` is also `K4`-free, since `K4` contains `J4` as a subgraph.
- Therefore `deg(v) <= R(4, 5) - 1 = 24`; equivalently, in any hypothetical witness on `m` vertices, every vertex degree lies in `[m - 25, 24]`.
- In particular, if `m = 32`, then every degree lies in `[7, 24]`.
- Stronger local lemma: if `uv` is an edge of `G`, then `G[N(u) cap N(v)]` is a matching.
- Proof sketch: among the five vertices `{u, v, a, b, c}` with `a, b, c in N(u) cap N(v)`, the edge `uv` and the six incident edges from `{u, v}` to `{a, b, c}` already contribute `7` edges. If `a, b, c` span two edges, then the same five-set has at least `9` edges and hence contains a `J5`. So every three vertices of `N(u) cap N(v)` span at most one edge, which forces maximum degree at most `1`.
- Consequence: if `uv` is an edge, then `|N(u) cap N(v)| <= 8`. Indeed, a matching on `9` vertices has an independent set of size `5`, which would also be independent in `G`, contradicting `alpha(G) <= 4`.
- Another consequence: for each vertex `v`, every vertex in `G[N(v)]` has degree at most `8`, because an edge `vx` has at most `8` common neighbors.
- So every neighborhood graph `G[N(v)]` is simultaneously `K4`-free, `alpha <= 4`, and `Delta <= 8`.

## approach_B
- Construction / extremal / contradiction route: assume a witness `G` exists on `m = 32` vertices and try to force it into a contradiction.
- For a nonedge `uv`, the common-neighborhood graph `G[N(u) cap N(v)]` is triangle-free.
- Reason: if three common neighbors of a nonedge formed a triangle, then together with `u` and `v` they would give a `J5` whose missing edge is `uv`.
- Using the classical value `R(3, 5) = 14`, this implies `|N(u) cap N(v)| <= 13` for every nonedge `uv`, since `G[N(u) cap N(v)]` is triangle-free and still has independence number at most `4`.
- This yields a rigid local profile for any `32`-vertex witness:
- `alpha(G) <= 4`.
- `G` is `J5`-free.
- Every degree lies in `[7, 24]`.
- Every edge has codegree at most `8`.
- Every nonedge has codegree at most `13`.
- Every neighborhood graph is `K4`-free with maximum degree at most `8`.
- This is the right contradiction framework, but it still does not rule out existence on `30`, `31`, or `32` vertices without either a much sharper counting argument or an actual seed construction to extend.
- The packet's recommended route remains correct: start from a real `29`-vertex witness and perform extension analysis, rather than attempt unguided global search.

## lemma_graph
- Step 1: translate the Ramsey problem into the graph problem `alpha(G) <= 4` and `J5`-free.
- Step 2: prove neighborhood exclusion `G[N(v)]` is `J4`-free, hence `K4`-free.
- Step 3: prove the edge-common-neighborhood matching lemma.
- Step 4: deduce edge codegree bound `<= 8` and neighborhood maximum-degree bound `<= 8`.
- Step 5: prove the nonedge-common-neighborhood triangle-free lemma.
- Step 6: deduce nonedge codegree bound `<= 13`.
- Step 7: use these local filters on a known `29`-vertex witness to test extendability to `30`, then `31`, then `32`.
- Step 8: if every extension dies before `32`, the exact value drops below `33`; if a `32`-vertex witness survives, then the exact value is `33`.

## chosen_plan
- Chosen path: structural route first, no brute force.
- Reason: the target is not marked `search-heavy`, no local witness file is present in this artifact directory, and the strongest honest progress available here is a clean obstruction packet for any critical witness.
- Minimal code decision: no code. The reasoning stage did not shrink the space to a tiny residue, so a search step would still be too broad to justify under the solve rules.

## self_checks
- Statement-lock check: the solve stayed on the exact intended theorem and used the standard graph reformulation only as an equivalent restatement.
- Approach-A check: each implication uses only five-vertex subgraph counting and the packet's inherited interval; no web or hidden source dependence entered.
- Approach-B check: the only external numerical inputs are the classical exact values `R(4, 5) = 25` and `R(3, 5) = 14`, used conservatively as local filters.
- Result check: no forcing proof and no explicit witness were obtained, so the classification cannot honestly exceed `PARTIAL`.

## code_used
- None.
- Rationale: minimal code is not yet justified because two reasoning strategies only produced a structural residue, not a sharply bounded certificate check.

## result
- No exact value or explicit counterexample was obtained in this solve pass.
- Best rigorous output: any critical witness `G` for the lower side of `R(K5, K5-e)` must satisfy all of the following.
- `alpha(G) <= 4`.
- `G` is `J5`-free.
- Every neighborhood graph `G[N(v)]` is `J4`-free, hence `K4`-free.
- Every degree is at most `24`, and on `m = 32` vertices every degree is at least `7`.
- For every edge `uv`, the graph `G[N(u) cap N(v)]` is a matching, so edge codegree is at most `8`.
- For every nonedge `uv`, the graph `G[N(u) cap N(v)]` is triangle-free, so nonedge codegree is at most `13`.
- This is a real theorem-facing slice, but it does not yet close the exact value. The current result is still too thin for the micro-paper lane on its own.

## family_affinity
- Strong.
- The problem is anchored in the residual five-vertex Ramsey table, and the structural lemmas above are about the same near-clique obstruction that makes the exact pair publication-worthy.
- If the main claim closes, it would already be roughly `70-90%` of a paper; here the packet estimate is `0.78`.

## generalization_signal
- Moderate, but asymmetric.
- What scales: the translation to `J_t`-free graphs with bounded independence number, then studying neighborhoods and common neighborhoods as obstruction carriers.
- What does not scale cleanly: the exact matching conclusion for edge common neighborhoods is special to `J5`; for larger `J_t` one only gets exclusion of denser patterns, not a one-regular structure.

## proof_template_reuse
- Reusable template: convert the Ramsey problem to a forbidden-subgraph-plus-bounded-independence graph problem, then mine common-neighborhood structure of edges and nonedges for extension filters.
- This template should transfer to nearby almost-clique pairs, but the numerical bounds and the sharp local shape need to be recomputed case by case.

## candidate_theorem_slice
- Clean slice visible: in any graph `G` with `alpha(G) <= 4` and no `K5-e`, the common neighborhood of an edge is a matching.
- Immediate consequences: every edge has codegree at most `8`, and every vertex neighborhood has maximum degree at most `8`.
- This is the smallest honest theorem slice produced here. It is useful support if the main claim closes, but by itself it is not yet a paper-shaped result.

## smallest_param_shift_to_test
- Best next parameter shift: obtain or reconstruct one actual `29`-vertex witness and test whether it extends to `30`.
- Second shift after that: if a `30`-vertex witness exists, test whether it extends to `31`.
- These are the smallest shifts that move the exact answer directly, whereas jumping immediately to `32` without a seed witness is too unconstrained.

## why_this_is_or_is_not_publishable
- If the exact value closes, yes: this target still looks like an honest micro-paper, and the title theorem would simply be `The Exact Value of R(K5, K5-e)`.
- Minimal remaining packaging after a genuine closure would be small: one compact literature paragraph, one exact proof or witness certificate, and one short comparison with neighboring solved five-vertex pairs.
- The current solve output is not publishable. It gives necessary structure for a critical witness, but no exact determination, no extremal example, and no theorem slice strong enough to stand alone as the title result.
- So the present package is still too thin for the micro-paper lane.

## paper_shape_support
- Smallest supporting theorem slice if the main claim closes: the edge-common-neighborhood matching lemma.
- Natural immediate corollary: in any critical witness, every vertex neighborhood is `K4`-free with maximum internal degree at most `8`.
- Why this matters for paper shape: it supplies one crisp local-rigidity lemma that can sit directly before either an extension obstruction or a witness verification.

## boundary_remark
- Boundary remark: the current argument explains why any successful extremal construction must be locally sparse even though the ambient graph has independence number only `4`.
- What part of the argument scales: the common-neighborhood obstruction method.
- What part does not: the exact matching structure is a `K5-e` phenomenon, not a generic `K_t-e` phenomenon.
- Suggested theorem slice from this run: `edge common neighborhoods are matchings in K5-e-free graphs with alpha <= 4`.
- Most useful next parameter shifts: `29 -> 30` and `30 -> 31`.
- Current package status: closer to an instance-preparation note than to a paper-shaped exact claim.

## likely_failure_points
- The solve lacks the actual known lower-bound witness on `29` vertices, so the most natural extension analysis cannot begin.
- The local codegree bounds are clean but still too weak to force a contradiction on `32` vertices by hand.
- A later computational step may be necessary, but only after importing a real seed construction or shrinking the residue much further.

## what_verify_should_check
- Verify the exact graph reformulation `R(K5, K5-e) = m + 1` with `alpha(G) <= 4` and `J5`-free.
- Check the edge-common-neighborhood matching lemma carefully.
- Check the derived edge codegree bound `<= 8`.
- Check the nonedge triangle-free common-neighborhood lemma and the derived nonedge codegree bound `<= 13`.
- Check whether the theorem slice already appears in the small Ramsey or almost-clique literature; if it does, then it is support only and not a novelty claim.
- Confirm that no stronger conclusion than `PARTIAL` is warranted from this solve pass.
