# Solve Record: The Cyclic (990,345,120) Difference-Set Case

- slug: `cyclic-difference-set-990-345-120`
- working_packet: `artifacts/cyclic-difference-set-990-345-120/working_packet.md`

## statement_lock
Determine whether the cyclic group C_990 admits a (990,345,120)-difference set.

Exact intended theorem if the solve closes:
`The cyclic group C_990 does not admit a (990,345,120)-difference set.`

If that exact nonexistence proof lands cleanly, it is plausibly 80%+ of the paper: the residual-case title theorem is already fixed, and the remaining packaging is mostly introduction, source-status context, and proof polishing.

## definitions
Write `G = Z/990Z` additively. A `(990,345,120)` difference set is a subset `D ⊂ G` with `|D| = 345` such that every nonzero `g ∈ G` has exactly `120` ordered representations `g = d_1 - d_2` with `d_i ∈ D`.

Set `n = k - λ = 225 = 3^2 5^2`.

For a quotient `π : G -> Q` with kernel size `h`, let `x_q = |D ∩ π^{-1}(q)|`. Then the contracted group-ring equations are:

- `Σ_q x_q = 345`
- `Σ_q x_q^2 = k + λ(h - 1) = n + λ h`
- for every nonzero `t ∈ Q`, `Σ_q x_q x_{q+t} = λ h`

For every nonprincipal character `χ` of `G`, `|χ(D)|^2 = n = 225`. On a quotient `Q`, this forces every nonprincipal Fourier coefficient of the contracted vector to have modulus `15`.

Ambiguities and conventions:

- I am using the standard additive cyclic model `Z/990Z`; translate-equivalent difference sets are identified for contraction arguments.
- I am treating multiplier normalization only on quotients where `t - 1` is invertible, so the fixed-point normalization is justified there.
- The local packet names multiplier and quotient-contraction arguments as the intended first-line route; I am not assuming any unpublished stronger classification theorem.

## approach_A
Structural / invariant route: use multiplier-fixed contractions on quotients coprime to a prime divisor of `n`, then solve the resulting orbit equations exactly.

1. Mod `11`: because `3,5 | n` and both are coprime to `11`, the contracted image on `Z/11Z` is multiplier-invariant under the order-`5` subgroup of `(Z/11Z)^×`. After translation, the coefficients must have the form
   `x = (a ; b on QR ; c on NQR)`,
   so `a + 5b + 5c = 345` and `a^2 + 5b^2 + 5c^2 = 11025`.
   Solving gives exactly five possible profiles:
   `(45,30,30)`, `(40,34,27)`, `(30,36,27)`, `(25,36,28)`, `(20,35,30)`,
   up to swapping the two size-`5` orbits.

2. Mod `9`: because `5 | n` and `gcd(5,9)=1`, after translation the coefficients are constant on the `×5`-orbits `{0}`, `{3,6}`, and the six units. Writing these as `(a ; b on units ; c on {3,6})`, the Fourier condition for primitive order-`9` characters gives `a - c = ±15`, and the group-ring equations force exactly two profiles:
   `(45,40,30)` and `(25,40,40)`.

3. Mod `5`: because `3 | n` and `gcd(3,5)=1`, after translation the coefficients are constant on `{0}` and the four nonzero residues. Writing `(a ; b on nonzero)`, primitive order-`5` characters give `a - b = ±15`, and the contracted equations force exactly two profiles:
   `(81,66)` and `(57,72)`.

The hope is that these local profiles are too rigid to coexist in a common lift, especially when combined on a composite quotient such as `45` or `99`.

## approach_B
Construction / contradiction route: assume a cyclic difference set exists and try to lift the quotient profiles compatibly through Chinese-remainder layers.

1. Any putative `D` induces a `45`-class count vector with entries in `[0,22]`, row sums matching one of the two mod-`5` profiles and column sums matching one of the two mod-`9` profiles (up to a common translation choice).
2. The same `45`-class vector must satisfy `Σ x_r^2 = 2865` and every nonprincipal Fourier coefficient on `Z/45Z` must again have modulus `15`.
3. If no such `45`-class vector exists, that is already a rigorous nonexistence proof for the full cyclic case.
4. If `45` still leaves possibilities, repeat the same bounded lift test on `99` using the mod-`9` and mod-`11` profile theorems. Because the kernel over `99` has size `10`, the counts are small, and orbit rigidity may close the contradiction.

This is still theorem-facing, not a search-heavy fallback: the finite check is only over already-proved quotient profiles, not over subsets of `C_990`.

## lemma_graph
Lemma skeleton now visible:

1. `L1` Contracted equations: every quotient count vector satisfies the standard sum / sum-of-squares / autocorrelation identities.
2. `L2` Mod-`11` multiplier lemma: after translation, the mod-`11` contraction is constant on `{0}`, quadratic residues, and nonresidues.
3. `L3` Mod-`11` profile classification: only five integer triples from `L2` satisfy the contracted equations.
4. `L4` Mod-`9` multiplier lemma: after translation, the mod-`9` contraction is constant on `{0}`, `{3,6}`, and the six units.
5. `L5` Mod-`9` profile classification: only two integer triples satisfy the order-`9` Fourier and contracted equations.
6. `L6` Mod-`5` profile classification: only two integer pairs satisfy the order-`5` Fourier and contracted equations.
7. `L7` Composite-lift obstruction candidate: no `45`- or `99`-class lift can realize these local profiles while keeping all nonprincipal Fourier coefficients of modulus `15`.
8. Title theorem if `L7` closes: `C_990` has no `(990,345,120)` difference set.

## chosen_plan
Best current path: push `L7` first on the smallest composite quotient that still couples independent local information.

- First target: `Z/45Z`, because the mod-`5` and mod-`9` profile theorems are already exact and the kernel size is only `22`.
- If `Z/45Z` still admits a feasible count vector, move to `Z/99Z` to couple the sharp mod-`11` classification with the mod-`9` classification.
- Only use minimal code as a bounded consistency checker for these quotient lifts.
- Stop condition: either derive a clean contradiction, or isolate the exact surviving quotient profiles and record them as the strongest theorem slice reached.

Outcome of the chosen plan:

- The `mod 99` route was executed first because `×5` gives a clean orbit decomposition there.
- When that still left exact candidates, I ran the parallel `mod 55` route with `×3`.
- I then tested whether the surviving `mod 99` and `mod 55` candidates could coexist inside a `mod 495` occupancy table with entries in `{0,1,2}`.
- This did not yield a contradiction, so the current solve stops at a sharpened structural slice rather than a full nonexistence proof.

## self_checks
- Check 1: the target statement is locked to the cyclic slice only; I am not claiming anything about noncyclic groups of order `990`.
- Check 2: every multiplier-normalization step has been restricted to quotients where `t-1` is invertible.
- Check 3: the mod-`11`, mod-`9`, and mod-`5` profile lists come from exact integer equations, not heuristic numerics.
- Check 4: no brute-force subset search has been used or planned.
- Check 5 after code: the `mod 99` finite search was only over the `×5`-orbit quotient variables and exact Fourier constraints on `Z/99Z`.
- Check 6 after code: the `mod 55` finite search was only over the `×3`-orbit quotient variables and exact Fourier constraints on `Z/55Z`.
- Check 7 after code: the failed `mod 495` obstruction is a real negative result for this path, not a missing implementation detail; both marginal compatibility and the exact `120` double-occupancy count remained feasible.

## code_used
Yes. Only bounded exact Python checks were used, all justified by the prior quotient-profile reduction:

1. `mod 99` orbit-variable enumeration under `×5`, with exact verification of all nonprincipal Fourier coefficients on `Z/99Z`;
2. `mod 55` orbit-variable enumeration under `×3`, with exact verification of all nonprincipal Fourier coefficients on `Z/55Z`;
3. `mod 495` CRT-slice compatibility checks between the surviving `mod 99` and `mod 55` candidates, including an exact check that the kernel-`2` occupancy count `(# of 2's) = 120` remains achievable.

No SAT / ILP / CP-SAT / subset brute force on `C_990` was used.

## result
Exact structural gain:

- Mod `5`: exactly two possible translated profiles.
- Mod `9`: exactly two possible translated profiles.
- Mod `11`: exactly five possible translated orbit-profiles.
- Mod `99`: after enforcing the `×5` orbit structure and the full nonprincipal Fourier condition on `Z/99Z`, only `12` orbit-level contractions survive.
- Mod `55`: after enforcing the `×3` orbit structure and the full nonprincipal Fourier condition on `Z/55Z`, only `18` orbit-level contractions survive.

Negative solve result:

- The surviving `mod 99` and `mod 55` contractions are still mutually compatible at the `mod 495` occupancy-table level.
- In particular, the kernel-`2` contraction can still realize the exact required count of `120` doubled residues and `105` single residues.
- Therefore the present multiplier-and-contraction package does **not** yet prove nonexistence for the cyclic `(990,345,120)` case.

Honest current verdict: strong finite quotient reduction, but no theorem closure.

## family_affinity
Strong affinity with cyclic residual-case elimination by multiplier-orbit and quotient-contraction arguments. The present packet is not trying to build a broad family theorem; it is using the standard family toolkit to close one named residual row.

## generalization_signal
Moderate. The exact profile-classification method should transfer to nearby residual cyclic cases whose `n = k - λ` has only a few prime divisors and where one can find small quotients with invertible `t-1` for numerical multipliers.

## proof_template_reuse
Reusable template:

1. choose a quotient `Q` coprime to a prime divisor of `n`,
2. normalize by a multiplier with `t-1` invertible on `Q`,
3. classify orbit-constant quotient profiles using Fourier modulus `|χ(D)| = sqrt(n)`,
4. combine several such profiles on a composite quotient to force incompatibility.

## candidate_theorem_slice
If `D ⊂ C_990` were a `(990,345,120)` difference set, then after suitable translation its quotient profiles must lie in the following exact lists:

- mod `5`: `(81,66)` or `(57,72)`,
- mod `9`: `(45,40,30)` or `(25,40,40)`,
- mod `11`: one of `(45,30,30)`, `(40,34,27)`, `(30,36,27)`, `(25,36,28)`, `(20,35,30)` up to swapping the two size-`5` orbits.

Stronger finite slice from the bounded checks:

- only `12` fully Fourier-valid `mod 99` orbit contractions survive;
- only `18` fully Fourier-valid `mod 55` orbit contractions survive.

This is a real theorem slice and the strongest exact structure currently established.

## smallest_param_shift_to_test
The best next parameter shifts, if this instance resists closure, are other cyclic cases with the same square `n = 225` or with quotient-friendly prime factors where the same multiplier-normalization works on mod `5`, `9`, or `11` layers.

## why_this_is_or_is_not_publishable
If the nonexistence theorem closes, it is already paper-shaped: the exact title theorem is fixed, the frontier hook is already source-anchored, and the remaining packaging work is small.

At the current partial stage, it is not yet publishable. The quotient classifications are sharp and finite, but they still stop short of the title theorem. The current packet is closer to a structural appendix than to a micro-paper unless the remaining `mod 495` / full odd-part Fourier obstruction closes.

## paper_shape_support
What would make the result paper-shaped, beyond the main closure, is small and explicit:

- a clean composite-quotient obstruction theorem,
- one short corollary or boundary remark explaining why the noncyclic `990` row is unaffected,
- a compact paragraph tying the obstruction back to Gordon's residual cyclic table.

Immediate natural corollary if the main claim closes: the 2019 small-open cyclic list loses the `(990,345,120,225)` row while the separately listed noncyclic `990` row remains logically distinct.

Minimal remaining packaging work if the main claim ever closes from this route:

- compress the quotient-profile lemmas into a short preliminaries section,
- present the decisive odd-part obstruction cleanly,
- add one paragraph explaining why the argument is genuinely cyclic and does not settle the noncyclic `990` row.

## boundary_remark
The present quotient arguments visibly use cyclicity and multiplier normalization. Even a full cyclic nonexistence proof here would not by itself settle the separate noncyclic order-`990` residual row.

One natural boundary remark already visible now: the quotient package is strong enough to force finite candidate lists on `mod 55` and `mod 99`, but not strong enough by itself to eliminate every compatible odd-part occupancy pattern.

## likely_failure_points
Most likely technical failure point: the local quotient profiles may still admit a composite lift, in which case the current argument becomes a structural slice rather than a closure.

Secondary risk: a simultaneous translation normalization across multiple quotients may need to be handled more carefully than the single-quotient statements.

Observed failure point in this run: even after exact Fourier checks on `mod 55` and `mod 99`, the lift to kernel `2` still leaves room. The missing ingredient is not another easy local profile theorem; it is a genuinely global odd-part obstruction.

## what_verify_should_check
Verify should check:

- the exact algebra producing the five mod-`11` profiles,
- the primitive-character derivations `a-c = ±15` on mod `9` and `a-b = ±15` on mod `5`,
- that the multiplier-normalization assumptions are only used where justified,
- the exact bounded-search counts: `12` surviving `mod 99` contractions and `18` surviving `mod 55` contractions,
- the CRT compatibility computation on `mod 495`, including the fact that `120` doubled residues remain achievable,
- if a later contradiction is claimed, that it is genuinely quotient-level exact and not an artifact of an overfixed translation gauge.
