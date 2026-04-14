# statement_lock

We lock the active intended statement as follows: determine whether every `4`-regular vertex-transitive Ramanujan graph on `48` or `52` vertices is globally rigid in `R^2`, or else exhibit one such graph that is not globally rigid in `R^2`.

For the solve stage, the exact title-theorem target is:

"Every `4`-regular vertex-transitive Ramanujan graph on `48` or `52` vertices is globally rigid in `R^2`."

The exact disproof target is:

"There exists a `4`-regular vertex-transitive Ramanujan graph on `48` or `52` vertices that is not globally rigid in `R^2`."

If the positive statement closes, that would already be about `0.79` of a paper by the packet's own calibration, and it would naturally support the short note title `The 48- and 52-Vertex Residue for 4-Regular Vertex-Transitive Ramanujan Graphs`.

# definitions

- A `4`-regular Ramanujan graph means a `4`-regular graph whose nontrivial adjacency eigenvalues have absolute value at most `2*sqrt(3)`.
- The packet permits use of the `2024` characterization: a `4`-regular graph is globally rigid in `R^2` exactly when it is `4`-vertex-connected and essentially `6`-edge-connected.
- I interpret "essentially `6`-edge-connected" in the standard graph-theoretic way: there is no edge cut of size at most `5` whose removal leaves at least two components with at least two vertices each.
- For a partition `(A,B)` in a `4`-regular graph with edge boundary `t = e(A,B)`, the average quotient matrix is

```text
Q(A,B) = [[4 - t/|A|, t/|A|],
          [t/|B|,     4 - t/|B|]]
```

and its nontrivial eigenvalue is `4 - t*(1/|A| + 1/|B|)`. By interlacing, this eigenvalue must lie in the adjacency spectral window of the whole graph.
- For a separator partition `(A,S,B)` with `S` a vertex cut and no edges between `A` and `B`, if `x = e(A,S)` and `y = e(B,S)`, the average quotient matrix is

```text
Q(A,S,B) = [[4 - x/|A|, x/|A|,     0],
            [x/|S|,     4-(x+y)/|S|, y/|S|],
            [0,         y/|B|,     4 - y/|B|]]
```

and its eigenvalues also interlace the graph spectrum.
- Missing local data: the repo does not contain the Royle-Holt candidate graphs or any precomputed list of the `48`- or `52`-vertex residue graphs, so a full certification of the exact statement is currently blocked on graph input rather than on a known contradiction in the packet itself.

# approach_A

Structural / invariant route.

Use the Ramanujan spectral window together with quotient-matrix interlacing to rule out the connectivity obstructions that the `2024` characterization forbids.

The first target is vertex connectivity. If a graph on `48` or `52` vertices had a vertex cut `S` with `|S| <= 3`, then the partition `(A,S,B)` would force a `3 x 3` quotient matrix with one or two nontrivial eigenvalues. If every feasible template already has spectral radius above `2*sqrt(3)`, then all `1`-, `2`-, and `3`-cuts are impossible, so the graph is `4`-vertex-connected.

The second target is essential edge connectivity. Since the graph is `4`-regular, any edge cut has even size because

`e(A,V\\A) = 4|A| - 2e(A)`.

So essential `5`-edge cuts cannot occur at all; only essential `4`-edge cuts matter. For a nontrivial `4`-edge cut with sides of size `a` and `n-a`, the nontrivial quotient eigenvalue is

`lambda_cut = 4 - 4*(1/a + 1/(n-a))`.

If `lambda_cut > 2*sqrt(3)`, the cut is impossible in a Ramanujan graph.

This route is theorem-facing because a clean exclusion of low-order separator templates is already very close to the exact global-rigidity criterion for degree `4`.

# approach_B

Construction / extremal / contradiction route.

Assume a non-globally-rigid example exists at order `48` or `52`. By the packet's transfer kit, any such example must realize one of the known obstruction patterns from the small-order analysis, especially the "one `4`-clique per vertex" divisibility pattern. Try to force the smallest possible obstruction side `A` and combine:

- the exact degree equation `4|A| = 2e(A) + e(A,V\\A)`,
- simplicity bounds on `e(A)`,
- the fact that the only nontrivial essential cut size left is `4`,
- and vertex-transitivity, which should replicate any local `K_4`-type obstruction across the whole graph.

This route aims for a contradiction of the form: a surviving essential `4`-edge cut would have to isolate a tiny dense block, but vertex-transitivity would then force a global block system or clique pattern incompatible with the Ramanujan residue. The likely payoff is not a full closure from packet-only information, but a sharper localization of what an unresolved counterexample would have to look like.

# lemma_graph

1. Ramanujan condition gives `|lambda| <= 2*sqrt(3)` for every nontrivial adjacency eigenvalue.
2. Quotient-matrix eigenvalues interlace adjacency eigenvalues.
3. Therefore any separator template whose quotient matrix has a nontrivial eigenvalue exceeding `2*sqrt(3)` is impossible.
4. In a `4`-regular graph, every edge cut has even size, so essential `6`-edge-connectivity reduces to excluding nontrivial `4`-edge cuts.
5. A nontrivial `4`-edge cut with both sides reasonably large already violates the Ramanujan bound by the `2 x 2` quotient.
6. A small vertex cut `S` can be tested through the `3 x 3` quotient templates `(A,S,B)`.
7. If all `|S| <= 3` templates are spectrally impossible, then every unresolved graph is `4`-vertex-connected.
8. If, in addition, all nontrivial `4`-edge-cut templates are impossible, the exact statement closes via the `2024` characterization.
9. If some `4`-edge-cut templates survive, they identify the narrowest remaining obstruction family and hence the smallest paper-shaped theorem slice available from this solve.

# chosen_plan

Take `approach_A` as the main line. It directly targets the published degree-`4` global-rigidity criterion and can produce a reusable theorem slice even if the exact residue does not close.

Concrete plan:

1. Lock the quotient formulas analytically.
2. Use a parity argument to remove essential `5`-edge cuts immediately.
3. Derive the spectral exclusion range for nontrivial `4`-edge cuts.
4. Run one bounded local Python check over feasible `(A,S,B)` quotient templates for `n in {48,52}` and `|S| <= 3`.
5. Record exactly what this proves, what still survives, and whether the surviving gap is still paper-shaped.

# self_checks

- Statement check: the solve record stays on the exact `48/52` residue and does not drift to a broader family.
- Criterion check: I am using only the `2024` characterization stated in the packet, not importing extra unrecorded literature claims.
- Code gate check: the only computation used is the promised bounded quotient-template experiment, with no graph search and no external data.
- Parity check: in any `4`-regular graph, every edge cut has even size, so essential `5`-edge cuts are genuinely impossible.
- Template check: after adding the obvious feasibility constraints `x <= |A||S|`, `y <= |B||S|`, and the induced-edge simplicity bounds on `A` and `B`, the surviving low-cut templates are all tiny-island cases.

# code_used

One bounded local Python experiment using `numpy` was used after the reasoning sections were written. It enumerated average quotient templates for separator partitions `(A,S,B)` with `n in {48,52}` and `|S| <= 3`, together with the obvious feasibility constraints:

- `x = e(A,S)` and `y = e(B,S)` are even and positive;
- `x + y <= 4|S|`;
- `x <= |A||S|` and `y <= |B||S|`;
- `e(A) = (4|A| - x)/2` and `e(B) = (4|B| - y)/2` must be integers not exceeding the simple-graph maxima.

For each feasible template, the code computed the nontrivial quotient eigenvalues and checked them against the Ramanujan bound `2*sqrt(3)`.

# result

Main partial output.

1. No `1`-vertex cut survives the quotient-template constraints.
2. No `2`-vertex cut survives the quotient-template constraints.
3. Any `3`-vertex cut would have to isolate a component of order at most `5`.
4. Any nontrivial essential edge cut has size `4`, and any such `4`-edge cut would have to isolate a side of order between `4` and `9`.

The last item is analytic, not computational: for a nontrivial `4`-edge cut with sides `a` and `n-a`,

`lambda_cut = 4 - 4*(1/a + 1/(n-a))`.

For `n in {48,52}`, this exceeds `2*sqrt(3)` whenever `a >= 10`, so interlacing rules out every such cut with larger small side. Simplicity excludes `a = 2,3`, because then `e(A) = 2a - 2` is too large for a simple graph. Hence only `4 <= a <= 9` can survive.

So the current strongest honest theorem slice is:

"Let `G` be a `4`-regular Ramanujan graph on `48` or `52` vertices. Then `G` is `3`-connected; moreover, if `G` is not `4`-connected, every `3`-vertex cut isolates a component on at most `5` vertices. If `G` fails essential `6`-edge-connectivity, every nontrivial essential cut has size `4` and isolates a side on between `4` and `9` vertices."

This is a real structural reduction, but it does not settle the exact residue. The unresolved burden is now concentrated in tiny-island obstruction shapes rather than balanced separator phenomena.

# family_affinity

High. This sits directly on the source paper's sharp finite residue and uses the same spectral-to-rigidity bridge highlighted in the packet.

# generalization_signal

Moderate. The quotient-template method should transfer to other low-degree Ramanujan rigidity residues, especially other finite-order cleanup problems where the global-rigidity criterion reduces to small separator exclusion. What scales is the interlacing-based elimination of balanced or medium-size separators. What does not automatically scale is the final treatment of very small islands, which needs family-specific structure or exact candidate data.

# proof_template_reuse

The reusable template is:

1. convert the target geometric property into a small-separator obstruction criterion;
2. encode each obstruction as an average quotient matrix;
3. force a Ramanujan contradiction by interlacing;
4. isolate only a tiny list of small surviving templates for any later exact certification.

For this specific residue, the template has already reduced the live obstruction list to `3`-cuts with island size at most `5` and essential `4`-edge cuts with island size between `4` and `9`.

# candidate_theorem_slice

Candidate slice after the bounded check:

"Any `4`-regular Ramanujan graph on `48` or `52` vertices is `3`-connected. Moreover, every `3`-vertex cut isolates a component on at most `5` vertices, and every nontrivial essential edge cut isolates a side on between `4` and `9` vertices."

# smallest_param_shift_to_test

The next parameter shift is not a different order; it is a sharper local case split inside the same residue. The most informative tests are:

- `3`-cuts isolating components of orders `2,3,4,5`;
- essential `4`-edge cuts with small side orders `4,5,6,7,8,9`.

Those are exactly the tiny cases not eliminated by the spectral argument.

# why_this_is_or_is_not_publishable

Not publishable yet. The current package is still below the micro-paper threshold because it does not certify the actual candidate graphs at orders `48` and `52`, nor does it prove that all obstruction templates are impossible. A successful full solve would still be `70-90%` of a paper, but the present pre-code slice is only a structural reduction.

# paper_shape_support

If the main claim closes positively, the exact title theorem is:

"Every `4`-regular vertex-transitive Ramanujan graph on `48` or `52` vertices is globally rigid in `R^2`."

The minimal remaining packaging work would be:

- a concise certification table for the `48`- and `52`-vertex candidates;
- one paragraph tying the residue certification back to the `>=53` theorem;
- one short discussion of whether any exceptional order remains.

What extra structure would make the current solve paper-shaped if the main claim closes? Just one more ingredient: an exact candidate-level certification or exclusion of the remaining tiny-island cases. The current record has already compressed the obstruction search to a finite list of local shapes.

One immediate corollary would be:

"The `53`-vertex threshold in the `2023` theorem can be sharpened to exclude the `48`- and `52`-vertex residue as well."

# boundary_remark

Even if the exact residue remains unresolved here, the solve is already suggesting that any counterexample would have to be a very small-island obstruction rather than a balanced separator phenomenon. That is useful because it makes the residue look like a finite certification problem, not a new large-scale structural theorem.

# likely_failure_points

- The packet does not provide the actual `48`- and `52`-vertex candidate graphs.
- Quotient-matrix interlacing does rule out large and medium separators, but it still leaves a handful of tiny-side templates alive.
- Vertex-transitivity is likely crucial for eliminating the surviving tiny templates, but the repo does not include the local classification data needed to exploit that fully.

# what_verify_should_check

- Check that the parity argument for edge cuts in a `4`-regular graph is stated correctly.
- Check the quotient-matrix formulas and the interlacing interpretation.
- Check whether the bounded template computation really exhausts all feasible `|S| <= 3` separator templates.
- If the later solve result claims a clean `4`-vertex-connectivity slice, verify that no feasible small-side template was accidentally omitted.
- If only tiny `4`-edge-cut templates survive, verify whether the source paper's small-order obstruction analysis already collapses some of them.
