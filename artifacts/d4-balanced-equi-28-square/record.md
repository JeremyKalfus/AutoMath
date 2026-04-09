# d4-balanced-equi-28-square

## statement_lock
- Active slug: `d4-balanced-equi-28-square`
- Title: `Does there exist a 4-balanced equi-28-square?`
- Locked intended statement: `A 4-balanced equi-28-square exists.`
- Working equivalent formulation from `selected_problem.md`: construct a Latin square of order `28` that decomposes into `4 x 7` Latin subrectangles.
- Conservative interpretation carried into this solve note: a `4 x 7` Latin subrectangle uses exactly `7` symbols, each row is a permutation of those `7` symbols, and each of those `7` symbols appears exactly `4` times in the block.
- Main ambiguity that I could not resolve locally without web/source access: whether "decomposes into `4 x 7` subrectangles" means a regular `7`-by-`4` grid coming from a partition of the rows into `7` four-sets and the columns into `4` seven-sets, or a more general tiling by arbitrary `4`-row by `7`-column Latin subrectangles.

Self-check:
- The exact intended statement is locked.
- The decisive unresolved convention is stated explicitly instead of being silently assumed.

## definitions
- A Latin square of order `28` has each symbol appearing exactly once in every row and exactly once in every column.
- In a `4 x 7` Latin subrectangle, each of the `4` rows contains the same `7` symbols once each, and each column contains `4` distinct symbols.
- Under the natural grid-aligned model, there are row groups `R_1, ..., R_7` of size `4`, column groups `C_1, ..., C_4` of size `7`, and blocks `B_{i,j} = R_i x C_j`.
- For such a block `B_{i,j}`, write `S_{i,j}` for its `7`-symbol set.
- In the broader arbitrary-tiling model, each subrectangle is still a cartesian product of `4` rows and `7` columns, but the family of rectangles need not come from one global row partition and one global column partition.

Self-check:
- These are the only conventions used later.
- The difference between the grid and arbitrary-tiling models is the main source of uncertainty.

## approach_A
Structural / invariant approach: assume the decomposition is the natural regular grid of `7` row groups by `4` column groups, then count how one fixed symbol can occupy the blocks.

Fix a symbol `x`.

1. For each row group `R_i`, the symbol `x` can belong to at most one block-symbol set `S_{i,j}`.
   Reason: if `x` belonged to both `S_{i,j}` and `S_{i,j'}` with `j != j'`, then every row in `R_i` would contain `x` once in `B_{i,j}` and once in `B_{i,j'}`, contradicting the Latin row condition.

2. For each row group `R_i`, the symbol `x` must belong to at least one `S_{i,j}`.
   Reason: pick any row in `R_i`; that row contains `x` somewhere, hence in exactly one of the four blocks meeting that row group.

3. Therefore, for each `i`, there is a unique column-group index `j(i)` with `x in S_{i,j(i)}`.

4. Fix one column group `C_j`. Let
   `I_j(x) = { i : x in S_{i,j} }`.
   For each `i in I_j(x)`, the symbol `x` appears in block `B_{i,j}` exactly `4` times, in `4` distinct columns of `C_j`; call that `4`-set `X_i subseteq C_j`.

5. The sets `X_i` for `i in I_j(x)` are pairwise disjoint.
   Reason: if a column `c in C_j` lay in both `X_i` and `X_{i'}` with `i != i'`, then the global column `c` would contain `x` twice, once from row group `R_i` and once from row group `R_{i'}`, contradicting the Latin column condition.

6. Hence
   `4 * |I_j(x)| = sum_{i in I_j(x)} |X_i| <= |C_j| = 7`,
   so `|I_j(x)| <= 1` for every `j`.

7. But the row-group argument gave one occurrence of `x` in each of the `7` row groups, so
   `sum_{j=1}^4 |I_j(x)| = 7`.
   This is impossible if every `|I_j(x)| <= 1`, because the left side is then at most `4`.

Conclusion of approach A:
- Under the regular grid interpretation of the `4 x 7` decomposition, no such Latin square exists.
- Therefore, under that interpretation, the intended statement is false.

Self-check:
- The contradiction uses only row uniqueness and column uniqueness in a Latin square.
- No source theorem beyond the grid-aligned decomposition assumption is being smuggled in.
- If the source allows arbitrary non-grid tilings, this approach is only conditional.

## approach_B
Construction / extremal / contradiction approach: work without assuming a regular grid and ask whether the same symbol-counting obstruction survives.

Fix a symbol `x` in an arbitrary tiling by `4 x 7` Latin subrectangles.

1. Since each subrectangle containing `x` contributes `4` occurrences of `x`, and `x` occurs `28` times total, the symbol `x` lies in exactly `7` subrectangles.

2. In each such subrectangle, `x` appears once in each of the `4` rows of that rectangle.
   Because each global row contains `x` exactly once, the row-sets of those `7` rectangles must partition the `28` rows into seven `4`-sets.

3. In each such subrectangle, `x` also occupies exactly `4` distinct columns.
   Because each global column contains `x` exactly once, those active-column `4`-sets must partition the `28` columns into seven `4`-sets.

4. So the clean obstruction from approach A disappears in the arbitrary-tiling model: `x` can use seven disjoint active column `4`-sets spread across seven different rectangles, with no immediate collision.

5. Locally, one `4 x 7` Latin subrectangle is also combinatorially feasible. If its `7` symbols are `s_1, ..., s_7`, then for each symbol the set of columns where it appears has size `4`, and each column is used by exactly `4` of the `7` symbols. That incidence pattern is not obviously contradictory; a Fano-complement pattern is a natural compatible local model.

Conclusion of approach B:
- The broad arbitrary-tiling interpretation still looks genuinely open from this solve pass.
- I do not see a direct extension of the grid obstruction to the general model.

Self-check:
- This is not a proof of existence.
- The point of this approach is to explain why the conditional contradiction from approach A does not immediately settle the dossier wording.

## lemma_graph
1. Lemma 1: In a `4 x 7` Latin subrectangle, each symbol in the block appears once in each row and in `4` distinct columns.
2. Lemma 2: In a grid-aligned decomposition, for a fixed symbol `x` and fixed row group `R_i`, there is exactly one column group `C_j` whose block-symbol set contains `x`.
3. Lemma 3: In a fixed column group `C_j`, two different row groups carrying `x` would force disjoint `4`-column supports inside `C_j`.
4. Lemma 4: Therefore a fixed column group can serve at most one row group for `x`.
5. Lemma 5: But `x` must be served in all `7` row groups, which is impossible with only `4` column groups.
6. Conditional conclusion: a regular-grid `4 x 7` decomposition cannot exist.
7. Remaining gap: the dossier wording may permit arbitrary tilings, and the above lemmas do not rule those out.

## chosen_plan
Use approach A as the strongest rigorous path available offline, but present it explicitly as a conditional disproof of the regular-grid version rather than as a full counterexample to the locked intended statement.

Rigorous attempt:

Assume there is a Latin square `L` of order `28` together with a regular grid decomposition into blocks
`B_{i,j} = R_i x C_j`
where the `R_i` partition the rows into `7` sets of size `4`, the `C_j` partition the columns into `4` sets of size `7`, and each `B_{i,j}` is a `4 x 7` Latin subrectangle.

Fix a symbol `x`.

For each row group `R_i`, there is exactly one `j(i)` such that `x in S_{i,j(i)}`. Indeed, `x` cannot lie in two different block-symbol sets in the same row group because then every row of `R_i` would contain `x` twice, and it cannot lie in none of them because every row of `R_i` contains `x` somewhere.

Now fix a column group `C_j`, and let `I_j(x) = { i : j(i) = j }`.
For each `i in I_j(x)`, the symbol `x` appears in block `B_{i,j}` in exactly `4` distinct columns of `C_j`; call this set `X_i`.
If `i != i'` and `X_i cap X_{i'}` were nonempty, then some global column in `C_j` would contain `x` twice, impossible in a Latin square. Hence the `X_i` are pairwise disjoint subsets of `C_j`, each of size `4`.

Therefore `4 |I_j(x)| <= 7`, so `|I_j(x)| <= 1` for each `j`.
But there are `7` row groups and only `4` column groups, while every row group must choose one column group for `x`. Hence
`7 = sum_j |I_j(x)| <= 4`,
contradiction.

So the regular-grid interpretation is impossible.

What this does and does not prove:
- It gives a genuine no-code contradiction for the most natural grid-aligned reading.
- It does not yet prove nonexistence for the broader arbitrary-tiling reading.

Self-check:
- The proof itself is short and internally tight.
- The only place where the full intended statement is not settled is the unresolved decomposition convention, not the counting argument.

## self_checks
- Statement-faithfulness check: I did not recycle the earlier order-20 mistake of treating a `4 x 7` block as containing all `28` symbols.
- Invariant check: the key contradiction is `7` required row-group placements of one symbol versus at most `4` possible column-group placements under disjoint `4`-column supports.
- Scope check: the contradiction is only as strong as the grid-aligned decomposition assumption.
- Conservatism check: because the arbitrary-tiling interpretation remains open locally, I am not classifying this as `COUNTEREXAMPLE`.

## code_used
- No code used.
- No bounded experiment seemed justified before the source-definition ambiguity is resolved, because the main blocker is conceptual rather than computational.

## result
- Provisional solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest rigorous output from this solve pass:
  - If the source's `4 x 7` Latin-subrectangle decomposition is required to be a regular grid coming from a row partition and a column partition, then a `4`-balanced equi-`28`-square does not exist.
  - If the source allows arbitrary tilings by `4 x 7` Latin subrectangles, then this solve pass does not settle the intended statement.
- Because I could not resolve that definition locally without browsing the source, I am stopping at `PARTIAL` rather than claiming `COUNTEREXAMPLE`.

## likely_failure_points
- The decisive one is the exact source meaning of "decomposes into `4 x 7` subrectangles".
- If the source theorem really means arbitrary tilings, then approach A only rules out a narrower variant.
- If the source theorem enforces a regular row/column block structure, then the current argument should upgrade cleanly to a full disproof.

## what_verify_should_check
- Check the canonical source definition of a Latin-square decomposition into `4 x 7` subrectangles:
  - regular grid from row and column partitions, or
  - arbitrary tiling by `4`-row by `7`-column rectangles.
- If it is the regular-grid notion, audit the counting proof above and consider upgrading the classification to `COUNTEREXAMPLE`.
- If it is the arbitrary-tiling notion, ignore the conditional disproof and continue from the arbitrary-tiling model instead.
- Independently confirm the local fact used throughout: in a `4 x 7` Latin subrectangle with `7` symbols, each symbol occupies exactly `4` distinct columns.

## verify_rediscovery
- PASS 1 used a bounded web audit only.
- The canonical source is Akbari, Marbach, Stones, and Wu, "Balanced Equi-n-Squares", Electron. J. Combin. 27(4) (2020), P4.8, DOI `10.37236/9118`.
- The source abstract and Table 1 still treat the `n = 28`, `d = 4` instance as unresolved. In Table 1, the row `n = 28` shows `[4]` in the column for Latin squares partitionable into `d x (n/d)` subrectangles and also `[4]` in the column for `d`-balanced equi-`n`-squares.
- A later MathOverflow answer by coauthor Rebecca J. Stones (2022-04-18) still lists `28 x 28` Latin squares into `4 x 7` subrectangles among the "smallest cases we didn't resolve".
- I did not find a later paper, theorem, proposition, example, or status note settling the exact `n = 28`, `d = 4` instance.
- Rediscovery verdict: not established.
- Short note on the current proof: it may be correct for a stricter regular-grid variant, but that would still not count as a rediscovery or a frontier-novel solution of the locked intended statement.

## verify_faithfulness
- The solve writeup is not faithful to the intended statement.
- The intended statement is: `A 4-balanced equi-28-square exists`, equivalently a Latin square of order `28` partitionable into `4 x 7` subrectangles in the sense used by the source.
- PASS 1 resolves the source ambiguity against the solve argument: the paper works with a partition into `d x (n/d)` subrectangles in general, not with a globally grid-aligned partition coming from `7` fixed row groups and `4` fixed column groups.
- The first fatal drift is the explicit assumption in `approach_A` / `chosen_plan` that the decomposition is a regular `7`-by-`4` grid. That is a stronger proxy problem, not the locked intended statement.
- Because the solver proves only nonexistence for this stricter proxy, the correct harness classification is `VARIANT`, not `COUNTEREXAMPLE` or `EXACT`.

## verify_proof
- First incorrect step relative to the intended statement: the introduction of a regular-grid decomposition `B_{i,j} = R_i x C_j` with fixed row groups and fixed column groups.
- That assumption is not justified by the dossier or by the canonical source wording, so the proof does not reach the intended claim.
- Conditional on that extra regular-grid assumption, I do not see an internal counting error in the core `7 <= 4` contradiction. The row-group uniqueness and column-group disjointness arguments are coherent for the narrower model.
- So the proof is best understood as a plausible conditional disproof of a different, stricter statement.

## verify_adversarial
- No code or checker exists in `artifacts/d4-balanced-equi-28-square/`; there was nothing to rerun.
- I adversarially tested whether the counting contradiction survives without the grid assumption. It does not: in an arbitrary partition into `4 x 7` Latin subrectangles, a fixed symbol can lie in exactly `7` subrectangles whose active row-sets partition the `28` rows and whose active column-sets partition the `28` columns into seven `4`-sets.
- That arbitrary-tiling picture avoids the solver's bottleneck of forcing `7` row-group placements through only `4` fixed column groups.
- This confirms that the present argument does not support the intended nonexistence claim.

## verify_verdict
- `WRONG_STATEMENT`
- Classification after verification: `VARIANT`
- Confidence: `high`
- Lean readiness: `false`
- Exact reason Lean is not ready: the current writeup does not settle the intended statement, only a stricter regular-grid variant not used by the source.

## minimal_repair_if_any
- Minimal conservative repair: relabel the existing argument as a conditional result only.
- Repaired claim: if one additionally requires the `4 x 7` subrectangles to come from a global partition of the rows into seven `4`-sets and the columns into four `7`-sets, then no such Latin square exists.
- Do not present that repaired claim as solving the selected problem.
