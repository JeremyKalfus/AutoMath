# dsrg-48-22-11-9-11

## statement_lock
- Active slug: `dsrg-48-22-11-9-11`
- Title: `Does a directed strongly regular graph with parameters (48,22,11,9,11) exist?`
- Locked intended statement for this solve pass: determine whether there exists a loopless directed strongly regular graph with parameters `(v,k,t,lambda,mu) = (48,22,11,9,11)`.
- Equivalent adjacency-matrix form: find a `48 x 48` `0/1` matrix `A` such that
  - `A_ii = 0` for all `i`,
  - every row sum and every column sum is `22`,
  - `A^2 = tI + lambda A + mu(J - I - A) = 11I + 9A + 11(J - I - A) = 11J - 2A`.
- So for every ordered pair of distinct vertices `(x,y)`, the number of directed `2`-paths from `x` to `y` is `9` when `x -> y` and `11` otherwise, while `(A^2)_{xx} = 11`.

Self-check:
- The intended statement stayed exact: the full dsrg tuple, not a Cayley-only or normal-only variant.
- The specialization `A^2 = 11J - 2A` is the correct dsrg identity for `(48,22,11,9,11)`.

## definitions
- `J` is the all-ones matrix and `j` is the all-ones column vector.
- `N^+(x)` and `N^-(x)` are the out-neighborhood and in-neighborhood of a vertex `x`.
- Relative to a fixed vertex `x`, write
  - `M(x) = N^+(x) cap N^-(x)`, size `11`,
  - `O(x) = N^+(x) \\ N^-(x)`, size `11`,
  - `I(x) = N^-(x) \\ N^+(x)`, size `11`,
  - `N(x) = V \\ ({x} union M(x) union O(x) union I(x))`, size `14`.
- I use the complementary `0/1` matrix `C := J - I - A`.
- I also use the sign matrix `H := 2C - J = J - 2I - 2A`.

Ambiguities / conventions:
- I assume only the standard loopless dsrg definition from the dossier.
- I do not assume symmetry, normality, a Cayley model, or vertex-transitivity.
- Spectral claims are over `R` or `C`; all relevant polynomials split with distinct roots, so diagonalizability statements are safe.

Self-check:
- The class sizes `11,11,11,14` sum to `47` as required.
- `C` and `H` are exact rewrites of the same existence problem, not nearby variants.

## approach_A
Structural / invariant route.

Major step 1: force the spectrum and rank.
- Since `Aj = 22j` and `j^T A = 22 j^T`, the subspace `j^\perp` is `A`-invariant.
- On `j^\perp`, the identity becomes `A^2 = -2A`, so every nontrivial eigenvalue is a root of `u(u+2)`.
- Let the multiplicities on `j^\perp` be `m_0` for `0` and `m_-2` for `-2`. Then
  - `m_0 + m_-2 = 47`,
  - `trace(A) = 0 = 22 - 2 m_-2`.
- Hence `m_-2 = 11` and `m_0 = 36`.
- The spectrum is therefore forced to be `22^1, (-2)^11, 0^36`.
- In particular, `rank(A) = 12` and `nullity(A) = 36`.

Self-check:
- The trace equation gives `22 - 2 * 11 = 0`.
- The spectrum is compatible with both `A^2 = 11J - 2A` and the row/column sums `22`.

Major step 2: pass to the complement and sign matrix.
- Set `C := J - I - A`.
- Using `AJ = JA = 22J`, one gets
  `C^2 = (J - I - A)^2 = I + 13J`.
- So `C` is a `0/1` matrix with zero diagonal, constant row and column sum `25`, and exact quadratic identity `C^2 = I + 13J`.
- On the `j`-line, `C` has eigenvalue `25`; on `j^\perp`, `C = -I - A`, so the nontrivial eigenvalues are `1` and `-1` with multiplicities `11` and `36`.
- Hence the spectrum of `C` is `25^1, 1^11, (-1)^36`, so `det(C) = 25`.
- Also `C^-1 = C - (13/25)J`, because `C(C - (13/25)J) = C^2 - 13J = I`.
- Define `H := 2C - J = J - 2I - 2A`. Then `H` is a `48 x 48` `+-1` matrix with diagonal `-1`, row sum `2`, column sum `2`, and exact square `H^2 = 4I`.

Self-check:
- The cancellation in `C^2` is exact: `48J - 2J - 22J - 22J + 11J = 13J`.
- Since `CJ = JC = 25J`, expanding `(H + J)^2 = 4(I + 13J)` really gives `H^2 = 4I`.

Major step 3: extract exact obstructions and easy global counts.
- No realization can be normal. If `A` were normal, then
  `trace(AA^T) = sum |lambda|^2`
  would hold. But `trace(AA^T) = 48 * 22 = 1056`, whereas the forced spectrum gives
  `22^2 + 11 * 2^2 = 484 + 44 = 528`, contradiction.
- So in particular there is no abelian Cayley realization and no normal Cayley realization.
- Fix a vertex `x` and let `P := N^-(x)` and `Q := V \\ ({x} union P)`. Then `|P| = 22`, `|Q| = 25`, and the partition `({x},P,Q)` is exact out-equitable with quotient
  ```text
  [0,11,11]
  [1, 9,12]
  [0,11,11]
  ```
  because vertices in `P` have exactly `9` out-neighbors in `P`, while vertices in `Q` have exactly `11`.
- The quotient has characteristic polynomial `u(u+2)(u-22)`, matching the global spectrum.
- Also
  `A^3 = A(11J - 2A) = 220J + 4A`,
  so `trace(A^3) = 48 * 220 = 10560`. Therefore there are exactly `3520` directed `3`-cycles, i.e. `220` through each vertex.

Self-check:
- The nonnormality obstruction uses only exact counts and the forced eigenvalues.
- The three-cell quotient is unconditional; it does not assume the finer `M/O/I/N(x)` split is equitable.

## approach_B
Construction / extremal / contradiction route.

Major step 1: refine around a fixed vertex.
- Fix `x` and use the four classes `M(x), O(x), I(x), N(x)` of sizes `11,11,11,14`.
- The strongest nearby local simplification is to assume this five-cell partition is exact out-equitable, with quotient
  ```text
  [0,11,11, 0, 0]
  [1, a, b, c, d]
  [0, e, f, g, h]
  [1, p, q, r, s]
  [0, u, v, w, z]
  ```
  and cell-size vector `[1,11,11,11,14]`.
- The dsrg axioms immediately force the linear constraints
  - `a + c = 9`, `a + e = 9`,
  - `b + f = 9`, `c + g = 11`, `d + h = 14`,
  - `p + r = 9`, `u + w = 11`,
  - row sums `a+b+c+d = 21`, `e+f+g+h = 22`, `p+q+r+s = 21`, `u+v+w+z = 22`.
- If the partition were genuinely out-equitable, the quotient would have to inherit the same quadratic identity:
  `Q^2 = 11K - 2Q`,
  where every row of `K` is `[1,11,11,11,14]`.

Self-check:
- This is a stronger ansatz than the raw dsrg axioms; it is a test for a natural local model, not a theorem that every dsrg must satisfy.
- The quotient identity is the correct inheritance law for an exact out-equitable partition.

Major step 2: bounded contradiction for that strengthened ansatz.
- After the handwritten setup was fixed, I ran one tiny bounded enumeration over the remaining quotient variables.
- Result: there are no nonnegative integer `5 x 5` quotient matrices of the displayed form satisfying the forced linear constraints together with `Q^2 = 11K - 2Q`.
- So the natural fixed-vertex five-cell out-equitable model is impossible for this parameter set.

What this does and does not prove:
- It proves a genuine local obstruction: any actual realization would have to be more irregular than that exact five-cell quotient picture.
- It does not prove global nonexistence, because a dsrg need not make the full `({x},M,O,I,N)` partition out-equitable.

Self-check:
- The code was used only after the local quotient equations were written down by hand.
- The conclusion is scoped correctly: it kills a strengthened local model, not the whole problem.

## lemma_graph
1. Lock the problem as a `48 x 48` zero-diagonal `0/1` matrix with row/column sum `22` and `A^2 = 11J - 2A`.
2. Restrict to `j^\perp` to force the spectrum `22^1, (-2)^11, 0^36`, hence `rank(A) = 12`.
3. Pass to `C = J - I - A` and derive `C^2 = I + 13J`, the spectrum `25^1, 1^11, (-1)^36`, `det(C) = 25`, and `C^-1 = C - (13/25)J`.
4. Repackage this as the sign-matrix identity `H = J - 2I - 2A`, `H^2 = 4I`.
5. Use the forced spectrum to rule out every normal realization exactly.
6. Derive the exact three-cell quotient on `({x},N^-(x),V \\ ({x} union N^-(x)))`.
7. Compute `A^3 = 220J + 4A`, hence exactly `3520` directed `3`-cycles.
8. Test the stronger five-cell out-equitable refinement and show that no quotient matrix can satisfy the inherited dsrg identity.

## chosen_plan
- The invariant route was the best first path because the dossier already pointed to the clean quadratic identity.
- That route gave exact algebra quickly: forced spectrum, low rank, the complementary identity `C^2 = I + 13J`, and the sign-matrix reformulation `H^2 = 4I`.
- Once those facts still did not close the full problem, the only justified code use was a tiny quotient check on the strongest local model suggested by the fixed-vertex partition.
- That local model also failed, but only as a strengthened ansatz. So the strongest honest solve-stage outcome remains `PARTIAL`, not a proof and not a disproof.

Self-check:
- I stopped at the point where the remaining gap is genuinely global, not a bookkeeping omission.
- Lean should stay off because there is no exact witness and no exact nonexistence proof yet.

## self_checks
- Statement fidelity:
  - the exact tuple `(48,22,11,9,11)` stayed locked throughout;
  - the core identity `A^2 = 11J - 2A` was used consistently.
- Structural algebra:
  - spectrum `22^1, (-2)^11, 0^36` is correct;
  - `rank(A) = 12` and `nullity(A) = 36` are correct;
  - `C = J - I - A` satisfies `C^2 = I + 13J`;
  - `C` has spectrum `25^1, 1^11, (-1)^36`, determinant `25`, and inverse `C - (13/25)J`;
  - `H = J - 2I - 2A` satisfies `H^2 = 4I`.
- Exact obstructions:
  - no normal realization exists;
  - therefore no abelian Cayley or normal Cayley realization exists.
- Local structure:
  - the exact three-cell quotient is `[[0,11,11],[1,9,12],[0,11,11]]`;
  - the strengthened five-cell out-equitable quotient model is impossible.
- Scope honesty:
  - I did not construct a witness;
  - I did not prove full nonexistence;
  - the five-cell contradiction is only for a stronger local ansatz.

## code_used
- One tiny bounded plain-Python enumeration was used only after the handwritten five-cell quotient ansatz had been derived.
- Purpose: test whether any nonnegative integer quotient matrix of the displayed `({x},M,O,I,N)` form can satisfy the inherited identity `Q^2 = 11K - 2Q`.
- Result: `0` such quotient matrices exist.
- No graph search, SAT, ILP, CP-SAT, adjacency-matrix brute force, or generic optimization was used.

Self-check:
- The computation was directly tied to one explicit hypothesis.
- It reduced overclaiming: it showed that a tempting local route really fails, rather than pretending it yields a full contradiction.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact outputs from this pass:
  - the exact normalization `A^2 = 11J - 2A`,
  - the forced spectrum `22^1, (-2)^11, 0^36`,
  - the rank statement `rank(A) = 12`,
  - the complementary reformulation `C^2 = I + 13J`, with `det(C) = 25` and `C^-1 = C - (13/25)J`,
  - the sign-matrix reformulation `H^2 = 4I`,
  - the exact obstruction that no normal realization can exist,
  - the exact three-cell quotient `[[0,11,11],[1,9,12],[0,11,11]]`,
  - exactly `3520` directed `3`-cycles and `220` through each vertex,
  - and the impossibility of the strengthened five-cell out-equitable quotient model.
- I did not prove existence.
- I did not prove full nonexistence.
- Lean was intentionally left off.

## likely_failure_points
- The clean identities `C^2 = I + 13J` and `H^2 = 4I` are rigid, but I did not find the missing transpose-sensitive argument that turns them into a global contradiction.
- The five-cell failure only shows that any realization must be locally more irregular than the obvious fixed-vertex quotient model.
- A real closure may require a coherent-configuration argument, a stronger `A` versus `A^T` constraint, or a classification of `0/1` matrices satisfying `C^2 = I + 13J`.

## what_verify_should_check
- Recompute `A^2 = 11J - 2A`, the forced spectrum `22^1, (-2)^11, 0^36`, and the rank `12`.
- Recheck `C = J - I - A`, the identity `C^2 = I + 13J`, the determinant `25`, and the inverse `C - (13/25)J`.
- Recheck `H = J - 2I - 2A` and `H^2 = 4I`.
- Recheck the exact no-normal obstruction.
- Recheck the exact three-cell quotient `[[0,11,11],[1,9,12],[0,11,11]]` and its characteristic polynomial `u(u+2)(u-22)`.
- Recheck `A^3 = 220J + 4A` and the resulting directed-triangle count `3520`.
- Rerun the tiny five-cell quotient enumeration and confirm that it returns `0`.
- Keep the classification conservative: this artifact supports `PARTIAL`, not `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.

## verify_rediscovery
- PASS 1 used limited tuple-specific web search on the exact instance `(48,22,11,9,11)`, alternative dsrg notation, the canonical Hobart-Brouwer source, and same-source checks for an explicit construction/nonexistence entry.
- The canonical table still lists the exact tuple with `?`, and the extra searches surfaced only the same table and general dsrg references, not a paper or theorem settling this instance.
- Verdict for PASS 1: no rediscovery established within the bounded audit.

## verify_faithfulness
- The solve artifact is faithful about its top-level claim: it does not pretend to settle existence or nonexistence and explicitly labels the run `PARTIAL`.
- The strongest verified statements are all still about the exact intended tuple `(48,22,11,9,11)`, not a Cayley-only, normal-only, or proxy variant.
- The only faithfulness issue is local to `approach_B`: the five-cell discussion is presented as a consequence of an exact out-equitable partition, but some of the linear constraints used there require stronger input than out-equitability alone.

## verify_proof
- PASS 3 first incorrect step: in the five-cell quotient setup, the constraints `a + e = 9`, `b + f = 9`, `c + g = 11`, and `d + h = 14` are not immediate consequences of an out-equitable partition.
- Reason: those equalities encode exact counts of vertices `z` in `M(x) cup O(x)` with `z -> y` for a fixed `y`, which is an in-neighborhood condition. Out-equitability controls the counts of edges leaving a fixed cell, not the exact incoming counts to each vertex of another cell.
- By contrast, the earlier algebra package checks out: `A^2 = 11J - 2A`, the spectrum `22^1,(-2)^11,0^36`, `rank(A)=12`, `C^2 = I + 13J`, `H^2 = 4I`, the no-normal obstruction, the three-cell quotient, and `A^3 = 220J + 4A` all recompute correctly.
- Therefore the record does not contain a proof of the five-cell obstruction as written. The rest of the artifact remains a sound partial analysis package.

## verify_adversarial
- There was no saved checker script in the artifact directory to rerun.
- I recomputed the core algebra independently from the defining identity and rechecked the numerical consequences:
  - spectrum multiplicities force trace `0` and rank `12`;
  - the no-normal contradiction is `trace(AA^T) = 48 * 22 = 1056` versus spectral sum `22^2 + 11 * 2^2 = 528`;
  - the three-cell quotient has characteristic polynomial `u(u+2)(u-22)`;
  - `A^3 = 220J + 4A`, so each diagonal entry of `A^3` is `220` and the total directed `3`-cycle count is `3520`.
- Adversarial outcome: the solver's strongest local obstruction does not survive scrutiny because its enumeration was built on overstrong five-cell constraints. I did not find a flaw in the earlier exact algebra.

## verify_verdict
- `MINOR_FIX`
- Classification after verification remains `PARTIAL`.
- Reason: the artifact is not a rediscovery and is mostly correct, but one advertised local obstruction is unsupported as written, so the run is not ready for Lean and not ready for any stronger classification.

## minimal_repair_if_any
- Conservative repair: drop the claim that the displayed five-cell quotient system is impossible under the stated assumptions, or restate it explicitly as an obstruction for a stronger model that also imposes the additional incoming-count constraints.
- Keep the verified package consisting of the quadratic identity, forced spectrum/rank, complement/sign-matrix reformulations, no-normal obstruction, three-cell quotient, and triangle count.
