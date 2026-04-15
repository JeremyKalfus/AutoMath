# Solve Record: bshm-120-12-12-0

## statement_lock
- Locked slug: `bshm-120-12-12-0`.
- Locked title: `The Parameter Set (120,12,12,0) for Balanced Splittable Hadamard Matrices`.
- Locked intended statement: determine whether there exists a balanced splittable Hadamard matrix with parameters `BSHM(120,12,12,0)`.
- Source-faithful interpretation: there should exist a Hadamard matrix `H` of order `120` and a choice of `12` rows forming a submatrix `H1` such that
  `H1^T H1 = 12 I_120 + 12 A`
  for some `(0,1)`-matrix `A`. Equivalently, the off-diagonal column inner products in `H1` are exactly `12` or `0`.
- If the main claim closed exactly, the title theorem would simply be:
  `Existence` or `nonexistence` of `BSHM(120,12,12,0)`.
- A successful exact solve here would already be about `79%` of a micro-paper. The remaining packaging work would mainly be a short family recap around Theorem 65 / Corollary 67, plus a cleaned certificate or obstruction.

## definitions
- Let `H` be a Hadamard matrix of order `120`, and let `H1` be the selected `12 x 120` row submatrix.
- Because the chosen rows come from a Hadamard matrix, `H1 H1^T = 120 I_12`.
- Set `B := H1^T H1`. In this instance, `B = 12(I + A)`.
- Since the columns of `H1` are `12`-vectors with `+/-1` entries:
  - `B_{ij} = 12` means columns `i` and `j` of `H1` are identical.
  - `B_{ij} = 0` means those two columns are orthogonal in `R^12`.
  - `B_{ij} = -12` cannot occur in this parameter set.
- The complementary `108 x 120` row submatrix is denoted `H2`.
- Conventions used below are only the standard balanced splittable setup encoded in the active packet.

## approach_A
- Structural / invariant route.
- Start from
  `B^2 = H1^T (H1 H1^T) H1 = 120 B`.
- Substituting `B = 12(I + A)` gives
  `A^2 = 8A + 9I`.
- Consequences:
  - diagonal entries give `deg_A(v) = 9` for every vertex;
  - if `A_{ij} = 1`, then vertices `i,j` have exactly `8` common neighbors;
  - if `A_{ij} = 0`, then vertices `i,j` have `0` common neighbors.
- Hence each connected component is a clique of size `10`, and there are `120 / 10 = 12` components.
- Therefore the column graph of `H1` is forced to be
  `12 K_10`.
- Once the columns are grouped by these cliques, the `12` distinct column types are pairwise orthogonal `+/-1` vectors in `R^12`, so they form a Hadamard basis of order `12`.
- After a column permutation,
  `H1 = V ⊗ 1_10^T`
  for some Hadamard matrix `V` of order `12`.
- Immediate consequence for the remaining rows: every row of `H2` is orthogonal to every row of `H1`, so every row of `H2` has block sum `0` on each of the `12` ten-column blocks. Since entries are `+/-1`, each block must contain exactly five `+1` and five `-1`.
- Self-check: every step above uses only `H1 H1^T = 120 I_12`, the source-faithful form of `B`, and elementary matrix algebra.

## approach_B
- Construction / extremal / contradiction route.
- Try to extend the forced top block
  `H1 = V ⊗ 1_10^T`
  to a full Hadamard matrix by analyzing `H2`.
- Since `H^T H = 120 I`, we get
  `H2^T H2 = 120 I - H1^T H1 = 108 I - 12 A`.
- Under the clique decomposition from Approach A, this becomes block diagonal with `12` copies of
  `120 I_10 - 12 J_10`.
- So within each ten-column block:
  - each column has norm `108` in `H2`;
  - distinct columns have inner product `-12`;
  - the ten columns sum to `0`;
  - the block contributes rank `9`.
- This is the Gram matrix of a regular simplex in a `9`-dimensional subspace, and the `12` blocks occupy mutually orthogonal `9`-dimensional subspaces of `R^108`.
- The obvious tensor lift would ask for a `9 x 10` zero-sum `+/-1` block whose rows are pairwise orthogonal. That cannot happen: any two zero-sum length-`10` `+/-1` vectors have inner product in
  `{-10,-6,-2,2,6,10}`,
  never `0`.
- This kills the simplest blockwise product construction.
- It does not prove nonexistence, because full-row orthogonality in `H2` can still arise by cancellation across different ten-column blocks.
- Self-check: this route gives a real obstruction to the easiest extension mechanism, but not a full contradiction.

## lemma_graph
- Lemma 1: `B = H1^T H1 = 12(I + A)` and `B^2 = 120 B`.
- Lemma 2: `A^2 = 8A + 9I`.
- Lemma 3: `A` is `9`-regular, adjacent pairs have `8` common neighbors, and nonadjacent pairs have `0` common neighbors.
- Lemma 4: every component of `A` is `K_10`; hence `A = 12 K_10`.
- Lemma 5: after column permutation, `H1 = V ⊗ 1_10^T` for some order-`12` Hadamard matrix `V`.
- Lemma 6: each row of `H2` has exactly five `+1` and five `-1` in each ten-column block.
- Lemma 7: `H2^T H2` is block diagonal with `12` copies of `120 I_10 - 12 J_10`.
- Open gap: convert Lemmas 5-7 either into an actual extension or into an impossibility theorem.

## chosen_plan
- Best path chosen: lock the invariant reduction first, because it is exact, short, and theorem-facing.
- I then tested the most natural constructive lift from the forced block structure. The local orthogonal block lift fails immediately.
- I did not move to search or optimization because:
  - the dossier marks the target as not search-heavy;
  - the structural reduction already yields a real theorem slice;
  - I do not yet have a sharply justified finite search space that would respect the minimal-code rule.
- Conservative conclusion: preserve the exact `12 K_10` reduction and the failed local-lift obstruction, then stop before speculative computation.
- Self-check: this stays inside the one-shot lane and does not drift into unjustified brute force.

## self_checks
- Statement-faithfulness check: the solve uses the column-Gram interpretation `H1^T H1 = lI + aA + b(J-A-I)` with `l=a=12`, `b=0`.
- Algebra check: `B^2 = 120 B` follows immediately from `H1 H1^T = 120 I_12`.
- Graph check: `A^2 = 8A + 9I` really does force degree `9`, adjacent common-neighbor count `8`, and nonadjacent common-neighbor count `0`.
- Clique check: these graph parameters force disjoint `K_10` components; there is no other connected pattern.
- Span check: the `12` distinct column representatives are pairwise orthogonal nonzero vectors in `R^12`, hence an order-`12` Hadamard basis.
- Complement check: orthogonality to `H1` is equivalent to zero block sum on each ten-column block, so every complementary row has a `5+/5-` split in every block.
- Conservatism check: no existence or nonexistence verdict is claimed beyond what the lemmas certify.

## code_used
- No code used.
- Reasoning was strong enough to isolate the block model, but not strong enough to justify a bounded exact search.

## result
- Strong partial result, no exact settle.
- Proven conditional structure:
  - any `BSHM(120,12,12,0)` forces the selected `12` rows to collapse the `120` columns into `12` classes of size `10`;
  - after column permutation, the selected submatrix must be `H_12 ⊗ 1_10^T`;
  - every remaining row must be a concatenation of `12` zero-sum ten-vectors, i.e. each block is exactly a `5+/5-` pattern.
- I also obtained a negative local construction result: the obvious blockwise tensor lift fails because zero-sum `+/-1` ten-vectors are never mutually orthogonal.
- This is not an existence proof, not a contradiction, and therefore not yet a paper-ready closure.
- Immediate remark falling out of the argument: the unresolved difficulty lies entirely in the complementary `108` rows; the selected `12` rows are already rigid once the parameter tuple is fixed.
- Self-check: this is genuinely theorem-facing, but it is still only a reduction package.

## family_affinity
- Very high family affinity.
- The same calculation works for the whole Type 2 family `BSHM(8rs,4s,4s,0)`.
- In general, writing `B = 4s(I + A)` and using `B^2 = 8rs B` yields
  `A^2 = 2(r-1)A + (2r-1)I`,
  so `A` must be a disjoint union of `4s` cliques `K_{2r}`.
- For the present instance `r = 5`, `s = 3`, this specializes to `12 K_10`.

## generalization_signal
- Strong theorem-slice signal.
- Suggested general lemma:
  `If BSHM(8rs,4s,4s,0) exists, then after a column permutation the selected 4s-row submatrix is H_(4s) ⊗ 1_(2r)^T for some Hadamard matrix H_(4s), and every complementary row has zero sum on each of the 4s blocks of size 2r.`
- What part of the argument scales:
  - the `B^2 = nB` calculation;
  - the clique decomposition of the column graph;
  - the tensor-shaped normal form for `H1`;
  - the block-zero-sum constraint on complementary rows.
- What part does not yet scale:
  - converting the block model into an explicit extension;
  - forcing a contradiction from the complementary-row constraints alone.

## proof_template_reuse
- Reusable template:
  1. write `B = H1^T H1`;
  2. use `B^2 = nB`;
  3. translate the quadratic identity into degree and common-neighbor counts for the column graph;
  4. identify the forced graph as a union of equal cliques;
  5. pass from clique structure to a tensor-shaped form for `H1`;
  6. deduce rigid block-sum conditions on `H2`.
- This should transfer directly to nearby odd-odd Type 2 cases with the same `b = 0` pattern.

## candidate_theorem_slice
- Candidate theorem slice:
  `Any BSHM(120,12,12,0), if it exists, is column-permutation equivalent on the selected 12-row submatrix to H_12 ⊗ 1_10^T; equivalently, the associated column graph is exactly 12 K_10 and every complementary row has a 5+/5- split on each ten-column block.`
- This is a real theorem slice with immediate structural content.
- It is still below the strict micro-paper threshold because the title statement itself remains open.

## smallest_param_shift_to_test
- First parameter shift to test: `(72,12,12,0)` with `r = s = 3`.
- Second parameter shift to test: `(168,12,12,0)` with `r = 7`, `s = 3`.
- Reason: the same reduction gives `12 K_6` in the first case and `12 K_14` in the second, so these are the cleanest neighbors for checking whether the complementary-row obstruction depends mainly on the block width `2r`.

## why_this_is_or_is_not_publishable
- Not publishable yet as a stand-alone micro-paper result.
- Why not:
  - there is no exact existence verdict;
  - there is no impossibility theorem;
  - the current output is a sharp reduction, not a closed title theorem.
- If the main claim were closed, the package would still be about `70-90%` of a paper, because the frontier hook is already in place and the remaining packaging would be light.
- In its current state, the result is still too thin for the micro-paper lane, though it is genuinely theorem-facing and worth preserving.

## paper_shape_support
- What extra structure would make this paper-shaped if the main claim closes?
  - one exact extension theorem converting the `12 K_10` reduction into an explicit order-`120` construction; or
  - one exact obstruction showing that no orthogonal `108`-row `5+/5-` block basis can exist.
- Minimal remaining packaging work after an exact closure:
  - restate the Type 2 family frontier from the source;
  - include the forced `12 K_10` lemma as the first structural proposition;
  - add the exact certificate or contradiction;
  - record the immediate family consequence that the first `r = 5`, `s = 3` case is settled.
- One natural remark already available: any solution must be a ten-fold lift over an order-`12` Hadamard skeleton, so the odd-odd difficulty lives entirely in the complementary `108` rows.

## boundary_remark
- Boundary remark:
  this instance is not arbitrary order-`120` noise. The parameter tuple forces the selected rows into a rigid ten-fold replication of an order-`12` Hadamard basis, and the only remaining flexibility is how to realize the `108` orthogonal complementary rows with `5+/5-` support on each ten-column block.
- This sharply isolates where the residual odd-odd barrier sits.

## likely_failure_points
- The current reduction may still be too weak to force nonexistence; cancellation across many ten-column blocks could support an exotic extension.
- The local tensor obstruction rules out only the most naive blockwise construction, not all global constructions.
- The family-level theorem slice may already be implicit in the published source, so verification should treat its novelty conservatively even though it is useful locally.
- If a later solve uses computation, it should justify a sharply bounded search space from the `12 K_10` block model rather than jumping to generic SAT or brute force.

## what_verify_should_check
- Check the definition-faithfulness of `B = H1^T H1 = 12(I + A)`.
- Recheck the algebra `B^2 = 120 B` and the derived identity `A^2 = 8A + 9I`.
- Recheck that these graph parameters force `A = 12 K_10`.
- Recheck the claim that the `12` distinct column representatives form an order-`12` Hadamard basis.
- Recheck the complementary-row consequence: orthogonality to all rows of `H1` is equivalent to block sum `0` on each ten-column block.
- Novelty check should ask whether the general family lemma `A = 4s K_{2r}` is already explicit in the source or only implicit there.
