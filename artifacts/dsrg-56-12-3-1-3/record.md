# dsrg-56-12-3-1-3

## statement_lock
- Active slug: `dsrg-56-12-3-1-3`
- Title: `Does a directed strongly regular graph with parameters (56,12,3,1,3) exist?`
- Locked intended statement for this solve pass: determine whether a loopless directed strongly regular graph with parameters
  `(v,k,t,lambda,mu) = (56,12,3,1,3)` exists.
- Equivalent adjacency-matrix form: for the `56 x 56` adjacency matrix `A`,
  `AJ = JA = 12J` and
  `A^2 = tI + lambda A + mu(J - I - A) = 3I + A + 3(J - I - A) = 3J - 2A`.
- So:
  - every vertex has indegree and outdegree `12`,
  - every vertex has exactly `3` mutual neighbors,
  - for every arc `x -> y`, there is exactly `1` directed `2`-path `x -> z -> y`,
  - for every nonarc `x -/-> y` with `x != y`, there are exactly `3` directed `2`-paths `x -> z -> y`.
- On `1^\perp`, the quadratic is `u^2 + 2u = 0`, so the restricted eigenvalues are `0` and `-2`.
- Using `trace(A) = 0` and `1 + m_0 + m_{-2} = 56`, the spectrum is forced to be
  `12^1, 0^49, (-2)^6`.
- In particular, `rank(A) = 7`.

Self-check:
- The locked matrix identity matches the exact intended tuple.
- The spectrum and rank follow directly from the quadratic and `trace(A) = 0`.

## definitions
- Fix a vertex `x`.
- Let `U = N^+(x)` and `T = N^-(x)`, so `|U| = |T| = 12`.
- Write
  - `C = U ∩ T`, so `|C| = 3`,
  - `O = U \ T`, so `|O| = 9`,
  - `I = T \ U`, so `|I| = 9`,
  - `N = V \ ({x} ∪ C ∪ O ∪ I)`, so `|N| = 34`.
- Let `R = V \ ({x} ∪ T)`, so `|R| = 43`.
- Let `B = J - I - A`, the `0/1` matrix of nonarcs. Then `BJ = JB = 43J`.

Exact translations used below:
- If `y ∈ T`, then `|N^+(y) ∩ T| = 1`; if `y ∉ T` and `y != x`, then `|N^+(y) ∩ T| = 3`.
- Dually, if `y ∈ U`, then `|N^-(y) ∩ U| = 1`; if `y ∉ U` and `y != x`, then `|N^-(y) ∩ U| = 3`.
- Therefore every vertex of `T` sends exactly `1` edge into `T`, every vertex of `R` sends exactly `3` edges into `T`, every vertex of `U` receives exactly `1` edge from `U`, and every vertex outside `U ∪ {x}` receives exactly `3` edges from `U`.

Self-check:
- The partition sizes are forced by `k = 12` and `t = 3`.
- The translation bullets are just the dsrg `2`-path rule specialized to the fixed base vertex `x`.

## approach_A
Structural / invariant route.

Major step 1: exact algebraic package from the quadratic identity.
- From `A^2 = 3J - 2A`,
  `A^3 = A(3J - 2A) = 36J - 2A^2 = 30J + 4A`.
- Taking traces gives
  `trace(A^3) = 56 * 30 = 1680`,
  so the digraph would contain exactly `1680 / 3 = 560` directed `3`-cycles, hence exactly `30` through each vertex.
- The spectrum is `12^1, 0^49, (-2)^6`, so the row space of `A` is only `7`-dimensional.

Self-check:
- The cubic identity is a direct substitution back into `A^2 = 3J - 2A`.
- The triangle count uses only `trace(A) = 0`.

Major step 2: pass to the nonarc matrix `B = J - I - A`.
- Since `A = J - I - B`, substituting into `A^2 = 3J - 2A` gives
  `B^2 = I + 33J`.
- So the spectrum of `B` is forced to be
  `43^1, 1^6, (-1)^49`.
- Hence:
  - `det(B) = -43`,
  - `B` is invertible,
  - `B^(-1) = B - (33/43)J`,
  - and on `1^\perp`, `B^2 = I`, so `B` is an involution there.

What this means:
- The complement nonarc relation is far more rigid than the original digraph presentation suggests.
- Any realization would have to hide inside a `0/1` involution-like matrix of determinant `43`.

Self-check:
- Expanding `(J - I - B)^2` and using `BJ = JB = 43J` indeed gives `B^2 = I + 33J`.
- The inverse formula is correct because `(B - (33/43)J)B = I`.

Major step 3: exact fixed-vertex quotient.
- The partition `({x}, T, R)` is out-equitable.
- Its exact quotient matrix is
  ```text
  Q =
  [0 3 9]
  [1 1 10]
  [0 3 9]
  ```
  because:
  - `x` sends `3` edges to `T` and `9` to `R`,
  - every vertex of `T` sends `1` edge to `x`, `1` edge to `T`, and `10` to `R`,
  - every vertex of `R` sends `0` to `x`, `3` to `T`, and `9` to `R`.
- The characteristic polynomial of `Q` is `u(u + 2)(u - 12)`, matching the global spectrum.

What this gives:
- the exact local geometry around one vertex is already quite narrow,
- but this three-cell quotient still stays feasible and does not by itself force a contradiction.

Self-check:
- The quotient entries are exactly the source-to-`T` counts from the dsrg axioms.
- The quotient spectrum matching `12,0,-2` confirms consistency, not nonexistence.

## approach_B
Construction / extremal / contradiction route: rule out every Cayley realization exactly.

Major step 1: translate the closed-neighborhood matrix into the group ring.
- Assume for contradiction that the digraph is a Cayley digraph on a finite group `G` of order `56`, with connection set `S` of size `12` and `e ∉ S`.
- Let `D = {e} ∪ S`, so `|D| = 13`.
- The matrix `M := A + I` is then the right-convolution operator by `D`.
- Since `M^2 = A^2 + 2A + I = I + 3J`, the corresponding group-ring identity is
  `D^2 = e + 3G`,
  where `G = sum_(g in G) g`.

Self-check:
- The coefficient of `e` on the right is `1 + 3 = 4`, matching the diagonal of `M^2`.
- The principal character also checks: `|D|^2 = 13^2 = 169 = 1 + 3 * 56`.

Major step 2: apply irreducible representations and Parseval.
- For any nontrivial irreducible unitary representation `rho` of `G`, one has `rho(G) = 0`, so
  `rho(D)^2 = I_(d_rho)`.
- Therefore `rho(D)` is diagonalizable with eigenvalues only `+1` and `-1`, hence
  `||rho(D)||_F^2 = d_rho`.
- Plancherel for finite groups gives
  `|G| * |D| = sum_rho d_rho ||rho(D)||_F^2`.
- The trivial representation contributes `13^2 = 169`.
- Every nontrivial representation contributes `d_rho * d_rho = d_rho^2`.
- Summing over all irreducibles therefore yields
  `56 * 13 = 169 + sum_(rho != 1) d_rho^2 = 169 + (56 - 1) = 224`,
  which is impossible because `56 * 13 = 728`.

Conclusion of Approach B:
- No Cayley realization exists on any group of order `56`, abelian or nonabelian.
- So any genuine witness would have to be essentially non-group-based.

Self-check:
- The contradiction is exact and unconditional inside the Cayley subclass.
- The only substantial input beyond the dsrg identity is standard finite-group Plancherel.

## lemma_graph
1. Lock the exact matrix identity `A^2 = 3J - 2A`.
2. Derive the forced spectrum `12^1, 0^49, (-2)^6` and `rank(A) = 7`.
3. Pass to the nonarc matrix `B = J - I - A` and obtain `B^2 = I + 33J`, `det(B) = -43`, and `B^(-1) = B - (33/43)J`.
4. Fix a vertex `x` and derive the exact three-cell quotient `[[0,3,9],[1,1,10],[0,3,9]]`.
5. Use `A^3 = 30J + 4A` to pin down the exact directed-triangle count `560`.
6. Test the strongest clean construction family available at solve stage: Cayley realizations.
7. Convert `M^2 = I + 3J` into the group-ring equation `D^2 = e + 3G` and close that route by the Parseval contradiction.
8. Remaining gap: the problem is still open for genuinely non-Cayley, locally nonuniform realizations.

## chosen_plan
- The best unconditional global route is still the structural one: the quadratic identity collapses the problem to a rank-`7` adjacency matrix and an involution-like nonarc matrix.
- The cleanest contradiction that actually closes in this pass is the Cayley obstruction. It rules out the most natural construction family without any search.
- I also checked the fixed-vertex quotient package because any full nonexistence proof will likely need to refine that local geometry. In this pass it stayed rigid but feasible.
- So the strongest honest solve-stage outcome is a partial obstruction package, not a full proof or disproof.

Self-check:
- The record distinguishes clearly between unconditional facts, the exact Cayley contradiction, and the unresolved general case.
- Lean should stay off because there is no exact proof of global existence or nonexistence yet.

## self_checks
- Statement fidelity: the artifact stays on the exact tuple `(56,12,3,1,3)`.
- Spectral check: `A^2 = 3J - 2A` forces restricted eigenvalues `0` and `-2`, with multiplicities `49` and `6`.
- Nonarc check: `B = J - I - A` satisfies `B^2 = I + 33J`, determinant `-43`, and inverse `B - (33/43)J`.
- Local quotient check: `({x}, T, R)` has exact quotient `[[0,3,9],[1,1,10],[0,3,9]]`.
- Triangle check: `A^3 = 30J + 4A` gives exactly `560` directed `3`-cycles.
- Cayley check: the Parseval arithmetic is `728` on the left versus `224` on the right, so the contradiction is real.
- Conservatism check: no statement here upgrades to global nonexistence.

## code_used
- No code used.
- Reason: the strongest outputs in this pass were exact algebraic consequences and a closed representation-theoretic contradiction; no bounded experiment was necessary to justify them.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact outputs from this pass:
  - the exact dsrg identity `A^2 = 3J - 2A`,
  - the forced spectrum `12^1, 0^49, (-2)^6` and `rank(A) = 7`,
  - the nonarc identity `B^2 = I + 33J`, with `det(B) = -43` and `B^(-1) = B - (33/43)J`,
  - the exact three-cell quotient `[[0,3,9],[1,1,10],[0,3,9]]`,
  - the exact directed-triangle count `560`,
  - and the exact theorem that no Cayley realization on any group of order `56` can exist.
- I did not prove global nonexistence and I did not produce a construction.
- Lean was intentionally left off.

## likely_failure_points
- The no-Cayley theorem is strong but still leaves the full non-Cayley case open.
- The three-cell quotient is exact yet too coarse to force a contradiction; a full disproof would likely need a sharper `C/O/I/N` or coherent-configuration argument.
- Because the tuple is still curation-open and solve runs with web off, it would be unsafe to present these partial obstructions as a final nonexistence theorem.

## what_verify_should_check
- Recompute the normalization `A^2 = 3J - 2A` and the spectrum `12^1, 0^49, (-2)^6`.
- Recheck the nonarc reformulation `B^2 = I + 33J`, especially the determinant `-43` and inverse `B - (33/43)J`.
- Recheck the fixed-vertex quotient `[[0,3,9],[1,1,10],[0,3,9]]`.
- Recheck the triangle count from `A^3 = 30J + 4A`.
- Audit the Cayley obstruction carefully:
  - `M = A + I` corresponds to convolution by `D = {e} ∪ S`,
  - `D^2 = e + 3G`,
  - `rho(D)^2 = I` for every nontrivial irreducible `rho`,
  - and the Plancherel normalization really gives the impossible equality `728 = 224`.

## verify_rediscovery
- PASS 1 used a bounded web audit on 2026-04-09 with exact-tuple searches, alternative dsrg notation searches, the canonical Hobart-Brouwer source, same-source checks, and one recent-status sweep.
- The canonical source still lists the exact tuple `(56,12,3,1,3)` as open (`?`).
- Within the search budget, I did not find an exact-instance construction, impossibility theorem, theorem/proposition/example in the same source, or a later paper that directly settles this exact tuple.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness
- The solve artifact stays locked to the exact intended statement for the tuple `(56,12,3,1,3)`.
- The unconditional algebraic identities are faithful consequences of the dsrg definition specialized to this tuple:
  - `A^2 = 3J - 2A`,
  - spectrum `12^1, 0^49, (-2)^6`,
  - `rank(A) = 7`,
  - `B := J - I - A` satisfies `B^2 = I + 33J`,
  - the fixed-vertex quotient `[[0,3,9],[1,1,10],[0,3,9]]`,
  - and `A^3 = 30J + 4A`, hence `560` directed triangles.
- There is no wrong-theorem drift in the main narrative: the artifact correctly says it did not prove global existence or nonexistence.
- The only overreach is the extra exact claim that all Cayley realizations are impossible; that claim is not supported by the written proof.

## verify_proof
- First incorrect step found at the Cayley obstruction, [record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/dsrg-56-12-3-1-3/record.md#L117) and specifically [record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/dsrg-56-12-3-1-3/record.md#L121).
- Up to `rho(D)^2 = I_(d_rho)`, the argument is fine.
- The next inference
  `rho(D)` is diagonalizable with eigenvalues `±1`, hence `||rho(D)||_F^2 = d_rho`
  is false in general.
- Reason: diagonalizable with eigenvalues `±1` does not imply normal or unitary, so the Frobenius norm is not determined by the eigenvalues alone.
- Therefore the subsequent Parseval computation that replaces every nontrivial contribution by `d_rho^2` is unjustified, and the claimed contradiction `728 = 224` does not follow.
- I did not find an error in the earlier linear-algebra package:
  - the spectrum and multiplicities satisfy the quadratic and trace constraints,
  - the nonarc identity gives determinant `-43`,
  - and the quotient eigenvalues are numerically `12, 0, -2`.

## verify_adversarial
- No code or checker existed in the artifact directory, so there was nothing to rerun.
- I reran small numerical sanity checks in plain Python:
  - the quotient matrix `[[0,3,9],[1,1,10],[0,3,9]]` has eigenvalues approximately `12, 0, -2`,
  - `12 + 0*49 + (-2)*6 = 0`,
  - `12^3 + 6(-2)^3 = 1680 = 56 * 30`,
  - and `det(B) = 43 * (-1)^49 = -43`.
- To stress-test the bad Cayley step, I checked the explicit matrix
  `M = [[1,1],[0,-1]]`, which satisfies `M^2 = I` but has Frobenius norm squared `3 != 2`.
- That concrete example breaks the inference pattern used in the record, so the no-Cayley theorem is not verified.

## verify_verdict
- `CRITICAL_FLAW`
- Explanation: the strongest claimed new theorem in the solve artifact, namely the full no-Cayley obstruction, fails at a specific and essential proof step. The remaining algebraic identities look correct, but the run does not currently justify even the partial theorem it claims beyond those identities.
- Classification after verification should remain `PARTIAL`, not `EXACT`, because no exact existence or nonexistence result was proved, and the artifact is not Lean-ready.

## minimal_repair_if_any
- Conservative repair: delete or explicitly downgrade the asserted theorem "no Cayley realization exists on any group of order `56`".
- Keep only the verified unconditional package:
  - `A^2 = 3J - 2A`,
  - spectrum `12^1, 0^49, (-2)^6`,
  - `rank(A) = 7`,
  - `B^2 = I + 33J`,
  - determinant `-43`,
  - inverse `B^(-1) = B - (33/43)J`,
  - quotient `[[0,3,9],[1,1,10],[0,3,9]]`,
  - and triangle count `560`.
- If solve is revisited, the Cayley route must be rebuilt from scratch with a valid representation-theoretic bound rather than the failed Frobenius-norm shortcut.
