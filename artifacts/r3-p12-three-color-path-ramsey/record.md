# `r3-p12-three-color-path-ramsey` Solve Record

## statement_lock
- Active slug: `r3-p12-three-color-path-ramsey`
- Active title: `Determine the exact value of R(P12, P12, P12)`
- Locked convention: `P12` means the path on 12 vertices.
- Locked exact target: determine whether every 3-coloring of `K22` contains a monochromatic `P12`, or else exhibit a 3-coloring of `K22` with no monochromatic `P12`.
- Exact title theorem if solved: `R(P12, P12, P12) = 22`.
- Publication relevance if solved: yes; this would already be about 70-90% of a short paper, with the remaining work mostly exposition, extremal-description cleanup, and comparison to the solved `P8` and `P9` cases.

## definitions
- `R(P12, P12, P12)` is the least `N` such that every 3-edge-coloring of `K_N` contains a monochromatic copy of `P12`.
- A lower-bound witness for the conjectural value `22` is a 3-coloring of `K21` with no monochromatic `P12`.
- A disproof of the conjectural value `22` would need a 3-coloring of `K22` with no monochromatic `P12`, yielding `R(P12, P12, P12) >= 23`.
- For complete bipartite graphs, the longest path in `K_{a,b}` has:
  - `a+b` vertices when `a=b`,
  - `2 min(a,b) + 1` vertices when `a != b`.
- In the four-block extremal template used below, the cross-colors are
  - red on `AB` and `CD`,
  - blue on `AC` and `BD`,
  - green on `AD` and `BC`.

Ambiguities / conventions that matter:
- The packet does not specify a canonical extremal-template class, so any template claim below must be stated explicitly as a slice, not as a theorem about all colorings.
- The solve stage cannot certify rediscovery and should not use web; any literature novelty check remains for verify.
- Even if a human proof of the exact statement appeared here, the harness would still stop short of `EXACT` before Lean.

## approach_A
Structural / invariant route.

Try to force `P12` in `K22` by analyzing a longest monochromatic path and the restrictions on outside vertices. A standard red-longest-path setup would be:
- take a longest red path `v1 ... vt` with `t <= 11`,
- use maximality to constrain how outside vertices can connect to the ends and to consecutive internal pairs of the path,
- convert the resulting scarcity of red extensions into a large blue/green structured region,
- then try to force a long blue or green path there.

Why this route is plausible:
- the conjectural value `22` is only one step above the standard `21`-vertex lower-bound scale,
- a successful upper bound should look like a stability statement saying that any putative counterexample must collapse toward the usual four-block path-avoiding template,
- that type of forcing argument is the natural path to a paper-shaped exact-value proof.

Why this route did not close here:
- I do not have a local theorem packet for the precise endpoint-rotation lemmas or a usable 3-color stability lemma,
- the red-maximal-path constraints alone do not immediately compress an arbitrary 22-vertex coloring into a finite template family,
- without that compression, this route remains conceptual rather than rigorous in the current pass.

Self-check:
- This is theorem-facing, not hand-waving, but it does not currently produce a complete contradiction on `K22`.

## approach_B
Construction / extremal / contradiction route.

Start from the standard four-block lower-bound philosophy and push it as far as possible.

### Rigorous lower-bound witness on 21 vertices
Partition `V(K21)` into `A,B,C,D` with sizes
- `|A| = 6`,
- `|B| = |C| = |D| = 5`.

Color edges as follows:
- all edges inside each part red,
- all edges between `A,B` and between `C,D` red,
- all edges between `A,C` and between `B,D` blue,
- all edges between `A,D` and between `B,C` green.

Then:
- the red graph is `K11 \cup K10`, so it has no `P12`,
- the blue graph is `K_{6,5} \cup K_{5,5}`, so its longest path has at most `11` vertices,
- the green graph is `K_{6,5} \cup K_{5,5}`, so its longest path also has at most `11` vertices.

Therefore this is a valid `K21` witness with no monochromatic `P12`, proving
- `R(P12, P12, P12) >= 22`.

### Theorem-facing slice on 22 vertices
Consider the template family `T` of 3-colorings obtained from a partition into four nonempty parts `A,B,C,D`, with the same fixed cross-color pattern
- red on `AB, CD`,
- blue on `AC, BD`,
- green on `AD, BC`,
and with each part internally monochromatic in one of the three colors.

Claim:
- No coloring in `T` on 22 vertices avoids a monochromatic `P12`.

Proof skeleton:
1. For any paired component `X-Y` of one color:
   - if neither `X` nor `Y` is internally that color, the component is `K_{|X|,|Y|}`;
   - if at least one of `X` or `Y` is internally that color, the component has a Hamilton path on all `|X| + |Y|` vertices, because one side is a clique joined completely to the other side.
2. Hence any `P12`-free member of `T` must satisfy:
   - for every monochromatic paired component with no internally colored side, not both part sizes are at least `6`,
   - for every monochromatic paired component with an internally colored side, the paired sum is at most `11`.
3. Since every unordered pair of parts occurs as one of the six monochromatic cross-pairs, two parts of size at least `6` would already create a monochromatic `K_{6,6}`, and thus a monochromatic `P12`.
4. So in a `P12`-free 22-vertex member of `T`, at most one part can have size at least `6`. Let the largest part have size `a`. Then `a >= 7`, and the other three parts all have size at most `5`.
5. Let the largest part be `A`. Its internal color is one of red, blue, or green, so it boosts exactly one paired component among `AB`, `AC`, `AD`. Let the chosen partner have size `x`.
6. Because the other two partner candidates are each at most `5`, the smallest partner size satisfies
   - `x >= 22 - a - 5 - 5 = 12 - a`.
7. But the boosted monochromatic component on `A` and that partner has a Hamilton path on `a + x` vertices, and
   - `a + x >= a + (12 - a) = 12`,
   so it contains a monochromatic `P12`, contradiction.

Conclusion:
- the standard four-block matching-template family with monochromatic parts has maximum order `21` if it avoids a monochromatic `P12`.

Self-check:
- The lower bound on `21` is fully rigorous.
- The template obstruction on `22` is fully rigorous for the stated family `T`.
- This is still not a proof that every 22-vertex coloring lies in `T`.

## lemma_graph
- Lemma 1: The explicit `6,5,5,5` four-block coloring avoids monochromatic `P12`.
- Lemma 2: In a paired component `X-Y` of the four-block template, if one side is internally the same color, then the component has a Hamilton path on all `|X| + |Y|` vertices.
- Lemma 3: If neither side is internally that color, the paired component is `K_{|X|,|Y|}` and contains `P12` whenever both sides have size at least `6`.
- Lemma 4: Therefore any `P12`-free 22-vertex coloring in the monochromatic-part four-block family can have at most one part of size at least `6`.
- Lemma 5: The largest part then has size at least `7`, and whichever internal color it chooses forces a boosted partner sum of at least `12`, contradiction.
- Candidate synthesis: the canonical 21-vertex extremal construction survives, but the same template family cannot extend to `22`.

## chosen_plan
The best path in this pass is the extremal-template route:
- secure a rigorous lower bound `R >= 22`,
- prove a real structural slice showing that the most natural 22-vertex extension of the witness family cannot work,
- stop explicitly once the argument no longer controls arbitrary 22-vertex colorings.

Reason for choosing this path:
- it yields an honest theorem slice rather than a vague heuristic,
- it keeps the micro-paper objective visible by isolating the exact missing step,
- it avoids drifting into broad brute force or infrastructure-heavy search.

Self-check:
- This is the strongest rigorous output available from the local packet without pretending to have the global stability theorem that would finish the exact value.

## self_checks
- Statement lock check: the target remained the exact value question for `R(P12,P12,P12)`, not a weaker existence problem.
- Scope check: I stayed inside the candidate-local files and used no web.
- Method check: reasoning came first; the only computation was a bounded sanity check for the finite template family after the proof skeleton was already in place.
- Claim check: the record distinguishes rigorously proved slice results from the still-open exact closure.

## code_used
- Minimal code was used only as a bounded sanity check on the finite four-block monochromatic-part template family.
- No SAT, ILP, CP-SAT, broad brute force over arbitrary 22-vertex colorings, or external tooling was used.
- The core mathematical claims recorded here do not rely on a black-box search over all `K22` colorings.

## result
- Proven in this pass: `R(P12, P12, P12) >= 22` via an explicit `K21` coloring.
- Proven theorem slice: within the four-block matching-template family with monochromatic parts, order `21` is maximal for avoiding a monochromatic `P12`; no 22-vertex member of that family works.
- Not proven in this pass: the global upper bound `R(P12, P12, P12) <= 22`.
- Therefore the exact value is still unresolved here.

Immediate corollary / boundary payoff:
- Any 22-vertex counterexample, if one exists, must be genuinely nontrivial: it cannot be a standard four-block matching-template coloring with monochromatic parts.

Paper-shape interpretation:
- If the main exact claim closes, the title theorem is already present.
- Minimal remaining packaging would be: write the forcing argument or explicit witness cleanly, compare against the known `P8` and `P9` cases, and isolate the extremal description or final obstruction remark.
- With only the current slice, the package is still too thin for the micro-paper lane by itself.

## family_affinity
High.

This attempt sits squarely in the diagonal three-color path-Ramsey line suggested by the packet. The lower-bound witness and the 22-vertex template obstruction both use the same four-block design language that underlies the conjectural value `22`.

## generalization_signal
Moderate but incomplete.

What seems to scale:
- the proof that a boosted paired component in the four-block family has a Hamilton path on the full paired sum,
- the observation that any two parts of size at least `m` immediately force `P_{2m}` through a monochromatic `K_{m,m}`,
- the template-maximality mechanism for even paths in matching-based four-block constructions.

What does not yet scale:
- the missing stability step from an arbitrary 22-vertex coloring to a four-block template,
- the control of non-template counterexamples with mixed internal structure.

Suggested theorem slice from the scaling signal:
- for even paths `P_{2m}`, determine the largest order of monochromatic-part four-block matching templates that avoid a monochromatic `P_{2m}`.

## proof_template_reuse
Reusable core:
- explicit lower-bound witness from a four-block matching template,
- template obstruction via a largest-part argument,
- distinction between bipartite-only paired components and paired components with an internal monochromatic clique.

This proof template should reuse well for nearby even-path diagonal cases where the conjectural value is also driven by a four-block lower-bound construction.

## candidate_theorem_slice
Candidate theorem slice:

`In the four-block matching-template family with monochromatic parts, the largest 3-coloring with no monochromatic P12 has order 21. In particular, no 22-vertex coloring of that family avoids a monochromatic P12.`

This is a real theorem-facing slice, but it is still a slice of the full exact-value problem rather than the title theorem itself.

## smallest_param_shift_to_test
- First shift: `P10`, because it is the first open diagonal case in the survey narrative and the same template analysis may be easier to close there.
- Second shift: keep `P12` fixed and enlarge the structural class slightly, for example allowing one non-monochromatic internal part while keeping the same four-block cross-color pattern.

These shifts would test whether the current obstruction argument is actually close to the full exact problem or only to a narrow template subclass.

## why_this_is_or_is_not_publishable
Current output is not yet publishable as a micro-paper.

Reason:
- the exact title theorem `R(P12, P12, P12) = 22` is not closed,
- the current slice is mathematically real but still an extremal-family obstruction rather than the full diagonal Ramsey determination,
- on its own, it does not yet supply the title theorem of a short paper.

If the exact upper bound on `22` were added, the package would immediately become paper-shaped and would likely need only modest exposition.

## paper_shape_support
What extra structure would make this paper-shaped if the main claim closes?

- A stability lemma showing that any 22-vertex `P12`-avoiding coloring must reduce to the four-block template language, or
- an explicit 22-vertex counterexample with a clear extremal description.

What would the paper then look like?
- Title theorem: `The Exact Value of R(P12, P12, P12)`.
- Supporting structure: one explicit lower-bound construction, one forcing argument or extremal witness description, one short comparison to `P8` and `P9`, and one brief remark about why the standard four-block family is the right obstruction language.

Current assessment against the 70-90% threshold:
- exact closure would satisfy that threshold,
- the current result does not.

## boundary_remark
Boundary remark:

The standard `21`-vertex four-block witness survives, but the same design principle cannot be extended to `22` inside the monochromatic-part template family. So the obstruction boundary sits exactly where the conjectural value says it should, at least for the most natural extremal template class.

## likely_failure_points
- The main unresolved risk is non-template behavior on 22 vertices; a genuine counterexample, if it exists, could use mixed internal colorings or a structure not captured by the four-block family.
- The largest-path structural route needs a real compression lemma; without it, the upper bound remains aspirational.
- The theorem slice proven here may be too narrow to materially shorten the final proof if the true extremal colorings are not close to this template family.

## what_verify_should_check
- Verify the explicit `K21` witness carefully, including the path-length calculation in `K_{6,5}` and `K_{5,5}`.
- Verify the largest-part argument for the monochromatic-part four-block family on 22 vertices.
- Check whether this template slice is already implicit in the literature; if so, downgrade the novelty of the slice even though the full exact-value target remains frontier-facing.
- Check whether any known partial results for `R(P10,P10,P10)`, `R(P11,P11,P11)`, or `R(P12,P12,P12)` already include a stronger template obstruction.
