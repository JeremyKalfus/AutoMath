# Solve Record: The Exact Value of R(K4-e, K4-e, K4-e; 3)

## statement_lock
Active slug: `r-k4e-k4e-k4e-three-uniform-hypergraph-ramsey`.

Active title: `Determine the exact value of R(K4-e, K4-e, K4-e; 3)`.

Exact intended statement for this solve run: determine whether every 3-coloring of the triples of a 13-element set contains a monochromatic 3-uniform `K4-e`, equivalently whether `R(K4-e, K4-e, K4-e; 3)` is `13` or `14`.

Working title theorem if the solve closes: `The Exact Value of R(K4-e, K4-e, K4-e; 3)`.

Publication target assessment up front: yes, a successful exact solve here would already be about `0.81` of a paper, because the current frontier is already a one-step interval and the remaining packaging would be short context, a compact main proof or construction, and a brief neighboring-case discussion.

## definitions
Interpret `K4-e` as the 3-uniform hypergraph on 4 vertices with exactly 3 of the 4 possible triples present.

Thus a 3-coloring of `([n] choose 3)` avoids monochromatic `K4-e` iff on every 4-set, no color appears on 3 or 4 of its 4 triples.

Equivalently, on each 4-set the color-multiplicity pattern must be either `2,1,1` or `2,2,0`.

Immediate local reformulation: fixing a vertex `v`, the color classes in the link graph on `V \\ {v}` must each be triangle-free, since a monochromatic triangle in a color-`c` link would already give 3 color-`c` triples through `v`, i.e. a monochromatic `K4-e`.

Ambiguities and conventions:
- I treat the 2021 upper bound `R(K4-e, K4-e, K4-e; 3) <= 14` as input, not something to reprove here.
- Solve-stage scope is only the endpoint `13` versus `14`; no wider family claims are assumed.
- Because solve runs with web disabled, any novelty judgment here is provisional and only about theorem-shape, not prior-art clearance.

## approach_A
Structural / invariant route.

1. Assume a 13-vertex coloring with no monochromatic `K4-e`.
2. Use the 4-set reformulation: every 4-set has pattern `2,1,1` or `2,2,0`.
3. For each vertex `v`, analyze the induced 3-coloring of the link `K12`; each color class is triangle-free.
4. Try to combine local triangle-free link constraints with pair-count constraints to force a contradiction on 13 vertices.

Promising ingredients:
- Every pair `{u,v}` lies in 11 colored triples, so one color appears at least 4 times on triples containing `{u,v}`.
- If a fixed pair `{u,v}` has many third vertices in one color, then among those third vertices the two corresponding link graphs at `u` and `v` must suppress that color heavily, because any pair of such third vertices would otherwise complete a monochromatic `K4-e`.
- This creates a tension between large pair-neighborhoods in one color and triangle-free link-graph density bounds.

Current weakness:
- The local constraints are strong, but I do not yet have a clean contradiction that closes 13 directly from counting alone.

Self-check after approach A: this is theorem-facing and not search-first, but at the moment it produces necessary structure rather than a full proof.

## approach_B
Construction / extremal route.

1. Try to realize a 13-vertex extremal coloring explicitly.
2. The most natural compact ansatz is a cyclic coloring on `Z/13Z`, because `13` is prime and the candidate lower-bound endpoint is a single-vertex lift over the known `12`-vertex existence range.
3. Translation symmetry collapses the triple set into only `286 / 13 = 22` orbit-types, so the problem becomes a finite constraint system on 22 variables rather than 286.
4. If a cyclic witness exists, that would settle the exact value at `14`. If no cyclic witness exists, that is still a meaningful structural obstruction and a candidate theorem slice about extremal symmetry.

Why this is a justified narrow computation rather than a broad brute-force solve:
- it is a symmetry-restricted ansatz,
- it directly tests the most natural compact witness shape for the `13` endpoint,
- and it becomes appropriate only after the two reasoning paths above expose the local forbidden-pattern structure.

Self-check after approach B: this does not prove the full theorem by itself unless a valid 13-vertex coloring is found, but it can sharply clarify whether the remaining endpoint plausibly comes from a small symmetric construction.

## lemma_graph
Lemma 1. A coloring avoids monochromatic `K4-e` iff every 4-set has color multiplicities `2,1,1` or `2,2,0`.

Lemma 2. For any vertex `v` and color `c`, the color-`c` link graph `L_v^c` on the other 12 vertices is triangle-free.

Lemma 3. For any pair `{u,v}` and color `c`, if `S_c(u,v) = {x : uvx has color c}`, then for every distinct `x,y` in `S_c(u,v)`, at most one of `uxy` and `vxy` can have color `c`.

Proof skeleton candidate if the main claim closes:
- either prove nonexistence of a 13-vertex coloring by pushing Lemmas 1 to 3 into a global contradiction,
- or exhibit a 13-vertex witness and then verify Lemma 1 directly on every 4-set.

## chosen_plan
Best path for this run:

1. Keep the structural contradiction route active as the paper-shaped ideal.
2. Use a very small exact search only on the cyclic `Z/13Z` ansatz, because that is the cleanest candidate construction family and the smallest bounded experiment likely to move the endpoint materially.
3. If the cyclic search fails, record that as a real obstruction but not as a full solve.
4. If the cyclic search succeeds, validate the witness and upgrade the result to a genuine exact-endpoint candidate (`14`).

Self-check: this plan stays inside the one-shot lane. It does not switch to a broad computational campaign; it asks one sharply bounded question that directly bears on the endpoint.

## self_checks
- Statement lock is exact: the only unresolved endpoint is `13` versus `14`.
- The reasoning so far keeps theorem shape in view rather than chasing an arbitrary instance.
- Code is now justified: both reasoning paths produced real structure but did not close the unrestricted 13-vertex case, so a narrow symmetry-restricted exact check is within policy.
- The bounded computation must be treated as a slice result unless it is upgraded to the unrestricted problem, which it is not.

## code_used
Yes, but only in a narrowly justified form.

Helper file: `artifacts/r-k4e-k4e-k4e-three-uniform-hypergraph-ramsey/cyclic_search.py`.

What it does:
- imposes full translation invariance on a hypothetical coloring of triples of `Z/13Z`,
- reduces the coloring to `22` triple-orbit variables,
- induces `55` translation-orbit constraints from 4-sets,
- and runs exact backtracking to forbid any constraint where one color appears on at least 3 of the 4 triples of a 4-set.

Outcome:
- the search returned `NO_CYCLIC_SOLUTION`,
- and an independent rerun with a separate inline backtracking routine reproduced the same negative answer.

Self-check:
- this is not a full search over all 13-vertex colorings,
- but it is an exact finite verification of the cyclic ansatz obstruction.

## result
Main theorem status: unresolved. I did not prove `R(K4-e, K4-e, K4-e; 3) = 13`, and I did not find a 13-vertex witness proving `R(K4-e, K4-e, K4-e; 3) = 14`.

Strong partial result obtained:

`No translation-invariant 3-coloring of the triples of Z/13Z avoids a monochromatic 3-uniform K4-e.`

Equivalent formulation:
- there is no cyclic 13-vertex coloring whose color depends only on the translation orbit of a triple and which avoids monochromatic `K4-e` on every 4-set.

Why this matters:
- it removes the cleanest compact witness family for the `14` endpoint,
- so any 13-vertex extremal coloring, if it exists at all, must break full cyclic symmetry.

Immediate corollary / boundary remark:
- the most natural `13`-vertex compact-construction route is blocked; an unrestricted `13`-vertex witness would need genuinely asymmetric or lower-symmetry structure.

Self-check after the result:
- this is mathematically real and exactly checked inside the cyclic ansatz,
- but it does not settle the unrestricted endpoint, so the overall solve classification must remain below `CANDIDATE` for the main theorem.

## family_affinity
High affinity with finite exact Ramsey-endpoint notes for small 3-uniform hypergraphs. The nearest family connection is the Lidicky-Pfender neighboring exact case `R(K4-e, K5; 3) = 12`, where a finite local obstruction package already behaves like a short-note theorem.

## generalization_signal
Moderate. The link-graph and pair-neighborhood constraints should generalize to other `R(K4-e, H; 3)` endpoint problems, and the symmetry-obstruction workflow should transfer to other one-step exact Ramsey gaps. The exact `Z/13Z` no-go statement itself is still instance-specific.

## proof_template_reuse
Likely reusable template:
- convert forbidden monochromatic 3-graph patterns into color-pattern restrictions on 4-sets,
- pass to triangle-free link graphs,
- isolate extremal candidate symmetries,
- then either complete a contradiction or verify a compact witness.

What scales:
- the 4-set reformulation,
- the triangle-free link method,
- and the tactic of exhausting the smallest high-symmetry witness class before spending effort on unrestricted search.

What does not scale cleanly:
- the exact orbit search is tied to the specific group action on `13` vertices,
- and by itself it does not say much about asymmetric extremals.

## candidate_theorem_slice
Candidate slice now supported by exact finite search:

`No translation-invariant 3-coloring of the triples of a 13-element cyclic group avoids a monochromatic 3-uniform K4-e.`

This is theorem-shaped and directly relevant to the endpoint, but it is still a supporting slice rather than the publication target itself.

## smallest_param_shift_to_test
The first parameter shift to test after the main endpoint is the symmetry shift rather than the vertex count:
- cyclic `13`-vertex ansatz versus unrestricted `13`-vertex colorings.

The next one or two parameter shifts that would help most now are:
- unrestricted `13`-vertex colorings with only a smaller automorphism assumption,
- or structural forcing on `13` built from the triangle-free link constraints without any symmetry assumption.

If the main claim later closes positively at `14`, the next useful shift is whether the obstruction at `13` can be upgraded from full cyclic symmetry-breaking to a complete nonexistence proof.

## why_this_is_or_is_not_publishable
If the full endpoint closes, it is publishable in the micro-paper lane: the title theorem is exact, the literature gap is one step, and the remaining packaging is small.

Current run outcome: still too thin for the micro-paper lane.

Reason:
- the cyclic no-go statement is a genuine supporting slice,
- but the title theorem remains open,
- so the package is not yet the `70-90% of a paper` target promised by the selected candidate.

Minimal remaining packaging work if the endpoint later closes:
- write the unrestricted proof or exhibit the unrestricted witness,
- keep the cyclic obstruction as a short structural remark,
- then add only the usual front-matter and verification layer.

## paper_shape_support
What would make the result paper-shaped if the main claim closes:
- the exact endpoint `13` or `14`,
- one compact proof or witness verification,
- one immediate boundary remark: e.g. the role of cyclic symmetry either as a successful witness family or as a ruled-out extremal shape,
- and a short comparison to the 2021 one-step interval.

Minimal remaining packaging work after a successful solve:
- formal proof cleanup,
- a short background paragraph around the known `13 <= R <= 14` interval,
- one figure or compact table for the witness/forbidden local traces if useful.

Current best paper-shape support from this run:
- a ready-made boundary remark that any 13-vertex witness must break cyclic symmetry,
- plus a concrete theorem slice that could appear as a proposition or appendix computation inside a full endpoint paper.

## boundary_remark
Natural immediate remark if a 13-vertex witness is found: the endpoint is attained by an extremal coloring already visible at a compact symmetry level, so the whole paper becomes an exact witness note.

Natural immediate remark if 13 is ruled out: the one-step gap collapses upward from the current lower bound, and the 2021 upper bound is sharp.

Boundary remark actually earned in this run:
- full cyclic symmetry is already too rigid at `n = 13`, so any surviving extremal construction would have to come from a more delicate configuration class.

## likely_failure_points
- The structural counting route may need one ingredient from the 2021 SDP certificate that is not present in the local packet.
- A cyclic ansatz may fail even if an unrestricted 13-vertex witness exists, so a negative cyclic result would not settle the theorem.
- Any positive computational witness must still be checked carefully on all 4-sets; otherwise it is not mathematically usable.
- There may still exist a low-symmetry witness on 13 vertices, so the current obstruction cannot be overread as evidence for `R = 13` beyond a heuristic nudge.

## what_verify_should_check
- If a 13-vertex witness is found: exact 4-set verification, isomorphism simplification, and bounded prior-art confirmation that the endpoint was not already published.
- If only a cyclic no-go statement is found: independent rerun of the orbit-level exact search, confirmation that the encoding matches the `K4-e` condition exactly, and confirmation that the translation action on triples indeed yields the `22` orbit variables and `55` distinct 4-set orbit constraints used here.
