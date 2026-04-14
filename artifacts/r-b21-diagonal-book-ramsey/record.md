# Solve Record: The Exact Value of R(B21, B21)

## statement_lock
- Active slug: `r-b21-diagonal-book-ramsey`.
- Active title: `Determine the exact value of R(B21, B21)`.
- I use `B21` to mean the book graph consisting of 21 triangles sharing one common edge.
- Exact target: decide whether `R(B21, B21) = 85` or `R(B21, B21) = 86`.
- Equivalent extremal form: on 85 vertices, either
  - every graph has an edge contained in at least 21 triangles or a complement-edge contained in at least 21 complement-triangles, giving `R(B21, B21)=85`, or
  - there exists a graph `G` on 85 vertices such that every edge of `G` has at most 20 common neighbors and every edge of `G^c` has at most 20 common neighbors, giving `R(B21, B21)=86`.
- If the main claim closes, the exact title theorem is simply: `The Exact Value of R(B21, B21)`.

## definitions
- Let `G` be a graph on `v=85` vertices.
- For a vertex `x`, write `d(x)` for its degree in `G`.
- For distinct vertices `u,v`, write `c(u,v) = |N(u) ∩ N(v)|`.
- If `uv` is an edge of `G`, then `c(u,v)` is the number of triangles of `G` using the edge `uv`.
- If `uv` is a nonedge of `G`, then the number of common neighbors of `u,v` in the complement is
  `83 - d(u) - d(v) + c(u,v)`.
- Ambiguities/conventions to lock now:
  - common-neighbor counts exclude the endpoints themselves;
  - the packet already supplies the one-gap window `85 <= R(B21,B21) <= 86`, and solve treats that literature input as given;
  - the extremal 85-vertex object, if it exists, is a witness for `R(B21,B21)=86`, not yet a Lean-complete exact result.

## approach_A
Structural / invariant route: force any 85-vertex witness into an extremely rigid parameter set.

Assume `G` on 85 vertices avoids `B21` in both colors.

1. Pairwise constraints.
   - If `uv` is an edge, then `c(u,v) <= 20`.
   - If `uv` is a nonedge, then `uv` is an edge of `G^c`, so
     `83 - d(u) - d(v) + c(u,v) <= 20`,
     hence
     `c(u,v) <= d(u) + d(v) - 63`.

2. Global common-neighbor sum.
   - Let `m = e(G)`.
   - Let `q = C(85,2) = 3570`.
   - Let `s1 = sum_x d(x) = 2m`.
   - Let `s2 = sum_x d(x)^2`.
   - Double counting 2-paths gives
     `T := sum_{ {u,v} } c(u,v) = sum_x C(d(x),2) = (s2 - s1)/2 = (s2 - 2m)/2`.

3. Upper bound `T` using the pairwise constraints.
   - Summing over edges contributes at most `20m`.
   - Summing over nonedges contributes at most
     `sum_{uv nonedge} (d(u)+d(v)-63)`.
   - Also
     `sum_{uv nonedge} (d(u)+d(v)) = sum_x d(x)(84-d(x)) = 84s1 - s2 = 168m - s2`.
   - Therefore
     `T <= 20m + (168m - s2) - 63(q-m) = 251m - s2 - 63q`.

4. Compare the two expressions for `T`.
   - From `(s2 - 2m)/2 <= 251m - s2 - 63q`, we get
     `3s2 <= 504m - 126q`.
   - Since `q=3570`, this is
     `3s2 <= 504m - 449820`.

5. Force equality by Cauchy.
   - Cauchy gives
     `s2 >= s1^2 / 85 = 4m^2 / 85`.
   - Combining with the previous inequality yields
     `12m^2/85 <= 504m - 449820`.
   - Multiplying through by 85 and simplifying gives
     `4m^2 - 14280m + 12744900 <= 0`,
     i.e.
     `4(m - 1785)^2 <= 0`.
   - Hence necessarily `m = 1785`.

6. Degree regularity.
   - Now `s1 = 3570`.
   - Equality in Cauchy forces all degrees equal, so every vertex has degree `42`.

7. Equality propagation to every pair.
   - With `d(u)=d(v)=42`, every nonedge satisfies `c(u,v) <= 21`.
   - Since the total upper bound on `T` is attained exactly, every edge term and every nonedge term must attain equality:
     - if `uv` is an edge, then `c(u,v) = 20`;
     - if `uv` is a nonedge, then `c(u,v) = 21`.

Conclusion of Approach A:
- Any 85-vertex witness for `R(B21,B21)=86` must be a strongly regular graph with parameters
  `srg(85,42,20,21)`.
- Equivalently, the extremal witness problem is exactly the existence problem for a conference graph on 85 vertices.

Self-check after Approach A:
- The nonedge inequality sign was checked carefully; it is an upper bound, not a lower bound.
- The quadratic collapse really is exact: `4(m-1785)^2 <= 0`.
- The resulting parameter set is internally consistent with the book constraints:
  adjacent pairs have exactly 20 common neighbors, nonadjacent pairs exactly 21.

## approach_B
Construction / extremal route: once the structural reduction is known, the only honest lower-bound lane is to construct an `srg(85,42,20,21)` candidate or prove none exists.

Reasoning:
- The reduction above eliminates irregular or ad hoc witnesses.
- So a successful `R(B21,B21)=86` proof now has to pass through a conference-graph object.
- Natural first constructions should come from the `85 = 5 * 17` factorization, because both 5 and 17 support Paley/conference behavior individually.

Bounded experiment performed only after the reasoning stage:
- I tested one natural Cayley family on `Z_5 x Z_17` built from matching quadratic-character classes. It is 42-regular, but edge common-neighbor counts hit `{20,21,22,24}`, so it fails.
- I tested the obvious conference-matrix product ansatz `((S_5 + I) ⊗ (S_17 + I)) - I`. It is again 42-regular, but nonedge common-neighbor counts reach `{21,22,23,25}`, so it fails.
- I then exhausted the 24 symmetry-respecting union-of-cells class-union Cayley families obtained from the eight coordinate classes
  `0R, 0N, R0, N0, RR, RN, NR, NN`
  with total valency 42. None satisfy the target bound; the best cases still overshoot by 4.

Conclusion of Approach B:
- No simple product-style algebraic witness appeared.
- This does not rule out an `srg(85,42,20,21)`; it only says the first easy `5 x 17` templates fail.

Self-check after Approach B:
- The experiment was deliberately bounded and structural, not a generic brute-force search over graphs.
- Failure of these templates is evidence against an easy witness, not a nonexistence proof.

## lemma_graph
1. Extremal witness assumption on 85 vertices.
2. Edge constraint: `c(u,v) <= 20`.
3. Complement-edge constraint on nonedges: `c(u,v) <= d(u)+d(v)-63`.
4. Double-counting common neighbors gives a global inequality in `m` and `sum d(x)^2`.
5. Cauchy collapses the inequality to equality, forcing `m=1785` and `d(x)=42` for all `x`.
6. Equality propagation forces every edge to have 20 common neighbors and every nonedge to have 21.
7. Therefore any witness is exactly an `srg(85,42,20,21)`.
8. Main problem reduced to existence/nonexistence of that conference graph.

## chosen_plan
- Best path: keep the exact intended statement locked, prove the strongest rigorous structural reduction available, then check whether a trivial algebraic witness survives.
- This was better than starting with search because the packet marks the target as non-search-heavy and the reduction sharply compresses the witness space.
- Current honest stopping point: the reduction is rigorous, the easy witness lane failed, and I do not yet have either a construction or a nonexistence proof for `srg(85,42,20,21)`.

## self_checks
- Statement check: the solve target remained the exact 85-vs-86 question throughout; no concept drift into a broader family claim.
- Proof check: every inequality used in the reduction has been re-expanded symbolically and matches the extremal interpretation.
- Scope check: the bounded code only tested natural structured witness families after the reasoning-first stage.
- Publication check: the current output is theorem-facing and useful, but it is not yet the title theorem.

## code_used
- Yes, but only minimally and after the reasoning stage.
- Type: tiny bounded witness-verification experiments.
- Used for:
  - checking a natural `Z_5 x Z_17` quadratic-character Cayley candidate;
  - checking a simple conference-matrix composition ansatz;
  - exhausting the 24 symmetry-respecting class-union Cayley families of that product type.
- Code was not used for a generic SAT/ILP/brute-force graph search.

## result
- Strong partial result:
  any 85-vertex graph with neither `G` nor `G^c` containing `B21` must be an `srg(85,42,20,21)`.
- Equivalently:
  `R(B21,B21)=86` if and only if there exists a strongly regular conference graph with parameters `(85,42,20,21)`.
- I did not prove existence or nonexistence of that graph.
- Therefore I did not close the exact value.

Self-check after result:
- This is a real theorem slice, not an exact solve of the selected problem.
- The slice is sharp: it leaves no irregular 85-vertex witness lane open.

## family_affinity
- Strong.
- The reduction sits exactly on the diagonal one-gap book Ramsey mechanism: a `4n+1`-vertex witness would have to saturate the pairwise book bounds everywhere.
- Here that gives the clean conference-graph residue at `n=21`.

## generalization_signal
- The proof template appears to generalize formally to any diagonal one-gap instance on `4n+1` vertices:
  if a graph on `4n+1` vertices avoids `Bn` in both colors, the same common-neighbor summation should force the conference parameters `(4n+1, 2n, n-1, n)`.
- I am not claiming that as a finished general theorem here, but the algebraic pattern is clear and reusable.
- What scales:
  the pairwise common-neighbor bounds, the global 2-path count, and the Cauchy equality collapse.
- What does not scale automatically:
  converting the resulting conference-graph existence problem into an exact Ramsey value.

## proof_template_reuse
- Reusable template:
  1. encode book avoidance as edge/nonedge common-neighbor inequalities;
  2. sum over all vertex pairs;
  3. rewrite the nonedge degree sum in terms of `sum d(x)^2`;
  4. combine with Cauchy to force equality;
  5. read off the conference-graph parameters.
- This is exactly the sort of proof skeleton worth reusing on other diagonal book residues with a one-gap window.

## candidate_theorem_slice
- Candidate theorem slice:
  `If G is a graph on 85 vertices such that neither G nor its complement contains B21, then G is strongly regular with parameters (85,42,20,21).`
- This is the smallest clean theorem-facing statement I can currently justify rigorously.
- It is strong enough to turn the selected problem into a pure conference-graph existence/nonexistence question.

## smallest_param_shift_to_test
- For this exact problem, the smallest useful shift is structural rather than numerical:
  test the witness question inside the conference-graph lane before any broader search.
- Immediate next shifts that would help most:
  - search for an `srg(85,42,20,21)` within more structured families than the naive `Z_5 x Z_17` class-union constructions;
  - in the family direction, test whether the same reduction can be written cleanly for the next unresolved diagonal residue of the form `4n+1` that is a sum of two squares but not a prime power.

## why_this_is_or_is_not_publishable
- If the main claim closes, yes: this is still a genuine micro-paper lane and a successful solve would already be roughly 70-90% of a paper.
- Exact title theorem if closed:
  `The Exact Value of R(B21, B21)`.
- Minimal remaining packaging if closed:
  - one short introduction situating the `85 <= R <= 86` gap;
  - the exact-value proof or witness;
  - a compact explanation of why `85` sits outside the standard exact criteria;
  - the conference-graph reduction as the main extremal structure lemma.
- Current output alone is probably too thin for the micro-paper lane unless verification shows the reduction is genuinely absent from the literature.
- So the honest assessment is:
  theorem-facing and useful, but not yet paper-ready and not yet enough to claim the selected exact value.

## paper_shape_support
- What extra structure would make the result paper-shaped if the main claim closes?
  - the exact witness or exact impossibility argument for `(85,42,20,21)`;
  - one concise structural lemma reducing the Ramsey problem to the conference-graph residue;
  - one short boundary remark comparing `n=21` with the already-settled prime-power and non-sum-of-two-squares diagonal cases.
- One immediate corollary / remark that already falls out:
  any 85-vertex extremal witness would necessarily be 42-regular and meet the book threshold with equality on every pair.
- Current package status:
  closer to a paper-shaped claim than a random partial computation, but still just a slice until the existence question is resolved.

## boundary_remark
- The `n=21` case is exactly the boundary where the standard diagonal criteria stop helping:
  `4n+1 = 85` is a sum of two squares, so the upper criterion does not collapse the value to `4n+1`,
  but `85` is not a prime power, so the usual Paley lower-bound mechanism does not automatically give `4n+2`.
- The present reduction shows that the entire remaining difficulty is concentrated in one conference-graph residue.

## likely_failure_points
- The structural reduction may already be implicit in the existing book-Ramsey or conference-graph literature.
- The bounded construction failures do not rule out more sophisticated conference-graph constructions.
- A later verifier may find that `srg(85,42,20,21)` is already known to exist or not exist in design-theory sources.
- If so, the real mathematical work in this solve record is the reduction, not yet the exact Ramsey closure.

## what_verify_should_check
- Check whether the theorem slice
  `85-vertex extremal witness => srg(85,42,20,21)`
  is already stated or immediate in prior book Ramsey papers.
- Check whether `srg(85,42,20,21)` or an equivalent symmetric conference matrix of order 86 is already known to exist or be impossible.
- Check whether the failed `Z_5 x Z_17` class-union families correspond to named constructions that are already understood.
- Check whether the general `4n+1` equality-collapse template is already standard folklore in the diagonal book-Ramsey literature.
