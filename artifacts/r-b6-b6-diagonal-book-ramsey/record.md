# Solve Record: The Exact Value of R(B6, B6)

## statement_lock
- Active slug: `r-b6-b6-diagonal-book-ramsey`.
- Active title: `Determine the exact value of R(B6, B6)`.
- I lock `B6` to mean the 6-page book graph: 6 triangles sharing one common base edge.
- In a red-blue coloring of `K_n`, a monochromatic `B6` exists exactly when some monochromatic edge has at least 6 common neighbors in its own color.
- The exact title theorem suggested by this solve is: `R(B6, B6) = 26`.
- If this closes cleanly, it already looks like about 80-85% of a short paper: the title theorem is the exact value, the remaining packaging is a compact citation of the known upper bound, a short presentation of the 25-vertex extremal coloring, and a novelty check that the lower construction was not already made explicit in the cited sources.
- Self-check: the missing step is the lower-bound side on `K25`, because the working packet already supplies the upper bound `R(B6, B6) <= 26`.

## definitions
- Write `c_R(uv)` for the number of common red neighbors of a red edge `uv`, and `c_B(uv)` analogously for blue.
- A color class avoids `B6` iff every edge in that color has same-color codegree at most 5.
- Therefore a coloring of `K25` with `c_R(uv) <= 5` on every red edge and `c_B(uv) <= 5` on every blue edge proves `R(B6, B6) >= 26`.
- For the constructive route, use the Paley graph on `F_25 = F_5[u]/(u^2-2)`. Color `xy` red when `x-y` is a nonzero square and blue otherwise.
- A concrete square set in this model is
  `{(1,0),(1,1),(1,4),(2,0),(2,2),(2,3),(3,0),(3,2),(3,3),(4,0),(4,1),(4,4)}`.
- Conventions fixed here:
  `u^2 = 2` in `F_25`, `2` is a nonsquare in `F_5`, and `-1 = 4` is a square in `F_5`, so the square-difference relation is symmetric.
- Self-check: this model is explicit enough for a direct checker and matches the book condition by same-color common-neighbor counts on edges.

## approach_A
- Structural / invariant route: assume there is a `B6`-free coloring of `K25`.
- Let `d(v)` be the red degree of vertex `v`. Then the number of non-monochromatic triangles is
  `N_mix = (1/2) * sum_v d(v)(24-d(v))`,
  because each mixed-color triangle contributes exactly 2 to the sum.
- Hence the number `M` of monochromatic triangles satisfies
  `M = C(25,3) - (1/2) * sum_v d(v)(24-d(v))`.
- Since `d(v)(24-d(v)) <= 12 * 12 = 144`, we get
  `M >= C(25,3) - (25 * 144)/2 = 2300 - 1800 = 500`.
- On the other hand, if both colors avoid `B6`, then every monochromatic edge lies in at most 5 monochromatic triangles, so
  `3M = sum_{red edge uv} c_R(uv) + sum_{blue edge uv} c_B(uv) <= 5 * C(25,2) = 1500`,
  hence `M <= 500`.
- Therefore any `B6`-free coloring of `K25` must satisfy equality everywhere:
  `M = 500`, every vertex has red degree 12, and every monochromatic edge has exactly 5 same-color common neighbors.
- So a `K25` countercoloring, if it exists, is forced onto an extremely rigid extremal surface: each color class must be a 12-regular graph in which every edge lies in exactly 5 monochromatic triangles.
- Self-check: this route does not prove `R(B6, B6) = 25`; it instead shows why naive counting stalls and why a Paley / self-complementary strongly regular configuration is the natural extremal target.

## approach_B
- Construction / extremal route: build the rigid extremal object explicitly.
- The Paley graph `P(25)` on `F_25` is a 12-regular self-complementary graph with strongly regular parameters `(25,12,5,6)`.
- In particular, every red edge of `P(25)` has exactly 5 red common neighbors.
- Because the complement of `P(25)` has the same parameters, every blue edge also has exactly 5 blue common neighbors.
- Therefore the Paley coloring of `K25` contains no monochromatic `B6`.
- Combined with the known upper bound `R(B6, B6) <= 26`, this yields `R(B6, B6) = 26`.
- Self-check: the only load-bearing point is that the chosen 25-vertex graph really has edge codegree 5 in both colors; this is standard from the Paley parameters and is also checked directly by the helper script below.

## lemma_graph
- Lemma 1: A monochromatic `B6` is equivalent to an edge with at least 6 same-color common neighbors.
- Lemma 2: In any red-blue coloring of `K25` with no monochromatic `B6`, the total number of monochromatic triangles is exactly 500, every vertex has red degree 12, and every monochromatic edge has same-color codegree exactly 5.
- Lemma 3: The Paley graph `P(25)` realizes that extremal profile: it is 12-regular, every edge has 5 same-color common neighbors, and the same holds in the complement.
- Lemma 4: Hence `P(25)` gives a monochromatic-book-free coloring of `K25`.
- Conclusion: the known upper bound `R(B6, B6) <= 26` plus Lemma 4 gives the candidate exact theorem `R(B6, B6) = 26`.
- Self-check: the logical chain is short and paper-shaped; the lower construction is the decisive step.

## chosen_plan
- Choose the construction route, but keep the structural argument in front because it explains why the construction is not ad hoc.
- Present the solve as:
  1. rigidity lemma from Goodman-style triangle counting on `K25`;
  2. explicit Paley-25 witness;
  3. immediate exact-value corollary from the known upper bound.
- Decide that minimal code is justified only as witness verification, not as search.
- Self-check: this stays inside the micro-paper lane because the exact value itself is the title theorem and the supporting structure is only one short rigidity lemma plus the witness.

## self_checks
- Statement lock: the target is genuinely the missing `K25` lower construction, not a broader family campaign.
- Definitions: the book condition is translated correctly into same-color edge codegree.
- Approach A: the extremal counting argument is internally consistent and explains why the threshold value 5 is globally sharp on 25 vertices.
- Approach B: the Paley witness is the right object because it exactly matches the forced numerology from Approach A.
- Code decision: any code used here is a bounded verifier for the explicit witness, not a search or optimizer.

## code_used
- Yes, but only minimally and only after the reasoning stage.
- Helper artifact: [paley25_check.py](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/r-b6-b6-diagonal-book-ramsey/paley25_check.py).
- Purpose: verify directly in the explicit `F_25` model that the red graph is 12-regular, every red edge has exactly 5 red common neighbors, every blue edge has exactly 5 blue common neighbors, and thus both monochromatic book sizes are 5.
- Checker summary from the run:
  `degree set = {12}`, `red edge common counts = {5}`, `blue edge common counts = {5}`, `max red book = 5`, `max blue book = 5`.
- Self-check: this is a verifier for a human-readable construction, not a computational discovery step.

## result
- Candidate exact result: `R(B6, B6) = 26`.
- Proof skeleton:
  1. The working packet already supplies `R(B6, B6) <= 26`.
  2. The Paley graph `P(25)` gives a red-blue coloring of `K25`.
  3. Every red edge in `P(25)` has exactly 5 red common neighbors, so red contains no `B6`.
  4. Every blue edge in the complement also has exactly 5 blue common neighbors, so blue contains no `B6`.
  5. Therefore `K25` admits a coloring with no monochromatic `B6`, so `R(B6, B6) >= 26`.
  6. Hence `R(B6, B6) = 26`.
- What extra structure makes the result paper-shaped if the main claim closes:
  the short rigidity lemma from `K25` triangle counting, one explicit Paley witness description, and one compact verifier. That is enough for a tight exact-value note.
- Immediate corollary / remark:
  any monochromatic-`B6`-free coloring of `K25` must already be extremal in the Goodman count and sit on the same rigid `12`-regular / edge-codegree-`5` threshold profile as the Paley witness.
- What part of the argument scales:
  the counting lemma scales to any odd order `4m+1`, forcing a candidate countercoloring at the diagonal threshold onto a balanced regular profile with edge codegree `m-1`.
- What part does not scale automatically:
  existence of a matching extremal graph is special; the Paley construction needs a suitable finite-field order and does not automatically exist for every sum-of-two-squares exception.
- Suggested theorem slice:
  `If a red-blue coloring of K25 avoids monochromatic B6, then each color class is 12-regular and every monochromatic edge has exactly 5 same-color common neighbors.`
- Next parameter shifts worth checking:
  `B7` at order 29, where the same Paley mechanism should be tested against the current family bounds;
  and nearby exceptional orders where `4m+1` is a sum of two squares but the standard shortcut does not decide exactness.
- Package assessment:
  this is no longer merely an isolated witness hunt; if the novelty check passes, it is already close to a paper-shaped exact-value claim rather than a thin instance.
- Self-check: the solve is mathematically coherent, but the verify stage must confirm that the Paley-25 lower construction is not already explicit in the cited literature.

## family_affinity
- Strong.
- This fits the diagonal book Ramsey exact-value family perfectly: a one-step open interval collapses via a compact extremal construction, and the surrounding family context is already prepared by the cited 2025-2026 work.
- Exact sentence for why the instance matters:
  `The case n = 6 is a genuine one-step diagonal gap in the current book Ramsey table, so closing it by an explicit K25 witness would immediately remove a frontier exception rather than add an isolated curiosity.`
- Self-check: this has the right family anchor for a micro-paper and does not require a feeder ladder.

## generalization_signal
- Moderate but real.
- The proof template suggests a broader heuristic: when the diagonal threshold order `4m+1` admits a Paley-type self-complementary construction with edge codegree `m-1`, the exact diagonal book Ramsey value should often jump to `4m+2`.
- I would still keep the current claim instance-first. The paper should not over-claim a family theorem from one Paley witness.
- Self-check: there is reusable structure here, but the publishable statement should remain the exact `B6` closure unless more cases are checked carefully.

## proof_template_reuse
- Reusable template:
  1. convert `B_m` avoidance into a same-color codegree bound `<= m-1`;
  2. use triangle counting at the critical odd order to force regularity and edge-codegree saturation;
  3. realize the saturated profile with a Paley or related self-complementary strongly regular graph;
  4. combine with the existing family upper bound.
- This is a plausible template for other one-step diagonal cases, but only when a matching extremal graph exists.
- Self-check: the template is honest and narrow; it is not a claim that all diagonal book gaps behave this way.

## candidate_theorem_slice
- Main candidate theorem:
  `R(B6, B6) = 26.`
- Supporting slice:
  `Any red-blue coloring of K25 with no monochromatic B6 has exactly 500 monochromatic triangles, each color class is 12-regular, and every monochromatic edge has exactly 5 same-color common neighbors.`
- Self-check: the slice is theorem-shaped and could survive even if verify later finds the exact-value observation was already implicit elsewhere.

## smallest_param_shift_to_test
- First shift: `R(B7, B7)`, because `4*7+1 = 29` is again a Paley order and should reveal whether the same lower-bound mechanism is already decisive there.
- Second shift: the nearest exceptional order where `4m+1` is a sum of two squares but not obviously covered by a prime-power Paley construction, because that is where this proof template would actually be stress-tested.
- Self-check: these shifts probe reuse of the method, not a drift into a broader campaign.

## why_this_is_or_is_not_publishable
- If the novelty check passes, this is publishable in the micro-paper lane.
- Why: the exact title theorem is already in hand, it closes a bounded one-step frontier gap, the proof package is short, and the remaining editorial work is cheap.
- Whether a successful solve would already be 70-90% of a paper:
  yes, about `0.84` is still the right estimate.
- Minimal remaining packaging work:
  cite the upper bound source cleanly, present the Paley-25 coloring and the rigidity lemma in polished prose, include the verifier as a supplementary artifact, and make sure the exact lower construction was not already stated in prior work.
- If verify finds the Paley-25 step was already explicitly known, then this solve is still mathematically real but too thin for the micro-paper lane because it would collapse to rediscovery rather than a frontier closure.
- Self-check: publication readiness here is dominated by novelty verification, not by mathematical incompleteness.

## paper_shape_support
- Proposed note title:
  `The Exact Value of R(B6, B6)`.
- Core paper ingredients now visible:
  1. one exact-value theorem;
  2. one short extremal-structure lemma on `K25`;
  3. one explicit Paley witness;
  4. one immediate rigidity remark.
- Natural boundary remark:
  this solve uses a very special extremal graph at order 25, so the narrative stays compact instead of drifting into a general theory of all diagonal book Ramsey exceptions.
- Self-check: the packet is paper-shaped without inventing extra side-goals.

## boundary_remark
- The solve cleanly distinguishes two layers:
  the global counting layer forces any `K25` countercoloring onto the exact threshold profile, and the local construction layer is then discharged by one explicit self-complementary graph.
- Boundary of the method:
  the counting argument alone does not decide existence, and the Paley witness is special to the availability of a 25-vertex field-based construction.
- So the current result is closer to a paper-shaped exact instance than to a family theorem.
- Self-check: this is the right scope discipline for the micro-paper objective.

## likely_failure_points
- The largest risk is bibliographic rather than mathematical: the Paley-25 lower construction may already be implicit or explicit in the cited family papers despite not being surfaced in the current selection packet.
- The second risk is a notation mismatch: verify should confirm that the source papers use the same `B6` convention as the common-neighbor-on-an-edge formulation used here.
- The third risk is presentational: if the paper packet cannot cleanly explain why the Paley lower construction was missed by the current interval statement, the novelty claim weakens.
- Self-check: no hidden search dependence remains; the main uncertainty is verify-stage prior-art checking.

## what_verify_should_check
- Check that the cited 2025 upper bound is exactly `R(B6, B6) <= 26` in the same book notation.
- Check whether the 2025 paper, the 2026 Wesley paper, or earlier book Ramsey papers already mention the 25-vertex Paley graph as a lower-bound witness for `B6`.
- Check whether the exact-value consequence `R(B6, B6) = 26` is already stated, even in a remark or table note.
- Check the helper script independently and confirm that the listed square set in `F_25` reproduces the claimed codegree profile.
- If the exact-value claim survives that audit, the publication packet should foreground the rigidity lemma plus the explicit Paley witness as the minimal paper-shaped support.

## verify_rediscovery
- PASS 1 establishes rediscovery.
- The bounded web audit found that William J. Wesley, `Lower bounds for book Ramsey numbers` (Discrete Mathematics 349(5) (2026), 114913), explicitly restates the older Rousseau-Sheehan diagonal theorem:
  `R(B_n, B_n) = 4n + 2` whenever `q = 4n + 1` is a prime power.
- Substituting `n = 6` gives `q = 25`, and `25 = 5^2` is a prime power, so the exact instance follows immediately:
  `R(B6, B6) = 26`.
- The active selection packet and working packet treated the case as still open on the basis of the 2025 EJC interval `25 <= R(B6, B6) <= 26`, but that packet missed the older family theorem already covering this instance.
- Verdict from PASS 1:
  the exact intended statement is already solved in prior art, not merely heuristically implied.

## verify_faithfulness
- The solver's stated theorem `R(B6, B6) = 26` matches the intended statement exactly.
- The local definition of `B6` as the 6-page book graph, equivalently an edge with at least 6 same-color common neighbors, is faithful to the standard book-graph notation used in the cited book Ramsey literature.
- There is no quantifier drift or proxy-statement drift inside the mathematics.
- The failure is status drift:
  the packet framed a previously solved instance as a frontier gap.

## verify_proof
- No first incorrect mathematical step was found in the local rederivation.
- The Paley-25 witness argument is mathematically coherent:
  a monochromatic `B6` is equivalent to an edge with at least 6 same-color common neighbors, and the displayed Paley coloring has same-color edge codegree exactly 5 in both colors.
- Combined with the known upper bound `R(B6, B6) <= 26`, the local proof does establish `R(B6, B6) = 26`.
- However, as a verification verdict this is a correct reproof of a known theorem, not a frontier closure.

## verify_adversarial
- Reran the checker at [paley25_check.py](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/r-b6-b6-diagonal-book-ramsey/paley25_check.py).
- Output reproduced the claimed witness profile exactly:
  `degree_set = [12]`,
  `red_edge_common_counts = [5]`,
  `blue_edge_common_counts = [5]`,
  `max_red_book = 5`,
  `max_blue_book = 5`.
- The explicit square set printed by the script matches the square set recorded in the solve notes.
- I did not find a computational mismatch between the code artifact and the prose claim.

## verify_theorem_worthiness
- Exactness: yes, but only as a rederived exact theorem.
- Novelty: no. The exact instance is already settled by the older Rousseau-Sheehan prime-power diagonal theorem and is restated in Wesley (2026).
- Reproducibility: yes. The local witness is explicit and the checker reruns cleanly.
- Lean readiness: no. Lean would not be the shortest path to a sealed publication packet because the publication bottleneck is not rigor but prior-art status.
- Paper leverage: none for the frontier micro-paper lane once rediscovery is accounted for.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  No. The title theorem is already occupied by prior art.
- What percentage of the paper would one solve already provide?
  Effectively `0%` for a new frontier note, because novelty is already gone.
- What title theorem is actually visible?
  `R(B6, B6) = 26`, but only as a known theorem being rederived.
- What part of the argument scales?
  The same-color codegree formulation and Paley witness mechanism fit the older prime-power diagonal book-Ramsey family.
- What part clearly does not?
  The claim that this instance is a new one-step frontier closure does not survive scrutiny.
- Best honest publication status:
  `REDISCOVERY`, not `INSTANCE_ONLY` and not a live `SLICE_CANDIDATE`.

## verify_verdict
- `REDISCOVERY`

## minimal_repair_if_any
- No mathematical repair is required for the local witness.
- The conservative repair is bibliographic and status-facing:
  relabel the run as `REDISCOVERY`, preserve the explicit Paley witness and checker as a known-instance artifact, and stop the publication path for this slug.
