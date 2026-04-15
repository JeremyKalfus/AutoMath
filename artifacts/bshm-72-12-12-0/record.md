# bshm-72-12-12-0

## statement_lock
- Active slug: `bshm-72-12-12-0`
- Title: `The First Odd-Odd Open Case for BSHM(8rs,4s,4s,0)`
- Locked intended statement: determine whether there exists a balanced splittable Hadamard matrix `BSHM(72,12,12,0)`.
- Working exact reformulation used here: there exists a Hadamard matrix `H` of order `72` and a choice of `12` rows forming a submatrix `H1` such that
  `B = H1^T H1 = 12 I_72 + 12 A`
  for some symmetric `(0,1)`-matrix `A` with zero diagonal. Equivalently, the off-diagonal column inner products of `H1` are exactly `12` or `0`.
- Exact title theorem if the main claim closes: `Existence or nonexistence of BSHM(72,12,12,0)`.
- Solve-to-paper note: if this exact existence question closes, the result should still account for roughly `70-90%` of a short paper because the frontier framing is already isolated by the source.

Self-check:
- I am locking the standard column-Gram interpretation, which is the only dossier-consistent reading for a Hadamard row selection.
- I am not weakening the target to a nearby certificate or a non-Hadamard proxy.

## definitions
- Let `H1` be the `12 x 72` selected-row submatrix.
- Let `B = H1^T H1`. Then `B` is symmetric positive semidefinite, `B_ii = 12`, and `B_ij in {12,0}` for `i != j`.
- Write `B = 12(I + A)`, where `A` is the adjacency matrix of the graph on the `72` columns joining pairs with inner product `12`.
- Because the selected rows come from a Hadamard matrix of order `72`, they are pairwise orthogonal and have squared norm `72`, so
  `H1 H1^T = 72 I_12`.
- Therefore
  `B^2 = H1^T(H1 H1^T)H1 = 72 B`.
- If the column graph turns out to be a disjoint union of `K_6` blocks, then after a column permutation
  `H1 = [u_1 repeated 6 times | ... | u_12 repeated 6 times]`
  where `u_1,...,u_12 in {+1,-1}^{12}` are pairwise orthogonal, hence form a Hadamard matrix of order `12`.

Self-check:
- The only real definitional risk is source faithfulness of the tuple `(72,12,12,0)`.
- Every identity here follows from standard Gram-matrix algebra for a selected set of Hadamard rows.

## approach_A
Structural / invariant route: use `B^2 = 72B` to force the exact column-collision graph.

Starting from `B = 12(I + A)`, the projector identity gives

`144(I + 2A + A^2) = 864(I + A)`,

so

`A^2 - 4A - 5I = 0`.

Consequences:
- Diagonal entries give `deg(v) = 5` for every vertex `v`.
- For adjacent `i ~ j`, `(A^2)_{ij} = 4`, so adjacent pairs have exactly `4` common neighbors.
- For distinct nonadjacent `i,j`, `(A^2)_{ij} = 0`, so nonadjacent pairs have no common neighbors.

This forces `A` to be the disjoint union of `12` copies of `K_6`:
- Fix a vertex `v`. Its neighborhood has size `5`.
- If `u` is a neighbor of `v`, then `u` shares exactly `4` common neighbors with `v`; these must be the other `4` vertices of `N(v)`, so `N(v)` together with `v` induces a `K_6`.
- If `w` lies outside this `K_6`, then `w` is nonadjacent to `v`, hence cannot be adjacent to any vertex of `N(v)`, because that would give a common neighbor of the nonadjacent pair `(v,w)`.
- So the connected component of `v` is exactly that `K_6`.

Therefore, after permuting columns,

`B = 12 (J_6 ⊕ J_6 ⊕ ... ⊕ J_6)`  with `12` blocks.

Equivalently, the selected `12` rows collapse the `72` columns into `12` classes of size `6`, with identical top `12` entries inside each class.

Self-check:
- The graph equation is exact and short; there is no heuristic step.
- The clique-union deduction is the main rigid theorem slice from the solve pass.

## approach_B
Construction / extremal route: analyze the remaining `60` rows after the clique decomposition.

Let `R` be the `60 x 72` matrix formed by the other rows of `H`, and partition the `72` columns into the `12` six-column classes forced by Approach A.

Write each row `r` of `R` as

`r = (r^{(1)} | r^{(2)} | ... | r^{(12)})`

with `r^{(t)} in {+1,-1}^6`.

Because `r` is orthogonal to every selected row and those selected rows span all block-constant sign patterns across the `12` classes, each block sum must vanish:

`sum(r^{(t)}) = 0` for every `t`.

Since each block has length `6`, every block of every remaining row has exactly `3` plus signs and `3` minus signs.

This gives an exact reduced formulation:
- if `BSHM(72,12,12,0)` exists, then there exists a `60 x 72` `(+1,-1)`-matrix `R` such that
  - `R R^T = 72 I_60`,
  - after partitioning the columns into `12` blocks of size `6`, every row is `3+/3-` on each block;
- conversely, if such an `R` exists, then stacking it under any order-`12` Hadamard block-constant top part produces a Hadamard matrix whose first `12` rows realize `BSHM(72,12,12,0)`.

So the original problem is equivalent to a sharply reduced completion problem: find or obstruct an orthogonal basis of the `60`-dimensional subspace

`W = {x in R^72 : each 6-column block of x sums to 0}`

consisting entirely of `(+1,-1)` vectors.

Local sanity check inside one block:
- Let `S` be the set of all `20` balanced sign vectors of length `6` with three `+1` and three `-1`.
- For a fixed pair of coordinates, a direct count over `S` shows column self-inner product `20` and off-diagonal column inner product `-4`.
- Repeating all `20` rows three times yields a `60 x 6` block with column Gram `72 I_6 - 12 J_6`.

This means a single `6`-column block has the right local statistics; any true obstruction must be global, in how `12` such blocks can be glued while keeping all `60` rows mutually orthogonal.

Self-check:
- The converse stack is exact, not heuristic.
- The local balanced-block construction is only a sanity check; it does not solve the global coupling problem.

## lemma_graph
1. Model the selected `12` rows by `H1` and write `B = H1^T H1 = 12(I + A)`.
2. Use `H1 H1^T = 72 I_12` to obtain `B^2 = 72B`.
3. Simplify to `A^2 - 4A - 5I = 0`.
4. Read off degree `5`, adjacent common-neighbor count `4`, and nonadjacent common-neighbor count `0`.
5. Deduce that `A` is `12 K_6`.
6. Permute columns so `H1` is block-constant on `12` blocks of size `6`.
7. Let `R` be the remaining `60` rows and use orthogonality against the selected rows to force each `6`-block sum to be `0`.
8. Reduce the original existence question to the existence of an orthogonal `(+1,-1)` basis of the block-sum-zero subspace `W`.

## chosen_plan
- The best path is Approach A first, because it turns the vague two-distance condition into an exact graph equation and rigidly identifies the column structure.
- Approach B is then the right continuation, because it converts the unsolved existence problem into a smaller orthogonal-completion problem with a clean blockwise constraint.
- I pushed the reduced problem as far as I could without jumping into unjustified search. The current blocker is no longer the BSHM definition; it is the global compatibility of `60` block-balanced orthogonal rows.

Self-check:
- This is still reasoning-first and theorem-facing.
- I did not silently switch to search once the structural reduction was obtained.

## self_checks
- Source-faithfulness check: verification should confirm that `(72,12,12,0)` means exactly `H1^T H1 = 12I + 12A`.
- Algebra check: `A^2 - 4A - 5I = 0` is the decisive invariant identity.
- Graph check: the step from local common-neighbor counts to `12 K_6` is exact.
- Reduction check: the converse stack with a `12 x 12` Hadamard matrix should be checked explicitly.
- Scope check: I have a real theorem slice, but not yet an existence or nonexistence proof for the full target.

## code_used
- No code used.
- I did not justify a search pass because the structural reduction was still advancing and the dossier is not marked `search_heavy`.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact mathematical output from this solve pass:
  - any `BSHM(72,12,12,0)` forces the selected-row column graph to be the disjoint union `12 K_6`;
  - equivalently, after permuting columns, the selected `12` rows are a `12 x 12` Hadamard matrix with each column repeated `6` times;
  - the full existence question is exactly equivalent to the existence of a `60 x 72` orthogonal `(+1,-1)` completion whose rows are `3+/3-` on each of the `12` six-column blocks.
- Main-claim status:
  - no exact construction was found;
  - no impossibility proof was obtained for the reduced `60`-row completion problem.
- What extra structure would make this paper-shaped if the main claim closes:
  - either an explicit reduced completion `R` or a clean obstruction to such an `R`;
  - one short proposition recording the `12 K_6` reduction;
  - one comparison remark tying the result back to the Type 2 family frontier in Theorem 65 / Corollary 67.

## family_affinity
- High.
- The identity behind Approach A scales to any candidate with parameters `BSHM(n,ell,ell,0)`: writing `B = ell(I + A)` and using `B^2 = nB` gives
  `A^2 - (n/ell - 2) A - (n/ell - 1) I = 0`,
  so the column graph is forced to be a disjoint union of cliques of size `n/ell`.
- In the Type 2 family `BSHM(8rs,4s,4s,0)`, this clique size is `2r`.
- For the present case `r = 3`, every realization must therefore be built over six-column classes.

## generalization_signal
- What scales:
  - the Gram-to-graph reduction;
  - the union-of-cliques conclusion for all `b = 0` cases with `a = ell`;
  - the deduction that the complementary rows must live in the block-sum-zero subspace.
- What does not yet scale:
  - the final orthogonal completion problem;
  - the global gluing of balanced rows across many forced blocks.
- Current signal: the reusable part is a theorem template, but the hard residue remains genuinely instance-sensitive.

## proof_template_reuse
- Reusable template:
  1. write the selected-row Gram matrix in the `ell I + aA + b(J-A-I)` form;
  2. impose `B^2 = nB`;
  3. translate the resulting polynomial identity into exact graph structure;
  4. compress the selected rows accordingly;
  5. rewrite the remaining rows as an orthogonal completion problem on the complementary subspace.
- This template should transfer directly to nearby `BSHM(n,ell,ell,0)` targets, especially others with `n/ell = 6`.
- It will not, by itself, settle those targets; it only identifies the reduced battlefield sharply.

## candidate_theorem_slice
- Candidate theorem slice proved in solve form:
  `A BSHM(72,12,12,0) exists if and only if there exists a 60 x 72 (+1,-1)-matrix R with RR^T = 72 I_60 such that, after partitioning the 72 columns into 12 blocks of size 6, every row of R has exactly three +1 and three -1 entries in each block.`
- Supporting lemma:
  `For any such realization, the selected-row column graph is exactly 12 K_6.`
- This is a real theorem slice, not just a heuristic restatement.

## smallest_param_shift_to_test
- Primary next shift: `BSHM(120,20,20,0)`.
- Reason: it keeps the same forced clique size `n/ell = 6`, so it tests whether the real obstruction is tied to six-column blocks or only to the small top block `ell = 12`.
- Secondary next shift: `BSHM(168,28,28,0)`.
- Reason: it stays on the same `r = 3` branch, again preserving six-column classes while enlarging the top Hadamard part.

## why_this_is_or_is_not_publishable
- Not publishable yet as a micro-paper packet, because the main frontier instance remains unresolved.
- The current package is mathematically real and theorem-facing, but it is still a reduction note rather than a solved title theorem.
- If the main claim closes from here, the paper is still near: the exact title theorem would simply be the existence or nonexistence of `BSHM(72,12,12,0)`, the `12 K_6` reduction becomes the main preparatory proposition, and the remaining packaging work is short.
- Minimal remaining packaging work after a closure:
  - verify source-faithful definitions;
  - write the reduction lemma cleanly;
  - present the construction or obstruction for the reduced completion problem;
  - add one paragraph linking back to the Type 2 odd-odd frontier.
- Current assessment: too thin for the micro-paper lane by itself, but close enough that a single further exact solve on the reduced problem would likely finish the packet.

## paper_shape_support
- Successful solve would still be about `0.84` of a paper, consistent with the selection packet.
- Exact title theorem if solved:
  - `The first odd-odd open case for BSHM(8rs,4s,4s,0): the parameter (72,12,12,0)`.
- Smallest natural supporting theorem if the main claim closes:
  - the forced `12 K_6` column decomposition and its block-balanced completion reformulation.
- Immediate corollary / remark that already falls out:
  - in any realizing order-72 Hadamard matrix, every row outside the selected `12` must contain exactly three `+1` and three `-1` entries in each of the twelve forced six-column classes.
- Current package status:
  - closer to a paper-shaped claim than a raw instance search;
  - still not enough on its own for `PAPER_READY`.

## boundary_remark
- Boundary of the current argument:
  - it completely determines the selected-row geometry;
  - it does not yet decide whether the complementary `60`-row orthogonal basis exists.
- The one-block arithmetic does not obstruct the problem; a single six-column block can already realize the needed local column Gram.
- So the residue is genuinely global.
- Current package is therefore not just an isolated witness hunt, but it is also not yet a finished micro-paper theorem. It sits in the middle: a strong reduction plus a sharply defined residual problem.

## likely_failure_points
- The main risk is source normalization: verification should confirm the exact tuple interpretation used here.
- The converse equivalence should be checked carefully for row ordering and block permutation conventions.
- The local one-block construction is only a sanity check; it must not be oversold as progress on the global existence question.
- There may still be a hidden global obstruction or a construction template not visible from this reduction alone.

## what_verify_should_check
- Confirm the source definition of a balanced splittable Hadamard matrix and the exact meaning of `(72,12,12,0)`.
- Check the algebra:
  - `B = 12(I + A)`;
  - `B^2 = 72B`;
  - `A^2 - 4A - 5I = 0`.
- Check the graph-theoretic deduction that this forces `12 K_6`.
- Check the reduction from orthogonality against the top `12` rows to the `3+/3-` condition on each six-column block.
- Check the converse stack: a `60 x 72` orthogonal block-balanced completion indeed reconstructs a Hadamard matrix realizing the BSHM condition.
