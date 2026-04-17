# Solve Record: The Elementary Abelian (729,273,102)-Difference-Set Problem

- slug: `abelian-difference-set-729-273-102-group-3-3-3-3-3-3`
- working_packet: `artifacts/abelian-difference-set-729-273-102-group-3-3-3-3-3-3/working_packet.md`

## statement_lock
Determine whether the elementary abelian group C_3^6 admits a (729,273,102)-difference set.

Equivalent locked target: if `D subset C_3^6` has size `273`, must every nonprincipal character sum `chi(D)` satisfy `|chi(D)|^2 = 171`; the solve target is to show such a set exists or that this character equation cannot be realized in `C_3^6`.

Intended title theorem if closed: `The elementary abelian group C_3^6 admits no (729,273,102)-difference set.` This is the sharper theorem-facing branch suggested by the current obstruction route.

## definitions
- Write `G = C_3^6` additively, identified with `F_3^6`.
- A `(v,k,lambda)`-difference set in `G` is a subset `D` of size `k` such that every nonzero `g in G` has exactly `lambda` representations as `d_1-d_2` with `d_i in D`.
- For a character `chi : G -> <omega>` with `omega^3 = 1`, the standard abelian difference-set identity gives
  `chi(D) overline{chi(D)} = k-lambda = 171`
  for every nonprincipal `chi`.
- Because `G` has exponent `3`, every `chi(D)` lies in the Eisenstein integers `Z[omega]`.
- Write an index-3 quotient as `G/H ~= F_3`, and for the three cosets of `H` write counts `(x_0,x_1,x_2)`. Then `x_0+x_1+x_2 = 273` and for the nontrivial character on `G/H`,
  `x_0 + x_1 omega + x_2 omega^2 = chi(D)`.

## approach_A
Structural / invariant route.

1. Use the character equation in `Z[omega]`:
   `chi(D) overline{chi(D)} = 171 = 3^2 * 19`.
2. Since `3 = -omega (1-omega)^2` ramifies in `Z[omega]`, every nonprincipal `chi(D)` must be divisible by `3` in `Z[omega]`.
3. For an index-3 quotient this forces
   `x_0-x_2` and `x_1-x_2` to be multiples of `3`, so the three coset counts are congruent mod `3`.
4. Solving the norm equation with that divisibility gives the unique index-3 line-sum multiset
   `{84,90,99}`.
5. Pass to a codimension-2 quotient `G/K ~= F_3^2`. Its nine coset counts form a `3 x 3` array. Every affine line in each of the four directions must then have sum multiset `{84,90,99}`.
6. Try to show no such array exists. If successful, this is a clean nonexistence proof with a short quotient-obstruction narrative.

Why this route is attractive: it attacks the exact named open case using only the elementary-abelian structure and the `19`-part / `3`-part arithmetic already highlighted in the working packet.

## approach_B
Construction / contradiction route.

1. Treat a putative difference set as an indicator function `f : F_3^6 -> {0,1}` with Fourier transform of constant nontrivial modulus `sqrt(171)`.
2. Push `f` to small quotients `F_3`, `F_3^2`, and possibly `F_3^3`, viewing each quotient as an integer-valued function with the same nontrivial Fourier modulus.
3. Attempt to assemble compatible small-quotient data. If the quotient data remain consistent, this route would suggest a lifting template toward a construction; if they fail quickly, it becomes a contradiction argument.
4. This is weaker as a proof route because it is closer to bounded search, but it is still theorem-facing: any obstruction found already speaks directly to `C_3^6` rather than to an auxiliary optimization problem.

## lemma_graph
- Lemma 1. For every nonprincipal `chi` of `G`, `chi(D) in Z[omega]` and `|chi(D)|^2 = 171`.
- Lemma 2. Every nonprincipal `chi(D)` is divisible by `3` in `Z[omega]`.
  Self-check: this uses only the factorization of `171` in `Z[omega]`.
- Lemma 3. For every index-3 subgroup `H <= G`, the three coset counts of `D` modulo `H` are exactly `{84,90,99}`.
  Self-check: this is the first exact theorem slice; it already rules out arbitrary hyperplane intersections.
- Lemma 4. For every codimension-2 subgroup `K <= G`, the induced `3 x 3` coset-count array on `G/K ~= F_3^2` has each affine parallel class summing to `{84,90,99}`.
- Target contradiction. No integer `3 x 3` array with entries in `[0,81]` has that four-direction line-sum behavior.

Proof skeleton: `difference-set characters -> Eisenstein divisibility -> forced hyperplane sums -> codimension-2 quotient consistency -> contradiction`.

## chosen_plan
Choose approach A.

Reason:
- It stays reasoning-first and keeps code optional rather than primary.
- The hyperplane multiset `{84,90,99}` is exact and cheap to derive.
- A contradiction in `F_3^2` would already be a short, title-theorem-level argument, with only light exposition left for a paper packet.

Immediate next step:
- Preserve this reasoning state in `status.json`.
- Then run one tiny bounded consistency check for the `3 x 3` quotient array. No SAT / ILP; just direct enumeration of the finitely many allowed direction patterns.

Outcome of chosen-plan test:
- the codimension-2 obstruction does **not** close;
- there exists a compatible `F_3^2` quotient array, so this branch stops at a theorem slice rather than a contradiction.
- explicit witness array for one admissible codimension-2 quotient:

  `29 28 33`
  `23 28 33`
  `38 28 33`

  Its row sums, column sums, and both diagonal-direction parallel classes are all permutations of `{84,90,99}`.

## self_checks
- Statement lock check: the target remains the exact `(729,273,102)` case in `C_3^6`; no family drift.
- Publication-shape check: a clean nonexistence proof from quotient arithmetic would already look like the title theorem of a short note, comfortably in the `70-90% of a paper` band.
- Risk check: this failure mode occurred. Compatible codimension-2 quotient arrays exist, so the `F_3^2` reduction alone is not decisive.
- Post-check: the solve artifact is still theorem-facing because the hyperplane-intersection lemma is exact, but the current package is not yet the title theorem.

## code_used
Yes, but only as a bounded checker / falsifier after the reasoning stage.

Code actually used:
- exhaustive line-sum search over all row/column/diagonal permutations of `{84,90,99}` for a `3 x 3` array with entries in `[0,81]`;
- independent Fourier-model cross-check on `F_3^2`.
- a short MacWilliams check on the induced putative ternary projective code weight spectrum.

What the code established:
- the first attempted contradiction was false;
- a compatible codimension-2 quotient witness exists, so any proof must use structure beyond the hyperplane-sum lemma alone.
- the induced weight spectrum `1 + 728 z^174 + 728 z^183 + 728 z^189 + 2 z^273` is at least MacWilliams-admissible in low degrees, so there is no immediate projective-code contradiction from the hyperplane data alone.

## result
Partial result only; no solve yet.

Rigorous pieces now on hand:
- every nonprincipal character value must be a multiple of `3` in `Z[omega]`;
- therefore every index-3 quotient has coset-count multiset `{84,90,99}`;
- codimension-2 quotients must realize `3 x 3` arrays with all four affine line classes summing to `{84,90,99}`;
- such arrays do exist, so the first low-dimensional quotient obstruction fails;
- the corresponding hyperplane spectrum is also not killed by the first MacWilliams checks.

One explicit admissible `F_3^2` quotient witness is

`29 28 33`
`23 28 33`
`38 28 33`

with line sums
- rows: `90,84,99`
- columns: `90,84,99`
- `i+j = t`: `90,84,99`
- `i+2j = t`: `90,99,84`

This means the current best honest claim is not the full nonexistence theorem. The exact theorem closure remains open inside this solve attempt.

## family_affinity
Strong. The surviving theorem slice is native to elementary abelian `3`-groups and uses exactly the quotient/character structure that distinguishes this family from generic abelian cases.

## generalization_signal
Moderate. The `3`-divisibility plus forced hyperplane-sum method should extend to other elementary-abelian `3`-group parameter sets with `3^2` dividing `n`. What does **not** automatically scale is the hoped-for codimension-2 contradiction: this case already admits compatible `F_3^2` data.

## proof_template_reuse
Reusable template:
`character norm -> ramified-prime divisibility -> forced quotient counts -> low-dimensional quotient obstruction`.

What scales:
- the first three arrows, especially the Eisenstein-divisibility step and the forced `{84,90,99}` hyperplane pattern.

What does not scale automatically:
- a codimension-2 contradiction. This exact case already shows that the `F_3^2` shadow can look perfectly consistent.

## candidate_theorem_slice
Candidate slice:
If a `(729,273,102)`-difference set exists in `C_3^6`, then every affine hyperplane meets it in exactly `84`, `90`, or `99` points, one value in each coset of every index-3 quotient.

## smallest_param_shift_to_test
Best next parameter shifts, if the main contradiction stalls:
- keep the same parameter set but inspect codimension-3 quotients `G/K ~= F_3^3`, where the extra direction classes may finally overdetermine the quotient data;
- compare with the nearest elementary-abelian residual cases sharing the same `3`-adic divisibility pattern, to see whether `{84,90,99}` is exceptional or generic.

## why_this_is_or_is_not_publishable
If the exact case closes, the result is still clearly in the `70-90% of a paper` band: the title theorem would be the existence or nonexistence statement for `C_3^6`, and the remaining packaging would just be brief family context plus a polished proof.

At the current stage the package is still too thin for the micro-paper lane. The hyperplane-sum lemma is real and theorem-facing, but it is still an instance-level structural slice rather than the title theorem.

## paper_shape_support
What would make the result paper-shaped if the main claim closes:
- the exact nonexistence theorem for `C_3^6`,
- the hyperplane-intersection lemma `{84,90,99}`,
- one decisive obstruction beyond codimension `2` or a construction showing realizability,
- one short remark that this resolves the smallest open elementary-abelian case listed by Gordon.

Minimal remaining packaging work after a successful solve:
- polish the Eisenstein-divisibility lemma,
- write the decisive obstruction or construction cleanly,
- add a one-paragraph family-context introduction and one boundary remark.

## boundary_remark
Natural boundary remark if the obstruction works:
the proof is exploiting the elementary-abelian `3`-group structure, especially the ramification of `3` in `Z[omega]`; it would not automatically settle non-elementary abelian groups with the same parameters.

Current boundary remark:
the hyperplane-intersection lemma is genuinely structural, but the codimension-2 witness array shows that low-dimensional quotient consistency is not by itself enough to distinguish existence from nonexistence here.

Additional boundary remark:
the obvious projective-code obstruction is also unavailable at this resolution; the forced weight spectrum passes the first MacWilliams nonnegativity checks, so any code-theoretic contradiction would need finer structure than the raw hyperplane counts.

## likely_failure_points
- The `3 x 3` quotient array does exist, so the codimension-2 test is exhausted.
- Even if `F_3^2` is impossible, I still need to state clearly why every codimension-2 quotient inherits the same nontrivial Fourier modulus.
- If the contradiction requires heavier search in `F_3^3` or beyond, the solve risks sliding away from the clean micro-paper lane.
- A construction route is not yet justified: the consistent `F_3^2` shadow is far weaker than a full difference-set witness.
- The hyperplane data may simply be too coarse; both quotient consistency and low-degree MacWilliams checks allow it.

## what_verify_should_check
- Recheck the Eisenstein arithmetic: every nonprincipal character value really is divisible by `3`, not merely by `(1-omega)`.
- Recheck that `{84,90,99}` is the unique index-3 quotient multiset up to order.
- Recheck the bounded code outputs: confirm the displayed `F_3^2` array really satisfies all four direction classes, and confirm the failed obstruction was recorded correctly rather than silently ignored.
- Later, verification should also do the bounded prior-art check for any known hyperplane-intersection or quotient obstruction theorem in this exact case.

## verify_rediscovery
- PASS 1 used a bounded web sweep on the exact tuple `(729,273,102)`, the alternate notation `[3,3,3,3,3,3]`, Gordon's La Jolla Difference Set Repository slides, and same-source theorem/example/corollary style checks.
- The sweep recovered Gordon's 2019 slide deck and older Gordon-Schmidt survey context, both still treating this elementary-abelian case as residual/open; no later direct existence or nonexistence theorem for `C_3^6` at `(729,273,102)` surfaced within budget.
- Conclusion: no rediscovery was established in PASS 1, so the run does not fail as `REDISCOVERY`.

## verify_faithfulness
- The intended statement is the exact existence/nonexistence question for a `(729,273,102)`-difference set in `C_3^6`.
- The solve artifact does not settle that statement. Its strongest claimed output is a structural slice about index-3 quotient counts.
- Even that slice is overstated. The record claims the quotient-count multiset is uniquely `{84,90,99}`; a direct bounded enumeration of all integer triples with
  `x_0+x_1+x_2 = 273`,
  `x_0^2+x_1^2+x_2^2-x_0x_1-x_1x_2-x_2x_0 = 171`,
  and `x_0 ≡ x_1 ≡ x_2 (mod 3)`
  yields two sorted possibilities:
  `{84,90,99}` and `{83,92,98}`.
- So the current artifact is not faithful to the stated theorem slice. The strongest honest output is a weaker nearby statement, so the run should be classified as `VARIANT`, not as a closure of the selected problem.

## verify_proof
- First incorrect step found: `approach_A`, step 4 / `Lemma 3`, where the record says that solving the norm equation gives the unique index-3 line-sum multiset `{84,90,99}`.
- This uniqueness claim is false. The alternative multiset `{83,92,98}` also satisfies the same sum, norm, and mod-`3` divisibility constraints.
- Because the advertised candidate slice and the downstream codimension-2 discussion both rely on that uniqueness, the proof as written does not establish the stated hyperplane theorem.
- No later step repairs this gap. The exact selected problem therefore remains open within this artifact.

## verify_adversarial
- No reusable checker file was present in the artifact directory, so PASS 4 reran the arithmetic directly with a short bounded script.
- That script confirmed two things:
  1. the displayed `3 x 3` witness array
     `29 28 33 / 23 28 33 / 38 28 33`
     really has all row, column, and both diagonal-direction parallel-class sums equal to a permutation of `{84,90,99}`;
  2. the same script also finds the second valid hyperplane multiset `{83,92,98}`, which breaks the uniqueness claim used to launch the codimension-2 branch.
- So the adversarial check does not rescue the proof. It sharpens the failure point.

## verify_theorem_worthiness
- Exactness: not exact. The selected theorem is unsolved here.
- Novelty: bounded PASS 1 did not uncover a prior-art settlement of the exact target, but the weaker surviving slice has unclear standalone novelty.
- Reproducibility: high for the arithmetic check; the flaw is easy to reproduce.
- Lean readiness: no. Formalizing the current weakened slice would be a detour because the remaining gap is mathematical, not formal.
- Paper leverage: low for the verified content now on hand.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- Percentage of the paper one solve already provides: the current verified output is only about `0.18` of a plausible note, not the `0.84` target imagined for a full closure.
- Title theorem actually visible: a weak necessary-condition variant, namely that any putative `(729,273,102)` difference set in `C_3^6` would have index-3 quotient counts in one of two multisets, `{84,90,99}` or `{83,92,98}`.
- What scales: the Eisenstein-divisibility setup and the passage from character arithmetic to quotient-count restrictions.
- What clearly does not: the uniqueness claim, the advertised hyperplane theorem `{84,90,99}` alone, and any codimension-2 obstruction that depends on forcing only that branch.
- Best honest publication status: `NONE`. The surviving variant is too thin and too publication-distant for the micro-paper lane.

## verify_verdict
- `verify_verdict = CRITICAL_FLAW`
- `classification = VARIANT`
- `publication_status = NONE`
- `lean_ready = false`
- `lean_packet_seal = false`
- `next_action = revisit the quotient analysis with the corrected two-branch hyperplane count lemma before making any further obstruction claims`

## minimal_repair_if_any
- Conservative repair available: replace the false uniqueness claim `{84,90,99}` with the weaker disjunction `{84,90,99}` or `{83,92,98}` for index-3 quotient counts.
- This is only a repair of the local theorem slice, not of the selected problem. After that repair, the codimension-2 and code-theoretic discussion must be treated as branch-specific exploratory work rather than as verified support for a decisive obstruction.

## publication_prior_art_audit
- On 2026-04-15 I ran the bounded publication-audit web pass on the exact tuple `(729,273,102)`, the group notation `C_3^6`, and the alternate notation `[3,3,3,3,3,3]`.
- Canonical source check: Gordon's 2019 La Jolla Difference Set Repository slides ask whether all non-cyclic elementary-abelian difference sets are Hadamard or Paley and list `729 273 102 [3,3,3,3,3,3]` among the "Small Open Cases." Within that source, this exact case appears as an open-question entry, not as a theorem, proposition, example, corollary, observation, or sufficient-condition settlement.
- Outside-source status check: the Gordon-Schmidt multiplier survey still lists `729 273 102 exp(G) <= 27` in its table of open difference-set parameters, so the bounded pass did not surface a direct later settlement of the selected problem.
- I also ran one narrow follow-up search on the weakened quotient-slice language and did not surface a directly matching published statement. That is not a novelty proof; it only means this bounded pass found no explicit prior-art match for the local two-branch lemma.
- Prior-art verdict: no rediscovery of the exact intended statement surfaced in this bounded audit, but the surviving slice has uncertain standalone novelty and should be treated conservatively.

## publication_statement_faithfulness
- The selected theorem remains the exact existence/nonexistence problem for a `(729,273,102)`-difference set in `C_3^6`.
- The current artifact does not settle that theorem. The strongest faithful output now on hand is only a necessary-condition slice about index-3 quotient counts.
- The source-faithful publication framing is therefore: "structural restriction for the open case," not "settlement of Gordon's smallest open elementary-abelian case."
- Any title, abstract, or status language claiming that the open case has been resolved would be false on the current record.

## publication_theorem_worthiness
- Stronger than "here is an example"? Yes, but only modestly: the surviving claim is a universal structural restriction on every putative difference set with these parameters.
- Real theorem slice? Yes, in the bounded current sense: for any putative `(729,273,102)`-difference set in `C_3^6`, every index-3 quotient has sorted coset-count multiset either `{83,92,98}` or `{84,90,99}`.
- Title-theorem strength: weak. This slice does not decide existence, does not force a sharp obstruction, and does not yet support a compelling theorem-level corollary.
- Structural or merely instance-specific? Structural in method, but still tightly parameter-locked in both values and narrative leverage.
- Referee test: this would not convincingly survive "what is the theorem?" as a one-shot note, because the answer is still a preparatory lemma rather than a publishable title theorem.

## publication_publishability
- This packet is not close to a publishable micro-paper in its current state.
- The attractive publication story belonged to the full closure of Gordon's named open case. Once that closure failed, the remaining slice supplies only a small fraction of the intended note.
- Honest fraction estimate: about `0.20` of a plausible paper packet, not the pre-audit `0.84`.
- The remaining gap is not genuinely small. A paper-shaped packet would still need a decisive obstruction, a construction, or a much sharper theorem slice with clear narrative leverage.
- Under the one-shot rules, this should be moved aside rather than automatically expanded into a broader codimension-3 or search-heavy program.

## publication_packet_audit
- Best honest publication-facing classification: `SLICE_EXACT`, not `PAPER_READY`.
- Reason: the two-branch index-3 quotient lemma is an exact local slice in the current bounded sense, but it is too thin, too publication-distant, and too novelty-uncertain to carry the micro-paper lane.
- `publication_packet_quality = weak`
- `proof_artifacts_preserved = true`
- `human_ready = false`
- Lean would not change the publication verdict here; it would only formalize a weak slice.

## micro_paper_audit
- Is the strongest honest claim stronger than "here is an example"? Yes, but only as a small necessary-condition lemma.
- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `0.20`.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a real theorem slice, but not a title theorem.
- Is the proof structural or merely instance-specific? Structural, but parameter-locked and narratively thin.
- Would this survive a referee asking "what is the theorem?" Not as a one-shot paper packet.
- Is the claim still too dependent on hand-picked small cases? The method is not hand-picked-case driven, but the resulting claim is still too local to carry publication leverage on its own.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? It only looked attractive because a full solve would have been paper-ready; from the current slice to a paper, the remaining gap is large.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Only optional polish / later archival formalization.

## strongest_honest_claim
If `D subset C_3^6` is a putative `(729,273,102)`-difference set, then for every index-3 quotient of `C_3^6` the sorted coset-count multiset is either `{83,92,98}` or `{84,90,99}`.

## paper_title_hint
Index-3 Quotient Restrictions for the Elementary Abelian `(729,273,102)`-Difference-Set Problem

## next_action
- Move this packet aside from the active micro-paper lane unless a same-lane decisive obstruction or construction is already in hand.
- Preserve the two-branch quotient lemma and the failed `{84,90,99}` uniqueness obstruction as reusable artifacts.
- Do not automatically expand into a broader codimension-3 theorem program; that would exceed the current one-shot publication scope.
