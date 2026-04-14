# Solve Record: r-b4-b7-book-ramsey

## statement_lock
Work on the exact-value target:

Determine whether every graph `G` on `22` vertices contains `B4` or has complement containing `B7`.

Equivalently, either:

- prove `R(B4, B7) = 22` by showing every `22`-vertex graph forces `B4` or co-`B7`, or
- disprove `R(B4, B7) = 22` by producing one explicit `22`-vertex graph with no `B4` and no co-`B7`, which together with the packet upper bound `R(B4, B7) <= 23` yields `R(B4, B7) = 23`.

Exact title theorem if this closes: `The Exact Value of R(B4, B7)`.

If the main claim closes, this still looks like an `0.81` solve-to-paper candidate: the title theorem is already about `70-90%` of the note, and the remaining packaging is a compact witness verification appendix or a short forcing argument around the extremal `22`-vertex case.

## definitions
Use the standard book notation `Bt` for the graph of `t` triangles sharing a common spine edge.

For a graph `G` on `22` vertices:

- `G` contains `B4` iff some edge `uv` has at least `4` common neighbors.
- `\bar G` contains `B7` iff some nonedge `uv` of `G` has at least `7` common nonneighbors in `G`.

So a hypothetical `22`-vertex witness against `R(B4, B7) = 22` must satisfy:

- for every edge `uv`, `c(uv) := |N(u) ∩ N(v)| <= 3`;
- for every nonedge `uv`, `\bar c(uv) := |V \\ (N(u) ∪ N(v) ∪ {u,v})| <= 6`.

Useful rewrites:

- if `uv` is an edge, then `d(u) + d(v) = |N(u) ∪ N(v)| + c(uv) <= 20 + 3 = 23`;
- if `uv` is a nonedge, then `|N(u) ∪ N(v)| >= 14`, so `d(u) + d(v) - c(uv) >= 14`, in particular `d(u) + d(v) >= 14`.

## approach_A
Structural / invariant route.

Assume a `22`-vertex witness `G` exists.

First slice: edge and nonedge degree-sum constraints.

- every edge `uv` satisfies `d(u) + d(v) <= 23`;
- every nonedge `uv` satisfies `d(u) + d(v) >= 14`.

This already forces any witness into a narrow middle-degree regime: high-degree vertices cannot be adjacent to other high-degree vertices, and very low-degree vertices must be adjacent to nearly every other low-degree vertex.

Second slice: Goodman-type concentration.

Let `t` be the number of triangles of `G`, let `a` be the number of anti-triangles of `G`, and let `m = e(G)`.

- Because every edge lies in at most `3` triangles, `3t = sum_{e in E} c(e) <= 3m`, hence `t <= m`.
- Because every nonedge lies in at most `6` anti-triangles, `3a <= 6(231 - m)`, hence `a <= 2(231 - m)`.
- Therefore `t + a <= 462 - m`.

Goodman's identity gives

`t + a = C(22,3) - (1/2) * sum_v d(v)(21 - d(v)) = 1540 - (1/2) * sum_v d(v)(21 - d(v))`.

Combining with `t + a <= 462 - m` and `2m = sum_v d(v)` yields

`sum_v d(v)(20 - d(v)) >= 2156`.

Since `d(20 - d) = 100 - (d - 10)^2`, this becomes the exact concentration bound

`sum_v (d(v) - 10)^2 <= 44`.

So any `22`-vertex witness must be strongly concentrated around degree `10`; the budget for degree irregularity is tiny.

This is the cleanest durable theorem slice obtained in this run.

## approach_B
Construction / extremal route.

Try to realize an explicit `22`-vertex witness with local constraints:

- edges with common-neighbor count at most `3`,
- nonedges with common-nonneighbor count at most `6`.

I split this into two submodes.

Exact compact-family search:

- exhaustively tested all `2048` circulant graphs on `22` vertices;
- result: no circulant witness exists.

The best circulant near-miss was the step set `{1,2,3}` on `Z/22Z`, which already fails because some edges have `4` common neighbors. This gives one exact boundary statement: a `22`-vertex witness, if it exists, is not circulant.

Bounded unrestricted search:

- ran a small greedy local search over general `22`-vertex graphs, penalizing edge codegrees above `3` and nonedge cocodegrees above `6`;
- no witness found in the bounded run;
- the best near-miss had degree sequence consisting only of `9`s and `10`s, with exactly `3` bad edges of common-neighbor count `4` and `5` bad nonedges of common-nonneighbor count `7`.

This is negative evidence only, not a proof.

## lemma_graph
Assume a `22`-vertex witness `G` exists.

1. Translate `B4` / co-`B7` into edge-codegree and nonedge-cocodegree bounds.
2. Deduce the pairwise degree-sum constraints:
   edge `=> d(u)+d(v) <= 23`, nonedge `=> d(u)+d(v) >= 14`.
3. Apply Goodman counting to obtain `sum_v (d(v) - 10)^2 <= 44`.
4. Use the resulting near-regularity either:
   - to force a contradiction by analyzing the extendability of the known `21`-vertex obstruction, or
   - to narrow the witness search to a very small family and verify an explicit `22`-vertex graph.
5. Supporting exact side result from this run:
   no `22`-vertex circulant graph is a witness.

## chosen_plan
Take the structural slice as the main durable output, then use only minimal code as a bounded falsifier.

Reason for choosing this path:

- the packet says the problem is not `search_heavy`;
- the structural translation is strong enough to justify a witness search only after the reasoning layer is written down;
- an explicit witness would immediately give a paper-shaped title theorem, while a partial structural slice still has value only if it is exact and reusable.

The run did not close the theorem. I am stopping conservatively at the strongest honest package:

- one exact structural slice for any hypothetical `22`-vertex witness;
- one exact negative family result (`no circulant witness`);
- one bounded unrestricted search that produced only near-misses.

## self_checks
- Statement lock check: the target remains the exact `22` versus `23` dichotomy; no concept drift occurred.
- Definition check: `B4` and co-`B7` were translated only into common-neighbor / common-nonneighbor conditions, which is the standard book interpretation.
- Structural check: the degree-sum inequalities use only set-union identities and do not depend on unverified outside claims.
- Goodman check: `C(22,3) = 1540`, `C(22,2) = 231`, and the algebra to `sum_v (d(v)-10)^2 <= 44` was rechecked symbolically.
- Construction check: the circulant search is exact on its stated family; the unrestricted search is heuristic and is treated only as evidence.
- Publication check: the current package is theorem-facing but still too thin to count as a micro-paper by itself.

## code_used
Minimal code was used only after the reasoning stage.

Code tasks:

- exact exhaustive check of all `2048` circulant graphs on `22` vertices;
- bounded greedy local search on unrestricted `22`-vertex graphs.

Outputs:

- exact result: no circulant witness exists;
- heuristic result: no unrestricted witness found in the bounded run; best near-miss was `9/10`-regular-looking with `3` edge violations at level `4` and `5` nonedge violations at level `7`.

No SAT, ILP, CP-SAT, or broad brute-force enumeration of all `22`-vertex graphs was used.

## result
No exact theorem closure and no explicit `22`-vertex counterexample were obtained in this run.

Strongest honest output:

- exact theorem-facing slice: any `22`-vertex witness must satisfy
  `d(u)+d(v) <= 23` on edges,
  `d(u)+d(v) >= 14` on nonedges,
  and `sum_v (d(v)-10)^2 <= 44`;
- exact boundary remark: no `22`-vertex circulant witness exists;
- bounded-search evidence: best unrestricted near-misses are already forced into a very narrow `9/10`-degree regime.

Immediate corollary / remark that naturally falls out:

- any eventual `22`-vertex counterexample must be non-circulant and highly degree-concentrated.

Why this still matters:

- it narrows the certificate class sharply enough that the next solve pass should focus on extending or killing the published `21`-vertex obstruction family, rather than starting from arbitrary `22`-vertex graphs.

Current package status:

- still too thin for the micro-paper lane on its own;
- it does not yet supply the title theorem;
- it does supply a usable structural preface for the next exact push.

## family_affinity
Strong.

This target remains tightly anchored to the small off-diagonal book Ramsey table. The degree-sum translation and Goodman concentration argument are family-native and should transfer to other one-gap small-book pairs, especially when one wants to rule out a single remaining order by local structure before invoking heavier machinery.

## generalization_signal
Moderate.

The specific constants `23`, `14`, and `44` are special to `(B4, B7)` on `22` vertices, but the proof template scales: translate book constraints into edge/nonedge codegree caps, convert them into pairwise degree-sum restrictions, then combine those with Goodman counting to force near-regularity in any critical graph.

## proof_template_reuse
High.

Reusable template:

- translate the target books into local codegree bounds;
- derive edge and nonedge degree-sum inequalities;
- use triangle / anti-triangle counting plus Goodman;
- restrict to a compact critical-family search only after the structural slice is fixed.

That template is likely reusable for other one-gap off-diagonal book numbers where the remaining order is small enough that a compact witness class can be checked exactly.

## candidate_theorem_slice
Candidate theorem-facing slice:

`If G is a graph on 22 vertices with no B4 and with complement containing no B7, then for every edge uv one has d(u)+d(v) <= 23, for every nonedge uv one has d(u)+d(v) >= 14, and the degree sequence satisfies sum_v (d(v)-10)^2 <= 44.`

Supporting exact boundary slice:

`No circulant graph on 22 vertices avoids both B4 and co-B7.`

This is a real theorem slice, but not yet the title theorem.

## smallest_param_shift_to_test
The most useful nearby shift is downward to `(B4, B6)`.

Reason:

- a sharp local value for `R(B4, B6)` would turn large non-neighborhoods in a hypothetical `22`-vertex witness into an immediate contradiction;
- that makes `(B4, B6)` the most leverage-heavy adjacent parameter for bootstrapping the current structural slice.

Within the current exact pair, the most important non-parameter shift is not a new Ramsey instance but a sharper study of `22`-vertex extensions of the published `21`-vertex lower-bound family.

## why_this_is_or_is_not_publishable
It is not publishable yet.

Why a successful solve would be publishable:

- yes, closing `R(B4, B7)` exactly would already be about `70-90%` of a short paper;
- the exact title theorem is already clear: `The Exact Value of R(B4, B7)`;
- minimal remaining packaging would be a short verification appendix, a local extremal discussion, and the usual table update.

Why the current run is not enough:

- the theorem itself is still open after this run;
- the structural slice and no-circulant certificate are useful but subordinate;
- without either a forcing proof at order `22` or an explicit `22`-vertex witness, this remains supporting infrastructure rather than the paper.

## paper_shape_support
If the main claim closes, the smallest support package that makes it paper-shaped is:

- one compact forcing lemma or one explicit adjacency-list witness;
- the structural slice from this run as a short prelude explaining why the `22`-vertex critical case is tightly constrained;
- one exact sentence situating the result in the existing small-book table.

What extra structure would make the current partial package paper-shaped even before full closure:

- a proof that every `22`-vertex witness must lie inside the published `21`-vertex obstruction extension class, together with either a contradiction or a single surviving witness.

## boundary_remark
Exact boundary remark from this run:

- there is no circulant `22`-vertex graph witnessing `R(B4, B7) = 23`.

Interpretation:

- if a `22`-vertex counterexample exists, it is already more irregular than the most compact certificate family one would naturally try first.

## likely_failure_points
- The degree-concentration slice may still leave room for a non-circulant `22`-vertex witness.
- The unrestricted local search is only heuristic and does not certify nonexistence.
- I did not load the published `21`-vertex construction itself in this solve pass, so the key extendability analysis is not yet done.
- The current slice may need one more local counting lemma before it can force contradiction without direct construction analysis.

## what_verify_should_check
- Recheck the algebra from the Goodman identity to `sum_v (d(v)-10)^2 <= 44`.
- Rerun the circulant exhaustive search independently and archive the exact family statement if confirmed.
- If local source files become available in scope, compare the structural slice against the published `21`-vertex obstruction and test all `22`-vertex one-vertex extensions of that family first.
- Treat the unrestricted local-search negative result only as heuristic evidence, not as a theorem.
