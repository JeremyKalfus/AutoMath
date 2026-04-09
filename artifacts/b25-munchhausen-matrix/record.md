# b25-munchhausen-matrix

## statement_lock
- Active slug: `b25-munchhausen-matrix`
- Title: `Does Baron Munchhausen's omni-sequence satisfy B(25)=3?`
- Locked intended statement: `B(25) = 3.`
- Working formulation: there exists a `3 x 25` ternary matrix `M` with entries in `{-1,0,1}` such that, for the weight vector `w = (1,2,...,25)^T`, every nonidentity permutation of the labels changes at least one of the three balance outcomes `sign(Mw)`.
- Solve-stage normalization: I may flip the sign of any row, so every nonzero row margin may be assumed positive.

Self-check:
- The target is exactly one certifying `3`-weighing schedule for labels `1,...,25`.
- I am treating `B(25)=3` as an existence claim for one verifying matrix, not as a universal statement about all `3 x 25` ternary matrices.

## definitions
- For a column `c_j in {-1,0,1}^3`, entry `1` means coin `j` is on the left pan in that weighing, `-1` means right pan, and `0` means absent.
- For row `r`, write `x_r = sum_{j=1}^{25} M_{rj} j`. After normalization, `x_r >= 0`.
- If a transposition swaps labels `i < j`, the row-`r` total changes by
  `(j - i)(M_{ri} - M_{rj})`.
- Therefore an adjacent swap `(i,i+1)` changes the sign of a row with margin `x_r` exactly under these local rules:
  - `x_r = 0`: iff `M_{ri} != M_{r,i+1}`;
  - `x_r = 1`: iff `M_{ri} < M_{r,i+1}`;
  - `x_r = 2`: iff `(M_{ri}, M_{r,i+1}) = (-1,1)`;
  - `x_r >= 3`: impossible.
- So every adjacent transposition must be detected by at least one row of margin `0`, `1`, or `2`.
- Another necessary condition is that all `25` columns be distinct, since identical columns can be swapped with no effect on any weighing.
- Because there are only `27` ternary column types in total, any distinct-column `3 x 25` matrix omits exactly two of them. That makes the problem extremely close to the full ternary cube.
- In the special all-balanced case `Mw = 0`, any single transposition between distinct columns is automatically detected. The real danger there is cancellation among several swaps.

Self-check:
- I re-derived the transposition formula before using it.
- The adjacent-swap rules are necessary conditions only, not a proof of verification.

## approach_A
Structural / invariant route: push the exact low-margin consequences of adjacent transpositions and ask whether the near-full-cube regime forces a contradiction.

1. Any row with margin `>= 3` is invisible to every adjacent swap.
2. So all `24` adjacent swaps must be covered by rows with margins `0`, `1`, or `2`.
3. For a fixed row, this becomes a finite path problem on `{-1,0,1}` with the exact weighted-sum constraint `sum i a_i = m`.
4. If the exact single-row maxima at `n = 25` are still large, then the local adjacent-transposition route will again be too weak by itself.
5. The extra `n = 25` feature is combinatorial scarcity: with `25` distinct columns out of `27`, the matrix is almost the whole ternary cube. If this helps, it should appear as a global cancellation obstruction rather than a row-by-row adjacent one.

Expectation before code:
- The nearby `n = 21,22,23,24` cases all showed that local adjacent coverage is too weak.
- I still need to check the exact row-level bounds at `n = 25` rather than assume they follow the same pattern.

Bounded exact calculation:
- margin `0`: maximum `24`
- margin `1`: maximum `16`
- margin `2`: maximum `11`

What this shows:
- Row-by-row adjacent coverage still does not force a contradiction.
- In particular, one balanced row can again certify all `24` adjacent swaps by itself, so the local adjacent-transposition filter remains too weak.
- The near-full-cube feature `25 of 27` does not show up at this rowwise level at all. If it matters, it must matter through a genuinely global cancellation invariant.

Self-check:
- These are exact maxima for the stated single-row problem, not heuristics.
- I still do not have a clean argument turning “only two column types are omitted” into a global impossibility theorem.

## approach_B
Construction / extremal / contradiction route: test the natural odd symmetric balanced fake-candidate family at `n = 25`.

General odd template for `n = 2m+1`:
- If there are distinct nonzero vectors `v_1,...,v_m in {-1,0,1}^3` with
  `sum_{k=1}^m k v_k = 0`,
  then the symmetric placement
  `c_{m+1-k} = v_k`, `c_{m+1} = 0`, `c_{m+1+k} = -v_k`
  gives a `3 x (2m+1)` matrix with exact row sums `0`.
- The involution swapping each symmetric pair `(m+1-k, m+1+k)` preserves every row sum because the total change is
  `4 sum_{k=1}^m k v_k = 0`.

For `n = 25`, this becomes:
- find `12` distinct nonzero ternary vectors with
  `1 v_1 + 2 v_2 + ... + 12 v_12 = 0`.

Why this route matters:
- If such a family exists, then the odd balanced obstruction seen at `n = 21` and `n = 23` survives again at `n = 25`.
- That would not disprove `B(25)=3`, but it would show that the almost-full-cube balanced regime already contains explicit non-verifying `25`-column schedules with all columns distinct.

Hand diagnosis before code:
- This is a sharply defined weighted-zero problem on only `13` opposite-pair classes of nonzero ternary vectors.
- It is the right first bounded experiment if the handwritten structural analysis stalls, because it probes a very specific global cancellation mechanism rather than brute-forcing all `3 x 25` matrices.

Explicit weighted-zero solution:
- A valid choice is
  - `v_1  = (0,-1,1)`
  - `v_2  = (1,1,-1)`
  - `v_3  = (-1,1,0)`
  - `v_4  = (-1,-1,-1)`
  - `v_5  = (1,-1,1)`
  - `v_6  = (0,1,1)`
  - `v_7  = (1,0,-1)`
  - `v_8  = (-1,0,-1)`
  - `v_9  = (0,0,1)`
  - `v_10 = (0,1,0)`
  - `v_11 = (-1,-1,0)`
  - `v_12 = (1,0,0)`
- These are pairwise from distinct opposite-pair classes and satisfy
  - `sum k (v_k)_1 = (2 + 5 + 7 + 12) - (3 + 4 + 8 + 11) = 0`
  - `sum k (v_k)_2 = (2 + 3 + 6 + 10) - (1 + 4 + 5 + 11) = 0`
  - `sum k (v_k)_3 = (1 + 5 + 6 + 9) - (2 + 4 + 7 + 8) = 0`

Therefore the `25` columns
- `(1,0,0), (-1,-1,0), (0,1,0), (0,0,1), (-1,0,-1), (1,0,-1), (0,1,1), (1,-1,1), (-1,-1,-1), (-1,1,0), (1,1,-1), (0,-1,1), (0,0,0), (0,1,-1), (-1,-1,1), (1,-1,0), (1,1,1), (-1,1,-1), (0,-1,-1), (-1,0,1), (1,0,1), (0,0,-1), (0,-1,0), (1,1,0), (-1,0,0)`
are pairwise distinct and have exact row sums `(0,0,0)`.

Preserving involution:
- The nonidentity permutation
  `(1 25)(2 24)(3 23)(4 22)(5 21)(6 20)(7 19)(8 18)(9 17)(10 16)(11 15)(12 14)`
  preserves all three row sums, because each swapped pair is symmetric around the center and the total change is
  `4 sum_{k=1}^{12} k v_k = 0`.

Interpretation:
- The odd balanced obstruction from `n = 21` and `n = 23` survives again at `n = 25`.
- So even in this near-full-cube regime, there are explicit all-balanced `25`-column fake candidates with all columns distinct and a nontrivial preserving involution.
- This still does not prove `B(25) != 3`; it only rules out a tempting proof strategy and shows that balanced matrices are not automatically safe.

Self-check:
- The weighted-zero identities are explicit and easy to audit.
- This is a genuine falsifier for one large balanced family, not a proof about all `3 x 25` matrices.

## lemma_graph
1. Lemma 1: identical columns are forbidden.
2. Lemma 2: a transposition `(i,j)` changes row `r` by `(j-i)(M_{ri} - M_{rj})`.
3. Lemma 3: after orienting rows positively, adjacent certification depends only on margins `0`, `1`, and `2`, with the local rules above.
4. Lemma 4: rows of margin `>= 3` are useless for adjacent swaps.
5. Lemma 5: therefore any witness must cover all `24` adjacent swaps using only low-margin rows.
6. Lemma 6: in the all-balanced regime, distinct columns already detect every single transposition, so the real obstruction is multiswap cancellation.
7. Lemma 7: exact single-row adjacent-coverage maxima at `n = 25` are `24`, `16`, and `11` for margins `0`, `1`, and `2`.
8. Lemma 8: the explicit weighted-zero identity above yields a balanced `25`-column matrix with all columns distinct.
9. Lemma 9: the symmetric involution swapping each opposite pair preserves all three row sums in that matrix.
10. Gap: neither route yet proves the intended positive statement or its negation.

## chosen_plan
1. First compute the exact single-row adjacent-coverage maxima for margins `0`, `1`, and `2` at `n = 25`.
2. If that does not force a contradiction, test the odd symmetric weighted-zero template
   `1 v_1 + 2 v_2 + ... + 12 v_12 = 0`
   in distinct nonzero ternary directions.
3. Stop once I either have an exact proof/disproof or a sharply delimited gap with only these bounded computations supporting it.

Outcome of that plan:
- Step 1 did not yield a contradiction: the exact row-level maxima `24,16,11` are still too large.
- Step 2 succeeded in the limited diagnostic sense: the odd symmetric balanced obstruction exists explicitly at `n = 25`.
- I still do not have a certifying `3 x 25` witness, and I still do not have a full impossibility theorem.

Current mathematical position:
- The local adjacent-transposition bottleneck is still too weak to disprove `B(25)=3`.
- The balanced near-full-cube regime already contains explicit full-distinctness fake candidates with a nontrivial preserving involution.
- So the unresolved space narrows to the same two global possibilities as in nearby cases:
  - a broader impossibility theorem controlling every `3 x 25` schedule, or
  - a genuinely non-balanced witness that escapes this balanced cancellation pattern.

Self-check:
- This stayed reasoning first, code second.
- Lean remains off because there is no exact proof or exact disproof in hand.

## self_checks
- Statement check: the target remains the exact claim `B(25) = 3`.
- Scope check: both approaches are explicitly partial routes, not hidden proofs.
- Method check: the only code used was one exact single-row DP and one bounded search inside the odd symmetric balanced family.
- Conservatism check: no stronger label than `PARTIAL` is justified.

## code_used
- Used two short Python computations, both directly tied to the handwritten reasoning.
- Computation 1: exact dynamic program for a single row `a_1,...,a_25 in {-1,0,1}` with prescribed margin `m`, maximizing adjacent certifications.
  - output `24` for `m = 0`
  - output `16` for `m = 1`
  - output `11` for `m = 2`
- Computation 2: bounded depth-first search over the odd symmetric template, looking for `12` distinct opposite-pair classes of nonzero ternary vectors with
  `1 v_1 + 2 v_2 + ... + 12 v_12 = 0`.
  - output: one explicit solution, giving the balanced `25`-column family displayed above
- No generic brute-force search over all `3 x 25` schemes, no SAT/ILP/CP-SAT, and no Lean.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Current conclusion:
  - I have no proof of `B(25) = 3`.
  - I have no proof of `B(25) != 3`.
  - The usual local adjacent-transposition obstruction is still too weak.
  - The odd all-balanced symmetric obstruction exists explicitly at `n = 25`, even with `25` pairwise distinct columns.
  - Therefore any exact proof or disproof for the active instance must control global multiswap cancellation and probably also the genuinely non-balanced regime.

## likely_failure_points
- The adjacent-transposition route may again be too weak to control higher-order permutations.
- The symmetric balanced obstruction only rules out one large family of fake candidates rather than all `3 x 25` schedules.
- A true witness, if it exists, may require nonzero row margins and asymmetry that are invisible to the current balanced template.
- The near-full-cube fact `25 of 27` still feels structurally important, but I do not yet see the invariant that converts it into either a witness construction or an impossibility theorem.

## what_verify_should_check
- Verify that the solve stage stayed locked to the exact intended statement `B(25) = 3`.
- Recheck the transposition formula and the local adjacent-swap rules before trusting any later bounded computation.
- Re-run the single-row DP and confirm the exact maxima `24`, `16`, `11`.
- Audit the explicit vectors `v_1,...,v_12` and the derived `25` columns, verifying:
  - all columns are distinct;
  - all three weighted row sums are `0`;
  - the involution `(1 25)(2 24)...(12 14)` preserves those row sums.
- Keep the classification conservative unless verification finds a genuinely global argument beyond this balanced obstruction family.

## verify_rediscovery
- PASS 1 used the allowed bounded web budget on the exact instance `B(25)`, alternate Munchhausen/omni-sequence phrasing, the canonical OEIS entry `A186313`, the Brand paper `Munchhausen Matrices`, and an exact-instance status sweep.
- Within that budget, I did not find any theorem, proposition, example, observation, corollary, or later discussion settling the exact intended statement `B(25) = 3` or `B(25) != 3`.
- The canonical source trail still matches the curated description that the window `20 <= n <= 26` remains unresolved there, and the bounded follow-up did not reveal a hidden exact-instance settlement inside the same source family.
- Rediscovery is therefore not established.

## verify_faithfulness
- The solve artifact stayed locked to the intended statement `B(25) = 3`.
- The working matrix formulation is faithful to the selected problem: a `3 x 25` ternary matrix must distinguish the identity labeling from every nontrivial permutation via the sign pattern of `Mw`.
- The writeup did not drift into claiming that adjacent-swap detection alone proves the result. It explicitly treated the adjacent analysis and the balanced fake-family construction as partial evidence only.

## verify_proof
- No incorrect step was found in the mathematical claims actually made.
- The transposition identity `(j-i)(M_{ri} - M_{rj})` is correct, and the listed adjacent-swap rules for row margins `0`, `1`, and `2` follow from it.
- The all-balanced interpretation is also used correctly here: distinct columns force every single transposition to change at least one row total, but that still leaves multiswap cancellation as the real obstruction.
- The first genuinely missing step is simply the absent global argument. The checked lemmas do not yet prove either a certifying `3`-weighing witness or an impossibility theorem for `B(25)`.

## verify_adversarial
- I independently reran the single-row dynamic program described in the record. It again returned the exact maxima `24`, `16`, and `11` for margins `0`, `1`, and `2`.
- I independently checked the explicit weighted-zero vectors `v_1,...,v_12`. They do satisfy `sum_{k=1}^{12} k v_k = 0`.
- Using the derived `25` columns, I confirmed that all columns are distinct, all three row sums are exactly `0`, and the involution `(1 25)(2 24)...(12 14)` preserves those row sums.
- This adversarial rerun supports the stated partial obstruction only. It does not produce an exact witness for `B(25)=3` and does not upgrade the artifact to `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.

## verify_verdict
- `UNVERIFIED`
- Reason: the bounded computations and partial lemmas check out, but they still do not settle the intended exact statement `B(25) = 3` or its negation.
- Classification remains `PARTIAL`.
- `lean_ready = false` because there is no frontier-novel exact theorem-level claim ready for formalization.

## minimal_repair_if_any
- No mathematical repair was needed.
- The only conservative repair is classificatory: keep the run at `PARTIAL` with `verify_verdict = UNVERIFIED` and do not run Lean.
