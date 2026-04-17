# Solve Record: Does the cyclic group C_419 admit a (419,133,42)-difference set?

- slug: `cyclic-difference-set-419-133-42`
- working_packet: `artifacts/cyclic-difference-set-419-133-42/working_packet.md`

## statement_lock
Determine whether the cyclic group C_419 admits a (419,133,42)-difference set.

Title theorem if the disproof closes: no cyclic `(419,133,42)` difference set exists.

## definitions
Work in `G = C_419 = Z/419Z` written additively.

A `(419,133,42)` difference set is a subset `D ⊂ G` with `|D| = 133` such that every nonzero `g ∈ G` has exactly `42` ordered representations `g = d1 - d2` with `d1,d2 ∈ D`.

The parameter identity holds:

- `k(k-1) = λ(v-1)` becomes `133·132 = 42·418 = 17556`.
- `n = k - λ = 133 - 42 = 91 = 7·13`.

Ambiguities / conventions to keep explicit:

1. The load-bearing external input is the multiplier theorem surface. The working packet cites Baumert-Gordon Theorem `3.2`; a repo-local audited paraphrase says: if each prime factor of `n` is congruent modulo `w` to a power of `t`, then `t` is a `w`-multiplier.
2. In the prime-order cyclic group, an affine multiplier relation `tD = D + s` can always be normalized to pure invariance by translating by the unique fixed point of `x ↦ tx - s`, because `t-1` is invertible modulo `419`.
3. Since this is solve stage, the proof should be read as theorem-facing with one source-check item preserved for verify: confirm the exact Baumert-Gordon Theorem `3.2` wording matches the use below.

## approach_A
Structural / invariant route.

1. Compute the orders of the prime divisors of `n` modulo `419`:
   - `7^19 ≡ 1 (mod 419)` and `7 ≠ 1`, so `ord_419(7) = 19`.
   - `13^11 ≡ 1 (mod 419)` and `13 ≠ 1`, so `ord_419(13) = 11`.
2. Therefore the subgroup `H = <7,13> ≤ (Z/419Z)^×` has order `19·11 = 209`; the two prime-order subgroups intersect trivially because `(Z/419Z)^×` is cyclic.
3. Choose a generator `t` of `H`. Then both prime factors `7` and `13` of `n` are powers of `t mod 419`.
4. Apply the repo-local Theorem `3.2` paraphrase with `w = 419`: `t` is a `419`-multiplier, so `tD = D + s` for some `s`.
5. Translate `D` to `E = D + c` with `(t-1)c ≡ -s (mod 419)`. Then `tE = E`.
6. Since `ord(t) = 209` and `419` is prime, the `t`-orbits on `G` are:
   - `{0}`,
   - two nonzero orbits, each of size `209`.
7. Any `t`-invariant subset has size in `{0,1,209,210,418,419}`. But `|E| = |D| = 133`, contradiction.

If the multiplier input is valid, this is already a full nonexistence proof.

## approach_B
Construction / extremal contradiction route.

1. Track the two prime divisors separately. The order computations give a `19`-orbit pattern from `7` and an `11`-orbit pattern from `13`.
2. Individually, these congruence constraints do not kill `k = 133`:
   - `133 ≡ 0 (mod 19)`,
   - `133 ≡ 1 (mod 11)`.
3. The useful point is not either congruence alone, but that the two primes together generate a subgroup of order `209`.
4. Once any generator `t` of that subgroup is certified as a multiplier, the affine orbit picture collapses to `1`- and `209`-blocks only, and `133` cannot be assembled from those block sizes.

This is the better contradiction route because it reaches a one-line orbit-count obstruction instead of a longer contracted-coefficient computation.

## lemma_graph
Lemma graph / proof skeleton.

1. Parameter check: `n = 91 = 7·13`.
2. Modular-order lemma:
   - `ord_419(7) = 19`,
   - `ord_419(13) = 11`.
3. Subgroup lemma: `H = <7,13>` has order `209` and is cyclic.
4. Multiplier lemma: if Theorem `3.2` is applied with a generator `t` of `H`, then `tD = D + s`.
5. Translation lemma: because `gcd(t-1,419)=1`, there exists `c` with `t(D+c) = D+c`.
6. Orbit lemma: a multiplier of order `209` on `C_419` has orbit sizes `1,209,209`.
7. Counting contradiction: `133` is not a sum of `0` or `1` copies of `1` and up to two copies of `209`.

Extra structure that would make the result paper-shaped if the main claim closes:

1. State the general orbit obstruction as a standalone lemma: in prime-order cyclic groups, a multiplier whose generated subgroup on nonzero elements has orbit size `m` forces `k ≡ 0 or 1 (mod m)` when `(v-1)/m = 2`.
2. Then present `(419,133,42)` as the first exact residual row where `m = 209` gives immediate nonexistence.
3. Minimal packaging after closure would be a short source-placement paragraph and a concise theorem/lemma split; mathematically this would already be about `80%` of a micro-paper.

## chosen_plan
Choose Approach `A`.

Reason:

1. It uses only one candidate-local external theorem surface, namely the multiplier criterion already singled out in the packet.
2. It avoids search, contraction algebra, and any heavy computation.
3. If valid, it yields the exact title theorem directly: `C_419` admits no `(419,133,42)` difference set.

Minimal remaining packaging work if this closes:

1. cite Baumert-Gordon's survivor-row placement and the exact Theorem `3.2` wording;
2. split the proof into a multiplier lemma and an orbit-count theorem proof;
3. add one brief boundary remark explaining why the argument is specific to the subgroup generated by the `n`-primes.

## self_checks
After statement lock:

1. The parameter arithmetic is exact: `133·132 = 42·418` and `n = 91`.

After the order computation:

2. `19 | 418` and `11 | 418`, so the claimed orders are plausible divisors of `|(Z/419Z)^×| = 418`.

After the multiplier step:

3. The affine normalization is legal because `t ≠ 1 (mod 419)`, hence `t-1` is invertible modulo prime `419`.

After the orbit count:

4. The only possible sizes of a `t`-invariant subset are `0,1,209,210,418,419`; `133` is excluded.

Global self-check:

5. The only load-bearing nontrivial citation is the Theorem `3.2` multiplier criterion. If verify confirms that citation, no further algebraic step looks open.

After the bounded arithmetic check:

6. A tiny Python verification confirmed `ord_419(7)=19`, `ord_419(13)=11`, `|<7,13>|=209`, and found `3` as an explicit generator of that subgroup.

## code_used
Yes, but only as bounded arithmetic verification.

Used:

1. a tiny `python3` snippet to confirm `ord_419(7)=19`, `ord_419(13)=11`, `|<7,13>|=209`, and to exhibit `3` as a generator of the subgroup generated by `7` and `13` modulo `419`.

Not used:

2. no search, SAT, ILP, brute force, or coefficient enumeration.

## result
Current solve-stage result: a clean candidate disproof.

Proof attempt.

Assume `D ⊂ Z/419Z` is a cyclic `(419,133,42)` difference set. Let `n = 91 = 7·13`.

First compute the orders of the two prime divisors of `n` modulo `419`.

- For `7`:
  - `7^2 = 49`,
  - `7^4 ≡ 49^2 = 2401 ≡ 306 (mod 419)`,
  - `7^8 ≡ 306^2 = 93636 ≡ 199 (mod 419)`,
  - `7^11 ≡ 7^8·7^2·7 ≡ 199·49·7 ≡ 379 (mod 419)`,
  - `7^19 ≡ 7^11·7^8 ≡ 379·199 = 75421 ≡ 1 (mod 419)`.
  Since `19` is prime and `7 ≠ 1`, this gives `ord_419(7) = 19`.

- For `13`:
  - `13^2 = 169`,
  - `13^4 ≡ 169^2 = 28561 ≡ 69 (mod 419)`,
  - `13^8 ≡ 69^2 = 4761 ≡ 152 (mod 419)`,
  - `13^11 ≡ 13^8·13^2·13 ≡ 152·169·13 ≡ 129·13 = 1677 ≡ 1 (mod 419)`.
  Since `11` is prime and `13 ≠ 1`, this gives `ord_419(13) = 11`.

Hence `H = <7,13>` has order `19·11 = 209` inside the cyclic group `(Z/419Z)^×`, so `H` itself is cyclic. The bounded arithmetic check found an explicit generator `t = 3` for `H`. Therefore both prime factors `7` and `13` of `n` are powers of `3 mod 419`.

Using the repo-local paraphrase of Baumert-Gordon Theorem `3.2`, this implies that `t` is a `419`-multiplier. Therefore

`tD = D + s`

for some `s ∈ Z/419Z`. Because `419` is prime and `t ≠ 1`, the congruence

`(t-1)c ≡ -s (mod 419)`

has a unique solution `c`. For `E = D + c`, we get

`tE = t(D+c) = tD + tc = D + s + tc = D + c = E`.

So `E` is setwise invariant under multiplication by `t`.

Now `ord(t) = 209`. On the additive group `Z/419Z`, multiplication by `t` fixes `0`, and if `x ≠ 0` then `tx = x` would imply `(t-1)x = 0`, impossible because `t ≠ 1` and `419` is prime. Thus every nonzero orbit has size `209`. Since there are `418` nonzero elements total, there are exactly two nonzero orbits.

Therefore every `t`-invariant subset of `Z/419Z` has size

`0, 1, 209, 210, 418, or 419`.

But `|E| = |D| = 133`, impossible. This contradiction shows that no cyclic `(419,133,42)` difference set can exist, provided the cited Theorem `3.2` paraphrase matches the source exactly.

What naturally falls out:

1. The instance matters because it converts a named survivor-row from Baumert-Gordon into a one-lemma orbit obstruction.
2. A natural boundary remark is that the proof uses only the subgroup generated by the prime divisors of `n`; it does not need a full coefficient contraction.
3. On the current evidence this is closer to a paper-shaped exact disproof than to a thin isolated computation, but the source-theorem check is still mandatory before promotion.

## family_affinity
High. This argument sits directly in the Baumert-Gordon cyclic-survivor lane: use the multiplier theorem coming from the factorization of `n`, then force an orbit-size contradiction in the prime-order ambient group.

## generalization_signal
Real but narrow. The part that scales is the template:

1. compute the subgroup `H` of `(Z/vZ)^×` generated by the prime divisors of `n`;
2. if Theorem `3.2` certifies a generator of `H` as a multiplier modulo `v`;
3. compare the resulting orbit sizes on `C_v` against `k`.

What does not automatically scale is the final contradiction: it depends on `v` prime and on `k` failing the orbit-size congruence forced by `|H|`.

## proof_template_reuse
Reusable template:

1. get `n = k-λ`;
2. compute orders of the primes dividing `n` modulo the cyclic modulus `v`;
3. pass to the subgroup generated by those prime residues;
4. invoke the multiplier theorem on a generator of that subgroup;
5. kill the case by orbit-size arithmetic after translation normalization.

This looks reusable for other residual cyclic rows where the `n`-prime subgroup is large and `v` is prime or nearly prime.

## candidate_theorem_slice
Suggested theorem slice:

If `v` is prime and a cyclic `(v,k,λ)` difference set has a multiplier `t` whose multiplicative order modulo `v` is `m`, then `k` must be a sum of `0` or `1` and whole `m`-orbits on `F_v^×`. In particular, when `(v-1)/m = 2`, one must have `k ∈ {0,1,m,m+1,2m,2m+1}`.

The `(419,133,42)` row is the concrete slice with `m = 209`.

## smallest_param_shift_to_test
Best next parameter shifts, if this proof shape survives verify:

1. any other Baumert-Gordon prime-order row where the subgroup generated by the prime divisors of `n` has index `2` in `(Z/vZ)^×`;
2. nearby rows where the same subgroup has orbit size forcing a simple congruence `k ≡ 0 or 1 (mod m)`.

Those are the shifts most likely to reuse the exact same proof skeleton with minimal new work.

## why_this_is_or_is_not_publishable
If the multiplier citation checks out, this is likely publishable in the micro-paper lane.

Why:

1. The exact title theorem would be: `The cyclic group C_419 admits no (419,133,42) difference set.`
2. That theorem closes a named survivor-row already framed in Baumert-Gordon.
3. The proof is short, structural, and not search-heavy.
4. The remaining packaging work is light: source placement, a precise theorem citation, and a concise writeup.

Current caveat:

5. Until verify confirms the exact Theorem `3.2` hypotheses and novelty surface, the honest solve-stage stance is "strong candidate disproof, not yet audited publication fact."

So a successful verification would leave this around the `70-90%` paper-complete band; without that theorem check, it is still too thin to call fully publication-ready.

## paper_shape_support
The smallest supporting structure needed for paper shape is already visible:

1. a lemma computing `ord_419(7)=19` and `ord_419(13)=11`;
2. a lemma that the subgroup generated by the `n`-primes has order `209`;
3. a multiplier lemma citing Baumert-Gordon Theorem `3.2`;
4. the final orbit-size contradiction theorem.

That is enough for a short residual-case note. No feeder ladder is visible.

## boundary_remark
Boundary remark: the proof is instance-sharp in one sense and family-facing in another. It is sharply tied to the large order-`209` multiplier subgroup inside `(Z/419Z)^×`, so it does not automatically say anything about arbitrary `(v,k,λ)` rows. But the mechanism is not ad hoc: it isolates a clean theorem slice for prime-order cyclic rows where the subgroup generated by the prime divisors of `n` is large enough that the orbit sizes already outrun `k`.

## likely_failure_points
1. The only serious failure point is theorem-surface accuracy: verify must check that the exact Baumert-Gordon Theorem `3.2` statement really permits choosing a generator `t` whose powers cover all prime divisors of `n`.
2. A secondary check is presentational: the final writeup should state clearly that the contradiction is obtained after affine translation normalization, not from literal fixedness of the original set.
3. No computational or brute-force gap is present in the current argument.

## what_verify_should_check
1. Confirm from the Baumert-Gordon source that Theorem `3.2` has the exact hypothesis used here: each prime factor of `n` is congruent modulo `419` to some power of `t`, implying `t` is a `419`-multiplier. The current solve uses `t = 3`.
2. Confirm the literature anchor still honestly treats `(419,133,42)` as unsettled before this argument.
3. Recheck the modular-order arithmetic:
   - `ord_419(7)=19`,
   - `ord_419(13)=11`,
   - therefore the generated subgroup has order `209`.
4. Confirm the translation-normalization and orbit-size count are stated cleanly in publication form.

## verify_rediscovery
PASS 1 used the bounded web budget and established rediscovery.

- The canonical source [`Baumert-Gordon 2004`](https://www.dmgordon.org/papers/cds.pdf) still anchors `(419,133,42)` as an open cyclic row in Table `1`.
- A later source, Leung-Ma-Schmidt, *A Multiplier Theorem* ([mirror used during verify](https://paperzz.com/doc/7715711/a-multiplier-theorem---nanyang-technological-university)), explicitly eliminates the exact tuple in Example `5.4`.
- That example records that for `(v,k,lambda)=(419,133,42)` one may apply Corollary `4.1` with `n_1=13`, making `13` a multiplier, and then finish by a quick computer search.

Conclusion for PASS 1:

- the exact intended statement is already settled in prior art;
- this run is a rediscovery, not a frontier solve;
- the verify classification must therefore be `REDISCOVERY`.

## verify_faithfulness
The solver targeted the exact intended statement. There is no theorem-scope drift in the main claim: the record is trying to decide precisely whether `C_419` admits a cyclic `(419,133,42)` difference set.

The failure is citation-direction drift inside the proof:

- Baumert-Gordon Theorem `3.2` is used as though it suffices that each prime divisor of `n` is a power of the chosen element `t` modulo `419`.
- The source hypothesis goes the other way: for each prime divisor `p_i` of `n`, one needs some exponent `j(i)` with `p_i^{j(i)} ≡ t (mod w)`.
- The solve record chooses `t = 3` as a generator of `<7,13>` and then argues that `7` and `13` are powers of `3`. That is not the cited theorem.

Faithfulness verdict: exact statement yes, exact source use no.

## verify_proof
First incorrect step: the application of Baumert-Gordon Theorem `3.2` to the order-`209` element `t = 3`.

Why it fails:

- the arithmetic check confirms `ord_419(7)=19` and `ord_419(13)=11`;
- therefore `<7>` and `<13>` have coprime orders and intersect only in `{1}`;
- so no nontrivial residue can simultaneously be a power of `7` and a power of `13` modulo `419`;
- in particular, `t = 3` cannot satisfy the actual Theorem `3.2` hypothesis for both prime divisors of `n = 7·13`.

Everything after that point depends on having a certified multiplier of order `209`. The translation-normalization and orbit-count contradiction are conditionally fine once such a multiplier exists, but the proof never establishes that premise.

Proof verdict: incorrect as written; the first load-bearing failure is the multiplier certification step.

## verify_adversarial
PASS 4 reran the bounded arithmetic checks used by the solve stage.

Python recheck results:

- `ord_419(7) = 19`
- `ord_419(13) = 11`
- `|<7,13>| = 209`
- `3 in <7,13>`
- `3 not in <7>`
- `3 not in <13>`
- `13 not in <7>`
- `7 not in <13>`
- `<7> ∩ <13> = {1}`

This adversarial check confirms two things simultaneously:

1. the local arithmetic scaffolding is correct;
2. the theorem application needed for the `209`-orbit obstruction is impossible in the form used by the solver.

No repo-local checker exists for the later-paper "quick computer search", so verify does not claim to have independently reproduced that prior-art computation.

## verify_theorem_worthiness
Exactness:

- the intended statement is exact, but the current run does not produce a new exact theorem.

Novelty:

- none; PASS 1 established rediscovery.

Reproducibility:

- the local proof is not reproducible as a valid argument because its key citation step fails;
- the exact nonexistence claim is reproducible only as prior art, not as a new result of this run.

Lean readiness:

- `false`; Lean would not be the shortest remaining path because the novelty lane is already closed and the current local proof is unsound.

Paper leverage:

- as frontier work, effectively none.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No. The exact statement is already in prior art.
- What percentage of the paper would one solve already provide? `0%` as new publication leverage, because the novelty-bearing contribution is gone.
- What title theorem is actually visible? The already-known theorem that no cyclic `(419,133,42)` difference set exists, with the later-paper route using multiplier `13` plus a quick computer search.
- What part of the argument scales? Only the arithmetic preprocessing and the general idea of using multiplier structure as a screen.
- What part clearly does not? The claimed order-`209` multiplier orbit contradiction; it depends on an invalid reading of Theorem `3.2`.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? Neither. Under the harness rules the correct publication status is `REDISCOVERY`.

## verify_verdict
- `verify_verdict = REDISCOVERY`
- `classification = REDISCOVERY`
- `publication_status = REDISCOVERY`
- `lean_ready = false`
- `next_action = archive_as_rediscovery`

## minimal_repair_if_any
No tiny conservative repair salvages the current proof into a new verified result.

The smallest honest repair is archival only:

- mark the packet as a rediscovery;
- cite the later prior-art elimination of `(419,133,42)`;
- preserve the local order computations as non-load-bearing background notes;
- do not retain the `t = 3` orbit argument as a valid proof.
