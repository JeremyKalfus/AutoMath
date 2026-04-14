# Solve Record: Determine the exact value of R(B19, B19)

## statement_lock
Active slug: `r-b19-b19-diagonal-book-ramsey`.

Active title: `Determine the exact value of R(B19, B19)`.

Locked target: decide whether every red-blue coloring of `K_77` already forces a monochromatic `B19`, since the queued frontier input is `77 <= R(B19, B19) <= 78`.

Convention: `B19` is the book with 19 pages, i.e. one spine edge together with 19 additional vertices each adjacent to both spine endpoints. In a color class, a monochromatic `B19` is therefore equivalent to an edge lying in at least 19 monochromatic triangles.

Exact title theorem if this closes on the upper-bound side: `R(B19, B19) = 77`.

If instead a 77-vertex witness exists, the exact title theorem would be `R(B19, B19) = 78`.

This still passes the 70-90% paper test: settling the endpoint is already the title theorem of a short note, and the remaining packaging would be a short frontier comparison plus a compact proof or witness description.

## definitions
Let `G` be the red graph of a red-blue coloring of `K_n`; the blue graph is the complement.

For an edge `uv` in `G`, let `tau_R(uv) = |N_G(u) ∩ N_G(v)|`. Then `G` is `B19`-free exactly when `tau_R(uv) <= 18` for every red edge `uv`.

For a blue edge `uv`, the same condition in the blue graph says the number of common blue neighbors of `u,v` is at most 18.

Let `T_R` and `T_B` be the numbers of red and blue triangles.

## approach_A
Structural / invariant route: use triangle counting plus Goodman's theorem at the knife-edge order `n = 77`.

If a coloring of `K_77` avoids monochromatic `B19`, then every monochromatic edge lies in at most 18 monochromatic triangles. Summing over edges gives

`3 T_R <= 18 e_R`, hence `T_R <= 6 e_R`,

and likewise `T_B <= 6 e_B`.

Adding,

`T_R + T_B <= 6(e_R + e_B) = 6 * binom(77,2) = 17556`.

Goodman's bound gives

`T_R + T_B >= binom(77,3) - (1/2) * sum_v d(v)(76 - d(v)) >= 77*76*72/24 = 17556`,

with equality in the last step only when every red degree is exactly 38.

So the upper and lower bounds coincide. Any 77-vertex coloring with no monochromatic `B19` must therefore be extremal in every place where slack was available.

## approach_B
Construction / extremal route: if `R(B19, B19) = 78`, then there must exist a 77-vertex critical coloring. Try to understand what such a witness would have to look like before attempting any search.

The equality forced by the triangle count means a critical witness cannot be merely approximate. It must be perfectly balanced: each vertex has red degree 38 and blue degree 38, and every monochromatic edge lies in exactly 18 monochromatic triangles.

That turns the constructive problem into a much narrower object-existence question: does there exist a 38-regular graph on 77 vertices with every edge in exactly 18 triangles and every nonedge in exactly 19 red common neighborhoods?

So the witness side is not a generic search problem. It is the existence of a conference-graph / strongly-regular structure.

## lemma_graph
1. Assume a red-blue coloring of `K_77` has no monochromatic `B19`.
2. Then each red edge lies in at most 18 red triangles, and each blue edge lies in at most 18 blue triangles.
3. Hence `T_R + T_B <= 6 * binom(77,2) = 17556`.
4. Goodman's theorem gives `T_R + T_B >= 17556`, so equality holds.
5. Equality forces every vertex to have red degree 38 and every monochromatic edge to lie in exactly 18 monochromatic triangles.
6. For a red nonedge `uv`, the blue-edge equality implies the number of common red neighbors is exactly 19.
7. Therefore the red graph is `srg(77,38,18,19)`, equivalently a conference graph on 77 vertices.
8. A conference graph on 77 vertices yields a symmetric conference matrix of order 78.
9. Standard conference-matrix number theory says order 78 is impossible because `77` is not a sum of two integer squares.
10. Therefore no such coloring of `K_77` exists, so the queued upper bound sharpens to `R(B19, B19) = 77`.

## chosen_plan
Pursue Approach A to force exact extremality, then convert the critical-coloring question into the existence question for `srg(77,38,18,19)`.

If that reduction is correct, the cleanest finish is the standard conference-matrix obstruction at order 78. This is the shortest route to a paper-shaped exact-value note because it avoids brute force and turns the endpoint into a rigid algebraic object.

## self_checks
Self-check after statement lock: the only live endpoint question is `77` versus `78`, so working entirely at `n = 77` is correct.

Self-check after Approach A: the arithmetic is exact. `6 * binom(77,2) = 6 * 2926 = 17556`, and Goodman's odd-order lower bound is also `77*76*72/24 = 17556`.

Self-check after equality extraction: since both colors individually satisfy edge-triangle upper bounds and the sum hits the global maximum, every red edge and every blue edge must actually attain the local value 18.

Self-check after the nonedge count: if `u,v` are nonadjacent in the red graph and `mu = |N_G(u) ∩ N_G(v)|`, then common blue neighbors equal `75 - (38 + 38 - mu) = mu - 1`, so blue-edge equality gives `mu = 19`.

Self-check on scope: the only imported non-local ingredient in the final contradiction is the standard nonexistence criterion for symmetric conference matrices of order `n` with `n-1` not a sum of two squares. That point is the main verify-stage dependency.

## code_used
No code used.

Reasoning was sufficient to isolate the extremal structure, and the dossier is explicitly not marked `search_heavy`. Starting with SAT, brute force, or generic optimization would have violated the solve policy here.

## result
Candidate conclusion: `R(B19, B19) = 77`.

Proof attempt.

Assume for contradiction that there is a red-blue coloring of `K_77` with no monochromatic `B19`. Let `G` be the red graph. Since a monochromatic `B19` is an edge contained in at least 19 monochromatic triangles, every red edge lies in at most 18 red triangles and every blue edge lies in at most 18 blue triangles.

Counting triangles through edges gives

`T_R <= 6 e_R`, `T_B <= 6 e_B`,

so

`T_R + T_B <= 6(e_R + e_B) = 6 * binom(77,2) = 17556`.

On the other hand, Goodman's theorem gives

`T_R + T_B >= 77*76*72/24 = 17556`.

Hence equality holds throughout. In particular:

- every vertex has red degree exactly 38,
- every red edge has exactly 18 red common neighbors,
- every blue edge has exactly 18 blue common neighbors.

Now take a red nonedge `uv`. Since the red graph is 38-regular on 77 vertices, if `mu = |N_G(u) ∩ N_G(v)|`, then the number of vertices adjacent to neither `u` nor `v` in red is

`75 - (38 + 38 - mu) = mu - 1`.

But that quantity is exactly the number of common blue neighbors of `u,v`, and blue-edge equality says it must equal 18. Therefore `mu = 19`.

So any putative 77-vertex extremal coloring yields a strongly regular graph with parameters

`(v,k,lambda,mu) = (77,38,18,19)`.

These are the conference-graph parameters for `v = 77`. Equivalently, if `A` is the adjacency matrix and `S = J - I - 2A` is the Seidel matrix, then `S 1 = 0` and `S^2 = 77 I - J`. From this one obtains the symmetric conference matrix

`C = [[0, 1^T], [1, S]]`,

which satisfies `C^2 = 77 I_78`.

At this point the solve reduces to a standard arithmetic obstruction: a symmetric conference matrix of order 78 can exist only when `77` is a sum of two squares. But `77 = 7 * 11` is not a sum of two squares.

Therefore no such conference matrix exists, hence no such coloring of `K_77` exists. Combined with the queued frontier bound `77 <= R(B19, B19) <= 78`, this yields the candidate exact value

`R(B19, B19) = 77`.

Conservatively: the conference-obstruction step is the one place that still needs verify-stage checking and citation support. If that step is confirmed, the solve is essentially complete and paper-shaped.

## family_affinity
This sits exactly in the diagonal book-Ramsey one-step-gap lane. The structural reduction is unusually clean because `n = 77 = 4*19 + 1` is the odd-order point where Goodman's lower bound meets the monochromatic-book upper count with no slack.

## generalization_signal
There is a genuine family signal here. The same argument shows:

If a red-blue coloring of `K_{4m+1}` avoids a monochromatic `B_m`, then equality in the same triangle-count argument forces the red graph to be `srg(4m+1, 2m, m-1, m)`, i.e. a conference graph.

So any one-step diagonal book gap at the order `4m+1` naturally reduces to a conference-graph existence question.

## proof_template_reuse
Reusable template:

1. convert `B_m`-avoidance into an edgewise triangle cap;
2. compare the induced global triangle upper bound against Goodman's lower bound at the knife-edge order `4m+1`;
3. exploit equality to force regularity and exact local counts;
4. identify the extremal object as a conference graph or related strongly regular graph;
5. finish by existence or nonexistence of that algebraic object.

The scalable part is the Goodman-tightness reduction. The non-scalable part is the final existence obstruction, which depends on the arithmetic of the specific conference-graph order.

## candidate_theorem_slice
Primary slice:

Any red-blue coloring of `K_77` with no monochromatic `B19` induces a strongly regular graph `srg(77,38,18,19)`.

Stronger family-shaped slice:

Any red-blue coloring of `K_{4m+1}` with no monochromatic `B_m` induces a conference graph with parameters `srg(4m+1,2m,m-1,m)`.

This slice is theorem-shaped and reusable even if the final conference-obstruction citation needs verify-stage confirmation.

## smallest_param_shift_to_test
The first useful parameter shift is the neighboring diagonal case `m = 20`, because the same reduction would point to a conference graph on 81 vertices. That tests whether the `m = 19` closure is an arithmetic obstruction phenomenon or part of a broader diagonal pattern.

The second useful shift is any other one-step diagonal book gap at `n = 4m+1`, since the same proof skeleton would apply unchanged through the reduction stage.

## why_this_is_or_is_not_publishable
If the conference-obstruction step verifies cleanly, this is publishable in the micro-paper lane.

Why: the exact title theorem would be `R(B19, B19) = 77`; the result already clears the 70-90% paper threshold because it closes a named one-step frontier gap; the remaining packaging is small; and the solve naturally supplies one reusable slice explaining why the endpoint reduces to a rigid algebraic object.

Without verification of the conference-matrix obstruction, the current package is still too thin for publication. It would then be a strong theorem-facing reduction, not yet an exact-value paper.

## paper_shape_support
If the main claim closes, the smallest extra structure needed for paper shape is:

- the conference-graph reduction as the main lemma package;
- one short paragraph citing the prior interval `77 <= R(B19, B19) <= 78`;
- one exact sentence explaining that the obstruction is arithmetic rather than search-based;
- one boundary remark identifying the 77-vertex critical object that would otherwise have to exist.

Minimal remaining packaging work after a verified closure:

- add the conference-matrix citation and verify the specialized nonexistence statement;
- write the Goodman-tightness proof cleanly;
- place the result next to the neighboring almost-diagonal exact value already recorded in the packet.

## boundary_remark
Natural boundary remark: the solve does not produce a 77-vertex witness. Instead it says any such witness would have to be a conference graph of order 77, so the endpoint is controlled by algebraic existence rather than an unstructured combinatorial search.

Immediate corollary / remark if the closure stands: every extremal coloring at the knife-edge order would have to be exactly balanced and strongly regular; there is no room for an irregular near-extremal counterexample.

## likely_failure_points
The main risk is the last step: the nonexistence criterion for symmetric conference matrices of order 78 must be checked carefully and cited correctly.

Secondary risk: verify should confirm the exact equivalence between the `srg(77,38,18,19)` object and the symmetric conference-matrix construction used here.

The reduction up to the conference-graph existence question looks robust and arithmetic-exact.

## what_verify_should_check
Check the Goodman equality argument line by line and confirm there is no off-by-one error in the triangle counts.

Check the conversion from a 77-vertex `B19`-free coloring to `srg(77,38,18,19)`.

Check the conference-matrix construction `C = [[0, 1^T], [1, S]]` and the identity `C^2 = 77 I_78`.

Check the exact standard theorem used in the final contradiction: symmetric conference matrix of order 78 impossible because `77` is not a sum of two squares.

Check whether the generalized slice for `K_{4m+1}` and `B_m` is already folklore in the literature, since it is reusable and could matter for framing.

## verify_rediscovery
PASS 1 used a bounded web audit on 2026-04-14 with exact-instance, alternate-notation, canonical-source-title, and recent-family-status queries.

The 2025 Electronic Journal of Combinatorics paper remained the canonical anchor for the interval `77 <= R(B19, B19) <= 78`; the bounded pass did not surface an explicit later theorem, proposition, example, observation, or corollary settling the exact diagonal `B19` endpoint.

The 2026 Wesley paper surfaced as family-status context for lower bounds in the book-Ramsey line, but the bounded pass did not reveal an exact closure of `R(B19, B19)` there either.

The exact-instance queries were somewhat noisy because `B19` collides with unrelated indexing and biomedical terms, so the strongest part of the audit came from the canonical-source and family-title anchors rather than raw tuple search.

Conservative rediscovery verdict: not established within the bounded pass. Novelty remains plausible, but this verify run does not claim a fully exhaustive literature certification.

## verify_faithfulness
The solve record is faithful to the selected theorem. The intended statement is the exact diagonal book Ramsey value `R(B19, B19)`, and the solver correctly narrows the live task to the missing upper-bound endpoint on `K_77` because the packet imports the prior interval `77 <= R(B19, B19) <= 78`.

I did not find wrong-theorem drift, quantifier drift, or a swap to a weaker proxy statement. The only extra material beyond the intended theorem is the family-shaped conference-graph discussion, which is clearly presented as reuse signal rather than as the selected claim itself.

## verify_proof
I did not find an incorrect internal step before the final imported obstruction.

The local combinatorial chain checks out:

- `B19`-avoidance is equivalent to every monochromatic edge lying in at most `18` monochromatic triangles.
- Summing edgewise triangle counts gives `T_R <= 6 e_R` and `T_B <= 6 e_B`.
- Goodman's lower bound at `n = 77` matches the same value `17556`, and equality forces every red degree to be `38`.
- Equality in the edgewise caps then forces every red edge to have exactly `18` red common neighbors and every blue edge to have exactly `18` blue common neighbors.
- For a red nonedge `uv`, the count of common blue neighbors is `75 - (38 + 38 - mu) = mu - 1`, so blue-edge equality yields `mu = 19`.
- Hence any extremal coloring indeed induces `srg(77,38,18,19)`.

The first unsupported step is the imported arithmetic obstruction: the claim that a symmetric conference matrix of order `78` can exist only when `77` is a sum of two squares. That statement is likely standard and likely true, but it is not independently derived or cited precisely inside the packet.

So the strongest fully checked in-file claim from this verify run is:

`If a red-blue coloring of K_77 avoids a monochromatic B19, then its red graph is srg(77,38,18,19).`

The exact-value conclusion `R(B19, B19) = 77` is therefore still conditional on the standard conference-matrix nonexistence theorem used in the last step.

## verify_adversarial
No checker or code artifact exists for this slug, so there was nothing to rerun.

I rechecked the arithmetic directly:

- `6 * binom(77,2) = 17556`.
- Goodman's odd-order lower bound at `77` is also `17556`.
- The nonedge common-neighbor conversion has no off-by-one error.
- `77` is not a sum of two integer squares.

I also tried to break the reduction by looking for slack between the local triangle caps and the global Goodman equality. I did not find any. Once the bounds meet exactly, the regularity and exact local common-neighbor counts really are forced.

The remaining adversarial failure mode is not the local counting argument; it is only the imported conference-matrix theorem and the need for an exact citation or fully sealed reference.

## verify_theorem_worthiness
Exactness: the endpoint theorem is exact if the final conference-matrix obstruction is verified cleanly.

Novelty: bounded PASS 1 did not establish rediscovery.

Reproducibility: the Goodman-tightness reduction is reproducible from the current record; the last arithmetic obstruction still needs a precise source anchor.

Lean readiness: not yet. Lean is not the shortest remaining path because the binding bottleneck is still source-level confirmation of the final conference-matrix theorem, not formalization of a fully sealed claim.

Would this result, if correct and Lean-sealed, already constitute most of a publishable note? Yes. It would already provide roughly `0.76` of the paper.

What title theorem is actually visible? `R(B19, B19) = 77`.

What part of the argument scales? The Goodman-tightness reduction from `B_m`-avoidance on `K_{4m+1}` to conference-graph parameters.

What part clearly does not? The final algebraic existence or nonexistence step, which is order-specific arithmetic rather than a uniform combinatorial closure.

Best honest publication status now: `SLICE_CANDIDATE`. This is stronger than `INSTANCE_ONLY` because the visible title theorem is already paper-shaped, but weaker than any sealed exact-publication status because the last imported theorem remains uncited and unsealed here.

## verify_verdict
`SURVIVES_WITH_EXTERNAL_THEOREM_DEPENDENCY`

Conservative verdict: not a rediscovery, faithful to the selected theorem, and internally sound through the reduction to `srg(77,38,18,19)`. The packet should remain classified as `CANDIDATE`, not `EXACT`, until the final conference-matrix obstruction is verified with a precise citation or equivalent sealed justification.

## minimal_repair_if_any
No mathematical patch was applied.

The minimal conservative repair is presentational: rewrite the final sentence of the solve as conditional until the imported theorem is pinned down exactly.

Suggested repaired closing sentence:

`Assuming the standard nonexistence criterion for symmetric conference matrices of order 78, the above reduction yields R(B19, B19) = 77.`

## publication_prior_art_audit
Audit date: `2026-04-14`.

Exact-statement searches for `R(B19, B19)`, `R(B19,B19)=77`, and `R(B_{19},B_{19})` were noisy but pointed back to the same small set of book-Ramsey sources rather than to a new exact-value paper.

Alternate-notation search for `book Ramsey 19 77 78` likewise pointed back to the 2025 canonical source family.

Canonical-source check changed the verdict decisively. In Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1 states `4n+1 <= R(B_n,B_n) <= 4n+2` for `4 <= n <= 21`. The note immediately under that theorem says it was already known that `R(B_n,B_n) <= 4n+1` whenever `4n+1` is not a sum of two squares.

At `n = 19`, that note already gives `R(B19, B19) <= 77`, while Theorem 1 gives `R(B19, B19) >= 77`. Since `77` is not a sum of two integer squares, the exact value `R(B19, B19) = 77` is already implied inside the canonical source packet itself.

The theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source therefore terminates at Theorem 1 plus its accompanying note; no extra interpretive jump is needed.

Outside-source status pass: William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026) served as the bounded recent-family check. That pass did not create a conflicting later status; the rediscovery conclusion was already forced by the canonical source.

No extra citation-follow-up pass was needed after that because the claim was no longer ambiguous.

Conservative prior-art verdict: `REDISCOVERY`.

## publication_statement_faithfulness
The solver stayed on the correct theorem. The reduction from a hypothetical `B19`-free coloring of `K_77` to `srg(77,38,18,19)` is faithful to the intended statement and does not drift to a weaker proxy.

The failure was not theorem drift but literature-gap drift. The selected packet described the frontier as `77 <= R(B19, B19) <= 78`, but the same cited canonical source already closes the `n = 19` endpoint once its note on the non-sum-of-two-squares upper bound is read together with Theorem 1.

So the mathematics in the record is statement-faithful, while the packet-level novelty framing was not.

## publication_theorem_worthiness
Is the strongest honest claim stronger than "here is an example"? Yes. The mathematical statement `R(B19, B19) = 77` is a genuine exact-value theorem.

Is there a real title theorem or theorem slice here? Yes. The title theorem is real, and the local reduction to `srg(77,38,18,19)` is also a real structural slice.

Is the proof structural or merely instance-specific? Structural. The known upper bound is a family statement for diagonal book Ramsey numbers at orders `4n+1` that are not sums of two squares, and the local Goodman-tightness reduction also has family shape.

Would this survive a referee asking "what is the theorem?" Yes. It would fail instead on "why is this new?" because the exact theorem is already available in prior work.

Is the claim too dependent on hand-picked small cases? No. The problem is not small-case fragility but rediscovery.

## publication_publishability
If this exact value were still open, the packet would be close to a publishable short note. The theorem is crisp, the proof route is compact, and the narrative is already title-theorem shaped.

After audit, that is no longer the relevant question. As a frontier publication packet this is not paper-ready, not because the remaining gap is small, but because the novelty gap is already zero in the wrong direction: the result is known.

Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No as a frontier note. At that point it would be an independent rederivation or archival formalization of a known theorem.

If this is not paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? It only looked attractive before audit. The packet underread the canonical source.

If this is not paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Do not salvage this by growing the scope. Mark it as rediscovered and move on.

Would Lean directly seal the packet, or would it only be optional polish? Only optional polish or archival formalization. Lean does not restore publication novelty here.

## publication_packet_audit
Current packet quality as a frontier packet: not viable.

Current packet quality as a preserved mathematical artifact: useful. The solve record contains a clean alternate route through Goodman tightness and conference-graph structure, and those proof artifacts should be kept.

The strongest honest current contribution is therefore not a new exact-value paper, but an internally coherent rederivation path for a theorem already implied by the literature.

## micro_paper_audit
Micro-paper verdict: fail the active one-shot lane for this slug.

What percentage of a publishable note would one solve now provide? About `0.12` at most, because the novelty-bearing theorem is already known. Most of the remaining work would be to find a new claim, not to finish this packet.

Would the result, if Lean-sealed, already constitute most of a publishable note? No.

Is there still a real theorem here? Yes, but it is already settled in prior art.

Does the packet still clear the micro-paper objective? No. The micro-paper lane requires a frontier theorem slice, and this audit shows that the selected endpoint is not frontier-novel.

## strongest_honest_claim
The exact value `R(B19, B19) = 77` is already implied by existing literature, specifically the 2025 canonical source's Theorem 1 together with its accompanying note on the known upper bound `R(B_n,B_n) <= 4n+1` when `4n+1` is not a sum of two squares. The current artifact's honest value is an alternative derivation route through the forced strongly regular graph `srg(77,38,18,19)`.

## paper_title_hint
No frontier micro-paper title is available for this slug. At most: `An Alternative Derivation of the Known Value R(B19, B19) = 77`.

## next_action
Mark this slug `REDISCOVERY`, preserve the conference-graph reduction as a reusable proof artifact, and move the queue back to a fresh frontier candidate rather than expanding this case into a broader theorem program.
