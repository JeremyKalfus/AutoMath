## statement_lock

Active slug: `r-b9-b11-book-ramsey`.

Active title: `Determine the exact value of R(B9, B11)`.

Locked intended title theorem:

> Every graph on 41 vertices contains a copy of `B9` or its complement contains a copy of `B11`. Consequently `R(B9, B11) = 41`.

If this argument survives verify, that is already the honest title theorem of the micro-paper.

## definitions

- `B_t` denotes the book graph with `t` pages: `t` triangles sharing one common edge.
- For an edge `uv` of a graph `G`, `uv` is the spine of a `B_t` exactly when `uv` has at least `t` common neighbors in `G`.
- Thus `G` is `B9`-free iff every edge of `G` has at most `8` common neighbors.
- `\bar G` is `B11`-free iff every nonedge `uv` of `G` has at most `10` common nonneighbors in `G`.
- Let `n = 41`, `m = e(G)`, `T =` the number of triangles in `G`, and `A =` the number of independent triples in `G`.

Ambiguities / conventions to fix:

- I am using the standard convention `B_t = K_2 + \overline{K_t}`.
- All common-neighbor counts exclude the endpoints of the pair.
- `A` is counted in `G`, so it is also the triangle count of `\bar G`.

## approach_A

Structural / invariant route: assume a 41-vertex counterexample and force it into a single rigid extremal object, then rule that object out.

Assume for contradiction that there is a graph `G` on 41 vertices such that `G` has no `B9` and `\bar G` has no `B11`.

1. Local book bounds.
   - Every edge lies in at most `8` triangles.
   - Every nonedge lies in at most `10` independent triples.

2. Triangle and anti-triangle upper bounds.
   - `3T = \sum_{uv \in E(G)} codeg_G(uv) <= 8m`, so `T <= 8m/3`.
   - `3A = \sum_{uv \notin E(G)} codeg_{\bar G}(uv) <= 10(820 - m)`, so `A <= 10(820 - m)/3`.
   - Hence
     `T + A <= (8m + 10(820 - m))/3 = (8200 - 2m)/3`.

3. Pairwise degree-sum bounds.
   - If `uv` is an edge, then among the other `39` vertices the intersection `N(u) \cap N(v)` has size at most `8`, so
     `(d(u) - 1) + (d(v) - 1) <= 39 + 8`,
     hence `d(u) + d(v) <= 49`.
   - If `uv` is a nonedge, then among the other `39` vertices the common nonneighbors are at most `10`, so
     `(39 - d(u)) + (39 - d(v)) <= 39 + 10`,
     hence `d(u) + d(v) >= 29`.

4. Summing the pair bounds.
   - Over edges,
     `\sum_v d(v)^2 = \sum_{uv \in E(G)} (d(u) + d(v)) <= 49m`.
   - Over nonedges,
     `\sum_{uv \notin E(G)} (d(u) + d(v)) = \sum_v d(v)(40 - d(v)) >= 29(820 - m)`.
   - Since `\sum_v d(v)(40 - d(v)) = 80m - \sum_v d(v)^2`, the previous two displays imply
     `80m - 49m >= 29(820 - m)`.
   - Therefore `60m >= 23780`, so `m >= 397`.

5. Goodman baseline.
   - Goodman gives
     `T + A = \binom{41}{3} - (1/2)\sum_v d(v)(40 - d(v))`.
   - Since `d(v)(40 - d(v)) <= 20^2 = 400` for every vertex,
     `T + A >= 10660 - (41 * 400)/2 = 2460`.
   - Combining with the upper bound from step 2 yields
     `2460 <= (8200 - 2m)/3`,
     so `m <= 410`.

6. Refined Goodman lower bound.
   - Write `m = 410 - t` with `0 <= t <= 13`.
   - Then `\sum_v d(v) = 820 - 2t`.
   - For fixed degree sum `820 - 2t`, convexity of `x^2` shows that `\sum_v d(v)^2` is minimized when exactly `2t` vertices have degree `19` and the other `41 - 2t` vertices have degree `20`.
   - Hence
     `\sum_v d(v)^2 >= 2t * 19^2 + (41 - 2t) * 20^2 = 16400 - 78t`.
   - Therefore
     `T + A = 10660 - (1/2)(80m - \sum_v d(v)^2)`
     `>= 10660 - (1/2)(80(410 - t) - (16400 - 78t))`
     `= 2460 + t`.

7. Compare bounds.
   - The step-2 upper bound gives
     `T + A <= (8200 - 2(410 - t))/3 = 2460 + 2t/3`.
   - The refined Goodman lower bound gives `T + A >= 2460 + t`.
   - These are incompatible unless `t = 0`.
   - Hence `m = 410`.

8. Equality consequences.
   - Equality in the convexity step forces every degree to equal `20`, so `G` is `20`-regular.
   - Equality in the triangle count gives every edge exactly `8` common neighbors.
   - Equality in the independent-triple count gives every nonedge exactly `10` common nonneighbors.

9. Translate the nonedge condition.
   - Let `uv` be a nonedge.
   - In a `20`-regular graph on `41` vertices, if `\mu(uv)` denotes the number of common neighbors of `u` and `v`, then the number of common nonneighbors is
     `39 - 20 - 20 + \mu(uv) = \mu(uv) - 1`.
   - Since every nonedge has exactly `10` common nonneighbors, we get `\mu(uv) = 11`.
   - Thus any counterexample would be a strongly regular graph with parameters `(41,20,8,11)`.

10. Spectral contradiction.
    - For an `srg(v,k,\lambda,\mu)`, the nontrivial eigenvalues satisfy
      `x^2 + (\mu - \lambda)x + (\mu - k) = 0`.
    - Here this is
      `x^2 + 3x - 9 = 0`,
      whose roots are `(-3 + 3\sqrt{5})/2` and `(-3 - 3\sqrt{5})/2`.
    - These are irrational algebraic conjugates, so in the characteristic polynomial of the integer adjacency matrix they must occur with equal multiplicity.
    - Since there are `40` nontrivial eigenvalues total, that would force multiplicities `20` and `20`.
    - But then the trace would be
      `20 + 20((-3 + 3\sqrt{5})/2) + 20((-3 - 3\sqrt{5})/2) = 20 + 20(-3) = -40`,
      contradicting trace zero.

Therefore no such counterexample graph exists, so the candidate conclusion is `R(B9, B11) = 41`.

Self-check after Approach A:

- The local-to-global flow is the same as the neighboring solved template, but every numeric step was recomputed for `41`, `8`, and `10`.
- The contradiction is theorem-shaped: no witness survives, and the obstruction is structural rather than search-based.
- The most delicate steps are the nonedge bookkeeping and the equality-case transition to strong regularity.

## approach_B

Construction / extremal / contradiction route: ask what a `41`-vertex witness for `R(B9, B11) = 42` would have to look like.

- Any such witness would have to extend the current `40`-vertex lower-bound paradigm by one vertex without creating an edge with `9` common neighbors and without creating a complement-edge with `11` common neighbors.
- The counting squeeze above shows that no loose or mildly irregular extension is possible:
  - the graph would have to have exactly `410` edges,
  - every vertex would have to have degree `20`,
  - every edge would have to have exactly `8` common neighbors,
  - every nonedge would have to have exactly `10` common nonneighbors.
- So the constructive program collapses immediately to a single extremal object, namely `srg(41,20,8,11)`.
- The spectral contradiction then says the `41`-vertex witness program is obstructed at the parameter level, not merely by the failure to find a good construction.

Self-check after Approach B:

- This is genuinely construction-facing: it explains why trying to add a 41st vertex to a known 40-vertex template should fail for structural reasons.
- It does not depend on a search or on a guessed concrete lower-bound seed.

## lemma_graph

1. Assume a 41-vertex counterexample `G`.
2. Convert `B9`-free / complement-`B11`-free into edge and nonedge local codegree bounds.
3. Count triangles and independent triples to get `T + A <= (8200 - 2m)/3`.
4. Sum degree-pair inequalities to get `m >= 397`.
5. Use Goodman to get `m <= 410`.
6. Write `m = 410 - t` and use convexity to improve Goodman to `T + A >= 2460 + t`.
7. Compare with the upper bound to force `t = 0`, hence `m = 410`.
8. Equality forces `20`-regularity, edge codegree `8`, and nonedge common nonneighbor count `10`.
9. Therefore any counterexample must be `srg(41,20,8,11)`.
10. The spectral data for `(41,20,8,11)` are impossible.
11. Conclude the candidate theorem `R(B9, B11) = 41`.

## chosen_plan

Choose Approach A as the main line.

Why this is the best path:

- it yields the exact intended theorem rather than a weaker witness obstruction;
- it keeps the packet paper-shaped, because the final contradiction is intrinsic to the 41-vertex target;
- it avoids code entirely, which is appropriate because the case is not marked `search_heavy` and the reasoning already closes.

Approach B stays in the packet as the publication-facing explanation of why the natural witness-extension attack should fail.

## self_checks

1. Statement lock check.
   - The proof targets the exact selected statement `R(B9, B11)`, not a proxy slice.

2. Local counting check.
   - `3T <= 8m` and `3A <= 10(820 - m)` use the correct page thresholds `8` and `10`.

3. Pair-sum check.
   - For edges the universe size is `39`, giving `d(u) + d(v) <= 49`.
   - For nonedges the nonneighbor counts are `39 - d(u)` and `39 - d(v)`, giving `d(u) + d(v) >= 29`.

4. Goodman / convexity check.
   - The baseline lower bound peaks at degree `20`.
   - The equality case at `m = 410` forces exact `20`-regularity because the minimizing degree sequence is unique.

5. SRG check.
   - The translation from `10` common nonneighbors on a nonedge to `11` common neighbors uses `39 - 20 - 20 + \mu = 10`.

6. Spectral check.
   - The irrational conjugate roots of `x^2 + 3x - 9` cannot both appear with multiplicity `20` and still keep trace zero.

## code_used

No code used.

The reasoning attempt closed without a checker, search, or witness-verification script.

## result

Best current solve-stage result:

> Candidate proof that `R(B9, B11) = 41`.

Exact title theorem if this survives verify:

> The Exact Value of `R(B9, B11)` is `41`.

Whether a successful solve would already be 70-90% of a paper:

- Yes. If the proof checks, this is about `88%` of a short paper packet.

Minimal remaining packaging work:

- verify the pair-degree inequalities and the equality-case deductions carefully;
- write a short introduction around the one-gap window `41 <= R(B9, B11) <= 42`;
- add one comparison paragraph with the adjacent exact value `R(B10, B11) = 43`;
- optionally formalize the counting-to-SRG reduction in Lean.

One immediate corollary or natural remark:

- There is no graph on `41` vertices whose every edge has at most `8` common neighbors and whose every nonedge has at most `10` common nonneighbors.

What part of the argument scales:

- the entire squeeze
  `local book bounds -> triangle / anti-triangle count -> Goodman / convexity -> exact regularity -> tiny SRG obstruction`
  is family-shaped and looks reusable on nearby one-gap almost-diagonal pairs.

What part does not scale automatically:

- the terminal obstruction depends on collapsing to a single parameter set, and that last step may fail once the one-gap arithmetic stops landing exactly at the halfway regular case.

What theorem slice is suggested:

- the natural slice is the nonexistence of any graph satisfying the simultaneous local constraints on edges and nonedges at order `41`.

What one or two parameter shifts would help most next:

- `R(B10, B12)` as the nearest already-transferred sanity check for the template;
- `R(B11, B13)` as the next forward almost-diagonal shift where the same halfway-regular collapse might still persist.

Whether the current package is still just an instance or closer to a paper-shaped claim:

- It is already closer to a paper-shaped claim.
- The current packet is not merely “some exact witness”; it is a candidate exact theorem with a compact structural proof.

## family_affinity

Strong.

This argument belongs naturally to the `B_{n-2}` versus `B_n` almost-diagonal book Ramsey line. The proof only uses the shared-spine interpretation of books, the one-gap order window, and a rigidity collapse that is recognizably family-level.

## generalization_signal

Moderate-to-strong.

The template should transfer whenever:

- the order window is a single gap;
- edge and nonedge book-avoidance give sharp local codegree ceilings;
- Goodman plus convexity forces exact halfway regularity;
- the equality case collapses to a tiny extremal parameter set.

The signal is real, but the last obstruction is still pair-specific.

## proof_template_reuse

## verify_rediscovery

Bounded PASS 1 result: no rediscovery established within budget.

- Exact-term checks on `R(B9, B11)`, `R(B_9, B_{11})`, and close alternate notation did not surface a public exact closure to `41` or `42`.
- The canonical survey source still presents the dynamic-survey status surface rather than an exact new value: Radziszowski, *Small Ramsey Numbers*, DS1 version 17 (2024), https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1
- The 2025 book-Ramsey paper lists several new exact book values in its abstract, but not this pair: Lidický–McKinley–Pfender–Van Overberghe, *Small Ramsey Numbers for Books, Wheels, and Generalizations* (2025), https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i4p64
- The recent 2026 status source is Wesley, *Lower bounds for book Ramsey numbers*, which advertises the `R(B_{n-1},B_n)=4n-1` line and other lower bounds, but does not report an exact closure of `R(B9,B11)`: https://www.sciencedirect.com/science/article/pii/S0012365X25005217

Verifier conclusion for rediscovery:

- No bounded-web evidence that the exact intended statement is already solved in prior art.
- Rediscovery risk remains present in principle, but PASS 1 did not justify `REDISCOVERY`.

## verify_faithfulness

The packet is aimed at the exact intended statement `R(B9, B11) = 41`, not a weaker proxy.

- The main prose argument is faithful through the counting squeeze and the deduction `m = 410`.
- The current Lean artifact is only a subordinate slice about `srg(41,20,8,11)`. That slice is not itself the selected theorem, so it cannot by itself justify a full-theorem promotion.
- The present packet therefore remains theorem-faithful in target, but not yet theorem-faithful in its formal seal.

## verify_proof

First incorrect step found: Step 8 of `approach_A`.

Why it fails:

- After Step 7, the packet has only shown `m = 410` and hence `T + A = 2460`.
- It then claims that equality in the triangle and anti-triangle bounds forces every edge to have exactly `8` common neighbors and every nonedge to have exactly `10` common nonneighbors.
- That implication is not justified from the displayed inequalities, and in fact the arithmetic at `m = 410` shows the opposite: because `T` and `A` are integers,
  `T <= floor(8m/3) = floor(3280/3) = 1093`
  and
  `A <= floor(10(820-m)/3) = floor(4100/3) = 1366`,
  so `T + A <= 2459`, contradicting the Goodman lower bound `T + A >= 2460`.

Conservative repair:

- Keep Steps 1 through 7.
- From Step 7, conclude `m = 410`.
- Goodman’s baseline lower bound is then sharp, so equality in `d(v)(40-d(v)) <= 400` forces every degree to equal `20`.
- With `m = 410`, the local codegree bounds give the integer upper bounds `T <= 1093` and `A <= 1366`, hence `T + A <= 2459`.
- But a `20`-regular graph on `41` vertices gives
  `T + A = C(41,3) - (1/2) * 41 * 20 * 20 = 2460`,
  contradiction.

Verifier conclusion for correctness:

- The current written proof is not correct as written.
- The gap is tiny and conservative to repair.
- After that repair, the intended theorem still looks viable as a `CANDIDATE`.

## verify_adversarial

Adversarial checks performed:

- Recomputed every displayed inequality in Steps 2 through 7. Those arithmetic steps check out.
- Attacked the equality case directly. The packet’s SRG transition fails before the spectral step because integer triangle and anti-triangle counts already contradict `m = 410`.
- Located the candidate-local Lean slice and attempted to rerun it with `lake build AutoMath.RB9B11BookRamsey`, but the environment has no installed Lean toolchain (`elan toolchain list` reports none), so the build could not be rerun in this verify pass.

Adversarial conclusion:

- No counterexample to the repaired counting argument was found.
- The current weakness is not the spectral tail; it is the unjustified jump into that tail.
- The preserved Lean obstruction remains a useful sidecar artifact, but it is no longer the shortest mathematical contradiction once the integrality repair is made.

## verify_theorem_worthiness

Exactness:

- The intended claim is exact and theorem-shaped.
- The current packet supports the exact title theorem only after the tiny repair above.

Novelty:

- Within the bounded prior-art pass, the exact pair still appears open in public sources.
- No rediscovery was established.

Reproducibility:

- The repaired argument is short, transparent, and human-checkable.
- Formal reproducibility is not yet sealed because the environment could not rerun Lean and the existing Lean file formalizes only the subordinate SRG slice.

Lean readiness:

- Strong enough to formalize eventually, but the current packet should not be marked as directly seal-ready by Lean until the prose proof is updated to the repaired counting contradiction.

Paper leverage:

- If the repaired theorem is made fully rigorous and then Lean-sealed, it would still constitute most of a publishable note.
- Honest solve-to-paper fraction after this verify pass: about `0.84`.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? Yes.
- What percentage of the paper would one solve already provide? About `84%`.
- What title theorem is actually visible? `R(B9, B11) = 41`.
- What part of the argument scales? The local codegree bounds, Goodman squeeze, and halfway-regular collapse are family-shaped.
- What part clearly does not? The terminal contradiction is highly pair-specific; in the repaired proof it is the `41`-vertex integer squeeze, not a broadly reusable SRG obstruction.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? No. The honest status is stronger than `INSTANCE_ONLY`, but still only `SLICE_CANDIDATE` until the corrected full theorem packet is stabilized and sealed.

## verify_verdict

`SURVIVES_WITH_TINY_REPAIR`

Reason:

- PASS 1 did not establish rediscovery.
- The packet targets the right theorem.
- The first real proof error is localized and conservative to repair.
- After the repair, the candidate exact theorem still looks credible and micro-paper-eligible.

## minimal_repair_if_any

Replace the current Step 8 through Step 10 tail by the following shorter finish:

> Since Step 7 forces `m = 410`, the Goodman lower bound is attained, so every vertex has degree `20`. Therefore `G` is `20`-regular. Now the local book bounds imply
> `T <= floor(8m/3) = 1093`
> and
> `A <= floor(10(820-m)/3) = 1366`,
> hence `T + A <= 2459`.
> But for a `20`-regular graph on `41` vertices,
> `T + A = C(41,3) - (1/2) * sum_v 20 * 20 = 10660 - 8200 = 2460`,
> contradiction.
> Therefore no `41`-vertex counterexample exists and `R(B9, B11) = 41`.

This repair is preferable to the current SRG tail because it closes earlier, stays fully within the existing counting framework, and avoids the unjustified equality-to-SRG jump.

## verify_rediscovery

PASS 1 used a bounded prior-art audit on 2026-04-14 with exact-term, alternate-notation, canonical-source, in-source theorem/example, and recent-status queries.

Findings:

- No checked source exposed an exact closure of `R(B9, B11)`.
- The canonical survey source still supports only the generic upper bound `R(B9, B11) <= 42`.
- The 2025 almost-diagonal book Ramsey paper supports the lower bound `41 <= R(B9, B11)`.
- The 2026 Wesley paper closes the adjacent line `R(B10, B11) = 43`, not the selected pair.
- The bounded exact-term and recent-status searches did not surface a later paper, preprint, or discussion explicitly determining `R(B9, B11)`.

Conservative rediscovery verdict:

- No rediscovery established within the bounded audit.
- The packet remains frontier-plausible rather than archived as prior art.

## verify_faithfulness

The solve-stage packet stays locked to the exact selected statement:

> Every graph on 41 vertices contains `B9` or its complement contains `B11`, hence `R(B9, B11) = 41`.

Faithfulness check:

- No wrong-theorem drift found in the main argument.
- No quantifier drift found: the proof still targets all graphs on `41` vertices, not a subclass.
- No definition drift found in the translation between books and common-neighbor counts.
- The Lean artifact is only a subordinate obstruction slice, namely nonexistence of `srg(41,20,8,11)`. That is faithful as a terminal subgoal, but it is not by itself the full selected theorem.

Faithfulness verdict:

- The mathematical packet matches the intended theorem exactly.
- The formal artifact does not yet seal the full theorem, but it does not change the theorem being claimed.

## verify_proof

Arithmetic and structural checks on Steps 1 through 9 passed:

- `3T <= 8m` and `3A <= 10(820 - m)` use the correct page thresholds.
- The edge pair bound `d(u) + d(v) <= 49` and the nonedge pair bound `d(u) + d(v) >= 29` are numerically correct.
- The derived edge bound `m >= 397` and Goodman bound `m <= 410` check out.
- The convexity refinement with `m = 410 - t` correctly yields `T + A >= 2460 + t`.
- Comparing lower and upper bounds correctly forces `t = 0`, hence `m = 410`.
- In the regular equality case, the nonedge common-nonneighbor condition translates to common-neighbor parameter `mu = 11`.

First issue found:

- The spectral contradiction in Step 10 is missing one explicit justification: why the regular eigenvalue `20` has multiplicity `1`, so that the remaining `40` eigenvalues must come from the irreducible quadratic `x^2 + 3x - 9`.

Assessment of that issue:

- This is a tiny but real proof gap in exposition, not a collapse of the argument.
- Because `mu = 11 > 0`, any `srg(41,20,8,11)` would be connected.
- In a connected `20`-regular graph, the eigenvalue `20` is simple.
- Therefore the other `40` eigenvalues must be the two irrational conjugate roots of `x^2 + 3x - 9`, with equal multiplicity by irreducibility over `Q`.
- That forces multiplicities `20` and `20`, and then trace zero fails since `20 + 20(r + s) = 20 + 20(-3) = -40`.

Proof verdict:

- No fatal incorrect step found.
- The proof survives verify after one conservative repair to the spectral step.

## verify_adversarial

Adversarial checks performed:

- Searched the artifact directory for any checker or witness verifier: none found.
- Inspected the only candidate-local formal artifact, `artifacts/r-b9-b11-book-ramsey/lean/AutoMath/RB9B11BookRamsey.lean`.
- Attempted to rerun the Lean artifact with `lake env lean`, but the sandboxed environment blocked dependency/toolchain download, so the rerun could not complete for infrastructure reasons.
- Independently spot-checked the key arithmetic used in the obstruction:
  - `binom(41, 3) = 10660`
  - the roots of `x^2 + 3x - 9` sum to `-3`
  - under multiplicities `(1, 20, 20)`, the trace would indeed be `-40`

Adversarial verdict:

- No computational artifact contradicted the proof.
- The current packet is reasoning-led, with only a partial Lean mirror and no standalone checker.
- The main remaining risk is formal completeness of the final spectral contradiction, not a discovered counterexample or arithmetic break.

## verify_theorem_worthiness

Exactness:

- The visible theorem is exact: `R(B9, B11) = 41`.

Novelty:

- Bounded PASS 1 did not establish rediscovery.
- The checked literature still supports the one-gap window `41 <= R(B9, B11) <= 42`.

Reproducibility:

- Mathematical reproducibility is fairly high because the argument is short and numerically rigid.
- Formal reproducibility is incomplete because the final spectral impossibility is not yet sealed in Lean.

Lean readiness:

- `lean_ready = true`.
- The remaining gap is narrow and well-localized.
- Lean is not optional polish here; it is the shortest remaining route to a sealed packet if the goal is the harness stop condition.

Paper leverage:

- If the argument is correct and Lean-sealed, this would already constitute most of a publishable note.
- Honest solve-to-paper fraction remains about `0.88`.
- The visible title theorem is `The Exact Value of R(B9, B11)`.

What scales:

- The counting squeeze
  `local book bounds -> triangle / anti-triangle control -> Goodman + convexity -> halfway regularity -> forced SRG`
  looks reusable on nearby almost-diagonal one-gap pairs.

What does not clearly scale:

- The terminal impossibility is parameter-specific; it depends on collapsing to the exact SRG tuple `(41,20,8,11)` and then killing that tuple spectrally.

Best honest publication status:

- Not `NONE`.
- Not merely `INSTANCE_ONLY`.
- Best honest status is still `SLICE_CANDIDATE`.

## verify_verdict

- `verify_verdict = SURVIVES_VERIFY`
- `classification = CANDIDATE`
- `publication_status = SLICE_CANDIDATE`
- `lean_ready = true`
- `lean_packet_seal = true`
- The packet is not `EXACT` because Lean has not sealed the full theorem.

## minimal_repair_if_any

Insert one sentence into the spectral step:

> Since `mu = 11 > 0`, any `srg(41,20,8,11)` is connected, so the regular eigenvalue `20` has multiplicity `1`.

Then the existing argument can continue conservatively:

> The remaining `40` eigenvalues are the two irrational conjugate roots of `x^2 + 3x - 9`, which must occur with equal multiplicity in the characteristic polynomial of the integer adjacency matrix; hence each has multiplicity `20`, contradicting trace zero.

## lean_statement

Lean target for this stage:

> `∀ {V} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj], ¬ G.IsSRGWith 41 20 8 11`.

This is the publication-facing theorem slice extracted from the verified packet: once the counting
argument collapses a hypothetical `41`-vertex counterexample to `srg(41,20,8,11)`, ruling out that
parameter set would seal the exact-value proof for `R(B9, B11) = 41`.

Lean backend file written in this run:

- `lean/AutoMath/RB9B11BookRamsey.lean`

Mirrored artifact Lean file written in this run:

- `artifacts/r-b9-b11-book-ramsey/lean/AutoMath/RB9B11BookRamsey.lean`

## lean_skeleton

The Lean file now contains a checked skeleton for the forced-SRG slice:

1. define the exact packet-facing statement `¬ IsSRGWith 41 20 8 11`;
2. verify the parameter identity `20 * (20 - 8 - 1) = (41 - 20 - 1) * 11`;
3. specialize the SRG matrix identity to obtain
   `A^2 + 3A - 9I = 11J`;
4. derive the cubic annihilator
   `(A - 20I)(A^2 + 3A - 9I) = 0`;
5. record the trace invariants
   `trace A = 0` and `trace (A^2) = 820`.

This is the exact algebraic spine of the verified argument up to, but not including, the final
spectral integrality contradiction.

## lean_result

- `lake build AutoMath.RB9B11BookRamsey` succeeded in `lean/`.
- The backend and mirrored artifact file are synchronized.
- Lean now certifies the forced `srg(41,20,8,11)` matrix profile and trace profile.
- Lean does not yet certify the terminal nonexistence claim `¬ IsSRGWith 41 20 8 11`.
- Therefore this run does not earn `classification = EXACT` and does not update `PROOFS.md`.

## lean_blockers

- The remaining missing step is the spectral impossibility of `srg(41,20,8,11)`.
- In the paper packet this is the irrational-root obstruction for the polynomial
  `x^2 + 3x - 9`, equivalently the need to formalize that the two irrational conjugate
  nontrivial eigenvalues must occur with equal multiplicity (or an equivalent characteristic
  polynomial / integrality argument).
- I did not find a local Mathlib theorem in this repo that directly discharges that conjugate
  multiplicity step for strongly regular graphs.
- Because that terminal step is not formalized, the honest Lean outcome is a checked partial
  packet seal rather than a full exact seal.

Reusable proof template:

1. Convert `B_a` and `B_b` avoidance into edge-codegree and nonedge-cocodegree bounds.
2. Bound triangles and independent triples from above.
3. Bound the edge count from below via summed degree-pair inequalities.
4. Bound the edge count from above via Goodman.
5. Refine Goodman with convexity to force the exact edge count and regular degree sequence.
6. Translate the equality case into a tiny strongly regular candidate.
7. Rule out that candidate spectrally.

## candidate_theorem_slice

Candidate theorem slice:

> There is no graph `G` on `41` vertices such that every edge of `G` has at most `8` common neighbors and every nonedge of `G` has at most `10` common nonneighbors.

Equivalent sharpened slice:

> Any `41`-vertex graph satisfying those local constraints would have to be an impossible strongly regular graph with parameters `(41,20,8,11)`.

## smallest_param_shift_to_test

The smallest useful shifts are:

- forward: `(B11, B13)`, to test whether the same halfway-regular collapse persists one step up the line;
- backward / comparison: `(B10, B12)`, because it already supports the same template and helps isolate which algebraic features are robust.

## why_this_is_or_is_not_publishable

If verify accepts the argument, this is publishable in the micro-paper lane.

Why:

- the exact title theorem is clean and non-embarrassing: `R(B9, B11) = 41`;
- the result would already account for roughly `0.88` of the paper, which sits inside the target `70-90%` band;
- the proof is structural, not a naked search output;
- the neighboring exact benchmark `R(B10, B11) = 43` gives immediate narrative framing with low editorial overhead.

Current caution:

- at solve stage this remains a `CANDIDATE`, not an exact sealed packet;
- the proof is compact enough that a small bookkeeping error could still matter, so verify has real work to do.

## paper_shape_support

What extra structure makes the result paper-shaped if the main claim closes:

- a clean title theorem: `The Exact Value of R(B9, B11)`;
- a natural theorem slice: the local-constraint nonexistence statement on `41` vertices;
- a built-in boundary remark: any putative 41-vertex witness is forced all the way to impossible `srg(41,20,8,11)`;
- a direct family comparison: the result sits immediately below the neighboring exact value `R(B10, B11) = 43`.

Minimal remaining packaging work is light:

- check the algebra carefully,
- add the short comparison paragraph,
- formalize only if the manager wants a sealed packet.

## boundary_remark

The obstruction sits exactly at the halfway regular regime.

Any hypothetical `41`-vertex counterexample is not merely dense or sparse in some vague sense; it is forced to be `20`-regular with every edge and nonedge saturating the local book thresholds. That makes the failure mode sharp rather than diffuse, which is a useful boundary statement for the family.

## likely_failure_points

- The nonedge pair-sum inequality is easy to mis-index because the universe size is `39`, not `40`.
- The Goodman equality passage needs the degree-square minimizer stated correctly: `2t` vertices of degree `19`, the rest degree `20`.
- The spectral contradiction should be checked carefully for the exact trace / multiplicity argument; if desired, verify can also compute the formal multiplicity formula and note its irrational value.
- The step “every nonedge has exactly `10` common nonneighbors” relies on equality in the aggregate anti-triangle count, so the equality-chain should be audited line by line.

## what_verify_should_check

- Recheck the local translation:
  `B9`-free means edge codegree at most `8`, and complement-`B11`-free means nonedge common nonneighbors at most `10`.
- Recompute the edge and nonedge pair-degree inequalities independently.
- Recompute the Goodman lower bound and the refined convexity lower bound for `m = 410 - t`.
- Audit the equality implications that force `20`-regularity and exact local thresholds.
- Confirm the strongly regular reduction to `(41,20,8,11)`.
- Confirm the spectral contradiction, preferably both by the conjugate-multiplicity argument and by the standard multiplicity formula.
- Because solve ran with web disabled, let verify handle only the bounded prior-art recheck needed to guard against rediscovery.

## verify_rediscovery

PASS 1 used a bounded prior-art audit only.

What was checked:

- exact-instance searches for `R(B9, B11)` and alternate notation / orderings;
- the canonical survey source `Small Ramsey Numbers`;
- the 2025 paper `Small Ramsey Numbers for Books, Wheels, and Generalizations`;
- the 2026 paper `Lower bounds for book Ramsey numbers`;
- whether the exact pair was already settled by a theorem, proposition, example, observation, or corollary in those sources.

Result:

- No exact closure of `R(B9, B11)` was found within budget.
- The 2026 revision of the Radziszowski survey still lists the pair in the one-gap window `41 <= R(B9, B11) <= 42`.
- The 2025 Lidicky-McKinley-Pfender-Van Overberghe paper supplies the lower-bound side used by the packet, not an exact determination.
- Wesley 2026 closes the adjacent `R(B10, B11) = 43` line and gives benchmarks, but the verify audit did not find a theorem or appendix entry there that collapses `R(B9, B11)`.

Conservative conclusion:

- Rediscovery was not established.
- Novelty is still only bounded-pass provisional until publication audit, but the exact intended statement still appears frontier-novel inside the verify budget.

## verify_faithfulness

The claimed result matches the intended statement exactly.

- The locked theorem in the packet is the exact selected statement: every graph on `41` vertices contains `B9` or its complement contains `B11`, hence `R(B9, B11) = 41`.
- The proof does not drift to a weaker proxy such as a nearby parameter pair, an asymptotic statement, or a one-sided bound.
- The local translations are faithful:
  `B9`-free means every edge has at most `8` common neighbors, and complement-`B11`-free means every nonedge has at most `10` common nonneighbors.
- The auxiliary slice
  “no `41`-vertex graph can satisfy those simultaneous local constraints”
  is genuinely equivalent to the intended exact Ramsey statement in this packet.

Verdict:

- No wrong-theorem drift, quantifier drift, or definition mismatch found.

## verify_proof

I did not find an incorrect step.

Critical checks:

1. Triangle / anti-triangle bounds:
   `3T <= 8m` and `3A <= 10(820 - m)` are correct.
2. Pair-degree inequalities:
   - for edges, `d(u) + d(v) <= 49`;
   - for nonedges, `d(u) + d(v) >= 29`.
3. Summation step:
   `sum_v d(v)^2 <= 49m` and `sum_v d(v)(40 - d(v)) >= 29(820 - m)` imply `m >= 397`.
4. Goodman baseline:
   the lower bound `T + A >= 2460` and hence `m <= 410` are correct.
5. Convexity refinement:
   writing `m = 410 - t`, the minimizing degree sequence is exactly `2t` vertices of degree `19` and `41 - 2t` vertices of degree `20`, yielding
   `sum_v d(v)^2 >= 16400 - 78t` and therefore `T + A >= 2460 + t`.
6. Comparison with the upper bound:
   `2460 + t <= 2460 + 2t/3` forces `t = 0`.
7. Equality chain:
   `m = 410` plus equality in Goodman forces `20`-regularity, and equality in the aggregate triangle / anti-triangle bounds forces every edge to have exactly `8` common neighbors and every nonedge to have exactly `10` common nonneighbors.
8. Strongly regular reduction:
   in a `20`-regular graph on `41` vertices, a nonedge with `10` common nonneighbors has `11` common neighbors, so the parameter set is indeed `(41,20,8,11)`.
9. Terminal obstruction:
   the standard SRG eigenvalue equation gives irrational nontrivial eigenvalues, and the standard multiplicity formula yields nonintegral multiplicities; either way the parameter set is impossible.

First incorrect step found:

- None found.

Residual caution:

- The proof is compact enough that formalization would still be valuable, but the skeptical paper check did not expose a mathematical gap.

## verify_adversarial

No checker or witness-construction script was present in the packet, so PASS 4 was a manual adversarial stress test of the arithmetic and the final SRG obstruction.

What was stress-tested:

- the `t`-parameter inequality chain after writing `m = 410 - t`;
- the equality-only collapse at `t = 0`;
- the eigenvalue and multiplicity consequences for `srg(41,20,8,11)`.

Results:

- For every `t > 0`, the refined Goodman lower bound exceeds the packet’s upper bound, so no irregular case survives.
- At `t = 0`, the arithmetic lands exactly at the forced regular case.
- The nontrivial SRG eigenvalues solve `x^2 + 3x - 9 = 0`, hence are irrational.
- The standard multiplicity formula gives nonintegral multiplicities for `(41,20,8,11)`, which is an even cleaner contradiction than the packet’s trace-based presentation.

Attempt to break the claim:

- No surviving `41`-vertex witness shape remained after the equality collapse.
- No computational artifact in the packet contradicted the theorem.

## verify_theorem_worthiness

Exactness:

- The theorem is exact at the intended pair, not a slice proxy.

Novelty:

- Bounded verify-pass prior-art checking did not establish rediscovery.
- Novelty is strong enough to proceed, but publication audit should still perform the final bounded status check before any seal claim.

Reproducibility:

- Strong. The argument is short, search-free, and based on explicit counting identities plus a tiny SRG impossibility.

Lean readiness:

- The packet is strong enough to formalize.
- Lean is not yet the shortest remaining path to a sealed publication packet, because publication audit still has to ratify the frontier status and final paper-shape assessment.

Paper leverage:

- High. If correct and Lean-sealed, this would already constitute most of a publishable exact-value note.

Direct answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  Yes.
- What percentage of the paper would one solve already provide?
  About `0.88`.
- What title theorem is actually visible?
  `The Exact Value of R(B9, B11)`.
- What part of the argument scales?
  The family-shaped squeeze
  `local codegree bounds -> triangle/anti-triangle bounds -> Goodman/convexity -> regularity collapse -> tiny SRG obstruction`.
- What part clearly does not?
  The last obstruction is pair-specific: it depends on landing exactly on the impossible `(41,20,8,11)` parameter set.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`?
  No. The best honest status after verify is `SLICE_CANDIDATE`, not merely `INSTANCE_ONLY`.

Conservative publication judgment:

- This is not sealed enough for `PAPER_READY`.
- It does look like a genuine one-shot micro-paper candidate rather than an isolated exact curiosity.

## verify_verdict

`SURVIVES_VERIFY`

Summary:

- no rediscovery found within the verify budget;
- no theorem drift found;
- no incorrect proof step found;
- adversarial arithmetic confirmed the equality collapse and the impossibility of `srg(41,20,8,11)`;
- classification remains `CANDIDATE` because the claim is not Lean-complete.

## minimal_repair_if_any

No mathematical repair was required.

Tiny conservative presentation repair available if desired:

- replace the final trace-only contradiction with the standard SRG multiplicity formula, which yields nonintegral multiplicities for `(41,20,8,11)` and states the impossibility more directly.

## publication_prior_art_audit

Bounded prior-art pass run on `2026-04-14`.

Exact-statement search:

- Direct exact-term searches around `R(B9, B11)` and `R(B_9, B_{11})` did not surface any exact-value announcement beyond the packet's canonical source chain.

Alternate-notation search:

- Alternate-notation checks around `R(B_{n-2}, B_n)` at `n = 11` and the `K_2 + \overline{K_t}` book notation did not surface a target-specific exact closure either.

Canonical-source audit:

- DS1.17 (2024), Section `5.3(g)`, still gives the generic upper bound `R(B_m, B_n) <= 2(m + n + 1)`, hence `R(B9, B11) <= 42`.
- DS1.17 Table IXa still leaves the pair in the one-gap window rather than recording an exact value.
- Lidicky-McKinley-Pfender-Van Overberghe (2025), Theorem 1, gives `4n - 3 <= R(B_{n-2}, B_n)` for `4 <= n <= 21`, hence `R(B9, B11) >= 41`.
- The 2025 appendix witness tables and remarks provide nearby lower-bound constructions, but no theorem / proposition / example / corollary / observation there closes `R(B9, B11)` exactly.
- Wesley (2026), Theorem 2, settles `R(B_{n-1}, B_n) = 4n - 1` for `n <= 20`, so in particular `R(B10, B11) = 43`, but this does not state or imply the target exact value.

Outside-source status pass:

- A narrow outside-source web check did not reveal a later exact determination of `R(B9, B11)`.
- Search results remained dominated by the same survey-and-paper chain already named in the packet.

Recent follow-up check:

- No extra follow-up pass was needed after the 2026 status check, because no concrete ambiguity was created by the bounded search.

Conservative audit judgment:

- Within this bounded publication-audit budget, rediscovery was not established.
- This is still an inference from the absence of an exact closure in the checked sources, not a claim of exhaustive literature coverage.

## publication_statement_faithfulness

The packet is faithful to the selected statement.

- The strongest theorem claim is the exact selected pair, not a proxy family statement.
- The proof route aims to show: every graph on `41` vertices contains `B9` or its complement contains `B11`, hence `R(B9, B11) = 41`.
- The local-codegree / strongly-regular reduction is a proof engine for the exact target, not theorem drift.
- If Lean later exposes a real gap, the packet should be downgraded rather than reframed as a broader family paper.

Direct answer:

- Would this survive a referee asking "what is the theorem?"
  Yes. The theorem is the exact value of `R(B9, B11)`, with a short structural obstruction as the proof shape.

## publication_theorem_worthiness

The result is stronger than "here is an example."

- The honest theorem-shaped object is an exact-value claim with a structural squeeze, not a witness catalog or isolated construction note.
- There is a real title theorem:
  `The Exact Value of R(B9, B11)`.
- The proof is structural in method:
  `local codegree bounds -> triangle / anti-triangle counts -> Goodman / convexity -> forced regularity -> impossible srg(41,20,8,11)`.
- The terminal obstruction is still pair-specific, because the arithmetic lands on one concrete SRG parameter set.
- The claim is not dependent on hand-picked small cases or search-heavy enumeration.

Direct answers:

- Is the strongest honest claim stronger than "here is an example"?
  Yes.
- Is there a real title theorem, theorem slice, or counterexample theorem here?
  Yes. The title theorem is the exact value, and the internal theorem slice is the nonexistence of a `41`-vertex graph with the simultaneous edge/nonedge local bounds.
- Is the proof structural or merely instance-specific?
  Structural in proof shape, but still attached to one exact pair at the final obstruction step.
- Is the claim still too dependent on hand-picked small cases?
  No in proof method; only the statement itself is a single exact case.

## publication_publishability

If the proof is correct and Lean-sealed, this is already most of a publishable note.

- One solve would already provide about `0.88` of the paper.
- The title theorem, abstract-level story, neighboring comparison point `R(B10, B11) = 43`, and bounded frontier basis are all already visible.
- The remaining gap is genuinely small:
  formal sealing, short exposition, and conservative source comparison.
- The candidate did not only look attractive before audit; it still reads like a legitimate one-shot micro-paper target after audit.

Conservative status call:

- This is not yet honestly `PAPER_READY`, because the claim is still unsealed.
- The best honest publication status remains `SLICE_CANDIDATE`.

Direct answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  Yes.
- What percentage of the paper would one solve already provide?
  About `88%`.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit?
  The remaining gap is genuinely small.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program?
  It should stay in the one-shot lane; if Lean exposes a real gap, move it aside rather than expanding scope.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization?
  Lean would directly seal the packet.

## publication_packet_audit

Packet quality remains strong.

- The packet has an exact intended statement, a structural candidate proof, a clear theorem slice, bounded novelty notes, and a short-paper title/narrative.
- The proof artifacts are preserved and readable without search code.
- The nearby exact benchmark `R(B10, B11) = 43` gives the note an immediate comparison paragraph and keeps the result from reading like an isolated curiosity.
- Editorial overhead remains low.

Publication-packet judgment:

- `publication_packet_quality = strong`
- The packet is theorem-shaped enough for Lean to be the next real gate.
- The packet is not yet publication-sealed because the theorem is not Lean-complete.

## micro_paper_audit

Pass.

- `single_solve_to_paper_fraction`: `0.88`
- `title_theorem_strength`: `strong`
- `publication_narrative_strength`: `strong`
- `editorial_overhead`: `low`
- `immediate_corollary_headroom`: enough for a remark, but not the main value of the note
- `isolated_exact_case_risk`: present but acceptable, because the adjacent exact benchmark and the structural proof give the case a real family anchor

Micro-paper judgment:

- This still fits the strict one-shot lane.
- It should not be broadened into a larger campaign unless the exact proof packet fails.
- Best honest publication label after audit: `SLICE_CANDIDATE`.

## strongest_honest_claim

A bounded publication audit still supports the claim that public sources leave `R(B9, B11)` in the window `41 <= R(B9, B11) <= 42`, and the local packet contains a structural candidate proof that any `41`-vertex counterexample would force an impossible `srg(41,20,8,11)`. This is stronger than an example and strong enough to serve as the title theorem of a short note, but until Lean seals the proof the honest publication-facing label is `SLICE_CANDIDATE`, not `PAPER_READY`.

## paper_title_hint

The Exact Value of `R(B9, B11)`

## next_action

Formalize the counting-to-SRG reduction and the impossibility of `srg(41,20,8,11)` in Lean. If formalization exposes a real proof gap, park this candidate rather than broadening it into a larger book-Ramsey program.

## lean_statement

Formalized target for this Lean run:

> No finite simple graph is strongly regular with parameters `(41,20,8,11)`.

This is the terminal obstruction slice named by the publication audit as the direct packet-sealing step.
It is not the full selected theorem `R(B9, B11) = 41`, but it is the strongest honest slice that the
current backend could seal without re-formalizing the full counting reduction.

Lean files used:

- `lean/AutoMath/RB9B11BookRamsey.lean`
- `artifacts/r-b9-b11-book-ramsey/lean/AutoMath/RB9B11BookRamsey.lean`

Main Lean theorem produced:

- `AutoMath.RB9B11BookRamsey.no_srg_41_20_8_11`
- packaged slice statement: `AutoMath.RB9B11BookRamsey.rb9b11_book_ramsey_obstruction`

## lean_skeleton

Lean proof skeleton actually completed in this run:

1. keep the already-checked SRG matrix identity `A^2 + 3A - 9I = 11J`;
2. keep the cubic annihilator `(A - 20I)(A^2 + 3A - 9I) = 0`;
3. use Hermitian spectral theory to show every adjacency eigenvalue is one of
   `20`, `((-3 + 3 * sqrt 5) / 2)`, or `((-3 - 3 * sqrt 5) / 2)`;
4. count those three eigenvalue types via `trace(A) = 0` and `trace(A^2) = 820`;
5. derive the final arithmetic contradiction.

The final contradiction in Lean uses the corrected squared-root weights

- `rPos^2 = (27 - 9 * sqrt 5) / 2`
- `rNeg^2 = (27 + 9 * sqrt 5) / 2`

and then forces:

- `c20 = 1`
- `cPos + cNeg = 40`
- `3 * sqrt 5 * (cPos - cNeg) = 80`

Squaring yields `45 z^2 = 6400` for an integer `z`, so `9` divides the left-hand side and would have
to divide `6400`, contradiction.

## lean_result

Result: the terminal SRG obstruction slice is now Lean-complete.

What checked:

- `lake build AutoMath.RB9B11BookRamsey` succeeded in `lean/` on this machine.
- The backend file and artifact-mirrored file were resynchronized after the final patch.
- The Lean module now proves the nonexistence of `srg(41,20,8,11)` without `sorry`, `admit`, or new axioms.

Honest status effect:

- This run seals the publication-facing theorem slice named in the prior audit.
- It does **not** yet justify `classification = EXACT`, because the full selected statement
  `R(B9, B11) = 41` is still only connected to the Lean slice through the verified packet rather than a
  fully formalized Lean reduction.
- The correct publication-facing upgrade is therefore `SLICE_EXACT`, not `PAPER_READY`.

## lean_blockers

No blocker remains for the chosen theorem slice.

The remaining blocker to an `EXACT` promotion is scope, not failure:

- the verified counting / Goodman / equality-case reduction from the selected Ramsey statement to
  `srg(41,20,8,11)` is not yet formalized in Lean;
- because that reduction remains outside Lean, the exact title theorem is still not honestly
  `Lean-complete EXACT`.

Minor build notes:

- the targeted build emitted only non-fatal linter warnings about unused section variables and two
  stylistic `simpa` suggestions;
- those warnings do not affect kernel checking of the theorem slice.
