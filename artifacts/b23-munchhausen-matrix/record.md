# b23-munchhausen-matrix

## statement_lock
- Active slug: `b23-munchhausen-matrix`
- Title: `Does Baron Munchhausen's omni-sequence satisfy B(23)=3?`
- Locked intended statement: `B(23) = 3.`
- Working formulation: there exists a `3 x 23` ternary matrix `M` with entries in `{-1,0,1}` such that, for the weight vector `w = (1,2,...,23)^T`, every nonidentity permutation of the labels changes at least one of the three balance outcomes `sign(Mw)`.
- Solve-stage normalization: I may flip the sign of any row, so every nonzero row margin may be assumed positive.

Self-check:
- The target is exactly the existence of one certifying `3`-weighing scheme for labels `1,...,23`.
- I am not upgrading any partial obstruction into a statement about the full sequence beyond the exact `n = 23` instance.

## definitions
- For a column `c_j in {-1,0,1}^3`, entry `1` means coin `j` is on the left pan in that weighing, `-1` means right pan, and `0` means absent.
- For row `r`, write `x_r = sum_{j=1}^{23} M_{rj} j`. After normalization, `x_r >= 0`.
- If a transposition swaps labels `i < j`, the row-`r` total changes by
  `(j - i) (M_{ri} - M_{rj})`.
- Therefore an adjacent swap `(i,i+1)` changes the sign of a row with margin `x_r` exactly under these local rules:
  - `x_r = 0`: iff `M_{ri} != M_{r,i+1}`;
  - `x_r = 1`: iff `M_{ri} < M_{r,i+1}`;
  - `x_r = 2`: iff `(M_{ri}, M_{r,i+1}) = (-1,1)`;
  - `x_r >= 3`: impossible.
- So every adjacent transposition must be detected by at least one row of margin `0`, `1`, or `2`.
- Another necessary condition is that all `23` columns be distinct, since identical columns can be swapped with no effect on any weighing.
- In the special all-balanced case `Mw = 0`, any single transposition between distinct columns is automatically detected, because some row total changes from `0` to a nonzero integer. The real danger there is cancellation among several swaps.

Self-check:
- I re-derived the transposition formula before using it.
- The adjacent-swap rules are only necessary conditions, not a verification criterion.

## approach_A
Structural / invariant route: push the exact low-margin consequences of adjacent transpositions.

1. Any row with margin `>= 3` is invisible to every adjacent swap.
2. So all `22` adjacent swaps must be covered by rows with margins `0`, `1`, or `2`.
3. For a fixed row, this becomes a finite path problem on `{-1,0,1}` with the exact weighted-sum constraint `sum i a_i = m`.
4. The immediate question is whether the exact single-row maxima at `n = 23` are small enough to force a contradiction.

Expectation before code:
- This route was too weak at `n = 21` and `n = 22`.
- I still need to check whether odd `23` behaves differently enough to make the row-level bounds bite.

Bounded exact calculation:
- margin `0`: maximum `22`
- margin `1`: maximum `15`
- margin `2`: maximum `11`

What this shows:
- Row-by-row adjacent coverage still does not force a contradiction.
- In particular, one balanced row can again certify all adjacent swaps by itself, so the local adjacent-transposition filter remains too weak.
- Any impossibility proof for `B(23) != 3` must use a more global invariant than rowwise adjacent coverage.

Self-check:
- These are exact maxima for the stated single-row problem, not heuristics.
- They do not imply the existence of a certifying `3 x 23` witness.

## approach_B
Construction / extremal / contradiction route: test whether the odd symmetric all-balanced fake-candidate template exists at `n = 23`.

General odd template for `n = 2m+1`:
- If there are distinct nonzero vectors `v_1,...,v_m in {-1,0,1}^3` with
  `sum_{k=1}^m k v_k = 0`,
  then the symmetric placement
  `c_{m+1-k} = v_k`, `c_{m+1} = 0`, `c_{m+1+k} = -v_k`
  gives a `3 x (2m+1)` matrix with exact row sums `0`.
- The involution swapping each symmetric pair `(m+1-k, m+1+k)` preserves every row sum because the total change is
  `4 sum_{k=1}^m k v_k = 0`.

For `n = 23`, this becomes:
- find `11` distinct nonzero ternary vectors with
  `1 v_1 + 2 v_2 + ... + 11 v_11 = 0`.

Why this route matters:
- If such a family exists, then the clean odd balanced obstruction from `n = 21` survives at `n = 23`.
- That would not disprove `B(23)=3`, but it would show again that local transposition checking is far from enough and that the balanced regime contains explicit multiswap cancellations.

Explicit weighted-zero solution:
- A valid choice is
  - `v_1  = (1,-1,0)`
  - `v_2  = (0,-1,1)`
  - `v_3  = (-1,0,1)`
  - `v_4  = (-1,-1,1)`
  - `v_5  = (0,-1,-1)`
  - `v_6  = (-1,-1,-1)`
  - `v_7  = (-1,0,-1)`
  - `v_8  = (1,1,0)`
  - `v_9  = (0,0,1)`
  - `v_10 = (0,1,0)`
  - `v_11 = (1,0,0)`
- These are distinct and satisfy
  - `sum k (v_k)_1 = (1 + 8 + 11) - (3 + 4 + 6 + 7) = 0`
  - `sum k (v_k)_2 = (8 + 10) - (1 + 2 + 4 + 5 + 6) = 0`
  - `sum k (v_k)_3 = (2 + 3 + 4 + 9) - (5 + 6 + 7) = 0`

Therefore the `23` columns
- `(1,0,0), (0,1,0), (0,0,1), (1,1,0), (-1,0,-1), (-1,-1,-1), (0,-1,-1), (-1,-1,1), (-1,0,1), (0,-1,1), (1,-1,0), (0,0,0), (-1,1,0), (0,1,-1), (1,0,-1), (1,1,-1), (0,1,1), (1,1,1), (1,0,1), (-1,-1,0), (0,0,-1), (0,-1,0), (-1,0,0)`
are pairwise distinct and have exact row sums `(0,0,0)`.

Preserving involution:
- The nonidentity permutation
  `(1 23)(2 22)(3 21)(4 20)(5 19)(6 18)(7 17)(8 16)(9 15)(10 14)(11 13)`
  preserves all three row sums, because each swapped pair is symmetric around the center and the total change is `4 sum_{k=1}^{11} k v_k = 0`.

Interpretation:
- The clean odd balanced obstruction from `n = 21` survives intact at `n = 23`.
- So the all-balanced regime again contains explicit full-distinctness fake candidates with global multiswap cancellation.
- This still does not prove `B(23) != 3`; it only rules out a tempting proof strategy and shows that balanced matrices are not automatically safe.

Self-check:
- The weighted-zero identities are explicit and easy to audit.
- This is a genuine falsifier for one large balanced family, not a proof about all `3 x 23` matrices.

## lemma_graph
1. Lemma 1: identical columns are forbidden.
2. Lemma 2: a transposition `(i,j)` changes row `r` by `(j-i)(M_{ri} - M_{rj})`.
3. Lemma 3: after orienting rows positively, adjacent certification depends only on margins `0`, `1`, and `2`, with the local rules above.
4. Lemma 4: rows of margin `>= 3` are useless for adjacent swaps.
5. Lemma 5: exact single-row adjacent-coverage maxima at `n = 23` are `22`, `15`, and `11` for margins `0`, `1`, and `2`.
6. Lemma 6: in the all-balanced regime, distinct columns already detect every single transposition, so the real obstruction is multiswap cancellation.
7. Lemma 7: the explicit weighted-zero identity above produces a balanced `23`-column matrix with all columns distinct.
8. Lemma 8: the symmetric involution swapping each opposite pair preserves all three row sums in that matrix.
9. Gap: I still do not know whether every `3 x 23` schedule fails, or whether some genuinely non-balanced witness exists.

## chosen_plan
Best path from the current no-web position:

1. Reuse the exact adjacent-swap algebra and see whether `n = 23` changes the row-level obstruction.
2. Test the odd symmetric balanced family, because it is the cleanest way to expose multiswap cancellation at `n = 23`.
3. Stop once I have either an exact proof/disproof or a sharply delimited gap with only minimal bounded computations supporting it.

Outcome of that plan:
- Step 1 did not yield a contradiction: the exact row-level maxima `22,15,11` are still too large.
- Step 2 succeeded: the odd symmetric balanced obstruction exists explicitly at `n = 23`.
- I still do not have a certifying `3 x 23` witness, and I still do not have a full impossibility theorem.

Current mathematical position:
- The local adjacent-transposition bottleneck is again too weak to disprove `B(23) = 3`.
- The all-balanced regime already contains explicit full-distinctness fake candidates with a nontrivial preserving involution.
- So the unresolved space narrows to the same two global possibilities as in nearby cases:
  - a broader impossibility theorem controlling every `3 x 23` schedule, or
  - a genuinely non-balanced witness that escapes the balanced cancellation pattern.

Self-check:
- This plan stayed reasoning-first.
- The bounded computations were introduced only after the two handwritten routes were pinned down.
- Lean remains off because there is no exact proof or exact disproof in hand.

## self_checks
- Statement check: the target remains the exact claim `B(23) = 3`.
- Scope check: the adjacent-swap analysis is only a necessary-condition route.
- Algebra check: the local sign-change rules still use ascents for margins `1` and `2`, consistent with the transposition formula.
- Conservatism check: the explicit `23`-column balanced family only falsifies a tempting strategy; it does not settle the intended statement.
- Scope check: the only code used was one exact single-row DP and one structured weighted-zero search in the symmetric balanced family.

## code_used
- Used two short Python computations, both directly tied to the handwritten reasoning.
- Computation 1: exact dynamic program for a single row `a_1,...,a_23 in {-1,0,1}` with prescribed margin `m`, maximizing adjacent certifications.
  - output `22` for `m = 0`
  - output `15` for `m = 1`
  - output `11` for `m = 2`
- Computation 2: a bounded depth-first search over the odd symmetric template, looking for `11` distinct nonzero ternary directions with
  `1 v_1 + 2 v_2 + ... + 11 v_11 = 0`.
  - output: one explicit solution, giving the `23`-column balanced family displayed above
- No generic brute-force search over all `3 x 23` schemes, no SAT/ILP/CP-SAT, and no Lean.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Current conclusion:
  - I have no proof of `B(23) = 3`.
  - I have no proof of `B(23) != 3`.
  - The usual local adjacent-transposition obstruction is still too weak.
  - The odd all-balanced symmetric obstruction already exists explicitly at `n = 23`, so any exact proof or disproof must control global multiswap cancellation and probably also the non-balanced regime.

## likely_failure_points
- The local adjacent-transposition route may again be too coarse to control higher-order permutations.
- The symmetric balanced obstruction rules out one large family of fake candidates rather than all `3 x 23` schedules.
- A true witness, if it exists, may require nonzero row margins and asymmetry that are invisible to the current balanced template.
- Conversely, a full impossibility theorem may need a genuinely global invariant that survives beyond adjacent coverage and beyond this symmetric family.

## what_verify_should_check
- Recheck the transposition formula and adjacent-swap rules for margins `0`, `1`, and `2`.
- Re-run the single-row DP and confirm the exact maxima `22`, `15`, `11`.
- Audit the explicit vectors `v_1,...,v_11` and the derived `23` columns, verifying:
  - all columns are distinct;
  - all three weighted row sums are `0`;
  - the involution `(1 23)(2 22)...(11 13)` preserves those row sums.
- Confirm that the final classification stays conservative: this should remain `PARTIAL`, not `COUNTEREXAMPLE` or `EXACT`.

## verify_rediscovery
- PASS 1 used a bounded web audit centered on the exact instance `B(23)`, the alternate names `Baron Munchhausen` and `Baron's omni-sequence`, the canonical OEIS source `A186313`, Brand's 2012 papers, and a source-internal check for any theorem / proposition / example / observation / corollary already settling the exact `n = 23` case.
- Within that budget, I did not find any paper, OEIS update, or source-internal statement proving `B(23) = 3` or `B(23) > 3`.
- The live canonical status I found is still consistent with the selected problem: OEIS `A186313` continues to state `3 <= a(n) <= 4` for `20 <= n <= 26`, and the linked Brand references remain the same family-level sources rather than an exact later resolution of `n = 23`.
- I therefore do not have evidence that the exact intended statement is already solved, directly implied, or explicitly exhibited in the existing literature checked in PASS 1.
- Rediscovery is not established on this pass.

## verify_faithfulness
- The solve record is faithful about claim scope.
- It does not claim to prove the intended statement `B(23) = 3` or its negation. It explicitly classifies the run as `PARTIAL`.
- The `statement_lock` formulation matches the intended statement exactly: existence of one certifying `3 x 23` ternary weighing matrix separating every nonidentity relabeling.
- The balanced symmetric construction is described only as an explicit obstruction to one tempting proof strategy, not as an exact counterexample to all `3 x 23` schemes. That is the correct claim type.
- I found no wrong-theorem drift, quantifier drift, or definition drift in the current record.

## verify_proof
- There is no claimed exact proof of `B(23) = 3` or `B(23) != 3` here to certify.
- For the claims actually made, I found no incorrect first step.
- I rechecked the transposition algebra: swapping labels `i < j` changes row `r` by `(j-i)(M_{ri} - M_{rj})`, and after orienting rows to nonnegative margin, the adjacent-swap sign-change rules recorded for margins `0`, `1`, and `2` are correct.
- I reran the exact single-row dynamic program from scratch and confirmed the recorded maxima:
  - margin `0`: `22`
  - margin `1`: `15`
  - margin `2`: `11`
- I also independently audited the explicit weighted-zero family `v_1,...,v_11`. The weighted coordinate sums are all `0`, the resulting `23` columns are pairwise distinct, all three weighted row sums are `0`, and the involution `(1 23)(2 22)...(11 13)` preserves those row sums.
- The decisive proof gap is unchanged: these verified claims still do not prove the intended existence statement, and they also do not prove impossibility for all `3 x 23` schemes.

## verify_adversarial
- There was no saved checker file in the artifact, so I reran the two recoverable computations independently in a fresh shell.
- The single-row dynamic-program outputs matched the record exactly: `22`, `15`, `11`.
- The explicit balanced-family audit also matched the record exactly:
  - weighted-zero identities hold in all three coordinates;
  - the derived `23` columns are all distinct;
  - the original weighted row sums are `(0,0,0)`;
  - after the nonidentity involution `(1 23)(2 22)...(11 13)`, the weighted row sums remain `(0,0,0)`.
- This adversarial pass confirms the displayed balanced fake candidate really does preserve the three outcomes, but only for that family. It does not close the global gap for arbitrary non-balanced schedules.

## verify_verdict
- `UNVERIFIED`
- Classification remains `PARTIAL`.
- Reason: PASS 1 did not establish rediscovery, but PASS 2 through PASS 4 also did not produce an exact proof or exact disproof of `B(23) = 3`. The current record contains correct-looking partial analysis and reproducible bounded computations only.
- `lean_ready = false` because there is still no frontier-novel exact statement strong enough to formalize.

## minimal_repair_if_any
- No repair applied.
- The solve record already uses the conservative label `PARTIAL`, and verification should keep it away from stronger labels such as `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.
