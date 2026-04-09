# dsrg-28-6-3-2-1

## statement_lock
- Active slug: `dsrg-28-6-3-2-1`
- Title: `Does a directed strongly regular graph with parameters (28,6,3,2,1) exist?`
- Locked intended statement: determine whether there exists a directed strongly regular graph with parameters `(v,k,t,lambda,mu) = (28,6,3,2,1)`.
- Exact matrix reformulation used here: there exists a `28 x 28` `0/1` matrix `A` such that
  - `A_ii = 0` for all `i`,
  - every row sum and every column sum is `6`,
  - `A^2 = tI + lambda A + mu(J - I - A) = 3I + 2A + (J - I - A) = J + A + 2I`.
- So for every ordered pair of distinct vertices `(x,y)`, the number of directed `2`-paths `x -> z -> y` is `2` when `x -> y` and `1` otherwise, while `(A^2)_{xx} = 3` for every vertex `x`.

Self-check:
- The target stayed exact throughout: existence of the dsrg itself, not a nearby tuple and not only a Cayley or normal realization.
- The identity `A^2 = J + A + 2I` is the correct specialization of the dsrg axioms for `(28,6,3,2,1)`.

## definitions
- `J` is the all-ones matrix and `j` is the all-ones column vector.
- `N^+(x)` is the out-neighborhood of `x`, and `N^-(x)` is the in-neighborhood of `x`.
- Since `t = 3`, every vertex has exactly `3` mutual neighbors:
  `|N^+(x) cap N^-(x)| = 3`.
- Relative to a fixed vertex `x`, I use the standard four-way partition
  - `M(x) = N^+(x) cap N^-(x)` with size `3`,
  - `O(x) = N^+(x) \ N^-(x)` with size `3`,
  - `I(x) = N^-(x) \ N^+(x)` with size `3`,
  - `N(x) = V \ ({x} union N^+(x) union N^-(x))` with size `18`.
- I also use
  - `P(x) = N^+(x) = M(x) union O(x)`,
  - `Q(x) = N^-(x) = M(x) union I(x)`,
  - `B = A + I`.

Ambiguities / conventions:
- The solve pass assumes the standard loopless dsrg convention from the dossier and does not add symmetry, normality, vertex-transitivity, or a Cayley hypothesis unless stated explicitly.
- All spectral statements are over `R`; since the relevant polynomials have distinct roots, diagonalizability claims here are safe.

Self-check:
- The local class sizes are forced by the tuple and sum to `27` as they should.
- The shifted matrix `B = A + I` is just a bookkeeping change; no assumption is hidden in it.

## approach_A
- Structural / invariant route: push the rigid quadratic identity `A^2 = J + A + 2I` as far as possible before trying any search.

Major step 1: forced spectrum and explicit inverse.
- Because `Aj = 6j` and `Jx = 0` for every `x` with `j^T x = 0`, the quadratic identity gives
  `A^2 x = A x + 2x` on the `27`-dimensional sum-zero subspace.
- Therefore every eigenvalue on that subspace is a root of `u^2 - u - 2 = 0`, so it is either `2` or `-1`.
- Let the multiplicities be `m_2` and `m_-1`. Then
  - `m_2 + m_-1 = 27`,
  - `trace(A) = 0 = 6 + 2 m_2 - m_-1`.
- Solving gives
  - eigenvalue `6` with multiplicity `1`,
  - eigenvalue `2` with multiplicity `7`,
  - eigenvalue `-1` with multiplicity `20`.
- Since `0` is not an eigenvalue, `A` is invertible. Writing `A^-1 = alpha A + beta I + gamma J` and using `A^2 = J + A + 2I` and `AJ = 6J` gives
  `A^-1 = (1/2)A - (1/2)I - (1/12)J`.

Self-check:
- The multiplicity equations are exact, and `6 + 2*7 - 20 = 0` checks the trace.
- On eigenvalues, the inverse formula gives `1/6`, `1/2`, and `-1`, exactly as required.

Major step 2: shifted rank-`8` reformulation.
- Set `B := A + I`. Then
  `B^2 = A^2 + 2A + I = J + 3A + 3I = J + 3B`.
- Define
  `Q := (1/3)B - (1/12)J`.
- A direct expansion using `B^2 = J + 3B`, `BJ = JB = 7J`, and `J^2 = 28J` gives `Q^2 = Q`.
- The diagonal entries of `Q` are all `1/4`, so
  `trace(Q) = 28 * (1/4) = 7`.
- Hence `Q` is an idempotent of rank `7`, and therefore `B = 3Q + (1/4)J` has rank `8`.
- Equivalently, `B` has spectrum `7^1, 3^7, 0^20`.

Self-check:
- The shift is internally consistent: adding `I` moves the eigenvalues from `6,2,-1` to `7,3,0`.
- The rank claim follows from the trace of an idempotent, not from any symmetry assumption.

Major step 3: exact three-cell quotient around one vertex.
- Fix a vertex `x` and partition `V` as `({x}, Q(x), R(x))`, where `Q(x) = N^-(x)` has size `6` and `R(x) = V \ ({x} union Q(x))` has size `21`.
- The outgoing counts into these three cells are forced:
  - from `x`: `(0,3,3)`, because `x` sends arcs to the `3` mutual neighbors and the `3` out-only neighbors;
  - from any `y in Q(x)`: `(1,2,3)`, because `y -> x`, and the number of out-neighbors of `y` inside `Q(x)` is exactly the number of directed `2`-paths from `y` to `x`, namely `lambda = 2`;
  - from any `y in R(x)`: `(0,1,5)`, because `y` does not point to `x`, and the number of out-neighbors of `y` inside `Q(x)` is exactly the number of directed `2`-paths from `y` to `x`, namely `mu = 1`.
- So the quotient matrix is exactly
  `[[0,3,3],[1,2,3],[0,1,5]]`.
- This quotient itself already has eigenvalues `6,2,-1`, matching the global spectrum.

Self-check:
- The only nontrivial point is the count into `Q(x)`, and that is exactly the dsrg `2`-path axiom specialized to the target vertex `x`.
- The row sums of the quotient are all `6`, as they must be.

Major step 4: triangle count and local triangle incidence.
- Multiplying once more gives
  `A^3 = A(J + A + 2I) = 6J + A^2 + 2A = 7J + 3A + 2I`.
- Therefore
  `trace(A^3) = 7 * 28 + 2 * 28 = 252`.
- In a loopless digraph, each directed `3`-cycle contributes exactly `3` to `trace(A^3)`, so the total number of directed triangles is exactly
  `252 / 3 = 84`.
- A local version around a fixed vertex `x` says:
  - each mutual out-arc `x -> y` with `y in M(x)` lies in exactly `2` directed triangles, because `y -> x`;
  - each one-way out-arc `x -> y` with `y in O(x)` lies in exactly `1` directed triangle, because `y` does not point to `x`.
- Hence each vertex lies in exactly
  `3 * 2 + 3 * 1 = 9`
  directed triangles, consistent with the global count `84 * 3 / 28 = 9`.

Self-check:
- The formula for `A^3` follows mechanically from the quadratic identity.
- The local and global triangle counts agree, so there is no counting slip there.

Major step 5: exact `P(x) -> Q(x)` incidence totals.
- Keep the same fixed vertex `x`, with `P(x) = M(x) union O(x)` and `Q(x) = M(x) union I(x)`.
- For each `y in Q(x)`, the number of in-neighbors of `y` coming from `P(x)` is the number of directed `2`-paths from `x` to `y`.
- Therefore:
  - each `y in M(x)` receives exactly `2` arcs from `P(x)`,
  - each `y in I(x)` receives exactly `1` arc from `P(x)`.
- Dually, for each `z in P(x)`, the number of out-neighbors of `z` inside `Q(x)` is the number of directed `2`-paths from `z` to `x`.
- Therefore:
  - each `z in M(x)` sends exactly `2` arcs into `Q(x)`,
  - each `z in O(x)` sends exactly `1` arc into `Q(x)`.
- So the bipartite incidence from `P(x)` to `Q(x)` has `9` edges total and both row and column degree multiset equal to `(2,2,2,1,1,1)`.
- In block-total language, if `e_CD` denotes the number of arcs from cell `C` to cell `D` for `C,D in {M,O,I,N}`, then the dsrg identities force
  - from `P(x)` into `(M,O,I,N)`: `(6,6,3,18)`,
  - from `(M,O,I,N)` into `Q(x)`: `(6,3,6,18)`.
- These totals are strong but still parametrically consistent; they did not close to a contradiction in this pass.

Self-check:
- The `9`-edge total is consistent from both sides:
  `3*2 + 3*1 = 3*2 + 3*1 = 9`.
- I stopped short of assuming the full five-cell partition is equitable; that would have been an unjustified extra hypothesis.

Major step 6: any realization must be strongly nonnormal.
- Every row of `A` has exactly `6` ones, so
  `trace(AA^T) = 28 * 6 = 168`.
- The sum of squared eigenvalue moduli is
  `6^2 + 7 * 2^2 + 20 * 1^2 = 36 + 28 + 20 = 84`.
- If `A` were normal, these two quantities would agree.
- Since `168 != 84`, any realization must be highly nonnormal.

Self-check:
- This does not prove nonexistence.
- It does exactly rule out the entire normal-matrix regime.

## approach_B
- Construction / extremal / contradiction route: test the most obvious algebraic construction class and see whether the tuple survives it.

Major step 1: abelian Cayley obstruction.
- Suppose the digraph were a Cayley digraph on an abelian group `G` of order `28`, with connection set `D subset G`, `|D| = 6`, and identity `e notin D`.
- The dsrg matrix identity becomes the group-ring identity
  `D^2 = G + D + 2e`.
- For any nonprincipal character `chi`, applying `chi` gives
  `chi(D)^2 = chi(G) + chi(D) + 2 chi(e) = chi(D) + 2`.
- So every nonprincipal character value `chi(D)` must be a root of
  `u^2 - u - 2 = 0`, hence `chi(D) in {2, -1}`.
- Parseval for subsets of a finite abelian group gives
  `sum_chi |chi(D)|^2 = |G| * |D| = 28 * 6 = 168`.
- The principal character contributes `|D|^2 = 36`.
- If `a` of the `27` nonprincipal characters had value `2` and the remaining `27-a` had value `-1`, Parseval would read
  `36 + 4a + (27 - a) = 168`,
  so `3a = 105`, impossible.
- Therefore no abelian Cayley realization exists.

Self-check:
- The contradiction is exact and arithmetic, not heuristic.
- Its scope is narrower than the full problem: it rules out abelian Cayley models only.

Major step 2: attempted closure from the rank-`7` projection model.
- The reformulation `Q = (1/3)(A + I) - (1/12)J`, `Q^2 = Q`, puts the problem into a very tight rank-`7` two-level matrix setting:
  - diagonal entries are `1/4`,
  - off-diagonal entries are `1/4` on arcs and `-1/12` off arcs.
- This is suggestive of a rigid incidence geometry, but I could not turn it into a global contradiction without an additional exact handle on row-row or column-column intersections.
- In particular, the one-vertex quotient and the `P(x) -> Q(x)` degree pattern are compatible with the projection reformulation rather than contradicting it.

Self-check:
- This route sharpened the structure but did not prove impossibility.
- I am not claiming that the projection model is realizable; only that I did not close a contradiction from it.

## lemma_graph
1. Lock the problem as a `28 x 28` zero-diagonal `0/1` matrix with row and column sums `6` and `A^2 = J + A + 2I`.
2. Restrict to the sum-zero subspace to force the nontrivial eigenvalues to be `2` and `-1`.
3. Use trace to get the exact spectrum `6^1, 2^7, (-1)^20` and derive the inverse formula `A^-1 = (1/2)A - (1/2)I - (1/12)J`.
4. Shift to `B = A + I`, derive `B^2 = J + 3B`, and package this as a rank-`7` idempotent `Q = B/3 - J/12`, so `rank(B) = 8`.
5. Fix a vertex `x` and use `Q(x) = N^-(x)` to derive the exact three-cell quotient `[[0,3,3],[1,2,3],[0,1,5]]`.
6. Compute `A^3 = 7J + 3A + 2I`, hence exactly `84` directed triangles and exactly `9` through each vertex.
7. Refine around `x` to the `M/O/I/N` partition and record the exact `P(x) -> Q(x)` degree pattern `(2,2,2,1,1,1)` on both sides.
8. Record the exact nonnormality obstruction `trace(AA^T) = 168` versus squared-eigenvalue total `84`.
9. Test the abelian Cayley route and rule it out exactly by character-sum arithmetic.

## chosen_plan
- The best path was the invariant route, because the dossier already pointed to adjacency-matrix and one-vertex counting arguments and the quadratic identity is unusually rigid at this size.
- I pushed that route first until it produced an exact spectrum, an explicit inverse, a rank-`8` shifted matrix, an exact three-cell quotient, and exact triangle counts.
- After that, the most targeted construction check was the abelian Cayley route. It is the cleanest algebraic family to test here, and it fails exactly.

Attempted rigorous closure:
- I tried to turn the one-vertex `M/O/I/N` bookkeeping into a contradiction.
- What does close exactly is the transport from `P(x)` into `Q(x)` and the three-cell quotient from `Q(x) = N^-(x)`.
- What does not close, at least in this pass, is a global impossibility theorem for arbitrary nonnormal, non-Cayley realizations.
- So the strongest honest solve-stage outcome is still a structural `PARTIAL`, not a proof or disproof.

Self-check:
- I am stopping because the unconditional contradictions I could prove are class-level, not whole-instance.
- No code failure caused the stop, because no code was needed.

## self_checks
- Statement fidelity:
  - the exact tuple `(28,6,3,2,1)` stayed locked throughout;
  - the matrix identity `A^2 = J + A + 2I` was used consistently.
- Structural algebra:
  - spectrum `6^1, 2^7, (-1)^20` is correct;
  - inverse formula `A^-1 = (1/2)A - (1/2)I - (1/12)J` is correct;
  - `B = A + I` satisfies `B^2 = J + 3B`;
  - `Q = B/3 - J/12` is idempotent of rank `7`, hence `rank(B) = 8`.
- Local structure:
  - the exact quotient on `({x}, N^-(x), V \ ({x} union N^-(x)))` is `[[0,3,3],[1,2,3],[0,1,5]]`;
  - the `P(x) -> Q(x)` incidence has `9` edges and degree multiset `(2,2,2,1,1,1)` on both sides.
- Triangle structure:
  - there are exactly `84` directed triangles;
  - each vertex lies in exactly `9` directed triangles;
  - mutual out-arcs lie in `2` triangles and one-way out-arcs lie in `1`.
- Obstructions:
  - any realization must be nonnormal;
  - no abelian Cayley realization exists.
- Final honesty check:
  - I did not construct a witness;
  - I did not prove global nonexistence;
  - therefore the classification must stay below `CANDIDATE` and below `COUNTEREXAMPLE`.

## code_used
- No code used.
- Reason: the handwritten algebraic package was already strong and exact, and I did not reach a point where a bounded experiment was clearly justified under the harness rules.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact output from this pass:
  - `A^2 = J + A + 2I`;
  - forced spectrum `6^1, 2^7, (-1)^20`;
  - explicit inverse `A^-1 = (1/2)A - (1/2)I - (1/12)J`;
  - shifted form `B = A + I` with `B^2 = J + 3B` and `rank(B) = 8`;
  - exact quotient `[[0,3,3],[1,2,3],[0,1,5]]` for `({x}, N^-(x), V \ ({x} union N^-(x)))`;
  - exactly `84` directed triangles, hence `9` through each vertex;
  - exact local `P(x) -> Q(x)` degree pattern `(2,2,2,1,1,1)`;
  - exact nonnormality requirement;
  - exact nonexistence of abelian Cayley realizations.
- I did not prove that no dsrg with these parameters exists, and I did not produce a construction.
- Lean should stay off.

## likely_failure_points
- The main gap is global: the one-vertex constraints are sharp but still leave room for a hypothetical nonnormal, non-Cayley realization.
- I did not prove that the full five-cell partition `({x}, M, O, I, N)` is equitable; assuming that would overreach.
- The projection reformulation is suggestive, but without an exact row-row intersection law it remains only a structural lens.
- The dossier carries nontrivial rediscovery risk, so even a stronger solve-stage claim would still need skeptical verification before any Lean decision.

## what_verify_should_check
- Recheck the statement lock and the exact dsrg identity `A^2 = J + A + 2I`.
- Recheck the spectrum and inverse:
  - `6^1, 2^7, (-1)^20`,
  - `A^-1 = (1/2)A - (1/2)I - (1/12)J`.
- Recheck the shifted reformulation:
  - `B = A + I`,
  - `B^2 = J + 3B`,
  - `Q = B/3 - J/12`,
  - `Q^2 = Q`,
  - `rank(B) = 8`.
- Recheck the one-vertex quotient
  `[[0,3,3],[1,2,3],[0,1,5]]`
  on the partition `({x}, N^-(x), V \ ({x} union N^-(x)))`.
- Recheck the triangle package:
  - `A^3 = 7J + 3A + 2I`,
  - exactly `84` directed triangles,
  - exactly `9` through each vertex.
- Recheck the `P(x) -> Q(x)` incidence claim and the block totals `(6,6,3,18)` and `(6,3,6,18)`.
- Recheck the nonnormality argument `trace(AA^T) = 168` versus squared-eigenvalue sum `84`.
- Recheck the abelian Cayley contradiction carefully:
  - group-ring identity `D^2 = G + D + 2e`,
  - nonprincipal character values in `{2,-1}`,
  - Parseval equation `36 + 4a + (27-a) = 168`,
  - impossibility of `a = 35`.

## verify_rediscovery
- PASS 1 used a bounded web audit only. I checked:
  - the exact tuple `(28,6,3,2,1)`,
  - the alternate notation `dsrg(28,6,3,2,1)`,
  - the canonical Hobart-Brouwer table,
  - nearby source pages for built-in construction / nonexistence tags,
  - a later feasibility-paper search.
- Result: I did not find a paper or source explicitly constructing a dsrg with parameters `(28,6,3,2,1)`, proving that no such dsrg exists, or giving a theorem/corollary/example that directly settles this exact tuple.
- The strongest rediscovery evidence is still the canonical table itself, which continues to list `(28,6,3,2,1)` and its complement row `(28,21,18,15,18)` with `?`, not with a construction tag or an `N*` nonexistence tag.
- I also found later dsrg literature and survey-style pages, but within budget none of them surfaced this exact tuple as solved. In particular, the 2017 Hobart-Williford feasibility paper appeared relevant at the topic level, but the bounded pass did not expose a same-instance theorem for `(28,6,3,2,1)`.
- Rediscovery verdict for PASS 1: not established.
- Sources used in PASS 1:
  - https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html
  - https://homepages.cwi.nl/~aeb/math/dsrg/dsrg-5.html
  - https://homepages.cwi.nl/~aeb/math/dsrg/dsrg-1.html
  - https://www.combinatorics.org/ojs/index.php/eljc/article/view/v24i1p16
- Note on the current proof: since the solve-stage output only claimed a structural `PARTIAL` package, not a full solve, there is no positive exact proof here to classify as rediscovered.

## verify_faithfulness
- The solve-stage writeup stayed faithful to the intended statement.
- It never claimed existence or nonexistence of a dsrg with parameters `(28,6,3,2,1)`.
- The actual deliverable was a list of exact consequences of the dsrg axioms, together with one class-level obstruction (`no abelian Cayley realization`).
- I found no wrong-theorem drift, quantifier drift, or change of definitions. The matrix identity `A^2 = J + A + 2I` is the correct specialization of the dsrg definition for `(v,k,t,lambda,mu) = (28,6,3,2,1)`.
- Because the claimed outcome remained `PARTIAL`, the classification should not be upgraded to `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.

## verify_proof
- First incorrect step found: none in the claimed `PARTIAL` package.
- I rechecked the main algebraic steps:
  - on the sum-zero subspace, `A^2 = A + 2I`, so the nontrivial eigenvalues are indeed `2` and `-1`;
  - using `trace(A)=0` gives multiplicities `7` and `20`, hence spectrum `6^1, 2^7, (-1)^20`;
  - solving `A(alpha A + beta I + gamma J) = I` with `A^2 = J + A + 2I` and `AJ = 6J` gives `A^-1 = (1/2)A - (1/2)I - (1/12)J`;
  - with `B = A + I`, one gets `B^2 = J + 3B`, and then `Q = B/3 - J/12` satisfies `Q^2 = Q`;
  - since `diag(Q) = 1/4`, `trace(Q)=7`, so `rank(Q)=7` and `rank(B)=8`;
  - the claimed three-cell quotient `[[0,3,3],[1,2,3],[0,1,5]]` is justified directly from the dsrg two-path axioms and has eigenvalues `6,2,-1`;
  - `A^3 = A(J + A + 2I) = 7J + 3A + 2I`, so `trace(A^3)=252` and therefore the number of directed triangles is `84`;
  - the nonnormality check is valid because `trace(AA^T)=28*6=168`, while the sum of squared eigenvalue moduli is `36 + 7*4 + 20 = 84`, so equality required by normality fails;
  - the abelian Cayley obstruction is valid: the character equation forces nonprincipal values in `{2,-1}`, and Parseval gives `36 + 4a + (27-a) = 168`, hence `a=35`, impossible.
- None of these steps proves global nonexistence, but that is a limitation already stated in the record, not a proof error.

## verify_adversarial
- There was no solver code or checker to rerun.
- I did rerun small arithmetic spot-checks in the repository environment to challenge the handwritten derivations:
  - multiplicity/trace arithmetic for `6^1,2^7,(-1)^20`,
  - inverse-coefficient equations for `A^-1`,
  - the idempotent coefficients for `Q^2 = Q`,
  - quotient-matrix trace/determinant checks against eigenvalues `6,2,-1`,
  - triangle and nonnormality arithmetic,
  - the final Parseval contradiction `a = 35`.
- Those spot checks supported the written algebra and did not expose a hidden sign mistake or arithmetic mismatch.
- Adversarial conclusion: the structural package appears internally correct, but it still falls short of the actual existence decision, so it cannot justify Lean.

## verify_verdict
- `VERIFIED`
- Meaning here: the solve-stage record appears mathematically correct as a `PARTIAL` package, and no rediscovery was established within the bounded audit.
- This is not a verification that the open problem has been solved. The verified content is only the structural algebra recorded in the solve stage.
- Classification after verification should remain `PARTIAL`.
- `lean_ready = false` because there is still no exact intended theorem or exact intended disproof to formalize.

## minimal_repair_if_any
- No repair was needed.
- The only conservative clarification is procedural: the verified output should continue to be labeled `PARTIAL`, not `CANDIDATE` and not `EXACT`, because the argument never reaches existence or nonexistence of the target dsrg.
