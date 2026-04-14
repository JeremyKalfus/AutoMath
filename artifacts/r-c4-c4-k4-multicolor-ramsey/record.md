# statement_lock

- Active slug: `r-c4-c4-k4-multicolor-ramsey`.
- Active title: `Determine the exact value of R(C4, C4, K4)`.
- I am treating the working packet's frontier interval `20 <= R(C4, C4, K4) <= 21` as trusted input for solve.
- Under that input, the live decision problem is equivalent to this exact statement: does there exist a 3-coloring of `E(K_20)` whose color-1 graph is `C4`-free, whose color-2 graph is `C4`-free, and whose color-3 graph is `K4`-free?
- If such a coloring exists, the exact title theorem would be `R(C4, C4, K4) = 21`.
- If no such coloring exists, the exact title theorem would be `R(C4, C4, K4) = 20`.
- If the main claim closes either way, this still looks like roughly `70-90%` of a short paper; the packet's estimate `0.86` still looks reasonable.

# definitions

- All graphs are simple graphs on the fixed vertex set of `K_n`.
- A monochromatic `C4` means any 4-cycle in that color; it is not required to be induced.
- The green color is the `K4`-avoiding color; red and blue are symmetric `C4`-avoiding colors.
- Ambiguity noted and frozen: I did not locally re-derive the 2021 upper bound `R(C4, C4, K4) <= 21`; I used the packet's statement as a binding input.
- Missing definition resolved conventionally: the exact question is about the least `n` forcing one forbidden monochromatic subgraph in every 3-coloring of `E(K_n)`.

# approach_A

- Structural invariant route: exploit necessary local conditions in any hypothetical `(C4, C4, K4; 20)` coloring.
- For either `C4`-avoiding color `i`, any pair of vertices has at most one common neighbor in color `i`. Equivalently,
  `sum_v C(d_i(v), 2) <= C(20, 2)`.
- For any vertex `v` and either `C4`-avoiding color `i`, the color-`i` graph induced on the color-`i` neighborhood `N_i(v)` is a matching. Reason: if `x in N_i(v)` had color-`i` edges to distinct `y, z in N_i(v)`, then `y-v-z-x-y` is a monochromatic `C4`.
- For any vertex `v`, the green graph induced on `N_g(v)` is triangle-free. Reason: a green triangle inside `N_g(v)` together with `v` would form a green `K4`.
- These lemmas strongly constrain local shape, especially around high-degree vertices, but with only the packet-local context I could not turn them into a clean global contradiction on 20 vertices.
- Self-check: every statement above follows directly from the forbidden-subgraph definitions and does not depend on external literature.

# approach_B

- Construction/extremal route: since the packet gives the upper bound `21`, a single `(C4, C4, K4; 20)` witness would already settle the main theorem as `R(C4, C4, K4) = 21`.
- Naive blow-up templates look bad. Any monochromatic complete bipartite block `K_{a,b}` with `a, b >= 2` already contains a monochromatic `C4`, so coarse product or Turan-style block colorings are immediately hazardous for the red and blue colors.
- That pushes candidate constructions toward sparse, incidence-like, or geometry-like red/blue layers rather than large monochromatic blocks.
- I tested the cleanest rigid family first: undirected circulant colorings on `Z_n`, where the edge color depends only on cyclic distance.
- Exhaustive scan over all circulant signatures found no witness for `n in {18, 19, 20}`:
  - `n = 18`: checked all `3^9 = 19683` signatures, no witness.
  - `n = 19`: checked all `3^9 = 19683` signatures, no witness.
  - `n = 20`: checked all `3^10 = 59049` signatures, no witness.
- I then ran a bounded local search directly on `K_20`. The best coloring found in this run had only `5` forbidden patterns left:
  - `2` red `C4`s,
  - `3` blue `C4`s,
  - `0` green `K4`s,
  - edge counts `(red, blue, green) = (41, 40, 109)`.
- Self-check: the circulant computation is exact inside that family; the local search is only heuristic evidence and was not used as proof.

# lemma_graph

1. Use the packet's interval `20 <= R(C4, C4, K4) <= 21` to reduce the frontier decision to existence/nonexistence of a `(C4, C4, K4; 20)` coloring.
2. Any such coloring must satisfy the red/blue common-neighbor bounds and the matching structure inside same-color neighborhoods.
3. Any such coloring must also satisfy that every green neighborhood is triangle-free.
4. These local constraints immediately rule out naive coarse blow-up constructions.
5. Exact computation rules out the simplest highly symmetric circulant family on `18`, `19`, and `20` vertices.
6. The remaining live routes are:
   - convert the local constraints into a true impossibility proof on `20`, or
   - find a non-circulant witness by a more structured construction/search.

# chosen_plan

- I chose the witness side first. If a 20-vertex witness exists, then together with the packet's upper bound `21` the title theorem `R(C4, C4, K4) = 21` is already in hand.
- I started with structural lemmas because they are the cheapest reusable proof ingredients.
- After that stalled, I used minimal code in two steps only:
  - exact elimination of a rigid template family;
  - bounded search to test whether the witness side looks dead or merely delicate.
- The output of that plan is honest but partial: the exact main claim did not close, but the natural circulant family was fully ruled out and the witness side still looks plausible.

# self_checks

- Statement-lock check: the whole run is conditioned on the packet's trusted frontier interval `20 <= R <= 21`.
- Structural check: the local lemmas are direct and internally consistent.
- Enumeration check: I reran the circulant scan without the invalid color-fixing shortcut; the final counts above are from the full search.
- Search check: the near-miss on `K_20` is evidence only, not a mathematical certificate.
- Publication check: the current packet is still below the micro-paper threshold because the frontier theorem itself is unresolved.

# code_used

- Yes.
- Only ephemeral inline Python was used; no saved scripts or persistent helper files were created.
- Exact computation:
  - exhaustive scan of all undirected circulant signatures for `n = 18, 19, 20`;
  - each signature was checked for a red `C4`, a blue `C4`, and a green `K4`.
- Heuristic computation:
  - bounded local search on `K_20` minimizing the total number of forbidden subgraphs.
- Best heuristic output from this run:
  - `2` red `C4`s,
  - `3` blue `C4`s,
  - `0` green `K4`s,
  - edge counts `(41, 40, 109)`.

# result

- Main frontier claim unresolved in this solve run.
- Strongest exact output obtained here:
  `There is no undirected circulant 3-coloring of K_n for n in {18, 19, 20} whose red and blue graphs are C4-free and whose green graph is K4-free.`
- Strongest heuristic output obtained here:
  a 20-vertex coloring with no green `K4` and only five residual red/blue `C4`s.
- What part of the argument scales:
  - the neighborhood lemmas scale immediately to nearby mixed `(C4, C4, K_t)` instances;
  - the circulant-family scan scales directly to nearby `n` and nearby distinguished third-color clique targets.
- What part does not scale:
  - the local search does not produce a proof mechanism;
  - the current local lemmas do not yet force a contradiction on 20 vertices.
- Suggested theorem slice:
  the exact circulant-family obstruction above.
- Most useful next parameter shifts:
  - keep `n = 20` and search for a seeded non-circulant witness starting from the best near-miss;
  - compare with the same heuristic landscape on `n = 21` to see whether the obstruction changes sharply.
- Current package status:
  this is still a slice-level partial result, not yet a paper-shaped closure of the frontier claim.

# family_affinity

- Strong.
- This problem sits cleanly inside mixed multicolor Ramsey exact-value work involving two `C4`-avoiding colors and one clique-avoiding color.
- The strongest reusable content from this run is construction-side rather than proof-side: local forbidden-pattern lemmas plus one exact template-family obstruction.

# generalization_signal

- Moderate, but narrow.
- The local neighborhood restrictions are reusable across nearby tuples of the form `(C4, C4, K_t)`.
- The circulant exclusion method is also reusable as a first construction filter for nearby parameters.
- What does not yet generalize is any human-proof mechanism from the heuristic near-miss.

# proof_template_reuse

- Reusable proof ingredients:
  - common-neighbor bounds for each `C4`-free color;
  - matching structure inside same-color neighborhoods;
  - triangle-free green neighborhoods;
  - exact elimination of a rigid symmetry class before broader search.
- Not yet reusable:
  - no global contradiction lemma was extracted from the near-miss data;
  - no finite-geometry or incidence construction was isolated from the heuristic run.

# candidate_theorem_slice

- Exact slice visible from this run:
  `No undirected circulant 3-coloring of K_n for n in {18, 19, 20} avoids a red C4, a blue C4, and a green K4.`
- This is a real exact statement, but by itself it is too thin for the current micro-paper lane.

# smallest_param_shift_to_test

- First shift: stay at `n = 20`, but seed search from the best `5`-violation coloring rather than random starts.
- Second shift: test `n = 21` in the same heuristic framework, not to re-prove the packet upper bound, but to see whether the search landscape materially softens there.
- If staying proof-first, the smallest structural shift is to extract degree-profile constraints from the `0`-green-`K4` near-misses and ask whether they are compatible with the red/blue matching lemmas.

# why_this_is_or_is_not_publishable

- If the main claim closes, the result is still about `0.86` of a paper by the packet's estimate.
- Minimal remaining packaging after a true solve would be:
  - write the exact proof or display the explicit `20`-vertex coloring;
  - restate the 2008 and 2021 frontier bounds;
  - add one short discussion paragraph and one compact verification section.
- The current output is not publishable in the intended micro-paper lane.
- Reason: the frontier theorem itself is still open in this run, and the exact circulant obstruction is only a side slice, not the title result.
- Current result is therefore still too thin for the micro-paper objective.

# paper_shape_support

- If the witness side closes, the title theorem would be `R(C4, C4, K4) = 21`.
- If the impossibility side closes, the title theorem would be `R(C4, C4, K4) = 20`.
- One immediate remark that now naturally falls out:
  any eventual 20-vertex witness must be genuinely non-circulant in the undirected cyclic-distance sense.
- Another natural boundary remark:
  in the heuristic search, suppressing green `K4`s was easy relative to suppressing both red and blue `C4`s, so the paired `C4`-packing problem appears to be the real bottleneck.
- This run adds one genuine paper-shape support beam, but not enough to make the packet paper-ready.

# boundary_remark

- Boundary remark: the best near-miss had `0` green `K4`s but still `5` red/blue `C4`s, which suggests the third-color clique obstruction is not the hardest constraint at `n = 20`.
- Natural corollary if the witness side eventually closes:
  the 2021 upper bound `R(C4, C4, K4) <= 21` is tight, and the extremal `20`-vertex coloring must avoid the simplest circulant symmetry.
- Natural corollary if the impossibility side closes:
  the whole one-step frontier gap collapses to the lower endpoint with almost no editorial residue.

# likely_failure_points

- I relied on the packet for the live frontier interval `20 <= R <= 21`.
- The exact slice is only about one symmetry class; the true extremal object could be highly asymmetric.
- The heuristic near-miss is suggestive but not reliable as evidence for exact value.
- I did not yet convert the near-miss data into a degree-sequence or neighborhood-structure obstruction.

# what_verify_should_check

- Verify that the working packet's `20 <= R(C4, C4, K4) <= 21` basis is correct and current.
- Re-run the circulant enumeration exactly as a complete search over all `3^9`, `3^9`, and `3^10` signatures for `n = 18, 19, 20`.
- Audit the `C4` checker carefully:
  each 4-set contributes exactly three distinct 4-cycles, and each was checked in both red and blue.
- Audit the green `K4` checker:
  every 4-set must test all six edges.
- If constructive work continues, capture and inspect the best `5`-violation coloring to see whether one or two local surgery moves remain.
