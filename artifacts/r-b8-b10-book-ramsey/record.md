# Solve Record: The Exact Value of R(B8, B10)

## statement_lock
We use the standard book-graph convention: `B_t` is the graph of `t` triangles sharing one common spine edge.

Thus the exact target is:

- either prove that every graph `G` on `37` vertices contains `B8` or its complement contains `B10`, which would give `R(B8, B10) = 37`;
- or construct a graph `G` on `37` vertices such that every edge of `G` has at most `7` common neighbors and every nonedge of `G` has at most `9` common nonneighbors, which would give `R(B8, B10) = 38`.

If this closes, the honest title theorem is exactly:

- `The Exact Value of R(B8, B10)`.

A successful closure here is already in the micro-paper lane: it would be about `85%` of a short note, with only verification, comparison to nearby exact cases, and Lean packaging left.

## definitions
Write `v = 37`, `e = e(G)`, `T = t(G)`, `\bar e = e(\bar G)`, and `\bar T = t(\bar G)`.

For distinct vertices `u, v`:

- if `uv` is an edge of `G`, let `c_G(u,v) = |N(u) cap N(v)|`; then `G` avoids `B8` iff `c_G(u,v) <= 7` for every edge `uv`;
- if `uv` is a nonedge of `G`, let `cn_G(u,v)` be the number of common nonneighbors of `u, v`; then `\bar G` avoids `B10` iff `cn_G(u,v) <= 9` for every nonedge `uv`.

I use Goodman's identity in the form

`T + \bar T = C(37,3) - (1/2) * sum_x d(x)(36 - d(x))`.

Numerically:

- `C(37,2) = 666`;
- `C(37,3) = 7770`.

## approach_A
Structural / invariant approach.

Assume for contradiction that a `37`-vertex witness `G` exists with no `B8` in `G` and no `B10` in `\bar G`.

Triangle caps in the two colors give:

1. Every edge of `G` lies in at most `7` triangles, so `3T <= 7e`.
2. Every edge of `\bar G` lies in at most `9` triangles of `\bar G`, so `3\bar T <= 9\bar e`.

Hence

`T + \bar T <= (7/3)e + 3\bar e = 1998 - (2/3)e`.

Substitute `e = (1/2) * sum_x d(x)` and compare with Goodman:

`7770 - (1/2) * sum_x d(x)(36 - d(x)) <= 1998 - (1/3) * sum_x d(x)`.

After rearranging,

`sum_x (106 d(x) - 3 d(x)^2) >= 34632`.

Now consider the integer quadratic

`f(d) = 106d - 3d^2`.

Its real maximum occurs at `d = 53/3`, so on integers the unique maximum is

- `f(18) = 936`,

and `f(d) <= 936` for every integer `d`, with equality only at `d = 18`.

Since there are `37` vertices,

`sum_x (106 d(x) - 3 d(x)^2) <= 37 * 936 = 34632`.

So equality must hold throughout, and therefore every vertex has degree exactly `18`.

Consequences:

- `G` is `18`-regular;
- `e = 37 * 18 / 2 = 333`;
- `\bar e = 333`.

Returning to the triangle bounds,

`T + \bar T <= (7/3) * 333 + 3 * 333 = 777 + 999 = 1776`.

But Goodman with all degrees `18` gives

`T + \bar T = 7770 - (1/2) * 37 * 18 * 18 = 1776`.

So equality also holds in both triangle-cap inequalities. Since each edge contribution was individually capped, this forces:

- every edge of `G` has exactly `7` common neighbors;
- every edge of `\bar G` has exactly `9` common neighbors in `\bar G`;
- equivalently, every nonedge of `G` has exactly `9` common nonneighbors.

Now fix a nonedge `uv` of `G`, and let `c = c_G(u,v)`.
Because `d(u) = d(v) = 18`,

- `|N(u) cup N(v)| = 18 + 18 - c = 36 - c`;
- among the other `35` vertices, the number adjacent to neither `u` nor `v` is `35 - (36 - c) = c - 1`.

But this is exactly `cn_G(u,v)`, so `c - 1 = 9`, hence `c = 10`.

Therefore any `37`-vertex witness would have parameters

- regular degree `18`,
- adjacent-pair common-neighbor count `7`,
- nonadjacent-pair common-neighbor count `10`,

that is, it would be an `srg(37,18,7,10)`.

Now rule this out spectrally.

Let `A` be the adjacency matrix of such a graph. The strongly regular relation is

`A^2 = 7A + 10(J - I - A) + 18I = -3A + 8I + 10J`.

On the subspace `1^perp`, the `J` term vanishes, so eigenvalues `x` satisfy

`x^2 + 3x - 8 = 0`.

Thus the two nontrivial eigenvalues are

`r, s = (-3 +- sqrt(41)) / 2`.

Because `A` has integer entries, its characteristic polynomial has rational coefficients, so the irrational conjugates `r` and `s` must occur with equal multiplicity. Since `dim(1^perp) = 36`, each would have multiplicity `18`.

But then the trace on `1^perp` would be

`18(r + s) = 18(-3) = -54`.

That is impossible, because `G` is `18`-regular, so the all-ones vector gives one eigenvalue `18`, and the remaining eigenvalues must sum to `-18` because `trace(A) = 0`.

Contradiction.

So no `37`-vertex witness exists, and therefore

- `R(B8, B10) = 37`.

Self-check after Approach A:

- The argument uses only the packet's one-gap window and standard graph identities.
- Equality propagation is exact: no heuristic regularity assumption was inserted.
- The spectral contradiction closes the title theorem candidate without code.

## approach_B
Construction / extremal / contradiction approach.

Assume a `37`-vertex witness exists and inspect the local partition around a vertex `v`.

From Approach A, any witness would already have to be `18`-regular. Let

- `A = N(v)`, so `|A| = 18`;
- `B = V(G) \\ (A cup {v})`, so `|B| = 18`.

The forced local profile is:

1. If `x in A`, then the edge `vx` has exactly `7` common neighbors, all in `A`. So `x` has exactly `7` neighbors in `A`, hence `10` neighbors in `B`.
2. If `y in B`, then `vy` is a nonedge. The common nonneighbors of `v` and `y` are exactly the vertices of `B \\ {y}` that are nonadjacent to `y`. Since there are exactly `9` of them, `y` has `17 - 9 = 8` neighbors in `B`, hence `10` neighbors in `A`.

So every local view of a hypothetical witness has quotient matrix

`[[7,10],[10,8]]`.

This is the extremal interpretation of the main proof: a `37`-vertex obstruction is not a loose search object. It would have to be a globally balanced, locally equitable, strongly regular graph with parameters `(37,18,7,10)`. Once one reaches that point, the spectral obstruction in Approach A kills the construction.

Self-check after Approach B:

- This route is not the shortest proof, but it exposes the exact local shape of any putative obstruction.
- The local partition data matches the global pair-count data from Approach A.
- It supports the paper narrative that the final one-gap residue collapses to a rigid impossible template.

## lemma_graph
1. `B8`-avoidance in `G` is equivalent to `c_G(u,v) <= 7` on every edge.
2. `B10`-avoidance in `\bar G` is equivalent to `cn_G(u,v) <= 9` on every nonedge.
3. Hence `3T <= 7e` and `3\bar T <= 9\bar e`.
4. Combine those bounds with Goodman to get `sum_x (106 d(x) - 3 d(x)^2) >= 34632`.
5. The quadratic bound is sharp only at `d(x) = 18`, so any witness is `18`-regular.
6. Equality then propagates to exact pair counts: each edge has exactly `7` common neighbors, each nonedge exactly `9` common nonneighbors.
7. Therefore each nonedge has exactly `10` common neighbors.
8. So any witness must be `srg(37,18,7,10)`.
9. The adjacency-matrix relation for that parameter set forces irrational conjugate eigenvalues with equal multiplicities, but the trace requirement for an `18`-regular graph disagrees.
10. Therefore no witness exists and `R(B8, B10) = 37`.

## chosen_plan
The best path was Approach A.

Reason:

- it converts the asymmetric one-gap problem into a sharp weighted Goodman equality problem;
- it forces a unique degree profile instead of leaving a broad construction search;
- it closes the instance cleanly once the impossible strongly regular parameter set is identified.

I did not turn on Lean and I did not use code. The solve-stage gain came from the structural reduction plus the spectral contradiction, not from a search certificate.

## self_checks
- Statement-lock check: the run stayed fixed on the exact `37` versus `38` question for `R(B8, B10)`.
- Definition check: `B8` and complement-`B10` were translated only through common-neighbor / common-nonneighbor counts.
- Arithmetic check: all numeric constants come from `C(37,2) = 666`, `C(37,3) = 7770`, and degree `18`.
- Equality check: once the degree quadratic saturates, both triangle-cap inequalities also saturate edgewise.
- Spectral check: the impossibility uses only the adjacency relation, rational characteristic polynomial, and trace.

## code_used
No code used.

Reason:

- the reasoning-first route already produced a full exact-value candidate proof;
- the packet explicitly downranks search-heavy work, and nothing in the solved argument required brute force, SAT, or bounded enumeration;
- any code at this point would only duplicate checks that belong in verify, not solve.

## result
Main outcome of this solve run:

- I obtained a full exact-value candidate proof that `R(B8, B10) = 37`.

Exact title theorem:

- `R(B8, B10) = 37`.

Smallest supporting theorem slice extracted from the proof:

- any graph on `37` vertices with no `B8` and no complement-`B10` must be `srg(37,18,7,10)`, hence impossible.

One immediate corollary / remark:

- there is no irregular or ad hoc `37`-vertex obstruction; any such obstruction would have to be a highly rigid strongly regular graph.

What extra structure would make this result paper-shaped if the main claim closes?

- the main claim is already closed at the solve stage, so the extra structure is now only packaging: verification of the arithmetic and spectral step, a short comparison with the neighboring exact case `R(B9, B10) = 39`, and Lean preservation if desired.

Minimal remaining packaging work:

- write the proof in short-note form;
- add a one-paragraph literature comparison on the `B_{n-2}` versus `B_n` line;
- run bounded prior-art verification and then Lean only if the manager wants formal sealing.

Current package assessment:

- this is not just an instance-only witness or a thin slice;
- if the proof survives verification, it is already the title theorem of the selected micro-paper target.

Self-check after result:

- The solve output is genuinely theorem-shaped.
- It already sits in the promised `70-90%` paper band.
- The remaining risk is verification, not missing mathematical structure.

## family_affinity
High.

This proof sits exactly on the almost-diagonal book-Ramsey line `R(B_{n-2}, B_n)`. The argument uses family-native quantities only: common-neighbor caps, Goodman's identity, forced regularity, and the resulting strongly regular obstruction.

## generalization_signal
Moderate-to-strong.

What part of the argument scales:

- the weighted Goodman saturation step at the one-gap order `4n - 3`;
- the forced regularity of any hypothetical witness;
- the reduction from a Ramsey obstruction to a specific strongly regular parameter set.

Concretely, the same algebra suggests the family reduction

## lean_statement
- Lean target formalized in `lean/AutoMath/RB8B10BookRamsey.lean` and mirrored at `artifacts/r-b8-b10-book-ramsey/lean/AutoMath/RB8B10BookRamsey.lean`.
- Exact Lean statement for this run:
  - `∀ {V} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj], ¬ G.IsSRGWith 37 18 7 10`.
- This matches the strongest honest reusable theorem slice extracted by solve and verify:
  - any hypothetical `37`-vertex obstruction to `R(B8, B10) = 37` would have to be `srg(37,18,7,10)`, so ruling out that parameter set is the packet-sealing Lean target.

## lean_skeleton
- I wrote a checked Lean module for the obstruction slice rather than over-claiming the full Ramsey theorem.
- The module includes:
  - `rb8b10_book_ramsey_statement`: faithfulness check for the intended SRG nonexistence target;
  - `parameters_satisfy_basic_srg_identity`: the basic SRG parameter equation for `(37,18,7,10)`;
  - `srg_matrix_identity`: the specialized adjacency-matrix identity from `SimpleGraph.IsSRGWith.matrix_eq`;
  - `trace_adjMatrix_zero`: zero-trace fact for adjacency matrices;
  - `spectral_factor_count_impossible`: the arithmetic contradiction `a + 2b = 37` together with `18a - 3b = 0`;
  - `srg_37_18_7_10_nonexistence_skeleton`: a checked skeleton reducing the final theorem to one missing spectral/minpoly factor-count lemma.
- Build checks run:
  - `lake build AutoMath.RB8B10BookRamsey`
  - `lake env lean ../artifacts/r-b8-b10-book-ramsey/lean/AutoMath/RB8B10BookRamsey.lean`

## lean_result
- Lean compilation succeeded for the new backend module and its mirrored artifact copy.
- Honest outcome:
  - the intended SRG obstruction statement is now present in the official Lean backend;
  - the key arithmetic sub-lemmas around the obstruction are formally checked;
  - the final nonexistence theorem is still a skeleton, so this run does **not** upgrade the candidate to `EXACT`.
- Publication consequence:
  - Lean advanced the packet materially, but it did not yet seal the note.
  - The run remains a live micro-paper candidate pending one last spectral/minpoly formalization step.

## lean_blockers
- The remaining blocker is not arithmetic; it is the bridge from the checked SRG matrix identity to the needed characteristic/minimal-polynomial factor-count equations.
- Concretely, Lean still needs a clean proof of the following implication for a hypothetical `srg(37,18,7,10)` adjacency matrix:
  - only one linear `18` contribution and quadratic `x^2 + 3x - 8` contributions can occur in the characteristic-polynomial support, yielding `a + 2b = 37` and `18a - 3b = 0`.
- I did not claim this step without proof and I did not use `sorry`, `admit`, or new axioms.
- Because that spectral/minpoly bridge is still missing, the strongest honest Lean status is:
  - checked theorem-slice statement plus checked support lemmas,
  - `lean_complete = false`,
  - `classification = CANDIDATE`,
  - `publication_status = SLICE_CANDIDATE`.

- a graph on `4n - 3` vertices avoiding `B_{n-2}` and whose complement avoids `B_n` would have to be `srg(4n - 3, 2n - 2, n - 3, n)`.

What does not automatically scale:

- the final obstruction step. For `n = 10`, the parameter set `(37,18,7,10)` is spectrally impossible by a short trace argument. For nearby `n`, the same forced parameter set may require a different existence/nonexistence check, and I am not claiming a full family theorem here without a separate verification pass.

Current package status relative to paper-shape:

- for `n = 10`, this is already close to paper-shaped;
- for the broader family, the reusable part is the reduction template, not yet a published family theorem.

## proof_template_reuse
High reuse potential.

Template:

1. translate book avoidance into edge codegree caps in both colors;
2. combine the two triangle caps with Goodman's identity;
3. force equality in a one-variable quadratic degree bound;
4. propagate equality to exact adjacent/nonadjacent common-neighbor counts;
5. identify the resulting strongly regular parameter set;
6. discharge that parameter set by a spectral or existence obstruction.

This is a reusable proof template for other one-gap almost-diagonal book Ramsey residues.

## candidate_theorem_slice
Candidate theorem slice:

- `Any graph on 37 vertices with no B8 and no complement-B10 must be strongly regular with parameters (37,18,7,10), and therefore does not exist.`

The smaller support theorem inside it is:

- `Any graph on 37 vertices with no B8 and no complement-B10 must be srg(37,18,7,10).`

That slice is exact, compact, and directly supports the title theorem.

## smallest_param_shift_to_test
The most informative next parameter shifts are:

- `R(B9, B11)`: the next almost-diagonal step on the same `B_{n-2}` versus `B_n` line;
- `R(B10, B12)`: one more step up the same line, already present as a local working packet.

Why these help most:

- they test whether the same weighted Goodman collapse keeps forcing impossible strongly regular parameters;
- they would tell us quickly whether the current proof is an isolated `n = 10` win or the visible start of a broader almost-diagonal mechanism.

## why_this_is_or_is_not_publishable
If verification confirms the proof, this is publishable as a micro-paper.

Why:

- the exact title theorem is closed;
- the literature shell is already present in the packet;
- the proof is short, self-contained, and family-anchored;
- the result appears to be in the intended `70-90%` single-solve-to-paper band.

Exact title theorem for publication:

- `The Exact Value of R(B8, B10)`.

Minimal remaining packaging work:

- tighten the exposition;
- include the one-gap context `37 <= R(B8, B10) <= 38`;
- add one short comparison with `R(B9, B10) = 39`;
- preserve the proof in Lean only after verification signs off.

Whether the current result is too thin for the micro-paper lane:

- no. This is already the right theorem-shaped unit for the micro-paper objective, not a thin instance with missing narrative.

## paper_shape_support
- Title theorem: `R(B8, B10) = 37`.
- Why a successful solve is already `70-90%` of a paper: the theorem itself is the note, and the rest is only proof polish plus table placement.
- Smallest supporting theorem slice: any `37`-vertex obstruction would be `srg(37,18,7,10)`.
- Immediate corollary: no irregular `37`-vertex obstruction exists.
- Minimal remaining packaging work: verify arithmetic and spectral details, add a short family comparison, then decide whether Lean sealing is worth the cost.

## boundary_remark
The asymmetric pair `(8,10)` still collapses to a perfectly balanced critical profile at the one-gap boundary: a hypothetical `37`-vertex obstruction would have to be `18`-regular with adjacent codegree `7` and nonadjacent codegree `10`. So the remaining residue was rigid rather than search-heavy.

## likely_failure_points
- A Goodman arithmetic slip in the passage from triangle caps to `sum_x (106 d(x) - 3 d(x)^2) >= 34632`.
- A mistaken equality-propagation step from the total triangle count to edgewise exact codegrees.
- A bad translation between complement-`B10` avoidance and common nonneighbors in `G`.
- A gap in the spectral contradiction, especially the equal-multiplicity claim for irrational conjugate eigenvalues of an integral matrix.

These are verification risks, not conceptual gaps in the proof plan.

## what_verify_should_check
- Recompute the Goodman identity constants for `v = 37`.
- Re-derive `3T <= 7e` and `3\bar T <= 9\bar e`.
- Check the rearrangement to `sum_x (106 d(x) - 3 d(x)^2) >= 34632`.
- Confirm that `f(d) = 106d - 3d^2` has unique integer maximum `936` at `d = 18`.
- Verify that equality indeed forces `18`-regularity and exact counts `lambda = 7`, common-nonneighbor count `9`, and hence `mu = 10`.
- Check the adjacency-matrix identity `A^2 = -3A + 8I + 10J`.
- Check that the irrational roots `(-3 +- sqrt(41))/2` must occur with equal multiplicity and that this contradicts the trace.
- Run the usual bounded prior-art verification on the exact statement and, if retained, on the family-reduction remark.

## verify_rediscovery
Bounded PASS 1 audit on `2026-04-13` did not establish rediscovery.

What was checked:

- exact-term searches for `R(B8, B10)` and notation variants such as `R(B_8, B_10)`;
- the canonical 2025 source `Small Ramsey Numbers for Books, Wheels, and Generalizations`;
- DS1.17 / Section `5.3(g)` for the recorded upper-bound status;
- a bounded recent-status sweep keyed to the 2026 Wesley follow-up.

Outcome:

- the 2025 paper still supplies the lower-bound side of the one-gap window, not an exact determination;
- DS1.17 still records the upper-bound mechanism leaving `37 <= R(B8, B10) <= 38`;
- the bounded recent-status sweep did not surface a later paper, preprint, theorem, proposition, example, observation, or corollary explicitly settling the exact pair.

Conservative verdict:

- no rediscovery found within budget;
- novelty remains plausible but should still be re-checked at publication-audit depth before any paper-ready claim.

## verify_faithfulness
The solve record matches the intended statement exactly.

Checks:

- the packet's target is the exact value of `R(B8, B10)`;
- the solve argument assumes a `37`-vertex witness, derives a contradiction, and concludes `R(B8, B10) = 37`;
- the translation between book avoidance and codegree bounds stays on the exact pair `(8, 10)`;
- no wrong-theorem drift, quantifier drift, or proxy replacement was found.

Faithfulness verdict:

- exact match to the selected theorem.

## verify_proof
I did not find an incorrect step.

Line-by-line checks:

- `B8`-avoidance and complement-`B10`-avoidance are correctly translated as edgewise bounds `c_G(u,v) <= 7` on edges and `cn_G(u,v) <= 9` on nonedges.
- The triangle inequalities `3T <= 7e` and `3\\bar T <= 9\\bar e` are valid because each triangle contributes to three edge-codegree counts.
- Combining those with Goodman gives
  `7770 - (1/2) * sum_x d(x)(36 - d(x)) <= 1998 - (1/3) * sum_x d(x)`,
  which rearranges to
  `sum_x (106 d(x) - 3 d(x)^2) >= 34632`.
- The quadratic `f(d) = 106d - 3d^2` has unique integer maximum `936` at `d = 18`, and `37 * 936 = 34632`, so equality forces `d(x) = 18` for every vertex.
- Once regularity is forced, Goodman and the triangle-cap bounds are simultaneously sharp, so every edge has exactly `7` common neighbors and every nonedge has exactly `9` common nonneighbors.
- For a nonedge `uv`, the count of vertices adjacent to neither endpoint is `35 - |N(u) cup N(v)| = c_G(u,v) - 1`, so `cn_G(u,v) = 9` implies `c_G(u,v) = 10`. This yields the strongly regular parameter set `(37,18,7,10)`.
- The adjacency relation
  `A^2 = 18I + 7A + 10(J - I - A) = -3A + 8I + 10J`
  is correct.
- On `1^perp`, the nontrivial eigenvalues satisfy `x^2 + 3x - 8 = 0`, so they are `(-3 +- sqrt(41))/2`. Since the characteristic polynomial has rational coefficients, these irrational conjugates must occur with equal multiplicity. Because `dim(1^perp) = 36`, each would have multiplicity `18`, forcing nontrivial eigenvalue sum `18(r+s) = -54`, which contradicts the trace requirement `-(18)`.

Proof verdict:

- the proof candidate is mathematically coherent as written;
- no hidden case split or missing hypothesis was needed beyond the standard book-graph convention fixed in `statement_lock`.

## verify_adversarial
No local checker existed, so PASS 4 was a direct stress test of the argument.

Adversarial checks performed:

- recomputed the key arithmetic constants: `37 * 936 = 34632` and Goodman at degree `18` gives `T + \\bar T = 1776`;
- checked that the equality case really forces edgewise saturation rather than only average saturation;
- solved the multiplicity equations for the two irrational nontrivial eigenvalues using only `m_r + m_s = 36` and trace `18 + m_r r + m_s s = 0`; this gives nonintegral multiplicities, which is consistent with the claimed impossibility and provides an independent stress check on the spectral contradiction;
- looked for an escape route via a weaker proxy claim or a misread complement count and found none.

Adversarial verdict:

- no surviving obstruction to the proof was found;
- the strongest pressure points remain publication-side novelty confirmation, not mathematical soundness of the current derivation.

## verify_theorem_worthiness
Exactness:

- yes, the claimed result is the exact selected statement `R(B8, B10) = 37`, not a nearby slice.

Novelty:

- bounded verify-stage audit did not find rediscovery;
- exact novelty still needs the usual publication-audit pass before any stronger claim than `SLICE_CANDIDATE`.

Reproducibility:

- high; the argument is short, self-contained, and does not depend on code or opaque computation.

Lean readiness:

- the theorem is strong enough to justify Lean work if publication audit clears;
- however Lean is not yet the shortest remaining path to a sealed packet because the publication-status gate is still open.

Paper leverage:

- strong. If correct and novelty-clean, this already looks like the title theorem of a short note.
- honest estimate: one solve here provides about `0.84` of the paper.
- visible title theorem: `The Exact Value of R(B8, B10)`.

What scales:

- the Goodman saturation reduction from a one-gap witness to a forced strongly regular parameter set.

What does not clearly scale:

- the final nonexistence discharge of the resulting parameter set; that last obstruction is instance-specific at present.

Best honest publication status now:

- not `PAPER_READY` yet;
- best conservative label is `SLICE_CANDIDATE`, because the exact theorem candidate looks real and paper-shaped but still awaits publication-audit clearance.

## verify_verdict
`VERIFIED`

Conservative interpretation:

- the exact-value proof candidate survived bounded rediscovery checking and skeptical mathematical review;
- keep the harness classification at `CANDIDATE` until publication audit and any later Lean sealing are complete.

## minimal_repair_if_any
No mathematical repair was needed.

Status correction only:

- downgrade the prior premature publication-facing label from `PAPER_READY` to `SLICE_CANDIDATE`;
- keep the claim as a verified exact-value candidate rather than an `EXACT` result, because Lean has not completed and publication audit has not yet signed off.

## publication_prior_art_audit
Audit date: `2026-04-13`.

Bounded passes performed:

- exact-statement web search for quoted forms of `R(B8,B10)` and `R(B8, B10)`;
- alternate-notation search for forms such as `R(B_{8}, B_{10})`;
- canonical-source check inside the 2025 Lidicky-McKinley-Pfender-Van Overberghe paper;
- outside-status check in Radziszowski DS1.17, Section `5.3`;
- one recent follow-up check via Wesley's 2026 abstract page.

What the bounded audit found:

- the exact-statement and alternate-notation searches did not surface a post-`2025` theorem, proposition, corollary, observation, example, or preprint explicitly settling `R(B8, B10)`;
- the 2025 canonical source does not directly list an exact value for `R(B8, B10)`, but Theorem `1` states `4n - 3 <= R(B_{n-2}, B_n)` for `4 <= n <= 21`, so for `n = 10` it implies the lower bound `37 <= R(B8, B10)`;
- the same 2025 source visibly records neighboring almost-diagonal activity, including the exact family `R(B_{n-1}, B_n) = 4n - 1`, but no direct theorem slice for the `(8,10)` pair beyond the lower-bound family;
- DS1.17 still records the Rousseau-Sheehan upper-bound mechanism in Section `5.3(g)`, including `R(B_m, B_n) <= 2(m+n+1)` under the stated hypothesis and `R(B_{n-2}, B_n) <= 4n - 3` when `n equiv 2 (mod 3)`; for `(m,n) = (8,10)` this leaves the standard upper bound `R(B8, B10) <= 38`;
- the 2026 Wesley follow-up advertises exact and infinite-family progress for `R(B_{n-1}, B_n)` plus improved bounds for several other pairs, but the bounded abstract-level check did not reveal any claim for `R(B8, B10)`.

Conservative prior-art verdict:

- no rediscovery was found within the bounded publication-audit budget;
- novelty is still only "cleared within budget", not absolutely exhausted;
- the live evidence supports keeping the target as a frontier-looking one-gap residue rather than demoting it to `REDISCOVERY`.

## publication_statement_faithfulness
The solve and verify packet stayed on the exact selected statement.

Checks:

- the selected theorem asks for the exact value of `R(B8, B10)`;
- the proof candidate assumes a `37`-vertex witness and derives a contradiction, yielding `R(B8, B10) = 37`;
- the extracted theorem slice, "any witness would be `srg(37,18,7,10)`", is a faithful internal reduction rather than a substitute target;
- no proxy theorem, weakened statement, or notation drift was introduced during solve or verify.

Faithfulness verdict:

- exact match to the intended statement;
- publication audit does not need to shrink the theorem claim.

## publication_theorem_worthiness
This is stronger than "here is an example."

Why:

- the honest claim is an exact Ramsey value, not a witness construction, isolated example, or one-direction bound;
- there is a real title theorem: `The Exact Value of R(B8, B10)`;
- the proof is structurally meaningful: Goodman saturation forces regularity, then exact codegrees, then a forbidden strongly regular parameter set;
- only the last obstruction is instance-specific; the core argument is not just a hand-picked small-case computation;
- a referee asking "what is the theorem?" would get a clean answer immediately.

Risks that remain:

- the theorem slice is still a single exact pair, so the family-level spillover is limited;
- the endpoint obstruction is specialized to `(37,18,7,10)`, so the proof is structural-first but not broad-family in its final move.

Theorem-worthiness verdict:

- yes, this is a genuine theorem packet;
- it survives the audit as a narrow but legitimate title-theorem slice.

## publication_publishability
If the claim is correct and Lean-sealed, it would already constitute most of a publishable short note.

Answers to the publication questions:

- Would one solve already provide most of the paper? Yes, about `85%`.
- Is there a real theorem slice? Yes: the exact value theorem together with the `srg(37,18,7,10)` obstruction reduction.
- Is the proof structural or merely instance-specific? Structural in its main reduction, instance-specific only at the final nonexistence discharge.
- Is the claim too dependent on hand-picked small cases? No. The scope is small, but the argument is not a pile of ad hoc cases.
- If this is not yet paper-ready, is the remaining gap genuinely small? Yes. The remaining gap is formal sealing plus short-note packaging, not a hidden feeder ladder.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger program? Do not expand it. Keep the one-shot lane and move straight to Lean.
- Would Lean directly seal the packet? Yes. Lean is now the direct trust-sealing step, not optional later polish.

Conservative publishability verdict:

- the candidate did not collapse under audit;
- it remains honestly close to a paper;
- keep the publication status below `PAPER_READY` until the exact theorem is formally sealed.

## publication_packet_audit
Packet quality is `strong`.

What is already present:

- exact intended statement;
- coherent structural proof candidate;
- verified theorem slice and stress-tested arithmetic/spectral steps;
- bounded literature positioning against the 2024 survey, the 2025 canonical paper, and the 2026 follow-up.

What is still missing before a fully sealed packet:

- Lean formalization of the Goodman-to-strongly-regular contradiction;
- final note-level prose packaging;
- one short literature paragraph positioning the result against `R(B_{n-1}, B_n) = 4n - 1` and the 2025 lower-bound family.

Packet verdict:

- this is a real publication packet, not merely a solve log;
- the remaining work is sealing and write-up, not theorem discovery.

## micro_paper_audit
Micro-paper verdict: `PASS`.

Assessment:

- strongest honest claim is a title theorem, not an example;
- family anchor remains strong because the target sits on the almost-diagonal book line;
- editorial overhead is still low;
- immediate corollary headroom is low, which is acceptable in the micro-paper lane because the exact theorem itself carries the note;
- isolated exact-case risk remains moderate, but the narrative is still viable because the one-gap residue is natural and canonically posed;
- the candidate still sits in the intended `70-90%` band, with honest estimate `0.85`.

Bottom line:

- this target still belongs in the strict one-shot micro-paper lane;
- the audit did not reveal a hidden feeder ladder or a weak "example-only" outcome.

## strongest_honest_claim
The strongest honest claim after publication audit is:

- there is a verified, bounded-novelty-clean candidate proof that every graph on `37` vertices contains `B8` or its complement contains `B10`, equivalently `R(B8, B10) = 37`;
- if Lean seals the Goodman-saturation-to-`srg(37,18,7,10)` contradiction, the result is already the title theorem of a short publishable note.

## paper_title_hint
`The Exact Value of R(B8, B10)`

## next_action
Move directly to Lean formalization of the `37`-vertex obstruction argument and the impossible `srg(37,18,7,10)` endpoint.

Do not broaden into a family campaign unless Lean exposes a real gap.
