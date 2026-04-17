# Solve Record: On the Cyclic (781,300,115) Difference-Set Problem

- slug: `cyclic-difference-set-781-300-115`
- working_packet: `artifacts/cyclic-difference-set-781-300-115/working_packet.md`

## statement_lock
Determine whether the cyclic group `C_781` admits a `(781,300,115)` difference set.

- Exact parameter identity check: `(v - 1)λ = 780 * 115 = 89700 = 300 * 299 = k(k - 1)`.
- Order factorization: `781 = 11 * 71`.
- Difference-set norm parameter: `n = k - λ = 185 = 5 * 37`.
- The intended title theorem, if the obstruction closes cleanly, is:
  `The cyclic group C_781 admits no (781,300,115) difference set.`
- A full nonexistence proof would already be about `80%` of a short paper because the statement is a named surviving cyclic row with light remaining packaging.

## definitions
- Work additively in `G = Z/781Z`.
- A `(781,300,115)` difference set is a subset `D ⊂ G` of size `300` such that every nonzero `g ∈ G` has exactly `115` ordered representations `g = d_1 - d_2` with `d_i ∈ D`.
- For a divisor `w | 781`, write `u = 781 / w` and let `b_i` be the number of elements of `D` in the residue class `i mod w`.
- The standard contracted equations for the residue counts are:
  `Σ_i b_i = 300`,
  `Σ_i b_i^2 = n + λu`,
  `Σ_i b_i b_{i-j} = λu` for every nonzero `j mod w`.
- The transfer kit points to Baumert-Gordon Theorems `3.1` and `3.2`: the first supplies these contracted equations, while the second supplies suitable `w`-multipliers coming from the prime divisors `5, 37` of `n`.
- Binding ambiguity for this run: I am using only the theorem content recorded in the packet, not re-importing the full paper text. Any final unconditional claim therefore has to remain faithful to that recorded contracted-multiplier premise.

## approach_A
Structural / invariant route: contract modulo `11`.

1. Use the contracted multiplier criterion on `w = 11`.
2. Choose `t = 5`, because `5 ≡ 5^1 (mod 11)` and also `37^2 ≡ 5 (mod 11)`, so the two prime divisors of `n` meet at the same multiplier residue class.
3. Since `gcd(t - 1, 11) = gcd(4,11) = 1`, a translated contraction can be taken `5`-invariant.
4. Multiplication by `5` on `Z/11Z` has orbit decomposition
   `{0}`, `Q = {1,3,4,5,9}`, and `N = {2,6,7,8,10}`.
5. Therefore the mod-`11` contraction has the form
   `c_0 = a`, `c_i = x` on `Q`, `c_i = y` on `N`.
6. The contracted equations give
   `a + 5x + 5y = 300`,
   `a^2 + 5x^2 + 5y^2 = 8350`.
7. Because `a ≡ 300 (mod 5)`, write `a = 5m`. Then
   `x + y = 60 - m`,
   `x^2 + y^2 = 1670 - 5m^2`.
8. The discriminant condition for integer `x,y` becomes
   `Δ = (x - y)^2 = -11m^2 + 120m - 260`.
9. With `0 ≤ a ≤ 71`, hence `0 ≤ m ≤ 14`, the only nonnegative square values are:
   `m = 3`, giving `(a,x,y) = (15,28,29)` up to swapping `x,y`;
   `m = 6`, giving `(a,x,y) = (30,23,31)` up to swapping `x,y`.

Self-check for Approach A:
- The algebra is internal to the packet assumptions and does not need code.
- This does not yet contradict existence; it only narrows the mod-`11` quotient to two possible occupancy patterns.

## approach_B
Construction / extremal / contradiction route: contract modulo `71`.

1. Use the same multiplier residue `t = 5`.
2. Here `5^5 = 3125 ≡ 1 (mod 71)`, so multiplication by `5` on `Z/71Z` has one fixed point `0` and `14` nonzero orbits of size `5`.
3. After translation, the mod-`71` contraction should therefore be constant on each of those `14` nonzero `5`-orbits.
4. Write the mod-`71` contraction as `b_0 = a` and `b_i = r_j` on the `j`th nonzero orbit.
5. Since each residue class mod `71` lifts to `11` points in `G`, the basic equations become
   `a + 5 Σ_j r_j = 300`,
   `a^2 + 5 Σ_j r_j^2 = 1450`,
   `Σ_i b_i b_{i-s} = 1265` for every nonzero `s mod 71`.
6. Because `0 ≤ a ≤ 11` and `a ≡ 300 (mod 5)`, only `a ∈ {0,5,10}` are possible.
7. This leaves a finite orbit-constant search problem on `15` integer variables, but it is theorem-facing rather than generic brute force: it checks exact coefficient equations forced by the multiplier reduction.

Self-check for Approach B:
- This is the stronger route because the fiber bound `b_i ≤ 11` is much tighter than the mod-`11` bound `c_i ≤ 71`.
- The only missing step is the exact orbit-constant consistency check for the nonzero correlation equations.

## lemma_graph
1. `Multiplier setup`: from the packeted Baumert-Gordon multiplier theorem, `t = 5` is a valid contracted multiplier at least for `w = 11`, and plausibly for `w = 71` as well.
2. `Translation normalization`: because `gcd(t - 1, w) = 1` for `w = 11,71`, a translate may be taken `t`-invariant on the contracted quotient.
3. `Orbit lemma mod 11`: the contraction is determined by three integers `(a,x,y)` on `{0}`, `Q`, `N`.
4. `Orbit lemma mod 71`: the contraction is determined by `a` plus one value on each nonzero `5`-orbit.
5. `Arithmetic slice`: mod `11` leaves only two occupancy patterns.
6. `Main obstruction target`: show that no mod-`71` orbit-constant integer vector satisfies all exact contracted equations.
7. `Conclusion if step 6 closes`: nonexistence of a cyclic `(781,300,115)` difference set.

## chosen_plan
Use Approach B as the main line.

- Approach A already shows the multiplier reduction is nontrivial and compresses the quotient sharply.
- The best next step is a bounded exact checker for the mod-`71` orbit-constant system.
- If the reduced system has no solution, the result is paper-shaped: it gives an exact cyclic nonexistence theorem for a long-lived residual row.
- If the reduced system still has solutions, the honest output is a theorem slice consisting of the two mod-`11` patterns plus the surviving mod-`71` orbit constraints.

## self_checks
- Statement locked and parameter identity verified.
- Two distinct reasoning approaches recorded before code.
- The intended path is still the same micro-paper lane: an exact obstruction for the named cyclic row.
- No silent fallback to broad search has happened.
- After the reasoning writeup, I added only candidate-local code for the exact orbit-compressed consistency check.
- The reduced checker did not finish quickly enough in-budget to certify the mod-`71` contradiction, so the honest endpoint of this run remains the quotient theorem slice.

## code_used
- Added [orbit_contraction_check.py](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/cyclic-difference-set-781-300-115/orbit_contraction_check.py).
- Purpose: exact bounded check of the mod-`71` `5`-orbit-constant contraction system under the packeted multiplier premise.
- Outcome in this run: the script preserves the intended reduced obstruction search, but it did not finish quickly enough to upgrade the current slice to a full nonexistence proof.

## result
Current best honest result:

- The mod-`11` contracted multiplier analysis leaves only two possible quotient patterns:
  `(15,28,29)` and `(30,23,31)` up to swapping the two nonzero `5`-orbits.
- Natural corollary / boundary remark:
  in particular, any hypothetical cyclic `(781,300,115)` difference set has `15` or `30` elements in the subgroup of index `11`.
- This is a genuine theorem-facing slice, but it is still too thin for the micro-paper lane by itself.
- The decisive unresolved step is still the mod-`71` orbit-constant contradiction.
- The bounded checker for that step has been preserved locally, but this run does not claim a solved nonexistence theorem.

## family_affinity
Strong. This is exactly the cyclic small-parameter residual-row lane where multiplier-orbit contractions have historically produced short nonexistence arguments.

## generalization_signal
Moderate. The concrete calculation suggests a reusable template:
prime-factor multiplier alignment in `n`, small prime quotient `w`, then exact orbit-constant contracted equations on the complementary quotient.

- What scales:
  the common-multiplier alignment and three-cell quotient compression on a small prime quotient.
- What does not yet scale:
  the unresolved mod-`71` orbit search still depends on the detailed additive structure of the `5`-cyclotomic classes in `Z/71Z`.

## proof_template_reuse
If the `w = 71` obstruction closes, the reusable template is:
pick a common contracted multiplier residue from the prime divisors of `n`, normalize by translation, collapse the quotient to orbit variables, and solve the exact contracted system.

## candidate_theorem_slice
Conditional theorem slice already visible:

`Assuming the packeted contracted-multiplier criterion applies with t = 5, any hypothetical cyclic (781,300,115) difference set has mod-11 contraction equal to either (15,28,29) or (30,23,31) on the orbit partition {0}, Q, N, up to swapping the two nonzero orbit values.`

The smallest supporting theorem slice extracted from the run is:

`Under the same multiplier premise, the index-11 subgroup contains either 15 or 30 points of any hypothetical cyclic (781,300,115) difference set.`

## smallest_param_shift_to_test
The smallest useful shift is not another parameter tuple yet; it is the companion quotient `w = 71` for the same tuple. If this run stalls, the next highest-value perturbations are:

- tighten the mod-`71` checker with stronger pruning or an orbit-algebra reformulation;
- test whether one can combine the two mod-`11` occupancy patterns with the mod-`71` sum/square constraints before invoking the full nonzero-correlation system.

## why_this_is_or_is_not_publishable
Not publishable yet.

- A full nonexistence proof would already be `70-90%` of a paper.
- The current artifact only isolates a quotient pattern and a clean reduced search problem.
- The current result is still closer to `SLICE_CANDIDATE` than to a paper-shaped note.
- Minimal remaining packaging work, if the obstruction closes, would be:
  state the common multiplier residue,
  present the orbit-constant quotient equations,
  give the contradiction certificate,
  and add the source-chain paragraph showing that `(781,300,115)` remained open in the bounded literature packet.

## paper_shape_support
- Exact title theorem if solved:
  `The cyclic group C_781 admits no (781,300,115) difference set.`
- Immediate paper-shaped support if solved:
  one quotient lemma at `w = 11`,
  one orbit-constant obstruction at `w = 71`,
  and a short boundary remark that the result closes one named residual cyclic row with `k ≤ 300`.
- Minimal remaining packaging from the current slice alone would still be too much; the note only becomes paper-shaped if the mod-`71` contradiction or an equivalent exact obstruction closes.

## boundary_remark
The mod-`11` slice already shows this is not just an arbitrary search problem: a hypothetical solution would have to realize one of only two highly rigid quotient occupancy profiles. The remaining uncertainty is whether that rigidity already forces a contradiction on the `71`-side.

## likely_failure_points
- The exact statement of the contracted multiplier theorem is not reloaded from source in this run; I am relying on the packeted summary.
- The mod-`71` orbit-constant system might still admit solutions, in which case the current line yields only a slice, not the title theorem.
- Even if the mod-`71` system is inconsistent, I need to make sure the normalization from multiplier to orbit-constant contraction is stated without a hidden gap.
- The local checker currently preserves the search but is not yet optimized enough to certify the reduced contradiction quickly.

## what_verify_should_check
- Verify the exact contracted multiplier statement used to make `t = 5` a valid multiplier for `w = 11` and `w = 71`.
- Check the translation-normalization step `gcd(t - 1,w)=1`.
- Recompute the mod-`11` algebra and the two surviving patterns.
- If a mod-`71` checker is run next, verify the orbit table and the exact correlation equations it encodes.

## verify_rediscovery
Bounded prior-art audit completed with the allowed limited web budget.

- Search patterns used: the exact tuple `(781,300,115)`, the alternate row notation `[781]`, the canonical Baumert-Gordon source title, the Gordon-Schmidt survey title, and the La Jolla Difference Set Repository / status-slide surface.
- Surfaced status chain: Baumert-Gordon 2004 still lists `(781,300,115)` among the surviving cyclic rows in Table 3; Gordon-Schmidt 2015 still lists `[781]` in Table 2; Gordon's 2019 LJDSR slides still surface `[781]` as open.
- No boundedly surfaced theorem, proposition, example, observation, corollary, or later discussion was found that settles the exact cyclic `C_781` instance.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness
The solve artifact does not match the intended statement exactly.

- Intended statement: determine whether `C_781` admits a `(781,300,115)` difference set.
- Strongest actual claim supported locally: a conditional mod-`11` contraction slice under the packeted contracted-multiplier premise.
- The solve record repeatedly frames the intended title theorem as cyclic nonexistence, but the proved content stops short of that and never reaches an exact existence/nonexistence determination.
- Because the strongest supported claim is nearby but different, the correct harness classification is `VARIANT`, not a solved exact-instance status.

## verify_proof
First incorrect load-bearing step found in `approach_B`, step 1: "Use the same multiplier residue `t = 5`" for `w = 71`.

- By the packeted Baumert-Gordon multiplier criterion, for a chosen divisor `w | v` the same residue `t (mod w)` must be represented by powers of every prime divisor of `n = 185 = 5 * 37`.
- Modulo `11`, this is fine: powers of `5` and powers of `37` both realize `t = 5`, and `gcd(5 - 1, 11) = 1`.
- Modulo `71`, the power sets disagree. Independent recomputation gives
  `5^j mod 71 in {1,5,25,54,57}` and
  `37^j mod 71 in {1,20,30,32,37,45,48}`.
- Their intersection is only `{1}`. Thus there is no nontrivial common `71`-multiplier residue with `gcd(t - 1, 71) = 1`, so the translation-normalized `5`-orbit reduction on `Z/71Z` is unjustified.
- Everything downstream that depends on that `w = 71`, `t = 5` orbit-constant model loses proof force, including the proposed contradiction route and the local checker.
- Independent recomputation confirms that the mod-`11` algebra itself is correct: the only integer solutions to
  `a + 5x + 5y = 300` and `a^2 + 5x^2 + 5y^2 = 8350`
  are `(15,28,29)` and `(30,23,31)` up to swapping `x,y`.

## verify_adversarial
The computational support was rerun skeptically.

- The local script `orbit_contraction_check.py` was executed, but it did not return a bounded contradiction certificate during the verification poll window.
- More importantly, the script encodes the invalid assumption that `t = 5` is a valid contracted multiplier modulo `71`; even a fast "no solution" output would therefore not certify the intended theorem.
- A separate independent arithmetic check reproduced the mod-`11` slice exactly, so that narrow slice appears computationally consistent.
- Adversarial conclusion: the code supports only a conditional and incomplete quotient slice, not the claimed route to nonexistence.

## verify_theorem_worthiness
Assessment of the strongest honest surviving claim:

- Exactness: not exact for the intended statement. The surviving result is only a conditional theorem slice.
- Novelty: bounded audit did not find rediscovery of the exact row, but novelty of the current slice alone is not the bottleneck.
- Reproducibility: the mod-`11` arithmetic is reproducible; the decisive nonexistence step is not.
- Lean readiness: `false`. Formalizing the current slice would formalize the wrong object first; the remaining gap is mathematical, not Lean labor.
- Paper leverage: low for the current slice. The present artifact is not "one solve away" in its current verified form because the advertised main obstruction collapses at `w = 71`.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of a paper does the current verified slice provide? About `20-25%`.
- What title theorem is actually visible? At best:
  `Under the valid mod-11 multiplier premise, any hypothetical cyclic (781,300,115) difference set has mod-11 contraction equal to (15,28,29) or (30,23,31), up to swapping the two nonzero 5-orbits.`
- What part scales? The mod-`11` contracted-multiplier compression and the resulting two-pattern arithmetic slice.
- What part clearly does not? The proposed `w = 71` `t = 5` orbit-constant reduction, and any contradiction extracted from that model.
- Best honest publication status now: `NONE`, not `INSTANCE_ONLY` and not `SLICE_CANDIDATE`, because the surviving claim is a conditional structural slice rather than a paper-shaped exact-instance result.

## verify_verdict
`NOT_VERIFIED`

- No rediscovery was established in the bounded prior-art pass.
- The intended exact statement was not proved.
- The first incorrect load-bearing step is the unsupported extension of the multiplier residue `t = 5` from `w = 11` to `w = 71`.
- The strongest honest retained output is a conditional mod-`11` quotient slice, so the run should be downgraded to `VARIANT`.

## minimal_repair_if_any
Tiny conservative repair available:

- Keep the verified mod-`11` slice only.
- Remove theorem-level reliance on the `w = 71` checker and on any claim that `t = 5` acts as a valid multiplier modulo `71`.
- Do not promote this run toward Lean or publication until a valid nontrivial `w = 71` (or alternate exact) obstruction is supplied from a justified multiplier premise.

## publication_prior_art_audit
Bounded publication prior-art audit completed on `2026-04-15`.

- Exact-statement searches for `"(781,300,115) difference set"` and `"cyclic (781,300,115) difference set"` surfaced the same tuple-specific status chain already in the packet: Baumert-Gordon `2004`, Gordon-Schmidt `2015`, and Gordon's `2019` LJDSR slides.
- Alternate-notation search for `"[781]" difference set` again surfaced the `2015` survey table and the `2019` slides, with no later exact-tuple settlement found in the bounded pass.
- Canonical-source check: Baumert-Gordon `2004` lists `781 300 115 185` only in Table 3 as a surviving cyclic row with `gcd(v,n)=1`; the named theorems and examples in Sections `3.2`-`3.4` treat other tuples such as `(429,108,27)` and `(303,151,75)`, not this exact row.
- Theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source found no local statement in Baumert-Gordon `2004` that already settles `(781,300,115)`.
- Outside-source status search: the current Difference Sets database page on Dan Gordon's site still presents an open / exists / does-not-exist parameter database for `v < 100000` and points to more recent multiplier-conjecture computations for `v < 10^6`, but bounded site-specific searches on `2026-04-15` surfaced no newer theorem or database hit settling `(781,300,115)`.
- No extra citation-chase was warranted after that narrow pass, because the packet already fails on statement-faithfulness and theorem closure rather than on novelty.

Conservative audit verdict: no rediscovery was established within the bounded pass, but the literature check does not rescue the current packet from its mathematical gap.

## publication_statement_faithfulness
The packet is not faithful to the selected statement at publication level.

- Selected statement: determine whether `C_781` admits a `(781,300,115)` difference set.
- Strongest honest supported claim: a conditional mod-`11` contraction lemma under the valid `w = 11` multiplier premise.
- This is stronger than "here is an example," because it gives a rigid necessary condition on any hypothetical difference set.
- It is still not the selected theorem. The current artifact does not determine existence or nonexistence in `C_781`.
- The surviving claim depends on a hand-picked quotient and on the packeted multiplier premise, while the attempted decisive `w = 71` route failed verification.
- A referee asking "what is the theorem?" would not receive the advertised title theorem; they would receive a small conditional structural lemma instead.

## publication_theorem_worthiness
The surviving result has some theorem content, but not enough theorem weight for this lane.

- Is the strongest honest claim stronger than "here is an example"? Yes, but only modestly: it is a conditional structural obstruction slice.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a theorem slice, but not a title theorem and not a counterexample theorem.
- Is the proof structural or merely instance-specific? Structural in method, instance-specific in scope, and still conditional on the valid mod-`11` multiplier setup.
- Would this survive a referee asking "what is the theorem?" No. The current answer is too small and too premise-dependent.
- Is the claim still too dependent on hand-picked small cases? Yes. The packet now rests on one quotient contraction and two occupancy patterns, not on a decisive row-closing theorem.
- If this is not yet paper-ready, is the remaining gap genuinely small? No. The remaining gap looked small before audit, but after the `w = 71` failure it is no longer a light closing step.

## publication_publishability
This is not publication-ready in the micro-paper sense.

- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- What percentage of a publishable note does the current boundedly supported result provide? About `20-25%`.
- Prospectively, an exact solve of the original row would still likely supply around `80%` of a short note, but that prospective leverage is not the same as the current audited packet.
- The current slice is too thin to carry the note by itself, because it does not close the row and does not yet force a theorem-sized obstruction.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. The honest action is to preserve the valid mod-`11` slice and move the candidate aside until a new exact route is found.
- Lean would not directly seal the packet. It would only formalize a conditional slice and would function as optional archival polish on a non-paper-ready result, not as the missing mathematical closure.

Publication status decision: `NONE`.

## publication_packet_audit
Packet-quality audit for the current strongest honest claim:

- `publication_status`: `NONE`
- `publication_confidence`: `high`
- `publication_packet_quality`: thin
- `proof_artifacts_preserved`: yes, for the surviving mod-`11` slice and for the failed `w = 71` route as an audited dead end
- `lean_packet_seal`: no
- `human_ready`: no

Why not `SLICE_CANDIDATE`:

- the current slice is conditional rather than theorem-closing,
- the remaining mathematical gap is not small after skeptical checking,
- and the packet would not satisfy the "what is the theorem?" referee test.

## micro_paper_audit
This run fails the strict micro-paper lane in its current audited form.

- The candidate originally looked attractive because a direct solve of `(781,300,115)` would be title-theorem-sized with light packaging.
- After audit, the current verified residue is only a conditional mod-`11` structural lemma.
- That is too small to count as the title theorem of a short note.
- The publication narrative remains real at the row level, but the current proof packet does not cash it out.
- The strongest honest packet is therefore not "close to paper"; it only looked close before the invalid `w = 71` route was removed.

## strongest_honest_claim
Under the valid mod-`11` multiplier premise from Baumert-Gordon Theorem `3.2`, any hypothetical cyclic `(781,300,115)` difference set has mod-`11` contraction equal to `(15,28,29)` or `(30,23,31)`, up to swapping the two nonzero `5`-orbits. In particular, the index-`11` subgroup contains either `15` or `30` points.

## paper_title_hint
No current publication title is recommended. The least misleading fallback title would be:

`Mod-11 Contraction Constraints for a Hypothetical Cyclic (781,300,115) Difference Set`

but this is not strong enough to justify a paper packet in the present lane.

## next_action
- Preserve the mod-`11` slice as a verified side theorem fragment.
- Treat the `w = 71`, `t = 5` route as audited dead code, not as near-complete proof.
- Move this candidate aside rather than widening it into a larger theorem program.
- Revisit only if a new exact obstruction or construction route is found that closes the `C_781` row without the invalid multiplier step.
