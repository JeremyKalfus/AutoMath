# dsrg-51-15-10-5-4

## statement_lock
- Active slug: `dsrg-51-15-10-5-4`
- Title: `Does a directed strongly regular graph with parameters (51,15,10,5,4) exist?`
- Locked intended statement for this solve pass: no loopless directed strongly regular graph with parameters
  `(v,k,t,lambda,mu) = (51,15,10,5,4)` exists.
- Equivalent adjacency-matrix form: for a `0/1` matrix `A` with zero diagonal,
  `AJ = JA = 15J` and
  `A^2 = tI + lambda A + mu(J - I - A) = 10I + 5A + 4(J - I - A) = A + 6I + 4J`.
- So every exact argument can be framed through
  `A^2 = A + 6I + 4J`, `AJ = JA = 15J`, `diag(A) = 0`.
- A useful factorization is
  `(A - 3I)(A + 2I) = 4J`.

Self-check:
- Substituting `(t,lambda,mu) = (10,5,4)` really gives `A^2 = A + 6I + 4J`.
- The intended statement stays locked to the exact tuple `(51,15,10,5,4)`.

## definitions
- Conventions:
  - the digraph is loopless and may have mutual pairs,
  - `x -> y` means `x != y` and `A_xy = 1`,
  - all `2`-path counts are ordered directed `2`-paths.
- Fix a vertex `x`.
- Let `S = N^+(x)` and `T = N^-(x)`, so `|S| = |T| = 15`.
- Write
  - `M = S ∩ T`, so `|M| = 10`,
  - `O = S \ T`, so `|O| = 5`,
  - `I_x = T \ S`, so `|I_x| = 5`,
  - `N = V \ ({x} ∪ M ∪ O ∪ I_x)`, so `|N| = 30`.
- For the structural route, also set `B := A + 2I`. Then
  `B^2 = A^2 + 4A + 4I = 5B + 4J`.

Self-check:
- The partition sizes `10,5,5,30` are forced by `k = 15` and `t = 10`.
- The identity `B^2 = 5B + 4J` is an exact rewrite of `A^2 = A + 6I + 4J`.

## approach_A
Structural / invariant route.

Major step 1: forced spectrum and inverse.
- On the `J`-orthogonal subspace, `A` satisfies
  `u^2 = u + 6`, so the only nontrivial eigenvalues are `3` and `-2`.
- Let their multiplicities be `m_3` and `m_{-2}`. Then
  - `m_3 + m_{-2} = 50`,
  - `15 + 3m_3 - 2m_{-2} = trace(A) = 0`.
- Solving gives
  - `m_3 = 17`,
  - `m_{-2} = 33`.
- Therefore the spectrum is forced to be
  `15^1, 3^17, (-2)^33`.
- Since `0` is not an eigenvalue, `A` is invertible, with
  `A^(-1) = (1/6)A - (1/6)I - (2/45)J`.
- Also `B = A + 2I` has spectrum
  `17^1, 5^17, 0^33`,
  so `rank(B) = 18`.

Self-check:
- `1 + 17 + 33 = 51`.
- `15 + 17*3 + 33*(-2) = 0`, so the trace condition is correct.
- On eigenvalues `15,3,-2`, the formula `(1/6)A - (1/6)I - (2/45)J` acts by `1/15, 1/3, -1/2`, respectively.

Major step 2: ordered-arc transport from column differences.
- Fix an ordered one-way arc `x -> y` with `y -/-> x`.
- Let `b_x` and `b_y` be the `x`-th and `y`-th columns of `B = A + 2I`.
- Because `(A - 3I)B = 4J`, the difference
  `d := b_x - b_y`
  satisfies
  `Ad = 3d`.
- On `V \ {x,y}`, define the four classes
  - `X10 = {z : z -> x and z -/-> y}`,
  - `X11 = {z : z -> x and z -> y}`,
  - `X00 = {z : z -/-> x and z -/-> y}`,
  - `X01 = {z : z -/-> x and z -> y}`.
- If `beta := |X11| = |N^-(x) ∩ N^-(y)|`, then
  - `|X10| = 15 - beta`,
  - `|X11| = beta`,
  - `|X01| = 15 - beta`,
  - `|X00| = 19 + beta`.
- Writing the coordinate equation `(Ad)_z = 3d_z` gives the exact transport rule
  `|N^+(z) ∩ X10| - |N^+(z) ∩ X01| =`
  - `2` for `z ∈ X10`,
  - `1` for `z ∈ X11`,
  - `0` for `z ∈ X00`,
  - `-1` for `z ∈ X01`.
- This is a genuine ordered-pair rigidity statement, but by itself it does not determine `beta`, `A^T A`, or a contradiction.

Self-check:
- The sizes above use only indegree `15` and the shared-in-neighbor parameter `beta`.
- At `z = x`, the eigenvector equation reduces to `10 - 5 - 2 = 3`, which matches `3d_x = 3`.
- At `z = y`, it reduces to `4 - 10 = -6`, which matches `3d_y = -6`.

## approach_B
Construction / extremal / contradiction route around a fixed vertex.

Major step 1: exact three-cell quotient.
- Keep the fixed vertex `x`, and set `T = N^-(x)` and `R = V \ ({x} ∪ T)`.
- Since every `y ∈ T` satisfies `y -> x`, each such `y` has exactly `5` out-neighbors in `T`.
- Since every `y ∈ R` satisfies `y -/-> x`, each such `y` has exactly `4` out-neighbors in `T`.
- Therefore the partition `({x}, T, R)` is exactly out-equitable with quotient
  ```text
  Q =
  [0 10  5]
  [1  5  9]
  [0  4 11]
  ```
- Its characteristic polynomial is
  `(u - 15)(u - 3)(u + 2)`,
  matching the forced spectrum.

Self-check:
- Every row of `Q` sums to `15`, as required.
- `trace(Q) = 16` and `det(Q) = -90`, agreeing with eigenvalues `15,3,-2`.

Major step 2: full `M/O/I_x/N` block totals.
- Let
  - `a = e(M,M)`, `b = e(M,O)`, `c = e(M,I_x)`, `d = e(M,N)`,
  - `e = e(O,M)`, `f = e(O,O)`, `g = e(O,I_x)`, `h = e(O,N)`,
  - `p = e(I_x,M)`, `q = e(I_x,O)`, `r = e(I_x,I_x)`, `s = e(I_x,N)`,
  - `u = e(N,M)`, `v = e(N,O)`, `w = e(N,I_x)`, `z = e(N,N)`.
- From sources counted against `T = M ∪ I_x`:
  - `a + c = 50`
  - `e + g = 20`
  - `p + r = 25`
  - `u + w = 120`
- From targets counted from `S = M ∪ O`:
  - `a + e = 50`
  - `b + f = 25`
  - `c + g = 20`
  - `d + h = 120`
- From row sums inside the partition:
  - `a + b + c + d = 140`
  - `e + f + g + h = 75`
  - `p + q + r + s = 70`
  - `u + v + w + z = 450`
- From column sums inside the partition:
  - `a + e + p + u = 140`
  - `b + f + q + v = 70`
  - `c + g + r + w = 75`
  - `d + h + s + z = 450`
- The whole unconditional system collapses to the parameterization
  - `c = e = 50 - a`
  - `g = a - 30`
  - `f = 25 - b`
  - `d = 90 - b`
  - `h = 30 + b`
  - `p = 25 - r`
  - `u = 65 + r`
  - `w = 55 - r`
  - `s = v = 45 - q`
  - `z = 285 + q`
- So the first fixed-vertex contradiction route remains parametrically feasible; no contradiction appears at this coarse level.

Self-check:
- The `S`-to-cell totals add to `50 + 25 + 20 + 120 = 215`, and adding the `10` arcs from `S` back to `x` gives `225 = 15*15`.
- The row-total bookkeeping uses that rows in `M` and `I_x` lose the arc to `x`, while rows in `O` and `N` do not.
- The parameterization is internally consistent: for example `e + g = (50 - a) + (a - 30) = 20` and `d + h = (90 - b) + (30 + b) = 120`.

## lemma_graph
1. Lock the exact identity `A^2 = A + 6I + 4J`.
2. Derive the forced spectrum `15^1, 3^17, (-2)^33`.
3. Obtain the explicit inverse of `A` and the rank-`18` package for `B = A + 2I`.
4. For a one-way arc `x -> y`, use `d = b_x - b_y` and `Ad = 3d` to derive the ordered-arc transport rule on the four classes `X10, X11, X00, X01`.
5. For a fixed vertex `x`, derive the exact three-cell quotient on `({x}, T, R)`.
6. Refine to `M/O/I_x/N` and write the full unconditional block-total system.
7. Conclude that both the spectral route and the first fixed-vertex route are still locally feasible, so no exact proof or disproof has been reached.

## chosen_plan
- The best path for this pass was the fixed-vertex contradiction route, because the dossier explicitly suggested neighborhood partitions and the one-way part has only size `5`.
- I paired that with the clean structural package `A^2 = A + 6I + 4J`, the exact spectrum, and the `B = A + 2I` column-difference identity, since those are unconditional and cheap.
- After pushing both routes, I stopped before any code:
  - the coarse one-vertex system is still consistent,
  - the ordered-arc transport lemma is suggestive but not yet closed,
  - and starting generic search on the actual instance would violate the solve-stage rules.

Self-check:
- This keeps the solve pass reasoning-first.
- Lean stays off because there is no exact proof or exact disproof candidate yet.

## self_checks
- Statement fidelity: all claims stay on the exact tuple `(51,15,10,5,4)`.
- Algebra: `A^2 = A + 6I + 4J`, `(A - 3I)(A + 2I) = 4J`, and `B^2 = 5B + 4J` are exact.
- Spectrum: the multiplicities `17` and `33` solve the trace and dimension equations exactly.
- Quotient: `Q = [[0,10,5],[1,5,9],[0,4,11]]` is an exact out-equitable quotient.
- Local counts: the `M/O/I_x/N` equations are unconditional and internally consistent.
- Scope: the ordered-arc transport lemma is exact, but it is still only a partial rigidity statement.
- Conservatism: nothing here justifies `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.

## code_used
- No code was used.
- Reason: after the handwritten setup, I did not have a narrowly justified bounded experiment that would answer the exact instance rather than just another heuristic side question.
- In particular, I did not run SAT, ILP, CP-SAT, brute force over digraphs, or generic optimization.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact outputs from this pass:
  - the normalized dsrg identity `A^2 = A + 6I + 4J`,
  - the forced spectrum `15^1, 3^17, (-2)^33`,
  - the explicit inverse of `A`,
  - the rank-`18` package for `B = A + 2I`,
  - the exact three-cell quotient on `({x}, T, R)`,
  - the full unconditional `M/O/I_x/N` block-total system,
  - and the ordered-arc transport lemma from `Ad = 3d`.
- I did not prove nonexistence.
- I did not construct a witness.
- Lean was intentionally left off.

## likely_failure_points
- The `M/O/I_x/N` partition is probably too coarse. A real contradiction, if one exists, likely needs a full ordered-pair refinement around a one-way arc.
- The ordered-arc transport lemma needs to be combined with the analogous row-difference information or with explicit `A^T A` / `A A^T` control; I did not close that bridge here.
- The spectrum and inverse are rigid but still feasible, so pure linear algebra is not enough by itself.
- Because the dossier already marked moderate rediscovery risk, even a future clean contradiction would still need skeptical verify-stage checking before any Lean decision.

## what_verify_should_check
- Recompute `A^2 = A + 6I + 4J`, `(A - 3I)(A + 2I) = 4J`, and `B^2 = 5B + 4J`.
- Recheck the spectrum `15^1, 3^17, (-2)^33` and the inverse
  `A^(-1) = (1/6)A - (1/6)I - (2/45)J`.
- Recheck the exact three-cell quotient
  `[[0,10,5],[1,5,9],[0,4,11]]`
  and its characteristic polynomial.
- Recheck every `M/O/I_x/N` block-total equation and the parameterization that follows.
- Recheck the ordered-arc transport lemma from `d = b_x - b_y`, especially the four right-hand sides `2,1,0,-1`.
- Keep the classification conservative: this artifact supports `PARTIAL`, not an exact disproof.

## verify_rediscovery
- PASS 1 used the bounded web budget on the exact tuple `(51,15,10,5,4)`, the complement tuple `(51,35,30,23,26)`, the canonical Brouwer-Hobart dsrg table, and one recent status check.
- The canonical table still lists the exact row `51  15  10  5  4  3^{17}  -2^{33}` with comment `?`, and the complement row is also still marked `?`.
- Within the same source, I did not find an attached theorem, proposition, example, observation, or corollary settling this exact tuple.
- The bounded follow-up did not uncover a later paper explicitly constructing or excluding `(51,15,10,5,4)`. A recent 2025 paper on directed strongly regular graphs over linear groups still points readers back to the Brouwer-Hobart webpage for current dsrg results/status, but it did not settle this tuple within the capped audit.
- Rediscovery was not established within budget.

## verify_faithfulness
- The solve artifact stayed faithful to the intended statement.
- It explicitly locked the exact tuple `(51,15,10,5,4)` and correctly rewrote the dsrg relation as `A^2 = 10I + 5A + 4(J - I - A) = A + 6I + 4J`.
- It did not drift into a different theorem: every derived claim is a structural consequence of the exact dsrg axioms for this tuple, and the artifact correctly stops at `PARTIAL`.

## verify_proof
- No incorrect step was found inside the artifact's actual claim envelope.
- The spectral package checks out: on the `J`-orthogonal subspace one has `u^2 - u - 6 = (u-3)(u+2)`, and solving
  `m_3 + m_{-2} = 50`, `15 + 3m_3 - 2m_{-2} = 0`
  gives `m_3 = 17`, `m_{-2} = 33`.
- The inverse formula is correct. With
  `X = (1/6)A - (1/6)I - (2/45)J`,
  the identities `A^2 = A + 6I + 4J` and `AJ = JA = 15J` give `AX = XA = I`.
- The quotient matrix
  ```text
  [0 10  5]
  [1  5  9]
  [0  4 11]
  ```
  is correct: every row sums to `15`, and `det(uI-Q)` vanishes at `u = 15, 3, -2`.
- The `M/O/I_x/N` block equations and the recorded parameterization are internally consistent.
- The ordered-arc transport lemma is also consistent. For `d = b_x - b_y`, the relation `(A-3I)d = 0` is correct, and the coordinate values of `d_z` on `X10, X11, X00, X01` yield the stated right-hand sides `2, 1, 0, -1`.
- The issue is incompleteness, not a false proof: these ingredients still do not force either a contradiction or a construction.

## verify_adversarial
- There was no code or checker to rerun.
- I reran the arithmetic checks that matter adversarially: the quotient eigenvalues, the inverse identity, and the consistency of the coarse block-total system.
- Those checks support the artifact's limited claims.
- I also looked for theorem drift, hidden assumptions, or an accidental contradiction already latent in the recorded equations and did not find one. The writeup remains a partial structural analysis only.

## verify_verdict
- `UNVERIFIED`.
- PASS 1 did not establish rediscovery, but PASS 2-4 also did not upgrade the artifact beyond `PARTIAL`.
- The run therefore remains `classification = PARTIAL`, not `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.
- `lean_ready = false` because there is no exact intended statement ready for formalization.

## minimal_repair_if_any
- No repair was needed.
- The conservative repair is classificatory only: keep the run at `PARTIAL` / `UNVERIFIED` and move on rather than escalating to Lean.
