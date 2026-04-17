# Solve Record: The Exact Value of R(B10, B10)

- slug: `r-b10-b10-diagonal-book-ramsey`
- working_packet: `artifacts/r-b10-b10-diagonal-book-ramsey/working_packet.md`

## statement_lock
Lock the convention: for `t >= 1`, the book graph `B_t` is the graph of `t` triangles sharing one common edge. Under this convention, the active target is to prove or disprove the exact identity

`R(B10, B10) = 42`.

Because the packet already supplies the literature interval `41 <= R(B10, B10) <= 42`, the solve-stage exact task reduces to one of two decisive endpoints:

- produce a 2-coloring of `K_41` with no monochromatic `B10`, which would force `R(B10, B10) >= 42` and hence equality;
- or prove that every 2-coloring of `K_41` already contains a monochromatic `B10`, which would force `R(B10, B10) = 41`.

## definitions
- `B10` means ten triangles sharing a common base edge.
- In a 2-coloring of `K_n`, a monochromatic `B10` in color `c` is equivalent to the existence of a color-`c` edge `uv` with at least `10` common color-`c` neighbors.
- For a graph `G`, write `codeg_G(u,v)` for the number of common neighbors of `u,v` in `G`.
- A lower-bound witness for `R(B10,B10)` at level `42` is therefore a graph `G` on `41` vertices such that:
  - `codeg_G(u,v) <= 9` for every edge `uv` of `G`;
  - `codeg_{\overline G}(u,v) <= 9` for every edge `uv` of `\overline G`.
- A natural candidate is the Paley graph `P(41)` on `F_41`, with adjacency defined by quadratic residues. Standard Paley facts suggest `P(41)` is strongly regular with parameters `(41,20,9,10)` and self-complementary.

## approach_A
Structural / invariant route:

- Try to rederive the sourced upper bound `R(B10,B10) <= 42` internally from common-neighbor inequalities.
- In a hypothetical bad coloring of `K_42`, every red edge has at most `9` red common neighbors and every blue edge has at most `9` blue common neighbors.
- Looking from a fixed vertex `v`, the induced red graph on `N_R(v)` has maximum degree at most `9`, and the induced blue graph on `N_B(v)` has maximum degree at most `9`.
- Since `|N_R(v)| + |N_B(v)| = 41`, one hopes to combine average-degree pressure, triangle counts, and complement symmetry to force one side above the `10`-page threshold.
- This path is theorem-facing but not the lowest-risk solve path here because the packet already treats the upper bound as sourced, while the lower endpoint is the unresolved step.

Self-check:

- This route is legitimate as a structural plan, but without reopening the source proof it is too easy to understate a hidden extremal case.

## approach_B
Construction / extremal route:

- Use a concrete `41`-vertex coloring.
- Color `K_41` by declaring red edges to be the edges of the Paley graph `P(41)` and blue edges to be the nonedges.
- If `P(41)` has strong regularity parameters `(41,20,9,10)`, then every red edge has exactly `9` red common neighbors.
- Because `P(41)` is self-complementary, the blue graph has the same relevant edge-codegree value `9`.
- Then neither color contains a `B10`, so this gives a decisive `K_41` witness and closes the interval to `R(B10,B10)=42`.

Self-check:

- The threshold must be checked carefully: `9` common same-color neighbors forbids `B10` but still allows `B9`.
- The Ramsey lower-bound convention must also be checked carefully: a bad coloring of `K_41` implies `R(B10,B10) >= 42`, not merely `>= 41`.

## lemma_graph
Proof skeleton currently targeted:

1. `B10` occurs in color `c` iff some color-`c` edge lies in at least `10` color-`c` triangles.
2. The Paley graph `P(41)` exists because `41` is a prime congruent to `1 mod 4`.
3. Standard Paley theory gives `P(41)` strongly regular parameters `(41,20,9,10)`.
4. Therefore each red edge in the Paley coloring has exactly `9` red common neighbors.
5. The complement of `P(41)` is isomorphic to `P(41)`, so each blue edge has exactly `9` blue common neighbors.
6. Hence the Paley coloring of `K_41` contains no monochromatic `B10`.
7. Combine with the sourced upper bound `R(B10,B10) <= 42` to conclude `R(B10,B10) = 42`.

Self-check:

- Step 5 can also be checked numerically from complement parameters: for a nonedge `uv` in `P(41)`, the number of common nonneighbors is `41 - 2 - 2*20 + 10 = 9`.

## chosen_plan
Best path: pursue Approach B.

Reason:

- It attacks exactly the missing endpoint.
- It uses a compact, theorem-shaped object rather than a broad case analysis.
- If it checks out, the result is already the title theorem of a short note: the exact value `R(B10,B10)=42`.

Planned bounded verification:

- verify the Paley(41) adjacency model directly by a tiny local checker;
- confirm that the maximum red and blue book sizes are both `9`;
- then package the witness as the decisive lower-bound theorem slice.

## self_checks
- Statement lock check: the packet asks for the least `n` with the monochromatic `B10` property, so exact equality at `42` is the right target theorem.
- Convention check: this record uses the standard book-graph convention "`B_t` = `t` pages"; if a local source uses shifted indexing, verification must catch it.
- Dependency check: the proposed closure depends on the packet's sourced upper bound `R(B10,B10) <= 42`; solve is not reproving that bound from scratch.
- Risk check: if the Paley witness already appears implicitly inside the cited literature, the mathematics may still be right but novelty would have to be checked in the later verify stage.
- Bounded-check update: a local finite checker on the Paley coloring of `K_41` returned degree set `[20]` in both colors and same-color edge codegree set `[9]` in both colors, exactly matching the intended witness profile.

## code_used
Yes, but only at the minimal certificate level.

Bounded local checker used:

- constructed the Paley graph on `F_41` via nonzero quadratic residues;
- verified every vertex has red degree `20` and blue degree `20`;
- verified every red edge has exactly `9` red common neighbors;
- verified every blue edge has exactly `9` blue common neighbors.

Recorded checker outcome:

`{'red_degree_set': [20], 'blue_degree_set': [20], 'red_edge_common_red_set': [9], 'blue_edge_common_blue_set': [9], 'witness_avoids_monochromatic_B10': True}`.

## result
Strong exact candidate obtained.

Main solve conclusion:

- The Paley coloring of `K_41` avoids a monochromatic `B10` in both colors.
- Therefore `R(B10,B10) >= 42`.
- Combined with the sourced upper bound `R(B10,B10) <= 42`, the exact candidate conclusion is
  - `R(B10,B10) = 42`.

This is not yet marked `EXACT` because solve does not promote to Lean-complete exactness, but mathematically this is the decisive theorem-shaped endpoint unless a convention or novelty issue appears in verification.

Immediate corollary / remark:

- The one-step diagonal gap `41 <= R(B10,B10) <= 42` collapses at the upper endpoint via a `41`-vertex self-complementary witness, so the decisive object is constructive rather than an additional upper-bound refinement.

What scales:

- the codegree formulation of book avoidance;
- the use of self-complementary strongly regular witnesses to certify both colors at once.

What does not automatically scale:

- the existence of an order-specific witness whose edge codegree is exactly `t-1` for the required page count.

Current package assessment:

- this is closer to a paper-shaped exact theorem than to a thin isolated instance, because the result already has a clean title theorem and a compact proof package.

## family_affinity
High. The candidate sits exactly on the diagonal book-Ramsey line and uses a classical pseudorandom/self-complementary witness template that is native to diagonal Ramsey constructions.

## generalization_signal
Moderate. The argument shape scales to any diagonal book instance where a self-complementary strongly regular graph realizes edge and complement edge codegrees below the page threshold. What scales is the witness template and the `book -> edge-codegree` translation; what does not automatically scale is finding the right order and parameter set.

## proof_template_reuse
Reusable template:

- translate `B_t` avoidance into an edge-codegree bound;
- identify a regular or strongly regular graph with edge-codegree exactly `t-1`;
- use self-complementarity or complement-parameter control to certify the other color simultaneously.

This template is potentially reusable for other one-step diagonal book gaps tied to Paley or conference-type graphs.

## candidate_theorem_slice
Candidate theorem slice:

`The Paley coloring of K_41 contains no monochromatic copy of B10. Consequently, together with the sourced upper bound R(B10,B10) <= 42, one obtains R(B10,B10)=42.`

## smallest_param_shift_to_test
Best immediate neighboring shifts after the main claim:

- inspect whether the same Paley witness language gives a compact reproof of the nearby solved diagonal point `R(B8,B8)=33`;
- test the next unresolved diagonal order where a Paley or Paley-type witness might hit the threshold exactly, rather than starting a broad family program.

Most useful next one or two shifts if verify wants family context:

- a downward calibration against the already solved neighbor `B8`;
- the nearest unresolved diagonal case whose lower endpoint matches an available Paley or conference-type order.

## why_this_is_or_is_not_publishable
If the Paley witness checks and the upper bound is indeed as stated in the packet, then this is very likely within the intended micro-paper lane.

- A successful solve would already be about `80%` of a paper, consistent with the packet.
- The exact title theorem would be `The Exact Value of R(B10,B10)`.
- Minimal remaining packaging work would be: write the Paley construction cleanly, state the sourced upper bound with correct citation, and include a compact verification certificate or explicit code appendix.
- The current solve package is not too thin for the micro-paper lane if novelty survives verification, because the solve already supplies the exact endpoint and the certificate is compact.

If the witness fails or depends on a shifted notation for `B10`, then the package collapses quickly and the current line would not yet be paper-ready.

## paper_shape_support
If the main claim closes, the smallest natural support package is:

- one lemma translating monochromatic books into same-color edge codegrees;
- one proposition recording the relevant Paley(41) parameters and self-complementarity;
- one corollary concluding `R(B10,B10)=42` from the existing upper bound.

This is enough structure to make the result read like a short theorem note rather than an isolated computational witness.

Remaining packaging work after the main claim:

- convert the checker-backed witness into a clean mathematical proof using Paley parameters;
- attach a short certificate appendix or reproducibility note;
- make the citation chain to the `<= 42` upper bound explicit.

## boundary_remark
Natural boundary remark:

The argument is exquisitely endpoint-specific. It appears to certify the lower endpoint `42` by a single `41`-vertex witness, but it does not by itself improve the general diagonal-book theory or produce a new upper-bound mechanism.

## likely_failure_points
- the local convention for `B10` could be shifted by one in the cited sources;
- the Paley codegree facts may certify only one color if the complement count is mishandled;
- the witness may be mathematically correct yet already explicit in prior art, which would move the later verdict toward rediscovery rather than frontier closure.

## what_verify_should_check
- confirm that all cited sources use the same book-graph indexing convention as this record;
- confirm that the sourced interval really is `41 <= R(B10,B10) <= 42`;
- novelty-check whether the Paley(41) witness or its exact implication for `R(B10,B10)` already appears in the literature;
- if the result survives, preserve the finite witness certificate and independent checker output.
- check whether the writeup should present the proof as a purely mathematical strongly-regular-graph argument, with the local checker only as a verification appendix.

## verify_rediscovery
PASS 1 verdict: rediscovery established.

Bounded prior-art audit outcome:

- The 2026 Wesley paper uses the standard book notation `B_n = K_2 + \overline{K_n}` and explicitly restates the classical Rousseau-Sheehan theorem that `R(B_n,B_n)=4n+2` whenever `4n+1` is a prime power.
- Substituting `n=10` gives `4n+1=41`, which is prime, hence the exact value `R(B10,B10)=42` already follows from prior art.
- This is stronger than merely reproducing the recent interval `41 <= R(B10,B10) <= 42`; the exact intended statement is already settled in the literature.

Conclusion:

- `verify_verdict = REDISCOVERY`
- the run cannot remain an open frontier exact candidate
- the correct archival action is `archive_as_rediscovery`

## verify_faithfulness
The solver's mathematical target matches the packet's intended statement exactly.

- The record locks onto the exact claim `R(B10,B10)=42`, which is the decisive endpoint for the packet's stated problem.
- The book-graph convention used locally is faithful to the standard convention cited in the literature: `B10` means ten triangles sharing a common base edge.
- No quantifier drift, proxy theorem drift, or statement weakening was found.

What failed was not faithfulness but novelty: the exact theorem is already known.

## verify_proof
No incorrect mathematical step was found in the solver's witness argument.

Verified proof skeleton:

1. A monochromatic `B10` is equivalent to a same-color edge with at least `10` same-color common neighbors.
2. In the Paley graph `P(41)`, every edge has exactly `9` common neighbors in the graph.
3. Because the Paley coloring is self-complementary, every blue edge also has exactly `9` blue common neighbors.
4. Therefore the Paley coloring of `K_41` avoids monochromatic `B10` in both colors.
5. Hence `R(B10,B10) >= 42`.

This lower-bound witness is correct, but it does not yield a new theorem because the exact equality was already known from prior art.

## verify_adversarial
Adversarial local rerun succeeded.

Independent bounded checker rerun on the Paley coloring of `K_41` returned:

`{'red_degree_set': [20], 'blue_degree_set': [20], 'red_edge_common_red_set': [9], 'blue_edge_common_blue_set': [9], 'max_red_book_pages': 9, 'max_blue_book_pages': 9, 'witness_avoids_monochromatic_B10': True}`.

Adversarial assessment:

- the claimed construction really does avoid monochromatic `B10`
- the lower-bound endpoint `R(B10,B10) >= 42` is supported
- no computational mismatch was found between the prose claim and the finite certificate

## verify_theorem_worthiness
Exactness:

- The solver isolated the right exact statement and supplied a correct lower-bound witness.

Novelty:

- Fails. The exact intended statement is already a classical theorem, so this cannot support a frontier micro-paper.

Reproducibility:

- Good. The Paley witness is compact and independently checkable.

Lean readiness:

- Not appropriate in the main lane. Formalizing a rediscovered theorem would be archival polish, not the shortest path to a publication packet.

Paper leverage:

- As a frontier claim: none.
- As an expository or archival exercise: moderate, but that is outside the active micro-paper objective.

Explicit publication answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No, because the exact theorem is already in prior art.
- What percentage of a new paper would one solve already provide? `0%` for frontier publication value.
- What title theorem is actually visible? `R(B10,B10)=42`, but as a known theorem rather than a new one.
- What part of the argument scales? The Paley/self-complementary witness template and the edge-codegree translation.
- What part clearly does not? Novelty and publication status for this exact diagonal instance.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? In the active lane it is `REDISCOVERY`, which dominates any instance-only packaging.

## verify_verdict
`REDISCOVERY`

The intended theorem is correctly targeted and the Paley witness is valid, but the exact value `R(B10,B10)=42` is already settled by prior art. This candidate must leave the frontier queue as a rediscovery rather than advance toward publication or Lean sealing.

## minimal_repair_if_any
No mathematical repair is needed.

The only required correction is classification:

- demote the run from frontier candidate status to `REDISCOVERY`
- preserve the Paley witness as an independently checked rederivation, not as a new result
