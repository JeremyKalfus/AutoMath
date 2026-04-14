## statement_lock

Let `B9` denote the book graph with 9 pages, i.e. 9 triangles sharing one common edge.

Target title theorem:

`R(B9, B9) = 38.`

Equivalent locked statement:

Every red-blue coloring of `K38` contains a monochromatic `B9`, and there exists a red-blue coloring of `K37` with no monochromatic `B9`.

If this closes, it is already about `80-90%` of a micro-paper. The honest title theorem is exactly `The Exact Value of R(B9, B9)`.

## definitions

Work with the red graph `G` on the vertex set of the colored complete graph; blue is `\bar G`.

- A red `B9` occurs iff some red edge `uv` has at least 9 common red neighbors.
- A blue `B9` occurs iff some blue edge `uv` has at least 9 common blue neighbors.
- Let `t(G)` be the number of red triangles and `e(G)` the number of red edges.

Thus a coloring is monochromatic-`B9`-free iff

- every edge of `G` lies in at most 8 red triangles, and
- every edge of `\bar G` lies in at most 8 blue triangles.

Ambiguities / conventions checked:

- I am using the standard book convention: `Bk` has `k` pages, so the common-edge codegree threshold is `k`.
- `R(B9,B9)` is diagonal and means the least forcing order.
- Solve uses no web and no prior-art claims beyond the selected packet.

## approach_A

Structural / invariant approach: combine local same-color codegree caps with Goodman's identity.

If a coloring of `Kn` is monochromatic-`B9`-free, then

`3 t(G) <= 8 e(G)` and `3 t(\bar G) <= 8 e(\bar G)`.

Hence

`t(G) + t(\bar G) <= (8/3) * binom(n,2)`.

On the other hand Goodman gives

`t(G) + t(\bar G) = binom(n,3) - (1/2) sum_v d(v)(n-1-d(v))`.

Since `d(v)(n-1-d(v))` is maximized at balanced degree, this yields:

- for `n = 38`, `t(G) + t(\bar G) >= 8436 - (1/2) * 38 * 18 * 19 = 1938`,
- but the book-free upper bound gives `t(G) + t(\bar G) <= (8/3) * 703 < 1875`,

which is impossible. Therefore every coloring of `K38` contains a monochromatic `B9`, so

`R(B9,B9) <= 38`.

For `n = 37`, the same argument gives

- `t(G) + t(\bar G) <= (8/3) * 666 = 1776`,
- `t(G) + t(\bar G) >= 7770 - (1/2) * 37 * 18^2 = 1776`.

So equality must hold throughout.

That equality forces:

- every vertex degree is exactly `18`,
- every red edge has exactly `8` red common neighbors,
- every blue edge has exactly `8` blue common neighbors.

In particular, for a nonedge `uv` of `G`,

`8 = 35 - (18 + 18 - |N(u) cap N(v)|)`,

so `|N(u) cap N(v)| = 9`.

Therefore any monochromatic-`B9`-free coloring of `K37` has red graph strongly regular with parameters

`(37, 18, 8, 9)`.

Self-check after Approach A:

- The `n=38` contradiction is strict, so the upper bound is complete.
- The `n=37` case is exactly tight, so the rigidity conclusion is load-bearing and not cosmetic.

## approach_B

Construction / extremal approach: realize the forced `srg(37,18,8,9)` structure explicitly via the Paley graph on `F37`.

Color `{x,y}` red iff `x-y` is a nonzero quadratic residue mod `37`; color it blue otherwise.

Checks:

- Since `37 ≡ 1 (mod 4)`, `-1` is a quadratic residue, so the coloring is undirected.
- Each vertex has red degree `18`.
- The complement is obtained by multiplying differences by any fixed nonresidue, so blue is isomorphic to red.

For a red edge one may translate and scale to the pair `{0,1}`. The number of common red neighbors is

`#{u in F37 : chi(u) = chi(u-1) = 1}`,

where `chi` is the quadratic character. Using

`sum_u chi(u) = 0` and `sum_u chi(u(u-1)) = -1`,

the indicator sum gives `(37-1)/4 = 9` before correcting the endpoints `u=0,1`, each contributing `1/2`; therefore the true count is `8`.

Because blue is isomorphic to red, every blue edge also has exactly `8` blue common neighbors.

So this Paley coloring of `K37` contains no monochromatic `B9`, and hence

`R(B9,B9) >= 38`.

Self-check after Approach B:

- The construction matches the exact rigidity parameters from Approach A.
- The complement symmetry removes the need for a separate blue-side count beyond the isomorphism.

## lemma_graph

1. `B9`-free implies every same-color edge has same-color codegree at most `8`.
2. Edge-triangle incidence then gives `3t <= 8e` in each color.
3. Goodman gives a global lower bound on `t + \bar t`.
4. For `n=38`, the two bounds conflict, proving the upper bound `R(B9,B9) <= 38`.
5. For `n=37`, the two bounds are equal, forcing degree balance and exact edge codegrees.
6. Thus any critical `K37` witness must be `srg(37,18,8,9)`.
7. The Paley graph `P(37)` realizes that parameter set and yields a `K37` witness.
8. Therefore `R(B9,B9) = 38`.

## chosen_plan

Use Approach A to force the global theorem shape and to show what any `K37` witness must look like. Then use Approach B to supply the explicit witness. This is better than a blind search because it gives both the exact value and the structural extremal slice that makes the result paper-shaped.

## self_checks

- Upper-bound check: the `n=38` contradiction is purely arithmetic and does not depend on hidden classification assumptions.
- Equality-case check: the `n=37` argument really needs equality in both the Goodman bound and the local edge-triangle bounds; that is why regularity and exact codegrees follow.
- Witness check: the Paley construction is standard, but I also verified computationally that in the `q=37` coloring every red edge has exactly `8` red common neighbors and every blue edge has exactly `8` blue common neighbors.
- Scope check: this is an exact solve candidate, not a feeder ladder. The natural supporting slice is the rigidity of any `K37` extremal witness.

## code_used

Minimal code used only for witness verification, not discovery.

An in-memory Python check confirmed:

- every vertex of the Paley `37` graph has degree `18`,
- every red edge has exactly `8` red common neighbors,
- every blue edge has exactly `8` blue common neighbors.

No durable code file was created.

## result

Best current solve claim:

`R(B9,B9) = 38`.

Proof package:

- `K38` forcing bound from Goodman plus local book-free triangle-incidence bounds.
- `K37` witness from the Paley coloring on `F37`.

This is not merely an instance-level witness. The argument also extracts the structural criticality statement that any `K37` extremal witness must be strongly regular with parameters `(37,18,8,9)`.

Immediate corollary / boundary remark:

Any monochromatic-`B9`-free coloring of `K37` lies on the exact Goodman boundary and therefore each color class is `18`-regular with every same-color edge contained in exactly `8` monochromatic triangles.

What scales:

- the Goodman-plus-local-codegree upper-bound template,
- the equality-case rigidity mechanism when the global counts meet exactly,
- Paley-type lower bounds when a prime power `q = 4m+1` matches the book threshold.

What does not automatically scale:

- the explicit lower-bound witness depends on a Paley field order with the right page parameter,
- the exact equality case at `n=37` is numerically special and will not occur for every neighboring diagonal book case.

This package is already closer to a paper-shaped claim than to a bare instance.

## family_affinity

Strong. This sits exactly in the diagonal book Ramsey family, closes a one-step recent interval, and comes with a natural extremal-structure statement rather than a raw ad hoc certificate.

## generalization_signal

Moderate. The proof suggests a reusable lane:

- use local monochromatic codegree caps for `Bm`,
- combine with Goodman,
- inspect whether the forcing bound is strict or equality-tight,
- in equality-tight cases look for strongly regular / Paley-type critical witnesses.

The next obvious parameter shift is `B10`, where the same Paley template at `q=41` gives a natural lower-bound candidate.

## proof_template_reuse

Reusable template:

1. convert monochromatic-book avoidance into same-color codegree caps;
2. sum triangle incidences in each color;
3. compare against Goodman;
4. when equality occurs, derive exact regularity and pairwise-intersection parameters;
5. try to realize those parameters by a known symmetric graph family.

This template should transfer best to diagonal `Bm` cases with `n` near `4m+1` and with balanced extremal density.

## candidate_theorem_slice

Candidate supporting theorem slice:

Any red-blue coloring of `K37` with no monochromatic `B9` has each color class `18`-regular; equivalently the red graph is strongly regular with parameters `(37,18,8,9)`.

That slice is immediate from the solve and is strong enough to be worth stating in the note.

## smallest_param_shift_to_test

Most informative next shifts:

- `R(B10,B10)`: test whether the same Goodman/Paley mechanism sharpens the current interval and whether `P(41)` is the right critical witness.
- Extremal uniqueness at `B9`: test whether every `(37,18,8,9)` witness is isomorphic to the Paley graph, which would strengthen the packet without changing the title theorem.

## why_this_is_or_is_not_publishable

If the argument survives verify, this is publishable in the strict micro-paper lane.

Why:

- the title theorem is exact and family-anchored,
- the result closes a one-step current interval,
- the proof is short,
- the package includes a nontrivial structural extremal slice.

Would a successful solve already be `70-90%` of a paper? Yes. I would score this around `0.88`.

Minimal remaining packaging work:

- write the Goodman-count upper-bound proof cleanly,
- present the Paley `K37` witness cleanly,
- include the tiny verification transcript or appendix,
- add the short literature paragraph around the existing `37 <= R(B9,B9) <= 38` interval.

Current solve is not too thin for the micro-paper lane.

## paper_shape_support

What extra structure makes the main claim paper-shaped once closed?

- the rigidity lemma at `n=37`,
- the explicit Paley witness,
- one short remark explaining why the proof naturally singles out `(37,18,8,9)`.

Together these mean the note is not just “here is a coloring”, but “the exact value is `38`, and the critical `37`-vertex boundary is rigid enough to be identifiable.”

## boundary_remark

## verify_rediscovery

PASS 1 result: `REDISCOVERY`.

Bounded web audit was enough to overturn the frontier premise. A recent search result for William J. Wesley, *Lower bounds for book Ramsey numbers* (Discrete Mathematics 349(5) (2026), 114913), quotes the Rousseau-Sheehan theorem:

`R(B_n,B_n) = 4n + 2` whenever `4n + 1` is a prime power.

This already settles the active instance, because for `n = 9` we have `4n + 1 = 37`, and `37` is prime. Hence the exact intended statement

`R(B9,B9) = 38`

is already known from prior art. That makes the present run a rediscovery rather than a frontier closure. The selected packet's novelty basis was therefore incorrect.

## verify_faithfulness

The local solved claim matches the intended theorem exactly: the packet aims to determine the least `n` forcing a monochromatic `B9`, and the solve claim is precisely `R(B9,B9) = 38`.

I did not find quantifier drift, wrong-theorem drift, or a proxy statement substituted for the intended one.

What failed is not theorem faithfulness but literature faithfulness: the packet treats the case as still open, while PASS 1 indicates the exact instance is already covered by an earlier family theorem.

## verify_proof

Within the bounded local proof check, I did not find an incorrect mathematical step.

Checks:

- the `K38` upper bound from `3t(G) <= 8e(G)`, `3t(\\bar G) <= 8e(\\bar G)`, and Goodman's identity is arithmetically correct and gives a strict contradiction;
- the `K37` equality case is also correct: equality forces `18`-regularity and exact same-color codegree `8` on each edge;
- the deduction of strongly regular parameters `(37,18,8,9)` from the blue-edge count is correct;
- the Paley graph `P(37)` is a valid witness with those parameters.

So the first substantive failure in the overall run is novelty, not proof correctness.

## verify_adversarial

I reran the claimed witness verification with a fresh inline Python check.

Observed:

- for `n = 38`, the Goodman lower bound is `1938` while the book-free upper bound is `1874.666...`, so the contradiction is real;
- for `n = 37`, both bounds equal `1776`, confirming the equality case used in the rigidity argument;
- the Paley graph on `F_37` has degree set `{18}`;
- every red edge has exactly `8` red common neighbors;
- every blue edge has exactly `8` blue common neighbors.

This adversarial pass did not break the construction or the arithmetic. The packet still fails overall because the result is already in the literature.

## verify_theorem_worthiness

Exactness: yes, the local argument targets and supports the exact theorem `R(B9,B9)=38`.

Novelty: no. PASS 1 indicates the exact theorem is already known, so the best honest status is `REDISCOVERY`.

Reproducibility: yes. The proof skeleton is short, and the Paley witness is easy to recheck computationally.

Lean readiness: no. Formalization here would be archival polish on a rediscovery, not the shortest path to a sealed frontier packet.

Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No, because the theorem is not frontier-novel.

What percentage of the paper would one solve already provide? `0%` of a new micro-paper, because the title theorem is already taken.

What title theorem is actually visible? `R(B9,B9)=38`, but as a known theorem rather than a new one.

What part of the argument scales? The Goodman plus local-codegree forcing template, the equality-case rigidity mechanism, and the Paley witness family.

What part clearly does not? The publication claim. This exact slice no longer supports a frontier note.

Best honest publication status: `REDISCOVERY`, not `INSTANCE_ONLY`, `SLICE_CANDIDATE`, or `PAPER_READY`.

## verify_verdict

`REDISCOVERY`.

The active packet should not proceed toward Lean or publication packaging as a frontier result. The correct next action is to archive this slug as a rediscovery and refresh curation memory so the exact case is not reselected.

## minimal_repair_if_any

No mathematical repair is needed for the local proof sketch.

The conservative repair is metadata-only:

- reclassify the run as `REDISCOVERY`;
- cite the prior theorem covering `R(B9,B9)=38`;
- archive the candidate instead of advancing it to Lean or publication audit as frontier work.

Boundary remark:

The `n=38` side is globally overdetermined by Goodman, but the `n=37` side is exactly tight. That gap of one Goodman unit is the entire reason a `K37` witness can exist at all, and it explains why the extremal witness must saturate every local and global inequality simultaneously.

## likely_failure_points

- The character-sum count for the Paley construction should be checked carefully in verify, although the computational witness check supports it.
- The writeup should distinguish clearly between the proof of the forcing bound at `38` and the explicit witness at `37`.
- If the publication packet wants a citation for the Paley parameter facts, verify should decide whether to present a self-contained count or cite standard strongly regular graph facts.

## what_verify_should_check

- Recheck the Goodman arithmetic for `n=38` and `n=37`.
- Recheck that the equality case indeed forces degree `18` at every vertex.
- Recheck the conversion from blue common-neighbor count `8` to red nonedge common-neighbor count `9`.
- Verify the Paley witness formally or with an independent checker.
- Confirm that combining the new `K37` witness with the existing forcing side yields the exact title theorem `R(B9,B9)=38`.
