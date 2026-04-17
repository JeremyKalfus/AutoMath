# Solve Record: The Exact Value of R(B22, B22)

- slug: `r-b22-b22-diagonal-book-ramsey`
- working_packet: `artifacts/r-b22-b22-diagonal-book-ramsey/working_packet.md`

## statement_lock
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B22.

## definitions
- I interpret `B22` as the book graph with one spine edge and 22 pages, i.e. 22 triangles sharing a common edge.
- In a 2-coloring of `K_n`, a monochromatic `B22` in color `c` is equivalent to the existence of a color-`c` edge `uv` with at least 22 common color-`c` neighbors.
- The active packet already supplies the frontier interval `89 <= R(B22, B22) <= 90`; solve only needs to close the missing direction without web use.
- Conventions needing verification later:
  - the packet's notation `B22` matches the standard "22 pages" convention rather than total-vertex indexing;
  - the upper bound `R(B22, B22) <= 90` is correctly sourced and not conditional on extra hypotheses.

## approach_A
Structural / invariant route.

- Recast the problem as a common-neighborhood bound on each monochromatic spine edge.
- For an upper-bound style argument on `K_90`, one would try to show that every 2-coloring has some edge whose same-color codegree is at least 22.
- A natural invariant is the codegree profile of each color class: avoiding `B22` forces every red edge and every blue edge to have same-color codegree at most 21.
- This is theorem-facing, but from the packet alone I do not have a short local derivation of the `n = 90` forcing step. So this route presently depends on the cited literature interval rather than a fresh self-contained proof.
- Self-check: this route is honest but not the best local solve path, because reproducing the upper bound from scratch would likely exceed the micro-paper solve budget.

## approach_B
Construction / extremal route.

- Try to realize an explicit coloring of `K_89` with no monochromatic `B22`.
- The working packet says diagonal lower bounds in this family use Paley-type constructions. Order 89 is immediately suggestive because `89` is prime and `89 == 1 mod 4`.
- The Paley graph `P(89)` is a self-complementary strongly regular graph with parameters `(v, k, lambda, mu) = (89, 44, 21, 22)`.
- If red is `P(89)` and blue is its complement, then every red edge has exactly 21 red common neighbors, so red contains no `B22`.
- For the blue graph, which is the complement of a self-complementary strongly regular graph, each blue edge also has exactly `v - 2 - 2k + mu = 89 - 2 - 88 + 22 = 21` blue common neighbors, so blue also contains no `B22`.
- Therefore there is a 2-coloring of `K_89` with no monochromatic `B22`, giving `R(B22, B22) >= 90`.
- Self-check: the only load-bearing inputs are the standard Paley parameters and the complement codegree formula; both are routine to verify.

## lemma_graph
1. A color-`c` copy of `B22` is equivalent to a color-`c` edge with at least 22 common color-`c` neighbors.
2. `89` admits a Paley graph because `89` is a prime congruent to `1 mod 4`.
3. `P(89)` has strongly regular parameters `(89, 44, 21, 22)`.
4. Hence every edge of `P(89)` lies in exactly 21 red triangles, so the red graph avoids `B22`.
5. The complement of `P(89)` has adjacent-pair common-neighbor count `89 - 2 - 2*44 + 22 = 21`, so the blue graph also avoids `B22`.
6. Thus `K_89` has a red-blue coloring with no monochromatic `B22`, yielding `R(B22, B22) >= 90`.
7. Combined with the packet's sourced upper bound `R(B22, B22) <= 90`, conclude `R(B22, B22) = 90`.

## chosen_plan
Choose approach B.

- It directly targets the missing endpoint by exploiting the exact order `89`.
- It produces the decisive lower-bound witness in theorem form, not just a search artifact.
- It keeps the result paper-shaped: once the literature upper bound is verified, the title theorem is immediate.
- Self-check: this is not a silent fallback. It is exactly the packet's recommended first attack, specialized to the Paley witness that matches the one-step gap.

## self_checks
- Statement lock check: I am solving the exact endpoint question `89` versus `90`, not a weaker witness-only claim.
- Definition check: `B22` needs 22 same-color common neighbors on a spine edge; having exactly 21 common neighbors is safe.
- Arithmetic check: for the complement, `89 - 2 - 2*44 + 22 = 21`.
- Logic check: lower witness on 89 plus sourced upper bound on 90 is sufficient to conclude the exact value.
- Scope check: I am not claiming Lean completeness or a web-checked rediscovery verdict inside solve.

## code_used
No code used.

- Reason: the Paley witness is closed-form and the parameter arithmetic is small enough to check by hand.
- Minimal-code decision: not needed for this attempt.

## result
Candidate exact closure:

- The natural title theorem is: `R(B22, B22) = 90`.
- Proof sketch: color `K_89` by the Paley graph `P(89)` and its complement. Since `P(89)` is strongly regular with parameters `(89, 44, 21, 22)`, every red edge has exactly 21 red common neighbors, so red contains no `B22`. Its complement has the same adjacent-pair codegree count 21, so blue also contains no `B22`. Therefore `R(B22, B22) >= 90`. The packet already supplies the upper bound `R(B22, B22) <= 90`. Hence `R(B22, B22) = 90`.
- This would already be about 80% of a micro-paper if verification confirms the packet upper bound and the standard Paley parameter citation.
- Minimal remaining packaging work: state the Paley construction explicitly, cite the standard strongly regular parameters, cite the existing upper bound, and add one short placement paragraph in the diagonal-book sequence.
- Immediate remark: the lower-bound side is not an opaque search certificate; it comes from a named algebraic construction, which makes the note cleaner than a brute-force witness.
- Self-check: the only unresolved dependence is external verification of the literature upper bound and notation alignment.

## family_affinity
Strong.

- This argument sits exactly in the standard diagonal book Ramsey family.
- The proof template is the expected Paley / strongly-regular lower-bound architecture already highlighted in the working packet.
- If verified, the result is not just an isolated coloring but a clean endpoint closure in a named sequence.

## generalization_signal
Moderate.

- What scales: whenever a diagonal book instance sits one step above a Paley order `q = 4m + 1` with Paley edge codegree `m - 1`, the same construction gives `R(B_m, B_m) >= q + 1 = 4m + 2`.
- What does not automatically scale: exact closure still needs an independently known or provable upper bound at `4m + 2`; the Paley argument only supplies the lower side.
- Most relevant next parameter shifts are the neighboring diagonal cases whose open interval is also one step and whose witness order matches a Paley or related self-complementary strongly regular graph.

## proof_template_reuse
Reusable template:

1. Translate `B_m` avoidance into a same-color codegree cap of `m - 1` on every monochromatic edge.
2. Choose a self-complementary strongly regular graph with adjacent-pair codegree exactly `m - 1`.
3. Use the graph and its complement as the two colors on `K_v`.
4. Infer `R(B_m, B_m) >= v + 1`.
5. Close the endpoint only when an upper bound of `v + 1` is already available.

For this instance, `m = 22` and `v = 89`.

## candidate_theorem_slice
Exact theorem-facing slice:

- `P(89)` and its complement give a 2-coloring of `K_89` with no monochromatic `B22`.
- Therefore, together with the sourced upper bound `R(B22, B22) <= 90`, the endpoint closes as `R(B22, B22) = 90`.
- This is already closer to a paper-shaped claim than to a mere instance witness, because the endpoint itself is the advertised title theorem.

## smallest_param_shift_to_test
Best next shifts after verification:

- Recheck the nearest diagonal cases where a one-step interval may also align with a Paley-type order.
- Recheck whether the same codegree computation explains the lower bounds for the nearest larger or smaller diagonal book numbers in the literature sequence.

For this run, no further shift is needed before verification because the active endpoint appears closed on the current packet.

## why_this_is_or_is_not_publishable
If verified, this is publishable in the micro-paper lane.

- It would supply the exact title theorem `R(B22, B22) = 90`.
- The solve-to-paper fraction is plausibly in the 70-90% band: the mathematics is the endpoint closure itself, and the remaining work is mostly packaging and verification.
- The package is not too thin for the lane because the claim closes a named one-step frontier gap, not just an arbitrary instance.
- The main residual risk is novelty / status hygiene rather than mathematical shape: verify must confirm that this exact closure is not already explicit in the cited literature and that the upper bound is correctly inherited.

## paper_shape_support
What makes the result paper-shaped if the main claim closes:

- A clean title theorem: `R(B22, B22) = 90`.
- A short proof split into two recognizable ingredients: existing upper bound plus explicit Paley lower-bound witness.
- One natural supporting remark: the lower bound is algebraic and self-complementary, so the obstruction is structurally legible rather than search-heavy.
- Minimal remaining packaging work:
  - cite the upper-bound source precisely;
  - spell out the Paley(89) construction and its parameters in one lemma;
  - add one sentence situating `n = 22` in the diagonal book family.

## boundary_remark
Boundary remark / corollary.

- The lower-bound mechanism scales only on the witness side: a self-complementary strongly regular graph with adjacent-pair codegree `m - 1` automatically avoids `B_m` in both colors.
- What does not scale for free is the matching upper bound.
- Natural corollary-style sentence: the order-89 Paley coloring is a sharp obstruction to any attempt to lower the diagonal threshold for `B22` below 90.

## likely_failure_points
- The packet upper bound `R(B22, B22) <= 90` may require a precise citation or hidden condition that is not reproduced locally.
- The notation `B22` must be checked carefully against the source conventions.
- Verification should confirm the exact strongly regular parameters used for `P(89)` and that the complement codegree computation matches the blue-book count convention.
- Publication risk remains if the exact closure is already noted explicitly in the modern literature despite the packet's open-status claim.

## what_verify_should_check
- Confirm from the cited sources that the public frontier before this run was exactly `89 <= R(B22, B22) <= 90`.
- Confirm that `B22` means 22 pages, so the forbidden threshold is 22 same-color common neighbors.
- Confirm the standard Paley graph facts for order 89: existence, self-complementarity, and strongly regular parameters `(89, 44, 21, 22)`.
- Check whether the cited literature already uses the Paley(89) lower witness explicitly; if so, verify whether the exact closure was still open or already settled.
- If all checks pass, the verify stage should treat this as a candidate exact closure with publication status trending toward `PAPER_READY`.

## verify_rediscovery
Rediscovery established.

- The canonical modern source cited in the packet, Wesley's "Lower bounds for book Ramsey numbers", explicitly restates Rousseau-Sheehan Theorem 1 for the diagonal case: whenever `q = 4n + 1` is a prime power, one has `R(B_n, B_n) = 4n + 2`.
- For the active instance, `n = 22` gives `q = 89`, and `89` is prime, hence a prime power. Therefore the exact value `R(B22, B22) = 90` is already implied by that quoted classical theorem.
- The same source also explains that the lower bound comes from the Paley graph of order `q`, with adjacent pairs having exactly `n - 1` common neighbors. That is the same witness mechanism used in the local solve record.
- Because the exact intended statement is already settled in prior art, this run must be classified as `REDISCOVERY`, not a frontier closure.

## verify_faithfulness
The local solve record is faithful to the intended statement, but not to the actual literature status.

- The solved claim matches the intended theorem exactly: determine `R(B22, B22)`.
- The notation is aligned: `B22` is the book with 22 pages, so forbidding a monochromatic `B22` is equivalent to requiring every monochromatic edge to have at most 21 same-color common neighbors.
- There is no wrong-theorem drift or quantifier drift in the combinatorial statement.
- The faithfulness failure is status drift: the packet and solve record treat `89 <= R(B22, B22) <= 90` as the live frontier, but the canonical source itself points to an older exact theorem that already settles this instance.

## verify_proof
No first mathematical error found in the local derivation of the value; the failure is novelty, not the witness arithmetic.

- The Paley-based lower-bound argument is standard and internally coherent:
  - `89` is prime and `89 ≡ 1 (mod 4)`, so the Paley graph `P(89)` exists and is self-complementary.
  - With parameters `(89, 44, 21, 22)`, each red edge has exactly 21 red common neighbors, so no red `B22` appears.
  - In the complement, each blue edge also has 21 blue common neighbors, so no blue `B22` appears.
- Thus the witness correctly gives `R(B22, B22) >= 90`.
- Once one imports the known theorem giving the matching upper bound in this prime-power case, the conclusion `R(B22, B22) = 90` is mathematically sound.
- The first decisive failure is not a proof step but the novelty premise: the result is already known.

## verify_adversarial
Adversarial check did not break the local arithmetic, but it did break the frontier claim.

- No checker or code artifact exists in the candidate directory, so there was nothing computational to rerun.
- The hand arithmetic survives basic adversarial scrutiny: the threshold for a monochromatic `B22` is 22 common neighbors, while the Paley and complementary codegrees are 21.
- The literature check is fatal to the claim of novelty: the same prime-power exact theorem already covers `n = 22`.
- So the construction is a valid rederivation of a known case, not a new micro-paper result.

## verify_theorem_worthiness
Assessment after the five-pass verify sweep:

- Exactness: yes, the theorem statement itself is exact.
- Novelty: no; this is a rediscovery of a previously settled prime-power diagonal book Ramsey case.
- Reproducibility: high; the Paley witness is explicit and the theorem dependency is standard.
- Lean readiness: no. Formalizing this would certify a known theorem, not shorten the path to a new publication packet.
- Paper leverage: effectively none for the active frontier objective, because the exact title theorem is already in the literature.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No, not as a new result; it would at best be a rederivation of known material.
- What percentage of a new paper would one solve already provide? `0%` for frontier novelty, because the publication bottleneck is not proof completion but prior-art status.
- What title theorem is actually visible? `R(B22, B22) = 90`, but only as an already known theorem.
- What part of the argument scales? The Paley / self-complementary strongly regular witness template for lower bounds in diagonal book Ramsey problems.
- What part clearly does not? The novelty claim and publication packet; those do not scale past the rediscovery barrier.
- Best honest publication status: `REDISCOVERY`, not `INSTANCE_ONLY`, `SLICE_CANDIDATE`, or `NONE`.

## verify_verdict
`REDISCOVERY`

- `classification = REDISCOVERY`
- `publication_status = REDISCOVERY`
- `lean_ready = false`
- `lean_packet_seal = false`
- `next_action = archive_as_rediscovery`

## minimal_repair_if_any
Only a classification repair is justified.

- Conservative repair: relabel the run as an independent rederivation of a known exact theorem and archive it as `REDISCOVERY`.
- No tiny local patch can restore frontier novelty or micro-paper eligibility for this exact statement.
