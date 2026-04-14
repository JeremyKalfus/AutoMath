# Solve Record: The Exact Value of R(B14, B14)

## statement_lock
Work with a graph `G` on `57` vertices. Let `B14` denote the book graph consisting of `14` triangles sharing a common edge.

The known public interval is

- `57 <= R(B14, B14) <= 58`.

So the exact binary task in solve is:

1. prove that every `57`-vertex graph `G` contains `B14` or its complement contains `B14`, which would show `R(B14, B14) = 57`;
2. or construct a `57`-vertex graph `G` with no `B14` and with complement containing no `B14`, which would show `R(B14, B14) = 58`.

There is one packet ambiguity worth locking explicitly: the working packet says one acceptable artifact is a proof that every `58`-vertex coloring forces `B14`. That is already known from the cited upper bound and does not decide `57` versus `58`. For this solve run, the binding exact statement is the `57`-vertex forcing-or-obstruction question above.

If the main claim closes, the exact title theorem would be `The Exact Value of R(B14, B14)`. A successful solve would still be about `70-90%` of a paper; the packet estimate `0.79` remains credible. The minimal remaining packaging work would be a short literature comparison, a compact statement of the rigidity lemma below, and either the final nonexistence argument or the final explicit `57`-vertex witness.

## definitions
For vertices `u,v` in `G`:

- `N(v)` is the open neighborhood of `v`;
- `d(v) = |N(v)|`;
- `c(u,v) = |N(u) ∩ N(v)|`;
- `t(G)` is the triangle count of `G`.

Conventions used below:

- `G` is `B14`-free iff every edge `uv` satisfies `c(u,v) <= 13`;
- `\bar G` is `B14`-free iff every nonedge `uv` of `G` has at most `13` common nonneighbors;
- for a nonedge `uv`, the number of common nonneighbors in `G` is
  `55 - d(u) - d(v) + c(u,v)`.

Ambiguities or missing definitions to keep in view:

- the cited lower-bound witness on `56` vertices is not locally present, so this run cannot do the recommended one-vertex-extension analysis;
- the exact notation from the cited papers is not locally present, so I am using the standard convention `B_t = K_2 + \overline{K_t}`;
- solve is web-disabled here, so any recollection about conference-graph existence must not be treated as verified fact.

## approach_A
Structural / invariant route.

Assume there is a `57`-vertex obstruction `G` with no `B14` and with `\bar G` also `B14`-free.

First count monochromatic triangles from above.

In the two-coloring viewpoint:

- every red edge lies in at most `13` red triangles;
- every blue edge lies in at most `13` blue triangles.

Therefore

- `3(t(G) + t(\bar G)) <= 13 * binom(57, 2) = 13 * 1596 = 20748`,
- so `t(G) + t(\bar G) <= 6916`.

Now use Goodman's identity:

- `t(G) + t(\bar G) = binom(57, 3) - (1/2) * sum_v d(v)(56 - d(v))`.

Since `d(56-d)` is maximized at `d = 28`, we have

- `d(v)(56-d(v)) <= 28^2 = 784` for every vertex `v`,
- hence `sum_v d(v)(56-d(v)) <= 57 * 784 = 44688`.

So

- `t(G) + t(\bar G) >= 29260 - 44688/2 = 6916`.

Combining the upper and lower bounds gives exact equality:

- `t(G) + t(\bar G) = 6916`.

This forces equality in every intermediate step. Hence:

1. every vertex has degree exactly `28`;
2. every red edge lies in exactly `13` red triangles;
3. every blue edge lies in exactly `13` blue triangles.

Translated back to `G`, that means:

- every edge `uv` of `G` has `c(u,v) = 13`;
- every nonedge `uv` of `G` has exactly `13` common nonneighbors.

For a nonedge `uv`, since `d(u)=d(v)=28`,

- `13 = 55 - 28 - 28 + c(u,v) = c(u,v) - 1`,
- so `c(u,v) = 14`.

Therefore any `57`-vertex obstruction must be a strongly regular graph with parameters

- `(v,k,lambda,mu) = (57,28,13,14)`.

Equivalently, the entire exact-value problem collapses to one rigid existence question:

- `R(B14, B14) = 58` iff a strongly regular graph `srg(57,28,13,14)` exists;
- otherwise `R(B14, B14) = 57`.

Self-check after Approach A:

- the triangle upper bound is exact and uses only the `B14` cap on monochromatic books;
- the Goodman lower bound is exact and the arithmetic checks;
- the deduction to `28`-regularity and exact pair-intersection numbers is rigorous;
- this is a real theorem slice, not heuristic evidence.

## approach_B
Construction / extremal / contradiction route.

If the answer is `58`, a witness on `57` vertices cannot be an arbitrary critical coloring. Approach A shows it must realize the conference-type parameter set `(57,28,13,14)`.

Write `A` for the adjacency matrix of such a hypothetical graph and define the Seidel matrix

- `S = J - I - 2A`.

For the parameter set `(57,28,13,14)`, the strongly regular identity gives

- `A^2 = 14J + 14I - A`,

and then a direct expansion yields

- `S^2 = 57I - J`.

So on the orthogonal complement of the all-ones vector, `S` has eigenvalues `+-sqrt(57)`. This means the obstruction problem is no longer a generic graph-search problem; it is the existence problem for a very rigid conference-graph-like object.

That immediately sharpens both possible endgames:

1. To prove `R(B14, B14) = 57`, it is enough to rule out `srg(57,28,13,14)`.
2. To prove `R(B14, B14) = 58`, it is enough to exhibit one graph with those exact parameters.

This also explains why a naive perturbation of the published `56`-vertex lower-bound construction is unlikely to be decisive unless it lands exactly on the forced regular/intersection pattern.

Self-check after Approach B:

- the matrix identity is a clean rephrasing of the rigidity forced in Approach A;
- the spectral statement is exact once the strongly regular reduction is accepted;
- this still does not decide existence versus nonexistence of the required parameter set.

## lemma_graph
Proof skeleton for the strongest theorem slice now available.

1. Assume `G` is a `57`-vertex graph with neither `G` nor `\bar G` containing `B14`.
2. Count monochromatic triangles from above to get `t(G) + t(\bar G) <= 6916`.
3. Apply Goodman's identity and the vertexwise bound `d(56-d) <= 784` to get `t(G) + t(\bar G) >= 6916`.
4. Conclude equality holds, so every vertex has degree `28`.
5. Conclude every edge lies in exactly `13` monochromatic triangles in its own color.
6. Translate the blue-edge equality into the nonedge condition `c(u,v) = 14`.
7. Deduce that any obstruction is `srg(57,28,13,14)`.
8. Therefore the exact value problem is equivalent to the existence or nonexistence of that single strongly regular graph.

Smallest immediate supporting corollary:

- any proof of `R(B14, B14) = 57` may focus entirely on excluding `srg(57,28,13,14)`, rather than on arbitrary `57`-vertex colorings.

## chosen_plan
The best current path is to bank the rigidity theorem slice above and stop there honestly.

Reasons:

- the structural route already compressed the full coloring space to one precise extremal object;
- the remaining step is an existence/nonexistence problem for `srg(57,28,13,14)`, not a broad generic obstruction problem;
- the local repo packet does not contain the cited witness, conference-graph existence notes, or a candidate matrix to verify;
- minimal code is not justified yet because the remaining task is algebraic and classification-like, not an open-ended graph search under the current solve policy.

If this run were continued later, the next mathematically coherent step would be one of:

1. find a local, self-contained nonexistence argument for `srg(57,28,13,14)`;
2. or import and verify an explicit `57`-vertex candidate with those exact parameters.

## self_checks
- Statement lock is exact: the live decision point is on `57` vertices, not `58`.
- The Goodman pinch is arithmetic-tight and leaves no slack.
- I did not use any unverified external theorem about conference-graph nonexistence.
- The current result is stronger than a heuristic and weaker than an exact solve.
- No code was used because the remaining unresolved step is not yet a justified search problem.

## code_used
No.

Reason:

- the structural reduction already turns the problem into a single strongly regular graph existence question;
- without a local candidate matrix or a narrow exact verification target, generic search would violate the solve-stage preference for reasoning first and minimal code only when justified.

## result
Strongest honest result of this solve run:

`Proposition.` If a graph `G` on `57` vertices has neither `G` nor `\bar G` containing `B14`, then `G` is a strongly regular graph with parameters `(57,28,13,14)`. Consequently,

- `R(B14, B14) = 58` iff `srg(57,28,13,14)` exists;
- `R(B14, B14) = 57` iff `srg(57,28,13,14)` does not exist.

This is a real theorem-facing reduction and already identifies the only possible `57`-vertex extremal shape.

What part of the argument scales:

- the Goodman pinch uses only the diagonal condition `n = 4m + 1` together with the `B_m` cap of `m-1` monochromatic triangles on each monochromatic edge;
- the same template should reduce any diagonal `R(B_m, B_m)` lower-endpoint obstruction on `4m+1` vertices to the conference parameters
  `(4m+1, 2m, m-1, m)`.

What does not scale automatically:

- the final existence/nonexistence question for the corresponding conference graph is family-specific;
- the reduction alone does not produce either a witness or a contradiction.

What theorem slice is suggested:

- the obstruction at the lower endpoint `4m+1` is necessarily conference-graph rigid;
- in the present instance, the exact problem is equivalent to the existence of `srg(57,28,13,14)`.

The one or two next parameter shifts that would help most are:

- `R(B13, B13)`, where the same argument should reduce a `53`-vertex obstruction to `srg(53,26,12,13)`;
- `R(B15, B15)`, where the same argument should reduce a `61`-vertex obstruction to `srg(61,30,14,15)`.

Whether the current package is still just an instance or already closer to a paper-shaped claim:

- it is still not an exact-value paper;
- but it is closer than a bare instance, because it gives a clean family-facing rigidity lemma and replaces the full solve space by one explicit extremal parameter set.

## family_affinity
High.

This attempt is well aligned with the diagonal book-Ramsey family because the core move is not ad hoc to `14`; it is the tight Goodman-versus-book-count pinch at the lower endpoint `4m+1`. That is exactly the kind of family anchor that can support a short micro-paper once the final existence question is settled.

## generalization_signal
High.

The main reduction should extend verbatim to diagonal book targets at the lower endpoint:

- if a graph on `4m+1` vertices avoids `B_m` in both colors, then equality in the Goodman pinch should force the conference parameters `(4m+1, 2m, m-1, m)`.

That is stronger than a one-off counting trick and suggests a reusable exact-value template on the diagonal line.

## proof_template_reuse
Strong.

Reusable template:

1. upper-bound `t(G) + t(\bar G)` by summing the book cap over monochromatic edges;
2. lower-bound the same quantity by Goodman's identity and convexity of `d(n-1-d)`;
3. exploit equality to force regularity and exact pair intersection numbers;
4. translate the surviving obstruction into one conference-graph existence question.

This template should be reusable on other one-gap diagonal book residues with lower endpoint `4m+1`.

## candidate_theorem_slice
Candidate theorem slice:

`Any 57-vertex graph with no B14 and with complement containing no B14 must be a strongly regular graph with parameters (57,28,13,14). Equivalently, the exact determination of R(B14, B14) is identical to the existence problem for srg(57,28,13,14).`

This is the smallest rigorous slice from the current run that is both exact and clearly theorem-shaped.

## smallest_param_shift_to_test
The smallest useful nearby test is `R(B13, B13)`.

Reason:

- it sits on the same diagonal one-gap corridor;
- the same proof should force the lower-endpoint obstruction on `53` vertices to be `srg(53,26,12,13)`;
- checking that neighboring case would test whether the conference-graph reduction is the right family-level narrative rather than a one-off coincidence at `14`.

## why_this_is_or_is_not_publishable
As it stands, this is not yet publishable as a micro-paper.

Why it is not enough yet:

- the exact value `57` versus `58` is still unresolved;
- there is no explicit `57`-vertex witness and no self-contained nonexistence proof for `srg(57,28,13,14)`;
- the current result is a sharp reduction lemma, not the title theorem.

Why it still matters:

- it is a genuine theorem slice with immediate paper-shape relevance;
- it drastically shortens the solve-to-publication distance by replacing an arbitrary coloring problem with one rigid extremal object;
- if the final existence question closes, the current reduction would naturally become one of the core lemmas in the paper.

So the current package is `SLICE_CANDIDATE`, not `PAPER_READY`. It is still too thin for the micro-paper lane unless the conference-graph existence question is settled.

## paper_shape_support
If the main claim closes, the smallest supporting structure already visible is:

1. the rigidity proposition reducing the `57`-vertex obstruction to `srg(57,28,13,14)`;
2. one spectral or matrix reformulation via `S^2 = 57I - J`;
3. one boundary remark explaining that the lower endpoint `57 = 4*14 + 1` is exactly the conference threshold for the diagonal book line.

That would be enough supporting structure for a short note because the title theorem would already be the exact value, and the present reduction supplies the natural proof scaffolding around it.

Immediate corollary / remark that naturally falls out:

- any eventual `57`-vertex witness must be `28`-regular and self-complementary at the parameter level; there is no room for an irregular or locally patched obstruction.

## boundary_remark
Boundary remark:

The endpoint `57` is not merely one less than the known upper bound `58`; it is the exact size at which the monochromatic-triangle cap from `B14` meets the Goodman lower bound with no slack. That is why any extremal `57`-vertex coloring, if it exists at all, must sit on the conference-graph boundary rather than in a broad critical family.

## likely_failure_points
- The reduction may already be implicit in the cited literature; verify should check novelty before overvaluing it.
- The unresolved existence question for `srg(57,28,13,14)` could have a standard answer already known in conference-graph/design literature.
- The packet's off-by-one artifact phrasing (`58`-vertex forcing rather than `57`-vertex forcing) should be corrected or at least flagged upstream.
- If a later step imports a candidate `57`-vertex graph, the parameter check must be exact; near-regularity is irrelevant here because the reduction leaves zero slack.

## what_verify_should_check
- Verify the arithmetic in the Goodman identity application and the equality case at `n = 57`.
- Verify that the reduction to `srg(57,28,13,14)` is logically complete.
- Check whether the same reduction or the conference-graph equivalence already appears explicitly in the 2025 or 2026 cited sources.
- Check whether the existence or nonexistence of `srg(57,28,13,14)` is already standard in the literature.
- Check the packet wording about the `58`-vertex forcing artifact, since the exact solve target here is the `57`-vertex case.
