# bshm-100-36-14-neg4

## statement_lock
- Active slug: `bshm-100-36-14-neg4`
- Title: `Primitive balancedly splittable Hadamard matrix BSHM(100,36,14,-4)`
- Locked intended statement: there exists a nontrivial primitive balancedly splittable Hadamard matrix with parameters `(v,k,lambda,mu) = (100,36,14,-4)`.
- Working exact reformulation used here: there exists a `100 x 100` Hadamard matrix `H` and a choice of `36` rows forming a submatrix `H1` such that the column Gram matrix `B = H1^T H1` has diagonal entries `36` and off-diagonal entries exactly `14` or `-4`.
- This reformulation is the dossier-consistent one: if "selected rows induce two off-diagonal inner products" were read as a row Gram statement, it would contradict Hadamard orthogonality immediately, so the only sensible reading is the standard column-Gram one.

Self-check:
- I am locking the exact existential statement, not a weaker variant.
- If the contradiction below rules out this stronger column-Gram realization, then it also rules out the primitive/nontrivial subcase.

## definitions
- Let `H1` be the `36 x 100` selected-row submatrix.
- Let `B = H1^T H1`. Then `B` is symmetric, positive semidefinite, and has
  - `B_ii = 36` for all `i`,
  - `B_ij in {14, -4}` for all `i != j`.
- Define a graph `A` on the `100` columns by `A_ij = 1` iff `i != j` and `B_ij = 14`. Then
  `B = 36I + 14A - 4(J - I - A) = 40I + 18A - 4J`.
- Because the `36` rows of `H1` are rows of a Hadamard matrix, they are pairwise orthogonal and have squared norm `100`, so
  `H1 H1^T = 100 I_36`.
- Therefore the nonzero eigenvalues of `B = H1^T H1` are all `100`, hence
  `B^2 = 100 B`.
- Also, for any vector `x`, `x^T B x = ||H1 x||^2 >= 0`. In particular,
  `1^T B 1 = ||H1 1||^2 >= 0`.

Self-check:
- Every identity here is standard linear algebra from the Hadamard condition.
- I have not used any hidden regularity assumption on `A`; that will be derived.

## approach_A
Structural / invariant route: use the projector identity `B^2 = 100B` plus positivity of the Gram matrix.

For each column index `i`, let `d_i` be the number of `j != i` with `B_ij = 14`. Then the diagonal entry of `B^2` at `i` is

`(B^2)_{ii} = 36^2 + d_i * 14^2 + (99 - d_i) * (-4)^2`.

Since `B^2 = 100B`, this must equal `100 * B_ii = 3600`. Hence

`1296 + 196 d_i + 16(99 - d_i) = 3600`

so

`2880 + 180 d_i = 3600`,

therefore

`d_i = 4` for every `i`.

Thus every row of `B` has sum

`36 + 4 * 14 + 95 * (-4) = -288`.

So

`1^T B 1 = 100 * (-288) < 0`.

But `1^T B 1 = ||H1 1||^2 >= 0`, contradiction.

Conclusion of Approach A:
- No such Gram matrix `B` exists.
- Therefore no balancedly splittable Hadamard matrix with parameters `(100,36,14,-4)` exists.

Self-check:
- The contradiction is exact and short: diagonal counting gives `d_i = 4`, then positivity is violated.
- The proof does not need primitivity; it disproves the stronger ambient existence statement.

## approach_B
Construction / extremal / contradiction route: continue the graph model and inspect a hypothetical pair of columns.

Assume again that `A` records which pairs have inner product `14`. From Approach A, every vertex has degree `4`.

Take adjacent vertices `i ~ j`, and let `c` be their number of common neighbors in `A`. Count `(B^2)_{ij}` by splitting the summation over `k` into cases:
- `k = i` or `k = j`: contribution `36*14 + 14*36 = 1008`.
- `k` adjacent to both: `c` terms of size `14*14 = 196`.
- `k` adjacent to exactly one of `i,j`: there are `6 - 2c` such indices, each contributing `14*(-4) = -56`.
- `k` adjacent to neither: there are `92 + c` such indices, each contributing `(-4)*(-4) = 16`.

So

`(B^2)_{ij} = 1008 + 196c - 56(6 - 2c) + 16(92 + c) = 2144 + 324c`.

But `B^2 = 100B` and `B_ij = 14`, so `(B^2)_{ij} = 1400`. Hence

`2144 + 324c = 1400`,

which gives

`c = -744 / 324 = -62 / 27`,

impossible.

So even the local common-neighbor arithmetic of a hypothetical realizing graph is inconsistent.

Self-check:
- This second route is not needed for the main disproof, but it independently points the same way.
- The counting cases cover all `k`, so the contradiction is combinatorially complete once degree `4` is known.

## lemma_graph
1. Reformulate the selected rows as a `36 x 100` submatrix `H1` with Gram matrix `B = H1^T H1`.
2. Use Hadamard orthogonality of the selected rows to get `H1 H1^T = 100 I_36`.
3. Deduce `B^2 = 100B` and `x^T B x >= 0` for all `x`.
4. Read the diagonal of `B^2 = 100B` to show each column has exactly four `14`-partners.
5. Sum a row of `B` to get the constant row sum `-288`.
6. Apply `1^T B 1 = ||H1 1||^2 >= 0` and obtain a contradiction.
7. Optional cross-check: the adjacent-pair common-neighbor count becomes negative fractional, so the graph model also breaks locally.

## chosen_plan
- The best path is Approach A. It uses only exact Gram-matrix identities forced by the problem data and ends in a one-line positivity contradiction.
- Approach B is retained only as a cross-check because it exposes a second impossibility once the degree count is known.
- No broader search or computation is justified after Approach A closes the statement directly.

Self-check:
- This is reasoning-first in the strongest sense: the core argument is pure algebra and counting.
- Stopping before any search is deliberate because the existential statement is already contradicted.

## self_checks
- Statement faithfulness check: the only real risk is definitional. Verification should confirm that `(100,36,14,-4)` means exactly the raw off-diagonal values in `H1^T H1`.
- Algebra check: the key numerical identity is `1296 + 196d_i + 16(99 - d_i) = 3600`, giving `d_i = 4`.
- Positivity check: `1^T B 1` is a squared norm, so it cannot be negative under the locked interpretation.
- Scope check: the disproof is stronger than needed because it does not use primitiveness.

## code_used
- Minimal code used: a tiny exact arithmetic sanity check in `node` after the reasoning was already complete.
- The proof itself does not depend on that code; it only rechecked the derived constants `d_i = 4` and row sum `-288`.

## result
- Solve-stage verdict: `COUNTEREXAMPLE`
- Confidence: `high`
- Exact mathematical output from this solve pass:
  - under the standard dossier-consistent BSHM interpretation, the required Gram matrix `B` cannot exist;
  - therefore the intended existential statement `There exists a primitive BSHM(100,36,14,-4)` is false.
- Lean was not run in solve.

## likely_failure_points
- The main residual risk is not the algebra; it is whether the canonical source uses a different normalization or affine transform of the two inner-product values than the dossier text suggests.
- Verification should check that `k = 36` really is the number of selected rows and that `14` and `-4` are the actual off-diagonal entries of `H1^T H1`, not shifted graph parameters.
- If the literature encodes the same tuple through a different sign convention or via the complementary row block, this solve writeup would need to be translated to that convention before the contradiction is judged final.

## what_verify_should_check
- Check source faithfulness first:
  - the definition of balancedly splittable Hadamard matrix used by the canonical source;
  - the exact meaning of the tuple `(100,36,14,-4)`.
- Then check the proof mechanically:
  - `H1 H1^T = 100I_36`;
  - `B = H1^T H1` implies `B^2 = 100B`;
  - the diagonal computation gives `d_i = 4`;
  - `1^T B 1 = ||H1 1||^2` contradicts the row sum `-288`.
- If verification agrees on the interpretation, this is a strong exact disproof candidate and should be considered for Lean formalization.

## verify_rediscovery
- PASS 1 used a bounded web audit focused on the exact tuple, alternative notation, the canonical balancedly splittable Hadamard source, and theorem/proposition checks within that source.
- The rediscovery audit found that the standard source definition matches the solver's interpretation: for a balancedly splittable Hadamard matrix of order `n`, a choice of `ell` rows gives a submatrix `H1` with
  `H1^T H1 = ell I_n + a A + b(J_n - A - I_n)`
  for some `(0,1)`-matrix `A`, so the tuple `(100,36,14,-4)` means exactly `n = 100`, `ell = 36`, and off-diagonal values `14` and `-4` in the column Gram matrix.
- The same literature already gives necessary parameter relations for this setup. Substituting `n = 100`, `ell = 36`, `a = 14`, `b = -4` into those relations does not yield a valid parameter set, so the exact intended instance is already ruled out in the published theory rather than remaining frontier-open.
- Therefore this run is a `REDISCOVERY`: the current argument may still be correct, but it is not a novel solution to an open problem.

## verify_faithfulness
- The solver's key interpretive move was correct. For a Hadamard matrix, the selected rows themselves are mutually orthogonal, so the two-valued condition cannot be about their row Gram matrix; it is about the column Gram matrix `H1^T H1`, exactly as in the source definition.
- Under that source-faithful reading, the claimed output is the exact intended disproof of `There exists a primitive BSHM(100,36,14,-4)`, not a weaker proxy and not a nearby variant.
- The only adjustment from the dossier wording is clarifying "selected rows induce two off-diagonal inner products" into the standard column-Gram formulation. That is a definition repair, not theorem drift.

## verify_proof
- No incorrect step was found in the solver's main contradiction once the standard definition is fixed.
- `H1 H1^T = 100 I_36` is immediate because the chosen `36` rows come from a Hadamard matrix of order `100`.
- Hence `B = H1^T H1` satisfies `B^2 = H1^T(H1 H1^T)H1 = 100B`.
- Writing `d_i` for the number of `14` entries in row `i` of `B`, the diagonal identity
  `36^2 + 196 d_i + 16(99 - d_i) = 100 * 36`
  gives `d_i = 4` for every `i`.
- Then every row sum is `36 + 4*14 + 95*(-4) = -288`, so `B1 = -288 1` and therefore
  `1^T B 1 = -28800 < 0`, contradicting positive semidefiniteness of `B = H1^T H1`.
- The optional common-neighbor count is unnecessary, but it is consistent with the main contradiction rather than exposing a flaw in it.

## verify_adversarial
- There was no stored checker file to rerun, so the adversarial pass reran the arithmetic directly in `node`.
- The exact sanity checks reproduced the decisive numbers: `d = 4`, row sum `-288`, and therefore `1^T B 1 = -28800`.
- Perturbation checks around the degree equation confirmed that `d = 4` is the unique integer value satisfying the diagonal identity: `d = 3` gives `3420`, `d = 4` gives `3600`, and `d = 5` gives `3780`, while the target is `3600`.
- No candidate construction exists in the artifact to attack further. The mathematical claim already breaks at the level of the required Gram matrix.

## verify_verdict
- `REDISCOVERY`

## minimal_repair_if_any
- No repair to the proof is needed.
- The conservative repair is to the harness classification only: this artifact must not proceed as `EXACT` or `CANDIDATE` because the exact instance is already settled by existing literature.
