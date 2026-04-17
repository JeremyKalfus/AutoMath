# Solve Record: Does the cyclic group C_963 admit a (963,222,51)-difference set?

- slug: `cyclic-difference-set-963-222-51`
- working_packet: `artifacts/cyclic-difference-set-963-222-51/working_packet.md`

## statement_lock
Determine whether the cyclic group C_963 admits a (963,222,51)-difference set.

The exact intended title theorem, if the nonexistence route closes, is:
"The cyclic group C_963 does not admit a (963,222,51)-difference set."

If that closes cleanly, it would already supply roughly 70-90% of a micro-paper: the case is isolated, the literature stop-line is already fixed by the working packet, and the remaining work is mainly exposition plus a bounded verification packet.

## definitions
Let G = C_963, and write a hypothetical difference set as D subseteq G with parameters
v = 963, k = 222, lambda = 51, n = k - lambda = 171.

Use the group-ring identity
D D^(-1) = n + lambda G.

For the quotient G -> C_9, let
B = sum_{j=0}^8 b_j x^j
where b_j counts elements of D in the j-th residue class mod 9.
Then
sum b_j = 222,
B B^(-1) = 171 + 5457 C_9,
hence
sum b_j^2 = 5628
and for every nonzero shift t mod 9,
sum_j b_j b_{j-t} = 5457.

For the further quotient C_9 -> C_3, define
c_r = b_r + b_{r+3} + b_{r+6}  for r = 0,1,2.
Then sum c_r = 222 and the nonprincipal C_3 character values also have squared modulus 171.

For the quotient G -> C_107, let
A = sum_{u=0}^{106} a_u y^u
where a_u counts elements of D in the u-th residue class mod 107.
Then
sum a_u = 222,
A A^(-1) = 171 + 459 C_107,
sum a_u^2 = 630,
and for every nonzero shift s mod 107,
sum_u a_u a_{u-s} = 459.

## approach_A
Structural / invariant route through small quotients.

1. Contract to C_9 and then to C_3.
2. Use the exact character equation |chi(B)|^2 = 171 for every nonprincipal character of C_9.
3. For the C_3 contraction c = (c_0,c_1,c_2), solve the Eisenstein norm equation forced by
   |c_0 + c_1 omega + c_2 omega^2|^2 = 171
   with c_0 + c_1 + c_2 = 222.
4. This yields a rigid block-sum profile:
   {c_0,c_1,c_2} = {81,75,66}.
5. The remaining task is then to determine whether any 9-tuple b_0,...,b_8 of nonnegative integers with those three block sums can satisfy the full cyclic autocorrelation equations on C_9.

This is attractive because a contradiction at the C_9 level is already a rigorous nonexistence proof for the original cyclic difference-set question.
In the bounded search recorded below, this route did not close: admissible C_9 lifts do exist.

## approach_B
Construction / extremal / contradiction route through the C_107 contraction.

1. Contract to Q = G / C_9 congruent to C_107 and let A = sum_{u in Q} a_u [u].
2. Because each Q-coset has size 9, every coefficient satisfies 0 <= a_u <= 9 and sum a_u = 222.
3. Use the contracted w-multiplier theorem with w = 107 and t = 19.
4. Since n = 171 = 3^2 * 19, and modulo 107 we have 19 congruent 19^1 and also 19 congruent 3^95, Theorem 3.2 of Baumert-Gordon makes 19 a 107-multiplier of D.
5. Therefore, after quotienting to Q and translating once, the contracted element can be made fixed by u -> 19u.
6. On C_107, multiplication by 19 has order 53, so the orbit decomposition is
   {0} union O_1 union O_2
   with |O_1| = |O_2| = 53.
7. Orbit constancy then forces
   222 = a_0 + 53(alpha + beta),
   so a_0 congruent 10 mod 53.
   But also 0 <= a_0 <= 9, impossible.

This route closes the nonexistence proof.

## lemma_graph
Lemma graph currently visible inside the allowed scope:

1. Hypothetical cyclic (963,222,51)-difference set D
   -> quotient to C_9 gives an integer 9-tuple b with constant nonzero cyclic correlation 5457.
2. The same quotient
   -> further contraction to C_3 gives c = (c_0,c_1,c_2) with
   c_0 + c_1 + c_2 = 222 and
   |c_0 + c_1 omega + c_2 omega^2|^2 = 171.
3. Solving that norm equation
   -> {c_0,c_1,c_2} = {81,75,66}.
4. Therefore any existence proof must pass through a very small list of C_9 block-sum types.
5. If no C_9 lift exists, the original difference set cannot exist.
6. Separately, the C_107 contraction plus the 107-multiplier theorem yields an orbit obstruction on C_107.
7. That orbit obstruction is incompatible with the weight 222 and the kernel-size bound a_u <= 9.
8. Therefore the original cyclic difference set does not exist.

## chosen_plan
Chosen path executed:

1. Lock the quotient identities in the record.
2. Extract the C_3 block-sum slice {81,75,66} from the C_9 contraction.
3. Run a bounded exact search on the C_9 contraction; this found admissible lifts, so the small-quotient route alone is not enough.
4. Switch to the already-identified C_107 multiplier route.
5. Use the contracted 107-multiplier theorem, normalize by translation on C_107, compute the 19-orbit structure, and derive the weight contradiction.

## self_checks
- Check 1: n = k - lambda = 222 - 51 = 171.
- Check 2: For the C_9 contraction, the kernel size is 107, so the off-identity quotient correlation is 51 * 107 = 5457 and the identity coefficient is 171 + 5457 = 5628.
- Check 3: For the C_107 contraction, the kernel size is 9, so the off-identity quotient correlation is 51 * 9 = 459 and the identity coefficient is 171 + 459 = 630.
- Check 4: For c_r = b_r + b_{r+3} + b_{r+6}, writing c_r = 74 + d_r with d_0 + d_1 + d_2 = 0, the nonprincipal C_3 norm equation becomes d_0^2 + d_1^2 + d_2^2 = 114, whose integer solutions are permutations of (7,1,-8). Hence {c_0,c_1,c_2} = {81,75,66}.
- Check 5: The bounded C_9 search produced actual lifts, so that route was correctly abandoned as insufficient rather than silently promoted into a proof.
- Check 6: For the final proof, the only external theorem input is the contracted 107-multiplier theorem: since n = 3^2 * 19, with 19 congruent 19^1 mod 107 and 3^95 congruent 19 mod 107, Theorem 3.2 of Baumert-Gordon makes 19 a 107-multiplier.
- Check 7: On C_107, (19/107) = -(107/19) = -(12/19) = 1, so 19^53 congruent 1 mod 107. Since 19 is not congruent 1 mod 107 and 53 is prime, ord_107(19) = 53.
- Check 8: Translation normalization on C_107 is valid because gcd(19 - 1, 107) = gcd(18,107) = 1.

## code_used
One bounded exact experiment was used.

Purpose:
test whether the C_3 block-sum obstruction already kills the C_9 contraction.

What was checked:
all ordered 9-tuples b_0,...,b_8 compatible with block sums {81,75,66} and the exact C_9 shift equations.

Outcome:
admissible C_9 lifts exist, so the C_9 route by itself is insufficient.

Role in the final argument:
diagnostic only. The final nonexistence proof does not depend on code.

## result
Result: COUNTEREXAMPLE / nonexistence proof for the exact cyclic case.

Claim.
The cyclic group C_963 does not admit a (963,222,51)-difference set.

Proof.
Assume D subseteq G = C_963 is a cyclic (963,222,51)-difference set. Let N be the unique subgroup of order 9, and let Q = G / N congruent to C_107. Write the contraction of D to Q as
A = sum_{u in Q} a_u [u],
so each coefficient a_u counts points of D in one N-coset. Therefore
0 <= a_u <= 9
for every u, and
sum_{u in Q} a_u = |D| = 222.

Now n = 171 = 3^2 * 19. We only need a multiplier statement on the quotient Q congruent to C_107. By Theorem 3.2 of Baumert-Gordon, if for each prime divisor p of n there is an exponent j with
p^j congruent t mod 107,
then t is a 107-multiplier of D. Take t = 19. For the prime divisor 19 this is immediate, and for the prime divisor 3 we have
3^95 congruent 19 mod 107.
Hence 19 is a 107-multiplier of D, so after passing to Q there is some q^s in Q such that
A^(19) = q^s A.

Because gcd(19 - 1,107) = 1, choose c with
(19 - 1)c congruent s mod 107,
and set
B = q^(-c) A.
Then
B^(19) = B.
So the coefficients of B are constant on the multiplication-by-19 orbits in Q.

It remains to compute those orbits. Since 107 is prime,
19^53 congruent (19/107) mod 107
by Euler's criterion. Quadratic reciprocity gives
(19/107) = -(107/19) = -(12/19) = 1,
so 19^53 congruent 1 mod 107. Because 19 is not congruent 1 mod 107 and 53 is prime, ord_107(19) = 53.
Therefore the action u -> 19u on Q has exactly three orbits:
{0}, O_1, O_2
with |O_1| = |O_2| = 53.

Hence B has the form
B = b_0 [0] + alpha sum_{u in O_1} [u] + beta sum_{u in O_2} [u]
with integers b_0, alpha, beta satisfying 0 <= b_0, alpha, beta <= 9.
Taking total coefficient sum gives
222 = b_0 + 53(alpha + beta).
Reducing mod 53 yields
b_0 congruent 222 congruent 10 mod 53.
But also 0 <= b_0 <= 9, impossible.

This contradiction proves that no cyclic (963,222,51)-difference set exists. QED.

Self-check after the main proof:
the contradiction uses only the quotient size 107, the kernel size 9, the exact weight 222, and the multiplier-orbit decomposition. No hidden search assumption enters the final step.

## family_affinity
High. The final proof is not an ad hoc witness check; it is anchored exactly in the [9,107] factorization that made this row a named Ryser/Lander residue in the first place.

## generalization_signal
Moderate. What scales is the orbit-count contradiction template:
if a prime multiplier t acts on a prime quotient C_q with one fixed point and large equal nonzero orbit sizes, and the kernel-size bound is smaller than k mod |O|,
then the quotient weight can force an immediate contradiction.

What does not scale automatically:
the case-specific input that 19 is an available multiplier and that ord_q(t) = (q - 1) / 2 for q = 107.

## proof_template_reuse
The reusable template is:
abelian difference set -> contract to a prime quotient -> invoke an available prime multiplier -> translate-normalize to true invariance -> read off orbit sizes -> compare the orbit decomposition with the quotient weight and kernel-size bounds.

## candidate_theorem_slice
Candidate theorem slice suggested by the proof:

Let G be cyclic of order m q with q prime and let D be a cyclic difference set in G. If a prime multiplier t acts on the quotient C_q with one fixed point and all other orbits of size h, then after translation-normalization the quotient contraction has coefficient sum
k = a_0 + h * M.
Whenever the kernel-size bound forces 0 <= a_0 < k mod h, this yields immediate nonexistence.

## smallest_param_shift_to_test
The most useful next parameter shifts are:

1. Other isolated cyclic [9,q] rows where some prime divisor of n outside v has orbit size (q - 1) / 2 on C_q.
2. Nearby [27,q] rows where the same multiplier-orbit argument might survive but the larger kernel bound may stop the final congruence contradiction.

## why_this_is_or_is_not_publishable
This now looks publishable in the micro-paper lane, subject to verification.

Why:
the exact named frontier row is closed by a short human-readable nonexistence proof using the family-defining [9,107] quotient structure and a standard multiplier input.

Whether this is already 70-90% of a paper:
yes. The mathematical core is now in place; the remaining work is mainly proof polishing, a bounded prior-art recheck, and a concise narrative around why the [9,107] residue mattered.

Minimal remaining packaging work:
state the contracted 107-multiplier input cleanly, present the quotient normalization in polished notation, and add one paragraph explaining how the orbit-size contradiction fits the La Jolla open-case framing.

## paper_shape_support
The result is now paper-shaped.

- title theorem: "The cyclic (963,222,51) difference-set case is impossible."
- smallest supporting theorem slice: the quotient-orbit obstruction lemma recorded above.
- natural immediate remark: the proof explains exactly why the [9,107] split is the operative obstruction surface.
- remaining packaging: verify the multiplier citation and write the literature stop-line cleanly.

## boundary_remark
Immediate boundary remark:

The proof is strong enough to kill the exact row, but it is not a blanket theorem for all cyclic [9,q] cases. Its decisive step is the congruence
222 = a_0 + 53(alpha + beta),
which depends both on the kernel bound a_0 <= 9 and on the specific half-order orbit size 53 coming from 19 modulo 107.

## likely_failure_points
1. Verification must confirm the exact contracted-multiplier citation: the proof needs 19 as a 107-multiplier, not a blanket numerical multiplier of D.
2. Verification should check the translation-normalization step carefully so there is no sign or indexing slip in passing from A^(19) = q^s A to a fixed contraction.
3. The C_9 experiment should remain clearly labeled as diagnostic only, not part of the proof.

## what_verify_should_check
1. Recheck the quotient identities and the kernel-size factors 107 and 9.
2. Verify the contracted 107-multiplier input for 19 explicitly and cite Baumert-Gordon Theorem 3.2 (or the equivalent Lander formulation) cleanly in the publication packet.
3. Recheck the orbit computation ord_107(19) = 53.
4. Recheck the translation-normalization step on C_107.
5. Confirm that the final contradiction uses only the quotient coefficient bound 0 <= a_u <= 9 and the weight 222.
6. Keep the bounded C_9 search as a side note only: it explains route selection, not theorem validity.

## verify_rediscovery
PASS 1 used a bounded prior-art sweep on the exact tuple `(963,222,51)`, the alternate family notation `[9,107]`, the canonical Gordon La Jolla slide deck, same-source theorem/example/open-case checks, and a recent status sweep aimed at 2020-2026 closure signals.

Outcome:
- the canonical source still isolates the cyclic row `(963,222,51,171)` / `[9,107]` as open;
- the bounded sweep did not surface a later paper, repository note, or discussion explicitly settling this exact cyclic instance;
- no direct implication or explicit construction/nonexistence result for this exact row was found within budget.

Rediscovery was therefore not established in PASS 1. This is only a bounded novelty check, so final publication audit should still cite the stop-line carefully, but the run should not be archived as a rediscovery.

## verify_faithfulness
The claimed solved statement matches the intended statement exactly.

- intended statement: determine whether `C_963` admits a `(963,222,51)` difference set;
- solved claim: `C_963` does not admit a `(963,222,51)` difference set.

No wrong-theorem drift, quantifier drift, or changed ambient group was found. The auxiliary `C_9` computation is clearly marked as diagnostic and is not substituted for the actual theorem claim. The final proof is genuinely about the exact named cyclic row.

## verify_proof
First incorrect step found: none.

Load-bearing checks:
- the only external theorem input needed is the contracted `107`-multiplier theorem for cyclic difference sets;
- here `n = 171 = 3^2 * 19`, with `19 ≡ 19^1 (mod 107)` and `3^95 ≡ 19 (mod 107)`, so Baumert-Gordon Theorem 3.2 makes `19` a `107`-multiplier;
- passing from that `107`-multiplier statement to `A^(19) = q^s A` in the `C_107` quotient is faithful;
- the translation-normalization step is valid because `gcd(19 - 1,107) = 1`, so one can choose `c` with `(19 - 1)c ≡ s (mod 107)` and obtain a translated contraction fixed by multiplication by `19`;
- fixedness under the multiplier action forces coefficient constancy on the multiplication-by-`19` orbits of `C_107`;
- `ord_107(19) = 53`, so the orbit decomposition is exactly `[1,53,53]`;
- the translated contraction still has coefficient bounds `0 <= a_u <= 9` because translation only permutes the quotient cosets.

The contradiction
`222 = a_0 + 53(alpha + beta)`
with `0 <= a_0 <= 9` is therefore rigorous. The proof does not depend on the diagnostic `C_9` search.

## verify_adversarial
No separate checker file exists in the artifact directory, so PASS 4 reran the arithmetic directly.

Recomputed checks:
- `gcd(18,107) = 1`;
- `19^53 ≡ 1 (mod 107)`;
- the multiplication-by-`19` action on `Z/107Z` has orbit sizes `[1,53,53]`;
- there is no triple `(a_0, alpha, beta)` with each entry in `{0,...,9}` satisfying `a_0 + 53(alpha + beta) = 222`;
- the recorded `C_3` norm slice also checks out: the only integer deviations with sum `0` and squared sum `114` are permutations of `(-8,1,7)`, giving the block sums `{66,75,81}`.

No adversarial break of the final proof surfaced.

## verify_theorem_worthiness
Exactness:
The theorem slice is exact. This is the named cyclic row itself, not a proxy instance or weakened reformulation.

Novelty:
PASS 1 did not establish rediscovery. Within the bounded audit budget, the exact row still appears frontier-novel.

Reproducibility:
High. The argument is short, human-readable, and depends only on a standard contracted-multiplier theorem plus explicit modular arithmetic on the `107`-quotient.

Lean readiness:
Not yet on the critical path. The remaining bottleneck is publication audit and clean source anchoring, not formalization.

Paper leverage:
Strong. If correct and later Lean-sealed, this already looks like most of a publishable note because the exact title theorem, frontier stop-line, and family anchor are already visible.

Explicit audit answers:
- would this result, if correct and Lean-sealed, already constitute most of a publishable note? Yes.
- what percentage of the paper would one solve already provide? About `0.80`.
- what title theorem is actually visible? `The cyclic group C_963 admits no (963,222,51)-difference set.`
- what part of the argument scales? The prime-quotient multiplier-orbit obstruction template.
- what part clearly does not? The case-specific availability of the `19` as a `107`-multiplier, the half-order orbit size `53`, and the decisive kernel bound `a_0 <= 9`.
- is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? No. The best honest status is `SLICE_CANDIDATE`.

## verify_verdict
`VERIFIED`

## publication_prior_art_audit
Bounded publication audit completed on 2026-04-15.

Exact-statement search:
- exact tuple searches on `(963,222,51)` and `cyclic 963 222 51 difference set` surfaced Gordon's 2019 slide deck as the clear canonical frontier source and did not surface a later exact closure within the audit budget.

Alternate-notation search:
- the alternate notation `[9,107]` surfaced the same Gordon open-case framing and no later exact paper or repository note settling that precise cyclic row.

Canonical-source check:
- Gordon's ArasuFest slides still list `963 222 51 171` among the Ryser small open cyclic cases and list `[9,107]` among the Lander small open cases.

Theorem / proposition / example / corollary / observation check inside the canonical source:
- the canonical source frames the row as open; it does not already contain a theorem, proposition, example, observation, or sufficient condition that visibly settles the exact cyclic `[9,107]` row.

Outside-source status check:
- the bounded outside search did not produce a post-2019 paper, note, or discussion explicitly claiming existence or nonexistence for the exact cyclic `(963,222,51)` case.

Follow-up check needed by a concrete ambiguity:
- the solver record originally cited a blanket prime-multiplier step. A follow-up source check against Baumert-Gordon's 2003 paper shows the proof should instead use the weaker and sufficient `w`-multiplier theorem with `w = 107`.

Publication-audit verdict on prior art:
- bounded audit did not establish rediscovery as of 2026-04-15, but the stop-line should remain explicitly bounded in any writeup.

## publication_statement_faithfulness
The intended statement and the strongest solved statement still match exactly:
"The cyclic group C_963 does not admit a (963,222,51)-difference set."

The only faithfulness correction needed is inside the proof packaging:
- the argument should not be described as proving that `19` is a full numerical multiplier of `D`;
- what the bounded source check supports is that `19` is a `107`-multiplier after contraction to `C_107`, which is exactly the amount of multiplier input the proof uses.

With that correction, the theorem claim is faithful to the intended selected-problem packet.

## publication_theorem_worthiness
This is stronger than "here is an example."

Why:
- the honest claim is a clean exact nonexistence theorem for a named open cyclic row;
- the theorem answers the exact selected question, rather than exhibiting one hand-picked quotient profile;
- the proof is structural in method even though the target is a single isolated residue.

Referee test:
- if a referee asks "what is the theorem?", the answer is immediate and title-sized;
- the packet does not depend on a broad search ladder or on many hand-picked small cases;
- the case-specificity is acceptable because the row is already isolated by the canonical source as a small open frontier residue.

## publication_publishability
Publishability audit: passes in the micro-paper lane.

The core mathematical packet is already close to a short publishable note:
- exact frontier statement fixed by the La Jolla source;
- short human-readable structural proof anchored to the family-defining `[9,107]` quotient;
- bounded novelty stop-line preserved;
- remaining work is citation polish, exposition, and final note assembly rather than a second theorem campaign.

Estimated paper fraction supplied by the current solve:
- about 0.82 of the eventual note.

Lean judgment:
- Lean is not required for publication status here;
- if desired, Lean would be a later archival seal for an already human-ready exact slice.

## publication_packet_audit
Packet quality after audit: strong.

Load-bearing strengths:
- exact title theorem exists now;
- proof is structural rather than brute-force;
- family anchor is explicit and recognizable;
- proof artifacts are preserved well enough for later polishing and formalization.

Residual bounded risks:
- novelty search remains bounded rather than exhaustive;
- the final note should cite the contracted-multiplier theorem precisely and avoid overclaiming a full multiplier.

Overall packet verdict:
- this should be treated as `PAPER_READY` on bounded human mathematical standards.

## micro_paper_audit
Micro-paper verdict: pass.

Questions answered explicitly:
- stronger than "here is an example": yes;
- most of a publishable note already present: yes;
- percentage of the paper supplied by one solve: about 82%;
- real title theorem present: yes;
- proof structural or merely instance-specific: structural, but on one isolated exact row;
- survives "what is the theorem?" referee question: yes;
- too dependent on hand-picked small cases: no, beyond the intended exact residue itself;
- remaining gap genuinely small or was the target misleading: genuinely small after correcting the multiplier citation;
- should it be moved aside instead of expanded: no;
- would Lean directly seal it: Lean would be secondary archival sealing, not a prerequisite for human-ready status.

## strongest_honest_claim
The cyclic group C_963 does not admit a (963,222,51)-difference set; a short quotient-orbit obstruction on the `C_107` contraction closes the exact `[9,107]` row.

## paper_title_hint
Nonexistence of a cyclic (963,222,51) difference set

## next_action
Treat this packet as HUMAN_READY, preserve the bounded prior-art stop-line, and polish the note around the corrected `107`-multiplier citation before sending it to the non-blocking Lean queue.

Conservative reading:
the nonexistence proof currently survives bounded rediscovery screening, faithfulness review, arithmetic reruns, and adversarial checking. The run should remain classified as `COUNTEREXAMPLE`, not `EXACT`, pending later publication audit and any eventual Lean seal.

## minimal_repair_if_any
No mathematical repair was needed.

Conservative status repair only:
- keep the classification below `EXACT`;
- move publication status to `SLICE_CANDIDATE`, not `PAPER_READY`;
- keep `lean_ready = false` and `lean_packet_seal = false` because publication audit, not Lean, is the shortest remaining path.
