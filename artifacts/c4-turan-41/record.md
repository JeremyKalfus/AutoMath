# c4-turan-41

## statement_lock
- Active slug: `c4-turan-41`
- Title: `Is ex(41, C4) = 132?`
- Locked intended statement: every `41`-vertex simple graph with `133` edges contains a `4`-cycle.
- Equivalent formulation used below: there is no `C4`-free simple graph on `41` vertices with `133` edges.
- Lower-bound context from the dossier: `132` edges are already known to occur, so the solve task is to eliminate or realize only the case `m = 133`.

Self-check:
- I am solving the exact `n = 41`, `m = 133` instance.
- A positive solve here would still be only `CANDIDATE` until Lean; a disproof would still need later exact checking.

## definitions
- Let `G` be a simple graph on `n = 41` vertices and `m = 133` edges.
- Write `d(v)` for the degree of `v`.
- `G` is `C4`-free iff every unordered pair of vertices has at most one common neighbor.
- Let `t(v) = e(G[N(v)])`; because `G` is `C4`-free, `G[N(v)]` is a matching, so `t(v) <= floor(d(v)/2)`.
- Let `N_2(v)` denote the set of vertices at graph distance exactly `2` from `v`.

Ambiguities / conventions:
- `C4` means a not-necessarily-induced `4`-cycle.
- All graphs are finite and simple.

Self-check:
- The common-neighbor reformulation is exact and is the main counting tool.
- The notation `t(v) = e(G[N(v)])` is valid because each edge inside `N(v)` is exactly one triangle through `v`.

## approach_A
- Global invariant route: count unordered `2`-paths by middle vertex.
- Since each unordered endpoint pair has at most one common neighbor,
  `sum_v C(d(v), 2) <= C(41, 2) = 820`.
- A slightly sharper split by adjacent / nonadjacent endpoint pairs gives
  `sum_v C(d(v), 2) = c + 3T`,
  where `c` is the number of nonedge pairs with a common neighbor and `T` is the number of triangles.
  Here `c <= 687`, and `3T <= sum_v floor(d(v)/2) <= 133`, so
  `sum_v C(d(v), 2) <= 819`.
- Therefore
  `sum_v d(v)^2 = 2 sum_v C(d(v), 2) + 266 <= 1904`.
- Cauchy also gives
  `(sum_v d(v))^2 <= 41 sum_v d(v)^2`,
  so `sum_v d(v)^2 >= 1726`.
- This places a hypothetical witness in a narrow near-regular window, but not yet in contradiction.

Self-check:
- The identity `sum_v C(d(v), 2) = c + 3T` is exact.
- This route controls variance but does not by itself settle `m = 133`.

## approach_B
- Local structural route: fix `v`.
- Because `G` is `C4`-free, every vertex outside `N[v]` is adjacent to at most one vertex of `N(v)`, and every vertex inside `N(v)` is adjacent to at most one other vertex of `N(v)`.
- Hence
  `sum_{u in N(v)} (d(u) - 1) = |N_2(v)| + 2 t(v) <= (40 - d(v)) + 2 t(v)`.
- Equivalently,
  `sum_{u in N(v)} d(u) <= 40 + 2 t(v) <= 40 + 2 floor(d(v)/2)`.
- Consequences in the near-regular regime:
  - if `d(v) = 7` and all degrees are at least `6`, then the neighbors of `v` have total excess over `6` at most `4`;
  - if `d(v) = 8` and all degrees are at least `6`, then that excess is `0`, so every neighbor of `v` has degree exactly `6` and `t(v) = 4`.
- In that `d(v) = 8` case the structure becomes exact:
  - `N(v)` is a perfect matching on `8` vertices;
  - each neighbor `u in N(v)` has one matched partner inside `N(v)` and exactly `4` neighbors outside `N[v]`;
  - the `32` outside vertices are partitioned into `8` disjoint classes of size `4`, one class attached to each `u`.

Self-check:
- The identity with `|N_2(v)| + 2 t(v)` is the strongest handwritten lemma from this pass.
- The `8`-vertex local picture is exact, not heuristic, once `delta(G) >= 6` is assumed.

## lemma_graph
1. `G` is `C4`-free iff each unordered vertex pair has at most one common neighbor.
2. Therefore `sum_v C(d(v), 2) = c + 3T <= 819`.
3. For every `v`,
   `sum_{u in N(v)} (d(u) - 1) = |N_2(v)| + 2 t(v) <= 40 - d(v) + 2 t(v)`.
4. Hence
   `sum_{u in N(v)} d(u) <= 40 + 2 t(v) <= 40 + 2 floor(d(v)/2)`.
5. If `delta(G) >= 6` and some vertex has degree `8`, then its neighborhood / second-neighborhood structure is completely rigid as described above.
6. If `delta(G) >= 6` and no vertex has degree `8`, then all degrees are `6` or `7`, so the degree sequence is exactly `21` vertices of degree `6` and `20` vertices of degree `7`.

## chosen_plan
- Best manual path: push the exact local identity from approach B and split the likely extremal regime by degree pattern.
- I could not prove `delta(G) >= 6` from first principles without importing nearby exact extremal data, so the cleanest reductions below are conditional on that step.

Major step 1: analyze the `delta(G) >= 6`, `Delta(G) = 8` branch.
- Let `v` have degree `8`.
- Then all `8` neighbors of `v` have degree `6`, `t(v) = 4`, and the `32` remaining vertices split into `8` classes of size `4`.
- Removing `v` and `N(v)` leaves a `32`-vertex induced subgraph with `89` edges and minimum degree at least `5`.
- Every outside vertex is adjacent to at most one vertex in each class, but I did not close a contradiction from this partitioned `32`-vertex core.

Self-check:
- The count `89 = 133 - 8 - 4 - 32` is correct.
- This branch is highly rigid but still unresolved in this pass.

Major step 2: analyze the `delta(G) >= 6`, `Delta(G) <= 7` branch.
- Then all degrees are `6` or `7`.
- Since `sum_v d(v) = 266`, the degree sequence is forced to be:
  - `21` vertices of degree `6`;
  - `20` vertices of degree `7`.
- Let `S` be the degree-`7` set and write `x = e(S)`.
- Degree bookkeeping gives:
  - `e(S, V \\ S) = 140 - 2x`,
  - `e(V \\ S) = x - 7`,
  - so `x >= 7`.
- Also every degree-`7` vertex lies in at least one triangle, because its neighbors have total degree at least `42 > 40`.
- The global bound becomes `sum_v C(d(v),2) = 21*15 + 20*21 = 735`, so `735 = c + 3T` and therefore `T >= 16`.
- These are real restrictions, but still not a contradiction.

Self-check:
- The `6/7` bookkeeping is exact once `delta(G) >= 6` and `Delta(G) <= 7`.
- The lower bound `T >= 16` is only pressure, not a closure.

Decision:
- The structural route is stronger than the raw global route, but I still do not have a proof or a witness.
- The main gap is the unproved low-degree branch and the unresolved rigid `8`-vertex branch.

## self_checks
- The intended statement stayed fixed throughout.
- Every displayed inequality is a necessary condition for a hypothetical `133`-edge `C4`-free graph.
- The strongest new handwritten point in this pass is the exact local identity
  `sum_{u in N(v)} (d(u)-1) = |N_2(v)| + 2t(v)`.
- I did not prove `delta(G) >= 6`, so the `6/7` and degree-`8` reductions are conditional.
- I did not find an exact contradiction or a counterexample.

## code_used
- Minimal code was used only after the two handwritten routes stalled.
- Scope:
  - a short randomized witness search over near-regular degree patterns, centered on the natural `20` vertices of degree `7` and `21` of degree `6`, plus a few small `5/8` perturbations;
  - degree-preserving edge switches only;
  - objective: minimize repeated-common-neighbor violations.
- Outcome:
  - no `133`-edge `C4`-free witness was found in the short budget;
  - the best sample still had `93` repeated-common-neighbor violations, so the search never approached a genuine witness.
- This is negative heuristic evidence only. It is not a proof of impossibility.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact output from this pass:
  - any `41`-vertex `133`-edge `C4`-free graph must satisfy the global bound `sum_v C(d(v),2) <= 819`;
  - for every vertex `v`,
    `sum_{u in N(v)} (d(u)-1) = |N_2(v)| + 2t(v) <= 40 - d(v) + 2t(v)`,
    hence
    `sum_{u in N(v)} d(u) <= 40 + 2 floor(d(v)/2)`;
  - conditional on `delta(G) >= 6`, the graph falls into one of two rigid patterns:
    - a degree-`8` anchored partition with a `32`-vertex, `89`-edge residual core; or
    - the exact `21`-by-`20` split of degree `6` and degree `7` vertices, with triangle pressure `T >= 16`.
- I did not prove `ex(41, C4) = 132`, and I did not find a `133`-edge counterexample.

## likely_failure_points
- The largest unresolved gap is whether a low-degree vertex can be ruled out offline without importing nearby exact values such as `ex(40, C4)`.
- The degree-`8` branch may require a tailored exact search inside the rigid `32`-vertex partitioned core, not just more soft inequalities.
- The `6/7` branch may need a sharper triangle / incidence lemma than the ones derived here.
- The randomized witness search was intentionally weak and should not be overinterpreted.

## what_verify_should_check
- Check the local identity carefully:
  `sum_{u in N(v)} (d(u)-1) = |N_2(v)| + 2t(v)`.
- Check the derived inequality
  `sum_{u in N(v)} d(u) <= 40 + 2 floor(d(v)/2)`.
- Check the conditional case split:
  - if `delta(G) >= 6` and `d(v)=8`, then the `8` neighbors of `v` all have degree `6`, form `4` matched pairs, and the outside `32` vertices split into `8` classes of size `4`;
  - if `delta(G) >= 6` and `Delta(G) <= 7`, then the degree sequence is exactly `21` sixes and `20` sevens, with `T >= 16`.
- In verify, the most useful bounded web task is to check whether exact nearby values such as `ex(40, C4)` are already canonical; if yes, that may eliminate the low-degree branch immediately.
- Do not treat the failed randomized search as more than heuristic negative evidence.

## verify_rediscovery
- PASS 1 used a bounded web audit against the exact instance, alternate notation, and the canonical sources.
- Exact-instance queries for `ex(41,C4)`, `ex(41,C_4)`, and `41`-vertex `C4`-free graphs with `132/133` edges did not produce any paper or database entry claiming an exact value for `n=41`.
- The canonical source OEIS A006855 still lists only the sandwich `a(41) >= 132` and `a(41) <= 133`, with the OEIS page modified on 2026-03-13.
- Brendan McKay's ANU extremal-graphs table still marks the `H={C4}` row at `n=41` as `>=132`, not exact, while exact values are explicitly marked without `>=` on that page.
- Older literature pages surfaced in the audit, including Clapham-Flockhart-Sheehan and Furedi, but nothing in the retrieved material settled the exact `n=41` instance or implied it directly.
- Verdict for PASS 1: no rediscovery established within the bounded search budget.

## verify_faithfulness
- The solver stayed locked to the intended statement `ex(41, C4) = 132`, equivalently the nonexistence of a `41`-vertex `133`-edge `C4`-free graph.
- I did not find wrong-theorem drift, definition drift, or quantifier drift in the writeup.
- The issue is not mismatch of statements; it is that the argument never reaches the intended statement. The claimed output is only a set of necessary conditions for a hypothetical counterexample.

## verify_proof
- First incorrect step found: none.
- The main displayed lemmas check out as necessary conditions:
  - `G[N(v)]` is a matching in a `C4`-free graph, so `t(v) <= floor(d(v)/2)`.
  - `sum_v C(d(v),2) = c + 3T` with `c <= 687`, hence `sum_v C(d(v),2) <= 819`.
  - For fixed `v`, each contribution to `sum_{u in N(v)} (d(u)-1)` comes either from a unique vertex of `N_2(v)` or from an edge internal to `N(v)`, giving the exact identity
    `sum_{u in N(v)} (d(u)-1) = |N_2(v)| + 2t(v)`.
  - The conditional `delta(G) >= 6` branches are then valid deductions from that identity.
- The proof still fails critically as a proof of the intended theorem because it never eliminates the low-degree branch and never closes either conditional high-minimum-degree branch.
- So the solver's record is mathematically faithful but incomplete: it supports `PARTIAL`, not `CANDIDATE` and not the target theorem.

## verify_adversarial
- No saved checker or witness file exists in `artifacts/c4-turan-41/`, so there was no executable artifact to rerun in PASS 4.
- The solve record itself says the randomized search was only heuristic and did not come close to a `133`-edge `C4`-free witness; that negative experiment cannot support the theorem.
- I adversarially checked the arithmetic dependencies in the handwritten deductions instead:
  - in the `6/7` branch, `21*6 + 20*7 = 266` and `21*15 + 20*21 = 735`, so the triangle-pressure bound `T >= 16` is correct;
  - in the `d(v)=8` branch, the residual-edge count `133 - 8 - 4 - 32 = 89` is correct.
- These checks support the local bookkeeping, but they do not repair the missing global contradiction.

## verify_verdict
- `UNVERIFIED`
- Reason: no rediscovery was found, but no exact proof or exact disproof was verified either.
- Appropriate harness classification here is still `PARTIAL`, because the current artifact contains valid reductions and no decisive conclusion.
- `lean_ready = false` because Lean should not be used on a merely partial argument.

## minimal_repair_if_any
- No repair to the mathematics was needed for correctness of the displayed lemmas.
- The conservative repair is only to downgrade the status cleanly: this run should remain `PARTIAL` / `UNVERIFIED`, not escalate to `CANDIDATE` or `EXACT`.
