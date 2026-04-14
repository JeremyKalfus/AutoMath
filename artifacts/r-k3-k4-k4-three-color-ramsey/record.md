# Solve Record: r-k3-k4-k4-three-color-ramsey

## statement_lock
- Active slug: `r-k3-k4-k4-three-color-ramsey`
- Active title: `Determine the exact value of R(K3, K4, K4)`
- Exact intended statement for this solve run: determine whether every 3-coloring of `E(K_21)` already forces a color-1 `K3` or a color-2 `K4` or a color-3 `K4`; equivalently decide whether `R(K3,K4,K4)=21` or `22`.
- Candidate title theorem if the solve closes: `R(K3,K4,K4)=22` or `R(K3,K4,K4)=21`, depending on the endpoint.
- Paper-shape note: if the endpoint is fixed honestly, that is already about `0.8` of a micro-paper packet by the selection packet's own assessment.

## definitions
- Use standard multicolor Ramsey notation: `R(H1,H2,H3)` is the least `n` such that every 3-coloring of `E(K_n)` contains a color-1 copy of `H1`, a color-2 copy of `H2`, or a color-3 copy of `H3`.
- Let the colors be `red`, `blue`, and `green`, with forbidden monochromatic subgraphs `red K3`, `blue K4`, and `green K4`.
- A `22`-vertex counterexample means a coloring of `K_22` avoiding all three forbidden monochromatic subgraphs.
- A `21`-vertex lower-bound certificate means a coloring of `K_21` avoiding all three forbidden monochromatic subgraphs.
- Packet ambiguity to resolve in verification: the working packet says both `21 <= R(K3,K4,K4) <= 22` and that a `21`-vertex avoiding coloring is already known. Under standard notation, a `21`-vertex avoiding coloring would imply `R(K3,K4,K4) >= 22`, so together with the cited upper bound `<= 22` the problem would already be closed at `22`. The most likely explanation is that the packet's lower-bound wording or toy-example sentence is off by one.

## approach_A
- Structural / invariant route: assume a `22`-vertex counterexample and analyze colored neighborhoods around a vertex `v`.
- Immediate local bound: `|N_red(v)| <= 17`, because edges inside `N_red(v)` cannot be red and therefore form a 2-coloring in blue/green with no monochromatic `K4`; this is bounded by `R(K4,K4)-1 = 17`.
- This gives a necessary condition for any `22`-vertex counterexample but does not by itself rule one out, because it only forces `d_blue(v)+d_green(v) >= 4`.
- Similar analysis on `N_blue(v)` or `N_green(v)` is weaker without importing additional exact small multicolor Ramsey values not present in the packet.
- Self-check: this route is mathematically sound at the local-lemma level, but the current packet does not provide enough adjacent exact values or SDP constraints to close the one-step gap by hand.

## approach_B
- Construction / extremal route: search for a highly symmetric `21`-vertex lower-bound coloring.
- The smallest credible construction family here is circulant colorings on `Z_21`, where each distance class `1,2,...,10` is assigned one of the three colors.
- This search space has size `3^10 = 59049`, which is small enough for a bounded certificate search and still structured enough to keep the solve reasoning-first rather than generic brute force.
- If a valid `21`-vertex circulant coloring exists, then combined with the cited literature upper bound `R(K3,K4,K4) <= 22`, the solve would produce a strong exact-value candidate for `R(K3,K4,K4)=22`.
- If no such circulant example exists, that does not decide the problem, but it gives a clean negative boundary on one natural extremal template.
- Self-check: this route is the best use of minimal code because the packet already frames the lower-bound side as certificate-compact and paper-shaped if found.

## lemma_graph
- Lemma 1: In any avoiding coloring, `N_red(v)` contains no red edges.
- Lemma 2: Therefore the induced coloring on `N_red(v)` is blue/green only and avoids blue `K4` and green `K4`.
- Lemma 3: Hence `|N_red(v)| <= 17`.
- Lemma 4: A `21`-vertex explicit avoiding coloring would imply `R(K3,K4,K4) >= 22`.
- Lemma 5: Combined with the cited source upper bound `R(K3,K4,K4) <= 22`, such a certificate would identify the exact value as `22`.
- Failure branch: if only a structured-subfamily nonexistence result is obtained, the main claim remains open and the result is only a partial slice.

## chosen_plan
- Best path: pursue Approach B with a tightly bounded circulant search on `21` vertices, because an explicit certificate would already be theorem-shaped and the structural route currently stalls at necessary conditions.
- Pre-code decision: the reasoning stage has identified one honest structural lemma and one honest constructive route; no broader search will be attempted.
- What extra structure would make the result paper-shaped if the main claim closes?
- Answer: an explicit `21`-vertex coloring certificate, a short verification script or compact proof of avoidance, and one boundary remark explaining why the same template does or does not extend to `22` vertices.

## self_checks
- Check after statement lock: the endpoint question is well-posed, but the packet contains an indexing inconsistency that verification must resolve.
- Check after approaches: Approach A yields a usable local lemma; Approach B is the only path likely to produce a paper-shaped artifact inside the current scope.
- Check after code: the first bounded search found a `21`-vertex circulant certificate and, more importantly, a `22`-vertex circulant certificate.
- Independent exhaustive recheck over all `3`-subsets and `4`-subsets confirmed both certificates are clean, so the `22`-vertex object should be treated as a serious counterexample candidate to the packet's stated upper bound.

## code_used
- Yes.
- Bounded code only, after the reasoning stage:
- Search 1: exhaustive search over all `3^10 = 59049` circulant 3-colorings of `K_21` indexed by distance classes `1,...,10`.
- Search 2: exhaustive search over all `3^11 = 177147` circulant 3-colorings of `K_22` indexed by distance classes `1,...,11`.
- Independent verifier: direct enumeration of all `3`-vertex and `4`-vertex subsets for the returned assignments.
- Returned `21`-vertex circulant assignment on distances `1..10`:
- `RBRBRGBBGB`
- So red distances are `{1,3,5}`, blue distances are `{2,4,7,8,10}`, and green distances are `{6,9}`.
- Returned `22`-vertex circulant assignment on distances `1..11`:
- `RBRBRGRBRGR`
- So red distances are `{1,3,5,7,9,11}`, blue distances are `{2,4,8}`, and green distances are `{6,10}`.

## result
- Strong result: there is an explicit `22`-vertex 3-coloring avoiding a red `K3`, a blue `K4`, and a green `K4`.
- Therefore the active packet's endpoint question `21 or 22?` is not compatible with this witness under standard notation; the witness proves at least `R(K3,K4,K4) >= 23`.
- Concrete construction on vertices `Z_22`:
- Color edge `{x,y}` red when `x-y mod 22` is an odd distance, namely one of `1,3,5,7,9,11`.
- Color edge `{x,y}` blue when the circular distance is in `{2,4,8}`.
- Color edge `{x,y}` green when the circular distance is in `{6,10}`.
- Structural description:
- The red graph is exactly the complete bipartite graph `K_11,11` given by the parity split, hence red-triangle-free.
- Blue and green edges lie inside the two parity classes; on each `11`-vertex class they become complementary circulant graphs with step sets `{1,2,4}` and `{3,5}` respectively.
- Exhaustive verification confirms neither the blue graph nor the green graph contains a `K4`.
- Immediate theorem slice suggested by the current solve output:
- `R(K3,K4,K4) >= 23`.
- Immediate corollary / boundary remark:
- The specific `21` vs `22` frontier in the active packet cannot be correct as written if standard Ramsey indexing is intended.

## family_affinity
- Strongest current affinity is now to compact lower-bound constructions for small multicolor clique Ramsey numbers, especially symmetric constructions that invalidate a claimed table endpoint.

## generalization_signal
- What scales:
- The parity-split template on even `n` naturally enforces the red triangle-free condition by taking red to be complete bipartite.
- The lower-bound method "bipartite red layer plus two-color circulant split inside each side" plausibly extends to nearby mixed-clique parameters.
- What does not yet scale:
- The exact blue/green step sets `{2,4,8}` and `{6,10}` were found by search; there is not yet a conceptual proof that this template extends beyond the single `n=22` instance.

## proof_template_reuse
- Reusable template:
- Split an even-order complete graph into two parity classes.
- Put all cross-part edges in the triangle-forbidden color.
- Search or design two complementary circulant `K4`-free graphs on each parity class for the remaining two colors.
- Verify the resulting lower-bound certificate exhaustively.

## candidate_theorem_slice
- Cleanest honest theorem slice from this run:
- `There exists a circulant 3-coloring of K_22 with no red K3, no blue K4, and no green K4; in particular R(K3,K4,K4) >= 23.`

## smallest_param_shift_to_test
- First shift: test whether the same parity-split circulant template yields a `23`-vertex or larger lower bound after adapting the odd-order geometry.
- Second shift: test nearby mixed-clique tuples such as `(K3,K4,K4-e)` or `(K3,K4,K5)` for the same bipartite-plus-circulant proof template.

## why_this_is_or_is_not_publishable
- If the `22`-vertex witness survives verification against the cited source and novelty check, the result is no longer a thin instance: it becomes a real theorem slice and could be the core of a short note correcting the active frontier to at least `23`.
- A successful exact solve would still be 70-90% of a micro-paper, but the current run does not close the exact value; it supplies a lower-bound counterexample candidate instead.
- Minimal remaining packaging work is:
- verify the cited theorem table directly,
- normalize the circulant construction into publishable notation,
- check whether this exact `22`-vertex construction is already known,
- decide whether the right publication claim is a corrected lower bound or a literature-audit correction rather than an exact value note.
- Current package assessment: stronger than `instance-only` mathematically, but still too unstable publication-wise until verification resolves the source conflict.

## paper_shape_support
- Exact title theorem if the current counterexample is verified and novel:
- `A 22-Vertex Lower-Bound Construction for R(K3,K4,K4)`.
- If a later stage also sharpens the upper bound to match, the title theorem would revert to the exact-value note, but that is not what this run proved.
- The smallest support making this paper-shaped is already visible:
- one explicit circulant construction,
- one short proposition proving the red layer is bipartite,
- one machine-checkable certificate that the blue and green layers are `K4`-free,
- one exact sentence explaining that this invalidates the packet's `21/22` endpoint.

## boundary_remark
- Boundary remark actually obtained:
- the same search family survives on `22` vertices, so the original `21` versus `22` dichotomy is not the correct live boundary for this tuple if standard notation is intended.
- A useful descriptive remark is that the `22`-vertex witness saturates Mantel in the red color via `K_11,11`, and pushes the complexity entirely into a two-color `K4`-avoidance problem on each `11`-vertex parity class.

## likely_failure_points
- The packet's lower-bound sentence may be off by one, which could make a rediscovered `21`-vertex certificate non-novel or show the problem was already closed in the cited source.
- The true lower-bound construction may be non-circulant, so a negative circulant search would not be mathematically decisive.
- The most serious remaining risk is not mathematical but bibliographic: the packet's claimed upper bound `<= 22` may simply be wrong for this tuple, or the tuple/source may have been mis-copied.
- The literature upper bound is used only as a packet claim here and is now in direct tension with the explicit `22`-vertex witness.

## what_verify_should_check
- Verify the off-by-one ambiguity in the packet: does the cited source give a `20`-vertex or a `21`-vertex avoiding coloring?
- Verify the `22`-vertex construction independently from the written distance-set description, not just by rerunning the same search code.
- Confirm whether the exact theorem table entry in the cited 2021 source is truly `21 <= R(K3,K4,K4) <= 22`, or whether the tuple / bound was copied incorrectly into the packet.
- Check whether the explicit circulant `22`-vertex witness is already known in the literature or in computational databases.

## verify_rediscovery
- PASS 1 result: rediscovery is established within budget.
- The cited 2021 source does not support the packet's claim `21 <= R(K3,K4,K4) <= 22`. In Theorem 8, the `22` upper bound is for `R(K3, K4-e, K4-e)`, not for `R(K3, K4, K4)`.
- The same 2021 paper's appendix table lists `55 <= R(K3, K4, K4) <= 77`, so the solver's claimed theorem slice `R(K3,K4,K4) >= 23` is already directly implied by published prior art.
- Bounded web pass found no exact closure for `R(K3,K4,K4)` through the limited audit window, but that does not matter for this run because the solver's claim is already a non-novel lower bound.
- Therefore this run cannot remain on an exact-value lane and must be marked `REDISCOVERY`.

## verify_faithfulness
- The run is not faithful to the intended statement.
- Intended statement in the active packet: decide whether `R(K3,K4,K4)` equals `21` or `22`.
- Actual cited source support: `21 <= R(K3, K4-e, K4-e) <= 22`, plus a separate appendix entry `55 <= R(K3,K4,K4) <= 77`.
- Actual solver output: an explicit `22`-vertex avoiding coloring, i.e. a lower-bound witness for `R(K3,K4,K4) >= 23`.
- So there are two layers of drift:
- packet/source drift: `K4-e` was copied as `K4`;
- theorem drift: the solver produced a lower-bound slice, not an exact-value determination.
- If rediscovery were ignored, the right faithfulness label would be `VARIANT`, but the bounded prior-art pass forces the overall verdict to `REDISCOVERY`.

## verify_proof
- For the mathematical content actually written down, no flaw was found in the `22`-vertex construction itself.
- First incorrect step in the solve packet: treating the active packet's bibliographic claim as an upper bound on `R(K3,K4,K4)` and interpreting the witness as a contradiction to the literature.
- That step fails because the packet miscopied the source tuple.
- Conditional on the written distance sets, the proof that the red layer is bipartite is correct, and the exhaustive finite check for blue/green `K4`-avoidance is the right correctness criterion.
- So the proof object is acceptable as a rediscovered lower-bound witness, but not as evidence against the literature and not as progress on the intended exact claim.

## verify_adversarial
- No candidate-local checker file exists, so I reran an independent minimal verifier directly from the written `K_22` distance sets.
- Independent exhaustive check on all `3`-subsets and `4`-subsets of `V(K_22)` returned:
- red triangles: `0`
- blue `K4`: `0`
- green `K4`: `0`
- The parity-split description also checks out: all odd distances are red, giving the complete bipartite graph `K_{11,11}`, and no same-parity edge is red.
- Adversarial conclusion: the construction survives local mathematical attack, but it does not support a frontier claim because the literature already gives a much stronger lower bound.

## verify_theorem_worthiness
- Exactness: not exact; the run does not determine `R(K3,K4,K4)`.
- Novelty: none; the claimed lower-bound consequence is already implied by published prior art.
- Reproducibility: high for the specific `22`-vertex witness; the certificate is compact and independently checkable.
- Lean readiness: no. Formalizing a rediscovered lower-bound witness would not be the shortest path to a sealed publication packet.
- Paper leverage: none for the current claim, because the honest output is bibliographic correction plus rediscovered mathematics.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
- No. Not in its current form, because the visible claim is already subsumed by known lower bounds.
- What percentage of the paper would one solve already provide?
- `0.0` for the active claim as verified, since there is no frontier-novel theorem left in this packet.
- What title theorem is actually visible?
- At best: `There exists a 22-vertex coloring witnessing R(K3,K4,K4) >= 23`, but this is rediscovered and publication-insufficient.
- What part of the argument scales?
- The parity-split plus finite certificate verification template scales as a construction method.
- What part clearly does not?
- The publication claim does not scale at all, because the packet is anchored to a miscopied source and the claimed frontier is false.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`?
- Neither. Under the required status vocabulary this run is `REDISCOVERY`.

## verify_verdict
- `verify_verdict = REDISCOVERY`
- Reason: the active packet miscopied the source tuple, and the solver's `K_22` witness only re-establishes a weak lower bound already implied by published literature.
- Required downstream action: `archive_as_rediscovery`.

## minimal_repair_if_any
- Tiny conservative repair only:
- keep the `K_22` construction as a checked witness artifact in the record;
- mark the packet as a rediscovery caused by source-faithfulness drift;
- do not treat this run as evidence about the exact value of `R(K3,K4,K4)`.
