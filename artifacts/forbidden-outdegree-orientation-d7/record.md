# Solve Record: forbidden-outdegree-orientation-d7

## statement_lock

- Active title: `Settle the d = 7 slice of the forbidden out-degree orientation conjecture`.
- Active slug: `forbidden-outdegree-orientation-d7`.
- Entry type: `paper_candidate`.
- Locked intended statement: prove that for every `7`-regular graph `G` and every forbidden set `F subseteq {0,1,2,3,4,5,6,7}` with `|F| <= 3`, there is an orientation of `G` in which no vertex has out-degree in `F`.
- This pass is locked to the exact `d = 7` slice. I will record any genuine theorem slice that falls out, but I will not silently relabel a slice theorem as a full `d = 7` closure.

Self-check:
- The target is the full selected `d = 7` regular slice, not a weakened family proxy.
- The paper-facing objective is still the next-case theorem `d = 7`, not a broad higher-degree campaign.

## definitions

- An `F`-avoiding orientation of a graph `G` is an orientation in which every vertex `v` has `d^+(v) notin F`.
- Reversing every edge sends out-degree `k` to `7 - k`, so the `d = 7` problem is symmetric under
  `F <-> 7 - F := {7 - a : a in F}`.
- A connected `7`-regular graph has a perfect matching by Petersen's theorem.
- If `M` is a perfect matching in a connected `7`-regular graph `G`, then `H := G - M` is `6`-regular.
- Every connected even-regular graph is Eulerian and bridgeless, so each connected component of `H` admits a strong Eulerian orientation.
- Conventions for this solve:
  - graphs are finite and simple unless the dossier states otherwise;
  - disconnected graphs may be treated componentwise;
  - `d^+(v)` always means out-degree in the final orientation of the full `7`-regular graph.
- Ambiguities or missing definitions:
  - none block the present pass;
  - the only missing ingredient is mathematical, not definitional: a global repair lemma that turns the base balanced orientation into one avoiding the central forbidden patterns.

Self-check:
- Every definition used below comes from standard orientation language plus the dossier's fixed `d = 7` setting.
- I am not assuming any result from the `d <= 6` paper beyond the dossier's statement that those cases are already known.

## approach_A

- Structural / invariant route: start from a perfect matching and force a canonical balanced orientation.

1. Let `M` be a perfect matching of a connected `7`-regular graph `G`, and let `H = G - M`.
2. Orient each connected component of `H` with a strong Eulerian orientation. Then every vertex has out-degree `3` inside `H`.
3. Contract each component of `H` to one vertex. The matching edges become the edges of a quotient multigraph `Q`.
4. `Q` is connected because `G` is connected. Also `Q` has no bridge: if some quotient edge were a bridge, the corresponding matching edge would be a bridge of `G`, impossible in an odd-regular graph.
5. By Robbins' theorem, `Q` has a strong orientation. Lift that orientation back to the matching edges.
6. In the resulting orientation of `G`, every vertex has out-degree either `3` or `4`:
  - `3` from the `6`-regular core `H`;
  - plus `0` or `1` from its matching edge in `M`.
7. Because the quotient orientation is strong and each `H`-component was oriented strongly, the full orientation is strong as well.

- Rigorous consequence:
  every connected `7`-regular graph admits a strong orientation with all out-degrees in `{3,4}`.

- Immediate theorem slice from that consequence:
  if `F cap {3,4} = emptyset`, then every `7`-regular graph has an `F`-avoiding orientation.

- This is already a real reduction of the full problem:
  the only unresolved forbidden sets in this pass are the ones that hit the central pair `{3,4}`.

- Repair idea suggested by this approach:
  in a strong orientation, reversing a directed path transfers one unit of out-degree from its start to its end while leaving internal vertices unchanged. That is exactly the local move one wants for turning a `3/4` orientation into a `2/5` or `1/4/5/6` orientation.

- Why the route stalls:
  I do not have a clean global theorem here saying that the required collection of path-repairs can always be chosen simultaneously in an arbitrary strong `3/4` orientation. That missing global repair lemma is the present blocker.

Self-check:
- The balanced `{3,4}` orientation proof is complete.
- The deduction `F cap {3,4} = emptyset =>` solvable is complete.
- The path-reversal discussion is explicitly heuristic here and is not being promoted to a theorem.

## approach_B

- Construction / extremal route: isolate a class where the full `d = 7` statement closes cleanly.

1. Suppose `G` is bipartite and `7`-regular, with bipartition `(L,R)`.
2. By Koenig's line-coloring theorem, `E(G)` decomposes into seven perfect matchings
   `M_1, ..., M_7`.
3. For any `k in {0,1,2,3,4,5,6,7}`, orient exactly `k` of these matchings from `L` to `R` and orient the remaining `7-k` from `R` to `L`.
4. Then every vertex of `L` has out-degree exactly `k`, and every vertex of `R` has out-degree exactly `7-k`.
5. The eight degrees split into the four complementary pairs
   `{0,7}`, `{1,6}`, `{2,5}`, `{3,4}`.
6. A forbidden set `F` of size at most `3` cannot hit all four complementary pairs, so there exists some `k` such that both `k` and `7-k` lie outside `F`.
7. Choosing that `k` gives an `F`-avoiding orientation of the whole bipartite graph.

- Rigorous consequence:
  the full `d = 7` conjecture holds for every bipartite `7`-regular graph.

- Why this matters for the active paper candidate:
  it isolates the frontier mass into the nonbipartite case. More specifically, after combining Approach A and Approach B, the still-open core is:
  - nonbipartite `7`-regular graphs;
  - forbidden sets `F` meeting `{3,4}`.

- Extremal interpretation:
  the base difficulty is not the sheer size of `F`; it is the nonbipartite inability, in this pass, to globally realize the same kind of two-level out-degree pattern that the bipartite `1`-factorization gives for free.

Self-check:
- The bipartite theorem is complete and uses only standard `1`-factorization of regular bipartite graphs.
- The complementary-pair pigeonhole step is exact: `|F| <= 3` leaves at least one pair `{k,7-k}` untouched.
- This closes a genuine theorem slice, not just a heuristic subclass.

## lemma_graph

1. `F` and `7 - F` are equivalent by reversing every edge.
2. Every connected `7`-regular graph has a perfect matching `M`.
3. Removing `M` leaves a `6`-regular graph `H`.
4. Each connected component of `H` admits a strong Eulerian orientation, so every vertex gets `3` outgoing `H`-edges.
5. Contracting `H`-components yields a bridgeless quotient on the matching edges, so those matching edges can be oriented strongly.
6. Therefore every connected `7`-regular graph has a strong `{3,4}`-orientation.
7. Hence every forbidden set `F` with `F cap {3,4} = emptyset` is already solved.
8. If the graph is bipartite, `G` has a `7`-edge-coloring into perfect matchings.
9. Orienting `k` matchings left-to-right and `7-k` right-to-left yields a `(k,7-k)`-orientation.
10. Since any `|F| <= 3` misses some complementary pair `{k,7-k}`, the full conjecture holds for bipartite `7`-regular graphs.
11. The unresolved residue of this solve pass is therefore the nonbipartite center-hitting regime.

## chosen_plan

- Use the perfect-matching / `6`-core decomposition first, because it gives the cleanest exact structural reduction available inside the repo without outside references.
- Push that reduction all the way to a fully rigorous theorem:
  every `7`-regular graph has a strong `{3,4}`-orientation.
- Then look for a second exact slice rather than forcing a speculative global repair lemma.
- The bipartite case closes completely, so preserve that as the strongest honest publication-facing slice from this pass.
- Stop there conservatively. I do not have a full proof for the nonbipartite center-hitting patterns, and there is no reasoning-first basis yet for SAT, brute force, or Lean.

Self-check:
- This plan keeps the solve packet reasoning-first and does not overstate the unfinished part.
- No code is justified because there is no explicit witness to verify and no bounded experiment that changes the mathematical status of the unresolved core.

## self_checks

- Statement lock:
  the full selected `d = 7` slice stayed fixed throughout.
- After Approach A:
  the strong `{3,4}` orientation theorem is proved and immediately discharges all `F` disjoint from `{3,4}`.
- After Approach B:
  the bipartite `7`-regular slice is fully proved for every `|F| <= 3`.
- At stop point:
  the remaining gap is explicit and narrow: nonbipartite graphs with center-hitting forbidden sets.
- Scope discipline:
  the writeup does not claim a full `d = 7` theorem, and it does not relabel a slice result as paper-ready.

## code_used

- No code was used in this solve pass.
- Reason:
  the strongest outputs here are purely structural theorems and reductions, and I do not yet have a concrete witness family or a sharply justified bounded falsifier that would materially improve the proof status.

## result

- Provisional solve-stage verdict: `PARTIAL`.
- Strongest rigorous outputs from this pass:
  - every connected `7`-regular graph admits a strong orientation with all out-degrees in `{3,4}`;
  - therefore every forbidden set `F` with `F cap {3,4} = emptyset` is solved immediately;
  - the full `d = 7` conjecture holds for every bipartite `7`-regular graph.

- Strongest honest frontier statement after this pass:
  the unresolved core is now concentrated in nonbipartite `7`-regular graphs and forbidden sets that meet the central pair `{3,4}`.

- What part of the argument scales:
  - the perfect-matching reduction from odd regular degree `2r+1` to an even `2r`-regular core;
  - the quotient-orientation trick for upgrading componentwise Eulerian orientations to a strong whole-graph orientation;
  - the complementary-pair argument on bipartite `1`-factorizations.

- What part does not:
  - the present writeup does not supply the missing global repair lemma needed to push a nonbipartite strong `{3,4}` orientation off the central forbidden values;
  - the bipartite proof uses full `1`-factorization and does not transfer verbatim to arbitrary nonbipartite `7`-regular graphs.

- What theorem slice is suggested:
  a clean short theorem package is visible:
  `For bipartite 7-regular graphs, the forbidden out-degree conjecture is true for every forbidden set F of size at most 3. More generally, for arbitrary 7-regular graphs the conjecture is already true whenever F cap {3,4} = emptyset.`

- What one or two next feeder instances would help most:
  - the normalized center-pair pattern `F = {3,4}` on nonbipartite `7`-regular graphs;
  - the next denser center-hitting pattern `F = {2,3,4}` up to complement symmetry.

- Whether the current package is still just an instance or already closer to a paper-shaped claim:
  it is closer to a paper-shaped claim than a single instance because it proves a genuine theorem slice, but it is still not the selected next-case theorem. The active paper target remains the full nonbipartite center-hitting closure.

Self-check:
- The result section distinguishes proved slices from the unsolved residue.
- The publication-facing claims are theorem-shaped but still below the selected full-paper objective.

## family_affinity

- Family affinity is high.
- The balanced `{3,4}` orientation theorem and the bipartite full slice both sit exactly on the selected `d = 7` line, not on a side family.
- The work also clarifies where future effort should go: nonbipartite center-hitting forbidden sets, rather than re-proving easy extreme or bipartite cases.

## generalization_signal

- Generalization signal is medium.
- The quotient proof suggests a reusable odd-degree template:
  remove one perfect matching, orient the even core Eulerian, then orient the matching quotient strongly.
- The bipartite argument scales even more cleanly to odd regular degree `2r+1`:
  in a bipartite `(2r+1)`-regular graph, a forbidden set of size at most `r` misses some complementary pair `{k, 2r+1-k}`, so a `1`-factorization gives an immediate avoiding orientation.
- What does not yet scale is the nonbipartite repair from the central balanced pair to other allowed out-degree palettes.

## proof_template_reuse

- Reusable template from this pass:
  1. normalize by complement symmetry `F <-> 7 - F`;
  2. remove a perfect matching;
  3. orient the even core componentwise Eulerian and strong;
  4. contract components and orient the matching quotient strongly;
  5. read off a balanced two-level out-degree orientation;
  6. if the graph is bipartite, replace the whole repair problem by a direct `1`-factorization construction on a complementary pair `{k,7-k}`.
- This is a real proof template, not just a post hoc summary.

## candidate_theorem_slice

- Candidate theorem slice:
  `Let G be a 7-regular graph and F subseteq {0,1,2,3,4,5,6,7} with |F| <= 3.`
  `If G is bipartite, then G has an F-avoiding orientation.`
  `More generally, for arbitrary G, if F cap {3,4} = emptyset, then G has an F-avoiding orientation.`
- This is the strongest exact theorem package actually proved in this solve pass.

## smallest_param_shift_to_test

- The smallest next normalized shift to test is not a larger degree; it is the first remaining forbidden-pattern core:
  `F = {3,4}` on nonbipartite `7`-regular graphs.
- After that, the next useful shift is
  `F = {2,3,4}` up to complement symmetry.
- Those are the places where a successful global repair lemma would immediately expand the solved slice toward the full paper claim.

## why_this_is_or_is_not_publishable

- If the full `d = 7` statement were solved, that would already be about `70-90%` of a short paper.
- The exact paper claim would be:
  `Every 7-regular graph admits an F-avoiding orientation for every forbidden set F of size at most 3.`
- The minimal remaining packaging after a successful full solve would be:
  - symmetry reduction on `F`;
  - positioning against the known `d <= 6` result;
  - one clean section isolating the few genuinely distinct forbidden-pattern classes;
  - optional Lean bookkeeping after the combinatorial proof stabilizes.

- The current package is not publishable as the selected one-shot paper candidate.
- Reason:
  it proves a real theorem slice, but not the next unresolved degree case itself.
- Conservative publication view:
  the bipartite slice and the easy forbidden-set slice may be note-worthy if novel, but on solve-stage evidence alone they should be treated only as `SLICE_CANDIDATE`, not as a paper-ready contribution.

## likely_failure_points

- The main failure point is the missing global repair lemma:
  local path reversals clearly move one unit of out-degree between vertices, but I do not yet know how to choose such repairs globally for arbitrary nonbipartite `7`-regular graphs.
- Another risk is overestimating the novelty of the bipartite slice or the `{3,4}`-disjoint slice. Solve runs with web disabled, so novelty has not been audited here.
- A proof attempt that leans too hard on `1`-factorization or parity patterns could silently collapse back to the bipartite case. That would be concept drift, not progress on the selected frontier.

## what_verify_should_check

- Verify the perfect-matching reduction and the claim that every connected `7`-regular graph is bridgeless.
- Verify the quotient step:
  after removing a perfect matching and contracting the `6`-regular components, the matching quotient is bridgeless, so Robbins applies.
- Verify that the lifted orientation is indeed strong and gives only out-degrees `3` and `4`.
- Verify the immediate corollary `F cap {3,4} = emptyset =>` solvable.
- Verify the bipartite slice carefully:
  - `7`-regular bipartite graphs decompose into seven perfect matchings;
  - orienting `k` matchings one way and `7-k` the other gives out-degrees `(k,7-k)`;
  - every `|F| <= 3` misses at least one complementary pair `{k,7-k}`.
- In the prior-art pass, check whether either proved slice is already implicit in the canonical source or its cited preliminaries.

## verify_rediscovery

- PASS 1 used a bounded live-web audit on `2026-04-12` against the exact `d = 7` slice, notation variants, the canonical source, internal theorem/example/corollary checks inside that source, and one recent status sweep.
- I did not find bounded evidence that the full intended statement
  `every 7-regular graph admits an F-avoiding orientation for every |F| <= 3`
  has already been closed in prior art.
- I did find that the strongest surviving exact slice from this packet is already known:
  - the canonical source states that the more general conjecture has already been verified for bipartite graphs in earlier work, so Approach B is a rediscovery rather than a new frontier slice;
  - the canonical source also records an odd-regular theorem covering the `d = 7` case `F = {1,2,3}`, and by global edge-reversal the complementary case `F = {4,5,6}` is also already settled.
- Rediscovery conclusion:
  after proof checking, the only fully correct slice left in this artifact is already in prior art, so this run should be archived as `REDISCOVERY`.

## verify_faithfulness

- The prose is disciplined about not claiming a full `d = 7` closure; it repeatedly says the center-hitting nonbipartite cases remain open.
- However, the solve packet still drifts from the locked intended statement.
- The claimed strongest theorem package includes the arbitrary-graph assertion
  `F cap {3,4} = emptyset =>` solvable,
  but that assertion is not proved.
- Once the broken part is removed, the surviving claim is only the bipartite slice, which is a nearby and already-known variant rather than the selected frontier target.
- Faithfulness verdict:
  honest about being partial, but mathematically the artifact ends at a rediscovered variant, not at the intended statement.

## verify_proof

- First incorrect step:
  [approach_A](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/forbidden-outdegree-orientation-d7/record.md:42) and
  [lemma_graph](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/forbidden-outdegree-orientation-d7/record.md:105).
- The sentence
  `if some quotient edge were a bridge, the corresponding matching edge would be a bridge of G, impossible in an odd-regular graph`
  is false.
- Connected odd-regular simple graphs can have bridges, so the quotient `Q` need not be bridgeless.
- Therefore Robbins' theorem cannot be invoked as written, the claimed strong `{3,4}`-orientation theorem fails, and the corollary for arbitrary `F` disjoint from `{3,4}` is unsupported.
- I did not find a repair inside the current packet that restores the nonbipartite argument.
- Approach B, the bipartite `1`-factorization argument, is correct on its own.

## verify_adversarial

- The universal strong-orientation claim breaks on explicit `7`-regular bridge graphs.
- Counterexample construction:
  - start with `K_9` on vertices `{u,v,w_1,...,w_7}`;
  - delete a perfect matching on the eight vertices other than `u`, so `u` keeps degree `8` and every other vertex has degree `7`;
  - delete the extra edge `uv`, leaving exactly one degree-`6` vertex `v` and all other vertices degree `7`;
  - build two disjoint copies of this `9`-vertex block and join their two degree-`6` vertices by one new edge.
- The resulting graph is connected, simple, and `7`-regular, and the new connecting edge is a bridge.
- No graph with a bridge admits a strong orientation, so the claimed theorem
  `every connected 7-regular graph admits a strong orientation with out-degrees in {3,4}`
  is false.
- No code or checker was needed; the combinatorial obstruction is decisive.

## verify_theorem_worthiness

- After proof correction, the only surviving theorem slice is the bipartite one.
- That slice is clean and structural, but PASS 1 shows it is already covered by prior art, so it does not support a new publication-facing status in this artifact.
- The nonbipartite quotient idea does isolate a genuine difficulty, but in its current form it is not a theorem slice; it fails before reaching the frontier center-hitting patterns.
- Best honest publication status here is `REDISCOVERY`, not `INSTANCE_ONLY` and not `SLICE_CANDIDATE`.
- If this line is ever revisited later, the smallest decisive stress test for the current template is:
  `bridgeless nonbipartite 7-regular graphs with F = {3,4}`.
  The present template already fails earlier on graphs with bridges.

## verify_verdict

- `verify_verdict = REDISCOVERY`.
- Reason:
  the only correct slice left after proof checking is already in prior art, while the purported new arbitrary-graph slice fails at the bridge step.
- The run must not remain labeled as a novel `CANDIDATE` or any stronger positive status.

## minimal_repair_if_any

- Conservative repair:
  delete the arbitrary-graph `{3,4}`-disjoint theorem from the claimed outputs and retain only the bipartite slice as a known fact.
- That repair does not salvage frontier novelty, so the correct operational next step is
  `archive_as_rediscovery`.
