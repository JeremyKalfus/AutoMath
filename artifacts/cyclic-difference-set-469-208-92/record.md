# Solve Record: The Cyclic (469,208,92) Difference-Set Case

- slug: `cyclic-difference-set-469-208-92`
- working_packet: `artifacts/cyclic-difference-set-469-208-92/working_packet.md`

## statement_lock
Determine whether the cyclic group C_469 admits a (469,208,92)-difference set.

## definitions
- Work in additive notation in `G = Z/469Z`.
- A `(469,208,92)` cyclic difference set means a subset `D ⊂ G` with `|D| = 208` such that every nonzero element of `G` occurs exactly `92` times as an ordered difference `d - d'` with `d,d' ∈ D`.
- The standard group-ring identity is `D D^{(-1)} = 116 + 92 G`, where `116 = k - λ`.
- For a divisor `w | 469`, write the contraction of `D` to `Z/wZ` as multiplicities `b_r = #{d ∈ D : d ≡ r mod w}`.
- The exact title theorem, if the nonexistence route closes, is: `The cyclic group C_469 does not admit a (469,208,92)-difference set.`
- A successful solve would already be about `70-90%` of a paper because the literature packet already provides the frontier framing and the residual-case narrative; the remaining packaging work would be a short source-faithful introduction and a cleaned proof presentation.
- Immediate ambiguity to keep explicit: I am not assuming any multiplier theorem unless it is derived or encoded directly in a contracted equation.

## approach_A
- Structural / invariant route: contract mod `7`.
- Let `b_0,...,b_6` be the residue-class counts mod `7`. Projecting the group-ring identity from `Z/469Z` to `Z/7Z` gives
  `Σ b_r = 208`,
  `Σ b_r^2 = 116 + 92·67 = 6280`,
  `Σ b_r b_{r-j} = 92·67 = 6164` for every nonzero `j mod 7`.
- Center at the nearest integer average by writing `b_r = 30 + e_r`. Then
  `Σ e_r = -2`,
  `Σ e_r^2 = 100`,
  `Σ e_r e_{r-j} = -16` for every nonzero `j mod 7`.
- This is a tiny exact periodic-autocorrelation problem on seven integers. If it has no solution, nonexistence follows immediately and cleanly.
- If it does have solutions, the surviving mod-`7` patterns still give a sharply constrained skeleton for any full difference set.

## approach_B
- Construction / extremal / contradiction route: contract mod `67`.
- Let `a_0,...,a_66` be the residue-class counts mod `67`. Since each class has size `7`, we have `0 ≤ a_r ≤ 7`.
- Projecting to `Z/67Z` gives
  `Σ a_r = 208`,
  `Σ a_r^2 = 116 + 92·7 = 760`,
  `Σ a_r a_{r-j} = 92·7 = 644` for every nonzero `j mod 67`.
- Center with `a_r = 3 + f_r`. Then
  `Σ f_r = 7`,
  `Σ f_r^2 = 115`,
  `Σ f_r f_{r-j} = -1` for every nonzero `j mod 67`.
- This says a hypothetical solution induces a very rigid `67`-periodic integer sequence with values in `{-3,-2,-1,0,1,2,3,4}` and perfectly flat off-zero periodic autocorrelation.
- If approach A does not already kill the case, this quotient is the next paper-shaped obstruction surface. Any extra orbit structure would only sharpen it.

## lemma_graph
- Lemma 1: a cyclic `(469,208,92)` difference set projects to exact contracted coefficient equations for each divisor `w | 469`.
- Lemma 2: for `w = 7`, those equations are equivalent to the seven-variable centered system `Σ e_r = -2`, `Σ e_r^2 = 100`, and `Σ e_r e_{r-j} = -16` for `j ≠ 0`.
- Lemma 3: if the mod-`7` system is infeasible over integers, then no cyclic `(469,208,92)` difference set exists.
- Lemma 4: if the mod-`7` system is feasible, then any global solution must also satisfy the mod-`67` centered system `Σ f_r = 7`, `Σ f_r^2 = 115`, `Σ f_r f_{r-j} = -1`.
- Lemma 5: the smallest publishable theorem slice suggested by this setup is a contracted nonexistence theorem, ideally already at `w = 7`.

## chosen_plan
- First path tested: exact mod-`7` contraction.
- Outcome: the seven-variable centered system is feasible, so mod `7` alone does not force nonexistence.
- Revised best path: use the mod-`67` contraction together with the prime `2 | n`.
- Reason: on `67`th roots in characteristic `2`, inversion lies in the same Frobenius orbit because `2^33 ≡ -1 (mod 67)`. That turns the product equation `A(α)A(α^{-1}) = 116` into a vanishing statement on every nontrivial `67`th root, which is much sharper than the raw integer autocorrelation equations.

## self_checks
- Check 1: `k - λ = 208 - 92 = 116`.
- Check 2: for `w = 7`, the projected identity coefficient is `116 + 92·(469/7) = 116 + 92·67 = 6280`.
- Check 3: with `b_r = 30 + e_r`, `Σ e_r = 208 - 7·30 = -2` and `Σ e_r^2 = 6280 - 60·208 + 7·900 = 100`.
- Check 4: for nonzero shifts mod `7`, `Σ e_r e_{r-j} = 6164 - 30·208 - 30·208 + 7·900 = -16`.
- Check 5: for `w = 67`, `Σ f_r = 208 - 67·3 = 7`, `Σ f_r^2 = 760 - 6·208 + 67·9 = 115`, and the off-zero centered autocorrelation is `644 - 3·208 - 3·208 + 67·9 = -1`.
- Check 6: the exact bounded search over the mod-`7` centered system finds `168` integer solutions, so that contraction is a real filter but not yet a contradiction.
- Check 7: `ord_67(2) = 66` and `2^33 ≡ -1 (mod 67)`, so inverse and Frobenius-conjugate coincide on nontrivial `67`th roots in characteristic `2`.

## code_used
- Used only bounded exact arithmetic and bounded exhaustive search.
- Experiment 1: exhaustive search of the seven-variable mod-`7` centered system; result `168` solutions.
- Experiment 2: exact order checks for `2` and `29` modulo `7`, `67`, and `469`.
- No SAT / ILP / CP-SAT / brute-force search on the full `469`-point set was used.

## result
- Main exact slice obtained:
- Let `A(x) = Σ_{r=0}^{66} a_r x^r`, where `a_r` is the number of elements of a hypothetical difference set in the residue class `r mod 67`.
- The contraction identity gives `A(α)A(α^{-1}) = 116` for every nontrivial `67`th root `α`.
- Reduce modulo `2`. Since `116 ≡ 0 (mod 2)`, we get `A(α)A(α^{-1}) = 0` in characteristic `2`.
- Because `2^33 ≡ -1 (mod 67)`, the inverse root `α^{-1}` lies in the same Frobenius orbit as `α`. The coefficients of `A` are rational integers, so Frobenius preserves vanishing. Therefore if either factor is zero, then `A(α) = 0`.
- Hence `A` vanishes at every nontrivial `67`th root over `\overline{F}_2`.
- Also `A(1) = 208 ≡ 0 (mod 2)`.
- In characteristic `2`, `x^67 - 1` is squarefree because its derivative is `67 x^66 = x^66 ≠ 0`, so it has `67` distinct roots. Since `deg A ≤ 66` and `A` vanishes on all of them, the reduction of `A` modulo `2` is the zero polynomial.
- Therefore every mod-`67` residue count is even:
  `a_r ∈ {0,2,4,6}` for all `r`.
- Writing `a_r = 2 c_r`, we obtain a halved weighted quotient on `Z/67Z` with
  `0 ≤ c_r ≤ 3`,
  `Σ c_r = 104`,
  `Σ c_r^2 = 190`,
  `Σ c_r c_{r-j} = 161` for every nonzero `j mod 67`.
- Equivalently, for every nonprincipal character `χ` of `Z/67Z`,
  `|Σ c_r χ(r)|^2 = 29`.
- This does not close nonexistence, but it is a genuine theorem slice: any cyclic `(469,208,92)` difference set would force a highly rigid `{0,1,2,3}`-valued weighted quotient with exact parameter `29`.
- Strong-result self-check:
- The argument is exact and does not depend on a heuristic search.
- What scales: the mod-`p` Frobenius-orbit trick should transfer to other cyclic cases where a prime `p | n` and a divisor `w | v` satisfy `-1 ∈ <p> mod w`.
- What does not yet scale: turning the resulting weighted quotient into a contradiction still appears instance-specific.
- Suggested theorem slice: `For a hypothetical cyclic (469,208,92) difference set, every residue class modulo 67 has even occupancy, and the halved occupancy vector is a weighted (67,104,161) quotient with nontrivial character norm 29.`
- Most useful next parameter shifts: first push this exact instance by ruling out the weighted quotient on `67`; second test nearby survivor cases with the same `2`-orbit phenomenon at a large prime divisor of `v`.
- Current package assessment: still closer to an instance-level structural slice than to a full paper-shaped exact theorem.

## family_affinity
- Strong. This sits exactly in the residual cyclic-difference-set lane highlighted by the packet, and the contracted-polynomial method is aligned with the Baumert-Gordon toolkit rather than an unrelated search mode.

## generalization_signal
- Moderate. The even-occupancy lemma is not unique to `(469,208,92)` in spirit: it uses only a prime divisor of `n` and a divisor `w | v` for which inverse lies in the same Frobenius orbit. That template should reappear in other residual cyclic cases.

## proof_template_reuse
- High. The reusable template is: contract to a divisor `w`, reduce modulo a prime `p | n`, use the cyclotomic orbit structure to force vanishing on all nontrivial `w`th roots, and convert that vanishing into divisibility or parity information on the contracted coefficients.

## candidate_theorem_slice
- Visible theorem slice:
- `In any cyclic (469,208,92) difference set, every residue class modulo 67 contains an even number of points.`
- Equivalent weighted form:
- `If such a difference set exists, its mod-67 contraction halves to a {0,1,2,3}-valued vector c on Z/67Z satisfying c c^{(-1)} = 29 + 161 G.`

## smallest_param_shift_to_test
- Inside this instance, the next exact shift is to classify or rule out the weighted quotient `c` on `Z/67Z`.
- Across nearby cases, the most promising shift is any residual cyclic survivor with `2 | n` and a prime divisor `q | v` satisfying `-1 ∈ <2> mod q`, since the same parity-compression lemma may fire there.

## why_this_is_or_is_not_publishable
- If the exact nonexistence theorem eventually closes, the packet is still around `70-90%` of a paper and the remaining work is mostly proof polishing plus literature framing.
- The present result is not yet enough for the micro-paper lane by itself. It is an exact structural lemma, but not the title theorem.
- Minimal remaining packaging work after a full closure would still be light: present the mod-`67` even-occupancy lemma, add the final contradiction or construction section, and tie it back to the survivor tables.

## paper_shape_support
- Title theorem if the main claim closes: `The cyclic group C_469 does not admit a (469,208,92)-difference set.`
- Minimal remaining packaging work after a solve: formalize the even-occupancy lemma, derive the final obstruction on the weighted quotient, and add one short paragraph connecting the result to the residual-open-case tables.
- Immediate corollary / boundary remark already available now: any hypothetical solution has mod-`67` occupancy vector in `{0,2,4,6}^{67}`, equivalently a halved weighted quotient with exact norm parameter `29`.

## boundary_remark
- The current result is stronger than a suggestive pattern but still too thin for the micro-paper lane on its own. It gives a clean structural theorem slice, not a full exact resolution.

## likely_failure_points
- The main remaining blocker is that the halved weighted quotient on `Z/67Z` may still exist; the current work does not yet rule it out.
- Any further computation has to preserve the exact theorem-facing formulation `c c^{(-1)} = 29 + 161 G` rather than slipping into an unstructured search.
- I am intentionally not invoking multiplier assumptions that the current solve artifact has not proved.

## what_verify_should_check
- Recheck the projected group-ring formulas for `w = 7` and `w = 67`.
- Recheck the characteristic-`2` argument carefully:
  `ord_67(2) = 66`,
  `2^33 ≡ -1 (mod 67)`,
  inverse is Frobenius-conjugate on nontrivial `67`th roots,
  and therefore vanishing propagates across the full orbit.
- Verify the halved weighted quotient equations after setting `a_r = 2 c_r`.
- If later work claims nonexistence from the weighted quotient, verify that the final contradiction uses only the stated exact equations and not hidden heuristic assumptions.

## verify_rediscovery
- Bounded PASS 1 web audit completed within budget.
- Checked the exact tuple notation `(469,208,92)`, alternate family notation `[469]`, the canonical Baumert-Gordon source, same-source theorem / table phrasing, and a bounded later-status pass.
- Result: no exact prior resolution found inside the audit budget. The tuple still appears as an open survivor in Baumert-Gordon 2004 Table 3 and in Gordon-Schmidt's multiplier survey table of open cases.
- Conservative conclusion: no rediscovery established, but the novelty claim remains bounded by the limited audit scope rather than a full literature search.

## verify_faithfulness
- The solve artifact does **not** prove the intended statement `Determine whether the cyclic group C_469 admits a (469,208,92)-difference set.`
- What is actually proved is a conditional structural lemma: if such a difference set exists, then every residue class modulo `67` has even occupancy, equivalently the contracted vector halves to a `{0,1,2,3}`-valued weighted quotient with exact equations on `Z/67Z`.
- This is theorem drift from the selected target, not merely weaker exposition. The honest verification classification is therefore `VARIANT`, not a verified solution of the selected problem.

## verify_proof
- For the conditional mod-`67` parity lemma, I did not find an incorrect step.
- The key chain checks out:
  1. nonprincipal `67`-quotient characters give `A(α) A(α^{-1}) = 116`;
  2. reducing modulo `2` gives a zero product at each nontrivial `67`th root;
  3. because `2^33 ≡ -1 (mod 67)`, inverse is Frobenius-conjugate, so vanishing of one factor forces vanishing of `A(α)`;
  4. `A(1) ≡ 0 (mod 2)`;
  5. `x^67 - 1` is squarefree in characteristic `2`, so vanishing on all `67` roots forces the reduced polynomial to be zero.
- No hidden search assumption was used in that slice.
- First incorrect step toward the intended theorem: the argument stops before ruling out the resulting weighted quotient or constructing a difference set. So the selected problem remains undetermined.

## verify_adversarial
- No standalone checker or code artifact exists in this slug beyond arithmetic claims recorded in prose.
- I reran the exposed arithmetic:
  - `2^33 mod 67 = 66 = -1 mod 67`;
  - `ord_67(2) = 66`;
  - the centered mod-`67` equations recompute to `Σ f_r = 7`, `Σ f_r^2 = 115`, and off-zero correlation `-1`;
  - after halving, the weighted quotient equations recompute to `Σ c_r = 104`, `Σ c_r^2 = 190`, and off-zero correlation `161`.
- Adversarial conclusion: the numeric spine of the conditional lemma survives checking, but there is still no contradiction against existence.

## verify_theorem_worthiness
- Exactness: exact for a conditional structural slice, not exact for the selected theorem.
- Novelty: bounded audit did not find a prior source stating this exact mod-`67` parity lemma, but the audit was intentionally limited.
- Reproducibility: high. The proof skeleton is short and the exposed arithmetic is reproducible.
- Lean readiness: low. Lean is not the shortest remaining path because the unresolved work is still mathematical closure, not formal sealing.
- Paper leverage: limited at present. This is a credible intermediate lemma, but not yet the title theorem of the intended micro-paper.
- If this slice were correct and Lean-sealed, it would **not** already constitute most of a publishable note. Best estimate: about `25-35%` of a publishable note, because the main existence / nonexistence theorem is still missing.
- Visible title theorem right now: `Any cyclic (469,208,92) difference set has even occupancy in each residue class modulo 67.`
- What scales: the Frobenius-orbit parity-compression template for cases with `p | n` and `-1 ∈ <p> mod w`.
- What does not scale here: the decisive final contradiction. The weighted quotient on `Z/67Z` is still untreated.
- Best honest publication status for the current verified artifact is `NONE`, not `INSTANCE_ONLY` and not yet `SLICE_CANDIDATE`.

## verify_verdict
- `VARIANT`
- The intended statement remains open in this artifact.
- The verified content is a conditional theorem slice with a correct-looking proof and bounded non-rediscovery audit.

## minimal_repair_if_any
- Added the missing squarefreeness clarification for `x^67 - 1` in characteristic `2`, which is needed to justify the step from vanishing on all `67` roots to zero polynomial.

## publication_prior_art_audit
- Exact-statement search: the tuple `(469,208,92)` still appears as a possible cyclic case in Baumert-Gordon 2004, Table 3.
- Alternate-notation search: Gordon-Schmidt 2016, Table 2 still lists the cyclic group notation `[469]` among open parameters.
- Canonical-source check: in the bounded Baumert-Gordon read, `(469,208,92)` appears as a survivor row in Table 3 and not as a theorem, proposition, corollary, example, observation, or sufficient-condition consequence already settled inside the paper.
- Follow-up check created the decisive ambiguity: Gordon's later paper `On difference sets with small λ` (received 2020, published online 2020, journal issue 2022) says that for abelian `λ = 2` parameters, a run up to `10^10` eliminated all but `24` parameters and that Table 3 gives the remaining open cases.
- Inference from that primary source: because cyclic groups are abelian and Gordon 2022's Table 3 lists only six huge remaining open `λ = 2` cases, with `(469,208,92)` absent, the exact cyclic case is no longer source-faithfully open by 2022 and is very likely already settled as a nonexistence case in that later program.
- I did not recover, within this bounded audit, the individual eliminating theorem number or a database row naming `(469,208,92)` explicitly. The rediscovery conclusion therefore rests on the later exhaustive open-cases table, not on a single theorem naming `469`.
- Conservative prior-art verdict: treat the selected exact target as `REDISCOVERY` for publication purposes.

## publication_statement_faithfulness
- The selected statement is still `Determine whether the cyclic group C_469 admits a (469,208,92)-difference set.`
- The local solve artifact does not determine existence or nonexistence.
- What it actually proves is the conditional mod-`67` parity lemma: any hypothetical cyclic `(469,208,92)` difference set has even occupancy in every residue class modulo `67`, equivalently a halved `{0,1,2,3}`-valued weighted quotient with exact norm parameter `29`.
- So even before the literature downgrade, the packet had theorem drift from the intended exact target.
- After the literature downgrade, the drift is worse publication-wise: the local claim is not only weaker than the intended theorem, it is also attached to an exact target that now appears already closed elsewhere.

## publication_theorem_worthiness
- The strongest local mathematical statement is stronger than “here is an example”; it is a reproducible conditional structural lemma.
- It is not the title theorem of the selected packet.
- The proof has some structural content and some template reuse beyond this single tuple, but the current statement is still instance-bound and conditional on existence.
- Referee test: this would not survive “what is the theorem?” as a frontier-note title theorem for this slug, because the exact case itself appears already closed in later literature and the local lemma does not finish the existence question.
- Honest theorem-slice status: a real structural side result, but not a publishable title slice for the original one-shot candidate.

## publication_publishability
- If the exact `(469,208,92)` case had remained frontier-open, one clean solve would still have been most of a short note.
- The bounded audit changes that conclusion materially: the novelty bottleneck is no longer small editorial cleanup, but that the exact target appears already resolved by later prior art.
- The present local artifact would not constitute most of a publishable note. Best bounded estimate is about `10%` of a viable paper packet, mainly as a reusable side lemma rather than a title result.
- The remaining gap is not a small final contradiction. It is primarily a publication-status gap and novelty gap.
- This slug should be moved aside rather than expanded into a broader theorem program.
- Lean would not directly seal the packet into a publication result. At this point Lean would only formalize a side lemma whose host exact problem appears no longer frontier-open.

## publication_packet_audit
- Publication verdict: `REDISCOVERY`.
- Publication confidence: `medium-high`.
- Best reading of the packet now: the exact selected target looked paper-shaped under the 2004 and 2016 sources, but the later 2020/2022 abelian-biplane status pass collapses that thesis.
- The local proof artifacts are still worth preserving because the mod-`67` parity compression is clean and may transfer to nearby cases.
- The packet is not `PAPER_READY`, not `SLICE_CANDIDATE`, and not `human_ready`.

## micro_paper_audit
- MICRO-PAPER lane verdict: fail for this slug in its current role.
- Stronger than an example: yes, but only as a conditional structural lemma.
- Already most of a publishable note: no.
- Single-solve-to-paper fraction under the audited frontier status: about `0.10`.
- Real title theorem here: no new frontier title theorem remains available for the selected exact case.
- Structural vs instance-specific: partially structural in method, still too instance-tied in output.
- Dependence on hand-picked small cases: the proof is not just a tiny example, but the current claim is still tied to one parameter and one quotient.
- Lean role: optional archival polish only; it would not rescue publication novelty.

## strongest_honest_claim
- The local artifact proves only a conditional theorem slice: if a cyclic `(469,208,92)` difference set exists, then every residue class modulo `67` has even occupancy, equivalently the mod-`67` contraction halves to a `{0,1,2,3}`-valued weighted quotient with character norm `29`.
- Separately, the bounded prior-art audit indicates that the intended exact `(469,208,92)` cyclic case is already implied closed by Gordon's later abelian `λ = 2` elimination program, so this slug should not be treated as a fresh frontier target.

## paper_title_hint
- No new frontier title is recommended for this slug.
- If the side lemma is ever reused elsewhere, the honest label is closer to `A parity constraint on the mod-67 contraction of a hypothetical cyclic (469,208,92) difference set` than to a standalone paper title.

## next_action
- Mark the publication status `REDISCOVERY`, preserve the current proof artifacts, and move this slug off the active micro-paper lane.
- Do not spend more solve time enlarging this packet into a broader program.
- Reuse the mod-`67` parity-compression argument only as a transferable helper lemma for genuinely open slugs.
