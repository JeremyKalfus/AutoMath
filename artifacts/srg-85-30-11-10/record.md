# srg-85-30-11-10

## statement_lock
- Active slug: `srg-85-30-11-10`
- Title: `Does a strongly regular graph with parameters (85,30,11,10) exist?`
- Locked object: a simple undirected graph `G` on `85` vertices with parameters `(v,k,lambda,mu) = (85,30,11,10)`.
- Locked intended statement for this solve pass: no such graph exists.
- Exact matrix identity:
  `A^2 = 30I + 11A + 10(J - I - A) = 20I + A + 10J`.
- The restricted eigenvalues are the roots of
  `u^2 + (mu - lambda)u + (mu - k) = u^2 - u - 20`,
  so they are `5` and `-4`. The full spectrum is therefore
  `30^1, 5^34, (-4)^50`.

Self-check:
- This is the exact tuple from [selected_problem.md](/Users/jeremykalfus/CodingProjects/AutoMath/selected_problem.md).
- I am not weakening the target to a symmetry-restricted subclass.

## definitions
- Fix a vertex `x`.
- Let `Delta = G[N(x)]`. Then `Delta` has `30` vertices and is `11`-regular.
- Let `Sigma = G[V \\ N[x]]`. Then `Sigma` has `54` vertices and is `20`-regular.
- With vertex order `x | N(x) | V \\ N[x]`, write
  ```text
  A =
  [0  1^T   0 ]
  [1   B    M ]
  [0  M^T   C ].
  ```
- Degree bookkeeping gives
  - `B 1 = 11 1`,
  - `M 1 = 18 1`,
  - `M^T 1 = 10 1`,
  - `C 1 = 20 1`.
- Expanding `A^2 = 20I + A + 10J` in blocks gives
  - `B^2 + M M^T = 20I_30 + B + 10J_30`,
  - `B M + M C = M + 10J_(30x54)`,
  - `C^2 + M^T M = 20I_54 + C + 10J_54`.
- For each `z in Sigma`, let `S_z = N(z) ∩ N(x)`. Then each `S_z` is a `10`-subset of `V(Delta)`, and the `54` sets `S_z` are the columns of `M`.
- For each `y in Delta`, let `R_y = N_Delta(y)`. Then each `R_y` has size `11`.

Self-check:
- The sizes `30`, `54`, `11`, `18`, `10`, and `20` are all forced by the SRG parameters.
- The three block equations are exact consequences of the locked matrix identity.

## approach_A
Structural / invariant route.

- Let `u` be an eigenvector of `B` orthogonal to `1`, with eigenvalue `t`.
- Applying `B^2 + M M^T = 20I + B + 10J` to `u` gives
  `M M^T u = (20 + t - t^2)u = -(t - 5)(t + 4)u`.
- Hence every nontrivial eigenvalue of `B` lies in `[-4,5]`, and `M^T u = 0` exactly when `t` is `5` or `-4`.
- Transposing `B M + M C = M + 10J` gives
  `M^T B + C M^T = M^T`.
  Therefore, if `t` is a nonboundary eigenvalue of `B` and `M^T u != 0`, then
  `C(M^T u) = (1 - t)(M^T u)`.
- So the nonboundary spectra of `Delta` and `Sigma` are coupled by the transport rule `t -> 1 - t`.

Write the nontrivial spectrum of `B` as
- `5^a, (-4)^b, t_1, ..., t_m`
with `m = 29 - a - b` and each `t_i` in `(-4,5)`.

Then the nontrivial spectrum of `C` must be
- `5^(b+4), (-4)^(a+20), 1 - t_1, ..., 1 - t_m`.

Reason:
- `C` has `53 - m = 24 + a + b` boundary slots left after transporting the `t_i`.
- Using `trace(C) = 0` and the transported sum
  `sum_i (1 - t_i) = m - sum_i t_i = 40 + 4a - 5b`
  forces the exact boundary multiplicities `5^(b+4)` and `(-4)^(a+20)`.

What this gives:
- an exact one-vertex spectral coupling between the `30`-vertex local graph and the `54`-vertex second subconstituent,
- the unconditional facts that `Sigma` has at least `4` eigenvalues equal to `5` and at least `20` equal to `-4`,
- but no contradiction by itself.

Self-check:
- The transport `t -> 1 - t` uses only the block equation `M^T B + C M^T = M^T`.
- The multiplicity formulas were rechecked against both the dimension count and the trace equation.

## approach_B
Construction / extremal / contradiction route.

Work with the `54` blocks `S_z`, each of size `10`, inside the `30`-vertex graph `Delta`.

For `u,v in V(Delta)`:
- if `u = v`, then `(M M^T)_{uu} = 18`,
- if `u ~ v` in `Delta`, then `(M M^T)_{uv}` equals the number of `z in Sigma` adjacent to both `u` and `v`, hence
  `(M M^T)_{uv} = 10 - (B^2)_{uv}`,
- if `u` and `v` are nonadjacent in `Delta`, then
  `(M M^T)_{uv} = 9 - (B^2)_{uv}`.

Let `T_Delta` be the number of triangles of `Delta`.
- Summing over edges of `Delta`, the total number of edges appearing inside the `54` blocks is
  `sum_z e(Delta[S_z]) = 165 * 10 - sum_{uv in E(Delta)} (B^2)_{uv} = 1650 - 3 T_Delta`,
  because `Delta` has `30 * 11 / 2 = 165` edges and each triangle contributes `1` to `(B^2)_{uv}` on each of its `3` edges.

Now use the standard spherical representation in the `34`-dimensional eigenspace for eigenvalue `5`. Normalize so that
- `v_i · v_i = 1`,
- `v_i · v_j = 1/6` when `i` and `j` are adjacent,
- `v_i · v_j = -1/9` when `i` and `j` are nonadjacent.

Nonadjacent-pair block bound:
- Fix `z in Sigma`, put `S = S_z`, and let `e_z = e(Delta[S])`.
- If `s = sum_{y in S} v_y`, then `s · v_x = s · v_z = 10/6 = 5/3`.
- The vector `s` is orthogonal to `v_x - v_z`, so its projection onto `span(v_x, v_z)` lies on the line `span(v_x + v_z)`.
- Since `||v_x + v_z||^2 = 2 - 2/9 = 16/9`, that projection has squared norm
  `((s · (v_x + v_z))^2) / ||v_x + v_z||^2 = (10/3)^2 / (16/9) = 25/4`.
- Also
  `||s||^2 = 10 + 2(e_z * 1/6 + (45 - e_z) * (-1/9)) = 5 e_z / 9`.
- Positivity of the orthogonal component gives
  `5 e_z / 9 >= 25 / 4`,
  hence `e_z >= 12` for every `z in Sigma`.

Adjacent-pair neighborhood bound inside `Delta`:
- Fix `y in V(Delta)` and let `tau_y = e(Delta[R_y])`, the number of triangles of `Delta` containing `y`.
- If `r_y = sum_{u in R_y} v_u`, then `r_y · v_x = r_y · v_y = 11/6`.
- Again `r_y` is orthogonal to `v_x - v_y`, so its projection onto `span(v_x, v_y)` lies on the line `span(v_x + v_y)`.
- Since `||v_x + v_y||^2 = 2 + 2/6 = 7/3`, that projection has squared norm
  `((r_y · (v_x + v_y))^2) / ||v_x + v_y||^2 = (11/3)^2 / (7/3) = 121/21`.
- Also
  `||r_y||^2 = 11 + 2(tau_y * 1/6 + (55 - tau_y) * (-1/9)) = (5 tau_y - 11) / 9`.
- Therefore
  `(5 tau_y - 11) / 9 >= 121 / 21`,
  so `tau_y >= 13` for every `y in Delta`.

Consequences:
- Since every block `S_z` has at least `12` edges,
  `1650 - 3 T_Delta >= 54 * 12 = 648`,
  hence `T_Delta <= 334`.
- Since every vertex of `Delta` lies in at least `13` triangles,
  `3 T_Delta = sum_y tau_y >= 30 * 13 = 390`,
  hence `T_Delta >= 130`.

So the first subconstituent must satisfy the exact interval
- `130 <= T_Delta <= 334`.

This is a real restriction, but it is not yet an exact contradiction.

Self-check:
- The identity `sum_z e(Delta[S_z]) = 1650 - 3 T_Delta` is exact.
- The inequalities `e_z >= 12` and `tau_y >= 13` come from the global eigenspace geometry, not from an unstructured search.

## lemma_graph
1. Lock the exact SRG identity `A^2 = 20I + A + 10J`.
2. Fix a vertex `x` and decompose `A` into the block matrices `B`, `M`, and `C`.
3. Use the block equations to derive the exact spectral transport `t -> 1 - t` from `Delta` to `Sigma`.
4. Introduce the `54` ten-element blocks `S_z = N(z) ∩ N(x)`.
5. Count the total number of block-internal edges as `1650 - 3 T_Delta`.
6. Use the `34`-dimensional positive eigenspace representation to prove `e(Delta[S_z]) >= 12`.
7. Use the same representation to prove every vertex of `Delta` lies in at least `13` triangles of `Delta`.
8. Conclude `130 <= T_Delta <= 334`.
9. Record that these are exact necessary conditions, but not a full disproof.

Self-check:
- Steps `1` through `8` are unconditional.
- Step `9` is the correct conservative conclusion for this pass.

## chosen_plan
- The best route here was the one-vertex block decomposition together with the eigenspace geometry coming from the positive eigenvalue `5`.
- I pushed that route far enough to get exact spectral coupling and exact lower bounds on two local edge-count statistics.
- I then checked whether those inequalities alone force a contradiction through the triangle count `T_Delta`; they do not.
- I am stopping before code because I do not yet have a sharply targeted bounded search that is more likely to help than another round of handwritten local-structure work.

Self-check:
- I did not drift into SAT, ILP, CP-SAT, or brute-force graph search.
- The current stopping point is based on the math becoming locally informative but not yet decisive.

## self_checks
- Statement check: everything above is about the exact tuple `(85,30,11,10)`.
- Spectral check: the global spectrum `30^1, 5^34, (-4)^50` was rederived from the locked matrix identity.
- Local-structure check: `Delta` is `11`-regular on `30` vertices and `Sigma` is `20`-regular on `54` vertices.
- Conservatism check: I obtained exact necessary conditions, not an exact construction and not an exact impossibility proof.
- Lean check: Lean stays off because there is no strong exact candidate or exact disproof yet.

## code_used
- No.
- I did not identify a bounded local computation that looked stronger than the handwritten constraints already obtained.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Exact outputs from this pass:
  - the locked matrix identity `A^2 = 20I + A + 10J`,
  - the spectrum `30^1, 5^34, (-4)^50`,
  - the one-vertex block equations for `B`, `M`, and `C`,
  - the spectral transport law `t -> 1 - t`,
  - the boundary multiplicity formulas `5^(b+4)` and `(-4)^(a+20)` for `C`,
  - the local bounds `e(Delta[S_z]) >= 12`, `tau_y >= 13`, and `130 <= T_Delta <= 334`.
- I do not currently have an exact construction or an exact contradiction for the intended statement.

## likely_failure_points
- The current constraints are still one-vertex local conditions; they may be too weak to rule out an irregular global witness.
- A real obstruction may require a sharper design-theoretic argument, a star-complement route, or a classification of `30`-vertex `11`-regular local graphs with least eigenvalue at least `-4`.
- The positive-eigenspace bounds may not be close to sharp enough to force impossibility.

## what_verify_should_check
- Recompute the locked identity `A^2 = 20I + A + 10J` and the spectrum `30^1, 5^34, (-4)^50`.
- Recheck the block equations for `B`, `M`, and `C`.
- Recheck the transport statement: for `Bu = t u` with `u ⟂ 1` and `t notin {5,-4}`, prove `C(M^T u) = (1 - t)(M^T u)`.
- Recheck the derived boundary multiplicities `5^(b+4)` and `(-4)^(a+20)` for `C`.
- Recheck the identity `sum_z e(Delta[S_z]) = 1650 - 3 T_Delta`.
- Recheck the Gram computations yielding `e(Delta[S_z]) >= 12` and `tau_y >= 13`.
- Verify that the solve artifact stays conservative: it should remain `PARTIAL`, with Lean still off.

## verify_rediscovery
- PASS 1 used a bounded prior-art audit focused on the exact tuple `(85,30,11,10)`, alternative SRG notation, the canonical Brouwer table, and whether the same source or nearby literature already settles this exact instance.
- The canonical source still treats the tuple as open: Brouwer's `srgtab51-100` table lists `(85,30,11,10)` with `?`, not with a construction or impossibility result.
- The older automorphism-based literature returned by the exact tuple search also still treats this parameter set as unresolved rather than solved.
- Within the bounded audit I found no theorem, proposition, example, observation, or corollary that directly implies existence or nonexistence of the exact intended instance.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness
- The solve artifact is faithful to the exact tuple `(85,30,11,10)` and does not drift to a symmetry-restricted subclass or a different SRG family.
- Its actual mathematical output is a list of necessary conditions on a hypothetical witness, not a proof of nonexistence.
- That is still faithful because the writeup explicitly labels the result `PARTIAL` and does not present those conditions as an exact disproof.
- I found no wrong-theorem drift, quantifier drift, or definition changes.

## verify_proof
- I rechecked the normalization
  `A^2 = 30I + 11A + 10(J-I-A) = 20I + A + 10J`;
  the restricted eigenvalue equation is `u^2 - u - 20 = 0`, so the full spectrum is indeed `30^1, 5^34, (-4)^50`.
- The block identities for `B`, `M`, and `C` around a fixed vertex `x` are the correct expansion of the locked matrix equation, and the row/column sums `B1 = 11 1`, `M1 = 18 1`, `M^T 1 = 10 1`, `C1 = 20 1` are forced.
- For `Bu = t u` with `u ⟂ 1`, the equation `B^2 + M M^T = 20I + B + 10J` gives
  `M M^T u = (20 + t - t^2)u = -(t-5)(t+4)u`.
  Hence `M^T u = 0` on the boundary eigenvalues `t in {5,-4}`. Transposing `B M + M C = M + 10J` gives `M^T B + C M^T = M^T`, so for nonboundary `t` one gets `C(M^T u) = (1-t)(M^T u)`.
- Writing the nontrivial spectrum of `B` as `5^a, (-4)^b, t_1, ..., t_m` with `m = 29-a-b`, the transported contribution to the nontrivial trace of `C` is
  `sum_i (1-t_i) = m - sum_i t_i = 40 + 4a - 5b`.
  Solving `x + y = 53 - m = 24 + a + b` and `5x - 4y + (40 + 4a - 5b) = -20` yields the claimed boundary multiplicities `x = b+4`, `y = a+20`.
- The identity
  `sum_z e(Delta[S_z]) = 1650 - 3 T_Delta`
  is correct: `Delta` has `165` edges, each edge `uv` of `Delta` has exactly `10 - (B^2)_{uv}` common neighbors in `Sigma`, and summing `(B^2)_{uv}` over edges counts each triangle of `Delta` three times.
- The Gram calculations also check:
  - for `z in Sigma`, `s = sum_{y in S_z} v_y` satisfies `||s||^2 = 5 e_z / 9`, while its projection onto `span(v_x + v_z)` has squared norm `25/4`, forcing `e_z >= 45/4`, hence `e_z >= 12`;
  - for `y in Delta`, `r_y = sum_{u in R_y} v_u` satisfies `||r_y||^2 = (5 tau_y - 11) / 9`, while its projection onto `span(v_x + v_y)` has squared norm `121/21`, forcing `tau_y >= 88/7`, hence `tau_y >= 13`.
- Therefore the derived interval `130 <= T_Delta <= 334` is sound.
- I found no incorrect step in the claims actually made in the solve artifact.

## verify_adversarial
- There is no checker or witness file in this artifact, so PASS 4 reduces to trying to break the handwritten claims.
- I reran the arithmetic behind the spectral data and the two Gram-based lower bounds; all threshold values match the record: eigenvalues `5` and `-4`, multiplicities `34` and `50`, `e_z >= 12`, `tau_y >= 13`, and therefore `130 <= T_Delta <= 334`.
- There is no exact construction or exact contradiction in the artifact to attack further. The writeup does not overread the calculations and remains limited to necessary conditions.

## verify_verdict
- `verify_verdict = VERIFIED`
- `classification = PARTIAL`
- `confidence = high`
- `lean_ready = false`
- `next_action = do not run Lean; continue only if a sharper unconditional obstruction or a credible exact witness route appears`

## minimal_repair_if_any
- None. No conservative patch was needed.
