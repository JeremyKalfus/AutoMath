# Solve Record: The Exact Value of R(B16, B16)

## statement_lock
We work with the standard book graph definition: `B16` is the graph of 16 triangles sharing a common spine edge. Thus a graph `G` contains `B16` iff some edge of `G` has at least 16 common neighbors.

The exact intended statement for this solve run is:

- either prove that every graph `G` on 65 vertices has an edge with at least 16 common neighbors or a nonedge with at least 16 common nonneighbors, yielding `R(B16, B16) = 65`;
- or produce a graph `G` on 65 vertices in which every edge has at most 15 common neighbors and every nonedge has at most 15 common nonneighbors, yielding `R(B16, B16) = 66`.

If this closes, the honest title theorem is still exactly:

- `The Exact Value of R(B16, B16)`.

This is still a genuine micro-paper target: a successful closure would already be about `82%` of a paper packet, with only light comparison-to-table exposition left.

## definitions
Write `n = 65`, `e = e(G)`, `T = t(G)`, and `\bar T = t(\bar G)`.

For vertices `u,v`:

- if `uv` is an edge, let `c_G(u,v) = |N(u) ∩ N(v)|`; then `G` avoids `B16` iff `c_G(u,v) <= 15` for every edge `uv`;
- if `uv` is a nonedge, then `\bar G` avoids `B16` iff `u,v` have at most 15 common neighbors in `\bar G`, equivalently at most 15 common nonneighbors in `G`.

I will use Goodman's identity in the form

`T + \bar T = C(65,3) - (1/2) * Σ_v d(v)(64 - d(v))`.

Numerically:

- `C(65,2) = 2080`;
- `C(65,3) = 43680`.

## approach_A
Structural / invariant approach.

Assume a 65-vertex witness `G` exists with no `B16` in either color. Then:

1. Every edge lies in at most 15 triangles, so `3T <= 15e`, hence `T <= 5e`.
2. Every edge of `\bar G` also lies in at most 15 triangles of `\bar G`, so `\bar T <= 5\bar e`.
3. Therefore
   `T + \bar T <= 5(e + \bar e) = 5*C(65,2) = 10400`.
4. Goodman then gives
   `43680 - (1/2) * Σ_v d(v)(64 - d(v)) <= 10400`,
   so
   `Σ_v d(v)(64 - d(v)) >= 66560`.
5. But `d(64-d) <= 32^2 = 1024` for every degree `d`, with equality only at `d = 32`.
6. Since there are 65 vertices,
   `Σ_v d(v)(64 - d(v)) <= 65 * 1024 = 66560`.

Hence equality is forced everywhere. So any 65-vertex witness must satisfy:

- every vertex has degree exactly 32;
- every edge lies in exactly 15 triangles;
- every edge of the complement lies in exactly 15 triangles of the complement.

Now let `u,v` be a nonedge of `G`. Because `d(u) = d(v) = 32`, if `c = |N(u) ∩ N(v)|`, then

- `|N(u) ∪ N(v)| = 64 - c`;
- among the remaining 63 vertices, the number adjacent to neither `u` nor `v` is
  `63 - (64 - c) = c - 1`.

But this is exactly the number of common neighbors of `u,v` in `\bar G`, so `c - 1 = 15`, hence `c = 16`.

Therefore any 65-vertex witness must be a strongly regular graph with parameters

- `srg(65,32,15,16)`.

Conversely, any `srg(65,32,15,16)` is automatically a 65-vertex witness, because adjacent pairs have exactly 15 common neighbors and nonadjacent pairs have exactly 15 common nonneighbors.

So the exact-value problem reduces cleanly to:

- does an `srg(65,32,15,16)` exist?

Self-check after Approach A:

- The reduction is exact, not heuristic.
- No code was needed.
- The only nontrivial ingredient used is Goodman plus the sharp triangle-cap saturation.
- This does not settle `R(B16,B16)` by itself; it converts the Ramsey gap into a conference-graph existence question.

## approach_B
Construction / extremal / contradiction approach.

Take a hypothetical 65-vertex witness `G` and inspect the local partition around one vertex `v`.

Let

- `A = N(v)`, so `|A| = 32`;
- `B = V(G) \ (A ∪ {v})`, so `|B| = 32`.

From the exact equalities forced in Approach A:

- for each `x in A`, the edge `vx` has exactly 15 common neighbors, so `x` has exactly 15 neighbors inside `A`, hence exactly 16 neighbors in `B`;
- for each `y in B`, the nonedge `vy` has exactly 15 common nonneighbors, so `y` has exactly 16 neighbors inside `B`, hence exactly 16 neighbors in `A`.

Thus every local view has the rigid form:

- `G[A]` is 15-regular on 32 vertices;
- `G[B]` is 16-regular on 32 vertices;
- the bipartite graph between `A` and `B` is 16-regular on both sides.

So a witness is much more rigid than an arbitrary 65-vertex graph; it is a globally balanced object with tightly prescribed local degree splits, not a generic extremal graph.

This suggests a concrete contradiction route:

1. Start from any candidate 64-vertex lower-bound template from the literature.
2. Try to add one vertex while preserving the forced 32/15/16 local profile.
3. Show that every attempted extension violates one of the exact intersection conditions.

The difficulty is that I do not have the explicit published 64-vertex template inside the current allowed local scope, so this route does not close here.

Self-check after Approach B:

- This route is structurally plausible and aligned with the packet's recommended first attack.
- Without the explicit candidate-local template, it remains only a proof program, not a completed argument.
- The rigid local degree split is correct and is a useful invariant to hand to a later solver or verifier.

## lemma_graph
Minimal proof skeleton obtained in this run:

1. `B16`-avoidance is equivalent to the edge codegree bound `c_G(u,v) <= 15`.
2. Two-color `B16`-avoidance on 65 vertices implies
   `T <= 5e` and `\bar T <= 5\bar e`.
3. Combine with Goodman to force
   `Σ_v d(v)(64-d(v)) = 65 * 32^2`.
4. Therefore `G` is 32-regular and both color triangle bounds are saturated edgewise.
5. Hence every edge has exactly 15 common neighbors and every nonedge has exactly 15 common nonneighbors.
6. Therefore every nonedge has exactly 16 common neighbors.
7. So any 65-vertex witness is exactly an `srg(65,32,15,16)`.
8. Conversely any `srg(65,32,15,16)` is a 65-vertex witness.

This yields the exact equivalence:

- `R(B16, B16) = 66` iff an `srg(65,32,15,16)` exists;
- `R(B16, B16) = 65` iff no such graph exists.

## chosen_plan
The best current path is Approach A.

Reason:

- it gives a rigorous theorem-shaped reduction immediately;
- it isolates the exact obstruction to finishing the instance;
- it materially shortens solve-to-publication distance if later work can prove existence or nonexistence of the forced conference graph.

I am not turning on Lean here. The result is not exact yet, and the best mathematical gain available in this run is the reduction theorem rather than formalization.

## self_checks
- Statement lock check: the solve target stayed fixed at the exact 65-versus-66 diagonal problem; no concept drift occurred.
- Scope check: only the active packet, working packet, and local artifact outputs were used.
- Proof check: every equality claim in the main reduction comes from a forced extremal equality, not from an unproved regularity guess.
- Publication check: the current result is theorem-shaped but still one step short of the title theorem.

## code_used
No code used.

Reason:

- the Goodman saturation argument already yields the strongest clean structural progress available from the local packet;
- any computation worth doing next would be a template-specific extension test or a bounded search inside a named construction family, and that requires a more explicit candidate template than I currently have in scope.

## result
Main outcome of this solve run:

- I did not determine whether `R(B16, B16)` is 65 or 66.
- I proved a sharp reduction: any 65-vertex witness avoiding `B16` in both colors must be an `srg(65,32,15,16)`, and conversely any `srg(65,32,15,16)` would prove `R(B16, B16) = 66`.

So the active instance is now compressed to a clean existence/nonexistence question for a conference graph:

- `R(B16, B16) = 66` iff there exists a conference graph on 65 vertices;
- otherwise `R(B16, B16) = 65`.

What extra structure would make the result paper-shaped if the main claim closes?

- one exact existence or nonexistence proof for `srg(65,32,15,16)`;
- one short argument connecting that structural fact back to the Ramsey statement;
- one immediate table-update corollary.

Immediate corollary / boundary remark already visible:

- any putative 65-vertex extremal graph is forced to be perfectly balanced and strongly regular, so there is no room for an irregular ad hoc counterexample.

Self-check after result:

- This is a real structural theorem slice.
- It is still too thin to count as a micro-paper win by itself.
- It meaningfully narrows the final step.

## family_affinity
High.

This reduction is not an isolated curiosity. It sits exactly at the diagonal one-gap regime `4n+1 <= R(Bn, Bn) <= 4n+2`, where a witness on `4n+1` vertices must saturate both color triangle bounds simultaneously. That is a natural family-level structural phenomenon.

## generalization_signal
Strong.

The same proof gives the following family statement:

- if a graph `G` on `4n+1` vertices avoids `Bn` in both `G` and `\bar G`, then `G` must be `srg(4n+1, 2n, n-1, n)`.

Equivalently, in the diagonal one-gap regime the lower-end witness problem reduces to the existence of a conference graph.

What scales:

- the Goodman saturation argument;
- the forced regularity at degree `2n`;
- the reduction from a Ramsey witness to a conference graph.

What does not yet scale:

- existence or nonexistence of the resulting conference graph is a separate problem and may depend heavily on `n`.

## proof_template_reuse
High reuse potential.

Template:

1. translate book avoidance into edge codegree caps;
2. sum triangle bounds in both colors;
3. invoke Goodman;
4. force equality in the quadratic degree bound;
5. extract a strongly regular graph parameter set.

This template should be reusable for other diagonal one-gap book residues such as `n = 11` or `n = 21`.

## candidate_theorem_slice
Candidate theorem slice:

- `Any graph on 65 vertices with no B16 in either the graph or its complement is strongly regular with parameters (65,32,15,16).`

Family-level variant:

- `Any graph on 4n+1 vertices with no Bn in either color is strongly regular with parameters (4n+1,2n,n-1,n).`

This is the smallest honest supporting theorem visible in the current run.

## smallest_param_shift_to_test
Best next parameter shifts:

- `n = 11`: test whether the same reduction isolates `srg(45,22,10,11)` as the exact lower-end witness problem;
- `n = 21`: test whether it isolates `srg(85,42,20,21)`.

Those are the nearest diagonal residues in the same one-gap family, and checking them would tell us whether this conference-graph reduction is systematically useful or only an `n = 16` accident.

## why_this_is_or_is_not_publishable
Current package is not yet publishable as a standalone micro-paper result.

Why not:

- it does not close the exact value of `R(B16, B16)`;
- the main new content is a structural reduction, not the title theorem;
- the remaining step, existence or nonexistence of `srg(65,32,15,16)`, is still load-bearing.

If the main claim closes, then yes: the package would already be about `70-90%` of a paper.

Minimal remaining packaging work after a closure:

- short introduction placing `n = 16` among the diagonal one-gap cases;
- one proof section for the exact closure;
- one short section recording the conference-graph reduction and the resulting table update.

At the current stage, the package is still too thin for the micro-paper lane.

## paper_shape_support
If a solve closes the main claim, the paper shape is immediate:

- title theorem: `The Exact Value of R(B16, B16)`;
- supporting theorem slice: the forced `srg(65,32,15,16)` reduction;
- natural corollary: the diagonal table entry for `R(B16, B16)` is updated from `65 <= R <= 66` to an exact value.

This run therefore supports paper shape, but does not yet complete it.

## boundary_remark
Boundary remark:

- the `n = 16` case sits exactly at the point where the standard number-theoretic criteria stop, but the combinatorial extremal witness, if it exists at all, cannot be messy; it must be a conference graph with the tight parameter set `(65,32,15,16)`.

That makes the instance matter: the Ramsey residue is equivalent to a sharply structured existence question rather than to an unrestricted search over 65-vertex graphs.

## likely_failure_points
- The conference-graph reduction may already be folklore in the diagonal book-Ramsey literature; solve cannot check that because web is off and no local source text is in scope.
- The local partition note in Approach B is suggestive but not yet a contradiction proof.
- A later stage may find that `srg(65,32,15,16)` existence is already known one way or the other, in which case this solve artifact is still useful but not frontier-closing.

## what_verify_should_check
- Verify each numerical step in the Goodman saturation argument.
- Check whether the family-level reduction `4n+1` -> `srg(4n+1,2n,n-1,n)` is already explicit in the literature.
- Check whether `srg(65,32,15,16)` or an equivalent symmetric conference matrix of order 66 is already known to exist or not exist.
- If the literature does not already settle that, inspect whether the 2025 appendix constructions can be extended to 65 vertices under the forced conference-graph constraints.
