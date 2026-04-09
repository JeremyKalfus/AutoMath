# d4-balanced-equi-20-square

## statement_lock
- Active slug: `d4-balanced-equi-20-square`
- Title: `Does there exist a 4-balanced equi-20-square?`
- Locked intended statement: `A 4-balanced equi-20-square exists.`
- Working equivalent formulation from `selected_problem.md`: it is enough to construct a Latin square of order `20` that is partitionable into `4 x 5` subrectangles, each subrectangle containing every symbol exactly once.

## definitions
- Work on the symbol set `Z/20Z = {0,1,...,19}` with arithmetic mod `20`.
- A Latin square of order `20` means each symbol appears exactly once in each row and each column.
- A `4 x 5` subrectangle means `4` rows by `5` columns.
- Ambiguity noted: the solve argument below proves the Latin-square partition formulation directly and then uses the dossier's stated equivalence to transfer back to the balanced equi-square statement.
- Missing-definition risk noted for verification: the exact equivalence theorem and any hidden hypotheses from the source should be re-checked before Lean.

## approach_A
Structural / invariant approach: use the cyclic Latin square and a factorization of `20` as `4 * 5`.

Take
`L(r,c) = r + c (mod 20)`.

This is the Cayley table of the cyclic group `Z/20Z`, so it is a Latin square.

Partition the rows into
- `R_a = {a, a+5, a+10, a+15}` for `a in {0,1,2,3,4}`

and partition the columns into
- `C_b = {5b, 5b+1, 5b+2, 5b+3, 5b+4}` for `b in {0,1,2,3}`.

Each `R_a x C_b` block has size `4 x 5`. The key claim is that each such block contains every residue mod `20` exactly once.

Why this should work:
- every entry in `R_a x C_b` has the form `a + 5u + 5b + t` with `u in {0,1,2,3}` and `t in {0,1,2,3,4}`
- the pair `(u,t)` ranges over `4 * 5 = 20` possibilities
- mod `5`, the residue determines `t`
- after fixing `t`, the quotient by `5` mod `4` determines `u`

So the block map `(u,t) -> a + 5u + 5b + t (mod 20)` should be bijective.

Self-check after approach A:
- The block orientation matches the dossier: `4` rows and `5` columns.
- The construction is genuinely structural, not a brute-force search.

## approach_B
Construction / extremal / contradiction approach: reinterpret a `4`-balanced equi-`20`-square by symbol incidences.

For a fixed symbol `s`, its incidence matrix has total weight `20`. Since every row and column contribution is either `0` or `4`, symbol `s` must occur in exactly `5` rows and exactly `5` columns. Inside those chosen rows and columns, every chosen row and every chosen column has degree `4`, so the support graph is a `4`-regular bipartite graph on `5 + 5` vertices, equivalently `K_{5,5}` minus a perfect matching.

This suggests trying to organize the full square by five row classes and five column classes, with each symbol determined by a highly structured cyclic rule rather than by search. That heuristic points back toward a group-based construction and is consistent with approach A.

Why I did not push this route to a standalone proof:
- it gives a useful local picture of each symbol
- but approach A already gives an explicit global witness in the equivalent Latin formulation
- forcing the incidence route all the way through would add complexity without improving confidence

Self-check after approach B:
- This route did not produce a contradiction.
- It supports, rather than undermines, the expectation that a cyclic construction exists.

## lemma_graph
1. Lemma 1: `L(r,c) = r + c (mod 20)` is a Latin square of order `20`.
2. Lemma 2: The row sets `R_a` partition the `20` rows into five `4`-sets.
3. Lemma 3: The column sets `C_b` partition the `20` columns into four `5`-sets.
4. Lemma 4: For every `a,b`, the block `R_a x C_b` contains each symbol of `Z/20Z` exactly once.
5. Conclusion: `L` is a Latin square of order `20` partitionable into `4 x 5` subrectangles.
6. Bridge step from dossier: by the stated equivalence, a `4`-balanced equi-`20`-square exists.

## chosen_plan
Use approach A. It gives an explicit witness with a short proof and no code.

Proof attempt:

Define `L(r,c) = r + c (mod 20)` on rows and columns indexed by `0,1,...,19`.

`L` is Latin because:
- fixing `r`, the map `c -> r+c` is a permutation of `Z/20Z`
- fixing `c`, the map `r -> r+c` is also a permutation of `Z/20Z`

Now partition rows and columns by
- `R_a = {a+5u : u = 0,1,2,3}` for `a = 0,1,2,3,4`
- `C_b = {5b+t : t = 0,1,2,3,4}` for `b = 0,1,2,3`

Fix `a` and `b`. Any entry of the block `R_a x C_b` has the form
`L(a+5u, 5b+t) = a + 5u + 5b + t (mod 20)`
with `u in {0,1,2,3}` and `t in {0,1,2,3,4}`.

To show every symbol appears exactly once in this block, suppose
`a + 5u + 5b + t == a + 5u' + 5b + t' (mod 20)`.
Then
`5(u-u') + (t-t') == 0 (mod 20)`.
Reducing mod `5` gives `t == t' (mod 5)`. Since both lie in `{0,1,2,3,4}`, this forces `t = t'`.
Then `5(u-u') == 0 (mod 20)`, so `4 | (u-u')`. Since both `u,u'` lie in `{0,1,2,3}`, this forces `u = u'`.

Thus the `20` pairs `(u,t)` give `20` distinct residues mod `20`, so the block contains all `20` symbols exactly once.

Therefore `L` is a Latin square of order `20` partitionable into `4 x 5` subrectangles.

Assuming the source equivalence recorded in `selected_problem.md`, this proves the intended statement: a `4`-balanced equi-`20`-square exists.

Self-check after chosen plan:
- The proof is explicit and constructive.
- No hidden search step was used.
- The only external dependency is the dossier-stated equivalence between the Latin formulation and the balanced equi-square formulation.

## self_checks
- Statement lock check: the target is existence, not uniqueness or classification.
- Orientation check: the partition really is into `5` row blocks of size `4` and `4` column blocks of size `5`, hence `4 x 5` rectangles.
- Latin check: every row and every column of `L(r,c)=r+c` is a permutation.
- Block-bijection check: the injectivity argument on `(u,t)` is complete and gives surjectivity because the block has exactly `20` cells.
- Conservatism check: I am not calling this `EXACT` in solve, and I am flagging the equivalence theorem as something verification should independently confirm.

## code_used
- No code used.
- No bounded experiment seemed necessary because the construction is symbolic and the arithmetic check is short.

## result
- Provisional solve-stage verdict: `CANDIDATE`
- Confidence: high on the Latin witness itself; slightly lower on the final transfer only because I am relying on the dossier's stated equivalence rather than reproving that equivalence here.
- Core witness: the cyclic Latin square `L(r,c) = r + c (mod 20)` with row partition `R_a = {a,a+5,a+10,a+15}` and column partition `C_b = {5b,5b+1,5b+2,5b+3,5b+4}`.
- Directly established here: this witness is a Latin square of order `20` partitioned into `4 x 5` blocks, each block containing every symbol exactly once.
- Hence, under the locked equivalence from the dossier, a `4`-balanced equi-`20`-square exists.

## likely_failure_points
- The exact equivalence theorem may have extra conventions or a directionality issue that should be checked against the source.
- The phrase "partitionable into `4 x 5` subrectangles" could, in principle, hide a stronger notion than the one used here, though the dossier wording strongly suggests the standard row-block/column-block partition.
- Verification should rule out any mismatch between the intended balanced-object indexing and the Latin witness indexing.

## what_verify_should_check
- Re-check the source theorem that a `4`-balanced equi-`20`-square exists if and only if there is a Latin square of order `20` partitionable into `4 x 5` subrectangles.
- Confirm that the specific partition above is admissible under the source's exact notion of subrectangle decomposition.
- Independently verify the block calculation for `L(r,c)=r+c (mod 20)`.
- If the equivalence is clean, either:
  - derive the corresponding balanced equi-square explicitly from this Latin witness, or
  - formalize the equivalence theorem plus this witness in Lean.

## verify_rediscovery
- Pass 1 result: no rediscovery established within the bounded search budget.
- Limited web search checked the exact instance phrase, alternate Latin-square partition wording, the canonical 2020 paper itself, and the unresolved-case table inside that paper.
- The canonical paper still presents the `n = 20`, `d = 4` case as unresolved, and the bounded recent-status search did not uncover a later paper or note settling this exact instance.
- Practical conclusion for Pass 1: this is not a known solved instance on the evidence gathered here, so the verification outcome must turn on faithfulness and proof correctness rather than rediscovery.

## verify_faithfulness
- Pass 2 result: not faithful.
- The first serious problem is definition drift in the Latin-square translation used by the solve record.
- In the canonical source, a Latin-square `d x (n/d)` subrectangle is not a `d x (n/d)` block containing all `n` symbols exactly once. The source definition is a rectangular submatrix in which the number of distinct symbols equals the number of columns, so for a `4 x 5` subrectangle the block should involve `5` distinct symbols, each repeated across the `4` rows.
- The solve record instead proves that each proposed `4 x 5` block in the cyclic Latin square contains all `20` symbols exactly once.
- That is a different and much stronger-looking block property, but it is not the source's subrectangle notion and does not justify the claimed transfer to a `4`-balanced equi-`20`-square.
- Therefore the solver proved a nearby variant statement about a cyclic Latin square partition, not the locked intended statement. The correct harness classification is `VARIANT`, not `CANDIDATE` or `EXACT`.

## verify_proof
- Pass 3 result: the first incorrect step is the bridge from the cyclic Latin-square block calculation to the intended existence claim.
- Up to that point, the internal arithmetic is fine: for the proposed row and column partition, each `4 x 5` block really does contain `20` distinct residues.
- But that fact does not match the source's required meaning of a `4 x 5` Latin subrectangle, so the sentence "Therefore `L` is a Latin square of order `20` partitionable into `4 x 5` subrectangles" is false under the paper's definitions.
- Because the proof target shifted at that step, the subsequent transfer to a `4`-balanced equi-`20`-square is unsupported.
- No tiny local repair is apparent. Fixing this would require a genuinely different construction or a different theorem, not a cosmetic edit.

## verify_adversarial
- Pass 4 result: the proposed construction fails the intended-support check.
- I ran an independent local checker on the solver's partition of the cyclic Latin square.
- Every proposed `R_a x C_b` block has exactly `20` distinct symbols, each appearing once.
- That computation confirms the solver's arithmetic, but adversarially it also confirms the mismatch: these blocks are not `4 x 5` subrectangles in the source sense, which would have only `5` distinct symbols.
- No code or witness supporting the actual intended balanced-equi-square statement was produced.

## verify_verdict
- `verify_verdict`: `WRONG_STATEMENT`
- `classification`: `VARIANT`
- `confidence`: `high`
- `lean_ready`: `false`
- Reason: the solve-stage argument establishes a different Latin-block property than the canonical source requires, so the intended statement remains unproved and is not ready for Lean.

## minimal_repair_if_any
- No conservative repair was made.
- A valid repair would need either:
  - an explicit construction whose `4 x 5` blocks satisfy the source's actual subrectangle definition, or
  - a source-backed theorem showing that the solver's stronger-looking block condition still implies the required decomposition.
- Neither was available within the verify budget, so the correct action is to mark this attempt as a wrong-statement variant rather than patch it speculatively.
