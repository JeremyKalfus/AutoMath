# Solve Record: On the (703,325,150) Cyclic Difference-Set Problem

- slug: `cyclic-difference-set-703-325-150`
- working_packet: `artifacts/cyclic-difference-set-703-325-150/working_packet.md`

## statement_lock
Exact intended statement: determine whether the cyclic group `C_703` admits a `(703,325,150)`-difference set.

Working title theorem if the argument below is correct: no `(703,325,150)` difference set exists in the cyclic group `C_703`.

Because `703 = 19 * 37` and `n := k - lambda = 325 - 150 = 175`, the cleanest available route is to combine the packet's multiplier input with a quotient-by-`37` contraction.

## definitions
Convention: write `C_703` additively as `Z/703Z`. A `(v,k,lambda)` difference set `D` means `|D| = k` and every nonzero group element occurs exactly `lambda` times among ordered differences `x-y` with `x,y in D`.

For a divisor `w | 703`, let `pi_w : Z/703Z -> Z/wZ` be reduction mod `w`, and let `b_i := |D ∩ pi_w^{-1}(i)|` be the contracted residue counts.

Multiplier convention used here: the working packet records `5` and `7` as MC primes for this row. I use only `5`. Since `gcd(5-1,703)=1`, the standard multiplier-normalization step allows translation of `D` so that `5D=D`.

Ambiguities or load-bearing inputs to verify later:
- The solve packet states that `5` is a valid multiplier for this exact row; the proof below depends on that sourced fact.
- The normalization from `5D = D + g` to a translate fixed by `5` uses `gcd(5-1,703)=1`.
- I use the standard character-sum identity for difference sets: every nonprincipal character has squared modulus `n = 175`.

## approach_A
Structural / invariant approach:

1. Translate `D` so that multiplication by `5` fixes it setwise.
2. Contract mod `37`. Since `5` has order `36` mod `37`, multiplication by `5` is transitive on the `36` nonzero residues of `Z/37Z`.
3. Therefore the contracted counts have only two values:
   - `a := b_0`
   - `b := b_i` for every `i != 0` mod `37`
4. For any nonprincipal character of `Z/37Z`, the contracted character sum is
   `a + b * sum_{i=1}^{36} zeta^{ri} = a-b`.
5. That character lifts to a nonprincipal character of `Z/703Z`, so its squared modulus must equal `175`.
6. But `a-b` is an integer, so `(a-b)^2 = 175`, impossible.

If all steps hold, this gives an exact nonexistence proof with no computation.

## approach_B
Construction / extremal / contradiction approach:

Reuse the same two-level contraction mod `37`, but avoid explicit characters.

Let `a = b_0` and `b = b_i` for `i != 0`. Then
- total-size equation: `a + 36b = 325`
- second-moment equation from contraction to `37`:
  `a^2 + 36b^2 = k + lambda * (703/37 - 1) = 325 + 150 * 18 = 3025`

Substituting `a = 325 - 36b` gives
`37b^2 - 650b + 2850 = 0`
with discriminant
`650^2 - 4 * 37 * 2850 = 700 = 4 * 175`,
not a square. Hence no integer pair `(a,b)` exists.

This is a good algebraic self-check on Approach A.

## lemma_graph
Lemma 1: For this row, `5` is a usable multiplier input from the packet.

Lemma 2: Because `gcd(5-1,703)=1`, some translate of any putative difference set is fixed setwise by multiplication by `5`.

Lemma 3: Mod `37`, `5` has order `36`, so `5` acts transitively on the nonzero residues of `Z/37Z`.

Lemma 4: The mod-`37` contracted counts therefore have the form `(a,b,b,...,b)`.

Lemma 5: Every nonprincipal quotient character on `Z/37Z` lifts to a nonprincipal character on `Z/703Z`, so its sum over `D` has squared modulus `175`.

Lemma 6: Under the two-level contraction, that character sum equals the integer `a-b`.

Conclusion: `(a-b)^2 = 175`, contradiction.

## chosen_plan
Use Approach A as the main proof because it is shortest and theorem-shaped: multiplier normalization plus a one-line quotient-character obstruction.

Keep Approach B as an internal consistency check because it derives the same contradiction from the contracted second-moment equations.

Extra structure that makes the result paper-shaped if the main claim closes:
- isolate the quotient-prime lemma: a transitive multiplier on `Z/qZ^×` forces a two-level contraction
- state the immediate square-obstruction corollary for nonsquare `n`
- then apply it to `(703,325,150)` with `q=37` and `t=5`

## self_checks
- Statement lock check: the proof attacks the exact intended cyclic row `(703,325,150)` and not a nearby family variant.
- Parameter check: `703 = 19 * 37`, `n = 325 - 150 = 175`.
- Orbit check: `5^18 ≡ -1 (mod 37)`, so `5` has order `36` mod `37`; hence the nonzero mod-`37` residues form one orbit.
- Character check: a nonprincipal character of `Z/37Z` composed with reduction `Z/703Z -> Z/37Z` is still nonprincipal on `Z/703Z`.
- Contradiction check: `175` is not a square, so the integer equation `(a-b)^2 = 175` is impossible.
- Cross-check: the alternate quadratic in Approach B has discriminant `700`, also not a square.

## code_used
None. No bounded experiment or checker was needed because the mod-`37` multiplier contraction already yields a direct contradiction.

## result
Assume for contradiction that `D ⊂ Z/703Z` is a `(703,325,150)` difference set.

By the packet's multiplier input, `5` is a multiplier for this row. Since `gcd(5-1,703)=1`, after translating `D` we may assume `5D = D`.

Reduce modulo `37`, and define contracted counts
`b_i := |D ∩ pi_37^{-1}(i)|` for `i in Z/37Z`.
Because `5D = D`, we have `b_i = b_{5i}` for all `i`.

Now `5` has order `36` modulo `37`: indeed `5^18 ≡ -1 (mod 37)`, so the order divides `36` but not `18`, hence must be `36`. Therefore multiplication by `5` is transitive on the `36` nonzero residues of `Z/37Z`. Hence there are integers `a,b` such that
- `b_0 = a`
- `b_i = b` for every nonzero `i mod 37`

Let `chi_r(i) = zeta_37^{ri}` be any nonprincipal character of `Z/37Z` (`r not≡ 0 mod 37`). Composing with reduction modulo `37` gives a nonprincipal character of `Z/703Z`, so the difference-set identity gives
`|sum_{x in D} chi_r(x)|^2 = n = 175`.

But
`sum_{x in D} chi_r(x) = sum_{i in Z/37Z} b_i zeta_37^{ri}
 = a + b * sum_{i=1}^{36} zeta_37^{ri}
 = a-b`,
because the full nontrivial character sum over `Z/37Z` is zero.

Therefore `(a-b)^2 = 175`, impossible since `175 = 25 * 7` is not a square.

Contradiction. So no `(703,325,150)` difference set exists in `C_703`.

Immediate supporting slice: the same proof actually yields the quotient-prime square obstruction stated below.

Immediate corollary / boundary remark: any cyclic candidate with a verified multiplier whose reduction is transitive on the nonzero residues modulo some prime divisor `q` of `v` must have square `n`, because every nonprincipal quotient character sum becomes the same integer difference of two contracted counts.

## family_affinity
This is strongly anchored to the cyclic multiplier-contraction family rather than to ad hoc search. The obstruction is exactly the kind of short residual-row argument that fits the Gordon-Schmidt / Baumert-Gordon toolkit.

If verified, the argument is already about `80-90%` of a paper: the exact title theorem is settled, and the remaining work is mostly citation, normal-form exposition, and one compact general lemma statement.

## generalization_signal
What scales:
- the multiplier-normalization step whenever a usable multiplier `t` satisfies `gcd(t-1,v)=1`
- the contraction argument whenever the image of `t` modulo a divisor `w` has very few orbits
- the square-obstruction whenever a quotient contraction collapses all nonzero residues to one orbit

What does not scale automatically:
- transitivity on nonzero residues is special; if the quotient action has several nonzero orbits, the character sums need Gauss-period or multi-orbit analysis instead of a one-line integer obstruction
- this proof only uses the exact row's multiplier packet; it does not by itself create new multipliers for other rows

Suggested next theorem slice:
If a cyclic `(v,k,lambda)` difference set admits a multiplier `t`, and for some prime `q | v` the image of `t` in `U(q)` is transitive on `Z/qZ^×`, then `n = k-lambda` must be a square.

Current package assessment: this is no longer merely an isolated witness-level fact; it points to a small reusable theorem slice plus a clean exact application.

## proof_template_reuse
Reusable template:
1. verify a packet-supplied multiplier `t`
2. normalize to a `t`-invariant translate
3. contract modulo a prime divisor `q` where `t` has one nonzero orbit
4. conclude that every nonprincipal quotient character sum equals `a-b`
5. force `n` to be a square

This template should be checked first on other cyclic residue rows where one multiplier is primitive mod a quotient prime.

## candidate_theorem_slice
Candidate slice proposition:

Let `D` be a cyclic `(v,k,lambda)` difference set with `n = k-lambda`. Suppose `t` is a multiplier of `D`, `gcd(t-1,v)=1`, and for some prime `q | v` the image of `t` generates `U(q)`. Then the contraction of `D` modulo `q` has the form `(a,b,...,b)`, so every nonprincipal quotient character sum equals the integer `a-b`. Consequently `n = (a-b)^2` is a square.

Application here: `q=37`, `t=5`, `n=175`, contradiction.

## smallest_param_shift_to_test
Best next parameter shifts:
- inspect other open cyclic rows with a listed multiplier whose reduction is primitive modulo a prime divisor of `v`
- especially test rows where `n` is visibly nonsquare, since the same square obstruction would close them immediately

For near-neighbor work inside this family, the first thing to test is not a nearby numeric tuple but a nearby quotient-prime pattern: find another unresolved cyclic row with a `q | v` and a packet-listed multiplier acting transitively on `Z/qZ^×`.

## why_this_is_or_is_not_publishable
If the multiplier input and normalization check survive verification, this is close to publishable in the micro-paper lane.

Why:
- the exact title theorem is clean: no `(703,325,150)` cyclic difference set exists
- the proof is compact and source-anchored to the existing cyclic multiplier toolkit
- one immediate general slice is visible, so the note need not read like a bare isolated computation

Whether a successful solve would already be `70-90%` of a paper: yes, approximately `85%`.

Minimal remaining packaging work:
- verify the multiplier citation and normalization lemma carefully
- present the two-level mod-`37` contraction as a standalone proposition
- add the short literature framing around the Gordon-Schmidt open row

If verification breaks the multiplier premise, the current package collapses quickly; otherwise it is already much closer to a paper-shaped claim than to an instance-only artifact.

## paper_shape_support
Exact title theorem:
No `(703,325,150)` difference set exists in the cyclic group `C_703`.

Smallest supporting theorem slice:
Transitive quotient multipliers force square `n`.

One natural corollary or remark:
Whenever an unresolved cyclic row has a packet-listed multiplier primitive modulo a quotient prime and `k-lambda` is nonsquare, a one-page nonexistence note may be available.

Why the instance matters:
The row is already singled out in the survey as an exact open cyclic residue, so closing it is intrinsically theorem-shaped rather than feeder-ladder work.

## boundary_remark
The obstruction uses only the quotient modulo `37` and the single multiplier `5`; it does not require search, SAT, or case splits across the full group of order `703`.

Boundary of the method:
- if the multiplier acts with more than one nonzero orbit modulo every useful divisor, the proof no longer collapses to a square obstruction
- if the packet's multiplier fact is wrong or weaker than assumed, this particular route fails completely

## likely_failure_points
- The proof depends on the packet's claim that `5` is a multiplier for this exact row; this must be checked against the cited source.
- The translate-to-fixed-set step should be cited in the exact form needed when `gcd(t-1,v)=1`.
- Verify that no hidden convention issue arises between subset notation and group-ring notation when passing to quotient characters.
- Although the arithmetic is simple, the order-of-`5` computation mod `37` should be rechecked cleanly in the verification packet.

## what_verify_should_check
- Confirm from the bounded source list that `5` is indeed a valid multiplier / MC prime for `(703,325,150)` in the cyclic case.
- Confirm the exact normalization lemma: from `D^(5) = D + g` and `gcd(4,703)=1`, one may translate to a set fixed by `5`.
- Check the quotient-character lift from `Z/37Z` to `Z/703Z`.
- Recompute `5^18 ≡ -1 (mod 37)` and therefore `ord_37(5)=36`.
- Recompute the alternate second-moment contradiction `a^2 + 36b^2 = 3025`, `a+36b=325` as an independent confirmation.
- Assess publication framing: exact nonexistence theorem plus the square-obstruction slice appears stronger than `INSTANCE_ONLY`, but the audit should decide whether it is already `PAPER_READY`.

## verify_rediscovery
Bounded prior-art pass run on `2026-04-15` with the required search patterns: exact tuple `(703,325,150)`, alternate notation / reordered tuple variants, the canonical Gordon-Schmidt survey source, theorem / proposition / example / observation / corollary style checks on the same source chain, and one recent-status style sweep.

Within the allotted pass, I did not find a published paper or database entry that settles the exact cyclic row `(703,325,150)` outright. The canonical survey source still surfaces this exact row as open, and the bounded follow-up web sweep did not expose a later direct existence proof, nonexistence proof, or explicit implication theorem for the exact instance.

Conservative outcome: rediscovery was not established within budget, so this run should not be archived as `REDISCOVERY`.

## verify_faithfulness
The solve artifact targets the exact intended statement: existence or nonexistence of a `(703,325,150)` difference set in the cyclic group `C_703`. I did not find theorem drift, quantifier drift, or a switch to a weaker proxy statement.

The main faithfulness risk is more specific: the proof treats the packet's multiplier note as the stronger statement "5 is an actual usable multiplier for this exact row." The local packet and bounded source pass did not verify that stronger premise in a form strong enough to support the proof as written. So the theorem target is faithful, but the first sourced input is not yet verified at the needed strength.

## verify_proof
First unsupported step found:

`By the packet's multiplier input, 5 is a multiplier for this row. Since gcd(5-1,703)=1, after translating D we may assume 5D = D.`

Everything after that step is internally coherent on skeptical re-check:
- `703 = 19 * 37` and `n = k - lambda = 175`
- `5^18 ≡ -1 (mod 37)`, hence `ord_37(5) = 36`
- if `5D = D`, the contracted counts mod `37` collapse to `(a,b,...,b)`
- every nonprincipal quotient character sum then equals the integer `a-b`
- the contradiction `(a-b)^2 = 175` is valid
- the quadratic cross-check `37b^2 - 650b + 2850 = 0` has discriminant `700`, not a square

So I did not find a downstream algebra mistake. The problem is that the argument has not yet verified the first load-bearing multiplier premise from which the contraction starts. As written, the exact nonexistence theorem is therefore unverified.

## verify_adversarial
No checker or code artifact exists for this candidate, so there was nothing executable to rerun.

I reran the arithmetic adversarially:
- `5^18 mod 37 = 36 = -1`, so `ord_37(5) = 36`
- the alternate discriminant is `700`, not a square
- the system `a + 36b = 325`, `a^2 + 36b^2 = 3025` has no nonnegative integer solution

These checks support the internal obstruction conditional on `5`-invariance. I did not find a way to break the quotient-character contradiction once the multiplier premise is granted. The adversarial failure point remains the same as in the proof pass: the artifact does not independently justify that premise.

## verify_theorem_worthiness
Exactness:
If the multiplier premise is genuinely available for this exact row, the visible theorem is exact and strong: no cyclic `(703,325,150)` difference set exists.

Novelty:
The bounded prior-art pass did not establish rediscovery of the exact instance.

Reproducibility:
The internal arithmetic is highly reproducible, but the argument is not yet reproducible end-to-end because its first structural premise is not yet pinned to a verified source statement.

Lean readiness:
`false`. Lean is not the shortest remaining path. The bottleneck is source-level mathematical validation of the multiplier premise, not formalization.

Paper leverage:
If correct and later Lean-sealed, this would already constitute most of a publishable note, roughly `80-85%`, because the exact row is survey-anchored and the proof is short. The visible title theorem would be:

`No (703,325,150) difference set exists in the cyclic group C_703.`

What scales:
The conditional slice "a transitive quotient multiplier forces square `n`" is a real reusable theorem pattern.

What clearly does not scale:
This artifact does not prove the multiplier premise itself, and the one-orbit quotient collapse is special; if the multiplier action has several nonzero orbits, the proof no longer reduces to a one-line square obstruction.

Best honest current publication status:
still `NONE` for this run. There is a promising conditional slice, but the exact frontier claim is not yet verified strongly enough to count even as `INSTANCE_ONLY`.

## verify_verdict
- `verify_verdict`: `UNVERIFIED`
- `classification`: `PARTIAL`
- `confidence`: `medium`
- `publication_status`: `NONE`
- `lean_ready`: `false`
- `next_action`: `verify_multiplier_premise_before_any_lean_or_publication_step`

## minimal_repair_if_any
Only one conservative repair path is visible: replace the unsupported sentence "5 is a multiplier for this row" with an exact source-backed lemma or a fully checked derivation that applies to `(703,325,150)`. If that stronger premise cannot be sourced or proved, then this exact nonexistence argument should not be accepted and should remain archived only as a conditional obstruction template.

## publication_prior_art_audit
Bounded publication audit run on `2026-04-15`.

Exact-statement and alternate-notation search:
- the exact tuple searches for `(703,325,150)` and reordered / prose variants surfaced the Gordon-Schmidt multiplier-conjecture survey as the only direct claim-specific hit
- the bounded search did not surface a later paper, repository entry, or announcement giving either an existence proof or a nonexistence proof for the exact cyclic row

Canonical-source check:
- Gordon-Schmidt 2015 Table 2 still lists `703 325 150 [703]` among the open difference-set parameters
- the same source explains that the `MC primes` column records prime factors of `n` that are multipliers under the multiplier conjecture; it does not, by itself, certify that the displayed primes are already proven usable multipliers for the exact row
- within the bounded canonical-source pass, I did not find a theorem / proposition / example / corollary / observation in that survey that already settles `(703,325,150)` outright

Outside-source status pass:
- the maintained La Jolla Difference Set Repository landing pages remain live in 2025 and describe an active database intended to include known difference sets and nonexistence results
- the bounded indexed search did not surface an exact page or indexed entry announcing a settlement of the cyclic row `(703,325,150)`

Conservative prior-art verdict:
- no rediscovery was established within budget
- no later settlement was surfaced within budget
- the exact cyclic row still looks open in the bounded publication audit, but only at the level of a narrow status check

## publication_statement_faithfulness
The packet stays on the exact intended statement: determine whether the cyclic group `C_703` admits a `(703,325,150)` difference set. There is no drift to a nearby parameter set or weaker group class.

The faithfulness break is at the first structural premise. The current solve artifact reads the survey row's `MC primes` data as though it already proved that `5` is a usable multiplier for this exact cyclic case. The bounded source pass did not justify that stronger reading. So the theorem target is faithful, but the current proof claim is not: the artifact presently supports only a conditional obstruction, not the unconditional nonexistence theorem stated in the title line.

## publication_theorem_worthiness
Is the strongest honest claim stronger than "here is an example"? Yes. The surviving content is a structural conditional obstruction, not a one-off witness or tiny computation.

Is there a real title theorem, theorem slice, or counterexample theorem here? For the exact row, not yet. The real surviving slice is conditional:

`If a cyclic difference set admits a multiplier whose image is transitive on the nonzero residues modulo a prime divisor q of v, then k-lambda must be a square.`

Is the proof structural or merely instance-specific? The mechanism is structural once the multiplier premise is granted, but the current application to `(703,325,150)` is still fragile because it depends on one unsourced row-specific premise.

Would this survive a referee asking "what is the theorem?" Not as an unconditional exact-row note. The honest answer today would be "conditional on a verified `5`-multiplier, the row is impossible by a mod-`37` quotient-character obstruction." That is too conditional to headline the intended exact paper.

Is the claim too dependent on hand-picked small cases? It is not search-heavy and it does not rely on brute-force small cases, but it is still dependent on a hand-picked quotient prime and a single multiplier premise that has not been source-validated.

Overall theorem-worthiness verdict: the exact-row theorem would be genuinely worthwhile if repaired, but the current packet does not yet possess a publication-stable exact theorem.

## publication_publishability
Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? Yes. If the missing multiplier premise were source-backed or independently derived, the proof would already provide roughly `80%` of a short publishable note because the exact row is survey-anchored and the remaining work would be mostly exposition.

What percentage of the paper would one solve already provide? Roughly `80%`.

Is the remaining gap genuinely small, or did the candidate only look attractive before audit? The target itself remains attractive, but the current packet looked closer than it really is. The missing piece is not cosmetic packaging; it is the first load-bearing premise. If that premise is unavailable, the present exact-row proof route collapses rather than merely needing polishing.

If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Unless a bounded follow-up can quickly recover a source-valid or independently proved multiplier premise, this candidate should be moved aside instead of being expanded into a broader multiplier program.

Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Lean would only be later archival polish. The bottleneck is mathematical and source-level, not formalization.

Publication verdict: `publication_status = NONE`.

## publication_packet_audit
Packet quality after audit: well-preserved but not publication-stable.

What is preserved well:
- the exact statement and the intended title theorem are clear
- the quotient-character contradiction from a transitive mod-`37` multiplier action is concise and reusable
- the artifacts preserve enough of the argument to resume from the exact failure point

What fails the publication packet:
- the packet does not currently justify the first sentence that turns `5` into a proven usable multiplier for this exact cyclic row
- because that step is load-bearing, the packet is not yet a referee-ready theorem note

Best bounded packet classification:
- strongest honest frontier claim is conditional, not exact
- publication packet quality is below `SLICE_CANDIDATE`
- human-ready threshold is not met

## micro_paper_audit
Micro-paper leverage of the target remains real. This is still the kind of exact survey residue where one clean solve would mostly be the paper.

But the current artifact does not yet realize that leverage. The packet passes the "would one clean solve largely be the note?" test, and fails the "is the solve already materially in hand?" test.

Conservative micro-paper assessment:
- the candidate was sensible to audit in the micro-paper lane
- the current proof packet is not yet close enough to count as paper-ready
- the right management action is to move it aside unless the multiplier premise can be repaired quickly and locally

## strongest_honest_claim
The current artifact does not settle whether `C_703` admits a `(703,325,150)` difference set. The strongest honest claim preserved here is conditional: if `5` is an actual multiplier for this exact cyclic row, then the mod-`37` contraction forces every nonprincipal quotient character sum to equal an integer whose square is `175`, which is impossible.

## paper_title_hint
No stable exact-row title is honest yet. The exact-row title

`No (703,325,150) Difference Set Exists in the Cyclic Group C_703`

becomes honest only if the `5`-multiplier premise is sourced or replaced. Until then, the surviving title material is only a conditional quotient-multiplier obstruction.

## next_action
Run at most one more bounded source-level check aimed only at the exact `5`-multiplier premise for `(703,325,150)`. If that premise still cannot be justified cleanly, move this candidate aside rather than expanding the theorem program or sending the packet to Lean.
