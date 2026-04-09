# b26-munchhausen-matrix

## statement_lock
- Active slug: `b26-munchhausen-matrix`
- Title: `Does Baron Munchhausen's omni-sequence satisfy B(26)=3?`
- Locked intended statement: `B(26) = 3.`
- Working formulation: there exists a `3 x 26` ternary matrix `M` with entries in `{-1,0,1}` such that, for the weight vector `w = (1,2,...,26)^T`, every nonidentity permutation of the labels changes at least one of the three balance outcomes `sign(Mw)`.
- Solve-stage normalization: I may flip the sign of any row, so every nonzero row margin may be assumed positive.

Self-check:
- The target is exactly one certifying `3`-weighing schedule for labels `1,...,26`.
- I am not claiming anything yet about the wider unresolved window beyond this exact `n = 26` instance.

## definitions
- For a column `c_j in {-1,0,1}^3`, entry `1` means coin `j` is on the left pan in that weighing, `-1` means right pan, and `0` means absent.
- For row `r`, write `x_r = sum_{j=1}^{26} M_{rj} j`. After normalization, `x_r >= 0`.
- If a transposition swaps labels `i < j`, the row-`r` total changes by
  `(j - i)(M_{ri} - M_{rj})`.
- Therefore an adjacent swap `(i,i+1)` changes the sign of a row with margin `x_r` exactly under these local rules:
  - `x_r = 0`: iff `M_{ri} != M_{r,i+1}`;
  - `x_r = 1`: iff `M_{ri} < M_{r,i+1}`;
  - `x_r = 2`: iff `(M_{ri}, M_{r,i+1}) = (-1,1)`;
  - `x_r >= 3`: impossible.
- So every adjacent transposition must be detected by at least one row of margin `0`, `1`, or `2`.
- Another necessary condition is that all `26` columns be distinct, since identical columns can be swapped with no effect on any weighing.
- Because there are only `27` ternary column types in total, any distinct-column `3 x 26` matrix omits exactly one of them.
- Up to row permutations and row sign flips, the omitted type lies in one of four orbits:
  - `(0,0,0)`
  - `(1,0,0)`
  - `(1,1,0)`
  - `(1,1,1)`
- A full opposite pair means that both `v` and `-v` occur among the columns.
- In the special all-balanced case `Mw = 0`, any single transposition between distinct columns is automatically detected. The real danger there is multiswap cancellation.

Self-check:
- I re-derived the transposition formula before using it.
- The adjacent-swap rules are necessary conditions only, not a verification criterion.

## approach_A
Structural / invariant route: push the exact low-margin consequences of adjacent transpositions.

1. Any row with margin `>= 3` is invisible to every adjacent swap.
2. So all `25` adjacent swaps must be covered by rows with margins `0`, `1`, or `2`.
3. For a fixed row, this becomes a finite path problem on `{-1,0,1}` with the exact weighted-sum constraint `sum i a_i = m`.
4. The immediate question is whether the exact single-row maxima at `n = 26` are finally small enough to force a contradiction.

Bounded exact calculation:
- margin `0`: maximum `25`
- margin `1`: maximum `16`
- margin `2`: maximum `12`

What this shows:
- Row-by-row adjacent coverage still does not force a contradiction.
- In particular, one balanced row can again certify all `25` adjacent swaps by itself, so the local adjacent-transposition filter remains too weak.
- The `26 of 27` full-cube feature does not show up at this rowwise level. If it matters, it must matter through a genuinely global permutation obstruction or a genuinely global witness construction.

Self-check:
- These are exact maxima for the stated single-row problem, not heuristics.
- I have not silently upgraded local adjacent detection into a proof about all permutations.

## approach_B
Construction / extremal / contradiction route: exploit the exact `26 of 27` column geometry directly.

Key observation:
- A distinct-column `3 x 26` matrix uses every ternary column type except one.
- In each orbit of the omitted type, there remain three available directions `a,b,c` such that
  `a + b + c = 0`,
  and the full opposite pairs `±a`, `±b`, `±c` are all present.

Concrete orbit-by-orbit choices:
- If the omitted type is `(0,0,0)`, take
  - `a = (1,0,0)`
  - `b = (0,1,0)`
  - `c = (-1,-1,0)`
- If the omitted type is in the orbit of `(1,0,0)`, take
  - `a = (0,1,0)`
  - `b = (0,0,1)`
  - `c = (0,-1,-1)`
- If the omitted type is in the orbit of `(1,1,0)`, take
  - `a = (1,0,0)`
  - `b = (0,0,1)`
  - `c = (-1,0,-1)`
- If the omitted type is in the orbit of `(1,1,1)`, take
  - `a = (1,0,0)`
  - `b = (0,1,0)`
  - `c = (-1,-1,0)`

Explicit fake-candidate family:
- Place the first six columns as
  `c_1 = a`, `c_2 = -a`, `c_3 = b`, `c_4 = -b`, `c_5 = c`, `c_6 = -c`.
- Fill the remaining positions `7,...,26` with the other `20` distinct available column types in any order.
- Then the nonidentity permutation
  `tau = (1 2)(3 4)(5 6)`
  preserves the exact row-sum vector, because its total change is
  `2a + 2b + 2c = 2(a + b + c) = 0`.

Interpretation:
- The near-full-cube condition by itself is far from sufficient: in every omitted-column orbit there are explicit `26`-column schedules with all columns distinct and a nontrivial preserving permutation.
- This is a genuine exact obstruction family, but only for some schedules. It does not prove that every `3 x 26` schedule fails.

Self-check:
- The construction is explicit and audit-able by hand.
- It only constructs non-verifying families; it does not upgrade to a proof that `B(26) != 3`.

## lemma_graph
1. Lemma 1: identical columns are forbidden.
2. Lemma 2: a transposition `(i,j)` changes row `r` by `(j-i)(M_{ri} - M_{rj})`.
3. Lemma 3: after orienting rows positively, adjacent certification depends only on margins `0`, `1`, and `2`, with the local rules above.
4. Lemma 4: rows of margin `>= 3` are useless for adjacent swaps.
5. Lemma 5: exact single-row adjacent-coverage maxima at `n = 26` are `25`, `16`, and `12` for margins `0`, `1`, and `2`.
6. Lemma 6: any distinct-column `3 x 26` matrix omits exactly one ternary type.
7. Lemma 7: in every omitted-type orbit, the remaining column set contains three full opposite-pair classes `±a`, `±b`, `±c` with `a + b + c = 0`.
8. Lemma 8: arranging those six columns as `a,-a,b,-b,c,-c` makes the permutation `(1 2)(3 4)(5 6)` preserve the exact row sums.
9. Gap: neither route yet proves the intended positive statement or its negation.

## chosen_plan
1. Push the low-margin adjacent-swap algebra to exact `n = 26`.
2. Use the exact `26 of 27` column geometry to see whether it already forces a clean cancellation family.
3. Only use code if the rowwise route actually needs exact finite maxima.

Outcome of that plan:
- Step 1 did not yield a contradiction: the exact row-level maxima `25,16,12` are still too large.
- Step 2 did yield a clean exact partial theorem: every omitted-column orbit admits explicit non-verifying `26`-column schedules with a six-column cancellation pattern.
- I also checked two much more rigid global opposite-pair involution templates by exact search:
  - omit `000` and use all `13` opposite pairs symmetrically with weights `25,23,...,1`;
  - omit one nonzero class and use `12` outer opposite pairs plus a middle `0`/singleton block with weights `25,23,...,3`.
  Both returned no solution, so the clean odd-style global balanced involution does not extend in those obvious even `26` forms.

Current mathematical position:
- I do not have a witness proving `B(26) = 3`.
- I do not have an impossibility theorem proving `B(26) != 3`.
- The local adjacent-transposition bottleneck is still too weak.
- The `26 of 27` geometry does give explicit bad schedules, but only in constructed families.
- So the unresolved space still looks like:
  - a genuinely non-balanced witness, or
  - a global impossibility theorem that depends on the actual order of the opposite pairs, not merely on which column type is omitted.

Self-check:
- This stayed reasoning first, code second.
- Lean remains off because there is no exact proof or exact disproof in hand.

## self_checks
- Statement check: the target remains the exact claim `B(26) = 3`.
- Scope check: both approaches are partial routes, not hidden proofs.
- Method check: the only code used was one exact single-row DP and one tiny structured search over two rigid involution templates singled out by the handwritten setup.
- Conservatism check: no stronger label than `PARTIAL` is justified.

## code_used
- Used two short Python computations, both directly tied to the handwritten reasoning.
- Computation 1: exact dynamic program for a single row `a_1,...,a_26 in {-1,0,1}` with prescribed margin `m`, maximizing adjacent certifications.
  - output `25` for `m = 0`
  - output `16` for `m = 1`
  - output `12` for `m = 2`
- Computation 2: exact search over two sharply defined global opposite-pair involution templates.
  - Template A: omit `000`, use all `13` opposite-pair classes with weights `25,23,...,1`
  - Template B: omit one nonzero class, use `12` outer opposite-pair classes with weights `25,23,...,3`
  - output: no solution in either template
- No generic brute-force search over all `3 x 26` schemes, no SAT/ILP/CP-SAT, and no Lean.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Current conclusion:
  - I have no proof of `B(26) = 3`.
  - I have no proof of `B(26) != 3`.
  - The usual low-margin adjacent-transposition obstruction is still too weak.
  - The exact `26 of 27` cube geometry already contains explicit non-verifying families in every omitted-column orbit via a six-column cancellation pattern.
  - The cleanest global even opposite-pair involution templates do not seem to exist in the obvious forms checked here.
  - Any exact resolution now has to control broader multiswap behavior than the local or rigid symmetric templates captured in this pass.

## likely_failure_points
- The local adjacent-transposition route may again be too weak to control higher-order permutations.
- The six-column cancellation family only shows that some schedules fail; it does not come close to proving that all schedules fail.
- A true witness, if it exists, may require nonzero margins and asymmetry that are invisible to the current cancellation templates.
- Conversely, a full impossibility theorem may require an invariant depending on the actual distance pattern of opposite pairs, not just the omitted-column orbit.

## what_verify_should_check
- Verify that the solve stage stayed locked to the exact intended statement `B(26) = 3`.
- Recheck the transposition formula and the local adjacent-swap rules for margins `0`, `1`, and `2`.
- Re-run the single-row DP and confirm the exact maxima `25`, `16`, `12`.
- Audit the omitted-type case split and the explicit six-column family, verifying:
  - the listed triples really satisfy `a + b + c = 0`;
  - the six columns `a,-a,b,-b,c,-c` are all present in the claimed omitted-type orbit;
  - the permutation `(1 2)(3 4)(5 6)` preserves the exact row-sum vector.
- Optionally rerun the two rigid opposite-pair template searches, but treat them only as diagnostic side facts, not as the main proof content.
- Keep the classification conservative unless verification finds a genuinely global argument beyond these partial obstructions.

## verify_rediscovery
- PASS 1 used a bounded prior-art audit focused on the exact instance `B(26)`, the family notation `A186313`, the canonical Brand paper, and same-source theorem/proposition/example/corollary style checks.
- Within that capped pass, I found no evidence that the exact intended statement `B(26)=3` or its exact negation has already been settled in the literature.
- The canonical source trail still points to the same open window: OEIS `A186313` continues to list `3 <= B(n) <= 4` for `20 <= n <= 26`, and the cited Brand paper is consistent with bounds and structural analysis rather than an exact `n=26` resolution.
- Verdict for PASS 1: no rediscovery established.

## verify_faithfulness
- The solve artifact stayed locked to the intended statement `B(26)=3`, phrased as existence of a certifying `3 x 26` Munchhausen matrix.
- The actual mathematical claims made in the record are weaker partial claims: exact local adjacent-swap maxima for single rows and an explicit family of non-verifying `26`-column schedules in every omitted-column orbit.
- I found no wrong-theorem drift, quantifier drift, or definition change. The record does not pretend that the partial obstruction proves `B(26) != 3`, and it does not mislabel the instance as solved.

## verify_proof
- I rederived the transposition identity `(j-i)(M_{ri}-M_{rj})` and the adjacent-swap detection rules for row margins `0`, `1`, and `2`; those checks are correct.
- I reran the bounded exact dynamic program for one row and confirmed the maxima `25`, `16`, and `12` at margins `0`, `1`, and `2`.
- I checked the omitted-type orbit argument and the listed triples `a,b,c`; in each case they satisfy `a+b+c=0`, their opposite pairs remain available after omitting the stated orbit representative, and the six-column placement `a,-a,b,-b,c,-c` makes the permutation `(1 2)(3 4)(5 6)` preserve the exact row-sum vector.
- First incorrect step: none found within the artifact's actual claim envelope.
- Critical limitation remains: these arguments only verify a partial obstruction package. They do not prove existence or impossibility for the exact intended statement.

## verify_adversarial
- I reran the only numerical claim that matters here: the exact single-row DP. It reproduced `25`, `16`, and `12`.
- I independently recomputed the six-column cancellation delta for all four omitted-type orbits and got zero row-sum change in every case.
- There is no witness matrix claiming `B(26)=3` to break, and there is no global impossibility proof to stress-test. The adversarial result is therefore only that the checked computations support the stated partial obstruction and do not accidentally certify the full theorem.

## verify_verdict
- `verify_verdict = UNVERIFIED`
- `classification = PARTIAL`
- `confidence = high`
- `lean_ready = false`
- Reason: PASS 1 did not establish rediscovery, but PASS 2 through PASS 4 only validate a partial analysis. The artifact still does not prove `B(26)=3` or `B(26) != 3`, so there is nothing exact or Lean-ready to carry forward.

## minimal_repair_if_any
- No patch to the mathematics was needed.
- The only conservative repair is interpretive: keep the artifact labeled strictly as `PARTIAL` and not as any exact proof or exact disproof.
