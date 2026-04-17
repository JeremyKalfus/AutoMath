# Solve Record: Does the cyclic group C_9423 admit a (9423,4711,2355)-difference set?

- slug: `cyclic-hadamard-difference-set-9423-4711-2355`
- working_packet: `artifacts/cyclic-hadamard-difference-set-9423-4711-2355/working_packet.md`

## statement_lock
Exact intended statement: determine whether the cyclic group `C_9423` admits a `(9423,4711,2355)`-difference set.

Equivalent title-theorem form if the solve closes:
`The cyclic group C_9423 admits no (9423,4711,2355)-difference set.`

Parameter lock:
- `v = 9423 = 3^3 * 349`
- `k = 4711`
- `lambda = 2355`
- `n = k - lambda = 2356 = 2^2 * 19 * 31`

The micro-paper target is exact-case disproof, not a looser witness search.

## definitions
Work additively in `G = Z/9423Z`.

A subset `D ⊂ G` is a `(v,k,lambda)`-difference set if `|D| = k` and every nonzero `g ∈ G` has exactly `lambda` ordered representations `g = d_1 - d_2` with `d_1,d_2 ∈ D`.

Standard identities used:
- `n = k - lambda = 2356`.
- For every nonprincipal character `chi` of `G`, `|chi(D)|^2 = n`.
- If a prime `p` divides `n` and `gcd(p,v)=1`, then `p` is a multiplier for an abelian difference set. Here `p=2`.

Conventions / ambiguities to lock:
- I use the standard translate-invariant formulation: replacing `D` by `D+a` preserves the difference-set property.
- I use the standard consequence of multiplier theory that if `t` is a multiplier and `gcd(t-1,v)=1`, then some translate of `D` is fixed by `t`.
- The subgroup of index `3` is `H = 3G`, so `|H| = 3141` and `G/H ≅ C_3`.

## approach_A
Structural / invariant route:

1. Use `2 | n` and `gcd(2,9423)=1` to invoke the multiplier theorem, so `2` is a multiplier.
2. Because `gcd(2-1,9423)=1`, translate `D` so that `2D = D`.
3. Pass to the quotient `G/H ≅ C_3`. Since doubling acts as multiplication by `2 ≡ -1 (mod 3)`, it swaps the two nonzero quotient classes, so the corresponding intersection numbers are equal.
4. Evaluate a nontrivial order-`3` character on `D`. The quotient symmetry forces the character sum to be an integer.
5. But every nonprincipal character value must have squared modulus `n = 2356`, so that integer would have square `2356`, impossible because `2356` is not a square.

Self-check after approach A:
- This route is case-specific, short, and theorem-shaped.
- The only delicate dependency is correct use of the multiplier/translate normalization step.

## approach_B
Construction / extremal / contradiction route:

1. Again normalize to `2D = D`.
2. Let `(x_0,x_1,x_2)` be the sizes of `D` on the three cosets of `H = 3G`.
3. Doubling symmetry gives `x_1 = x_2`.
4. Use the two exact counting equations
   - `x_0 + x_1 + x_2 = 4711`
   - `x_0^2 + x_1^2 + x_2^2 = k + lambda(|H|-1) = 4711 + 2355*3140 = 7399411`
5. Substitute `x_2=x_1`. Then
   - `x_0 + 2x_1 = 4711`
   - `x_0^2 + 2x_1^2 = 7399411`
6. Eliminating `x_0` yields
   - `6x_1^2 - 18844x_1 + 14794110 = 0`
   whose discriminant is `18844^2 - 24*14794110 = 37696 = 194^2`, but the roots are `(18844 ± 194)/12`, neither an integer.
7. Hence no integral coset profile exists.

Self-check after approach B:
- This gives an independent arithmetic contradiction using only quotient counts.
- It cross-checks the character argument and guards against a hidden mistake in the order-`3` character computation.

## lemma_graph
Lemma skeleton:

1. Multiplier lemma:
   Since `2 | n` and `gcd(2,v)=1`, `2` is a multiplier.
2. Fixed-translate lemma:
   Since `gcd(2-1,v)=1`, some translate of `D` satisfies `2D=D`.
3. Quotient-symmetry lemma:
   For `H=3G`, the induced action of `2` on `G/H ≅ C_3` swaps the two nonzero cosets, so their intersection sizes with `D` are equal.
4. Order-`3` character lemma:
   If `(x_0,x_1,x_1)` is the quotient profile, then for a nontrivial quotient character `psi`, `psi(D)=x_0+x_1ω+x_1ω^2=x_0-x_1 ∈ Z`.
5. Character-norm contradiction:
   Nonprincipal character sums satisfy `|psi(D)|^2=n=2356`, forcing an integer square equal to `2356`, contradiction.

Proof skeleton:
`multiplier -> fixed translate -> C_3 quotient symmetry -> real/integer order-3 character value -> nonsquare contradiction`.

## chosen_plan
Choose approach A as the main proof because it is shorter, cleaner, and already reads like the core theorem of a short note. Keep approach B as an internal consistency check and as a backup presentation if a referee prefers purely combinatorial quotient-count equations.

Self-check after plan choice:
- The main path produces a one-page argument.
- The backup path confirms the same obstruction without extra machinery beyond multiplier normalization.

## self_checks
Major-step checks:

1. Statement lock:
   The intended theorem is exact-case nonexistence, not a weaker obstruction.
2. Multiplier step:
   `2` is eligible because `2` is prime, `2 | 2356`, and `gcd(2,9423)=1`.
3. Translate normalization:
   `gcd(2-1,9423)=1`, so the usual fixed-translate argument applies.
4. Quotient step:
   The relevant index-`3` subgroup is canonical in `C_9423`, so the quotient is unambiguous.
5. Character step:
   The lifted nontrivial quotient character is nonprincipal on `G`, hence its squared modulus must equal `n`.
6. Arithmetic step:
   `2356 = 4*19*31` is not a perfect square.
7. Redundancy check:
   The pair-count contradiction in `approach_B` lands on the same nonexistence verdict.

## code_used
No code used.

The reasoning closed before any bounded experiment became necessary, so this solve attempt stays within the preferred no-code lane.

## result
Claim obtained in solve:

`C_9423` does not admit a `(9423,4711,2355)`-difference set.

Rigorous argument:

Assume `D ⊂ G = Z/9423Z` is a `(9423,4711,2355)`-difference set. Then `n = k-lambda = 2356`.

Because the prime `2` divides `n` and `gcd(2,9423)=1`, the standard multiplier theorem gives that `2` is a multiplier of `D`. Therefore `2D = D + t` for some `t ∈ G`. Since `gcd(2-1,9423)=1`, choose `a ∈ G` with `(2-1)a = -t`; then the translate `D' = D + a` satisfies `2D' = D'`. Replacing `D` by this translate, assume from now on that `2D = D`.

Let `H = 3G`, the subgroup of order `3141`, and let `pi : G -> G/H ≅ C_3` be the quotient map. Write
- `x_0 = |D ∩ H|`
- `x_1 = |D ∩ (1+H)|`
- `x_2 = |D ∩ (2+H)|`.

Because `2D=D`, multiplication by `2` permutes the quotient cosets while preserving their intersection sizes. On `G/H ≅ C_3`, multiplication by `2` exchanges the two nonzero classes, so `x_1 = x_2`.

Now let `psi` be a nontrivial character of `G/H`, with `psi(1+H)=ω` where `ω^2+ω+1=0`. Lift `psi` to a character `chi = psi ∘ pi` of `G`. This `chi` is nonprincipal, so the difference-set character identity gives

`|chi(D)|^2 = n = 2356`.

But

`chi(D) = x_0 + x_1ω + x_2ω^2 = x_0 + x_1(ω+ω^2) = x_0 - x_1`,

which is an integer because `x_1=x_2`. Hence `2356` would have to be the square of an integer. Since `2356 = 4*19*31` is not a perfect square, this is impossible.

Therefore no `(9423,4711,2355)`-difference set exists in `C_9423`.

Smallest supporting slice extracted from the proof:
- fixed-by-`2` normalization
- index-`3` quotient symmetry
- order-`3` character becomes integral
- nonsquare contradiction

Immediate corollary / boundary remark:
- The same proof template rules out any cyclic `(v,k,lambda)` difference set with `3 | v`, `2 | (k-lambda)`, `gcd(2,v)=1`, and nonsquare `k-lambda`, provided the standard multiplier normalization to a `2`-fixed translate is available.

What scales:
- the index-`3` quotient plus `2`-multiplier argument
- the conclusion that the order-`3` character value is integral

What does not automatically scale:
- cases with `3 ∤ v`
- cases where `2 ∤ n`
- cases where `n` is already a square

Current package assessment:
- This is closer to a paper-shaped exact case than to a thin instance-only computation.
- In solve-stage bookkeeping it should still be treated conservatively until verify checks the multiplier dependency and prior-art status.

## family_affinity
Very high family affinity.

This is not an isolated curiosity: it settles one named residual case from the small cyclic Hadamard survivor list. The proof uses family-typical ingredients, namely multiplier normalization and low-index quotient characters, rather than ad hoc search.

If verified, the result already sits in the intended family narrative: eliminate one survivor from the sub-`10000` cyclic Hadamard table.

## generalization_signal
Real theorem-slice signal is visible.

The proof suggests the following exact slice:

`If a cyclic (v,k,lambda)-difference set has 3 | v, gcd(2,v)=1, 2 | (k-lambda), and k-lambda is not a square, then the 2-multiplier forces an index-3 quotient character value to be integral, contradicting |chi(D)|^2 = k-lambda.`

That slice needs careful verify-stage checking for novelty and scope, but it is mathematically genuine and extracted directly from the solved case.

## proof_template_reuse
Reusable template:

1. Find a prime multiplier `p` dividing `n = k-lambda`.
2. Normalize to a `p`-fixed translate when `gcd(p-1,v)=1`.
3. Choose a low-index quotient where multiplication by `p` collapses two character-conjugate classes.
4. Show a nontrivial character sum becomes rational or integral.
5. Compare against the forced norm equation `|chi(D)|^2 = n`.

For this case the sweet spot is `p=2` and the quotient of order `3`.

## candidate_theorem_slice
Candidate slice:

`No cyclic difference set with 3 dividing the group order and nonsquare n = k-lambda can survive a 2-multiplier normalization when 2 divides n and gcd(2,v)=1, because the order-3 character sum becomes an integer whose square must equal n.`

This is the smallest theorem slice naturally suggested by the proof. It is stronger than a one-off computation but still close enough to the exact case to keep packaging cheap.

## smallest_param_shift_to_test
Best next parameter shifts if this exact proof is to be stress-tested rather than broadened immediately:

1. Other unresolved cyclic Hadamard cases with `3 | v` and nonsquare `n`.
2. Nearby non-Hadamard cyclic difference-set candidates where `v` is divisible by `3` and `2 | n`.

What would help most is not a broad campaign, but one or two exact tuples where the same index-`3` quotient obstruction can be checked cleanly.

## why_this_is_or_is_not_publishable
If the argument survives verify, it is close to publishable in the micro-paper lane.

Why it is publishable:
- the title theorem is exact and already family-labeled
- the proof is short and structural
- the result removes a named survivor from a canonical open list
- the remaining exposition burden is light

Why solve should still be conservative:
- verify must confirm multiplier normalization is stated with the right hypotheses
- verify must confirm no earlier source already contains this exact index-`3` obstruction for `9423`

Estimated solve-to-paper fraction if the proof checks out: about `0.8` to `0.9`.

Minimal remaining packaging work:
- state the multiplier lemma cleanly with citation
- present the one-paragraph quotient-character proof
- add a short literature paragraph placing `9423` among the residual cyclic Hadamard cases
- decide whether to advertise only the exact case or also the extracted theorem slice

If verify finds the slice already known, the exact case still looks like a short-note theorem. If verify finds the exact case already settled, the packet drops to rediscovery.

## paper_shape_support
Exact title theorem:

`The cyclic group C_9423 admits no (9423,4711,2355)-difference set.`

What makes it paper-shaped if verified:
- one clean theorem with immediate family context
- a compact proof using standard but nontrivial tools
- no feeder ladder or large computation needed

One immediate natural remark:
- the obstruction is driven entirely by the interaction of the `2`-multiplier with the index-`3` quotient, so the decisive arithmetic is visible at very low compression depth.

Current micro-paper verdict from solve:
- not too thin for the lane
- already much closer to a paper-shaped claim than to a raw instance computation
- still awaiting verify before claiming `PAPER_READY`

## boundary_remark
Boundary of the argument:

The proof is exquisitely tied to the presence of an index-`3` quotient and a `2`-multiplier. It does not say that all remaining cyclic Hadamard survivors fail for similar reasons, and it should not be oversold as a broad elimination theorem without careful verify-stage novelty checking.

This case matters because it shows that one of the canonical survivors may collapse under a very shallow quotient obstruction rather than deep search or heavy field-descent machinery.

## likely_failure_points
Main points verify should stress:

1. Exact multiplier citation and hypothesis match for `p=2`.
2. Translate normalization from `2D = D+t` to a `2`-fixed translate.
3. Whether the order-`3` character argument, or an equivalent quotient-count contradiction, already appears in prior work for this case or as a known general theorem.
4. Whether any hidden convention difference in the local packet changes the intended parameterization.

I do not currently see a mathematical gap inside the proof skeleton once the multiplier step is accepted.

## what_verify_should_check
Verify should check:

1. The standard multiplier theorem indeed applies exactly as used to cyclic `(9423,4711,2355)` difference sets.
2. The fixed-translate argument is stated correctly and does not require an extra hypothesis beyond `gcd(2-1,9423)=1`.
3. The lifted quotient character is nonprincipal and therefore subject to `|chi(D)|^2 = n`.
4. The exact tuple `(9423,4711,2355)` has not already been ruled out in the literature by this same argument.
5. Whether the broader slice in `candidate_theorem_slice` is already known, which affects packaging but not the exact-case solve.

## verify_rediscovery
PASS 1 used a bounded prior-art audit focused on the exact tuple and the named cyclic-Hadamard survivor list.

Primary-source outcomes:
- Baumert-Gordon 2004, Table 5, still lists `9423 4711 2355` as `Open`.
- Gordon's 2019 La Jolla Difference Set Repository slides still say the cyclic Hadamard cases are confirmed for all but seven cases with `v <= 10000`, and the seven-case table again includes `9423 4711 2355`.
- Bounded exact-tuple and alternate-notation web searches did not surface a later paper, note, repository entry, or discussion explicitly settling the exact case.

Verifier decision:
- No rediscovery was established within the bounded audit.
- The novelty check is still bounded rather than exhaustive, so this supports `VERIFIED` rather than an overconfident publication claim.

## verify_faithfulness
The solve packet stays faithful to the intended statement.

Checks:
- The intended statement is exact-case existence for a cyclic `(9423,4711,2355)` difference set in `C_9423`.
- The solve record proves the exact negation of that statement, not a weakened proxy and not a different group/family claim.
- The main argument uses only translation invariance, the `2`-multiplier normalization, the index-`3` quotient, and the standard character norm identity. No quantifier drift or definition change was found.

Faithfulness verdict:
- No wrong-theorem drift found.

## verify_proof
First incorrect step in the main proof:
- None found.

Main-proof check:
- The proof only needs the standard first multiplier theorem for abelian difference sets with `p | n` and `gcd(p,v)=1`, applied with `p = 2`.
- The translate-normalization step from `2D = D + t` to a translate `D'` with `2D' = D'` is correct because `gcd(2-1,9423)=1`.
- In the quotient `G/H ≅ C_3` with `H = 3G`, multiplication by `2` swaps the two nonzero classes, so the profile satisfies `x_1 = x_2`.
- For a nontrivial quotient character, `chi(D) = x_0 + x_1 omega + x_2 omega^2 = x_0 - x_1` is an integer.
- Since `chi` is nonprincipal, `|chi(D)|^2 = n = 2356`, but `2356 = 4 * 19 * 31` is not a square. Contradiction.

Important correction:
- The backup quotient-count route in `approach_B` is not correct as written.
- The solve record claims `37696 = 194^2`; this is false, since `194^2 = 37636`.
- So `approach_B` cannot be cited as an independent corroboration in its present form.
- This does not affect the main proof, which is self-contained and does not depend on the discriminant calculation.

Proof verdict:
- Main proof verified.
- Backup proof sketch failed as written and should be treated only as a repairable side note.

## verify_adversarial
No checker or code artifact exists for this candidate, so adversarial verification was mathematical rather than computational.

Checks performed:
- Recomputed `n = 4711 - 2355 = 2356` and confirmed it is not a square.
- Recomputed the `approach_B` quadratic and confirmed the discriminant claim in the solve record is arithmetically wrong.
- Checked that this arithmetic bug does not propagate into the main `2`-multiplier plus order-`3` character argument.

Adversarial verdict:
- No break found in the main proof.
- One real arithmetic error found in the auxiliary backup route.

## verify_theorem_worthiness
Exactness:
- The verified claim is exact-case nonexistence for the selected tuple.

Novelty:
- Bounded prior-art checking did not show rediscovery.
- The broader extracted slice may well overlap known multiplier/quotient folklore, so the exact-case theorem is the safest publication claim.

Reproducibility:
- High. The main proof is short, symbolic, and checkable line by line without search or heavy computation.

Lean readiness:
- Not yet.
- The remaining bottleneck to a sealed packet is publication positioning and audit discipline, not formalization throughput.
- Lean would be optional formal sealing, not the shortest path to a human-ready packet.

Paper leverage:
- If correct and later audit-cleared, this already constitutes most of a publishable short note because it removes a named survivor from a canonical cyclic-Hadamard open list.
- Estimated single-solve contribution to a paper: about `0.78`.
- Visible title theorem: `The cyclic group C_9423 admits no (9423,4711,2355)-difference set.`

What scales:
- The local mechanism `2`-multiplier -> fixed translate -> `C_3` quotient symmetry -> integral order-`3` character value -> nonsquare contradiction.

What does not clearly scale:
- Any broad claim beyond cases with `3 | v`, `2 | n`, and an available `2`-multiplier normalization.
- The publication-level novelty of the broader theorem slice was not established in this verify pass.

Best honest publication status:
- `SLICE_CANDIDATE`, not `PAPER_READY` yet.
- This is stronger than `INSTANCE_ONLY` because the exact residual case already reads like a title theorem in a named family, but it still needs publication audit and careful literature positioning.

## verify_verdict
`VERIFIED`

Reason:
- No rediscovery was established in the bounded audit.
- No flaw was found in the main proof of nonexistence.
- The classification must remain below `EXACT` because Lean has not been completed.

## minimal_repair_if_any
Minimal conservative repair:
- Do not use `approach_B` as supporting evidence in its current form.
- The only verified proof artifact for this run is the main `2`-multiplier plus order-`3` character argument.
- If the backup route is retained later, its discriminant arithmetic must be rewritten from scratch before reuse.

## publication_prior_art_audit
Bounded prior-art pass completed on `2026-04-15`.

Exact-statement search:
- Queries of the form `"9423 4711 2355" difference set` and `"(9423,4711,2355)"` surfaced the canonical Baumert-Gordon 2004 source and later status material, but no later paper or note explicitly settling the exact tuple.

Alternate-notation search:
- Queries using `cyclic Hadamard 9423`, `C_9423 difference set`, and the exact parameter triple again returned family-status sources rather than a later exact-case resolution.

Canonical-source check:
- Baumert-Gordon 2004, Table 5, still lists `9423 4711 2355` as `Open` among the cyclic Hadamard cases.
- Within that source, the surrounding eliminations are attached to named theorems or filters for other rows; no theorem, proposition, example, corollary, observation, or sufficient condition in the bounded canonical check appears to settle the exact `9423` row indirectly.

Outside-source status pass:
- Daniel Gordon's 2019 ArasuFest slide deck, in the `Small Open Cases` cyclic-Hadamard slide, still includes `9423 4711 2355` among the seven unresolved cases with `v <= 10000`.
- A bounded 2026 follow-up search surfaced a Hong-Yeop Song slide snippet repeating the same seven surviving cyclic Hadamard values, again including `9423`.

Prior-art verdict:
- Within this bounded audit, no rediscovery was found and no broader published theorem was located that already disposes of the exact `9423` case.
- The honest claim here is still an exact-case frontier resolution rather than a rediscovered folklore corollary.

## publication_statement_faithfulness
The audited packet stays faithful to the selected problem.

Checks:
- The strongest audited claim is still the exact negation of the intended statement: no cyclic `(9423,4711,2355)` difference set exists in `C_9423`.
- The proof does not drift to a different ambient group, a weaker proxy statement, or an unverified broader family theorem.
- The broader slice suggested in solve remains packaging context only; the publication-facing claim should stay at the exact `9423` case.

Faithfulness verdict:
- Yes, the strongest honest claim is stronger than "here is an example."
- No theorem drift was found.

## publication_theorem_worthiness
The theorem-worthiness check passes.

Assessment:
- There is a real title theorem here: `The cyclic group C_9423 admits no (9423,4711,2355)-difference set.`
- This would survive a referee asking "what is the theorem?" because the theorem is exact, family-labeled, and directly removes a named survivor from a canonical open list.
- The proof is structural rather than merely instance-specific: the decisive mechanism is the `2`-multiplier normalization followed by the index-`3` quotient character obstruction.
- The packet is still exact-case and should not be oversold as a broad new general theorem, but it is not merely a hand-picked small example either.
- Dependence on small-case accident is limited: the case is singled out by the literature itself, and the proof uses standard family tools rather than bespoke computation.

Theorem-worthiness verdict:
- Strong exact-case theorem slice.
- Best honest theorem slice for publication purposes is still the exact `9423` nonexistence result, not the broader extracted pattern.

## publication_publishability
Publishability audit is favorable.

Answers to the stage questions:
- Would this already constitute most of a publishable note if correct and verified in the current bounded sense? Yes.
- Estimated single-solve contribution to the paper: about `0.84`.
- Is there a real title theorem or counterexample theorem? Yes, the exact-case nonexistence theorem above.
- Is the remaining gap genuinely small? Yes. What remains is bounded citation pinning, omission or repair of the broken backup route, and short-note packaging.
- Should this be moved aside rather than expanded into a larger theorem program? Yes. Move it off the main discovery queue as a human-ready exact-case note; do not expand it into a broader theorem campaign from this packet.
- Would Lean directly seal the packet? No. Lean is optional secondary formalization here, not the gate to publication worthiness.

Publishability verdict:
- The bounded audit supports `PAPER_READY`.
- The result looks like a short publishable note rather than a merely correct but too-thin instance.

## publication_packet_audit
Packet-quality verdict: human-ready, with one explicit caution.

What is preserved well enough:
- The main proof artifact is short, structural, and easy to restate cleanly.
- The literature positioning is bounded but sufficient for a conservative micro-paper packet.
- The exact title theorem and family context are already legible from the current artifacts.

What must not be used as evidence:
- `approach_B` is arithmetically broken as written and should be omitted from any packet unless repaired independently.

Packet verdict:
- `publication_status = PAPER_READY`
- `publication_confidence = medium-high`
- `publication_packet_quality = human-ready`
- `proof_artifacts_preserved = true`

## micro_paper_audit
This candidate passes the strict micro-paper lane.

Why it passes:
- The exact claim is already the title theorem of a short note.
- The family anchor is strong because `9423` is one of the named residual cyclic Hadamard survivors.
- The proof is short and structural, so editorial overhead stays low.
- The packet does not require a feeder ladder, broad campaign buildup, or heavy computational appendix.

Conservative limits:
- The broader extracted slice may overlap known folklore and should not carry the publication claim.
- The paper should stay focused on the exact `9423` case.

Micro-paper verdict:
- This did not merely look attractive before audit; it remains genuinely close to a paper.
- Best honest audit label: `PAPER_READY`.

## strongest_honest_claim
Within the bounded verify and publication audit, the strongest honest claim is:

`The cyclic group C_9423 admits no (9423,4711,2355)-difference set.`

More explicitly:
- Baumert-Gordon 2004 still anchors the exact tuple as an open cyclic Hadamard survivor.
- Gordon's 2019 status slide and a bounded 2026 follow-up status check still treat `9423` as unresolved.
- The preserved proof gives a short structural disproof: a `2`-fixed translate forces equal occupancy of the two nonzero classes modulo `3`, so a nonprincipal order-`3` character value becomes an integer, contradicting `|chi(D)|^2 = 2356`.

## paper_title_hint
On the Nonexistence of a Cyclic `(9423,4711,2355)` Difference Set

## next_action
Mark this packet `PAPER_READY` / `HUMAN_READY`, move it to the secondary Lean queue without blocking new discovery work, and draft the note around the exact `9423` theorem only.

Implementation note:
- cite the multiplier step cleanly,
- cite Baumert-Gordon 2004 plus the 2019 status slide,
- mention the bounded 2026 follow-up status check,
- omit `approach_B` unless it is separately repaired.
