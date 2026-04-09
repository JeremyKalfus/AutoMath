# dsrg-30-11-9-2-5

## statement_lock
- Active slug: `dsrg-30-11-9-2-5`
- Title: `Does a directed strongly regular graph with parameters (30,11,9,2,5) exist?`
- Locked intended statement: determine whether there exists a loopless directed strongly regular graph with parameters
  `(v,k,t,lambda,mu) = (30,11,9,2,5)`.
- Exact matrix form used throughout:
  - `AJ = JA = 11J`,
  - `A_ii = 0`,
  - `A^2 = tI + lambda A + mu(J - I - A) = 9I + 2A + 5(J - I - A) = 5J + 4I - 3A`.
- On the sum-zero subspace `1^\perp`, this forces
  `u^2 + 3u - 4 = 0`,
  so the only restricted eigenvalues are `1` and `-4`.
- Using `trace(A) = 0` and `1 + m_1 + m_{-4} = 30`, the spectrum is forced to be
  `11^1, 1^21, (-4)^8`.
- Since `0` is not an eigenvalue, `A` is invertible, and solving against the quadratic identity gives
  `A^(-1) = (1/4)A + (3/4)I - (5/44)J`.

Self-check:
- The locked statement is still the exact existence problem, not a variant family.
- The specialized identity `A^2 = 5J + 4I - 3A` and spectrum `11^1,1^21,(-4)^8` are internally consistent.

## definitions
- Fix a vertex `x`.
- Let
  - `U = N^+(x)`,
  - `W = N^-(x)`,
  - `M = U ∩ W`,
  - `O = U \ W`,
  - `I = W \ U`,
  - `N = V \ ({x} ∪ M ∪ O ∪ I)`.
- Since `k = 11` and `t = 9`, the class sizes are forced:
  - `|M| = 9`,
  - `|O| = 2`,
  - `|I| = 2`,
  - `|N| = 16`.
- For block totals, write `e(C,D)` for the number of arcs from cell `C` to cell `D`, with `C,D in {M,O,I,N}`.
- I also use the coarser partition
  - `W = N^-(x)`, with `|W| = 11`,
  - `R = V \ ({x} ∪ W)`, with `|R| = 18`.

Ambiguities / conventions:
- The solve pass uses only the standard loopless dsrg definition from `selected_problem.md`.
- No symmetry, normality, Cayley, association-scheme, or vertex-transitivity assumption is added.

Self-check:
- The classes `M,O,I,N` sum to `29`, so together with `x` they cover all `30` vertices.
- The notation keeps the exact one-vertex data separate from later optional structure.

## approach_A
- Structural / invariant route: push the quadratic identity, the coarse equitable quotient, and the one-vertex block counts before considering any search.

Major step 1: shifted idempotent package.
- Set `B := A + 4I`. Then
  `B^2 = A^2 + 8A + 16I = 5J + 20I + 5A = 5J + 5B`.
- Define
  `P := B/5 - J/10 = (A + 4I)/5 - J/10`.
- Using `BJ = JB = 15J` and `J^2 = 30J`, a direct expansion gives `P^2 = P`.
- The diagonal entries of `P` are all
  `4/5 - 1/10 = 7/10`,
  so `trace(P) = 30 * 7/10 = 21`.
- Therefore `P` is an idempotent of rank `21`, and `B = 5P + J/2`.
- Equivalently, the integer matrix
  `M0 := 10P = 2A + 8I - J`
  has diagonal `7`, off-diagonal entries `±1`, row and column sums `0`, and satisfies
  `M0^2 = 10 M0`.

Self-check:
- The shift is the natural one: `11,1,-4` moves to `15,5,0`.
- `trace(P) = rank(P) = 21` is correct for an idempotent.

Major step 2: exact three-cell quotient around one vertex.
- For the partition `({x}, W, R)`, the outgoing counts are forced:
  - from `x`: `(0,9,2)`,
  - from any `y in W`: `(1,2,8)`, because `y -> x` and `|N^+(y) ∩ W| = lambda = 2`,
  - from any `y in R`: `(0,5,6)`, because `y -/-> x` and `|N^+(y) ∩ W| = mu = 5`.
- So the exact quotient matrix is
  `Q = [[0,9,2],[1,2,8],[0,5,6]]`.
- Its row sums are `11`, and its remaining eigenvalues are `1` and `-4`, matching the global spectrum.

Self-check:
- The only nontrivial entry is the count into `W`, and that is exactly the dsrg `2`-path axiom specialized to target `x`.
- The quotient is genuinely exact, not an average statement.

Major step 3: exact directed-triangle count.
- Using the quadratic identity once more,
  `A^3 = A(5J + 4I - 3A) = 55J + 4A - 3(5J + 4I - 3A) = 40J - 12I + 13A`.
- Hence
  `trace(A^3) = 30 * (40 - 12) = 840`.
- In a loopless digraph, each directed `3`-cycle contributes `3` to `trace(A^3)`, so the total number of directed triangles is
  `840 / 3 = 280`.
- Through a fixed vertex `x`, this also appears locally:
  - each arc `x -> y` with `y in M` lies in `lambda = 2` directed triangles,
  - each arc `x -> y` with `y in O` lies in `mu = 5` directed triangles,
  so each vertex lies in exactly
  `9 * 2 + 2 * 5 = 28`
  directed triangles.

Self-check:
- The cubic identity follows mechanically from `A^2 = 5J + 4I - 3A`.
- The local and global triangle counts agree: `30 * 28 = 3 * 280`.

Major step 4: exact `M/O/I/N` block-total family.
- Let
  - `a = e(M,M)`, `b = e(M,O)`, `c = e(M,I)`, `d = e(M,N)`,
  - `e = e(O,M)`, `f = e(O,O)`, `g = e(O,I)`, `h = e(O,N)`,
  - `p = e(I,M)`, `q = e(I,O)`, `r = e(I,I)`, `s = e(I,N)`,
  - `u = e(N,M)`, `v = e(N,O)`, `w = e(N,I)`, `z = e(N,N)`.
- The dsrg path counts force
  - `a + c = 18`,
  - `p + r = 4`,
  - `e + g = 10`,
  - `u + w = 80`,
  - `a + e = 18`,
  - `b + f = 4`,
  - `c + g = 10`,
  - `d + h = 80`.
- Row and column sums then reduce the whole block-total system to the exact four-parameter family

  ```text
        to:    M        O        I        N
  from M      a        b      18-a     72-b
  from O    18-a      4-b      a-8      8+b
  from I     4-r       q        r      16-q
  from N    68+r     16-q     12-r     80+q
  ```

- Capacity constraints on the `2 x 2` blocks give
  - `8 <= a <= 12`,
  - `2 <= b <= 4`,
  - `0 <= r <= 2`,
  - `0 <= q <= 4`.
- The triangle types through `x` are therefore forced in aggregate:
  - `a` triangles of type `x -> M -> M -> x`,
  - `18-a` of type `x -> M -> I -> x`,
  - `18-a` of type `x -> O -> M -> x`,
  - `a-8` of type `x -> O -> I -> x`.

Self-check:
- Every displayed total checks simultaneously against the dsrg path counts and the row/column sums.
- The family is exact bookkeeping, not an equitability assumption.

## approach_B
- Construction / extremal / contradiction route: repackage the digraph into its mutual and asymmetric parts, and test the natural structural obstructions.

Major step 1: symmetric/asymmetric decomposition.
- Let `S` be the undirected graph of mutual adjacencies:
  `x ~ y` iff `x -> y` and `y -> x`.
- Let `C` be the digraph of asymmetric arcs:
  `x ->_C y` iff `x -> y` and `y -/-> x`.
- Then every vertex has
  - `deg_S(x) = 9`,
  - `outdeg_C(x) = indeg_C(x) = 2`.
- So the dsrg is the superposition of a `9`-regular simple graph `S` and a `2`-in, `2`-out digraph `C` on the same `30` vertices.

Self-check:
- This is only a decomposition of the locked dsrg data; no new hypothesis has been added.
- The degree counts match `t = 9` and `k - t = 2`.

Major step 2: a concrete local sparsity theorem for the mutual graph.
- Fix `x`, and let `y in M(x)`.
- Any common neighbor of `x` and `y` in the mutual graph `S` is a vertex `z in M(x)` with `y -> z`.
- But because `y -> x`, the dsrg rule gives `|N^+(y) ∩ W(x)| = lambda = 2`, and `W(x) = M(x) ∪ I(x)`.
- Therefore `y` has at most `2` out-neighbors inside `M(x) ∪ I(x)`, so in particular `y` has at most `2` mutual neighbors inside `M(x)`.
- Equivalently:
  - for every adjacent pair `x ~ y` in `S`, the number of common neighbors of `x` and `y` in `S` is at most `2`;
  - for every vertex `x`, the induced mutual-neighbor graph `S[M(x)]` has maximum degree at most `2`.
- A corollary is that the total number of triangles in the mutual graph `S` is at most
  `|E(S)| * 2 / 3 = (30 * 9 / 2) * 2 / 3 = 90`.

Self-check:
- The common-neighbor bound uses only the exact dsrg rule `lambda = 2`.
- The conclusion is genuinely about the intended tuple, not a side variant.

Major step 3: nonnormality and the failed abelian-Cayley route.
- Since every row of `A` has `11` ones,
  `trace(AA^T) = 30 * 11 = 330`.
- If `A` were normal, this would equal the sum of squared eigenvalue moduli
  `11^2 + 21 * 1^2 + 8 * 4^2 = 121 + 21 + 128 = 270`,
  which is false.
- So any realization must be strongly nonnormal.
- I also checked the clean abelian-Cayley route. For an abelian Cayley realization with connection set `D` of size `11`, every nonprincipal character value would have to satisfy
  `chi(D)^2 + 3 chi(D) - 4 = 0`,
  hence `chi(D) in {1,-4}`.
- Parseval gives
  `121 + a + 16(29-a) = 30 * 11 = 330`,
  so `a = 17`.
- That arithmetic is consistent, so the abelian-Cayley route does not close a contradiction here.

Self-check:
- The nonnormality obstruction is exact and unconditional.
- The abelian-Cayley computation is recorded as a failed contradiction attempt, not a theorem.

## lemma_graph
1. Lock the dsrg as a `30 x 30` zero-diagonal `0/1` matrix with row and column sums `11` and `A^2 = 5J + 4I - 3A`.
2. Restrict to `1^\perp` to force the nontrivial eigenvalues `1` and `-4`, hence the spectrum `11^1, 1^21, (-4)^8`.
3. Derive `A^(-1) = A/4 + 3I/4 - 5J/44`.
4. Shift to `B = A + 4I`, package the `1`-eigenspace by the idempotent `P = (A + 4I)/5 - J/10`, and record `rank(P) = 21`.
5. Fix a vertex `x` and derive the exact three-cell quotient `[[0,9,2],[1,2,8],[0,5,6]]` on `({x},W,R)`.
6. Compute `A^3 = 40J - 12I + 13A`, hence exactly `280` directed triangles and exactly `28` through each vertex.
7. Refine to the `M/O/I/N` partition and reduce all block totals to the four-parameter family in `a,b,r,q`.
8. Decompose the digraph into the mutual graph `S` and asymmetric part `C`.
9. Prove the exact local sparsity theorem: every adjacent pair in `S` has at most `2` common neighbors in `S`, equivalently `S[M(x)]` has maximum degree at most `2` for every `x`.
10. Record the exact nonnormality obstruction and the fact that the abelian-Cayley arithmetic remains feasible.

## chosen_plan
- Approach A was the best primary route because the tuple already comes with a rigid quadratic identity and the one-vertex partition is unusually tight: only `2` out-only and `2` in-only neighbors.
- I pushed that route first until it yielded:
  - the exact spectrum and inverse,
  - the rank-`21` idempotent package,
  - the exact three-cell quotient,
  - the exact triangle count,
  - and the exact four-parameter `M/O/I/N` block family.
- After that, Approach B was the natural contradiction attempt. It did not settle nonexistence, but it did produce two exact constraints:
  - the mutual graph is `9`-regular with adjacent-pair common-neighbor count at most `2`,
  - any witness must be nonnormal.
- The abelian-Cayley route stayed arithmetically possible, so I stopped short of any global existence or nonexistence claim.

Self-check:
- The strongest honest solve-stage output is structural, not final.
- Lean should remain off because there is no exact intended proof or exact intended disproof to formalize.

## self_checks
- Statement fidelity:
  - the exact tuple `(30,11,9,2,5)` stayed locked throughout;
  - the matrix identity `A^2 = 5J + 4I - 3A` was used consistently.
- Algebra package:
  - spectrum `11^1, 1^21, (-4)^8` is correct;
  - `A^(-1) = A/4 + 3I/4 - 5J/44` is correct;
  - `P = (A + 4I)/5 - J/10` is idempotent of rank `21`;
  - `M0 = 2A + 8I - J` satisfies `M0^2 = 10 M0`.
- Local structure:
  - the exact quotient on `({x},W,R)` is `[[0,9,2],[1,2,8],[0,5,6]]`;
  - the `M/O/I/N` block totals reduce to the displayed four-parameter family.
- Triangle structure:
  - there are exactly `280` directed triangles;
  - each vertex lies in exactly `28` directed triangles.
- Mutual-graph structure:
  - the mutual graph `S` is `9`-regular;
  - every adjacent pair in `S` has at most `2` common neighbors in `S`;
  - each induced graph `S[M(x)]` has maximum degree at most `2`.
- Construction checks:
  - any witness must be nonnormal;
  - the abelian-Cayley route does not yield a contradiction at solve stage.
- Conservatism:
  - this writeup does not claim a construction, a counterexample, or a full nonexistence proof.

## code_used
- No code used.
- Reason: the handwritten structural routes still produced exact new constraints, and I did not isolate a small enough residual search target to justify even a tiny local exact search yet.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact outputs from this solve pass:
  - the forced spectrum `11^1, 1^21, (-4)^8`,
  - the inverse formula `A^(-1) = A/4 + 3I/4 - 5J/44`,
  - the rank-`21` idempotent `P = (A + 4I)/5 - J/10`,
  - the exact three-cell quotient `[[0,9,2],[1,2,8],[0,5,6]]`,
  - the exact directed-triangle count `280`,
  - the exact four-parameter local block family on `M/O/I/N`,
  - the mutual-graph sparsity theorem that adjacent mutual pairs have at most `2` common mutual neighbors,
  - and the exact nonnormality obstruction.
- I did not prove existence, I did not prove nonexistence, and I did not turn on Lean.

## likely_failure_points
- The `M/O/I/N` block reduction is bookkeeping-heavy; verification should independently rederive the row/column equations before trusting the four-parameter family.
- The mutual-graph common-neighbor bound should be checked carefully to make sure the target set is really `W(x) = M(x) ∪ I(x)`.
- The abelian-Cayley arithmetic check is only a failed route, not evidence for existence; verification should avoid overreading it.
- Because no code was used, there may still be a narrowly targeted local search opportunity inside the `13`-vertex `M ∪ O ∪ I ∪ {x}` configuration that solve did not exploit.

## what_verify_should_check
- Recompute the normalization `A^2 = 5J + 4I - 3A`, the spectrum `11^1,1^21,(-4)^8`, and the inverse formula for `A`.
- Recheck the idempotent package:
  - `P = (A + 4I)/5 - J/10`,
  - `P^2 = P`,
  - `trace(P) = 21`.
- Re-derive the exact quotient matrix on `({x},W,R)` and confirm its nontrivial eigenvalues are `1` and `-4`.
- Recheck `A^3 = 40J - 12I + 13A` and the total of `280` directed triangles.
- Re-derive the full `M/O/I/N` block-total family and the bounds
  - `8 <= a <= 12`,
  - `2 <= b <= 4`,
  - `0 <= r <= 2`,
  - `0 <= q <= 4`.
- Recheck the mutual-graph lemma:
  - for `x ~ y` in the mutual graph, the number of common mutual neighbors is at most `2`,
  - equivalently `S[M(x)]` has maximum degree at most `2`.
- Recheck the nonnormality obstruction `trace(AA^T) = 330 != 270`.
- After the bounded rediscovery pass, decide whether the next best action is
  - a skeptical proof check only, or
  - a narrowly justified exact local search on the `M/O/I` configuration, rather than a full-graph SAT or brute-force branch.

## verify_rediscovery
- PASS 1 used a bounded web audit focused on the exact tuple `(30,11,9,2,5)`, alternative dsrg notation, the Hobart-Brouwer canonical table, and later status checks.
- The canonical source still lists the row `(30,11,9,2,5)` with `?`, not with a construction or a nonexistence tag.
- A later status paper I checked, Greaves-Hubaut-Koolen `Directed strongly regular dihedrants and 2-arc-transitive Cayley digraphs` (RISC preprint, 2021), explicitly rules out vertex-transitive realizations for some parameter sets and still includes `(30,11,9,2,5)` among the open general cases rather than claiming a full solution.
- I did not find an exact-instance construction, impossibility theorem, proposition, example, or corollary settling the full dsrg existence question for `(30,11,9,2,5)`.
- Rediscovery verdict: not established within the bounded search budget.

## verify_faithfulness
- The solve record stayed locked to the exact intended statement: existence or nonexistence of a loopless dsrg with parameters `(30,11,9,2,5)`.
- The main algebra package is faithful to that statement:
  - `A^2 = 5J + 4I - 3A`,
  - `AJ = JA = 11J`,
  - zero diagonal,
  - and the one-vertex partition `M,O,I,N` derived from one fixed vertex `x`.
- No wrong-theorem drift or proxy problem substitution was found.
- The verifier repair below also stays on the exact intended statement; it does not switch to a restricted family such as Cayley or vertex-transitive dsrgs.

## verify_proof
- PASS 3 found the first incorrect step in `approach_A`, Major step 4, in the displayed `M/O/I/N` block-total family.
- The row sum for the `M` block was misapplied. Since `|M| = 9` and each vertex has out-degree `11`, one must have
  `a + b + c + d = 9 * 11 = 99`.
- Together with the valid path-count identity `a + c = 18`, this gives
  `d = 81 - b`,
  not `d = 72 - b`.
- The rest of the local identities used there are standard dsrg specializations and check out:
  - `a + e = 18`,
  - `e + g = 10`,
  - `b + f = 4`,
  - `d + h = 80`,
  - `e + f + g + h = 2 * 11 = 22`.
- Eliminating `e,f,g,d,h` from these valid equations yields
  - `e = 18 - a`,
  - `g = a - 8`,
  - `f = 4 - b`,
  - `h = 8 + b`,
  - `d = 81 - b`.
- Therefore
  `d + h = (81 - b) + (8 + b) = 89`,
  contradicting the independently required identity `d + h = 80`.
- This contradiction is local, exact, and uses only the dsrg axioms for the tuple `(30,11,9,2,5)`.
- Conclusion of PASS 3: the solve record’s partial bookkeeping contained a small arithmetic mistake, and correcting it produces an exact nonexistence proof. No earlier invalid step was needed for the contradiction.

## verify_adversarial
- PASS 4 rechecked the contradiction by direct elimination with a tiny local Python script, without any search over graphs.
- The script confirmed that the valid local equations admit no solution and that `d + h` is forced to be `89`, never `80`.
- No code witness or candidate graph existed to rerun or break; the adversarial target here was the counting system itself.
- I also rechecked the other headline algebra claims manually:
  - the restricted eigenvalues `1` and `-4` follow from `u^2 + 3u - 4 = 0` on `1^\perp`,
  - the multiplicities `21` and `8` follow from trace and dimension,
  - the quotient matrix on `({x},W,R)` is consistent.
- Those facts are no longer the bottleneck because the local counting contradiction already forbids existence.

## verify_verdict
- `verify_verdict = "MINOR_FIX"`
- Classification after verification: `COUNTEREXAMPLE`.
- Confidence: `high`.
- `lean_ready = true`.
- Reason:
  - no rediscovery was established in PASS 1,
  - the intended statement stayed exact,
  - and a minimal arithmetic repair converts the solver's local block-count argument into an exact contradiction proving that no dsrg with parameters `(30,11,9,2,5)` exists.
- This is still not `EXACT` because Lean has not yet checked the repaired disproof.

## minimal_repair_if_any
- Replace the incorrect line in the displayed four-parameter family
  - from `d = 72 - b`
  - to `d = 81 - b`.
- Then keep the already valid identities
  - `h = 8 + b`
  - and `d + h = 80`.
- These imply `89 = d + h = 80`, contradiction.
- Minimal repaired proof sketch:
  1. Fix a vertex `x` and partition `V \\ {x}` into `M,O,I,N` with sizes `9,2,2,16`.
  2. Let `a,b,c,d,e,f,g,h` count arcs from `M,O` into `M,O,I,N` as in the record.
  3. From the dsrg two-path axiom:
     - `a + c = 18`,
     - `a + e = 18`,
     - `e + g = 10`,
     - `b + f = 4`,
     - `d + h = 80`.
  4. From row sums:
     - `a + b + c + d = 99`,
     - `e + f + g + h = 22`.
  5. Hence `d = 81 - b` and `h = 8 + b`.
  6. Therefore `d + h = 89`, contradicting `d + h = 80`.
  7. So a dsrg with parameters `(30,11,9,2,5)` cannot exist.

## lean_statement
- Backend file: `lean/AutoMath/DSRG3011925.lean`
- Mirrored Lean file: `artifacts/dsrg-30-11-9-2-5/lean/AutoMath/DSRG3011925.lean`
- Exact Lean target:
  - `AutoMath.DSRG3011925.intendedStatement := ∃ Adj : Fin 30 → Fin 30 → Prop, IsDSRG3011925 Adj`
  - `AutoMath.DSRG3011925.exactCounterexampleStatement := ¬ intendedStatement`
- Exact statement theorem written first:
  - `AutoMath.DSRG3011925.no_dsrg_30_11_9_2_5_statement`
  - `AutoMath.DSRG3011925.exact_counterexample_statement_faithful`
- This keeps the Lean target locked to the exact intended dsrg existence question on `Fin 30`, not a proxy family or a local linear subsystem.

## lean_skeleton
- The proof skeleton is recorded as
  - `AutoMath.DSRG3011925.no_dsrg_30_11_9_2_5_skeleton`
- Skeleton plan kept in the file:
  1. fix a vertex `x` and split `V \ {x}` into `M,O,I,N`;
  2. translate the dsrg two-path rules into exact block-total equations;
  3. derive a contradiction only from faithful equations.
- I did not write a final `no_dsrg_30_11_9_2_5` theorem because the current verification repair fails the faithfulness audit below.

## lean_result
- `lake build AutoMath.DSRG3011925` succeeded in the official `lean/` AutoMath backend on 2026-04-09.
- The mirrored Lean source under `artifacts/dsrg-30-11-9-2-5/lean/AutoMath/DSRG3011925.lean` is byte-identical to the backend file.
- `lake env lean ../artifacts/dsrg-30-11-9-2-5/lean/AxiomAudit.lean` succeeded.
- The axiom audit reported:
  - `no_dsrg_30_11_9_2_5_statement`: `[propext, Classical.choice, Quot.sound]`
  - `exact_counterexample_statement_faithful`: `[propext, Classical.choice, Quot.sound]`
  - `no_dsrg_30_11_9_2_5_skeleton`: `[propext, Classical.choice, Quot.sound]`
  - arithmetic blocker lemmas: `[propext, Quot.sound]` or `[propext, Classical.choice, Quot.sound]`
- No `sorryAx` appeared in the audit output for the theorems checked.
- `lean4checker --fresh` is unavailable on this machine (`lean4checker not found`).
- Repo-wide `lake build` still fails in unrelated existing modules:
  - `lean/AutoMath/C16458CNBC.lean`
  - `lean/AutoMath/C244512CNBC.lean`
- Therefore the new module checks locally, but the repository as a whole still has pre-existing Lean failures unrelated to this slug.
- Lean did not produce a full exact theorem for the selected problem, so this run does not qualify for `classification = EXACT`.

## lean_blockers
- The current verification repair is not faithful to the intended statement.
- The claimed contradiction replaces the correct mutual-block row sum
  - `a + b + c + d = 90`
  with the incorrect value
  - `a + b + c + d = 99`.
- The missing `9` comes from the forced arcs `y -> x` for `y in M`; those arcs are outside the `M/O/I/N` block totals and cannot be counted inside `a+b+c+d`.
- With the faithful row sums, Lean proves:
  - `AutoMath.DSRG3011925.correct_row_sum_consequence`: `d = 72 - b`
  - `AutoMath.DSRG3011925.out_only_row_sum_consequence`: `h = 8 + b`
  - `AutoMath.DSRG3011925.corrected_local_constraints_force_d_plus_h`: `d + h = 80`
- So the advertised `89 = 80` contradiction disappears.
- Lean also proves the faithful local linear system is consistent via
  - `AutoMath.DSRG3011925.corrected_local_constraints_consistent`
  using the explicit witness `(a,b,c,d,e,f,g,h) = (8,2,10,70,10,2,0,10)`.
- Net effect: the current nonexistence claim is not strong enough to formalize to an exact theorem. The run should be downgraded from `COUNTEREXAMPLE` to a conservative non-Lean status until a new faithful argument is found.
