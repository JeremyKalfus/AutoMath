# statement_lock

Let `B_t` denote the book graph with `t` pages, i.e. `t` triangles sharing one common edge. For a graph `G`, an edge `uv` is the base of a `B_t` exactly when `u` and `v` have at least `t` common neighbors.

The exact intended statement for this solve run is:

> Every graph `G` on `49` vertices contains `B11` or its complement contains `B13`. Equivalently, `R(B11, B13) = 49`.

The title theorem, if the argument below survives verification, is:

> The Exact Value of `R(B11, B13)` is `49`.

# definitions

- Write `n = 49`.
- Let `e = |E(G)|`, `d(v)` the degree of `v`, and `S = \sum_v d(v)^2`.
- Let `T` be the number of triangles in `G`, and `\bar T` the number of triangles in `\overline G`.
- For an edge `uv` of `G`, let `c(uv) = |N(u) \cap N(v)|`. Avoiding `B11` means `c(uv) <= 10` for every edge.
- For a nonedge `uv` of `G`, avoiding `B13` in the complement means `uv` has at most `12` common neighbors in `\overline G`, equivalently `u` and `v` have at most `12` common nonneighbors in `G`.
- Goodman identity on `49` vertices:
  `T + \bar T = \binom{49}{3} - \frac12 \sum_v d(v)(48 - d(v)) = 18424 - 48e + S/2`.

Ambiguities/conventions fixed here:

- `B11` and `B13` use the standard book-graph convention: shared base edge, not shared spine vertex.
- Since solve is web-disabled, the only claim made here is an internal theorem candidate. Novelty and rediscovery remain for verify.
- I treat the public lower bound `R(B11, B13) >= 49` and upper bound `R(B11, B13) <= 50` from the packet as given input.

# approach_A

Structural / invariant route:

- Assume for contradiction that there is a `49`-vertex witness `G` with no `B11` and with `\overline G` containing no `B13`.
- Then every edge of `G` lies in at most `10` triangles, so `3T = \sum_{uv in E(G)} c(uv) <= 10e`, hence `T <= 10e/3`.
- Every edge of `\overline G` lies in at most `12` triangles of `\overline G`, so `3\bar T <= 12(1176 - e)`, hence `\bar T <= 4(1176 - e)`.
- Insert both bounds into Goodman:
  `18424 - 48e + S/2 <= 10e/3 + 4(1176 - e)`,
  so
  `S <= (284/3)e - 27440`.
- Cauchy gives `S >= (2e)^2 / 49`. This already squeezes `e` into `572 <= e <= 588`.
- Write `e = 588 - t`. Then `\sum_v d(v) = 1176 - 2t`.
- For fixed integer sum `1176 - 2t`, convexity minimizes `S` by taking `2t` vertices of degree `23` and the other `49 - 2t` vertices of degree `24`, so
  `S >= (49 - 2t)24^2 + (2t)23^2 = 28224 - 94t`.
- The Goodman upper bound becomes
  `S <= 28224 - (284/3)t`.
- For any `t > 0`, one has `28224 - 94t > 28224 - (284/3)t`, impossible. Therefore `t = 0`, so `e = 588`.
- Equality now holds everywhere: `G` is `24`-regular, `T = 10e/3`, and `\bar T = 4(1176 - e)`.
- Since every edge contribution is at most `10`, the equality `3T = 10e` forces every edge of `G` to have exactly `10` common neighbors.
- Since every edge of `\overline G` contributes at most `12`, the equality `3\bar T = 12|E(\overline G)|` forces every edge of `\overline G` to have exactly `12` common neighbors in `\overline G`.
- Thus `G` would have to be strongly regular with parameters `(49, 24, 10, 13)`: adjacent pairs have `10` common neighbors, and because `G` is `24`-regular, a nonedge with `12` common nonneighbors has exactly `13` common neighbors in `G`.
- But `(49, 24, 10, 13)` is infeasible. The restricted eigenvalues would solve
  `x^2 + (13 - 10)x + (13 - 24) = x^2 + 3x - 11 = 0`,
  hence `x = (-3 +- sqrt(53))/2`.
- If their multiplicities are `m_+` and `m_-`, then `m_+ + m_- = 48` and `24 + m_+ r + m_- s = 0`. Solving gives a multiplicity involving `48 / sqrt(53)`, hence not an integer. So no such graph exists.
- Therefore the assumed `49`-vertex witness cannot exist, and `R(B11, B13) = 49`.

Self-check after Approach A:

- The proof uses only local triangle caps, Goodman, convexity of square-sum, and a final strongly-regular feasibility obstruction.
- The only delicate algebra is the passage from `S <= (284/3)e - 27440` to the `t = 0` conclusion.

# approach_B

Construction / extremal contradiction route:

- Start from a hypothetical `49`-vertex witness and inspect one vertex `v` of degree `d`.
- Let `M(v)` be the nonneighbors of `v`; then `|M(v)| = 48 - d`.
- For `w in M(v)`, the pair `vw` is a nonedge, so `v` and `w` have at most `12` common nonneighbors. Inside `G[M(v)]`, that means `w` has at least `(48 - d) - 1 - 12 = 35 - d` neighbors.
- Hence `\delta(G[M(v)]) >= 35 - d`.
- Any edge `xy` in `G[M(v)]` then has at least
  `deg_{M(v)}(x) + deg_{M(v)}(y) - (|M(v)| - 2) >= 2(35 - d) - (46 - d) = 24 - d`
  common neighbors inside `M(v)`.
- If `d <= 13`, then some edge of `G[M(v)]` would have at least `11` common neighbors, giving a `B11` in `G`. So every vertex has degree at least `14`.
- Applying the same argument to `\overline G` gives `\delta(\overline G) >= 15`, hence `\Delta(G) <= 33`.
- So any witness already lives in a narrow degree window `14 <= d(v) <= 33`.
- Approach A strengthens this dramatically: the only remaining extremal possibility is a `24`-regular graph with exact local parameters `(lambda, mu) = (10, 13)`, which is impossible.

Self-check after Approach B:

- This route does not close the theorem by itself, but it gives a useful sanity bound and shows why the witness, if it existed, would have to be highly balanced.
- The degree-window argument is consistent with the final `24`-regular collapse from Approach A.

# lemma_graph

Lemma skeleton used by the chosen proof:

1. Witness assumption:
   Assume `G` has `49` vertices, no `B11`, and `\overline G` has no `B13`.
2. Triangle-cap lemma:
   `T <= 10e/3` and `\bar T <= 4(1176 - e)`.
3. Goodman lemma:
   `T + \bar T = 18424 - 48e + S/2`.
4. Square-sum squeeze:
   `S <= (284/3)e - 27440`, hence `572 <= e <= 588`.
5. Deficiency lemma:
   If `e = 588 - t`, then convexity gives `S >= 28224 - 94t`, contradicting the previous upper bound unless `t = 0`.
6. Equality-collapse lemma:
   `e = 588` forces `24`-regularity and exact local triangle counts on every edge in `G` and `\overline G`.
7. Parameter lemma:
   Any such graph is strongly regular with parameters `(49, 24, 10, 13)`.
8. Spectral obstruction:
   `(49, 24, 10, 13)` has nonintegral multiplicities, impossible.
9. Conclusion:
   No `49`-vertex witness exists, so `R(B11, B13) = 49`.

# chosen_plan

Choose Approach A as the main proof.

Reason:

- It closes the exact theorem directly instead of only shrinking the search space.
- It is publication-shaped: one global counting identity, one extremal regularity collapse, one final infeasible-parameter obstruction.
- It needs no brute force and no code.

What extra structure makes this paper-shaped if the main claim closes:

- A short preliminary lemma packaging the `t = 0` regularity collapse.
- A one-paragraph comparison with the neighboring exact case `R(B12, B13) = 51`.
- A brief boundary remark explaining that the whole obstruction reduces to the nonexistent strongly regular graph `(49,24,10,13)`.

# self_checks

- Statement lock check: the target is the exact threshold `49`, not merely a witness classification.
- Definition check: the proof uses the standard common-neighbor characterization of books.
- Counting check: `\binom{49}{2} = 1176` and `\binom{49}{3} = 18424`.
- Goodman check: `18424 - 48e + S/2` is the correct specialization for `n = 49`.
- Triangle-cap check: `B11` means cap `10` on edge common-neighbor counts in `G`; `B13` in the complement means cap `12` on edge common-neighbor counts in `\overline G`.
- Deficiency check: with `e = 588 - t`, the convex lower bound `S >= 28224 - 94t` and the Goodman upper bound `S <= 28224 - (284/3)t` are incompatible for every positive integer `t`.
- Extremal check: at `e = 588`, equality in Cauchy forces `24`-regularity.
- Final obstruction check: the only remaining candidate is a putative strongly regular graph `(49,24,10,13)`, and the spectral multiplicity calculation blocks it.

# code_used

No code used.

Reason:

- The solve closed through a pure counting argument.
- The problem was not marked `search_heavy`, and no bounded experiment was needed after the structural route succeeded.

# result

Provisional solve result:

> There is no graph on `49` vertices avoiding `B11` whose complement also avoids `B13`. Hence `R(B11, B13) = 49`.

Rigorous proof candidate:

Assume to the contrary that such a graph `G` exists. Let `e = |E(G)|`, let `S = \sum_v d(v)^2`, let `T` be the number of triangles of `G`, and let `\bar T` be the number of triangles of `\overline G`.

Because `G` contains no `B11`, every edge of `G` has at most `10` common neighbors, so
`3T <= 10e`.
Because `\overline G` contains no `B13`, every edge of `\overline G` has at most `12` common neighbors in `\overline G`, so
`3\bar T <= 12(1176 - e)`.

Goodman gives
`T + \bar T = 18424 - 48e + S/2`.
Combining,

`18424 - 48e + S/2 <= 10e/3 + 4(1176 - e)`,

so

`S <= (284/3)e - 27440`.     `(1)`

Now write `e = 588 - t`, where `t >= 0`. Then `\sum_v d(v) = 1176 - 2t`.
Among integer sequences with this total sum, convexity minimizes `\sum_v d(v)^2` by taking `2t` vertices of degree `23` and the remaining `49 - 2t` vertices of degree `24`, hence

`S >= (49 - 2t)24^2 + (2t)23^2 = 28224 - 94t`.     `(2)`

But from `(1)`,

`S <= (284/3)(588 - t) - 27440 = 28224 - (284/3)t`.     `(3)`

For every positive integer `t`,

`28224 - 94t > 28224 - (284/3)t`,

so `(2)` and `(3)` are incompatible unless `t = 0`. Therefore `e = 588`.

Then `\sum_v d(v) = 1176`, and equality in Cauchy implies every degree is exactly `24`. Also `(1)` is now tight, so the triangle-cap inequalities are tight:

- every edge of `G` has exactly `10` common neighbors;
- every edge of `\overline G` has exactly `12` common neighbors in `\overline G`.

Since `G` is `24`-regular on `49` vertices, a nonedge `uv` has

`47 - |N(u) \cup N(v)| = 47 - (24 + 24 - |N(u) \cap N(v)|) = |N(u) \cap N(v)| - 1`

common nonneighbors. Because that number is exactly `12`, every nonedge of `G` has exactly `13` common neighbors in `G`.

So `G` would be strongly regular with parameters `(49,24,10,13)`.

For such a strongly regular graph, the restricted eigenvalues satisfy
`x^2 + (13 - 10)x + (13 - 24) = x^2 + 3x - 11 = 0`,
so they are

`r,s = (-3 +- sqrt(53))/2`.

If their multiplicities are `m_r,m_s`, then

- `m_r + m_s = 48`,
- `24 + m_r r + m_s s = 0` because the adjacency matrix has trace `0`.

Solving gives

- `m_r = 24 + 48 / sqrt(53)`,
- `m_s = 24 - 48 / sqrt(53)`,

which are not integers, contradiction.

Thus the assumed `49`-vertex witness does not exist. Combined with the packet lower bound `R(B11, B13) >= 49`, this gives the exact value

`R(B11, B13) = 49`.

Self-check after main result:

- The theorem closure is exact modulo verification of the arithmetic and the spectral obstruction.
- This is already theorem-shaped, not just an instance witness.
- Before Lean, the correct harness classification remains `CANDIDATE`, not `EXACT`.

# family_affinity

Strong.

Why:

- This sits exactly on the almost-diagonal book Ramsey corridor highlighted by the packet.
- The adjacent solved benchmark `R(B12, B13) = 51` gives an immediate comparison point.
- The proof style is family-aware: it exploits the edge-triangle cap on one color and the complement edge-triangle cap on the other.

# generalization_signal

Moderate but real.

What seems to scale:

- The Goodman-plus-convexity squeeze should remain useful on other one-gap almost-diagonal book pairs where the public bounds differ by `1`.
- The “deficiency from middle density” parameter `t` is a natural organizing variable for near-balanced candidates.

What does not obviously scale:

- The last step used the very specific infeasibility of `(49,24,10,13)`.
- For other parameter pairs, the extremal collapse may land on a feasible strongly regular parameter set or fail to hit exact equality at all.

# proof_template_reuse

Reusable template:

1. Translate book avoidance into an edgewise common-neighbor cap in each color.
2. Use triangle counts and Goodman to turn local caps into a global upper bound on `S = \sum d(v)^2`.
3. Compare against the convex lower bound coming from total edge count.
4. Force near-regularity, then exact regularity.
5. Identify the resulting extremal candidate as a highly rigid regular object and kill it spectrally or structurally.

This template looks reusable for nearby one-gap book Ramsey cases, but the last obstruction will be parameter-specific.

# candidate_theorem_slice

Smallest strong theorem slice exposed by the proof:

> Any `49`-vertex graph with no `B11` and with complement containing no `B13` would have to be `24`-regular, every edge would have exactly `10` common neighbors, and every nonedge would have exactly `13` common neighbors.

That slice is already substantial because it reduces the whole problem to the infeasible parameter set `(49,24,10,13)`.

# verify_rediscovery

Bounded PASS 1 verdict: no rediscovery found within budget.

What I checked:

- exact-term searches for `R(B11, B13)` and reversed / alternate notation for the same pair;
- source-targeted searches around the canonical chain `DS1.17` -> Lidicky-McKinley-Pfender-Van Overberghe 2025 -> Wesley 2026;
- exact-value checks for both candidate closures `R(B11, B13) = 49` and `R(B11, B13) = 50`;
- theorem / proposition / example style checks aimed at whether the 2025 and 2026 papers already settle the exact pair indirectly.

What turned up:

- the 2025 book-Ramsey paper remains the visible lower-bound anchor for this pair;
- the survey / benchmark material still supports the one-gap window `49 <= R(B11, B13) <= 50`;
- the 2026 Wesley material appears to close the adjacent `R(B12, B13) = 51` benchmark rather than the exact `B11` versus `B13` pair.

Conservative verify conclusion:

- no bounded evidence that the exact intended statement is already solved or directly implied in the cited public chain;
- rediscovery risk is not zero, but PASS 1 did not establish rediscovery;
- this run must not be labeled `EXACT` regardless, because Lean has not been completed.

# verify_faithfulness

The solve packet is faithful to the intended statement.

- The intended statement asks for the exact value of `R(B11, B13)` by either forcing `49` or producing a `49`-vertex witness for `50`.
- The record proves the forcing direction: every `49`-vertex graph contains `B11` or its complement contains `B13`.
- Combined with the packet's accepted lower bound `R(B11, B13) >= 49`, this yields the exact claim `R(B11, B13) = 49`.

I found no theorem drift, quantifier drift, or definition drift. The proof does not silently switch to a weaker proxy statement. The strongest positive claim remains the exact threshold `49`, but the honest harness classification is still `CANDIDATE` until Lean.

# verify_proof

First incorrect step found: none.

Detailed check:

- The book-avoidance translation is correct: avoiding `B11` means each edge of `G` has at most `10` common neighbors, and avoiding `B13` in the complement means each edge of `\overline G` has at most `12` common neighbors in `\overline G`.
- The triangle-count bounds `3T <= 10e` and `3\bar T <= 12(1176 - e)` are correct.
- The specialized Goodman identity `T + \bar T = 18424 - 48e + S/2` for `n = 49` is correct.
- Combining the previous lines gives `S <= (284/3)e - 27440`, and the arithmetic checks out.
- Writing `e = 588 - t`, the convexity lower bound `S >= (49 - 2t)24^2 + (2t)23^2 = 28224 - 94t` is the correct minimum square-sum for integer degrees with total degree `1176 - 2t`.
- For every integer `t > 0`, the lower bound exceeds the Goodman upper bound, so `t = 0` is forced.
- At `t = 0`, the equality chain is legitimate: `S = 28224` forces `24`-regularity, and the triangle-cap inequalities must both be tight.
- Tightness implies every edge of `G` has exactly `10` common neighbors and every edge of `\overline G` has exactly `12` common neighbors in `\overline G`.
- In a `49`-vertex `24`-regular graph, a nonedge having `12` common nonneighbors is equivalent to having `13` common neighbors in `G`, so the putative witness is strongly regular with parameters `(49,24,10,13)`.
- The strongly-regular obstruction is correct after making the multiplicities explicit: the restricted eigenvalues are `(-3 +- sqrt(53))/2`, and the multiplicities are `24 +- 48 / sqrt(53)`, impossible because multiplicities must be integers.

Net proof verdict: the argument appears mathematically correct as written after the tiny spectral-obstruction repair above.

# verify_adversarial

There is no checker or search code in this artifact. PASS 4 therefore reduces to direct arithmetic and consistency attacks on the proof.

What I reran locally:

- verified `binom(49,2) = 1176` and `binom(49,3) = 18424`;
- verified the Goodman-derived bound `S <= (284/3)e - 27440`;
- checked the deficiency inequalities numerically for `e = 588 - t` and confirmed contradiction for every integer `t = 1, ..., 16`, leaving only `e = 588`;
- computed the putative strongly-regular multiplicities numerically as approximately `30.5933` and `17.4067`, confirming they are nonintegral.

Adversarial conclusion:

- I did not find a hidden surviving case below the regularity collapse.
- I did not find a computational contradiction with the claimed counting argument.
- There is no explicit witness graph to attack because the proof is a universal nonexistence argument.

# verify_theorem_worthiness

Exactness:

- The claim is exact in content, but not Lean-sealed, so the harness classification cannot exceed `CANDIDATE`.

Novelty:

- The bounded rediscovery audit did not uncover an exact prior solution for `R(B11, B13)`.
- The novelty picture is therefore provisionally clean, not certified.

Reproducibility:

- High. The proof is short, self-contained, and depends only on standard counting identities plus a final strongly-regular infeasibility check.

Lean readiness:

- The argument is formalizable in principle, but Lean is not the shortest remaining path from this packet to a sealed publication outcome.
- The remaining work is still publication-facing: preserve the novelty position, present the counting chain cleanly, and decide whether formalization helps rather than detours.

Paper leverage:

- If correct and later Lean-sealed, this already looks like most of a publishable note.
- Best estimate: one solve would provide about `80%` to `85%` of the final paper.
- The visible title theorem is exactly `The Exact Value of R(B11, B13)`.

What scales:

- the Goodman plus convexity squeeze and the regularity-collapse template;
- the reduction from a one-gap threshold problem to a rigid extremal parameter set.

What does not clearly scale:

- the final obstruction is specific to the infeasible strongly regular parameter set `(49,24,10,13)`;
- nearby cases may collapse to feasible parameter sets or may fail to force equality.

Best honest publication status:

- not `INSTANCE_ONLY`, because the result is an exact title-theorem candidate on a frontier one-gap pair;
- not `PAPER_READY`, because verification is bounded, publication audit is still pending, and Lean is incomplete;
- best current label: `SLICE_CANDIDATE`.

# verify_verdict

- `verify_verdict = "CANDIDATE_CONFIRMED"`
- `classification = "CANDIDATE"`
- `confidence = 0.87`
- `publication_status = "SLICE_CANDIDATE"`
- `publication_confidence = 0.82`
- `lean_ready = false`
- `lean_packet_seal = false`
- `next_action = "publication_audit"`

# minimal_repair_if_any

Applied one tiny conservative repair only:

- replaced the terse spectral-obstruction sentence with the explicit multiplicity formulas `m_r = 24 + 48 / sqrt(53)` and `m_s = 24 - 48 / sqrt(53)`.

No other proof edits were needed.

# smallest_param_shift_to_test

Most informative next parameter shifts:

- `R(B10, B13)`: this tests whether the same Goodman/regularity mechanism survives one page lower on the left side.
- `R(B11, B14)`: this tests the same mechanism one page higher on the right side.

Why these are the right next probes:

- They perturb only one local triangle cap at a time.
- They indicate whether the present proof is a one-off rigidity event or the first case of a broader almost-diagonal pattern.

# why_this_is_or_is_not_publishable

If verification confirms the argument, this is publishable in the micro-paper lane.

Reason:

- The solve would already be about `80` to `85` percent of the paper, in line with the packet’s `0.83` estimate.
- The exact title theorem is already the whole point: `R(B11, B13) = 49`.
- Minimal remaining packaging work is small:
  state the current one-gap literature window,
  present the counting proof cleanly,
  isolate the `24`-regular collapse as a lemma,
  compare briefly to the neighboring exact case `R(B12, B13) = 51`.

Current caution:

- This is still only a solve-stage theorem candidate until verify checks the algebra, the spectral obstruction, and the prior-art status.

# paper_shape_support

What extra structure makes the result paper-shaped once the main claim closes:

- Supporting theorem slice:
  any extremal `49`-vertex witness must collapse to the impossible strongly regular parameter set `(49,24,10,13)`.
- Immediate corollary / remark:
  there is no extremal witness at the upper-bound threshold; the one-gap window collapses on the lower endpoint.
- Exact sentence for why the instance matters:
  This closes the last recorded one-gap case at `n = 13` on the `B_{n-2}` versus `B_n` book Ramsey line identified in the packet.
- Minimal packaging after solve:
  introduction, one counting lemma section, one spectral-obstruction paragraph, and a short frontier comparison paragraph.
- Micro-paper lane assessment:
  if the proof verifies, this is not too thin; it already reads like a one-theorem exact-value note rather than a loose computational instance.

# boundary_remark

Natural boundary remark:

- The proof does not produce a broader exact formula for `R(B_{n-2}, B_n)`.
- What it really shows is that for this parameter pair, any putative threshold witness would have to sit at the exact middle density and realize a highly rigid intersection pattern.
- So the scalable part is the regularity squeeze; the non-scalable part is the final parameter-specific impossibility of `(49,24,10,13)`.

# likely_failure_points

- The Goodman arithmetic should be rechecked line by line.
- The convex lower bound for `S` should be verified carefully in integer form.
- The strongly regular reduction should be checked for any hidden assumption when passing from complement-edge common-neighbor counts to `mu = 13`.
- The spectral obstruction should be written in a clean, referee-proof way during verify.
- The publication claim still depends on verify confirming that no exact closure of `R(B11, B13)` already exists in prior art.

# what_verify_should_check

- Recompute the Goodman specialization and all numeric constants:
  `1176`, `18424`, `28224`, and the coefficient `284/3`.
- Check the strict contradiction for every `t > 0` in the deficiency argument.
- Confirm that equality in the triangle-cap bounds really forces every edge to hit the cap.
- Confirm the conversion from “every complement edge has exactly `12` common neighbors in the complement” to `mu = 13` in `G`.
- Rewrite the strongly regular impossibility using a standard multiplicity formula and check it mechanically.
- Run the bounded prior-art check for this exact counting proof and exact value claim.
