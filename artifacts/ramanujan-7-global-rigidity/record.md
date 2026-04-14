# Solve Record: ramanujan-7-global-rigidity

## statement_lock
We lock the intended statement as follows: determine whether every 7-regular Ramanujan graph is generically globally rigid in `R^2`, or else exhibit one 7-regular Ramanujan graph that is not generically globally rigid in `R^2`.

For the current worker run, the usable local reduction is the one stated in the selection packet: the only unresolved orders are `n in {16, 18, 20}`, while orders `> 22` are already covered by the 2023 source.

The exact title-theorem target, if this closes positively, is:
"Every 7-regular Ramanujan graph is globally rigid in `R^2`."

If this closes negatively, the title theorem becomes:
"A 7-regular Ramanujan graph that is not globally rigid in `R^2`."

## definitions
- Interpret "globally rigid in `R^2`" in the standard generic-combinatorial sense used in rigidity theory.
- A 7-regular Ramanujan graph means a 7-regular graph whose nontrivial adjacency eigenvalues have absolute value at most `2*sqrt(6)`.
- Local finite-residue target: it is enough to settle the small orders `16, 18, 20`.
- Conventions for separator analysis:
  - `S` is a vertex cut.
  - `A` is a smallest component of `G - S`.
  - `C = V(G) \\ (A union S)`.
  - `a = |A|`, `s = |S|`, `c = |C|`.

Ambiguities or missing local inputs:
- The repo does not contain the source paper's exact Section 6 tables or the canonical finite residue data.
- The repo also does not contain a precomputed list of 7-regular Ramanujan graphs on orders `16, 18, 20`.
- Because solve runs with web disabled, any exact closure here must come from local reasoning or a very small local certification computation.

## approach_A
Structural / invariant approach.

Try to force high vertex connectivity from the Ramanujan eigenvalue bound. If every unresolved graph is at least 6-connected, then one can route to a known planar global-rigidity criterion already described in the source packet as part of the "connectivity and spectral machinery."

The immediate separator facts are:
- Since every vertex in `A` has degree `7` and no neighbors in `C`, we have `7a = 2e(A) + e(A,S)`.
- Because `e(A) <= a(a-1)/2` and `e(A,S) <= as`, any separator must satisfy `a >= 8 - s`.
- Expander mixing for the empty cut between `A` and `C` gives
  `49ac <= 24(a+s)(c+s)`.
  This already rules out `1`- and `2`-cuts for `n in {16,18,20}`, and it also rules out a `3`-cut when `n = 20`.

The sharper idea is to combine separator saturation with quotient-matrix interlacing:
- when `s` is small, `A` must be extremely dense;
- that forces many edges from `S` into `A`;
- then the block partition `(A union S, C)` or `(A, S, C)` has a nontrivial quotient eigenvalue that may exceed `2*sqrt(6)`, contradicting Ramanujan.

This is the best purely structural route visible from the local packet.

Self-check after Approach A:
- This uses only local packet facts plus standard spectral manipulations.
- It is theorem-facing and could become paper-shaped if it eliminates all small separators strongly enough to certify generic global rigidity.
- The unresolved point is whether the argument can eliminate `4`- and `5`-cuts, not just `1`-, `2`-, and `3`-cuts.

## approach_B
Construction / extremal / contradiction approach.

Assume a counterexample exists among orders `16, 18, 20`.

Then at least one of the usual obstructions to planar generic global rigidity must occur:
- low vertex connectivity, or
- failure of redundant rigidity.

The contradiction strategy is:
- show low-connectivity obstructions are spectrally impossible for Ramanujan graphs at these orders;
- if separator obstructions survive, convert them into a tiny family of quotient templates;
- only after both conceptual routes are exhausted, use a bounded local computation to test the quotient templates or certify that the surviving obstruction shapes still violate the Ramanujan bound.

This is still not full graph enumeration. It is a template-level falsifier for possible counterexample geometry.

Self-check after Approach B:
- This keeps code secondary and bounded.
- It does not silently switch to exhaustive search.
- It remains honest about the missing local residue tables.

## lemma_graph
Working proof skeleton.

1. Finite reduction from the packet: only `n = 16, 18, 20` matter.
2. If `G` has a separator `S` of size `s <= 5`, let `A` be a smallest component of `G-S`.
3. Degree counting gives `a >= 8 - s`.
4. Expander mixing on the empty bipartite pair `(A,C)` gives `49ac <= 24(a+s)(c+s)`.
5. For `s = 3`, the small value of `a` forces `A` to be complete and fully joined to `S`.
6. That saturates the degree budget of `S`, forcing a small cross-edge count between `A union S` and `C`.
7. The two-block quotient matrix for `(A union S, C)` then has second eigenvalue
   `7 - m/(a+s) - m/c`,
   where `m = e(S,C)`.
8. If this exceeds `2*sqrt(6)`, Ramanujan is contradicted.
9. Repeat the same template for `s = 4` and `s = 5`; if all such cuts are eliminated, the separator route is dead.
10. If a sufficiently strong connectivity threshold follows, invoke the source-paper machinery to convert it into global rigidity.

## chosen_plan
Best current path:
- first eliminate all `3`-cuts by a direct hand proof using the saturated-small-component argument;
- then test the surviving `4`- and `5`-cut quotient templates by a tiny local eigenvalue computation;
- if those templates all violate the Ramanujan bound, the separator obstruction is gone;
- if they do not, stop conservatively and record that the present run produced a structural slice, not a closure.

This is the best available route because the local repo does not expose the exact residue tables needed for graph-by-graph certification.

## self_checks
- The solve is still inside the small-order residue identified by the packet.
- No web or outside source is being used.
- No brute-force graph generation has started.
- A tiny quotient-matrix computation is justified only after the two reasoning routes above.
- After the bounded computation, the argument still does not claim the main theorem; it only claims the separator slice that the computation actually certifies.

## code_used
Yes, but only minimally.

Used one tiny local Python script to enumerate feasible `(A,S,C)` quotient templates for small separators:
- inputs: `n in {16,18,20}`, `s in {3,4,5}`, component size `a`, cut-edge count `x = e(A,S)`, and `m = e(S,C)`;
- constraints enforced:
  - `A` is connected,
  - `A` has no edges to `C`,
  - degree sum on `S` is respected,
  - internal edges of `S` fit a simple graph on `s` vertices;
- output: the nontrivial eigenvalues of the quotient matrix.

This is not graph enumeration. It is a bounded obstruction-template check.

## result
Partial but mathematically real.

Certified theorem-facing slice from the present run:
- every 7-regular Ramanujan graph on `16`, `18`, or `20` vertices has no vertex cut of size at most `3`;
- every 7-regular Ramanujan graph on `20` vertices has no vertex cut of size `4`.

Equivalently:
- for the unresolved orders `16` and `18`, any counterexample must be at least `4`-connected;
- for order `20`, any counterexample must be at least `5`-connected.

How this was obtained:
- `1`- and `2`-cuts are ruled out directly by expander mixing on the empty pair `(A,C)`;
- all feasible `3`-cut quotient templates violate the Ramanujan bound `|lambda| <= 2*sqrt(6)`;
- all feasible `4`-cut quotient templates for `n = 20` also violate the same bound.

What remains unresolved:
- `4`-cut templates survive the quotient check for `n = 16` and `n = 18`;
- `5`-cut templates survive for all three unresolved orders;
- no redundant-rigidity conclusion was obtained from the current local data.

So this run did not solve the intended statement. It did, however, produce a nontrivial structural slice that narrows the counterexample geometry.

## family_affinity
High. This sits exactly on the family anchor from the packet: the remaining exact-degree residue for global rigidity of Ramanujan graphs.

## generalization_signal
Moderate.

The separator-plus-interlacing method transfers cleanly to bounded separator sizes and other fixed-degree spectral residues, but the constants are degree-specific and the method weakens once `s = 5` leaves enough degree budget in the separator.

## proof_template_reuse
The reusable template is:
- reduce to a finite unresolved residue;
- encode any low-connectivity obstruction by a tiny separator partition;
- use degree saturation to bound the quotient matrix;
- contradict the Ramanujan spectral window by interlacing.

What scales:
- the finite-residue-plus-separator-template reduction;
- the quotient-matrix contradiction for very small cuts.

What does not yet scale:
- larger separator sizes where the middle block still has enough degree budget to keep quotient eigenvalues inside the Ramanujan window;
- any step that would convert connectivity alone into redundant rigidity without importing more of the source paper.

## candidate_theorem_slice
Smallest honest theorem slice currently visible:

"A 7-regular Ramanujan graph on `16`, `18`, or `20` vertices has no vertex cut of size at most `3`; moreover, a 20-vertex 7-regular Ramanujan graph has no vertex cut of size `4`."

Immediate corollary / remark:
"Any unresolved counterexample to global rigidity in the degree-7 Ramanujan residue must be at least 4-connected, and if it has 20 vertices then it must be at least 5-connected."

If the remaining `4`- and `5`-cut cases can also be excluded, the slice becomes substantially stronger and closer to paper shape.

## smallest_param_shift_to_test
The immediate parameter shifts worth testing are:
- separator size `s = 4`;
- separator size `s = 5`.

After the present run:
- `s = 4` remains open only for orders `16` and `18`;
- `s = 5` is the dominant unresolved separator size.

So the best next parameter shifts are:
- `n = 16, s = 4`;
- `n = 18, s = 4`;
- then `s = 5` with additional rigidity information rather than more raw quotient bounds.

## why_this_is_or_is_not_publishable
If the main claim closes, this is likely `70-90%` of a paper, consistent with the packet's `single_solve_to_paper_fraction = 0.77`.

At the current stage it is not publishable:
- it is still a proof program rather than an exact theorem closure;
- it does not yet certify all unresolved small orders;
- it does not yet produce a counterexample;
- the current slice is interesting but still too thin by itself for the micro-paper lane.

Minimal remaining packaging work after a positive closure would be:
- state the finite reduction from the 2023 paper,
- present the small-order separator elimination or residue certification,
- append one short corollary that the all-orders `k = 7` case is settled.

Current micro-paper assessment:
- the result is closer to a theorem-shaped slice than to a paper-ready solve;
- it is not yet enough to claim that the current package is paper-shaped.

## paper_shape_support
What extra structure would make this paper-shaped if the main claim closes?

- an exact theorem slice eliminating all small separator types for the residue orders;
- one clean bridge sentence from that slice to generic global rigidity via the source paper's rigidity machinery;
- one compact residue summary table for `n = 16, 18, 20`.

Without that exact closure, the present run is still too thin for the micro-paper lane.

One natural corollary already visible:
- any future counterexample at the unresolved orders must have unexpectedly high connectivity, so the search space is materially narrower than the raw finite residue suggests.

## boundary_remark
Natural boundary remark if the positive route works:

"The only nontrivial work beyond the 2023 asymptotic theorem is the finite residue at orders `16`, `18`, and `20`; once those cases are certified, the degree-7 all-orders statement follows immediately."

Current boundary remark:
"The present separator argument seems to stop exactly where the separator itself still has enough unused degree budget to mimic an expander, which is why `s = 5` remains alive under quotient interlacing alone."

## likely_failure_points
- The local repo does not include the source's exact residue tables.
- Separator exclusion may stop at `4`- or `5`-cuts and fail to imply enough rigidity.
- Even if all low-connectivity obstructions are eliminated, a redundant-rigidity obstruction might still survive unless the source machinery already closes that gap.
- The quotient-template computation is a certification of impossible separator shapes, not a substitute for a full rigidity proof.

## what_verify_should_check
- Confirm that the 2023 source really reduces the exact `k = 7` problem to orders `16, 18, 20`.
- Check whether the source machinery indeed turns the connectivity threshold achieved here into generic global rigidity in `R^2`.
- Verify the separator inequalities and quotient-eigenvalue bounds.
- If a full closure is later claimed, perform a bounded prior-art check that the exact degree-7 completion has not already appeared after 2023.
