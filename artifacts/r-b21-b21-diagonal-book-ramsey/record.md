# Solve Record: Determine the exact value of R(B21, B21)

## statement_lock
Active slug: `r-b21-b21-diagonal-book-ramsey`.

Active title: `Determine the exact value of R(B21, B21)`.

Locked target: decide whether the remaining endpoint is `R(B21, B21) = 85` or `R(B21, B21) = 86`.

Convention: `B21` means the book with 21 pages, so in a monochromatic graph an edge is the spine of a monochromatic `B21` exactly when it lies in at least 21 monochromatic triangles.

Equivalent 85-vertex extremal form: if there exists a red-blue coloring of `K_85` with no monochromatic `B21`, then the red graph `G` on 85 vertices satisfies

- every edge of `G` has at most 20 common neighbors in `G`, and
- every edge of `G^c` has at most 20 common neighbors in `G^c`.

Exact title theorem if the upper-bound side closes: `R(B21, B21) = 85`.

Exact title theorem if a witness exists: `R(B21, B21) = 86`.

If this exact endpoint closes, it is still about `70-90%` of a short paper. The title theorem is already the whole note, and the remaining packaging would just be the prior interval, the decisive forcing/witness argument, and one compact structural lemma.

## definitions
Let `G` be the red graph of a red-blue coloring of `K_85`.

For distinct vertices `u,v`, let `c(u,v) = |N_G(u) ∩ N_G(v)|`.

If `uv` is an edge of `G`, then `c(u,v)` is the number of red triangles containing `uv`, so `B21`-avoidance gives `c(u,v) <= 20`.

If `uv` is a nonedge of `G`, then `uv` is an edge of `G^c`, and the number of common blue neighbors of `u,v` is

`83 - d(u) - d(v) + c(u,v)`.

So blue `B21`-avoidance gives

`83 - d(u) - d(v) + c(u,v) <= 20`,

hence

`c(u,v) <= d(u) + d(v) - 63`.

Ambiguities locked now:

- common-neighbor counts exclude the endpoints;
- the selection packet already supplies the frontier interval `85 <= R(B21, B21) <= 86`;
- in solve, a non-Lean exact proof would still only be `CANDIDATE`, and here I do not reach even that exact closure.

## approach_A
Structural / invariant route: sum common-neighbor counts over all unordered pairs and force equality.

Assume `G` on 85 vertices avoids `B21` in both colors.

Write

- `m = e(G)`,
- `q = C(85,2) = 3570`,
- `s1 = sum_x d(x) = 2m`,
- `s2 = sum_x d(x)^2`.

Let

`T = sum_{ {u,v} } c(u,v)`.

By double-counting 2-paths,

`T = sum_x C(d(x),2) = (s2 - s1)/2 = (s2 - 2m)/2`.

Now bound `T` from the pairwise constraints.

Edges contribute at most `20m`.

For nonedges,

`sum_{uv nonedge} (d(u)+d(v)) = sum_x d(x)(84-d(x)) = 168m - s2`.

So

`T <= 20m + (168m - s2) - 63(q-m) = 251m - s2 - 63q`.

Comparing the two formulas for `T`,

`(s2 - 2m)/2 <= 251m - s2 - 63q`,

so

`3s2 <= 504m - 126q = 504m - 449820`.

By Cauchy,

`s2 >= s1^2 / 85 = 4m^2 / 85`.

Hence

`12m^2 / 85 <= 504m - 449820`,

equivalently

`4m^2 - 14280m + 12744900 <= 0`.

But

`12744900 = 4 * 1785^2`,

so this is

`4(m - 1785)^2 <= 0`.

Therefore `m = 1785`, and equality holds everywhere in the chain.

Consequences:

- `s2 = 4m^2 / 85`, so every vertex has degree `42`;
- each edge attains its local cap, so `c(u,v) = 20` on edges;
- each nonedge attains its local cap, so `c(u,v) = 21` on nonedges.

Thus any 85-vertex witness is exactly a strongly regular graph with parameters

`(v,k,lambda,mu) = (85,42,20,21)`.

Equivalently, the full 85-vs-86 Ramsey question collapses to:

does an `srg(85,42,20,21)` exist?

Self-check after Approach A: the quadratic collapse is exact, not approximate. There is no room left for an irregular near-extremal witness.

## approach_B
Construction / contradiction route: test whether the residue `srg(85,42,20,21)` can be disposed of cheaply.

The standard diagonal conference-graph obstruction that worked in the neighboring `B19` case does not fire here. The conference order would be `86`, and the usual arithmetic necessary condition only says `85` must be a sum of two squares; that condition is satisfied because

`85 = 9^2 + 2^2`.

So the easy contradiction lane stops immediately.

On the constructive side, the natural first guess is a `5 x 17` algebraic witness because `85 = 5 * 17`. Inside the repo there is already a nearby `B21` diagonal record reporting that first product-style `Z_5 x Z_17` Cayley templates fail the target pairwise counts. I did not rerun those bounded experiments here, but I use their negative outcome as a reason not to spend this solve turn on the same easy construction family.

So the honest output of Approach B is not an exact witness or impossibility proof. It is the narrower conclusion that the remaining residue is genuinely a conference-graph existence problem, and neither the cheapest arithmetic obstruction nor the cheapest product-style witness template settles it.

Self-check after Approach B: this is still on the exact selected statement. I did not switch to a broader family theorem or a generic search lane.

## lemma_graph
1. Assume a red-blue coloring of `K_85` avoids monochromatic `B21`.
2. Translate book-avoidance into pairwise common-neighbor caps on edges and nonedges.
3. Sum `c(u,v)` over all unordered pairs.
4. Rewrite the nonedge contribution in terms of `m` and `sum d(x)^2`.
5. Use Cauchy to collapse the resulting inequality to equality.
6. Deduce `m = 1785` and 42-regularity.
7. Propagate equality to every edge and nonedge.
8. Conclude any 85-vertex witness is `srg(85,42,20,21)`.
9. Reduce the Ramsey endpoint to the existence or nonexistence of that conference graph.

## chosen_plan
Best path for this solve was the structural one. The packet marks the target as non-`search_heavy`, and the common-neighborhood summation completely rigidifies any putative 85-vertex witness.

After that reduction, I checked the shortest contradiction lane. It fails because `85` passes the sum-of-two-squares arithmetic test.

So the strongest honest stopping point is:

- rigorous theorem slice: `85`-vertex extremal witness implies `srg(85,42,20,21)`;
- unresolved final residue: conference-graph existence at order `85`.

## self_checks
After statement lock: the active endpoint is exactly `85` versus `86`, so working at `K_85` is correct.

After the pairwise translation: edge and nonedge caps are stated in the same graph `G`, so there is no color-switch ambiguity in the summation.

After the global inequality: the coefficient arithmetic was rechecked; the final quadratic really is `4(m-1785)^2 <= 0`.

After equality propagation: because the total sum hits the pairwise upper bound exactly, every local pairwise bound must also be tight.

After the contradiction attempt: the arithmetic conference obstruction is unavailable here, so claiming `R(B21, B21) = 85` would be unjustified.

## code_used
No new code used in this run.

Reasoning was sufficient to isolate the exact extremal residue. At that point, new code would only have been justified for a tightly scoped structured conference-graph search, and the repo already contains a nearby failed bounded attempt in the easiest `5 x 17` product family.

## result
Strong partial result:

`If G is a graph on 85 vertices such that neither G nor its complement contains B21, then G is strongly regular with parameters (85,42,20,21).`

Equivalent reformulation of the selected problem:

`R(B21, B21) = 86` if and only if an `srg(85,42,20,21)` exists.

I did not prove existence or nonexistence of that graph, so I did not close the exact Ramsey value.

What part of the argument scales:

- the pairwise common-neighbor inequalities,
- the global 2-path summation,
- the equality collapse at the odd order `4m+1`.

What part does not scale automatically:

- the last existence/nonexistence step for the conference graph residue.

Suggested theorem slice:

`Any diagonal B21 extremal witness on 85 vertices is exactly a conference graph with parameters (85,42,20,21).`

Best next parameter shifts:

- first, stay on the same parameter and attack `(85,42,20,21)` directly;
- second, compare with the nearest diagonal one-gap cases of the form `K_{4m+1}` where the conference residue either is ruled out arithmetically or is realized by a prime-power construction.

Current package assessment:

closer to a paper-shaped claim than a raw computation, but still only a theorem-facing slice, not yet the exact title theorem.

## family_affinity
This sits squarely in the diagonal one-gap book Ramsey lane. The reason it is publication-relevant is that the entire remaining endpoint compresses to one rigid conference-graph residue rather than a broad campaign of feeder lemmas.

## generalization_signal
The algebra plainly generalizes.

For any `m`, if a red-blue coloring of `K_{4m+1}` avoids monochromatic `B_m`, the same calculation forces the red graph to be

`srg(4m+1, 2m, m-1, m)`.

That is a reusable family-shaped proof template. What does not generalize for free is the final step from that conference residue to the exact Ramsey value.

## proof_template_reuse
Reusable template:

1. encode book-avoidance as common-neighbor caps;
2. sum the caps over all pairs;
3. rewrite the nonedge term using degree squares;
4. collapse with Cauchy;
5. identify the resulting extremal object as a conference graph.

This is the part worth reusing on other diagonal one-gap book residues.

## candidate_theorem_slice
Candidate theorem slice:

`If G is a graph on 85 vertices such that neither G nor its complement contains B21, then G is strongly regular with parameters (85,42,20,21).`

This is the smallest clean structural theorem I can defend rigorously in solve.

## smallest_param_shift_to_test
The most useful immediate shift is not a new Ramsey parameter. It is the same endpoint inside the conference-graph lane:

- settle existence or nonexistence of `srg(85,42,20,21)`.

If a family comparison is needed after that, the best shift is to neighboring diagonal one-gap cases `K_{4m+1}` where the same reduction holds but the conference residue is better understood.

## why_this_is_or_is_not_publishable
If the exact endpoint closes, then yes: this is still a micro-paper target and the solve would already be about `70-90%` of a short paper.

Exact title theorem if closed:

`The Exact Value of R(B21, B21)`.

Minimal remaining packaging work after a true closure:

- cite the prior interval `85 <= R(B21, B21) <= 86`;
- present either the exact witness or the exact impossibility argument for `(85,42,20,21)`;
- include the conference-graph reduction as the main structural lemma;
- add one short comparison paragraph with the neighboring diagonal/almost-diagonal book cases.

Current result alone is still too thin for the micro-paper lane. It is a real theorem slice, but not yet the title theorem and not yet paper-ready.

## paper_shape_support
What extra structure would make this paper-shaped if the main claim closes:

- one decisive closure of the conference residue `(85,42,20,21)`;
- the reduction above as the main lemma;
- one immediate remark explaining why `n=21` sits just beyond the easy arithmetic and prime-power criteria.

One immediate boundary remark already available:

any 85-vertex extremal witness would have to hit the book threshold with equality on every pair, so there is no irregular escape route left.

## boundary_remark
The `n=21` case is a genuine boundary point.

The `B19`-style arithmetic nonexistence route no longer works because `85` is a sum of two squares, but the usual Paley-style easy witness route also does not automatically apply because `85` is not a prime power.

So the whole endpoint really does concentrate into one conference-graph residue rather than collapsing for a routine reason in either direction.

## likely_failure_points
The structural reduction may already be folklore in the conference-graph or book-Ramsey literature.

The unresolved residue might already be known in design-theory sources, in which case the actual frontier work here is only the clean reduction.

If the conference residue is genuinely open, then solve may stall without either a more specialized structured construction lane or a sharper nonexistence theorem than the sum-of-two-squares test.

## what_verify_should_check
Check the reduction

`85`-vertex witness `=> srg(85,42,20,21)`

line by line, especially the nonedge summation and the equality propagation.

Check whether `srg(85,42,20,21)` is already known to exist or to be impossible.

Check whether the generalized slice

`K_{4m+1}` diagonal `B_m` witness `=> srg(4m+1,2m,m-1,m)`

is already explicitly stated in the literature.

Check whether the nearby in-repo bounded `5 x 17` product-family failures correspond to named constructions already ruled out in the literature.
