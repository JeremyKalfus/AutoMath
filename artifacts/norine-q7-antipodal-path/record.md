# norine-q7-antipodal-path

## statement_lock
- Active slug: `norine-q7-antipodal-path`
- Title: `Norine antipodal-path conjecture at dimension 7`
- Locked intended statement from `selected_problem.md`: every edge-antipodal `2`-coloring of `Q7` has a monochromatic antipodal path.
- Literal meaning used below: a monochromatic antipodal path is any single-color edge path in `Q7` joining some vertex `x` to its antipode `\bar x`.

Self-check:
- I am solving the exact statement written in the selected problem file, not a strengthened or repaired variant.
- The canonical background says the case is open through dimension `6`, so any trivial disproof must be treated as a possible sign of a source-definition mismatch and flagged for verification.

## definitions
- Write vertices of `Q7` as bitstrings `x = (x_1,\dots,x_7) \in \{0,1\}^7`.
- A dimension-`i` edge is an edge joining `x` to `x \oplus e_i`.
- The antipode of `x` is `\bar x = x \oplus (1,1,1,1,1,1,1)`.
- Two edges are antipodal if one is obtained from the other by complementing every coordinate of both endpoints.
- In a monochromatic path from `u` to `v`, every edge has the same color.

Ambiguities / conventions that matter:
- The selected file does not require the monochromatic path to be geodesic or induced; I therefore read "path" in the ordinary graph-theoretic sense.
- The selected file does not impose any nontriviality condition on the coloring beyond the antipodal-edge constraint.
- Under that literal reading, a coloring that is constant on each coordinate direction is allowed.

Self-check:
- These conventions are all directly compatible with the text in `selected_problem.md`.
- The likely danger is not in the proof below but in whether the selected file omitted an intended extra hypothesis from the canonical source.

## approach_A
Structural / invariant route: exploit a coordinate fixed on every monochromatic component.

Idea:
- If one color never uses some coordinate direction `i`, then every path in that color preserves the `i`-th coordinate.
- Therefore every connected component of that monochromatic subgraph is contained in one codimension-`1` face `x_i = 0` or `x_i = 1`.
- No two vertices in the same such face are antipodal in `Q7`, because antipodal vertices differ in every coordinate, including coordinate `i`.

Immediate consequence:
- Any coloring in which red omits at least one dimension and blue omits at least one dimension has no monochromatic antipodal path.

Self-check:
- The invariant is exact: a path can only change coordinates along dimensions actually used by its edges.
- This route already suggests a very small explicit counterexample.

## approach_B
Construction / extremal / contradiction route: build the smallest possible direction-split coloring.

Construction candidate:
- Color every dimension-`1` edge red.
- Color every dimension-`i` edge blue for `i = 2,3,4,5,6,7`.

Why it is legal:
- Antipodal edges in `Q7` are parallel, hence have the same dimension.
- Since the coloring depends only on the dimension, each antipodal pair of edges receives the same color.

Why it should kill monochromatic antipodal paths:
- A red path uses only dimension `1`, so it never changes coordinates `2,3,4,5,6,7`.
- A blue path uses only dimensions `2,3,4,5,6,7`, so it never changes coordinate `1`.
- But antipodal vertices differ in all seven coordinates.

Self-check:
- This is a concrete witness, not merely a family heuristic.
- The proof burden is now just to formalize the preceding two bullets cleanly.

## lemma_graph
1. Lemma 1: if a monochromatic path uses no edge in dimension `i`, then the `i`-th coordinate is constant along that path.
2. Lemma 2: in the direction-split coloring with red = dimension `1` and blue = dimensions `2..7`, every red path has constant coordinates `2..7`, and every blue path has constant coordinate `1`.
3. Lemma 3: antipodal vertices of `Q7` differ in every coordinate.
4. Conclusion: in that coloring, no red path and no blue path can join antipodal vertices.
5. Auxiliary legality check: the coloring is edge-antipodal because antipodal edges have the same dimension.

## chosen_plan
- The structural route and the explicit construction route collapse to the same disproof.
- I therefore chose the direct witness from approach B and proved it using the coordinate-invariance lemma from approach A.
- No code is justified before writing out that exact proof, because the witness is already fully explicit and human-checkable.

Self-check:
- This is the shortest path to an exact solve-stage output.
- I am not claiming anything about the canonical Norine source beyond the literal selected statement.

## self_checks
- Statement check: every claim refers to the literal intended statement in `selected_problem.md`.
- Legality check: the proposed coloring does satisfy the selected file's edge-antipodal condition.
- Scope check: the argument actually proves a stronger fact for the literal formulation, namely that the same construction works in every `Qn` with `n >= 2`.
- Conservatism check: because that stronger fact clashes sharply with the dossier's "verified through dimension 6" narrative, verification must audit the source wording before treating this as faithful to the external problem.

## code_used
- No code used.
- Reason: the disproof is explicit and short enough to verify directly from coordinate invariants.

## result
- Solve-stage verdict: `COUNTEREXAMPLE`
- Confidence on the literal selected statement: `high`
- Explicit counterexample coloring:
  - red edges: exactly the dimension-`1` edges;
  - blue edges: exactly the dimension-`2`, `3`, `4`, `5`, `6`, and `7` edges.

Rigorous disproof:

Take the coloring just described. It is edge-antipodal because antipodal edges are parallel and therefore have the same dimension.

Now consider any red path. Every red edge changes only coordinate `1`, so coordinates `2,3,4,5,6,7` remain constant along the entire path. Hence the two endpoints of a red path can differ in at most coordinate `1`. In particular, they cannot be antipodal.

Likewise, any blue path changes only coordinates `2,3,4,5,6,7`, so coordinate `1` remains constant along the entire path. Hence the two endpoints of a blue path cannot be antipodal either.

Therefore this edge-antipodal `2`-coloring of `Q7` contains no monochromatic path between any pair of antipodal vertices. So the literal intended statement in `selected_problem.md` is false.

Self-check:
- The proof uses only the selected definitions and a concrete witness.
- There is no hidden search step, induction, or unproved lemma left.

## likely_failure_points
- The main risk is faithfulness, not mathematics: the canonical source may use a stronger notion than the selected file copied over.
- In particular, verification should test whether "monochromatic antipodal path" was intended to mean geodesic with one edge in every dimension, or whether "edge-antipodal coloring" had an additional constraint omitted here.
- If the selected wording is accurate, the disproof is complete; if not, this run may really be a disproof of an unintended weakened variant.

## what_verify_should_check
- First check faithfulness to the source before anything else. The literal statement here is defeated by a one-direction-vs-six-directions coloring, so the source wording should be audited carefully.
- Check the legality of the witness under the selected definitions:
  - antipodal edges are parallel;
  - the color depends only on the dimension, so antipodal edges match.
- Check the invariant argument:
  - red paths preserve coordinates `2..7`;
  - blue paths preserve coordinate `1`;
  - antipodal pairs differ in all seven coordinates.
- If the selected statement is indeed literal, this artifact should move forward as an exact finite counterexample candidate and become Lean-friendly immediately after skeptical verification.

## verify_rediscovery
- PASS 1 used a bounded web audit and stopped once the source-definition mismatch was clear.
- The canonical MathCheck statement for Norine's conjecture is not the same as the selected-file statement: it asks for a path `v_0,\dots,v_n` from `x` to its antipode such that the colors satisfy `c(v_i v_{i+1}) != c(v_{n-i-1} v_{n-i})` for each `i`, rather than requiring antipodal edge pairs to receive the same color and then asking for an arbitrary monochromatic path.
- The same MathCheck source reports computational verification only for small dimensions of that canonical statement, which is consistent with the dossier's narrative and inconsistent with the trivial direction-split disproof of the copied statement.
- Conclusion for PASS 1: no bounded search evidence showed that the exact copied statement from `selected_problem.md` is a frontier-open problem. Instead, the web audit showed that the selected file drifted away from the canonical source and turned the target into a different, much weaker variant.
- Because the run is already non-faithful to the canonical conjecture, I do not classify this as `REDISCOVERY`; I classify it as a wrong-statement variant.

## verify_faithfulness
- The solve-stage argument is faithful to the literal text currently written in `selected_problem.md`.
- It is not faithful to the canonical Norine problem described by the cited source material. The crucial drift is definitional:
  - selected file: antipodal edges are required to have the same color, and the target is an arbitrary monochromatic antipodal path;
  - canonical source: the path condition is an antipodal color-complement condition along a length-`n` path, not the existence of a single-color path under a same-color antipodal-edge rule.
- This is therefore wrong-theorem drift, not merely a missing lemma. The solver disproved a nearby weakened statement, not the intended canonical conjecture.
- Classification consequence: this run must be `VARIANT`, not `EXACT`, `CANDIDATE`, or a verified disproof of the canonical problem.

## verify_proof
- First incorrect step relative to the intended canonical problem: the statement lock imported the wrong definitions, so the solve proof is aimed at the wrong theorem from the outset.
- Conditional on the literal copied statement, I found no incorrect mathematical step in the counterexample argument.
- The key claims are sound under that literal reading:
  - antipodal edges in `Q7` are parallel and therefore share a coordinate direction;
  - the dimension-split coloring is legal for the copied same-color antipodal-edge rule;
  - red paths preserve coordinates `2..7`, blue paths preserve coordinate `1`, so neither color can connect antipodes.
- Therefore the proof is locally correct but globally irrelevant to the canonical target because of the source mismatch.

## verify_adversarial
- No checker existed in the artifact, so I ran one tiny local enumeration on the explicit witness only.
- The computation confirmed that under the copied coloring rule, the red subgraph and the blue subgraph each have no connected component containing an antipodal pair in `Q7`.
- This supports the solver's local claim, but it does not repair the faithfulness failure.

## verify_verdict
- `WRONG_STATEMENT`
- Final classification for this run: `VARIANT`
- Confidence: `high`
- `lean_ready = false`
- Exact reason Lean should not run: the artifact currently solves a non-canonical weakened variant created by a definition drift in `selected_problem.md`, so formalizing it would not advance the frontier target.

## minimal_repair_if_any
- No tiny conservative repair can save this run in place.
- The needed repair is to restore the canonical Norine statement in problem selection and restart solve from that corrected statement.

## lean_statement
- Lean file: `lean/AutoMath/NorineQ7Variant.lean`
- Mirrored Lean file: `artifacts/norine-q7-antipodal-path/lean/NorineQ7Variant.lean`
- Formalized statement: there exists the explicit direction-split coloring of `Q7` with red on dimension `0` and blue on dimensions `1..6`, antipodal edges stay in the same dimension, and neither color admits a path from any vertex to its antipode.
- Main theorem: `AutoMath.NorineQ7Variant.norine_q7_variant_counterexample`
- Scope note: this is the copied repo variant only, not the canonical Norine conjecture audited in verification.

## lean_skeleton
- Represent vertices as `Fin 7 → Bool`.
- Define `antipode`, `EdgeInDim`, the witness dimension-coloring, and color-specific step relations.
- Prove that red steps can only move in coordinate `0` and blue steps can never change coordinate `0`.
- Lift those coordinate invariants from one step to `Relation.ReflTransGen` monochromatic paths.
- Conclude that no red or blue monochromatic path can reach an antipode, because antipodes differ in every coordinate.

## lean_result
- `lake env lean AutoMath/NorineQ7Variant.lean` succeeded on 2026-04-08.
- `lake build AutoMath.NorineQ7Variant` succeeded on 2026-04-08.
- `lake build AutoMath` succeeded after importing the file into the main project.
- `#print axioms AutoMath.NorineQ7Variant.norine_q7_variant_counterexample` reported only `[propext]`.
- The artifact is Lean-checked as a `VARIANT` counterexample to the copied statement, not as an `EXACT` result for the canonical problem.

## lean_blockers
- No Lean blocker remains for the copied variant statement.
- The real blocker is still mathematical faithfulness: verification already showed that the selected repo statement drifted away from the canonical Norine source, so this Lean result should not be promoted to a frontier success.
