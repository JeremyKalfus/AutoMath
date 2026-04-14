# Solve Record: The Exact Value of R(P10, P10, P10)

## statement_lock
- Active slug: `r3-p10-three-color-path-ramsey`.
- Active title: `Determine the exact value of R(P10, P10, P10)`.
- Exact intended theorem for this run: determine whether every 3-coloring of `K18` contains a monochromatic `P10`, or else produce an explicit 3-coloring of `K18` with no monochromatic `P10`.
- Exact title theorem if the upper bound closes: `R(P10, P10, P10) = 18`.
- Exact title theorem if the target fails: `R(P10, P10, P10) >= 19`.
- Publication bar check: a full exact solve here would still be about `70-90%` of a short paper; the packet estimate `0.85` still looks right.

## definitions
- Convention: `P10` means the simple path on `10` vertices.
- Convention: `R(P10, P10, P10)` is the least `N` such that every 3-edge-coloring of `K_N` has a monochromatic `P10`.
- Lower-bound convention: a coloring of `K17` with no monochromatic `P10` proves `R(P10, P10, P10) >= 18`.
- Disproof convention: to refute the conjectural value `18`, one needs a coloring of `K18` with no monochromatic `P10`, which would prove `R(P10, P10, P10) >= 19`.
- Ambiguity resolved: the packet uses path notation by number of vertices, consistent with the neighboring values `R(P8,P8,P8)=14` and `R(P9,P9,P9)=17`.
- Missing definition that matters for the attempted upper bound: what exact stability form should replace the heuristic “every near-extremal counterexample resembles the 4-block lower template”? This remains the main unresolved reduction step.

## approach_A
- Structural / invariant route: treat the standard `K17` lower-bound coloring as the extremal model and try to prove that any `K18` counterexample must be a one-vertex extension of that 4-block quotient pattern.
- Natural quotient pattern: partition into four blocks and color cross edges by a 1-factorization of `K4`, namely `red: AB, CD`, `blue: AC, BD`, `green: AD, BC`.
- Key invariant inside that model:
  - a monochromatic `K5,5` already contains a `P10`;
  - a monochromatic `K6,4` plus a same-color internal edge on the size-6 side already contains a `P10`.
- Consequence inside the natural extremal family: every one-vertex extension of the standard `K17` 4-block template already forces a monochromatic `P10`.
- What this route still needs for the full theorem: a genuine stability reduction from an arbitrary `K18` coloring with no monochromatic `P10` to that 4-block model. I do not have that reduction yet.

## approach_B
- Construction / extremal route: first lock the sharp lower bound with an explicit `K17` coloring.
- Construction:
  - partition the vertex set into blocks `A,B,C,D` of sizes `5,4,4,4`;
  - color all edges inside each block red;
  - color cross edges by `red: AB, CD`, `blue: AC, BD`, `green: AD, BC`.
- Check:
  - the red graph is `K9` on `A ∪ B` together with `K8` on `C ∪ D`, so it has no `P10`;
  - the blue graph is `K5,4` on `A ∪ C` together with `K4,4` on `B ∪ D`, so it has no `P10`;
  - the green graph is `K5,4` on `A ∪ D` together with `K4,4` on `B ∪ C`, so it has no `P10`.
- Therefore `R(P10, P10, P10) >= 18` exactly.
- Construction route obstruction on `K18`: the obvious one-vertex four-block extensions fail, but that alone does not exclude more irregular `K18` colorings.

## lemma_graph
- Lemma 1. The explicit `5,4,4,4` block coloring above gives a valid `K17` counterexample, hence `R(P10,P10,P10) >= 18`.
- Lemma 2. `K5,5` contains a `P10` by alternating across the bipartition.
- Lemma 3. If all edges between disjoint sets `A,B` are red with `|A| = 6` and `|B| = 4`, then any red edge inside `A` creates a red `P10`.
  - Proof skeleton: if `xy` is a red edge in `A`, and `B = {b1,b2,b3,b4}`, with remaining `A`-vertices `a1,a2,a3,a4`, then `x-y-b1-a1-b2-a2-b3-a3-b4-a4` is a red `P10`.
- Lemma 4. Every one-vertex extension of the standard `5,4,4,4` four-block lower template on `18` vertices forces a monochromatic `P10`.
  - Case `5,5,4,4`: one matched pair is a monochromatic `K5,5`, so Lemma 2 applies.
  - Case `6,4,4,4`: the size-6 block is paired with a size-4 block in each of the three colors; by Lemma 3, the size-6 block can contain no internal edge of any color, impossible.
- Lemma 5. The same obstruction pattern generalizes for even paths: in the standard lower-bound four-block family for `P_{2m}`, any one-vertex extension of the block sizes `(m,m-1,m-1,m-1)` already forces a monochromatic `P_{2m}`.

## chosen_plan
- Chosen path: formalize the sharp lower bound and the strongest clean upper-bound slice available, namely the complete obstruction to one-vertex extensions of the natural 4-block extremal family.
- Explicit paper-shape question: what extra structure would make this result paper-shaped if the main claim closes?
- Answer: a stability theorem saying that every `K18` counterexample must reduce to the same four-block quotient pattern, plus the already obtained one-vertex-extension obstruction, would make the final note almost fully packaged.
- Because that stability reduction did not close, I used one bounded experiment only after the two reasoning routes above: exhaustive search over vertex-transitive circulant colorings of `K18`.

## self_checks
- Self-check after statement lock: the target is still exactly the intended `K18` upper bound or `K18` counterexample; I did not drift into a feeder problem.
- Self-check after Approach B: the `K17` construction is rigorous and genuinely sharp for the lower bound `>= 18`.
- Self-check after Lemma 4: the upper-bound slice is honest but narrower than the full theorem; it only kills the obvious four-block extension family.
- Self-check after the bounded experiment: zero circulant counterexamples is evidence, not proof; it cannot upgrade the classification beyond `PARTIAL`.

## code_used
- Minimal code used: `artifacts/r3-p10-three-color-path-ramsey/circulant_check.py`.
- Purpose:
  - verify the explicit `K17` lower-bound coloring;
  - exhaust the narrow family of vertex-transitive circulant 3-colorings of `K18`.
- Output:
  - the `K17` construction was confirmed to have no monochromatic `P10`;
  - no circulant coloring of `K18` avoided a monochromatic `P10`.
- Mathematical role: supportive only. The lower bound and Lemma 4 do not depend on the script.

## result
- Proven rigorously in this run:
  - `R(P10, P10, P10) >= 18`;
  - every one-vertex four-block extension of the standard `K17` lower template already forces a monochromatic `P10`.
- Not proven in this run:
  - the full upper bound `R(P10, P10, P10) <= 18`.
- Best current honest claim:
  - `PARTIAL`, with a real theorem-facing slice and strong but still nonconclusive evidence toward `R(P10, P10, P10) = 18`.
- Immediate corollary / boundary remark:
  - the usual one-vertex extension of the standard four-block lower construction cannot supply a `K18` counterexample.
- Minimal remaining packaging work if the main claim closes later:
  - add the missing stability reduction;
  - present the `K17` extremal coloring and the one-vertex-extension obstruction as the extremal discussion section;
  - include a short comparison to the solved `P8` and `P9` diagonal cases.

## family_affinity
- Strong.
- This sits exactly at the first open diagonal point of the three-color path Ramsey family, and the obstruction proved here directly targets the standard lower-bound family for even diagonal path cases.

## generalization_signal
- Clear theorem-slice signal: for even `P_{2m}`, the natural lower-bound four-block template `(m,m-1,m-1,m-1)` cannot survive a one-vertex extension inside the same quotient pattern.
- What scales:
  - the `K_{m,m}` obstruction in the balanced extension case;
  - the “size `(m+1)` block cannot contain an internal edge of any color” obstruction in the unbalanced extension case.
- What does not yet scale:
  - the stability reduction from arbitrary colorings to that four-block quotient pattern.

## proof_template_reuse
- Reusable proof template:
  - write the standard four-block lower construction;
  - classify all one-vertex extensions of the block-size vector;
  - prove that balanced matched pairs create `K_{m,m}` and unbalanced matched pairs plus one internal edge force `P_{2m}`;
  - conclude that the natural extremal family is already saturated at the conjectured upper bound.
- This template looks reusable for future even diagonal path cases if the same lower construction is the right extremal model.

## candidate_theorem_slice
- Candidate slice:
  - `In the standard four-block lower-bound family for diagonal three-color path Ramsey numbers, every one-vertex extension of the even case already forces the target monochromatic path.`
- Specialization to this slug:
  - `Every one-vertex extension of the standard (5,4,4,4) four-block coloring for P10 contains a monochromatic P10.`
- This is a genuine theorem-shaped statement, but by itself it is still thinner than the full micro-paper target.

## smallest_param_shift_to_test
- First shift: test whether the same one-vertex-extension obstruction for the four-block family can be written cleanly for general `P_{2m}` and checked against the next unsolved even case.
- Second shift: test whether the analogous statement for two-vertex extensions yields any stronger stability leverage.
- Most useful immediate local shift for this exact slug: attempt a reduction showing that any `K18` counterexample must have a block decomposition whose reduced graph is the `K4` 1-factorization template.

## why_this_is_or_is_not_publishable
- Not yet publishable as the intended micro-paper.
- Reason:
  - the full title theorem `R(P10,P10,P10)=18` is not closed;
  - the current result is still a theorem slice plus evidence, not the exact-value note itself.
- Honest micro-paper assessment:
  - the current package is not just an isolated witness, but it is still too thin for the micro-paper lane on its own.
- If the main claim closes later, this solve packet is still useful because it already supplies the extremal lower construction, one clean obstruction lemma family, and a bounded falsifier sweep over a natural symmetric family.

## paper_shape_support
- Question: what extra structure would make this paper-shaped if the main claim closes?
- Answer:
  - a stability statement identifying the `5,4,4,4` lower construction as the unique or canonical `K17` obstruction;
  - a reduction from any `K18` counterexample to a one-vertex extension of that obstruction;
  - the already obtained extension lemma as the short contradiction step.
- If the full upper bound is proved, the remaining packaging work would be small: title theorem, proof, explicit extremal `K17` coloring, short section comparing `P8` and `P9`, and a paragraph on why the natural extension family fails.

## boundary_remark
- Boundary remark:
  - the current evidence points strongly toward `R(P10,P10,P10)=18`, but the unresolved boundary is no longer the standard four-block extremal family. Any genuine `K18` counterexample, if it exists, must be structurally less naive than a one-vertex extension of the usual lower template and also did not appear in the circulant family.

## likely_failure_points
- The main vulnerable point is the missing stability reduction from arbitrary `K18` colorings to the four-block quotient pattern.
- The generalization lemma for one-vertex extensions should be checked carefully for indexing and path length counts in the general `P_{2m}` statement.
- The bounded circulant search is only evidence; verify should not overread it as a proof ingredient.

## what_verify_should_check
- Check the explicit `K17` construction carefully and confirm each monochromatic component description.
- Check Lemma 3 exactly, especially the path-length count in the `K6,4` plus one internal-edge argument.
- Check Lemma 4 as stated: it is about one-vertex extensions of the standard `5,4,4,4` template, not arbitrary four-block colorings on `18` vertices.
- Check the generalized even-case wording in Lemma 5 and decide whether it belongs in the canonical packet or should stay as a conjectural proof template.
- For publication audit later:
  - treat the current output as `SLICE_CANDIDATE`, not as a finished exact-value result;
  - record that the natural lower-template extension family has been eliminated;
  - keep the circulant sweep as bounded negative evidence only.
