# Solve Record: On (243,121,60)-Difference Sets in C3 x C9 x C9

## statement_lock
- Active slug: `abelian-difference-set-243-121-60-group-3-9-9`.
- Active title target: `On (243,121,60)-Difference Sets in C3 x C9 x C9`.
- Exact intended statement: determine whether the abelian group `G = C3 x C9 x C9` admits a `(243,121,60)`-difference set.
- If the main claim closes, the title theorem is exactly: `The group C3 x C9 x C9 does / does not admit a (243,121,60)-difference set.`
- If closed honestly, this is still an `0.84` solve-to-paper target: the remaining packaging would be short notation, one comparison paragraph with the sibling group `[3,3,3,9]`, and a compact proof-or-witness presentation.

## definitions
- Write `v=243`, `k=121`, `lambda=60`, `n=k-lambda=61`.
- For a putative difference set `D subseteq G`, the group-ring relation is `D D^(-1) = 61 + 60 G`.
- Character criterion: for every nontrivial character `chi` of `G`, `|chi(D)|^2 = 61`.
- Let `H = 3G = {0} x 3C9 x 3C9`, so `|H|=9` and `G/H ~= C3^3`.
- Let `T = G[3] = C3 x 3C9 x 3C9`, so `|T|=27` and `G/T ~= C3^2`.
- Let `alpha(g1,g2,g3) = (g1, 7g2, 7g3)`. Since `61 == 7 (mod 9)`, this is the numerical-multiplier automorphism attached to `61`.

## approach_A
Structural / quotient-first approach through `G/H ~= C3^3`.

Let `x_q = |D cap q|` for the `27` cosets `q` of `H`.

From the quotient character criterion:
- `sum_q x_q = 121`.
- For each nontrivial character of `G/H`, the Fourier coefficient has squared modulus `61`.

Fourier inversion gives:
- `sum_q x_q^2 = 601`.
- `sum_q x_q x_(q+t) = 540` for every nonzero `t in C3^3`.

For any hyperplane partition of `C3^3` into three affine planes, the three plane sums must be `{36,40,45}` because the corresponding order-`3` character value has norm `61`.

Incidence count at a point `p`:
- `sum_(P contains p) wt(P) = 13 x_p + 4(121 - x_p) = 484 + 9 x_p`.
- If `a_p,b_p,c_p` are the numbers of incident planes of weights `36,40,45`, then
  `36 a_p + 40 b_p + 45 c_p = 484 + 9 x_p` and `a_p + b_p + c_p = 13`.
- This forces either:
  - `b_p=13` and `x_p=4`, or
  - `b_p=4` and `x_p=c_p`.

Summing `c_p` over all points counts incidences with the `13` planes of weight `45`, hence
`sum_p c_p = 13 * 9 = 117`. Since `sum_p x_p = 121`, there is exactly one exceptional point with `x_p=4` and `b_p=13`.

After translating that exceptional point to `0`:
- every linear hyperplane of `C3^3` has total weight `40`,
- `x(0)=4`,
- for every nonzero projective pair `{u,-u}`, `x(u) + x(-u) = 9`.

This gives a rigid quotient normal form, but not yet a contradiction.

## approach_B
Construction / contradiction approach through the multiplier and the fixed subgroup `T`.

Step 1: use the classical first multiplier theorem.
- Because `61 | n`, `gcd(61,243)=1`, and `61 > lambda = 60`, the integer `61` is a numerical multiplier.
- Therefore `D^(61) = g D` for some `g in G`, where `D^(61)` means apply `x -> x^61`.

Step 2: locate the translation `g`.
- Modulo `T`, the automorphism `alpha` is trivial because `7 == 1 (mod 3)`.
- Hence the `9` coset counts of `D` modulo `T` must be invariant under translation by `g mod T`.
- A nonzero translation on `G/T ~= C3^2` would force all `9` coset counts equal, impossible since they sum to `121`.
- So `g in T`.
- Projecting further to the first `C3` factor, the three coset counts must also be translation-invariant under the first coordinate of `g`. Since those three counts must be `{36,40,45}`, the first coordinate of `g` is forced to be `0`.
- Thus `g in 3G = {0} x 3C9 x 3C9`.

Step 3: remove the translation.
- On `G`, `alpha-1` acts as `(0,6,6)`, whose image is exactly `3G`.
- So choose `h in G` with `(alpha-1)(h) = -g`, replace `D` by `hD`, and obtain an equivalent putative difference set satisfying `alpha(D)=D`.

Step 4: exploit the `alpha`-orbit structure.
- The fixed subgroup of `alpha` is `T = G[3]`, of size `27`.
- Every element outside `T` lies in an `alpha`-orbit of size `3`.
- Since `alpha(D)=D`, the set `D` is the disjoint union of:
  - `A = D cap T`, and
  - full size-`3` `alpha`-orbits outside `T`.
- Hence `|A| == 121 (mod 3)`, so `|A| == 13`, and every nonzero `T`-coset count is a multiple of `3`.

Now project to `G/T ~= C3^2`. Let `c_u = |D cap u|`.

Exactly as above:
- `sum_u c_u = 121`,
- each nontrivial quotient character has squared modulus `61`,
- every direction gives line sums `{36,40,45}`.

Point-line incidence in `C3^2` yields:
- there is exactly one exceptional point of weight `13`,
- after translating it to `0`, every line through `0` has weight `40`,
- for each of the four opposite pairs `{u,-u}` in `(G/T) \\ {0}`, one has `c(u) + c(-u) = 27`.

Because the nonzero coset counts are multiples of `3`, write the four pair differences as
`t_i = c(u_i) - c(-u_i)`, so `t_i in {+-3, +-9, +-15, +-21, +-27}`.

Using projective coordinates on `C3^2`, the four affine-line conditions reduce to
- `|t1 + t3 + t4| = 9`
- `|t2 + t3 - t4| = 9`
- `|t1 - t2 - t4| = 9`
- `|t1 + t2 - t3| = 9`

I then used a tiny exhaustive check on these four variables. Every solution is, up to relabeling and sign choices,
`(t1,t2,t3,t4) = (+-3, +-3, +-3, +-9)`.

Therefore any multiplier-normalized putative difference set has the following exact quotient profile on `G/T`:
- one distinguished `T`-coset of size `13`,
- three opposite `T`-coset pairs with counts `{12,15}`,
- one opposite `T`-coset pair with counts `{9,18}`.

This is a real theorem-facing slice. It is still only a necessary condition, not the full nonexistence proof.

## lemma_graph
1. Character criterion on a quotient gives exact weighted autocorrelation equations.
2. On `G/H ~= C3^3`, those equations force a unique weight-`4` exceptional coset and pair-sum rule `x(u)+x(-u)=9`.
3. The multiplier theorem forces `61` to act as a numerical multiplier.
4. The translation defect lies in `3G`, hence can be removed; so one may assume `alpha(D)=D`.
5. `alpha`-invariance forces `|D cap T| = 13` and makes every nonzero `T`-coset count a multiple of `3`.
6. On `G/T ~= C3^2`, the quotient line sums are again `{36,40,45}`.
7. Those line sums force a unique central `T`-coset of size `13`, opposite-pair sums `27`, and finally the rigid outer pattern `{12,15},{12,15},{12,15},{9,18}`.
8. Remaining blocker: convert this quotient rigidity into an obstruction or construction inside the actual `27`-element subgroup `T` and the `36` selected size-`3` orbits outside it.

## chosen_plan
- Best path for this run: push the multiplier first, because it collapses the ambient `243`-point problem to a `9`-coset quotient with only four outer pair variables.
- That path produced a clean necessary structure.
- It did not yet reach a contradiction, so I am stopping at the strongest honest slice rather than pretending to have solved the instance.

## self_checks
- Self-check after the `G/H` quotient:
  the incidence count is internally consistent and explains the unique weight-`4` exceptional coset without overclaiming nonexistence.
- Self-check after the multiplier step:
  the only delicate point is the normalization from `D^(61)=gD` to `alpha(D)=D`; this depends on correctly locating `g` in `3G`.
- Self-check after the `G/T` quotient:
  the central `13` and opposite-pair sum `27` are forced by line-sum counting, independent of the tiny search.
- Self-check after the bounded check:
  the code only solves the final four-variable reduced system; it does not search the original `243`-point problem and does not claim more than quotient rigidity.

## code_used
- Minimal code was used.
- I ran two bounded Python checks:
  - a sanity check on cyclic quotient profiles of order `9`,
  - the decisive four-variable exhaustive check for the multiplier-normalized `G/T` quotient.
- No repository source file was introduced for the code; both checks were one-off terminal snippets.

## result
- Main claim status in this run: not solved.
- Strongest honest mathematical output:
  any putative `(243,121,60)`-difference set in `C3 x C9 x C9` can be normalized by the `61` multiplier so that, modulo `T = G[3]`, its coset counts are rigid up to affine symmetry:
  `13` at one distinguished `T`-coset, three opposite pairs `{12,15}`, and one opposite pair `{9,18}`.
- What part of the argument scales:
  the multiplier-plus-quotient package should scale to other abelian exponent-`9` Hadamard-difference-set problems with prime `n` and a usable numerical multiplier.
- What part does not:
  the final obstruction still needs information inside `T` and inside the selected size-`3` `alpha`-orbits; the quotient data alone is realizable in reduced models and does not force impossibility.
- Theorem slice suggested:
  a proposition classifying the `G/T` quotient profile of any multiplier-normalized putative difference set.
- Best next parameter shifts:
  first, push the same slice against the sibling group `[3,3,3,9]` as a control calculation;
  second, apply the same multiplier-normalized quotient analysis to the next exponent-`9` comparison case where `n` still has a large prime multiplier.
- Current package assessment:
  this is closer to a paper-shaped lemma than to a paper-shaped full theorem; it is still an instance-level partial result, not yet a micro-paper closure.

## family_affinity
- High.
- This instance sits in the abelian Hadamard / exponent-sensitivity family at order `3^5`, exactly where group structure rather than parameter arithmetic is supposed to decide existence.

## generalization_signal
- Moderate positive signal.
- The multiplier-normalized quotient argument is not tied to a random computation; it uses structural ingredients that should recur in neighboring exponent-`9` abelian groups.
- The unresolved part is local orbit geometry, not the high-level reduction.

## proof_template_reuse
- Reusable template:
  1. force a numerical multiplier from `p | n` with `p > lambda`,
  2. remove the translation defect,
  3. pass to the fixed subgroup quotient,
  4. classify the reduced line-sum pattern,
  5. only then inspect the internal subgroup geometry.
- This template should be reusable for related abelian difference-set nonexistence attempts where quotient character values collapse to order-`3` data.

## candidate_theorem_slice
- Candidate slice:
  `If a (243,121,60)-difference set exists in C3 x C9 x C9, then after multiplier normalization by 61 its image in G/G[3] ~= C3^2 has one coset of weight 13, three opposite coset pairs of weights {12,15}, and one opposite coset pair of weights {9,18}.`

## smallest_param_shift_to_test
- Smallest productive shift to test next:
  the same multiplier-normalized quotient package on the sibling group `[3,3,3,9]` as a control, and then on the next unresolved exponent-`9` group-specific case if one remains live.

## why_this_is_or_is_not_publishable
- If the main claim closed, the solve would already be about `70-90%` of a short paper. That assessment remains unchanged.
- The current run is not publishable on its own.
- Reason:
  the quotient classification is a substantial supporting proposition, but it does not yet settle existence or nonexistence, and it does not yet isolate a human-ready obstruction inside `T`.
- Minimal remaining packaging work if the main claim closes:
  a short proof of the multiplier proposition, the rigid quotient-profile proposition, and then the decisive final obstruction or explicit construction.
- Immediate natural corollary / remark from the current slice:
  any future exact proof may assume from the start that the `G[3]` quotient profile is the rigid `13 / (12,15)^3 / (9,18)` pattern, so any candidate witness outside that shape can be discarded immediately.
- Current verdict for the micro-paper lane:
  still too thin without the final closure.

## paper_shape_support
- What extra structure would make this paper-shaped if the main claim closes:
  1. a final theorem showing the rigid quotient profile cannot be lifted to an actual difference set, or
  2. an explicit lift witnessing existence.
- The present quotient slice would then become the paper's main structural proposition and would materially shorten the final proof.

## boundary_remark
- Boundary remark:
  the reduction stops exactly at the point where one must control the `13` chosen points in `T ~= C3^3` and the placement of the `36` selected size-`3` `alpha`-orbits outside `T`.
- So the argument currently separates global quotient rigidity from the still-open local lift problem.

## likely_failure_points
- The largest technical risk is the multiplier-normalization step `D^(61)=gD => alpha(D)=D`; verify carefully that `g` is indeed forced into `3G`.
- The second risk is a sign convention error in reducing the four affine-line equations on `G/T ~= C3^2`.
- The third risk is strategic, not algebraic:
  the quotient profile may be perfectly consistent with some highly structured lift, so more quotient work alone may never finish the problem.

## what_verify_should_check
- Check the exact multiplier theorem hypothesis used here: `61 | n`, `61 > lambda`, and the abelian numerical-multiplier conclusion.
- Check the argument forcing the translation defect into `3G`, not merely into `T`.
- Re-run the four-variable exhaustive check independently.
- Confirm that the quotient-profile proposition is stated only as a necessary condition, not as a hidden nonexistence claim.
- If verification wants a next move, inspect the induced character sums on `A = D cap T` and on the `36` selected size-`3` `alpha`-orbits to see whether the rigid outer quotient can actually be lifted.

## verify_rediscovery
- PASS 1 used bounded web only.
- I checked the exact tuple `(243,121,60)` with `C3 x C9 x C9`, the alternate group notation `[3,9,9]`, the canonical Gordon ArasuFest slide deck, and one status-style follow-up search for a later exact resolution.
- The canonical source still presents `[3,9,9]` at `(243,121,60)` as the smallest open exact abelian case in this exponent-sensitivity lane.
- Within the capped pass I did not find a later theorem, proposition, example, observation, corollary, or repository status page settling the exact group `C3 x C9 x C9`.
- Rediscovery was therefore not established in budget.

## verify_faithfulness
- The intended statement is exact existence or nonexistence of a `(243,121,60)`-difference set in `C3 x C9 x C9`.
- The solve artifact does not establish that intended statement.
- What it actually proves, if sound, is a narrower necessary-condition proposition about the quotient profile of a multiplier-normalized putative difference set in `G/G[3]`.
- So the artifact is not an exact solve, not an exact disproof, and not Lean-ready for the selected problem itself.
- Faithfulness verdict: the writeup is honest about being partial, but the strongest surviving claim is a nearby theorem slice, so the run must be classified as `VARIANT`.

## verify_proof
- The multiplier-theorem input is plausible as stated: `61 | n`, `61 > lambda`, and `gcd(61,243)=1` are the standard hypotheses for a numerical multiplier in the abelian setting.
- The normalization step `alpha(D)=gD` with `g in 3G` also survives checking once the quotient argument is written carefully.
- First incorrect step in the current writeup:
  `|A| == 121 (mod 3), so |A| == 13`.
- That inference is too strong. From orbit divisibility alone one gets only `|A| == 1 (mod 3)`.
- Conservative repair:
  first record only that every nonzero `T`-coset count is divisible by `3`;
  then use the `G/T ~= C3^2` incidence calculation to show there is exactly one coset of weight `13`;
  because `T` is the only coset that can carry a non-multiple-of-`3` count under `alpha`-invariance, that unique `13`-weight coset must be `T`.
- A second wording repair is needed earlier in Step 2:
  a nonzero translation on `G/T ~= C3^2` does not force all `9` coset counts equal, only constancy on three size-`3` orbits.
  That is already enough to force the total to be divisible by `3`, contradicting the sum `121`.
- After those tiny repairs, I did not find a deeper algebraic flaw in the actual variant claim envelope.

## verify_adversarial
- I reran the bounded four-variable check from the record.
- Result: exactly `16` signed solutions occur, and every one has absolute-value pattern `(3,3,3,9)`, matching the writeup.
- I independently checked the order-`3` quotient line-sum constraint by solving the nonnegative integer norm equation with total `121`; the only multiset is `{36,40,45}`.
- I also checked the local point-line incidence systems on `C3^3` and `C3^2`.
- For `C3^3`, the recorded dichotomy is correct: either the exceptional weight is `4` with all `13` incident planes of weight `40`, or else the count of incident weight-`40` planes is `4` and the number of incident weight-`45` planes equals the point weight.
- For `C3^2`, the admissible point weights are `9,12,13,15,18`, and the global incidence equations force exactly one point of weight `13`.
- These reruns support the claimed quotient-rigidity slice, but they do not support the original exact existence/nonexistence question.

## verify_theorem_worthiness
- Exactness:
  no exact theorem for the selected problem has been proved here.
- Novelty:
  bounded prior-art checking did not establish rediscovery of the exact selected instance, but I also did not separately certify that this narrower quotient-profile proposition is absent from the literature.
- Reproducibility:
  moderate.
  The necessary computations are small and rerunnable, but they are not preserved as a stable repo script.
- Lean readiness:
  no.
  Formalizing this slice would seal only a supporting proposition, not the shortest remaining step to a publication packet.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  No.
- What percentage of a note does the present slice provide?
  Roughly `0.25` to `0.35`, not the `0.84` expected from an exact solve of the selected problem.
- What title theorem is actually visible?
  Any multiplier-normalized putative `(243,121,60)`-difference set in `C3 x C9 x C9` has quotient profile `13 / (12,15)^3 / (9,18)` in `G/G[3]`, up to affine symmetry.
- What part of the argument scales?
  The multiplier-plus-quotient-plus-line-sum package should transfer to nearby abelian exponent-`9` cases.
- What part clearly does not?
  The lift from quotient data to an actual subset of `G`; the unresolved local geometry inside `T` and the selected size-`3` outer orbits is still the real blocker.
- Best honest publication status:
  `NONE`.
  This is a supporting structural proposition, not yet an exact instance result and not yet close enough to a standalone micro-paper packet.

## verify_verdict
- `verify_verdict = MINOR_FIX`
- `classification = VARIANT`
- `confidence = 0.78`
- `lean_ready = false`
- `lean_packet_seal = false`
- `publication_status = NONE`
- `next_action = do_not_run_lean_continue_only_if_the_quotient_slice_can_be_converted_into_an_exact_obstruction_or_witness`

## minimal_repair_if_any
- Replace the sentence `|A| == 121 (mod 3), so |A| == 13` by the weaker congruence claim `|A| == 1 (mod 3)`.
- Then justify `|A| = 13` only after the `G/T` incidence argument has produced a unique `13`-weight coset and after using `alpha`-invariance to note that only `T` can have a count not divisible by `3`.
- Replace the overstrong phrase `a nonzero translation ... would force all 9 coset counts equal` by the correct orbit statement `a nonzero translation partitions the 9 quotient points into three 3-cycles, so invariant counts would make the total divisible by 3`.

## publication_prior_art_audit
- Exact-statement search:
  bounded web searches for `(243,121,60)` together with `C3 x C9 x C9` surfaced Gordon's 2019 slide deck, not a later exact resolution.
- Alternate-notation search:
  bounded web searches for `(243,121,60)` together with `[3,9,9]` again surfaced the same Gordon source and no later exact settlement in the capped pass.
- Canonical source check:
  Gordon's ArasuFest slide `38 / 49` still records the exponent-sensitivity comparison table with `[3,3,3,9]` marked `No` and `[3,9,9]` marked `Open`.
- Canonical-source proposition / example / corollary / observation check:
  the same slide isolates the selected statement as a named smallest-open case, while Gordon's group-ring slide and character slide provide only the ambient necessary-condition toolkit, not a hidden theorem already deciding `[3,9,9]`.
- Outside-source status pass:
  Gordon's current difference-set site remains the active repository surface for abelian difference sets, and Gordon's current publications page lists difference-set papers through `2025` without an obvious title settling the exact `(243,121,60)` `[3,9,9]` case. This is an inference from a bounded author-and-repository check, not a proof that no such paper exists.
- Prior-art verdict:
  rediscovery was not established in budget, but the negative search is still only bounded rather than exhaustive.

## publication_statement_faithfulness
- The canonical selected statement remains exact:
  determine whether `C3 x C9 x C9` admits a `(243,121,60)`-difference set.
- The strongest surviving artifact does not prove or disprove that statement.
- What the run honestly supports is narrower:
  a structural necessary-condition theorem slice about the `G/G[3] ~= C3^2` quotient of a multiplier-normalized putative difference set.
- Is the strongest honest claim stronger than `here is an example`?
  Yes.
  It is a structural proposition, not a single witness or tiny computation.
- Faithfulness verdict:
  the record is honest about partiality, but the audited packet is still a `VARIANT` relative to the selected exact claim.

## publication_theorem_worthiness
- Is there a real title theorem, theorem slice, or counterexample theorem here?
  Yes, there is a real theorem slice:
  any multiplier-normalized putative `(243,121,60)`-difference set in `C3 x C9 x C9` has the rigid quotient profile `13 / (12,15)^3 / (9,18)` in `G/G[3]`, up to affine symmetry.
- Would this survive a referee asking `what is the theorem?`
  As a supporting proposition, probably yes.
  As the title theorem of a standalone note in this lane, no.
- Is the proof structural or merely instance-specific?
  It is structural inside one exact instance: multiplier, quotient, and incidence arguments do real work, but the claim remains tightly attached to this one group and parameter set.
- Is the claim too dependent on hand-picked small cases?
  Not in the usual example-by-example sense.
  The bounded computation appears only after the quotient reduction and only to finish a four-variable residue check.
- Theorem-worthiness verdict:
  mathematically meaningful as a lemma-level slice, but not yet strong enough to reclassify the packet as a near-paper theorem result.

## publication_publishability
- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note?
  No.
- What percentage of the paper would one solve already provide?
  The audited output currently provides about `0.30` to `0.35` of a note, not the `0.84` that the original candidate would have delivered if the exact instance had been closed.
- Is there a real title theorem here?
  Only at the supporting-proposition level, not yet at the note-title level expected by the micro-paper lane.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit?
  For the current artifact, the packet looked closer than it really is.
  The remaining gap is still decisive rather than editorial: one still needs either a lift obstruction or an explicit construction.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program?
  Yes.
  Keep only the same one-shot line alive: attempt one more direct obstruction-or-witness push from the rigid quotient profile, and otherwise move the slug aside rather than broadening into a larger campaign.

## publication_packet_audit
- Publication packet quality:
  supporting-slice only.
- Proof artifacts preserved:
  yes.
  The quotient package, the repaired proof notes, and the bounded computational checks are all preserved well enough for a later exact push.
- Publication status verdict:
  `NONE`.
- Reason:
  the audited packet does not yet contain a decisive theorem about existence or nonexistence, and the remaining gap is not small enough to call it a slice-level near-paper result.
- Would Lean directly seal the packet?
  No.
  Lean would only formalize a supporting structural proposition, which would be optional polish rather than the decisive human-ready seal.

## micro_paper_audit
- Micro-paper leverage of the selected problem itself remains high if the exact instance closes.
- Micro-paper leverage of the current audited output is not high enough.
- This run does produce something stronger than scaffolding-free experimentation, but it does not yet shorten solve-to-publication distance enough to justify continued expansion on publication grounds alone.
- Micro-paper verdict:
  keep the exact target conceptually alive, but do not treat the present quotient slice as a publishable micro-paper packet.

## strongest_honest_claim
- Strongest honest claim:
  `If a (243,121,60)-difference set exists in C3 x C9 x C9, then after multiplier normalization by 61 its image in G/G[3] ~= C3^2 has one coset of weight 13, three opposite coset pairs of weights {12,15}, and one opposite coset pair of weights {9,18}.`

## paper_title_hint
- Paper title hint:
  `A Multiplier-Normalized Quotient Constraint for Putative (243,121,60)-Difference Sets in C3 x C9 x C9`
- Audit note:
  this is the title of the current slice, not a recommendation that the packet is already paper-ready.

## next_action
- Next action:
  attempt exactly one more same-lane push converting the rigid quotient profile into either a lift obstruction inside `T = G[3]` or an explicit witness.
  If that does not close quickly, move the candidate aside rather than expanding into a broader theorem program or Lean-first formalization.
