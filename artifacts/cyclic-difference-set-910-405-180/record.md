# Solve Record: On the Cyclic (910,405,180) Difference-Set Problem

- slug: `cyclic-difference-set-910-405-180`
- working_packet: `artifacts/cyclic-difference-set-910-405-180/working_packet.md`

## statement_lock
Determine whether the cyclic group C_910 admits a (910,405,180)-difference set.

## definitions
Write the group additively as `G = Z/910Z`, and let `D subset G` be a hypothetical `(v,k,lambda) = (910,405,180)` difference set.

Set `n = k - lambda = 225`.

For a subgroup `H <= G` of order `w` with quotient `G/H` of order `m = 910 / w`, let `b_x = |D cap (x + H)|`. The standard quotient group-ring identity is

`sum_x b_x = 405`

`sum_x b_x^2 = n + lambda w = 225 + 180 w`

and for every nonzero shift `t` in `G/H`,

`sum_x b_x b_(x-t) = 180 w`.

Because `3 | n` and `gcd(3,910) = 1`, the numerical-multiplier theorem makes `3` a multiplier. On any odd-order quotient `Q` of `G`, `gcd(3-1, |Q|) = 1`, so after translation the contracted coefficient function on `Q` may be taken to be invariant under multiplication by `3`.

## approach_A
Structural / invariant route:

1. Contract to odd-index quotients where the `3`-multiplier can be normalized to literal invariance.
2. Use orbit decompositions under `x -> 3x` on `C_5`, `C_7`, and `C_35`.
3. Combine the exact first-moment and second-moment equations with the orbit structure to force a tiny list of possible contracted patterns.
4. If that list becomes empty on some quotient, we get a rigorous nonexistence proof. If not, we still obtain a real theorem slice: any cyclic `(910,405,180)` set must have one of a handful of exact residue-count profiles.

The main attraction is that this route stays theorem-shaped: the quotient patterns themselves are paper-usable supporting lemmas.

## approach_B
Construction / contradiction route:

1. Contract first by the subgroup of order `2`. This yields a sequence `c_j in {0,1,2}` on `C_455` with
   `sum c_j = 405` and `sum c_j^2 = 585`.
2. Hence the multiplicities are forced exactly:
   `n_2 = 90`, `n_1 = 225`, `n_0 = 140`.
3. Center by `d_j = c_j - 1 in {-1,0,1}`. Then
   `sum d_j = -50`
   and the group-ring relation becomes
   `E E^(-1) = 225 + 5 C_455`,
   where `E = sum d_j g^j`.
4. Because the quotient order `455` is odd, the normalized `3`-multiplier makes `d_j` constant on the `3`-orbits in `C_455`.

This is a good contradiction setup: it turns the problem into a ternary perfect-sequence type object on `C_455`. The weakness is that the full orbit system on `C_455` is still fairly large, so this route likely needs a bounded exact check after the reasoning stage.

## lemma_graph
Lemma skeleton:

1. If `D` exists, then `3` is a numerical multiplier because `3 | 225` and `gcd(3,910)=1`.
2. On any odd quotient `Q` of `G`, translate so the contracted coefficient function is invariant under `x -> 3x`.
3. On the quotient `C_5`, the nonzero residues form one `3`-orbit of size `4`. The contracted counts must therefore be `(x_0, x, x, x, x)`.
4. Solving
   `x_0 + 4x = 405`,
   `x_0^2 + 4x^2 = 32985`
   gives exactly two possibilities:
   `(69,84,84,84,84)` or `(93,78,78,78,78)`.
5. On the quotient `C_7`, the nonzero residues form one `3`-orbit of size `6`. Solving
   `y_0 + 6y = 405`,
   `y_0^2 + 6y^2 = 23625`
   gives the unique pattern
   `(45,60,60,60,60,60,60)`.
6. On the quotient `C_35`, the `3`-orbit sizes are `1,4,6,12,12`. Write the corresponding orbit values as `(a,b,c,d,e)`. Projection to `C_5` and `C_7` forces
   `a + 4b = 45`,
   `c + 2d + 2e = 60`,
   and either
   `a + 6c = 69, b + 3d + 3e = 84`
   or
   `a + 6c = 93, b + 3d + 3e = 78`.
7. Adding the second-moment equation
   `a^2 + 4b^2 + 6c^2 + 12d^2 + 12e^2 = 4905`
   leaves exactly three integer solutions up to swapping the two size-`12` orbit values:
   `(9,9,10,15,10)`,
   `(21,6,12,12,12)`,
   `(9,9,14,14,9)`.

So any real solution must survive one of these three `C_35` profiles.

## chosen_plan
Best current path:

1. Keep the invariant route as the main line.
2. Use the exact quotient lemmas above as the durable theorem-facing core.
3. Then run one bounded experiment on the next odd quotient layer, preferably `C_65` or `C_91`, to see whether any `3`-invariant contracted profile is compatible with the forced `C_5`, `C_7`, and `C_35` data.
4. Stop if the bounded experiment does not clearly close the row; do not drift into broad search.

## self_checks
- Check 1: `n = 405 - 180 = 225` and the quotient identity uses `225 + 180 w` at zero shift.
- Check 2: the normalization of the `3`-multiplier is only being used on odd-order quotients, where `gcd(2, |Q|) = 1`; this avoids the translation issue present on even quotients.
- Check 3: the quotient-`5` and quotient-`7` patterns were derived only from orbit transitivity plus the first two moments, so they are rigorous once the multiplier step is accepted.
- Check 4: the `C_35` reduction uses only orbit bookkeeping and the same exact moment equations; no brute-force assumption has been smuggled in.

## code_used
Used minimal bounded Python checks only after the theorem-facing quotient skeleton was written.

1. `C_13` check:
   enumerated the five `3`-orbit variables and enforced the full quotient autocorrelation equations.
   Survivors:
   - `(45,30,30,30,30)`;
   - `(30,25,30,35,35)` up to permutation of the four nonzero `3`-orbits.
2. `C_65` check:
   enumerated `3`-invariant quotient profiles constrained by the already forced `C_5` and `C_13` patterns, then tested the full quotient autocorrelation equations.
   Result:
   - the only surviving `C_65` family has orbit values
     `a = 6`,
     `b = 6`,
     `c_i` equal to the multiset `{11,11,6,1}`,
     and all four mixed size-`12` orbit values equal to `6`.
   - equivalently, only the high-special `C_5` pattern `(93,78,78,78,78)` survives to `C_65`, and only the nonuniform `C_13` pattern with zero-class value `30` and nonzero-orbit multiset `{25,30,35,35}` survives.
3. A first attempt to push the same method to `C_91` was started, but it was not completed and is not being used as evidence.

## result
Partial structural package only so far.

Main exact reductions established:

- On the index-`5` quotient, the contracted counts must be either `(69,84,84,84,84)` or `(93,78,78,78,78)`.
- On the index-`7` quotient, the contracted counts must be exactly `(45,60,60,60,60,60,60)`.
- On the index-`35` quotient, only three orbit-value patterns survive, up to exchanging the two size-`12` orbits:
  `(9,9,10,15,10)`,
  `(21,6,12,12,12)`,
  `(9,9,14,14,9)`.
- On the index-`13` quotient, only two `3`-invariant patterns survive:
  `(45,30,30,30,30)`,
  or `(30,25,30,35,35)` up to permutation of the four nonzero `3`-orbits.
- On the index-`65` quotient, the search collapses further: after suitable translation, the only surviving `3`-invariant profile has
  fixed-point value `6`,
  order-`5` orbit value `6`,
  mixed size-`12` orbit values all equal to `6`,
  and order-`13` orbit values equal to the multiset `{11,11,6,1}`.

This is still not a proof of nonexistence or existence. It is, however, a sharper theorem-facing slice than before: any cyclic `(910,405,180)` difference set would have to land in a very narrow contracted corridor, and the `C_65` layer already kills most of the earlier quotient possibilities.

## family_affinity
Strong. The argument is squarely in the classical multiplier / quotient-contraction lane for cyclic difference sets, exactly the family indicated by the packet.

## generalization_signal
Moderate. The prime-index quotient trick clearly scales to other open cyclic rows with odd normalized multipliers, and the composite-quotient intersection step also looks reusable. What does not yet obviously scale is the last step from a rigid quotient corridor to a full contradiction.

## proof_template_reuse
Reusable template:

1. pick a prime numerical multiplier `p | n` with `gcd(p,v)=1`;
2. normalize on odd quotients;
3. solve the prime-index contracted moments exactly;
4. pass to a composite quotient and intersect the projection constraints.

That template should transfer to other residual cyclic rows with sparse odd-part factorization.

## candidate_theorem_slice
Candidate theorem slice:

"If a cyclic `(910,405,180)` difference set exists, then after suitable translation its contractions to `C_5`, `C_7`, `C_13`, `C_35`, and `C_65` lie in the exact finite profile list recorded above; in particular, the `C_65` contraction has a unique surviving `3`-orbit pattern family."

## smallest_param_shift_to_test
The most informative nearby shift is still a quotient shift rather than a parameter shift: either finish the `C_91` check cleanly or lift the rigid `C_65` profile back to the `C_455` ternary contraction. If a parameter shift is needed, the closest structural analogue is another cyclic row with the same square defect `n = 15^2` and an odd quotient where `3` has similarly sparse orbit structure.

## why_this_is_or_is_not_publishable
Not publishable yet. The current package is still a structural slice, not a closed row.

If the main claim closes, this row is still a good micro-paper target: the title theorem would simply be "On the cyclic `(910,405,180)` difference-set problem," and a successful solve would already be about `70-90%` of the paper. Minimal remaining packaging would be a short literature placement paragraph plus the decisive quotient or multiplier argument. At the moment, though, the present result is still too thin for the micro-paper lane on its own, even after the `C_65` narrowing.

## paper_shape_support
If the main nonexistence or existence claim closes, the immediate support already visible is:

- an exact quotient-`5` lemma,
- an exact quotient-`7` lemma,
- an exact quotient-`13` lemma,
- a finite quotient-`35` profile lemma,
- a rigid quotient-`65` profile lemma,
- and a brief remark that these are the residue patterns any putative solution must realize.

That would be enough supporting structure for a short note. Right now it is supporting scaffolding, not the title theorem itself.

## boundary_remark
Immediate boundary remark:

The quotient reductions show that the row is not "free-form" at all; any putative solution already lives inside a tiny contracted search corridor. What scales well is the multiplier-driven contraction to odd quotients. What does not yet scale is the final lift from rigid quotient data, especially the unique `C_65` family, to a contradiction or construction in `C_910`.

## likely_failure_points
- The multiplier normalization is strong but only useful on odd quotients; the even part `2` may still hide the last obstruction.
- The quotient-`35` slice leaves three survivors and the quotient-`65` slice leaves one family, so the current algebra has not yet forced a contradiction.
- The remaining obstruction likely sits in how the rigid odd-quotient data interacts with the pair contraction to `C_455`; that lift is the unresolved step.
- A bounded exact search on a larger odd quotient can still stall if the orbit system does not collapse fast enough, as the unfinished `C_91` attempt suggests.

## what_verify_should_check
- Recheck the numerical-multiplier step for `3`.
- Recompute the quotient moment equations for subgroup orders `182`, `130`, and `26`.
- Independently verify the surviving `C_13` and `C_65` profiles.
- Confirm that the `C_65` search really eliminates the low-special `C_5` branch and the uniform `C_13` branch.
- If a later contradiction is found, verify that it uses only the normalized odd-quotient contractions and does not assume an unjustified translation on an even quotient.

## verify_rediscovery
- PASS 1 stayed within the bounded audit budget and did not establish rediscovery.
- The exact cyclic row `(910,405,180)` was still being treated as open in the canonical-source chain used by the packet: Gordon-Schmidt 2016 Table 2, Gordon's 2019 La Jolla repository slides, and Buratti-Nakic 2024.
- I did not find a later source within the audit budget that explicitly settles the exact cyclic instance in `C_910`.
- Conclusion for PASS 1: `verify_verdict` is not `REDISCOVERY`.

## verify_faithfulness
- The intended statement is still the exact existence question: determine whether `C_910` admits a `(910,405,180)` difference set.
- The solve artifact does not settle that statement. Its strongest honest content is a conditional quotient-profile slice of the form "if such a cyclic set exists, then certain contractions are forced."
- That is theorem drift relative to the intended packet: the current artifact is a supporting structural variant, not a solve of the selected problem.
- The drift becomes material at the `C_65` layer, where the record claims a unique surviving family and an elimination of the uniform `C_13` branch. That stronger claim is not supported by independent recomputation.

## verify_proof
- The basic quotient identities check out:
  - for subgroup order `182` (quotient `C_5`), `sum b_x^2 = 225 + 180*182 = 32985`;
  - for subgroup order `130` (quotient `C_7`), `sum b_x^2 = 23625`;
  - for subgroup order `70` (quotient `C_13`), `sum b_x^2 = 12825`;
  - for subgroup order `26` (quotient `C_35`), `sum b_x^2 = 4905`;
  - for subgroup order `14` (quotient `C_65`), `sum b_x^2 = 2745`.
- The `C_5` and `C_7` reductions are correct as written:
  - `C_5`: exactly `(69,84,84,84,84)` or `(93,78,78,78,78)`;
  - `C_7`: exactly `(45,60,60,60,60,60,60)`.
- The `C_35` orbit bookkeeping is also correct. Up to swapping the two size-`12` orbit values, the only solutions are exactly the three listed in the record.
- The `C_13` full autocorrelation check is also correct. Up to permutation of the four nonzero `3`-orbits, the only solutions are `(45,30,30,30,30)` and `(30,25,30,35,35)`.
- The first incorrect step appears at the `C_65` conclusion. An independent recomputation shows that the record's elimination claim is too strong:
  - besides the nonuniform family with size-`3` orbit multiset `{11,11,6,1}` and all mixed size-`12` orbit values equal to `6`,
  - there is also a uniform surviving branch with orbit values `(21,6,6,6,6,6,6,6,6,6)` on the ten `3`-orbits of `C_65`.
- That uniform branch has:
  - total `405`,
  - square-sum `2745`,
  - all nonzero autocorrelations equal to `2520`,
  - projection to `C_5` equal to `(93,78,78,78,78)`,
  - projection to `C_13` equal to `(45,30,30,30,30)`.
- Therefore the record's statements
  - "the only surviving `C_65` family ..."
  - "only the nonuniform `C_13` pattern survives"
  are false.

## verify_adversarial
- No saved checker file exists in the artifact directory, so I reran the quotient computations independently with bounded local Python scripts.
- Those reruns reproduced the `C_5`, `C_7`, `C_35`, and `C_13` slices, but they did not reproduce the claimed `C_65` elimination.
- Adversarially, the easiest break is the explicit uniform `C_65` profile
  - orbit values `(21,6,6,6,6,6,6,6,6,6)` on the sorted `3`-orbits of `C_65`;
  - this profile satisfies the full `C_65` moment and autocorrelation equations and matches the high-special `C_5` branch together with the uniform `C_13` branch.
- So the current packet does not yet support a theorem claiming a unique `C_65` corridor.

## verify_theorem_worthiness
- Exactness: not achieved. The intended row `(910,405,180)` in `C_910` is still unresolved.
- Novelty: bounded PASS 1 did not show rediscovery of the exact row, so the target still appears frontier-novel within the audit budget.
- Reproducibility: the low-quotient slices through `C_13` and `C_35` are reproducible from the packet. The `C_65` uniqueness claim is not.
- Lean readiness: no. The strongest surviving claim is only a supporting quotient-profile variant, and formalization would not be the shortest path to a sealed publication packet.
- Paper leverage: the target row remains a strong micro-paper target if closed, but the currently verified output is still far from paper-ready.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No. The currently surviving claim is a support lemma package, not the title theorem.
- What percentage of the paper would one solve already provide? Still about `0.79` for the exact row itself, but the present verified slice is much smaller, closer to supporting scaffolding than the paper core.
- What title theorem is actually visible? At best: a conditional proposition forcing exact quotient profiles on `C_5`, `C_7`, `C_13`, and `C_35` for any hypothetical cyclic `(910,405,180)` difference set.
- What part of the argument scales? The multiplier-driven contraction to odd quotients and the small-quotient orbit bookkeeping scale cleanly.
- What part clearly does not? The claimed final sharpening at `C_65`; that step currently overstates what the computations show.
- Best honest publication status now: still `NONE`, not `INSTANCE_ONLY` and not `SLICE_CANDIDATE`. The target remains attractive, but this artifact is still publication-distant.

## verify_verdict
- `verify_verdict = UNVERIFIED`
- `classification = VARIANT`
- Reason: the packet does not solve the intended exact row, and its strongest claimed new structural theorem fails at the `C_65` uniqueness step.

## publication_prior_art_audit
- Exact-statement web search on 2026-04-15 using the row `(910,405,180)` and the cyclic phrasing surfaced the same Gordon / La Jolla chain already named in the packet and no explicit settlement of the exact cyclic `C_910` instance.
- Alternate-notation search using bare parameter notation `910 405 180`, cyclic-language variants, and the open-case framing likewise did not surface a later exact solve; the useful hits collapsed back to the canonical survey, Gordon's repository talk, and the 2024 Buratti-Nakic paper.
- Canonical-source check: Gordon-Schmidt 2016 still list `910 405 180 [910]` in Table 2 of open difference-set parameters. A direct scan of that source did not reveal a theorem, proposition, corollary, observation, example, or sufficient condition in the same paper that already settles this exact cyclic row.
- Outside-source status check: Gordon's 2019 La Jolla Difference Set Repository slides still place `910 405 180 225` among the small open cyclic / Lander-conjecture cases.
- Recent follow-up check: Buratti-Nakic 2024 still write that the cyclic `(910,405,180)` existence problem is open when applying their additive-design theorem.
- Bounded conclusion: within the required narrow audit, the row still looks frontier-open rather than rediscovered, but this remains a bounded rather than exhaustive literature search.

## publication_statement_faithfulness
- The intended statement is unchanged: determine whether the cyclic group `C_910` admits a `(910,405,180)` difference set.
- The strongest verified local content does not settle that statement. It gives only conditional quotient-profile restrictions on hypothetical solutions.
- The failed `C_65` uniqueness claim matters publication-wise: without it, the packet no longer supports even the stronger "tiny surviving corridor" story that the solve writeup initially implied.
- So the current artifact is faithful only as supporting structure for the selected problem, not as a solve of the selected problem itself.

## publication_theorem_worthiness
- The strongest honest claim is stronger than "here is an example": it is a structural conditional statement forcing exact contracted profiles on `C_5`, `C_7`, `C_13`, and `C_35`.
- Even so, it is not a real title theorem for this micro-paper lane. It reads as a preparatory proposition package, not as the decisive theorem of a short note.
- The proof method is structural in style, but the output is still tightly tethered to hand-picked small quotients of one exact row.
- A referee asking "what is the theorem?" would get a respectable supporting lemma, not a row-closing theorem, a sharp obstruction theorem, or a counterexample theorem.
- Best theorem-worthiness verdict: mathematically nontrivial supporting slice, but below standalone micro-paper threshold.

## publication_publishability
- If the exact row were solved, the packet's original leverage assessment still looks basically right: one clean existence or nonexistence proof would be most of a short paper.
- The current verified packet is not close in that sense. The remaining gap is still the mathematical core, not light exposition.
- The present slice is too dependent on low-order quotient bookkeeping to survive as a standalone note in the one-shot lane.
- Therefore the candidate did not fail because the target stopped being paper-worthy; it failed because the current artifact is still substantially short of the title theorem.

## publication_packet_audit
- Best honest publication status now: `NONE`.
- `PAPER_READY` is not justified, and even `SLICE_CANDIDATE` would overstate the packet. The verified content is still a supporting-lemma packet rather than a near-paper theorem slice.
- The useful artifacts are preserved: the corrected quotient-profile reductions and the audit trail showing exactly where the stronger story breaks.
- Lean would not directly seal this packet into a publishable result. At this stage formalization would be later archival polish for supporting lemmas, not the missing publication step.

## micro_paper_audit
- As a target, the row remains micro-paper-eligible: the exact statement is crisp, source-stable, and one decisive solve would still likely provide about `0.79` of a publishable note.
- As an audited packet, however, this run is not close to human-ready. The current verified output is supporting scaffolding, not a one-shot publication packet.
- The remaining gap is not genuinely tiny. It is still the hard last step that would turn conditional quotient restrictions into existence or nonexistence.
- One-shot recommendation: move the current packet aside unless one more bounded same-lane compatibility check has a concrete reason to close the row quickly. Do not grow this into a broader theorem program.

## strongest_honest_claim
If a cyclic `(910,405,180)` difference set exists, then after suitable translation its contractions to `C_5`, `C_7`, `C_13`, and `C_35` must lie in the exact finite profile lists recorded in the verified part of this artifact. This is a real structural claim, but it is still a supporting proposition package rather than the title theorem of a publishable note on the selected row.

## paper_title_hint
Quotient-Profile Constraints for a Hypothetical Cyclic `(910,405,180)` Difference Set

## next_action
Do not promote this packet. Preserve the corrected quotient-profile lemmas, explicitly retire the invalid unique-`C_65` corridor narrative, and either run one more bounded same-lane compatibility check with a strict close-or-cool stop condition or cool the slug as a not-yet-publishable variant.

## minimal_repair_if_any
- The only conservative repair is classificatory and local:
  - keep the verified `C_5`, `C_7`, `C_13`, and `C_35` lemmas;
  - delete the claim that `C_65` leaves a unique surviving family or kills the uniform `C_13` branch;
  - restate the strongest honest claim as a weaker conditional quotient-profile variant;
  - do not send this packet to Lean yet.
- If the slug is pursued further, the next same-lane step is to recompute the exact `C_65` survivor set correctly and then test whether compatibility with another quotient layer or with the `C_455` ternary contraction closes the row.
