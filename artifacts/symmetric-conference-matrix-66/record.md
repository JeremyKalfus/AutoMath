# Solve Record: symmetric-conference-matrix-66

## statement_lock

- Active title: `Does a symmetric conference matrix of order 66 exist?`
- Active slug: `symmetric-conference-matrix-66`
- Locked target statement: determine whether there exists a symmetric `66 x 66` matrix `C` with diagonal entries `0`, off-diagonal entries in `{ -1, 1 }`, and
  `C^T C = 65 I`.
- Because `C` is symmetric, the equation is equivalent to `C^2 = 65 I`.
- Standard switching is allowed for analysis: if `D` is diagonal with `±1` on the diagonal, then `D C D` is again a symmetric conference matrix. So one may normalize a hypothetical witness to have first row and first column all `+1` off the diagonal.
- Equivalent exact formulations I will use:
  - a symmetric conference matrix of order `66`;
  - a Seidel matrix `S` of order `65` with `S = S^T`, diagonal `0`, off-diagonal `±1`, `S 1 = 0`, and `S^2 = 65 I - J`;
  - a strongly regular graph with parameters `(65,32,15,16)`;
  - an equiangular tight frame of `66` lines in `R^33` with common angle `1 / sqrt(65)`.
- I am not claiming anything here about other orders.

## definitions

- Conference matrix: `n x n`, diagonal `0`, off-diagonal `±1`, and `C^T C = (n-1) I`.
- Symmetric conference matrix: additionally `C = C^T`.
- Normalized form: after switching, write
  `C = [[0, 1^T], [1, S]]`
  where `S` is `65 x 65`.
- Then `C^2 = 65 I` gives:
  - `S 1 = 0`,
  - `S^2 = 65 I - J`.
- Graph translation: define
  `A = (J - I - S) / 2`.
  Then `A` is a `0/1` adjacency matrix of a simple graph on `65` vertices.
- Strongly regular graph translation: `A` has parameters `(v,k,lambda,mu) = (65,32,15,16)`, equivalently
  `A^2 = 16 I - A + 16 J`.
- ETF translation: with `P = (I + C / sqrt(65)) / 2` on the full `66 x 66` conference matrix, `P` is an orthogonal projector of rank `33` and diagonal entries `1/2`.
- Ambiguities / conventions resolved:
  - The graph is simple and undirected.
  - The conference-graph equivalence uses the normalized `65 x 65` Seidel matrix, not the original `66 x 66` matrix directly.
  - For Cayley graphs I use additive notation, so inverse-closed means `D = -D`.

## approach_A

Structural / invariant route through normalization, spectrum, and extremal reformulations.

1. Normalize a hypothetical witness and pass to `S`.
   From
   `C = [[0, 1^T], [1, S]]`
   and `C^2 = 65 I`, the off-diagonal block gives `S 1 = 0`, and the lower-right block gives `S^2 = 65 I - J`.

2. Translate to a graph.
   Set `A = (J - I - S) / 2`. Since `S` has diagonal `0` and off-diagonal `±1`, `A` has diagonal `0` and off-diagonal `0/1`.
   Because `S 1 = 0`, every row sum of `A` is `(64 - 0)/2 = 32`, so the graph is `32`-regular.
   Substituting `S = J - I - 2A` into `S^2 = 65 I - J` yields
   `A^2 = 16 I - A + 16 J`,
   hence the graph is strongly regular with parameters `(65,32,15,16)`.

3. Extract the spectrum.
   For an srg `(65,32,15,16)`, the nontrivial eigenvalues solve
   `x^2 + x - 16 = 0`, so
   `r = (-1 + sqrt(65)) / 2`,
   `s = (-1 - sqrt(65)) / 2`.
   The multiplicities are both `32`.
   So the parameter set is admissible, but it is extremal: the irrational pair is exactly what one expects from a conference graph.

4. Repackage as an equiangular tight frame.
   Return to the full `66 x 66` matrix `C`. Since `C^2 = 65 I`, the matrix
   `P = (I + C / sqrt(65)) / 2`
   satisfies `P^2 = P`.
   Because `tr(C) = 0`, we have `tr(P) = 33`, so `rank(P) = 33`.
   Thus existence is equivalent to `66` equiangular lines in `R^33` at angle `1 / sqrt(65)`.
   This saturates the relative bound exactly:
   `N <= d (1 - alpha^2) / (1 - d alpha^2)` with `d = 33`, `alpha^2 = 1/65` gives `N <= 66`.

5. Try local and modular obstructions.
   None of the immediate easy obstructions closes the problem:
   - determinant admissibility is fine because `det(C)^2 = 65^66`;
   - the graph parameters satisfy the standard integrality and Krein feasibility checks;
   - modulo `5` and `13`, the normalized Seidel matrix satisfies `S^2 = -J`, which is restrictive but not contradictory by itself.

Self-check after Approach A:
- The conference-to-Seidel-to-srg chain is exact and instance-specific.
- The ETF reformulation is strong evidence that the problem is genuinely extremal, but it does not by itself prove existence or nonexistence.
- No exact contradiction emerged from the structural route alone.

## approach_B

Construction / contradiction route through the most natural algebraic model: a Cayley conference graph on `65` vertices.

1. Assume the graph side is Cayley.
   Let `G` be a group of order `65`, and suppose the putative conference graph is `Cay(G,D)` for some inverse-closed set `D subset G \\ {0}` of size `32`.

2. Use the group structure of order `65`.
   Let `n_13` and `n_5` be the numbers of Sylow `13`- and `5`-subgroups.
   Then
   `n_13 congruent 1 mod 13` and `n_13 | 5`, so `n_13 = 1`.
   Also
   `n_5 congruent 1 mod 5` and `n_5 | 13`, so `n_5 = 1`.
   Hence both Sylow subgroups are normal, so `G ~= C_13 x C_5 ~= C_65`.
   So any Cayley realization must be on `G ~= C_65`.

3. Compute the adjacency eigenvalues via characters.
   For an abelian Cayley graph, the eigenvalues are exactly
   `chi(D) = sum_{d in D} chi(d)`
   as `chi` ranges over the characters of `G`.
   Because the target graph is strongly regular `(65,32,15,16)`, every nonprincipal character must give one of the two nontrivial eigenvalues
   `r = (-1 + sqrt(65)) / 2`
   or
   `s = (-1 - sqrt(65)) / 2`.

4. Use small-order characters to force a field contradiction.
   The cyclic group `C_65` has nonprincipal characters of orders `5` and `13`.
   - If `chi` has order `5`, then `chi(D)` lies in `Q(zeta_5)`.
     If `chi(D)` were `r` or `s`, then `sqrt(65) = 2 chi(D) + 1` would lie in `Q(zeta_5)`.
     But `Q(zeta_5)` has only one quadratic subfield, namely `Q(sqrt(5))`, so `sqrt(65)` is impossible there.
   - If `chi` has order `13`, then `chi(D)` lies in `Q(zeta_13)`.
     If `chi(D)` were `r` or `s`, then again `sqrt(65)` would lie in `Q(zeta_13)`.
     But `Q(zeta_13)` has only one quadratic subfield, namely `Q(sqrt(13))`, so `sqrt(65)` is impossible there as well.
   Therefore an order-`5` or order-`13` character cannot take value `r` or `s`.
   This contradicts the strongly regular spectrum.

5. Conclusion of the route.
   No Cayley graph on a group of order `65` can realize the parameters `(65,32,15,16)`.
   Equivalently, no symmetric conference matrix of order `66` can come from an abelian regular construction on `65` points.

Self-check after Approach B:
- The only delicate input is the standard eigenvalue formula for abelian Cayley graphs.
- The field argument is rigid: the order-`5` and order-`13` characters force eigenvalues into the wrong quadratic fields.
- This proves a clean variant theorem, but it still does not settle the full existence question.

## lemma_graph

1. If a symmetric conference matrix of order `66` exists, switching-normalize it and remove one row/column to get `S` with `S 1 = 0` and `S^2 = 65 I - J`.
2. From `S`, form `A = (J - I - S) / 2`; then `A` is the adjacency matrix of an srg `(65,32,15,16)`.
3. Any such graph has nontrivial adjacency eigenvalues `r,s = (-1 +- sqrt(65)) / 2`.
4. If the graph were Cayley on a group of order `65`, the group would have to be cyclic.
5. In an abelian Cayley graph, eigenvalues are character sums `chi(D)`.
6. Characters of orders `5` and `13` force those sums to lie in `Q(zeta_5)` and `Q(zeta_13)`, respectively.
7. Since `r,s` lie in `Q(sqrt(65))` instead, a Cayley realization is impossible.
8. Therefore any genuine solution at order `66` must be non-Cayley.

## chosen_plan

- I pursued Approach B as the main line because it gives a rigorous theorem rather than only a reformulation.
- Approach A remains useful context: it shows exactly what any successful witness must look like and why the instance is extremal but still admissible.
- I am not claiming a full nonexistence proof. The strongest defensible solve-stage output is:
  - the exact intended statement remains unresolved here;
  - a strict subclass is ruled out rigorously.
- Minimal code is not needed. The main obstruction is short and purely symbolic, and I do not have a narrowly justified checker or witness to verify.

## self_checks

- Statement-lock check: all arguments stay on the exact order-`66` instance and its exact graph/ETF translations.
- Algebra check: substituting `S = J - I - 2A` into `S^2 = 65 I - J` really gives the srg identity `A^2 = 16 I - A + 16 J`.
- Spectral check: the nontrivial eigenvalues indeed satisfy `x^2 + x - 16 = 0`.
- Cayley check: every group of order `65` is cyclic, so the abelian character argument covers every Cayley realization.
- Field check: if `chi(D) = r` or `s`, then `sqrt(65) = 2 chi(D) + 1` lies in the same cyclotomic field as `chi(D)`. That is impossible in `Q(zeta_5)` and `Q(zeta_13)` because their unique quadratic subfields are `Q(sqrt(5))` and `Q(sqrt(13))`.
- Conservatism check: I am classifying this as `VARIANT`, not an exact solve, because the proof only eliminates the Cayley/abelian route.

## code_used

- No code used.
- Reason: no explicit candidate matrix emerged, and the cleanest new statement here is a purely handwritten no-Cayley obstruction.

## result

- I did not prove existence or nonexistence of a symmetric conference matrix of order `66`.
- I did prove a rigorous variant:
  no strongly regular graph with parameters `(65,32,15,16)` can be a Cayley graph on a group of order `65`.
- Since every group of order `65` is cyclic, this rules out all abelian regular constructions at once.
- Equivalently, any actual symmetric conference matrix of order `66`, if it exists, must come from a genuinely non-Cayley source.
- Solve-stage classification: `VARIANT`.

## likely_failure_points

- Verification should recheck the character-sum eigenvalue formula carefully and make sure the additive/Cayley conventions are aligned.
- Verification should also check the field step explicitly: the argument uses the fact that `Q(zeta_5)` and `Q(zeta_13)` have unique quadratic subfields `Q(sqrt(5))` and `Q(sqrt(13))`, so neither can contain `sqrt(65)`.
- Prior-art risk is moderate to high for this variant theorem. The no-Cayley obstruction may already be standard.
- The structural ETF reformulation is correct but not yet leveraged into a contradiction; verification should not overread it as progress toward full nonexistence.

## what_verify_should_check

- Re-derive the normalized Seidel form and the exact graph equivalence `(66 conference) <-> (65,32,15,16 srg)`.
- Recompute the nontrivial eigenvalues `(-1 +- sqrt(65))/2`.
- Check that every group of order `65` is cyclic.
- Check the abelian Cayley eigenvalue formula `lambda_chi = chi(D)`.
- Check the field containment argument for order-`5` and order-`13` characters.
- Run the bounded prior-art audit mainly on the variant statement:
  whether the no-Cayley / no-abelian-regular obstruction for `(65,32,15,16)` is already known.
- If verification confirms the obstruction but finds it to be old, the run should become a rediscovered variant rather than an exact advance.

## verify_rediscovery

- PASS 1 result: rediscovery established for the exact intended statement.
- Limited web audit found an explicit construction of a strongly regular graph with parameters `(65,32,15,16)`, namely the Gritsenko graph.
- Because the solve record itself uses the exact equivalence
  `(symmetric conference matrix of order 66) <-> (srg(65,32,15,16))`,
  this directly implies that a symmetric conference matrix of order `66` exists.
- Source trail used in the bounded audit:
  - Andries E. Brouwer's distance-regular graphs page for the Gritsenko graph lists parameters `(65,32,15,16)` and identifies it as a conference graph.
  - Gritsenko's 2021 preprint `There is a new strongly regular graph with parameters (65,32,15,16)` gives the explicit existence claim.
  - The 2022 paper `Spectral symmetry in conference matrices` says the smallest undecided orders for symmetric conference matrices are `86` and `162`, which is incompatible with order `66` being open.
- Therefore the selected problem dossier is stale: the exact intended statement is already solved in the literature.
- Short note on the current proof attempt: the solve-stage no-Cayley obstruction may still be mathematically correct as a variant theorem, but it is not frontier-novel progress on the exact intended statement because existence at order `66` is already known.

## verify_faithfulness

- The solve record is internally honest that it does **not** settle the intended statement and labels itself `VARIANT`.
- Relative to the intended statement, there is still wrong-theorem drift: the record proves only that a hypothetical realization cannot be Cayley, while the intended statement asks for existence or nonexistence of a symmetric conference matrix of order `66`.
- After PASS 1, that drift matters more sharply because the exact statement is already known to be true.
- Verdict on faithfulness: the artifact is faithful about what it actually proved, but the proved claim is a nearby variant rather than the target statement.

## verify_proof

- First incorrect step for the **variant theorem**: none found.
- The normalization from a symmetric conference matrix of order `66` to a Seidel matrix of order `65` with `S 1 = 0` and `S^2 = 65 I - J` is correct.
- The translation to an srg with parameters `(65,32,15,16)` and nontrivial eigenvalues `(-1 +- sqrt(65)) / 2` is correct.
- The group-theoretic step is correct: every group of order `65 = 5 * 13` is cyclic.
- For a Cayley graph on an abelian group, the adjacency eigenvalues are character sums `chi(D)`, hence lie in the cyclotomic field generated by the character values.
- Characters of orders `5` and `13` exist in `C_65`; if their eigenvalues had to equal `(-1 +- sqrt(65)) / 2`, then `sqrt(65)` would lie in `Q(zeta_5)` or `Q(zeta_13)`, impossible because those fields have unique quadratic subfields `Q(sqrt(5))` and `Q(sqrt(13))`.
- So the no-Cayley conclusion appears correct.
- That proof does not repair the main issue: it proves a side statement about one construction class, while the exact intended statement is already settled positively.

## verify_adversarial

- No code, checker, or witness file exists in the artifact directory, so there was nothing executable to rerun.
- Adversarial pressure was applied to the mathematical argument instead:
  - try to break the graph translation: no issue found;
  - try to break the spectrum computation: no issue found;
  - try to break the field argument by allowing the nontrivial eigenvalues to live in smaller cyclotomic subfields: no issue found.
- The adversarial outcome is therefore:
  - the solve-stage variant argument still looks sound;
  - the run nevertheless fails as an exact-problem advance because the exact instance is a rediscovery.

## verify_verdict

- `REDISCOVERY`

## minimal_repair_if_any

- No mathematical repair can convert this run into an exact advance.
- Minimal conservative repair is classificatory only:
  - mark the run as `REDISCOVERY`;
  - keep `lean_ready = false`;
  - archive the problem as already solved in the literature;
  - if desired later, salvage the no-Cayley argument only as a side note, not as progress on the selected problem.
