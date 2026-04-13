# statement_lock
Slug: `five-regular-pseudograph-4-1-factor`.

Title: `Does every 5-regular pseudograph contain a {4,1}-factor?`

Exact intended statement for solve: either prove that every 5-regular pseudograph admits a spanning subgraph with vertex-degrees in `{4,1}`, or exhibit a genuine counterexample pseudograph together with a direct exclusion of all `{4,1}`-factors.

Working reformulation used here: for a 5-regular pseudograph `G`, a `{4,1}`-factor is equivalent to a labeling `w : E(G) -> {1,2}` such that the weighted incidence sum at every vertex is `0 mod 3`, with loops counted twice in both degree bookkeeping and the vertex-sum. The conversion is: edges of the factor receive label `1`, non-factor edges receive label `2`, and then each vertex sum is `d_F(v) + 2(5-d_F(v)) = 10 - d_F(v)`, so the sum is `0 mod 3` exactly when `d_F(v)` is `1` or `4`.

# definitions
- Degree convention: loops contribute `2` to the degree.
- In the mod-3 reformulation, a loop also contributes its label twice to the vertex sum.
- A minimal counterexample means vertex-minimal unless explicitly stated otherwise.
- Because `5|V(G)| = 2|E(G)|`, every 5-regular pseudograph has even order; this removes the most obvious parity obstruction.

Ambiguities or load-bearing conventions:
- The reformulation is only safe if loops are counted twice in the vertex sum; that is the convention used below.
- A counterexample relevant to the micro-paper lane should be connected after deleting isolated solved components, because disconnectedness would let one pass to a smaller bad component.

# approach_A
Structural / invariant route: work in the mod-3 labeling language and analyze a vertex-minimal counterexample by local interface states.

Main idea:
- A cut edge `e` suggests a two-state interface problem: on either side, can the boundary endpoint be completed when `e` is forced in, and when `e` is forced out?
- Small loop-heavy boundary types are often flexible. For example, if a pendant vertex has two loops and one ordinary edge to the rest of the graph, then in a `{4,1}`-factor that vertex can be handled in exactly two local ways: take only the bridge (degree `1`), or take both loops and omit the bridge (degree `4`). So this smallest one-edge attachment is not itself an obstruction.
- More generally, for a one-edge-attached rooted gadget, the obstruction mechanism would have to be rigidity of the boundary state set, not mere presence of loops or bridges.

What this route would need to close:
- Show that every proper one-edge side of a minimal counterexample is flexible enough to realize both boundary states, or at least enough states to glue across every cut.
- Then deduce that a minimal counterexample is bridgeless or has a reducible cut configuration, after which one would continue with 2-edge or 3-edge cut analysis in the mod-3 language.

Current obstruction:
- I do not yet have a proof that all rooted 5-regular sides are flexible. The two-loop pendant is flexible, but that does not rule out a larger rigid rooted gadget.

# approach_B
Construction / extremal / contradiction route: try to build the smallest rigid rooted gadget and glue several copies to force a forbidden center state.

Main idea:
- A rooted gadget with one dangling edge can have interface state set contained in `{in, out}`. If a gadget exists with only `in` feasible, then gluing five copies to a new center would force degree `5` at the center in any candidate factor, which is forbidden. If only `out` is feasible, the center would be forced to degree `0`, also forbidden.
- Thus the smallest counterexample should arise from a smallest rigid one-edge gadget, if such a gadget exists.
- Failing that, a direct bounded search over small connected 5-regular pseudographs can test whether counterexamples exist at the first few orders and reveal what local interface patterns are actually realizable.

What this route would need to close:
- Either exhibit a rigid rooted gadget and convert it into a genuine connected counterexample, or show computationally that no such rigid gadget or counterexample appears at the smallest relevant sizes.

Current obstruction:
- I do not have a hand derivation of a rigid rooted gadget. A bounded search is justified if the reasoning-only route stalls here.

# lemma_graph
1. `{4,1}`-factor `<=>` mod-3 `{1,2}` edge-labeling with zero vertex sums.
2. Any smallest counterexample may be taken connected.
3. Any successful obstruction through a cut must come from a rooted side with a restricted interface state set.
4. Smallest obvious one-edge rooted type, namely a vertex with two loops and one external edge, is flexible, so not every bridge is bad.
5. If every proper rooted side is flexible, then a minimal counterexample should have no reducible cut and the proof must continue through a denser local configuration analysis.
6. If some rooted side is rigid, it is a concrete candidate seed for a counterexample construction.

# chosen_plan
Pursue the rooted-gadget obstruction route first, because it is the cleanest way to decide whether the cut analysis is actually pointing toward a proof or toward a counterexample. If a smallest rigid gadget is not visible by hand, run a bounded exact search on the smallest connected 5-regular pseudographs and, if needed, on smallest one-edge rooted gadgets. Keep the search tiny and certificate-oriented.

# self_checks
- Self-check after statement lock: the equivalence is internally consistent, including the loop convention.
- Self-check after structural route: I have a real obstruction criterion, namely rigidity of boundary states, not just a vague “analyze cuts” slogan.
- Self-check after construction route: the proposed gadget-gluing mechanism would genuinely force a forbidden center degree if a one-state rooted gadget exists.

# code_used
None yet. Reasoning-first stage only so far. If code becomes necessary, it should be a tiny bounded checker / falsifier for the smallest connected pseudographs or rooted gadgets.

# result
No theorem or counterexample is established yet. The live mathematical question is whether a smallest rigid one-edge rooted gadget exists; that is the concrete obstruction between the current reasoning package and a full proof-by-reduction.

# family_affinity
High. This instance sits exactly at the low-degree endpoint of the regular `{a,b}`-factor family, and the proof template is clearly “equivalent residue + local reducibility” rather than a broad multi-step theorem program.

# generalization_signal
Moderate. A successful rooted-state analysis would likely transfer to other low odd-degree `{r-1,1}` residues, but the larger odd-degree landscape already has counterexamples, so the transferable content would be a local reduction template, not a new broad theorem.

# proof_template_reuse
If the positive route works, the reusable template is: translate to a finite-field edge-labeling problem, classify rooted interface states on small cuts, and exclude minimal obstructions by gluing contradictions. If the negative route works, the reusable template is: build a rigid rooted gadget and amplify it into a global degree obstruction.

# candidate_theorem_slice
Natural theorem slice if the full claim does not close immediately: classify one-edge-attached rooted 5-regular pseudographs by feasible boundary states and prove that the smallest loop-pendant rooted type is flexible. That is not yet paper-ready by itself, but it is the first theorem-facing slice.

# smallest_param_shift_to_test
Test the smallest even orders first, namely connected 5-regular pseudographs on `2` and `4` vertices, and separately the smallest rooted one-edge gadgets on `1` to `3` internal vertices.

# why_this_is_or_is_not_publishable
If the full statement closes, yes: this would still be about `70-90%` of a short paper, with exact title theorem `Every 5-regular pseudograph contains a {4,1}-factor` or an explicit minimal obstruction theorem. At the current stage it is not publishable: there is a coherent obstruction criterion and a concrete search target, but no theorem closure or minimal counterexample yet.

# paper_shape_support
- Exact title theorem if solved positively: `Every 5-regular pseudograph contains a {4,1}-factor.`
- Exact title theorem if solved negatively: `A connected 5-regular pseudograph with no {4,1}-factor`, together with a minimal obstruction package.
- Minimal remaining packaging work after a successful solve: write the mod-3 equivalence as the setup lemma, present the proof or obstruction, and add one short discussion paragraph explaining why this settles the last 5-regular odd-degree residue.
- Immediate corollary or remark if solved positively: the signless mod-3 incidence system on every 5-regular pseudograph has a nowhere-zero `{1,2}` solution.
- Current assessment: still too thin for the micro-paper lane right now, because the result is only a strategy package plus one local flexibility observation.

# boundary_remark
The smallest local loop-pendant configuration is supportive rather than obstructive: a vertex carrying two loops and one external edge can always be satisfied in one of the two boundary states. So any genuine counterexample, if it exists, has to hide in a less trivial rooted interface pattern.

# likely_failure_points
- The rooted-state space may be more than two-valued once multiple boundary edges or multiple root vertices enter, making the one-edge gadget route incomplete.
- A bounded search on tiny orders may find no counterexample and still not illuminate the general positive proof.
- The positive theorem may require a nonlocal theorem such as a specialized factor criterion rather than purely local reducibility.

# what_verify_should_check
- Verify the loop convention used in the mod-3 reformulation against the cited source.
- If the bounded search is used, independently verify the generator and the factor checker on hand examples such as `K_6` and the two-loop pendant examples.
- If a rigid rooted gadget or full counterexample appears, verify exhaustively that every candidate `{4,1}`-factor fails.
- If the positive route later closes, verify that every claimed cut reduction is reversible and preserves 5-regularity where required.
