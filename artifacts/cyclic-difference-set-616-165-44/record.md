# Solve Record: Does the cyclic group C_616 admit a (616,165,44)-difference set?

- slug: `cyclic-difference-set-616-165-44`
- working_packet: `artifacts/cyclic-difference-set-616-165-44/working_packet.md`

## statement_lock
Locked target: determine whether there exists a subset D of Z/616Z of size 165 such that every nonzero group element occurs exactly 44 times as an ordered difference x-y with x,y in D.

Equivalent title theorem if closed: "The cyclic group C_616 does not admit a (616,165,44)-difference set" or "The cyclic group C_616 admits a (616,165,44)-difference set."

Micro-paper test at the solve stage: a decisive existence or nonexistence proof would already be about 70-90% of a paper, because the family anchor and literature stop line are already in the packet.

## definitions
Write n = k-lambda = 121 = 11^2 and v = 616 = 56*11.

For a quotient of size m obtained from a subgroup of size s = v/m, let c_0,...,c_{m-1} be the intersection counts of D with the m cosets. Then:

- sum_i c_i = k = 165
- sum_i c_i^2 = k + lambda(s-1)
- for each nonzero t in Z/mZ, sum_i c_i c_{i-t} = lambda s

Two contractions are central here.

- Mod 11 contraction: 11 counts a_j in [0,56], with sum a_j = 165 and nontrivial quotient-character sums of absolute value 11.
- Mod 56 contraction: 56 counts b_i in [0,11], with sum b_i = 165, sum b_i^2 = 605, and off-zero periodic autocorrelation 484.

It is convenient on the 56-side to write x_i = b_i - 3. Then:

- sum_i x_i = -3
- sum_i x_i^2 = 119
- for t != 0, sum_i x_i x_{i-t} = -2
- every nontrivial Fourier coefficient of x has squared magnitude 121

Ambiguities / conventions:

- I treat the group additively as Z/616Z.
- "Contract modulo 11" means pass to the quotient of size 11, so each quotient class has size 56.
- "Contract modulo 56" means pass to the quotient of size 56, so each quotient class has size 11.
- The local packet suggests, but does not reprove, a multiplier-fixed orbit constraint for the 56-quotient coming from the n = 11^2 structure.

## approach_A
Structural / invariant route:

1. Use the quotient of size 11. Let a_0,...,a_10 be the 11 coset counts.
2. Since every nonprincipal character of the quotient is also a nonprincipal character of the full cyclic group, each nontrivial Fourier coefficient of a has absolute value 11.
3. Subtract the mean 15: set y_j = a_j - 15. Then sum_j y_j = 0 and each nontrivial Fourier coefficient of y still has absolute value 11.
4. In Q(zeta_11), the prime 11 is totally ramified. Because Y_r * conjugate(Y_r) = 121 for each nontrivial Fourier coefficient Y_r, each Y_r is divisible by 11 as an algebraic integer, so Y_r / 11 is an algebraic integer whose Galois conjugates all have absolute value 1.
5. By Kronecker, Y_r / 11 is a root of unity. This forces the nontrivial spectrum to be a single monomial orbit, hence y is, up to cyclic shift and sign, either (10,-1,...,-1) or (-10,1,...,1).
6. Therefore, up to translation, the mod-11 class sizes are forced to be either (25,14,14,14,14,14,14,14,14,14,14) or (5,16,16,16,16,16,16,16,16,16,16).

This is a genuine theorem slice: any cyclic (616,165,44) difference set would have an extremely rigid distribution modulo 11.

## approach_B
Construction / extremal / contradiction route:

1. Use the quotient of size 56. Let b_i in [0,11] be the 56 coset counts.
2. The contracted equations give sum b_i = 165, sum b_i^2 = 605, and off-zero correlations 484.
3. After centering with x_i = b_i - 3, we get a length-56 integer sequence with sum -3, square-sum 119, and two-level periodic autocorrelation: 119 at shift 0 and -2 at every nonzero shift.
4. The packet's recommended first attack is to combine this with the standard multiplier-fixed orbit constraint on the quotient by 56 induced by the 11^2 structure. Under multiplier 11 on Z/56Z, the 56 coordinates collapse into a small number of orbits.
5. If the orbit-constant reduced system has no integer solution, that would give a clean nonexistence proof candidate. If it has solutions, those solutions still provide a sharply reduced search surface and expose where the obstruction must live.

This route is contradiction-oriented and is the best available path toward a paper-shaped nonexistence theorem.

## lemma_graph
Lemma graph / proof skeleton:

1. Difference-set assumption on Z/616Z.
2. Quotient-character lemma: every nonprincipal character on any quotient of Z/616Z evaluates on D with absolute value 11.
3. Mod-11 contraction lemma: the 11 quotient counts a_j satisfy the rigid dichotomy {25,14^10} or {5,16^10}, up to cyclic shift.
4. Mod-56 contraction lemma: the centered 56-sequence x has sum -3 and off-zero autocorrelation -2.
5. Multiplier-orbit reduction on Z/56Z under multiplication by 11: the 56 variables reduce to orbit variables.
6. Reduced integer system:
   - linear sum condition
   - quadratic energy condition
   - reduced correlation conditions
   - bounds 0 <= b_i <= 11
7. Either:
   - contradiction, giving nonexistence, or
   - a very small family of survivors to inspect against the mod-11 slice.

## chosen_plan
Best path after the first pass: make the mod-56 multiplier route primary, and keep the mod-11 rigidity as a supporting slice rather than the main contradiction.

Candidate proof strategy:

1. Let b_0,...,b_55 be the quotient-56 coset counts.
2. Use the standard contracted-multiplier theorem indicated by the packet: multiplication by 11 acts affinely on the contracted count vector, so there is a shift g mod 56 with b_i = b_{11i+g}.
3. Split into parity classes for g.
4. If g is even, translate to kill g because 10u runs through every even residue mod 56. Then b_i = b_{11i}, and reducing mod 4 forces the two odd mod-4 class totals to be equal.
5. Independently, the order-2 and order-4 character equations force the mod-4 class totals to be 44, 44, 44, 33 up to translation, so the odd classes are unequal. Contradiction.
6. If g is odd, translate to g = 1. The affine map i -> 11i + 1 has only orbits of sizes 4 and 12 on Z/56Z, so any orbit-constant count vector has total sum divisible by 4. But sum_i b_i = 165 is not divisible by 4. Contradiction.

This gives a full candidate nonexistence proof, modulo verification of the exact multiplier theorem hypotheses.

## self_checks
- Self-check after statement lock: the intended statement stayed exact; no concept drift into a broader Ryser program.
- Self-check after definitions: both contractions were derived from the standard coset-pair counting identity; no external computation used.
- Self-check after Approach A: the claimed rigid mod-11 shape is strong but depends on the cyclotomic divisibility step; this is a place for later verification scrutiny.
- Self-check after Approach B: the multiplier-fixed part is presently treated as the standard sourced tool indicated by the packet, not yet rederived locally.
- Self-check after the even-g contradiction: the only real external dependency is the precise contracted-multiplier theorem statement; the mod-4 character calculation itself is elementary.
- Self-check after the odd-g contradiction: once g is normalized to 1, the orbit-size divisibility argument is elementary and does not depend on search.

## code_used
A tiny bounded Python checker was used only as corroboration for the affine-orbit reductions. It confirmed:

- odd affine class g = 1 has no orbit-constant count vector even at the basic sum / square level
- the even affine class test with the exact mod-8 split also has no full contracted solution

The current candidate proof does not need those computations in its final logical spine; the odd case already dies by orbit-size divisibility and the even case by the mod-4 contradiction.

## result
Candidate disproof:

Assume D is a cyclic (616,165,44) difference set and let b_0,...,b_55 be the counts on the 56 cosets of the subgroup of order 11.

Step 1. Elementary mod-4 contraction.

Let c_r = sum_{i congruent r mod 4} b_i, so c_0 + c_1 + c_2 + c_3 = 165.

- The order-2 quotient character gives |(c_0 + c_2) - (c_1 + c_3)| = 11, hence after a cyclic relabeling:
  - c_0 + c_2 = 88
  - c_1 + c_3 = 77
- The order-4 quotient character gives
  |(c_0 - c_2) + i(c_1 - c_3)| = 11,
  so
  (c_0 - c_2)^2 + (c_1 - c_3)^2 = 121.
- Here c_0 - c_2 is even and c_1 - c_3 is odd, so the only possibility is
  - c_0 - c_2 = 0
  - |c_1 - c_3| = 11.

Therefore

- c_0 = c_2 = 44
- {c_1, c_3} = {33,44}.

In particular, the two odd mod-4 classes are unequal.

Step 2. Affine multiplier reduction on the quotient of size 56.

Using the standard contracted-multiplier tool flagged in the packet for the 11^2 case, there exists g mod 56 such that

- b_i = b_{11i+g} for all i mod 56.

Case 2a. g even.

Because 10u runs through every even residue mod 56, we can translate the original difference set so that g becomes 0. Then

- b_i = b_{11i}.

Reducing mod 4, multiplication by 11 is multiplication by -1, so the map swaps the odd residue classes 1 and 3. Hence it forces

- c_1 = c_3,

contradicting the mod-4 calculation above.

Case 2b. g odd.

Again by translation, it is enough to take g = 1. Consider the affine map

- f(i) = 11i + 1 mod 56.

On Z/8Z this is r -> 3r + 1, which has two 4-cycles:

- 0 -> 1 -> 4 -> 5 -> 0
- 2 -> 7 -> 6 -> 3 -> 2.

On Z/7Z this is s -> 4s + 1, which has one fixed point and two 3-cycles. Hence every orbit on

- Z/56Z ~= Z/8Z x Z/7Z

has size lcm(4,1) = 4 or lcm(4,3) = 12. Since b is constant on f-orbits, each orbit contributes a multiple of 4 to sum_i b_i. Therefore

- sum_i b_i is divisible by 4,

contradicting sum_i b_i = 165.

Conclusion.

Both affine-multiplier cases contradict the quotient-56 contraction. This yields a candidate theorem:

"The cyclic group C_616 admits no (616,165,44)-difference set."

Why this matters for the micro-paper lane:

- If the multiplier hypothesis checks exactly as expected in verification, this is already very close to a paper-shaped nonexistence note.
- The exact title theorem is already visible.
- Minimal remaining packaging work is to formalize the multiplier citation, write the mod-4 character calculation cleanly, and add the Gordon open-row framing.

Immediate corollary / remark:

- Any hypothetical cyclic (616,165,44) construction would have to evade both the odd affine orbit divisibility and the even affine mod-4 symmetry, so the standard 11^2 contracted-multiplier lane already blocks it completely.

What part of the argument scales:

- the odd-affine orbit divisibility mechanism whenever the induced map on a small quotient forces all orbit sizes to share a common factor incompatible with k
- the even-affine normalization step whenever t-1 hits the relevant shift class
- the mod-4 character split whenever a single order-4 quotient already makes one residue class exceptional

What does not obviously scale:

- the exact mod-4 contradiction uses the special k = 165 arithmetic of this row
- the reduction to multiplier 11 on the 56-quotient is tied to the n = 11^2 structure

Suggested theorem slice if a narrower writeup is preferred:

- the mod-4 lemma by itself
- or the odd-affine orbit-divisibility obstruction on the quotient of size 56

Best next parameter shifts if this needs family follow-up:

- inspect the other small cyclic Ryser rows with the same prime-square n structure
- specifically ask whether their contracted affine multiplier maps also force orbit sizes with a forbidden common divisor or a small mod-m symmetry contradiction

Package assessment:

- this is no longer just an instance-level witness hunt
- it is a candidate full theorem for the exact row
- pending verification of the multiplier theorem hypotheses, it is much closer to paper-shaped than the earlier structural slice

## family_affinity
Strong family affinity: this sits exactly in the cyclic Ryser-conjecture lane with n = 11^2 and gcd(v,n) = 11, and the candidate proof uses the expected contraction-plus-multiplier toolkit in the most local exact-case form.

## generalization_signal
Moderate-to-strong generalization signal: the argument suggests a reusable two-branch template for prime-square n cases:

- affine-multiplier odd branch killed by orbit-size divisibility
- affine-multiplier even branch reduced to a small-modulus character contradiction after normalization

## proof_template_reuse
Reusable proof template:

1. Contract to a prime quotient q where all nonprincipal quotient-character values have absolute value p.
2. Center by the integer mean when possible.
3. Use ramification in Q(zeta_q) plus Kronecker to force the quotient count vector into a tiny explicit family.
4. Feed that rigid slice, or a simpler mod-m contraction, into a second contraction with multiplier or orbit constraints.
5. Split the affine multiplier cases by the shift class and kill them separately: normalize the removable shift class, and use orbit-size divisibility on the non-removable class.

Here the orbit-divisibility / normalization split looks especially reusable.

## candidate_theorem_slice
Primary candidate theorem:

"The cyclic group C_616 admits no (616,165,44)-difference set."

Smallest supporting slice if verification wants the proof split:

"For any putative cyclic (616,165,44) difference set, the counts on residue classes mod 4 are 44,44,44,33 up to translation."

## smallest_param_shift_to_test
Best next parameter shifts, if verification wants family context rather than more work on this row:

- other small cyclic Ryser rows with n = p^2 and a quotient where the affine multiplier map has orbit sizes sharing a nontrivial common divisor
- rows where an even shift class can be normalized away and a mod-4 or mod-8 contraction can force an asymmetric residue pattern

For solve itself, I do not recommend leaving this row until the multiplier hypothesis is checked.

## why_this_is_or_is_not_publishable
If verification confirms the multiplier step exactly as used here, then this is likely 70-90% of a paper. The title theorem is already exact, the contradiction is short, and the family framing is already supplied by the packet.

Minimal remaining packaging work:

- verify the exact contracted-multiplier theorem statement and hypotheses
- write the mod-4 character calculation as a short lemma
- explain the odd-shift orbit divisibility on Z/8 x Z/7
- add the short Ryser-case framing paragraph

At solve time I still treat the result conservatively as a candidate theorem, not a finished publication packet.

## paper_shape_support
Paper-shape support already visible:

- exact title theorem is locked
- the row is already isolated by the packet's frontier basis
- the main contradiction is short and exact-case sized
- the mod-4 count lemma is a natural first lemma in a short note
- one immediate boundary remark is already visible: the affine multiplier action leaves no viable quotient-56 symmetry class

Immediate corollary / remark if the main claim closes:

- the proof would show that Gordon's open row is blocked by standard cyclic-contraction arithmetic alone; no large search or feeder ladder is needed.

## boundary_remark
Boundary remark: the current package is still an exact-instance theorem candidate, not yet a broader family theorem. The contradiction is compact and promising for the micro-paper lane, but its cleanest form still appears tied to the 56-side arithmetic of this row.

## likely_failure_points
- The main load-bearing issue is the exact contracted-multiplier theorem statement and whether it indeed yields the affine invariance b_i = b_{11i+g} on the 56-quotient for this row.
- The mod-4 character calculation should be checked carefully for convention mismatches, but it is elementary and unlikely to be the real risk.
- The mod-11 rigidity slice is now secondary; if its cyclotomic step is shaky, it does not damage the main nonexistence route.

## what_verify_should_check
- Verify that the standard contracted-multiplier theorem cited in the packet really yields an affine 11-action on the quotient-56 count vector for this exact parameter set.
- Verify the normalization step: when g is even, 10u = -g mod 56 is always solvable and translation preserves the contracted equations as used.
- Verify the mod-4 calculation independently:
  - parity block sums are 88 and 77
  - the order-4 character forces c_0 = c_2 and {c_1,c_3} = {33,44}
- Optionally rerun the tiny checker as corroboration, but the intended final proof should not depend on computation.

## verify_rediscovery
Bounded PASS 1 found prior art settling the exact intended statement.

- Baumert and Gordon, "Cyclic Difference Sets with k <= 150" (2003), Table 4, explicitly lists `(616,165,44,121)` under "Cases eliminated by Theorem 3.1."
- The same paper also notes the later Leung-Ma-Schmidt prime-power-order nonexistence theorem for cyclic difference sets with `n = p^a`, `p > 3`, and `(n,v) > 1`; this general criterion also covers `n = 121 = 11^2` and `gcd(616,121) = 11`.
- The 2019 La Jolla slide used in curation is therefore stale or at least inconsistent with earlier published nonexistence results for this exact tuple.

Verdict from PASS 1: the exact cyclic `(616,165,44)` row is already settled in prior art, so this run is a rediscovery rather than a frontier solve.

## verify_faithfulness
The solver stayed on the intended theorem. The claimed conclusion, "the cyclic group `C_616` admits no `(616,165,44)` difference set," is the exact negation of the intended existence question, so there is no quantifier drift, proxy-statement drift, or family drift.

The problem is not faithfulness to the target statement. The problem is novelty: the exact target appears already solved in prior art.

## verify_proof
No arithmetic or logical error was found in the local contradiction argument itself.

- The mod-4 contraction lemma is internally consistent: from the order-2 and order-4 quotient character constraints one gets mod-4 class totals `44,44,44,33` up to translation.
- The affine normalization argument is coherent: translating by `u` changes the affine shift by `g -> g - 10u`, so even `g` can be normalized to `0` and odd `g` to `1`.
- The odd-shift branch is valid once `b_i = b_{11i+1}` is granted: all affine orbits on `Z/56Z` have size `4` or `12`, hence every orbit contribution is divisible by `4`, contradicting total sum `165`.

The first real load-bearing gap from the solve record was the unverified multiplier citation. PASS 1 removed that gap by locating prior art strong enough to settle the exact row anyway. So the proof is best treated as an independent rederivation of a known nonexistence result, not as a new theorem.

## verify_adversarial
No durable checker file was preserved in the artifact directory, so there was nothing canonical to rerun.

I did rerun the smallest local arithmetic sanity checks:

- for `f(i) = 11i + 1 mod 56`, the orbit sizes are exactly `4` and `12`, so every orbit contribution is a multiple of `4`
- for `g = 0`, multiplication by `11 mod 56` acts as `-1 mod 4`, swapping residue classes `1` and `3`

Those checks support the local contradiction argument. They do not rescue novelty, because PASS 1 already established rediscovery.

## verify_theorem_worthiness
Exactness: yes, the local claim addresses the exact intended statement.

Novelty: no. The exact tuple appears already eliminated in published prior art, so this does not support a frontier micro-paper.

Reproducibility: medium-high. The local argument is compact and mostly elementary once the multiplier input is granted, and the orbit arithmetic is easy to check.

Lean readiness: no. Lean is not the shortest remaining path, because the main blocker is not proof rigor but lack of novelty.

Paper leverage: effectively zero for a new note. If correct and Lean-sealed, this would still not constitute a publishable frontier packet because the title theorem is already known.

Direct answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No, because the exact result is already in prior art.
- What percentage of a paper would one solve already provide? `0%` for the frontier lane; at best it would be an independent rederivation of a known row.
- What title theorem is actually visible? "The cyclic group `C_616` does not admit a `(616,165,44)` difference set."
- What part of the argument scales? The affine-orbit divisibility and small-modulus contraction template may scale to other prime-square rows.
- What part clearly does not? The publication claim does not scale here, because this exact row is already settled.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? Neither. The correct publication-facing label for this run is `REDISCOVERY`.

## verify_verdict
`REDISCOVERY`

Reason: PASS 1 located prior art indicating that the exact cyclic `(616,165,44)` difference-set problem was already settled as a nonexistence case before this run. The local solve record is therefore an exact rediscovery, not a frontier result.

## minimal_repair_if_any
No tiny mathematical repair is needed to salvage the local proof as a proof of nonexistence.

The required repair is procedural: archive this slug as a rediscovery and refresh the curation basis so the stale 2019 slide does not keep this exact row in the live micro-paper lane.
