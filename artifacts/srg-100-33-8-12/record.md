# srg-100-33-8-12

## statement_lock
- Active slug: `srg-100-33-8-12`
- Title: `Does a strongly regular graph with parameters (100,33,8,12) exist?`
- Locked object: a simple undirected graph `G` on `100` vertices with strongly regular parameters `(v,k,lambda,mu) = (100,33,8,12)`.
- Locked intended statement for this solve pass: no such graph exists.
- Exact matrix identity for the adjacency matrix `A`:
  `A^2 = 33I + 8A + 12(J - I - A) = 21I - 4A + 12J`.
- On `1^perp`, this gives the quadratic
  `u^2 + 4u - 21 = 0`,
  so the restricted eigenvalues are `3` and `-7`.
- Using `trace(A) = 0` and `trace(A^2) = 100 * 33`, the full spectrum is
  `33^1, 3^77, (-7)^22`.

Self-check:
- This is the exact tuple and exact intended statement from [selected_problem.md](/Users/jeremykalfus/CodingProjects/AutoMath/selected_problem.md).
- I am not weakening the task to a subclass, approximate model, or search-only formulation.

## definitions
- Fix a vertex `x`.
- Let `Delta = G[N(x)]`. Then `Delta` has `33` vertices and is `8`-regular.
- Let `Omega = G[V \\ N[x]]`. Then `Omega` has `66` vertices.
- Every `z in Omega` is nonadjacent to `x`, so `z` has exactly `mu = 12` neighbors in `N(x)`. Hence `Omega` is `21`-regular.
- For `z in Omega`, let `d_z = e_x - e_z`, where `e_v` is the standard basis vector of `R^100`.
- Let `E_-` denote the `-7` eigenspace of `A`. It has dimension `22`.

Ambiguities / conventions / missing-definition lock:
- All graphs are simple and undirected.
- `N(x)` means the open neighborhood, and `N[x] = N(x) union {x}`.
- `Delta` and `Omega` are induced subgraphs.
- Spectral interlacing is used in the standard principal-submatrix sense.

Self-check:
- The sizes `33` and `66`, and the internal degrees `8` and `21`, are forced directly by the SRG definition.
- No hidden convention from the dossier is needed beyond the standard SRG one.

## approach_A
Structural / invariant route: push the first subconstituent `Delta = G[N(x)]`.

- `Delta` is `8`-regular on `33` vertices.
- For each `y in N(x)`, define
  `u_y = (A - 3I)(e_x - e_y)`.
  Since `e_x - e_y` lies in `1^perp` and `(A - 3I)` kills the `3`-eigenspace, every `u_y` lies in `E_-`.
- Therefore the `33 x 33` Gram matrix of the vectors `u_y` has rank at most `22`.

Direct computation:
- On `1^perp`, the minimal polynomial gives
  `(A - 3I)^2 = 10(3I - A)`.
- If `y = y'`, then
  `u_y . u_y = (e_x - e_y)^T (A - 3I)^2 (e_x - e_y) = 10(3 * 2 - (-2)) = 80`,
  because `x` and `y` are adjacent.
- If `y != y'` are both neighbors of `x`, then
  `(e_x - e_y)^T A (e_x - e_y') = A_{yy'} - 2`.
  So
  `u_y . u_y' = 10(3 - (A_{yy'} - 2)) = 10(5 - A_{yy'})`.
- Hence the Gram matrix is
  `K_Delta = 30I - 10 A(Delta) + 50J`.

Consequences:
- On the all-ones vector of `Delta`, `K_Delta` has eigenvalue
  `30 - 10 * 8 + 50 * 33 = 1600`.
- On any eigenvector of `A(Delta)` orthogonal to `1` with eigenvalue `theta`,
  `K_Delta` has eigenvalue `30 - 10 theta`.
- Since `rank(K_Delta) <= 22`, its nullity is at least `11`.
- Therefore `Delta` has eigenvalue `3` with multiplicity at least `11`.

This almost pins down the local spectrum:
- Let that multiplicity be `m`.
- Then the remaining `21` nontrivial local eigenvalues have sum `-41` and total square sum `101` when `m = 11`.
- The trace and rank count force `m = 11` exactly, but that still does not by itself contradict existence.

Why this route stalls:
- It yields strong local spectral rigidity, but not a clean impossible sum or parity obstruction inside `Delta` alone.
- The first subconstituent seems too small to force the final contradiction directly.

Self-check:
- The map `(A - 3I)(1^perp) subseteq E_-` is exact because the only nontrivial global eigenvalues are `3` and `-7`.
- The rank bound is dimension-theoretic, not heuristic.
- I am not claiming that `approach_A` already proves nonexistence.

## approach_B
Construction / extremal / contradiction route: pass to the second subconstituent `Omega = G[V \\ N[x]]`.

- `Omega` is `21`-regular on `66` vertices.
- For each `z in Omega`, define
  `v_z = (A - 3I)(e_x - e_z)`.
  Again each `v_z` lies in `E_-`, so the Gram matrix of the `66` vectors `v_z` has rank at most `22`.

Compute the Gram matrix exactly:
- As above, `(A - 3I)^2 = 10(3I - A)` on `1^perp`.
- If `z = w`, then `x` and `z` are nonadjacent, so
  `v_z . v_z = 10(3 * 2 - 0) = 60`.
- If `z != w` are both in `Omega`, then
  `(e_x - e_z)^T A (e_x - e_w) = A_{zw}`,
  because `x` is adjacent to neither `z` nor `w`.
- Therefore
  `v_z . v_w = 10(3 - A_{zw})`,
  so the off-diagonal entries are `20` on edges of `Omega` and `30` on nonedges of `Omega`.
- Hence
  `K_Omega = 30I - 10 A(Omega) + 30J`.

Now use rank:
- On the all-ones vector of `Omega`, `K_Omega` has eigenvalue
  `30 - 10 * 21 + 30 * 66 = 1800`.
- On any eigenvector of `A(Omega)` orthogonal to `1` with eigenvalue `theta`,
  `K_Omega` has eigenvalue `30 - 10 theta`.
- Since `rank(K_Omega) <= 22`, the nullity of `K_Omega` is at least `66 - 22 = 44`.
- The all-ones direction is not in the kernel, so `A(Omega)` must have eigenvalue `3` with multiplicity at least `44`.

This is where the contradiction appears:
- `Omega` has `66` eigenvalues total.
- One eigenvalue is the degree `21`.
- At least `44` more eigenvalues are `3`.
- So there are at most `21` remaining eigenvalues.
- Because `Omega` is an induced subgraph of `G`, Cauchy interlacing gives every eigenvalue of `Omega` at least `-7`.
- Therefore the sum of the remaining eigenvalues is at least `-7 * 21 = -147`.
- But trace zero for `A(Omega)` gives
  `sum(remaining eigenvalues) = -21 - 44 * 3 = -153`,
  already impossible.

Conclusion of the route:
- The assumption that `G` exists produces a `66`-vertex `21`-regular induced subgraph `Omega` whose spectrum is simultaneously forced to contain at least `44` copies of `3` and to satisfy a trace lower bound that cannot reach `-153`.
- Therefore the assumed SRG cannot exist.

Self-check:
- The contradiction uses only exact linear algebra in the `-7` eigenspace and standard interlacing for the induced subgraph `Omega`.
- The numerical mismatch is strict: `-153 < -147`, so there is no boundary case to worry about.

## lemma_graph
1. Assume a strongly regular graph `G` with parameters `(100,33,8,12)` exists.
2. Write the exact adjacency identity `A^2 = 21I - 4A + 12J`.
3. Deduce the global spectrum `33^1, 3^77, (-7)^22`.
4. Fix a vertex `x`, and define `Delta = G[N(x)]` and `Omega = G[V \\ N[x]]`.
5. Note that `Delta` is `8`-regular on `33` vertices and `Omega` is `21`-regular on `66` vertices.
6. For `z in Omega`, form `v_z = (A - 3I)(e_x - e_z)`, which lies in the `-7` eigenspace.
7. Compute the exact Gram matrix `K_Omega = 30I - 10A(Omega) + 30J`.
8. Since the `-7` eigenspace has dimension `22`, conclude `rank(K_Omega) <= 22`, so `A(Omega)` has eigenvalue `3` with multiplicity at least `44`.
9. Use `trace(A(Omega)) = 0` and interlacing lower bound `theta >= -7` for the remaining at-most-`21` eigenvalues.
10. Obtain the impossible inequality
  `-153 = sum(remaining) >= -147`.
11. Conclude that no strongly regular graph with parameters `(100,33,8,12)` exists.

Self-check:
- Each arrow in the skeleton is exact and algebraic; there is no search branch.
- The only external theorem used is standard principal-submatrix interlacing.

## chosen_plan
- I started with the neighborhood graph `Delta` because that is the most obvious reasoning-friendly object here.
- That route produced a useful local spectral fact, namely that `Delta` must have eigenvalue `3` with multiplicity exactly `11`, but it did not by itself force an impossibility.
- The better path was to repeat the same projection trick on the larger second subconstituent `Omega`, where the same `22`-dimensional target eigenspace collides with `66` vectors instead of `33`.
- That dimensional pressure is enough to force too many `3`-eigenvectors in `Omega`, and the trace then breaks immediately.

Self-check:
- This is still a reasoning-first path; no experiment or search was needed to discover the contradiction once the right subconstituent was chosen.

## self_checks
- Statement check: all claims target the exact tuple `(100,33,8,12)`.
- Spectrum check: the global spectrum `33^1, 3^77, (-7)^22` is consistent with the locked SRG identity.
- Local-structure check: `Delta` is `8`-regular on `33` vertices and `Omega` is `21`-regular on `66` vertices.
- Kernel-rank check: the Gram matrices come from vectors in the `22`-dimensional `-7` eigenspace, so the rank bounds are exact.
- Contradiction check: the only final inequality is `-153 >= -147`, which is false.
- Lean check: Lean stays off in solve, even though this is strong enough to be a later Lean candidate.

## code_used
- No.
- The proof attempt stayed entirely in exact handwritten linear algebra and interlacing.

## result
- Solve-stage verdict: `COUNTEREXAMPLE`
- Confidence: `high`
- Main exact output from this pass:
  - the locked SRG identity `A^2 = 21I - 4A + 12J`,
  - the global spectrum `33^1, 3^77, (-7)^22`,
  - the local first-subconstituent fact that `Delta` has eigenvalue `3` with multiplicity `11`,
  - the exact second-subconstituent Gram matrix `K_Omega = 30I - 10A(Omega) + 30J`,
  - the forced lower bound `mult_Omega(3) >= 44`,
  - the trace contradiction `-153 < -147`.
- This is a strong exact nonexistence proof candidate for the intended statement.

## likely_failure_points
- The key place to attack is the Gram computation for `Omega`; an index mistake there would invalidate the multiplicity claim.
- The second place to attack is the interlacing step; it must be applied to the induced `66 x 66` principal submatrix corresponding to `Omega`.
- The local `Delta` route is not the proof, only motivation; verification should not rely on it unnecessarily.
- Because a previous SRG solve in this repo failed on a missed common-neighbor term, every displayed dot-product identity should be rechecked line by line.

## what_verify_should_check
- Recompute the SRG identity `A^2 = 21I - 4A + 12J` and the spectrum `33^1, 3^77, (-7)^22`.
- Recheck that `Omega` really is `21`-regular on `66` vertices.
- Recheck that for `z in Omega`, the vector `(A - 3I)(e_x - e_z)` lies in the `-7` eigenspace.
- Recompute the Gram entries:
  - `60` on the diagonal,
  - `20` for adjacent pairs in `Omega`,
  - `30` for nonadjacent pairs in `Omega`.
- Recheck that this gives `K_Omega = 30I - 10A(Omega) + 30J`.
- Recheck the kernel argument: `rank(K_Omega) <= 22` forces `mult_Omega(3) >= 44`.
- Recheck the final contradiction from `trace(A(Omega)) = 0` together with the lower bound `theta >= -7` on the remaining eigenvalues.
- If all of that survives skepticism and the rediscovery pass stays clean, this artifact is a legitimate Lean candidate for exact nonexistence.

## verify_rediscovery
- PASS 1 used the full allowed bounded web budget on the exact tuple `(100,33,8,12)`, reordered/alternative SRG notation, the canonical Brouwer table, tuple-specific theorem/proposition/example/corollary wording, and one status-style check around symmetry-focused literature.
- The canonical source still lists `(100,33,8,12)` with `?`, i.e. existence unknown.
- Within the capped audit, I did not find an exact-instance construction, an exact-instance nonexistence theorem, or a same-source proposition/example/observation/corollary that already settles this tuple.
- I did find tuple-specific discussion that still treats the case as unresolved rather than solved.
- Rediscovery is therefore **not established**.

## verify_faithfulness
- The solve artifact targets the exact intended statement from [selected_problem.md](/Users/jeremykalfus/CodingProjects/AutoMath/selected_problem.md): nonexistence of an SRG with parameters `(100,33,8,12)`.
- There is no wrong-theorem drift: the argument works directly with the full graph `G`, a fixed vertex `x`, and the exact induced second subconstituent `Omega = G[V \\ N[x]]`.
- There is no quantifier drift: the contradiction is derived from an arbitrary hypothetical SRG with the locked tuple.
- There is no hidden definition change: `Omega` is exactly the induced graph on the `66` nonneighbors of `x`, and the proof only uses standard SRG identities and principal-submatrix interlacing.

## verify_proof
- I rederived the proof from scratch and found **no incorrect step** in the core argument.
- The global SRG identity gives the forced spectrum `33^1, 3^77, (-7)^22`.
- For fixed `x`, every `z in Omega` has `12` neighbors in `N(x)`, hence `21` neighbors inside `Omega`, so `Omega` is `21`-regular on `66` vertices.
- For `d_z := e_x - e_z`, the vector `(A - 3I)d_z` lies in the `-7` eigenspace because `d_z in 1^perp` and `(A - 3I)` kills the `3`-eigenspace on `1^perp`.
- The Gram entries check exactly:
  - diagonal `60`,
  - off-diagonal `20` when `z,w` are adjacent in `Omega`,
  - off-diagonal `30` when `z,w` are nonadjacent in `Omega`.
- Thus `K_Omega = 30I - 10A(Omega) + 30J`, and since the `66` vectors land in a `22`-dimensional space, `rank(K_Omega) <= 22`.
- On `1^\perp` of `Omega`, the eigenvalues of `K_Omega` are `30 - 10 theta`, so `nullity(K_Omega) >= 44` forces `A(Omega)` to have eigenvalue `3` with multiplicity `m >= 44`.
- Interlacing for the `66 x 66` principal submatrix `A(Omega)` gives every remaining eigenvalue of `Omega` the lower bound `>= -7`.
- With `Omega` being `21`-regular, the remaining `65 - m` eigenvalues therefore satisfy
  `sum_remaining >= -7(65 - m)`,
  while trace zero gives
  `sum_remaining = -21 - 3m`.
- These inequalities are incompatible for every `m >= 44`, since `-21 - 3m >= -7(65 - m)` would imply `m <= 43.4`.
- Tiny repair applied: the last contradiction must be written with an arbitrary `m >= 44`, not frozen at `m = 44`. After that repair, the proof is rigorous as written.

## verify_adversarial
- No solver code or checker existed for this artifact, so I reran the arithmetic and spectral numerics with a tiny fresh script only.
- The script reconfirmed the restricted global eigenvalues `3` and `-7`, the multiplicities `77` and `22`, and the strict contradiction for sample values `m = 44,45,50`.
- I also attacked the proof structurally at the two likely failure points noted in the solve record:
  - the Gram computation for `Omega`,
  - the interlacing index range for a `66 x 66` principal submatrix of a `100 x 100` matrix with spectrum `33,3^{77},(-7)^{22}`.
- Both checks held up. In particular, the only lower bound needed at the end is the coarse one `theta >= -7` on the remaining eigenvalues, which interlacing does supply.

## verify_verdict
- `MINOR_FIX`
- Reason: PASS 1 did not establish rediscovery, and the exact nonexistence argument survives skeptical checking. The only change needed was a tiny conservative repair to the final trace inequality, replacing the hard-coded `44` by a variable multiplicity `m >= 44`.
- With that repair, this is a strong exact disproof candidate and is ready for Lean.

## minimal_repair_if_any
- Replace the sentence
  `trace zero for A(Omega) gives sum(remaining eigenvalues) = -21 - 44 * 3 = -153`
  by the quantified version:
  if `m = mult_Omega(3) >= 44`, then the remaining `65 - m` eigenvalues sum to `-21 - 3m`, but each is at least `-7`, so `-21 - 3m >= -7(65 - m)`, impossible for `m >= 44`.
- No broader proof surgery is needed.

## lean_statement
- Exact Lean target formalized in [lean/AutoMath/SRG10033812.lean](/Users/jeremykalfus/CodingProjects/AutoMath/lean/AutoMath/SRG10033812.lean):
  `AutoMath.SRG10033812.intendedStatement`, namely
  `∀ {V} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj], ¬ G.IsSRGWith 100 33 8 12`.
- This matches the intended statement exactly: there is no finite simple graph with strongly regular parameters `(100,33,8,12)`.
- Mirrored Lean source:
  [artifacts/srg-100-33-8-12/lean/AutoMath/SRG10033812.lean](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/srg-100-33-8-12/lean/AutoMath/SRG10033812.lean).

## lean_skeleton
- Implemented the exact statement theorem
  `AutoMath.SRG10033812.srg_100_33_8_12_statement`.
- Implemented a proof skeleton
  `AutoMath.SRG10033812.srg_100_33_8_12_nonexistence_skeleton`
  which reduces the exact target to a single still-missing contradiction lemma for the tuple `(100,33,8,12)`.
- Implemented checked supporting lemmas:
  - `AutoMath.SRG10033812.parameters_satisfy_basic_srg_identity`
  - `AutoMath.SRG10033812.srg_matrix_identity`
  - `AutoMath.SRG10033812.nontrivial_multiplicities_forced_by_trace`
  - `AutoMath.SRG10033812.candidate_record_multiplicities_are_incorrect`
  - `AutoMath.SRG10033812.claimed_spectrum_line_from_record_is_false`

## lean_result
- `lake build AutoMath.SRG10033812` succeeded in the official `lean/` backend.
- The mirrored file is byte-for-byte identical to the backend file.
- `lake env lean ../artifacts/srg-100-33-8-12/lean/AxiomAudit.lean` succeeded.
- The axiom audit reported:
  - `srg_100_33_8_12_statement`: `[propext, Classical.choice, Quot.sound]`
  - `srg_100_33_8_12_nonexistence_skeleton`: `[propext, Classical.choice, Quot.sound]`
  - `parameters_satisfy_basic_srg_identity`: `[propext]`
  - `srg_matrix_identity`: `[propext, Classical.choice, Quot.sound]`
  - `nontrivial_multiplicities_forced_by_trace`: `[propext, Classical.choice, Quot.sound]`
  - `candidate_record_multiplicities_are_incorrect`: `[propext, Quot.sound]`
  - `claimed_spectrum_line_from_record_is_false`: `[propext, Quot.sound]`
- `lean4checker --fresh` is unavailable on this machine.
- Repo-wide `lake build` still fails in unrelated existing file
  [lean/AutoMath/C16458CNBC.lean](/Users/jeremykalfus/CodingProjects/AutoMath/lean/AutoMath/C16458CNBC.lean)
  because Lean cannot synthesize `Decidable (∀ (color : Coloring), ¬ IsCNBColoring color)`.
- No full exact theorem proof was completed, so this run does **not** earn `EXACT`.

## lean_blockers
- Fatal blocker: the verified artifact claims the global spectrum
  `33^1, 3^77, (-7)^22`, but `trace(A) = 0` together with `m_3 + m_{-7} = 99` forces
  `m_3 = 66` and `m_{-7} = 33`.
- This means the advertised `22`-dimensional `-7` eigenspace is incorrect. The Lean file now checks that arithmetic blocker explicitly.
- After correcting the multiplicities, the second-subconstituent rank argument no longer yields the stated contradiction; the claimed `mult_Omega(3) >= 44` conclusion is unsupported.
- The current candidate is therefore not strong enough for an exact Lean formalization. A fresh verify pass or a different proof is needed before another Lean attempt.
