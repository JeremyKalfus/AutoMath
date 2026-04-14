# Solve Record: Recolourability of 4-Chromatic (2K2, K4)-Free Graphs

## statement_lock
Target slug: `2k2-k4-recolourable`.

Locked title theorem target: **Every 4-chromatic `(2K2, K4)`-free graph has connected `R_l(G)` for every `l > 4`**.

Solve-stage operational reduction: since `chi(G)=4`, the first obstruction level is `l=5`. A frozen 5-colouring or a disconnected `R_5(G)` would already refute the target. A positive proof that every 5-colouring can be linked to a 4-colouring would strongly suggest the full theorem, but I am treating the `l=5` step as the exact place where the solve either closes or visibly stalls.

If this closed positively, the exact title theorem would be:
`Recolourability of 4-Chromatic (2K2, K4)-Free Graphs`.

If this closed negatively, the exact title theorem would be:
`A Frozen 5-Colouring in a 4-Chromatic (2K2, K4)-Free Graph`.

## definitions
- A proper `l`-colouring is a map `alpha: V(G) -> {1, ..., l}` with adjacent vertices receiving different colours.
- `R_l(G)` is the recolouring graph whose vertices are proper `l`-colourings, with edges given by recolouring exactly one vertex.
- A colouring is frozen if no single-vertex recolouring is possible. In a proper 5-colouring this means every vertex sees all four other colours in its neighbourhood.
- In a proper colouring with colour classes `V_1, ..., V_l`, the subgraph `G[V_i \cup V_j]` is bipartite. Since `G` is `2K2`-free, every such bichromatic subgraph is a bipartite `2K2`-free graph, hence a chain graph.
- Ambiguity to keep explicit: the packet phrases the open problem as connectedness of `R_l(G)` for all `l > chi(G)`. I am using `l=5` as the first exact obstruction level. Turning a positive `R_5(G)` proof into all `l>4` is standard in recolouring arguments, but I am not assuming that reduction without proof inside this solve record.

## approach_A
Structural / invariant approach: assume a frozen 5-colouring `alpha` exists and exploit the fact that every bichromatic layer is a chain graph.

Write the colour classes as `V_1, ..., V_5`.

1. For every pair `i != j`, `G[V_i \cup V_j]` is a chain graph.
2. If `alpha` is frozen, then every vertex of `V_i` has at least one neighbour in `V_j`, because each vertex sees all other colours.
3. Therefore no bichromatic layer `G[V_i \cup V_j]` has an isolated vertex on either side.
4. In a chain graph with no isolated vertices, one side has a vertex complete to the other side, and conversely. So for each pair `i != j` there is a dominating edge between `V_i` and `V_j`: some `x_{ij} in V_i` is complete to `V_j`, and some `x_{ji} in V_j` is complete to `V_i`.
5. Fix a smallest colour class `V_s`. For each other colour `t`, choose `x_t in V_t` complete to `V_s`.
6. Every vertex of `V_s` is adjacent to all four vertices `x_t`. Since `G` is `K4`-free, the induced graph on `{x_t : t != s}` must be triangle-free; otherwise any triangle among them together with any `v in V_s` gives a `K4`.
7. Because `G` is also `2K2`-free, that 4-vertex witness graph is a triangle-free `2K2`-free graph, so only very restricted local shapes can occur.

Why this looks promising: the frozen condition upgrades the weak `2K2` restriction into a strong pairwise-domination pattern across the five colour classes, while the `K4`-free condition forbids those witnesses from organizing into triangles around a smallest class.

Self-check after Approach A: this gives a real obstruction skeleton, but it does not yet force a recolouring move or exclude all possible witness configurations.

## approach_B
Construction / extremal / contradiction approach: try to build a counterexample directly from a frozen 5-colouring and see what minimal form it must have.

1. Any counterexample with a frozen 5-colouring must be 4-chromatic, `K4`-free, and have minimum degree at least 4, because every vertex must see all four other colours.
2. In a `K4`-free graph, every neighbourhood is triangle-free. So a frozen 5-colouring would force each neighbourhood to be a triangle-free graph that still hits all four other colour classes.
3. Since each bichromatic layer is a chain graph, the entire candidate must look like five independent sets tied together by pairwise nested adjacencies.
4. The smallest natural 4-chromatic `(2K2, K4)`-free model is the 5-wheel `W_6` (a `C_5` plus a hub). Longer odd wheels already create induced `2K2`, so any negative example should be much more special than a generic odd-wheel family.
5. This suggests an extremal strategy: if a counterexample exists, minimality should push it toward a wheel-like or `C_5`-anchored configuration with highly constrained expansions of the five colour classes.

Why this looks promising: the packet already says the gap from source is small, so a sharp obstruction may be compact if it exists.

Self-check after Approach B: this does not currently build a genuine counterexample, but it identifies a bounded family shape worth checking if the structural proof stalls.

## lemma_graph
- Lemma 1: for any two colour classes `V_i, V_j`, the bichromatic graph `G[V_i \cup V_j]` is a chain graph.
- Lemma 2: in a frozen 5-colouring, every bichromatic graph `G[V_i \cup V_j]` has minimum degree at least 1 on both sides.
- Lemma 3: hence every colour pair admits a dominating edge across the two colour classes.
- Lemma 4: if `V_s` is a smallest colour class and `x_t` is chosen complete to `V_s` for each `t != s`, then `{x_t : t != s}` induces a triangle-free `2K2`-free graph.
- Lemma 5 candidate: classify the possible 4-vertex witness graphs from Lemma 4 and show each shape yields a recolouring move or a forced wheel-like reduction.

Proof skeleton:
assume a minimal frozen 5-colouring -> pass to bichromatic chain graphs -> choose a smallest colour class -> extract four witness vertices complete to it -> classify the resulting 4-vertex local configuration -> either derive a recolouring move or reduce to a very small extremal model.

## chosen_plan
I am pursuing the positive direction first.

Chosen path:
1. Treat frozen 5-colourings as the first exact obstruction level.
2. Use the chain-graph structure of every bichromatic layer as the main invariant.
3. Try to force a contradiction from a smallest colour class and its four complete witnesses in the other colours.
4. If the local case split still leaves viable configurations, run one tiny bounded experiment on the smallest available graphs to see whether the extremal model already collapses in practice.

Paper-shape question asked explicitly: if the main claim closes, what extra structure is needed to make it paper-shaped?

Answer: almost nothing beyond the main theorem. The remaining packaging would be:
- one compact structural lemma explaining why the `K4`-free condition kills the frozen-colouring mechanism,
- one short bridge paragraph to the 2025 near-dichotomy,
- one immediate corollary that the forbidden-pair-on-four-vertices recolourability classification is now complete.

So a successful solve here would already be about `80%` of a short paper, consistent with the packet.

## self_checks
- Statement lock check: I am not silently downgrading the target to "no frozen 5-colourings" as the final theorem. That is only the first exact obstruction level.
- Scope check: no web, no unrelated dossiers, no broad ledger replay.
- Method check: reasoning was written before the bounded experiment.
- Strength check: the current argument is structural but incomplete; no proof claim is being overstated.

## code_used
One tiny bounded experiment was used after the reasoning phase.

Experiment:
- exhaustive enumeration of all labelled graphs on 6 vertices;
- filter to connected, `2K2`-free, `K4`-free, and 4-chromatic graphs;
- for each survivor, enumerate all proper 5-colourings and test connectivity of `R_5` as well as existence of frozen 5-colourings.

Observed exact output:
- there are `72` labelled survivors, all with degree sequence `[3,3,3,3,3,5]`;
- that degree sequence forces one universal vertex and five remaining vertices of degree 2 among themselves, hence the survivor is exactly the 5-wheel `W_6` up to isomorphism;
- for each labelled copy, `R_5` is connected;
- each has exactly `1200` proper 5-colourings and `0` frozen 5-colourings.

So the smallest possible 4-chromatic `(2K2, K4)`-free graph is already recolourable, and the first extremal model does not support a negative obstruction.

## result
Current solve-state: partial structural progress only.

Strongest mathematically honest output so far:
- In any hypothetical frozen 5-colouring of a `(2K2, K4)`-free graph, every bichromatic layer is a chain graph with no isolated vertices.
- Consequently every pair of colour classes has a dominating edge, and any smallest colour class is simultaneously dominated by one witness from each of the other four colours.
- The four witnesses around a smallest colour class induce a triangle-free `2K2`-free graph, which is a much narrower local configuration than in the unrestricted `2K2`-free setting.
- Exact bounded slice: on 6 vertices, the only connected 4-chromatic `(2K2, K4)`-free graph is the wheel `W_6`, and its recolouring graph `R_5` is connected with no frozen 5-colouring.

This is not yet a proof of recolourability and not yet a counterexample.

Self-check after code: the computation certifies only the 6-vertex case. It supports the positive direction, but it does not meaningfully shorten the full proof unless the wheel-like reduction can be proved structurally.

## family_affinity
Very strong. This candidate is still tightly coupled to a named family-level dichotomy: the last unresolved recolourability case for pairs of forbidden induced four-vertex graphs.

## generalization_signal
Moderate positive signal. The chain-graph reduction is not peculiar to one hand-built example; it is a reusable mechanism for pair-forbidden recolouring problems where every bichromatic layer inherits a strong forbidden-subgraph condition.

## proof_template_reuse
Most reusable template identified so far:
- convert a frozen-colouring obstruction into pairwise constraints on bichromatic layers,
- use forbidden induced subgraphs to upgrade those layers to a rigid class (here: chain graphs),
- extract dominating witnesses around a smallest colour class,
- then combine that local domination with clique-forbiddance to collapse the obstruction.

That template could plausibly transfer to other "last case" recolouring questions with one sparse forbidden graph and one clique-type forbidden graph.

## candidate_theorem_slice
Best current theorem-facing slice:

Structural slice:

`If a 4-chromatic (2K2, K4)-free graph admits a frozen 5-colouring with colour classes V_1, ..., V_5, then for every pair i != j the bichromatic graph G[V_i \cup V_j] is a chain graph of minimum degree at least 1, and for any smallest colour class V_s there exist witnesses x_t in V_t complete to V_s (t != s) whose induced subgraph is triangle-free and 2K2-free.`

Exact bounded slice:

`Up to isomorphism, the unique connected 6-vertex 4-chromatic (2K2, K4)-free graph is the 5-wheel W_6, and R_5(W_6) is connected. In particular, no 6-vertex graph in the target class has a frozen 5-colouring.`

This is now a real theorem slice, but it is still too thin to count as the micro-paper result.

## smallest_param_shift_to_test
The most informative nearby shifts are:
- exact bounded size: extend the now-complete 6-vertex classification to 7 vertices and test `R_5`,
- extremal local shape: isolate the case where the four witnesses around a smallest colour class induce `C_4`, `P_4`, or `K_{1,3}` and test whether each shape always yields a recolouring move.

## why_this_is_or_is_not_publishable
Not publishable yet.

Why not:
- the current output is a structural reduction, not the title theorem;
- it does not yet prove connectedness of `R_5(G)` or exhibit a counterexample;
- it does not yet close the dichotomy.

If the main claim closed, the package would already be paper-shaped and about `70-90%` of a paper. Right now it is still too thin for the micro-paper lane on its own.

What part of the current argument scales:
- the bichromatic chain-graph reduction is family-level and should scale to arbitrary graph order;
- the "smallest colour class plus four witnesses" template also scales.

What does not yet scale:
- the exact 6-vertex computation does not directly control larger graphs;
- the wheel-like intuition is not yet a theorem for all target graphs.

What theorem slice is suggested:
- either a full local classification of the four-witness graph around a smallest colour class,
- or a reduction showing every minimal counterexample contains a wheel-like core already known to recolour.

Best next parameter shifts:
- 7 vertices exact,
- the `C_4 / P_4 / K_{1,3}` witness-shape case split.

Current package assessment:
- closer to a paper-shaped claim than a bare instance, but still only an instance-plus-structure slice, not yet the title theorem.

## paper_shape_support
Minimal remaining packaging work after a genuine solve would be:
- write the main proof cleanly,
- add one short contextual theorem statement tying the result to the 2025 classification,
- add one immediate corollary: the pair-forbidden four-vertex recolourability dichotomy is complete,
- optionally include one boundary remark comparing the result with the known frozen examples `D_2` and `F_2` from the broader `2K2`-free setting.

## boundary_remark
Natural immediate boundary remark if the positive theorem closes:

`The K4-free hypothesis is exactly strong enough to eliminate the frozen-colouring behaviour that already appears in the wider 2K2-free class.`

Natural immediate boundary remark if a negative example closes:

`Even the K4-free restriction does not remove all frozen 5-colourings inside 2K2-free graphs, so the last pair-forbidden case fails by a compact obstruction.`

## likely_failure_points
- The reduction from frozen 5-colourings to chain-graph witness structure may still leave several 4-vertex witness shapes alive.
- Excluding those shapes may require one additional source lemma from the 2025 paper, which I have not loaded in this run due the read-budget discipline.
- Even if frozen 5-colourings are excluded, disconnected `R_5(G)` without a frozen colouring could in principle remain, so the proof may need more than local obstruction removal.

## what_verify_should_check
- Whether the chain-graph claims are stated with the right level of generality and no hidden assumptions.
- Whether proving `R_5(G)` connected is genuinely sufficient for all `l > 4` in this exact literature setting.
- Whether the positive direction really only needs elimination of frozen 5-colourings, or whether disconnected non-frozen components are known to occur in related classes.
- If a bounded experiment is added below, verify the exact graph-class filter and the recolouring-connectivity test.
