# Solve Record: The Exact Value of R(B7, B7)

## statement_lock
- Active slug: `r-b7-b7-diagonal-book-ramsey`.
- Active title: `Determine the exact value of R(B7, B7)`.
- Working interpretation from the active packet: `B7` is the 7-page book graph, so a monochromatic `B7` is an edge contained in at least 7 monochromatic triangles of one color.
- Exact title theorem targeted here: `R(B7, B7) = 30`.
- Solve posture: construct a `K29` coloring with no monochromatic `B7`, then pair it with the packet's cited upper bound `R(B7, B7) <= 30`.

## definitions
- For a red-blue coloring of `K_n`, let `G_R` be the red graph.
- A monochromatic `B7` in red is an edge `uv` of `G_R` with at least 7 common red neighbors, equivalently at least 7 red triangles through `uv`.
- The same translation holds for blue in the complement graph.
- Paley candidate used below: vertices `F_29`, with `xy` red iff `x-y` is a nonzero quadratic residue modulo `29`; blue is the complement.
- Ambiguities that must be verified later:
  - the source notation really uses `B7` for the 7-page book;
  - the cited upper bound `R(B7, B7) <= 30` is correctly transferred into the packet;
  - no hidden convention shifts the book index by one.

## approach_A
- Structural / invariant route: count monochromatic triangles.
- If a coloring of `K_29` has no monochromatic `B7`, then every monochromatic edge lies in at most 6 monochromatic triangles.
- Therefore the total number `M` of monochromatic triangles satisfies
  - `3M <= 6 * binom(29,2)`,
  - hence `M <= 2 * 406 = 812`.
- Goodman gives the sharp lower bound `M >= 812` for every 2-coloring of `K_29`.
- So any hypothetical `K_29` witness must hit equality everywhere:
  - it must be extremal for Goodman;
  - every monochromatic edge must lie in exactly 6 monochromatic triangles.
- That points directly at a conference / Paley type extremal object rather than an ad hoc irregular coloring.
- Self-check: this route does not yet decide existence, but it narrows the search to a very rigid equality case.

## approach_B
- Construction / extremal route: test the Paley graph on `29` vertices.
- Standard Paley parameters for `q = 29` are
  - `v = 29`,
  - `k = (29-1)/2 = 14`,
  - `lambda = (29-5)/4 = 6`,
  - `mu = (29-1)/4 = 7`.
- Hence in the red Paley graph:
  - every red edge has exactly 6 common red neighbors;
  - every red nonedge has exactly 7 common red neighbors.
- The complement of `P(29)` is isomorphic to `P(29)`, so every blue edge also has exactly 6 common blue neighbors.
- Therefore neither color contains an edge with 7 same-color common neighbors, so the coloring contains no monochromatic `B7`.
- This gives a direct `K_29` witness and therefore `R(B7, B7) >= 30`.
- Self-check: this is the decisive path if the packet's notation and upper bound are correct.

## lemma_graph
- Lemma 1: A monochromatic `B7` is equivalent to a monochromatic edge lying in at least 7 monochromatic triangles.
- Lemma 2: In a `B7`-free 2-coloring of `K_29`, the total number of monochromatic triangles is at most `812`.
- Lemma 3: Goodman forces at least `812` monochromatic triangles in every 2-coloring of `K_29`.
- Lemma 4: So any `K_29` witness must be an equality case for both Lemma 2 and Lemma 3.
- Lemma 5: The Paley graph `P(29)` is such an equality-case witness; every monochromatic edge has exactly 6 same-color common neighbors.
- Closure: `K_29` witness plus the packet's upper bound `R(B7, B7) <= 30` yields the candidate theorem `R(B7, B7) = 30`.

## chosen_plan
- Choose the constructive Paley path.
- Reason:
  - it produces the lower-bound witness directly;
  - it matches the extremal triangle-count equality picture;
  - it yields a compact certificate, which is ideal for a micro-paper packet.
- What extra structure makes this paper-shaped if the main claim closes:
  - the explicit `K_29` witness;
  - one paragraph explaining why the packet's upper bound already closes the gap;
  - one short extremal-count remark showing the witness sits exactly at the Goodman threshold.
- Self-check: this is already 80-90% of a short paper if verification confirms the source-side upper bound and notation.

## self_checks
- Step 1, statement lock: interpreted `B7` as 7 pages, not 7 total vertices.
- Step 2, invariant route: the upper bound `M <= 812` is correct because each monochromatic triangle contributes to 3 monochromatic edges.
- Step 3, extremal route: Paley parameter arithmetic gives `lambda = 6`, exactly the threshold needed to avoid `B7`.
- Step 4, complement check: because `P(29)` is self-complementary, blue edges satisfy the same page bound.
- Step 5, closure check: the exact-value conclusion uses the packet's cited upper bound `R(B7, B7) <= 30`; without that citation, this record alone proves the lower bound `R(B7, B7) >= 30`.

## code_used
- Minimal code used: one inline Python witness verification, no persistent script.
- Verification output:
  - red degree set `[14]`;
  - red edge red-common set `[6]`;
  - red nonedge red-common set `[7]`;
  - blue edge blue-common set `[6]`;
  - maximum monochromatic book size `6`.
- Self-check: the computation matches the Paley parameter claim exactly and supports the human proof sketch.

## result
- Strong solve-stage candidate: `R(B7, B7) = 30`.
- Proof/disproof status inside solve:
  - lower-bound side is explicit: color `K_29` by the Paley graph `P(29)` on `F_29`;
  - each red edge lies in exactly 6 red triangles, so no red `B7`;
  - each blue edge lies in exactly 6 blue triangles, so no blue `B7`;
  - thus `K_29` avoids monochromatic `B7`, giving `R(B7, B7) >= 30`.
- Paired with the packet's cited upper bound `R(B7, B7) <= 30`, this closes to the exact candidate value `30`.
- Immediate corollary / boundary remark:
  - the Paley witness is extremal for the monochromatic-triangle count on `K_29`, so the one-step gap is closed by a very compact certificate rather than a search-heavy argument.
- What part of the argument scales:
  - the Paley / conference construction scales to other orders `q = 4t + 1` with the same `lambda = t-1` mechanism.
- What part does not:
  - the closure to an exact Ramsey value still needs an external upper bound at the matching order.
- Theorem slice suggested:
  - a family-level lower-bound slice via Paley graphs for diagonal book Ramsey numbers.
- Most useful next parameter shifts:
  - test the same construction at `q = 25` for the nearby `B6` case;
  - test it at `q = 41` for the `B10` case.
- Package assessment:
  - this is closer to a paper-shaped exact theorem than to a mere instance witness, because the witness and the upper-bound citation together already produce the title theorem.

## family_affinity
- Very strong.
- This fits the standard diagonal book Ramsey lane where conference / Paley objects supply sharp lower witnesses and recent family literature supplies near-matching upper bounds.

## generalization_signal
- Strong lower-bound generalization signal.
- For prime powers `q = 4t + 1`, the Paley graph `P(q)` has `lambda = t-1`, so it avoids `B_t` in one color and, by self-complementarity, in both colors.
- That suggests the reusable family slice `R(B_t, B_t) >= 4t + 2` whenever a Paley order `q = 4t + 1` is available.

## proof_template_reuse
- Reusable template:
  - use a local triangle-count or literature upper bound to reduce the gap to one step;
  - realize the lower witness by a Paley / conference graph;
  - certify the common-neighbor counts directly.
- This template is cheap, exact, and publication-friendly when the family upper bound is already known.

## candidate_theorem_slice
- Candidate theorem slice: the Paley graph on `29` vertices gives a `B7`-free red-blue coloring of `K_29`, so `R(B7, B7) >= 30`.
- If the packet's upper bound `R(B7, B7) <= 30` is confirmed verbatim, the slice upgrades immediately to the exact theorem `R(B7, B7) = 30`.

## smallest_param_shift_to_test
- Smallest nearby parameter shift worth testing: `B6` via `P(25)`.
- Second high-yield shift: `B10` via `P(41)`.
- Reason:
  - both preserve the same Paley lower-witness mechanism;
  - they would show whether this is just an isolated instance closure or a more systematic exactness pattern.

## why_this_is_or_is_not_publishable
- If the packet's upper bound and notation verify cleanly, this is publishable.
- Honest estimate: a verified solve here is about `0.85` to `0.90` of a short paper.
- Why:
  - the exact title theorem is already visible: `The Exact Value of R(B7, B7)`;
  - the lower witness is explicit and compact;
  - the remaining packaging is only the upper-bound citation, a short extremal-context paragraph, and a tiny certificate appendix.
- If verification finds a notation mismatch, then the current packet is too thin for publication in its present form and drops back to a family-construction note rather than an exact closure.

## paper_shape_support
- Title theorem: `R(B7, B7) = 30`.
- Why this matters:
  - it closes a one-step frontier gap in a currently active family;
  - the proof packet is short and certificate-friendly.
- Minimal remaining packaging work:
  - verify the packet's upper-bound citation line by line;
  - state the Paley construction explicitly;
  - include the common-neighbor parameter check and one extremal-triangle remark.
- Natural corollary / remark:
  - the extremal `K_29` witness is a conference-type equality case for the Goodman triangle bound.
- Micro-paper lane assessment:
  - not too thin if the upper bound verifies;
  - too thin only if the exact-value closure fails and the output collapses to a bare lower-bound witness.

## boundary_remark
- Boundary remark: the solve is construction-heavy rather than upper-bound-heavy.
- The Paley witness cleanly explains why `29` can still fail, but it does not by itself strengthen the family upper theory.
- So the instance matters because it closes a one-step gap cheaply, not because it opens a broad new method on the upper-bound side.

## likely_failure_points
- The active packet may have a notation shift or transcription issue around `B7`.
- The cited source upper bound `R(B7, B7) <= 30` may need a more careful restatement than the packet currently gives.
- A referee-quality version should cite the Paley strongly-regular parameters explicitly, not just rely on the computational check.
- If the packet's literature summary already overlooked the `K_29` Paley witness, verification must resolve that discrepancy before publication claims are made.

## what_verify_should_check
- Confirm from the cited source that `B7` really means the 7-page book graph.
- Confirm the packet's upper bound `R(B7, B7) <= 30`.
- Confirm the Paley-29 construction is legitimate in the exact notation used by the source.
- Check whether the lower-bound witness is already standard / published for this exact instance, since the solve stage did not browse.
- If those checks pass, this should advance as an exact candidate with a compact publication packet.

## verify_rediscovery
- PASS 1 used a bounded web audit on the exact notation `R(B7,B7)`, alternate notation `R(B_7,B_7)`, the cited EJC source, same-source theorem checks, and recent family-context hits.
- The active packet's canonical-source line is bibliographically wrong: Electronic Journal of Combinatorics `32(4)`, `#P4.64` is Lidicky, McKinley, Pfender, and Van Overberghe, *Small Ramsey Numbers for Books, Wheels, and Generalizations*, not Pchelintsev, Rath, and Angeltveit.
- That EJC paper's Theorem 1 gives `4n+1 <= R(B_n,B_n) <= 4n+2` for `4 <= n <= 21`, so for `n = 7` it already yields `29 <= R(B7,B7) <= 30`.
- The bounded search also surfaced Wesley's *Lower bounds for book Ramsey numbers*, which states the family lower bound `R(B_n,B_n) >= 4n+2` when `q = 4n+1` is a prime power, using Paley graphs with each adjacent pair sharing exactly `n-1` common neighbors.
- Substituting `n = 7` and `q = 29` gives `R(B7,B7) >= 30`. Combined with the published upper bound `R(B7,B7) <= 30`, the exact value `R(B7,B7) = 30` is already directly implied in prior art.
- Rediscovery is therefore established within budget. This run cannot remain frontier-positive.

## verify_faithfulness
- The solver's mathematical target matches the intended statement: determine the exact diagonal book Ramsey value for the 7-page book graph.
- The solve record's interpretation of `B7` as an edge contained in at least `7` same-color triangles is faithful to the standard book-graph meaning used by the cited literature.
- There is no theorem-scope drift in the mathematical claim itself.
- There is, however, source drift in the packet metadata:
  - the canonical source attribution is wrong;
  - the line claiming that public sources stop at `29 <= R(B7,B7) <= 30` is stale once Wesley's family lower bound is included.
- Verdict on faithfulness: mathematically faithful claim, but unfaithful literature/status framing.

## verify_proof
- First incorrect step found: none in the lower-bound argument.
- The Paley-29 computation uses the standard strongly regular parameters `k = 14`, `lambda = 6`, `mu = 7`, so every red edge has exactly `6` red common neighbors.
- Because the complement of `P(29)` is isomorphic to `P(29)`, every blue edge also has exactly `6` blue common neighbors.
- That is enough to certify a `K_29` coloring with no monochromatic `B7`, hence `R(B7,B7) >= 30`.
- The closure to the exact value uses an external published upper bound rather than a new upper-bound argument. So the solve-stage proof is correct as a rederivation, but it is not novel.

## verify_adversarial
- Re-ran an independent inline Python check of the Paley coloring on `29` vertices.
- Output reproduced the expected witness invariants:
  - red degree set `[14]`;
  - red edge common-neighbor set `[6]`;
  - blue edge common-neighbor set `[6]`;
  - maximum monochromatic book size `6`.
- No monochromatic edge with `7` same-color common neighbors appeared, so the claimed `K_29` witness survived adversarial checking.
- No computation-based defect was found; the failure mode here is novelty, not correctness.

## verify_theorem_worthiness
- Exactness: yes, the exact value `R(B7,B7) = 30` is the right title theorem.
- Novelty: no. The exact value is already directly implied in the literature, so this is not a frontier solve.
- Reproducibility: high. The Paley witness is compact and easy to recheck.
- Lean readiness: no. Formalization would only certify a rediscovery and is not the shortest remaining path to a publishable frontier packet.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? Not in the active micro-paper lane, because the theorem is already implied by prior art.
- What percentage of the paper would one solve already provide? As a frontier micro-paper, effectively `0.00`; the missing ingredient is not proof polish but novelty.
- What title theorem is actually visible? `R(B7,B7) = 30`.
- What part of the argument scales? The Paley / conference lower-bound mechanism scales across diagonal book parameters with `q = 4n+1` prime power.
- What part clearly does not? The exact closure only works where an independent matching upper bound already exists, and publication leverage collapses once the exact instance is already implied.
- Best honest publication status: `REDISCOVERY`, not `INSTANCE_ONLY`, because the exact claim is already recoverable from prior art rather than merely too thin.

## verify_verdict
- `verify_verdict = "REDISCOVERY"`
- `classification = "REDISCOVERY"`
- `publication_status = "REDISCOVERY"`
- `lean_ready = false`
- `lean_packet_seal = false`
- `next_action = "archive_as_rediscovery"`

## minimal_repair_if_any
- No mathematical repair is needed for the Paley lower-bound witness.
- The only conservative repair is bibliographic/status cleanup:
  - correct the packet's canonical-source attribution for EJC `32(4)`, `#P4.64`;
  - replace the stale "current public sources stop at `29 <= R(B7,B7) <= 30`" line with the rediscovery conclusion that the exact value is already directly implied by the published interval plus Wesley's family lower bound.
