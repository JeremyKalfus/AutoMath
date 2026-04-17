# Solve Record: The Cyclic (1785,224,28) Difference-Set Case

- slug: `cyclic-difference-set-1785-224-28`
- working_packet: `artifacts/cyclic-difference-set-1785-224-28/working_packet.md`

## statement_lock
Determine whether the cyclic group `C_1785` admits a `(1785,224,28)` difference set.

For this solve pass I lock the intended title theorem as:

`The cyclic group C_1785 does not admit a (1785,224,28) difference set.`

If this argument is correct, it is already about `80%` of a micro-paper: the title theorem is exact, source-anchored, and needs only light packaging around Baumert-Gordon Table 2, the multiplier normalization, and the final quotient contradiction.

## definitions
Work additively in `G = Z/1785Z`.

A `(1785,224,28)` difference set is a subset `D ⊂ G` of size `224` such that every nonzero element of `G` has exactly `28` representations as `d1 - d2` with `d1,d2 ∈ D`.

Set

- `v = 1785 = 3 * 5 * 7 * 17`
- `k = 224`
- `λ = 28`
- `n = k - λ = 196 = 2^2 * 7^2`

For a quotient of order `w` with kernel size `m = v / w`, if the contracted coefficients are `b_0, ..., b_{w-1}`, then the standard contracted equations are

- `sum b_i = 224`
- `sum b_i^2 = n + λ m = 196 + 28m`

because the identity coefficient of the contracted group-ring product is `k + λ(m-1) = n + λm`.

Conventions and ambiguity resolution:

- I use the standard cyclic prime-multiplier fact only for the prime `2`, since `2 | n` and `gcd(2,1785)=1`.
- Because `2 - 1 = 1`, any translate parameter can be killed exactly, so I may replace a hypothetical difference set by a translate and assume `2D = D`.
- All later quotient coefficients are therefore constant on multiplication-by-`2` orbits.

## approach_A
Structural / invariant route.

1. Use `2 | n` and `gcd(2,1785)=1` to translate a hypothetical difference set so that `2D = D` exactly.
2. Compress modulo `17`. Since multiplication by `2` on `C_17` has orbit decomposition
   - `{0}`
   - two nonzero orbits of size `8`,
   the quotient profile must be `(a, b^8, c^8)`.
3. Solve the exact sum and square-sum equations on `C_17`. They force `a = 0` and `b = c = 14`. Hence `D` contains no element divisible by `17`.
4. Compress modulo `3`. Since `2` has orbit decomposition `{0}` and `{1,2}`, the mod-`3` contraction must be `(u, v, v)`. The quotient equations force `(u,v) = (84,70)`.
5. Pass to the mixed quotient `C_51 = C_3 × C_17`. Because the entire `0 mod 17` fiber is empty, the only classes contributing to the `0 mod 3` coefficient are the `16` classes divisible by `3` but not by `17`, and under multiplication by `2` these split into two size-`8` orbits.
6. Therefore the mod-`3` zero coefficient must be divisible by `8`, but step 4 forces it to be `84`, contradiction.

Self-check after approach A: this route is fully reasoning-first, uses only exact quotient arithmetic, and if correct already has the shape of a stand-alone residual-case note.

## approach_B
Construction / extremal / contradiction route.

Use the same exact `2D = D` normalization, then work modulo `15` and modulo `17` simultaneously.

1. Modulo `17`, force the zero class to vanish and all nonzero classes to have coefficient `14`.
2. Modulo `5`, solve the orbit-constant contraction `(56,42,42,42,42)`.
3. Try to push these two contractions through the CRT quotient `C_85`.
4. Seek a contradiction from the `2`-orbit sizes on the fibers over `0 mod 5` versus nonzero mod `5`.

This approach looks viable but heavier: it introduces more local variables than needed and does not improve on the cleaner `C_17 -> C_51 -> C_3` contradiction.

Self-check after approach B: useful as a backup family template, but it adds bookkeeping without sharpening the core contradiction.

## lemma_graph
Proof skeleton.

1. Multiplier normalization:
   if `D` is a cyclic `(1785,224,28)` difference set, then since `2 | n` and `gcd(2,1785)=1`, after translation one may assume `2D = D`.
2. Mod-`17` orbit decomposition:
   multiplication by `2` on `C_17` has one fixed point and two size-`8` nonzero orbits.
3. Mod-`17` equations:
   if the coefficients are `(a,b,c)` on those three orbits, then
   - `a + 8b + 8c = 224`
   - `a^2 + 8b^2 + 8c^2 = 196 + 28 * 105 = 3136`
4. Solving step 3 gives uniquely `a = 0`, `b = 14`, `c = 14`.
5. Therefore every residue class congruent to `0 mod 17` is empty in every finer quotient.
6. Mod-`3` orbit decomposition:
   multiplication by `2` on `C_3` has orbits `{0}` and `{1,2}`.
7. Mod-`3` equations:
   if the coefficients are `(u,v,v)`, then
   - `u + 2v = 224`
   - `u^2 + 2v^2 = 196 + 28 * 595 = 16856`
   which give uniquely `(u,v) = (84,70)`.
8. Mod-`51` orbit decomposition after step 5:
   among the `17` classes congruent to `0 mod 3`, one class is `0 mod 17` and has coefficient `0`; the remaining `16` classes split into two size-`8` `2`-orbits.
9. Hence the mod-`3` zero coefficient must be a sum of two terms of the form `8x`, so it is divisible by `8`.
10. But step 7 gives that coefficient as `84`, impossible.

Self-check after lemma graph: every step is now exact, local, and theorem-facing; no bounded experiment is needed.

## chosen_plan
Choose approach A.

Reason:

- it uses the smallest effective multiplier, namely `2`;
- it produces an exact mod-`17` theorem slice before the contradiction;
- it closes without code, search, or a separate residue check;
- the contradiction lives in a mixed quotient `C_51`, which fits the intended contracted-multiplier paper shape from the packet.

Extra structure that makes the result paper-shaped if the main claim closes:

- the exact mod-`17` contraction `(0,14,14)` on the three `2`-orbits;
- the exact mod-`3` contraction `(84,70,70)`;
- the explicit `C_51` orbit-count contradiction showing why those two slices cannot coexist;
- the observation that the obstruction is caused by the empty `0 mod 17` fiber together with the parity-of-orbit-size obstruction inside the `0 mod 3` fiber.

Minimal remaining packaging work if this proof survives verify:

- cite the prime-multiplier normalization cleanly;
- write the two quotient lemmas as propositions;
- add one short paragraph explaining why this exact row survives Baumert-Gordon Table 2 but dies under this sharper mixed-quotient obstruction.

## self_checks
After major steps:

1. Statement lock:
   the target remains the exact Baumert-Gordon row `(1785,224,28)`, not a feeder slice.
2. Multiplier step:
   the only multiplier fact used is the standard one for prime `2`, which is the cleanest available because `2-1=1` kills the translate parameter immediately.
3. Mod-`17` step:
   I checked the arithmetic explicitly:
   - `3136 = 56^2`
   - `a` must be a multiple of `8`
   - testing `a ∈ {0,8,16,24}` leaves only `a=0`, and then `b+c=28`, `b^2+c^2=392`, so `bc=196` and `b=c=14`
4. Mod-`3` step:
   solving
   - `u + 2v = 224`
   - `u^2 + 2v^2 = 16856`
   gives `v=70`, `u=84`
5. Final contradiction:
   the `0 mod 3` fiber inside `C_51` has exactly `17` classes; one is the empty `0 mod 17` class, and the other `16` are partitioned into two size-`8` orbits, so its total coefficient must lie in `8Z`
6. Final self-check:
   `84` is not divisible by `8`, so the contradiction is exact and does not depend on any hidden search assumption.

## code_used
No code was used.

No checker, bounded search, or witness verification was needed because the quotient equations and orbit sizes close the contradiction directly.

## result
Provisional exact disproof in solve stage.

Claim:
`C_1785` does not admit a `(1785,224,28)` difference set.

Proof attempt.

Assume `D ⊂ Z/1785Z` is a cyclic `(1785,224,28)` difference set.

Step 1. Normalize by the prime multiplier `2`.

Since `2 | n = 196` and `gcd(2,1785)=1`, the standard cyclic prime-multiplier theorem gives `2D = D + s` for some `s`. Replacing `D` by `D - s`, we may assume

`2D = D`.

So every contracted coefficient vector in every quotient is constant on multiplication-by-`2` orbits.

Step 2. Solve the mod-`17` contraction exactly.

On `C_17`, multiplication by `2` has orbit decomposition

- `{0}`
- one size-`8` orbit on the quadratic residues
- one size-`8` orbit on the nonresidues

Let the corresponding coefficients be `a,b,c`. The kernel size is `1785 / 17 = 105`, so

- `a + 8b + 8c = 224`
- `a^2 + 8b^2 + 8c^2 = 196 + 28 * 105 = 3136`

Because `224 - a` is divisible by `8`, `a` is a multiple of `8`. Also `a >= 0`, and from the second equation one gets `a <= 24`. So `a ∈ {0,8,16,24}`.

Checking these values:

- `a=0` gives `b+c=28` and `b^2+c^2=392`, hence `bc=196` and `b=c=14`
- `a=8` gives `b+c=27` and `b^2+c^2=384`, impossible
- `a=16` gives `b+c=26` and `b^2+c^2=360`, impossible
- `a=24` gives `b+c=25` and `b^2+c^2=320`, impossible

Therefore the unique mod-`17` contraction is

`(0,14,14)`.

In particular, `D` contains no element congruent to `0 mod 17`.

Step 3. Solve the mod-`3` contraction exactly.

On `C_3`, multiplication by `2` has orbits `{0}` and `{1,2}`. Let the coefficients be `(u,v,v)`. The kernel size is `1785 / 3 = 595`, so

- `u + 2v = 224`
- `u^2 + 2v^2 = 196 + 28 * 595 = 16856`

Substituting `u = 224 - 2v` gives

`3v^2 - 448v + 16660 = 0`,

whose discriminant is `448^2 - 12 * 16660 = 784 = 28^2`. Thus

`v = 70`, `u = 84`.

So the mod-`3` contraction is

`(84,70,70)`.

Step 4. Derive the contradiction on `C_51`.

Consider the quotient `C_51 = C_3 × C_17`.

From step 2, the total coefficient on the `0 mod 17` fiber is `0`. Since the coefficients in `C_51` are nonnegative, each of the three residue classes

- `0`
- `17`
- `34`

has coefficient `0`.

Now look at the residue classes congruent to `0 mod 3`. There are `17` such classes in `C_51`; one of them is `0 mod 17`, namely the class `0`, and it has coefficient `0`. The remaining `16` classes are divisible by `3` but not by `17`.

Because `2D = D`, the coefficients on `C_51` are constant on multiplication-by-`2` orbits. On those `16` classes, multiplication by `2` acts with orbit size `8` because the mod-`3` coordinate is fixed at `0` while the nonzero mod-`17` coordinate runs in a `2`-orbit of size `8`. Hence those `16` classes split into exactly two size-`8` orbits.

Therefore the total coefficient on the `0 mod 3` fiber is a sum of two multiples of `8`, so it must be divisible by `8`.

But by step 3 the `0 mod 3` coefficient is exactly `84`, and `84` is not divisible by `8`.

Contradiction.

Therefore no cyclic `(1785,224,28)` difference set exists.

What part of the argument scales:

- exact normalization by a prime multiplier `p | n` with `gcd(p,v)=1`;
- solving a prime-quotient contraction with one fixed class and a few equal-sized orbits;
- using an empty fiber in one quotient to force a divisibility contradiction in a mixed quotient.

What part does not scale cleanly:

- the exact numbers `224`, `3136`, and `16856`;
- the final divisibility obstruction depends on the specific pair `(3,17)` and the orbit size `8` of `2 mod 17`.

What theorem slice is suggested:

- if a cyclic difference set with these parameters existed, then after translation it would be `2`-invariant and its mod-`17` contraction would have to be exactly `(0,14,14)`;
- that slice already forces the decisive mixed-quotient contradiction.

What next parameter shifts would help most:

1. other Baumert-Gordon rows with a small prime multiplier `p` satisfying `p-1 = 1` or a small invertible factor, so translation normalization is exact;
2. rows where a prime quotient gives an empty fiber and a second quotient turns that emptiness into an orbit-divisibility obstruction.

Current package assessment:

This is much closer to a paper-shaped claim than to a thin instance-only witness. If verify confirms the multiplier citation and quotient arithmetic, the result already reads like the main theorem of a short residual-case note.

## family_affinity
High family affinity with the Baumert-Gordon cyclic survivor lane.

This proof stays squarely inside the intended micro-paper family:

- start from a residual cyclic Table 2 row;
- use a multiplier coming from `n`;
- solve exact contracted equations on a prime quotient;
- finish with a mixed-quotient orbit contradiction.

It is not campaign work and does not require a feeder ladder.

## generalization_signal
Moderate positive generalization signal.

The reusable core is:

- choose a prime multiplier `p | n` with `gcd(p,v)=1`;
- normalize to exact `p`-invariance when the translate can be killed cheaply;
- solve a prime quotient where the nonzero part breaks into a small number of equal orbits;
- exploit an empty or highly rigid fiber in a second quotient.

## verify_rediscovery
Bounded rediscovery audit completed on `2026-04-15`.

- Exact-tuple searches for `"(1785,224,28)"`, `"1785 224 28 difference set"`, and the cyclic phrasing surfaced Baumert-Gordon `2004` as the direct tuple anchor.
- Alternate-notation searches using `C_1785`, `v=1785, k=224, lambda=28`, and site-specific Gordon / difference-set surfaces did not produce a later theorem, proposition, example, observation, or database hit explicitly settling this exact row.
- Canonical-source check: Baumert-Gordon `2004` lists `(1785,224,28)` among the surviving cyclic rows and gives the contracted-coefficient and contracted-multiplier machinery in Section `3`.
- Theorem / proposition / example / corollary checks inside the canonical source did not uncover any local statement already disposing of `(1785,224,28)`.
- One bounded later-status check on Gordon's difference-set publication surface likewise did not expose a direct later settlement for this tuple.

Conservative audit verdict: no rediscovery was established within the bounded pass, but the search also does not certify novelty beyond "no later exact settlement surfaced."

## verify_faithfulness
The solve artifact stayed locked to the intended statement, but the proved content does not reach that statement.

- Intended statement: determine whether `C_1785` admits a `(1785,224,28)` difference set.
- The solve-stage narrative also targeted that exact theorem and did not drift to a different parameter set or family.
- The strongest honest verified output after audit is only a quotient slice:
  under a source-justified `w = 17`, `t = 2` multiplier premise, any hypothetical cyclic `(1785,224,28)` difference set has mod-`17` contraction exactly `(0,14,14)`.
- So the packet is faithful in target selection, but not faithful in advertised closure: the verified content is a nearby structural lemma, not the intended existence / nonexistence theorem.

## verify_proof
First incorrect load-bearing step: the opening global multiplier normalization.

- The record claims:
  `Since 2 | n = 196` and `gcd(2,1785)=1`, the standard cyclic prime-multiplier theorem gives `2D = D + s`, hence after translation `2D = D`.`
- In the bounded source record, the relevant cited tool is Baumert-Gordon Theorem `3.2`, which gives a `w`-multiplier `t` only when each prime divisor of `n` has some power congruent to `t (mod w)`.
- That criterion does support `t = 2` modulo `17`: a power of `2` is trivially `2 mod 17`, and `7^10 ≡ 2 (mod 17)`.
- It does not support `t = 2` modulo `3`, modulo `51`, or modulo `1785`: powers of `7` are never congruent to `2` modulo those moduli.
- Therefore the current packet does not justify the global statement `2D = D`, nor the later claim that the mod-`3` and mod-`51` contraction coefficients are constant on multiplication-by-`2` orbits.
- Once that premise is removed, the derived mod-`3` contraction `(84,70,70)` and the final `8 | 84` contradiction are not established.

What survives:

- the contracted equations themselves;
- the exact mod-`17` orbit decomposition for multiplication by `2`;
- the unique mod-`17` solution `(0,14,14)`.

What fails:

- the theorem-level nonexistence conclusion for `C_1785`.

## verify_adversarial
Independent checks support the arithmetic slice, but not the advertised theorem.

- I reran the orbit calculations for multiplication by `2`. They confirm orbit sizes `[1,8,8]` on `C_17`, `[1,2]` on `C_3`, and two size-`8` orbits on the nonzero `0 mod 3` fiber inside `C_51`.
- I reran the contracted-equation solves. They confirm:
  - unique mod-`17` solution `(a,b,c) = (0,14,14)`;
  - unique mod-`3` orbit-constant solution `(u,v) = (84,70)` if one assumes `2`-orbit constancy there.
- These computations do not repair the proof, because the missing point is not arithmetic; it is the unsupported transfer of the `t = 2` multiplier premise from the valid `w = 17` setting to the invalid `w = 3`, `51`, and `1785` settings.
- No separate checker, witness, or counterexample object exists to attack beyond these exact orbit and equation checks.

## verify_theorem_worthiness
- Exactness: the intended exact theorem is not verified. The surviving claim is a structural mod-`17` theorem slice only.
- Novelty: bounded prior-art checking did not show rediscovery of the exact row.
- Reproducibility: high for the surviving slice. The mod-`17` contraction argument is short, exact, and reproducible.
- Lean readiness: `false`. Lean would only formalize the wrong object first; the remaining blocker is mathematical closure, not formalization labor.
- Paper leverage: low in current audited form. The surviving slice is useful, but it is not yet a title theorem for a micro-paper.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No, not in its currently verified form.
- What percentage of the paper would one solve already provide? About `25%` to `30%`.
- What title theorem is actually visible? At best:
  `Any hypothetical cyclic (1785,224,28) difference set has mod-17 contraction exactly (0,14,14), so the 0 mod 17 fiber is empty.`
- What part of the argument scales? The source-backed mod-`17` contracted-multiplier slice and the exact quotient-equation solve.
- What part clearly does not? The unsupported upgrade to global / mod-`3` / mod-`51` `2`-invariance and the final mixed-quotient divisibility contradiction.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? `NONE`.

The honest packet does not currently meet the micro-paper lane. It preserves one rigid helper lemma, not a row-closing theorem.

## verify_verdict
- `verify_verdict = "NOT_VERIFIED"`
- `classification = "VARIANT"`
- `confidence = "high"`
- strongest honest claim:
  under the valid Baumert-Gordon Theorem `3.2` multiplier premise at `w = 17`, any hypothetical cyclic `(1785,224,28)` difference set has mod-`17` contraction exactly `(0,14,14)`, hence the `0 mod 17` fiber is empty.
- `publication_status = "NONE"`
- `next_action = "preserve the verified mod-17 slice, discard the global/mod-3/mod-51 2-invariance step as theorem evidence, and revisit the row only with a source-justified multiplier or a different exact obstruction"`

## minimal_repair_if_any
Tiny conservative repair available:

- Keep the verified mod-`17` theorem slice only.
- Remove theorem-level reliance on `2D = D` in `C_1785` and on any downstream claim that mod-`3` or mod-`51` contractions are constant on multiplication-by-`2` orbits.
- Do not send the current packet to Lean, because Lean would formalize a helper slice rather than seal a publication-ready theorem.

What seems row-specific:

- the exact mod-`17` profile `(0,14,14)`;
- the final contradiction that `84` fails an `8`-divisibility test.

## proof_template_reuse
Reusable proof template.

1. Normalize by a prime multiplier `p` dividing `n`.
2. Solve one prime quotient exactly using only sum and square-sum.
3. Convert that exact quotient profile into a structural statement such as an empty fiber or a uniform nonzero profile.
4. Pass to a mixed quotient where `p`-orbit sizes force a divisibility condition on one residue fiber.
5. Compare that divisibility condition with a second exact small-prime contraction.

This template should be checked against nearby rows where:

- `p=2` or another very small prime divides `n`,
- one prime divisor of `v` gives a long nonzero orbit under `p`,
- another divisor of `v` gives a small contraction with a rigid zero-class count.

## candidate_theorem_slice
Candidate theorem slice.

Let `D` be a hypothetical cyclic `(1785,224,28)` difference set. After translation one may assume `2D = D`. Then:

- the contracted image of `D` in `C_17` is exactly `(0,14,14)` on the three `2`-orbits;
- the contracted image of `D` in `C_3` is exactly `(84,70,70)`;
- the classes of `C_51` that are `0 mod 17` are all empty, so the `0 mod 3` fiber of `C_51` is a union of two size-`8` `2`-orbits;
- hence the `0 mod 3` coefficient must lie in `8Z`, contradicting the exact value `84`.

This is already a clean theorem slice, not just a loose heuristic.

## smallest_param_shift_to_test
The most informative next parameter shifts are rows where the same `p=2` normalization is available and one prime factor of `v` gives a nonzero orbit of size `8` or another large power of `2`.

Concretely, the smallest useful shifts are not tiny perturbations of `(1785,224,28)` but neighboring residual cyclic rows with:

- `2 | (k-λ)`,
- a prime divisor `q | v` for which `ord_q(2)` is large and odd fibers can vanish, and
- a second small quotient that produces a rigid zero-class count.

## why_this_is_or_is_not_publishable
If the solve-stage proof survives verify, this is publishable in the intended micro-paper lane.

Why it is paper-shaped:

- the statement is an exact source-listed survivor row;
- the title theorem is one sentence long and already sharp;
- the proof is short, arithmetic, and self-contained once the multiplier citation is stated;
- the remaining writeup burden is light.

Why caution is still needed:

- solve stage is not a rediscovery check;
- the multiplier normalization must be cited exactly in verify;
- the quotient-orbit bookkeeping on `C_51` should be checked line by line.

So the current result is not too thin for the micro-paper lane; it already looks like a near-paper theorem packet pending verification.

## paper_shape_support
Paper-shape support now present:

- exact title theorem:
  `The cyclic group C_1785 does not admit a (1785,224,28) difference set.`
- one decisive structural lemma:
  after translation, any hypothetical set is `2`-invariant and has mod-`17` contraction `(0,14,14)`
- one short contradiction proposition:
  the induced `C_51` orbit structure forces the mod-`3` zero-class coefficient to be divisible by `8`
- one immediate corollary / remark:
  no survivor row with this exact quotient geometry can persist past the mixed `C_17` and `C_3` contraction stage

This is consistent with the packet's `single_solve_to_paper_fraction = 0.8`.

## boundary_remark
Boundary remark.

The argument does not rely on a broad theorem about all rows with `n = 196`; it uses the specific interaction of:

- the exact multiplier normalization by `2`,
- the order `8` of `2 mod 17`,
- and the exact mod-`3` zero-class count `84`.

So the proof is simultaneously family-relevant and row-specific. That is good micro-paper territory: it closes one exact source-exposed survivor without pretending to settle a larger program.

One natural remark falling out is that the obstruction is already visible before any heavy contraction modulo `255` or `357`; the smaller mixed quotient `51 = 3 * 17` is enough once the prime quotient `17` is solved exactly.

## likely_failure_points
The main places verify should probe are:

1. the exact statement of the cyclic prime-multiplier theorem and the translation step from `2D = D + s` to exact `2D = D`
2. the claim that on `C_17`, multiplication by `2` has two nonzero size-`8` orbits
3. the claim that the zero mod-`17` coefficient being `0` forces each of the three `0 mod 17` classes in `C_51` to be individually `0`
4. the claim that the `16` classes in `C_51` with `0 mod 3` and nonzero mod `17` split into two size-`8` `2`-orbits
5. the contracted square-sum arithmetic on `C_17` and `C_3`

If any of those fails, the present proof collapses; I do not currently see a second independent contradiction of equal strength.

## what_verify_should_check
Verify should check exactly:

1. the source-correct multiplier citation for the prime `2` in cyclic difference sets with `2 | n` and `gcd(2,v)=1`
2. the contracted equation `sum b_i^2 = n + λ(v/w)` in the quotient conventions used here
3. the mod-`17` calculation yielding the unique profile `(0,14,14)`
4. the mod-`3` calculation yielding the unique profile `(84,70,70)`
5. the `C_51` orbit count:
   - two size-`8` orbits in the `0 mod 3`, nonzero mod-`17` fiber
   - therefore zero-class coefficient in `8Z`
6. bounded prior-art checking for whether this exact `(1785,224,28)` row has already been disposed of elsewhere

If those checks pass, the solve verdict should be treated as a strong exact nonexistence candidate and likely micro-paper ready after verification.

## publication_prior_art_audit
Bounded publication-stage prior-art audit completed on `2026-04-15`.

- Exact statement searches for `"(1785,224,28)" difference set` and `"1785 224 28 cyclic difference set"` surfaced Baumert-Gordon `2004` as the direct row anchor and did not surface a later paper, theorem page, or database entry explicitly settling the exact cyclic row.
- Alternate-notation search for `"C_1785" difference set 224 28` likewise surfaced no later exact settlement.
- Canonical-source check: Baumert-Gordon `2004` Table `2` still lists `(1785,224,28)` as a possible cyclic case with `gcd(v,n) > 1`.
- Canonical-source theorem / proposition / example / corollary / observation / sufficient-condition check: Section `3.2` gives Theorems `3.1` and `3.2` as general contracted-equation and `w`-multiplier tools, but the paper does not include a local statement already disposing of `(1785,224,28)`.
- Outside-source status check: Gordon's current Difference Sets database describes itself as a status surface for possible parameters, known examples, and nonexistence results. Site-specific tuple searches plus the bounded web pass did not surface a row-specific entry or later exact settlement for `(1785,224,28)`.
- One bounded follow-up check: Gordon's `2022` paper `On difference sets with small λ` cites both Baumert-Gordon `2004` and the database, but the bounded exact-row / follow-up pass surfaced no treatment of the `(1785,224,28)` row.

Conservative prior-art verdict: no rediscovery was established in the bounded audit, but no publication-strength novelty certificate was found either. The honest conclusion is only that this narrow pass did not surface a later exact settlement.

## publication_statement_faithfulness
The packet stays faithful to the intended exact row, but not to the advertised closure.

- Intended statement: determine whether `C_1785` admits a `(1785,224,28)` difference set.
- Strongest audited claim: under the valid Baumert-Gordon Theorem `3.2` premise with `w = 17` and `t = 2`, any hypothetical cyclic `(1785,224,28)` difference set has mod-`17` contraction exactly `(0,14,14)`, so the `0 mod 17` fiber is empty.
- The dropped step is the unsupported upgrade from a valid `17`-multiplier to global / mod-`3` / mod-`51` `2`-invariance.
- So the packet remains faithful in target selection but not in theorem delivery: the surviving audited content is an auxiliary structural lemma, not the intended row-closing theorem.

## publication_theorem_worthiness
- Is the strongest honest claim stronger than `here is an example`? Yes. It is a rigid necessary-condition proposition, not an example.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a theorem slice only.
- Is the proof structural or merely instance-specific? The surviving argument is structural on the `mod 17` quotient, but still tightly tied to this one row and too thin to stand as a title theorem.
- Would this survive a referee asking `what is the theorem?` Not in current form. The best answer would be a helper proposition about the `mod 17` contraction of a hypothetical set, not a row-closing theorem or counterexample theorem.
- Is the claim still too dependent on hand-picked small cases? Yes. Once the invalid global multiplier step is removed, the packet retains only one quotient slice and no verified mechanism that closes the exact row.

The honest theorem-worthiness verdict is therefore `weak`: the surviving claim is mathematically clean, but publication-weak and below the one-shot title-theorem threshold.

## publication_publishability
- Would the current boundedly verified result already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `25%` to `30%`, not the pre-audit `80%`.
- Is the remaining gap genuinely small? No. The candidate looked attractive before audit because the solve record relied on a load-bearing multiplier step that does not survive source checking.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Preserve the mod-`17` slice and move the row aside unless a new source-justified exact obstruction appears.
- Would Lean directly seal the packet? No. Lean would only formalize an auxiliary slice; here it would be optional archival polish, not the missing publication step.

## publication_packet_audit
Packet judgment after bounded publication audit:

- `publication_status = NONE`
- `publication_packet_quality = weak`
- the strongest honest claim is a preserved helper proposition, not a HUMAN_READY micro-paper packet
- `proof_artifacts_preserved = true` because the mod-`17` slice is exact and worth keeping
- no feeder-ladder expansion is justified from this packet
- the packet should not go to the Lean queue and should not block fresh discovery work

## micro_paper_audit
This packet fails the strict micro-paper lane in its current audited form.

- The result is stronger than a mere example, but weaker than a publishable theorem slice.
- One solve no longer supplies most of a paper; it supplies one rigid lemma plus a failed closure attempt.
- There is no credible current title theorem.
- The surviving claim would not carry the note through referee scrutiny without a new exact obstruction or construction.
- Micro-paper leverage after audit is low enough that the row should be cooled rather than expanded.

## strongest_honest_claim
Under the valid Baumert-Gordon Theorem `3.2` multiplier premise at `w = 17` with `t = 2`, any hypothetical cyclic `(1785,224,28)` difference set has contracted mod-`17` coefficient pattern `(0,14,14)` on the three `2`-orbits, so its `0 mod 17` fiber is empty.

## paper_title_hint
No paper-ready title is justified. At most: `A mod-17 contraction constraint for hypothetical cyclic (1785,224,28) difference sets`.

## next_action
Preserve the verified mod-`17` slice as a helper artifact, mark the packet `publication_status = NONE`, and move this row aside unless a new source-justified multiplier or different exact obstruction closes the full `(1785,224,28)` case without expanding into a broader theorem program.
