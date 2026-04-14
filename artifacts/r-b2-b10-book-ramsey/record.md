# Solve Record: The Exact Value of R(B2, B10)

## statement_lock
Work with a graph `G` on `25` vertices. Let `B_t` denote the book graph consisting of `t` triangles sharing a common edge.

The intended exact statement is:

- either prove that every `25`-vertex graph `G` contains `B2` or its complement contains `B10`, which would show `R(B2, B10) = 25`;
- or construct a `25`-vertex graph `G` with no `B2` and with complement containing no `B10`, which would show `R(B2, B10) = 26`.

Equivalently:

- `G` is `B2`-free iff every edge of `G` has at most one common neighbor;
- `\bar G` is `B10`-free iff every nonedge `uv` of `G` has at most `9` common nonneighbors in `G`.

If the main claim closes, the exact title theorem would be `The Exact Value of R(B2, B10)`. A successful solve here would already be about `70-90%` of a paper; the packet estimate `0.79` still looks right.

## definitions
For vertices `u,v` in `G`:

- `N(v)` is the open neighborhood of `v`;
- `d(v) = |N(v)|`;
- for an edge `uv`, let `c_G(uv) = |N(u) \cap N(v)|`;
- for a nonedge `uv`, let `\bar c_G(uv)` be the number of common nonneighbors of `u,v` in `G`, so `\bar c_G(uv) = |V(G) \setminus (N(u) \cup N(v) \cup {u,v})|`.

Conventions used below:

- `B2`-free means `c_G(uv) <= 1` for every edge `uv`;
- `\bar G` `B10`-free means `\bar c_G(uv) <= 9` for every nonedge `uv`;
- `n = 25`, `m = e(G)`, and `\bar m = \binom{25}{2} - m = 300 - m`.

Ambiguities or missing definitions to keep in view:

- the local packet does not include the published `24`-vertex witness itself, so I cannot run the recommended one-vertex-extension analysis directly;
- the exact notation from the cited papers is not locally present, so I am using the standard book-graph convention `B_t = K_2 + \overline{K_t}`;
- because solve is web-disabled here, any apparent exact closure must still be treated as a solve-stage claim pending later verification.

## approach_A
Structural / invariant route.

Assume a counterexample `G` exists on `25` vertices with no `B2` and no complement `B10`.

First local consequence:

- for every vertex `v`, the induced graph `G[N(v)]` has maximum degree at most `1`.

Reason: if `x in N(v)` had two neighbors `y,z` inside `N(v)`, then the edge `vx` would have two common neighbors `y,z`, giving a `B2`. So every neighborhood is a disjoint union of isolated vertices and single edges.

Immediate corollaries:

- every neighborhood is triangle-free;
- every edge lies in at most one triangle, so `3T <= m` for the triangle count `T`;
- the number of edges inside `N(v)` is at most `d(v)/2`.

Second local consequence:

- for every nonedge `uv`, `d(u) + d(v) - |N(u) \cap N(v)| >= 14`.

This is just the complement-book condition rewritten from `\bar c_G(uv) <= 9` on `23` available third vertices.

Third consequence: independent sets are small.

- `alpha(G) <= 11`.

Indeed, if `G` had an independent set of size `12`, then any pair inside it would have at least `10` common nonneighbors, producing `B10` in the complement.

Fourth consequence: low-degree vertices cannot spread out.

- if `uv` is a nonedge, then `d(u) + d(v) >= 14`;
- hence vertices of degree at most `6` form a clique;
- since `K_4` already contains `B2`, there can be at most `3` vertices of degree at most `6`.

Global counting slice.

Let

- `S = sum \bar c_G(uv)` over all nonedges `uv`.

If `\bar G` is `B10`-free, then `S <= 9 \bar m`.

On the other hand,

- `S = sum_{uv notin E} (23 - d(u) - d(v) + |N(u) \cap N(v)|)`;
- `sum_{uv notin E} (d(u)+d(v)) = sum_v d(v)(24-d(v))`;
- `sum_{uv notin E} |N(u) \cap N(v)| = sum_v \binom{d(v)}{2} - sum_{uv in E} c_G(uv)`;
- because `G` is `B2`-free, `sum_{uv in E} c_G(uv) <= m`.

Therefore

`S >= 23(300-m) - sum_v d(v)(24-d(v)) + sum_v \binom{d(v)}{2} - m`

which simplifies to

`S >= 6900 - 73m + (3/2) sum_v d(v)^2`.

Combining this with `S <= 9(300-m)` yields the necessary inequality

`(3/2) sum_v d(v)^2 <= 64m - 4200`.

Using Cauchy, `sum_v d(v)^2 >= 4m^2/25`, so any counterexample must satisfy

`117 <= m <= 150`.

So any `25`-vertex witness must live in a fairly narrow density window with average degree between `9.36` and `12`.

Self-check after Approach A:

- the neighborhood-max-degree claim is solid and is the strongest elementary local restriction I have;
- the `alpha(G) <= 11` and low-degree-clique consequences are solid;
- the edge-count window `117 <= m <= 150` is a real theorem slice, but it does not by itself force a contradiction.

## approach_B
Construction / extremal / contradiction route.

Start from the most natural dense `B2`-free template: complete bipartite graphs.

- `K_{12,13}` is triangle-free, hence `B2`-free.
- But for two vertices in the part of size `12`, the other `10` vertices of that part are common nonneighbors.
- So `K_{12,13}` already creates a complement `B10`.

That makes `K_{12,13}` the threshold obstruction: it is exactly one unit too weak on the complement side.

This suggests two possibilities.

1. `R(B2, B10) = 25`:
The extremal picture may say that every `25`-vertex `B2`-free graph is forced close enough to a bipartite split that some nonedge still has `10` common nonneighbors.

2. `R(B2, B10) = 26`:
There may exist a tuned quasi-regular graph near degree `10-12` where every edge has at most one common neighbor and every nonedge pair nearly covers the graph.

Why the naive repair of `K_{12,13}` is difficult:

- adding edges inside a part immediately risks huge books unless many cross edges are simultaneously deleted;
- deleting only a few cross edges does not fix the `10` common-nonneighbor issue on same-part pairs;
- so any actual witness is likely global and highly balanced, not a local perturbation of a complete bipartite graph.

This makes a bounded structured search reasonable after the reasoning stage. The natural test family is near-regular circulant or otherwise symmetric `25`-vertex graphs, because the necessary density window already points toward a balanced construction rather than a sparse gadget glued to the published `24`-vertex witness.

Self-check after Approach B:

- the extremal baseline `K_{12,13}` really does explain why the window is tight;
- the conclusion is heuristic, not a proof;
- I do not yet have an argument excluding globally tuned balanced witnesses.

## lemma_graph
Proof skeleton if the answer is `25`.

1. Assume `G` is a `25`-vertex graph with no `B2` and no complement `B10`.
2. Use the neighborhood lemma to get `G[N(v)]` of maximum degree `1` for all `v`.
3. Deduce `alpha(G) <= 11`, the nonedge degree-sum constraint, and the edge-count window `117 <= m <= 150`.
4. Strengthen the degree analysis enough to show that some nonedge must have at least `10` common nonneighbors.
5. Conclude `\bar G` contains `B10`, contradiction.

Proof skeleton if the answer is `26`.

1. Produce an explicit `25`-vertex graph `G`.
2. Verify for every edge `uv` that `|N(u) \cap N(v)| <= 1`.
3. Verify for every nonedge `uv` that `\bar c_G(uv) <= 9`.
4. Conclude `G` has no `B2` and `\bar G` has no `B10`, so `R(B2, B10) >= 26`.
5. Combine with the known upper bound `R(B2, B10) <= 26` to get exactness.

At present the local theorem slice I can honestly defend is:

- any `25`-vertex witness for `R(B2, B10) = 26` must satisfy `117 <= e(G) <= 150`, `alpha(G) <= 11`, and every vertex neighborhood must induce a matching plus isolated vertices.

## chosen_plan
Best current path:

- keep the structural slice above as the rigorous backbone;
- use one bounded, symmetry-biased search to test whether a `25`-vertex witness exists in a plausible near-regular family;
- if a witness appears, verify it exactly;
- if no witness appears in that family, report that the search only narrows the construction side and does not prove `R(B2, B10) = 25`.

This is the best use of the solve budget because the purely structural route has not yet crossed the final contradiction line, while the construction route has a very compact exact-verification criterion.

## self_checks
- Statement lock is exact and binary: either force `B10` in the complement on `25` vertices or build one `25`-vertex obstruction.
- All current rigorous claims are internal graph-theoretic consequences of the forbidden-book conditions.
- I have not claimed anything that depends on the missing `24`-vertex witness.
- If code is used, it should stay bounded and serve only witness search / verification.
- After the bounded searches below, I still do not have a proof either way; the search outcomes are heuristic evidence only.

## code_used
Yes, bounded search only.

I ran two compact experiments.

1. Exhaustive circulant-family search on `25` vertices.
   Every symmetric circulant graph on `Z/25Z` was tested.
   Result: no hit. No circulant graph satisfied both
   `max_{uv in E} |N(u) cap N(v)| <= 1`
   and
   `max_{uv notin E} \bar c_G(uv) <= 9`.

2. Bounded local search over general graphs.
   I used a penalty function for edge-book and complement-book violations, with one unrestricted run and one fixed-edge run at the structural lower bound `m = 117`.

   Best unrestricted near-miss:
   - `m = 116`
   - degree sequence `9^18 10^7`
   - `42` bad edges, worst edge common-neighbor count `3`
   - `37` bad nonedges, worst common-nonneighbor count `10`

   Best fixed-edge search at `m = 117`:
   - no hit
   - best state still had edge-book and complement-book violations, with worst values `4` and `12`.

These computations do not settle the problem. Their only honest role is to say that I did not find a symmetric or near-boundary witness quickly, and that the unrestricted search drifted to `116` edges, just below the rigorous lower bound for any true `25`-vertex obstruction.

## result
Current state before any bounded experiment:

- no exact solve yet;
- real structural progress: a hypothetical `25`-vertex obstruction must sit in a narrow density window and satisfy strong local sparsity in every neighborhood;
- this already suggests that if the problem closes positively, the supporting theorem slice is likely about the constrained shape of any `25`-vertex near-extremal witness.

State after the bounded experiments:

- still no exact solve;
- no witness was found in the full circulant family;
- no witness was found by bounded local search in the general `25`-vertex space explored here;
- the strongest near-miss found by unrestricted search sat at `116` edges, which is suggestive because the rigorous counting slice forces any actual witness to have at least `117` edges.

What part of the argument scales:

- the neighborhood-sparsity lemma and the global common-nonneighbor summation method should scale to nearby `R(B2, Bn)` residues;
- the nonedge degree-sum constraint `d(u)+d(v)-|N(u) cap N(v)| >= 14` is the right local inequality for any future exact classification of the `25`-vertex case.

What does not scale cleanly yet:

- the bounded search evidence is not proof and does not transfer beyond the tested families or time budget;
- the current counting slice does not yet classify all graphs in the feasible density window `117 <= m <= 150`.

The theorem slice suggested by the present attempt is still:

- any `25`-vertex obstruction must be a near-regular, medium-density graph with matching-like neighborhoods and no large independent set.

The next parameter shifts that would help most are:

- import the published `24`-vertex witness and classify all `25th`-vertex extensions exactly;
- or run an exact search restricted to the proven feasible band `117 <= m <= 150`.

At the moment this package is still closer to an instance-level obstruction analysis than to a paper-shaped claim. It is not yet enough for the micro-paper lane.

## family_affinity
High. The target is a one-gap exact-value problem in a named `B2`-versus-`Bn` table, and the current slice still speaks the language of the family: neighborhood shape, density window, and complement-cover constraints.

## generalization_signal
Moderate. The counting argument does not use `10` very delicately; the same template should produce analogous density windows for `R(B2, Bn)` one-gap residues by replacing the `9` threshold with `n-1`.

## proof_template_reuse
The reusable template is:

- translate `B2`-free into a local neighborhood sparsity condition;
- translate complement `Bn`-free into a nonedge cover inequality;
- sum common-nonneighbor counts over all nonedges to force a narrow edge-density regime;
- then either classify or computationally test the remaining structured witness space.

## candidate_theorem_slice
Candidate theorem slice:

`If G is a 25-vertex graph with no B2 and with complement containing no B10, then every neighborhood G[N(v)] has maximum degree at most 1, alpha(G) <= 11, and 117 <= e(G) <= 150.`

This is theorem-shaped and exact, but it is still weaker than the desired title theorem.

## smallest_param_shift_to_test
The most informative nearby shifts are:

- `R(B2, B9)`, because the same proof template may already explain why that window is wider;
- a direct search for whether the same style of `25`-vertex witness constraints persists when the complement threshold is lowered from `10` to `9`.

## why_this_is_or_is_not_publishable
Not publishable yet.

- A full solve here would still be about `79%` of a paper, and the title theorem would be immediate.
- The current result is still too thin for the micro-paper lane by itself because it does not settle the exact value.
- Minimal remaining packaging work after a genuine solve would be short: write the forcing proof or explicit obstruction, include one comparison paragraph with nearby `B2` versus `Bn` values, and append a compact verification table or edge list.

## paper_shape_support
If the main claim closes, the smallest extra structure that makes it paper-shaped is:

- one clean supporting proposition giving the neighborhood-sparsity and density-window constraints for a hypothetical `25`-vertex obstruction;
- one immediate remark comparing the exact answer with `R(B2, B8)=21` and the current `B2` versus `B9` window;
- one short verification appendix if the result is constructive.

## boundary_remark
Natural boundary remark:

- `K_{12,13}` is triangle-free and therefore `B2`-free, but it fails exactly at the complement-book threshold because same-part pairs have `10` common nonneighbors. So the open pair `R(B2, B10)` sits right at the point where the obvious bipartite construction stops working.

## likely_failure_points
- The structural inequalities may still leave a nonempty family of balanced quasi-regular witnesses.
- A bounded symmetric search might miss an asymmetric witness even if `R(B2, B10) = 26`.
- Without the published `24`-vertex obstruction in the repo, I cannot execute the recommended extension-classification attack directly.
- The current counting slice may need one more genuinely sharp lemma, not just more search, to turn the `117 <= m <= 150` window into a contradiction.

## what_verify_should_check
- Every algebraic step in the common-nonneighbor counting inequality.
- Whether the candidate theorem slice above already appears implicitly in existing literature.
- If a witness is later found, verify both forbidden-book conditions independently from the saved edge list.
- If no witness is found by bounded search, do not over-read that as evidence of exactness.
- Check whether the “search pressure at `116` edges” phenomenon persists under an exact solver or was just an artifact of the hill-climber.
