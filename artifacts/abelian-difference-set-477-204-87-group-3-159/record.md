# Solve Record: Does the abelian group C_3 x C_159 admit a (477,204,87)-difference set?

- slug: `abelian-difference-set-477-204-87-group-3-159`
- working_packet: `artifacts/abelian-difference-set-477-204-87-group-3-159/working_packet.md`

## statement_lock
Locked target: prove or disprove the existence of a `(477,204,87)` difference set in
`G = C_3 x C_159`.

For solve purposes I identify
`G ≅ C_3^2 x C_53 = A x B`
with `A ≅ C_3^2` and `B ≅ C_53`.

Exact title-theorem target if the obstruction closes:

`The abelian group C_3 x C_159 admits no (477,204,87)-difference set.`

If correct, this would already be about `80-90%` of a short paper: the title theorem,
the frontier hook, and the core proof are all present, with only verification and light
packaging left.

## definitions
- A `(v,k,lambda)` difference set in a finite abelian group `G` of order `v` is a subset
  `D ⊆ G` with `|D| = k` such that every nonidentity element of `G` has exactly `lambda`
  ordered representations `d_1 d_2^{-1}` with `d_1,d_2 ∈ D`.
- Here `v = 477`, `k = 204`, `lambda = 87`, and
  `n := k - lambda = 117 = 3^2 * 13`.
- In the group ring,
  `D D^(-1) = n + lambda G`.
- Since `13 | n` and `gcd(13, |G|) = 1`, the standard abelian multiplier theorem makes
  `13` a numerical multiplier candidate for this difference set.
- Under `G = A x B` with `A ≅ C_3^2`, `B ≅ C_53`, the power map `x -> x^13` is the
  identity on `A` and has order `13` on `B^x`.

Ambiguities / conventions:

- I use additive language on `A x B` when discussing translations, and multiplicative
  notation only inside the formal difference-set identity.
- The only delicate step is multiplier normalization: I must justify passing from
  `D^(13) = g + D` to a translated difference set fixed by `13`.
- No external source is being checked in solve, so the argument must stand on local
  algebra alone.

## approach_A
Structural / invariant route.

1. Use the `13`-multiplier to translate to a `13`-stable difference set.
2. Classify the `13`-orbits on `A x B`.
   The fixed points are exactly `A x {0}`, so there are `9` orbits of size `1`, and every
   other orbit has size `13`.
3. Since `|D| = 204 ≡ 9 (mod 13)`, a `13`-stable `D` must contain all `9` fixed points
   and then a union of `15` nontrivial `13`-orbits.
4. Fiber over `A`: for each `a ∈ A`, the fiber size
   `s_a := |D ∩ ({a} x B)|`
   must equal `1 + 13 b_a` with `b_a ∈ {0,1,2,3,4}`.
5. Push `D` to the quotient `G/B ≅ A`. The identity coefficient in the quotient
   group-ring relation forces `sum_a s_a^2 = 117 + 87 * 53 = 4728`.
6. But `sum_a s_a = 204` implies `sum_a b_a = 15`, hence
   `sum_a s_a^2 = 9 + 26 * 15 + 169 * sum_a b_a^2 = 399 + 169 * sum_a b_a^2`,
   impossible modulo `169` because `4728 - 399 = 4329` is not divisible by `169`.

This route would give a clean nonexistence proof with no search.

## approach_B
Construction / extremal / contradiction route.

1. Ignore multipliers at first and work only with the quotient to `A ≅ C_3^2`.
2. Let `s_a = |D ∩ ({a} x B)|`. Then
   `sum_a s_a = 204` and `sum_a s_a^2 = 4728`.
3. One could try to classify all integer `9`-tuples `(s_a)` compatible with the quotient
   autocorrelation equations on `A`, then lift to actual `B`-fibers.
4. After that, impose character constraints on each fiber in `B`.

Why this is weaker:

- Without the multiplier, the quotient moment equations alone do not seem sharp enough.
- The multiplier route already forces a strong congruence pattern on every fiber, so the
  direct extremal path looks strictly less efficient for this exact row.

## lemma_graph
Lemma skeleton.

1. Multiplier lemma:
   `13 | n` and `gcd(13,477)=1`, so for any difference set `D` there is `g ∈ G` with
   `D^(13) = g + D`.
2. Normalization lemma:
   After translating in the `B ≅ C_53` direction, assume `g ∈ A x {0}`.
3. Fixed-translate lemma:
   Because the `13`-power map has order `13` on `G`, iterating the previous relation gives
   `D = D + g`; hence the translated set is actually fixed by `13`.
4. Orbit lemma:
   A `13`-fixed subset of `A x B` is a union of the `9` fixed points in `A x {0}` and
   `13`-element orbits elsewhere. Since `204 ≡ 9 (mod 13)`, all `9` fixed points must lie
   in `D`.
5. Fiber lemma:
   For each `a ∈ A`, `s_a = 1 + 13 b_a`, with `b_a ∈ {0,1,2,3,4}`, and `sum_a b_a = 15`.
6. Quotient lemma:
   Applying the quotient map `G -> A` to `D D^(-1) = 117 + 87 G` yields
   `sum_a s_a^2 = 117 + 87 * 53 = 4728`.
7. Final contradiction:
   `sum_a s_a^2 = 399 + 169 * sum_a b_a^2`, but `4728 - 399 = 4329` is not divisible by
   `169`.

## chosen_plan
Choose Approach A.

It directly targets theorem shape: a short multiplier-orbit obstruction for the exact
`[3,159]` row. It also matches the packet's recommended first attack and avoids any
search-heavy drift.

Rigorous attempt.

Assume `D ⊆ G = A x B` is a `(477,204,87)` difference set.

Because `13 | n = 117` and `gcd(13,477)=1`, `13` is a numerical multiplier, so
`D^(13) = g + D` for some `g ∈ G`.

Write `g = (a_0,b_0)` with `a_0 ∈ A`, `b_0 ∈ B`. Since multiplication by `12` is an
automorphism of `B ≅ C_53`, choose `t ∈ B` with `12 t = -b_0`. Replacing `D` by the
translate `D' := D + (0,t)`, we get

`(D')^(13) = D' + (a_0,0)`.

Now iterate this relation `13` times. The `13`-power map is the identity on `A` and has
order `13` on `B`, so its `13`th iterate is the identity on `G`. Therefore

`D' = D' + sum_{i=0}^{12} (a_0,0) = D' + (13 a_0,0) = D' + (a_0,0)`

because `A` has exponent `3` and `13 a_0 = a_0`.

Hence `D'` is translation-invariant by `(a_0,0)`, and then the displayed relation reduces
to `(D')^(13) = D'`. So, after harmless translation, we may assume from the start that
`D` is fixed by the `13`-power map.

The fixed points of `x -> x^13` are exactly the elements of `A x {0}`, so there are `9`
orbits of size `1`. Every other element has nonzero `B`-coordinate and lies in an orbit of
size `13`, because `13` has order `13` modulo `53`.

Since `|D| = 204 ≡ 9 (mod 13)`, a `13`-stable `D` must contain exactly `9` fixed points.
As there are only `9` of them, `D` contains all of `A x {0}`.

For each `a ∈ A`, let
`s_a := |D ∩ ({a} x B)|`.
Then each fiber contains the fixed point `(a,0)` and then some number of `13`-orbits in
`B^x`, so

`s_a = 1 + 13 b_a`, with `b_a ∈ {0,1,2,3,4}`.

Summing over the `9` values of `a`,

`204 = sum_a s_a = 9 + 13 sum_a b_a`,

so `sum_a b_a = 15`.

Now apply the quotient map `pi : G -> A` with kernel `B`. If
`X := pi(D) = sum_{a ∈ A} s_a a`,
then applying `pi` to the difference-set identity gives

`X X^(-1) = 117 + 87 * 53 * A`.

Taking the identity coefficient yields

`sum_a s_a^2 = 117 + 87 * 53 = 4728`.

But from `s_a = 1 + 13 b_a` and `sum_a b_a = 15`,

`sum_a s_a^2 = sum_a (1 + 26 b_a + 169 b_a^2)`
`           = 9 + 26 * 15 + 169 sum_a b_a^2`
`           = 399 + 169 sum_a b_a^2`.

Therefore `4728 - 399 = 4329` must be divisible by `169`, which it is not. Contradiction.

So no such difference set exists.

## self_checks
- Check 1: `n = k - lambda = 204 - 87 = 117` and `13 | 117`, `gcd(13,477)=1`.
- Check 2: `G ≅ C_3^2 x C_53` is valid because `C_159 ≅ C_3 x C_53`.
- Check 3: the normalization only uses translation in the `C_53` direction, where
  multiplication by `12` is invertible.
- Check 4: after normalization, iterating the multiplier relation `13` times gives
  translation by `13(a_0,0) = (a_0,0)`, so invariance really follows.
- Check 5: orbit count is consistent:
  `9 + 36 * 13 = 477`.
- Check 6: size check is consistent:
  `204 = 9 + 15 * 13`.
- Check 7: quotient identity coefficient:
  `117 + 87 * 53 = 117 + 4611 = 4728`.
- Check 8: congruence obstruction:
  `4728 - 399 = 4329`, and `169 * 25 = 4225`, `169 * 26 = 4394`, so divisibility fails.

## code_used
None. The obstruction closed by hand, so minimal-code policy stays at zero.

## result
Strong candidate nonexistence proof:

`C_3 x C_159` does not admit a `(477,204,87)` difference set.

The proof is short and theorem-facing. Its key move is that the `13`-multiplier forces a
translate to be `13`-stable, which in turn forces every `C_53`-fiber above `C_3^2` to have
size `1 (mod 13)`. The quotient square-sum identity over `C_3^2` then contradicts that
congruence pattern.

Immediate corollary / remark:

- Any putative solution of this exact row would have to break the multiplier-orbit pattern,
  but the multiplier theorem prevents that. So the obstruction is structural, not
  computational.

Minimal remaining packaging work if the proof checks:

- tighten the multiplier-normalization lemma into citation-ready prose,
- write the quotient coefficient computation as a standalone lemma,
- prepare one short verification note confirming the arithmetic and orbit counts.

## family_affinity
High. This sits exactly in the multiplier-survey open-row family, and the proof method is a
classic multiplier-orbit obstruction specialized to one exact abelian row.

## generalization_signal
Moderate but real.

What scales:

- the template "multiplier -> orbit decomposition -> quotient moment contradiction";
- any case where a prime divisor of `n` acts with one small fixed subgroup and one uniform
  nontrivial orbit length on the complementary Sylow factor.

What does not automatically scale:

- the specific congruence `s_a = 1 (mod 13)` and the exact square-sum contradiction depend
  on the orbit length `13`, the `9` fixed fibers, and the exact value `4728`.

This is closer to a theorem slice than to a broad family theorem.

## proof_template_reuse
Reusable proof template:

1. isolate a prime multiplier `q | n` with `q ∤ |G|`,
2. normalize to a `q`-stable translate,
3. decompose `D` into multiplier orbits,
4. push to a quotient where fiber sizes become constrained modulo the orbit length,
5. clash that congruence with an identity-coefficient or character-sum moment equation.

## candidate_theorem_slice
Candidate theorem slice:

`There is no (477,204,87)-difference set in the abelian group C_3 x C_159.`

Suggested exact supporting slice:

`In any putative such difference set, 13-multiplier invariance would force each C_53-fiber
above C_3^2 to have cardinality 1 mod 13, but the quotient identity over C_3^2 forbids
this.`

## smallest_param_shift_to_test
Best next parameter shifts, only after verification of the current proof:

- look for another open row with the same multiplier shape `q | n`, `q` acting trivially on
  the small Sylow part and with a single nontrivial orbit length on the large prime part;
- within this row's neighborhood, test exact cases where the quotient has order `9` again,
  because the same fiber-square argument may recur.

For this exact package, there is no need to drift now; the current row is already the right
micro-paper target.

## why_this_is_or_is_not_publishable
If the obstruction is verified, this is publishable in the micro-paper lane.

- A successful solve here would already be about `0.85` of a paper.
- Exact title theorem:
  `On the Nonexistence of a (477,204,87)-Difference Set in C_3 x C_159`.
- The frontier basis is already packaged by the Gordon-Schmidt open table row.
- Remaining work is light: proof polishing, one bounded verification pass, and standard
  exposition around the table entry.

If the multiplier-normalization step were found to have a gap, the current result would drop
back to "promising obstruction sketch" and would be too thin for the lane. At present the
argument looks compact enough to clear that bar.

## paper_shape_support
What extra structure makes the result paper-shaped once the main claim closes:

- one clean lemma stating the normalized `13`-multiplier action,
- one short proposition for the fiber congruence `s_a = 1 + 13 b_a`,
- one contradiction lemma from the quotient coefficient at the identity,
- one boundary remark explaining why this is a row-specific obstruction rather than a broad
  classification theorem.

That is enough for a short note; no feeder ladder is needed.

## boundary_remark
Boundary remark:

The argument is exact-instance heavy. It uses the precise decomposition
`C_3 x C_159 ≅ C_3^2 x C_53`, the multiplier prime `13`, and the fact that `13` has order
`13` on the `53`-part. So the current package is no longer "just a witness-level instance",
but it is still closer to a sharp table-row theorem than to a family-wide classification.

## likely_failure_points
- The main place to stress-test is the multiplier-normalization step from `D^(13) = g + D`
  to a translated `13`-fixed set.
- Verify that the solve-stage use of the abelian multiplier theorem is legitimate in this
  exact parameter setting.
- Recheck the quotient computation carefully so the kernel size is `53`, not `9`.
- Confirm that the orbit count on `B^x` is exactly `4` orbits of size `13` for each
  `a ∈ A`, though the proof only needs the orbit size `13`, not the number `4`.

## what_verify_should_check
- Confirm the multiplier input: `13` is indeed a valid numerical multiplier because
  `13 | n` and `13 ∤ 477`.
- Audit the normalization argument line by line.
- Check the quotient identity
  `X X^(-1) = 117 + 87 * 53 * A`
  and especially the identity coefficient `sum_a s_a^2 = 4728`.
- Recompute the final congruence obstruction modulo `169`.
- Prior-art check should ask whether an equivalent obstruction for the `[3,159]` row already
  appears somewhere, because if so the mathematical proof may still be a rediscovery.

## verify_rediscovery
PASS 1: bounded rediscovery audit on 2026-04-15.

Searches used:

- exact tuple: `"(477,204,87)" difference set "C_3 x C_159"`
- alternate notation: `"477 204 87" "[3,159]" difference set`
- canonical source: `"A Survey of the Multiplier Conjecture" Table 2 477 204 87 [3,159]`
- source / repository freshness: targeted `dmgordon.org` searches for the exact tuple and
  `[3,159]`
- recent-status check: `"(477,204,87)" difference set 2024 OR 2025 OR 2026`

Outcome:

- The canonical source still surfaces the exact row `477 204 87 [3,159]` as open in Table 2.
- The bounded web audit did not surface a later paper, repository entry, proposition,
  example, or discussion explicitly settling the exact `C_3 x C_159` case.
- Therefore rediscovery is not established within verify budget.

Conservative verdict for PASS 1:

- `verify_verdict != REDISCOVERY`
- novelty remains plausible but not proven beyond the bounded audit

## verify_faithfulness
The solve artifact is faithful to the intended statement in scope and target:

- It addresses the exact group `C_3 x C_159`, rewritten as the isomorphic group
  `C_3^2 x C_53`.
- It aims at the exact theorem slice
  `There is no (477,204,87)-difference set in C_3 x C_159`.
- No quantifier drift or weakened proxy claim was found.

However, the proof imports an unstated extra premise:

- The argument silently upgrades `13` from a prime divisor of `n = 117` to an actual
  proved multiplier for this row.
- In the canonical survey, Table 2 records `13` only in the `MC primes` sense, i.e. as a
  multiplier under the multiplier conjecture rather than as a multiplier already justified
  by the cited unconditional theorem.

So the theorem target is faithful, but the proof basis is not faithful to the cited source.

## verify_proof
First incorrect step found:

- `approach_A`, `lemma_graph` item 1, and the opening paragraph of `chosen_plan` infer that
  `13` is a numerical multiplier from `13 | n` and `gcd(13,477)=1`.

Why this fails:

- The Gordon-Schmidt survey's unconditional first multiplier theorem requires a prime
  `p > lambda`.
- Here `lambda = 87`, so `13 < 87`; the theorem does not apply.
- Table 2's `MC primes` column does not certify unconditional multiplier status for this
  row.

Everything after that point is conditional on a premise not established in the record.
The later orbit decomposition and quotient-moment contradiction are internally coherent
as a conditional argument, but they do not verify the intended theorem without an
independent proof that `13` is a genuine multiplier here.

Proof verdict:

- exact theorem not verified
- strongest local obstruction is only conditional

## verify_adversarial
Arithmetic and consistency checks rerun:

- `117 + 87*53 = 4728`
- `4728 - 399 = 4329`, and `4329 mod 169 = 104`
- orbit count check: `9 + 36*13 = 477`
- size decomposition check: `9 + 15*13 = 204`

These computations confirm that the contradiction would be valid if the `13`-stability
premise were available. No arithmetic defect was found downstream of the multiplier step.

Adversarial conclusion:

- the proof breaks at the first multiplier claim, not at the later arithmetic
- no code/checker existed to rerun beyond these direct sanity checks

## verify_theorem_worthiness
Exactness:

- The intended theorem slice remains exact and well-posed.

Novelty:

- Within the bounded 2026-04-15 audit, the exact row still appears frontier-novel.
- No rediscovery was established, but the novelty check remains bounded rather than final.

Reproducibility:

- The current artifact is reproducible only as a conditional argument.
- The unconditional theorem is not reproducible from the written proof because the
  multiplier input is missing.

Lean readiness:

- Not Lean-ready. Formalization would only formalize a proof gap.

Paper leverage:

- The target row still looks micro-paper eligible if solved.
- The current verified output is not yet paper-shaped because it does not establish the
  title theorem.

Required explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  Yes. A correct exact nonexistence proof for this row would still provide most of the note.
- What percentage of the paper would one solve already provide?
  About `70-80%` for the target theorem, but the current verified artifact provides much
  less because the main multiplier premise is missing.
- What title theorem is actually visible?
  Only the conditional theorem:
  `If 13 is a valid multiplier for any (477,204,87)-difference set in C_3 x C_159, then no such difference set exists.`
- What part of the argument scales?
  The orbit-plus-quotient contradiction template scales once a genuine multiplier is in hand.
- What part clearly does not?
  The present run does not justify the multiplier itself, and that missing step is the
  entire load-bearing gateway.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`?
  `NONE` for the current verified artifact. The target theorem could still become a
  `SLICE_CANDIDATE` once an unconditional proof exists.

## verify_verdict
`NOT_VERIFIED`

The run did not establish rediscovery, but it also did not verify the claimed nonexistence
theorem. The strongest honest outcome is that the current solve artifact contains a useful
conditional obstruction template, not a proved theorem.

## minimal_repair_if_any
No tiny conservative repair is available.

What would be needed is load-bearing, not cosmetic:

- either an independent unconditional proof that `13` is a multiplier for this exact row,
- or a different obstruction that avoids assuming multiplier status.

So this should return to solve rather than be patched in verify.

## publication_prior_art_audit
Bounded prior-art pass completed on `2026-04-15`.

- Exact-statement web searches for the tuple `(477,204,87)` together with `[3,159]` and
  `C_3 x C_159` surfaced the canonical Gordon-Schmidt survey, but no later source
  explicitly settling this exact row.
- Alternate-notation searches (`[3,159]`, `C3 x C159`, `Z_3 x Z_159`) likewise did not
  surface a direct construction or nonexistence paper for this exact case.
- The canonical source remains decisive: Gordon-Schmidt state that Table 2 gives the
  smallest open cases, and Table 2 still contains the row
  `477 204 87 [3,159]`.
- The source-internal check matters here: the survey's easy unconditional multiplier
  theorem is the First Multiplier Theorem, which requires `p > lambda`; for this row
  `13 < 87`, so the source does not hand the solve packet the needed multiplier input for
  free.
- The survey also explains that the Table 2 `MC primes` column records primes that would
  be multipliers under the multiplier conjecture; that column is not, by itself, a proof
  that the listed prime is already an unconditional multiplier for the row.
- As a bounded outside-source freshness check, Dan Gordon's current publications page on
  `2026-04-15` lists later difference-set papers through `2025`, and the current
  difference-set repository page remains the maintained status surface; this pass did not
  locate a later exact-row settlement there either.

Audit verdict:

- No rediscovery surfaced in the bounded audit.
- That is not a proof of openness, but it is enough to keep the packet out of
  `REDISCOVERY`.

## publication_statement_faithfulness
The selected problem is faithful to the literature: the exact target really is the row
`477 204 87 [3,159]` listed in Table 2 of the Gordon-Schmidt survey.

The current solve record is not fully faithful to what has been established:

- It is faithful as a target theorem.
- It is not faithful as a completed proof packet, because it treats `13` as though it had
  already been justified as an unconditional multiplier for this exact row.
- The current artifacts honestly support a conditional structural obstruction, not the
  unconditional nonexistence theorem written in `candidate_theorem_slice`.

## publication_theorem_worthiness
If the exact nonexistence theorem were proved, this would be a real title-theorem slice:
it removes one named open row from a canonical survey table.

For the current packet, the strongest honest claim is still stronger than “here is an
example,” because the argument is structural:

- It uses a multiplier-orbit and quotient-moment template rather than a hand-picked small
  computation.
- It is not merely instance-enumerative.
- It identifies a potentially reusable obstruction shape.

But theorem-worthiness fails at the publication threshold in its present form:

- The referee question “what is the theorem?” is not answered cleanly by the current
  packet, because the visible claim is only conditional on the missing multiplier step.
- The packet is not too dependent on hand-picked small cases, but it is still dependent on
  one unproved gateway premise.
- So the exact target has theorem value, while the current strongest honest claim has only
  limited theorem value.

## publication_publishability
Current publishability verdict: not paper-ready.

- If the exact theorem were correct and verified, the note would still be close to
  publishable, because the survey already supplies the frontier framing.
- In the current bounded state, however, the remaining gap is not editorial or Lean-facing;
  it is mathematical and load-bearing.
- The packet therefore did not turn out to be “almost a paper” after audit. It looked
  attractive before audit because the target row is well chosen, but the present proof
  packet is not close enough to human-ready publication.
- This should be moved aside rather than expanded into a broader theorem program unless the
  missing multiplier step can be closed directly and quickly.

## publication_packet_audit
Packet audit summary:

- Strongest current artifact: a conditional obstruction template.
- Proof artifacts preserved: yes.
- Canonical frontier anchor preserved: yes.
- Human-ready publication packet: no.
- Referee-ready title theorem packet: no.
- Lean would not directly seal this packet; formalization would only become useful after
  the unconditional mathematics is closed.

## micro_paper_audit
Micro-paper leverage remains real at the target level but not at the current packet level.

- One exact solve of this row would still likely provide about `70-80%` of a short note,
  because the theorem statement, novelty hook, and paper shape are already concentrated in
  one survey-table row.
- The current packet delivers materially less than that, because the missing multiplier
  justification blocks the title theorem itself.
- So the candidate remains micro-paper-eligible in principle, but this audit does not
  certify a near-paper packet.

Required explicit answers:

- Is the strongest honest claim stronger than “here is an example”?
  Yes. It is a conditional structural obstruction, not just an example.
- Would this result, if correct and verified in the current bounded sense, already
  constitute most of a publishable note?
  No for the current bounded packet; yes for the intended exact theorem.
- What percentage of the paper would one solve already provide?
  About `70-80%` for the exact theorem, but the current packet is well below that because
  the multiplier premise is still open in the artifacts.
- Is there a real title theorem, theorem slice, or counterexample theorem here?
  Yes as a target slice; not yet as a supported packet.
- Is the proof structural or merely instance-specific?
  Structural in style.
- Would this survive a referee asking “what is the theorem?”
  Not in its current conditional form.
- Is the claim still too dependent on hand-picked small cases?
  No, but it is too dependent on one unproved multiplier gateway.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the
  candidate only look attractive before audit?
  The remaining gap is not genuinely small in the present packet.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a
  larger theorem program?
  Yes.
- Would Lean directly seal the packet, or would it only be optional polish / later
  archival formalization?
  Only later polish after new mathematics closes the proof.

## strongest_honest_claim
The current artifacts support the following strongest honest claim:

`If 13 is an unconditional multiplier for any (477,204,87)-difference set in C_3 x C_159, then the orbit-plus-quotient argument in this packet yields nonexistence.`

That is a useful structural side result, but it is not the target theorem and it is not a
paper-ready packet.

## paper_title_hint
`A Conditional 13-Multiplier Obstruction for the (477,204,87) Difference-Set Case in C_3 x C_159`

## next_action
Move this row aside rather than expanding it.

Reopen only if one of the following arrives quickly and explicitly:

- a citation-ready unconditional proof that `13` must be a multiplier for this exact row,
- or an independent exact obstruction that avoids the multiplier premise entirely.
