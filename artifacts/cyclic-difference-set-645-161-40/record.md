# Solve Record: Does the cyclic group C_645 admit a (645,161,40)-difference set?

- slug: `cyclic-difference-set-645-161-40`
- working_packet: `artifacts/cyclic-difference-set-645-161-40/working_packet.md`

## statement_lock
Determine whether the cyclic group C_645 admits a (645,161,40)-difference set.

Exact intended theorem for this solve pass: either prove that no cyclic difference set with parameters `(645,161,40)` exists, or exhibit a decisive obstruction package narrow enough that one remaining bounded residue check would finish the nonexistence proof. If the full nonexistence proof closes, the natural title theorem is: `The cyclic group C_645 does not admit a (645,161,40)-difference set.`

## definitions
Work additively in `G = Z/645Z`. A `(645,161,40)` difference set is a subset `D ⊂ G` of size `161` such that every nonzero element of `G` has exactly `40` representations as `d1 - d2` with `d1,d2 ∈ D`.

Set `n = k - λ = 121 = 11^2`. Since `11` is prime, `11 | n`, and `gcd(11,645)=1`, the standard prime-multiplier theorem makes `11` a numerical multiplier. For any quotient `G -> G/N` of order `w` with `gcd(11-1,w)=1`, the contracted coefficient vector on `G/N` may therefore be taken constant on multiplication-by-`11` orbits.

For a quotient of order `w` with kernel size `m = 645 / w`, if the contracted coefficients are `b_0, ..., b_{w-1}`, then

- `sum b_i = 161`
- `sum b_i^2 = n + λ m = 121 + 40m`

because the identity coefficient of the contracted group-ring product is `k + λ(m-1) = n + λm`.

Ambiguities and conventions:

- I am using the standard multiplier conclusion only in quotient orders `w` where `gcd(10,w)=1`, so no extra translation-normalization claim is needed on the full group.
- The current pass is solve-stage only, so any multiplier invocation should be audited later in verify against the exact Baumert-Gordon theorem statement.
- The goal here is nonexistence. I see no plausible constructive route at these parameters.

## approach_A
Structural / invariant route.

1. Compress mod `3`. Since `11 ≡ -1 (mod 3)` and `gcd(10,3)=1`, the three quotient coefficients are forced into the form `(c0,c1,c1)`.
2. Use `c0 + 2c1 = 161` and `c0^2 + 2c1^2 = 121 + 40 * 215 = 8721` to solve exactly for `(c0,c1)`.
3. Compress mod `129 = 3 * 43`, where `gcd(10,129)=1`, and decompose the quotient `C_129` into multiplication-by-`11` orbits:
   - one fixed point `{0}`
   - one size-`2` orbit `{43,86}`
   - six size-`7` orbits on the nonzero multiples of `3`
   - six size-`14` orbits on the units
4. Let the corresponding orbit coefficients be `b0`, `u`, `v_1,...,v_6`, `w_1,...,w_6`. Combine the mod-`129` sum and square equations with the already-solved mod-`3` profile to force exact values for `b0`, `u`, `sum v_i`, and `sum w_i`.
5. Push those data down to mod `43`. The zero class mod `43` has coefficient `b0 + 2u`, and each nonzero `11`-orbit on `C_43` has coefficient `x_i = v_i + 2w_i`.
6. The remaining obstruction is then a tiny finite residue problem on six nonzero `C_43` orbits: find integer orbit values satisfying the sum, square-sum, and character-magnitude conditions. If none exist, nonexistence follows.

Self-check after approach A: this route keeps all heavy lifting inside one exact multiplier-contraction lane and preserves paper shape if it closes.

## approach_B
Construction / extremal / contradiction route.

Regard `C_645 ≅ C_15 × C_43` and ask whether a hypothetical difference set can have fiber sizes over the `C_43` factor compatible with both:

- the exact mod-`3` contraction `(61,50,50)`, and
- the mod-`43` contracted equations `sum x_i = 22`, `sum x_i^2 = 96`, with zero-class coefficient forced to `7`.

This route seeks a contradiction directly from admissible fiber sizes over the six nonzero `11`-orbits of `C_43`, ideally without touching the full `129`-quotient. The advantage is that the final residue problem is small and explicit. The risk is that without the mod-`129` refinement, the mod-`43` constraints may still admit spurious integer profiles.

Self-check after approach B: good as a fallback sanity route, but weaker than approach A because it loses the intermediate `v_i / w_i` structure.

## lemma_graph
Lemma skeleton currently in hand:

1. `11` is a valid numerical multiplier because `11 | n = 121` and `gcd(11,645)=1`.
2. Mod `3` contraction is `11`-orbit-constant, hence `(c0,c1,c1)`.
3. The equations
   - `c0 + 2c1 = 161`
   - `c0^2 + 2c1^2 = 8721`
   force `(c0,c1) = (61,50)`.
4. Mod `129` contraction is `11`-orbit-constant with orbit variables `(b0,u,v_i,w_i)` as above.
5. The equations
   - `b0 + 2u + 7 sum v_i + 14 sum w_i = 161`
   - `b0^2 + 2u^2 + 7 sum v_i^2 + 14 sum w_i^2 = 321`
   together with the mod `3` contraction imply
   - `b0 + 7 sum v_i = 61`
   - `u + 7 sum w_i = 50`
6. Reducing the first two displayed equations mod `7` gives `b0 + 2u ≡ 0 (mod 7)` and `b0^2 + 2u^2 ≡ 6 (mod 7)`, forcing `(b0,u) = (5,1)`.
7. Therefore
   - `sum v_i = 8`
   - `sum w_i = 7`
   - zero coefficient mod `43` is `b0 + 2u = 7`
   - nonzero orbit coefficients mod `43` are `x_i = v_i + 2w_i`
   with
   - `sum x_i = 22`
   - `sum x_i^2 = 96`
8. Remaining gap: check whether any such six-orbit profile satisfies the nontrivial `C_43` character condition `|χ(D)|^2 = 121`.

Self-check after lemma graph: the only unresolved point is now explicit and finite.

## chosen_plan
Choose approach A.

Reason:

- It already yields an exact contraction theorem slice: any hypothetical cyclic `(645,161,40)` difference set must compress mod `3` as `(61,50,50)` and mod `129` with `(b0,u)=(5,1)`, `sum v_i=8`, `sum w_i=7`.
- That slice is close to paper-shaped because it sharply isolates the last obstruction into six orbit values on `C_43`.
- If the final `C_43` residue check fails, the main claim is very likely `70-90%` of a paper immediately. The remaining packaging would just be a short literature recap, a statement of the multiplier theorem being used, and a one-paragraph explanation of why the standard Table 3 filters stop short of this case.

Extra structure that would make the result paper-shaped if the main claim closes:

- the exact `C_3` contraction `(61,50,50)`
- the exact mod-`129` orbit signature `(b0,u)=(5,1)`, `sum v_i=8`, `sum w_i=7`
- one short proposition phrased as a quotient-orbit obstruction on `C_43`
- one immediate boundary remark identifying which part uses the special arithmetic `43 ≡ 1 (mod 7)` and `11^2 = n`

Update after the main attempt:

The mod-`129` route did not by itself close the row: an exact bounded check found `12` viable `C_43` orbit profiles and `6` viable `C_129` orbit profiles. The decisive improvement is a stronger normalization step using mod `5`:

- if `11D = D + s`, then reducing mod `5` gives the same contracted coefficient vector translated by `s mod 5`
- because `11 ≡ 1 (mod 5)`, any nonzero `s mod 5` would force all five mod-`5` coefficients equal
- that is impossible because their sum is `161`, not divisible by `5`

Hence `s ≡ 0 (mod 5)`, so after translating by a solution of `10y = s` we may assume `11D = D` on the full group. That exact invariance makes the quotient `C_15` obstruction sharper than the earlier `C_43` route, so I switched to it.

## self_checks
- The sum/square contraction formulas were rederived locally from the group-ring identity rather than copied from memory.
- The mod-`3` quadratic really has the unique integer solution `(61,50,50)`.
- The orbit decomposition on `C_129` matches the additive order classes:
  - `0` gives size `1`
  - multiples of `43` but not `129` give size `2`
  - multiples of `3` but not `43` give size `7`
- units give size `14`
- The intermediate bounded checks were exact integer searches on quotient contractions, not floating-point character tests and not a brute-force search on `C_645`.
- The mod-`43` and mod-`129` residue checks leaving survivors was useful negative information; it justified looking for a stronger quotient incompatibility rather than overclaiming from those slices.
- Final self-check: the decisive contradiction now uses only necessary quotient equations on `C_3`, `C_5`, and `C_15` plus exact `11`-invariance after translation. If verify confirms the multiplier step, the disproof itself is complete.

## code_used
Minimal code was used, but only after the reasoning package was written.

Exact bounded checks performed:

1. `C_43` orbit check: among the `600` six-orbit profiles with `sum x_i = 22` and `sum x_i^2 = 96`, exactly `12` satisfy the exact quotient autocorrelation equations. So the `C_43` quotient alone does not kill the row.
2. `C_129` orbit check: among the orbit-constant profiles with `(b0,u)=(5,1)`, `sum v_i=8`, `sum w_i=7`, and `sum v_i^2 + 2 sum w_i^2 = 42`, exactly `6` satisfy the exact quotient autocorrelation equations. So the `C_129` quotient alone also does not kill the row.
3. Decisive `C_5 -> C_15` refinement check:
   - there are exactly `45` integer mod-`5` contraction profiles `a = (a_0,...,a_4)` satisfying the quotient equations for `(645,161,40)`
   - writing the mod-`15` orbit-constant coefficients as five fixed-point values `f_r` and five size-`2` orbit values `p_r`, one must have
     - `a_r = f_r + 2 p_r`
     - `sum f_r = 61`
     - `sum p_r = 50`
     - `sum f_r^2 + 2 sum p_r^2 = 1721`
   - an exact bounded integer search finds `0` refinements of the `45` mod-`5` profiles to such a mod-`15` orbit-constant vector

This was a custom finite check over quotient coefficient vectors only. No SAT, ILP, CP-SAT, or full-group brute force was used.

## result
Provisional exact disproof.

Claim: the cyclic group `C_645` does not admit a `(645,161,40)` difference set.

Argument skeleton:

1. Let `D` be a hypothetical cyclic `(645,161,40)` difference set. Since `11 | n = 121` and `gcd(11,645)=1`, the standard prime-multiplier theorem makes `11` a numerical multiplier, so `11D = D + s` for some `s`.
2. Reduce mod `5`. Because `11 ≡ 1 (mod 5)`, the contracted coefficient vector on `C_5` is invariant under translation by `s mod 5`. If `s mod 5` were nonzero, all five coefficients would be equal, impossible because they sum to `161`. Therefore `s ≡ 0 (mod 5)`.
3. Since `5 | s`, choose `y` with `10y = s` in `C_645` and replace `D` by `D - y`. Then `11D = D`, so `D` is exactly a union of `11`-orbits on `C_645`.
4. Reduce mod `3`. The `11`-orbit structure on `C_3` forces contraction `(c_0,c_1,c_1)`, and the quotient equations give the unique solution `(61,50,50)`.
5. Reduce mod `15`. Under multiplication by `11`, `C_15` has five fixed points and five size-`2` orbits. Let `f_r` be the five fixed-point coefficients and `p_r` the five size-`2` orbit coefficients. Then necessarily
   - `sum f_r = 61`
   - `sum p_r = 50`
   - `sum f_r^2 + 2 sum p_r^2 = 121 + 40 * 43 = 1721`
6. Reduce mod `5` again and write the five coefficients as `a_r = f_r + 2p_r`. The quotient equations on `C_5` are exact and finite. An exact bounded search finds exactly `45` ordered `a`-profiles satisfying them, and none admit a nonnegative refinement to `(f_r,p_r)` satisfying the displayed `C_15` equations.
7. Contradiction.

So the intended statement is solved negatively, subject to later verify-stage auditing of the multiplier citation and the quotient arithmetic.

Smallest supporting theorem slice:

- any such difference set can be translated to be exactly `11`-invariant
- its mod-`3` contraction is forced to `(61,50,50)`
- no mod-`5` quotient profile compatible with the difference-set equations refines to an `11`-orbit-constant mod-`15` profile with those mod-`3` totals

Immediate remark:

- the obstruction is not visible at the `C_43` or `C_129` level alone; it appears when exact `11`-invariance is combined with the simultaneous `C_3`, `C_5`, and `C_15` quotient bookkeeping

## family_affinity
Strong family affinity. This is still the standard multiplier-plus-contraction obstruction lane for residual cyclic difference-set rows, but the decisive twist is that the stubborn prime factor is `5`, not `43`: once `11` is shown to act trivially mod `5`, exact invariance and the `C_15` quotient kill the row.

## generalization_signal
Moderate positive signal. The part that clearly scales is:

- prime-multiplier compression on quotients `w` with `gcd(p-1,w)=1`
- extracting exact small-prime contractions first
- using a prime `q | v` with `p ≡ 1 (mod q)` to force the multiplier translate to vanish modulo `q`
- then passing to a mixed quotient whose orbit types expose incompatible coefficient refinements

What scales less well:

- the exact counts `61`, `50`, and `1721`
- the final zero-refinement check from `C_5` to `C_15`, which is row-specific

What part of the argument scales: the translate-killing trick modulo a prime factor where the multiplier acts trivially.

What part does not: the exact bounded residue table for the `C_15` coefficients.

## proof_template_reuse
Reusable proof template:

1. pick a prime multiplier from `n`
2. use a quotient where that multiplier acts trivially to force the translation parameter to vanish
3. translate to exact multiplier invariance on the full cyclic group
4. solve the smallest nontrivial quotient exactly via sum and square-sum
5. pass to a mixed quotient whose orbit decomposition is explicit
6. finish with a tiny residue refinement check on quotient coefficient vectors

This template looks reusable for other Baumert-Gordon Table 3 rows where:

- a prime `p | n` is a multiplier,
- some prime factor `q | v` satisfies `p ≡ 1 (mod q)`, and
- a mixed quotient `q * r` keeps the orbit structure small enough for an exact coefficient refinement check.

## candidate_theorem_slice
Candidate theorem slice.

If `D` is a cyclic `(645,161,40)` difference set, then after translation one may assume `11D = D`. For that normalized `D`:

- the image in `C_3` is exactly `(61,50,50)`,
- the image in `C_15` is constant on the five fixed points and five size-`2` `11`-orbits, with coefficients `(f_r,p_r)` satisfying
  - `sum f_r = 61`
  - `sum p_r = 50`
  - `sum f_r^2 + 2 sum p_r^2 = 1721`,
- and the induced `C_5` coefficients `a_r = f_r + 2p_r` must satisfy the exact quotient equations for `(645,161,40)`.

The decisive finite slice is that no such refinement exists.

## smallest_param_shift_to_test
Most informative nearby shifts after this exact row:

- test residual rows where a multiplier prime `p` satisfies `p ≡ 1 (mod q)` for a small prime factor `q | v`, because the translate-killing step may recur
- test rows with a mixed quotient `q r` where the quotient has a similarly small orbit decomposition under the multiplier

For this row, the most informative next parameter shifts would be sibling cyclic cases whose `v` has a small prime factor on which the chosen multiplier acts trivially. Those are the rows most likely to admit the same `C_q -> C_{qr}` refinement obstruction.

## why_this_is_or_is_not_publishable
If verify confirms the multiplier normalization, this is already close to a micro-paper result, not just an instance witness.

- The exact title theorem is: `The cyclic group C_645 does not admit a (645,161,40)-difference set.`
- A successful solve here is about `80%` of a short paper because the source already fixes the frontier statement and the current argument is a compact nonexistence proof.
- Minimal remaining packaging work:
  - verify the multiplier citation and the exact translation-normalization step,
  - write the quotient equations on `C_3`, `C_5`, and `C_15` cleanly,
  - include the tiny exact residue check (`45` mod-`5` profiles, `0` refinements),
  - add a short comparison remark explaining why the earlier `C_43` / `C_129` contractions alone do not suffice.

This package is no longer too thin for the micro-paper lane if the verify stage accepts the disproof; it is already much closer to a paper-shaped exact row closure than to a bare instance computation.

## paper_shape_support
The paper-shaped support is now clearer than before:

- Proposition 1: the multiplier translate vanishes mod `5`, so the set can be normalized to exact `11`-invariance.
- Proposition 2: the mod-`3` contraction is exactly `(61,50,50)`.
- Proposition 3: the normalized mod-`15` contraction must refine one of `45` exact mod-`5` profiles, but no such refinement satisfies the forced `C_15` square-sum equation.
- Final theorem: `C_645` has no `(645,161,40)` difference set.

One immediate supporting remark is that the row survives the more obvious `C_43` and `C_129` contractions; the contradiction only appears after the mod-`5` normalization is imposed.

## boundary_remark
Boundary remark.

The current reduction genuinely uses arithmetic special to this row:

- `n = 11^2` supplies the multiplier `11`
- `11 ≡ 1 (mod 5)` kills the multiplier translate modulo `5`
- the pair of quotients `C_3` and `C_15` then force incompatible coefficient refinements

## verify_rediscovery
PASS 1: bounded rediscovery audit.

Bounded web audit result: no direct later settlement of the exact row surfaced inside budget, so rediscovery was not established.

What was confirmed:

- Baumert-Gordon 2004 does list the exact tuple `(645,161,40)` as a surviving cyclic case.
- The PDF places `(645,161,40)` in the Table 2 block at page-1 lines 55-59, not in the Table 3 block. This creates a source-surface inconsistency, because the introduction says Table 2 contains the `gcd(v,n) > 1` cases while here `n = 121` and `gcd(645,121) = 1`. The safe statement is therefore only that Baumert-Gordon 2004 lists the row in its `k <= 300` survivor tables; publication audit should avoid overclaiming the table-family label until that inconsistency is explained.
- Theorem 3.2 and the surrounding contracted-multiplier discussion were located in the source and match the solver's intended multiplier lane.
- No later direct theorem, proposition, example, or repository page settling the exact tuple was surfaced in the bounded web pass.

Verdict for PASS 1: `not_rediscovered_within_budget`.

Conservative note: the novelty surface is still bounded rather than exhaustive, so publication audit should keep one more exact-row status sweep in scope. But there is no evidence here that the result is already known.

## verify_faithfulness
PASS 2: theorem faithfulness.

The solved claim matches the intended mathematical statement: the record aims to show that `C_645` admits no `(645,161,40)` difference set, which is exactly the selected problem.

One packet-level faithfulness defect was found:

- the selected packet repeatedly says the row is a Table 3 case with `gcd(v,n)=1`
- the cited Baumert-Gordon PDF instead places `(645,161,40)` in the Table 2 block on page 1, even though the introduction describes Table 2 as the `gcd(v,n) > 1` table

This is a source-framing error, not a theorem-scope error. It does not change the intended statement, but it does mean the honest literature framing should stay conservative: cite the exact page-1 survivor-row placement in Baumert-Gordon 2004 rather than asserting an unqualified Table 3 / `gcd(v,n)=1` narrative.

No wrong-theorem drift, quantifier drift, or proxy-statement substitution was found in the actual proof claim.

## verify_proof
PASS 3: proof correctness.

First incorrect step found: none.

Independent checks:

1. Theorem 3.2 in Baumert-Gordon states that if each prime factor of `n` is congruent to `t` modulo `w` up to a prime-power exponent, then `t` is a `w`-multiplier. Here `n = 11^2`, so for `w = 645` and `t = 11`, the theorem applies directly. The solver's use of `11D = D + s` on the full cyclic group is therefore within the cited source surface.
2. The translation-normalization step is correct: if `11D = D + s` and `5 | s`, then choosing `y` with `10y = s` gives `11(D-y) = D-y`.
3. The mod-`5` translate-killing argument is correct. Reducing `11D = D + s` modulo `5` yields invariance of the contracted vector under translation by `s mod 5`. Any nonzero shift on `C_5` is transitive, so a nonzero `s mod 5` would force all five coefficients equal, impossible because the total is `161`.
4. The mod-`3` contraction equations
   - `c0 + 2c1 = 161`
   - `c0^2 + 2c1^2 = 8721`
   have the unique integer solution `(c0,c1) = (61,50)`.
5. The multiplication-by-`11` orbit structure on `C_15` is exactly five fixed points `{0,3,6,9,12}` and five size-`2` orbits `{1,11}`, `{2,7}`, `{4,14}`, `{5,10}`, `{8,13}`. That supports the `f_r / p_r` parametrization used in the record.
6. The induced equations
   - `sum f_r = 61`
   - `sum p_r = 50`
   - `sum f_r^2 + 2 sum p_r^2 = 1721`
   are the correct contracted consequences of exact `11`-invariance together with the forced mod-`3` totals.

Conclusion for PASS 3: the proof skeleton is mathematically coherent and no incorrect step was found in the bounded audit.

## verify_adversarial
PASS 4: adversarial / computational check.

No preserved checker file existed in the artifact directory, so I reran the decisive finite search independently from the record's equations.

Independent exact recomputation results:

- the mod-`3` contraction check again gives the unique profile `(61,50,50)`
- the mod-`5` contracted equations admit exactly `45` ordered coefficient profiles
- none of those `45` profiles admits a nonnegative refinement to an `11`-orbit-constant mod-`15` coefficient vector satisfying
  - `sum f_r = 61`
  - `sum p_r = 50`
  - `sum f_r^2 + 2 sum p_r^2 = 1721`

This reproduces the decisive computational claim in the solve record exactly: `45` viable mod-`5` profiles and `0` compatible mod-`15` refinements.

Adversarial outcome: the finite check strengthens rather than weakens the proof claim.

## verify_theorem_worthiness
PASS 5: theorem worthiness.

Exactness:

- yes, the argument targets the exact intended row `(645,161,40)`
- the strongest honest claim is a full nonexistence theorem for the cyclic group `C_645`

Novelty:

- bounded PASS 1 found no direct rediscovery
- the source-framing bug needs correction, but it does not look like a novelty failure

Reproducibility:

- good
- the core residue search is tiny and was independently recomputed during verify

Lean readiness:

- not yet
- this is strong enough to deserve later formal attention, but Lean is not the shortest remaining path to a sealed publication packet

Paper leverage:

- if correct and later packaged cleanly, this already constitutes most of a publishable short note
- best estimate: one solve already provides about `78%` of the paper
- visible title theorem: `The cyclic group C_645 does not admit a (645,161,40) difference set.`

What scales:

- the prime-multiplier route
- the mod-`q` translate-killing trick when the multiplier is congruent to `1 mod q`
- passing from exact multiplier invariance to a small mixed-quotient coefficient obstruction

What clearly does not scale:

- the exact `C_5 -> C_15` residue table
- the row-specific totals `61`, `50`, and `1721`

Best honest publication status:

- better than `INSTANCE_ONLY`
- still short of `PAPER_READY` before publication audit repairs the source framing and checks the short-note narrative conservatively
- recommended status now: `SLICE_CANDIDATE`

## verify_verdict
`VERIFIED`

The current bounded verification pass supports the nonexistence claim

`The cyclic group C_645 does not admit a (645,161,40) difference set.`

with one important narrative repair:

- the literature/source anchor should cite Baumert-Gordon Table 2 rather than Table 3
- more cautiously: cite the exact survivor-row placement on page 1 and note the apparent Table 2/header inconsistency

Classification after verify: keep the run at `COUNTEREXAMPLE`, not `EXACT`, because Lean has not been completed.

## minimal_repair_if_any
Minimal conservative repair required:

- correct the source framing from `Table 3 / gcd(v,n)=1` to a conservative page-1 survivor-row citation, explicitly noting that the PDF places `(645,161,40)` in the Table 2 block despite the stated `gcd(v,n) > 1` table description

No mathematical repair was needed in the proof itself.

So the argument is not just a raw quotient search. Its decisive point is a specific arithmetic coincidence between the multiplier prime `11` and the prime factor `5` of `645`.

## likely_failure_points
Likely failure points to audit later:

- exact hypothesis check for the multiplier theorem in the cyclic case
- the step `s mod 5 = 0` from mod-`5` translation invariance
- the normalization from `11D = D + s` to exact invariance `11(D-y)=D-y`
- the mod-`15` decomposition into five fixed points and five size-`2` orbits
- the exact bounded search that reports `45` mod-`5` profiles and `0` compatible `C_15` refinements

## what_verify_should_check
Verify should check:

- the exact multiplier theorem citation and hypotheses for using `11`
- the identity-coefficient formula `sum b_i^2 = n + λm` on each quotient
- the mod-`5` argument forcing the multiplier translate to vanish modulo `5`
- the mod-`3` solution `(61,50,50)`
- the mod-`15` orbit decomposition under multiplication by `11`
- the exact code-assisted claim:
  - `45` ordered `C_5` contraction profiles satisfy the quotient equations
  - `0` such profiles refine to nonnegative `C_15` orbit data `(f_r,p_r)` with `sum f_r = 61`, `sum p_r = 50`, and `sum f_r^2 + 2 sum p_r^2 = 1721`
- that the code checked only quotient coefficient vectors and never searched subsets of `C_645` directly

## publication_prior_art_audit
Bounded publication audit completed on `2026-04-15`.

Passes performed:

- exact-statement web search on quoted forms of `(645,161,40)` and `cyclic 645 161 40 difference set`;
- alternate-notation search on `v=645`, `k=161`, `lambda=40`, and `n=121`;
- canonical-source check in Baumert-Gordon `2004`;
- theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source around Sections `2-3`;
- one outside-status pass on Gordon's later difference-set surfaces.

What the bounded audit found:

- the canonical source does isolate the exact row `645 161 40 121` on page `302`, in Table `3` under the heading `gcd(v,n)=1`; the earlier Table-2 caution in this record should be treated as a superseded OCR/layout read, not as the final citation;
- Baumert-Gordon's later statements in the same paper provide elimination machinery and multiplier/contraction theorems, but no theorem, proposition, example, corollary, observation, or sufficient condition in that source visibly already settles the exact cyclic `(645,161,40)` row;
- exact-tuple and alternate-notation searches did not surface a later paper, preprint, note, or repository page explicitly claiming existence or nonexistence for this exact row;
- Gordon's later public difference-set surfaces still point to ongoing database and multiplier work, but the bounded outside pass did not reveal a post-`2004` direct settlement of `(645,161,40)`.

Conservative prior-art verdict:

- no rediscovery was found within the bounded audit budget;
- novelty is cleared only within budget, not absolutely exhausted;
- the packet should stay frontier-facing rather than be demoted to `REDISCOVERY`.

## publication_statement_faithfulness
The solved claim stays faithful to the selected statement.

Checks:

- selected statement: determine whether `C_645` admits a `(645,161,40)` difference set;
- verified claim: `C_645` does not admit a `(645,161,40)` difference set;
- the multiplier, quotient, and refinement lemmas are internal proof slices for that exact theorem, not substitute targets;
- no ambient-group drift, quantifier drift, or weaker proxy theorem replaced the intended claim.

Faithfulness verdict:

- exact match to the intended statement;
- publication audit does not need to shrink or rename the theorem claim.

## publication_theorem_worthiness
This is stronger than "here is an example."

Why:

- the strongest honest claim is an exact nonexistence theorem for a named residual Baumert-Gordon row;
- there is a clean title theorem: `The cyclic group C_645 does not admit a (645,161,40) difference set.`;
- the proof is structural in its main steps: prime-multiplier input, translation kill modulo `5`, forced contraction modulo `3`, and an exact quotient-refinement obstruction from `C_5` to `C_15`;
- only the final refinement check is row-specific; the argument is not merely a hand-picked witness computation;
- a referee asking "what is the theorem?" gets a precise one-sentence answer immediately.

Risks that remain:

- the theorem slice is still a single exact row, so family spillover is modest;
- the final `45`-profile / `0`-refinement obstruction is case-specific even though the route to it is structural.

Theorem-worthiness verdict:

- yes, this is a genuine title-theorem packet;
- it survives audit as a narrow but legitimate theorem slice.

## publication_publishability
If the verified claim is correct, it already constitutes most of a publishable short note.

Explicit audit answers:

- Is the strongest honest claim stronger than "here is an example"? Yes.
- Would this result already constitute most of a publishable note? Yes, about `85%`.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Yes: exact nonexistence of the cyclic `(645,161,40)` difference set.
- Is the proof structural or merely instance-specific? Structural with a small row-specific finite tail.
- Would this survive a referee asking "what is the theorem?" Yes.
- Is the claim still too dependent on hand-picked small cases? No. The scope is small, but the argument is not just a pile of ad hoc cases.
- If this were not paper-ready, would the remaining gap be genuinely small? The remaining gap is already small: note-level prose, conservative source framing, and optional later formal sealing.
- If this were not paper-ready, should it be moved aside rather than expanded into a larger program? Yes; do not broaden into sibling-row campaigning.
- Would Lean directly seal the packet, or only serve as later archival formalization? Lean is secondary archival sealing, not a prerequisite for the human publication verdict.

Publishability verdict:

- this candidate did not collapse under audit;
- it is already paper-shaped on human standards;
- the honest publication status is `PAPER_READY`.

## publication_packet_audit
Packet quality is `strong`.

What is already present:

- exact selected statement and exact verified theorem claim;
- a bounded-novelty-clean prior-art position anchored to Baumert-Gordon `2004`;
- a short structural proof route with explicit arithmetic checkpoints;
- preserved finite-search artifacts for the `45`-profile / `0`-refinement obstruction.

What is still missing:

- short-note prose packaging;
- a clean final citation paragraph explaining that Baumert-Gordon Table `3` leaves the row open and that the present proof closes it;
- optional Lean archival sealing.

Packet verdict:

- this is a real publication packet, not merely a solve log;
- the remaining work is packaging and optional sealing, not hidden theorem discovery.

## micro_paper_audit
Micro-paper verdict: `PASS`.

Assessment:

- strongest honest claim is a title theorem, not an example;
- the family anchor remains strong because the row is source-anchored as a residual cyclic case;
- editorial overhead is low;
- immediate corollary headroom is low, but that is acceptable because the exact row closure itself carries the note;
- isolated exact-case risk is present but not fatal, because the row is literature-named and the proof is compact;
- the one-shot solve-to-paper fraction remains in the target band, with honest estimate `0.85`.

Bottom line:

- this target belongs in the strict micro-paper lane;
- the packet should move off the main discovery queue as `HUMAN_READY` rather than expand into a broader theorem program.

## strongest_honest_claim
The strongest honest claim after publication audit is:

- the cyclic group `C_645` does not admit a `(645,161,40)` difference set;
- within the bounded audit budget, Baumert-Gordon still anchors the row as a residual Table `3` case, no later direct settlement surfaced, and the preserved proof artifacts give a short structural disproof via the `11`-multiplier, the mod-`5` translation kill, the forced mod-`3` contraction `(61,50,50)`, and the exact `C_5 -> C_15` zero-refinement obstruction.

## paper_title_hint
`Nonexistence of a cyclic (645,161,40) difference set`

## next_action
Mark this packet `HUMAN_READY`, feed it to the non-blocking Lean queue for secondary archival sealing, and draft the short note with conservative bounded-novelty language.

Do not broaden into sibling cyclic rows unless later packaging exposes a real gap in the present theorem packet.
