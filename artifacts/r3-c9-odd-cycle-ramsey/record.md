# Solve Record: The Exact Value of R(C9, C9, C9)

## statement_lock
- Active slug: `r3-c9-odd-cycle-ramsey`.
- Active title: `Determine the exact value of R(C9, C9, C9)`.
- Exact intended statement for this solve run: either prove that every 3-coloring of `K33` contains a monochromatic `C9`, or construct a 3-coloring of `K33` with no monochromatic `C9` and thereby show `R(C9, C9, C9) >= 34`.
- The exact title theorem, if the upper-bound side closes, is `R(C9, C9, C9) = 33`.
- A successful exact solve would already be about `0.83` of a short paper, because it would settle the first open bounded three-color odd-cycle diagonal case named in the packet.

## definitions
- `C9` means a simple 9-cycle on distinct vertices.
- A `counterexample` means a 3-edge-coloring of `K33` with no monochromatic `C9`.
- For a color `i` and vertex `v`, write `N_i(v)` for the neighbors of `v` joined to `v` by color `i`.
- The standard lower-bound scaffold means the Bondy-Erdos four-block `32`-vertex construction behind the conjectural value `4n - 3`, here with four blocks of size `8`.
- Ambiguity kept explicit: the packet does not pin down one canonical internal realization of the `32`-vertex lower-bound coloring, so any argument that uses the scaffold must stay at the quotient/template level unless a concrete realization is fixed later.
- Missing load-bearing ingredient: no local file currently provides a proved stability theorem forcing a hypothetical `33`-vertex counterexample to resemble that four-block scaffold.

## approach_A
- Structural / invariant route: assume a counterexample exists and study monochromatic neighborhoods.
- Fix a vertex `v` and a color `i`. If the color-`i` graph induced by `N_i(v)` contained a `P8`, then adding `v` to the ends of that path would create a color-`i` `C9`.
- Therefore, in any counterexample and for every `v,i`, the graph `G_i[N_i(v)]` is `P8`-free.
- By the Erdos-Gallai path bound, a `P8`-free graph on `d = |N_i(v)|` vertices has at most `3d` edges.
- In particular, if `d >= 11`, then the majority-color neighborhood around `v` is locally sparse in its own color. For `d = 11`, at most `33` of the `55` internal edges of `N_i(v)` can use color `i`, so at least `22` internal edges are forced into the other two colors.
- This is the right local signature for a multipartite stability picture: a hypothetical counterexample cannot afford a dense monochromatic cluster around any vertex in its majority color.
- The natural next upgrade would be a global partition lemma turning these local `P8` exclusions into an almost-balanced four-block structure matching the known `32`-vertex lower-bound scaffold.

## approach_B
- Construction / extremal route: start from the standard `32`-vertex lower-bound scaffold and ask whether a `33`rd vertex can be added without creating a monochromatic `C9`.
- Model the lower-bound scaffold by four blocks `A,B,C,D`, each of size `8`, with the quotient `K4` colored by a 1-factorization. For each quotient edge, the corresponding monochromatic cross-block graph is a complete bipartite `K_{8,8}` in that color.
- Template obstruction lemma: if a new vertex `x` sends some color `c` to at least one vertex in each of the two blocks joined by a quotient edge of color `c`, then `x` already lies on a monochromatic color-`c` `C9`.
- Reason: pick `u` and `v` in those two blocks with `xu` and `xv` colored `c`. Inside the color-`c` `K_{8,8}` between the blocks there is a color-`c` path of length `7` from `u` to `v`, using `4` vertices from each side. Together with the edges `xu` and `xv`, this yields a color-`c` cycle of length `9`.
- So any counterexample built as a one-vertex extension of the standard lower-bound scaffold must obey a sharp quotient-level restriction: for every monochromatic block pair, the `33`rd vertex may not use that pair's own color on both sides of the pair.
- This turns the construction problem from an unrestricted coloring search into a finite attachment-signature problem plus an internal-block completion problem.
- What is still missing is the hard part: after imposing the quotient-level restriction, one must still prove that no compatible internal coloring of the enlarged blocks survives, or else explicitly exhibit one.

## lemma_graph
- `L1`: In a hypothetical counterexample, `G_i[N_i(v)]` is `P8`-free for every vertex `v` and color `i`.
- `L2`: By Erdos-Gallai, each such neighborhood is sparse in its own color.
- `L3`: A counterexample should therefore have strong multipartite/stability behavior rather than dense same-color neighborhood structure.
- `L4`: In the standard `32`-vertex scaffold, a `33`rd vertex cannot use a block-pair's own color on both sides of that monochromatic pair.
- `L5`: The main remaining task is to combine `L1`-`L4` into a theorem that every `33`-vertex counterexample must be an inadmissible extension of the `32`-vertex scaffold.

## chosen_plan
- The better path remains the upper-bound route, because closing it gives the exact title theorem `R(C9, C9, C9) = 33`.
- The construction route is still valuable, but right now it only yields a rigid attachment obstruction rather than an explicit `33`-vertex witness.
- Chosen proof plan:
1. Use `P8`-free monochromatic neighborhoods as the invariant that should force four-block structure.
2. Reduce any hypothetical `33`-vertex counterexample to a constrained extension of the standard `32`-vertex lower bound.
3. Kill the remaining admissible extension signatures by internal-block analysis.
- This is publication-aligned because, if it works, the main theorem is already the paper and the only packaging left is exposition plus a short critical-coloring discussion.

## self_checks
- Statement lock matches the active packet exactly.
- `Approach_A` contains one rigorous local lemma and one unproved global stability jump; I am not claiming the jump.
- `Approach_B` contains one rigorous quotient-level obstruction, but it relies on the standard four-block lower-bound scaffold rather than a locally fixed explicit witness.
- No exact value, proof, or `33`-vertex witness has been established in this run.
- The current output is theorem-facing but still incomplete.

## code_used
- No code was used in this run.
- Reason for keeping code off: the remaining gap is structural. Any useful search now would first need a canonical `32`-vertex template and a symmetry-reduced model of admissible `33`rd-vertex attachments. Without that setup, computation would be broader than the minimal-code policy allows for this stage.

## result
- No rigorous proof of `R(C9, C9, C9) = 33` and no explicit `33`-vertex counterexample were obtained in this solve run.
- The best honest progress is a pair of theorem-facing reductions:
  - every monochromatic neighborhood `G_i[N_i(v)]` in a hypothetical counterexample is `P8`-free,
  - every one-vertex extension of the standard `32`-vertex lower-bound scaffold is heavily restricted at the quotient level.
- Strongest honest takeaway: the remaining gap looks like a stability problem, not a broad search problem. Any successful proof of the upper bound likely has to show that every `33`-vertex counterexample is forced into a forbidden extension pattern of the known `32`-vertex scaffold.
- If the main claim closes, the exact title theorem is `The Exact Value of R(C9, C9, C9)`.
- Minimal remaining packaging work after a successful closure would be:
  - state the standard `32`-vertex lower bound cleanly,
  - present the stability/exclusion argument,
  - compare briefly with the solved predecessor `R(C7, C7, C7) = 25`,
  - add a short critical-coloring or boundary remark.
- The present result is still too thin for the micro-paper lane by itself.

## family_affinity
- Family affinity is high. Both reductions sit directly inside the Bondy-Erdos odd-cycle diagonal program.
- What part of the argument scales: the neighborhood observation scales from `C9` to general odd cycles `C_{2m+1}` by replacing `P8` with `P_{2m}` inside `N_i(v)`.
- The one-vertex extension obstruction also scales: in the standard `4(n-1)` lower-bound scaffold for `C_{2m+1}`, using a pair's own color on both sides of a monochromatic `K_{n-1,n-1}` again creates the target odd cycle through the new vertex.
- What does not yet scale is the missing stability step that turns those local restrictions into a global four-block decomposition.

## generalization_signal
- Generalization signal is moderate but conditional.
- If a four-block stability theorem can be proved here, the same proof template plausibly targets the next bounded odd-cycle diagonal cases rather than only `C9`.
- The most informative next parameter shifts are:
  - rephrase the solved `C7` case in the same neighborhood/extension language to see whether the method recovers known behavior,
  - test the same extension obstruction on `C11` to see which parts are family-level and which are genuinely `C9`-specific.
- At the moment this is still closer to an instance-guided family template than to a proved family theorem.

## proof_template_reuse
- Reusable proof template suggested by this run:
1. Assume a `3`-color counterexample on the conjectural upper-bound order.
2. Show each monochromatic neighborhood is path-free at the length that would close the target odd cycle through the center vertex.
3. Convert those local path obstructions into near-extremal block structure matching the Bondy-Erdos lower bound.
4. Prove that a new vertex cannot attach to both sides of a monochromatic template pair in the pair's own color.
5. Eliminate the remaining admissible attachment signatures.
- Reuse value is real only if step `3` becomes rigorous. Without that step, this is a scaffold rather than a proof method.

## candidate_theorem_slice
- The clearest candidate theorem slice visible from this run is:
  `In the standard four-block 32-vertex lower-bound scaffold for R(C9, C9, C9), any added vertex that uses the color of a quotient edge on both blocks incident to that edge creates a monochromatic C9.`
- Why this slice matters: it replaces an unrestricted `33`-vertex construction problem with a sharply constrained attachment problem.
- This is a genuine theorem-facing slice, but it is not yet strong enough to make the package publication-ready without the missing stability reduction.

## smallest_param_shift_to_test
- First shift to test: recover the solved `C7` benchmark in the same language. If the same neighborhood/extension mechanism already explains `R(C7, C7, C7) = 25`, that is evidence the method is on the right track.
- Second shift to test: carry only the quotient-level obstruction to `C11` and check whether it remains verbatim after replacing block size `8` by `10`.
- These shifts would clarify whether the current obstruction is merely instance-level or the front edge of a reusable theorem slice.

## why_this_is_or_is_not_publishable
- A full exact solve here would already be `70-90%` of a short paper; the packet's `0.83` estimate is still credible.
- The current output is not publishable. It isolates the likely stability bottleneck, but it does not settle the exact value and it does not yet prove a standalone structural theorem with independent paper weight.
- Minimal remaining packaging work if the main claim closes is small: exposition of the lower bound, the exact upper-bound argument, and one short remark on extremal colorings.
- As it stands, the current result is still too thin for the strict micro-paper lane.

## paper_shape_support
- What extra structure would make the result paper-shaped if the main claim closes:
  - one clean stability proposition reducing any hypothetical `33`-vertex counterexample to the standard `32`-vertex scaffold,
  - one exclusion proposition eliminating all admissible `33`rd-vertex attachment signatures,
  - one short extremal-coloring remark.
- One immediate corollary or natural remark, if the upper bound is proved, is that every extremal `32`-vertex avoiding coloring must be close to the known lower-bound scaffold, because the first extension step is already rigid.
- If that stability layer cannot be proved, then even a mathematically correct partial obstruction remains too thin to be paper-shaped.

## boundary_remark
- Exact boundary remark from this run: within the standard four-block lower-bound scaffold, the obstruction already appears at the first extension step. A `33`rd vertex may not use the color of a monochromatic block pair on both sides of that pair.
- This is useful because it says the problem is structurally narrow even though the exact value remains unresolved.

## likely_failure_points
- The main danger is that local `P8`-free neighborhoods do not by themselves force a unique or near-unique four-block global structure.
- The `32`-vertex lower bound may admit multiple internally different realizations, so a quotient-level argument alone may not shrink the extension problem to a tiny finite family.
- A genuine `33`-vertex counterexample could exist outside the naive one-vertex extension picture.
- If later computation is required, the search must be symmetry-reduced around a concrete lower-bound witness; otherwise it will violate the minimal-code intent of this stage.

## what_verify_should_check
- Verify the exact form of the Erdos-Gallai bound used here for `P8`-free graphs.
- Verify that the standard `32`-vertex lower-bound scaffold really contains monochromatic complete bipartite block pairs of size `8`, because `Approach_B` uses that exact feature.
- Compare the local path-neighborhood language with whatever is known for the solved benchmark `R(C7, C7, C7) = 25`.
- If computation is later introduced, verify that it is restricted to admissible `33`rd-vertex extension signatures rather than generic brute force.
