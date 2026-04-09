# p7-square-prime-labeling

## statement_lock
- Active slug: `p7-square-prime-labeling`
- Title: `Does the square of the 7-vertex path P_7^2 admit a prime labeling?`
- Locked intended statement: `P_7^2` admits a prime labeling.
- Working model: write the path vertices in order as `v_1,v_2,...,v_7`; then in `P_7^2` two vertices are adjacent exactly when their path distance is at most `2`, equivalently when `|i-j| <= 2`.

Self-check:
- The target is the exact `n = 7` path-square instance, not the whole family `P_n^2`.
- I am solving the positive existence statement selected in the dossier.

## definitions
- A prime labeling is a bijection `f : V(P_7^2) -> {1,2,3,4,5,6,7}` such that `gcd(f(u), f(v)) = 1` for every edge `uv`.
- Among distinct labels in `{1,2,3,4,5,6,7}`, the only non-coprime pairs are
  `(2,4)`, `(2,6)`, `(3,6)`, `(4,6)`.
- Therefore a labeling is prime if and only if each of those four label pairs lands on nonadjacent vertices.
- In `P_7^2`, nonadjacent pairs are exactly vertex pairs `v_i, v_j` with `|i-j| >= 3`.

Self-check:
- No other distinct pair in `{1,...,7}` has gcd greater than `1`.
- Translating the problem into placement constraints on the labels `2,3,4,6` is faithful.

## approach_A
Structural / invariant route: force the location of the troublesome label `6`.

1. The label `6` is not coprime to `2`, `3`, or `4`, so those three labels must all be placed on vertices nonadjacent to the vertex carrying `6`.
2. Count nonneighbors in `P_7^2`:
   - `v_1` and `v_7` each have `4` nonneighbors.
   - `v_2` and `v_6` each have `3` nonneighbors.
   - `v_3`, `v_4`, `v_5` each have only `2` nonneighbors.
3. So `6` cannot sit on `v_3`, `v_4`, or `v_5`, because there would not even be room for `2,3,4`.
4. If `6` sat on `v_2`, its nonneighbors would be exactly `v_5,v_6,v_7`. But `2` and `4` are themselves non-coprime, and every pair among `v_5,v_6,v_7` is adjacent in `P_7^2` because their indices differ by at most `2`. So `2` and `4` cannot both live there. The same argument rules out `v_6`.
5. Hence `6` is forced to an endpoint: `v_1` or `v_7`.

Self-check:
- This is a complete case split on the possible positions of `6`.
- The obstruction at `v_2` and `v_6` really uses the extra `(2,4)` conflict, not just the count of nonneighbors.

## approach_B
Construction / extremal route: once `6` is at an endpoint, the rest is almost forced.

By path-reversal symmetry, place `6` on `v_1`.

1. The nonneighbors of `v_1` are `v_4,v_5,v_6,v_7`.
2. The labels `2` and `4` must be nonadjacent to each other, so they must occupy two vertices in that set whose indices differ by at least `3`.
3. Inside `{v_4,v_5,v_6,v_7}`, the only such pair is `v_4` and `v_7`.
4. Therefore `{2,4}` is forced onto `{v_4,v_7}`.
5. The label `3` only has to avoid `6`, so after putting `6` on `v_1`, it may be placed on either remaining nonneighbor `v_5` or `v_6`.
6. The remaining labels `1,5,7` are coprime to every other distinct label in `{1,...,7}`, so they may fill the remaining three vertices arbitrarily.

One explicit witness is
`(f(v_1),f(v_2),f(v_3),f(v_4),f(v_5),f(v_6),f(v_7)) = (6,1,5,2,3,7,4)`.

Self-check:
- This gives an explicit bijection.
- The construction uses only the exact coprimality obstructions already identified.

## lemma_graph
1. Lemma 1: in `{1,...,7}`, the only distinct non-coprime pairs are `(2,4)`, `(2,6)`, `(3,6)`, `(4,6)`.
2. Lemma 2: in `P_7^2`, vertices `v_i` and `v_j` are nonadjacent iff `|i-j| >= 3`.
3. Lemma 3: because `6` conflicts with `2,3,4`, the vertex carrying `6` must have at least three suitable nonneighbors.
4. Lemma 4: `6` cannot be on `v_2` or `v_6`, because then `2` and `4` would be forced into a consecutive triple and would remain adjacent.
5. Lemma 5: thus `6` must be on `v_1` or `v_7`.
6. Lemma 6: with `6` on `v_1`, the labels `2` and `4` are forced to `v_4` and `v_7`.
7. Lemma 7: then `3` can be placed on `v_5` or `v_6`, and `1,5,7` fill the leftover vertices freely.
8. Conclusion: an explicit prime labeling exists.

## chosen_plan
Use the structural forcing from `approach_A` to reduce the search space to one endpoint case, then complete the problem by the explicit placement from `approach_B`.

Rigorous solve-stage proof:

Let the path vertices be `v_1,...,v_7` in order. In `P_7^2`, adjacency means index difference at most `2`.

Among the distinct labels `1,...,7`, the only pairs with gcd greater than `1` are `(2,4)`, `(2,6)`, `(3,6)`, `(4,6)`. So it is enough to place those pairs on nonadjacent vertices.

Because `6` is non-coprime to `2,3,4`, those three labels must all be placed on vertices nonadjacent to the vertex labeled `6`. This immediately rules out `v_3,v_4,v_5`, since each has only two nonneighbors in `P_7^2`. It also rules out `v_2`: its nonneighbors are exactly `v_5,v_6,v_7`, but then `2` and `4` would have to lie in that triple, and any two of `v_5,v_6,v_7` are adjacent in `P_7^2`. By symmetry, `v_6` is also impossible. Therefore `6` must lie on `v_1` or `v_7`.

Reverse the path if necessary and assume `f(v_1)=6`. Then the nonneighbors of `v_1` are `v_4,v_5,v_6,v_7`. Since `2` and `4` are non-coprime, they must be placed on two nonadjacent vertices from this set. The only such pair is `v_4` and `v_7`, so put `f(v_4)=2` and `f(v_7)=4`. Now `3` only needs to avoid `6`, so choose `f(v_5)=3`. Fill the remaining vertices with the remaining labels `1,5,7`, for example `f(v_2)=1`, `f(v_3)=5`, `f(v_6)=7`.

This yields the labeling
`(6,1,5,2,3,7,4)`.
Its only potentially bad pairs are exactly the four non-coprime pairs listed above, and their vertex gaps are:
- `6` with `2`: `|1-4| = 3`
- `6` with `3`: `|1-5| = 4`
- `6` with `4`: `|1-7| = 6`
- `2` with `4`: `|4-7| = 3`

All these gaps are at least `3`, so each pair is nonadjacent in `P_7^2`. Hence every adjacent pair receives coprime labels, and the labeling is prime.

Therefore `P_7^2` is prime.

Self-check:
- The proof ends with an explicit witness, not just an existence heuristic.
- Every non-coprime pair has been checked against the graph adjacency rule.

## self_checks
- Statement check: still locked to the exact intended statement `P_7^2 is prime`.
- Proof check: the only nontrivial graph fact used is the `|i-j| <= 2` adjacency rule in the square of a path.
- Conservatism check: this is a strong handwritten exact candidate, but solve still stops at `CANDIDATE` until verification and Lean.
- Method check: no search, SAT, ILP, CP-SAT, or brute force was used.

## code_used
- No code used.
- Reason: the obstruction set reduces to four non-coprime label pairs, so the explicit witness can be checked entirely by hand.

## result
- Solve-stage verdict: `CANDIDATE`
- Confidence: `high`
- Current conclusion: the explicit labeling
  `(6,1,5,2,3,7,4)` on path-order vertices `v_1,...,v_7`
  is a rigorous prime-labeling candidate for `P_7^2`.
- Lean remains off in this stage, but the instance now looks ready for skeptical verification and then formalization.

## likely_failure_points
- The only realistic failure point is a convention mismatch about the vertex order or the definition of `P_7^2`; verification should recheck that adjacency really is path distance at most `2`.
- Verification should also confirm that no distinct non-coprime pair among labels `1,...,7` was missed.
- Frontier-novelty remains a separate verify-stage question; the solve stage has not checked prior art.

## what_verify_should_check
- Re-derive the adjacency relation in `P_7^2` and confirm the nonneighbors of each vertex.
- Reconfirm that the only distinct non-coprime pairs in `{1,...,7}` are `(2,4)`, `(2,6)`, `(3,6)`, `(4,6)`.
- Check the forcing argument that `6` must be on an endpoint.
- Check the explicit witness `(6,1,5,2,3,7,4)` directly against all edges of `P_7^2`.
- If the bounded prior-art search still finds no rediscovery, this should be a Lean-ready candidate.

## verify_rediscovery
- PASS 1 used a bounded web audit targeted at the exact instance, alternative notation, the canonical survey, and one recent status check.
- Exact-instance searches for `"P_7^2" prime labeling` and `"square of P_7" prime labeling` did not surface any paper or note explicitly settling the `n = 7` case.
- The canonical-source check recovered Gallian's survey table entry for squared paths: the table records `P_n^2` as not prime for `n >= 6, n != 7`, which is consistent with the dossier's claim that `n = 7` is the lone gap rather than an already-settled exception.
- A recent-status check found a 2025 paper on prime labeling of `P_n^2 o K_1` that still states, in its introduction/background, that `P_n^2` is not prime for `n >= 6, n != 7`; that again treats `n = 7` as unresolved rather than solved.
- I did not find an exact prior solution, direct implication, or explicit exhibited labeling for `P_7^2` within the search budget.
- Rediscovery conclusion: not established.

## verify_faithfulness
- The solver's claim matches the intended statement exactly: existence of a prime labeling for the specific graph `P_7^2`.
- Definitions are used faithfully. The graph model is the square of the 7-vertex path with edges between vertices at path distance at most `2`.
- There is no quantifier drift: the proof constructs one explicit bijection on the seven vertices, which is exactly what the intended existential statement asks for.
- There is no wrong-theorem drift to a broader family or to a different labeling notion.

## verify_proof
- First incorrect step found: none.
- The key reduction is correct: among distinct labels `1,...,7`, the only non-coprime pairs are `(2,4)`, `(2,6)`, `(3,6)`, `(4,6)`, so it is enough to ensure those four pairs lie on nonadjacent vertices.
- The graph facts used in the forcing argument are correct. In `P_7^2`, nonadjacency is exactly index gap at least `3`, and the nonneighbor sets are:
  - `v_1`: `v_4,v_5,v_6,v_7`
  - `v_2`: `v_5,v_6,v_7`
  - `v_3`: `v_6,v_7`
  - `v_4`: `v_1,v_7`
  - `v_5`: `v_1,v_2`
  - `v_6`: `v_1,v_2,v_3`
  - `v_7`: `v_1,v_2,v_3,v_4`
- From this, the endpoint forcing for label `6` is valid, and the secondary argument excluding `v_2` and `v_6` correctly uses the extra conflict between `2` and `4`.
- The explicit witness `(6,1,5,2,3,7,4)` is sufficient, and the final check against the four potentially bad pairs is rigorous.

## verify_adversarial
- I reran a direct checker on the proposed labeling `(6,1,5,2,3,7,4)` against all edges of `P_7^2`; it found no bad edge.
- I also reran a brute-force verifier over all `7!` labelings as an adversarial check. It found `48` valid prime labelings in total, including the solver's witness.
- In the exhaustive check, the label `6` appears only at positions `1` or `7` in every valid labeling, which independently confirms the proof's central forcing claim.
- No computational contradiction to the mathematical claim was found.

## verify_verdict
- `VERIFIED`
- The candidate is mathematically sound on current evidence and the bounded prior-art audit did not establish rediscovery.
- Classification remains `CANDIDATE`, not `EXACT`, because Lean has not yet formalized the result.
- `lean_ready = true` because the statement appears exact, faithful, frontier-novel within the audit budget, and supported both by proof and by direct checking.

## minimal_repair_if_any
- None needed.

## lean_statement
- Official Lean backend module: `lean/AutoMath/P7SquarePrimeLabeling.lean`.
- Mirrored artifact Lean file: `artifacts/p7-square-prime-labeling/lean/AutoMath/P7SquarePrimeLabeling.lean`.
- Lean vertex model: `Vertex = Fin 7`, interpreted in path order `0,1,...,6` corresponding to `v_1,...,v_7`.
- Lean adjacency: `Adj v w := v ≠ w ∧ Nat.dist v.val w.val ≤ 2`, which is exactly the `P_7^2` adjacency rule.
- Lean label model: `Label = Fin 7`, interpreted as the mathematical labels `{1,...,7}` by `labelValue i = i + 1`.
- Exact target theorem: `AutoMath.P7SquarePrimeLabeling.p7_square_prime : intendedStatement`.
- Expanded exact target: `intendedStatement := ∃ f : Vertex → Label, Function.Bijective f ∧ ∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))`.
- Faithfulness audit: `p7_square_prime_statement` and `intendedStatement_faithful` are both definitional (`rfl`), and `witness_values_match_record` matches the verified witness `(6,1,5,2,3,7,4)`.

## lean_skeleton
- Skeleton theorem: `AutoMath.P7SquarePrimeLabeling.p7_square_prime_skeleton`.
- Skeleton content: if the verified witness `label` is shown bijective and edge-coprime for the exact `Adj` relation, then the exact intended statement follows immediately.
- Remaining obligations isolated by the skeleton were `label_injective` and `label_edgeCoprime`.

## lean_result
- `lake build AutoMath.P7SquarePrimeLabeling` succeeded in the official `lean/` backend.
- The backend file is imported by `lean/AutoMath.lean`, so the result is wired into the official AutoMath Lean project.
- `lake build` was also run repo-wide; it still fails in unrelated existing modules `lean/AutoMath/C16458CNBC.lean` and `lean/AutoMath/C244512CNBC.lean`, not in this new module.
- The exact witness is formalized by `label`, and `witness_values_match_record` confirms the path-order values `(6,1,5,2,3,7,4)`.
- `p7_square_prime_checked` proves the witness is a genuine prime labeling for the exact graph instance.
- `p7_square_prime_explicit` records the explicit natural-number form of the witness.
- Axiom audit via `lake env lean ../artifacts/p7-square-prime-labeling/lean/AxiomAudit.lean` reported only `[propext, Classical.choice, Quot.sound]` for `p7_square_prime`; no `sorryAx` appeared in the audit output.
- Lean conclusion: the exact intended statement `P_7^2 is prime` is fully formalized and checked, so this run earns `classification = EXACT` and `lean_complete = true`.

## lean_blockers
- No blocker remains for the target theorem itself.
- `lean4checker --fresh` is unavailable on this machine, so no fresh-environment recheck was run.
- Repo-wide `lake build` still has unrelated pre-existing failures in `C16458CNBC` and `C244512CNBC`, but the target module checks independently.
