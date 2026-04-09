## statement_lock

Active slug: `srg-99-42-21-15`

Active title: `Does a strongly regular graph with parameters (99,42,21,15) exist?`

Exact intended statement for solve:

> No strongly regular graph with parameters `(v,k,lambda,mu) = (99,42,21,15)` exists.

Equivalent adjacency-matrix form:

- `G` is a simple graph on `99` vertices.
- Its adjacency matrix `A` satisfies
  `A^2 = (k-mu) I + (lambda-mu) A + mu J = 27 I + 6 A + 15 J`.

Forced spectrum:

- principal eigenvalue `42` with multiplicity `1`
- nontrivial eigenvalues `9` and `-3`
- multiplicities forced by trace:
  `42 + 9f - 3g = 0`, `f + g = 98`, hence `f = 21`, `g = 77`
- so the spectrum is `42^1, 9^21, (-3)^77`

## definitions

- `N(x)` means the neighbor set of a vertex `x`.
- Common-neighbor counts never include the endpoints themselves.
- Fix an adjacent pair `u ~ v`.
- Around that edge, write
  - `U := N(u) ∩ N(v)`, so `|U| = lambda = 21`
  - `B_u := N(u) \ (U ∪ {v})`, so `|B_u| = k - lambda - 1 = 20`
  - `B_v := N(v) \ (U ∪ {u})`, so `|B_v| = 20`
  - `D := V \ ({u,v} ∪ U ∪ B_u ∪ B_v)`, so `|D| = 36`
- Check: `2 + 21 + 20 + 20 + 36 = 99`.

Two spectral extremal facts used later:

- Hoffman clique bound with smallest eigenvalue `-3` gives `omega(G) <= 1 - k/(-3) = 15`.
- Hoffman coclique bound gives `alpha(G) <= 99 * 3 / (42 + 3) = 6.6`, hence `alpha(G) <= 6`.

## approach_A

Structural / invariant route: analyze the exact edge partition around a fixed edge `uv`.

For `a in U`, define `x(a) := |N(a) ∩ U|`. Then:

- since `u ~ a`, the `21` common neighbors of `u,a` are `v`, the `x(a)` vertices in `U`, and the neighbors of `a` in `B_u`
- since `v ~ a`, the same holds with `B_v`
- since `deg(a) = 42`, the remaining neighbors lie in `D`

So each `a in U` satisfies

- `|N(a) ∩ B_u| = 20 - x(a)`
- `|N(a) ∩ B_v| = 20 - x(a)`
- `|N(a) ∩ D| = x(a)`

For `b in B_u`, define `y(b) := |N(b) ∩ U|`. Then:

- from the adjacent pair `u ~ b`, the `21` common neighbors are in `U ∪ B_u`
- from the nonadjacent pair `v not~ b`, the `15` common neighbors are `u` plus vertices in `U ∪ B_v`

Hence each `b in B_u` satisfies

- `|N(b) ∩ B_u| = 21 - y(b)`
- `|N(b) ∩ B_v| = 14 - y(b)`
- `|N(b) ∩ D| = 6 + y(b)`
- in particular `2 <= y(b) <= 14`

For `d in D`, define `z(d) := |N(d) ∩ U|`. Then:

- from `u not~ d` and `v not~ d`, the common neighbors lie in `U ∪ B_u` and `U ∪ B_v`

Hence each `d in D` satisfies

- `|N(d) ∩ B_u| = 15 - z(d)`
- `|N(d) ∩ B_v| = 15 - z(d)`
- `|N(d) ∩ D| = 12 + z(d)`
- so `0 <= z(d) <= 15`

Let `e := E(U)`, the number of edges inside the `21`-vertex graph induced by `U`. Summing the displayed identities gives

- `sum_{a in U} x(a) = 2e`
- `sum_{b in B_u} y(b) = E(U,B_u) = 420 - 2e`
- `sum_{d in D} z(d) = E(U,D) = 2e`

and therefore the whole edge-count package

- `E(B_u) = E(B_v) = e`
- `E(U,D) = e`
- `E(B_u,B_v) = 2e - 140`
- `E(B_u,D) = E(B_v,D) = 540 - 2e`
- `E(D) = 216 + e`

Immediate nonnegativity already gives `70 <= e <= 210`.

Now use the SRG identity on `1_U`. Since

- `1_U^T A 1_U = 2e`
- `1_U^T A^2 1_U = 21*27 + 6*(2e) + 15*21^2 = 7182 + 12e`

and `A 1_U` has coordinates

- `21` on `u` and on `v`
- `x(a)` on `U`
- `|N(b) ∩ U|` on `B_u` and `B_v`
- `z(d)` on `D`

the Cauchy lower bound yields

`(2e)^2 / 21 + 2 * (420 - 2e)^2 / 20 + (2e)^2 / 36 <= 6300 + 12e`

which simplifies to `112 <= e <= 145`.

This looked promising, but the first attempted contradiction was false: the partition around an edge is not automatically equitable. The variables `x(a), y(b), z(d)` may vary from vertex to vertex inside their cells, so one cannot collapse them to single constants.

To test whether the first- and second-moment constraints are already contradictory, I then checked exact reachability of the local degree multisets. They are not contradictory. A concrete exact witness exists already at `e = 112`:

- for `a in U`, take `x(a)` to be seven `10`s and fourteen `11`s
- for `b in B_u`, take `y(b)` to be four `9`s and sixteen `10`s
- for `d in D`, take `z(d)` to be one `5`, twenty-six `6`s, and nine `7`s

These satisfy

- `sum x = 224 = 2e`, `sum x^2 = 2394`
- `sum y = 196 = 420 - 2e`, `sum y^2 = 1924`
- `sum z = 224 = 2e`, `sum z^2 = 1402`

and therefore

- `sum x^2 + 2 sum y^2 + sum z^2 = 2394 + 2*1924 + 1402 = 7644 = 6300 + 12e`

So approach A produces a sharp local package, but not a contradiction.

## approach_B

Construction / extremal / contradiction route: test whether the parameter set is forced into the geometric `(-3)`-eigenvalue template.

Because the smallest eigenvalue is `-3`, the clique bound is exactly `15`. If the graph were geometric in the Delsarte sense, its edges would be covered by `15`-cliques, and the SRG would match the point graph of a partial geometry `pg(s,t,alpha)` with parameters

- `k = s(t+1)`
- `lambda = s - 1 + t(alpha - 1)`
- `mu = alpha(t+1)`

Matching `(k,lambda,mu) = (42,21,15)` forces

- `t + 1` divides both `42` and `15`, so the only nontrivial possibility is `t + 1 = 3`
- hence `t = 2`, `alpha = 5`, `s = 14`

and indeed

- `k = 14*3 = 42`
- `lambda = 13 + 2*4 = 21`
- `mu = 5*3 = 15`

So the tempting geometric model is `pg(14,2,5)`.

But that incidence structure cannot exist, because counting point-line incidences would require

- each point lies on `t+1 = 3` lines
- each line contains `s+1 = 15` points
- hence the number of lines would be `b = v(t+1)/(s+1) = 99*3/15 = 99/5`, not an integer

Therefore any SRG with parameters `(99,42,21,15)` would have to be nongeometric.

This is a real obstruction to the most natural construction route, but it is not an existence contradiction by itself.

## lemma_graph

1. SRG hypothesis implies `A^2 = 27I + 6A + 15J`.
2. That forces the spectrum `42^1, 9^21, (-3)^77`.
3. Fix an edge `uv` and partition `V` into `{u},{v},U,B_u,B_v,D` with sizes `1,1,21,20,20,36`.
4. Per-vertex common-neighbor counts give exact formulas in terms of `x(a), y(b), z(d)`.
5. Summing those formulas collapses every aggregate edge count to one parameter `e = E(U)`.
6. The quadratic-form identity for `1_U` plus Cauchy bounds gives `112 <= e <= 145`.
7. An exact bounded reachability check finds local multisets satisfying all those constraints already at `e = 112`, so this route does not contradict existence.
8. Separately, Hoffman gives `omega <= 15` and `alpha <= 6`.
9. If the graph were geometric, it would match `pg(14,2,5)`.
10. Incidence counting rules out `pg(14,2,5)` because `b = 99/5` is nonintegral.
11. Therefore any surviving SRG would have to be nongeometric, and a stronger global obstruction is still needed.

## chosen_plan

I chose the edge-partition route first because the dossier explicitly pointed toward fixed-vertex / Seidel / parity structure, and the tuple has a very small negative eigenvalue `-3`, which often makes local counting rigid.

After that route stalled, I used the clique-geometry route as the cleanest extremal test. It does rule out the most obvious `15`-clique-based construction, but not the original SRG.

So the best conservative solve-stage outcome is:

- keep the exact local formulas and the nongeometric observation
- do not claim nonexistence
- do not claim a candidate construction either

## self_checks

- Checked the SRG identity directly from `(k,lambda,mu)`: `27I + 6A + 15J`.
- Checked the nontrivial spectrum and multiplicities from the quadratic `x^2 - 6x - 27 = 0` and trace equations.
- Checked the edge-partition sizes: `1 + 1 + 21 + 20 + 20 + 36 = 99`.
- Checked the per-cell formulas for `a in U`, `b in B_u`, `d in D` against adjacent/nonadjacent common-neighbor counts.
- Checked the aggregate edge-count formulas by double counting from both sides.
- Checked the Cauchy bound arithmetic, giving `112 <= e <= 145`.
- Checked that the exact bounded experiment only tests local integer multisets; it does not search over full graphs.
- Checked the geometric parameter match `(s,t,alpha) = (14,2,5)` and the incidence-count obstruction `b = 99/5`.
- Final claim check: the writeup proves only necessary conditions plus “nongeometric if it exists”, so the classification must stay below `COUNTEREXAMPLE`.

## code_used

Yes, but only after the handwritten reasoning had already fixed the local equations and the first two routes had stalled.

The code was a tiny bounded exact reachability check for the multiset data

- `x(a)` on `U`
- `y(b)` on `B_u`
- `z(d)` on `D`

subject to the already-derived sum and sum-of-squares constraints. It was used only to test whether the moment identities were genuinely contradictory.

Outcome:

- exact feasibility was found at `e = 112`
- witness multisets:
  - `x`: seven `10`s and fourteen `11`s
  - `y`: four `9`s and sixteen `10`s
  - `z`: one `5`, twenty-six `6`s, and nine `7`s`

So the code weakens, rather than strengthens, the current contradiction attempt: it shows the local moment system alone is not enough.

## result

Classification for solve: `PARTIAL`.

Best exact outputs obtained in this pass:

- the locked SRG identity `A^2 = 27I + 6A + 15J`
- forced spectrum `42^1, 9^21, (-3)^77`
- the full fixed-edge local-count package in terms of `x(a), y(b), z(d)`
- the aggregate one-parameter reduction with `e = E(U)`
- the Cauchy consequence `112 <= e <= 145`
- the observation that any such SRG would have to be nongeometric, because the geometric `pg(14,2,5)` model has nonintegral line count

What I did not get:

- no exact contradiction
- no exact witness or construction
- no Lean-ready theorem

## likely_failure_points

- The biggest trap is falsely treating the edge partition `{u},{v},U,B_u,B_v,D` as equitable. It is not forced to be equitable by SRG alone.
- The bounded experiment only proves numerical feasibility of the local moment data, not realizability by an actual graph.
- The nongeometric deduction removes one natural model but leaves a large search space of nongeometric SRGs with smallest eigenvalue `-3`.
- A real obstruction may need a stronger tool than the present counting: Seidel-matrix congruences, higher-order trace identities, a Terwilliger-algebra argument, or a sharper bound on common-neighborhood subgraphs.

## what_verify_should_check

- Re-derive `A^2 = 27I + 6A + 15J` and the spectrum `42^1, 9^21, (-3)^77`.
- Check every local formula in approach A, especially the `+1` term in the nonadjacent-pair count for `b in B_u`; that is exactly the sort of place where earlier SRG attempts in this repo have failed.
- Recheck the aggregate edge counts from the sums of `x(a), y(b), z(d)`.
- Recheck the Cauchy inequality arithmetic leading to `112 <= e <= 145`.
- Rerun the tiny bounded experiment and confirm that the witness multisets really hit the exact sum and sum-of-squares targets.
- Check the geometric reduction to `(s,t,alpha) = (14,2,5)` and the incidence obstruction `b = 99/5`.
- Confirm that the final claim envelope is only `PARTIAL` plus “nongeometric if it exists”, with no hidden overclaim of nonexistence.

## verify_rediscovery

PASS 1 used a bounded web audit on the exact tuple, alternate tuple notation, the canonical Brouwer source, and one later status source.

Findings:

- Brouwer's SRG table still lists `(99,42,21,15)` with `?`, i.e. open / existence unknown.
- A later survey-style source located in the audit, Brouwer and Van Maldeghem, "Strongly regular graphs with non-trivial automorphisms" (2010), includes `(99,42,21,15)` among open parameter sets rather than as a solved instance.
- No exact-instance theorem, proposition, example, observation, or corollary was found in the bounded search that settles this parameter set.

Conclusion:

- `REDISCOVERY` was not established within the allotted pass.
- The current writeup does not appear to reprove a known exact resolution; it only derives necessary conditions and a conditional nongeometric observation.

## verify_faithfulness

The intended statement is:

> No strongly regular graph with parameters `(99,42,21,15)` exists.

The solve-stage record does not actually prove that statement, and to its credit it no longer claims to. The mathematically supported claim is narrower:

- the SRG equations force `A^2 = 27I + 6A + 15J`
- the spectrum is forced to be `42^1, 9^21, (-3)^77`
- the fixed-edge partition formulas are valid
- the quadratic / Cauchy step gives `112 <= e <= 145`
- any such graph would be nongeometric, because the natural `pg(14,2,5)` model is impossible by incidence counting

So the record is faithful if and only if the run stays classified as `PARTIAL`. Any upgrade to nonexistence, `COUNTEREXAMPLE`, `CANDIDATE`, or `EXACT` would be wrong. I found no wrong-theorem drift inside the final claimed envelope.

## verify_proof

I rechecked the displayed deductions inside the final claimed envelope.

- `A^2 = 27I + 6A + 15J` is the standard SRG identity for `(99,42,21,15)`.
- The nontrivial eigenvalues are roots of `x^2 + (mu-lambda)x + (mu-k) = 0`, namely `9` and `-3`, and the multiplicities `21,77` follow from trace and dimension.
- The local formulas for `a in U`, `b in B_u`, and `d in D` are correct, including the `+1` contribution of `u` in the nonadjacent pair count for `v` and `b`.
- The aggregate edge-count formulas obtained from summing those local identities are consistent.
- The Cauchy lower bound on `||A 1_U||^2` does simplify to the stated integer range `112 <= e <= 145`.
- The geometric parameter match to `pg(14,2,5)` and the nonintegral line count `b = 99*3/15 = 99/5` are correct.

First incorrect step found: none inside the final claimed envelope.

Important limitation:

- the bounded multiset witness at `e = 112` shows only that the local first- and second-moment constraints are arithmetically feasible
- it does not show that a full SRG exists

That limitation is already acknowledged in the solve record, so it is not a verification failure.

## verify_adversarial

There is no standalone checker file in this artifact, so the adversarial pass was limited to recomputing the displayed arithmetic.

Reruns:

- recomputed the Cauchy-derived feasible integer range for `e`; it is exactly `112` through `145`
- recomputed the claimed witness multisets at `e = 112`
  - `x`: seven `10`s and fourteen `11`s gives length `21`, sum `224`, square-sum `2394`
  - `y`: four `9`s and sixteen `10`s gives length `20`, sum `196`, square-sum `1924`
  - `z`: one `5`, twenty-six `6`s, and nine `7`s gives length `36`, sum `224`, square-sum `1402`
  - total `sum x^2 + 2 sum y^2 + sum z^2 = 7644 = 6300 + 12*112`

Adversarial conclusion:

- the computation supports exactly what the record says it supports: local arithmetic feasibility
- it does not support the existence of a full graph, and the record does not claim otherwise

## verify_verdict

`VERIFIED`

The solve-stage writeup is mathematically sound as a `PARTIAL` result. No rediscovery of an exact resolution was established in PASS 1, but the argument also does not prove the intended nonexistence statement. Therefore this run is not Lean-ready.

## minimal_repair_if_any

Minimal repair applied at the status level only:

- keep the artifact classified as `PARTIAL`
- mark verification as complete
- keep `lean_ready = false`
- direct the next step toward finding a genuinely stronger global obstruction rather than attempting Lean
