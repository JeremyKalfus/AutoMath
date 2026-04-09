# b20-munchhausen-matrix

## statement_lock
- Active slug: `b20-munchhausen-matrix`
- Title: `Is the Baron's omni-sequence value B(20) equal to 3?`
- Locked intended statement: `B(20) = 3.`
- Working formulation: there exists a `3 x 20` ternary matrix `M` with entries in `{-1,0,1}` such that, for the weight vector `w = (1,2,...,20)^T`, no nonidentity permutation `pi` of the weights yields the same three balance outcomes as `M w`.
- Solve-stage convention: I may flip the sign of any row of `M`, so every nonzero row outcome may be assumed positive. Balanced rows are left as balanced.
- Equivalent transposition test used below: if swapping weights `i < j` between columns `i` and `j` leaves all three row outcomes unchanged, then `M` is not verifying.

Self-check:
- The object to construct or rule out is exactly a `3`-weighing verification for labels `1,...,20`.
- I am treating `B(20)=3` as an existence claim for one verifying `3 x 20` matrix, not as a universal statement about all such matrices.

## definitions
- For a column `c_j in {-1,0,1}^3`, the entry `1` means coin `j` is on the left pan in that weighing, `-1` means right pan, and `0` means absent.
- For row `r`, write `x_r = sum_{j=1}^{20} M_{rj} j`. After orienting the row, `x_r >= 0`.
- The outcome vector is `s = sign(M w) in {-1,0,1}^3`.
- If a transposition swaps weights `i < j`, the row-`r` total changes by
  `(j-i) (M_{ri} - M_{rj})`.
- So for a positive row total `x_r > 0`, a transposition can only flip or balance that row if it moves a heavier weight toward the side that was previously lighter, and the margin `x_r` is small enough.
- In particular, for an adjacent swap `(i,i+1)`:
  - if `x_r = 0`, the row changes outcome exactly when `M_{ri} != M_{r,i+1}`;
  - if `x_r = 1`, the row changes outcome only when `M_{ri} > M_{r,i+1}`;
  - if `x_r = 2`, the row changes outcome only for the sharp drop `(1,-1)`;
  - if `x_r >= 3`, the row cannot detect any adjacent swap.
- A necessary condition for verification is therefore: every adjacent transposition `(i,i+1)` must change the outcome in at least one row.
- Another basic necessary condition: all `20` columns must be distinct, since identical columns can be swapped with no effect on any weighing.

Self-check:
- The adjacent-swap criterion is used only as a necessary condition.
- The row-margin observations are exact for adjacent swaps because all row totals are integers.

## approach_A
Structural / invariant route: squeeze the problem through row margins and adjacent transpositions.

1. Let `x_r` be the oriented row margins.
2. Any row with `x_r >= 3` is useless against all adjacent swaps.
3. Therefore the `19` adjacent swaps must all be certified by rows of type `0`, `1`, or `2` in the sense above.
4. This makes low-margin rows the structural bottleneck:
   - a balanced row only certifies an adjacent pair when its entries differ there;
   - a row with margin `1` only certifies a local descent;
   - a row with margin `2` only certifies the maximal descent `1 -> -1`.
5. So if `B(20)=3`, the three row sequences must simultaneously:
   - have all `20` columns distinct,
   - realize the required exact row margins,
   - cover all `19` adjacent swaps by the local rules above,
   - and still defeat every larger transposition and every more complicated permutation.

Why this looks promising:
- It turns the problem into a finite path problem on the `27` ternary column types, with strong local restrictions from the margins.
- If even the adjacent-swap necessary condition fails for every plausible margin profile, that would already prove `B(20) != 3`.

Obstruction noticed on paper:
- The adjacent-swap filter is still only a necessary condition, not a full certificate of verification.
- Balanced rows are much more flexible than positive rows, so the local condition alone may leave many fake candidates.

Self-check:
- This route is rigorous up to the stated necessary conditions.
- I have not silently upgraded a necessary condition into a proof of impossibility.

## approach_B
Construction / extremal route: try to design a witness with very small row margins, because only such rows can reliably react to nearby swaps.

Heuristic starting point:
- A candidate `3`-weighing witness should probably use row margins in `{0,1,2}` whenever possible.
- Rows with larger margins are too insensitive locally, so they likely force the other rows to do nearly all the work.

Natural construction ideas:
1. Balanced-row strategy:
   choose all three rows balanced, so any swap of coins whose columns differ in some coordinate immediately breaks at least one balancing equality.
   Weakness: a nontrivial permutation can still preserve all three equalities simultaneously, so balanced rows alone do not obviously isolate the identity permutation.

2. Mixed-margin strategy:
   use one or two balanced rows for coarse partitioning and one tiny positive-margin row to orient the labels within those classes.
   Weakness: with only three coordinates, repeated column patterns under projections are unavoidable, and a tiny positive-margin row can only resolve such collisions through a very restricted descent pattern.

3. Extremal ordering strategy:
   order `20` distinct ternary columns so that consecutive labels always move in at least one certifying direction.
   Weakness: even if this works, one still must exclude longer permutations, not just adjacent ones.

Self-check:
- This route explains why a witness, if it exists, is likely highly tuned rather than generic.
- The failure mode is clear: one can satisfy many local checks without proving full uniqueness.

## lemma_graph
1. Lemma 1: identical columns are forbidden.
2. Lemma 2: for a transposition `(i,j)`, row `r` changes by `(j-i)(M_{ri}-M_{rj})`.
3. Lemma 3: for an adjacent swap, a row with margin `>= 3` cannot change outcome.
4. Lemma 4: therefore every adjacent swap must be certified by a row of margin `0`, `1`, or `2`.
5. Lemma 5: a balanced row certifies adjacent pair `i,i+1` iff its entries differ there; a margin-`1` row certifies only a descent; a margin-`2` row certifies only `1 -> -1`.
6. Consequence: any true witness must live inside a sharply constrained finite family of low-margin local patterns.
7. Remaining gap: those local constraints do not by themselves rule out all nonadjacent permutations.

## chosen_plan
Best path from the current no-web position:

1. Push the low-margin transposition analysis as far as possible by hand.
2. If that stalls, run one tiny bounded experiment tied directly to the hand proof:
   compute exact per-row extremal data for rows of margin `0`, `1`, or `2`, and test whether three such rows can even satisfy the adjacent-swap necessary condition while keeping all `20` columns distinct.
3. Use that experiment only as evidence for or against the structural route, not as a substitute for a proof of full verification.

Current handwritten attempt:
- I do not yet see a clean no-code impossibility argument that upgrades the adjacent-swap bottleneck to a full contradiction.
- I also do not have a concrete `3 x 20` witness.
- So the next justified step is a very small exact computation about the low-margin rows themselves.

Bounded experiment outcome:
- For a single row of exact margin `0`, the maximum number of adjacent pairs it can certify is `19`.
- For a single row of exact margin `1`, the maximum number is `13`.
- For a single row of exact margin `2`, the maximum number is `9`.
- So row-by-row counting alone does not force a contradiction.
- I then searched only for a length-`20` sequence of distinct ternary columns satisfying the adjacent-swap local rules with target margins `(0,0,0)`.
- Such a sequence exists. One explicit example is
  `[(0,0,0), (-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1), (-1,-1,0), (1,1,0), (-1,0,-1), (1,0,1), (0,-1,-1), (0,1,1), (-1,0,1), (1,1,1), (0,1,-1), (1,-1,-1), (1,-1,0), (-1,-1,-1), (-1,1,1)]`.
- This shows the adjacent-swap necessary condition is realizable even with all three rows balanced.
- But that same explicit path is still not verifying: the two disjoint transpositions `(1 7)` and `(13 16)` preserve all three row sums, because their row-sum changes are
  `6(c_1-c_7) = (0,0,-6)` and `3(c_13-c_16) = (0,0,6)`,
  which cancel exactly.

Self-check:
- The planned computation is directly motivated by the reasoning, not by generic brute force over all matrices.
- Lean remains off because there is no exact proof or exact disproof in hand.
- The experiment strengthened the diagnosis of the gap: the local adjacent-swap filter is genuinely too weak.

## self_checks
- Statement check: the target remains the exact claim `B(20)=3`.
- Conservatism check: every claim above is either a direct calculation or explicitly marked as heuristic.
- Method check: the only code used was the promised low-margin bounded experiment.
- Falsifier check: the explicit balanced fake candidate fails by a concrete nonidentity permutation, so I am not mistaking a local condition for a witness.

## code_used
- Used one short Python experiment, tightly scoped to the low-margin analysis.
- Computation 1: dynamic programming for the exact row-level maxima
  - margin `0`: max adjacent-pair certifications `= 19`
  - margin `1`: max adjacent-pair certifications `= 13`
  - margin `2`: max adjacent-pair certifications `= 9`
- Computation 2: bounded DFS over distinct ternary columns for the local adjacent-swap rule with target margins `(0,0,0)`, producing one explicit `20`-column path.
- Computation 3: direct search over pairs of disjoint transpositions for that explicit path, finding `(1 7)(13 16)` as a preserving permutation.

## result
- Solve-stage verdict after bounded experiment: `PARTIAL`
- Confidence: `medium`
- Current mathematical position:
  - I have a clean set of necessary low-margin constraints coming from adjacent transpositions.
  - Those constraints are not by themselves strong enough to settle the problem: there are explicit `20`-column low-margin fake candidates that satisfy the local adjacent-swap tests but still admit nontrivial preserving permutations.
  - I do not yet have either a witness for `B(20)=3` or a rigorous contradiction showing `B(20) != 3`.
  - The most defensible current conclusion is that any successful proof or disproof must use a stronger global invariant than the adjacent-transposition filter alone.

## likely_failure_points
- The adjacent-swap analysis may be too weak: a matrix can fail full verification even while passing all adjacent-swap checks.
- Conversely, a true witness could use one seemingly insensitive row together with two highly structured rows in a way that the current pencil-and-paper analysis misses.
- Without the canonical matrix criterion from the source paper, it is easy to overestimate what the local transposition tests can prove.
- The bounded search only explored one low-margin family explicitly; it was diagnostic, not exhaustive over all `3 x 20` matrices.

## what_verify_should_check
- Check whether the low-margin transposition analysis can be strengthened into a genuine impossibility theorem.
- If a candidate matrix later appears, verify not only adjacent transpositions but all nontrivial permutations consistent with the outcome vector.
- Audit whether the solve-stage experiment, if used, stayed within the promised bounded scope and did not silently become a generic brute-force search over all schedules.
- Re-run the explicit fake-candidate falsifier:
  - balanced path above,
  - preserving permutation `(1 7)(13 16)`,
  - cancellation identity `6(c_1-c_7) + 3(c_13-c_16) = 0`.

## verify_rediscovery
- PASS 1 used a bounded web audit with exact-instance and alternate-notation searches for `B(20)`, `Baron's omni-sequence`, `A186313`, and Brand's 2012 paper, plus a recent-status check.
- Within that budget, I found no later source establishing `B(20)=3` or `B(20)=4`, and no theorem / proposition / example / observation in the canonical 2012 paper that already settles the exact `n=20` instance.
- The canonical-status evidence seen in PASS 1 still matches the selected problem: Brand's paper is the main source, and the current OEIS A186313 status note still keeps `20 <= n <= 26` in the unresolved window with `3 <= B(n) <= 4`.
- Therefore rediscovery was not established within budget.

## verify_faithfulness
- The solve writeup stays locked to the exact intended statement `B(20)=3` and explicitly treats it as an existence claim for one verifying `3 x 20` ternary matrix.
- I found no wrong-theorem drift, quantifier drift, or definition change in the solve record.
- The only substantive conclusion actually reached by the solve stage is weaker than the intended statement: the adjacent-transposition filter alone does not settle `B(20)=3`.
- So the writeup is faithful, but it never proves either the intended positive claim or its negation.

## verify_proof
- First incorrect step: none found, because there is no claimed complete proof of `B(20)=3` or of `B(20) != 3` to refute.
- The local lemmas about transpositions and adjacent swaps are correct as stated and are used conservatively as necessary conditions.
- The decisive proof gap is explicit and real: the solve argument does not upgrade the local adjacent-swap constraints to a global uniqueness theorem for all permutations.
- So the correct verification outcome is not "wrong proof", but "insufficient proof": the run remains unverified on the exact statement.

## verify_adversarial
- I reran the explicit falsifier for the displayed balanced `20`-column path.
- The original row sums are `(0,0,0)`, and after the nonidentity permutation `(1 7)(13 16)` they are still `(0,0,0)`, so the same outcome vector is preserved.
- The cancellation identity also checks directly: `6(c_1-c_7) + 3(c_13-c_16) = (0,0,0)`.
- This confirms the advertised counterexample to the local adjacent-swap heuristic and supports the solver's claim that the bounded experiment exposed a fake candidate rather than a witness.

## verify_verdict
- `UNVERIFIED`
- Classification remains `PARTIAL`.
- Reason: PASS 1 did not show rediscovery, but PASS 2 through PASS 4 also did not produce an exact proof or exact disproof of `B(20)=3`; the current record only gives correct necessary conditions and one falsified local-pattern candidate.
- `lean_ready = false` because there is no exact statement in hand that is strong enough to formalize as a frontier-novel final result.

## minimal_repair_if_any
- No mathematical repair was applied to upgrade the run.
- Conservative wording repair only: any language that sounds like a disproof should be read as a diagnosis of a proof gap in the current approach, not as evidence that `B(20) != 3`.
