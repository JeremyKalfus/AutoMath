# Solve Record: The Exact Value of R(B15, B17)

## statement_lock
- Active slug: `r-b15-b17-book-ramsey`.
- Active title: `Determine the exact value of R(B15, B17)`.
- Standard convention used here: `B_t` is the book graph consisting of `t` triangles sharing one common edge.
- Exact intended theorem for this solve pass: `R(B15, B17) = 65`.
- Equivalent contradiction target: there is no graph `G` on `65` vertices such that every edge of `G` has at most `14` common neighbors and every nonedge of `G` has at most `16` common nonneighbors.
- If this closes, the title theorem is exactly: `The Exact Value of R(B15, B17)`.

## definitions
- Let `n = 65`.
- For `v in V(G)`, let `d(v)` be its degree.
- For distinct `u, v`, let `c(u,v) = |N(u) ∩ N(v)|`.
- If `uv` is an edge, then `c(u,v) <= 14` is exactly the condition that edge `uv` is not the spine of a `B15`.
- If `uv` is a nonedge, then the number of common nonneighbors of `u, v` is at most `16`; this is exactly the condition that `uv` is not the spine of a `B17` in the complement.
- Ambiguities to watch:
  - the book notation must be the standard shared-edge convention;
  - the known lower bound `R(B15, B17) >= 65` is taken from the packet as an input to solve and should be citation-checked in verify;
  - the solve argument only needs local common-neighbor counts plus standard triangle identities.

## approach_A
Structural / invariant route: force any `65`-vertex witness to be rigid.

Assume for contradiction that a witness graph `G` on `65` vertices exists with no `B15` and with complement containing no `B17`.

Let:
- `e` be the number of edges of `G`;
- `t` be the number of triangles of `G`;
- `t_bar` be the number of triangles of the complement;
- `Q = sum_v d(v)^2`.

From the local book caps:
- every edge lies in at most `14` triangles, so `t <= 14e/3`;
- every nonedge lies in at most `16` complement-triangles, so `t_bar <= 16(2080 - e)/3`, since `binom(65,2) = 2080`.

Goodman's identity gives

`t + t_bar = binom(65,3) - (1/2) sum_v d(v)(64 - d(v))`.

Using `binom(65,3) = 43680` and `sum_v d(v)(64 - d(v)) = 128e - Q`, this becomes

`t + t_bar = 43680 - 64e + Q/2`.

Combining with the upper bounds,

`43680 - 64e + Q/2 <= (14e + 16(2080 - e))/3 = (33280 - 2e)/3`.

After simplification:

`3Q - 380e + 195520 <= 0`.

Now write `e = 1040 - s`, so `s >= 0` measures the edge deficit from `32`-regularity, and set `x_v = d(v) - 32`. Then

- `sum_v x_v = 2e - 65*32 = -2s`,
- `Q = sum_v (32 + x_v)^2 = 66560 - 128s + sum_v x_v^2`.

Substituting into the inequality yields

`3 sum_v x_v^2 <= 4s`.

But the `x_v` are integers summing to `-2s`. For fixed sum `-2s`, the smallest possible square-sum is `2s`, achieved only by taking `2s` entries equal to `-1` and the rest `0`. Hence

`sum_v x_v^2 >= 2s`.

Therefore

`6s <= 3 sum_v x_v^2 <= 4s`,

which forces `s = 0`. Then `sum_v x_v^2 = 0`, so every `x_v = 0`.

Conclusion of Approach A: any `65`-vertex witness must be exactly `32`-regular.

## approach_B
Construction / extremal contradiction route: once regularity is forced, show the witness would have to be a nonexistent strongly regular graph.

Assume the `32`-regular witness from Approach A exists.

First convert the complement cap into a common-neighbor cap for nonedges. If `uv` is a nonedge, then

- `|N(u) ∪ N(v)| = 32 + 32 - c(u,v) = 64 - c(u,v)`;
- among the other `63` vertices, the number of common nonneighbors is `63 - (64 - c(u,v)) = c(u,v) - 1`.

Since the complement contains no `B17`, we get `c(u,v) - 1 <= 16`, hence

`c(u,v) <= 17` for every nonedge `uv`.

Now fix a vertex `u`. Count common-neighbor incidences `c(u,v)` over all `v != u`:

`sum_{v != u} c(u,v) = sum_{w in N(u)} (d(w) - 1) = 32 * 31 = 992`.

But `u` has exactly `32` neighbors and `32` nonneighbors, with

- `c(u,v) <= 14` on each edge `uv`,
- `c(u,v) <= 17` on each nonedge `uv`.

So

`sum_{v != u} c(u,v) <= 32*14 + 32*17 = 992`.

The upper bound matches the exact value, so equality holds term-by-term:

- every edge has exactly `14` common neighbors;
- every nonedge has exactly `17` common neighbors.

Thus any witness would be a strongly regular graph with parameters

`(v, k, lambda, mu) = (65, 32, 14, 17)`.

Let `A` be its adjacency matrix. Then

`A^2 = 32I + 14A + 17(J - I - A) = 15I - 3A + 17J`.

On the subspace orthogonal to the all-ones vector, `J` vanishes, so any nontrivial eigenvalue `theta` of `A` must satisfy

`theta^2 + 3 theta - 15 = 0`.

Hence the two nontrivial eigenvalues are

`r = (-3 + sqrt(69))/2`, `s = (-3 - sqrt(69))/2`.

Let their multiplicities be `f` and `g`. Since `A` is `65 x 65`,

- `f + g = 64`,
- `32 + fr + gs = trace(A) = 0`.

Solving gives

- `f = 32 + 64 / sqrt(69)`,
- `g = 32 - 64 / sqrt(69)`.

These are not integers, contradiction.

Conclusion of Approach B: the forced witness graph cannot exist.

## lemma_graph
1. A `65`-vertex witness would satisfy edge cap `c(u,v) <= 14` and complement-edge cap `common_nonneighbors(u,v) <= 16`.
2. Goodman plus these caps forces the witness to be `32`-regular.
3. In a `32`-regular witness, every nonedge also satisfies `c(u,v) <= 17`.
4. The per-vertex common-neighbor sum is exactly saturated, forcing `lambda = 14` and `mu = 17`.
5. Therefore the witness would be an `srg(65,32,14,17)`.
6. The spectral multiplicities of such an SRG are nonintegral, so the graph cannot exist.
7. Since the packet already supplies `R(B15, B17) >= 65`, the exact value is `65`.

## chosen_plan
The best path is the contradiction route:
- lock the witness conditions in common-neighbor language;
- use the invariant route to remove all degree slack;
- turn that rigidity into an impossible strongly regular parameter set.

This is better than a construction-first search because the problem is flagged `search_heavy = False`, the window is only one gap wide, and the local caps are balanced enough that a counting argument can plausibly force a unique extremal shape.

## self_checks
- Statement-lock check: the translation from `B15` / complement `B17` to common-neighbor caps is standard for book graphs.
- Goodman-step check: the algebra reduces to `3 sum_v x_v^2 <= 4s`; no sign reversal appears in the simplification.
- Degree-rigidity check: `sum_v x_v^2 >= 2s` uses only integrality and the fixed sum `sum_v x_v = -2s`.
- Nonedge conversion check: in a `32`-regular graph on `65` vertices, common nonneighbors for a nonedge are exactly `c(u,v) - 1`.
- Saturation check: the global value `992` equals the vertexwise cap `32*14 + 32*17`, so every term must attain its cap.
- Spectral check: the contradiction is not that the eigenvalues are irrational; it is that their multiplicities are nonintegral.
- Scope check: the solve result is theorem-shaped, but verify still needs to confirm the cited lower bound and the absence of a prior exact determination.

## code_used
- None.
- No checker or search was needed because the reasoning path closed before any bounded experiment became necessary.

## result
Provisional main theorem for the solve stage:

`R(B15, B17) = 65`.

Reasoning summary:
- Assume a `65`-vertex witness exists.
- Goodman plus the edge/nonedge book caps force the graph to be `32`-regular.
- That regularity makes the witness saturate every local common-neighbor bound, so it must be an `srg(65,32,14,17)`.
- The adjacency matrix of such a graph would have nontrivial eigenvalues `(-3 +/- sqrt(69))/2` with multiplicities `32 +/- 64/sqrt(69)`, impossible.
- Therefore no `65`-vertex witness exists.
- Combining this with the packet's lower bound `65 <= R(B15, B17)` gives the exact value `R(B15, B17) = 65`.

What scales:
- the `Goodman -> regularity -> exact local parameters -> spectral obstruction` pipeline;
- the extremal principle that a one-gap witness, if it exists, may be forced into a rigid pseudorandom template.

What does not obviously scale:
- the exact saturation `32*14 + 32*17 = 32*31`;
- the odd-order symmetry `65 = 2*32 + 1`;
- the final contradiction depends on the resulting SRG parameters being spectrally impossible.

Current package assessment:
- this is no longer just an instance witness or a thin slice;
- if verify confirms the lower-bound citation and novelty status, the argument is already close to a paper-shaped exact theorem note.

## family_affinity
This result sits naturally on the almost-diagonal book Ramsey strip `B_{n-2}` versus `B_n`. The proof does not look like an isolated ad hoc witness kill; it uses the same family language as the packet and extracts a structural obstruction that is meaningful in the surrounding line.

## generalization_signal
The reusable signal is narrow but real: if another unresolved one-gap book pair produces an odd-order witness candidate whose Goodman bound is exactly tight, then the same route may force a regular graph and possibly a strongly regular obstruction. What likely will not generalize is the perfect cap saturation; once Goodman leaves slack, the argument loses its rigidity quickly.

## proof_template_reuse
Reusable template:
- translate book avoidance into edgewise common-neighbor caps;
- combine both colors with Goodman to force near-regularity;
- upgrade near-regularity to exact regularity using integrality;
- convert the witness into a candidate SRG;
- kill the SRG with spectral multiplicity arithmetic.

This template is worth reusing only for one-gap, low-search, almost-diagonal pairs where the target order is already numerically pinned.

## candidate_theorem_slice
Independent theorem slice suggested by the solve:

`There is no graph on 65 vertices in which every edge has at most 14 common neighbors and every nonedge has at most 16 common nonneighbors. Equivalently, there is no strongly regular graph with parameters (65,32,14,17).`

This is the smallest structural slice extracted by the proof and is the main nontrivial supporting theorem behind the Ramsey exact value.

## smallest_param_shift_to_test
The most informative next shifts are:
- `R(B14, B17)`, if the literature leaves a similarly narrow one-gap window;
- `R(B15, B18)`, under the same condition.

Reason: these are the nearest asymmetric perturbations of the present pair, so they are the first places to test whether the `Goodman -> SRG obstruction` template survives even a one-step change in parameters.

## why_this_is_or_is_not_publishable
If the argument survives verify, this is already about `80-90%` of a micro-paper.

- Exact title theorem: `R(B15, B17) = 65`.
- Why paper-shaped: it closes a named frontier one-gap case in a current family, with a short self-contained proof and a clean obstruction theorem underneath it.
- Minimal remaining packaging work:
  - verify the lower-bound citation and exact-status frontier claim;
  - write the contradiction proof in polished theorem/lemma form;
  - add one short comparison paragraph with the adjacent solved case `R(B16, B17) = 67`;
  - optionally formalize the counting identities in Lean.

This is not too thin for the micro-paper lane. If correct, it reads like the title theorem of the paper rather than like a supporting curiosity.

## paper_shape_support
The main claim already comes with the minimum extra structure a short paper needs:
- a structural lemma forcing `32`-regularity;
- an obstruction lemma forcing the nonexistent parameter set `(65,32,14,17)`;
- a natural boundary remark explaining why the method is specific to the one-gap balanced case.

Immediate corollary / remark:
- the packet's lower bound `65 <= R(B15, B17)` is sharp, because any `65`-vertex witness would have to be an impossible `srg(65,32,14,17)`.

## boundary_remark
The proof is powered by exact balance, not by a wide flexible theory. Its strongest boundary is that the argument uses both the odd target order and a perfect saturation identity; if either changes, the witness need not collapse to an impossible SRG. So the result is strongly paper-shaped for this pair, but the method should be advertised as a narrow frontier obstruction rather than as a broad general theorem.

## likely_failure_points
- Verify that the packet's lower bound `R(B15, B17) >= 65` is exactly correct and not an indexing mismatch.
- Check that `B_t` is indeed the shared-edge book graph in every cited source.
- Recheck the Goodman algebra and the substitution `e = 1040 - s`.
- Recheck the multiplicity calculation from `f + g = 64` and `32 + fr + gs = 0`.
- Confirm that no hidden assumption stronger than the witness conditions was introduced during the nonedge-to-`mu` conversion.

## what_verify_should_check
- Confirm the literature gap still ends at `65 <= R(B15, B17) <= 66`.
- Confirm the lower bound `65 <= R(B15, B17)` from the 2025 source applies exactly to this pair.
- Check the proof line-by-line, especially the Goodman identity and the multiplicity contradiction.
- Check whether the nonexistence of `srg(65,32,14,17)` is already explicitly known in the literature; if so, cite it rather than presenting that part as folklore.
- Check whether the same obstruction argument already appears implicitly in a source on nearby book Ramsey numbers.

## verify_rediscovery
- PASS 1 established rediscovery.
- In Lidicky-McKinley-Pfender-Van Overberghe 2025, Theorem 1 states `4n - 3 <= R(B_{n-2}, B_n)` for all `4 <= n <= 21`.
- The note immediately below Theorem 1 states that it was already known that `R(B_{n-2}, B_n) <= 4n - 3` when `n ≡ 2 (mod 3)`.
- Substituting `n = 17` gives both `65 <= R(B15, B17)` and `R(B15, B17) <= 65`, hence the exact value `R(B15, B17) = 65` is already implied in the 2025 source.
- The packet frontier claim `65 <= R(B15, B17) <= 66` is therefore stale. DS1.17's older upper bound `66` was superseded for this pair by the 2025 family result plus its cited known upper-bound regime.
- Bounded additional checks did not surface a later different exact value; the issue is not contradiction but prior settlement.

## verify_faithfulness
- The local solve targets the intended theorem exactly: it proves nonexistence of a `65`-vertex witness and therefore aims at `R(B15, B17) = 65`.
- The main faithfulness failure is upstream packet drift, not theorem drift: the selection packet treated the pair as still open, but the 2025 source already settles the exact value.
- There is also citation drift in the packet narrative. The 2025 source does support the lower bound `65 <= R(B15, B17)`, but the packet's claimed surviving upper bound `66` is not the best available bound for this pair.
- Verdict on faithfulness: theorem target matches, frontier-status framing does not.

## verify_proof
- Bounded proof audit found no fatal mathematical error in the local contradiction argument.
- The Goodman identity, the reduction to `32`-regularity, the conversion of the nonedge cap to `c(u,v) <= 17`, the saturation count `32*14 + 32*17 = 32*31 = 992`, and the spectral multiplicity obstruction all check out.
- The first repairable overstatement is in Approach A: the sentence claiming the minimum of `sum_v x_v^2` for fixed integer sum `-2s` is achieved only by `2s` copies of `-1` and the rest `0` is stronger than needed and is not justified for large `s`.
- The argument only needs the weaker bound `sum_v x_v^2 >= sum_v |x_v| >= |sum_v x_v| = 2s`, which still yields `6s <= 4s` and forces `s = 0`.
- So the proof appears internally correct after this tiny conservative repair, but that does not rescue novelty.

## verify_adversarial
- No dedicated code or checker existed to rerun.
- Arithmetic spot-checks were rerun locally:
  - `binom(65, 3) = 43680` and `binom(65, 2) = 2080`;
  - the combined cap identity is exact: `32*14 + 32*17 = 32*31 = 992`;
  - the nontrivial SRG eigenvalue multiplicities are approximately `39.7046945975` and `24.2953054025`, so they are nonintegral.
- No computational counterexample to the local proof skeleton emerged in this bounded pass.
- The adversarial failure remains the literature one: the solve is an independent rederivation of an already settled exact value.

## verify_theorem_worthiness
- Exactness: yes, the local argument is aimed at the exact theorem `R(B15, B17) = 65`.
- Novelty: no. The exact value is already implied by the 2025 source, so this run is a rediscovery.
- Reproducibility: high for the local argument, which is short and mostly counting-based.
- Lean readiness: no for harness purposes, because formalizing an already known exact value would not be the shortest route to a frontier publication packet.
- Paper leverage: collapsed by rediscovery. Even a clean independent proof does not satisfy the micro-paper novelty requirement here.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No as a frontier note, because the title theorem is already known.
- What percentage of the paper would one solve already provide? As a frontier micro-paper, effectively `0%`; the novelty gap is fatal.
- What title theorem is actually visible? `R(B15, B17) = 65`, but it is already available from prior art.
- What part of the argument scales? The local `Goodman -> regularity -> SRG obstruction` template may still be useful as an independent method on other one-gap book pairs.
- What part clearly does not? The publication claim for this exact pair; novelty does not scale because the pair is already closed.
- Best honest publication status: `REDISCOVERY`, not `INSTANCE_ONLY` and not a frontier slice candidate.

## verify_verdict
- `REDISCOVERY`.
- Reason: the exact intended statement `R(B15, B17) = 65` is already implied by Lidicky-McKinley-Pfender-Van Overberghe 2025 via Theorem 1 plus the known upper-bound regime quoted immediately below it.

## minimal_repair_if_any
- Minimal proof repair, if the local derivation is retained for archival value: replace the square-sum minimizer sentence in Approach A with the direct bound `sum_v x_v^2 >= sum_v |x_v| >= |sum_v x_v| = 2s`.
- No repair can restore frontier status for this candidate; the correct harness action is archival as rediscovery.
