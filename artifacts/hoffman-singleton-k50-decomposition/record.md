# statement_lock

- Active slug: `hoffman-singleton-k50-decomposition`
- Active title: `Does K_50 decompose into 7 copies of the Hoffman-Singleton graph?`
- Exact intended theorem: `Either K_50 admits an edge decomposition into seven Hoffman-Singleton graphs, or no such decomposition exists.`
- Title theorem if closed: `K_50 does (or does not) decompose into seven copies of the Hoffman-Singleton graph.`
- Paper leverage if closed: a successful exact solve would still be about `0.82` of a short paper, because the title theorem, certificate format, and comparison point from the known five-copy packing are already fixed.
- Minimal remaining packaging work after a full solve: present the five-copy precursor briefly, give the exact completion or obstruction certificate, and add a short verification appendix.

Self-check: the target is locked as a yes/no theorem, not as a looser search for one more packing or an ad hoc witness.

# definitions

- Model the desired decomposition as an edge-coloring of `K_50` by colors `1,...,7`, where color class `H_i` is a Hoffman-Singleton graph for each `i`.
- Each `H_i` is strongly regular with parameters `(50,7,0,1)`. I use only the consequences `7`-regular, triangle-free (`lambda = 0`), and every nonedge having a unique common neighbor (`mu = 1`).
- For a fixed vertex `v`, define `B_i := N_{H_i}(v)`. Then the `B_i` partition `V(K_50) \ {v}` into seven sets of size `7`.

Ambiguities / missing inputs:

- The working packet states that a five-copy packing is known, but this solve packet does not include the explicit packing or the explicit `14`-regular residue.
- Because the concrete residue is absent, a final completion-or-obstruction argument cannot honestly be closed from the local data alone.
- Color labels are arbitrary; all statements below are invariant under permuting the seven color classes.

Self-check: every later claim is written only in terms of the decomposition itself and does not assume any unavailable certificate for the known five-copy packing.

# approach_A

Structural / invariant route: force as much as possible from the local `(50,7,0,1)` structure before considering any search.

Proposition A1. Assume `K_50` decomposes into seven Hoffman-Singleton color classes `H_1,...,H_7`. Fix a vertex `v` and write `B_i = N_{H_i}(v)`.

Then:

1. `V(K_50) \ {v} = B_1 \sqcup ... \sqcup B_7` with `|B_i| = 7`.
2. `B_i` is independent in `H_i`.
3. For each distinct `i,j`, the `H_i`-edges between `B_i` and `B_j` form a perfect matching.
4. For each distinct `i,j`, the `H_j`-edges between `B_i` and `B_j` also form a perfect matching.
5. Consequently, every `x in B_i` has exactly one `H_i`-neighbor in each block `B_j` with `j != i`, and no `H_i`-neighbor inside `B_i`.

Proof sketch:

- Items `1` and `2` are immediate: each color class is `7`-regular, and if two vertices of `B_i` were adjacent in `H_i`, then together with `v` they would form a triangle in `H_i`, contradicting `lambda = 0`.
- For item `3`, fix `i != j` and a vertex `y in B_j`. Since `v` and `y` are nonadjacent in `H_i`, the `mu = 1` property in `H_i` gives a unique common `H_i`-neighbor of `v` and `y`. That common neighbor lies in `B_i`, so `y` has exactly one `H_i`-neighbor in `B_i`. Applying this to all `y in B_j` gives a perfect matching from `B_j` into `B_i`.
- Item `4` is the same argument with the roles of `i` and `j` reversed.
- Item `5` follows because the perfect matching in item `3` gives each `x in B_i` exactly one `H_i`-neighbor in every `B_j`, `j != i`, accounting for all six `H_i`-neighbors of `x` other than `v`.

This already forces a rigid vertex-centered `7 x 7` block system around every vertex. Any valid completion of a known five-copy packing must realize this structure inside the final two missing color classes.

Self-check: Proposition A1 uses only the Hoffman-Singleton parameter set and is rigorous. It does not depend on a guessed explicit model.

Proposition A2. In any such decomposition, every edge of `K_50` lies in exactly `30` rainbow triangles.

More precisely, if `uv` has color `c`, then among the `48` third vertices `w`:

- exactly `6` satisfy `col(u,w) = col(v,w) = a` for some `a != c`,
- exactly `12` satisfy that exactly one of `col(u,w), col(v,w)` equals `c`,
- the remaining exactly `30` give triangles with three distinct colors.

Proof sketch:

- For each `a != c`, the vertices `u` and `v` are nonadjacent in `H_a`, so `mu = 1` in `H_a` gives exactly one vertex `w` with both `uw` and `vw` colored `a`. This contributes `6` vertices.
- In `H_c`, both `u` and `v` have degree `7`, and because `H_c` is triangle-free they have no common `H_c`-neighbor. So aside from the edge `uv`, the remaining `H_c`-neighbors of `u` and of `v` contribute `6 + 6 = 12` distinct third vertices for which exactly one of the two incident colors is `c`.
- The remaining `48 - 6 - 12 = 30` third vertices use neither repeated non-`c` color nor repeated color `c`, so their triangles are rainbow.

The exact split `30/18` between rainbow and non-rainbow triangles is a strong local certificate that any explicit candidate decomposition must satisfy edge-by-edge.

Self-check: the `30` count is forced and exact; no unproved uniformity assumption on the non-rainbow color distribution is being smuggled in.

# approach_B

Construction / extremal / contradiction route: reduce the problem to the final two copies over the known five-copy packing and ask whether the `14`-regular residue can split into two Hoffman-Singleton graphs.

Reasoning:

- A five-copy packing leaves a spanning `14`-regular residual graph `R`.
- Closing the main theorem is equivalent to proving `R = H_6 \sqcup H_7` with both summands Hoffman-Singleton, or proving that no such split exists.
- By Proposition A1, if such a split exists, then for every vertex `v` the `14` neighbors of `v` in `R` must split into two `7`-sets whose cross-block interactions satisfy the same unique-common-neighbor and perfect-matching constraints forced by `(50,7,0,1)`.
- By Proposition A2, every edge of `R` in a hypothetical completion inherits the exact local triangle profile forced by the missing color labels.

Why this route stalls here:

- The explicit residual graph `R` is not present in the solve packet.
- Without `R`, an impossibility proof cannot be honest, because the obstruction would have to use actual adjacency data, not only abstract counting.
- Without `R`, a constructive completion also cannot be honest, because the last two colors are not anchored to a concrete certificate.

So the contradiction route identifies the right reduced object, but it cannot be finished from the bounded local file set supplied to this solve run.

Self-check: this is a genuine reduction, not a silent fallback. The blockage is the missing concrete residue, not a change of objective.

# lemma_graph

1. Full decomposition of `K_50` into seven Hoffman-Singleton graphs
2. Fix a vertex `v` and partition `V \ {v}` into the seven color neighborhoods `B_i`
3. Use `lambda = 0` to show each `B_i` is independent in its own color
4. Use `mu = 1` to force, for every `i != j`, perfect matchings of color `i` and of color `j` between `B_i` and `B_j`
5. Deduce the local `7 x 7` block system around each vertex
6. Use the same `lambda / mu` split to count third vertices around an edge and obtain the `30` rainbow triangle count
7. Apply these constraints to the missing two-color residue of any five-copy packing
8. Exact closure now requires the explicit residual graph, not just the abstract packet

Self-check: the lemma graph is logically linear and every edge in it is justified by a previously stated property.

# chosen_plan

Best path for this run: push the structural route until it yields a rigorous theorem slice, then stop conservatively rather than inventing a construction or obstruction without the actual five-copy residue.

Reason for choosing this path:

- It is the only route that produces honest mathematics from the available file scope.
- It keeps the MICRO-PAPER objective visible by extracting the smallest theorem-facing support that would materially help a later exact completion.
- It avoids premature code or brute-force search on an unspecified residual graph.

Self-check: this plan is aligned with solve-stage rules and does not overclaim.

# self_checks

- Statement lock check: the target stayed a yes/no decomposition theorem throughout.
- Definition check: only standard Hoffman-Singleton consequences were used.
- Structural check: Proposition A1 is exact and fully local.
- Counting check: Proposition A2 uses a complete partition of the `48` third vertices.
- Scope check: no web, no Lean, no external packet expansion, no speculative certificate.
- Publication check: current output is theorem-facing but still not enough for a paper packet by itself.

# code_used

No code used.

Reason:

- The working packet does not include the explicit five-copy packing or the explicit `14`-regular residual graph.
- Without a concrete target graph, any search would be premature and would violate the reasoning-first constraint.
- A bounded checker would become justified only after the manager provides an explicit packing certificate or residual adjacency list.

Self-check: code abstention is deliberate rather than accidental.

# result

Strongest honest result of this solve run:

- I did not close the main decomposition or impossibility theorem.
- I did prove a rigorous local theorem slice that any future exact solution must satisfy.

Candidate slice:

`If K_50 decomposes into seven Hoffman-Singleton graphs, then around every vertex the seven color neighborhoods form a rigid 7-by-7 block system, with perfect matchings in each of the two corresponding colors between every pair of blocks; moreover every edge lies in exactly 30 rainbow triangles.`

What part of the argument scales:

- The vertex-neighborhood partition and perfect-matching forcing scale to any hypothetical decomposition of `K_{d^2+1}` into `d` copies of a triangle-free Moore graph of degree `d`.
- The rainbow-triangle counting argument scales wherever `lambda = 0` and `mu = 1` are available.

What part does not scale:

- Turning the local block system into a global completion or obstruction depends on the actual residual graph, not just the parameter set.
- The exceptional rigidity of the Hoffman-Singleton graph may matter globally in ways not visible from local counting alone.

What theorem slice is suggested:

- A standalone structural proposition about any Hoffman-Singleton decomposition of `K_50`: local block matchings plus the forced edge-triangle profile.

What next parameter shifts would help most:

- First: obtain the concrete `14`-regular residue coming from the known five-copy packing and test whether even one Hoffman-Singleton spanning subgraph sits inside it.
- Second: study the simpler analogue `K_10` into three Petersen graphs as a sanity model for how the local block system globalizes in a known Moore-graph decomposition.

Current package assessment:

- This is still an instance-level structural slice, not yet a paper-shaped exact theorem.

Self-check: the result section states precisely what is proved and what is not.

# family_affinity

High.

This problem sits in the narrow family of exceptional Moore-graph decompositions and complete-graph edge-colorings whose color classes are strongly regular with parameters `(50,7,0,1)`. The cleanest nearby analogy is the Petersen decomposition of `K_10`, where a small Moore graph really does tile the ambient complete graph. That makes the present target feel like a natural exceptional-family theorem rather than an isolated curiosity.

# generalization_signal

Moderate but conditional.

The proof template extracted here is not specific to `50` except for the Moore-graph numerology. It suggests a general local statement for any hypothetical decomposition of `K_{d^2+1}` into `d` triangle-free Moore graphs of degree `d`. In practice, that family is tiny, so the reusable value is more in the proof method than in a large parameter family.

# proof_template_reuse

Reusable template:

1. Convert the decomposition claim into an edge-coloring whose color classes are strongly regular.
2. Freeze one vertex and partition the remaining vertices by color-neighborhood.
3. Use `mu = 1` to force perfect matchings between the corresponding blocks.
4. Use `lambda = 0` to forbid within-block edges in the matching color and to count edge-centered triangle types.
5. Push the resulting local incidence constraints against the actual residual graph.

This template should transfer directly to any later exact check of a concrete two-color residue for this same slug.

# candidate_theorem_slice

Proposed exact theorem slice:

`Let H_1,...,H_7 be edge-disjoint Hoffman-Singleton graphs whose union is K_50. For any vertex v and the induced partition B_i = N_{H_i}(v), each pair B_i,B_j supports a perfect matching of H_i-edges and a perfect matching of H_j-edges, and every edge of K_50 lies in exactly 30 rainbow triangles with respect to the seven-color decomposition.`

Why this is the right slice:

- It is exact.
- It is nontrivial.
- It would be part of any eventual proof or certificate check.
- It is still subordinate to the title theorem rather than drifting into a different program.

# smallest_param_shift_to_test

Best immediate shift:

- Replace the abstract missing residue by the concrete residue from the known five-copy packing and test whether it contains one Hoffman-Singleton spanning subgraph.

Best sanity-model shift:

- Rehearse the same neighborhood-partition argument on the known decomposition of `K_10` into Petersen graphs, to see exactly which local constraints are enough to globalize in the smaller Moore-graph case.

# why_this_is_or_is_not_publishable

Not publishable yet.

Why not:

- The main title theorem is still unsettled.
- The current packet does not contain the explicit five-copy residue, so the structural slice cannot yet be turned into a completion theorem or an impossibility theorem.
- The present output would read as a supporting lemma section, not as the paper's central result.

If the main claim closes, then yes, the solve would still be around `70-90%` of a paper.

Current micro-paper-lane judgment:

- Still too thin on its own for the micro-paper lane.
- Strong enough to justify `SLICE_CANDIDATE` as a publication-facing status, because a real theorem slice is now visible.

# paper_shape_support

What extra structure would make the result paper-shaped if the main claim closes:

- an explicit final two-color completion of the known five-copy packing, or
- a clean obstruction theorem for the actual `14`-regular residue.

Smallest supporting structure needed beyond the main claim:

- Proposition A1 as a local constraint lemma,
- Proposition A2 as a short corollary / certificate check,
- one paragraph explaining how the known five-copy packing reduces the problem to a `14`-regular residue,
- one compact machine-checkable certificate if the outcome is constructive.

Immediate corollary or remark that naturally falls out:

- Any successful completion of the five-copy packing is highly non-generic: every edge in the completed decomposition must have the forced `30`-rainbow-triangle profile, so arbitrary `14`-regular residues cannot serve as candidates.

# boundary_remark

Boundary remark:

The current structural slice lives exactly at the boundary between a genuine theorem ingredient and a complete paper result. It says something rigid and checkable about any hypothetical decomposition, but it does not yet distinguish existence from nonexistence. That is the right stopping point for solve when the concrete residual graph is absent.

# likely_failure_points

- The local block constraints may still admit multiple incompatible global completions.
- A final obstruction, if true, is likely to depend on the explicit geometry of the five-copy residue rather than on parameter counting alone.
- A constructive solve, if true, may require an explicit coordinate model of the Hoffman-Singleton graph or of the known five-copy packing, neither of which is present in the current bounded file set.
- There is a real risk that the exact problem is solved only by a concrete certificate rather than by a short conceptual obstruction.

# what_verify_should_check

- If a future completion is proposed, check that each color class is exactly Hoffman-Singleton: `50` vertices, `175` edges, `7`-regular, triangle-free, and every nonedge has a unique common neighbor.
- Check that the seven color classes partition all `1225` edges of `K_50` with no overlap.
- Check the local block-matching lemma from Proposition A1 on at least one vertex and, preferably, on all vertices by automation.
- Check the `30`-rainbow-triangle edge profile from Proposition A2 as a fast certificate sanity test.
- If a future obstruction is proposed, confirm that it uses the actual five-copy residue rather than only parameter heuristics.
- During verification, perform the bounded prior-art search for the exact yes/no claim; solve itself has not done that.
