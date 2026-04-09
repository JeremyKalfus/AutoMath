# dsrg-40-18-9-7-9

## statement_lock
- Active slug: `dsrg-40-18-9-7-9`
- Title: `Does a directed strongly regular graph with parameters (40,18,9,7,9) exist?`
- Locked intended statement for this solve pass: determine whether there exists a loopless directed strongly regular graph with parameters
  `(v,k,t,lambda,mu) = (40,18,9,7,9)`.
- Equivalent adjacency-matrix form: there exists a `40 x 40` `0/1` matrix `A` such that
  - `A_ii = 0` for all `i`,
  - every row sum and every column sum is `18`,
  - `A^2 = tI + lambda A + mu(J - I - A) = 9I + 7A + 9(J - I - A) = 9J - 2A`.
- So for every ordered pair of distinct vertices `(x,y)`, the number of directed `2`-paths `x -> z -> y` is `7` when `x -> y` and `9` otherwise, while `(A^2)_{xx} = 9` for every vertex `x`.

Self-check:
- The target stayed exact: the whole dsrg tuple, not a Cayley-only, normal-only, or equitable-only variant.
- The identity `A^2 = 9J - 2A` is the correct specialization of the dsrg axioms for `(40,18,9,7,9)`.

## definitions
- `J` is the all-ones matrix and `j` is the all-ones column vector.
- `N^+(x)` and `N^-(x)` are the out-neighborhood and in-neighborhood of a vertex `x`.
- Relative to a fixed vertex `x`, I use the standard four-way partition
  - `M(x) = N^+(x) cap N^-(x)`, with size `9`,
  - `O(x) = N^+(x) \ N^-(x)`, with size `9`,
  - `I(x) = N^-(x) \ N^+(x)`, with size `9`,
  - `N(x) = V \ ({x} union M(x) union O(x) union I(x))`, with size `12`.
- I also use the complementary `0/1` matrix
  `C := J - I - A`.
  This records nonarcs: for `x != y`, `C_xy = 1` exactly when `x -/-> y`.
- I use the sign matrix
  `H := 2C - J = J - 2I - 2A`.
  Its entries are `-1` on the diagonal and on arcs, and `+1` on nonarcs.

Ambiguities / conventions:
- The solve pass assumes only the standard loopless dsrg definition from the dossier.
- I do not assume symmetry, normality, vertex-transitivity, or a Cayley model unless explicitly stated.
- Spectral statements are over `R` or `C`; all polynomials used here split with distinct roots, so diagonalizability claims are safe.

Self-check:
- The local class sizes are forced by `k = 18` and `t = 9`, and they sum to `39` as required.
- `C` and `H` are exact rewrites of the same existence problem, not nearby variants.

## approach_A
Structural / invariant route.

Major step 1: forced spectrum and rank of `A`.
- Since `Aj = 18j`, the all-ones vector is a right eigenvector with eigenvalue `18`.
- On the `39`-dimensional subspace orthogonal to `j`, the identity `A^2 = 9J - 2A` becomes
  `A^2 = -2A`,
  so every nontrivial eigenvalue is a root of `u^2 + 2u = u(u+2)`.
- Let the multiplicities of `0` and `-2` on that subspace be `m_0` and `m_-2`.
  Then
  - `m_0 + m_-2 = 39`,
  - `trace(A) = 0 = 18 - 2 m_-2`.
- Therefore `m_-2 = 9` and `m_0 = 30`.
- The spectrum is forced to be
  `18^1, (-2)^9, 0^30`.
- In particular,
  `rank(A) = 10`
  and
  `nullity(A) = 30`.

Self-check:
- The trace equation `18 - 2 * 9 = 0` is correct.
- The spectrum is compatible with `A^2 = 9J - 2A` and with the row sum `18`.

Major step 2: complementary matrix reformulation.
- Set `C := J - I - A`.
- Using `AJ = JA = 18J`, one gets
  `C^2 = (J - I - A)^2 = I + 11J`.
- So `C` is a `0/1` matrix with zero diagonal, constant row and column sum `21`, and the exact quadratic identity
  `C^2 = I + 11J`.
- On the `j`-line, `C` has eigenvalue `21`.
- On the orthogonal subspace, `C = -I - A`, so its nontrivial eigenvalues are `1` and `-1`, with multiplicities `9` and `30`.
- Hence the spectrum of `C` is
  `21^1, 1^9, (-1)^30`,
  so
  `det(C) = 21`.
- Also
  `C^-1 = C - (11/21)J`,
  because
  `C(C - (11/21)J) = C^2 - 11J = I`.

Self-check:
- The cancellation in `C^2` is exact; the `A`-terms disappear completely.
- The inverse formula is consistent with both `C^2 = I + 11J` and `CJ = 21J`.

Major step 3: sign-matrix reformulation.
- Define
  `H := 2C - J = J - 2I - 2A`.
- Then `H` is a `40 x 40` `±1` matrix with
  - diagonal entries `-1`,
  - row sum `2`,
  - column sum `2`.
- Since `C = (H + J)/2`, the identity `C^2 = I + 11J` becomes
  `H^2 = 4I`.
- So existence of the dsrg is equivalent to existence of a `±1` matrix `H` with row and column sums `2` and exact involutory square `4I`.

Self-check:
- The row-sum check is exact: each row of `H` has `21` entries `+1` and `19` entries `-1`, so the sum is `2`.
- Expanding `(H + J)^2 = 4(I + 11J)` indeed gives `H^2 = 4I` because `HJ = JH = 2J` and `J^2 = 40J`.

Major step 4: exact fixed-vertex quotient.
- Fix a vertex `x` and set `Q(x) := N^-(x)` and `R(x) := V \ ({x} union Q(x))`.
- Then `|Q(x)| = 18` and `|R(x)| = 21`.
- The partition `({x}, Q(x), R(x))` is exactly out-equitable:
  - from `x`: `(0,9,9)`,
  - from a vertex in `Q(x)`: `(1,7,10)`,
  - from a vertex in `R(x)`: `(0,9,9)`.
- So the quotient matrix is
  ```text
  [0 9 9]
  [1 7 10]
  [0 9 9]
  ```
- Its characteristic polynomial is `u(u+2)(u-18)`, matching the forced global spectrum.

Self-check:
- The count into `Q(x)` is exactly the dsrg `2`-path axiom specialized to target `x`.
- The quotient row sums are all `18`, as they must be.

Major step 5: exact triangle count and nonnormality.
- Multiplying once more gives
  `A^3 = A(9J - 2A) = 144J + 4A`.
- Therefore
  `trace(A^3) = 144 * 40 = 5760`.
- Each directed `3`-cycle contributes exactly `3` closed walks of length `3`, so the total number of directed `3`-cycles is
  `5760 / 3 = 1920`.
- Averaging over vertices shows exactly `144` directed `3`-cycles through each vertex.
- Also
  `trace(AA^T) = 40 * 18 = 720`,
  while the sum of squared eigenvalue moduli is
  `18^2 + 9 * 2^2 = 360`.
- If `A` were normal, these quantities would agree, so any realization must be strongly nonnormal.

Self-check:
- The triangle count is exact and uses only `A^3 = 144J + 4A`.
- The nonnormality test is a valid obstruction class statement, not a global impossibility proof.

Major step 6: local `M/O/I/N(x)` totals.
- With `x` fixed and `M,O,I,N` abbreviating `M(x),O(x),I(x),N(x)`, write
  - `a,b,c,d` for arcs from an `M`-vertex into `M,O,I,N`,
  - `e,f,g,h` for arcs from an `O`-vertex into `M,O,I,N`,
  - `p,q,r,s` for arcs from an `I`-vertex into `M,O,I,N`,
  - `u,v,w,z` for arcs from an `N`-vertex into `M,O,I,N`.
- The exact dsrg constraints give
  - `a+b+c+d = 17`, `a+c = 7`,
  - `e+f+g+h = 18`, `e+g = 9`,
  - `p+q+r+s = 17`, `p+r = 7`,
  - `u+v+w+z = 18`, `u+w = 9`,
  - `a+e = 7`, `b+f = 7`, `c+g = 9`, `d+h = 12`,
  - `9a + 9e + 9p + 12u = 153`,
  - `9b + 9f + 9q + 12v = 153`,
  - `9c + 9g + 9r + 12w = 162`,
  - `9d + 9h + 9s + 12z = 216`.
- These are strong exact bookkeeping constraints, but they do not by themselves force a contradiction.

Self-check:
- The `12` in `d + h = 12` is correct because the target class `N(x)` has size `12`.
- I did not silently assume the full five-cell partition is equitable; these are aggregate constraints only.

## approach_B
Construction / extremal / contradiction route.

Major step 1: abelian Cayley obstruction.
- Suppose there were an abelian Cayley realization on a group `G` of order `40`, with connection set `D subset G`, `|D| = 18`, and `e notin D`.
- In the group ring, the dsrg identity becomes
  `D^2 = 9G - 2D`.
- For any nonprincipal character `chi`, since `chi(G) = 0`, one gets
  `chi(D)^2 = -2 chi(D)`,
  so every nonprincipal character value lies in `{0,-2}`.
- If `a` of the `39` nonprincipal characters had value `-2`, Parseval would give
  `18^2 + 4a = 40 * 18 = 720`.
- That forces
  `324 + 4a = 720`,
  hence
  `a = 99`,
  impossible.
- Therefore no abelian Cayley realization exists.

Self-check:
- This is an exact contradiction, not a heuristic.
- Its scope is narrower than the full problem: it rules out abelian Cayley models only.

Major step 2: strengthened five-cell quotient test.
- After the handwritten `M/O/I/N(x)` derivation, I tested the stronger ansatz that for a fixed vertex `x`, the five-cell partition
  `({x}, M(x), O(x), I(x), N(x))`
  is an exact out-equitable partition.
- Under that ansatz the quotient matrix must be
  ```text
  [0,9,9,0,0]
  [1,a,b,c,d]
  [0,e,f,g,h]
  [1,p,q,r,s]
  [0,u,v,w,z]
  ```
  with the linear constraints written in Approach A.
- A tiny bounded enumeration over those quotient variables found
  `2416`
  integral solutions to the linear system.
- Imposing the full quotient identity
  `Q^2 = 9K - 2Q`,
  where every row of `K` is the cell-size vector `[1,9,9,9,12]`,
  still leaves
  `11`
  integral quotient matrices.
- One explicit quotient solution is
  ```text
  [0,9,9,0,0]
  [1,0,0,7,10]
  [0,7,7,2,2]
  [1,6,6,1,4]
  [0,3,3,6,6]
  ```

Conclusion of Approach B:
- The natural fixed-vertex five-cell quotient route is locally consistent, even after imposing the exact quotient polynomial.
- So this strengthened local contradiction does not settle the existence question.

Self-check:
- The code only tested a quotient-level consistency question after the handwritten equations were fixed.
- Finding quotient solutions means I should not claim any contradiction from this strengthened local model.

## lemma_graph
1. Lock the problem as a `40 x 40` zero-diagonal `0/1` matrix with row and column sum `18` and `A^2 = 9J - 2A`.
2. Restrict to the sum-zero subspace to force the spectrum `18^1, (-2)^9, 0^30`, hence `rank(A) = 10`.
3. Pass to `C = J - I - A` and derive the cleaner identity `C^2 = I + 11J`, the spectrum `21^1, 1^9, (-1)^30`, `det(C) = 21`, and `C^-1 = C - (11/21)J`.
4. Repackage this as a sign-matrix statement: `H = J - 2I - 2A` is a `±1` matrix with row and column sums `2` and exact square `H^2 = 4I`.
5. Fix a vertex `x` and derive the exact three-cell quotient `[[0,9,9],[1,7,10],[0,9,9]]` on `({x}, N^-(x), V \ ({x} union N^-(x)))`.
6. Compute `A^3 = 144J + 4A`, hence exactly `1920` directed `3`-cycles and `144` through each vertex.
7. Record the full unconditional `M/O/I/N(x)` block-total system.
8. Rule out all abelian Cayley realizations exactly by character sums.
9. Test the strengthened five-cell out-equitable quotient ansatz and find it locally feasible rather than contradictory.

## chosen_plan
- The best first path was the invariant route because the dossier already pointed to the quadratic adjacency identity and rank obstruction.
- The cleanest reformulation I found is not `A(A + 2I) = 9J` itself, but the complementary matrix identity
  `C^2 = I + 11J`
  and the equivalent sign-matrix identity
  `H^2 = 4I`.
- After extracting that exact algebra package, the most targeted construction-style check was the abelian Cayley route, which fails exactly.
- I then used one tiny bounded computation only to test the strongest nearby local quotient contradiction suggested by the fixed-vertex partition. That route survives.
- So the strongest honest solve-stage outcome is still `PARTIAL`, not a proof and not a disproof.

Self-check:
- I am stopping because the exact statements proved here are structural obstructions and reformulations, not a complete existence theorem or complete impossibility theorem.
- Lean should stay off because there is no exact candidate witness or exact counterexample yet.

## self_checks
- Statement fidelity:
  - the exact tuple `(40,18,9,7,9)` stayed locked throughout;
  - the core identity `A^2 = 9J - 2A` was used consistently.
- Structural algebra:
  - spectrum `18^1, (-2)^9, 0^30` is correct;
  - `rank(A) = 10` and `nullity(A) = 30` are correct;
  - `C = J - I - A` satisfies `C^2 = I + 11J`;
  - `C` has spectrum `21^1, 1^9, (-1)^30`, determinant `21`, and inverse `C - (11/21)J`;
  - `H = J - 2I - 2A` satisfies `H^2 = 4I`.
- Local structure:
  - the exact three-cell quotient is `[[0,9,9],[1,7,10],[0,9,9]]`;
  - the `M/O/I/N(x)` totals written in Approach A are exact aggregate consequences of the dsrg axioms.
- Further obstructions:
  - any realization must be strongly nonnormal;
  - no abelian Cayley realization exists.
- Scope honesty:
  - I did not construct a witness;
  - I did not prove global nonexistence;
  - the strengthened five-cell quotient model remains locally feasible.

## code_used
- One tiny bounded Python enumeration was used only after the handwritten `M/O/I/N(x)` system had been derived.
- Purpose: test the strengthened ansatz that `({x}, M(x), O(x), I(x), N(x))` is an exact out-equitable partition with quotient satisfying the inherited quadratic identity.
- Result:
  - `2416` integral quotient matrices satisfy the linear count constraints;
  - `11` of those also satisfy the full quotient identity `Q^2 = 9K - 2Q`.
- No graph search, SAT, ILP, CP-SAT, or adjacency-matrix brute force was used.

Self-check:
- The code was directly tied to a single local hypothesis and stayed well inside the solve-stage code policy.
- The computation reduced overclaiming rather than manufacturing a speculative result.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact outputs from this pass:
  - the exact normalization `A^2 = 9J - 2A`,
  - the forced spectrum `18^1, (-2)^9, 0^30`,
  - the rank statement `rank(A) = 10`,
  - the complementary reformulation `C^2 = I + 11J`, with `det(C) = 21` and `C^-1 = C - (11/21)J`,
  - the sign-matrix reformulation `H^2 = 4I`,
  - the exact three-cell quotient `[[0,9,9],[1,7,10],[0,9,9]]`,
  - exactly `1920` directed `3`-cycles and `144` through each vertex,
  - no abelian Cayley realization,
  - and the fact that the natural five-cell quotient route remains locally consistent.
- I did not prove existence.
- I did not prove nonexistence.
- Lean was intentionally left off.

## likely_failure_points
- The clean identities `C^2 = I + 11J` and `H^2 = 4I` are rigid, but I did not find the missing bridge from them to a contradiction involving `A^T`, common out-neighbor counts, or a global classification of such nonnormal matrices.
- The fixed-vertex partition leaves enough room that even the strengthened five-cell out-equitable quotient ansatz survives locally.
- A true closure may require a transpose-sensitive argument, a coherent-configuration classification, or a deeper design-theoretic interpretation of `C^2 = I + 11J`.

## what_verify_should_check
- Recompute `A^2 = 9J - 2A`, the forced spectrum `18^1, (-2)^9, 0^30`, and the rank `10`.
- Recheck `C = J - I - A`, the identity `C^2 = I + 11J`, the determinant `21`, and the inverse `C - (11/21)J`.
- Recheck `H = J - 2I - 2A` and `H^2 = 4I`.
- Recheck the exact three-cell quotient `[[0,9,9],[1,7,10],[0,9,9]]` and its characteristic polynomial `u(u+2)(u-18)`.
- Recheck `A^3 = 144J + 4A` and the resulting directed-triangle count `1920`.
- Recheck the abelian Cayley character-sum contradiction.
- Recheck the tiny quotient enumeration and verify that the displayed sample matrix really satisfies `Q^2 = 9K - 2Q`.
- Keep the classification conservative: this artifact supports `PARTIAL`, not `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.

## verify_rediscovery
- PASS 1 used a bounded exact-tuple prior-art audit with searches centered on the exact tuple `(40,18,9,7,9)`, reordered / alternate dsrg notation, the Hobart-Brouwer canonical table, and explicit checks for theorem / proposition / example / observation / corollary coverage in that source line.
- The canonical source still lists `(40,18,9,7,9)` with `?` and the bounded exact-instance search did not surface a later paper, construction, or nonexistence theorem settling this exact tuple.
- I therefore do not find rediscovery established within budget.
- If the solve-stage algebra package is correct, it still appears to be a correct partial analysis of a still-open exact instance rather than a proof of a known solved theorem.

## verify_faithfulness
- The artifact stays faithful to the intended statement. It never upgrades a structural lemma into an existence or nonexistence theorem.
- The matrix identity specialization is exact: for `(v,k,t,lambda,mu) = (40,18,9,7,9)`, one gets `A^2 = 9I + 7A + 9(J - I - A) = 9J - 2A`.
- The scope is also stated correctly: the abelian Cayley argument rules out only abelian Cayley realizations, and the five-cell quotient computation tests only a strengthened local ansatz.
- No wrong-theorem drift, quantifier drift, or definition change found.

## verify_proof
- I found no incorrect step in the claimed partial results.
- The forced spectrum / rank argument is correct once both row and column sums are fixed to `18`, because `j` and `j^\top` are eigenvectors and `j^\perp` is `A`-invariant.
- The complementary reformulation is correct: `C := J - I - A` satisfies `C^2 = I + 11J`; from that, the stated spectrum, determinant `21`, and inverse `C - (11/21)J` follow.
- The sign-matrix reformulation is correct: with `H := 2C - J`, the identities `CJ = JC = 21J` imply `H^2 = 4I`.
- The fixed-vertex three-cell quotient `[[0,9,9],[1,7,10],[0,9,9]]` is correct, and its characteristic polynomial vanishes at `0`, `-2`, and `18` as claimed.
- The triangle count is correct: `A^3 = A(9J - 2A) = 144J + 4A`, so `trace(A^3) = 5760`, hence `1920` directed `3`-cycles.
- The abelian Cayley obstruction is correct: nonprincipal character values are forced into `{0,-2}`, and Parseval gives `324 + 4a = 720`, so `a = 99`, impossible.

## verify_adversarial
- I reran local arithmetic checks in plain Python.
- The displayed five-cell sample quotient really satisfies `Q^2 = 9K - 2Q`.
- The three-cell quotient also passes the advertised spectral check: its characteristic polynomial vanishes at `0`, `-2`, and `18`.
- The normality warning is sound: `trace(AA^\top) = 40 * 18 = 720`, while the sum of squared eigenvalue moduli from the forced spectrum is only `18^2 + 9 * 2^2 = 360`, so any realization would indeed be nonnormal.
- I did not find a counterexample to any stated lemma. The only caution is interpretive: the sample five-cell quotient has no reason to have balanced column sums, because only out-equitability was asserted.

## verify_verdict
- `VERIFIED`
- Classification remains `PARTIAL`, not `CANDIDATE`, `COUNTEREXAMPLE`, `VARIANT`, or `EXACT`.
- `lean_ready = false` because the artifact still does not contain an exact existence proof, exact nonexistence proof, or exact witness/counterexample for the intended dsrg instance.

## minimal_repair_if_any
- No repair applied.
- The only conservative clarification needed is that the verification supports the solve-stage package as a sound partial analysis, not a complete resolution of the instance.
