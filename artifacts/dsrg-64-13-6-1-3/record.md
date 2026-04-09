# dsrg-64-13-6-1-3

## statement_lock
- Active slug: `dsrg-64-13-6-1-3`
- Title: `Does a directed strongly regular graph with parameters (64,13,6,1,3) exist?`
- Locked intended statement for this solve pass: no loopless directed strongly regular graph with parameters
  `(v,k,t,lambda,mu) = (64,13,6,1,3)` exists.
- Exact matrix form: for an adjacency matrix `A`,
  `AJ = JA = 13J` and
  `A^2 = tI + lambda A + mu(J - I - A) = 6I + A + 3(J - I - A) = 3I - 2A + 3J`.
- Equivalent walk formulation:
  - every vertex has indegree and outdegree `13`,
  - every vertex has exactly `6` mutual neighbors,
  - every arc `x -> y` lies on exactly `1` directed `2`-path `x -> z -> y`,
  - every nonarc `x -/-> y` with `x != y` lies on exactly `3` directed `2`-paths `x -> z -> y`.

Self-check:
- The intended statement is locked to the exact tuple from `selected_problem.md`, not a nearby variant.
- The normalization `A^2 = 3I - 2A + 3J` is exact.

## definitions
- Standard convention used here: a dsrg is loopless, has constant indegree and outdegree `k`, and counts ordered directed `2`-paths.
- The diagonal condition `(A^2)_{xx} = t = 6` means each vertex has exactly `6` vertices `z` with `x -> z -> x`, so exactly `6` mutual neighbors.
- Fix a vertex `x`.
- Let `S = N^+(x)` and `T = N^-(x)`, so `|S| = |T| = 13`.
- Write
  - `M = S ∩ T`, so `|M| = 6`,
  - `O = S \\ T`, so `|O| = 7`,
  - `I = T \\ S`, so `|I| = 7`,
  - `N = V \\ ({x} ∪ M ∪ O ∪ I)`, so `|N| = 43`.
- For classes `C,D` among `M,O,I,N`, let `e(C,D)` be the number of directed edges from `C` to `D`.

Translation facts used repeatedly:
- If `y ∈ T`, then `|N^+(y) ∩ T| = 1`; if `y ∉ T` and `y != x`, then `|N^+(y) ∩ T| = 3`.
- If `y ∈ S`, then `|N^-(y) ∩ S| = 1`; if `y ∉ S` and `y != x`, then `|N^-(y) ∩ S| = 3`.

Ambiguities or conventions to keep explicit:
- The dossier's intended statement is nonexistence, but solve must stay conservative unless a full contradiction is found.
- No prior-art judgment is made here because solve runs with web disabled.

Self-check:
- The partition sizes are forced by `k = 13` and `t = 6`.
- The two translation bullets are direct rewrites of the dsrg `2`-path rule relative to `x`.

## approach_A
Structural / invariant route.

Major step 1: spectral package.
- On the orthogonal complement of the all-ones vector, `A` satisfies
  `u^2 + 2u - 3 = 0`,
  so the restricted eigenvalues are `1` and `-3`.
- Using `trace(A) = 0` and `1 + m_1 + m_{-3} = 64`, the multiplicities are
  `m_1 = 44` and `m_{-3} = 19`.
- So the spectrum is forced to be
  `13^1, 1^44, (-3)^19`.

Major step 2: the cleaner `0/1` reformulation.
- Let `B := A + I`.
- Then `B` is a `0/1` matrix with row and column sums `14` and
  `B^2 = A^2 + 2A + I = 4I + 3J`.
- Equivalently, for every pair of vertices `x,y`,
  `|R_x ∩ C_y| = 7` when `x = y` and `|R_x ∩ C_y| = 3` when `x != y`,
  where `R_x` is the support of row `x` of `B` and `C_y` is the support of column `y`.
- A further renormalization is
  `K := 4B - J`, whose entries are `3` and `-1`; it satisfies
  `K^2 = 64I`
  and has row and column sums `-8`.

Major step 3: exact `3`-cell quotient around a fixed vertex.
- For the partition `({x}, T, R)` with `R = V \\ ({x} ∪ T)` and `|R| = 50`, the dsrg axioms force the out-equitable quotient
  ```text
  Q =
  [0 6  7]
  [1 1 11]
  [0 3 10]
  ```
  because:
  - `x` sends `6` edges to `T` and `7` to `R`,
  - every vertex of `T` sends `1` edge to `x`, `1` to `T`, and `11` to `R`,
  - every vertex of `R` sends `0` to `x`, `3` to `T`, and `10` to `R`.
- The characteristic polynomial of `Q` is `(u - 13)(u - 1)(u + 3)`, so its eigenvalues match the global spectrum.

Major step 4: finer fixed-vertex partition.
- With `M = S ∩ T`, `O = S \\ T`, `I = T \\ S`, `N = V \\ ({x} ∪ M ∪ O ∪ I)`, the dsrg rules force exact aggregate totals
  - `e(S,M) = 6`, `e(S,O) = 7`, `e(S,I) = 21`, `e(S,N) = 129`,
  - `e(M,T) = 6`, `e(O,T) = 21`, `e(I,T) = 7`, `e(N,T) = 129`.
- Writing all block totals `e(C,D)` with `C,D ∈ {M,O,I,N}` gives a complete linear system of row, column, and walk-count constraints.
- That aggregate system is consistent, so the raw `M/O/I/N` bookkeeping does not by itself prove nonexistence.
- However, the natural stronger hypothesis that this `M/O/I/N` partition is out-equitable is impossible: it collapses to the equation `7p + 43u = 66` with `p ∈ {0,1}` and `u ∈ {0,1,2,3}`, which has no solution.

What this route gives:
- a rigid exact spectral package,
- the especially clean reformulation `B^2 = 4I + 3J`,
- one exact local quotient,
- and evidence that any hypothetical witness must be locally nonuniform near a vertex.
- It still does not force global nonexistence.

Self-check:
- The multiplicities `44` and `19` satisfy both trace and dimension.
- The identity `B^2 = 4I + 3J` is exact and is stronger-looking than the raw dsrg equation, but I do not currently know how to close a contradiction from it alone.
- The quotient matrix is exact and spectrally compatible, so there is no hidden contradiction at this stage.

## approach_B
Construction / contradiction route: test whether any witness could at least be Cayley.

Major step 1: translate `B^2 = 4I + 3J` into a group-ring equation.
- Assume for contradiction that the digraph is a Cayley digraph on a group `G` of order `64`.
- Let `S ⊂ G \\ {e}` be the connection set, so `|S| = 13`, and let `D := {e} ∪ S`, so `|D| = 14`.
- In the left-regular representation, the matrix of `D` is exactly `B = I + A`.
- Therefore the exact matrix identity `B^2 = 4I + 3J` becomes the group-ring identity
  `D^2 = 4e + 3G`,
  where `G` on the right means the formal sum of all group elements.

Major step 2: apply irreducible representations.
- Let `rho` be an irreducible representation of `G` of degree `d_rho`.
- For the trivial representation, `rho(D) = 14`.
- For every nontrivial irreducible representation, `rho(G) = 0`, so the group-ring identity gives
  `rho(D)^2 = 4 I_{d_rho}`.

Major step 3: compare traces in the regular representation.
- The coefficient of the identity in `D^2` is `4`, so in the regular representation
  `tr_reg(D^2) = 64 * 4 = 256`.
- On the other hand, decomposing the regular representation into irreducibles gives
  `tr_reg(D^2) = sum_rho d_rho tr(rho(D)^2)`.
- Using the previous step,
  - the trivial representation contributes `14^2 = 196`,
  - each nontrivial irreducible contributes `d_rho * tr(4 I_{d_rho}) = 4 d_rho^2`.
- Since `sum_rho d_rho^2 = |G| = 64`, the nontrivial irreducibles satisfy
  `sum_{rho != 1} d_rho^2 = 63`.
- Hence the same trace must also equal
  `196 + 4 * 63 = 448`,
  contradiction.

Conclusion of Approach B:
- no Cayley digraph can satisfy the dsrg equations for `(64,13,6,1,3)`;
- equivalently, any actual witness would have to be genuinely non-Cayley.

Self-check:
- The passage from `B = I + A` to `D^2 = 4e + 3G` is exact for a Cayley realization in the left-regular representation.
- The trace identity `tr_reg(X) = 64 * [e]X` for group-ring elements `X` is standard and is the only representation-theoretic input.
- This proves a genuine variant obstruction, not the full intended nonexistence statement.

## lemma_graph
1. Lock the exact matrix identity `A^2 = 3I - 2A + 3J`.
2. Derive the forced spectrum `13^1, 1^44, (-3)^19`.
3. Pass to `B := A + I` and record the stronger-looking exact identity `B^2 = 4I + 3J`.
4. Around a fixed vertex `x`, derive the exact `3`-cell quotient `[[0,6,7],[1,1,11],[0,3,10]]`.
5. Refine to the `M,O,I,N` partition and extract exact aggregate totals; note that the raw linear system is consistent but the natural out-equitable refinement is impossible.
6. Separately, assume a Cayley realization, rewrite `B^2 = 4I + 3J` as `D^2 = 4e + 3G`, and apply irreducible-representation traces.
7. Derive the contradiction `256 = tr_reg(D^2) = 448`, so no Cayley witness exists.

## chosen_plan
- The best exact output from this solve pass is now the Cayley obstruction: any witness would have to be non-Cayley.
- I kept the fixed-vertex partition because it independently shows that the most obvious locally equitable model cannot occur.
- Those two routes fit together well: the graph is spectrally rigid, cannot be Cayley, and would also need locally nonuniform behavior near every tested vertex.
- That is still short of the intended global nonexistence statement, so Lean should remain off.

Self-check:
- This preserves faithfulness to the intended statement while making the strongest proved claim explicit.
- Lean should stay off because the exact intended statement is still not settled.

## self_checks
- Statement fidelity: the artifact stays on the exact tuple `(64,13,6,1,3)`.
- Structural check: `A^2 = 3I - 2A + 3J`, `B^2 = 4I + 3J`, and `K^2 = 64I` are all exact consequences of the dsrg axioms.
- Spectral check: the restricted eigenvalues are `1` and `-3` with multiplicities `44` and `19`.
- Local-count check: the `M/O/I/N` aggregate system is consistent, so no unconditional contradiction was proved there; only the extra out-equitable refinement was ruled out.
- Variant check: the Cayley contradiction is exact and does not depend on any web lookup or hidden classification theorem.
- Conservatism check: the solve verdict must stay below `COUNTEREXAMPLE` and below `CANDIDATE`, since the full intended statement is still open in this solve pass.

## code_used
- No code used.
- Reason: the handwritten algebra already isolated the strongest exact outputs found in this pass, and I did not reach a point where bounded search or a checker was justified.

## result
- Solve-stage verdict: `VARIANT`
- Confidence: `medium-high`
- Strongest exact outputs from this pass:
  - the exact normalization `A^2 = 3I - 2A + 3J`,
  - the forced spectrum `13^1, 1^44, (-3)^19`,
  - the `0/1` reformulation `B^2 = 4I + 3J`,
  - the equivalent `{3,-1}` reformulation `K := 4B - J` with `K^2 = 64I`,
  - the exact `3`-cell quotient `[[0,6,7],[1,1,11],[0,3,10]]`,
  - the exact impossibility of the natural out-equitable `M/O/I/N` refinement,
  - and the strongest new exact claim: no Cayley dsrg with parameters `(64,13,6,1,3)` exists.
- I did not prove global nonexistence and I did not produce a construction, so the active problem remains open inside solve.
- Lean was intentionally left off.

## likely_failure_points
- The remaining gap is exactly the non-Cayley case.
- The involutory reformulation `K^2 = 64I` is striking, but I did not find the missing step that would upgrade it from a Cayley obstruction to full nonexistence.
- A genuine witness, if it exists, would have to be both non-Cayley and locally quite nonuniform, since the obvious equitable local model already fails.

## what_verify_should_check
- Recompute the normalization `A^2 = 3I - 2A + 3J` and the multiplicities `1^44` and `(-3)^19`.
- Recheck the exact reformulation `B^2 = 4I + 3J` and the derived identity `K^2 = 64I` for `K = 4B - J`.
- Recheck the exact `({x}, T, R)` quotient `[[0,6,7],[1,1,11],[0,3,10]]`.
- Recheck the `M/O/I/N` aggregate totals and the conditional contradiction for the out-equitable refinement.
- Verify the Cayley obstruction carefully:
  - for a Cayley witness, `B` really is the left-regular matrix of `D = {e} ∪ S`,
  - `B^2 = 4I + 3J` really becomes `D^2 = 4e + 3G`,
  - the regular-representation trace of `D^2` is both `256` and `448`, yielding the contradiction.
- In the web-enabled verify stage, check whether any known construction claim for this tuple is necessarily non-Cayley or whether the no-Cayley variant is already in the literature.

## verify_rediscovery
- PASS 1 used a bounded web audit on 2026-04-08 and checked the exact tuple `(64,13,6,1,3)`, alternate `DSRG(64,13,6,1,3)` notation, the canonical Hobart-Brouwer dsrg tables, and tuple-specific theorem/example/observation/corollary style searches.
- Within the allowed budget, I did not find a source establishing the exact intended statement "no dsrg with parameters `(64,13,6,1,3)` exists."
- The canonical source still lists the tuple as unresolved rather than settled.
- I also did not find an in-budget source explicitly recording the stronger variant "no Cayley dsrg with these parameters exists." The closest canonical material located in-budget only pointed to broader dsrg parameter tables and general background, not a tuple-specific no-Cayley theorem.
- Rediscovery is therefore not established in this verify pass.

## verify_faithfulness
- The solve artifact is mathematically faithful about what it actually proves: the strongest claimed theorem is only that no Cayley realization can have parameters `(64,13,6,1,3)`.
- That does **not** match the intended statement, which is full nonexistence of any dsrg with those parameters.
- So the artifact must remain `classification = VARIANT`, not `EXACT`, `COUNTEREXAMPLE`, or `CANDIDATE`.
- The supporting structural identities `A^2 = 3I - 2A + 3J`, `B^2 = 4I + 3J`, and the forced spectrum `13^1,1^44,(-3)^19` are exact consequences of the target tuple, but they do not close the gap from "non-Cayley" to "nonexistent."

## verify_proof
- First incorrect step found for the intended statement: the proof never produces one; it stops at the narrower no-Cayley conclusion. So there is no proof of the intended statement here.
- For the actual variant claim, I found no incorrect algebraic step.
- The spectral multiplicities recheck correctly: from `m_1 + m_{-3} = 63` and `13 + m_1 - 3m_{-3} = 0`, one gets `m_1 = 44` and `m_{-3} = 19`.
- The Cayley reduction is coherent: if `A` were the adjacency matrix of a Cayley digraph on a group `G` of order `64` with connection set `S`, then `B = I + A` is the regular representation matrix of `D = {e} ∪ S`, so `B^2 = 4I + 3J` becomes the group-ring identity `D^2 = 4e + 3G`.
- For each nontrivial irreducible representation `rho`, this gives `rho(D)^2 = 4I`; for the trivial representation, `rho(D) = 14`.
- The regular trace computation is then valid on both sides:
  - from coefficients, `tr_reg(D^2) = 64 * [e](D^2) = 64 * 4 = 256`;
  - from irreducible decomposition, `tr_reg(D^2) = 14^2 + 4 * 63 = 448`.
- That contradiction is sound, so the no-Cayley variant appears proved.

## verify_adversarial
- There was no checker or search code in the artifact, so the adversarial pass focused on recomputation and trying to break the key algebraic equalities.
- I rechecked the two fragile numerical points:
  - the spectrum arithmetic gives `44` and `19`, not any other multiplicities;
  - the contradiction really is `256 != 448`.
- I also tried the obvious escape hatch that the regular-representation trace formula might have been misapplied, but for a group-ring element `X`, `tr_reg(X) = |G| * [e]X` is exactly the right identity here, so that escape hatch fails.
- I did not find a hidden assumption beyond the explicit extra hypothesis "the graph is Cayley." That is exactly why the result stays a variant only.

## verify_verdict
- `VERIFIED`
- The bounded rediscovery pass did not establish that the exact intended statement is already settled.
- The artifact's actual theorem appears correct, but it is only the variant claim that no Cayley dsrg with parameters `(64,13,6,1,3)` exists.
- Therefore:
  - `classification = VARIANT`
  - `lean_ready = false`
  - the intended frontier claim remains open in this run

## minimal_repair_if_any
- No mathematical repair was needed inside the no-Cayley proof.
- The only conservative repair is classificatory: keep the run labeled `VARIANT` and explicitly say that the intended nonexistence statement is still unproved.
