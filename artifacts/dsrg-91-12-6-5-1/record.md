# dsrg-91-12-6-5-1

## statement_lock
- Active slug: `dsrg-91-12-6-5-1`
- Title: `Does a directed strongly regular graph dsrg(91,12,6,5,1) exist?`
- Locked intended statement: there exists a loopless directed graph `A` on `91` vertices with constant indegree and outdegree `12` such that
  - for every arc `x -> y`, there are exactly `5` directed `2`-paths `x -> z -> y`,
  - for every non-arc `x -> y` with `x != y`, there is exactly `1` directed `2`-path `x -> z -> y`,
  - for every vertex `x`, there are exactly `6` directed `2`-paths `x -> z -> x`.
- Matrix form used below: with adjacency matrix `A`,
  `A^2 = t I + lambda A + mu (J - I - A) = 6I + 5A + (J - I - A) = 5I + 4A + J`.
- Because the diagonal of `A` is zero, the condition `(A^2)_{xx} = 6` means each vertex has exactly `6` mutual neighbors.

Self-check:
- This is the exact existential statement from the dossier, not a variant.
- The proof below uses only standard dsrg identities and the same parameter tuple.

## definitions
- Fix a vertex `x`.
- Let `S = N^+(x)` be the out-neighborhood of `x`, so `|S| = 12`.
- Let `T = N^-(x)` be the in-neighborhood of `x`, so `|T| = 12`.
- Write
  - `M = S ∩ T` for the `6` mutual neighbors of `x`,
  - `O = S \ T` for the `6` out-only neighbors of `x`,
  - `I = T \ S` for the `6` in-only neighbors of `x`,
  - `N = V \ ({x} ∪ M ∪ O ∪ I)` for the remaining `72` vertices.
- For classes `C,D` among `M,O,I,N`, let `e(C,D)` denote the number of directed edges from `C` to `D`.

Useful translation facts:
- From the dsrg condition in the original graph:
  - if `y ∈ S`, then `|N^-(y) ∩ S| = 5`,
  - if `y ∉ S` and `y != x`, then `|N^-(y) ∩ S| = 1`,
  - if `y = x`, then `|N^-(x) ∩ S| = 6`.
- Also from the dsrg condition in the original graph:
  - if `y ∈ T`, then `|N^+(y) ∩ T| = 5`,
  - if `y ∉ T` and `y != x`, then `|N^+(y) ∩ T| = 1`,
  - if `y = x`, then `|N^+(x) ∩ T| = 6`.

Self-check:
- No equitability assumption is being smuggled in; these are direct `2`-path counts from the dsrg definition itself.
- The partition sizes are forced by `k = 12` and `t = 6`.

## approach_A
Structural / invariant route: use the adjacency algebra first.

- The matrix identity is
  `A^2 = 5I + 4A + J`.
- On the orthogonal complement of the all-ones vector, `A` satisfies
  `u^2 - 4u - 5 = 0`,
  so the only restricted eigenvalues are `5` and `-1`.
- Using `trace(A) = 0` and `1 + m_5 + m_{-1} = 91`, one gets multiplicities
  `m_5 = 13` and `m_{-1} = 77`.
- Equivalently, for `B = A + I`,
  `B` is a `0/1` matrix with row and column sums `13` and
  `B^2 = 6B + J`.
  So `B` has eigenvalues `13`, `6`, and `0`, hence rank `14`.

What this suggests:
- The hypothetical graph is extremely rigid.
- The sets `S` and `T` should impose very tight local incidence counts against the four blocks `M,O,I,N`.
- This route does not by itself finish the disproof, but it strongly motivates a fixed-vertex local count.

Self-check:
- The spectral arithmetic is exact and internally consistent.
- No contradiction appears yet, so this remains a setup route rather than the final proof.

## approach_B
Construction / extremal / contradiction route: fix `x` and count arcs between `M,O,I,N`.

Write
- `a = e(M,M)`, `b = e(M,O)`, `c = e(M,I)`, `d = e(M,N)`,
- `e = e(O,M)`, `f = e(O,O)`, `g = e(O,I)`, `h = e(O,N)`.

Now record the four exact block identities forced by the dsrg definition.

1. Targets in `O` receive exactly `5` edges from `S = M ∪ O`, so
   `b + f = 30`.
2. Targets in `N` receive exactly `1` edge from `S = M ∪ O`, so
   `d + h = 72`.
3. Sources in `M` send exactly `5` edges into `T = M ∪ I`, so
   `a + c = 30`.
4. Sources in `O` send exactly `1` edge into `T = M ∪ I`, so
   `e + g = 6`.

Now use row sums.

- The `6` vertices of `M` have total outdegree `72`, so
  `a + b + c + d = 72`.
  Combined with `a + c = 30`, this gives
  `b + d = 42`.
- The `6` vertices of `O` also have total outdegree `72`, so
  `e + f + g + h = 72`.
  Combined with `e + g = 6`, this gives
  `f + h = 66`.

These two short equations already force the contradiction:

- From `b + d = 42`, we have `d = 42 - b`.
- Then `d + h = 72` gives `h = 30 + b`.
- From `f + h = 66`, we get `f = 36 - b`.
- Hence
  `b + f = b + (36 - b) = 36`,
  contradicting the earlier exact identity `b + f = 30`.

So no directed strongly regular graph with parameters `(91,12,6,5,1)` can exist.

Self-check:
- Every equation above is a direct block-total identity coming from the original dsrg definition, with no appeal to the reverse graph.
- The contradiction is sharp: the same block `M ∪ O -> O` is forced to total both `30` and `36`.

## lemma_graph
1. Translate the dsrg parameters into the exact matrix identity `A^2 = 5I + 4A + J`.
2. Fix a vertex `x` and partition the other `90` vertices into `M,O,I,N` with sizes `6,6,6,72`.
3. Use the dsrg rule to control incoming edges from `S` and outgoing edges into `T`.
4. Let `b = e(M,O)`, `d = e(M,N)`, `f = e(O,O)`, `h = e(O,N)` and derive
   `b + f = 30`, `d + h = 72`, `b + d = 42`, and `f + h = 66`.
5. Eliminate `d` and `h` to force `b + f = 36`.
6. Contradict the exact target count `b + f = 30`.

## chosen_plan
- The best path is Approach B.
- Approach A shows that the parameters are spectrally feasible but highly rigid, which explains why a fixed-vertex partition should be effective.
- Approach B closes the problem exactly with a short contradiction and does not require code.

Self-check:
- The chosen proof is purely local and algebraic, so it matches the "reasoning first, minimal code" requirement.
- I do not see any hidden dependence on literature or on a stronger theorem than the dossier states.

## self_checks
- Statement check: the proof addresses the exact existential dsrg tuple `(91,12,6,5,1)`.
- Definition check: the proof uses only the standard dsrg `2`-path counts for arcs, non-arcs, and the diagonal `t`.
- Count check: the contradiction is the incompatible pair `b + f = 30` and `b + f = 36`.
- Conservatism check: this is a strong exact disproof candidate, but still only `COUNTEREXAMPLE` at solve stage because Lean has not been run.

## code_used
- No code used.
- The argument closed at the handwritten counting stage, so no checker or bounded experiment was needed.

## result
- Solve-stage verdict: `COUNTEREXAMPLE`
- Confidence: `high`
- Exact mathematical output from this solve pass:
  - assuming the standard dsrg definition used in the dossier, the parameter set `(91,12,6,5,1)` is impossible;
  - therefore the intended existential statement `There exists a dsrg(91,12,6,5,1)` is false.
- Lean was intentionally left off during solve.

## likely_failure_points
- Verification should recheck that the standard dsrg convention really treats `(A^2)_{xx} = t = 6` as the number of mutual neighbors, which is the usual convention here.
- The block-count proof itself is short enough that the main risk is simply transcription error, not a hidden theorem.
- I do not see a numerical weak point in the contradiction itself.

## what_verify_should_check
- Check the source-faithful definition of directed strongly regular graph for the tuple `(v,k,t,lambda,mu)`.
- Recompute the four block-total rules actually used:
  - targets in `O` receive `5` edges from `S`,
  - targets in `N` receive `1` edge from `S`,
  - sources in `M` send `5` edges into `T`,
  - sources in `O` send `1` edge into `T`.
- Recheck the final algebra:
  - `b + d = 42`,
  - `f + h = 66`,
  - `d + h = 72`,
  - `b + f` is forced to equal both `30` and `36`.
- If verification agrees, this is a strong candidate for later Lean formalization as an exact disproof.

## verify_rediscovery
- PASS 1 used a bounded web audit on 2026-04-08 focused on the exact tuple `(91,12,6,5,1)`, reordered notation, the canonical Hobart-Brouwer table, and later dsrg status pages/papers.
- The canonical source still lists `91 12 6 5 1` with comment `?`, while nearby settled rows carry explicit construction or nonexistence markers.
- The source definition page confirms the standard identity `A^2 = tI + λA + µ(J-I-A)`, matching the solver's convention and the interpretation of `(A^2)_{xx}=t`.
- I found no theorem, proposition, example, observation, corollary, or later exact-instance citation in the checked material that already settles this tuple.
- Rediscovery verdict: not established within the bounded pass. The current disproof does not look like an obvious rederivation of a cited exact-instance result.

## verify_faithfulness
- The solver addresses the exact intended statement `There exists a dsrg(91,12,6,5,1)`.
- There is no wrong-theorem drift: the argument assumes a hypothetical dsrg with the locked tuple and derives a contradiction.
- The definitions used are faithful to the canonical source: loopless digraph, constant indegree/outdegree `k`, and the matrix identity equivalent to the `2`-path conditions.
- The diagonal interpretation is also faithful: `(A^2)_{xx}=t=6` counts vertices `z` with `x -> z -> x`, i.e. the `6` mutual neighbors of `x`.

## verify_proof
- I did not find an incorrect step.
- The key orientation-sensitive translations are sound:
  - for each `y in O`, since `x -> y` but `y -> x` is absent, the number of `z` with `y -> z -> x` is `µ=1`, so each such `y` sends exactly one edge into `T = M ∪ I`;
  - for each `y in M`, since `y -> x` is an arc, the number of `z` with `y -> z -> x` is `λ=5`, so each such `y` sends exactly five edges into `T`.
- From these, the block equations
  `b+f=30`, `d+h=72`, `a+c=30`, `e+g=6`, `b+d=42`, `f+h=66`
  are all justified.
- Eliminating `d,h,f` gives `d=42-b`, `h=30+b`, `f=36-b`, hence `b+f=36`, contradicting `b+f=30`.
- This is an exact disproof of the existential statement if the argument is formalized cleanly.

## verify_adversarial
- No checker or search code existed to rerun.
- I adversarially rederived the argument from both the column-count side (`S` into targets) and the row-count side (sources into `T`) to test for transpose mistakes. The same contradiction reappears.
- I specifically tried to break the proof at the two most vulnerable spots:
  - confusing incoming counts to `y` with outgoing counts from `y`;
  - misreading `t=6` as something weaker than the count of mutual neighbors.
- Neither attack succeeds under the canonical definition from the source page.

## verify_verdict
- `VERIFIED`

## minimal_repair_if_any
- No repair needed.
- The only conservative caveat is novelty: PASS 1 did not prove frontier novelty, it only failed to find an exact prior resolution within the bounded audit.

## lean_statement

- Lean backend file: `lean/AutoMath/DSRG9112651.lean`
- Mirrored Lean file: `artifacts/dsrg-91-12-6-5-1/lean/AutoMath/DSRG9112651.lean`
- Axiom audit file: `artifacts/dsrg-91-12-6-5-1/lean/AxiomAudit.lean`
- Exact intended Lean proposition: `AutoMath.DSRG9112651.exactCounterexampleStatement`, i.e.
  `¬ ∃ Adj : Fin 91 → Fin 91 → Prop, AutoMath.DSRG9112651.IsDSRG9112651 Adj`.
- Faithfulness audit theorems: `AutoMath.DSRG9112651.no_dsrg_91_12_6_5_1_statement` and
  `AutoMath.DSRG9112651.exact_counterexample_statement_faithful`.

## lean_skeleton

- The Lean file starts from the exact theorem statement, not a proxy: it defines the precise dsrg
  predicate on `Fin 91`, the intended existential statement, and its exact negation.
- The checked proof skeleton is `AutoMath.DSRG9112651.no_dsrg_91_12_6_5_1_skeleton`, which says
  that any future exact contradiction lemma for `IsDSRG9112651` immediately yields the target
  nonexistence theorem.
- The intended route remains the fixed-vertex partition `M,O,I,N`: translate the exact `2`-path
  counts into block-total equations and then derive a genuine contradiction if one exists.
- The Lean audit also formalized the critical blocker lemmas
  `corrected_mutual_block_row_sum`, `corrected_out_only_block_row_sum`, and
  `counterexample_linear_constraints_consistent`.

## lean_result

- `lake build` succeeded in `lean/` on 2026-04-08 after importing `AutoMath.DSRG9112651` into the
  main backend.
- `lake env lean AutoMath/DSRG9112651.lean` succeeded on 2026-04-08.
- `lake env lean ../artifacts/dsrg-91-12-6-5-1/lean/AxiomAudit.lean` succeeded on 2026-04-08.
- `#print axioms` on the statement, faithfulness theorem, skeleton theorem, and blocker lemmas
  reported only `[propext, Classical.choice, Quot.sound]` or `[propext, Quot.sound]`; no
  `sorry`, `sorryAx`, or new axioms were introduced by this Lean artifact.
- The exact theorem itself was not proved. During the Lean audit, the handwritten contradiction
  failed at the row-sum step on `M`: because every `y ∈ M` has the forced edge `y -> x`, the
  correct identity is `6 + a + b + c + d = 72`, not `a + b + c + d = 72`.
- With that correction one gets `b + d = 36`, not `42`, and the displayed linear system is still
  consistent. The Lean theorem `counterexample_linear_constraints_consistent` gives an explicit
  witness to that consistency.
- Conservative outcome: no exact Lean formalization exists for the intended statement from the
  current artifact, so this run does not earn `EXACT`, `COUNTEREXAMPLE`, or a `PROOFS.md` update.

## lean_blockers

- The blocker is mathematical, not syntactic: the current nonexistence proof is invalid after the
  corrected `M` row sum.
- Since the advertised contradiction disappears, the verified result is not strong enough to
  formalize as an exact frontier result in this run.
- `lean4checker --fresh` is unavailable on this machine, so that extra audit could not be run.
