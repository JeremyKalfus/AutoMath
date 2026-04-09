# dsrg-60-18-11-6-5

## statement_lock
- Active slug: `dsrg-60-18-11-6-5`
- Title: `Does a directed strongly regular graph with parameters (60,18,11,6,5) exist?`
- Locked intended statement: there exists a loopless directed graph on `60` vertices with constant indegree and outdegree `18` whose adjacency matrix `A` satisfies
  `AJ = JA = 18J` and
  `A^2 = 11I + 6A + 5(J - I - A) = 6I + A + 5J`.
- Equivalent walk formulation used below:
  - every vertex has exactly `11` mutual neighbors,
  - every arc `x -> y` lies on exactly `6` directed `2`-paths `x -> z -> y`,
  - every nonarc `x -/-> y` with `x != y` lies on exactly `5` directed `2`-paths `x -> z -> y`.

Self-check:
- This is the exact existential statement from `selected_problem.md`.
- I am not claiming an exact disproof or construction in solve stage.

## definitions
- Fix a vertex `x`.
- Let `S = N^+(x)` and `T = N^-(x)`, so `|S| = |T| = 18`.
- Write
  - `M = S ∩ T`, so `|M| = 11`,
  - `O = S \\ T`, so `|O| = 7`,
  - `I = T \\ S`, so `|I| = 7`,
  - `N = V \\ ({x} ∪ M ∪ O ∪ I)`, so `|N| = 34`.
- For classes `C,D` among `M,O,I,N`, let `e(C,D)` be the number of directed edges from `C` to `D`.
- Two exact translations used repeatedly:
  - if `y ∈ T`, then `|N^+(y) ∩ T| = 6`; if `y ∉ T` and `y != x`, then `|N^+(y) ∩ T| = 5`,
  - if `y ∈ S`, then `|N^-(y) ∩ S| = 6`; if `y ∉ S` and `y != x`, then `|N^-(y) ∩ S| = 5`.

Self-check:
- The partition sizes are forced by `k = 18` and `t = 11`.
- The two translation bullets are direct restatements of the dsrg `2`-path rule.

## approach_A
Structural / invariant route.

- On the orthogonal complement of the all-ones vector, `A` satisfies
  `u^2 - u - 6 = 0`,
  so the only restricted eigenvalues are `3` and `-2`.
- Using `trace(A) = 0` and `1 + m_3 + m_{-2} = 60`, the spectrum is
  `18^1, 3^20, (-2)^39`.
- The one-vertex partition `({x}, T, R)` with `R = V \\ ({x} ∪ T)` and `|R| = 41` is exactly equitable for out-neighbors:
  - `x` sends `11` edges to `T` and `7` to `R`,
  - every vertex of `T` sends `1` edge to `x`, `6` to `T`, and `11` to `R`,
  - every vertex of `R` sends `0` to `x`, `5` to `T`, and `13` to `R`.
- So the exact quotient matrix is
  ```text
  Q_T =
  [0 11  7]
  [1  6 11]
  [0  5 13]
  ```
  and it has eigenvalues `18, 3, -2`, matching the global spectrum.
- The spectral projectors are also explicit:
  - `P_3 = (-J + 6I + 3A) / 15`,
  - `P_-2 = (J + 12I - 4A) / 20`.
- Equivalently, the matrices
  - `K_3 = -J + 6I + 3A`,
  - `K_-2 = J + 12I - 4A`
  have ranks `20` and `39` and entries
  - for `K_3`: diagonal `5`, arc `2`, nonarc `-1`,
  - for `K_-2`: diagonal `13`, arc `-3`, nonarc `1`.

What this gives:
- an exact local quotient around every vertex,
- a clean spectral package that explains why the tuple is rigid,
- but no contradiction by itself.

Self-check:
- All formulas above come directly from `A^2 = 6I + A + 5J`.
- I do not see a way to turn the projector package into an unconditional obstruction yet.

## approach_B
Construction / extremal / contradiction route.

Start with the full `5`-cell partition `M,O,I,N` around `x`. The dsrg rules force the following exact block totals.

From targets receiving edges from `S = M ∪ O`:
- `e(M,M) + e(O,M) = 66`
- `e(M,O) + e(O,O) = 42`
- `e(M,I) + e(O,I) = 35`
- `e(M,N) + e(O,N) = 170`

From sources sending edges into `T = M ∪ I`:
- `e(M,M) + e(M,I) = 66`
- `e(O,M) + e(O,I) = 35`
- `e(I,M) + e(I,I) = 42`
- `e(N,M) + e(N,I) = 170`

From row and column sums inside the partition:
- `e(M,O) + e(M,N) = 121`
- `e(O,O) + e(O,N) = 91`
- `e(I,O) + e(I,N) = 77`
- `e(N,O) + e(N,N) = 442`
- `e(I,M) + e(N,M) = 121`
- `e(I,O) + e(N,O) = 77`
- `e(I,I) + e(N,I) = 91`
- `e(I,N) + e(N,N) = 442`

These equations can be parameterized by four free nonnegative integers:
- let `a = e(M,M)`, `b = e(M,O)`, `d = e(I,M)`, `s = e(I,O)`,
- then
  - `e(M,I) = 66 - a`,
  - `e(O,M) = 66 - a`,
  - `e(O,I) = a - 31`,
  - `e(O,O) = 42 - b`,
  - `e(M,N) = 121 - b`,
  - `e(O,N) = 49 + b`,
  - `e(I,I) = 42 - d`,
  - `e(N,M) = 121 - d`,
  - `e(N,I) = 49 + d`,
  - `e(I,N) = 77 - s`,
  - `e(N,O) = 77 - s`,
  - `e(N,N) = 365 + s`.
- The only immediate bounds are `31 <= a <= 66`, `0 <= b <= 42`, `0 <= d <= 42`, and `0 <= s <= 77`.

So the aggregate `M,O,I,N` block-total system is consistent. For example,
- `a = 31`, `b = 0`, `d = 0`, `s = 0`
gives a nonnegative exact solution to all displayed aggregate equations.

Self-check:
- This is the same kind of block-total bookkeeping that closed `dsrg-91-12-6-5-1`, but here it does not force a contradiction.
- Recording an explicit feasible aggregate solution is important because it prevents a fake disproof.

## lemma_graph
1. Lock the exact matrix identity `A^2 = 6I + A + 5J`.
2. Use it to derive the spectrum `18^1, 3^20, (-2)^39`.
3. Fix a vertex `x` and derive the exact equitable `3`-cell quotient `Q_T` on `({x}, T, R)`.
4. Refine to the `5`-cell partition `M,O,I,N` and write the exact unconditional block-total system.
5. Observe that this aggregate system remains consistent, so the first local contradiction route fails.
6. Test the strongest natural refinement next: assume the `5`-cell partition is out-equitable.
7. Under that extra uniformity assumption, derive an integer contradiction.
8. Finally test a slightly stronger aggregate model with mutual-pair bookkeeping; it is still feasible, so no exact contradiction emerges at that level either.

Self-check:
- Steps `1` through `5` are unconditional.
- Step `7` is only conditional on out-equitability.
- Step `8` is a bounded local feasibility check, not a global graph search.

## chosen_plan
- The best path is still the local partition route, but it must be reported conservatively.
- The exact unconditional output from this pass is:
  - the spectrum and projector package,
  - the exact `3`-cell quotient `Q_T`,
  - the full unconditional `5`-cell block-total system,
  - and a proof that the most obvious extra regularity hypothesis, namely out-equitability of `M,O,I,N`, is impossible.

Conditional obstruction under the extra out-equitable assumption:
- Suppose every source class has constant out-counts to the target classes:
  - `M : (a,b,c,d)`
  - `O : (e,f,g,h)`
  - `I : (p,q,r,s)`
  - `N : (u,v,w,z)`
- Then the dsrg equations force
  - `a + c = 6`,
  - `e + g = 5`,
  - `11a + 7e = 66`,
  - `11b + 7f = 42`,
  - `11c + 7g = 35`,
  - `11d + 7h = 170`.
- Solving gives
  - `a = 6`, `c = 0`,
  - `e = 0`, `g = 5`,
  - `b = 0`, `f = 6`,
  - `d = 11`, `h = 7`.
- Now the target-`M` indegree count gives
  `11a + 7e + 7p + 34u = 187`,
  so
  `7p + 34u = 121`.
- But `p + r = 6` and `u + w = 5` force `0 <= p <= 6` and `0 <= u <= 5`, and no such pair solves `7p + 34u = 121`.
- Therefore the natural out-equitable `5`-cell refinement is impossible.

I also tested a slightly stronger aggregate model that introduces mutual-pair counts between the ten unordered cell pairs. That bounded exact search still found feasible local data, so even that strengthened bookkeeping does not by itself rule out the dsrg.

Self-check:
- The out-equitable contradiction is real, but it depends on an extra hypothesis not forced by the dsrg axioms.
- The final bounded computation was used to avoid overstating the strength of the aggregate obstruction.

## self_checks
- Statement check: the artifact stays on the exact tuple `(60,18,11,6,5)`.
- Faithfulness check: every unconditional equation displayed above comes directly from the dsrg walk counts and degree constraints.
- Conservatism check: the aggregate `5`-cell system is recorded as consistent, and even the slightly strengthened mutual-pair aggregate model remains feasible.
- Scope check on the computation: the code only searched a small local integer system; it did not search adjacency matrices or run SAT, ILP, or CP-SAT.
- Lean check: Lean remains off because there is no exact proof or exact counterexample yet.

## code_used
- Yes, but only minimally and only after the two handwritten routes above were exhausted.
- The code was a tiny exact feasibility search for the strengthened local model obtained by adding mutual-pair variables to the `M,O,I,N` aggregate bookkeeping.
- That bounded search found a feasible local solution, so it served as a falsifier for the hoped-for aggregate contradiction rather than as a construction search.
- No SAT, ILP, CP-SAT, or global brute force over graphs was used.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Exact output from this pass:
  - the matrix identity is `A^2 = 6I + A + 5J`,
  - the spectrum is forced to be `18^1, 3^20, (-2)^39`,
  - every vertex gives an exact equitable `3`-cell quotient
    `Q_T = [[0,11,7],[1,6,11],[0,5,13]]`,
  - the finer `5`-cell block-total system around a vertex is consistent,
  - the strongest natural local uniformity hypothesis tested by hand, out-equitability of `M,O,I,N`, is impossible,
  - even a modestly strengthened local aggregate model with mutual-pair bookkeeping is still feasible.
- I do not currently have an exact construction or an exact contradiction for the intended statement.

## likely_failure_points
- The main gap is structural: the clean contradiction appears only after imposing out-equitability, and the dsrg axioms do not force that.
- The spectral projector package is exact, but I did not find the missing bridge from rank information to a contradiction.
- A genuine witness could still exist with highly nonuniform local profiles even though the naive uniform model fails.

## what_verify_should_check
- Recompute the normalization `A^2 = 6I + A + 5J` and the spectrum `18^1, 3^20, (-2)^39`.
- Recheck the exact quotient `Q_T = [[0,11,7],[1,6,11],[0,5,13]]` on the partition `({x}, T, R)`.
- Recheck the unconditional `5`-cell block-total equations and the four-parameter consistency package.
- Confirm that the out-equitable contradiction really depends on the extra uniformity assumption and does not settle the dsrg by itself.
- Rerun the tiny local feasibility search with mutual-pair variables and verify that it indeed has feasible solutions.

## verify_rediscovery
- PASS 1 used a bounded web audit only.
- Checked the exact tuple notation and family notation against the canonical source and tuple searches.
- The canonical Hobart-Brouwer dsrg table still lists `(60,18,11,6,5)` with `?`, and the companion constructions/nonexistence page does not display an exact theorem, proposition, example, observation, corollary, or construction settling this tuple.
- Within the search budget, I did not find a later paper or discussion explicitly resolving the exact instance `(60,18,11,6,5)`.
- Verdict for PASS 1: no rediscovery established within budget. This is only a bounded audit, not a proof of novelty.

## verify_faithfulness
- The artifact is faithful to the intended statement in `selected_problem.md`: it stays on the exact existential question for dsrg parameters `(60,18,11,6,5)`.
- There is no wrong-theorem drift in the solve result. The record explicitly says it does not prove existence or nonexistence, and labels the output as `PARTIAL`.
- The only proved contradiction in the record is conditional on an extra out-equitable `5`-cell hypothesis, and the record states that dependence clearly. So there is no hidden upgrade from a conditional obstruction to an exact disproof.

## verify_proof
- I rechecked the normalization and it is correct:
  `A^2 = 11I + 6A + 5(J - I - A) = 6I + A + 5J`.
- On the orthogonal complement of `J`, the restricted polynomial is `u^2 - u - 6 = (u-3)(u+2)`, so the restricted eigenvalues are `3` and `-2`.
- Using `trace(A)=0` and `1 + m_3 + m_{-2} = 60`, the multiplicities are forced to be `m_3 = 20` and `m_{-2} = 39`.
- The claimed quotient matrix
  ```text
  Q_T =
  [0 11  7]
  [1  6 11]
  [0  5 13]
  ```
  is correct, and its eigenvalues are indeed `18,3,-2`.
- The unconditional `M,O,I,N` aggregate equations and the displayed four-parameter parametrization are algebraically consistent. The sample choice `a=31, b=0, d=0, s=0` gives a nonnegative exact solution to those aggregate constraints.
- The conditional out-equitable contradiction also checks out: the forced values are `a=6, c=0, e=0, g=5, b=0, f=6, d=11, h=7`, and then `7p + 34u = 121` has no solution with `0 <= p <= 6`, `0 <= u <= 5`.
- First incorrect step found: none in the stated partial argument. The proof remains incomplete because the final contradiction uses an extra hypothesis not implied by the dsrg axioms.

## verify_adversarial
- There is no checker or witness file under this slug, so PASS 4 reduced to adversarial recomputation of the handwritten identities.
- I reran the key arithmetic checks locally:
  - multiplicities `20` and `39`,
  - quotient eigenvalues `18,3,-2`,
  - aggregate right-hand sides `66,42,35,170` and row remainders `121,91,77,442`,
  - feasibility of the displayed aggregate assignment,
  - infeasibility of the conditional out-equitable completion.
- These computations support the record's conservative conclusion: the local aggregate model is feasible, while the stronger out-equitable model is impossible.
- No computation in the artifact currently supports an existence proof, a nonexistence proof, or Lean readiness.

## verify_verdict
- `UNVERIFIED`
- Classification remains `PARTIAL`.
- Reason: the recorded derivations appear correct as partial structure, but they do not settle the exact intended existence statement, and PASS 1 did not establish rediscovery.
- `lean_ready = false` because there is no exact theorem or exact counterexample to formalize.

## minimal_repair_if_any
- No mathematical repair was needed.
- The only conservative repair is interpretive: keep the run explicitly labeled `PARTIAL` / `UNVERIFIED`, and do not promote the conditional out-equitable contradiction into an exact nonexistence claim.
