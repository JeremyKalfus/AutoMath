# statement_lock

We work with the standard book graph convention: `B_k` is the graph of `k` triangles sharing a common edge, so a graph contains `B_k` iff some edge has at least `k` common neighbors.

Locked target for this solve run:

- Assume `G` is a graph on `57` vertices.
- If `G` avoids `B13`, then every edge of `G` has at most `12` common neighbors.
- If `\bar G` avoids `B15`, then every edge of `\bar G` has at most `14` common neighbors.

The intended theorem candidate is:

`R(B13, B15) = 57`.

Equivalent title-theorem form:

Every graph on `57` vertices contains `B13` or its complement contains `B15`.

This would already be about `85%` to `90%` of a micro-paper. The minimal remaining packaging work would be a short literature-positioning paragraph, a clean writeup of the counting contradiction, and a one-paragraph comparison with the neighboring `B14` versus `B15` exact case.

# definitions

Let:

- `n = 57`
- `m = e(G)`
- `\bar m = \binom{57}{2} - m = 1596 - m`
- `t = t(G)` be the number of triangles in `G`
- `\bar t = t(\bar G)` be the number of triangles in `\bar G`
- `d_1, ..., d_57` be the vertex degrees in `G`

Basic translations:

- `G` avoids `B13` implies every edge lies in at most `12` triangles, so `3t <= 12m`, hence `t <= 4m`.
- `\bar G` avoids `B15` implies every edge of `\bar G` lies in at most `14` triangles, so `3\bar t <= 14\bar m`, hence `\bar t <= 14\bar m / 3`.
- Goodman gives

```text
t + \bar t = \binom{57}{3} - 56m + (1/2)\sum_i d_i^2.
```

Since `\binom{57}{3} = 29260`, this is

```text
t + \bar t = 29260 - 56m + (1/2)\sum_i d_i^2.
```

Conventions/ambiguities checked:

- This argument depends on the standard page-count convention for `B_k`.
- The lower bound `57 <= R(B13, B15)` is taken as input from the active packet, not reproved here.
- Solve stays inside the local packet and does not perform rediscovery checks.

# approach_A

Structural / invariant route:

1. Assume a `57`-vertex counterexample `G` exists.
2. Use the book-avoidance hypotheses to bound `t` and `\bar t`.
3. Combine those bounds with Goodman to force a very narrow edge count window and then a very narrow degree sequence.
4. Use integer convexity on `\sum d_i^2` to show the only possible edge count is `m = 798`, hence `G` is `28`-regular.
5. Equality in all counting bounds then forces:
   every edge has exactly `12` common neighbors and every nonedge has exactly `15` common neighbors.
6. That makes `G` a putative strongly regular graph with parameters `(57, 28, 12, 15)`.
7. The standard eigenvalue multiplicity formulas for those parameters are nonintegral, so such a graph cannot exist.

Why this path is attractive:

- It aims directly at theorem closure, not just a witness search.
- If it works, the proof is already paper-shaped: one clean contradiction with a named extremal object at the end.

# approach_B

Construction / extremal / contradiction route:

1. Try to extend the known `56`-vertex lower-bound architecture to `57` vertices.
2. Use the local degree translations for a putative counterexample:
   for a nonedge `uv`, the common-neighbor count in `G` must satisfy `c_G(u,v) >= d(u) + d(v) - 41`.
3. Around a fixed vertex `v` of degree `d`, the nonneighbor set `B(v)` would have to induce a `(41-d)`-regular graph on `56-d` vertices, equivalently a graph whose complement is `14`-regular.
4. Repeatedly exploiting those local regularity constraints might obstruct every witness extension.

Why I did not choose it:

- It looks more fragile and more dependent on detailed witness templates from the papers.
- The global counting route already seems to close the full theorem without code.

# lemma_graph

Proof skeleton:

1. Counterexample assumption:
   there exists `G` on `57` vertices with no `B13` and no `B15` in `\bar G`.
2. Triangle bounds:

```text
t <= 4m,    \bar t <= 14(1596 - m)/3.
```

3. Goodman identity:

```text
29260 - 56m + (1/2)\sum d_i^2 = t + \bar t <= 7448 - 2m/3.
```

Hence

```text
\sum d_i^2 <= -43624 + (332/3)m.          (1)
```

4. Continuous convexity also gives `\sum d_i^2 >= (2m)^2 / 57`, which forces `779 <= m <= 798`.
5. Because `2m` lies between `1558` and `1596`, integer convexity forces

```text
\sum d_i^2 >= (57-x)27^2 + x28^2 = 110m - 43092,
```

where `x = 2m - 1539`.
6. Combining that with `(1)` yields `m >= 798`, so with the previous window we get `m = 798`.
7. Therefore all degrees equal `28`.
8. Equality in the triangle bounds gives:

- every edge of `G` has exactly `12` common neighbors
- every edge of `\bar G` has exactly `14` common neighbors

9. Since `G` is `28`-regular, a nonedge `uv` has

```text
c_{\bar G}(u,v) = 55 - 28 - 28 + c_G(u,v) = c_G(u,v) - 1.
```

So `c_{\bar G}(u,v) = 14` implies `c_G(u,v) = 15` for every nonedge.
10. Thus `G` would be strongly regular with parameters `(57, 28, 12, 15)`.
11. On the orthogonal complement of the all-ones vector, the adjacency eigenvalues satisfy

```text
x^2 + (\mu - \lambda)x + (\mu - k) = x^2 + 3x - 13.
```

The roots are `(-3 +/- sqrt(61))/2`, and the corresponding multiplicities are

```text
28 +/- 56/sqrt(61),
```

which are not integers.
12. Contradiction.

# chosen_plan

Choose Approach A.

The main reason is proof leverage: the Goodman-plus-integrality squeeze is already theorem-shaped and avoids a construction-heavy witness hunt. It also naturally produces the best supporting slice for a paper:

- any `57`-vertex counterexample would have to be an infeasible strongly regular graph.

# self_checks

- Statement lock check: the whole argument uses only the standard interpretation "`B_k` means an edge with at least `k` common neighbors."
- Triangle-count check: `3t = \sum_{xy \in E(G)} c_G(x,y)`, so `c_G(x,y) <= 12` really does give `t <= 4m`. The complement bound is identical with `14`.
- Goodman check: `t + \bar t = \binom{57}{3} - (1/2)\sum d_i(56-d_i) = 29260 - 56m + (1/2)\sum d_i^2`.
- Integer-convexity check: once `779 <= m <= 798`, the average degree is between `27.33...` and `28`, so the minimum integer value of `\sum d_i^2` at fixed `2m` is attained by degrees only in `{27, 28}`.
- Equality check: at `m = 798`, equation `(1)` and the convex lower bound force exact equality, so `G` must be `28`-regular and both triangle upper bounds must be tight term-by-term.
- SRG check: regularity `28`, edge codegree `12`, and nonedge codegree `15` is exactly the parameter set `(57, 28, 12, 15)`.
- Spectral check: the nontrivial eigenvalue multiplicities being nonintegral is a decisive contradiction, assuming the standard strongly regular graph identity.

# code_used

No code used.

Reason:

- The contradiction closes at the reasoning stage.
- I do not yet see a need for a checker, witness verifier, or bounded experiment.

# result

Candidate exact solve:

Assume there is a graph `G` on `57` vertices with no `B13` and whose complement has no `B15`.

From the book bounds,

```text
t <= 4m,    \bar t <= 14(1596 - m)/3.
```

Goodman gives

```text
29260 - 56m + (1/2)\sum d_i^2 = t + \bar t <= 7448 - 2m/3,
```

so

```text
\sum d_i^2 <= -43624 + (332/3)m.          (1)
```

Also `\sum d_i^2 >= (2m)^2 / 57`, hence

```text
m^2 - 1577m + 621642 <= 0,
```

which forces `779 <= m <= 798`.

Now minimize `\sum d_i^2` over integer degree sequences with total degree `2m`. Since the average degree is at most `28`, the minimum occurs when all degrees are `27` or `28`. If `x` vertices have degree `28`, then

```text
27(57 - x) + 28x = 2m  =>  x = 2m - 1539,
```

and therefore

```text
\sum d_i^2 >= (57 - x)27^2 + x28^2 = 110m - 43092.     (2)
```

Combining `(1)` and `(2)`:

```text
110m - 43092 <= -43624 + (332/3)m
```

which simplifies to

```text
2m >= 1596.
```

So `m >= 798`. Together with `m <= 798`, this gives `m = 798`.

Hence `G` is `28`-regular, and all inequalities above are equalities. Therefore:

- every edge of `G` has exactly `12` common neighbors
- every edge of `\bar G` has exactly `14` common neighbors

For a nonedge `uv` of `G`, regularity gives

```text
c_{\bar G}(u,v) = 55 - 28 - 28 + c_G(u,v) = c_G(u,v) - 1,
```

so `c_G(u,v) = 15`.

Thus `G` would be a strongly regular graph with parameters `(57, 28, 12, 15)`.

But for a strongly regular graph with parameters `(v, k, \lambda, \mu)`, the nontrivial eigenvalues satisfy

```text
x^2 + (\mu - \lambda)x + (\mu - k) = 0.
```

Here this is

```text
x^2 + 3x - 13 = 0,
```

with roots `(-3 +/- sqrt(61))/2`. The corresponding multiplicities are

```text
28 +/- 56/sqrt(61),
```

not integers. That is impossible for an adjacency matrix.

So no such `57`-vertex counterexample exists. Since the active packet already records the lower bound `57 <= R(B13, B15)`, the candidate conclusion is

```text
R(B13, B15) = 57.
```

Smallest immediate supporting slice:

- Any `57`-vertex graph avoiding `B13` and co-avoiding `B15` would have to realize the impossible strongly regular parameter set `(57, 28, 12, 15)`.

Natural immediate corollary / remark:

- The one-gap interval `57 <= R(B13, B15) <= 58` collapses on the lower endpoint because the only extremal equality pattern is spectrally infeasible.

Why this instance matters:

- It closes an almost-diagonal `B_{n-2}` versus `B_n` book Ramsey gap with a proof whose core obstruction is structural rather than computational.

What scales:

- The Goodman-plus-integrality squeeze should scale to other one-gap almost-diagonal book pairs when the upper and lower bounds are tight enough to force a near-regular extremal graph.

What does not obviously scale:

- The final contradiction here depends on landing on a specific infeasible strongly regular parameter set; other nearby pairs may land on feasible parameter sets or fail to force exact regularity.

What theorem slice is suggested:

- A reusable theorem template is: if a one-gap book Ramsey counterexample is forced into a unique strongly regular parameter set, then spectral infeasibility can close the Ramsey number exactly.

What next parameter shifts would help most:

- Test the same squeeze on the next live `B_{n-2}` versus `B_n` one-gap cases.
- The first concrete shifts worth checking are `(12, 14)` and `(14, 16)` if their live windows are also width `1`.

Current package assessment:

- If the counting and spectral steps survive verify, this is much closer to a paper-shaped claim than to a bare instance, because the exact theorem and the obstruction lemma are already both present.

# family_affinity

Strong family affinity.

This sits directly on the almost-diagonal book Ramsey line `B_{n-2}` versus `B_n`, and the proof naturally explains why a one-gap residue on that line can collapse by forcing an impossible extremal configuration.

# generalization_signal

Moderate-positive.

The method is not a generic formula proof, but it does expose a reusable signal:

- when the gap is width `1`

## verify_rediscovery

- Bounded prior-art audit run on `2026-04-14` with limited web, using exact-instance queries for `R(B13, B15)`, alternate notation queries for `R(B_13, B_15)` and `book Ramsey 13 15`, and canonical-source checks keyed to DS1.17, Lidicky-McKinley-Pfender-Van Overberghe 2025, and Wesley 2026.
- Within budget, the audit re-found only the already-recorded one-gap state: DS1.17 still supplies the general upper bound `R(B13, B15) <= 58`, the 2025 book-Ramsey paper supplies the lower bound `57 <= R(B13, B15)`, and Wesley 2026 resolves the adjacent pair `R(B14, B15) = 59` rather than the selected pair.
- I did not find an exact closure of `R(B13, B15)` or a same-source theorem / proposition / example / observation / corollary that directly settles the exact pair.
- Rediscovery is therefore not established within the bounded verify pass.

## verify_faithfulness

- The solve artifact is faithful to the intended statement.
- It does not drift to a proxy family claim or a neighboring Ramsey pair.
- The claimed conclusion is exactly: every graph on `57` vertices contains `B13` or its complement contains `B15`, hence `R(B13, B15) = 57` once the packet's recorded lower bound `57 <= R(B13, B15)` is admitted from the literature.
- The only explicit dependency outside the local proof is that recorded lower bound. That is compatible with the selected packet and does not change the theorem being claimed.

## verify_proof

- I did not find a first incorrect step.
- The triangle bounds are correct: `3t = \sum_{xy in E(G)} c_G(x,y)` and `c_G(x,y) <= 12` give `t <= 4m`; the complement analogue gives `\bar t <= 14(1596-m)/3`.
- The Goodman specialization is correct:

```text
t + \bar t = 29260 - 56m + (1/2)\sum_i d_i^2.
```

- Combining Goodman with the triangle bounds yields

```text
\sum_i d_i^2 <= -43624 + (332/3)m.
```

- Together with Cauchy / convexity, `\sum_i d_i^2 >= (2m)^2/57`, this becomes

```text
m^2 - 1577m + 621642 <= 0,
```

so the integer edge window is exactly `779 <= m <= 798`.
- The integer convexity step is also correct: for fixed degree sum `2m` with average degree in `(27,28]`, the minimum integer value of `\sum d_i^2` is attained by a `{27,28}`-valued degree sequence, giving

```text
\sum_i d_i^2 >= 110m - 43092.
```

- Comparing the two bounds forces `m >= 798`, hence `m = 798`. Equality then forces `G` to be `28`-regular and forces equality in both triangle upper bounds, so every edge of `G` has exactly `12` common neighbors and every edge of `\bar G` has exactly `14` common neighbors.
- For a nonedge `uv` of `G`, the identity

```text
c_{\bar G}(u,v) = 55 - d(u) - d(v) + c_G(u,v)
```

specializes under `28`-regularity to `c_{\bar G}(u,v) = c_G(u,v) - 1`, so `c_G(u,v) = 15`.
- That gives a strongly regular parameter set `(57, 28, 12, 15)`. The standard nontrivial eigenvalue equation

```text
x^2 + (\mu-\lambda)x + (\mu-k) = 0
```

becomes `x^2 + 3x - 13 = 0`, with roots `(-3 +/- sqrt(61))/2`, and the multiplicities are `28 +/- 56/sqrt(61)`, which are nonintegral. That is impossible.
- Conclusion: the local proof is mathematically coherent as written, modulo the external lower-bound citation already locked in the packet.

## verify_adversarial

- No dedicated checker or witness-verifier file exists in the candidate artifact; `record.md` also states that no solve-stage code was used.
- I reran the vulnerable arithmetic by direct computation:
  - `\binom{57}{2} = 1596`, `\binom{57}{3} = 29260`
  - the quadratic window is exactly rooted at `m = 779` and `m = 798`
  - the convex lower bound and Goodman upper bound meet only at `m = 798`
  - the claimed multiplicities `28 +/- 56/sqrt(61)` are indeed nonintegral
- I did not find a computational or combinatorial counterexample to the argument's key equality chain.

## verify_theorem_worthiness

- Exactness: strong, conditional only on the packet's cited lower bound, which is exactly the right external input for this selected problem.
- Novelty: still plausible after the bounded rediscovery pass; no exact prior closure surfaced.
- Reproducibility: high. The proof is short, arithmetic-heavy rather than search-heavy, and all decisive constants are easy to rerun.
- Lean readiness: yes. The claim is cleanly theorem-shaped and the proof decomposes into standard counting lemmas plus an SRG spectral contradiction.
- Paper leverage: strong. If correct and Lean-sealed, this already looks like most of a publishable micro-note rather than an isolated curiosity.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? Yes.
- What percentage of the paper would one solve already provide? About `0.85`.
- What title theorem is actually visible? `The Exact Value of R(B13, B15)`.
- What part of the argument scales? The Goodman-plus-integrality squeeze that forces a one-gap counterexample into a narrowly constrained regular or near-regular extremal shape.
- What part clearly does not? The final contradiction is instance-specific: it depends on landing on the spectrally impossible SRG parameter set `(57, 28, 12, 15)`.
- Best honest publication status now: `SLICE_CANDIDATE`, not `INSTANCE_ONLY`, because the theorem has a clear family anchor and already reads like a note title if the current verification stands.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- `classification = "CANDIDATE"`
- No rediscovery was established in PASS 1.
- No wrong-statement drift was found in PASS 2.
- No first incorrect proof step was found in PASS 3.
- The adversarial rerun in PASS 4 supported the arithmetic spine of the proof.
- The run must remain below `EXACT` until Lean completes.

## minimal_repair_if_any

- No mathematical repair was needed.
- The conservative repair is classificatory only: keep the result at verified `CANDIDATE`, not `EXACT`, until Lean seals the theorem.
- and the triangle bounds nearly saturate Goodman
- and the remaining variance budget is tiny

then the counterexample space may collapse to a near-regular or strongly regular candidate.

# proof_template_reuse

Reusable template:

1. Translate book avoidance into edge-codegree caps in `G` and `\bar G`.
2. Combine with Goodman to upper-bound `\sum d_i^2`.
3. Use integer convexity to force a unique degree sequence.
4. Push equality to exact edge and nonedge codegrees.
5. Identify the resulting strongly regular parameter set.
6. Kill the parameter set by spectral multiplicity or another feasibility obstruction.

That template is stronger than a one-off witness search and is the main reason this solve would transfer to nearby micro-paper candidates.

# candidate_theorem_slice

Best supporting theorem slice:

If a graph on `57` vertices avoids `B13` and its complement avoids `B15`, then it must be strongly regular with parameters `(57, 28, 12, 15)`. Since that parameter set is spectrally infeasible, such a graph does not exist.

This slice is worth keeping even if some arithmetic detail in the final Ramsey conclusion needs polishing, because it isolates the exact extremal obstruction.

# smallest_param_shift_to_test

Smallest useful follow-up shifts:

- `R(B12, B14)` if its current literature window is also a single gap.
- `R(B14, B16)` for the same reason.

Reason:

- they preserve the almost-diagonal shape where this Goodman-to-SRG template is most likely to transfer.

# why_this_is_or_is_not_publishable

If the proof verifies, this is publishable in the strict micro-paper lane.

Why:

- the exact title theorem is already crisp: `R(B13, B15) = 57`
- the solve would already be roughly `85%` to `90%` of the paper
- the remaining work is cheap exposition, verification, and possibly Lean formal packaging

What still has to happen before calling it paper-ready:

- verify the Goodman arithmetic line by line
- verify the strongly regular multiplicity contradiction cleanly
- run the bounded prior-art audit in the later stage
- optionally formalize the short counting chain if the manager wants Lean closure

# paper_shape_support

What makes this paper-shaped beyond a bare exact value:

- the title theorem is exact and family-anchored
- the proof has a compact named mechanism: Goodman squeeze plus infeasible strongly regular extremal case
- the boundary remark is immediate and clean
- the post-solve editorial overhead is low

Minimal remaining packaging work:

- a 1-2 paragraph setup explaining the one-gap literature window
- one polished theorem-proof section
- one short comparison remark with the adjacent `R(B14, B15) = 59` benchmark already noted in the packet

# boundary_remark

Boundary remark:

This argument appears tuned to exact one-gap cases. If the literature window were wider than `1`, the same Goodman squeeze would likely leave too much degree variance and would no longer force a unique extremal configuration.

# likely_failure_points

- The biggest technical risk is a sign or constant slip in the Goodman-to-`sum d_i^2` calculation.
- The second risk is the strongly regular multiplicity algebra; it should be written explicitly in verify rather than left implicit.
- A softer risk is notation mismatch if some source uses a different indexing convention for `B_k`.
- A publication-stage risk remains that the exact value could already be known despite the packet's bounded novelty check, but solve itself is not the stage to clear that.

# what_verify_should_check

- Recheck the book translation: `B13` means edge codegree at least `13`, `B15` means edge codegree at least `15`.
- Recompute `\binom{57}{2} = 1596` and `\binom{57}{3} = 29260`.
- Re-derive Goodman exactly:
  `t + \bar t = 29260 - 56m + (1/2)\sum d_i^2`.
- Re-derive inequality `(1)` and the window `779 <= m <= 798`.
- Re-derive the integer convexity lower bound `(2)` and the conclusion `m = 798`.
- Confirm that equality forces `28`-regularity and exact codegrees `(12, 15)`.
- Write the strongly regular multiplicity computation explicitly and confirm the nonintegrality.
- Then perform the bounded rediscovery search and only after that decide whether to promote toward publication audit and Lean.
