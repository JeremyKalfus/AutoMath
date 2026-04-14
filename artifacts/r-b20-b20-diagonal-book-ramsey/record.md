# Solve Record: Determine the exact value of R(B20, B20)

## statement_lock
Active slug: `r-b20-b20-diagonal-book-ramsey`.

Active title: `Determine the exact value of R(B20, B20)`.

Locked target: decide whether every red-blue coloring of `K_81` already forces a monochromatic `B20`, since the active packet imports the frontier interval `81 <= R(B20, B20) <= 82`.

Convention: `B20` is the book with `20` pages, meaning one spine edge together with `20` further vertices adjacent to both spine endpoints. In a color class, a monochromatic `B20` is therefore equivalent to an edge contained in at least `20` monochromatic triangles.

Exact title theorem if this closes on the witness side: `R(B20, B20) = 82`.

Exact title theorem if this closes on the forcing side: `R(B20, B20) = 81`.

If the exact endpoint is settled honestly, that is already about `70-90%` of a short paper: the title theorem is the main result, the literature gap is only one step wide, and the remaining packaging is mostly the frontier comparison plus a compact proof or witness description.

## definitions
Let `G` be the red graph of a red-blue coloring of `K_n`; the blue graph is its complement.

For a red edge `uv`, let `tau_R(uv) = |N_G(u) ∩ N_G(v)|`. Then `G` is red-`B20`-free exactly when `tau_R(uv) <= 19` for every red edge `uv`.

Likewise, the blue graph is blue-`B20`-free exactly when every blue edge has at most `19` common blue neighbors.

Write `T_R, T_B` for the numbers of red and blue triangles, and `e_R, e_B` for the numbers of red and blue edges.

A strongly regular graph `srg(v,k,lambda,mu)` has `v` vertices, is `k`-regular, every edge lies in exactly `lambda` triangles, and every nonedge has exactly `mu` common neighbors.

## approach_A
Structural / invariant route: repeat the knife-edge counting argument at `n = 81`.

If a coloring of `K_81` avoids monochromatic `B20`, then every monochromatic edge lies in at most `19` monochromatic triangles. Summing over edges gives

`3 T_R <= 19 e_R`, `3 T_B <= 19 e_B`,

so

`T_R + T_B <= (19/3)(e_R + e_B) = (19/3) * binom(81,2) = 20520`.

For odd `n`, Goodman's bound gives

`T_R + T_B >= n(n-1)(n-3)/24`,

and for `n = 81` this is also

`81 * 80 * 78 / 24 = 20520`.

So equality is forced. Any `B20`-free coloring of `K_81` must therefore be extremal in every place where the counting argument had slack.

Consequences of equality:

- every vertex has red degree exactly `40` and blue degree exactly `40`;
- every red edge has exactly `19` red common neighbors;
- every blue edge has exactly `19` blue common neighbors.

For a red nonedge `uv`, if `mu = |N_G(u) ∩ N_G(v)|`, then the number of common blue neighbors is

`79 - (40 + 40 - mu) = mu - 1`.

Since `uv` is a blue edge and every blue edge has exactly `19` common blue neighbors, it follows that `mu = 20`.

Therefore any critical `81`-vertex coloring with no monochromatic `B20` induces a red graph `srg(81,40,19,20)`. This is exactly the conference-graph parameter set at order `81`.

## approach_B
Construction / extremal route: instead of trying to force `B20` on `81` vertices, try to realize the extremal structure exposed by Approach A.

The structural reduction says a witness, if it exists, must be much more rigid than a generic coloring. It must be a conference graph with parameters `srg(81,40,19,20)`.

That suggests the natural candidate is the Paley graph of order `81`, because Paley graphs on fields of order `q ≡ 1 (mod 4)` are conference graphs with parameters

`srg(q, (q-1)/2, (q-5)/4, (q-1)/4)`.

For `q = 81`, these parameters become exactly

`srg(81,40,19,20)`.

If such a graph is realized, then every red edge lies in exactly `19` red triangles and every blue edge lies in exactly `19` blue triangles, so both color classes are `B20`-free. That would give an explicit `81`-vertex witness and therefore show `R(B20, B20) = 82` using the packet's imported upper bound `R(B20, B20) <= 82`.

## lemma_graph
1. Work at the only live endpoint order `n = 81`.
2. Assume a red-blue coloring of `K_81` has no monochromatic `B20`.
3. Then every monochromatic edge lies in at most `19` monochromatic triangles.
4. Hence `T_R + T_B <= (19/3) * binom(81,2) = 20520`.
5. Goodman's theorem gives the opposite inequality `T_R + T_B >= 20520`.
6. Therefore equality holds, forcing `40`-regularity in each color and exact local triangle counts.
7. A red nonedge then has exactly `20` red common neighbors, so the red graph is `srg(81,40,19,20)`.
8. Any `srg(81,40,19,20)` immediately yields a red-blue coloring of `K_81` with no monochromatic `B20`.
9. A Paley graph on `81` vertices is expected to realize `srg(81,40,19,20)`.
10. Therefore the solve reduces to verifying the existence and local counts of that Paley witness.

## chosen_plan
Choose Approach B.

Reason: the knife-edge structure at `81 = 4 * 20 + 1` does not point toward an impossibility. It points toward the existence of a conference graph, and `81` is exactly the kind of order where a Paley conference graph should exist. So the shortest honest route is to present the witness class, explain why it has the right parameters, and use a tiny bounded computation only if needed to verify the common-neighborhood counts directly.

## self_checks
Self-check after statement lock: the only unresolved endpoint is `81` versus `82`, so analyzing `K_81` is correct.

Self-check after Approach A: the arithmetic matches exactly. `binom(81,2) = 3240`, and `(19/3) * 3240 = 20520`; Goodman's odd-order lower bound also gives `20520`.

Self-check after the nonedge computation: for a red nonedge `uv`, the common blue neighbors are exactly the vertices adjacent to neither `u` nor `v` in red, namely `79 - (40 + 40 - mu) = mu - 1`, so blue-edge equality indeed forces `mu = 20`.

Self-check on direction: unlike the `B19` case, the conference-graph reduction here suggests existence rather than arithmetic obstruction. So a witness-first solve is the right lane.

Self-check after bounded verification: a direct local construction over `F_81 = F_3[t]/(t^4 + t^3 + t^2 + 1)` with red adjacency defined by `x-y` being a nonzero square produced a symmetric graph on `81` vertices with degree set `{40}`, red-edge common-neighbor set `{19}`, and red-nonedge common-neighbor set `{20}`. So the expected Paley witness parameters check out exactly.

## code_used
One bounded Python verifier was used for witness verification only.

It searched for an irreducible quartic over `F_3`, obtained `t^4 + t^3 + t^2 + 1`, built `F_81 = F_3[t]/(t^4 + t^3 + t^2 + 1)`, defined the Paley graph by declaring `x` adjacent to `y` when `x-y` is a nonzero square, and checked the local parameters directly.

Observed output:

- `40` nonzero squares;
- symmetric adjacency because `-1` is a square;
- degree set `{40}`;
- edge common-neighbor set `{19}`;
- nonedge common-neighbor set `{20}`.

No search, SAT, ILP, or brute force was used.

## result
Candidate conclusion: `R(B20, B20) = 82`.

Explicit witness package.

Let `F_81 = F_3[t]/(t^4 + t^3 + t^2 + 1)`. Color the edge `xy` of `K_81` red when `x-y` is a nonzero square in `F_81`, and blue otherwise. Because `-1` is a square in `F_81`, this is an undirected coloring.

The bounded verifier confirms that the red graph is `srg(81,40,19,20)`. Hence:

- every red edge lies in exactly `19` red triangles, so the red graph is `B20`-free;
- every blue edge lies in exactly `19` blue triangles, because the complement of a conference graph with these parameters has the same parameters, so the blue graph is also `B20`-free.

Therefore this coloring of `K_81` contains no monochromatic `B20`, and so

`R(B20, B20) > 81`.

The active packet imports the source-backed upper bound `R(B20, B20) <= 82`. Combining these yields the solve-stage exact-value candidate

`R(B20, B20) = 82`.

This is already very close to paper shape. The exact title theorem would be `The Exact Value of R(B20, B20)`. The minimal remaining packaging work is to present the Paley construction cleanly, cite the imported upper bound precisely, and decide whether to keep the direct parameter check as a supplemental computational certificate or replace it with a short standard Paley-graph citation.

## family_affinity
This candidate sits exactly on the diagonal `R(B_m, B_m)` knife-edge line `n = 4m + 1`, where the Goodman lower bound and the monochromatic-book triangle cap meet with no slack.

For `m = 20`, that edge-of-equality order is `81`, so the family structure is unusually rigid and naturally tied to conference graphs.

## generalization_signal
There is a clear family signal:

If a red-blue coloring of `K_{4m+1}` avoids a monochromatic `B_m`, then the red graph must be `srg(4m+1, 2m, m-1, m)`.

So the diagonal knife-edge cases reduce systematically to the existence or nonexistence of conference graphs.

For `m = 20`, the parameter set is favorable because `81` is a prime power congruent to `1 mod 4`, which is exactly the usual Paley-construction regime.

## proof_template_reuse
Reusable template:

1. turn `B_m`-avoidance into an edgewise cap on monochromatic triangles;
2. compare against Goodman's lower bound at `n = 4m + 1`;
3. force equality and deduce `srg(4m+1, 2m, m-1, m)`;
4. decide the endpoint by the existence or nonexistence of that conference graph.

What scales: the equality reduction and parameter extraction.

What does not automatically scale: the last existence step, which depends on the arithmetic / explicit construction regime for the corresponding conference graph order.

In this specific case, the part that scales is the conference-graph reduction at `n = 4m + 1`. The part that does not scale automatically is the witness existence itself; here it works because `81` lies in the Paley regime, but nearby orders need not.

## candidate_theorem_slice
Primary slice:

Any red-blue coloring of `K_81` with no monochromatic `B20` induces a strongly regular graph `srg(81,40,19,20)`.

Title-theorem slice if the witness seals:

The Paley graph of order `81` gives a red-blue coloring of `K_81` with no monochromatic `B20`, and hence `R(B20, B20) = 82`.

## smallest_param_shift_to_test
The first natural shift is the neighboring diagonal case `m = 21`, which would ask for a conference graph on `85` vertices. That tests whether the same existence-side phenomenon persists beyond the prime-power square order `81`.

The second useful shift is to revisit `m = 19`, where the same conference-graph reduction points in the opposite direction because order `77` appears obstruction-driven rather than construction-driven.

## why_this_is_or_is_not_publishable
If the Paley witness is written explicitly and its local counts are verified cleanly, this looks publishable in the micro-paper lane.

Why: the exact title theorem would be `R(B20, B20) = 82`; the solve would already contribute the decisive endpoint witness, the structural conference-graph reduction, and the natural one-step frontier comparison. That is comfortably in the advertised `70-90%` paper zone.

What minimal packaging would remain:

- cite the imported upper bound `81 <= R(B20, B20) <= 82`;
- write the Paley witness explicitly enough for reproducibility;
- add one short structural lemma explaining why the witness has `19` monochromatic triangles on each monochromatic edge.

Without sealing the Paley witness explicitly, the current package is still too thin. In that state it is a theorem-facing construction plan, not yet a micro-paper result.

With the witness now written explicitly and locally checked, the package is no longer just an instance-level curiosity. It is closer to a paper-shaped exact-value claim, although verify still needs to confirm the imported upper-bound citation and decide how much standard Paley theory should be cited versus recomputed.

## paper_shape_support
If the main claim closes, the smallest extra structure needed for paper shape is:

- one lemma giving the `srg(81,40,19,20)` reduction from `B20`-avoidance at `K_81`;
- one explicit paragraph describing the Paley graph on `F_81`;
- one immediate remark that the complement has the same parameters, so the witness is genuinely two-color symmetric;
- one sentence comparing the closure with the imported one-step interval `81 <= R(B20, B20) <= 82`.

The immediate corollary / boundary remark is that every monochromatic edge in the witness lies in exactly `19` monochromatic triangles, so the construction is perfectly tight against the `B20` threshold.

One natural immediate remark is that the witness is exactly tight: replacing `B20` by `B19` would no longer be avoided, since every monochromatic edge already lies in `19` monochromatic triangles.

## boundary_remark
Boundary remark: this case appears to be controlled by exact conference-graph existence rather than by an irregular ad hoc coloring. The expected witness is maximally balanced: each vertex has `40` neighbors in each color, every red edge has exactly `19` red common neighbors, and every blue edge has exactly `19` blue common neighbors.

If the witness is confirmed, the result is not merely “some exact instance”; it comes with a rigid extremal object and a compact explanation of why the endpoint lands at `82`.

## likely_failure_points
The main risk is explicitness: I still need to present the Paley witness at a level verify can audit without importing too much external theory.

The second risk is presentation: verify must decide whether the direct local parameter check is enough as a durable certificate, or whether the solve should be rewritten around a standard theorem on Paley graph parameters.

The structural reduction to `srg(81,40,19,20)` looks robust.

## what_verify_should_check
Check the Goodman equality argument at `n = 81` and confirm there is no arithmetic slip in the forced parameters.

Check the conversion from a `B20`-free coloring of `K_81` to `srg(81,40,19,20)`.

Check that the Paley graph of order `81` exists and has parameters `(81,40,19,20)`.

Check that the complement of this graph has the same parameters, so both colors are `B20`-free.

Check whether the family-shaped slice "knife-edge diagonal book cases reduce to conference-graph existence" is already standard folklore and how to frame it conservatively.

## verify_rediscovery
Bounded PASS 1 established rediscovery within budget, so web work stopped there.

The active packet's novelty basis was incorrect. The canonical 2025 source still records the interval `81 <= R(B20, B20) <= 82`, but a bounded recent-status check surfaced William J. Wesley, `Lower bounds for book Ramsey numbers` (Discrete Mathematics 349(5), 2026), which explicitly cites the older theorem of Rousseau and Sheehan: `R(B_n, B_n) = 4n + 2` whenever `4n + 1` is a prime power.

For `n = 20`, we have `4n + 1 = 81 = 3^4`, so this classical theorem already gives

`R(B20, B20) = 82`.

This was corroborated by a bibliographic hit for Rousseau-Sheehan, `On Ramsey Numbers for Books` (Journal of Graph Theory 2 (1978), 77-87). That is enough to classify the exact intended statement as already solved in prior art.

PASS 1 verdict: `REDISCOVERY`.

## verify_faithfulness
The solver's mathematical target matches the intended statement exactly. The record aims to determine the exact value of `R(B20, B20)` by constructing a `K_81` coloring with no monochromatic `B20` and combining that witness with the known upper bound.

No quantifier drift, definition drift, or proxy-theorem substitution was found inside the solve writeup itself. The main faithfulness failure is external to the proof body: the packet and solve framing treated the exact statement as frontier-open even though the exact value was already known.

Faithfulness verdict: exact statement targeted, but novelty/public-status framing drifted from reality.

## verify_proof
No incorrect mathematical step was found in the lower-bound witness argument itself.

The Goodman equality calculation at `n = 81` is correct, the forced parameter extraction to `srg(81,40,19,20)` is correct, and the Paley-style construction described in the record does produce that parameter set.

The first substantive failure in the overall solve packet is therefore not a proof error but a novelty error: the claim was pursued as an open frontier exact-value problem even though prior literature already settles the exact statement.

Proof-correctness verdict: the witness argument is mathematically sound as a rederivation, but it does not constitute a frontier solve.

## verify_adversarial
I reran the witness construction inline from the solve description over

`F_81 = F_3[t]/(t^4 + t^3 + t^2 + 1)`,

with red adjacency defined by `x-y` being a nonzero square.

Observed checks:

- `40` nonzero squares;
- `-1` is a square, so the adjacency is undirected;
- degree set `{40}`;
- red-edge common-neighbor set `{19}`;
- red-nonedge common-neighbor set `{20}`.

So the construction really is an `srg(81,40,19,20)`. Its complement therefore has the same parameters, and both colors are `B20`-free. The adversarial pass did not break the witness; it confirmed that the solve rediscovered a genuine classical extremal construction.

## verify_theorem_worthiness
Exactness: yes, the visible theorem is the exact statement `R(B20, B20) = 82`.

Novelty: no. PASS 1 establishes that this exact theorem is already in prior art, so the honest classification is `REDISCOVERY`.

Reproducibility: high. The Paley witness is explicit and the local parameter check is easy to rerun.

Lean readiness: no. Lean would not seal a frontier publication packet here; the bottleneck is not rigor but novelty. Formalizing a rediscovered exact theorem would be optional archival work, not the shortest path to a publishable micro-paper.

Paper leverage:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? `No`, because the exact theorem is already known.
- What percentage of a new paper would one solve already provide? About `5%` at most, as an expository verification note rather than a frontier contribution.
- What title theorem is actually visible? `The Exact Value of R(B20, B20)`.
- What part of the argument scales? The knife-edge reduction from `B_m`-avoidance on `K_{4m+1}` to `srg(4m+1, 2m, m-1, m)`, together with Paley/conference-graph witnesses when `4m+1` lies in the standard prime-power regime.
- What part clearly does not? The novelty claim. This exact diagonal instance is not publication-fresh.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? Neither; for harness purposes it is `REDISCOVERY`.

The theorem is true, exact, and reproducible, but it fails the micro-paper lane because the decisive publication criterion here is novelty, not correctness.

## verify_verdict
`REDISCOVERY`.

Reason: the exact intended statement `R(B20, B20) = 82` was already settled in prior art via the Rousseau-Sheehan prime-power theorem, and the current solve packet independently reconstructs one of the classical witness mechanisms rather than closing an open frontier gap.

## minimal_repair_if_any
No mathematical repair is needed to the witness argument.

The minimal conservative repair is classificatory only:

- relabel the run as `REDISCOVERY`;
- archive it as prior art rather than as a frontier success;
- preserve the explicit Paley witness check as a useful reusable certificate pattern for future diagonal book cases, but not as a publication-ready new result.
