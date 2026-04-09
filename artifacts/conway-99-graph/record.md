# Solve Record: conway-99-graph

## statement_lock

- Active title: `Does Conway's 99-graph exist?`
- Active slug: `conway-99-graph`
- Locked target statement: determine whether there exists a simple graph on `99` vertices in which adjacent pairs have exactly `1` common neighbor and nonadjacent pairs have exactly `2` common neighbors.
- Equivalent exact formulation: determine whether there exists a strongly regular graph with parameters `(v,k,lambda,mu) = (99,14,1,2)`.
- Matrix form I will use: for the adjacency matrix `A`,
  `A^2 = 14 I + A + 2 (J - I - A) = 12 I - A + 2 J`.
- This solve pass does not claim anything about nearby parameter sets.

## definitions

- `G` is a finite simple undirected graph.
- `N(v)` denotes the open neighborhood of a vertex `v`.
- `W(v)` denotes the set of vertices outside `{v} union N(v)`.
- A triangle means a `3`-cycle.
- For a fixed base vertex `v`, once `N(v)` is shown to be a matching, I write its `7` edges as
  `e_i = {a_i^0, a_i^1}` for `i = 1,...,7`.
- For `x in W(v)`, the two neighbors of `x` inside `N(v)` determine a label
  `x = x_{ij}^{alpha beta}` when `x` is adjacent to `a_i^alpha` and `a_j^beta` with `i != j`.
- Conventions locked:
  - the graph is simple;
  - every use of `lambda = 1` means each edge lies in a unique triangle;
  - every use of `mu = 2` means each nonedge has exactly two common neighbors.

## approach_A

Structural / invariant route through the strongly regular identities.

1. Parameter feasibility is consistent:
   `k (k - lambda - 1) = (v - k - 1) mu`
   becomes
   `14 * 12 = 84 * 2`.

2. The nontrivial eigenvalues solve
   `x^2 + (mu - lambda) x + (mu - k) = 0`,
   hence
   `x^2 + x - 12 = 0`,
   so the spectrum is
   `14^1, 3^54, (-4)^44`.

3. Hoffman bounds give
   `alpha <= 99 * 4 / (14 + 4) = 22`
   and
   `omega <= 1 - 14 / (-4) = 4`.
   But `lambda = 1` rules out `K_4` immediately, because an edge of a `K_4` has two common neighbors. So in fact `omega <= 3`.

4. Because every edge lies in a unique triangle, every vertex of degree `14` lies in exactly `14 / 2 = 7` triangles.
   Therefore the total number of triangles is
   `99 * 7 / 3 = 231`.

Self-check after Approach A:
- The spectral data are exact and instance-specific.
- These checks show the parameter set is feasible and quite rigid, but they do not produce either a construction or a contradiction.

## approach_B

Construction / extremal / contradiction route through the local neighborhood structure around one vertex.

1. Fix a vertex `v`.
   For each `u in N(v)`, the number of neighbors of `u` inside `N(v)` equals the number of common neighbors of `u` and `v`, namely `lambda = 1`.
   So the induced graph on `N(v)` is `1`-regular on `14` vertices:
   `G[N(v)] = 7 K_2`.

2. Label those `7` neighborhood edges as
   `e_i = {a_i^0, a_i^1}`.
   Now take two vertices `a_i^alpha` and `a_j^beta` from distinct edges.
   They are nonadjacent inside `N(v)`, so they have exactly `2` common neighbors.
   One common neighbor is `v`.
   Because `G[N(v)]` is a matching, there is no second common neighbor inside `N(v)`.
   Hence there is a unique vertex of `W(v)` adjacent to both.
   This gives a canonical labeling
   `x_{ij}^{alpha beta}` of every vertex of `W(v)`.

3. The count is exact:
   there are
   `binom(7,2) * 2 * 2 = 84`
   such labels, matching
   `|W(v)| = 99 - 1 - 14 = 84`.
   So every second-neighborhood vertex is forced and uniquely identified by one choice of two distinct neighborhood edges and one endpoint on each.

4. Let `x = x_{ij}^{alpha beta}` with neighborhood vertices
   `p = a_i^alpha` and `q = a_j^beta`.
   Since `x` has degree `14`, and exactly `2` of those neighbors are `p` and `q`, the induced graph `G[W(v)]` is `12`-regular.

5. More sharply, `x` has exactly two neighbors in `W(v)` that share one neighborhood vertex with `x`.
   For the edge `xp`, the pair `(x,p)` is adjacent, so it has exactly one common neighbor.
   That common neighbor cannot be `v`, cannot be `q`, and cannot lie in `N(v)`.
   Therefore there is a unique vertex `tau_p(x) in W(v)` adjacent to both `x` and `p`.
   The same argument gives a unique `tau_q(x) in W(v)`.
   These are distinct, so exactly two neighbors of `x` in `W(v)` share one `N(v)`-neighbor with `x`.
   The remaining ten neighbors of `x` in `W(v)` share no `N(v)`-neighbor with `x`.

Self-check after Approach B:
- The local model is fully forced by `lambda = 1` and `mu = 2`; no heuristic choices entered.
- The count `84 = binom(7,2) * 4` exactly matches the second-neighborhood size, so there is no slack in the labeling.

## lemma_graph

1. `G[N(v)] = 7 K_2` for every vertex `v`.
2. For fixed `v`, every vertex of `W(v)` is uniquely labeled by a pair of distinct neighborhood edges and one endpoint choice on each.
3. `G[W(v)]` is `12`-regular.
4. If `x in W(v)`, exactly `2` of its `12` neighbors in `W(v)` share one `N(v)`-neighbor with `x`, and the other `10` share none.
5. Every vertex of `G` lies in exactly `7` triangles, so `G` has exactly `231` triangles.
6. Exactly `7` of those triangles contain `v`.
7. Exactly `84` triangles contain one vertex of `N(v)` and two vertices of `W(v)`.
8. Exactly `140` triangles lie completely inside `W(v)`.

## chosen_plan

I chose Approach B as the main proof attempt because it gives exact, hand-checkable structure rather than only admissibility tests.

Step 1. Lock the local neighborhood.
Fix `v`. Since each `u in N(v)` has exactly one common neighbor with `v`, every `u` has exactly one neighbor inside `N(v)`. Therefore `N(v)` is a perfect matching on `14` vertices.

Self-check:
- A `1`-regular graph on `14` vertices is necessarily `7 K_2`.

Step 2. Label the entire second neighborhood.
For distinct matching edges `e_i, e_j` and endpoint choices `a_i^alpha, a_j^beta`, the pair is nonadjacent, so it has exactly two common neighbors. One is `v`; the other must lie in `W(v)` and is unique. This produces `84` distinct labels `x_{ij}^{alpha beta}` and exhausts `W(v)`.

Self-check:
- Distinct labels cannot represent the same vertex, because a vertex of `W(v)` has exactly two neighbors in `N(v)`.
- The count matches `|W(v)|`, so nothing is missing.

Step 3. Count the `W(v)`-neighbors of a labeled vertex.
Take `x = x_{ij}^{alpha beta}` with `N(v)`-neighbors `p` and `q`.
The edge `xp` lies in a unique triangle, so there is a unique vertex `tau_p(x) in W(v)` adjacent to both `x` and `p`.
Likewise `xq` has a unique `tau_q(x) in W(v)`.
Thus exactly two neighbors of `x` in `W(v)` share one `N(v)`-neighbor with `x`.
Since `deg(x) = 14` and `x` already uses `p` and `q`, the other ten neighbors of `x` lie in `W(v)` and share no `N(v)`-neighbor with `x`.

Self-check:
- `tau_p(x)` cannot equal `tau_q(x)`, because then that vertex would be adjacent to both endpoints `p` and `q` together with `x`, contradicting uniqueness of the `N(v)`-labels.
- The count `2 + 10 = 12` matches the `W(v)`-degree.

Step 4. Count triangles by location relative to `v`.
Every vertex lies in `7` triangles, so there are `231` total triangles.
Exactly `7` contain `v`, one for each matching edge in `N(v)`.
Now fix `p in N(v)`.
Inside `N(p)`, the pair `{v, p'}` coming from the matching edge of `N(v)` accounts for one edge of the neighborhood matching at `p`.
The remaining `12` neighbors of `p` lie in `W(v)`, and because `N(p)` is again a matching, they split into `6` adjacent pairs.
Each pair gives a triangle with exactly one `N(v)`-vertex, namely `p`.
Summing over all `14` choices of `p` gives `14 * 6 = 84` such triangles.
So the remaining
`231 - 7 - 84 = 140`
triangles lie completely in `W(v)`.

Self-check:
- A triangle with two vertices in `N(v)` must be one of the `7` triangles through `v`, because the only edges inside `N(v)` are the `7` matched pairs.
- A triangle with exactly one `N(v)`-vertex is counted exactly once.

Step 5. Try to force a contradiction.
This structure is much tighter than the raw parameter list, but I do not currently see a clean global contradiction from it.
The likely next layer would be a coherent-configuration or star-complement analysis on the `21` four-vertex cells `C_{ij} = {x_{ij}^{00}, x_{ij}^{01}, x_{ij}^{10}, x_{ij}^{11}}`, but I do not have a rigorous closure of that route in this solve pass.

Self-check:
- Stopping at `PARTIAL` is the conservative choice: the local theorem is rigorous, but it does not settle existence.

## self_checks

- Statement-lock check: every argument stays on the exact `(99,14,1,2)` instance.
- Neighborhood check: `lambda = 1` really forces each `N(v)` to be a matching, not just triangle-sparse.
- Labeling check: every nonadjacent pair from distinct matching edges has exactly one second-neighborhood witness besides `v`, so the `84` labels are exact.
- Degree check: each `x in W(v)` has `2` neighbors in `N(v)` and therefore `12` neighbors in `W(v)`.
- Triangle-count check: `99 * 7 / 3 = 231`, and the split `7 + 84 + 140` is consistent.
- Conservatism check: I am not claiming a disproof or a construction; this is a structural reduction only.

## code_used

- No code used in the artifact.
- Reason: the strongest progress in this pass is purely handwritten local structure, and I did not reach a narrowly justified need for a checker or bounded search.

## result

- I did not prove or disprove existence of a strongly regular graph with parameters `(99,14,1,2)`.
- I did prove a rigid local structure package that any such graph must satisfy:
  - every neighborhood is exactly `7 K_2`;
  - relative to any fixed vertex `v`, the `84` second-neighborhood vertices are canonically labeled by endpoint choices on two distinct matched neighborhood edges;
  - the induced graph on that second neighborhood is `12`-regular;
  - each second-neighborhood vertex has exactly `2` neighbors sharing one neighborhood endpoint and `10` sharing none;
  - the whole graph has exactly `231` triangles, split as `7` through `v`, `84` with exactly one neighbor of `v`, and `140` entirely in the second neighborhood.
- Solve-stage classification: `PARTIAL`.

## likely_failure_points

- The last unsolved step is global, not local: I do not yet know how to turn the `21` four-vertex cells into a contradiction or construction.
- Verification should check carefully that the labeling map `x_{ij}^{alpha beta}` is truly bijective and that no hidden double-counting occurs in the `84`-triangle count.
- The triangle split is exact, but it still leaves many possible adjacency patterns inside `W(v)`.
- There is prior-art risk on the local theorem package itself; parts of it may already be standard folklore for Conway's `99`-graph problem.

## what_verify_should_check

- Re-derive the spectrum `14^1, 3^54, (-4)^44`.
- Recheck the Hoffman consequences `alpha <= 22` and `omega <= 3`.
- Verify that `G[N(v)] = 7 K_2` for every `v`.
- Verify the bijection
  `W(v) <-> { (i,j,alpha,beta) : 1 <= i < j <= 7, alpha,beta in {0,1} }`.
- Verify that each `x in W(v)` has exactly two `W(v)`-neighbors sharing one `N(v)`-neighbor with `x`.
- Verify the triangle count split `231 = 7 + 84 + 140`.
- In the rediscovery pass, check whether this local package is already a standard reformulation in the literature around Conway's `99`-graph problem.

## verify_rediscovery

- PASS 1 outcome: no bounded-search evidence that the exact intended statement
  `there exists an srg(99,14,1,2)` has already been solved.
- The exact tuple still appears to be treated as open in recent discussion, so this verify pass does not mark the intended statement as `REDISCOVERY`.
- However, the specific local package proved in this solve record is not frontier-novel. In particular, Wilbrink's 1984 paper on the hypothetical `(99,14,1,2)` graph treats the object as a partial quadrangle with lines of size `3` and `7` lines through each point, which already contains the same basic neighborhood-triangle geometry behind `G[N(v)] = 7K_2`, the `7` triangles through each vertex, and related local counting.
- Rediscovery conclusion: the solve record is best read as a correct re-derivation of known local consequences of the Conway `99`-graph axioms, not as a new solution of the open existence problem.

## verify_faithfulness

- The record is faithful about its actual mathematical content.
- It does not claim existence or nonexistence of an `srg(99,14,1,2)`. Its explicit solve-stage result is only a structural reduction, and that matches what is proved.
- There is no wrong-theorem drift in the main body: all deductions stay inside the exact `(99,14,1,2)` instance and use the intended `lambda = 1`, `mu = 2` definitions.
- The only necessary clarification is interpretive, not mathematical: this artifact verifies a partial theorem about any hypothetical witness, so the harness classification must remain `PARTIAL`, not `CANDIDATE` or `EXACT`.

## verify_proof

- First incorrect step found: none.
- The spectral calculation is correct. For strongly regular parameters `(99,14,1,2)`, the nontrivial eigenvalues are the roots of
  `x^2 + (mu - lambda)x + (mu - k) = x^2 + x - 12`,
  namely `3` and `-4`, with multiplicities `54` and `44`.
- The neighborhood argument is correct: for any fixed `v`, each `u in N(v)` has exactly one neighbor in `N(v)` because adjacent pairs have exactly one common neighbor, so `G[N(v)]` is `1`-regular on `14` vertices, hence `7K_2`.
- The labeling of `W(v)` is correct. Since `(x,v)` is a nonedge for `x in W(v)`, the pair has exactly `2` common neighbors, both in `N(v)`. They cannot lie on the same matching edge of `N(v)`, because then that edge would have two common neighbors, `v` and `x`, contradicting `lambda = 1`. So each `x in W(v)` determines exactly one unordered pair of distinct matching edges together with one endpoint on each, and the count `binom(7,2) * 4 = 84 = |W(v)|` makes this a bijection.
- The degree count for `G[W(v)]` is correct: each `x in W(v)` has exactly `2` neighbors in `N(v)`, so its remaining `12` neighbors lie in `W(v)`.
- The `tau_p(x)` / `tau_q(x)` argument is correct. For an edge `xp`, the unique third vertex in the triangle through `xp` cannot be `v`, cannot be the other `N(v)`-neighbor `q` because `pq` is a nonedge, and cannot lie in `N(v)` because `p` has only one neighbor in `N(v)`, namely its partner in the matching. So it lies in `W(v)`. The two vertices are distinct; otherwise `(p,q)` would have both `x` and that common vertex in `W(v)` in addition to `v`, violating `mu = 2`.
- The triangle split `231 = 7 + 84 + 140` is also correct. Each vertex lies in `14/2 = 7` triangles, so the graph has `99 * 7 / 3 = 231` triangles. Exactly `7` contain `v`. For each `p in N(v)`, the `12` neighbors of `p` inside `W(v)` form `6` matched pairs in `G[N(p)]`, each giving one triangle with exactly one vertex in `N(v)`. Summing over the `14` choices of `p` gives `84`, and these triangles are counted once because such a triangle has exactly one vertex in `N(v)`.

## verify_adversarial

- There is no checker or construction file in `artifacts/conway-99-graph`, so there was no code to rerun.
- I tried to break the key claims by targeting the likely weak points named in the record:
  the bijection `W(v) <-> x_{ij}^{alpha beta}`,
  the distinctness of `tau_p(x)` and `tau_q(x)`,
  and the `84`-triangle count.
- Those attacks did not expose a flaw. Each point reduces cleanly to the exact `lambda = 1` and `mu = 2` axioms plus the already proved fact that `N(v)` is a matching.
- Adversarial conclusion: the local package survives skeptical checking, but it remains only a necessary-condition theorem for a hypothetical witness.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- `classification = "PARTIAL"`
- `confidence = "high"`
- `lean_ready = false`
- Exact reason Lean is not ready: the record does not prove or disprove the intended statement `there exists an srg(99,14,1,2)`; it only verifies known local consequences of that hypothesis, and the bounded prior-art audit indicates those consequences are not novel.

## minimal_repair_if_any

- No repair was needed.
- The conservative harness action is to keep this artifact as a verified partial reduction and move on rather than escalating to Lean.
