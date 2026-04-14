# Solve Record: Determine the exact value of R(K3, K4-e, K4-e)

## statement_lock
- Active slug: `r-k3-k4e-k4e-three-color`.
- Active title theorem target: determine whether `R(K3, K4-e, K4-e)` is `21` or `22`.
- Exact intended statement: either every 3-coloring of `K21` contains a red `K3` or a blue/green `K4-e`, or there exists a 3-coloring of `K21` avoiding all three forbidden patterns.
- Working title theorem if solved: `The Exact Value of R(K3, K4-e, K4-e)`.
- If this closes, it is already about `0.84` of a paper by the active packet's own estimate, because the solve itself is the main theorem and the remaining packaging is short.

## definitions
- Write `J4 := K4-e`.
- A color class is `J4`-free iff no 4-vertex set spans at least five edges of that color.
- Equivalent local form: if `H` is `J4`-free and `uv` is an edge of `H`, then `u` and `v` have at most one common neighbor in `H`.
- Neighborhood form: for every vertex `v` in a `J4`-free graph `H`, the induced graph `H[N_H(v)]` has maximum degree at most `1`, hence is a matching plus isolated vertices.
- Extension form: if `G` is a valid 20-vertex coloring and we try to add a new vertex `x`, then the red neighbors of `x` must form an independent set in the old red graph, while the blue and green neighbors of `x` must each induce a matching in the corresponding old color graph.
- Ambiguities resolved: `K4-e` is treated as a non-induced forbidden subgraph, so a monochromatic `K4` is also forbidden in blue or green.
- Missing ingredient: the packet does not include the exact small two-color thresholds that would most naturally support an upper-bound contradiction on `21`.

## approach_A
- Structural / invariant route.
- Fix any vertex `v`. In each `J4`-free color, the same-color neighborhood of `v` induces only a matching, so large same-color neighborhoods immediately reduce to smaller two-color Ramsey subinstances.
- The red neighborhood `N_R(v)` is itself red-independent because red triangles are forbidden, so `N_R(v)` is a blue/green 2-coloring with both colors `J4`-free. Any sharp `R(J4, J4)` threshold would bound `deg_R(v)`.
- Similarly, each blue or green neighborhood contains a large subset with no edges of that same color, reducing to a 2-color `(K3, J4)` problem on roughly half the neighborhood size.
- This route is the cleanest potential proof of `R(K3, J4, J4) = 21`, but under the current local file budget it stalls at exactly the place where one needs those sharp small thresholds or an equivalent forcing lemma.
- Self-check: every use of `J4`-freeness here is local and exact; the blocker is not correctness but missing sharp closure data.

## approach_B
- Construction / extremal / contradiction route.
- The cheapest honest closure is a `K21` witness, because the active packet already supplies the inherited upper bound `R(K3, K4-e, K4-e) <= 22`.
- An older same-target artifact under the prior slug `k3-k4minus-k4minus-three-color-ramsey` already eliminated pure circulant distance-colorings on `Z_n` for `17 <= n <= 21`, so the next bounded constructive step should not repeat that family.
- The natural next experiment is extension-based: first recover an explicit valid 20-vertex coloring, then test whether any new vertex can be attached to it with exact local constraints.
- This is stronger than a raw 21-vertex random search because the extension condition is exact once a 20-vertex witness is fixed.
- Self-check: failure to extend one sampled 20-vertex witness does not prove `21`; it only says that this particular extremal template does not continue to `21`.

## lemma_graph
- `J4`-free implies each same-color edge has codegree at most `1`.
- Therefore each same-color neighborhood induces a matching.
- Therefore an attempted one-vertex extension of a valid witness becomes a partition problem into one independent-set color and two matching-induced colors.
- Therefore exact extension checks on sampled 20-vertex witnesses are cheap and rigorous once the base witness is known.
- Separately, pure circulant certificates are already ruled out locally by the older artifact, so the present run should focus on non-circulant witnesses or upper-bound forcing.

## chosen_plan
- Use the structural observations as the reasoning-first backbone.
- Preserve the inherited exact negative fact from the older local artifact: pure circulant witnesses do not occur for `17 <= n <= 21`.
- Run one bounded helper script with three tasks:
- recover one or more valid `K20` witnesses by local search;
- for each recovered `K20` witness, run an exact one-vertex extension backtrack;
- only if no `K21` witness appears that way, allow a direct `K21` local search as non-conclusive evidence.
- Stop condition for this run: either produce a verified `K21` witness, or record the strongest honest partial package without overstating heuristic misses.

## self_checks
- Statement lock is consistent with the packet's one-gap window `21 <= R(K3, K4-e, K4-e) <= 22`.
- The constructive branch is publication-relevant because a single `K21` witness would already determine the exact value `22`.
- The extension test is exact only relative to the specific sampled `K20` witnesses.
- Any heuristic search miss on `21` must be reported only as search evidence, never as a proof of `21`.

## code_used
- Added [`search_witness.py`](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/r-k3-k4e-k4e-three-color/search_witness.py), a bounded local-search helper with:
- an exact validator for red triangles and blue/green `J4`;
- an exact one-vertex extension backtracker that activates only after a valid 20-vertex witness is found;
- a heuristic hill-climber for recovering sample witnesses on `20` or `21` vertices.
- Completed bounded runs:
- `python3 -u artifacts/r-k3-k4e-k4e-three-color/search_witness.py --restarts20 20 --steps20 8000 --restarts21 10 --steps21 15000`
- Output summary:
- `n=20` best score `7 = 6` red triangles `+ 1` green `J4`;
- `n=21` best score `13 = 9` red triangles `+ 2` blue `J4` `+ 2` green `J4`;
- no valid witness found at either size in that bounded run.
- `python3 -u artifacts/r-k3-k4e-k4e-three-color/search_witness.py --skip21 --restarts20 40 --steps20 20000`
- Output summary:
- `n=20` best score `5 = 3` red triangles `+ 2` blue `J4`;
- still no valid 20-vertex witness recovered, so the exact extension backtracker never fired on an actual sample witness.
- Self-check: the validator and extension logic are exact, but the hill-climber is only heuristic. These misses are search evidence, not mathematical impossibility statements.

## result
- No exact solve obtained in this run.
- New exact theorem closure was not reached in either direction:
- no `K21` witness was found;
- no forcing proof of `21` was obtained;
- no exact one-vertex extension obstruction was derived, because the bounded search never recovered a concrete valid 20-vertex witness to extend.
- The strongest exact information still available locally remains the inherited negative result from the older same-target artifact: pure circulant distance-colorings do not realize witnesses for `17 <= n <= 21`.
- The present run adds only heuristic evidence that naive non-circulant local search does not quickly recover even the known `20`-vertex lower-bound witness, which means the witness landscape is more rigid than the simplest local-search model sees.
- Honest current state: `PARTIAL`, theorem-facing but still not paper-shaped.

## family_affinity
- Strong small-graph three-color Ramsey residue around `R(K3, J4, J4)`.
- The family anchor is real rather than cosmetic: closing this exact value removes a named one-gap survey entry.

## generalization_signal
- The neighborhood-matching reduction scales to other `R(K3, J_s, J_t)` settings with `J4` on one side.
- The extension viewpoint also scales: once an `(n-1)`-vertex witness is known, adding one vertex becomes a sharply constrained partition problem.
- The failed local search adds a weaker signal: extremal witnesses in this family may be structurally narrow enough that uninformed hill-climbing is a poor discovery mechanism.

## proof_template_reuse
- Upper-bound template: reduce same-color neighborhoods to smaller 2-color thresholds.
- Lower-bound template: recover a compact extremal witness, then convert the `n -> n+1` step into an exact local extension problem before trying looser search.
- Implementation reuse from this pass: the extension checker is ready for any future explicit 20-vertex witness, whether imported from prior literature or recovered by a better structured search.

## candidate_theorem_slice
- Pre-code slice only: pure circulant distance-colorings are already ruled out by the older local artifact, so any `K21` witness must be less rigid than a one-orbit cyclic certificate.
- No stronger theorem slice emerged in this run. The new code produced only heuristic non-results, not a publishable exact subtheorem.

## smallest_param_shift_to_test
- First shift: import or recover one explicit valid `K20` witness and immediately run the exact one-vertex extension checker from this artifact.
- Second shift: search the smallest structured non-circulant family that contains the known `20`-vertex witness, rather than using unconstrained hill-climbing.

## why_this_is_or_is_not_publishable
- If the exact value closes here, the result is already micro-paper shaped. The exact title theorem is `The Exact Value of R(K3, K4-e, K4-e)`.
- The minimal remaining packaging work after a genuine close would be a cleaned proof or a compact witness description, one verification appendix, and a short comparison against adjacent `J4` entries.
- Without the exact close, the current run is still too thin for the micro-paper lane. The present output does not isolate a new crisp theorem slice beyond the older circulant obstruction, and the added heuristic misses are not publication-grade mathematics.

## paper_shape_support
- A successful solve would already be in the `70-90%` range of a paper because the title theorem is the main payload.
- The smallest extra structure that would make the result paper-shaped, if the main claim closes, is:
- one compact structural lemma explaining the forcing or one compact witness normal form;
- one exact verification appendix or certificate description;
- one short boundary remark tying the value to the nearby `J4` landscape.
- Current package is still too thin for the micro-paper lane because the main theorem remains open and the new computational residue is only heuristic.

## boundary_remark
- Natural corollary if a `K21` witness exists: the survey upper bound `22` is tight, so the one-gap residue closes at the lower-bound end.
- Natural corollary if the forcing proof closes instead: every 3-coloring already fails on `21`, so no new `22`-vertex extremal phenomenon exists.
- Present boundary remark: the older exact no-circulant slice survives, and the new unconstrained local search did not even rediscover the known `20`-vertex witness under modest budgets, suggesting that any eventual lower-bound certificate is likely to need sharper structure than naive hill-climbing.

## likely_failure_points
- The upper-bound route may remain blocked without sharp local two-color thresholds.
- The lower-bound route may produce valid `K20` witnesses but no clear extension pattern to `21`.
- Heuristic search may fail for reasons unrelated to the mathematics.
- This pass hit exactly that third failure mode: the search tool likely underfit the witness structure rather than exposing a real obstruction.

## what_verify_should_check
- Recheck the inherited literature dependency giving `R(K3, K4-e, K4-e) <= 22`.
- If a `K21` witness is found, independently verify every forbidden-subgraph claim from the saved coloring.
- If only partial extension obstructions are found, verify that they are phrased as template-specific exact facts rather than global impossibility claims.
- If future work imports an explicit 20-vertex witness, verify that the extension backtracker in this artifact reports the correct feasibility result for that specific witness.
