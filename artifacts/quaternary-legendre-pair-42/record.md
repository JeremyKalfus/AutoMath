# statement_lock

Active slug: `quaternary-legendre-pair-42`

Active title: `Does there exist a quaternary Legendre pair of length 42?`

I lock the intended statement as:

There exists a pair of sequences `A, B : Z/42Z -> {1, -1, i, -i}` such that for every nonzero shift `s mod 42`,

`PAF_A(s) + PAF_B(s) = -2`,

where

`PAF_A(s) = sum_j A_j * conjugate(A_{j+s})`

and likewise for `B`.

This `-2` constant is not written explicitly in `selected_problem.md`, so this solve attempt depends on the standard Legendre-pair convention being exactly that one. If verification finds a different normalization or constant, the argument below has to be re-derived.

# definitions

Let `omega = exp(2*pi*i/42)`, and define the Fourier transforms

`A^(k) = sum_{j=0}^{41} A_j * omega^(jk)`,

`B^(k) = sum_{j=0}^{41} B_j * omega^(jk)`.

By the periodic Wiener-Khinchin identity,

`|A^(k)|^2 = sum_{s=0}^{41} PAF_A(s) * omega^(-ks)`,

and similarly for `B`.

Write the even/odd partial sums

`E_A = sum_{j=0}^{20} A_{2j}`, `O_A = sum_{j=0}^{20} A_{2j+1}`,

`E_B = sum_{j=0}^{20} B_{2j}`, `O_B = sum_{j=0}^{20} B_{2j+1}`.

Then

`A^(0) = E_A + O_A`,

`A^(21) = E_A - O_A`,

and similarly for `B`, because `omega^21 = -1`.

For any odd-length quaternary block `X` of length `21`, if its symbol counts are

`n_1, n_{-1}, n_i, n_{-i}`,

then its sum is

`S_X = (n_1 - n_{-1}) + i (n_i - n_{-i})`.

Since `n_1 + n_{-1} + n_i + n_{-i} = 21` is odd, the real and imaginary parts of `S_X` have opposite parity. Therefore `|S_X|^2` is always odd.

# approach_A

Structural / invariant route: use Fourier identities at special frequencies and parity splitting.

Assuming the standard Legendre condition `PAF_A(s) + PAF_B(s) = -2` for all nonzero `s`, the combined autocorrelation sequence is

`C(0) = 84`,

`C(s) = -2` for `1 <= s <= 41`.

Hence

`|A^(0)|^2 + |B^(0)|^2 = 84 - 2*41 = 2`,

and for every nonzero frequency `k`,

`|A^(k)|^2 + |B^(k)|^2 = 84 - 2*(-1) = 86`.

In particular,

`|E_A + O_A|^2 + |E_B + O_B|^2 = 2`,

`|E_A - O_A|^2 + |E_B - O_B|^2 = 86`.

Adding these gives

`|E_A|^2 + |O_A|^2 + |E_B|^2 + |O_B|^2 = 44`.

Since each of the four norms comes from a length-21 quaternary block, each is odd.

This is a strong necessary condition, but not yet a contradiction: four odd sums of two squares can sum to `44`.

Immediate consequence from the zero-frequency equation:

For a length-42 quaternary sequence, the total sum has real and imaginary parts of the same parity, so its norm is even. Because two even norms sum to `2`, one sequence must have total sum `0`, and the other must have norm `2`. Up to swapping `A, B` and multiplying a sequence by a unit, I may normalize to

`sum A_j = 0`,

`sum B_j = 1 + i`.

That forces

`O_A = -E_A`,

`E_B + O_B = 1 + i`.

Self-check:

- I initially wrote the nonzero Fourier constant as `44`; that was wrong. The correct value is `86` because `C(0) = 84`, not `42`.
- After correction, the parity argument becomes a necessary-condition reduction, not a proof.

# approach_B

Construction / extremal / contradiction route: normalize the full sums, then reduce the parity totals to a small finite state space.

Under the normalization

`sum A_j = 0`, `sum B_j = 1 + i`,

write

`E_A = u`, `O_A = -u`,

`E_B = x`, `O_B = 1 + i - x`.

Then the parity-norm identity becomes

`2|u|^2 + |x|^2 + |1 + i - x|^2 = 44`,

where `u` and `x` must each be realizable as sums of `21` quaternary unit entries.

That is a finite Gaussian-integer feasibility problem at the aggregate level. It does not encode the full sequence, but it sharply limits the allowed parity profiles before any search over actual sequences.

Self-check:

- This route is still reasoning-first: it uses only parity totals, not sequence enumeration.
- It cannot by itself prove existence or nonexistence, because many distinct sequences collapse to the same Gaussian totals.

# lemma_graph

1. Standard Legendre condition implies the combined autocorrelation values are `84` at shift `0` and `-2` at every nonzero shift.
2. Fourier transform of the combined autocorrelation gives the PSD identities:
   `|A^(0)|^2 + |B^(0)|^2 = 2` and `|A^(k)|^2 + |B^(k)|^2 = 86` for `k != 0`.
3. Evaluating at `k = 0` and `k = 21` rewrites these as equations in the even/odd block sums.
4. Any length-21 quaternary block sum has odd norm.
5. Therefore the four parity-block norms are odd and sum to `44`.
6. The full-sequence sums are even norms summing to `2`, so after normalization one sequence has total sum `0` and the other total sum `1 + i`.
7. Under that normalization, the parity-block totals reduce to the finite equation
   `2|u|^2 + |x|^2 + |1 + i - x|^2 = 44`.
8. If that finite system had no realizable solutions, we would get a contradiction. It does have realizable aggregate states, so more structure is needed.

# chosen_plan

The best path was Approach A first, because special-frequency identities are exact, cheap, and potentially decisive at `42 = 2 * 3 * 7`.

Once that stopped short of a contradiction, I used Approach B only at the aggregate level: normalize the total sums and enumerate the surviving Gaussian parity-block totals. This is much smaller than any sequence search and stays within the repo's solve-stage code policy.

# self_checks

Step 1: statement lock

- Checked that the dossier never spells out the constant.
- Chose the standard Legendre-pair convention `-2` explicitly and flagged it as the main dependency.

Step 2: special-frequency identities

- Re-derived the Fourier identities from the combined autocorrelation sequence.
- Corrected an earlier arithmetic mistake: nonzero PSD total is `86`, not `44`.

Step 3: parity-block norms

- Verified that every length-21 quaternary block sum has odd norm because its real and imaginary parts have opposite parity.
- Confirmed that the four parity-block norms therefore sum to `44`.

Step 4: normalized totals

- Verified that a length-42 quaternary total sum has even norm, so the zero-frequency identity forces one total sum to be `0` and the other to have norm `2`.
- Normalized to `sum A_j = 0`, `sum B_j = 1 + i` up to swapping and unit multiplication.

Step 5: bounded aggregate search

- Checked only Gaussian-integer parity totals, not full sequences.
- Found a small surviving state space, so the current obstruction is incomplete.

# code_used

Yes, but only a tiny bounded aggregate enumerator.

Purpose:

- Enumerate feasible Gaussian totals for the even/odd length-21 blocks under the normalization
  `sum A_j = 0`, `sum B_j = 1 + i`.
- No SAT/ILP/CP-SAT/brute-force sequence search was used.
- No candidate sequence search was attempted.

Result of the aggregate enumeration:

There are `88` surviving parity-total states, collapsing to only `8` norm triples for

`(|E_A|^2, |E_B|^2, |O_B|^2)`:

- `(1, 17, 25)`
- `(1, 25, 17)`
- `(9, 9, 17)`
- `(9, 13, 13)`
- `(9, 17, 9)`
- `(13, 5, 13)`
- `(13, 13, 5)`
- `(17, 5, 5)`

Since `O_A = -E_A`, the corresponding `|O_A|^2` equals `|E_A|^2`.

This is useful narrowing, but not a full contradiction.

# result

Current solve-stage verdict: `PARTIAL`.

What was established under the standard `-2` convention:

- One sequence must have total sum `0`.
- The other must have total sum of norm `2`, so after unit normalization its total sum may be taken as `1 + i`.
- The four even/odd block sums of length `21` must have odd norms summing to `44`.
- After normalization, only `88` aggregate parity-total states survive, spread across the `8` norm triples listed above.

What was not established:

- I did not prove nonexistence.
- I did not construct a witness.
- I did not reduce the problem to a contradiction that is independent of any further residue-class structure.

# likely_failure_points

- The entire derivation depends on the exact Legendre-pair condition being `PAF_A(s) + PAF_B(s) = -2` for every nonzero shift.
- If the source uses a different normalization of autocorrelation or a different constant, the Fourier identities in this record must be adjusted.
- The aggregate search only tracks Gaussian block sums; it deliberately ignores the finer autocorrelation structure across the `21` positions, so it cannot certify feasibility.

# what_verify_should_check

- First confirm from the canonical source that the standard quaternary Legendre-pair condition at length `42` is exactly `PAF_A(s) + PAF_B(s) = -2` for all nonzero `s`.
- Re-check the Fourier calculation:
  `|A^(0)|^2 + |B^(0)|^2 = 2` and `|A^(k)|^2 + |B^(k)|^2 = 86` for `k != 0`.
- Re-check the parity fact that every length-21 quaternary block sum has odd norm.
- Reproduce the bounded aggregate enumeration of parity-block totals.
- If continuing solve work, the next plausible attack is to combine the surviving parity-total states with a residue-class split mod `3` or mod `7`, rather than launching a full sequence search immediately.

# verify_rediscovery

PASS 1 used a bounded web audit only.

Search targets covered:

- exact instance: `quaternary Legendre pair 42`
- alternative family notation: `Quaternary Legendre pairs II 42`
- canonical source lookup
- same-source theorem / proposition / example / corollary checks
- one recent status check for any post-2025 resolution

Outcome:

- I found no evidence that the exact instance `l = 42` has been solved in the literature.
- The canonical 2025 source still presents `42` as the smallest unresolved case.
- The same-source checks support the normalization used in this record: for a quaternary Legendre pair of even length `l`, the nonzero-shift condition is `PAF_A(s) + PAF_B(s) = -2`.
- A bounded follow-up status search did not surface a later construction for length `42`.

Verdict for PASS 1:

- `verify_verdict` is not `REDISCOVERY`.
- This run should not be archived as a rediscovery on current evidence.
- The current solve notes also do not amount to a rediscovered proof of a known theorem; they are only a partial reduction.

# verify_faithfulness

The record is mostly faithful to the intended problem after the normalization issue is checked.

- The locked mathematical statement matches the standard quaternary Legendre-pair definition once the nonzero-shift constant is taken to be `-2`.
- The Fourier identities and parity-splitting setup are aimed at the exact intended instance `l = 42`; they are not solving a different length or a different object.
- However, the solve-stage output does not prove the intended existential statement. It proves only necessary conditions and a reduced aggregate feasibility equation.

So there is no wrong-theorem drift in the setup, but there is also no exact solve. The run should remain a partial attempt, not an exact result and not a Lean candidate.

# verify_proof

First incorrect step found: none, for the partial claims actually established.

Checks performed:

- From `C(0) = 84` and `C(s) = -2` for nonzero `s`, the PSD totals
  `|A^(0)|^2 + |B^(0)|^2 = 2` and `|A^(k)|^2 + |B^(k)|^2 = 86` for `k != 0`
  are correct.
- At `k = 21`, the identities
  `A^(21) = E_A - O_A` and `B^(21) = E_B - O_B` are correct because `omega^21 = -1`.
- For a length-21 quaternary block, the real and imaginary parts of its sum have opposite parity, so the squared norm is odd.
- For a length-42 quaternary sequence, the real and imaginary parts of the total sum have the same parity, hence the squared norm is even.
- Therefore the zero-frequency identity forces the pair of total norms to be `(0, 2)` up to order, so the normalization to `sum A_j = 0`, `sum B_j = 1 + i` up to swapping and multiplication by a unit is justified.

What fails is not a specific derivation step but the jump from these necessary conditions to any exact existential conclusion. The argument stops at a reduced state space and does not settle existence or nonexistence.

# verify_adversarial

No saved checker or enumerator was present in the artifact directory, so I reran the aggregate-state computation from scratch locally.

Local recomputation results:

- realizable Gaussian sums of `21` quaternary entries: `484`
- surviving normalized aggregate states: `88`
- surviving norm triples: `8`

The reproduced triples are exactly:

- `(1, 17, 25)`
- `(1, 25, 17)`
- `(9, 9, 17)`
- `(9, 13, 13)`
- `(9, 17, 9)`
- `(13, 5, 13)`
- `(13, 13, 5)`
- `(17, 5, 5)`

This confirms the reported aggregate enumeration, but it also confirms the limitation: these states are only aggregate totals and do not certify an actual Legendre pair.

# verify_verdict

`UNVERIFIED`

Reason:

- no rediscovery established
- setup and partial derivation look mathematically sound
- but the intended statement is still unresolved by this artifact
- no witness, no contradiction, and no exact theorem has been proved
- therefore the run is not Lean-ready

Recommended classification after verification:

- `classification = "PARTIAL"`
- `lean_ready = false`

# minimal_repair_if_any

No mathematical repair was needed for the partial claims in the record.

The only conservative repair is classificatory:

- do not treat the run as a proof attempt that is close enough for Lean
- keep it as a partial reduction
- continue only if a new reasoning step uses the surviving parity states together with additional mod `3` or mod `7` structure
