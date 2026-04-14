# Solve Record: Determine the exact value of R(K3, K4-e, K4-e)

## statement_lock
- Active slug: `k3-k4minus-k4minus-three-color-ramsey`.
- Active title theorem target: determine whether `R(K3, K4-e, K4-e)` is `21` or `22`.
- Working interpretation: either force a red `K3` or blue/green `K4-e` in every 3-coloring of `K21`, or exhibit one 3-coloring of `K21` with no red `K3` and no blue/green `K4-e`.
- Solve-stage claim discipline: even if the mathematics closes, the strongest positive solve classification here is `CANDIDATE` until Lean.
- If a `K21` witness is found, then, together with the packet's inherited upper bound `R(K3, K4-e, K4-e) <= 22`, the exact value becomes `22`.

## definitions
- Write `J4 := K4-e`.
- A color class is `J4`-free iff no 4-vertex set spans at least five edges of that color.
- Useful local reformulation: if `H` is `J4`-free and `uv` is an edge of `H`, then `u` and `v` have at most one common neighbor in `H`; otherwise `uv` together with two distinct common neighbors gives a copy of `J4`.
- Equivalent neighborhood form: for every vertex `v` in a `J4`-free graph `H`, the induced graph `H[N_H(v)]` has maximum degree at most `1`, hence is a matching plus isolated vertices.

## approach_A
Structural / invariant route.

1. Fix a vertex `v`. In the blue graph, `B[N_B(v)]` is a matching. Therefore one can delete at most one endpoint from each blue edge in `B[N_B(v)]` and obtain a subset `S_B(v) ⊆ N_B(v)` of size at least `ceil(deg_B(v)/2)` with no blue edges.
2. On `S_B(v)`, every edge is red or green. Red still avoids `K3`, and green still avoids `J4`.
3. So any sharp 2-color threshold for `(K3, J4)` immediately converts into an upper bound on `deg_B(v)`, and symmetrically on `deg_G(v)`.
4. A parallel statement holds for red neighborhoods: `R[N_R(v)]` is edgeless because red is triangle-free, so the packet's inherited upper bound plausibly comes from mixing this with known small 2-color Ramsey thresholds.
5. This route is attractive for a forcing proof of `21`, but with the current file budget I do not have the local two-color threshold tables in hand. The route is still useful because it explains why same-color neighborhoods are structurally sparse and why any eventual proof on `21` should be highly local.

Self-check:
- The matching claim is correct: if some `x ∈ N_B(v)` had two blue neighbors `y,z` inside `N_B(v)`, then edge `vx` would have common blue neighbors `y,z`, yielding a blue `J4`.
- This route gives real constraints, but not yet a closed contradiction on `21` from the packet alone.

## approach_B
Construction / extremal / contradiction route.

1. The lower-bound side is cheaper: one explicit `K21` coloring closes the exact value at `22`, because the packet already carries the external upper bound `22`.
2. A naive blow-up construction is sharply obstructed. If a part `P` has a same-color external neighbor class `Q` of size at least `2`, then any same-color edge inside `P` together with two vertices of `Q` creates `J4`. So template blow-ups can only use internal blue/green edges in very restricted circumstances.
3. This obstruction pushes toward compact, high-symmetry certificates rather than loose multipartite substitutions.
4. The most economical such family is circulant colorings on `Z_21`: assign each undirected distance class `1,2,...,10` one of the three colors. The search space is only `3^10 = 59049`.
5. A valid circulant witness would be a strong micro-paper-quality certificate: it would give the exact value `22`, a compact construction, and a natural theorem statement.

Self-check:
- This is not a generic SAT or CP-SAT launch. It is a tightly symmetry-reduced witness search justified only after recording structural reasoning.
- Failure of the circulant family would not prove `21`; it would only say that the most compact cyclic certificates do not occur.

## lemma_graph
1. `J4`-free implies every same-color edge has codegree at most `1`.
2. Therefore each same-color neighborhood induces a matching.
3. Therefore each same-color neighborhood contains a large subset free of that color.
4. This yields local two-color reductions that are the natural path toward a forcing proof of `21`.
5. On the lower-bound side, any witness with strong cyclic symmetry would be especially valuable because it compresses the certificate and the eventual paper narrative.

## chosen_plan
- Best path under the file and time budget: pursue the lower-bound witness route first inside the circulant family on `21` vertices.
- Rationale: the forcing route toward `21` clearly needs one more layer of small-case Ramsey input, while a single `K21` witness would immediately settle the exact value at `22`.
- Scope discipline: only a bounded cyclic search plus exact checking of the target forbidden subgraphs.

## self_checks
- Statement lock is consistent with the packet: the only open values are `21` and `22`.
- The lower-bound logic is valid only because the inherited upper bound `22` is already part of the active packet.
- Any computational result below must be phrased conservatively: a witness would settle the value; a search miss inside one template family would not.
- Post-search check: the validator uses the exact common-neighbor criteria, namely `>= 1` common same-color neighbor for a red edge means a red triangle, and `>= 2` common same-color neighbors for a blue or green edge means a blue or green `J4`.

## code_used
- Added [`circulant_scan.py`](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/k3-k4minus-k4minus-three-color-ramsey/circulant_scan.py), a minimal exhaustive checker over pure circulant colorings on `Z_n`.
- The script assigns each undirected cyclic distance class one of the three colors and checks:
- red validity by forbidding any red edge with a common red neighbor;
- blue/green validity by forbidding any blue or green edge with two common same-color neighbors.
- Exhaustive outputs obtained from the script:
- `17 -> None`
- `18 -> None`
- `19 -> None`
- `20 -> None`
- `21 -> None`

## result
- No exact solve obtained in this pass.
- Strong negative evidence on the lower-bound side: there is no pure circulant coloring on `Z_n` for `17 <= n <= 21` that avoids a red `K3` and blue/green `J4`.
- In particular, the most compact cyclic witness family does not realize the known lower bound at `20`, so a `K21` counterexample, if it exists, must already be substantially less rigid than a one-orbit circulant construction.
- The upper-bound route toward `21` remains alive, but I did not close it from the current packet because the natural next ingredient is a sharper local two-color threshold or equivalent forcing lemma.
- Current honest state: `PARTIAL`, theorem-facing, but not an exact value and not yet a publishable packet.

## family_affinity
- This problem sits in the small three-color Ramsey family around `R(K3, J4, J4)` and the equivalent `R(K3+e, J4, J4)` slice named in the packet.
- The strongest family feature is that an exact solve would close a survey-line one-gap residue rather than create an isolated ad hoc computation.

## generalization_signal
- The neighborhood-matching lemma scales to every `R(K3, J_s, J_t)`-type target where one color forbids `J4`.
- The failed circulant scan suggests that pure one-orbit cyclic symmetry may be too rigid for this family even below the true lower-bound frontier, so the next construction layer should be only slightly less rigid rather than fully unconstrained.

## proof_template_reuse
- Upper-bound reuse template: convert `J4`-free same-color neighborhoods into large opposite-color reductions, then close with small 2-color Ramsey thresholds.
- Lower-bound reuse template: rule out the cheapest symmetry classes first, then escalate to the smallest non-circulant extensions only if the structured search miss is genuine.

## candidate_theorem_slice
- Real slice visible after this pass: pure circulant distance-colorings on `Z_n` do not furnish lower-bound witnesses for `17 <= n <= 21`.
- This is mathematically exact for that family, but still too thin to count as the target micro-paper result.

## smallest_param_shift_to_test
- The next two parameter shifts with the best information value are:
- test two-orbit or near-circulant templates on `21`, because pure circulants already fail below the known lower bound;
- return to the forcing side and isolate the smallest exact 2-color threshold needed to turn the neighborhood-matching reduction into a contradiction on `21`.

## why_this_is_or_is_not_publishable
- If the exact value closes, it is already about `0.78` of a paper by the packet's own assessment, and the title theorem is immediate: `The Exact Value of R(K3, K4-e, K4-e)`.
- The current outcome is still too thin for the micro-paper lane. It removes one natural certificate family and sharpens the solver map, but it does not by itself supply the title theorem or a paper-shaped theorem slice with immediate narrative leverage.

## paper_shape_support
- A successful solve would already be `70-90%` of a paper because the remaining packaging work is small: write the proof or present the extremal coloring, connect it to the `K3+e` equivalence, and add one short comparison against the known one-gap survey entry.
- Minimal remaining packaging after an exact close: a cleaned proof narrative or a checked witness table, plus one short boundary discussion.
- Current remaining gap is still the main theorem itself, so this pass does not change the publication status.

## boundary_remark
- Natural immediate remark if a `K21` witness exists: the survey upper bound `22` is tight, so the unresolved `J4/J4` residue collapses exactly at the lower endpoint.
- Natural immediate remark if the upper-bound direction closes instead: the final obstruction already appears on `21`, so no new `22`-vertex extremal phenomenon is needed.
- Current boundary remark from the experiment: any future lower-bound witness on `21` cannot be a pure distance-coloring on the cycle, and in fact neither can the already-known lower-bound witness at `20`.

## likely_failure_points
- The upper-bound route may stall without importing a small exact 2-color `(K3, J4)` threshold or an equivalent local lemma.
- The lower-bound route may fail simply because no compact cyclic witness exists, even if a non-circulant witness does.
- A computational near-miss must not be overstated as evidence for either `21` or `22`.

## what_verify_should_check
- Recheck every inherited literature-bound dependency that turns a `K21` witness into the exact value `22`.
- If a witness is found, independently verify the coloring and every forbidden-subgraph claim.
- If only structural reductions are obtained, verify that no step accidentally assumes a sharper threshold than what is written here.
