# dsrg-27-7-4-1-2

## statement_lock
- Active slug: `dsrg-27-7-4-1-2`
- Title: `Does a directed strongly regular graph with parameters (27,7,4,1,2) exist?`
- Locked intended statement: determine whether there exists a loopless directed strongly regular graph with parameters `(v,k,t,lambda,mu) = (27,7,4,1,2)`.
- Exact matrix reformulation used here: there exists a `27 x 27` `0/1` matrix `A` such that
  - `A_ii = 0` for all `i`,
  - every row sum and every column sum is `7`,
  - `A^2 = tI + lambda A + mu(J - I - A) = 4I + A + 2(J - I - A) = 2J + 2I - A`.
- So for every ordered pair of distinct vertices `(x,y)`, the number of directed `2`-paths `x -> z -> y` is `1` when `x -> y` and `2` otherwise, while `(A^2)_{xx} = 4` for every vertex `x`.

Self-check:
- The intended statement stayed exact: existence of the dsrg itself, not only a special construction class.
- The specialization `A^2 = 2J + 2I - A` is the correct dsrg identity for `(27,7,4,1,2)`.

## definitions
- `J` is the all-ones matrix and `j` is the all-ones column vector.
- For a fixed vertex `x`, write
  - `U = N^+(x)`,
  - `W = N^-(x)`,
  - `M = U cap W`,
  - `O = U \ W`,
  - `I = W \ U`,
  - `N = V \ ({x} union U union W)`.
- Since `k = 7` and `t = 4`, the local class sizes are forced:
  - `|M| = 4`,
  - `|O| = 3`,
  - `|I| = 3`,
  - `|N| = 16`.
- I use `R = V \ ({x} union W)`, so `|R| = 19`.

Ambiguities / conventions:
- The solve pass uses only the standard loopless dsrg definition from the dossier.
- No symmetry, normality, vertex-transitivity, Cayley assumption, or equitable-partition assumption is added unless explicitly stated.

Self-check:
- The class sizes sum to `26`, so together with `x` they cover all `27` vertices.
- The notation cleanly separates the exact forced data (`U`, `W`, `M/O/I/N`) from later optional hypotheses.

## approach_A
- Structural / invariant route: push the quadratic identity and one-vertex partition as far as possible before considering any construction-specific obstruction.

Major step 1: forced spectrum and inverse.
- Since `Aj = 7j`, on the `26`-dimensional sum-zero subspace the identity becomes
  `A^2 = 2I - A`.
- Therefore every nontrivial eigenvalue is a root of
  `u^2 + u - 2 = 0`,
  hence is `1` or `-2`.
- Let the multiplicities be `m_1` and `m_-2`. Using `m_1 + m_-2 = 26` and `trace(A) = 0 = 7 + m_1 - 2 m_-2`, we get
  - eigenvalue `7` with multiplicity `1`,
  - eigenvalue `1` with multiplicity `15`,
  - eigenvalue `-2` with multiplicity `11`.
- Writing `A^-1 = alpha A + beta I + gamma J` and using `A^2 = 2J + 2I - A` and `AJ = 7J` gives
  `A^-1 = (1/2)A + (1/2)I - (1/7)J`.

Self-check:
- The trace check is exact: `7 + 15 - 22 = 0`.
- The inverse formula matches the three eigenvalues: it gives `1/7`, `1`, and `-1/2` on the eigenspaces of `7`, `1`, and `-2`.

Major step 2: shifted idempotent package.
- Set `B := A + 2I`. Then
  `B^2 = A^2 + 4A + 4I = 2J + 6I + 3A = 2J + 3B`.
- Define
  `P := (1/3)B - (1/9)J = (A + 2I)/3 - J/9`.
- Using `BJ = JB = 9J`, `J^2 = 27J`, and `B^2 = 2J + 3B`, a direct expansion gives `P^2 = P`.
- The diagonal entries of `P` are all `5/9`, so
  `trace(P) = 27 * (5/9) = 15`.
- Hence `P` is an idempotent of rank `15`. Since `Pj = 0` and `B = 3P + J`, it follows that `rank(B) = 16`.

Self-check:
- The shift is the natural one: `7,1,-2` moves to `9,3,0`.
- The rank count is exact and uses only the trace of an idempotent and the fact that `j` is outside `im(P)`.

Major step 3: exact three-cell quotient around one vertex.
- Fix `x` and partition `V` as `({x}, W, R)`, where `W = N^-(x)` has size `7` and `R = V \ ({x} union W)` has size `19`.
- The outgoing counts into these three cells are forced:
  - from `x`: `(0,4,3)`, because `x` points to the `4` mutual neighbors and the `3` out-only neighbors;
  - from any `y in W`: `(1,1,5)`, because `y -> x` and the number of out-neighbors of `y` inside `W` is exactly the number of directed `2`-paths from `y` to `x`, namely `lambda = 1`;
  - from any `y in R`: `(0,2,5)`, because `y` does not point to `x` and the number of out-neighbors of `y` inside `W` is `mu = 2`.
- So the exact quotient matrix is
  `[[0,4,3],[1,1,5],[0,2,5]]`.

Self-check:
- The only nontrivial entries are the counts into `W`, and those are exactly the dsrg `2`-path axiom specialized to the target `x`.
- Each row sum is `7`, as required.

Major step 4: directed triangle count.
- Multiplying once more gives
  `A^3 = A(2J + 2I - A) = 14J + 2A - A^2 = 12J - 2I + 3A`.
- Therefore
  `trace(A^3) = 12 * 27 - 2 * 27 = 270`.
- In a loopless digraph each directed `3`-cycle contributes exactly `3` to `trace(A^3)`, so the total number of directed triangles is
  `270 / 3 = 90`.
- Through a fixed vertex `x`, this is also seen locally:
  - each `y in M` contributes exactly `1` triangle `x -> y -> z -> x`, because `y -> x`;
  - each `y in O` contributes exactly `2` such triangles, because `y` does not point to `x`.
- Hence each vertex lies in exactly
  `4 * 1 + 3 * 2 = 10`
  directed triangles, consistent with `90 * 3 / 27 = 10`.

Self-check:
- The formula for `A^3` follows mechanically from the quadratic identity.
- The local and global triangle counts agree.

Major step 5: exact `M/O/I/N` block-total system.
- Keep the same fixed `x`. Let `e_CD` be the total number of arcs from class `C` to class `D`, for `C,D in {M,O,I,N}`.
- The dsrg path counts force:
  - `e_MM + e_MI = 4`,
  - `e_IM + e_II = 3`,
  - `e_OM + e_OI = 6`,
  - `e_NM + e_NI = 32`,
  - `e_MM + e_OM = 4`,
  - `e_MO + e_OO = 3`,
  - `e_MI + e_OI = 6`,
  - `e_MN + e_ON = 32`.
- Together with row and column sums, this reduces the whole block-total system to the exact integer family

  ```
        to:    M        O        I        N
  from M      a        b      4-a     20-b
  from O    4-a      3-b      2+a     12+b
  from I   20-u        q     u-17     15-q
  from N      u     15-q     32-u     65+q
  ```

  with
  - `0 <= a <= 4`,
  - `0 <= b <= 3`,
  - `17 <= u <= 20`,
  - `0 <= q <= 15`.
- This is exact bookkeeping, not an assumption of equitability.
- In particular, the local totals determine
  - `U -> W = 10`,
  - `M -> W = 4`,
  - `O -> W = 6`,
  - `U -> M = 4`,
  - `U -> I = 6`.
- I tried to close a contradiction from these block totals plus triangle counts, but the parameter family remains arithmetically consistent at this level.

Self-check:
- Every displayed total checks simultaneously against the dsrg path counts, the row sums `7`, and the column sums `7`.
- This step is useful because it records exactly what the one-vertex analysis does and does not force.

## approach_B
- Construction / extremal / contradiction route: isolate exact obstructions to natural realization classes, while checking whether they already settle the full problem.

Major step 1: abelian Cayley obstruction.
- Suppose the digraph were an abelian Cayley digraph on a group `G` of order `27`, with connection set `D subseteq G`, `|D| = 7`, and identity `e notin D`.
- The dsrg identity becomes the group-ring identity
  `D^2 = 2G + 2e - D`.
- For any nonprincipal character `chi`, applying `chi` gives
  `chi(D)^2 = -chi(D) + 2`,
  so every nonprincipal character value is in `{1,-2}`.
- Parseval for subsets of a finite abelian group gives
  `sum_chi |chi(D)|^2 = |G| |D| = 27 * 7 = 189`.
- The principal character contributes `|D|^2 = 49`.
- If `a` of the `26` nonprincipal characters had value `1` and the rest had value `-2`, Parseval would read
  `49 + a + 4(26-a) = 189`,
  i.e.
  `153 - 3a = 189`,
  hence `a = -12`, impossible.
- Therefore no abelian Cayley realization exists.

Self-check:
- The contradiction is exact arithmetic, not heuristic.
- Its scope is narrower than the full problem: it rules out abelian Cayley models only.

Major step 2: nonnormality obstruction.
- `trace(AA^T) = 27 * 7 = 189`, because every row has `7` ones.
- The sum of squared moduli of the eigenvalues of `A` is
  `7^2 + 15 * 1^2 + 11 * (-2)^2 = 49 + 15 + 44 = 108`.
- If `A` were normal, these two quantities would agree.
- Since `189 != 108`, any realization must be strongly nonnormal.

Self-check:
- This rules out the entire normal-matrix regime, including the cleanest spectral constructions.
- It still does not prove global nonexistence.

## lemma_graph
1. Lock the problem as a `27 x 27` zero-diagonal `0/1` matrix with row and column sums `7` and `A^2 = 2J + 2I - A`.
2. Restrict to the sum-zero subspace to force the nontrivial eigenvalues to be `1` and `-2`.
3. Use trace to get the exact spectrum `7^1, 1^15, (-2)^11` and derive `A^-1 = (1/2)A + (1/2)I - J/7`.
4. Shift to `B = A + 2I`, derive `B^2 = 2J + 3B`, and package this as the rank-`15` idempotent `P = B/3 - J/9`, hence `rank(B) = 16`.
5. Fix a vertex `x` and derive the exact three-cell quotient `[[0,4,3],[1,1,5],[0,2,5]]` for `({x}, N^-(x), V \ ({x} union N^-(x)))`.
6. Compute `A^3 = 12J - 2I + 3A`, hence exactly `90` directed triangles and exactly `10` through each vertex.
7. Refine to the `M/O/I/N` partition and record the exact four-parameter block-total family.
8. Test the abelian Cayley route and rule it out exactly by character arithmetic.
9. Record the exact nonnormality obstruction.

## chosen_plan
- The invariant route was the best first path because the dossier already suggested the quadratic identity, spectral obstruction, and fixed-vertex partition as the most promising low-search tools.
- I pushed that route first until it produced an exact spectrum, an explicit inverse, a rank-`16` shifted matrix, an exact three-cell quotient, exact triangle counts, and the exact one-vertex block-total family.
- After that, the most targeted construction-specific check was the abelian Cayley route. It fails exactly.

Attempted rigorous closure:
- I tried to turn the `M/O/I/N` bookkeeping into a contradiction.
- What closes exactly is the local total system, not a full impossibility theorem.
- The parameters `a,b,u,q` still leave room for hypothetical nonnormal, non-Cayley realizations.
- So the strongest honest solve-stage outcome is `PARTIAL`, not `COUNTEREXAMPLE`.

Self-check:
- I am stopping because the unconditional contradictions proved here apply to important subclasses, not to all realizations.
- No code was needed to reach the current frontier of the argument.

## self_checks
- Statement fidelity:
  - the exact tuple `(27,7,4,1,2)` stayed locked throughout;
  - the matrix identity `A^2 = 2J + 2I - A` was used consistently.
- Structural algebra:
  - spectrum `7^1, 1^15, (-2)^11` is correct;
  - `A^-1 = (1/2)A + (1/2)I - J/7` is correct;
  - `B = A + 2I` satisfies `B^2 = 2J + 3B`;
  - `P = (A + 2I)/3 - J/9` is idempotent of rank `15`.
- Local structure:
  - the exact quotient on `({x}, N^-(x), V \ ({x} union N^-(x)))` is `[[0,4,3],[1,1,5],[0,2,5]]`;
  - the `M/O/I/N` block totals reduce to the displayed four-parameter family.
- Triangle structure:
  - there are exactly `90` directed triangles;
  - each vertex lies in exactly `10` directed triangles.
- Obstructions:
  - any realization must be nonnormal;
  - no abelian Cayley realization exists.
- Final honesty check:
  - I did not construct a witness;
  - I did not prove global nonexistence;
  - therefore the classification must stay conservative.

## code_used
- No code used.
- Reason: the handwritten algebraic package was exact, and I did not reach a point where a bounded experiment was clearly justified under the harness rules.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact outputs from this pass:
  - `A^2 = 2J + 2I - A`;
  - forced spectrum `7^1, 1^15, (-2)^11`;
  - explicit inverse `A^-1 = (1/2)A + (1/2)I - J/7`;
  - shifted form `B = A + 2I` with `B^2 = 2J + 3B` and `rank(B) = 16`;
  - exact quotient `[[0,4,3],[1,1,5],[0,2,5]]` for `({x}, N^-(x), V \ ({x} union N^-(x)))`;
  - exactly `90` directed triangles, hence `10` through each vertex;
  - exact one-vertex `M/O/I/N` block-total family;
  - exact nonexistence of abelian Cayley realizations;
  - exact nonnormality requirement.
- I did not prove existence or nonexistence for arbitrary realizations.
- Lean should stay off.

## likely_failure_points
- The main gap is global: the one-vertex block totals are sharp but still do not force a contradiction.
- I did not prove that the full five-cell partition is equitable; assuming that would be unjustified.
- The idempotent package is strong, but without exact control of `AA^T` or `A^T A` it does not by itself settle the problem.
- The dossier carries medium rediscovery risk, so even a stronger solve-stage claim would still need skeptical verification before any Lean decision.

## what_verify_should_check
- Recheck the statement lock and the exact dsrg identity `A^2 = 2J + 2I - A`.
- Recheck the spectrum and inverse:
  - `7^1, 1^15, (-2)^11`,
  - `A^-1 = (1/2)A + (1/2)I - J/7`.
- Recheck the shifted reformulation:
  - `B = A + 2I`,
  - `B^2 = 2J + 3B`,
  - `P = (A + 2I)/3 - J/9`,
  - `P^2 = P`,
  - `rank(P) = 15`,
  - `rank(B) = 16`.
- Recheck the one-vertex structure:
  - quotient `[[0,4,3],[1,1,5],[0,2,5]]`,
  - `A^3 = 12J - 2I + 3A`,
  - `90` directed triangles total,
  - the displayed four-parameter `M/O/I/N` block-total family.
- Recheck the abelian Cayley obstruction and the nonnormality obstruction.
- Verify whether the one-vertex bookkeeping can be sharpened to a real contradiction; if not, this should remain a verified `PARTIAL`.

## verify_rediscovery
- PASS 1 used a bounded web audit focused on the exact tuple, complement notation, the canonical Hobart-Brouwer source, and later status checks.
- The canonical Brouwer/Hobart dsrg tables still list `(27,7,4,1,2)` with `?`, and the complement tuple `(27,19,16,13,14)` is likewise not marked as settled.
- A later survey-style source I checked, Jorgić's 2021 paper on directed strongly regular graphs, discusses parameter feasibility and vertex-transitive nonexistence patterns, but I did not find an exact theorem, proposition, example, or corollary settling this specific tuple.
- Within budget, I did not find an exact construction, impossibility theorem, or explicit reduction in the literature that directly settles the intended statement.
- Rediscovery verdict: not established within the bounded audit.

## verify_faithfulness
- The solve record is faithful about its own scope. It locks the intended statement correctly as existence of a dsrg with parameters `(27,7,4,1,2)`.
- The matrix reformulation `A^2 = 2J + 2I - A` is exact for this tuple.
- The solver does not falsely claim to have proved existence or nonexistence. Its actual output is a package of necessary conditions and subclass obstructions.
- So there is no wrong-theorem drift inside the writeup, but the mathematical outcome remains only `PARTIAL` relative to the intended statement.

## verify_proof
- I found no incorrect step in the claimed partial package.
- Rechecked exactly:
  - the nontrivial eigenvalues on the sum-zero subspace satisfy `u^2 + u - 2 = 0`, hence are `1` and `-2`;
  - trace gives multiplicities `1^15` and `(-2)^11`;
  - the inverse formula `A^-1 = (1/2)A + (1/2)I - J/7` is correct;
  - with `B = A + 2I`, one gets `B^2 = 2J + 3B`;
  - `P = (A + 2I)/3 - J/9` is idempotent, has trace `15`, and yields `rank(B) = 16`;
  - `A^3 = 12J - 2I + 3A`, so `trace(A^3) = 270`, giving exactly `90` directed triangles and `10` through each vertex;
  - the abelian Cayley obstruction is valid: nonprincipal character values would have to lie in `{1,-2}`, but Parseval gives an impossible count.
- The one-vertex `M/O/I/N` bookkeeping does not produce a contradiction by itself. The displayed four-parameter family is consistent with the local equations, so the solver was correct not to overclaim.

## verify_adversarial
- There was no candidate witness or counterexample to attack, and no solver checker existed to rerun.
- I ran small independent arithmetic checks in the repo environment for the spectral multiplicities, inverse formula, idempotent computation, quotient-row sanity, and triangle count identities. These checks passed.
- I also stress-tested the `M/O/I/N` total system by reconstructing the linear constraints. The system remains feasible at the bookkeeping level, which supports the solver's conservative conclusion that no full contradiction was obtained.
- Adversarial outcome: the partial algebraic package survives, but it does not imply the intended existence/nonexistence claim.

## verify_verdict
- `VERIFIED`
- Classification stays `PARTIAL`.
- Reason:
  - no rediscovery found within the bounded audit;
  - the recorded partial proofs and obstructions appear correct;
  - the intended statement itself is still not resolved;
  - therefore this is not `CANDIDATE`, not `COUNTEREXAMPLE`, and certainly not `EXACT`.
- `lean_ready = false` because there is no exact intended theorem to formalize yet, only verified necessary conditions and subclass exclusions.

## minimal_repair_if_any
- Tiny repair only: when reading the displayed `M/O/I/N` block-total family, the totals should be interpreted as counting arcs between the four classes only, with arcs involving the distinguished vertex `x` handled separately. This matches the displayed formulas and avoids accidental confusion about row/column totals.
- No mathematical upgrade is justified. The honest status remains a verified `PARTIAL`.
