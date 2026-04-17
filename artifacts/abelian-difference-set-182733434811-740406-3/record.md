# Solve Record: abelian-difference-set-182733434811-740406-3

## statement_lock
Target slug: `abelian-difference-set-182733434811-740406-3`.

Locked intended statement: determine whether any abelian group of order
`182733434811` admits a `(182733434811,740406,3)`-difference set.

Working title theorem if the current argument is sound:

> No abelian group of order `182733434811` admits a
> `(182733434811,740406,3)`-difference set.

If this closes exactly, it is already about 80-90% of a micro-paper because it
deletes one named residual row from Gordon's 2022 `lambda = 3` table.

## definitions
Use additive notation for an abelian group `G`.

A `(v,k,lambda)`-difference set `D subseteq G` satisfies
`|G| = v`, `|D| = k`, and every nonzero `g in G` has exactly `lambda`
representations as `d1 - d2` with `d1,d2 in D`.

Set the order parameter
`n = k - lambda = 740406 - 3 = 740403 = 3^2 * 82267`.

Parameter factorization:

- `v = 182733434811 = 3^4 * 19391 * 116341`
- `k = 740406 = 2 * 3 * 123401`
- `n = 740403 = 3^2 * 82267`

Standard parameter check:
`k(k-1) = 740406 * 740405 = 548200304430 = 3(v-1)`.

Conventions imported from the working packet:

- If a prime `q | n` is coprime to `v`, Hall's multiplier theorem makes `q` a
  numerical multiplier.
- Gordon's Theorem 2 gives, for a prime `p | v` and quotient `G/H` of order
  `p`, integers `a,b` with
  `k = a o + b`,
  `b(b-1) <= lambda(|H|-1)`,
  and `a o(o-1) <= lambda(p-1)`,
  where `o` is the order of the multiplier modulo `p`.

## approach_A
Structural / invariant route.

Use the Hall prime `q = 82267` from `n` as a multiplier, project to a prime
quotient `G/H` of order `p`, and use Gordon's orbit decomposition. The hope is
that the multiplier order `o = ord_p(q)` is so large that
`a o(o-1) <= 3(p-1)` forces `a = 0`, after which
`b = k` contradicts `b(b-1) <= 3(|H|-1)`.

This is attractive because:

- the packet already says the standard fast eliminations failed, so a new
  contradiction should come from a sharper orbit count;
- `n` has a large prime factor `82267` coprime to `v`;
- `v` has two nontrivial odd prime divisors, giving quotients of orders
  `19391` and `116341`.

Self-check after approach A setup:
the route is theorem-facing and uses only the transfer-kit ingredients already
named in the packet.

## approach_B
Construction / extremal / contradiction route.

Work through character values on a prime quotient. Since an abelian
`(v,k,lambda)`-difference set forces `|chi(D)|^2 = n` for nonprincipal
characters, one can try to push the quotient `G -> G/H -> C_p` into a rigid
character sum obstruction. In practice that seems less economical here because
the packet already exposes Gordon's Theorem 2 as the sharper quotient tool.

A weaker extremal variant is to test the same Hall multiplier on the larger
prime quotient `p = 116341` and seek the same `a = 0` collapse there.

Self-check after approach B:
it is plausible as backup structure, but it looks strictly less direct than the
orbit-count route.

## lemma_graph
Minimal proof skeleton:

1. Assume `D` is an abelian `(v,k,3)`-difference set in some group `G` of order
   `v = 182733434811`.
2. Since `82267 | n` and `gcd(82267,v) = 1`, Hall's theorem gives numerical
   multiplier `t = 82267`.
3. Since `19391 | |G|` and `G` is abelian, choose a subgroup `H` of index
   `19391`, so `|H| = v/19391 = 9423621` and `G/H` has order `19391`.
4. Compute `o = ord_19391(82267) = 9695`.
5. Apply Gordon's Theorem 2:
   `k = a o + b`,
   `b(b-1) <= 3(|H|-1)`,
   `a o(o-1) <= 3(19391-1)`.
6. Since `9695 * 9694 > 3(19391-1)`, deduce `a = 0`.
7. Then `b = k = 740406`, but
   `b(b-1) = 548200304430 > 3(9423621-1) = 28270860`, contradiction.

Self-check:
every step is local and algebraic; the only source-sensitive points are the
precise Hall-multiplier hypothesis and the exact Gordon Theorem 2 statement.

## chosen_plan
Choose approach A with `p = 19391`.

Reason:

- it uses the large Hall prime `82267` directly;
- the computed order `9695` is already enormous relative to `p`;
- the resulting contradiction is one-line once Gordon's inequality is in force;
- it gives a theorem-shaped nonexistence result, not just a failed search.

## self_checks
Major-step checks:

1. Parameter arithmetic:
   `k(k-1) = 3(v-1)` holds exactly.
2. Hall-prime check:
   `82267 | n` and `gcd(82267,v) = 1`, so the multiplier route is legally
   available if Hall's theorem is being used in the standard abelian form.
3. Quotient check:
   because `G` is abelian and `19391` divides `|G|`, an index-`19391` subgroup
   exists.
4. Order check:
   `82267^9695 == 1 (mod 19391)`, while the prime-factor tests
   `82267^1939`, `82267^1385`, and `82267^35` are all nontrivial modulo
   `19391`, so `ord_19391(82267) = 9695`.
5. Inequality check:
   `9695 * 9694 = 93998830 > 3 * 19390 = 58170`, hence `a = 0`.
6. Final contradiction check:
   with `a = 0`, one gets
   `740406 * 740405 = 548200304430 > 28270860 = 3(9423621-1)`.

Net self-check:
the arithmetic contradiction is decisive if the imported theorems are exactly
as summarized in the packet.

## code_used
Minimal code only.

Used short local `python3` arithmetic snippets to:

- factor `v`, `k`, and `n`;
- verify `gcd(82267,v) = 1`;
- compute `ord_19391(82267) = 9695`;
- confirm the numerical inequalities.

No search, optimization, SAT, or construction code was used.

## result
Candidate nonexistence proof.

Assume there is an abelian `(182733434811,740406,3)`-difference set `D` in a
finite abelian group `G` of that order. Let
`n = k - lambda = 740403 = 3^2 * 82267`.

Because `82267` is a prime divisor of `n` and `gcd(82267,|G|)=1`, Hall's
multiplier theorem gives a numerical multiplier `t = 82267`.

Now `19391` divides `|G| = 3^4 * 19391 * 116341`. Since `G` is abelian, there
is a subgroup `H <= G` with quotient `G/H` of order `19391`; thus
`|H| = 182733434811 / 19391 = 9423621`.

The order of `t` modulo `19391` is `o = 9695`. Indeed
`19391 - 1 = 19390 = 2 * 5 * 7 * 277`, one checks
`82267^9695 == 1 (mod 19391)`, and also
`82267^1939`, `82267^1385`, and `82267^35` are all nontrivial modulo `19391`.

Apply Gordon's Theorem 2 to the quotient `G/H` and multiplier `t`. Then there
exist integers `a,b` with

- `740406 = a * 9695 + b`,
- `b(b-1) <= 3(9423621-1) = 28270860`,
- `a * 9695 * 9694 <= 3(19391-1) = 58170`.

But `9695 * 9694 = 93998830 > 58170`, so `a = 0`. Hence `b = 740406`.
Substituting into the second inequality gives

`740406 * 740405 <= 28270860`,

which is false because the left-hand side is `548200304430`.

This contradiction rules out the assumed difference set.

Conclusion:
subject to exact source-level confirmation of the Hall-multiplier step and the
packet's statement of Gordon's Theorem 2, the tuple
`(182733434811,740406,3)` has no abelian realization.

Self-check after result:
the proof is short, parameter-local, and paper-shaped; the remaining risk is
source-hypothesis mismatch, not a missing combinatorial step.

## family_affinity
Very high.

This sits exactly in the residual abelian `lambda = 3` cleanup family from
Gordon's Table 4. The proof template is not an ad hoc computation; it is a
direct elimination by Hall multiplier plus Gordon orbit structure.

## generalization_signal
Moderate and concrete.

What scales:

- any residual abelian difference-set tuple with a Hall prime `q | (k-lambda)`
  coprime to `v`;
- any prime quotient `p | v` for which `ord_p(q)` is large enough that
  `ord_p(q)(ord_p(q)-1) > lambda(p-1)`.

What does not automatically scale:

- tuples where every Hall multiplier has tiny order on every available prime
  quotient;
- tuples where Gordon's orbit decomposition leaves `a > 0` possible.

## proof_template_reuse
Reusable template:

1. factor `v` and `n = k-lambda`;
2. pick a Hall prime `q | n` with `gcd(q,v)=1`;
3. choose a prime divisor `p | v`;
4. compute `o = ord_p(q)`;
5. if `o(o-1) > lambda(p-1)`, Gordon's Theorem 2 forces `a = 0`;
6. then test whether `k(k-1) <= lambda(v/p - 1)` can possibly hold.

For this tuple, step 5 already kills the case.

## candidate_theorem_slice
Exact theorem slice suggested by the current solve:

> Let `G` be a finite abelian group of order `182733434811`. Then `G` admits no
> `(182733434811,740406,3)`-difference set.

Immediate corollary / boundary remark:
this removes one named residual line from Gordon's 2022 list of six unresolved
abelian `lambda = 3` cases with `k <= 10^10`.

## smallest_param_shift_to_test
Two small next moves are most valuable:

1. Redundant same-tuple check on the other prime quotient `p = 116341`.
   This is not needed for the contradiction, but it would show the proof is not
   fragile with respect to the chosen quotient.
2. Apply the same Hall-multiplier order test to the other Gordon Table 4
   residual tuples, especially those where `n` has a Hall prime and `v` has a
   large prime divisor.

I did not read other residual dossiers in this solve pass, so I am not naming a
specific neighboring tuple beyond this abstract filter.

## why_this_is_or_is_not_publishable
If the source-level hypotheses verify cleanly, this is publishable in the
micro-paper lane.

Why:

- the exact title theorem is already present;
- the argument is short and family-anchored, not a raw computer witness;
- the literature gap is explicit: Gordon 2022 leaves this tuple open;
- remaining packaging is light.

Minimal remaining packaging work:

- quote the exact Hall multiplier statement used;
- quote Gordon's Theorem 2 precisely in the notation of the paper;
- include the modular-order computation and one paragraph explaining the chosen
  quotient `G/H`;
- add a short contextual paragraph stating that this deletes one residual row.

If either imported theorem turns out to require an extra hypothesis not recorded
in the packet, the current result drops from "candidate paper theorem" to
"strong solve lead". That is the main publishability risk.

## paper_shape_support
Extra structure needed to make the result fully paper-shaped is minimal:

- one exact theorem statement as above;
- one short lemma recording `ord_19391(82267) = 9695`;
- one contextual proposition explaining why Hall's theorem and Gordon's Theorem
  2 apply;
- one sentence on significance:
  "This eliminates the parameter set `(182733434811,740406,3)` from Gordon's
  residual abelian `lambda = 3` table."

Natural supporting theorem slice:
the Hall-multiplier / large-order quotient criterion described in
`proof_template_reuse`.

This is comfortably within the intended 70-90% solve-to-paper window if the
main contradiction survives verification.

## boundary_remark
Boundary remark:
the proof uses only one prime quotient `19391` and one Hall prime `82267`.
It does not claim a broader theorem about all residual `lambda = 3` tuples, and
it does not use any construction or exhaustive search.

What part of the argument scales:
the Hall-multiplier plus orbit-order collapse.

What part does not:
the specific numerical contradiction
`740406 * 740405 > 3(9423621-1)` is instance-bound.

Current package assessment:
if source verification passes, this is closer to a paper-shaped claim than to a
mere instance witness, because the result is already an exact nonexistence
theorem anchored to a named residual family.

## likely_failure_points
Main failure points to check before promotion:

- whether the packet's Hall-multiplier summary is being used in exactly the
  right generality for abelian difference sets;
- whether Gordon's Theorem 2 applies exactly with `p = 19391`,
  `|H| = v/p`, and multiplier order `o = ord_p(t)`;
- whether there is any hidden convention on the quotient action or on fixed
  points that changes the formulas for `a` and `b`;
- whether the notation in the paper uses `lambda(|H|-1)` exactly as summarized
  here.

I do not currently see an arithmetic failure point.

## what_verify_should_check
Verification should check the following in order:

1. Confirm the exact Hall multiplier theorem being invoked:
   prime `82267` divides `n = 740403` and is coprime to `v`.
2. Confirm Gordon Theorem 2 exactly matches the packet summary:
   `k = a o + b`,
   `b(b-1) <= lambda(|H|-1)`,
   `a o(o-1) <= lambda(p-1)`.
3. Confirm that an abelian group of order `v` always admits a quotient of order
   `19391`.
4. Recompute `ord_19391(82267) = 9695`.
5. Recompute the two numerical inequalities forcing `a = 0` and then the final
   contradiction.
6. Optionally repeat the same calculation for `p = 116341` as a robustness
   appendix.

## verify_rediscovery
- PASS 1 used a bounded web audit on 2026-04-15 with exact-tuple, reordered/family, canonical-source, same-source Table 4, and recent-status/citation style searches.
- The searches returned Gordon's 2022 paper and tuple-specific echoes of that source, but no later paper, repository entry, theorem, proposition, example, observation, or corollary explicitly settling the exact abelian `(182733434811,740406,3)` case.
- Within this bounded budget, rediscovery is **not established**.

## verify_faithfulness
- The solve writeup targets the exact intended negation of the packet statement: nonexistence of an abelian `(182733434811,740406,3)` difference set.
- There is no drift to a weaker proxy theorem or to a nearby parameter set.
- The source-faithfulness issue is instead at the level of theorem instantiation:
  the record uses `o = ord_19391(82267) = 9695`, but Gordon's Theorem 2 is not
  stated in terms of that raw order alone.
- The quotient-versus-product wording is a smaller issue here. Because `19391`
  appears to the first power in `v`, an abelian group of order `v` does split
  as `Z_19391 x H` for some `H` of order `9423621`, so that part is repairable.
- The fatal faithfulness problem is the order parameter, not the statement of
  the intended theorem.

## verify_proof
- The first incorrect step is the use of `o = ord_19391(82267)` as the orbit
  size parameter in Gordon's Theorem 2.
- The record's own setup says the theorem depends on a multiplier power
  determined by the complementary factor. Once that source-sensitive parameter
  is restored, the advertised contradiction disappears.
- Let `q = 82267`. For the `p = 19391` split, `|H| = 9423621 = 3^4 * 116341`,
  so `exp(H)` is `3^e * 116341` for some `1 <= e <= 4`.
- Rerunning the arithmetic gives:
  `ord_3(q) = 1`, `ord_9(q) = 3`, `ord_27(q) = 9`, `ord_81(q) = 27`,
  `ord_116341(q) = 29085`, and `ord_19391(q) = 9695`.
- Therefore every admissible complementary exponent-forcing integer `s` is a
  multiple of `29085`, hence in particular a multiple of `9695`. So
  `q^s == 1 mod 19391`, and the relevant order on the `19391` factor is
  `ord_19391(q^s) = 1`, not `9695`.
- With `o = 1`, Gordon's inequality `a o(o-1) <= 3(19391-1)` becomes vacuous
  and does **not** force `a = 0`. The claimed contradiction never starts.
- The fallback check on the other prime divisor also fails to rescue the proof:
  for `p = 116341`, the same computation gives `ord_116341(q^s) = 3` in the
  most favorable `3`-exponent case and `1` otherwise, so again no useful
  contradiction is available.
- Verdict for PASS 3: the current nonexistence proof is not a tiny-fix proof.
  Its decisive theorem application is wrong, and no exact theorem survives from
  the displayed argument.

## verify_adversarial
- There is no saved checker or witness file in the slug directory to rerun.
- I reran the arithmetic adversarially in fresh local scripts.
- Confirmed:
  `ord_19391(82267) = 9695`,
  `ord_116341(82267) = 29085`,
  `ord_3(82267) = 1`,
  `ord_9(82267) = 3`,
  `ord_27(82267) = 9`,
  `ord_81(82267) = 27`.
- From these, every admissible `s` for the `19391` split is a multiple of
  `9695`, forcing `ord_19391(82267^s) = 1`.
- For the `116341` split, `ord_116341(82267^s)` is at most `3`, and usually
  `1`.
- This adversarial recomputation directly breaks the advertised orbit-count
  contradiction and shows that the "optional robustness appendix" quotient does
  not repair it.

## verify_theorem_worthiness
- Exactness:
  the target theorem remains exact and well-posed, but the currently verified
  output is only a failed proof attempt plus a useful diagnostic.
- Novelty:
  bounded PASS 1 did not establish rediscovery, so the target still looks
  frontier-plausible.
- Reproducibility:
  high for the flaw. The arithmetic falsification of the theorem application is
  short and repeatable.
- Lean readiness:
  `false`. There is no verified theorem or disproof packet here for Lean to
  seal.
- Paper leverage:
  the *target*, if later solved exactly, would still look like roughly
  `75%` to `80%` of a short cleanup note because it removes one named Gordon
  Table 4 residual row.
- Would this result, if correct and Lean-sealed, already constitute most of a
  publishable note?
  For the intended nonexistence theorem, yes. For the currently verified
  residue, no.
- What percentage of the paper would one solve already provide?
  About `0.75` to `0.80` for a true exact solve; the present verified content is
  far below that.
- What title theorem is actually visible?
  None yet beyond the negative verifier statement that the current Hall/Gordon
  application does not work.
- What part of the argument scales?
  The diagnostic template scales: compute the exact complementary exponent
  parameter first, then test `ord_p(q^s)` rather than `ord_p(q)`.
- What part clearly does not?
  The shortcut from a large raw order `ord_p(q)` to an immediate Gordon
  contradiction.
- Best honest publication status now:
  `NONE` for the verified packet. This is not even `INSTANCE_ONLY` yet because
  there is no verified exact result, only an invalid proof attempt on a good
  frontier target.

## verify_verdict
- `CRITICAL_FLAW`
- PASS 1 did not establish rediscovery of the exact tuple.
- PASS 2 found no theorem drift on the target statement itself, but it found a
  source-faithfulness issue in the key theorem parameter.
- PASS 3 found the first incorrect step: using `ord_p(82267)` where the Gordon
  argument needs the order after the complementary exponent condition is
  imposed.
- PASS 4 confirmed numerically that this kills the contradiction on both prime
  quotient choices.
- Appropriate harness classification is therefore `PARTIAL`, not
  `COUNTEREXAMPLE`, not `CANDIDATE`, and certainly not `EXACT`.
- `lean_ready = false` and `lean_packet_seal = false` because Lean would only
  formalize a broken argument rather than seal a frontier packet.

## minimal_repair_if_any
- Tiny conservative repair only: downgrade the artifact and preserve the
  useful arithmetic check that `ord_p(q^s)` collapses on the available prime
  quotients.
- No small local edit recovers the advertised nonexistence theorem.
- Any future solve attempt must restart from the exact source statement of
  Gordon's Theorem 2 and a source-faithful computation of the complementary
  exponent parameter.

## publication_prior_art_audit
- On `2026-04-15` I ran a bounded web pass with exact-statement searches for
  `(182733434811,740406,3)` and alternate-notation searches using
  `v = 182733434811`, `k = 740406`, and `lambda = 3`, together with a
  canonical-source search on Gordon's paper title and Table 4 wording.
- Those searches surfaced Gordon's 2022 paper and tuple-specific echoes of that
  source, but no later theorem, proposition, example, corollary, observation,
  database entry, or note settling the exact abelian case.
- Canonical-source check: Gordon's Table 4 still lists
  `(182733434811,740406,3)` among the six remaining abelian `(v,k,3)` cases
  with `k <= 10^10`.
- Same-source theorem check: Gordon's Theorem 2 and the surrounding elimination
  machinery do not themselves settle this row; the paper keeps the tuple in the
  residual table after those filters are applied.
- One outside-source status pass did not surface any later resolution. Because
  the packet already fails on source-faithfulness grounds, no broader citation
  chase was warranted.
- Prior-art verdict: no rediscovery established in this bounded audit, but also
  no solved theorem packet survives.

## publication_statement_faithfulness
- The target statement stayed exact throughout: the intended claim is still the
  nonexistence or existence question for abelian
  `(182733434811,740406,3)` difference sets.
- The current artifact is not source-faithful at the decisive theorem
  instantiation step. Gordon's Theorem 2 uses the orbit order attached to a
  multiplier of the form `q^s` after the complementary exponent condition on
  `H` is imposed, not the raw `ord_p(q)` substituted in the solve record.
- Once that source-faithful order parameter is restored, the advertised orbit
  contradiction disappears on both available prime-quotient choices.
- Faithfulness verdict: the statement is stable, but the proof packet is not.
  The strongest faithful claim is only that the present Hall/Gordon route does
  not eliminate the tuple.

## publication_theorem_worthiness
- Is the strongest honest claim stronger than "here is an example"?
  Slightly, in the narrow sense that it records a reproducible structural
  failure of a proof template rather than an isolated example. That is still
  not a publishable theorem about the difference-set problem itself.
- Is there a real title theorem, theorem slice, or counterexample theorem here?
  No. The target would have a real title theorem if solved, but the audited
  packet does not currently contain one.
- Is the proof structural or merely instance-specific?
  The failed route is structural in style, but the surviving output is only an
  instance-local diagnostic about why this particular application of Gordon's
  theorem fails.
- Would this survive a referee asking "what is the theorem?"
  No.
- Is the claim still too dependent on hand-picked small cases?
  No small-case dependence is the problem here. The problem is that the key
  source instantiation is wrong, so there is no theorem to referee.
- Theorem-worthiness verdict: below `INSTANCE_ONLY`; the current packet is
  diagnostic only.

## publication_publishability
- Would this result, if correct and verified in the current bounded sense,
  already constitute most of a publishable note?
  No. The currently verified residue is only that the advertised nonexistence
  proof fails.
- What percentage of the paper would one solve already provide?
  A genuine exact solve on this tuple would still supply about `75%` to `80%`
  of a short cleanup note, but the current verified packet contributes only
  about `15%` to `20%`.
- Is there a real title theorem, theorem slice, or counterexample theorem here?
  Not in the present packet.
- If this is not yet paper-ready, is the remaining gap genuinely small or did
  the candidate only look attractive before audit?
  The candidate looked attractive for a real reason, namely Gordon's residual
  Table 4 framing, but the remaining mathematical gap is not small after audit:
  the main proof disappears rather than needing light repair.
- If this is not yet paper-ready, should it be moved aside rather than
  expanded into a larger theorem program?
  Yes. Preserve the diagnostic and cool the slug rather than growing it into a
  broader campaign.
- Would Lean directly seal the packet, or would it only be optional polish /
  later archival formalization?
  Lean cannot seal the current packet. Formalization becomes relevant only if a
  new exact theorem or counterexample packet is found later.
- Publishability verdict: `publication_status = NONE`.

## publication_packet_audit
- publication status: `NONE`
- publication confidence: `0.94`
- publication packet quality: `diagnostic_only`
- proof artifacts preserved: `true`
- human ready: `false`
- lean ready: `false`
- packet verdict:
  keep the verifier arithmetic and source-faithfulness notes, but do not treat
  this as a near-paper theorem packet.

## micro_paper_audit
- The target tuple remains micro-paper eligible in principle because Gordon's
  Table 4 gives it a clean one-row cleanup narrative if the case is actually
  solved.
- The current audited packet is not micro-paper ready because no exact theorem
  slice survives. What remains is a failed proof plus a useful warning about
  the complementary-exponent parameter in Gordon's Theorem 2.
- `single_solve_to_paper_fraction` for the present verified packet is best kept
  low, around `0.18`.
- `title_theorem_strength` is `weak` because there is no surviving theorem.
- `publication_narrative_strength` remains `moderate` only in the underlying
  target-selection sense; it does not rescue the current packet.
- Micro-paper verdict:
  move aside rather than expand.

## strongest_honest_claim
The bounded audit did not find a prior-art resolution of the exact abelian
`(182733434811,740406,3)` case, but the current nonexistence proof is not
source-faithful. Gordon's Theorem 2 must be applied with the multiplier order
after the complementary exponent condition on `H`; under that faithful
parameter, the orbit-count contradiction disappears on both available prime
quotients. The strongest honest outcome is therefore a preserved diagnostic,
not a publishable theorem slice.

## paper_title_hint
No current title is justified. If a future exact solve appears, the honest note
title would be something like:

> On the Residual Abelian `(182733434811,740406,3)` Difference-Set Case

## next_action
Move this slug aside as a `PARTIAL` diagnostic rather than enlarging it into a
broader theorem program. Preserve the source-faithful verifier notes and reopen
it only if a new argument produces an actual exact theorem or counterexample
packet.
