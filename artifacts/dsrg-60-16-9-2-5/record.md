# dsrg-60-16-9-2-5

## statement_lock
- Active slug: `dsrg-60-16-9-2-5`
- Title: `Does a directed strongly regular graph with parameters (60,16,9,2,5) exist?`
- Locked intended statement: there exists a loopless directed graph on `60` vertices with constant indegree and outdegree `16` whose adjacency matrix `A` satisfies
  `AJ = JA = 16J` and
  `A^2 = 9I + 2A + 5(J - I - A) = 4I - 3A + 5J`.
- Equivalent walk formulation used below:
  - every vertex has exactly `9` mutual neighbors,
  - every arc `x -> y` lies on exactly `2` directed `2`-paths `x -> z -> y`,
  - every nonarc `x -/-> y` with `x != y` lies on exactly `5` directed `2`-paths `x -> z -> y`.

Self-check:
- This is the exact existential statement from `selected_problem.md`, not a variant.
- I am not claiming rediscovery or exact nonexistence in solve stage.

## definitions
- Fix a vertex `x`.
- Let `S = N^+(x)` and `T = N^-(x)`, so `|S| = |T| = 16`.
- Write
  - `M = S ∩ T`, so `|M| = 9`,
  - `O = S \ T`, so `|O| = 7`,
  - `I = T \ S`, so `|I| = 7`,
  - `N = V \ ({x} ∪ M ∪ O ∪ I)`, so `|N| = 36`.
- For classes `C,D` among `M,O,I,N`, let `e(C,D)` be the number of directed edges from `C` to `D`.
- Also set `R = V \ ({x} ∪ T)`, so `|R| = 43`.

Two exact translations used repeatedly:
- If `y ∈ T`, then `|N^+(y) ∩ T| = 2`; if `y ∉ T` and `y != x`, then `|N^+(y) ∩ T| = 5`.
- If `y ∈ S`, then `|N^-(y) ∩ S| = 2`; if `y ∉ S` and `y != x`, then `|N^-(y) ∩ S| = 5`.

Self-check:
- The partition sizes are forced by `k = 16` and `t = 9`.
- The two translation bullets are direct restatements of the dsrg `2`-path rule.

## approach_A
Structural / invariant route.

- The nontrivial eigenvalues come from
  `u^2 + 3u - 4 = 0`,
  so they are `1` and `-4`.
- Using `trace(A) = 0` and `1 + m_1 + m_{-4} = 60`, the spectrum is
  `16^1, 1^44, (-4)^15`.
- Rearranging the quadratic identity gives
  `(A - I)^2 = 5(J - A + I)`.
  In particular, modulo `5`,
  `(A - I)^2 ≡ 0`.
- There is also an exact equitable `3`-cell quotient around any fixed vertex `x` for the partition
  `({x}, T, R)` with `|T| = 16`, `|R| = 43`:
  - `x` sends `9` edges to `T` and `7` to `R`,
  - every vertex of `T` sends `1` edge to `x`, `2` to `T`, and `13` to `R`,
  - every vertex of `R` sends `0` to `x`, `5` to `T`, and `11` to `R`.
- So the exact quotient matrix is
  ```text
  Q_T =
  [0 9  7]
  [1 2 13]
  [0 5 11]
  ```
  and it has eigenvalues `16, 1, -4`, matching the global spectrum.

What this gives:
- a rigid exact local package that is genuinely forced by the dsrg axioms,
- but no contradiction by itself.

Self-check:
- The quotient above is exact, not heuristic.
- The modular identity `(A - I)^2 ≡ 0 (mod 5)` is correct, but I do not yet know how to force a contradiction from it.

## approach_B
Construction / extremal / contradiction route.

Start with the full `5`-cell partition `M,O,I,N` around `x`. Let
- `a = e(M,M)`, `b = e(M,O)`, `c = e(M,I)`, `d = e(M,N)`,
- `e = e(O,M)`, `f = e(O,O)`, `g = e(O,I)`, `h = e(O,N)`,
- `p = e(I,M)`, `q = e(I,O)`, `r = e(I,I)`, `s = e(I,N)`,
- `u = e(N,M)`, `v = e(N,O)`, `w = e(N,I)`, `z = e(N,N)`.

The dsrg rules force the following exact block totals.

From targets receiving edges from `S = M ∪ O`:
- `a + e = 18`
- `b + f = 14`
- `c + g = 35`
- `d + h = 180`

From sources sending edges into `T = M ∪ I`:
- `a + c = 18`
- `e + g = 35`
- `p + r = 14`
- `u + w = 180`

From outdegree totals inside the partition:
- `a + b + c + d = 135`
- `e + f + g + h = 112`
- `p + q + r + s = 105`
- `u + v + w + z = 576`

From indegree totals inside the partition:
- `a + e + p + u = 135`
- `b + f + q + v = 105`
- `c + g + r + w = 112`
- `d + h + s + z = 576`

Useful consequences:
- `e = c`
- `b + d = 117`
- `f + h = 77`
- `q + s = 91`
- `r + w = 77`

This system is consistent at the block-total level. So the simple hope of a contradiction from aggregate `M,O,I,N` counts alone fails.

Self-check:
- I explicitly stopped short of a false contradiction here.
- This is the main reason the solve verdict stays conservative.

## lemma_graph
1. Lock the exact matrix identity `A^2 = 4I - 3A + 5J`.
2. Fix a vertex `x` and derive the exact `3`-cell quotient `({x}, T, R)` with quotient matrix `Q_T`.
3. Refine to the `5`-cell partition `M,O,I,N` and write the exact block-total equations above.
4. Observe that those aggregate equations remain consistent, so the first local contradiction route fails.
5. Test the strongest natural refinement next: assume the `5`-cell partition is out-equitable, meaning every vertex in a given class has the same number of out-neighbors in each other class.
6. Under that extra uniformity assumption, derive an integer contradiction.

Self-check:
- Steps `1` through `4` are unconditional.
- Step `6` is conditional and is recorded that way below.

## chosen_plan
- The best unconditional output from this solve pass is the exact `3`-cell quotient plus the consistent `5`-cell total system.
- After the two handwritten routes stalled, I used one tiny exact computation only to test the narrowest next hypothesis: whether the `5`-cell partition could be out-equitable.
- That hypothesis fails, but the failure is only a partial obstruction because the dsrg axioms do not force `M,O,I,N` itself to be equitable.

Conditional obstruction under the extra out-equitable assumption:
- Suppose each source class has constant out-counts to the target classes:
  - `M : (a,b,c,d)`
  - `O : (e,f,g,h)`
  - `I : (p,q,r,s)`
  - `N : (u,v,w,z)`
- Then
  - `a + c = 2`, `e + g = 5`, `p + r = 2`, `u + w = 5`,
  - `9a + 7e = 18`, `9b + 7f = 14`, `9c + 7g = 35`, `9d + 7h = 180`.
- The first four equations force
  - `a = 2`, `c = 0`,
  - `e = 0`, `g = 5`,
  - `b = 0`, `f = 2`,
  - `d = 13`, `h = 9`.
- Now the target-`M` indegree total gives
  `9a + 7e + 7p + 36u = 135`,
  so
  `7p + 36u = 117`.
- But `p + r = 2` and `u + w = 5` force `0 <= p <= 2` and `0 <= u <= 5`, and no such pair solves `7p + 36u = 117`.
- Therefore the natural out-equitable `5`-cell refinement is impossible.

Self-check:
- This is a real obstruction, but only under an extra regularity assumption.
- I am not upgrading that conditional contradiction into a full nonexistence proof.

## self_checks
- Statement check: the artifact stays on the exact tuple `(60,16,9,2,5)`.
- Faithfulness check: all unconditional equations come directly from the dsrg walk counts and degree constraints.
- Conservatism check: the aggregate `5`-cell system is recorded as consistent, so no fake disproof is being smuggled in.
- Scope check on the computation: the tiny script only verified that the conditional out-equitable refinement has no integer solution; it was not a graph search.
- Lean check: Lean remains off because there is no exact proof or exact counterexample yet.

## code_used
- Yes, but only minimally and only after the two handwritten routes above were exhausted.
- The code was a tiny exact integer-feasibility check for the conditional out-equitable `5`-cell refinement. It searched the small integer parameter space for
  `(a,b,c,d),(e,f,g,h),(p,q,r,s),(u,v,w,z)`
  satisfying the conditional equations and found `0` solutions.
- No SAT, ILP, CP-SAT, or global graph search was used.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Exact output from this pass:
  - the spectrum is forced to be `16^1, 1^44, (-4)^15`,
  - every vertex gives an exact equitable `3`-cell quotient `Q_T = [[0,9,7],[1,2,13],[0,5,11]]` for the partition `({x}, T, R)`,
  - the finer `5`-cell block-total system around `x` is consistent,
  - the simplest natural strengthening of that local picture, namely an out-equitable `5`-cell partition `M,O,I,N`, is impossible.
- I do not currently have an exact construction or an exact contradiction for the intended statement.

## likely_failure_points
- The main gap is structural: the `5`-cell partition need not be equitable, so the clean contradiction there is only conditional.
- The modular identity `(A - I)^2 ≡ 0 (mod 5)` may hide a stronger obstruction, but I did not close it.
- A genuine witness could exist with highly nonuniform local profiles even though the naive equitable model fails.

## what_verify_should_check
- Recompute the matrix identity `A^2 = 4I - 3A + 5J` and the spectrum `16^1, 1^44, (-4)^15`.
- Recheck the exact quotient `Q_T` on the partition `({x}, T, R)`.
- Recheck the unconditional `5`-cell block-total equations and confirm that they are consistent.
- Confirm that the conditional contradiction really depends on the extra out-equitable assumption and does not by itself settle the dsrg.
- Rerun the tiny integer-feasibility script, or just rederive the forced values
  `a=2,e=0,c=0,g=5,b=0,f=2,d=13,h=9`
  and the impossible equation `7p + 36u = 117` with `0 <= p <= 2`, `0 <= u <= 5`.

## verify_rediscovery
- PASS 1 used a bounded live web audit focused on the exact tuple `(60,16,9,2,5)`, alternative dsrg notation, the canonical Hobart-Brouwer table, and whether the same source or nearby literature already contains a theorem, proposition, example, observation, or corollary settling this exact instance.
- The canonical source still lists `(60,16,9,2,5)` with `?`, and its complement tuple `(60,43,36,31,30)` also remains `?`.
- Within the search budget, I did not find a later paper or database entry explicitly constructing this exact dsrg or proving exact nonexistence for this tuple.
- So rediscovery is not established. This remains a frontier-status instance as far as the bounded audit could determine.

## verify_faithfulness
- The solve artifact stays faithful to the intended statement. It does not claim existence, nonexistence, or a nearby parameter variant.
- The local partition definitions, the exact `3`-cell quotient `Q_T = [[0,9,7],[1,2,13],[0,5,11]]`, and the `5`-cell block-total equations are all presented as consequences of the dsrg axioms for the exact tuple `(60,16,9,2,5)`.
- The only obstruction claimed beyond those unconditional consequences is explicitly labeled conditional on an extra out-equitable hypothesis for the `M,O,I,N` partition.
- I found no wrong-theorem drift, quantifier drift, or definition drift.

## verify_proof
- First incorrect step found: none in the claims actually made.
- The algebraic normalization `A^2 = 4I - 3A + 5J` is correct.
- The spectrum claim `16^1, 1^44, (-4)^15` is consistent with the quadratic relation, trace `0`, and `trace(A^2) = vt = 540`.
- The quotient matrix `Q_T` has eigenvalues `16, 1, -4`, matching the claimed local quotient picture.
- The unconditional `5`-cell aggregate system is genuinely consistent; for example,
  `a=0,b=0,c=18,d=117,e=18,f=14,g=17,h=63,p=14,q=0,r=0,s=91,u=103,v=91,w=77,z=305`
  satisfies all displayed block-total equations.
- The conditional obstruction is also correct as stated: under out-equitability the equations force
  `a=2,c=0,e=0,g=5,b=0,f=2,d=13,h=9`, and then the target-`M` indegree count gives
  `7p + 36u = 117`, impossible with `p + r = 2` and `u + w = 5`.
- The important verification conclusion is therefore not that the dsrg is impossible, but only that the current artifact remains a sound partial analysis.

## verify_adversarial
- There is no witness matrix and no standalone checker file in this artifact directory, so there was no graph certificate to rerun.
- I reran small exact computations instead:
  - the quotient matrix numerically has eigenvalues `-4, 1, 16`,
  - the aggregate `5`-cell system admits explicit integer solutions, confirming that no unconditional contradiction was proved there,
  - the conditional out-equitable subsystem has no integer solution.
- I also tried to break the writeup by reading it as if it asserted full nonexistence. That attack fails because the record repeatedly and correctly says the contradiction is only conditional.

## verify_verdict
- `UNVERIFIED`
- Reason: the record appears mathematically sound and faithful, but it does not prove or disprove the exact intended statement. No rediscovery was established, yet there is still no exact witness and no unconditional contradiction.
- Classification remains `PARTIAL`, not `EXACT`, `COUNTEREXAMPLE`, or `REDISCOVERY`.
- `lean_ready = false` because Lean should not be used on a merely conditional obstruction or a partial local analysis.

## minimal_repair_if_any
- No mathematical repair was needed.
- Editorially, the artifact is already careful enough. If it is touched later, the only conservative improvement would be to make the phrase "conditional on out-equitability" even more visually prominent near the result summary.
