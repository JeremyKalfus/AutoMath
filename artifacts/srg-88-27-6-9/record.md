# srg-88-27-6-9

## statement_lock
- Active slug: `srg-88-27-6-9`
- Title: `Does a strongly regular graph with parameters (88,27,6,9) exist?`
- Locked object: a simple undirected graph `G` on `88` vertices with parameters `(v,k,lambda,mu) = (88,27,6,9)`.
- Locked intended statement for this solve pass: no such graph exists.
- Exact matrix identity:
  `A^2 = 27I + 6A + 9(J - I - A) = 18I - 3A + 9J`.
- The restricted eigenvalues are the roots of
  `u^2 + (mu - lambda)u + (mu - k) = u^2 + 3u - 18`,
  so they are `3` and `-6`. The full spectrum is therefore
  `27^1, 3^55, (-6)^32`.

Self-check:
- This is the exact tuple from `selected_problem.md`.
- The proof target is the full existence question, not a symmetry-restricted subclass.

## definitions
- Fix an edge `xy`.
- Define the standard edge partition
  - `X = {x}`,
  - `Y = {y}`,
  - `U = N(x) ∩ N(y)`, so `|U| = lambda = 6`,
  - `A = N(x) \ (U ∪ {y})`, so `|A| = k - lambda - 1 = 20`,
  - `B = N(y) \ (U ∪ {x})`, so `|B| = 20`,
  - `C = V \ (X ∪ Y ∪ U ∪ A ∪ B)`, so `|C| = 40`.
- Let `1_S` denote the indicator vector of a set `S`.
- Define two difference vectors
  - `u = 1_X - 1_Y`,
  - `v = 1_A - 1_B`.

Self-check:
- The partition sizes add to `1 + 1 + 6 + 20 + 20 + 40 = 88`.
- The vectors `u` and `v` are nonzero and linearly independent.

## approach_A
Structural / invariant route.

- Start from the locked identity `A^2 = 18I - 3A + 9J`.
- The global spectrum is forced to be `27^1, 3^55, (-6)^32`.
- Fixing a vertex `x` and writing the one-vertex block decomposition gives the local graph `Delta` on `27` vertices, the second subconstituent `Sigma` on `60` vertices, and the usual block equations
  - `B 1 = 6 1`,
  - `M 1 = 20 1`,
  - `M^T 1 = 9 1`,
  - `C 1 = 18 1`,
  - `B^2 + M M^T = 18I_27 - 3B + 9J_27`,
  - `B M + M C = -3M + 9J_(27x60)`,
  - `C^2 + M^T M = 18I_60 - 3C + 9J_60`.
- For any `Bu = t u` with `u ⟂ 1`,
  `M M^T u = (18 - 3t - t^2)u = -(t - 3)(t + 6)u`,
  so the nontrivial eigenvalues of `Delta` lie in `[-6,3]`.
- Transposing `B M + M C = -3M + 9J` gives
  `M^T B + C M^T = -3M^T`, so any nonboundary local eigenvalue `t` transports to `-3 - t` in `Sigma`.

What this gives:
- exact local spectral constraints,
- but not by itself an impossibility proof.

Self-check:
- Every displayed equation is an exact consequence of the SRG definition.
- This route is useful background, but it does not yet force a contradiction.

## approach_B
Construction / extremal / contradiction route.

Use the edge partition around a fixed edge `xy`.

First compute `A u` exactly.
- Since `u = 1_x - 1_y`, a vertex sees `u` by comparing adjacency to `x` and `y`.
- Therefore
  - `(A u)_x = -1`,
  - `(A u)_y = 1`,
  - `(A u)` is `0` on `U` and `C`,
  - `(A u)` is `1` on `A`,
  - `(A u)` is `-1` on `B`.
- So
  `A u = -u + v`.

Now compute `A v` exactly, not just on average.

- For `p in A`, let `alpha_p = |N(p) ∩ U|`.
  Because `p ~ x` and `p !~ y`,
  - common neighbors of `p` and `x`: `alpha_p + |N(p) ∩ A| = 6`,
  - common neighbors of `p` and `y`: `alpha_p + |N(p) ∩ B| = 9`.
  Subtracting gives
  `|N(p) ∩ A| - |N(p) ∩ B| = -3`.
  Hence `(A v)_p = -3`.

- For `q in B`, the symmetric argument gives `(A v)_q = 3`.

- For `r in U`, let `d_r = |N(r) ∩ U|`.
  Since `r` is adjacent to both `x` and `y`,
  - `1 + d_r + |N(r) ∩ A| = 6`,
  - `1 + d_r + |N(r) ∩ B| = 6`,
  so `|N(r) ∩ A| = |N(r) ∩ B|` and `(A v)_r = 0`.

- For `c in C`, since `c` is adjacent to neither `x` nor `y`,
  - `|N(c) ∩ U| + |N(c) ∩ A| = 9`,
  - `|N(c) ∩ U| + |N(c) ∩ B| = 9`,
  so `|N(c) ∩ A| = |N(c) ∩ B|` and `(A v)_c = 0`.

- At the edge endpoints,
  - `(A v)_x = |A| = 20`,
  - `(A v)_y = -|B| = -20`.

Therefore
`A v = 20u - 3v`.

So the `2`-dimensional subspace
`W = span{u,v}`
is `A`-invariant, and in the basis `(u,v)` the adjacency operator is represented by
```text
[ -1  20 ]
[  1  -3 ].
```
Its characteristic polynomial is
`lambda^2 + 4 lambda - 17`,
with eigenvalues
`lambda = -2 ± sqrt(21)`.

But an SRG with parameters `(88,27,6,9)` has only the eigenvalues `27`, `3`, and `-6`.
Since
`-2 - sqrt(21) < -6`,
the invariant-subspace eigenvalue is impossible.

Therefore no strongly regular graph with parameters `(88,27,6,9)` exists.

Self-check:
- The formulas for `A u` and `A v` are exact pointwise identities on each cell.
- No averaging or quotient interlacing is needed in the final contradiction.
- The only spectral input used at the end is the already-forced global spectrum `27, 3, -6`.

## lemma_graph
1. Lock the exact SRG identity `A^2 = 18I - 3A + 9J` and the forced spectrum `27^1, 3^55, (-6)^32`.
2. Fix an edge `xy` and partition the vertex set into `X, Y, U, A, B, C` with sizes `1,1,6,20,20,40`.
3. Define the difference vectors `u = 1_X - 1_Y` and `v = 1_A - 1_B`.
4. Prove the exact adjacency action `A u = -u + v`.
5. Use common-neighbor counts on each cell to prove the exact adjacency action `A v = 20u - 3v`.
6. Conclude that `W = span{u,v}` is `A`-invariant with matrix `[[ -1, 20 ], [ 1, -3 ]]`.
7. Compute the resulting eigenvalues `-2 ± sqrt(21)`.
8. Compare with the forced SRG spectrum and obtain a contradiction.

Self-check:
- Each step is exact and local to a single chosen edge.
- The contradiction is already complete at Step 8, with no Lean and no search.

## chosen_plan
- The best path is the edge-partition contradiction, not the one-vertex block analysis.
- The one-vertex route verified the basic spectral landscape and suggested looking for a smaller invariant configuration.
- The edge route then produced an exact `2`-dimensional invariant subspace, which is much stronger than a quotient-matrix interlacing argument and directly forces a forbidden eigenvalue.
- This is a strong exact nonexistence proof, so the conservative solve-stage classification is `COUNTEREXAMPLE` with `lean_ready = true`.

Self-check:
- The final proof is short enough to replay completely during verify.
- I am not upgrading to `EXACT` before Lean.

## self_checks
- Statement check: every step stays on the exact tuple `(88,27,6,9)`.
- Partition check: `|U| = 6`, `|A| = |B| = 20`, `|C| = 40` follows directly from `k = 27` and `lambda = 6`.
- Endpoint check: `(A v)_x = 20` and `(A v)_y = -20` use only the sizes of `A` and `B`.
- Cell-by-cell check:
  - on `A` and `B`, the difference `|N(.) ∩ A| - |N(.) ∩ B|` is forced by the equations `6` versus `9`,
  - on `U` and `C`, the same common-neighbor counts force exact cancellation.
- Spectral check: the matrix `[[ -1, 20 ], [ 1, -3 ]]` has eigenvalues `-2 ± sqrt(21)`, and `-2 - sqrt(21)` is strictly less than `-6`.
- Conservatism check: this is a strong exact disproof candidate, but still not Lean-checked.

## code_used
- Yes, but only minimally and only after the two handwritten routes were in place.
- I ran one transient unsaved `numpy` snippet to inspect a coarse edge-partition quotient matrix for possible local triangle counts.
- That probe suggested the final invariant-subspace pattern, but the proof written above is handwritten and does not rely on the snippet or on any saved script.

## result
- Solve-stage verdict: `COUNTEREXAMPLE`
- Confidence: `high`
- Exact output from this pass:
  - the forced spectrum is `27^1, 3^55, (-6)^32`,
  - for any edge `xy`, the difference vectors `u = 1_x - 1_y` and `v = 1_A - 1_B` span an exact `A`-invariant subspace,
  - the restricted adjacency matrix on that subspace is `[[ -1, 20 ], [ 1, -3 ]]`,
  - its eigenvalues are `-2 ± sqrt(21)`,
  - hence the assumed SRG would have a forbidden eigenvalue and cannot exist.
- So the intended statement `No strongly regular graph with parameters (88,27,6,9) exists` now has a strong exact nonexistence proof candidate.

## likely_failure_points
- The only real risk is a bookkeeping mistake in the cell-by-cell derivation of `A v = 20u - 3v`.
- In particular, verify should scrutinize the `A/B` difference counts on the `U` and `C` cells, because those cancellations are what make the subspace exactly invariant.
- A second risk is presentation drift: the argument proves nonexistence of the full SRG instance, not just a quotient obstruction for a relaxed model.

## what_verify_should_check
- Recompute the locked identity `A^2 = 18I - 3A + 9J` and the global spectrum `27^1, 3^55, (-6)^32`.
- Recheck the edge partition sizes `1,1,6,20,20,40`.
- Recheck the exact vector identities
  - `A u = -u + v`,
  - `A v = 20u - 3v`.
- In particular, verify the four cell arguments:
  - `p in A` gives `|N(p) ∩ A| - |N(p) ∩ B| = -3`,
  - `q in B` gives the symmetric `+3`,
  - `r in U` gives `|N(r) ∩ A| = |N(r) ∩ B|`,
  - `c in C` gives `|N(c) ∩ A| = |N(c) ∩ B|`.
- Recompute the eigenvalues of `[[ -1, 20 ], [ 1, -3 ]]` and confirm `-2 - sqrt(21) < -6`.
- If the rediscovery pass stays clean, formalize exactly this `2`-dimensional invariant-subspace contradiction in Lean.

## verify_rediscovery
- PASS 1 used a bounded live web audit on the exact tuple, variant notation, the canonical Brouwer table, and exact-instance status checks.
- No rediscovery was established within budget.
- The canonical source still appears to be Brouwer's SRG tables, and the tuple `(88,27,6,9)` still appears there as unresolved rather than settled.
- I did not find a theorem, proposition, example, observation, or corollary in the searched material that explicitly settles this exact instance.
- So the current run is not a rediscovery on the evidence gathered here.

## verify_faithfulness
- The solve artifact is faithful to the intended statement.
- It claims a full nonexistence proof for the exact SRG instance `(88,27,6,9)`, not a relaxed model, symmetry-restricted subclass, or nearby tuple.
- The locked SRG identity, the spectrum computation, the edge partition sizes, and the target contradiction all match the intended statement exactly.

## verify_proof
- First incorrect step found: in the `p in A` computation inside `approach_B`, the count of common neighbors of `p` and `y` omits the vertex `x`.
- For `p in A`, because `p ~ x` and `p !~ y`, the nonadjacent-pair condition gives
  `1 + |N(p) ∩ U| + |N(p) ∩ B| = 9`,
  not
  `|N(p) ∩ U| + |N(p) ∩ B| = 9`.
- Writing `alpha_p = |N(p) ∩ U|`, the correct equations are
  `alpha_p + |N(p) ∩ A| = 6`
  and
  `1 + alpha_p + |N(p) ∩ B| = 9`,
  hence
  `|N(p) ∩ A| - |N(p) ∩ B| = -2`.
- Symmetrically, for `q in B` one gets
  `|N(q) ∩ A| - |N(q) ∩ B| = 2`.
- The `U` and `C` cell cancellations are still correct, and the endpoint values `(A v)_x = 20`, `(A v)_y = -20` are still correct.
- Therefore the repaired exact identity is
  `A v = 20u - 2v`,
  not
  `A v = 20u - 3v`.
- On `W = span{u,v}`, the repaired matrix is
  `[[ -1, 20 ], [ 1, -2 ]]`,
  whose characteristic polynomial is
  `lambda^2 + 3 lambda - 18`
  with eigenvalues `3` and `-6`.
- Those are exactly the allowed restricted eigenvalues of an SRG with these parameters, so the claimed spectral contradiction disappears.
- Verdict on proof correctness: critical flaw. The main contradiction is invalid.

## verify_adversarial
- There was no saved checker script in `artifacts/srg-88-27-6-9`; the solve stage only reported an unsaved exploratory snippet.
- I reran the decisive `2 x 2` matrix check directly after repairing the omitted `x` term.
- The repaired matrix has trace `-3`, determinant `-18`, discriminant `81`, and eigenvalues `3` and `-6`.
- This adversarial recomputation confirms that the claimed forbidden eigenvalue `-2 - sqrt(21)` came entirely from the counting mistake.
- So the computation does not support the mathematical claim being made.

## verify_verdict
- `CRITICAL_FLAW`
- PASS 1 did not establish rediscovery.
- PASS 2 found the claim faithful to the intended statement.
- PASS 3 found a first concrete incorrect step: omission of `x` in the `p in A` nonadjacent-pair count.
- PASS 4 showed that repairing that step removes the contradiction and yields only the already-allowed eigenvalues `3` and `-6`.
- Therefore this artifact is not Lean-ready and should not be treated as an exact disproof candidate.

## minimal_repair_if_any
- Minimal conservative repair: replace the false identity `A v = 20u - 3v` by the correct identity `A v = 20u - 2v`.
- But this repair does not salvage the proof, because it changes the restricted matrix to `[[ -1, 20 ], [ 1, -2 ]]` and removes the contradiction.
- So there is no tiny repair that preserves the claimed nonexistence result.
