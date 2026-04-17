# Solve Record: The Abelian [3,165] (495,247,123) Difference-Set Case

- slug: `abelian-difference-set-495-247-123-group-3-165`
- working_packet: `artifacts/abelian-difference-set-495-247-123-group-3-165/working_packet.md`

## statement_lock
Exact intended statement: determine whether the abelian group of type `[3,165]` admits a `(495,247,123)`-difference set.

For this solve pass I lock the group as
`G = C_3 x C_165 ~= C_3 x C_3 x C_5 x C_11`,
which is the standard interpretation of the abelian type notation `[3,165]`.

The exact title-theorem candidate visible from this pass is:

`The abelian group of type [3,165] admits no (495,247,123)-difference set.`

If correct, this is already about `80-90%` of a short paper: the main theorem is exact, source-anchored, and needs only a concise introduction, proof cleanup, and a brief comparison with the survey row.

## definitions
- A `(v,k,lambda)`-difference set in a finite abelian group `G` is a subset `D subseteq G` with `|D| = k` such that every nonzero `g in G` has exactly `lambda` ordered representations `g = d_1 - d_2` with `d_1,d_2 in D`.
- For such a difference set, `n = k - lambda`. Here
  `n = 247 - 123 = 124`.
- For every nonprincipal character `chi` of `G`, the standard character identity gives
  `|chi(D)|^2 = n = 124`.
- Because `2 | 124` and `gcd(2,495) = 1`, the standard first multiplier theorem makes `2` a numerical multiplier.
- Since `2-1 = 1` acts invertibly on `G`, the usual translation-normalization for multipliers lets us assume a hypothetical difference set is fixed by doubling:
  `2D = D`.
- The group `G` has a quotient `G -> C_3`; equivalently, `G` has characters of exact order `3`.

Ambiguities and conventions to keep explicit:
- I am using additive notation for `G`.
- I am using the standard multiplier theorem in the form "if `p | n` and `gcd(p,|G|)=1`, then `p` is a multiplier for an abelian difference set".
- I am using the standard normalization fact that if `t` is a multiplier and multiplication by `t-1` is an automorphism of `G` (for example, if `gcd(t-1, exp(G))=1`), then some translate of `D` is `t`-invariant.
- The solve conclusion depends on those standard facts being checked in verify.

## approach_A
Structural / invariant approach: `2`-multiplier plus an index-`3` quotient.

1. Assume for contradiction that `D subseteq G` is a `(495,247,123)`-difference set.
2. Because `2 | n = 124` and `gcd(2,495)=1`, `2` is a multiplier. Translate `D` so that `2D = D`.
3. Fix a quotient map `pi : G -> C_3`.
4. In `C_3`, doubling is multiplication by `2 = -1`, so it swaps the two nonzero quotient classes.
5. Therefore the contracted quotient counts of `D` modulo `ker pi` have the form `(a,b,b)`.
6. Let `psi` be a nonprincipal character of `C_3`; then
   `psi(pi(D)) = a + b omega + b omega^2 = a - b`,
   because `1 + omega + omega^2 = 0`.
7. Lift `psi` to a nonprincipal character `chi = psi o pi` of `G`. Then `chi(D) = a-b` is an integer.
8. But the difference-set character identity says `|chi(D)|^2 = 124`, so `(a-b)^2 = 124`.
9. This is impossible because `124` is not a square.

This route gives a short direct contradiction without search, orbit enumeration, or heavy contraction.

Self-check after approach A:
- The argument uses only three structural inputs: `2` is a multiplier, `2D=D` after translation, and `G` has an order-`3` quotient.
- Nothing in the contradiction uses the `5`- or `11`-parts of `G`; that is good for robustness, but it also means verify should check whether this broader slice is already known in the literature.

## approach_B
Construction / extremal / contradiction approach: `31`-multiplier on the `11`-part.

1. Since `31 | n = 124` and `gcd(31,495)=1`, `31` is also a numerical multiplier.
2. On `G ~= C_3^2 x C_5 x C_11`, multiplication by `31` acts trivially on the `3`- and `5`-parts and as multiplication by `9` on `C_11`.
3. The action of `9` on `C_11` has orbit decomposition
   `\{0\}` plus two nonzero `5`-cycles.
4. Therefore in each coset of the order-`11` subgroup, a `31`-invariant translate can meet that coset in only
   `0,1,5,6,10,11`
   points.
5. Contracting to the quotient of order `45` would force an integer profile `c_x in {0,1,5,6,10,11}` with
   `sum c_x = 247`
   and
   `sum c_x^2 = 247 + 123(11-1) = 1477`.

This looks promising for a semigroup obstruction, but it is heavier than approach A and not needed once the order-`3` character contradiction is available.

Self-check after approach B:
- The orbit-size restriction is correct if the normalization to a `31`-invariant translate is valid.
- This route is useful as a backup or as supporting structure, but it is not the shortest theorem-facing path.

## lemma_graph
Small proof skeleton:

1. Hypothetical difference set `D` in `G`.
2. Compute `n = k-lambda = 124`.
3. First multiplier lemma gives that `2` is a multiplier.
4. Translation-normalization gives a translate with `2D = D`.
5. Choose any quotient `pi : G -> C_3`.
6. `2D = D` forces quotient counts `(a,b,b)` because doubling swaps the two nonzero classes of `C_3`.
7. Any order-`3` quotient character then has integer value `a-b` on `D`.
8. Character identity requires its squared modulus to equal `124`.
9. Since `124` is not a square, contradiction.
10. Therefore no such difference set exists.

## chosen_plan
Choose approach A.

Reason:
- It is the shortest exact disproof.
- It uses a clean invariant with no code.
- If the multiplier normalization checks out, the result is already paper-shaped: one standard multiplier lemma, one quotient-count lemma, one contradiction.

What extra structure would make this result paper-shaped if the main claim closes?
- One explicit lemma isolating the `2`-fixed quotient profile `(a,b,b)` on any index-`3` quotient.
- One brief corollary recording the broader odd-order / `3`-divisible / even-`n` nonsquare obstruction.
- One paragraph tying that slice back to the exact Gordon-Schmidt Table 2 row.

Minimal remaining packaging work if this proof survives verify:
- polish the multiplier-normalization citation,
- write the quotient-character lemma cleanly,
- add a short source-to-theorem introduction and one paragraph on scope.

## self_checks
Major-step self-checks:

- Statement lock check:
  The intended theorem is exact-case existence in the unique abelian type `[3,165]`, not a family-wide existence claim.
- Definitions check:
  The only nontrivial imported facts are the standard multiplier theorem and the standard character identity.
- Structural path check:
  The quotient-to-`C_3` step is legitimate because `G` has a direct `3`-factor.
- Contradiction check:
  `chi(D)` is shown to be an integer before applying `|chi(D)|^2 = 124`; the impossibility is exactly that an integer square cannot equal `124`.
- Scope check:
  The proof is a nonexistence proof for the exact selected row. Any broader theorem slice should be treated as a suggested generalization until verify checks novelty.

## code_used
No code was used.

No checker, search, SAT, ILP, CP-SAT, brute force, or bounded experiment was needed because the contradiction is purely structural.

## result
Provisional strong result:

`The abelian group of type [3,165] admits no (495,247,123)-difference set.`

Rigorous proof attempt:

Assume for contradiction that `D subseteq G = C_3 x C_165` is a `(495,247,123)`-difference set.
Then
`n = k-lambda = 124`.

Because `2 | 124` and `gcd(2,495)=1`, the standard first multiplier theorem makes `2` a multiplier of `D`.
Since `2-1=1` acts invertibly on `G`, we may translate `D` and assume
`2D = D`.

Now choose a quotient map
`pi : G -> C_3`.
Let the three fibers over `C_3` have sizes
`a, b, c`.
The condition `2D = D` implies that doubling preserves the image multiset of `D` in `C_3`.
But doubling on `C_3` is multiplication by `-1`, so it fixes `0` and swaps the two nonzero elements.
Hence the two nonzero fibers have equal size:
`b = c`.
So the quotient profile is `(a,b,b)`.

Let `psi` be a nonprincipal character of `C_3`, and let `omega = psi(1)`.
Then
`omega^2 + omega + 1 = 0`,
so
`omega + omega^2 = -1`.
Therefore
`psi(pi(D)) = a + b omega + b omega^2 = a - b`.
This is an integer.

Lift `psi` to a character `chi = psi o pi` of `G`.
Because `psi` is nonprincipal, `chi` is nonprincipal.
By the standard character equation for difference sets,
`|chi(D)|^2 = n = 124`.
But `chi(D) = a-b in Z`, so this says
`(a-b)^2 = 124`,
which is impossible.

This contradiction proves that no `(495,247,123)`-difference set exists in the abelian group of type `[3,165]`.

Self-check after the proof:
- The contradiction is exact and does not rely on a heuristic search.
- The proof uses only standard difference-set technology.
- The only load-bearing external check is the multiplier normalization step; verify should test that citation carefully.

One natural immediate corollary / remark:
- The same proof template appears to show that any odd-order abelian difference set with `3 | |G|`, `2 | (k-lambda)`, and nonsquare `k-lambda` is impossible, because a `2`-fixed translate forces an order-`3` character value to be an integer.

What part of the argument scales:
- The quotient-to-`C_3` and integer-character-value mechanism scales to any odd-order abelian group with a quotient `C_3`.
- The use of the first multiplier theorem scales to any case with `2 | (k-lambda)` and `gcd(2,|G|)=1`.

What part does not scale automatically:
- The exact publication claim does not automatically scale, because novelty of the broader slice is not checked in solve.
- If `k-lambda` is a square, this exact contradiction disappears.

What theorem slice is suggested:
- Suggested slice: if a finite abelian group has odd order divisible by `3`, and if a `(v,k,lambda)`-difference set in that group satisfies `2 | (k-lambda)` with `k-lambda` not a square, then no such difference set exists.

What one or two parameter shifts would help most:
- Check other abelian `[3,m]` rows with even nonsquare `n`.
- Check any odd-order abelian row with `3 | v` and `2 | n`, regardless of the other prime factors.

Whether the current package is still just an instance or already closer to a paper-shaped claim:
- If verify confirms the standard multiplier normalization and novelty status, this is already closer to a paper-shaped claim than to a bare instance, because the exact row closes and a broader obstruction slice is visible.

## family_affinity
High affinity with abelian odd-order cases carrying an order-`3` quotient.

More specifically:
- exact group-type rows `[3,m]`,
- abelian cases where `2` is the first useful multiplier,
- quotient-character obstructions in small prime quotients,
- micro-paper closures where one exact row is solved by a short multiplier argument.

## generalization_signal
Moderate to strong.

The proof does not use any special `5`- or `11`-structure. It only uses:
- odd group order,
- existence of a quotient `C_3`,
- `2 | n`,
- nonsquare `n`.

That makes the exact-case disproof look like the front face of a broader theorem slice. However, solve should not claim that broader slice as novel before verify checks the literature.

## proof_template_reuse
Reusable template:

1. Use a small prime multiplier `t` dividing `n`.
2. Normalize to a `t`-fixed translate when multiplication by `t-1` is an automorphism of `G` (for example, when `gcd(t-1, exp(G))=1`).
3. Push to a small quotient where multiplication by `t` permutes nonzero classes.
4. Show the resulting character value lies in a smaller ring, ideally in `Z`.
5. Contradict `|chi(D)|^2 = n`.

Here that template specializes beautifully with `t=2` and quotient `C_3`.

## candidate_theorem_slice
Suggested theorem slice:

`Let G be a finite abelian group of odd order with 3 dividing |G|. If D subseteq G is a (v,k,lambda)-difference set and n = k-lambda is even but not a square, then no such D exists.`

Reason for the slice:
- `2 | n` makes `2` a multiplier,
- `2-1=1` acts invertibly on `G`,
- `3 | |G|` gives a quotient `G -> C_3`,
- `2` fixes `0` and swaps the two nonzero classes of `C_3`,
- the order-`3` character value becomes an integer whose square must equal `n`.

For the exact selected row, this slice specializes immediately to `[3,165]` and `n=124`.

## smallest_param_shift_to_test
Most useful next shifts:

1. Other abelian `[3,m]` rows with even nonsquare `n`, because the same quotient-`C_3` contradiction may close them immediately.
2. Odd-order abelian rows outside the `[3,m]` notation but still with `3 | v` and `2 | n`, to test how broad the slice really is.

## why_this_is_or_is_not_publishable
If the proof is verified, this is publishable in the micro-paper lane.

Why:
- the exact Gordon-Schmidt Table 2 row is closed,
- the argument is short and theorem-facing,
- the main theorem already reads like a note title,
- the remaining writeup burden is light.

What the exact title theorem would be:
- `The abelian group of type [3,165] admits no (495,247,123)-difference set.`

## verify_rediscovery
PASS 1 used a bounded web audit only.

Search patterns covered:
- exact tuple plus group notation: `(495,247,123)` with `[3,165]`
- alternate tuple / reordered notation: `495 247 123` with abelian difference-set language
- the canonical source itself: Gordon-Schmidt, *A Survey of the Multiplier Conjecture*
- theorem / table checks inside the same source
- a later status / discussion check via Gordon's difference-set pages and later multiplier-theorem discussion

Result:
- I found the canonical survey row again in Table 2, where `(495,247,123)` in group `[3,165]` is still listed among the open cases.
- I found no exact later paper, repository note, or source snippet establishing existence, nonexistence, or a direct implication settling this exact group-specific row.
- I did find a later Gordon paper on small `lambda` restating the First Multiplier Theorem with the condition `p > lambda`, which matters for proof checking but does not settle the row.

Verdict for PASS 1:
- No rediscovery was established within the bounded audit.
- The exact intended statement still appears frontier-open on the checked evidence.

Bounded web sources consulted:
- Gordon-Schmidt survey PDF, especially Result 1.1 and Table 2.
- Gordon difference-set page.
- Gordon, "On difference sets with small `lambda`", which restates the multiplier theorem conditions.

## verify_faithfulness
The intended statement and the solver's headline claim match at the title level:
- exact group type `[3,165]`
- exact parameters `(495,247,123)`
- exact task: existence versus nonexistence in that group

But the proof packet is not faithful to that headline theorem.

Reason:
- The contradiction actually proves only a conditional statement of the form:
  if a hypothetical difference set can be translated so that `2D = D`, then the `C_3` quotient argument forces an impossible integer square.
- The packet silently upgrades that conditional lemma into an unconditional nonexistence theorem by citing the First Multiplier Theorem incorrectly.

Faithfulness verdict:
- wrong imported theorem condition, not wrong problem statement
- exact-case theorem drift occurs at the proof-to-claim interface
- strongest honest claim is conditional, not the intended exact disproof

## verify_proof
First incorrect step:
- In `definitions`, `approach_A`, `lemma_graph`, and the final proof, the packet claims that because `2 | n = 124` and `gcd(2,495)=1`, the standard First Multiplier Theorem makes `2` a multiplier.

This step is incorrect.

Reason:
- The canonical source states the First Multiplier Theorem as: if `p` divides `n`, `p` does not divide `v`, and `p > lambda`, then `p` is a multiplier.
- Here `p = 2` and `lambda = 123`, so `2 > 123` is false.
- The survey presents the multiplier conjecture precisely because the `p > lambda` hypothesis cannot simply be dropped in general.

Consequences:
- The packet does not justify that `2` is a multiplier.
- Therefore it does not justify the translation-normalization step to a `2`-invariant translate.
- Therefore the quotient profile `(a,b,b)` is not established for an arbitrary hypothetical difference set.
- Therefore the integer-value character contradiction does not settle the exact `[3,165]` row.

What survives:
- Conditional lemma: if one independently proved that some translate satisfies `2D = D`, then the quotient-to-`C_3` argument would indeed force an impossible square `(a-b)^2 = 124`.
- That conditional obstruction is mathematically coherent, but it is not the intended theorem.

Proof-correctness verdict:
- first incorrect step found
- exact theorem not verified
- no conservative local patch upgrades the packet to a proof of nonexistence

## verify_adversarial
Code / checker rerun:
- No code or checker exists for this packet, so there was nothing to rerun.

Adversarial stress test applied to the mathematics:
- Remove the unsupported claim that `2` is a multiplier.
- Re-run the argument from the next line onward.

Outcome:
- The proof immediately loses the invariant `2D = D`.
- Without `2D = D`, there is no reason the image of `D` in `C_3` has quotient counts `(a,b,b)`.
- Without `(a,b,b)`, the order-`3` character value need not be an integer.
- Without integrality, the contradiction with `|chi(D)|^2 = 124` disappears.

So the construction is not robust under skeptical replay: the packet depends entirely on the unsupported multiplier step.

## verify_theorem_worthiness
Exactness:
- The intended theorem slice is exact and attractive.
- The verified surviving claim is only a conditional side lemma, so the current packet is not exact in the sense needed for publication.

Novelty:
- No rediscovery was found for the exact row in the bounded audit.
- Novelty of the salvaged conditional lemma was not separately established and should not be promoted as a paper claim.

Reproducibility:
- The logical failure is reproducible: the cited multiplier theorem condition does not apply to `p = 2`.
- The surviving conditional quotient argument is reproducible from the packet.

Lean readiness:
- Not Lean-ready.
- Lean would formalize either an incorrect theorem claim or only a conditional lemma that is not the publication bottleneck.

Paper leverage:
- If the exact row were truly settled, it would still provide most of a short note, roughly `80%`.
- The current verified content provides far less, because it does not close the row.

Direct answers:
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? For the exact row theorem, yes. For the currently verified conditional lemma, no.
- What percentage of the paper would one solve already provide? About `80%` for a genuine exact solve; the present audited packet is much less than that.
- What title theorem is actually visible? Only the conditional statement that a `2`-invariant translate would force a contradiction through the `C_3` quotient.
- What part of the argument scales? The quotient-character integrality mechanism scales to any setting where a valid `2`-invariant translate is already available.
- What part clearly does not? The jump from `2 | n` to "`2` is a multiplier" does not scale; it is simply unsupported here.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? `NONE` for the current packet, because the exact row is not settled and the surviving conditional lemma is not yet a paper-shaped theorem.

Overall worthiness verdict:
- the target remains micro-paper-worthy
- the present proof packet does not yet clear even instance-only publication status
- the exact row should remain open in the harness until a source-justified multiplier theorem or a different exact argument is supplied

## verify_verdict
- `verify_verdict`: `NOT_VERIFIED`
- `classification`: `VARIANT`
- `confidence`: `high`

Reason:
- No rediscovery found.
- The intended exact theorem was not verified.
- The strongest honest surviving statement is a nearby conditional obstruction rather than the selected exact disproof.

## minimal_repair_if_any
Smallest conservative repair:
- downgrade the solver's main claim to the conditional lemma:
  if a hypothetical `(495,247,123)`-difference set in abelian `[3,165]` can be translated to satisfy `2D = D`, then the `C_3` quotient yields an impossible square, so such a `2`-invariant translate cannot exist

Why this is only a salvage patch:
- it preserves a useful obstruction fragment
- it does not solve the exact row
- it does not by itself improve publication status beyond `NONE`

No smaller citation edit fixes the proof, because the missing ingredient is substantive: the packet has not proved that `2` is a multiplier here.

## publication_prior_art_audit
Bounded publication audit on `2026-04-16` used only the exact row, alternate group notation, the canonical survey PDF, one outside-source status search, and one recent follow-up theorem check.

Exact-statement and alternate-notation checks:
- searches for `(495,247,123)` with `[3,165]`, `C_3 x C_165`, and `C_3 x C_3 x C_5 x C_11` returned the Gordon-Schmidt survey as the only precise claim-level hit inside the audit budget
- the outside-source status search surfaced Dan Gordon's live difference-set database page as the current status hub for abelian difference-set parameters, but no exact indexed hit settling the `[3,165]` row
- no later paper, theorem statement, construction, or explicit nonexistence result for the exact abelian `[3,165]` row surfaced in the bounded pass

Canonical-source check:
- Gordon-Schmidt state that Table 2 lists open difference-set parameters and includes the exact row `(495,247,123)` in group `[3,165]`
- Result 1.1 states the First Multiplier Theorem with the hypothesis `p > lambda`
- visual inspection of Table 2 together with the source legend shows that circled primes are not known to be forced multipliers and boxed primes cannot be multipliers
- on the exact `[3,165]` row, `2` is circled while `31` appears without a circle or box
- therefore the canonical source supports the row as open, supports `31` as an available multiplier entry for the row, and does not support the packet's use of `2` as an established multiplier
- no theorem / proposition / example / corollary / observation / sufficient-condition in the canonical source was found that directly settles the exact row

Recent follow-up / status check:
- Gordon's later paper *On Difference Sets with Small λ* still states the classical first multiplier theorem with the hypothesis that a prime divisor `p` of `n` satisfy `p > λ`
- that follow-up therefore does not rescue the packet's claim that `2 | n` alone makes `2` a multiplier here, because `2 < 123`
- the bounded exact-row web search outside the survey surfaced no later indexed exact-resolution hit for `(495,247,123)` in `[3,165]`

Prior-art verdict:
- `REDISCOVERY` is not established in the bounded audit
- the exact row remains source-anchored as an open theorem slice
- the no-later-resolution judgment is an inference from the bounded claim-specific search, not an absolute literature proof

## publication_statement_faithfulness
The selected problem remains faithful to the exact survey row. There is no group-notation drift, no quantifier drift, and no need to broaden the claim to identify the intended publication object.

What changes after audit is the strongest honest claim:
- it is not the exact nonexistence theorem written in the solve section
- it is instead a conditional obstruction plus a source-faithfulness diagnosis
- namely: if one could justify a translate with `2D = D`, then the `C_3` quotient would force a contradiction; the bounded audit does not justify that normalization for this row

The broader odd-order / `3`-divisible / even-nonsquare obstruction remains out of scope for publication from this packet.

## publication_theorem_worthiness
The target itself is theorem-worthy, but the current packet does not yet deliver the theorem.

Explicit answers:
- Is the strongest honest claim stronger than "here is an example"? Slightly, but only conditionally. The packet preserves a structural conditional lemma, not an exact theorem about the selected row.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Yes. The exact `[3,165]` existence / nonexistence question is a genuine title-theorem slice.
- Is the proof structural or merely instance-specific? The intended route is structural, not a hand-picked case search, but the present argument breaks at a structural multiplier step.
- Would this survive a referee asking "what is the theorem?" No. The referee-facing theorem exists as a target, but the packet does not yet prove it.
- Is the claim still too dependent on hand-picked small cases? No. The route is not search-heavy and does not depend on cherry-picked finite checks.

The theorem-worthiness of the selected row remains high. The theorem-worthiness of the current proof packet is presently low because the theorem is still missing.

## publication_publishability
If the exact `[3,165]` row were solved correctly, it would already constitute most of a publishable note. The best bounded estimate remains about `80%` of the paper from one correct solve: the family anchor, title theorem, and writeup narrative are already visible.

However, the current packet is not close to `PAPER_READY`.

Explicit answers:
- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? Yes.
- What percentage of the paper would one solve already provide? About `80%`.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? The candidate is genuinely attractive for the right reason, but the remaining gap in the current packet is not small; it is a load-bearing mathematical gap, not editorial cleanup.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. It should be cooled or retried only on the exact row, not widened into a broader multiplier program.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Lean would not seal the current packet. It becomes useful only after an exact theorem is actually proved.

Best bounded publication judgment:
- `publication_status = NONE` for the current packet
- not `PAPER_READY`
- not `SLICE_EXACT`
- the exact row remains a good micro-paper target, but this artifact is not yet a near-paper theorem packet

## publication_packet_audit
Packet strengths:
- exact source anchor
- clear note title and theorem slice
- preserved proof attempt and preserved proof-gap diagnosis
- no feeder-ladder packaging requirement if the exact row is eventually closed

Packet weaknesses:
- no verified exact theorem
- the load-bearing `2`-multiplier step is still unsupported
- the current artifact therefore does not yet shorten the final proof gap enough for a human-ready packet

Conservative publication-packet verdict:
- publication packet quality: `weak`
- proof artifacts preserved: `true`
- human-ready: `false`
- lean-ready: `false`

## micro_paper_audit
The row remains MICRO-PAPER-lane eligible as a target, but the current packet is not a near-paper packet.

Why the candidate still belongs in the lane:
- one exact solve still looks like the title theorem of a short note
- the family anchor is explicit and stable
- no broad campaign buildup is required after a correct solve

Why the current packet is not near HUMAN_READY:
- the audit shows that the packet leaned on an unresolved source-level multiplier, so the apparent last-mile proof distance was underestimated
- the remaining gap is mathematical and could still be substantial
- the right response is to preserve the packet and avoid concept drift, not to inflate it into a broader theorem program

Micro-paper verdict:
- the candidate did not only look attractive before audit
- the target remains a good exact one-shot slice
- the present solve artifact is still materially short of publishable-theorem status

## strongest_honest_claim
No exact existence or nonexistence theorem is currently verified for `(495,247,123)` in the abelian group `[3,165]`. The strongest honest mathematical claim preserved by this packet is conditional: if a hypothetical difference set in `[3,165]` could be translated to satisfy `2D = D`, then the `C_3` quotient would force an impossible integer square. That conditional observation does not settle the actual survey row, because the bounded audit did not justify `2` as a multiplier here and the canonical source itself marks `2` only as conjectural on this row.

## paper_title_hint
If an exact proof is later obtained, the right micro-paper title remains:

`The Abelian [3,165] (495,247,123) Difference-Set Case`

No stronger publication title is honest from the current packet.

## next_action
Do not widen this into the broader odd-order / `3`-divisible / even-nonsquare program.

Preserve the packet as an exact-row candidate and only re-enter solve with one of the following:
- a checked theorem that genuinely makes `2` a multiplier for this row
- a different exact argument that uses only justified source facts, for example the known `31`-multiplier structure

If neither route materializes quickly, cool or move aside the packet rather than building a feeder ladder.
