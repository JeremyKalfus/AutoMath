# Solve Record: The Half-Set Density Threshold in Triangle-Free Graphs

## statement_lock
- Active slug: `density-turan-beta-half-two`.
- Active title: `Is beta(1/2,2) equal to 1/50 in the density version of Turan's theorem?`
- Exact intended statement for this run: either prove that every triangle-free `n`-vertex graph with every `n/2`-vertex subset spanning more than `n^2/50` edges contains a triangle, or give a triangle-free construction showing the sharp threshold is larger than `1/50`.
- Working theorem-facing slice isolated here: among triangle-free graphs admitting a homomorphism to `C_5`, the minimum induced edge count over `n/2`-vertex subsets is at most `n^2/50`, with equality only for the balanced `C_5` blow-up.
- Title theorem if the main conjecture closed: `The Half-Set Density Threshold in Triangle-Free Graphs`.
- If the main conjecture closed honestly, it would already be about `78%` of a short paper: the title theorem, the lower-bound example, and the main structural reduction would already be in place.

## definitions
- Let `m_{1/2}(G)` denote the minimum of `e(G[S])` over all `S ⊆ V(G)` with `|S| = n/2`. The target constant `beta(1/2,2)` is the supremum of `m_{1/2}(G) / n^2` over triangle-free `n`-vertex graphs, in the usual asymptotic sense.
- I treat the problem in the clean divisible setting `n` even, and for blow-up calculations I assume the part sizes are divisible enough to ignore rounding. Any final paper would need one short rounding paragraph.
- A `C_5` blow-up means a partition `V(G) = V_1 ∪ ... ∪ V_5` into independent sets with edges only between consecutive parts mod `5`.
- Weighted notation: `a_i = |V_i|/n`, `x_i = |S ∩ V_i|/n`, so `a_i ≥ 0`, `x_i ∈ [0,a_i]`, `Σ a_i = 1`, `Σ x_i = 1/2`, and `e(G[S]) / n^2 = Σ x_i x_{i+1}`.
- Ambiguities still present in the packet:
  - exact finite-`n` normalization versus asymptotic `beta`;
  - whether equality at `1/50` should be stated with floor/ceiling half-sets for odd `n`;
  - whether Petersen blow-ups belong in the same sharpness statement or only as parallel lower-bound witnesses.

## approach_A
- Structural / invariant route: force a near-extremal triangle-free graph into a `C_5`-type partition, then solve the induced weighted optimization problem exactly on that partition.
- The immediate useful subproblem is already clean: for a fixed `C_5` blow-up with weights `a_1,...,a_5`, compute
  `min { Σ x_i x_{i+1} : 0 ≤ x_i ≤ a_i, Σ x_i = 1/2 }`.
- If this subproblem has maximum value `1/50`, attained only by `a_i = 1/5`, then any future global proof can focus on reducing arbitrary extremal graphs to the `C_5`-homomorphic family.
- Self-check: this route matches the transfer kit and keeps the paper packet honest, because it attacks the named lower-bound family directly instead of drifting into unrelated triangle-free structure.

## approach_B
- Construction / extremal / contradiction route: look for a triangle-free family beating the `C_5` lower bound, with Petersen-type or other non-`C_5` blow-ups as the first plausible candidates.
- The useful contradiction question is narrower: can any unbalanced `C_5` blow-up beat the balanced one for the half-set minimum? If not, the known `C_5` witness is at least internally rigid.
- This route can also fail productively: proving that every unbalanced `C_5` blow-up has a half-set with induced density strictly below `1/50` eliminates a whole class of fake counterexamples.
- Self-check: this does not resolve the global conjecture, but it gives a real theorem slice instead of a vague heuristic.

## lemma_graph
- Lemma 1: In a `C_5` blow-up with weights `a_i`, if `a_i + a_{i+2} ≥ 1/2` for some `i`, then there is a half-set with `0` induced edges.
- Lemma 2: If `a_i + a_{i+2} < 1/2` for all `i`, then for each `i` the half-set taking all of `V_i`, all of `V_{i+2}`, and `r_i n` vertices from `V_{i+4}`, where `r_i = 1/2 - a_i - a_{i+2}`, is feasible and has induced density `a_i r_i`.
- Lemma 3: `Σ_i a_i r_i = 1/2 - Σ_i a_i^2 - Σ_i a_i a_{i+2}`.
- Lemma 4: With `s_i = a_i + a_{i+2}`, one has `Σ_i s_i = 2` and
  `Σ_i s_i^2 = 2 Σ_i a_i^2 + 2 Σ_i a_i a_{i+2} ≥ 4/5`
  by Cauchy, hence `Σ_i a_i^2 + Σ_i a_i a_{i+2} ≥ 2/5`.
- Conclusion: `Σ_i a_i r_i ≤ 1/10`, so some `i` satisfies `a_i r_i ≤ 1/50`.
- Equality analysis: equality forces all `s_i = 2/5`, hence all `a_i = 1/5`.
- Self-check: every step is elementary and uses only the fixed `C_5`-blow-up model.

## chosen_plan
- Choose approach A, but only for the theorem slice that I can close rigorously inside this run.
- Prove the exact optimization statement for `C_5` blow-ups.
- Record explicitly why this is not yet the full conjecture: the missing reduction is from an arbitrary triangle-free graph to a `C_5`-homomorphic or stability-controlled structure.
- Paper-shaped extra structure if the main claim closes: a stability reduction showing that any graph near the `1/50` threshold must be close to a balanced `C_5` blow-up or the parallel Petersen-type witness family.

## self_checks
- After statement lock: the intended global claim stayed fixed; I did not switch to a broader or easier lane.
- After the two approaches: one is structural and one is construction-based, as required.
- After the lemma graph: the slice is theorem-shaped and directly supports the target lower-bound family.
- After the chosen proof: the result is rigorous within the `C_5`-homomorphic family but does not yet justify a global `EXACT` or even a global `CANDIDATE`.

## code_used
- None. The `C_5`-blow-up slice closes by hand, and no checker or search was needed.

## result
- Rigorous theorem slice obtained:
  - Let `G` be a triangle-free graph admitting a homomorphism to `C_5`, with blow-up part weights `a_1,...,a_5`.
  - Then there exists a vertex subset `S` of size `n/2` with
    `e(G[S]) ≤ n^2 / 50`.
  - Equality in the weighted optimization is attained only by the balanced `C_5` blow-up `a_1 = ... = a_5 = 1/5`.
- Proof:
  - If `a_i + a_{i+2} ≥ 1/2` for some `i`, choose `S` inside `V_i ∪ V_{i+2}`. These parts are anticomplete, so `e(G[S]) = 0`.
  - Otherwise `a_i + a_{i+2} < 1/2` for every `i`. Define `r_i = 1/2 - a_i - a_{i+2}`.
  - Since `a_{i+1} + a_{i+3} < 1/2` as well, we have
    `a_{i+4} = 1 - a_i - a_{i+1} - a_{i+2} - a_{i+3} > 1/2 - a_i - a_{i+2} = r_i`,
    so it is feasible to choose `S_i` consisting of all of `V_i`, all of `V_{i+2}`, and `r_i n` vertices from `V_{i+4}`.
  - The only edges inside `S_i` lie between `V_i` and the chosen vertices from `V_{i+4}`, so
    `e(G[S_i]) / n^2 = a_i r_i`.
  - Summing gives
    `Σ_i a_i r_i = 1/2 - Σ_i a_i^2 - Σ_i a_i a_{i+2}`.
  - With `s_i = a_i + a_{i+2}`, Cauchy yields
    `4/5 = 5 (2/5)^2 ≤ Σ_i s_i^2 = 2 Σ_i a_i^2 + 2 Σ_i a_i a_{i+2}`.
    Hence `Σ_i a_i^2 + Σ_i a_i a_{i+2} ≥ 2/5`, so `Σ_i a_i r_i ≤ 1/10`.
  - Therefore some `i` satisfies `a_i r_i ≤ 1/50`, giving a half-set with induced density at most `1/50`.
  - Equality in the Cauchy step forces all `s_i = 2/5`. Subtracting consecutive equations gives `a_i = a_{i+2}` for all `i`, hence all `a_i = 1/5`.
- Self-check:
  - The proof only certifies the `C_5`-homomorphic slice.
  - I did not prove that every extremal triangle-free graph lies in this slice.
  - I also did not analyze Petersen blow-ups here.

## family_affinity
- Very strong affinity with the canonical lower-bound family: the result identifies the balanced `C_5` blow-up as the unique optimizer inside the `C_5`-homomorphic class.
- Moderate affinity with a future stability proof: the slice says any exact global proof must explain why no non-`C_5` family can outperform this balanced witness.
- Weak current coverage of the Petersen side of the packet: that family remains outside this run's closed argument.

## generalization_signal
- The proof template should extend to other fixed odd-cycle blow-up families where half-set minimizers can be expressed with one-edge-support templates.
- The most immediate generalization signal is not a parameter change in `alpha`; it is a family change:
  - optimize the same half-set functional on Petersen blow-ups;
  - then compare the two canonical lower-bound families on equal footing.
- A second signal is a stability statement: if a triangle-free graph is already known to be close to a `C_5` blow-up, the same averaging proof should convert closeness into a quantitative gap below `1/50` unless the blow-up is nearly balanced.

## proof_template_reuse
- Reusable template:
  - pick a small homomorphic target family;
  - write the induced-density objective as a weighted polynomial in part masses;
  - exhibit a handful of explicit half-set templates;
  - average the resulting candidate values;
  - use a quadratic inequality to force the sharp constant and identify equality.
- This is a realistic reusable proof shell for Petersen blow-ups and for any later stability reduction that compresses a near-extremal graph into five coarse parts.

## candidate_theorem_slice
- Candidate theorem slice:
  - `Among triangle-free graphs admitting a homomorphism to C_5, the maximum possible value of m_{1/2}(G) / n^2 is 1/50, attained uniquely by the balanced blow-up of C_5.`
- This is the smallest honest theorem slice produced in this run.
- What scales:
  - the weighted-template optimization on a fixed five-part cycle structure;
  - the equality analysis showing balanced parts are forced.
- What does not scale yet:
  - reduction from arbitrary triangle-free graphs to the `C_5`-homomorphic family;
  - comparison with Petersen-type constructions.

## smallest_param_shift_to_test
- First parameter/family shift to test: the identical half-set optimization on weighted Petersen blow-ups.
- Second shift: keep the `C_5`-homomorphic family fixed but perturb `alpha` from `1/2` to nearby values and see whether the same one-edge-support templates still determine the sharp weighted optimum.
- These are the two shifts most likely to say whether the current package is merely an instance or the front face of a broader theorem.

## why_this_is_or_is_not_publishable
- This run is not yet publishable as the claimed micro-paper result because the global conjecture `beta(1/2,2) = 1/50` remains open here.
- The current package is not just a witness computation, though: it is a clean theorem slice that isolates the exact optimum inside the main conjectured extremal family.
- If the missing global reduction were supplied, the remaining packaging work would be small:
  - one background section fixing notation and prior lower bounds;
  - one theorem section stating the exact threshold and equality/stability;
  - one short section placing the `C_5` and Petersen witnesses.
- Honest assessment:
  - a successful full solve would already be `70-90%` of a paper;
  - the current result is still too thin for the micro-paper lane by itself;
  - it is best treated as a strong structural side result feeding the intended title theorem.

## paper_shape_support
- What extra structure would make this paper-shaped if the main claim closes:
  - a reduction proving that every extremal or near-extremal triangle-free graph is close to one of the known lower-bound families;
  - or a direct argument excluding every non-`C_5` / non-Petersen candidate above `1/50`.
- Immediate natural corollary from the current slice:
  - any unbalanced `C_5` blow-up has a half-set with induced density strictly below `1/50`.
- Exact sentence for why the instance matters:
  - `The balanced C_5 witness is not merely a lower-bound example; inside the full C_5-homomorphic family it is the unique sharp optimizer for the half-set density functional.`
- Current package status:
  - closer to a theorem-shaped claim than to a bare instance;
  - still not paper-ready without the global exclusion or stability step.

## boundary_remark
- Boundary remark: the slice sharply separates two tasks.
  - The weighted extremal optimization over the obvious `C_5` family is now elementary and closed.
  - The actual difficulty is global: showing that no triangle-free graph outside the known extremal families can keep every half-set above `n^2/50`.
- This makes the next proof burden much clearer than before the run.

## likely_failure_points
- The main missing bridge is structural, not algebraic: I do not know how to force a general near-extremal triangle-free graph into the `C_5`-homomorphic model.
- Petersen blow-ups may require a separate weighted optimization, and a sharper global proof might need both families simultaneously.
- The finite-`n` rounding details are straightforward but not yet written carefully.
- If the literature already contains the `C_5`-homomorphic optimization as a standard exercise, this slice would still be useful internally but less novel as a publication component.

## what_verify_should_check
- Check the algebra in the identity `Σ_i a_i r_i = 1/2 - Σ_i a_i^2 - Σ_i a_i a_{i+2}`.
- Check the feasibility implication `a_{i+4} ≥ r_i` under the standing assumption `a_j + a_{j+2} < 1/2` for all `j`.
- Check the equality analysis: `s_i = 2/5` for all `i` really forces `a_1 = ... = a_5 = 1/5`.
- Check whether the same weighted optimization is already explicitly recorded in the prior art around `beta(1/2,2)` or in expositions of `C_5` blow-ups.
- Check whether the Petersen family admits the same sharp constant or creates a distinct equality branch.
