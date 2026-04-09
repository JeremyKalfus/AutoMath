# dsrg-36-14-7-6-5

## statement_lock
- Active slug: `dsrg-36-14-7-6-5`
- Title: `Does a directed strongly regular graph with parameters (36,14,7,6,5) exist?`
- Locked intended statement for this solve pass: no loopless directed strongly regular graph with parameters
  `(v,k,t,lambda,mu) = (36,14,7,6,5)` exists.
- Equivalent adjacency-matrix form: for a `0/1` matrix `A` with zero diagonal,
  `AJ = JA = 14J` and
  `A^2 = tI + lambda A + mu(J - I - A) = 7I + 6A + 5(J - I - A) = A + 2I + 5J`.
- So:
  - every vertex has indegree and outdegree `14`,
  - exactly `7` out-neighbors are also in-neighbors,
  - for every arc `x -> y`, there are exactly `6` directed `2`-paths `x -> z -> y`,
  - for every nonarc `x -/-> y` with `x != y`, there are exactly `5` such directed `2`-paths.

Self-check:
- The intended statement is locked exactly to the active tuple.
- The normalization `A^2 = A + 2I + 5J` is the right dsrg identity for `(36,14,7,6,5)`.

## definitions
- Conventions:
  - the graph is loopless but may have mutual pairs,
  - `x -> y` always means `x != y` and `A_xy = 1`,
  - all counting below is for ordered directed `2`-paths.
- Fix a vertex `x`.
- Let `S = N^+(x)` and `T = N^-(x)`, so `|S| = |T| = 14`.
- Write
  - `M = S ∩ T`, so `|M| = 7`,
  - `O = S \ T`, so `|O| = 7`,
  - `I = T \ S`, so `|I| = 7`,
  - `N = V \ ({x} ∪ M ∪ O ∪ I)`, so `|N| = 14`.
- Let `B := A + I`. Then `B` is a `0/1` matrix with row and column sum `15`, and
  `B^2 = A^2 + 2A + I = 3B + 5J`.

Self-check:
- The local partition sizes are forced by `k = 14` and `t = 7`.
- Passing to `B = A + I` is exact and keeps the problem finite and algebraic.

## approach_A
Structural / invariant route.

Major step 1: global spectral and low-rank package.
- On the `J`-orthogonal subspace, `A` satisfies `u^2 = u + 2`, so the restricted eigenvalues are `2` and `-1`.
- Using `trace(A) = 0` and `1 + m_2 + m_{-1} = 36`,
  `14 + 2m_2 - m_{-1} = 0`,
  hence
  `m_2 = 7` and `m_{-1} = 28`.
- Therefore the spectrum is forced to be
  `14^1, 2^7, (-1)^28`.
- Since `B = A + I`, the spectrum of `B` is
  `15^1, 3^7, 0^28`, so `rank(B) = 8`.
- Also `M0 := 12B - 5J` has entries in `{7,-5}`, row and column sums `0`, and
  `M0^2 = 36M0`.
  Thus `M0 / 36` is an idempotent of rank `7`.

Self-check:
- The multiplicities solve the trace equations exactly.
- `rank(B) = 8` is a genuine rigidity statement, but by itself it is not yet a contradiction.

Major step 2: exact `({x}, T, R)` quotient.
- Let `R = V \ ({x} ∪ T)`, so `|R| = 21`.
- For `y ∈ T`, since `y -> x`, the number of out-neighbors of `y` inside `T` is `6`.
- For `y ∈ R`, since `y -/-> x`, the number of out-neighbors of `y` inside `T` is `5`.
- Therefore the partition `({x}, T, R)` is exactly out-equitable with quotient
  ```text
  Q =
  [0 7 7]
  [1 6 7]
  [0 5 9]
  ```
- Its characteristic polynomial is
  `u^3 - 15u^2 + 12u + 28 = (u - 14)(u - 2)(u + 1)`,
  matching the forced global spectrum.

Self-check:
- The three-cell quotient is exact and uses only the dsrg axioms.
- Its agreement with the global eigenvalues means this natural first quotient does not contradict feasibility.

## approach_B
Construction / extremal / contradiction route around a fixed vertex.

Major step 1: full `M/O/I/N` block totals.
- Let
  - `a = e(M,M)`, `b = e(M,O)`, `c = e(M,I)`, `d = e(M,N)`,
  - `e = e(O,M)`, `f = e(O,O)`, `g = e(O,I)`, `h = e(O,N)`,
  - `p = e(I,M)`, `q = e(I,O)`, `r = e(I,I)`, `s = e(I,N)`,
  - `u = e(N,M)`, `v = e(N,O)`, `w = e(N,I)`, `z = e(N,N)`.
- From targets receiving edges from `S = M ∪ O`:
  - `a + e = 42`
  - `b + f = 42`
  - `c + g = 35`
  - `d + h = 70`
- From sources sending edges into `T = M ∪ I`:
  - `a + c = 42`
  - `e + g = 35`
  - `p + r = 42`
  - `u + w = 70`
- From row sums inside the partition:
  - `a + b + c + d = 91`
  - `e + f + g + h = 98`
  - `p + q + r + s = 91`
  - `u + v + w + z = 196`
- From column sums inside the partition:
  - `a + e + p + u = 91`
  - `b + f + q + v = 91`
  - `c + g + r + w = 98`
  - `d + h + s + z = 196`
- Immediate consequences:
  - `e = c`
  - `b + d = 49`
  - `f + h = 63`
  - `p + u = 49`
  - `q + v = 49`
  - `r + w = 56`

Self-check:
- The only subtle point is the `91/98/196` bookkeeping: rows from `M` and `I` lose the forced arc to `x`, while rows from `O` and `N` do not.
- Up to here everything is unconditional.

Major step 2: test the strongest nearby quotient closure.
- The dossier suggested an equitable-quotient contradiction, so after the handwritten block algebra I tested the strengthened hypothesis that the five-cell partition
  `({x}, M, O, I, N)` is an exact out-equitable partition.
- Under that hypothesis its quotient matrix must have the form
  ```text
  [0,7,7,0,0]
  [1,*,*,*,*]
  [0,*,*,*,*]
  [1,*,*,*,*]
  [0,*,*,*,*]
  ```
  and must satisfy the exact quotient identity
  `Q^2 = Q + 2I + 5K`,
  where every row of `K` is `[1,7,7,7,14]`.
- A tiny bounded enumeration over the resulting integer constraints found `11` integral quotient matrices.
- One explicit solution is
  ```text
  [0,7,7,0,0]
  [1,1,2,5,5]
  [0,5,4,0,5]
  [1,1,1,5,6]
  [0,3,3,2,6]
  ```
  which already satisfies the full quotient identity.

Conclusion of Approach B:
- The full local block system is consistent.
- Even the stronger exact five-cell equitable quotient model is still locally feasible.
- So the hoped-for local quotient contradiction does not materialize in this pass.

Self-check:
- The tiny computation only tested a very specific strengthened model; it did not search over digraphs.
- The existence of explicit quotient solutions means I should not claim any contradiction from the fixed-vertex partition alone.

## lemma_graph
1. Lock the exact dsrg identity `A^2 = A + 2I + 5J`.
2. Derive the spectrum `14^1, 2^7, (-1)^28`.
3. Pass to `B = A + I` to get `B^2 = 3B + 5J` and `rank(B) = 8`.
4. Fix a vertex `x` and derive the exact three-cell quotient `({x}, T, R)` with matrix `[[0,7,7],[1,6,7],[0,5,9]]`.
5. Refine to `M/O/I/N` and derive the full unconditional block-total system.
6. Test whether the strongest nearby exact quotient model on `({x}, M, O, I, N)` is already impossible.
7. Since that strengthened quotient system has explicit integer solutions, stop short of any exact nonexistence claim.

## chosen_plan
- The best path here is the structural one: the low-rank `B` package and the exact `({x}, T, R)` quotient are forced and clean.
- I then pushed the local partition as far as it would honestly go, because the dossier specifically suggested a quotient-style contradiction.
- That route did not close: the local totals are consistent, and even the stronger five-cell equitable quotient ansatz survives.
- So the correct solve-stage output is a partial obstruction package, not a proof and not a disproof.

Self-check:
- This preserves rigor instead of forcing a false contradiction.
- Lean should remain off because there is no exact candidate theorem or exact counterexample yet.

## self_checks
- Statement fidelity: all claims stay on the exact tuple `(36,14,7,6,5)`.
- Algebra check: `A^2 = A + 2I + 5J` and `B^2 = 3B + 5J` are exact.
- Spectral check: the multiplicities `2^7` and `(-1)^28` are forced by the trace equations.
- Rank check: `rank(B) = 8` follows from the spectrum of `B`.
- Quotient check: the three-cell quotient `[[0,7,7],[1,6,7],[0,5,9]]` is exact.
- Scope check: the five-cell quotient experiment only tests a strengthened local hypothesis, so it cannot be promoted to a global existence or nonexistence result.
- Conservatism check: no statement here justifies `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.

## code_used
- One tiny bounded Python enumeration was used only after the reasoning stage fixed the exact five-cell quotient equations.
- Purpose: check whether the strengthened exact out-equitable quotient model on `({x}, M, O, I, N)` is already inconsistent.
- Result: it found `11` integral quotient matrices satisfying the full identity `Q^2 = Q + 2I + 5K`.
- No graph search, SAT, ILP, CP-SAT, or adjacency-matrix brute force was used.

Self-check:
- The code stayed within the repo and only answered a narrowly defined consistency question.
- The computation reduced overclaiming rather than creating a speculative result.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact outputs from this pass:
  - the exact normalization `A^2 = A + 2I + 5J`,
  - the forced spectrum `14^1, 2^7, (-1)^28`,
  - the low-rank consequence `rank(A + I) = 8`,
  - the exact three-cell quotient `[[0,7,7],[1,6,7],[0,5,9]]`,
  - the full unconditional `M/O/I/N` block-total system,
  - and the fact that the natural five-cell equitable quotient route is locally consistent rather than contradictory.
- I did not prove nonexistence.
- I did not construct a witness.
- Lean was intentionally left off.

## likely_failure_points
- The low-rank package for `B = A + I` is rigid, but I did not find the missing bridge from that right/left linear algebra to a contradiction involving `A^T` or common out-neighbor counts.
- The fixed-vertex partition leaves substantial local freedom once one stops assuming hidden equitability.
- A true obstruction may require a sharper bilinear identity, a transpose-sensitive argument, or a design-theoretic interpretation of `B^2 = 3B + 5J` that I did not close here.

## what_verify_should_check
- Recompute `A^2 = A + 2I + 5J`, the restricted eigenvalues `2,-1`, and multiplicities `7,28`.
- Recheck that `B = A + I` has spectrum `15^1, 3^7, 0^28`, hence `rank(B) = 8`.
- Recheck `M0 := 12B - 5J` and the identity `M0^2 = 36M0`.
- Recheck the exact three-cell quotient `[[0,7,7],[1,6,7],[0,5,9]]` and its characteristic polynomial `u^3 - 15u^2 + 12u + 28`.
- Recheck the full `M/O/I/N` block-total equations, especially the `91/98/196` bookkeeping.
- Recheck the tiny quotient enumeration logic and verify that the displayed sample matrix really satisfies `Q^2 = Q + 2I + 5K`.
- Keep the classification conservative: this artifact supports `PARTIAL`, not an exact disproof.

## verify_rediscovery
- PASS 1 used a bounded live web audit on the exact tuple `(36,14,7,6,5)`, alternative dsrg notation, the complement tuple `(36,21,14,11,14)`, the canonical Hobart-Brouwer source, and whether the same source or nearby literature already contains a theorem, proposition, example, observation, or corollary settling this exact instance.
- Within the search budget, I did not find any later paper, database entry, or discussion page explicitly constructing a dsrg with parameters `(36,14,7,6,5)` or proving exact nonexistence for that tuple.
- The canonical Hobart-Brouwer dsrg table still appears to treat this exact row as unresolved rather than tagged by a construction or nonexistence marker.
- So rediscovery is not established. This run should not be classified as `REDISCOVERY`.

## verify_faithfulness
- The solve artifact is faithful to the intended statement because it never upgrades the local obstruction package into a proof of nonexistence.
- The claimed normalization `A^2 = A + 2I + 5J`, the spectrum `14^1,2^7,(-1)^28`, the exact three-cell quotient on `({x},T,R)`, and the displayed `M/O/I/N` block-total system all concern the exact tuple `(36,14,7,6,5)`.
- The five-cell quotient computation is explicitly framed as a check of a strengthened out-equitable hypothesis, not as a consequence of the dsrg axioms.
- I found no wrong-theorem drift, quantifier drift, or definition drift. The classification must remain `PARTIAL`, not `VARIANT`, `CANDIDATE`, or `EXACT`.

## verify_proof
- First incorrect step found: none in the claims actually made.
- The algebra checks out:
  - `A^2 = 7I + 6A + 5(J - I - A) = A + 2I + 5J`,
  - on the `J`-orthogonal subspace the minimal polynomial is `u^2 - u - 2 = (u-2)(u+1)`,
  - the trace equations give multiplicities `7` and `28`,
  - hence `B = A + I` has spectrum `15^1,3^7,0^28` and `rank(B) = 8`.
- The matrix `M0 = 12B - 5J` really satisfies `M0^2 = 36M0`, since `B^2 = 3B + 5J`, `BJ = JB = 15J`, and `J^2 = 36J`.
- The exact three-cell quotient is correct: for `y in T`, the number of out-neighbors in `T` is `lambda = 6`; for `y in R`, it is `mu = 5`; together with row sum `14` this gives
  `[[0,7,7],[1,6,7],[0,5,9]]`.
- I did not find a contradiction in the unconditional `M/O/I/N` block totals. The solver's conclusion that this route stays locally consistent is therefore still credible.
- The sample five-cell quotient matrix displayed in the solve artifact does satisfy the claimed identity `Q^2 = Q + 2I + 5K`, so the stated failure of that strengthened contradiction route is supported.

## verify_adversarial
- There is no witness digraph, no adjacency matrix, and no standalone checker file in this artifact directory, so there was no certificate to attack directly.
- I reran the concrete computation that can be checked from the record:
  - the displayed five-cell quotient matrix has row sums `14`,
  - it exactly satisfies `Q^2 = Q + 2I + 5K`,
  - so it really is a valid integral solution of the strengthened quotient equations.
- I also rechecked the arithmetic behind the spectral package and the `M0^2 = 36M0` identity; those computations are consistent with the written proof.
- Adversarial conclusion: the artifact survives skeptical checking as a sound partial analysis, but it still does not settle existence or nonexistence of the exact dsrg.

## verify_verdict
- `UNVERIFIED`
- Reason: no rediscovery was established, but the solve artifact still does not prove the intended nonexistence statement. It gives only a correct partial obstruction package.
- Classification remains `PARTIAL`.
- `lean_ready = false` because there is no frontier-novel exact theorem or exact counterexample to formalize.

## minimal_repair_if_any
- No mathematical repair was needed.
- The only conservative editorial improvement would be to make the phrase "strengthened out-equitable hypothesis" even more prominent anywhere the five-cell quotient scan is summarized.
