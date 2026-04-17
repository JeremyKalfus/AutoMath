# Solve Record: The Cyclic (1925,260,35) Difference-Set Case

- slug: `cyclic-difference-set-1925-260-35`
- working_packet: `artifacts/cyclic-difference-set-1925-260-35/working_packet.md`

## statement_lock
Determine whether the cyclic group `C_1925` admits a `(1925,260,35)` difference set.

Exact intended title theorem if this pass is correct:
`The cyclic group C_1925 does not admit a (1925,260,35) difference set.`

Solve-stage stance: treat the current argument as a theorem-facing nonexistence proof candidate, not as Lean-complete exact closure.

## definitions
Work additively in `G = Z/1925Z`, with `1925 = 5^2 * 7 * 11`.

A `(1925,260,35)` difference set is a subset `D ⊂ G` of size `260` such that every nonzero element of `G` has exactly `35` representations as `d1 - d2` with `d1,d2 ∈ D`.

Set `n = k - λ = 260 - 35 = 225 = 3^2 * 5^2`.

Conventions used below:

- For a quotient of order `w`, let `m = 1925 / w` be the kernel size.
- If the contracted coefficient vector is `(b_i)`, then
  - `sum b_i = 260`
  - `sum b_i^2 = n + λ m = 225 + 35m`
  because the identity coefficient in the contracted group-ring product is `k + λ(m-1) = n + λm`.
- Since `3 | n` and `gcd(3,1925) = 1`, I use the standard prime-multiplier theorem to assert that `3` is a numerical multiplier, so `3D = D + s` for some `s ∈ G`.
- Because `gcd(3 - 1,1925) = gcd(2,1925) = 1`, there exists `y` with `2y = s`. Replacing `D` by `D - y` gives `3D = D`. After this translation normalization, `D` is exactly a union of multiplication-by-`3` orbits.

Ambiguity to preserve for verify:

- verify should confirm that the Baumert-Gordon multiplier surface supports this standard use of the prime `3 | n` on the full cyclic group.

## approach_A
Structural / invariant route.

1. Normalize to exact `3`-invariance.
2. Contract first to `C_5`, `C_25`, and `C_7`, where the `3`-orbit structure is tiny and the quotient equations can be solved exactly.
3. Use the exact `C_25` and `C_7` profiles as linear shadows of the `C_175` contraction, where `C_175` has only eight `3`-orbits:
   - one orbit of size `1`
   - one of size `4`
   - one of size `20`
   - one of size `6`
   - two of size `12`
   - two of size `60`
4. Because each `C_175` coefficient counts points in an `11`-element fiber, every orbit coefficient lies in `[0,11]`.
5. The projection equations to `C_25` and `C_7` then force exact orbit-sums on `C_175`.
6. The `C_175` square-sum equation contradicts those exact sums.

Self-check after approach A:
this route is theorem-shaped, uses only standard quotient identities, and avoids search-heavy machinery.

## approach_B
Construction / extremal / contradiction route.

Start from the exact `C_25` profile and try to refine it through `C_35` or `C_55`, looking for a contradiction from orbit refinements before reaching `C_175`.

Why this looked plausible:

- `C_25` is already very rigid, with the three coefficient values forced to `(20,5,11)`;
- `C_7` is also forced, with profile `(50,35,35,35,35,35,35)`.

Why I did not choose it:

- the mixed quotients `25 * 7 = 175` and `25 * 11 = 275` keep the orbit data cleaner than `35` or `55`;
- `C_175` is especially attractive because its fibers have size `11`, so all coefficient variables are bounded by `11`, which is exactly what closes the contradiction.

Self-check after approach B:
useful as a fallback, but weaker than the direct `C_175` orbit package.

## lemma_graph
Lemma skeleton.

1. `3` is a numerical multiplier because `3 | n = 225` and `gcd(3,1925) = 1`.
2. After translation, one may assume `3D = D`.
3. Mod `5`, the contracted coefficients are `(u,v,v,v,v)` with
   - `u + 4v = 260`
   - `u^2 + 4v^2 = 13700`
   hence `(u,v) = (40,55)` or `(64,49)`.
4. Mod `25`, the orbit-constant coefficients are `(a,b,c)` on
   - `{0}`
   - the four nonzero multiples of `5`
   - the twenty units,
   with
   - `a + 4b + 20c = 260`
   - `a^2 + 4b^2 + 20c^2 = 2920`.
5. Reduction `C_25 -> C_5` gives
   - zero coefficient `u = a + 4b`
   - each nonzero coefficient `v = 5c`,
   so `v` must be divisible by `5`, forcing the `C_5` profile `(40,55,55,55,55)` and therefore
   - `c = 11`
   - `a + 4b = 40`
   - `a^2 + 4b^2 = 500`,
   hence `(a,b,c) = (20,5,11)`.
6. Mod `7`, the orbit-constant coefficients are `(p,q,q,q,q,q,q)` with
   - `p + 6q = 260`
   - `p^2 + 6q^2 = 9850`,
   hence `(p,q) = (50,35)`.
7. Mod `175`, write the `3`-orbit coefficients as
   - `A` on the fixed point `0`
   - `B` on the size-`4` orbit of order-`5` elements
   - `C` on the size-`20` orbit of order-`25` elements
   - `D` on the size-`6` orbit of order-`7` elements
   - `e_1,e_2` on the two size-`12` order-`35` orbits
   - `f_1,f_2` on the two size-`60` order-`175` orbits.
8. Let `E = e_1 + e_2` and `F = f_1 + f_2`. Projection to `C_25` and `C_7` gives
   - `A + 6D = 20`
   - `B + 3E = 5`
   - `C + 3F = 11`
   - `A + 4B + 20C = 50`
   equivalently
   - `D + 2E + 10F = 35`.
9. Bounds `0 <= A,B,C,D,e_i,f_i <= 11` force:
   - `E <= 1` from `B + 3E = 5`
   - `F <= 3` from `C + 3F = 11`
   - `F = 3` from `D + 2E + 10F = 35` and `D <= 11`, `E <= 1`
   - then `D + 2E = 5`
   - `E = 1`, `D = 3` because otherwise `A = 20 - 6D < 0`
   - so `A = 2`, `B = 2`, `C = 2`, `E = 1`, `F = 3`.
10. The `C_175` square-sum equation is
    - `A^2 + 4B^2 + 20C^2 + 6D^2 + 12(e_1^2 + e_2^2) + 60(f_1^2 + f_2^2) = 610`.
11. Substituting `A = B = C = 2`, `D = 3` gives
    - `154 + 12(e_1^2 + e_2^2) + 60(f_1^2 + f_2^2) = 610`
    - `e_1^2 + e_2^2 + 5(f_1^2 + f_2^2) = 38`.
12. But `e_1 + e_2 = 1`, so `e_1^2 + e_2^2 = 1`. Hence
    - `5(f_1^2 + f_2^2) = 37`,
    impossible.

## chosen_plan
Choose approach A.

Reason:

- the mod-`25` and mod-`7` contractions are forced exactly and cheaply;
- the `C_175` orbit decomposition is still small enough to keep the argument human-readable;
- the fiber bound `<= 11` on `C_175` is the decisive extra structure.

What extra structure makes the result paper-shaped if the main claim closes:

- the exact `C_25` theorem slice `(20,5,11)`;
- the exact `C_7` theorem slice `(50,35)`;
- the orbit-refinement proposition on `C_175`;
- the one-line square-sum contradiction `e_1^2 + e_2^2 + 5(f_1^2 + f_2^2) = 38` with `e_1 + e_2 = 1`.

This would already be about `80%` of a short paper if verify accepts the multiplier normalization.

## self_checks
Major-step self-checks.

1. Statement lock:
   the target remained the exact Baumert-Gordon survivor row `(1925,260,35)`, with no drift to a family-level proxy.
2. Multiplier normalization:
   the normalization uses only `gcd(2,1925) = 1`, so no extra mod-`5` or mod-`7` translation argument is needed.
3. Mod `25` contraction:
   the third equation came from the already-forced mod-`5` orbit structure, not from an unjustified guess.
4. Mod `7` contraction:
   the quadratic has a unique integer solution.
5. `C_175` orbit bookkeeping:
   the orbit sizes match the additive orders `1,5,25,7,35,175` under multiplication by `3`.
6. Projection multiplicities:
   every factor `6`, `3`, `2`, and `10` comes from quotient-fiber sizes, not from heuristic averaging.
7. Final contradiction:
   the last step is genuinely arithmetic, not computational; once `E = 1` and `F = 3` are forced, the square-sum equation is impossible mod `5`.

## code_used
No code used.

The argument closed by exact quotient equations and orbit-count arithmetic alone, so no bounded experiment, checker, or search was needed.

## result
Provisional solve-stage disproof.

Claim:
the cyclic group `C_1925` does not admit a `(1925,260,35)` difference set.

Proof attempt.

Assume `D ⊂ C_1925` is a difference set with these parameters. Since `3 | n = 225` and `gcd(3,1925) = 1`, let `3D = D + s`. Choose `y` with `2y = s`; replacing `D` by `D - y` gives `3D = D`. Thus every contraction of `D` is constant on multiplication-by-`3` orbits.

First, contract to `C_5`. The `3`-orbits are `{0}` and the four nonzero elements, so the contracted coefficients are `(u,v,v,v,v)`. The quotient equations give

- `u + 4v = 260`
- `u^2 + 4v^2 = 13700`.

Hence `(u,v) = (40,55)` or `(64,49)`.

Next, contract to `C_25`. The `3`-orbits are `{0}`, the four nonzero multiples of `5`, and the twenty units, with coefficients `(a,b,c)`. The quotient equations are

- `a + 4b + 20c = 260`
- `a^2 + 4b^2 + 20c^2 = 2920`.

Reducing from `C_25` to `C_5`, the zero coefficient is `a + 4b` and each nonzero coefficient is `5c`. Therefore `v = 5c` is divisible by `5`, which eliminates `(64,49)` and forces `(u,v) = (40,55)`. So `c = 11`, and then

- `a + 4b = 40`
- `a^2 + 4b^2 = 500`,

giving `(a,b,c) = (20,5,11)`.

Now contract to `C_7`. The `3`-orbits are `{0}` and the six nonzero elements, with coefficients `(p,q,q,q,q,q,q)`. The quotient equations

- `p + 6q = 260`
- `p^2 + 6q^2 = 9850`

force `(p,q) = (50,35)`.

Finally, contract to `C_175`. Because `3` has orders `4,20,6,12,60` on additive orders `5,25,7,35,175`, the quotient has eight `3`-orbits with coefficients

- `A` on `0`
- `B` on the size-`4` orbit
- `C` on the size-`20` orbit
- `D` on the size-`6` orbit
- `e_1,e_2` on the two size-`12` orbits
- `f_1,f_2` on the two size-`60` orbits.

Each coefficient is in `[0,11]` because each `C_175` fiber has size `11`.

Let `E = e_1 + e_2` and `F = f_1 + f_2`.

Projecting `C_175 -> C_25` gives

- `A + 6D = 20`
- `B + 3E = 5`
- `C + 3F = 11`.

Projecting `C_175 -> C_7` gives

- `A + 4B + 20C = 50`,

equivalently

- `D + 2E + 10F = 35`.

Now use the bounds.

- From `B + 3E = 5`, one has `E <= 1`.
- From `C + 3F = 11`, one has `F <= 3`.
- From `D + 2E + 10F = 35` with `D <= 11` and `E <= 1`, one gets `F = 3`.
- Then `D + 2E = 5`.
- If `E = 0`, then `D = 5`, but `A = 20 - 6D = -10`, impossible.
- Therefore `E = 1`, `D = 3`, and consequently
  - `A = 2`
  - `B = 2`
  - `C = 2`
  - `D = 3`
  - `F = 3`.

The `C_175` square-sum equation is

`A^2 + 4B^2 + 20C^2 + 6D^2 + 12(e_1^2 + e_2^2) + 60(f_1^2 + f_2^2) = 610`.

Substituting the forced values yields

`154 + 12(e_1^2 + e_2^2) + 60(f_1^2 + f_2^2) = 610`,

so

`e_1^2 + e_2^2 + 5(f_1^2 + f_2^2) = 38`.

But `e_1 + e_2 = E = 1`, so `e_1^2 + e_2^2 = 1`. Hence

`5(f_1^2 + f_2^2) = 37`,

which is impossible.

Contradiction. Therefore no such difference set exists.

What part of the argument scales:

- exact multiplier normalization when `gcd(t-1,v) = 1`;
- solving tiny prime-power contractions first;
- pushing those forced profiles into a mixed quotient with small orbit census and small fiber bound.

What part does not scale automatically:

- the exact `C_175` orbit census for this `v`;
- the lucky fiber bound `<= 11`;
- the particular linear system coming from the forced `C_25` and `C_7` profiles.

What theorem slice is suggested:

- any hypothetical `(1925,260,35)` cyclic difference set, after translation, would have exact contractions `(40,55,55,55,55)` mod `5`, `(20,5,11)` by orbit type mod `25`, and `(50,35,35,35,35,35,35)` mod `7`;
- these profiles admit no orbit-constant refinement on `C_175`.

What next parameter shifts would help most:

- rows where a small multiplier `t` satisfies `gcd(t-1,v) = 1`, so exact invariance is immediate after translation;
- rows where a mixed quotient has small fiber size, giving hard coefficient bounds analogous to the `<= 11` bound here.

Current package assessment:
this is already much closer to a paper-shaped exact-row disproof than to a thin instance computation, but solve-stage conservatism means verify still needs to validate the multiplier theorem surface and the orbit-projection bookkeeping.

## family_affinity
Strong.

This sits squarely in the residual cyclic-difference-set lane:

- choose a small multiplier from `n`;
- normalize to exact invariance;
- solve tiny quotient contractions exactly;
- push them into one mixed quotient whose orbit structure is still human-manageable.

The argument is not a brute-force witness search. It is a short structural obstruction on a named Baumert-Gordon survivor row.

## generalization_signal
Moderate positive signal.

What looks reusable:

- the exact-invariance normalization when `gcd(t-1,v) = 1`;
- the prime-power quotient lock on `C_5` or `C_25`;
- the mixed-quotient contradiction using a small-fiber bound.

What looks row-specific:

- the exact forced values `(20,5,11)` and `(50,35)`;
- the fact that `C_175` has just enough orbit complexity to be informative but not too much to handle by hand;
- the final impossibility `5(f_1^2 + f_2^2) = 37`.

If this template transfers, it will transfer to sibling rows where one quotient supplies exact small coefficient values and another mixed quotient keeps the orbit variables few and tightly bounded.

## proof_template_reuse
Reusable template.

1. take a prime multiplier `t | n` with `gcd(t,v) = 1`;
2. if `gcd(t-1,v) = 1`, translate to exact `t`-invariance immediately;
3. solve the smallest quotient contractions exactly;
4. choose a mixed quotient whose orbit variables are few and whose fiber size is small;
5. use the smaller quotient profiles as projection constraints;
6. finish with the mixed-quotient square-sum contradiction.

This is a good micro-paper template because the proof remains theorem-first and human-readable throughout.

## candidate_theorem_slice
Candidate theorem slice.

After translation, any hypothetical cyclic `(1925,260,35)` difference set is exactly `3`-invariant. Its orbit-constant contractions are forced to be:

- mod `5`: `(40,55,55,55,55)`;
- mod `25`: coefficient `20` on `0`, coefficient `5` on each nonzero multiple of `5`, and coefficient `11` on each unit;
- mod `7`: coefficient `50` on `0` and `35` on each nonzero class.

There is no orbit-constant refinement of these slices to `C_175`.

## smallest_param_shift_to_test
Most informative nearby shifts:

- other Baumert-Gordon survivor rows where a prime multiplier `t` has `gcd(t-1,v) = 1`;
- rows where a prime-power quotient already forces one coefficient to be uniquely congruent or uniquely large, making the mixed-quotient refinement rigid;
- rows with a mixed quotient whose fibers are of size at most about `10` to `12`, since the hard coefficient bounds are doing real work here.

For this row’s immediate neighborhood, the first thing to test is any sibling tuple with a `5^2 * q * r` factorization of `v` and a small multiplier from `n`.

## why_this_is_or_is_not_publishable
If verify confirms the multiplier step and the orbit projection bookkeeping, this is already in the micro-paper lane.

- A successful solve here would already be roughly `80%` of a short paper.
- The exact title theorem is:
  `The cyclic group C_1925 does not admit a (1925,260,35) difference set.`
- Minimal remaining packaging work:
  - quote the precise multiplier theorem surface from Baumert-Gordon;
  - write the `C_5`, `C_25`, `C_7`, and `C_175` orbit decompositions cleanly;
  - add one short introductory paragraph locating the row in the Baumert-Gordon survivor table;
  - include one paragraph explaining why the contradiction is structural rather than search-based.

This is not too thin for the micro-paper lane if the proof survives verify. It already closes the exact row by a short orbit-refinement obstruction.

## paper_shape_support
Minimal paper-shaped support now visible.

- Proposition 1: after translation, the set is exactly `3`-invariant.
- Proposition 2: the mod-`25` orbit profile is exactly `(20,5,11)`.
- Proposition 3: the mod-`7` profile is exactly `(50,35)`.
- Proposition 4: no `3`-orbit-constant coefficient vector on `C_175` can project to both profiles.
- Main theorem: `C_1925` has no `(1925,260,35)` difference set.

One immediate corollary-style remark:
the obstruction is already visible before any character calculations or heavy search; the exact quotient arithmetic alone kills the row.

## boundary_remark
Boundary remark.

The proof uses specific arithmetic of this row:

- `n = 225` supplies the multiplier `3`;
- `gcd(3-1,1925) = 1` makes exact invariance available after translation;
- the quotient pair `25` and `7` gives forced profiles;
- the mixed quotient `175 = 25 * 7` has small enough orbit census and fiber size to close the contradiction.

So the scalable theme is real, but the exact contradiction is still parameter-specific.

## likely_failure_points
Load-bearing points for later audit.

1. Verify the exact source theorem supporting the use of `3` as a full-group multiplier for this row.
2. Check the `C_175` orbit census under multiplication by `3`:
   - sizes `1,4,20,6,12,12,60,60`.
3. Check the projection multiplicities:
   - to `C_25`: `6`, `3`, `3`;
   - to `C_7`: `2`, `10`.
4. Check the square-sum constants:
   - `13700` for `C_5`,
   - `2920` for `C_25`,
   - `9850` for `C_7`,
   - `610` for `C_175`.

If those four items hold, the contradiction itself is very short.

## what_verify_should_check
Verify should check the following exact points.

1. Baumert-Gordon or the standard multiplier theorem really permits the step:
   `3 | n` and `gcd(3,1925)=1` implies `3D = D + s`.
2. The translation normalization is written correctly:
   from `3D = D + s`, replacing `D` by `D - y` with `2y = s` gives exact `3D = D`.
3. The mod-`5` contraction equations have only the two solutions `(40,55)` and `(64,49)`.
4. The reduction `C_25 -> C_5` really forces `5c = 55`, hence `(20,5,11)`.
5. The mod-`7` contraction is exactly `(50,35)`.
6. The `C_175` orbit census and projection multiplicities are correct.
7. The final contradiction is exact:
   `e_1 + e_2 = 1` and `e_1^2 + e_2^2 + 5(f_1^2 + f_2^2) = 38` is impossible.

## verify_rediscovery
- PASS 1 used a bounded web sweep on the exact tuple, alternate cyclic notation, the canonical Baumert-Gordon source surface, and Daniel Gordon's web surfaces.
- The exact-tuple and alternate-notation probes did not uncover a later paper, repository entry, theorem, proposition, example, observation, or corollary explicitly settling the cyclic `(1925,260,35)` row.
- The canonical source still behaves as advertised: Baumert-Gordon isolate `(1925,260,35)` as a surviving Table 2 case rather than settling it internally.
- Within the allotted verify budget I did not find rediscovery evidence, so this run should not be archived as `REDISCOVERY`.

## verify_faithfulness
- The claimed theorem matches the intended statement exactly: the packet asks whether `C_1925` admits a `(1925,260,35)` difference set, and the solve artifact proves the exact negation of that statement.
- I did not find parameter drift, family-level broadening, proxy substitution, or a switch from cyclic existence to a different ambient-group question.
- The intermediate quotient propositions remain in service of the exact selected row rather than a nearby variant, so the correct verify classification is not `VARIANT`.

## verify_proof
- I did not find a first incorrect step.
- The load-bearing multiplier normalization is mathematically standard: since `3 | n = 225` and `gcd(3,1925) = 1`, the standard prime multiplier theorem for abelian difference sets gives `3D = D + s`; because `gcd(3 - 1,1925) = 1`, one can translate by `y` with `2y = s` and obtain exact `3D = D`.
- A conservative citation repair is still warranted in exposition: this opening step should be cited as the standard first multiplier theorem, not as Baumert-Gordon Theorem 3.2, which is a contracted-multiplier statement.
- The quotient identities are consistent:
  - mod `5`: `u + 4v = 260`, `u^2 + 4v^2 = 13700`, with integer solutions `(40,55)` and `(64,49)`;
  - mod `25`: reduction to mod `5` forces `5c = 55`, hence `(a,b,c) = (20,5,11)`;
  - mod `7`: the only integer solution is `(p,q) = (50,35)`.
- The `C_175` orbit census under multiplication by `3` is correct: orbit sizes are `1,4,6,12,12,20,60,60`, corresponding to additive orders `1,5,7,35,35,25,175,175`.
- The projection multiplicities are also correct:
  - to `C_25`: `A + 6D = 20`, `B + 3E = 5`, `C + 3F = 11`;
  - to `C_7`: `A + 4B + 20C = 50`, equivalently `D + 2E + 10F = 35`.
- With `0 <= A,B,C,D,e_i,f_i <= 11`, these equations force `A = B = C = 2`, `D = 3`, `E = 1`, `F = 3`.
- The `C_175` square-sum identity
  `A^2 + 4B^2 + 20C^2 + 6D^2 + 12(e_1^2 + e_2^2) + 60(f_1^2 + f_2^2) = 610`
  then reduces to
  `e_1^2 + e_2^2 + 5(f_1^2 + f_2^2) = 38`,
  while `e_1 + e_2 = 1` forces `e_1^2 + e_2^2 = 1`, giving `5(f_1^2 + f_2^2) = 37`, impossible.
- I do not see a hidden case or unjustified leap after the multiplier citation is stated correctly.

## verify_adversarial
- No checker file existed for this slug, so the adversarial pass reran the key arithmetic directly.
- I independently enumerated the multiplication-by-`3` orbits on `Z/175Z` and confirmed the exact orbit sizes and residue distributions used in the proof.
- I independently checked the orbit-to-quotient fiber counts:
  - each order-`35` orbit contributes `3` points to each nonzero multiple-of-`5` residue mod `25` and `2` points to each nonzero residue mod `7`;
  - each order-`175` orbit contributes `3` points to each unit residue mod `25` and `10` points to each nonzero residue mod `7`.
- I also reran a finite consistency check on the projected `C_175` integer system under the bounds `0..11` for every orbit coefficient; it has zero solutions.
- I did not find a computational escape hatch or a surviving candidate coefficient vector.

## verify_theorem_worthiness
- Exactness: strong. This is the exact Baumert-Gordon Table 2 row, not a softened or broadened claim.
- Novelty: bounded-positive. PASS 1 did not reveal rediscovery, but novelty remains only as strong as the capped exact-tuple search.
- Reproducibility: strong. The proof is short, arithmetic, and auditable by hand, with only tiny local checks needed.
- Lean readiness: not yet. The theorem is formalizable in principle, but Lean is not the shortest remaining path because publication audit and literature packaging are still the immediate gating work.
- Paper leverage: high for the micro-paper lane. If correct and later formalized, this argument already supplies most of a short residual-case note anchored to a named survivor row.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? Yes.
- What percentage of the paper would one solve already provide? About `0.80`.
- What title theorem is actually visible? `The cyclic group C_1925 does not admit a (1925,260,35) difference set.`
- What part of the argument scales? The multiplier normalization, the forced small-quotient contractions, and the mixed-quotient orbit-refinement contradiction template.
- What part clearly does not? The exact `C_175` arithmetic, the forced values `(20,5,11)` and `(50,35)`, and the terminal impossibility `5(f_1^2 + f_2^2) = 37`.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? No. The best honest publication status is `SLICE_CANDIDATE`: this is still an exact-row result, but it already looks like most of a residual-case note rather than a bare isolated computation.

## verify_verdict
- `verify_verdict = VERIFIED`
- `classification = COUNTEREXAMPLE`
- `publication_status = SLICE_CANDIDATE`
- `lean_ready = false`
- `lean_packet_seal = false`
- Reason: I found no rediscovery evidence and no incorrect mathematical step, but the claim is still not `EXACT` because Lean has not been completed, and publication audit is the next shorter path rather than formal sealing.

## minimal_repair_if_any
- No mathematical repair is needed.
- The only conservative repair is expository: cite the opening `3`-multiplier step as the standard first multiplier theorem for abelian difference sets, rather than implicitly leaning on Baumert-Gordon Theorem 3.2.

## publication_prior_art_audit
- Audit date: `2026-04-16`.
- Exact-statement probes on the tuple forms `(1925,260,35)`, `"1925,260,35" difference set`, and `v = 1925, k = 260, λ = 35` surfaced the Baumert-Gordon canonical source and did not surface a later exact-row settlement.
- Alternate-notation probes on `C_1925`, `n = 225`, and cyclic-difference-set wording likewise did not surface a later theorem, proposition, example, corollary, or observation settling this exact row.
- Canonical-source check: Baumert-Gordon still list `(1925,260,35)` in Table 2 as a surviving cyclic case with `gcd(v,n) > 1`; Sections `3.1` and `3.2` supply the contraction and contracted-multiplier tools, but the source's worked nonexistence theorem is for `(429,108,27)`, and Table 4 does not eliminate the `1925` row.
- Outside-source status pass: Dan Gordon's difference-set repository page presents itself as a status surface for known constructions and nonexistence results, and Gordon's publications page lists later difference-set papers through `2025`; within this bounded pass I did not find a title-level or accessible-preview indication that `(1925,260,35)` was later settled elsewhere.
- Conservative verdict: bounded-positive novelty only. I did not find rediscovery evidence, but this remains a capped audit rather than an exhaustive referee-grade survey.

## publication_statement_faithfulness
- The strongest honest claim is the exact negation of the selected question: `C_1925` does not admit a `(1925,260,35)` difference set.
- This is stronger than "here is an example." The packet presents a theorem-facing nonexistence result, not a witness, computation, or suggestive small case.
- No statement drift occurred during solve or verify: the argument stays on the exact cyclic row named in Baumert-Gordon Table 2 and does not silently broaden to a family theorem or narrow to a proxy instance.
- The candidate theorem slice is faithful to the packet: exact `3`-invariance, forced contractions modulo `25` and `7`, and the impossibility of a compatible orbit-constant refinement on `C_175`.

## publication_theorem_worthiness
- Is the strongest honest claim stronger than "here is an example"? Yes. It is an exact nonexistence theorem for a named survivor row.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Yes: `The cyclic group C_1925 does not admit a (1925,260,35) difference set.`
- Is the proof structural or merely instance-specific? Structural-but-row-specific. The contradiction comes from multiplier normalization, quotient identities, orbit structure, and a forced square-sum obstruction, not from a hand-picked construction failure.
- Would this survive a referee asking "what is the theorem?" Yes. The theorem is crisp, exact, and source-anchored.
- Is the claim still too dependent on hand-picked small cases? No in the harmful sense. The quotients `25`, `7`, and `175` are specific to the row, but they appear as load-bearing structural quotients, not as arbitrary case-bashing.

## publication_publishability
- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? Yes.
- What percentage of the paper would one solve already provide? About `0.86`.
- Publication narrative: strong. The note would close one exact Baumert-Gordon Table 2 survivor by a short structural nonexistence proof.
- Remaining gap: genuinely small. What remains is a clean literature-status paragraph, explicit citation of the first multiplier theorem, polished exposition of the quotient bookkeeping, and optional formal sealing. No broader theorem program is needed.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Lean is now a direct secondary seal for an already human-ready packet; it is not the gate for publication worthiness.

## publication_packet_audit
- Best honest publication status: `PAPER_READY`.
- Reason: the packet now has a clear title theorem, a short auditable structural proof, a canonical literature anchor, and a bounded prior-art pass that did not surface rediscovery. The remaining work is packaging, not new mathematics.
- Publication packet quality: strong.
- Proof artifacts are preserved well enough for handoff into the secondary Lean lane without blocking discovery work.
- Conservative caveat: the literature audit is intentionally narrow, so a later submission workflow should still rerun a fuller bibliography check before external circulation.

## micro_paper_audit
- MICRO-PAPER verdict: pass.
- Single-solve leverage remains high because the solve itself already supplies the title theorem, the main contradiction, and the paper's mathematical payload.
- Editorial overhead remains low: the proof is short and self-contained, and the source table already provides the narrative hook.
- The result is not merely an isolated curiosity. It closes an exact residual cyclic row in a standard reference and does so by a proof pattern that is recognizable to a combinatorics referee.
- This packet should be moved forward as a human-ready note, not expanded into a feeder-ladder program.

## strongest_honest_claim
No cyclic `(1925,260,35)` difference set exists. After first-multiplier normalization to exact `3`-invariance, the forced contractions modulo `25` and `7` admit no orbit-constant refinement on `C_175`; the bounded `2026-04-16` prior-art audit did not uncover a prior exact-tuple settlement.

## paper_title_hint
Nonexistence of a Cyclic `(1925,260,35)` Difference Set

## next_action
Mark this packet `PAPER_READY` and `human_ready`, move it off the main discovery queue, and place it in the secondary Lean queue. During writeup, cite the first multiplier theorem explicitly, keep the literature paragraph bounded to the Baumert-Gordon row plus Gordon's repository/publications surfaces, and do not expand the claim into a broader program.
