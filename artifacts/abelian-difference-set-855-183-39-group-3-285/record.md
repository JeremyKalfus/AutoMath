# Solve Record: On the (855,183,39) Difference-Set Problem in C_3 x C_285

- slug: `abelian-difference-set-855-183-39-group-3-285`
- working_packet: `artifacts/abelian-difference-set-855-183-39-group-3-285/working_packet.md`

## statement_lock
Determine whether the abelian group C_3 x C_285 admits a (855,183,39)-difference set.

## definitions
Let `G = C_3 x C_285 ≅ C_3^2 x C_5 x C_19`, and let `D ⊂ G` be a hypothetical `(v,k,lambda) = (855,183,39)` difference set.

Write `n = k - lambda = 144 = 12^2`.

For any quotient `pi : G -> Q`, write
`pi(D) = sum_{q in Q} x_q q`
with `x_q = |D ∩ pi^{-1}(q)|`. Since `D D^(-1) = n + lambda G`, every quotient image satisfies
`pi(D) pi(D)^(-1) = n * 1_Q + lambda * |ker pi| * Q`.

Two quotient systems are immediately relevant:

1. `Q_19 = G / (C_3^2 x C_5) ≅ C_19`, with kernel size `45`.
   Then for the coset counts `x_j` on `C_19`,
   `sum x_j = 183`,
   `sum x_j^2 = 1899`,
   and every nonzero cyclic shift has correlation `1755`.

2. `Q_5 = G / (C_3^2 x C_19) ≅ C_5`, with kernel size `171`.
   Then for the coset counts `a_i` on `C_5`,
   `sum a_i = 183`,
   `sum a_i^2 = 6813`,
   and every nonzero cyclic shift has correlation `6669`.

Centered variables:

- On `C_19`, set `y_j = x_j - 9`. Then
  `sum y_j = 12`,
  `sum y_j^2 = 144`,
  and every nonzero cyclic shift has correlation `0`.

- On `C_5`, set `b_i = a_i - 36`. Then
  `sum b_i = 3`,
  `sum b_i^2 = 117`,
  and every nonzero cyclic shift has correlation `-27`.

## approach_A
Structural / invariant route.

Use quotient images and centered autocorrelation identities. The `C_19` quotient is especially rigid because centering by `9` turns the quotient image into an integer length-19 sequence with perfect periodic autocorrelation:

`Y Y^(-1) = 144 * 1` in `Z[C_19]`.

Because `3^9 ≡ -1 (mod 19)` and `2^9 ≡ -1 (mod 19)`, inversion on 19th roots is Frobenius in characteristics `3` and `2`. Reducing the centered quotient relation mod `3`, then mod `2`, should force strong divisibility of `Y`, and the small remaining norm should classify the sequence completely.

If this closes, the 19-quotient is not merely constrained but uniquely determined up to translation:
one coset has occupancy `21`, the remaining eighteen cosets have occupancy `9`.

This is the cleanest invariant currently visible because it uses only quotient algebra and no search.

## approach_B
Construction / contradiction route.

Combine the `C_19` quotient classification with the `C_5` quotient classification. After verification repair, the latter collapses, up to cyclic translation, to the row-sum pattern

`27, 39, 39, 39, 39`.

Passing to the quotient by the `C_3^2` kernel yields a `5 x 19` array of cell counts in `[0,9]` whose:

- row sums are `27,39,39,39,39`,
- column sums are `21,9,9,...,9`,
- total square-sum is fixed by the quotient relation.

The hoped-for contradiction is that these marginals, together with the mixed-character `|hat f(a,b)| = 12` constraints on `C_5 x C_19`, have no realization. This route is more combinatorial and, if needed later, is the only place where a tiny bounded experiment seems justified.

## lemma_graph
Lemma 1.
For the `C_19` quotient counts `x_j`, the centered sequence `y_j = x_j - 9` satisfies
`sum y_j = 12`, `sum y_j^2 = 144`, and zero off-peak periodic autocorrelation.

Lemma 2.
In `F_3[C_19]`, the reduction of `Y = sum y_j g^j` is zero. Reason: `Y Y^(-1) = 144 * 1`, so mod `3` we get `Y Y^(-1) = 0`; since `3^9 ≡ -1 (mod 19)`, evaluating at any 19th root `omega` gives
`Y(omega) Y(omega)^3^9 = Y(omega)^(1+3^9) = 0`,
hence `Y(omega)=0` for every 19th root, so all coefficients are divisible by `3`.

Lemma 3.
After dividing by `3`, the same argument mod `2` applies because `2^9 ≡ -1 (mod 19)`. Therefore all `y_j` are divisible by `6`.

Lemma 4.
Write `y_j = 6 w_j`. Then
`sum w_j = 2` and `sum w_j^2 = 4`.
The only integer possibility compatible with zero off-peak autocorrelation is one entry `2` and all others `0`. Therefore, up to translation,
`(x_j) = (21,9,9,...,9)`.

Lemma 5.
For the `C_5` quotient counts `a_i`, the centered sequence `b_i = a_i - 36` satisfies
`sum b_i = 3`, `sum b_i^2 = 117`, and constant off-peak autocorrelation `-27`.

Lemma 6.
Because `3^2 ≡ -1 (mod 5)`, the same mod-`3` Frobenius argument forces `b_i` to be divisible by `3`. Writing `b_i = 3 c_i`, we obtain
`sum c_i = 1` and `sum c_i^2 = 13`.
A verifier rerun found the original multiset classification here was wrong. A bounded exhaustive check over integer 5-tuples with
`sum c_i = 1`, `sum c_i^2 = 13`, and every nonzero cyclic shift correlation `-3`
shows that the unique cyclic pattern is `(-3,1,1,1,1)`.
Hence, up to cyclic translation,
`(a_i) = (27,39,39,39,39)`.

Target conclusion.
Either these quotient shapes can be lifted consistently through the mixed `C_5 x C_19` character constraints, or they already force a contradiction.

## chosen_plan
Best path: close as much of the quotient-classification argument as possible without over-claiming a full nonexistence proof.

Immediate target:

1. Make the `C_19` and `C_5` quotient classifications fully explicit and self-checked.
2. Use them as the candidate theorem slice.
3. Only then decide whether a bounded quotient-level experiment on the `5 x 19` lift is worth running.

If the lift contradiction does not close cleanly, the honest output is a strong partial package, not a fake theorem.

## self_checks
- The centered quotient identities were recomputed directly from `n = 144` and the relevant kernel sizes `45` and `171`.
- The divisibility argument is only being claimed on the quotient images, not yet on the full difference set.
- The current packet does not yet prove existence or nonexistence in `G`; it proves only that any solution must satisfy very rigid quotient data.
- The micro-paper lane remains plausible only if the mixed `C_5 x C_19` lift can be closed without large search.

## code_used
No code-derived claim is used in the current packet.

I briefly considered a bounded `5 x 19` quotient-table consistency search after the quotient slices were recorded, but that experiment is not part of the mathematical result here. The current artifact should be read as a reasoning-only structural package.

## result
Current strongest rigorous slice:

- Any hypothetical `(855,183,39)` difference set in `C_3^2 x C_5 x C_19` must project to `C_19` with coset counts
  `21,9,9,...,9`
  up to translation.

- Any hypothetical `(855,183,39)` difference set in `C_3^2 x C_5 x C_19` must project to `C_5` with coset counts
  `27,39,39,39,39`
  up to cyclic translation.

This is theorem-shaped structural information, but it is not yet a full solve. The remaining gap is the mixed-character lift from these one-factor quotient profiles to the full `C_5 x C_19` quotient by the `C_3^2` kernel.

Exact sentence for why this instance matters:
this row is important because the open Gordon-Schmidt Table 2 case is now reduced to a sharply constrained `C_95` lift problem rather than an unconstrained existence question.

## family_affinity
High. The argument uses standard abelian-difference-set quotient and character machinery, but the concrete output is unusually sharp for this exact residual row. If it closes, it would look like a residual-row elimination via quotient-profile rigidity.

## generalization_signal
Moderate. The finite-field divisibility trick depends on a prime `p` for which inversion on the quotient is Frobenius, i.e. `p^j ≡ -1 (mod m)` on the relevant quotient order `m`. That suggests a reusable template for other open rows with quotient factors `5` or `19`, but not a broad family theorem yet.

## proof_template_reuse
Reusable template:

1. pass to a prime-order quotient,
2. center the quotient counts so the image has perfect or near-perfect periodic autocorrelation,
3. use `p^j ≡ -1 (mod m)` to convert inversion into Frobenius mod `p`,
4. force divisibility of the centered quotient image,
5. collapse the remaining low-norm possibilities by integer square-sum classification.

This template is strong whenever one quotient factor is prime and the centered norm becomes very small after divisibility.

## candidate_theorem_slice
Candidate theorem slice:

If a `(855,183,39)` difference set exists in `C_3 x C_285`, then:

1. modulo the `C_3^2 x C_5` kernel, its `C_19` coset occupancies are exactly `21,9,9,...,9` up to translation;
2. modulo the `C_3^2 x C_19` kernel, its `C_5` coset occupancies are exactly `27,39,39,39,39` up to cyclic translation.

This is already a real theorem slice, and it is the smallest supporting structure that currently looks paper-relevant.

## smallest_param_shift_to_test
Best nearby shifts:

1. inspect the quotient by the `C_3^2` kernel, i.e. the `C_5 x C_19 ≅ C_95` lift problem, because that is the exact unresolved residue after the one-factor quotient collapses;
2. compare whether the same centered-divisibility argument survives for the analogous `[3,95]` or `[9,95]` style rows, where the prime-order quotient structure may be similar.

## why_this_is_or_is_not_publishable
If the full nonexistence proof closes from these quotient profiles, then yes: this would already be about `70-90%` of a short paper. The exact title theorem would still be:

`On the (855,183,39) Difference-Set Problem in C_3 x C_285`.

What remains in that successful scenario would be light packaging: state the Gordon-Schmidt Table 2 context, present the quotient-rigidity lemmas, and finish with the decisive lift contradiction.

At the current stage, the package is not yet publishable. It is still too thin for the strict micro-paper lane because the main existence/nonexistence claim is not closed.

## paper_shape_support
The quotient profiles give the first genuinely paper-facing support:

- they are exact, not heuristic;
- they isolate a decisive residual obstruction rather than a broad campaign;
- they indicate what the title-theorem proof would have to look like: first collapse `C_19`, then `C_5`, then eliminate the `C_95` lift.

If the lift contradiction is found, the immediate supporting structure is already in place.

## boundary_remark
Natural boundary remark:

The current argument scales through prime-order quotients where inversion is Frobenius modulo a small prime, but it does not yet control the mixed `C_5 x C_19` interaction. So the part that scales is the one-factor quotient collapse; the part that does not yet scale is the final two-factor lift obstruction.

## likely_failure_points
- The Frobenius divisibility argument must be stated carefully so it is genuinely ring-theoretic and not just suggestive character manipulation.
- The jump from one-factor quotient rigidity to a contradiction in `C_5 x C_19` may fail; there may exist many quotient-level lifts consistent with the marginals.
- A bounded computational check, if used, might show consistency of weak lift data rather than inconsistency, in which case the packet stays partial.

## what_verify_should_check
Verification should check:

1. the quotient group-ring identities, especially the centered constants `144`, `117`, `-27`, and `0`;
2. the finite-field step using `3^9 ≡ -1 (mod 19)`, `2^9 ≡ -1 (mod 19)`, and `3^2 ≡ -1 (mod 5)`;
3. the uniqueness of the integer low-norm solutions after divisibility:
   `sum w_i = 2`, `sum w_i^2 = 4` on `C_19`,
   and `sum c_i = 1`, `sum c_i^2 = 13` on `C_5`;
4. whether the quotient slice is enough to certify `publication_status = SLICE_CANDIDATE` rather than `NONE`;
5. whether any later lift contradiction was proved rigorously or only explored experimentally.

## verify_rediscovery
Bounded PASS 1 rediscovery audit: no rediscovery established.

Limited web checks repeated the required patterns against the exact tuple `(855,183,39)`, the group notations `C_3 x C_285` and `[3,285]`, and the canonical Gordon-Schmidt survey. Within this pass budget I found the canonical 2016 source listing the row as open, but no later paper, note, database entry, theorem, proposition, example, or corollary explicitly settling the exact `[3,285]` case. The result therefore does not verify as a rediscovery on the evidence gathered here.

## verify_faithfulness
The current artifact does not solve the intended statement "determine whether `C_3 x C_285` admits a `(855,183,39)` difference set." It proves only necessary quotient-profile constraints for any hypothetical solution.

That means the packet is faithful only as a nearby theorem slice. It must not be treated as a solve of the intended statement, and the correct harness classification is `VARIANT`, not `EXACT` and not a completed solve of the selected row.

## verify_proof
The quotient arithmetic in the `C_19` and `C_5` images checks out: the centered identities `sum y_j = 12`, `sum y_j^2 = 144`, `sum b_i = 3`, `sum b_i^2 = 117`, and the off-peak correlations `0` and `-27` all recompute correctly from the standard quotient relation.

The first incorrect step is the original Lemma 6 classification on `C_5`. From `sum c_i = 1` and `sum c_i^2 = 13`, the record claimed the unique multiset `{3,1,-1,-1,-1}`, hence `a_i = (45,39,33,33,33)`. That is false: the claimed pattern does not satisfy the required off-peak correlation `-3` after dividing by `9`.

The smallest conservative repair is to replace that step by the verified cyclic pattern `(-3,1,1,1,1)`, which yields `a_i = (27,39,39,39,39)` up to cyclic translation. With that repair, the nearby quotient-rigidity slice is supported; without it, the original proof is incorrect as written.

## verify_adversarial
No checker file exists in the candidate artifact, so I reran bounded direct computations inline.

For the `C_19` slice, I exhaustively tested the only nontrivial low-norm alternative to the claimed classification, namely all length-19 cyclic placements of the multiset `(1,1,1,-1)`. None has zero off-peak periodic autocorrelation, so the only surviving integer pattern is one entry `2` and the rest `0`, giving `21,9,9,...,9`.

For the `C_5` slice, I exhaustively tested all integer 5-tuples with `sum c_i = 1` and `sum c_i^2 = 13`. The unique pattern with off-peak periodic autocorrelation `-3` is `(-3,1,1,1,1)` up to cyclic translation, yielding `27,39,39,39,39` after undoing the centering.

These checks support the repaired variant slice, but they do not touch the actual unresolved `C_95` lift problem, so they do not verify the intended existence or nonexistence claim.

## verify_theorem_worthiness
Exactness: the repaired result is an exact theorem slice about quotient occupancies, but it is not the intended existence/nonexistence theorem.

Novelty: bounded PASS 1 web checking did not establish rediscovery of the selected row, but it also does not prove the repaired quotient slice itself is new. The exact frontier claim remains open on this record.

Reproducibility: good. The arithmetic reductions are short, and the repaired low-norm classifications are reproducible by a bounded exhaustive check.

Lean readiness: no. Lean is not the shortest remaining path to a sealed packet because the main unresolved gap is still mathematical: the `C_95` lift obstruction has not been proved.

Paper leverage: limited. If the intended row were later closed, this quotient slice would likely become a useful section of the paper, but by itself it does not already supply most of a publishable note.

Direct answers:
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `35%` at best in its current repaired form.
- What title theorem is actually visible? Any hypothetical `(855,183,39)` difference set in `C_3 x C_285` must project to `C_19` with occupancies `21,9,9,...,9` and to `C_5` with occupancies `27,39,39,39,39`, up to translation.
- What part of the argument scales? The prime-order quotient centering, Frobenius-divisibility step, and low-norm collapse.

## publication_prior_art_audit
Exact-statement and alternate-notation searches on `2026-04-15` using `(855,183,39) difference set`, `C_3 x C_285 difference set`, and `[3,285] difference set` surfaced the Gordon-Schmidt survey as the claim-specific anchor, but no later primary source explicitly settling this exact row.

Inside the canonical source, the status is clear rather than ambiguous: Gordon-Schmidt say Table 2 records the smallest open cases, and the exact row `855 183 39 [3, 285]` appears in that table. So, within the source itself, no theorem, proposition, corollary, observation, or sufficient-condition check in that paper has already removed this row.

As one bounded outside-source follow-up check, I inspected Dan Gordon's current publications page. It lists later difference-set papers through `2025`, but no title-level follow-up there points to a claim-specific settlement of the `(855,183,39)` row. This is only a bounded negative check, not a proof that no later settlement exists.

Audit verdict: no rediscovery is established for the selected exact row on this bounded pass, but the current quotient-rigidity slice also has no strong novelty certificate beyond "not obviously already written down".

## publication_statement_faithfulness
The active selected statement is still:

`Determine whether the abelian group C_3 x C_285 admits a (855,183,39)-difference set.`

The current artifact does not answer that question. It proves only necessary quotient-profile conditions for any hypothetical difference set. So the packet is faithful only as a nearby theorem slice, not as a solve of the selected row.

That distinction matters for publication audit: the honest claim is not "the row is solved", but "the row collapses to one exact `C_19` profile and one exact `C_5` profile". The record should therefore be read as a structural side theorem anchored to the row, not as a completed residual-row note.

## publication_theorem_worthiness
The strongest honest claim is stronger than "here is an example". It is an exact structural necessity theorem for the open row:
any hypothetical `(855,183,39)` difference set in `C_3 x C_285` must have one forced `C_19` quotient profile and one forced `C_5` quotient profile, up to translation.

There is a real theorem slice here, and it is structural rather than merely anecdotal. The proof uses quotient identities, Frobenius-divisibility, and low-norm classification, not a hand-picked witness. Still, the slice remains tightly instance-anchored because it does not resolve the mixed `C_95` lift and does not yet broaden to a family theorem.

Would this survive a referee asking "what is the theorem?" Yes at the slice level: the theorem is quotient rigidity for this exact row. But the follow-up referee question would immediately be "why is this enough for a paper if the open row is still open?" On the current packet, there is not yet a strong answer.

## publication_publishability
This is not `PAPER_READY`. The quotient-rigidity theorem slice is real, but it does not yet supply most of a publishable note targeted at the Gordon-Schmidt residual row. The unresolved `C_95` lift is still the main mathematical burden, not light cleanup.

My bounded audit answer is that the candidate looked closer to paper status before audit than it does now. Once the selected statement failed to close, the remaining publication gap stopped being "small finishing work" and became "prove the decisive contradiction or change the paper's theorem". That is too large for the strict one-shot micro-paper lane.

If one insists on publishing something from the current packet, the honest title would have to be about quotient rigidity rather than the row itself. Even then, the narrative is only moderate at best because novelty of the slice is not strongly audited and the slice feels more like supporting structure than a standalone note.

## publication_packet_audit
Packet quality is good as a preserved research artifact: the repaired theorem slice, the proof skeleton, and the exact unresolved bottleneck are all recorded clearly enough for future reuse. So `proof_artifacts_preserved` should remain true.

However, the packet is not human-ready. Lean would not directly seal the publication outcome because formalizing the current slice would still leave the main publication gap untouched. At most, Lean would archive the quotient-rigidity theorem as optional later polish.

Recommended publication reading: treat this dossier as a well-preserved exact slice with downstream value, not as a near-complete paper packet.

## micro_paper_audit
- Stronger than "here is an example": yes.
- Most of a publishable note already present: no.
- Estimated solve-to-paper fraction actually achieved by the current packet: about `35%`.
- Real title theorem or theorem slice present: yes, a quotient-rigidity slice.
- Proof structural or merely instance-specific: structural, but narrowly tied to this one row.
- Too dependent on hand-picked small cases: not fatally, but the final low-norm collapses do use tiny bounded case analysis and the true missing step is still substantial.
- Remaining gap genuinely small: no.
- Should this be moved aside rather than expanded into a larger theorem program: yes, unless a short rigorous `C_95` lift obstruction is already visible.
- Would Lean directly seal the packet: no; it would only formalize the slice, not close the publication case.

Micro-paper verdict: the selected row remains a good source-anchored target in principle, but this run's actual output is below one-shot publication threshold. The packet should be kept as an exact supporting slice and moved aside unless the final lift contradiction can be obtained cheaply.

## strongest_honest_claim
Any hypothetical `(855,183,39)` difference set in `C_3 x C_285` must project to `C_19` with occupancies `21,9,9,...,9` and to `C_5` with occupancies `27,39,39,39,39`, up to translation.

## paper_title_hint
Quotient Rigidity for the `(855,183,39)` Difference-Set Problem in `C_3 x C_285`

## next_action
Preserve the quotient-rigidity slice, but move this packet out of the active micro-paper lane unless a short rigorous contradiction for the induced `C_95` lift can be written next without broadening the program.
- What part clearly does not? The final mixed `C_5 x C_19` lift to `C_95`.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? `NONE`; this is a verified supporting slice, not yet a near-paper packet.

## verify_verdict
`VARIANT_REPAIRED`

The intended statement is still open in this artifact. What survives verification is a corrected nearby theorem slice on quotient occupancies.

## minimal_repair_if_any
Applied a minimal conservative repair to the false `C_5` quotient pattern:

- replaced `45,39,33,33,33` by `27,39,39,39,39`;
- recorded that the original Lemma 6 multiset classification was incorrect;
- preserved the verified `C_19` slice and downgraded the packet to a repaired `VARIANT` rather than a solve of the selected problem.
