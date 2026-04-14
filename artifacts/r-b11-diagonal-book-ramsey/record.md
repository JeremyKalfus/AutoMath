# Solve Record: The Exact Value of R(B11, B11)

## statement_lock
We work with the standard book graph definition: `B11` is the graph of 11 triangles sharing a common edge. Equivalently, a graph contains `B11` iff some edge has at least 11 common neighbors.

The active intended statement is:

- either prove that every graph `G` on 45 vertices has an edge with at least 11 common neighbors or a nonedge with at least 11 common nonneighbors, which would give `R(B11,B11)=45`;
- or construct a 45-vertex graph `G` in which every edge has at most 10 common neighbors and every nonedge has at most 10 common nonneighbors, which would give `R(B11,B11)=46`.

If a successful solve closes cleanly, the exact title theorem would be: `The exact value of R(B11,B11) is 45` or `The exact value of R(B11,B11) is 46`.

The packet already makes clear that a clean closure here would be about 70-90% of a short paper. My current assessment is that a complete proof or explicit 45-vertex witness would indeed land in that range, with only light packaging remaining.

## definitions
- `B11`: 11 triangles sharing one common edge.
- For an edge `uv` in `G`, let `c(uv)=|N(u) ∩ N(v)|`. Then `G` is `B11`-free iff `c(uv) <= 10` for every edge `uv`.
- For a nonedge `uv` in `G`, the complement contains a `B11` on the edge `uv` iff `u` and `v` have at least 11 common nonneighbors in `G`. So `\overline{G}` is `B11`-free iff every nonedge `uv` in `G` has at most 10 common nonneighbors.
- Let `n=45`, `m=e(G)`, `t` the number of triangles in `G`, and `\bar t` the number of triangles in `\overline{G}`.

Ambiguities / conventions / missing definitions:

- I am using the standard convention that the book size counts pages, so `B11` has 13 vertices in the abstract but only the shared-edge common-neighbor formulation matters here.
- The packet does not specify a canonical extremal-model notation, so I will use the graph/complement pair language directly.
- The packet does not include a pre-existing local witness construction, so any lower-end closure must emerge here from structural reasoning plus a verified concrete object.

## approach_A
Structural / invariant route.

For each edge `uv`, the edge can lie in at most 10 triangles, so

`3t = sum_{uv in E(G)} c(uv) <= 10m`.

Likewise, because every edge of `\overline{G}` lies in at most 10 triangles of `\overline{G}`,

`3\bar t <= 10(\binom{45}{2} - m) = 10(990-m)`.

Therefore

`t + \bar t <= 10m/3 + 10(990-m)/3 = 3300`.

Now invoke Goodman's identity:

`t + \bar t = \binom{45}{3} - (1/2) sum_v d(v)(44-d(v))`.

Because `x(44-x)` is maximized at `x=22`, we get

`sum_v d(v)(44-d(v)) <= 45 * 22 * 22 = 21780`,

so

`t + \bar t >= \binom{45}{3} - 21780/2 = 14190 - 10890 = 3300`.

Thus any 45-vertex graph avoiding both `B11` and its complement must achieve equality in both bounds. That forces all intermediate inequalities to be equalities.

Consequences of equality:

- every vertex has degree exactly 22;
- every edge lies in exactly 10 triangles;
- every nonedge lies in exactly 10 triangles of the complement, equivalently has exactly 10 common nonneighbors in `G`.

Once degrees are 22, a nonedge `uv` has exactly 11 common neighbors as well, because among the other 43 vertices we have

`43 = |N(u) ∩ N(v)| + |N(u)\setminus N(v)| + |N(v)\setminus N(u)| + |V \setminus (N(u) ∪ N(v) ∪ {u,v})|`

`= c + (22-c) + (22-c) + 10 = 54-c`,

so `c=11`.

Therefore any 45-vertex witness is necessarily a strongly regular graph with parameters

`(v,k,\lambda,\mu) = (45,22,10,11)`.

So the original problem has been reduced to:

- either produce an `srg(45,22,10,11)`, which would give `R(B11,B11)=46`;
- or prove that no `srg(45,22,10,11)` exists, which would give `R(B11,B11)=45`.

Self-check after Approach A:

- The triangle upper bound is exact and uses only the book-avoidance condition.
- The Goodman lower bound arithmetic checks out: `\binom{45}{3}=14190`.
- The equality case is rigid; there is no slack left once both bounds meet at 3300.

## approach_B
Construction / extremal / contradiction route.

After Approach A, the entire question collapses to the existence or nonexistence of `srg(45,22,10,11)`, equivalently a 45-vertex conference graph.

There are now two conceptually clean subroutes.

1. Construction route:
Find an explicit 45-vertex graph with parameters `(45,22,10,11)`. If such a graph is found and verified, then every edge has exactly 10 common neighbors and every nonedge exactly 10 common nonneighbors, so it is a certified 45-vertex obstruction and yields `R(B11,B11)=46`.

2. Contradiction route:
Show that no `srg(45,22,10,11)` can exist. Since Approach A proves every hypothetical 45-vertex obstruction must be exactly such a graph, nonexistence would force `R(B11,B11)=45`.

At the reasoning level, the construction route looks more plausible than a from-scratch nonexistence proof. The parameter set is feasible under the standard strongly regular relations, so there is no quick counting contradiction visible at this level. The natural contradiction route would likely need a deeper structural theorem about conference graphs or symmetric conference matrices, which is outside the current local packet unless I can derive it directly.

So the best next step is not a broad search. It is a tightly scoped attempt to realize or refute the unique extremal object forced by Approach A.

Self-check after Approach B:

- This is still the same one-shot lane; there is no concept drift.
- The construction route would directly produce the theorem-shaping counterexample.
- The contradiction route remains viable in principle, but I do not yet have a clean local argument for nonexistence.

## lemma_graph
1. `B11`-avoidance in `G` gives `3t <= 10m`.
2. `B11`-avoidance in `\overline{G}` gives `3\bar t <= 10(990-m)`.
3. Combining 1 and 2 gives `t+\bar t <= 3300`.
4. Goodman plus concavity of `d(44-d)` gives `t+\bar t >= 3300`.
5. Equality in 3 and 4 forces 22-regularity and exact edge / nonedge page counts.
6. Hence any 45-vertex obstruction is exactly an `srg(45,22,10,11)`.
7. Therefore the Ramsey problem is equivalent to the existence problem for that strongly regular graph.
8. A verified explicit `srg(45,22,10,11)` would settle the exact value at 46.
9. A proof of nonexistence of `srg(45,22,10,11)` would settle the exact value at 45.

## chosen_plan
The best path is:

1. Keep the structural reduction from Approach A as the core theorem skeleton.
2. Use minimal local code only to test concrete realization hypotheses for `srg(45,22,10,11)` or instantiate a local known construction if one is available in the environment.
3. If a verified witness appears, promote the current result to a counterexample-based closure candidate for `R(B11,B11)=46`.
4. If no witness appears from the bounded structured attempt, do not overclaim. The reduction to the unique extremal parameter set remains a strong partial result, but it is not by itself a solve.

The extra structure that would make the result paper-shaped if the main claim closes is very small:

- an explicit construction rule or explicit adjacency certificate for the 45-vertex witness, or
- a short impossibility theorem ruling out `srg(45,22,10,11)`.

Minimal remaining packaging work, if the main claim closes:

- write the reduction from books to the conference-graph parameter set cleanly;
- state the explicit witness or obstruction theorem;
- add one paragraph explaining why `n=11` is the first diagonal residue outside the number-theoretic criteria;
- include one small comparative remark with neighboring exact diagonal book cases.

## self_checks
- The active target remains exactly `R(B11,B11)`.
- I have not introduced SAT / ILP / CP-SAT / generic brute force before the reasoning stage.
- The reduction to `srg(45,22,10,11)` is theorem-facing and publication-relevant even if the full existence question stays open in this pass.
- If computation is used next, it will only be to test or verify a tightly narrowed candidate object.
- Post-code self-check: the computation stayed inside one rigid structured family question, namely symmetric Cayley realizations of `srg(45,22,10,11)` on groups of order 45.

## code_used
Yes, but only in a tightly justified form after the reasoning reduction.

I ran two exact searches over symmetric Cayley graphs of degree 22 on the only two abelian groups of order 45:

- `Z/45Z`;
- `Z/15Z x Z/3Z`.

For each group, I enumerated every symmetric generating set `D` of size 22 by choosing 11 inverse pairs from the 22 nonzero inverse pairs, so exactly `binom(22,11)=705432` candidates per group. For each candidate I checked the partial-difference-set conditions

- `|D ∩ (D+g)| = 10` when `g in D`,
- `|D ∩ (D+g)| = 11` when `g notin D`, `g != 0`.

Both searches were exhaustive inside their family and returned no solution.

So there is no symmetric abelian Cayley realization of `srg(45,22,10,11)` on any group of order 45.

## result
Current strongest result:

- Any 45-vertex graph witnessing `R(B11,B11)=46` must be a strongly regular graph with parameters `(45,22,10,11)`.
- Equivalently, the open instance is reduced to the existence or nonexistence of a 45-vertex conference graph.
- The two abelian Cayley families of order 45 were searched exactly and contain no such graph.

Because every group of order 45 is abelian, this exhausts all regular Cayley-action candidates on 45 vertices. Therefore any 45-vertex witness, if one exists, must be a non-Cayley `srg(45,22,10,11)`.

This is mathematically real and theorem-facing, but by itself it does not yet settle the Ramsey value. At this moment the result is still too thin to count as a micro-paper closure on its own.

## family_affinity
High. The reduction fits the diagonal book family exactly: the unresolved one-gap case collapses to a rigid extremal object in the same spirit as the known number-theoretic exact criteria. This is not a detached instance computation; it is a family-aware extremal characterization of the `n=11` residue.

## generalization_signal
Moderate. The Goodman-tightness argument is not special to `n=11` in spirit; it suggests a reusable template for one-gap diagonal book residues at odd orders `4n+1`, where simultaneous upper and lower triangle bounds may force a conference-graph-type extremal structure. What is special here is that the numbers align exactly at 45.

## proof_template_reuse
The reusable template is:

1. translate `B_n` / complement-`B_n` avoidance into per-edge monochromatic triangle bounds;
2. sum to bound `t+\bar t`;
3. compare with Goodman's identity;
4. read off equality conditions to force regularity and exact pair-intersection numbers;
5. identify the residue with a strongly regular or conference-graph existence problem.

That template should transfer to nearby diagonal one-gap book cases, though the equality numerics may not always close as tightly.

## candidate_theorem_slice
Candidate theorem slice:

`If G is a graph on 45 vertices with no copy of B11 and no copy of B11 in its complement, then G is strongly regular with parameters (45,22,10,11).`

Companion slice from the computation:

`No symmetric Cayley graph on a group of order 45 has parameters (45,22,10,11).`

This is the smallest clean theorem slice currently visible from the solve attempt.

## smallest_param_shift_to_test
The most informative nearby parameter shifts are:

- test whether the same Goodman-tightness reduction cleanly characterizes hypothetical obstructions at neighboring diagonal cases such as `B10` or `B12`;
- within the present case, move from abelian Cayley families to genuinely non-Cayley conference-graph constructions or obstruction arguments.

The first shift probes proof-template reuse; the second probes whether the present instance is actually on the `46` side after the regular-action route has been exhausted.

## why_this_is_or_is_not_publishable
This record is not yet publishable as a micro-paper. The reduction to `(45,22,10,11)` is meaningful, but the title theorem is still missing. For this candidate, the solve is publishable only if it closes the exact value.

If the main claim does close, then yes: the solve would already be roughly 70-90% of the paper. The title theorem is already fixed, and the remaining work is mostly exposition and comparison to the existing diagonal book table.

## paper_shape_support
If the main claim closes, the immediate paper-shaping support is:

- the exact title theorem `R(B11,B11)=45` or `R(B11,B11)=46`;
- the structural reduction above as the main lemma;
- one natural boundary remark: the `n=11` case is the first diagonal book residue not dispatched by the published number-theoretic criteria.

One immediate corollary / remark that would fall out is:

- any 45-vertex extremal obstruction is necessarily a conference graph, so the entire exact-value question for `R(B11,B11)` is equivalent to one rigid strongly regular parameter set;
- moreover, the regular abelian Cayley route is already eliminated, so any obstruction would have to be more structurally exceptional than the first obvious construction families.

## boundary_remark
Boundary remark:

The present reduction does not by itself say whether the 45-vertex conference graph exists. It isolates the exact obstruction class. The added exact search shows that the obstruction cannot come from any regular Cayley action on 45 vertices. That is strong enough to organize the rest of the proof, but not strong enough yet to certify the Ramsey value.

If a counterexample is eventually found, the part of the argument that scales is the Goodman-tightness reduction and the elimination of the obvious regular-action families; the part that does not scale automatically is the actual realization of the resulting non-Cayley strongly regular parameter set.

## likely_failure_points
- A local construction attempt for `srg(45,22,10,11)` may fail even if the graph exists, because the chosen template could be too narrow.
- Even exhaustive failure in the Cayley family does not prove global nonexistence.
- A full nonexistence proof likely needs more conference-graph structure than is presently in the local packet.
- If the only output here is the reduction theorem slice, the current package remains instance-preparatory rather than paper-ready.

## what_verify_should_check
- Check the Goodman identity arithmetic and the equality-case deductions carefully.
- Check the claim that every group of order 45 is abelian, since that is what upgrades the computational search from "two families" to "all regular Cayley families".
- Re-run the Cayley partial-difference-set search independently and confirm that both `Z/45Z` and `Z/15Z x Z/3Z` return no solution.
- If a concrete witness is later produced, verify every edge has exactly 10 common neighbors and every nonedge exactly 10 common nonneighbors.
- Check whether `srg(45,22,10,11)` is already a standard named conference graph construction in the literature; solve itself cannot mark rediscovery, but verify should inspect that point.
- If the solve ends with only the reduction theorem slice, verify should assess whether that slice is already known or is an easy folklore observation.
