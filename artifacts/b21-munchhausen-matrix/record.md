# b21-munchhausen-matrix

## statement_lock
- Active slug: `b21-munchhausen-matrix`
- Title: `Is the Baron's omni-sequence value B(21) equal to 3?`
- Locked intended statement: `B(21) = 3.`
- Working formulation: there exists a `3 x 21` ternary matrix `M` with entries in `{-1,0,1}` such that, for the weight vector `w = (1,2,...,21)^T`, every nonidentity permutation of the labels changes at least one of the three balance outcomes `sign(Mw)`.
- Solve-stage normalization: I may flip the sign of any row, so every nonzero row outcome may be assumed positive.

Self-check:
- The target is exactly the existence of one verifying `3`-weighing schedule for labels `1,...,21`.
- I am not claiming anything about the full function `B(n)` beyond the exact `n = 21` instance.

## definitions
- For a column `c_j in {-1,0,1}^3`, entry `1` means coin `j` is on the left pan in that weighing, `-1` means right pan, and `0` means absent.
- For row `r`, write `x_r = sum_{j=1}^{21} M_{rj} j`. After normalization, `x_r >= 0`.
- If a transposition swaps labels `i < j`, the row-`r` total changes by
  `(j - i) (M_{ri} - M_{rj})`.
- Therefore an adjacent swap `(i,i+1)` changes the sign of a row with margin `x_r` exactly under the following local rules:
  - `x_r = 0`: iff `M_{ri} != M_{r,i+1}`;
  - `x_r = 1`: iff `M_{ri} < M_{r,i+1}`;
  - `x_r = 2`: iff `(M_{ri}, M_{r,i+1}) = (-1,1)`;
  - `x_r >= 3`: impossible.
- This sign convention matters: for a positive row, the only helpful adjacent move is an ascent `-1 -> 0`, `0 -> 1`, or `-1 -> 1`, because that moves the heavier coin toward the lighter side and decreases the row total.
- A necessary condition for verification is that every adjacent transposition `(i,i+1)` be detected by at least one row.
- Another necessary condition is that all `21` columns be distinct, since identical columns can be swapped with no effect on any weighing.

Self-check:
- I re-derived the transposition sign formula from scratch before using it.
- The local adjacent-swap rules are necessary conditions only; they are not a proof of verification.

## approach_A
Structural / invariant route: push the exact low-margin consequences of adjacent transpositions.

1. Any row with margin `>= 3` is invisible to every adjacent swap.
2. So every one of the `20` adjacent swaps must be certified by rows of margin `0`, `1`, or `2`.
3. With the corrected sign convention, a margin-`1` row certifies local ascents, not descents, and a margin-`2` row certifies only the sharp ascent `(-1,1)`.
4. I then asked how many adjacent pairs one row can certify at all, subject to the exact weighted-sum constraint `sum i a_i = m`.

Bounded exact calculation:
- For `n = 21`, a single row of margin `0` can certify at most `20` adjacent swaps.
- A single row of margin `1` can certify at most `13`.
- A single row of margin `2` can certify at most `9`.

What this shows:
- Row-by-row counting alone does not force a contradiction.
- In particular, one balanced row is flexible enough to certify all adjacent swaps by itself if all consecutive columns are distinct, so the adjacent-swap filter is weak in the all-balanced regime.

Self-check:
- These are exact maxima, not heuristics.
- They only address adjacent transpositions, so they cannot by themselves prove `B(21) != 3`.

## approach_B
Construction / contradiction route: build an explicit all-balanced fake candidate and exhibit a global multiswap symmetry that defeats it.

General template for odd length `2m+1`:
- If there are distinct nonzero vectors `v_1,...,v_m in {-1,0,1}^3` with
  `sum_{k=1}^m k v_k = 0`,
  then the symmetric placement
  `c_{m+1-k} = v_k`, `c_{m+1} = 0`, `c_{m+1+k} = -v_k`
  gives a `3 x (2m+1)` matrix with exact row sums `0`.
- The involution swapping each symmetric pair `(m+1-k, m+1+k)` changes the row-sum vector by
  `sum_{k=1}^m 2k (c_{m+1-k} - c_{m+1+k}) = 4 sum_{k=1}^m k v_k = 0`,
  so this matrix is never verifying.

For `m = 10`, one explicit choice is:
- `v_1  = (0,0,-1)`
- `v_2  = (-1,0,0)`
- `v_3  = (0,-1,0)`
- `v_4  = (1,-1,0)`
- `v_5  = (0,1,-1)`
- `v_6  = (-1,0,1)`
- `v_7  = (-1,-1,-1)`
- `v_8  = (-1,1,1)`
- `v_9  = (1,-1,1)`
- `v_10 = (1,1,-1)`

These are distinct and satisfy
- `sum k (v_k)_1 = (4 + 9 + 10) - (2 + 6 + 7 + 8) = 0`
- `sum k (v_k)_2 = (5 + 8 + 10) - (3 + 4 + 7 + 9) = 0`
- `sum k (v_k)_3 = (6 + 8 + 9) - (1 + 5 + 7 + 10) = 0`

So the concrete `21` columns
- `(1,1,-1), (1,-1,1), (-1,1,1), (-1,-1,-1), (-1,0,1), (0,1,-1), (1,-1,0), (0,-1,0), (-1,0,0), (0,0,-1), (0,0,0), (0,0,1), (1,0,0), (0,1,0), (-1,1,0), (0,-1,1), (1,0,-1), (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)`
have all three row sums equal to `0`.

Why this matters:
- All `21` columns are distinct, so every single transposition is detected by at least one balanced row.
- Nevertheless the nonidentity permutation
  `(1 21)(2 20)(3 19)(4 18)(5 17)(6 16)(7 15)(8 14)(9 13)(10 12)`
  preserves all three exact row sums, hence preserves the outcome vector `(0,0,0)`.
- So any proof or disproof of `B(21) = 3` must control global cancellation among several swaps, not just local adjacent behavior.

Self-check:
- The weighted-zero identities are explicit and easy to audit.
- This is a genuine falsifier for one tempting balanced family, not a proof about all `3 x 21` matrices.

## lemma_graph
1. Lemma 1: identical columns are forbidden.
2. Lemma 2: a transposition `(i,j)` changes row `r` by `(j-i)(M_{ri} - M_{rj})`.
3. Lemma 3: after orienting rows positively, adjacent certification depends only on margins `0`, `1`, `2`, with the corrected ascent rules above.
4. Lemma 4: rows of margin `>= 3` are useless for adjacent swaps.
5. Lemma 5: exact row-level maxima for adjacent certification at `n = 21` are `20`, `13`, and `9` for margins `0`, `1`, and `2`.
6. Lemma 6: in the all-balanced regime, distinct columns already guarantee detection of every single transposition, so the real obstruction is multiswap cancellation.
7. Lemma 7: the explicit symmetric `21`-column construction above has exact row sums `(0,0,0)` and a nontrivial preserving involution.
8. Gap: I still do not know whether every `3 x 21` schedule must admit such a global preserving permutation, or whether some non-balanced witness escapes all such cancellations.

## chosen_plan
Best path from the current no-web position:

1. Correct the local transposition algebra and push it to exact row-level bounds.
2. Test whether those bounds actually bite at `n = 21`.
3. If they do not, build or find one explicit `21`-column low-margin fake candidate to show what a future proof must defeat.

Outcome of that plan:
- Step 1 succeeded: the adjacent-swap rule is now sign-correct.
- Step 2 did not yield a contradiction: the exact row-level maxima are still too large.
- Step 3 succeeded in a useful but limited way: the explicit all-balanced symmetric family above shows that local transposition screening is far from sufficient.

Current mathematical position:
- I do not have a witness proving `B(21) = 3`.
- I do not have an impossibility theorem proving `B(21) != 3`.
- I do have a sharper diagnosis of the proof gap than in the nearby `n = 20` notes: the balanced case already contains large exact-zero fake candidates with a very structured preserving involution.

Self-check:
- The chosen path stayed reasoning-first.
- Lean remains off because there is no exact proof or exact disproof to formalize.

## self_checks
- Statement check: the target remained the exact claim `B(21) = 3`.
- Algebra check: I re-derived the transposition sign and corrected the local ascent/descent direction before using any bounded computation.
- Conservatism check: the explicit `21`-column matrix is used only as a falsifier for a tempting proof strategy, not as evidence for or against the exact statement by itself.
- Scope check: the only code used was one tiny DP for the row-level adjacent certification maxima.

## code_used
- Used one short exact dynamic program after the hand analysis was fixed.
- Computation: for a single row sequence `a_1,...,a_21 in {-1,0,1}` with exact weighted sum `sum i a_i = m`, maximize the number of adjacent positions certified under the corrected rules for `m = 0, 1, 2`.
- Output:
  - margin `0`: maximum `20`
  - margin `1`: maximum `13`
  - margin `2`: maximum `9`
- No generic search over all `3 x 21` schedules, no SAT/ILP/CP-SAT, and no Lean.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Current conclusion:
  - The low-margin adjacent-transposition route does not settle `B(21) = 3`.
  - A concrete all-balanced `21`-column fake family exists with exact row sums `(0,0,0)`, all columns distinct, and a nontrivial preserving involution.
  - Therefore any successful proof or disproof for the exact `n = 21` instance must use a stronger global invariant than single-transposition or adjacent-transposition screening.

## likely_failure_points
- The key gap is global: several individually detectable swaps can cancel vectorially across the three rows.
- The explicit fake family only rules out a tempting balanced normalization, not all possible witnesses with nonzero row margins.
- A genuine witness could use one or two non-balanced rows in a way that defeats the symmetric-cancellation pattern found here.
- The row-level DP bounds are exact but too coarse to control higher-order permutations.

## what_verify_should_check
- Recheck the transposition sign formula and confirm that the local margin-`1` and margin-`2` rules really use ascents, not descents.
- Re-run the tiny DP and confirm the exact maxima `20`, `13`, `9`.
- Audit the explicit vectors `v_1,...,v_10` and the derived `21` columns, verifying:
  - all columns are distinct;
  - all three weighted row sums are `0`;
  - the involution `(1 21)(2 20)...(10 12)` preserves those row sums.
- Decide whether the balanced symmetric fake family can be upgraded into a broader impossibility theorem, or whether verification should instead look for a genuinely non-balanced witness family.

## verify_rediscovery
- PASS 1 used a bounded web audit only, within budget, centered on the exact instance `B(21)`, the alternative name `Baron's omni-sequence`, the canonical Brand paper, and OEIS `A186313`.
- I found no source establishing the exact instance `B(21)=3` or `B(21)>3`.
- The public status material I found remained consistent with the canonical unresolved window `20 <= n <= 26`, with `3 <= B(n) <= 4` there.
- I did not find a later theorem, proposition, example, observation, corollary, or OEIS correction settling the exact `n=21` case.
- Rediscovery is therefore not established on this pass.

## verify_faithfulness
- The solve record is faithful about scope.
- It does not claim to have proved `B(21)=3` or `B(21)!=3`; it explicitly reports only a `PARTIAL` structural analysis.
- The matrix formulation in `statement_lock` matches the intended statement exactly: existence of a `3 x 21` schedule separating every nonidentity relabeling.
- The balanced `21`-column construction is presented only as a falsifier for one proof strategy, not as a solution to the intended statement. That is the correct claim type.
- I found no wrong-theorem drift, quantifier drift, or definition drift in the record itself.

## verify_proof
- There is no exact proof of the intended statement here to certify.
- For the claims that are actually made, I did not find an incorrect first step.
- I rechecked the critical local algebra: for a row with positive margin `x_r`, swapping adjacent labels `i,i+1` changes that row total by `(M_{ri}-M_{r,i+1})`, so the sign-change rules recorded for margins `0,1,2` are consistent.
- I reran the exact single-row dynamic program described in the record and confirmed the maxima:
  - margin `0`: `20`
  - margin `1`: `13`
  - margin `2`: `9`
- I also audited the explicit balanced family:
  - the `21` columns are pairwise distinct;
  - each weighted row sum is exactly `0`;
  - the involution `(1 21)(2 20)(3 19)(4 18)(5 17)(6 16)(7 15)(8 14)(9 13)(10 12)` preserves every row sum.
- The decisive gap is unchanged: none of this yields an exact witness for `B(21)=3` or an impossibility theorem for `B(21) != 3`.

## verify_adversarial
- I reran the only concrete computations recoverable from the record in a fresh shell.
- The DP outputs matched the record exactly: `20`, `13`, `9`.
- The explicit balanced construction survived adversarial checking: distinctness, exact zero row sums, and invariance under the stated involution all checked out.
- This adversarial pass therefore strengthens the obstruction example, but it does not advance the main claim beyond `PARTIAL`.
- I found no candidate witness, no counterexample to the intended existence claim, and no computation that closes the global multiswap gap.

## verify_verdict
- `UNVERIFIED`
- Classification remains `PARTIAL`.
- Reason: the record contains a correct-looking partial analysis and a verified obstruction example, but no exact proof or disproof of `B(21)=3`.
- `lean_ready = false` because there is nothing exact to formalize yet, and PASS 1 did not establish rediscovery either.

## minimal_repair_if_any
- No repair applied.
- The record already classifies itself conservatively as `PARTIAL`.
- The only necessary verifier action was to keep the run away from any stronger label such as `CANDIDATE` or `EXACT`.
