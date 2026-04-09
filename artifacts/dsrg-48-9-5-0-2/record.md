# dsrg-48-9-5-0-2

## statement_lock
- Active slug: `dsrg-48-9-5-0-2`
- Title: `Does a directed strongly regular graph with parameters (48,9,5,0,2) exist?`
- Locked intended statement for this solve pass: determine whether a loopless directed strongly regular graph with parameters
  `(v,k,t,lambda,mu) = (48,9,5,0,2)` exists.
- Exact adjacency-matrix form:
  `AJ = JA = 9J`
  and
  `A^2 = tI + lambda A + mu(J - I - A) = 5I + 2(J - I - A) = 2J + 3I - 2A`.
- Equivalent walk formulation:
  - every vertex has indegree and outdegree `9`,
  - every vertex has exactly `5` mutual neighbors,
  - every arc `x -> y` lies on exactly `0` directed `2`-paths `x -> z -> y`,
  - every nonarc `x -/-> y` with `x != y` lies on exactly `2` directed `2`-paths `x -> z -> y`.
- Let `B := A + I`. Then `B` is a `0/1` matrix with row and column sums `10` and
  `B^2 = A^2 + 2A + I = 4I + 2J`.
- On `1^\perp`, the quadratic is `u^2 + 2u - 3 = 0`, so the restricted eigenvalues are `1` and `-3`.
- Using `trace(A) = 0` and `1 + m_1 + m_{-3} = 48`, the spectrum is forced to be
  `9^1, 1^33, (-3)^14`.
- Hence `B` has spectrum `10^1, 2^33, (-2)^14`, so `B` is invertible with
  `B^(-1) = (1/4)B - (1/20)J`.

Self-check:
- The locked statement matches the exact intended tuple.
- The spectral multiplicities satisfy both the trace constraint and the total dimension `48`.

## definitions
- Fix a vertex `x`.
- Let `U = N^+(x)` and `T = N^-(x)`, so `|U| = |T| = 9`.
- Write
  - `C = U ∩ T`, so `|C| = 5`,
  - `O = U \ T`, so `|O| = 4`,
  - `I = T \ U`, so `|I| = 4`,
  - `N = V \ ({x} ∪ C ∪ O ∪ I)`, so `|N| = 34`.

Exact local translations forced by `lambda = 0`:
- If `y ∈ U`, then no vertex of `U` points to `y`, because any `x -> z -> y` would be a forbidden `2`-path along the arc `x -> y`.
- If `y ∈ T`, then `y` points to no vertex of `T`, because any `y -> z -> x` would be a forbidden `2`-path along the arc `y -> x`.
- If `y ∈ T` and `z ∈ U`, then `y -> z` is impossible, because `y -> x -> z` already gives a directed `2`-path from `y` to `z`.

Consequences:
- There are no arcs from `U` to `U`.
- There are no arcs from `T` to `T`.
- There are no arcs from `T` to `U`.
- Therefore:
  - every `c ∈ C` sends exactly `1` edge to `x` and `8` to `N`,
  - every `o ∈ O` sends exactly `2` edges to `I` and `7` to `N`,
  - every `i ∈ I` sends exactly `1` edge to `x` and `8` to `N`.
- Dually:
  - every `c ∈ C` receives exactly `1` edge from `x` and `8` from `N`,
  - every `o ∈ O` receives exactly `1` edge from `x` and `8` from `N`,
  - every `i ∈ I` receives exactly `2` edges from `O` and `7` from `N`.

Useful exact block totals:
- `e(C,N) = 40`, `e(O,I) = 8`, `e(O,N) = 28`, `e(I,N) = 32`.
- `e(N,C) = 40`, `e(N,O) = 32`, `e(N,I) = 28`, `e(N,N) = 206`.

Self-check:
- The partition sizes are forced by `k = 9` and `t = 5`.
- The row profiles for `C`, `O`, and `I` are exact consequences of `lambda = 0`, not extra hypotheses.

## approach_A
Structural / invariant route.

Major step 1: algebraic package from the quadratic identity.
- The shifted matrix `B = A + I` satisfies `B^2 = 4I + 2J`.
- Hence `B` is invertible and `B^(-1) = (1/4)B - (1/20)J`.
- Also
  `A^3 = A(2J + 3I - 2A) = 18J + 3A - 2(2J + 3I - 2A) = 14J + 7A - 6I`.
- Therefore every diagonal entry of `A^3` is `14 - 6 = 8`, so the digraph would contain exactly
  `trace(A^3) / 3 = 48 * 8 / 3 = 128`
  directed `3`-cycles, hence exactly `8` through each vertex.
- At the base vertex `x`, these `8` triangles are exactly the triangles `x -> o -> i -> x`, so the `O -> I` bipartite block is `2`-regular on each side.

Self-check:
- The cubic identity is a direct substitution into `A^2 = 2J + 3I - 2A`.
- The triangle count agrees with the already-derived total `e(O,I) = 8`.

Major step 2: the natural five-cell out-equitable model is impossible.
- Because the rows on `C`, `O`, and `I` are already exact, the only possible source of uniformity failure is the `N` block.
- If the full partition `({x}, C, O, I, N)` were out-equitable, then every `n ∈ N` would have to send constant numbers of edges into `C`, `O`, `I`, and `N`.
- But the exact totals force those constants to be
  - `40 / 34 = 20 / 17` into `C`,
  - `32 / 34 = 16 / 17` into `O`,
  - `28 / 34 = 14 / 17` into `I`,
  - `206 / 34 = 103 / 17` into `N`,
  which are not integers.
- So any actual witness would have to be locally nonuniform on the `34`-vertex residual block `N`.

Self-check:
- This is a genuine obstruction, but only against the most naive local-quotient model.
- It does not by itself prove global nonexistence.

## approach_B
Construction / extremal / contradiction route: rule out all Cayley realizations.

Major step 1: translate `B^2 = 4I + 2J` into the group ring.
- Assume for contradiction that the digraph is a Cayley digraph on a finite group `G` of order `48`.
- Let `S ⊂ G \ {e}` be the connection set, so `|S| = 9`.
- Let `D := {e} ∪ S`, so `|D| = 10`.
- In the left-regular representation, the matrix of `D` is exactly `B = A + I`.
- Therefore the exact matrix identity `B^2 = 4I + 2J` becomes the group-ring identity
  `D^2 = 4e + 2G`,
  where `G` on the right denotes the formal sum of all group elements.

Self-check:
- The principal character check is exact:
  `|D|^2 = 10^2 = 100 = 4 + 2 * 48`.

Major step 2: apply irreducible representations and regular traces.
- For the trivial representation, `rho(D) = 10`.
- For every nontrivial irreducible representation `rho` of degree `d_rho`, one has `rho(G) = 0`, hence
  `rho(D)^2 = 4 I_(d_rho)`.
- Taking traces in the regular representation:
  - from the coefficient of `e` in `D^2`, one gets
    `tr_reg(D^2) = 48 * 4 = 192`,
  - but decomposing the regular representation into irreducibles gives
    `tr_reg(D^2) = 10^2 + sum_(rho != 1) d_rho tr(4 I_(d_rho))`
    `= 100 + 4 sum_(rho != 1) d_rho^2`
    `= 100 + 4(48 - 1) = 288`.
- This contradiction proves that no Cayley realization exists for the tuple `(48,9,5,0,2)`.

Self-check:
- This uses only the exact identity `D^2 = 4e + 2G` and the standard decomposition of the regular representation.
- Unlike the flawed Frobenius-norm route used elsewhere, this contradiction is trace-based and does not assume normality.

## lemma_graph
1. Lock the exact dsrg identity `A^2 = 2J + 3I - 2A`.
2. Pass to `B := A + I` and obtain `B^2 = 4I + 2J`, the spectrum `10^1, 2^33, (-2)^14`, and `B^(-1) = (1/4)B - (1/20)J`.
3. Fix a vertex `x` and partition `V` into `x`, `C`, `O`, `I`, `N`.
4. Use `lambda = 0` to prove:
   - `U -> U` is empty,
   - `T -> T` is empty,
   - `T -> U` is empty,
   and therefore derive the exact source profiles for `C`, `O`, and `I`.
5. Compute `A^3 = 14J + 7A - 6I`, hence exactly `128` directed `3`-cycles.
6. Observe that the natural five-cell out-equitable model is impossible because the forced `N`-row averages are nonintegral.
7. Test the strongest clean construction family available at solve stage: Cayley realizations.
8. Translate `B^2 = 4I + 2J` into `D^2 = 4e + 2G` and close that route by the regular-trace contradiction `192 = 288`.
9. Remaining gap: the problem is unresolved only for genuinely non-Cayley and locally nonuniform realizations.

## chosen_plan
- The cleanest exact theorem available in solve is the no-Cayley obstruction.
- The best unconditional local information is the fixed-vertex `C/O/I/N` decomposition: three of the four source cells have completely rigid row profiles, and the remaining `N` block cannot be uniform.
- That is enough to justify a conservative `VARIANT` classification, but not enough to claim full nonexistence.

Self-check:
- The record separates exact theorems from unresolved gaps.
- Lean should remain off because there is no exact proof or exact disproof of the intended statement.

## self_checks
- Statement fidelity: every claim stays on the exact tuple `(48,9,5,0,2)`.
- Spectral check: `A` has spectrum `9^1, 1^33, (-3)^14`, and `B = A + I` has spectrum `10^1, 2^33, (-2)^14`.
- Inverse check: `B((1/4)B - (1/20)J) = I`.
- Local check: the forbidden-arc consequences `U -> U = ∅`, `T -> T = ∅`, and `T -> U = ∅` force the displayed exact rows on `C`, `O`, and `I`.
- Triangle check: `A^3 = 14J + 7A - 6I` gives exactly `8` directed triangles through each vertex.
- Cayley check: the contradiction is the exact arithmetic `tr_reg(D^2) = 192` versus `tr_reg(D^2) = 288`.
- Conservatism check: the artifact does not upgrade a no-Cayley theorem into global nonexistence.

## code_used
- No code used.
- Reason: the strongest outputs in this solve pass were exact algebraic and representation-theoretic consequences, and I did not reach a point where a bounded experiment was necessary to justify them.

## result
- Solve-stage verdict: `VARIANT`
- Confidence: `medium`
- Strongest exact outputs from this pass:
  - the exact identity `A^2 = 2J + 3I - 2A`,
  - the forced spectrum `9^1, 1^33, (-3)^14`,
  - the shifted reformulation `B := A + I` with `B^2 = 4I + 2J` and `B^(-1) = (1/4)B - (1/20)J`,
  - the exact fixed-vertex forbidden-arc package `U -> U = ∅`, `T -> T = ∅`, `T -> U = ∅`,
  - the exact source profiles for the cells `C`, `O`, and `I`,
  - the exact directed-triangle count `128`,
  - the impossibility of the naive five-cell out-equitable model,
  - and the exact variant theorem that no Cayley dsrg with parameters `(48,9,5,0,2)` can exist.
- I did not prove global nonexistence and I did not produce a construction.
- Lean was intentionally left off.

## likely_failure_points
- The main unresolved mass of the problem is the `34`-vertex `N` block, where the dsrg axioms still allow nonuniform behavior.
- The no-Cayley theorem is mathematically exact but may still be a rediscovery of known general dsrg facts; solve cannot settle that with web off.
- A full disproof would need a sharper contradiction inside the non-Cayley `N`-block equations, not just the coarse local partition.

## what_verify_should_check
- Recompute the normalization `A^2 = 2J + 3I - 2A`, the spectra of `A` and `B`, and the inverse formula for `B`.
- Recheck the fixed-vertex deductions `U -> U = ∅`, `T -> T = ∅`, and `T -> U = ∅`, and verify the exact row profiles of `C`, `O`, and `I`.
- Recheck the triangle count from `A^3 = 14J + 7A - 6I`.
- Recheck the five-cell nonuniformity obstruction: the exact `N`-row averages are nonintegral, so the partition cannot be out-equitable.
- Audit the Cayley obstruction carefully:
  - for a Cayley witness, `B` really is the left-regular matrix of `D = {e} ∪ S`,
  - `B^2 = 4I + 2J` really becomes `D^2 = 4e + 2G`,
  - the regular-trace computation is exactly `192` on one side and `288` on the other.
- In the verify stage, check whether the no-Cayley theorem is already known in the literature and whether any sharper theorem already settles the full tuple.

## verify_rediscovery
- PASS 1 used a bounded web audit on 2026-04-09 with the required patterns: exact tuple notation `(48,9,5,0,2)`, alternative dsrg notation, the canonical Hobart-Brouwer source, same-source theorem / proposition / example / observation / corollary coverage, and one recent status-style check.
- Within the search budget, I did not find an exact-instance construction, exact-instance nonexistence theorem, or a same-source observation that already settles the full tuple.
- The canonical Hobart-Brouwer table still lists the exact row `(48,9,5,0,2)` with `?`, so PASS 1 does not establish rediscovery.
- I also did not find a source establishing the solver's stronger variant claim that no Cayley realization exists for this exact tuple.

## verify_faithfulness
- The solve writeup is faithful about the intended statement in one important sense: it does not claim a full solution of the existence question.
- Its positive mathematical target is instead a nearby variant statement, namely a claimed exact theorem that no Cayley realization exists for `(48,9,5,0,2)`.
- The local algebra package, fixed-vertex partition, triangle count, and five-cell nonuniformity observation are all stated for the exact tuple and match the definitions.
- So there is no wrong-tuple drift, but the solve-stage classification depends on a nearby variant theorem rather than the intended existence question itself.

## verify_proof
- First incorrect step found: `approach_B`, Major step 2.
- The record says that from `D^2 = 4e + 2G`, one gets `tr_reg(D^2) = 48 * 4 = 192` "from the coefficient of `e` in `D^2`".
- That is incorrect. In the left-regular representation, the matrix of `4e + 2G` is `4I + 2J`, and
  `tr(4I + 2J) = 4 * 48 + 2 * 48 = 288`,
  because `J` contributes `1` on every diagonal entry.
- Therefore the purported contradiction `192 = 288` disappears; both sides give `288`.
- As a result, the claimed exact theorem "no Cayley realization exists for this tuple" is unsupported.
- I did not find an earlier incorrect step in the basic dsrg algebra:
  - `A^2 = 2J + 3I - 2A`,
  - the spectrum `9^1, 1^33, (-3)^14`,
  - `B := A + I` with `B^2 = 4I + 2J`,
  - `B^(-1) = (1/4)B - (1/20)J`,
  - the forbidden-arc deductions `U -> U = ∅`, `T -> T = ∅`, `T -> U = ∅`,
  - the exact row profiles for `C`, `O`, and `I`,
  - the triangle identity `A^3 = 14J + 7A - 6I`,
  - and the observation that the five-cell partition cannot be out-equitable.
- But those verified pieces do not add up to an exact disproof or even a valid no-Cayley variant theorem.

## verify_adversarial
- There was no checker or witness file to rerun.
- I reran the decisive arithmetic adversarially in plain Python:
  - `trace(4I + 2J) = 4*48 + 2*48 = 288`,
  - while the irreducible-decomposition side in the solve writeup also gives `10^2 + 4*(48 - 1) = 288`.
- This directly breaks the claimed contradiction and confirms that the main variant result does not survive skeptical checking.
- I did not find an adversarial issue with the verified local identities, but they remain only partial structural information.

## verify_verdict
- `CRITICAL_FLAW`
- PASS 1 did not establish rediscovery of the exact intended statement.
- PASS 2 found no statement drift on the tuple itself, but the solve-stage output rests on a nearby variant claim.
- PASS 3 found a fatal error in that variant proof: the trace of `4I + 2J` was computed incorrectly.
- PASS 4 confirmed the failure numerically.
- The surviving content is partial: exact local consequences of the dsrg equations, not a proof or disproof of existence and not a valid no-Cayley theorem.
- `lean_ready = false` because there is no longer any exact candidate theorem strong enough to formalize as a frontier-novel stop condition.

## minimal_repair_if_any
- Tiny conservative repair only: remove the unsupported sentence claiming an exact no-Cayley theorem for `(48,9,5,0,2)`.
- The artifact can still retain the verified algebraic package and local block-structure deductions as `PARTIAL` information.
- No tiny repair recovers the advertised `VARIANT` result; a new argument would be required.
