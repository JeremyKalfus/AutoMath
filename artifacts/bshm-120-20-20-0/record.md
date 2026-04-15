# Solve Record: bshm-120-20-20-0

## statement_lock
- Locked slug: `bshm-120-20-20-0`.
- Locked title: `The First Open s = 5 Case for BSHM(8rs,4s,4s,0)`.
- Locked intended statement: determine whether there exists a balanced splittable Hadamard matrix with parameters `BSHM(120,20,20,0)`.
- Source-faithful interpretation: there should exist a Hadamard matrix `H` of order `120` and a choice of `20` rows forming a submatrix `H1` such that
  `H1^T H1 = 20 I_120 + 20 A`
  for some `(0,1)`-matrix `A`. Equivalently, the off-diagonal column inner products in `H1` are exactly `20` or `0`.
- If the main claim closed exactly, the title theorem would simply be:
  `Existence` or `nonexistence` of `BSHM(120,20,20,0)`.
- A successful exact solve here would still look like roughly `80%` of a micro-paper, with the remaining packaging work mainly being the short family recap around Theorem 65 / Corollary 67 and a cleaned certificate or obstruction.

## definitions
- Let `H` be a Hadamard matrix of order `120`, and let `H1` be the selected `20 x 120` row submatrix.
- Because the chosen rows come from a Hadamard matrix, `H1 H1^T = 120 I_20`.
- Set `B := H1^T H1`. In this instance, `B = 20(I + A)`.
- Since the columns of `H1` are `20`-vectors with `±1` entries:
  - `B_{ij} = 20` means columns `i` and `j` of `H1` are identical.
  - `B_{ij} = 0` means those two columns are orthogonal in `R^20`.
  - `B_{ij} = -20` cannot occur in this parameter set.
- The complementary `100 x 120` row submatrix is denoted `H2`.
- Conventions used below are entirely local to the standard balancedly splittable definition above; no theorem drift is being introduced.

## approach_A
- Structural / invariant route.
- Start from `B^2 = H1^T(H1 H1^T)H1 = 120 B`.
- Substituting `B = 20(I + A)` gives
  `A^2 = 4A + 5I`.
- Consequences:
  - diagonal entries give `deg_A(v) = 5` for every vertex;
  - if `A_{ij} = 1`, then vertices `i,j` have exactly `4` common neighbors;
  - if `A_{ij} = 0`, then vertices `i,j` have `0` common neighbors.
- Hence each connected component is a clique of size `6`, and there are `120 / 6 = 20` components.
- Therefore the column graph of `H1` is forced to be
  `20 K_6`.
- This is much stronger than the original statement of the instance: the selected `20` rows do not permit an arbitrary two-valued pattern; they force a rigid `6`-fold column repetition structure.
- Once the columns are grouped by these cliques, the `20` distinct column types are pairwise orthogonal `±1` vectors in `R^20`, so they form a Hadamard basis of order `20`.
- After a column permutation,
  `H1 = V ⊗ 1_6^T`
  for some Hadamard matrix `V` of order `20`.
- Immediate consequence for the remaining rows: every row of `H2` is orthogonal to every row of `H1`, so every row of `H2` has block sum `0` on each of the `20` six-column blocks. Since entries are `±1`, each block must contain exactly three `+1` and three `-1`.
- Self-check: every step above uses only `H1 H1^T = 120 I_20`, the source-faithful definition of `B`, and elementary matrix identities.

## approach_B
- Construction / extremal route.
- Try to extend the forced top block
  `H1 = V ⊗ 1_6^T`
  to a full Hadamard matrix by analyzing `H2`.
- Since `H^T H = 120 I`, we get
  `H2^T H2 = 120 I - H1^T H1 = 100 I - 20 A`.
- Under the clique decomposition from Approach A, this becomes block diagonal with `20` copies of
  `120 I_6 - 20 J_6`.
- So within each six-column block:
  - each column has norm `100` in `H2`;
  - distinct columns have inner product `-20`;
  - the six columns sum to `0`;
  - the block contributes rank `5`.
- This is the Gram matrix of a regular simplex in a `5`-dimensional subspace, and the `20` blocks occupy mutually orthogonal `5`-dimensional subspaces of `R^100`.
- A naive tensor construction would therefore want a `5 x 6` zero-sum `±1` building block. But any two length-`6` zero-sum `±1` vectors have inner product in `{6,2,-2,-6}`, never `0`, so the simplest local orthogonal lift does not exist.
- That kills the most obvious product construction, but it does not yet give a contradiction, because orthogonality of full rows in `H2` can still arise by cancellation across different six-column blocks.
- Self-check: this route produces a genuine obstruction to the simplest extension mechanism, but not a proof of nonexistence.

## lemma_graph
- Lemma 1: `B = H1^T H1 = 20(I + A)` and `B^2 = 120 B`.
- Lemma 2: `A^2 = 4A + 5I`.
- Lemma 3: `A` is `5`-regular, adjacent pairs have `4` common neighbors, and nonadjacent pairs have `0` common neighbors.
- Lemma 4: every component of `A` is `K_6`; hence `A = 20 K_6`.
- Lemma 5: after column permutation, `H1 = V ⊗ 1_6^T` for some order-`20` Hadamard matrix `V`.
- Lemma 6: each row of `H2` has exactly three `+1` and three `-1` in each six-column block.
- Lemma 7: `H2^T H2` is block diagonal with `20` copies of `120 I_6 - 20 J_6`.
- Open gap: convert Lemmas 5-7 either into an actual extension or into an impossibility argument.

## chosen_plan
- Best path chosen: fully lock the invariant reduction first, because it is exact, short, and theorem-facing.
- I then tested whether the forced block structure admits an immediate constructive lift from a local `5 x 6` zero-sum `±1` factor. It does not.
- I did not move to search or optimization because:
  - the dossier marks the target as not search-heavy;
  - the invariant reduction already produced a real theorem slice;
  - I do not yet have a sharply justified finite search space that would respect the "minimal code" rule.
- Conservative conclusion: retain the proved structural reduction, stop before speculative brute force, and hand verification a clean local package.

## self_checks
- Statement-faithfulness check: the solve uses the standard column-Gram interpretation `H1^T H1 = ell I + aA + b(J-A-I)`, not a row-Gram proxy.
- Algebra check: `B^2 = 120B` follows immediately from `H1 H1^T = 120I_20`.
- Graph check: `A^2 = 4A + 5I` really does force degree `5`, adjacent common-neighbor count `4`, and nonadjacent common-neighbor count `0`.
- Clique check: those graph parameters imply exactly disjoint `K_6` components; there is no room for another connected pattern.
- Span check: the `20` distinct column representatives are pairwise orthogonal nonzero vectors in `R^20`, hence a basis, so the block-constant subspace argument for `H2` is valid.
- Conservatism check: no existence or nonexistence verdict is claimed beyond what the above lemmas certify.

## code_used
- No code used.
- The current packet is reasoning-first only.

## result
- Strong partial result, no exact settle.
- Proven conditional structure:
  - any `BSHM(120,20,20,0)` forces the selected `20` rows to collapse the `120` columns into `20` classes of size `6`;
  - after column permutation, the selected submatrix must be `V ⊗ 1_6^T` with `V` an order-`20` Hadamard matrix;
  - every remaining row must be a concatenation of `20` zero-sum six-vectors, i.e. each block is exactly a `3+ / 3-` pattern.
- I also obtained a negative local construction result: the obvious blockwise tensor lift fails because zero-sum `±1` six-vectors are never mutually orthogonal.
- This is not yet an existence proof, not yet a contradiction, and therefore not yet a paper-ready closure.
- Natural boundary remark falling out immediately: the unresolved difficulty is entirely in the `100` complementary rows; the top `20` rows are already rigid once the parameter tuple is fixed.

## family_affinity
- Very high family affinity.
- The same calculation works for the whole Type 2 family `BSHM(8rs,4s,4s,0)`.
- In general, writing `B = 4s(I + A)` and using `B^2 = 8rs B` yields
  `A^2 = 2(r-1)A + (2r-1)I`,
  so `A` must be a disjoint union of `4s` cliques `K_{2r}`.
- For the present instance `r = 3`, `s = 5`, this specializes to `20 K_6`.

## generalization_signal
- Strong theorem-slice signal.
- Suggested general lemma:
  `If BSHM(8rs,4s,4s,0) exists, then after a column permutation the selected 4s-row submatrix is H_(4s) ⊗ 1_(2r)^T for some Hadamard matrix H_(4s), and every complementary row has zero sum on each of the 4s blocks of size 2r.`
- What scales:
  - the `B^2 = nB` calculation;
  - the clique decomposition of the column graph;
  - the block-zero-sum constraint on complementary rows.
- What does not yet scale:
  - turning the block structure into an explicit extension;
  - deriving a general impossibility from the complementary-row constraints alone.

## proof_template_reuse
- Reusable template:
  1. write `B = H1^T H1`;
  2. use `B^2 = nB`;
  3. translate the quadratic identity into exact degree / common-neighbor counts for the column graph;
  4. identify the forced graph as a union of equal cliques;
  5. pass from clique structure to a tensor-shaped form for `H1`;
  6. deduce rigid block-sum conditions on `H2`.
- This template should transfer directly to the nearby odd-odd Type 2 cases, especially the other open tuples with the same `b = 0` pattern.

## candidate_theorem_slice
- Candidate theorem slice:
  `Any BSHM(120,20,20,0), if it exists, is column-permutation equivalent on the selected 20-row submatrix to H_20 ⊗ 1_6^T; equivalently, the associated column graph is exactly 20 K_6 and every complementary row has a 3+/3- split on each six-column block.`
- This is a real theorem-facing slice with immediate structural content, but by itself it is still below the micro-paper threshold.

## smallest_param_shift_to_test
- First parameter shift to test: `(72,12,12,0)` with `r = s = 3`.
- Second parameter shift to test: `(168,12,12,0)` with `r = 7`, `s = 3`.
- Reason: the same forced-clique argument gives `12 K_6` in the first case and `12 K_14` in the second, so these are the cleanest neighbors for seeing whether the complementary-row obstruction is genuinely local to `r = 3, s = 5` or part of a wider Type 2 pattern.

## why_this_is_or_is_not_publishable
- Not publishable yet as a stand-alone micro-paper result.
- Why not:
  - there is no exact existence verdict;
  - there is no impossibility theorem;
  - the current output is a strong reduction, not a closed title theorem.
- If the main claim were closed, the package would still be about `70-90%` of a paper, because the frontier hook is already in place and the remaining packaging would be light.
- In its current state, the result is still too thin for the strict micro-paper lane, though it is genuinely theorem-facing and worth preserving.

## paper_shape_support
- What extra structure would make this paper-shaped if the main claim closes?
  - one exact extension theorem converting the `20 K_6` reduction into an explicit order-`120` construction; or
  - one exact obstruction showing that no orthogonal `100`-row `3+/3-` block basis can exist.
- Minimal remaining packaging work after an exact closure:
  - restate the Type 2 family frontier from the source;
  - include this forced `20 K_6` lemma as the first structural proposition;
  - add the exact certificate or contradiction;
  - record the immediate corollary that the first open `s = 5` case is settled.
- One immediate remark already available: any solution must be a six-fold lift over an order-`20` Hadamard skeleton, so the odd-odd difficulty lives entirely in the complementary `100` rows.

## boundary_remark
- Boundary remark:
  the instance is not arbitrary order-`120` noise. The parameter tuple forces the selected rows into a rigid six-fold replication of an order-`20` Hadamard basis, and the only remaining flexibility is how to realize the `100` orthogonal complementary rows with `3+/3-` support on each six-column block.
- This sharply isolates where the odd-odd barrier actually sits.

## likely_failure_points
- The current reduction may still be too weak to force nonexistence; cancellation across many six-column blocks could support an exotic extension.
- The simple tensor obstruction is only local. It rules out the most naive construction, not all global constructions.
- The family-level theorem slice may already be implicit in the published source, so verification should treat its novelty conservatively even though it is useful locally.
- If a future solve uses computation, it must justify a sharply bounded search space from the block model above rather than jumping directly to generic SAT / brute force.

## what_verify_should_check
- Check the definition-faithfulness of `B = H1^T H1 = 20(I + A)`.
- Recheck the algebra `B^2 = 120B` and the derived identity `A^2 = 4A + 5I`.
- Recheck that these graph parameters force `A = 20 K_6`.
- Recheck the claim that the `20` distinct column representatives form an order-`20` Hadamard basis.
- Recheck the complementary-row consequence: orthogonality to all rows of `H1` is equivalent to block sum `0` on each six-column block.
- Novelty check should ask whether the general family lemma `A = 4s K_{2r}` is already explicitly stated or only implicit in the source.
