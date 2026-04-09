# c4-turan-42

## statement_lock
- Active slug: `c4-turan-42`
- Title: `Is ex(42, C4) = 137?`
- Locked intended statement: `ex(42, C4) = 137`.
- Working equivalent for this solve pass: there is no simple `42`-vertex `C4`-free graph with `138` or `139` edges.
- Dossier context only: `selected_problem.md` already supplies a `137`-edge lower bound and a `<= 139` upper range, but this solve pass does not re-prove those external facts.

Self-check:
- I am attacking only the exact `n = 42` instance.
- I do not have an exact proof or an explicit counterexample, so no stronger classification than `PARTIAL` is justified here.

## definitions
- Let `G` be a simple graph on `n = 42` vertices with `m in {138,139}` edges.
- Write `d(v)` for the degree of `v`.
- Let `t(v) = e(G[N(v)])`. In a `C4`-free graph, `G[N(v)]` is a matching, so `t(v) <= floor(d(v)/2)`.
- Let `N_2(v)` be the set of vertices at graph distance exactly `2` from `v`.
- `G` is `C4`-free iff every unordered pair of vertices has at most one common neighbor.
- Every edge lies in at most one triangle, because two distinct common neighbors of an edge would create a `4`-cycle.

Ambiguities / conventions:
- `C4` means a not-necessarily-induced `4`-cycle.
- All graphs are finite and simple.

Self-check:
- The common-neighbor formulation is exact and is the main counting tool.
- The claim that `G[N(v)]` is a matching is standard: if two edges in `N(v)` shared an endpoint, they would give two common neighbors for an edge through `v`.

## approach_A
- Global `2`-path count:
  `sum_v C(d(v), 2) <= C(42, 2) = 861`.
- A sharper split into nonedge pairs with a common neighbor plus triangles gives
  `sum_v C(d(v), 2) = c + 3T`,
  where `c` counts nonadjacent pairs with a common neighbor and `T` is the number of triangles. Since `c <= 861 - m`,
  - for `m = 138`, `c <= 723`;
  - for `m = 139`, `c <= 722`.
  Also every edge lies in at most one triangle, so `3T <= m`.
- Fix `v`. Each contribution to `sum_{u in N(v)} (d(u) - 1)` comes either from a unique vertex of `N_2(v)` or from an edge inside `N(v)`, so
  `sum_{u in N(v)} (d(u) - 1) = |N_2(v)| + 2 t(v) <= 41 - d(v) + 2 t(v)`.
- Therefore
  `sum_{u in N(v)} d(u) <= 41 + 2 t(v) <= 41 + 2 floor(d(v)/2)`.

Consequences in the conditional regime `delta(G) >= 6`:
- A vertex of degree `9` is impossible, because then the left side is at least `9 * 6 = 54` while the right side is at most `41 + 2 floor(9/2) = 49`.
- So `Delta(G) <= 8`.
- If `d(v) = 8`, then the neighbors of `v` have total excess over `6` at most `1`, because
  `sum_{u in N(v)} d(u) <= 49`.
  Hence:
  - `v` has no degree-`8` neighbor;
  - `v` has at most one degree-`7` neighbor.
- Also any degree-`8` vertex is triangle-saturated. Since `sum_{u in N(v)} d(u) >= 48` and also
  `sum_{u in N(v)} d(u) <= 41 + 2 t(v)`,
  we must have `t(v) = 4`.
  So `N(v)` is a perfect matching on `8` vertices, and every incident edge of `v` lies in a triangle.
- More explicitly:
  - if all `8` neighbors of `v` have degree `6`, then the `33` vertices outside `N[v]` receive exactly `32` attachments from `N(v)`, so exactly one outside vertex avoids `N(v)`;
  - if one neighbor has degree `7` and the other seven have degree `6`, then the outside `33` vertices are covered exactly once by `N(v)`.
- In the no-`8` branch with `delta(G) >= 6`, all degrees are `6` or `7`, so the degree sequence is forced:
  - for `m = 138`: `24` vertices of degree `7` and `18` of degree `6`;
  - for `m = 139`: `26` vertices of degree `7` and `16` of degree `6`.
- This already forces triangle pressure:
  - for `m = 138`, the minimum possible `sum_v C(d(v),2)` is `24*21 + 18*15 = 774`, hence `774 = c + 3T` with `c <= 723`, so `T >= 17`;
  - for `m = 139`, the minimum possible `sum_v C(d(v),2)` is `26*21 + 16*15 = 786`, hence `786 = c + 3T` with `c <= 722`, so `T >= 22`.
- In the pure `6/7` branch, every degree-`7` vertex lies in at least one triangle, because its neighbors have total degree at least `7*6 = 42 > 41`.

Self-check:
- The local identity `sum_{u in N(v)} (d(u) - 1) = |N_2(v)| + 2 t(v)` is exact.
- The degree-`8` conclusions are rigorous once `delta(G) >= 6` is assumed.
- This route gives a tight near-regular picture, but not a contradiction.

## approach_B
- Extremal / contradiction route: look first for a low-degree escape, then force near-regularity.
- If some vertex has degree at most `5`, deleting it leaves a `41`-vertex graph with at least `133` or `134` edges. That suggests a hypothetical `42`-vertex counterexample would already sit right next to the unresolved `41`-vertex frontier, not in a genuinely sparse branch.
- I could not close that deletion branch without importing an exact theorem for `n = 41`, so the more promising handwritten path is again the conditional regime `delta(G) >= 6`.
- Let `x` be the number of degree-`8` vertices in that regime.
  Then the degree counts are forced by the handshake lemma:
  - for `m = 138`: `(n_8, n_7, n_6) = (x, 24 - 2x, 18 + x)`;
  - for `m = 139`: `(n_8, n_7, n_6) = (x, 26 - 2x, 16 + x)`.
- Since degree-`8` vertices are independent and each has at most one degree-`7` neighbor, any high-degree branch is heavily supported by degree-`6` vertices.
- In the pure `6/7` branch (`x = 0`), let `B` be the degree-`7` set and `C` the degree-`6` set. Degree bookkeeping gives:
  - for `m = 138`:
    `e(B,C) = 168 - 2 e(B)` and `e(C) = e(B) - 30`, so `e(B) >= 30`;
  - for `m = 139`:
    `e(B,C) = 182 - 2 e(B)` and `e(C) = e(B) - 43`, so `e(B) >= 43`.
- Also every `v in B` has at most `5` neighbors inside `B`, because each such neighbor contributes one unit of excess over the baseline degree `6`, and the local bound at a degree-`7` vertex allows total excess at most `5`.

Self-check:
- The deletion observation is only guidance; it is not a proof step.
- The degree-class formulas are exact once `delta(G) >= 6`.
- I still do not have a contradiction in either the `x > 0` branch or the pure `6/7` branch.

## lemma_graph
1. `G` is `C4`-free iff each unordered vertex pair has at most one common neighbor.
2. Therefore `sum_v C(d(v),2) = c + 3T`, and since `c <= 861 - m` and `3T <= m`, we get `sum_v C(d(v),2) <= 861`.
3. For every `v`,
   `sum_{u in N(v)} (d(u) - 1) = |N_2(v)| + 2 t(v) <= 41 - d(v) + 2 t(v)`.
4. Hence
   `sum_{u in N(v)} d(u) <= 41 + 2 t(v) <= 41 + 2 floor(d(v)/2)`.
5. If `delta(G) >= 6`, then `Delta(G) <= 8`.
6. If `delta(G) >= 6` and `d(v) = 8`, then `t(v) = 4`, `v` has no degree-`8` neighbor, and at most one degree-`7` neighbor.
7. If `delta(G) >= 6` and there are no degree-`8` vertices, then the graph is exactly `6/7`-regular with the two forced degree counts listed above.
8. In that `6/7` branch, triangle pressure already gives `T >= 17` for `m = 138` and `T >= 22` for `m = 139`.

## chosen_plan
- Best handwritten path: force as much structure as possible from the local common-neighbor identity, then split into:
  - a degree-`8` branch with rigid triangle-saturated neighborhoods; and
  - a pure `6/7` branch with exact degree counts and many forced triangles.
- That reduced the search space substantially, but it did not close the low-degree deletion branch and did not turn the conditional `delta(G) >= 6` branches into contradictions.

Major step 1:
- I pushed the local identity hard enough to get the exact degree-`8` behavior above.

Self-check:
- This is the strongest rigorous output of the solve pass.
- It is still conditional on proving `delta(G) >= 6`.

Major step 2:
- After both handwritten routes stalled, I used one tiny bounded falsifier search, directly tied to the intended statement.
- The search fixed `n = 42` and `m = 139` first, then `m = 138`, and minimized the score
  `sum_{u<v} max(0, codeg(u,v) - 1)`
  by random edge swaps at fixed edge count.
- Budget: `12` restarts of `60000` proposed swaps for each edge count.
- Outcome:
  - no `139`-edge `C4`-free graph was found;
  - no `138`-edge `C4`-free graph was found;
  - best scores reached were `69` for `m = 139` and `61` for `m = 138`.

Self-check:
- This search is strictly heuristic negative evidence.
- It is not a proof of impossibility and should not be treated as one.

## self_checks
- The intended statement stayed locked throughout.
- All displayed lemmas before the search step are necessary conditions for a hypothetical `138`- or `139`-edge `C4`-free graph.
- I did not prove `delta(G) >= 6`.
- I did not eliminate the low-degree deletion branch without borrowing external exact data.
- I did not find a genuine `138`- or `139`-edge witness.

## code_used
- Yes, but only after two handwritten strategies stalled.
- Scope:
  - a short direct falsifier search with fixed edge count and a `C4`-violation score;
  - random edge swaps only;
  - no SAT, ILP, CP-SAT, or exhaustive brute force.
- Result:
  - no witness for `m = 138` or `m = 139` was found in the short budget;
  - the search stayed far from a certified witness, so it provides only weak negative evidence.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact output from this pass:
  - for every vertex `v`,
    `sum_{u in N(v)} (d(u) - 1) = |N_2(v)| + 2 t(v) <= 41 - d(v) + 2 t(v)`,
    hence
    `sum_{u in N(v)} d(u) <= 41 + 2 floor(d(v)/2)`;
  - conditional on `delta(G) >= 6`, every hypothetical counterexample has `Delta(G) <= 8`;
  - any degree-`8` vertex is highly rigid: it is triangle-saturated, has no degree-`8` neighbor, and at most one degree-`7` neighbor;
  - in the no-`8` branch, the degree sequence is forced to `24/18` or `26/16` in the `7/6` split, with at least `17` or `22` triangles respectively.
- I did not prove `ex(42, C4) = 137`, and I did not disprove it by finding a larger witness.

## likely_failure_points
- The main unresolved gap is the low-degree branch: I do not know how to rule out `delta(G) <= 5` without a sharper exact nearby theorem.
- Even in the conditional `delta(G) >= 6` regime, the pure `6/7` branch still leaves many configurations.
- The bounded local search may simply miss a structured near-extremal witness.
- The dossier mentions a known `137`-edge witness, but no explicit local witness file was available here to extend or perturb directly.

## what_verify_should_check
- Check the exact local identity
  `sum_{u in N(v)} (d(u) - 1) = |N_2(v)| + 2 t(v)`.
- Check the derived bound
  `sum_{u in N(v)} d(u) <= 41 + 2 floor(d(v)/2)`.
- Check the degree-`8` consequences carefully:
  - `delta(G) >= 6` implies `Delta(G) <= 8`;
  - a degree-`8` vertex has `t(v) = 4`, no degree-`8` neighbors, and at most one degree-`7` neighbor.
- Verify that the triangle lower bounds `T >= 17` and `T >= 22` in the pure `6/7` branches are derived correctly from `sum_v C(d(v),2) = c + 3T`.
- Treat the edge-swap search as heuristic only.
- In verify, the most useful bounded prior-art task is probably to audit whether exact nearby values such as the `41`-vertex case are already settled canonically; that could decide whether the low-degree deletion branch was actually enough.

## verify_rediscovery
- PASS 1 used a bounded web audit against the exact instance, alternate notation, and the canonical sources.
- Exact-instance queries for `ex(42,C4)`, `ex(42,C_4)`, and `42`-vertex `C4`-free graphs with `137/138/139` edges did not produce any paper or database entry claiming an exact value for `n = 42`.
- The canonical source OEIS A006855 still shows the range `137 <= ex(42, C4) <= 139` rather than an exact value.
- Brendan McKay's ANU extremal-graphs table for `H={C4}` still treats the `42` row as lower-bound-only at `137`, while exact rows on that page are presented without the lower-bound marker.
- I did not find a theorem, proposition, example, observation, or corollary in the surfaced source material that already settles the exact `n = 42` instance directly.
- Verdict for PASS 1: no rediscovery established within the bounded search budget.

## verify_faithfulness
- The solver stayed locked to the intended statement `ex(42, C4) = 137`, equivalently the nonexistence of a `42`-vertex `C4`-free graph with `138` or `139` edges, conditional on the dossier's external `137`-edge lower bound.
- I did not find definition drift, quantifier drift, or substitution of a different graph notion.
- The only faithfulness caveat is wording: the line calling this a "working equivalent" depends on importing the external `137`-edge witness from the dossier. Internally, the record proves only necessary conditions against the `138/139` cases, not the full theorem.
- So the issue is incompleteness, not wrong-theorem drift.

## verify_proof
- First incorrect step found: none in the displayed rigorous lemmas.
- The main deductions check out as necessary conditions:
  - `G[N(v)]` is a matching in a `C4`-free graph, so `t(v) <= floor(d(v)/2)`.
  - `sum_v C(d(v),2) = c + 3T` with `c <= 861 - m`, hence `sum_v C(d(v),2) <= 861`.
  - For fixed `v`, each contribution to `sum_{u in N(v)} (d(u)-1)` comes either from a unique vertex of `N_2(v)` or from an edge inside `N(v)`, giving the exact identity
    `sum_{u in N(v)} (d(u)-1) = |N_2(v)| + 2 t(v)`.
  - From that identity, the bound `sum_{u in N(v)} d(u) <= 41 + 2 floor(d(v)/2)` is valid.
  - Under `delta(G) >= 6`, the deductions `Delta(G) <= 8`, the rigidity of degree-`8` vertices, and the forced `6/7` degree counts are valid.
  - In the pure `6/7` branch, the triangle-pressure lower bounds `T >= 17` for `m = 138` and `T >= 22` for `m = 139` are arithmetically correct.
- The proof still fails as a proof of the intended theorem because it never eliminates the low-degree deletion branch and never closes the conditional high-minimum-degree branches.
- So the artifact is mathematically coherent but incomplete: it supports `PARTIAL`, not `CANDIDATE` and not the target equality.

## verify_adversarial
- No saved checker, witness, or executable search script exists in `artifacts/c4-turan-42/`, so there was no local artifact to rerun in PASS 4.
- The solve record itself already labels the edge-swap search as heuristic only; that negative experiment cannot verify the theorem.
- I stress-tested the key bookkeeping instead:
  - in the `m = 138` pure `6/7` branch, `24*7 + 18*6 = 276 = 2m` and `24*21 + 18*15 = 774`, so `774 = c + 3T` with `c <= 723` gives `T >= 17`;
  - in the `m = 139` pure `6/7` branch, `26*7 + 16*6 = 278 = 2m` and `26*21 + 16*15 = 786`, so `786 = c + 3T` with `c <= 722` gives `T >= 22`;
  - for `d(v) = 8` and `delta(G) >= 6`, the lower bound `sum_{u in N(v)} d(u) >= 48` against the upper bound `41 + 2t(v)` forces `t(v) = 4`, exactly as claimed.
- These adversarial checks support the local deductions, but they do not produce the missing contradiction.

## verify_verdict
- `UNVERIFIED`
- Reason: PASS 1 did not establish rediscovery, but PASS 2 through PASS 4 did not verify any exact proof or exact disproof either.
- Appropriate harness classification here remains `PARTIAL`, because the artifact contains valid reductions but no decisive theorem-level conclusion.
- `lean_ready = false` because Lean should not be used on a partial argument, and there is no frontier-novel exact statement ready to formalize.

## minimal_repair_if_any
- No repair to the displayed mathematics was needed for correctness of the local lemmas.
- The conservative wording repair is this: replace "working equivalent" by "conditional reduction assuming the dossier's external `137`-edge lower bound".
- The status repair is to keep this run at `PARTIAL` / `UNVERIFIED`, not escalate it to `CANDIDATE` or `EXACT`.
