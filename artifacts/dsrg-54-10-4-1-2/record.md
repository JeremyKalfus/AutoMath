# dsrg-54-10-4-1-2

## statement_lock
- Active slug: `dsrg-54-10-4-1-2`
- Title: `Does a directed strongly regular graph with parameters (54,10,4,1,2) exist?`
- Locked intended statement for this solve pass: no loopless directed strongly regular graph with parameters
  `(v,k,t,lambda,mu) = (54,10,4,1,2)` exists.
- Equivalent matrix form: for an adjacency matrix `A`,
  `AJ = JA = 10J` and
  `A^2 = tI + lambda A + mu(J - I - A) = 4I + A + 2(J - I - A) = 2J + 2I - A`.
- So:
  - every vertex has indegree and outdegree `10`,
  - every vertex has exactly `4` mutual neighbors,
  - for every arc `x -> y`, there is exactly `1` directed `2`-path `x -> z -> y`,
  - for every nonarc `x -/-> y` with `x != y`, there are exactly `2` directed `2`-paths `x -> z -> y`.
- The restricted eigenvalues come from `u^2 + u - 2 = 0`, so they are `1` and `-2`.
- Using `trace(A) = 0` and `1 + m_1 + m_{-2} = 54`, the spectrum is forced to be
  `10^1, 1^32, (-2)^21`.
- Also `(A - I)(A + 2I) = 2J`, and `B := A + I` is a `0/1` matrix with spectrum `11^1, 2^32, 0^21`, hence `rank(B) = 33`.

Self-check:
- The target has been locked exactly to the intended nonexistence statement for the active tuple.
- The algebraic normalization `A^2 = 2J + 2I - A` and the spectral multiplicities are exact.

## definitions
- Fix a vertex `x`.
- Let `S = N^+(x)` and `T = N^-(x)`, so `|S| = |T| = 10`.
- Write
  - `M = S ∩ T`, so `|M| = 4`,
  - `O = S \ T`, so `|O| = 6`,
  - `I = T \ S`, so `|I| = 6`,
  - `N = V \ ({x} ∪ M ∪ O ∪ I)`, so `|N| = 37`.
- For classes `C,D` among `M,O,I,N`, let `e(C,D)` be the number of directed edges from `C` to `D`.
- Let `R = V \ ({x} ∪ T)`, so `|R| = 43`.

Exact translations that will be used repeatedly:
- If `y ∈ T`, then `|N^+(y) ∩ T| = 1`; if `y ∉ T` and `y != x`, then `|N^+(y) ∩ T| = 2`; and `x` itself sends exactly `4` edges into `T`.
- Dually, if `y ∈ S`, then `|N^-(y) ∩ S| = 1`; if `y ∉ S` and `y != x`, then `|N^-(y) ∩ S| = 2`; and `x` itself receives exactly `4` edges from `S`.

Self-check:
- The partition sizes are forced by `k = 10` and `t = 4`.
- The two translation bullets are just the dsrg `2`-path counts rewritten relative to the fixed vertex `x`.

## approach_A
Structural / invariant route.

Major step 1: exact `({x}, T, R)` quotient.
- The partition `({x}, T, R)` is out-equitable.
- Its exact quotient matrix is
  ```text
  Q =
  [0 4 6]
  [1 1 8]
  [0 2 8]
  ```
  because:
  - `x` sends `4` edges to `T` and `6` to `R`,
  - every vertex of `T` sends `1` edge to `x`, `1` edge to `T`, and `8` to `R`,
  - every vertex of `R` sends `0` to `x`, `2` to `T`, and `8` to `R`.
- The characteristic polynomial of `Q` is `(u - 10)(u - 1)(u + 2)`, matching the global spectrum.

Self-check:
- The quotient is exact and uses only the source-to-`T` counts forced by the dsrg axioms.
- The eigenvalues of `Q` agree with the global spectral package, so there is no contradiction yet.

Major step 2: centered columns of `A + 2I` are `1`-eigenvectors.
- From `(A - I)(A + 2I) = 2J`, for each vertex `x` the column
  `c_x := (A + 2I)e_x` satisfies `A c_x = c_x + 2j`.
- Since each column sum of `A + 2I` is `12`, the centered vector
  `d_x := c_x - (2/9)j`
  satisfies `A d_x = d_x`.
- So the `54` explicit vectors `d_x` all lie in the `32`-dimensional `1`-eigenspace.

What this gives:
- the parameter set is spectrally feasible but rigid,
- the fixed-vertex quotient is exact,
- and the columns of `A + 2I` all collapse into a low-dimensional affine translate of the `1`-eigenspace.

Self-check:
- The centering constant is correct because `sum(c_x) = 12`.
- This is a genuine structural restriction, but by itself it does not prove nonexistence.

## approach_B
Construction / extremal / contradiction route: push the full `M,O,I,N` partition.

Let
- `a = e(M,M)`, `b = e(M,O)`, `c = e(M,I)`, `d = e(M,N)`,
- `e = e(O,M)`, `f = e(O,O)`, `g = e(O,I)`, `h = e(O,N)`,
- `p = e(I,M)`, `q = e(I,O)`, `r = e(I,I)`, `s = e(I,N)`,
- `u = e(N,M)`, `v = e(N,O)`, `w = e(N,I)`, `z = e(N,N)`.

Major step 1: exact block totals forced by the dsrg axioms.

From targets receiving edges from `S = M ∪ O`:
- `a + e = 4`
- `b + f = 6`
- `c + g = 12`
- `d + h = 74`

From sources sending edges into `T = M ∪ I`:
- `a + c = 4`
- `e + g = 12`
- `p + r = 6`
- `u + w = 74`

From row sums inside the partition:
- `a + b + c + d = 36`
- `e + f + g + h = 60`
- `p + q + r + s = 54`
- `u + v + w + z = 370`

From column sums inside the partition:
- `a + e + p + u = 36`
- `b + f + q + v = 54`
- `c + g + r + w = 60`
- `d + h + s + z = 370`

Useful consequences:
- `e = c`
- `b + d = 32`
- `f + h = 48`
- `p + u = 32`
- `q + v = 48`
- `r + w = 48`

Self-check:
- The row sums for `M` and `I` correctly exclude the forced arcs into `x`, so there is no hidden off-by-one at the base vertex.
- Up to this point everything is unconditional.

Major step 2: the aggregate system is consistent, so the first contradiction attempt fails.
- One explicit integer solution of the displayed block-total system is
  - `a=0, b=0, c=4, d=32, e=4, f=6, g=8, h=42,`
  - `p=6, q=0, r=0, s=48, u=26, v=48, w=48, z=248`.
- So a contradiction cannot come from the aggregate `M,O,I,N` totals alone.

Self-check:
- This is exactly why the solve verdict must stay conservative.
- The failed contradiction route is recorded honestly rather than polished into a false proof.

Major step 3: conditional obstruction under the extra out-equitable hypothesis.
- Suppose, in addition, that every vertex in the same source class has the same out-profile across `M,O,I,N`.
- Then the per-vertex equations are:
  - `a + c = 1`, `e + g = 2`, `p + r = 1`, `u + w = 2`,
  - `4a + 6e = 4`, `4b + 6f = 6`, `4c + 6g = 12`, `4d + 6h = 74`,
  - `a + b + c + d = 9`, `e + f + g + h = 10`.
- Solving the first eight equations forces
  - `a = 1`, `c = 0`,
  - `e = 0`, `g = 2`,
  - `b = 0`, `f = 1`,
  - `d = 8`, `h = 7`.
- Now target-`M` indegree gives
  `4a + 6e + 6p + 37u = 36`,
  so
  `6p + 37u = 32`.
- But `p + r = 1` and `u + w = 2` force `p ∈ {0,1}` and `u ∈ {0,1,2}`, and no such pair solves `6p + 37u = 32`.

Conclusion of Approach B:
- the natural out-equitable `M/O/I/N` refinement is impossible,
- but the dsrg axioms do not force that refinement to be equitable,
- so this is a real obstruction but not a full disproof.

Self-check:
- The contradiction here is exact, but only after the extra out-equitable assumption is added.
- I am not upgrading that conditional obstruction into a global nonexistence claim.

## lemma_graph
1. Lock the exact matrix identity `A^2 = 2J + 2I - A`.
2. Derive the global spectrum `10^1, 1^32, (-2)^21`.
3. Fix a vertex `x` and form the exact out-equitable quotient `({x}, T, R)` with matrix
   `[[0,4,6],[1,1,8],[0,2,8]]`.
4. Refine to the full `M,O,I,N` partition and derive the exact block-total system above.
5. Observe that the aggregate system admits integer solutions, so the naive block-total contradiction route fails.
6. Test the strongest nearby regularity hypothesis: that the `M,O,I,N` partition is out-equitable.
7. Under that extra hypothesis, derive the forced rows
   `M : (1,0,0,8)` and `O : (0,1,2,7)`, then the impossible equation `6p + 37u = 32`.

## chosen_plan
- The best unconditional route is still the structural one: it gives an exact quotient and a clean spectral package with no search.
- I then pushed the local partition as far as it would go. That route does not close unconditionally, but it does show that the simplest natural `M/O/I/N` equitable model is impossible.
- Because the unconditional totals remain consistent, the strongest honest solve-stage outcome is a partial obstruction package, not an exact proof.

Self-check:
- This keeps the artifact faithful to the actual mathematics found in this pass.
- Lean should stay off because there is no exact candidate proof or exact disproof yet.

## self_checks
- Statement fidelity: the artifact stays on the exact tuple `(54,10,4,1,2)`.
- Spectral check: `A^2 = 2J + 2I - A` gives restricted eigenvalues `1` and `-2`, with multiplicities `32` and `21`.
- Local quotient check: the exact `({x}, T, R)` quotient is `[[0,4,6],[1,1,8],[0,2,8]]`.
- Counting check: the `M/O/I/N` block totals are consistent, so no unconditional contradiction was proved there.
- Conditional-scope check: the equation `6p + 37u = 32` only contradicts the added out-equitable hypothesis, not the full dsrg axioms.
- Conservatism check: the solve classification must stay below `COUNTEREXAMPLE` and below `CANDIDATE`.

## code_used
- No code used.
- Reason: the handwritten spectral reduction, exact quotient, and conditional local obstruction were already stronger than any justified bounded experiment, and I did not reach the point where search-heavy computation was warranted.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact outputs from this pass:
  - the exact matrix identity `A^2 = 2J + 2I - A`,
  - the forced spectrum `10^1, 1^32, (-2)^21`,
  - the exact out-equitable quotient `({x}, T, R)` with matrix `[[0,4,6],[1,1,8],[0,2,8]]`,
  - the full unconditional `M/O/I/N` block-total system,
  - the fact that those aggregate equations are consistent,
  - and the exact impossibility of the natural out-equitable `M/O/I/N` refinement.
- I did not prove global nonexistence and I did not produce a construction.
- Lean was intentionally left off.

## likely_failure_points
- The main gap is structural: the full dsrg axioms do not force the `M/O/I/N` partition to be out-equitable.
- The centered-column `1`-eigenvector package is rigid but still too soft to force a contradiction on its own.
- A real witness, if it exists, would have to be locally quite nonuniform, since the obvious equitable local model already fails.

## what_verify_should_check
- Recompute the normalization `A^2 = 2J + 2I - A` and the multiplicities `1^32` and `(-2)^21`.
- Recheck the exact source-to-`T` quotient `[[0,4,6],[1,1,8],[0,2,8]]`.
- Recheck the unconditional `M/O/I/N` block-total system, especially the row sums `36,60,54,370` that exclude or include the base vertex correctly.
- Confirm that the displayed aggregate system really is consistent by checking the explicit sample solution.
- Confirm that the later contradiction `6p + 37u = 32` depends on the extra out-equitable assumption and does not by itself settle the dsrg.

## verify_rediscovery
- PASS 1 used a bounded web audit aimed at the exact tuple, alternate tuple formatting, the canonical Brouwer-Hobart dsrg tables, and possible theorem/proposition/example hits inside the same source family.
- The canonical source still lists the parameter set `(54,10,4,1,2)` as undecided rather than settled.
- The limited exact-tuple and recent-status searches did not surface a construction, a nonexistence theorem, or a same-source proposition/example that already settles this exact instance.
- Rediscovery was not established within budget.

## verify_faithfulness
- The artifact is faithful about scope. It locks the intended statement to nonexistence for `(54,10,4,1,2)`, but the actual solve-stage result is stated only as `PARTIAL`.
- I did not find wrong-theorem drift, quantifier drift, or a silent definition change.
- The record is careful that the contradiction `6p + 37u = 32` is conditional on an added out-equitable hypothesis and is not being promoted to a proof of the intended statement.
- So the mathematical object under discussion remains the exact dsrg instance, but the solved claim is weaker than the intended statement.

## verify_proof
- I rechecked the normalization `A^2 = 2J + 2I - A` from the dsrg identity for `(v,k,t,lambda,mu) = (54,10,4,1,2)`. This is correct.
- I rechecked the restricted eigenvalue equation `u^2 + u - 2 = 0`, giving eigenvalues `1` and `-2`, and the multiplicities forced by `1 + m_1 + m_{-2} = 54` and `10 + m_1 - 2m_{-2} = 0`, namely `(m_1,m_{-2}) = (32,21)`. This is correct.
- I rechecked the exact `({x},T,R)` quotient counts: rows `[0,4,6]`, `[1,1,8]`, and `[0,2,8]` are forced by the dsrg axioms relative to a fixed vertex `x`. Its characteristic roots are indeed `10`, `1`, and `-2`.
- I rechecked the displayed aggregate `M/O/I/N` block-total system and the sample integer solution. The sample solution satisfies all displayed aggregate equations, so the text is correct that those totals alone do not force a contradiction.
- I rechecked the conditional obstruction. Under the added out-equitable hypothesis, the forced rows lead to `6p + 37u = 32` with `p in {0,1}` and `u in {0,1,2}`, which is impossible.
- I did not find an incorrect algebraic step inside the claims actually proved. The issue is not a bad derivation; the issue is that the unconditional gap remains, so the intended nonexistence statement is still unproved.

## verify_adversarial
- No checker or candidate digraph file exists in this artifact, so there was nothing executable to rerun beyond arithmetic verification.
- I reran the arithmetic checks that matter most for adversarial pressure:
- the quotient-spectrum claim is consistent with roots `10,1,-2`;
- the explicit aggregate block-total sample solution is genuine;
- the conditional contradiction has no allowed `(p,u)` solution.
- These checks support the limited claims in the record, but they do not upgrade the result to an exact disproof because the extra out-equitable hypothesis is not justified by the dsrg axioms.

## verify_verdict
- `UNVERIFIED`
- Classification stays `PARTIAL`.
- Reason: no rediscovery was established, and the recorded mathematics appears internally correct, but it does not prove the intended statement that no dsrg with parameters `(54,10,4,1,2)` exists.
- `lean_ready` must remain `false` because there is no frontier-novel exact proof or exact disproof to formalize.

## minimal_repair_if_any
- No mathematical repair was applied.
- The artifact already states the key limitation honestly: the contradiction requires an extra out-equitable assumption not forced by the dsrg axioms.
