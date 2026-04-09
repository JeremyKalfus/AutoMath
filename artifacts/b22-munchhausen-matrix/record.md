# b22-munchhausen-matrix

## statement_lock
- Active slug: `b22-munchhausen-matrix`
- Title: `Does Baron Munchhausen's omni-sequence satisfy B(22)=3?`
- Locked intended statement: `B(22) = 3.`
- Working formulation: there exists a `3 x 22` ternary matrix `M` with entries in `{-1,0,1}` such that, for the weight vector `w = (1,2,...,22)^T`, every nonidentity permutation of the labels changes at least one of the three balance outcomes `sign(Mw)`.
- Solve-stage normalization: I may flip the sign of any row, so every nonzero row margin may be assumed positive.

Self-check:
- The target is exactly the existence of one certifying `3`-weighing scheme for labels `1,...,22`.
- I am not upgrading any partial obstruction into a claim about the full function `B(n)` beyond the exact `n = 22` instance.

## definitions
- For a column `c_j in {-1,0,1}^3`, entry `1` means coin `j` is on the left pan in that weighing, `-1` means right pan, and `0` means absent.
- For row `r`, write `x_r = sum_{j=1}^{22} M_{rj} j`. After normalization, `x_r >= 0`.
- If a transposition swaps labels `i < j`, the row-`r` total changes by
  `(j - i) (M_{ri} - M_{rj})`.
- Therefore an adjacent swap `(i,i+1)` changes the sign of a row with margin `x_r` exactly under these local rules:
  - `x_r = 0`: iff `M_{ri} != M_{r,i+1}`;
  - `x_r = 1`: iff `M_{ri} < M_{r,i+1}`;
  - `x_r = 2`: iff `(M_{ri}, M_{r,i+1}) = (-1,1)`;
  - `x_r >= 3`: impossible.
- So every adjacent transposition must be detected by at least one row of margin `0`, `1`, or `2`.
- Another necessary condition is that all `22` columns be distinct, since identical columns can be swapped with no effect on any weighing.
- In the special all-balanced case `Mw = 0`, any single transposition between distinct columns is automatically detected, because some row total changes from `0` to a nonzero integer. The real danger there is cancellation among several swaps.

Self-check:
- I re-derived the transposition formula before using it.
- The adjacent-swap rules are used only as necessary conditions, not as a verification criterion.

## approach_A
Structural / invariant route: push the exact low-margin consequences of adjacent transpositions.

1. Any row with margin `>= 3` is invisible to every adjacent swap.
2. So all `21` adjacent swaps must be covered by rows with margins `0`, `1`, or `2`.
3. For a fixed row, this becomes a finite path problem on `{-1,0,1}` with the exact weighted-sum constraint `sum i a_i = m`.
4. I then computed the exact maximum number of adjacent pairs a single row can certify at `n = 22`.

Bounded exact calculation:
- margin `0`: maximum `21`
- margin `1`: maximum `14`
- margin `2`: maximum `10`

What this shows:
- Row-by-row counting does not force a contradiction.
- In particular, one balanced row can certify all `21` adjacent swaps by itself, so the adjacent-transposition filter is again too weak to settle the instance.
- Any impossibility proof for `B(22) != 3` must use a more global invariant than local adjacent coverage.

Self-check:
- These are exact maxima for the stated single-row problem, not heuristics.
- They do not imply existence of a `3 x 22` witness, only that the naive local obstruction is insufficient.

## approach_B
Construction / extremal / contradiction route: test whether the explicit all-balanced opposite-pair obstruction from the nearby odd case extends to `n = 22`.

Natural even-`22` template:
- Put columns in opposite pairs around the midpoint:
  `c_k = v_k`, `c_{23-k} = -v_k` for `k = 1,...,11`,
  where the `v_k` are chosen from distinct nonzero directions in `{-1,0,1}^3`.
- Then the row-sum vector is
  `sum_{k=1}^{11} (2k - 23) v_k`,
  so all three rows are balanced exactly when
  `sum_{k=1}^{11} (23 - 2k) v_k = 0`.
- Under that same condition, the involution
  `(1 22)(2 21)...(11 12)`
  preserves all three row sums, so any such matrix would be a concrete non-verifying fake candidate.

Exact bounded search in that restricted family:
- I exhaustively checked all choices of `11` distinct directions from the `13` opposite-pair classes of nonzero ternary vectors, together with all `2^11` sign choices.
- No solution exists to
  `21 v_1 + 19 v_2 + ... + 3 v_10 + 1 v_11 = 0`
  in that family.

Interpretation:
- The clean symmetric all-balanced obstruction used for `n = 21` does not extend verbatim to `n = 22`.
- That makes the even case look structurally different: the simplest global cancellation family disappears.
- But this still does not prove `B(22) = 3`; it only removes one tempting fake-candidate mechanism.

Self-check:
- The search here is exact, but only for one sharply defined opposite-pair template.
- I am not claiming that all balanced `3 x 22` matrices avoid multiswap cancellations, only that this obvious symmetric family does.

## lemma_graph
1. Lemma 1: identical columns are forbidden.
2. Lemma 2: a transposition `(i,j)` changes row `r` by `(j-i)(M_{ri} - M_{rj})`.
3. Lemma 3: after orienting rows positively, adjacent certification depends only on margins `0`, `1`, `2`, with the local rules above.
4. Lemma 4: rows of margin `>= 3` are useless for adjacent swaps.
5. Lemma 5: at `n = 22`, exact single-row adjacent-coverage maxima are `21`, `14`, and `10` for margins `0`, `1`, and `2`.
6. Lemma 6: in the all-balanced regime, distinct columns already detect every single transposition, so the real obstruction is multiswap cancellation.
7. Lemma 7: the most obvious even opposite-pair balanced involution template would require a weighted-zero identity
   `21 v_1 + 19 v_2 + ... + 1 v_11 = 0`
   among `11` distinct ternary directions.
8. Lemma 8: that restricted template has no solution.
9. Gap: I still do not know whether every `3 x 22` schedule fails, or whether some genuinely non-balanced witness exists.

## chosen_plan
Best path from the current no-web position:

1. Use the low-margin adjacent-swap algebra to see whether a clean impossibility argument is available.
2. If not, test whether the strongest fake family from `n = 21` survives in the even `22` case.
3. Stop once I have either an exact proof/disproof or a sharply delimited gap.

Outcome of that plan:
- Step 1 did not yield a contradiction: the exact row-level maxima `21,14,10` are too large.
- Step 2 produced a meaningful difference from the nearby odd case: the straightforward opposite-pair all-balanced obstruction does not exist for `n = 22`.
- I still do not have a certifying `3 x 22` witness, and I still do not have a global impossibility theorem.

Current mathematical position:
- The usual local adjacent-transposition bottleneck is not enough to disprove `B(22) = 3`.
- The cleanest explicit balanced cancellation template from `n = 21` is absent at `n = 22`.
- So the unresolved space has narrowed to two plausible directions:
  - a broader multiswap obstruction not captured by the symmetric template, or
  - a genuinely non-balanced `3`-weighing witness.

Self-check:
- This plan stayed reasoning-first.
- The bounded computations were introduced only after the two handwritten routes had clear, sharply stated gaps.
- Lean remains off because there is no exact proof or exact disproof in hand.

## self_checks
- Statement check: the target remained the exact claim `B(22) = 3`.
- Algebra check: the adjacent-swap sign rule uses ascents for margins `1` and `2`, matching the transposition formula.
- Scope check: the only code used was a single-row exact DP and one restricted opposite-pair family search.
- Conservatism check: failure of the symmetric template is not being misreported as evidence that a full witness exists.

## code_used
- Used two short Python computations, both directly tied to the handwritten reasoning.
- Computation 1: exact dynamic program for a single row `a_1,...,a_22 in {-1,0,1}` with prescribed margin `m`, maximizing adjacent certifications.
  - output `21` for `m = 0`
  - output `14` for `m = 1`
  - output `10` for `m = 2`
- Computation 2: exhaustive search over the restricted all-balanced opposite-pair template
  `c_k = v_k`, `c_{23-k} = -v_k`
  with `11` distinct ternary directions, checking whether
  `21 v_1 + 19 v_2 + ... + 1 v_11 = 0`.
  - output: no solution in that family
- No generic brute-force search over all `3 x 22` schemes, no SAT/ILP/CP-SAT, and no Lean.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Current conclusion:
  - I have no proof of `B(22) = 3`.
  - I have no proof of `B(22) != 3`.
  - The low-margin local obstruction is too weak, but the easiest explicit global balanced obstruction from `n = 21` does not carry over to `n = 22`.
  - The exact instance remains open from this solve-stage pass.

## likely_failure_points
- The single-row adjacency bounds are exact but still too coarse to control higher-order permutations.
- The opposite-pair template search only rules out one symmetric cancellation mechanism; a different balanced fake family may still exist.
- A true witness, if it exists, may require carefully chosen nonzero margins rather than the all-balanced regimes that were easiest to analyze.
- Conversely, a full impossibility theorem may need a global permutation invariant that is invisible to the current local analysis.

## what_verify_should_check
- Recheck the transposition formula and the adjacent-swap rules for margins `0`, `1`, and `2`.
- Re-run the single-row DP and confirm the exact maxima `21`, `14`, `10`.
- Re-run the restricted opposite-pair template search and confirm that no weighted-zero solution exists there.
- Check that the solve writeup does not overclaim from the negative template search: it should remain `PARTIAL`, not `CANDIDATE` or `COUNTEREXAMPLE`.
- Decide whether verification can either enlarge the balanced-obstruction search in a principled way or find a concrete non-balanced witness route worth testing later.

## verify_rediscovery
- PASS 1 used a bounded web audit only, within budget, centered on the exact instance `B(22)`, the alternate names `Baron Munchhausen` and `Baron's omni-sequence`, the canonical OEIS source `A186313`, Brand's 2012 paper, and source-internal theorem/proposition/example/corollary checks aimed at the same family.
- I did not find a source establishing the exact instance `B(22)=3` or `B(22)>3`.
- The live status material located in PASS 1 remained consistent with the canonical unresolved window `20 <= n <= 26`, with `3 <= B(n) <= 4` there.
- I did not find a later theorem, proposition, example, observation, corollary, or OEIS correction that settles the exact `n = 22` case directly or by immediate implication.
- Rediscovery is therefore not established on this pass.

## verify_faithfulness
- The solve record is faithful about scope.
- It does not claim to prove `B(22)=3` or `B(22)!=3`; it explicitly reports only a `PARTIAL` structural analysis.
- The matrix formulation in `statement_lock` matches the intended statement exactly: existence of a `3 x 22` schedule separating every nonidentity relabeling.
- The restricted opposite-pair computation is presented only as a falsifier for one symmetric fake-candidate mechanism, not as a solution to the intended statement. That is the correct claim type.
- I found no wrong-theorem drift, quantifier drift, or definition drift in the record itself.

## verify_proof
- There is no exact proof of the intended statement here to certify.
- For the claims that are actually made, I did not find an incorrect first step.
- I rechecked the key algebra: swapping labels `i < j` changes row `r` by `(j-i)(M_{ri} - M_{rj})`, and for adjacent swaps the sign-change rules recorded for row margins `0`, `1`, and `2` follow correctly after orienting each row to nonnegative margin.
- I reran the exact single-row dynamic program described in the record and confirmed the maxima:
  - margin `0`: `21`
  - margin `1`: `14`
  - margin `2`: `10`
- I also reran the restricted all-balanced opposite-pair search over `11` distinct ternary directions and all `2^11` sign choices, and confirmed that there is no solution to the weighted-zero identity `21 v_1 + 19 v_2 + ... + 1 v_11 = 0` in that family.
- The decisive gap is unchanged: none of this yields an exact witness for `B(22)=3` or an impossibility theorem for `B(22) != 3`.

## verify_adversarial
- I reran the only concrete computations recoverable from the record in a fresh shell.
- The dynamic-program outputs matched the record exactly: `21`, `14`, `10`.
- The restricted opposite-pair exhaustive search also matched the record exactly: it checked `159744` assignments and found no weighted-zero balanced template in that family.
- This adversarial pass therefore strengthens the negative evidence against that one symmetric obstruction route, but it does not advance the main claim beyond `PARTIAL`.
- I found no candidate witness, no exact counterexample to the intended existence claim, and no computation that closes the global multiswap gap.

## verify_verdict
- `UNVERIFIED`
- Classification remains `PARTIAL`.
- Reason: the record contains correct-looking partial analysis and verified bounded computations, but no exact proof or exact disproof of `B(22)=3`.
- `lean_ready = false` because there is nothing exact to formalize yet, and PASS 1 did not establish rediscovery either.

## minimal_repair_if_any
- No repair applied.
- The record already classifies itself conservatively as `PARTIAL`.
- The necessary verifier action was to keep the run away from any stronger label such as `CANDIDATE` or `EXACT`.
