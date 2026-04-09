# srg-69-20-7-5

## statement_lock
- Active slug: `srg-69-20-7-5`
- Title: `Does a strongly regular graph with parameters (69,20,7,5) exist?`
- Locked intended statement: there exists a simple undirected strongly regular graph `G` with parameters `(v,k,lambda,mu) = (69,20,7,5)`.
- Equivalent matrix identity used below:
  `A^2 = 20I + 7A + 5(J - I - A) = 15I + 2A + 5J`.
- The restricted eigenvalues are the roots of
  `u^2 + (mu - lambda)u + (mu - k) = 0`,
  so they are `5` and `-3`; the full spectrum is forced to be
  `20^1, 5^20, (-3)^48`.

Self-check:
- This is the exact existential statement from `selected_problem.md`.
- I am not claiming an exact construction or exact nonexistence proof in solve stage.

## definitions
- Fix a vertex `x`.
- Let `Delta = G[N(x)]`. Then `Delta` has `20` vertices and is `7`-regular.
- Let `Sigma = G[V \\ N[x]]`. Then `Sigma` has `48` vertices and is `15`-regular.
- Let `B` be the adjacency matrix of `Delta`, `C` the adjacency matrix of `Sigma`, and `M` the `20 x 48` incidence matrix between `N(x)` and `V \\ N[x]`.
- With the vertex order `x | N(x) | V \\ N[x]`, the adjacency matrix of `G` is
  ```text
  A =
  [0  1^T   0 ]
  [1   B    M ]
  [0  M^T   C ].
  ```
- Degree bookkeeping gives
  - `B 1 = 7 1`,
  - `M 1 = 12 1`,
  - `M^T 1 = 5 1`,
  - `C 1 = 15 1`.
- Expanding `A^2 = 15I + 2A + 5J` in blocks gives the exact relations
  - `B^2 + M M^T = 15I_20 + 2B + 5J_20`,
  - `B M + M C = 2M + 5J_(20x48)`,
  - `C^2 + M^T M = 15I_48 + 2C + 5J_48`.
- For each `z in Sigma`, let `S_z = N(z) ∩ N(x)`. Then each `S_z` is a `5`-subset of `V(Delta)`, and the `48` sets `S_z` are the columns of `M`.

Self-check:
- The sizes `20`, `48`, `7`, `12`, `5`, and `15` are all forced by the srg parameters.
- The three displayed block equations are exact consequences of the locked matrix identity.

## approach_A
Structural / invariant route.

- Let `u` be an eigenvector of `B` orthogonal to `1`, with eigenvalue `t`.
- Applying `B^2 + M M^T = 15I + 2B + 5J` to `u` gives
  `M M^T u = (15 + 2t - t^2)u = -(t - 5)(t + 3)u`.
- Hence every nontrivial eigenvalue of `B` lies in `[-3,5]`, and
  `M^T u = 0` exactly when `t` is `5` or `-3`.
- Transposing `B M + M C = 2M + 5J` gives
  `M^T B + C M^T = 2M^T`.
  Therefore, if `t` is a nonboundary eigenvalue of `B` and `M^T u != 0`, then
  `C(M^T u) = (2 - t)(M^T u)`.
- So the nonboundary spectra of `B` and `C` are transported by `t -> 2 - t`.

Write the nontrivial spectrum of `B` as
- `5^a, (-3)^b, t_1, ..., t_m`
with `m = 19 - a - b` and each `t_i` in `(-3,5)`.

Then the nontrivial spectrum of `C` must be
- `5^(b+3), (-3)^(a+25), 2 - t_1, ..., 2 - t_m`.

Derivation of the boundary multiplicities:
- `C` has `47 - m = 28 + a + b` nontrivial boundary slots.
- Using `trace(C) = 0` and `trace(C^2) = 48 * 15 = 720` together with the transported nonboundary eigenvalues forces the exact counts `5^(b+3)` and `(-3)^(a+25)`.

What this gives:
- an exact local spectral coupling between the first and second subconstituents,
- the fact that `Sigma` always has at least `3` eigenvalues equal to `5` and at least `25` equal to `-3`,
- but no contradiction by itself.

Self-check:
- The transport `t -> 2 - t` uses only the block equation `M^T B + C M^T = 2M^T` on the orthogonal complement of `1`.
- The multiplicity formulas were rechecked against both `trace` and `trace of square`.

## approach_B
Construction / extremal / contradiction route.

Work with the `48` blocks `S_z`, each of size `5`, on the `20`-vertex graph `Delta`.

For `u,v in V(Delta)`:
- if `u = v`, then `(M M^T)_{uu} = 12`,
- if `u ~ v` in `Delta`, then `(M M^T)_{uv}` equals the number of `z in Sigma` adjacent to both `u` and `v`, hence
  `(M M^T)_{uv} = 6 - (B^2)_{uv}`,
- if `u` and `v` are nonadjacent in `Delta`, then
  `(M M^T)_{uv} = 4 - (B^2)_{uv}`.

Let `T_Delta` be the number of triangles of `Delta`.
- Summing over edges of `Delta`, the total number of edges appearing inside the `48` blocks is
  `sum_z e(Delta[S_z]) = 70 * 6 - sum_{uv in E(Delta)} (B^2)_{uv} = 420 - 3 T_Delta`,
  because each triangle of `Delta` contributes `1` to `(B^2)_{uv}` on each of its `3` edges.

Now switch to the standard spherical representation in the `20`-dimensional eigenspace for eigenvalue `5`. Normalize so that
- `v_i · v_i = 1`,
- `v_i · v_j = 1/4` when `i` and `j` are adjacent,
- `v_i · v_j = -1/8` when `i` and `j` are nonadjacent.

Nonadjacent-pair block bound:
- Fix `z in Sigma`, put `S = S_z`, and let `e_z = e(Delta[S])`.
- If `s = sum_{y in S} v_y`, then `s · v_x = s · v_z = 5/4`.
- The projection of `s` onto `span(v_x + v_z)` has squared norm `25/7`.
- Also
  `||s||^2 = 5 + 2(e_z * 1/4 + (10 - e_z) * (-1/8)) = (10 + 3e_z) / 4`.
- Positivity of the orthogonal component gives
  `(10 + 3e_z) / 4 >= 25 / 7`,
  hence `e_z >= 2`.

Adjacent-pair neighborhood bound inside `Delta`:
- Fix `y in V(Delta)`, let `R_y = N_Delta(y)` with `|R_y| = 7`, and let `tau_y = e(Delta[R_y])`.
- If `r_y = sum_{u in R_y} v_u`, then `r_y · v_x = r_y · v_y = 7/4`.
- The projection of `r_y` onto `span(v_x + v_y)` has squared norm `49/10`.
- Also
  `||r_y||^2 = 7 + 2(tau_y * 1/4 + (21 - tau_y) * (-1/8)) = (7 + 3tau_y) / 4`.
- Therefore
  `(7 + 3tau_y) / 4 >= 49 / 10`,
  so `tau_y >= 5` for every `y`.

Consequences:
- Since every block `S_z` has at least `2` edges,
  `420 - 3 T_Delta >= 48 * 2 = 96`,
  hence `T_Delta <= 108`.
- Since every vertex of `Delta` lies in at least `5` triangles of `Delta`,
  `3 T_Delta = sum_y tau_y >= 20 * 5 = 100`,
  hence `T_Delta >= 34`.

So the first subconstituent must satisfy the exact interval
- `34 <= T_Delta <= 108`.

This narrows the local graph, but it does not force a contradiction.

Self-check:
- The block-edge identity `sum_z e(Delta[S_z]) = 420 - 3 T_Delta` is exact.
- The inequalities `e_z >= 2` and `tau_y >= 5` come from the global eigenspace geometry, not from a local search over graphs.

## lemma_graph
1. Lock the exact srg matrix identity `A^2 = 15I + 2A + 5J`.
2. Fix a vertex `x` and decompose `A` into the block matrices `B`, `M`, and `C`.
3. Use the block equations to derive the exact spectral transport `t -> 2 - t` from `B` to `C`.
4. Introduce the `48` five-element blocks `S_z = N(z) ∩ N(x)`.
5. Count the total number of block-internal edges as `420 - 3 T_Delta`.
6. Use the `20`-dimensional positive eigenspace representation to prove `e(Delta[S_z]) >= 2`.
7. Use the same representation to prove every vertex of `Delta` lies in at least `5` triangles of `Delta`.
8. Conclude `34 <= T_Delta <= 108`.
9. Note that this is a real structural restriction, but still not an exact contradiction.

Self-check:
- Steps `1` through `8` are unconditional.
- Step `9` is the correct conservative conclusion for the current pass.

## chosen_plan
- The best route here is the one-vertex spectral / incidence decomposition, because it gives exact formulas without starting a global graph search.
- That route produced two usable outputs:
  - an exact spectral coupling between the `20`-vertex local graph and the `48`-vertex second subconstituent,
  - and exact lower / upper bounds on the triangle count of the local graph.
- I then checked whether a weaker induced-subgraph eigenvalue condition alone could sharpen the `e(Delta[S_z]) >= 2` bound; it cannot.
- At this point the honest solve-stage conclusion is still `PARTIAL`, not an exact disproof.

Self-check:
- I did not switch to SAT, ILP, CP-SAT, or brute force over `69`-vertex graphs.
- The tiny computation only probed a bounded local hypothesis after the two handwritten routes above had stabilized.

## self_checks
- Statement check: everything above is about the exact tuple `(69,20,7,5)`.
- Spectral check: the global spectrum `20^1, 5^20, (-3)^48` was rederived from the locked matrix identity.
- Local-structure check: `Delta` is `7`-regular on `20` vertices and `Sigma` is `15`-regular on `48` vertices.
- Conservatism check: I obtained exact local restrictions, not an exact construction and not an exact impossibility proof.
- Lean check: Lean stays off because there is no strong exact candidate or exact disproof yet.

## code_used
- Yes, but only minimally and only after the two handwritten routes above stalled.
- File: `artifacts/srg-69-20-7-5/local_check_nonadjacent_5set.py`
- Purpose: enumerate all `5`-vertex graphs `F` and test the induced-subgraph condition `lambda_min(K̄_2 ∨ F) >= -3`, where `K̄_2` represents a fixed nonadjacent pair together with its `5` common neighbors.
- Result: the induced-subgraph eigenvalue condition alone already allows examples with exactly `1` internal edge in `F`, so the handwritten bound `e(Delta[S_z]) >= 2` genuinely uses the global `20`-dimensional eigenspace geometry and is stronger than plain interlacing.
- No SAT, ILP, CP-SAT, or global adjacency-matrix search was used.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Exact output from this pass:
  - the locked matrix identity is `A^2 = 15I + 2A + 5J`,
  - the spectrum is `20^1, 5^20, (-3)^48`,
  - the one-vertex decomposition yields exact block equations for `B`, `M`, and `C`,
  - the nonboundary eigenvalues of `B` are transported to those of `C` by `t -> 2 - t`,
  - if `B` has boundary multiplicities `5^a, (-3)^b`, then `C` has `5^(b+3), (-3)^(a+25)`,
  - the local triangle count satisfies `34 <= T_Delta <= 108`.
- I do not currently have an exact construction or an exact contradiction for the intended statement.

## likely_failure_points
- The current constraints are local and spectral; they may still be too coarse to rule out a genuinely irregular witness.
- The open tuple may require a sharper design-theoretic obstruction or a deeper star-complement argument than I found here.
- The bounded computation was deliberately weak; it only separated a global eigenspace argument from a weaker induced-subgraph interlacing heuristic.

## what_verify_should_check
- Recompute the locked identity `A^2 = 15I + 2A + 5J` and the spectrum `20^1, 5^20, (-3)^48`.
- Recheck the block equations for `B`, `M`, and `C`.
- Recheck the spectral transport statement: for `Bu = t u` with `u ⟂ 1` and `t notin {5,-3}`, prove `C(M^T u) = (2 - t)(M^T u)`.
- Recheck the derived multiplicity formulas `5^(b+3)` and `(-3)^(a+25)` for `C`.
- Recheck the Gram computations yielding `e(Delta[S_z]) >= 2` and `tau_y >= 5`.
- Rerun `artifacts/srg-69-20-7-5/local_check_nonadjacent_5set.py` and confirm that the induced-subgraph condition alone permits one-edge `5`-sets.
- During verify, perform the required bounded rediscovery search before deciding whether any of these local facts are already standard in the literature.

## verify_rediscovery
- PASS 1 used a bounded live search only.
- The canonical Brouwer-Van Maldeghem parameter table still lists `srg(69,20,7,5)` with a `?`, so the exact existence problem is not marked solved there.
- The same-source check did not uncover a theorem, proposition, example, observation, or corollary in that table/preprint settling this exact tuple; the nearby remarks are about related obstructions, not an exact resolution of `(69,20,7,5)`.
- A 2011 paper on strongly regular graphs with nontrivial automorphisms still lists `(69,20,7,5)` among unresolved cases with `v <= 100`.
- A 2009 tri-Cayley / tri-circulant paper only rules out that symmetry-restricted subclass, not all strongly regular graphs with these parameters.
- Verify conclusion for PASS 1: no rediscovery established within budget. This run is not a known-result reproving case on the evidence found.

## verify_faithfulness
- The solve artifact stays locked to the exact tuple `(69,20,7,5)` throughout.
- It does not claim an existence proof or a nonexistence proof. Its actual output is a package of exact necessary conditions on any hypothetical witness:
  - the global matrix identity and spectrum,
  - the block equations for `B`, `M`, `C`,
  - the spectral transport law from `Delta` to `Sigma`,
  - the local triangle bound `34 <= T_Delta <= 108`.
- I found no wrong-theorem drift, quantifier drift, or definition changes. The natural-language conclusion remains a conservative `PARTIAL`, not a disguised exact solve.

## verify_proof
- I rechecked the normalization `A^2 = 20I + 7A + 5(J-I-A) = 15I + 2A + 5J`; the forced spectrum is indeed `20^1, 5^20, (-3)^48`.
- The block identities for `B`, `M`, and `C` are the correct matrix expansion around a fixed vertex `x`.
- For `Bu = t u` with `u ⟂ 1`, the equation `B^2 + M M^T = 15I + 2B + 5J` gives
  `M M^T u = (15 + 2t - t^2)u = -(t-5)(t+3)u`.
  Hence `M^T u = 0` exactly on the boundary eigenvalues `t in {5,-3}`. Transposing `B M + M C = 2M + 5J` then gives
  `M^T B + C M^T = 2M^T`, so for nonboundary `t` one gets `C(M^T u) = (2-t)(M^T u)`.
- Using `trace(C) = 0`, `trace(C^2) = 48 * 15 = 720`, and `m = 19-a-b`, the claimed boundary multiplicities for `C`, namely `5^(b+3)` and `(-3)^(a+25)`, check out.
- The identity
  `sum_z e(Delta[S_z]) = 420 - 3 T_Delta`
  is correct: each of the `70` edges of `Delta` contributes `6 - (B^2)_{uv}`, and summing `(B^2)_{uv}` over edges counts each triangle three times.
- The Gram calculations in the `20`-dimensional positive eigenspace also check:
  - for a nonadjacent pair `x,z`, the projection of `s = sum_{y in S_z} v_y` onto `span(v_x+v_z)` has squared norm `25/7`, while `||s||^2 = (10+3e_z)/4`, forcing `e_z >= 2`;
  - for an adjacent pair `x,y`, the projection of `r_y = sum_{u in N_Delta(y)} v_u` onto `span(v_x+v_y)` has squared norm `49/10`, while `||r_y||^2 = (7+3tau_y)/4`, forcing `tau_y >= 5`.
- Therefore the derived interval `34 <= T_Delta <= 108` is sound.
- I found no incorrect step in the claims actually made in the solve artifact.

## verify_adversarial
- I reran `artifacts/srg-69-20-7-5/local_check_nonadjacent_5set.py`.
- Output was `{1: 10, 2: 45, 3: 120, 4: 210, 5: 252, 6: 210, 7: 120, 8: 45, 9: 10, 10: 1}`.
- This confirms the script's stated purpose: induced-subgraph interlacing alone still permits one-edge `5`-vertex common-neighbor graphs, so the handwritten lower bound `e(Delta[S_z]) >= 2` is genuinely stronger than that weaker heuristic.
- There is no exact construction or exact counterexample in the artifact to attack further. The computation supports only the limited claim just stated, and the writeup does not overread it.

## verify_verdict
- `verify_verdict = VERIFIED`
- `classification = PARTIAL`
- `confidence = high`
- `lean_ready = false`
- `next_action = do not run Lean; continue only if a sharper unconditional obstruction or a credible exact witness route appears`

## minimal_repair_if_any
- None. No conservative patch was needed.
