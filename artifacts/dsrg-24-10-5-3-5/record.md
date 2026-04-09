# dsrg-24-10-5-3-5

## statement_lock
- Active slug: `dsrg-24-10-5-3-5`
- Title: `Does a directed strongly regular graph with parameters (24,10,5,3,5) exist?`
- Locked intended statement: determine whether there exists a loopless directed graph on `24` vertices with constant indegree and outdegree `10` such that
  - each vertex has exactly `5` mutual neighbors,
  - for every arc `x -> y`, there are exactly `3` directed `2`-paths `x -> z -> y`,
  - for every non-arc `x -> y` with `x != y`, there are exactly `5` directed `2`-paths `x -> z -> y`.
- Matrix form used below: if `A` is the adjacency matrix, then
  `A^2 = t I + lambda A + mu (J - I - A) = 5I + 3A + 5(J - I - A) = 5J - 2A`.
- The diagonal equation `(A^2)_{xx} = 5` means each vertex has exactly `5` mutual neighbors.

Self-check:
- This is the exact existential statement from `selected_problem.md`.
- No stronger variant or complement reformulation is being substituted for the target.

## definitions
- Fix a vertex `x`.
- Let `S = N^+(x)` and `T = N^-(x)`. Then `|S| = |T| = 10`.
- Write
  - `M = S ∩ T` for the `5` mutual neighbors of `x`,
  - `O = S \ T` for the `5` out-only neighbors of `x`,
  - `I = T \ S` for the `5` in-only neighbors of `x`,
  - `N = V \ ({x} ∪ M ∪ O ∪ I)` for the remaining `8` vertices.
- For classes `C,D` among `M,O,I,N`, let `e(C,D)` denote the number of directed edges from `C` to `D`.

Direct dsrg translations used below:
- Because `x -> y` for `y in M ∪ O`, each such target receives exactly `3` edges from `S`.
- Because `x` does not point to `y` for `y in I ∪ N`, each such target receives exactly `5` edges from `S`.
- Because `y -> x` for `y in M ∪ I`, each such source sends exactly `3` edges into `T`.
- Because `y` does not point to `x` for `y in O ∪ N`, each such source sends exactly `5` edges into `T`.

Self-check:
- These are direct `2`-path counts from the locked dsrg definition.
- No equitability assumption is being made beyond those exact counts.

## approach_A
Structural / invariant route: exploit the rigid matrix equation first.

- On the all-ones vector, `A` has eigenvalue `10`.
- On the orthogonal complement of the all-ones vector, `J` vanishes, so `A` satisfies
  `u^2 + 2u = 0`.
  Hence the only restricted eigenvalues are `0` and `-2`.
- Using `trace(A) = 0` and `1 + m_0 + m_{-2} = 24`, one gets
  `10 - 2 m_{-2} = 0`, so `m_{-2} = 5` and `m_0 = 18`.
- Therefore any hypothetical adjacency matrix has spectrum
  `10^1, 0^18, (-2)^5`
  and rank `6`.
- Writing `B = A - (5/12) J`, one checks
  `B^2 = -2 B`.
  So the centered adjacency matrix acts like `-2` times a rank-`5` idempotent on the sum-zero subspace.

What this gives:
- The tuple is spectrally feasible but extremely rigid.
- Any construction would have a `5`-dimensional nontrivial image and an `18`-dimensional kernel.
- This route did not by itself produce a contradiction, but it strongly suggests that a fixed-vertex partition count is the right next move.

Self-check:
- The eigenvalue arithmetic is exact and internally consistent with `trace(A)=0` and row sum `10`.
- No contradiction appears at the purely spectral level.

## approach_B
Construction / extremal / contradiction route: count arcs between `M,O,I,N`.

Write
- `a = e(M,M)`, `b = e(M,O)`, `c = e(M,I)`, `d = e(M,N)`,
- `e = e(O,M)`, `f = e(O,O)`, `g = e(O,I)`, `h = e(O,N)`.

From the direct dsrg translations:

1. Targets in `M` receive `3` edges from `S = M ∪ O`, so
   `a + e = 15`.
2. Targets in `O` receive `3` edges from `S`, so
   `b + f = 15`.
3. Targets in `I` receive `5` edges from `S`, so
   `c + g = 25`.
4. Targets in `N` receive `5` edges from `S`, so
   `d + h = 40`.
5. Sources in `M` send `3` edges into `T = M ∪ I`, so
   `a + c = 15`.
6. Sources in `O` send `5` edges into `T`, so
   `e + g = 25`.
7. The `5` vertices of `M` have total outdegree `50`, but they also send the `5` forced edges into `x`, so
   `a + b + c + d = 45`.
8. The `5` vertices of `O` have total outdegree `50` and no edges into `x`, so
   `e + f + g + h = 50`.

Now eliminate:

- From `(1)` and `(5)`, `c = e = 15 - a`.
- From `(6)`, `g = 10 + a`.
- From `(7)`, `d = 30 - a - b`.
- From `(2)` and `(4)`, `f = 15 - b` and `h = 10 + a + b`.

Plugging these into `(8)` gives
`(15 - a) + (15 - b) + (10 + a) + (10 + a + b) = 50`,
so `50 + a = 50`, hence
`a = e(M,M) = 0`.

This is an exact structural obstruction:
- for every vertex `x`, its `5` mutual neighbors induce no arcs at all;
- equivalently, the mutual-neighbor set `M(x)` is an independent set in the underlying digraph.

Useful consequences of `a = 0`:
- `c = e = 15`, so each mutual neighbor of `x` receives all three `S`-in-edges from `O`, and each mutual neighbor of `x` sends all three `T`-out-edges into `I`;
- if `y in M(x)`, then `x in M(y)`, and since `M(y)` is also independent, every other mutual neighbor of `y` is nonadjacent to `x`, hence lies in `N(x)`;
- therefore each `y in M(x)` has its other four mutual neighbors entirely inside `N(x)`, so `y` has no mutual neighbors in `M(x) \ {y}`, in `O(x)`, or in `I(x)`.

What did not close:
- I tried to push this into a full contradiction by counting the remaining `M-N`, `M-O`, and `M-I` incidences, but the unresolved blocks involving sources `I,N` and targets `O,N` still leave slack.
- The argument therefore produces a sharp local obstruction, but not yet an exact nonexistence proof.

Self-check:
- The only delicate step is the row-total correction: the `M` rows must exclude the `5` forced edges from `M` into `x`, so the correct block total is `45`, not `50`.
- With that correction, the derivation `a = 0` is algebraically sound.

## lemma_graph
1. Translate the tuple into the exact matrix identity `A^2 = 5J - 2A`.
2. Derive the spectrum `10^1, 0^18, (-2)^5` and rank `6`.
3. Fix a vertex `x` and partition the other vertices into `M,O,I,N` with sizes `5,5,5,8`.
4. Use dsrg `2`-path counts to write the six exact block equations for incoming edges from `S` and outgoing edges into `T`.
5. Add the corrected row totals for the `M` and `O` source blocks.
6. Eliminate variables to force `e(M,M) = 0`.
7. Propagate that to the structural consequence that every mutual-neighbor set is independent.

## chosen_plan
- The best path was Approach B.
- Approach A shows the tuple is low-rank and highly rigid, but Approach B is where an exact local obstruction appears.
- I pushed the block-count route until it yielded a theorem-level lemma `e(M,M)=0`; after that, the remaining equations still had genuine slack, so I stopped short of claiming a disproof.

Self-check:
- This stays within the solve-stage requirement to prefer reasoning over code.
- The current artifact records the strongest exact claim I can presently defend without overclaiming.

## self_checks
- Statement check: the writeup addresses the exact dsrg tuple `(24,10,5,3,5)`.
- Spectral check: `10 - 2 m_{-2} = 0` and `1 + m_0 + m_{-2} = 24` give `m_{-2} = 5`, `m_0 = 18`.
- Block-count check: the corrected `M` row total is `45` because each vertex of `M` already uses its edge to `x`.
- Obstruction check: the elimination in Approach B really forces `a = 0`.
- Conservatism check: this is not yet a full proof of nonexistence, so the solve-stage classification stays `PARTIAL`.

## code_used
- No code used.
- I considered a bounded exact search only after the handwritten routes, but the current reasoning did not isolate a small enough final search target to justify generic SAT/ILP or a broader brute-force branch at solve stage.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Exact mathematical output from this solve pass:
  - any hypothetical dsrg with parameters `(24,10,5,3,5)` would have adjacency spectrum `10^1, 0^18, (-2)^5` and rank `6`;
  - for every vertex `x`, the `5` mutual neighbors of `x` induce no arcs;
  - consequently, if `y` is a mutual neighbor of `x`, then the other four mutual neighbors of `y` must all lie in `N(x)`.
- Lean was intentionally left off during solve.

## likely_failure_points
- The main technical risk is a transpose mistake between "incoming from `S`" and "outgoing into `T`"; verification should rederive those equations independently.
- The step `M(y) \ {x} ⊆ N(x)` depends on reusing the proved lemma `e(M,M)=0` around the vertex `y`; that should be checked carefully.
- The solve pass does not settle whether the obstruction package already appears implicitly in the literature, but solve is intentionally web-off and does not classify rediscovery.

## what_verify_should_check
- Recompute the matrix identity `A^2 = 5J - 2A` and the spectrum/rank package.
- Re-derive the eight equations used in Approach B, especially the corrected row totals
  - `a + b + c + d = 45`,
  - `e + f + g + h = 50`.
- Confirm that those equations force `a = e(M,M) = 0`.
- Check the propagation step:
  - for `y in M(x)`, the independence of `M(y)` implies `M(y) \ {x} ⊆ N(x)`.
- Decide whether the next best verify-stage action is
  - a skeptical proof check of the local obstruction only, or
  - a bounded exact-instance search for whether the remaining slack can still support a full digraph.

## verify_rediscovery
- PASS 1 used a bounded web audit aimed at the exact instance `(24,10,5,3,5)`, alternate notation `dsrg(24,10,5,3,5)`, the complement tuple `(24,13,8,7,7)`, and the canonical Hobart-Brouwer source.
- The canonical source still lists `(24,10,5,3,5)` with `?` on the `dsrg-5` page, and the complementary row `(24,13,8,7,7)` is likewise not marked as settled.
- Exact-instance searches for the tuple did not surface a construction paper, a nonexistence theorem, or an explicit example/proposition/corollary settling this specific parameter set.
- A recent status-style check found later papers on constructing new parameter sets and on low-rank dsrgs, but within the verification budget none gave an accessible exact-instance implication for `(24,10,5,3,5)`.
- In particular, I did not find evidence strong enough to say the intended statement is already solved or directly implied in existing literature.
- Rediscovery conclusion: `not established within budget`.

## verify_faithfulness
- The solve record is faithful about what it actually proves.
- It does **not** claim to settle existence or nonexistence of a dsrg with parameters `(24,10,5,3,5)`.
- Its strongest mathematical claim is the local lemma `e(M,M)=0` for the mutual-neighbor block around an arbitrary vertex `x`, plus the spectral package `10^1,0^18,(-2)^5`.
- That is a genuine partial consequence of the exact intended statement, not a theorem-drift to a different parameter set or a changed definition.
- So there is no wrong-theorem drift, but there is also no full solution yet. The overall run should remain `PARTIAL`, not `EXACT` and not `CANDIDATE`.

## verify_proof
- First incorrect step found: `none found` in the proof of the stated local lemma.
- The matrix identity is correct:
  `A^2 = tI + \lambda A + \mu(J-I-A) = 5I + 3A + 5(J-I-A) = 5J - 2A`.
- On the sum-zero subspace, `J=0`, so the restricted eigenvalues satisfy `u^2+2u=0`; with row sum `10` and `trace(A)=0`, this forces multiplicities `m_{-2}=5`, `m_0=18`, hence rank `6`.
- The block equations around a fixed vertex `x` are also correct:
  - targets in `M,O,I,N` receive `15,15,25,40` edges from `S=M \cup O`,
  - sources in `M,O` send `15,25` edges into `T=M \cup I`,
  - row totals are `45` for `M` because each vertex of `M` already spends one out-edge on `x`, and `50` for `O`.
- Eliminating from
  `a+e=15`, `b+f=15`, `c+g=25`, `d+h=40`, `a+c=15`, `e+g=25`, `a+b+c+d=45`, `e+f+g+h=50`
  gives
  `c=e=15-a`, `g=10+a`, `f=15-b`, `d=30-a-b`, `h=10+a+b`,
  and substituting into the last equation yields `50+a=50`, hence `a=0`.
- Therefore the mutual-neighbor block `M(x)` is independent in the digraph for every `x`.
- The propagation step is also valid: if `y in M(x)`, then `x in M(y)`; since `M(y)` is independent, every `z in M(y) \\ {x}` is nonadjacent to `x`, so `z` lies in `N(x)`.

## verify_adversarial
- No checker or search code exists for this artifact, so there was nothing existing to rerun.
- I independently recomputed the spectrum/rank consequences from `A^2 = 5J - 2A` and confirmed `m_0=18`, `m_{-2}=5`, rank `6`.
- I also redid the block-variable elimination outside the prose argument; it again forces `a=0` and leaves one free parameter `b`, so the solve proof really proves only a local obstruction, not nonexistence.
- This slack is important adversarially: the current record has not boxed the hypothetical graph into inconsistency, only into a stricter local structure.

## verify_verdict
- `UNVERIFIED`
- Reason:
  - PASS 1 did not establish rediscovery.
  - PASS 2 found the writeup faithful as a `PARTIAL` result.
  - PASS 3 found the claimed local lemma mathematically sound.
  - PASS 4 confirmed that the argument still leaves genuine structural slack and therefore does not settle the intended existence question.
- Lean is **not** ready because there is no exact intended proof or disproof to formalize yet.

## minimal_repair_if_any
- No repair to the mathematical argument was needed.
- The conservative status repair is only classificatory:
  - keep the artifact as `PARTIAL`,
  - set verify-stage verdict to `UNVERIFIED`,
  - leave `lean_ready = false`.
