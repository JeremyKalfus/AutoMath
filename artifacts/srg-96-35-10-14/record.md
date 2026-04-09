## statement_lock

Target title: `Does a strongly regular graph with parameters (96,35,10,14) exist?`

Exact solve-stage target: analyze the existence of a simple undirected strongly regular graph `G` with

- `v = 96`
- `k = 35`
- `lambda = 10`
- `mu = 14`

Intended statement from the dossier: `No strongly regular graph with parameters (96,35,10,14) exists.`

Current solve-stage claim level: I do not have an exact proof or an exact disproof. The strongest honest classification from this pass is `PARTIAL`.

Self-check: the intended statement is locked to exact nonexistence for the tuple `(96,35,10,14)`, not to a broader family and not to a geometric reformulation.

## definitions

Let `A` be the adjacency matrix of `G`. Then the SRG identity is

```text
A^2 = kI + lambda A + mu (J - I - A) = 21 I - 4 A + 14 J.
```

Fix a vertex `x`.

- `Delta := G[N(x)]`, the first subconstituent, on `35` vertices.
- `Omega := G[V(G) \ (N(x) ∪ {x})]`, the second subconstituent, on `60` vertices.
- `B := A(Delta)`.
- `D := A(Omega)`.
- `C` is the `35 x 60` incidence matrix between `N(x)` and `Omega`.

Missing-definition check:

- The dossier already fixes the standard SRG convention, so there is no ambiguity about loops, multiple edges, or directed edges.
- The hint `pg(5,6,2)?` is treated only as a heuristic possibility, not as an allowed assumption.

Self-check: all later equations are derived only from the exact SRG tuple and these fixed definitions.

## approach_A

Structural / invariant route: use the SRG polynomial, the `x`-based block decomposition, and spectral transport between `Delta` and `Omega`.

1. Global spectrum.

   The restricted eigenvalues solve

   ```text
   t^2 + (mu - lambda)t + (mu - k) = t^2 + 4t - 21 = 0,
   ```

   so they are `3` and `-7`. The multiplicities are forced by trace:

   ```text
   35 + 3f - 7g = 0,   f + g = 95,
   ```

   hence

   ```text
   Spec(G) = 35^1, 3^63, (-7)^32.
   ```

2. Fixed-vertex block equations.

   With the partition `({x}, N(x), Omega)`,

   ```text
   A =
   [ 0   1^T   0 ]
   [ 1    B    C ]
   [ 0   C^T   D ].
   ```

   Comparing blocks in `A^2 = 21I - 4A + 14J` gives

   ```text
   B^2 + C C^T = 21I - 4B + 13J,
   B C + C D   = -4C + 14J,
   C^T C + D^2 = 21I - 4D + 14J.
   ```

   Diagonal entries immediately force:

   - `Delta` is `10`-regular on `35` vertices.
   - `Omega` is `21`-regular on `60` vertices.
   - Every vertex of `Delta` has `24` neighbors in `Omega`.
   - Every vertex of `Omega` has `14` neighbors in `Delta`.

3. Spectral transport.

   Let `u ⟂ 1` be a `B`-eigenvector with `Bu = theta u`.

   From `B^2 + C C^T = 21I - 4B + 13J` we get

   ```text
   C C^T u = (21 - 4 theta - theta^2) u = -(theta - 3)(theta + 7) u.
   ```

   Therefore every nontrivial eigenvalue of `B` lies in `[-7, 3]`.

   If `theta ∉ {3, -7}`, then `C^T u != 0`, and the mixed block equation gives

   ```text
   D (C^T u) = (-4 - theta) (C^T u).
   ```

   So nonboundary eigenvalues of `Delta` are transported to `Omega` by

   ```text
   theta  ->  -4 - theta.
   ```

4. Boundary multiplicities.

   Write

   - `a := mult_Delta(3)`
   - `b := mult_Delta(-7)`.

   Then the kernel of `C^T` on the `Delta` side is exactly the direct sum of the `3`- and `-7`-eigenspaces, so

   ```text
   rank(C) = 35 - a - b.
   ```

   The kernel of `C` on the `Omega` side has dimension

   ```text
   60 - rank(C) = 25 + a + b.
   ```

   Since `C^T C = 0` on a nontrivial `D`-eigenvector exactly when the eigenvalue is `3` or `-7`, the boundary eigenspaces of `Omega` have total dimension `25 + a + b`.

   Using `trace(D) = 0`, one gets

   ```text
   mult_Omega(-7) = a - 3,
   mult_Omega(3)  = b + 28.
   ```

   In particular `a >= 3`.

This route gives a clean package of necessary conditions, but no contradiction yet.

Self-check: the trace identities were rechecked explicitly:

- `35 + 3*63 - 7*32 = 0`
- `21*60 + sum(nontrivial D-eigenvalues) = 0`
- the formulas above preserve the total multiplicity `60`.

## approach_B

Construction / extremal / contradiction route: analyze common-neighbor sets around an edge or a nonedge, with the geometric `pg(5,6,2)` hint in mind but not assumed.

1. Adjacent pair `x ~ y`.

   Partition the other `94` vertices into

   - `U := N(x) ∩ N(y)`, so `|U| = 10`
   - `X := N(x) \ (U ∪ {y})`, so `|X| = 24`
   - `Y := N(y) \ (U ∪ {x})`, so `|Y| = 24`
   - `Z := V \ ({x,y} ∪ U ∪ X ∪ Y)`, so `|Z| = 36`

   If `s := 2 e(G[U])`, then the block-count identities force the average row sums

   - `U -> (s/10, 9 - s/10, 9 - s/10, 15 + s/10)`
   - `X -> ((90 - s)/24, 10 - (90 - s)/24, 13 - (90 - s)/24, 11 + (90 - s)/24)`
   - `Z -> ((150 + s)/36, 14 - (150 + s)/36, 14 - (150 + s)/36, 7 + (150 + s)/36)`

   A tiny exact quotient scan after the handwritten derivation found that the resulting averaged quotient interlaces the global SRG spectrum only when

   ```text
   s <= 30,
   ```

   i.e.

   ```text
   e(G[U]) <= 15.
   ```

2. Nonadjacent pair `x not~ y`.

   Partition the other `94` vertices into

   - `U := N(x) ∩ N(y)`, so `|U| = 14`
   - `X := N(x) \ U`, so `|X| = 21`
   - `Y := N(y) \ U`, so `|Y| = 21`
   - `Z := V \ ({x,y} ∪ U ∪ X ∪ Y)`, so `|Z| = 38`

   If again `s := 2 e(G[U])`, the same bookkeeping gives an averaged quotient matrix depending only on `s`. The same bounded interlacing check found that feasibility requires

   ```text
   8 <= s <= 58,
   ```

   i.e.

   ```text
   4 <= e(G[U]) <= 29.
   ```

3. Geometric heuristic.

   The tuple matches the point graph parameters of a hypothetical `pg(5,6,2)`. Nothing in the constraints above rules that geometry out. I tried to push the clique/common-neighbor route in that direction, but I could not force enough extra structure to obtain a contradiction.

This route gives local density restrictions, but still no exact obstruction.

Self-check: the pair-partition equations were rederived twice, specifically to avoid the kind of off-by-one common-neighbor mistake that often appears when toggling between adjacent and nonadjacent cases.

## lemma_graph

1. `A^2 = 21I - 4A + 14J`.
2. Therefore `Spec(G) = 35^1, 3^63, (-7)^32`.
3. Around a fixed vertex `x`, the first subconstituent `Delta` is `10`-regular on `35` vertices and the second subconstituent `Omega` is `21`-regular on `60` vertices.
4. The block equations imply `C C^T u = -(theta - 3)(theta + 7)u` for every `B`-eigenvector `u ⟂ 1`.
5. Hence every nontrivial eigenvalue of `Delta` lies in `[-7,3]`.
6. If `theta ∉ {3,-7}` is a `Delta`-eigenvalue, then `-4-theta` is an `Omega`-eigenvalue.
7. If `a = mult_Delta(3)` and `b = mult_Delta(-7)`, then `mult_Omega(-7) = a - 3` and `mult_Omega(3) = b + 28`.
8. Around an edge, the `10`-vertex common-neighbor graph must satisfy `e(U) <= 15`.
9. Around a nonedge, the `14`-vertex common-neighbor graph must satisfy `4 <= e(U) <= 29`.
10. These are real necessary conditions but they do not yet contradict each other.

## chosen_plan

I chose approach A as the main route because it produces exact algebraic constraints that are global, reusable in verification, and independent of any speculative geometry.

I still pushed approach B far enough to test whether the local common-neighbor sets were already impossible. They were not. Since the dossier already warned about hidden geometry, that failure matters: it means the current data is more consistent with a constrained candidate family than with an immediate local contradiction.

Self-check: this plan stayed reasoning-first. The only computation came after the block formulas were already fixed and only tested a one-parameter interlacing condition for averaged quotient matrices.

## self_checks

- Step 1, statement lock: exact tuple and intended nonexistence statement fixed with no family drift.
- Step 2, global spectrum: rechecked against both the quadratic equation and the trace equation.
- Step 3, block decomposition: rechecked diagonal entries to confirm the `10`-regular / `21`-regular subconstituent degrees.
- Step 4, transport law: rechecked the sign in `theta -> -4 - theta`.
- Step 5, multiplicity formulas: rechecked with total-dimension and trace constraints on `Omega`.
- Step 6, pair partitions: rederived the adjacent and nonadjacent cases separately to avoid counting `x` or `y` incorrectly.
- Step 7, code usage: the bounded scan only tested the derived one-parameter quotients; it did not search over graphs, SAT instances, or brute-force constructions.

## code_used

Yes, but only minimally.

I used one tiny `python3` command-line scan, after the reasoning stage, to diagonalize the averaged quotient matrices coming from:

- the adjacent-pair partition `(x, y, U, X, Y, Z)` with `|U| = 10`
- the nonadjacent-pair partition `(x, y, U, X, Y, Z)` with `|U| = 14`

The scan did not search for graphs. It only checked which values of the single parameter `s = 2e(G[U])` keep the quotient eigenvalues within the interlacing window imposed by `35, 3, -7`.

## result

Classification: `PARTIAL`.

What I can support exactly from this solve pass:

- the forced global spectrum `35^1, 3^63, (-7)^32`
- the exact first/second-subconstituent degree data `10` and `21`
- the exact spectral transport law `theta -> -4-theta`
- the exact boundary multiplicity formulas
- the local common-neighbor edge bounds `e(U) <= 15` for adjacent pairs and `4 <= e(U) <= 29` for nonadjacent pairs

What I cannot currently support:

- a contradiction proving nonexistence
- a construction or witness supporting existence
- a Lean-ready exact theorem beyond the necessary conditions above

So the intended nonexistence statement remains unresolved in this solve artifact.

## likely_failure_points

- The most likely mathematical gap is that the current invariant package is too weak: it constrains `Delta` and `Omega` but does not yet force an impossible spectrum or impossible local graph.
- The geometric hint may be genuinely relevant. If every surviving configuration naturally organizes around a `pg(5,6,2)`-type incidence structure, then a purely local contradiction may never appear without stronger geometric input.
- The averaged quotient interlacing bounds are necessary conditions only. They are useful, but they are not close to sufficient.
- I did not derive a clique-geometry theorem or a forbidden-subgraph theorem strong enough to close the argument.

## what_verify_should_check

- Recompute the global spectrum and multiplicities from the SRG tuple; this is the base dependency for everything else.
- Recheck the three block equations for the `({x}, N(x), Omega)` partition.
- Recheck the transport law `theta -> -4-theta` and the formulas `mult_Omega(-7) = a - 3`, `mult_Omega(3) = b + 28`.
- Recheck the adjacent-pair and nonadjacent-pair partition bookkeeping carefully, especially which of `x` or `y` is counted as a common neighbor in each case.
- Rerun the tiny quotient scan and confirm the bounds `e(U) <= 15` and `4 <= e(U) <= 29`.
- Keep Lean off unless verification discovers a genuinely sharper contradiction than the current necessary conditions.

## verify_rediscovery

I used the allowed bounded web pass on the exact tuple `(96,35,10,14)`, reordered tuple notation, the canonical Brouwer table, the `pg(5,6,2)` hint, and one older tuple-specific status thread. Within that capped pass I did not find any theorem, proposition, example, observation, or corollary settling the exact intended statement.

The strongest source remains Brouwer's `51-100 vertices` SRG table, which still marks `(96,35,10,14)` with `?`. A tuple-specific secondary hit in the automorphism literature also treated `(96,35,10,14)` as one of the unresolved parameter sets rather than as a solved instance. So this verify pass does not establish rediscovery.

Conclusion for PASS 1: `verify_verdict` is not `REDISCOVERY`.

## verify_faithfulness

The solve artifact is faithful to what it actually proves. It does not claim the intended exact nonexistence statement has been established. Instead it explicitly labels the run `PARTIAL` and limits its conclusions to necessary conditions forced by the SRG equations and the two quotient scans.

I did not find wrong-theorem drift, quantifier drift, changed definitions, or a swap from exact nonexistence to a nearby proxy claim. The natural-language summary and the mathematical content match.

## verify_proof

I rederived the core algebra from scratch.

- From `A^2 = kI + lambda A + mu(J-I-A)` with `(v,k,lambda,mu) = (96,35,10,14)`, the normalized identity is exactly `A^2 = 21I - 4A + 14J`.
- The restricted eigenvalues are exactly `3` and `-7`, and the trace equations force multiplicities `63` and `32`.
- In the vertex partition `({x}, N(x), Omega)`, the diagonal block identities force `Delta` to be `10`-regular on `35` vertices, `Omega` to be `21`-regular on `60` vertices, every vertex of `Delta` to have `24` neighbors in `Omega`, and every vertex of `Omega` to have `14` neighbors in `Delta`.
- For a `B`-eigenvector `u ⟂ 1` with `Bu = theta u`, the identity `C C^T u = -(theta-3)(theta+7)u` is correct, so every nontrivial `Delta`-eigenvalue lies in `[-7,3]`.
- If `theta` is a nonboundary `Delta`-eigenvalue, then `C^T u != 0` and `D(C^T u) = (-4-theta) C^T u`, so the transport law `theta -> -4-theta` is correct.
- Writing `a = mult_Delta(3)` and `b = mult_Delta(-7)`, the boundary multiplicity formulas `mult_Omega(-7) = a - 3` and `mult_Omega(3) = b + 28` follow correctly from rank plus trace bookkeeping.

I did not find an incorrect step in the claims the solve artifact actually makes. The first incorrect step is therefore: none found inside the partial-claim envelope.

## verify_adversarial

There was no saved checker file for this slug, so I reran the bounded computations independently with fresh one-off Python snippets.

- For the adjacent-pair partition `(x,y,U,X,Y,Z)` with `|U| = 10`, the averaged quotient spectrum stays inside the SRG interlacing window exactly for `s = 2e(U) <= 30`, reproducing `e(U) <= 15`.
- For the nonadjacent-pair partition with `|U| = 14`, the independently reconstructed quotient matrix reproduces the feasible range `8 <= s <= 58`, hence `4 <= e(U) <= 29`.

These checks support the recorded necessary conditions but do not produce any contradiction. They also do not supply a witness for existence.

## verify_verdict

`VERIFIED`.

Meaning: the solve artifact appears mathematically sound as a `PARTIAL` analysis, but it does not prove the intended exact nonexistence statement. The frontier status still appears open within the bounded rediscovery budget, so this run remains far short of Lean readiness.

## minimal_repair_if_any

No substantive repair is needed. The only conservative clarification worth noting is that, in the nonadjacent-pair quotient reconstruction, the `Z -> Z` average row sum is `(448 + s)/38`; using that value reproduces the recorded range `8 <= s <= 58`. The solve artifact did not state that row explicitly, so no correction to the existing writeup is required.
