# b24-munchhausen-matrix

## statement_lock
- Active slug: `b24-munchhausen-matrix`
- Title: `Does Baron Munchhausen's omni-sequence satisfy B(24)=3?`
- Locked intended statement: `B(24) = 3.`
- Working formulation: there exists a `3 x 24` ternary matrix `M` with entries in `{-1,0,1}` such that, for the weight vector `w = (1,2,...,24)^T`, every nonidentity permutation of the labels changes at least one of the three balance outcomes `sign(Mw)`.
- Solve-stage normalization: I may flip the sign of any row, so every nonzero row margin may be assumed positive.

Self-check:
- The target is exactly one certifying `3`-weighing schedule for labels `1,...,24`.
- I am not claiming anything yet about the full sequence beyond the exact `n = 24` instance.

## definitions
- For a column `c_j in {-1,0,1}^3`, entry `1` means coin `j` is on the left pan in that weighing, `-1` means right pan, and `0` means absent.
- For row `r`, write `x_r = sum_{j=1}^{24} M_{rj} j`. After normalization, `x_r >= 0`.
- If a transposition swaps labels `i < j`, the row-`r` total changes by
  `(j - i)(M_{ri} - M_{rj})`.
- Therefore an adjacent swap `(i,i+1)` changes the sign of a row with margin `x_r` exactly under these local rules:
  - `x_r = 0`: iff `M_{ri} != M_{r,i+1}`;
  - `x_r = 1`: iff `M_{ri} < M_{r,i+1}`;
  - `x_r = 2`: iff `(M_{ri}, M_{r,i+1}) = (-1,1)`;
  - `x_r >= 3`: impossible.
- So every adjacent transposition must be detected by at least one row of margin `0`, `1`, or `2`.
- Another necessary condition is that all `24` columns be distinct, since identical columns can be swapped with no effect on any weighing.
- In the special all-balanced case `Mw = 0`, any single transposition between distinct columns is automatically detected, because some row total changes from `0` to a nonzero integer. The real danger there is cancellation among several swaps.

Self-check:
- I re-derived the transposition formula before using it.
- The adjacent-swap rules are necessary conditions only, not a proof of verification.

## approach_A
Structural / invariant route: push the exact low-margin consequences of adjacent transpositions.

1. Any row with margin `>= 3` is invisible to every adjacent swap.
2. So all `23` adjacent swaps must be covered by rows with margins `0`, `1`, or `2`.
3. For a fixed row, this becomes a finite path problem on `{-1,0,1}` with the exact weighted-sum constraint `sum i a_i = m`.
4. The immediate question is whether the exact single-row maxima at `n = 24` are small enough to force a contradiction.

Bounded exact calculation:
- margin `0`: maximum `23`
- margin `1`: maximum `15`
- margin `2`: maximum `11`

What this shows:
- Row-by-row adjacent coverage still does not force a contradiction.
- In particular, one balanced row can again certify all `23` adjacent swaps by itself, so the local adjacent-transposition filter remains too weak.
- Any impossibility proof for `B(24) != 3` must use a more global invariant than rowwise adjacent coverage.

Self-check:
- These are exact maxima for the stated single-row problem, not heuristics.
- I have not silently upgraded local adjacent detection into a global verification criterion.

## approach_B
Construction / extremal / contradiction route: test the natural even balanced opposite-pair obstruction family.

Even `24` template:
- Put columns in opposite pairs around the midpoint:
  `c_k = v_k`, `c_{25-k} = -v_k` for `k = 1,...,12`,
  where the `v_k` are distinct nonzero ternary directions.
- Then the row-sum vector is
  `sum_{k=1}^{12} (2k - 25) v_k`,
  so all three rows are balanced exactly when
  `sum_{k=1}^{12} (25 - 2k) v_k = 0`,
  i.e.
  `23 v_1 + 21 v_2 + 19 v_3 + ... + 3 v_11 + 1 v_12 = 0`.
- Under that same condition, the involution
  `(1 24)(2 23)...(12 13)`
  preserves all three row sums, so any such matrix is a concrete non-verifying fake candidate.

Why this route is natural at `n = 24`:
- With `24` distinct columns available out of only `27` ternary types, the matrix is already very close to the full ternary cube.
- The even opposite-pair family is the cleanest way to expose global multiswap cancellation if it exists.

Exact bounded search in that restricted family:
- I exhaustively checked all choices of `12` distinct directions from the `13` opposite-pair classes of nonzero ternary vectors, together with all `2^12` sign choices.
- No solution exists to
  `23 v_1 + 21 v_2 + 19 v_3 + ... + 3 v_11 + 1 v_12 = 0`
  in that family.

Interpretation:
- The clean symmetric opposite-pair balanced obstruction does not exist in this restricted even `24` family.
- So the explicit odd-case fake family from `n = 21` and `n = 23` still fails to extend directly to the even cases `22` and `24`.
- This removes one tempting multiswap-cancellation mechanism, but it still does not prove `B(24) = 3`.

Self-check:
- The search here is exact, but only for one sharply defined symmetry class.
- It would not, by itself, settle all `3 x 24` matrices.

## lemma_graph
1. Lemma 1: identical columns are forbidden.
2. Lemma 2: a transposition `(i,j)` changes row `r` by `(j-i)(M_{ri} - M_{rj})`.
3. Lemma 3: after orienting rows positively, adjacent certification depends only on margins `0`, `1`, and `2`, with the local rules above.
4. Lemma 4: rows of margin `>= 3` are useless for adjacent swaps.
5. Lemma 5: exact single-row adjacent-coverage maxima at `n = 24` are `23`, `15`, and `11` for margins `0`, `1`, and `2`.
6. Lemma 6: in the all-balanced regime, distinct columns already detect every single transposition, so the real obstruction is multiswap cancellation.
7. Lemma 7: if the weighted-zero identity
   `23 v_1 + 21 v_2 + ... + 1 v_12 = 0`
   has a solution in distinct ternary directions, then the even opposite-pair family yields an explicit balanced fake candidate for `n = 24`.
8. Lemma 8: that restricted opposite-pair family has no solution.
9. Gap: neither route yet proves the intended positive statement or its negation.

## chosen_plan
1. Push the low-margin adjacent-swap algebra at exact `n = 24`.
2. Test the restricted even opposite-pair balanced family, because it is the cleanest explicit multiswap-cancellation mechanism available locally.
3. Keep Lean off unless a strong exact candidate or exact disproof appears.

Outcome of that plan:
- Step 1 did not yield a contradiction: the exact row-level maxima `23,15,11` are still too large.
- Step 2 also failed to settle the instance: the restricted opposite-pair family has no weighted-zero solution, so there is no explicit fake candidate of that clean symmetric type.
- I still do not have a certifying `3 x 24` witness, and I still do not have a full impossibility theorem.

Current mathematical position:
- I do not yet have a witness proving `B(24) = 3`.
- I do not yet have an impossibility theorem proving `B(24) != 3`.
- The local adjacent-transposition bottleneck remains too weak.
- The cleanest even balanced obstruction family does not appear here, just as it did not at `n = 22`.
- So the unresolved space narrows to two plausible directions:
  - a broader multiswap obstruction not captured by the opposite-pair symmetry class, or
  - a genuinely non-balanced `3`-weighing witness.

## self_checks
- Statement check: the target remains the exact claim `B(24) = 3`.
- Scope check: both approaches are still partial routes, not completed proofs.
- Method check: the only code used was a single-row exact DP and one restricted symmetry-family search.
- Conservatism check: Lean remains off and no stronger label than `PARTIAL` is justified.

## code_used
- Used two short Python computations, both directly tied to the handwritten reasoning.
- Computation 1: exact dynamic program for a single row `a_1,...,a_24 in {-1,0,1}` with prescribed margin `m`, maximizing adjacent certifications.
  - output `23` for `m = 0`
  - output `15` for `m = 1`
  - output `11` for `m = 2`
- Computation 2: exhaustive search over the restricted all-balanced opposite-pair template
  `c_k = v_k`, `c_{25-k} = -v_k`
  with `12` distinct ternary directions, checking whether
  `23 v_1 + 21 v_2 + ... + 1 v_12 = 0`.
  - output: no solution in that family
- No generic brute-force search over all `3 x 24` schemes, no SAT/ILP/CP-SAT, and no Lean.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Current conclusion:
  - I have no proof of `B(24) = 3`.
  - I have no proof of `B(24) != 3`.
  - The usual low-margin adjacent-transposition obstruction is still too weak.
  - The clean symmetric opposite-pair balanced fake family does not exist in this restricted even `24` setting.
  - The exact instance remains unresolved from this solve-stage pass.

## likely_failure_points
- The adjacent-transposition route may again be too weak to control higher-order permutations.
- The opposite-pair balanced template may either fail entirely or succeed only as a restricted fake family, leaving the true instance unresolved.
- A genuine witness, if it exists, may need nonzero margins and asymmetry not visible in the clean balanced templates.
- Conversely, a full impossibility theorem may require a genuinely global invariant beyond local adjacent coverage.

## what_verify_should_check
- Verify that the solve stage stayed locked to the exact intended statement `B(24) = 3`.
- Recheck the transposition formula and the local adjacent-swap rules before trusting any later computation.
- Re-run the single-row DP and confirm the exact maxima `23`, `15`, `11`.
- Re-run the restricted opposite-pair template search and confirm that no weighted-zero solution exists there.
- Keep the classification conservative unless an exact witness or exact disproof really appears.

## verify_rediscovery
- PASS 1 used a bounded live audit focused on the exact instance `B(24)`, alternative Munchhausen/omni-sequence notation, the canonical OEIS entry `A186313`, and the two standard source lines around Brand and Khovanova-Lewis.
- Within that budget, I found no theorem, proposition, example, observation, corollary, or later discussion that settles the exact statement `B(24) = 3` or `B(24) != 3`.
- The canonical source still matches the curated claim that the interval `20 <= n <= 26` is unresolved there, and the bounded follow-up around the cited papers did not reveal an exact-instance settlement hidden inside the source family.
- Rediscovery is therefore not established.

## verify_faithfulness
- The solve artifact stayed faithful to the intended statement. It did not drift to a weaker proxy such as adjacent-swap detection alone or to a different value of `n`.
- The working formulation using a `3 x 24` ternary weighing matrix and the condition that every nonidentity relabeling changes at least one sign in `sign(Mw)` matches the selected problem definition.
- The solver did not claim a proof of `B(24) = 3`; it explicitly labeled both routes as partial and left the exact instance unresolved.

## verify_proof
- No incorrect mathematical step was found in the claims actually made.
- The transposition identity `(j-i)(M_{ri} - M_{rj})` is correct, and the adjacent-swap rules for row margins `0`, `1`, and `2` follow from it.
- The important scope boundary is also handled correctly: those local adjacent-swap rules are necessary conditions only, not a proof that all permutations are separated.
- Since the solve-stage conclusion is only `PARTIAL`, there is no hidden upgrade to an exact proof or exact disproof to reject. The first genuinely missing step is simply the absent global argument that would turn the partial lemmas into either a certifying `3`-weighing witness or an impossibility theorem.

## verify_adversarial
- I independently reran the single-row dynamic program described in the record. It again returned the exact maxima `23`, `15`, and `11` for margins `0`, `1`, and `2`.
- I independently reran the restricted opposite-pair search over the `13` nonzero ternary direction classes and all `12`-class selections with `2^12` sign choices. It again returned `NO_SOLUTION` for the weighted-zero identity `23 v_1 + 21 v_2 + ... + 1 v_12 = 0`.
- There is no separate candidate witness, checker, or counterexample construction to attack beyond those two bounded computations.
- These computations support exactly the partial claims written in the solve artifact and do not support a stronger classification.

## verify_verdict
- `UNVERIFIED`
- Reason: the partial lemmas and bounded computations check out, but they do not prove the intended statement `B(24) = 3` or its negation.
- Classification remains `PARTIAL`, not `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.
- `lean_ready = false` because there is no exact theorem-level claim yet to formalize.

## minimal_repair_if_any
- No mathematical repair was needed.
- The only conservative repair is classificatory: keep the run at `PARTIAL` with `verify_verdict = UNVERIFIED` and do not escalate to Lean.
