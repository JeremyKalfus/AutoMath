# Solve Record: Does the abelian group C_3 x C_207 admit a (621,156,39)-difference set?

- slug: `abelian-difference-set-621-156-39-group-3-207`
- working_packet: `artifacts/abelian-difference-set-621-156-39-group-3-207/working_packet.md`

## statement_lock
Locked statement: determine whether there exists a `(621,156,39)` difference set in
`G = C_3 x C_207`.

For the solve attempt I write
`G = P x Q` with `P ~= C_3 x C_9` and `Q ~= C_23`, using additive notation. A subset
`D subseteq G` of size `156` is a `(621,156,39)` difference set if every nonzero group
element occurs exactly `39` times as a difference of ordered pairs from `D`.

The exact title theorem, if this closes, is:

`The abelian group C_3 x C_207 admits no (621,156,39) difference set.`

## definitions
- Parameters: `v = 621`, `k = 156`, `lambda = 39`, `n = k - lambda = 117 = 3^2 * 13`.
- The prime `13` is coprime to `v`, so the standard numerical-multiplier theorem is the
  natural first tool.
- Let `alpha` be the endomorphism `x -> 13x` on `G`. On `P ~= C_3 x C_9`, this is
  multiplication by `(1,4)`; on `Q ~= C_23`, this is multiplication by `13`.
- Since `13` has order `11` modulo `23`, the action on `Q` has one fixed point `0` and
  two nonzero orbits of size `11`.
- Write the fiber over `q in Q` as
  `D_q = { p in P : (p,q) in D }`,
  with size `b_q = |D_q|`.
- For any character `chi` of `G`, a difference set satisfies
  `|chi(D)|^2 = n = 117` for every nonprincipal `chi`.

Ambiguities and conventions:

- I am assuming the standard multiplier theorem in the abelian setting: because `13 | n`
  and `gcd(13,621)=1`, one has `alpha(D) = D + g` for some `g in G`.
- I normalize only on the `Q` coordinate; this avoids the false stronger claim that one
  can always translate to make `D` globally `13`-fixed.
- The working packet says `C_3 x C_207 = C_3^3 x C_23`; that decomposition is not
  correct. The correct Sylow-`3` part is `C_3 x C_9`.

## approach_A
Structural / invariant approach:

1. Use the `13`-multiplier to organize the `23` quotient into one fixed fiber and two
   `11`-cycles.
2. Push `D` to `Q ~= C_23`; the fiber sizes `b_q` must be constant on the two
   `11`-cycles, so the quotient count pattern is `(x ; y^11 ; z^11)`.
3. Use the difference-set Fourier equations on `Q` to solve for `(x,y,z)`.
4. Then inspect order-`3` characters on `P ~= C_3 x C_9`. After the multiplier
   normalization, their fiberwise character sums are also constant on the two
   `11`-cycles.
5. Parseval on `Q` turns that into a congruence obstruction modulo `11`, producing the
   contradiction.

Why this looks promising: it uses only the published multiplier hint (`13`) and the
exact group decomposition, so it is theorem-facing rather than search-heavy.

## approach_B
Construction / contradiction approach:

1. Treat the fibers `D_q subseteq P` as subsets of sizes `2`, `5`, or `9` if the quotient
   orbit count route succeeds.
2. Ask whether the internal ordered-difference counts inside `P` can sum to exactly `39`
   for every nonzero element of `P`.
3. Try to force a contradiction from the small fiber `|D_0| = 2` together with the
   repeated `11`-orbit structure on the other fibers.

Why I am not choosing this first: it seems to need more casework on subsets of
`C_3 x C_9`, while the character route compresses the same information into a single
divisibility obstruction.

## lemma_graph
Proof skeleton:

1. Multiplier normalization lemma:
   if `alpha(D) = D + (u,v)` with `alpha(q)=13q` on `Q`, translate by `(0,w)` with
   `12w = v` in `Q` to arrange `alpha(D) = D + (u,0)`.
2. Fiber orbit lemma:
   with that normalization, `D_{13q} = 4D_q + u`, hence the fiber sizes are constant on
   the two `11`-orbits of `Q^times`.
3. Quotient count lemma:
   write the fiber sizes as `(x ; y^11 ; z^11)`. From
   `sum b_q = 156`, `sum b_q^2 = 1170`, and one nonprincipal Fourier equation on `Q`,
   the only possibility is `x = 2` and `{y,z} = {5,9}`.
4. Order-`3` character transport lemma:
   for any nonprincipal order-`3` character `psi` of `P`, define
   `z_q = sum_{p in D_q} psi(p)`. Then `z_{13q} = psi(u) z_q`.
5. Small-fiber forcing lemma:
   if `psi(u) != 1`, then `z_q = 0` on both `11`-orbits, so
   `|sum_q z_q| = |z_0| <= |D_0| = 2`, contradicting
   `|sum_q z_q|^2 = 117`. Hence `psi(u)=1` for every such `psi`.
6. Final Parseval contradiction:
   then `z_q` is constant on each `11`-orbit, say `(c ; a^11 ; b^11)`, with
   `|c|^2 in {1,4}` because `|D_0|=2`.
   Parseval on `Q` gives `|c|^2 + 11|a|^2 + 11|b|^2 = 117`.
   But `|a|^2, |b|^2 in Z` for order-`3` character sums, so the left side is congruent to
   `|c|^2 mod 11`, while the right side is `117 congruent 7 mod 11`; neither
   `1` nor `4` is congruent to `7 mod 11`. Contradiction.

## chosen_plan
Chosen path: pursue Approach A to a full contradiction.

Self-imposed stop condition:

- Either complete the multiplier-plus-order-`3` character obstruction cleanly, or stop at
  the exact place where the normalization or quotient Fourier step fails.

Reason for choosing it:

- It directly targets the micro-paper theorem shape: one decisive nonexistence argument
  tied to the exact Table 2 row, with only light packaging left if correct.

## self_checks
Self-check after statement lock:

- The problem is still the exact `C_3 x C_207` row, not a broadened family claim.

Self-check after quotient setup:

- I corrected the Sylow-`3` decomposition to `C_3 x C_9`, which is essential because the
  order-`3` character argument lives on that exact structure.

Self-check after fiber-count computation:

- The count equations use only standard identities:
  `sum b_q = k = 156` and `sum b_q^2 = n + lambda|P| = 117 + 39*27 = 1170`.

Self-check after the final contradiction:

- The contradiction is not numerical noise; it is a residue-class obstruction modulo
  `11` coming from the unique small fixed fiber forced by the multiplier action.

## code_used
No code used.

I deliberately avoided a bounded search because the multiplier and character equations
already yield a direct contradiction candidate.

## result
Candidate rigorous result: nonexistence.

Detailed argument:

Assume for contradiction that `D subseteq G = P x Q` is a `(621,156,39)` difference set,
with `P ~= C_3 x C_9` and `Q ~= C_23`.

Because `13 | n = 117` and `gcd(13,621)=1`, the standard multiplier theorem gives
`alpha(D) = D + (u,v)` for some `(u,v) in P x Q`, where
`alpha(p,q) = (4p,13q)`.

Since multiplication by `12` is bijective on `Q ~= C_23`, choose `w in Q` with
`12w = v` and replace `D` by `D - (0,w)`. Then the new difference set still has the same
parameters and satisfies

`alpha(D) = D + (u,0)`.

For each `q in Q`, define the fiber `D_q subseteq P` and its size `b_q = |D_q|`.
The multiplier relation becomes

`D_{13q} = 4D_q + u`,

so `b_{13q} = b_q`. Since `13` has one fixed point `0` and two nonzero `11`-orbits on
`Q`, there are integers `x,y,z` such that the multiset of fiber sizes is

`(x ; y^11 ; z^11)`.

Now

`x + 11y + 11z = 156`

because `|D|=156`, and

`x^2 + 11y^2 + 11z^2 = 1170`

because pushing the group-ring equation to `Q` gives
`sum_q b_q^2 = n + lambda|P| = 117 + 39*27 = 1170`.

Also for every nonprincipal character `varphi` of `Q`,

`|sum_q b_q varphi(q)|^2 = 117`.

Let `O_0, O_1` be the two nonzero `13`-orbits in `Q`, and let
`eta_i = sum_{q in O_i} varphi(q)`. Since `O_0` and `O_1` are the two index-`2`
cyclotomic classes in `F_23^times`, the quadratic-period identities are

`eta_0 + eta_1 = -1`,
`eta_0 eta_1 = 6`.

Hence

`|x + y eta_0 + z eta_1|^2 = x^2 - x(y+z) - 11yz + 6(y^2+z^2) = 117`.

Solving the two size equations first gives the only integer possibilities

- `(x,y,z) = (2,5,9)` up to swapping `y,z`,
- `(x,y,z) = (13,3,10)` up to swapping `y,z`.

Substituting into the Fourier equation eliminates the second pair and leaves only

`x = 2`, `\{y,z\} = \{5,9\}`.

So the unique fixed fiber has size `|D_0| = 2`.

Now let `psi` be any nonprincipal order-`3` character of `P`, and define

`z_q = sum_{p in D_q} psi(p)`.

Because `psi(4p)=psi(p)` on `P` (the multiplier `4` acts trivially modulo `3`), the
fiber transport law becomes

`z_{13q} = psi(u) z_q`.

If `psi(u) != 1`, then going once around an `11`-cycle in `Q^times` gives

`z_q = psi(u)^{11} z_q = psi(u)^2 z_q`,

so `z_q = 0` on both nonzero `11`-orbits. Then

`(psi x 1_Q)(D) = sum_q z_q = z_0`,

but `|z_0| <= |D_0| = 2`, contradicting the difference-set character identity

`|(psi x 1_Q)(D)|^2 = 117`.

Therefore `psi(u)=1` for every nonprincipal order-`3` character `psi` of `P`.

Fix such a `psi`. Then `z_{13q}=z_q`, so `z_q` is constant on each nonzero `11`-orbit:

`(z_q) = (c ; a^11 ; b^11)`.

Because `|D_0| = 2`, the value `c` is the sum of two cube roots of unity, so

`|c|^2 in {1,4}`.

Now for every character `tau` of `Q`, the character `psi x tau` is nonprincipal on `G`,
so

`|(psi x tau)(D)|^2 = 117`.

Applying Parseval on `Q` to the sequence `q -> z_q` yields

`|c|^2 + 11|a|^2 + 11|b|^2 = 117`.

For an order-`3` character sum, squared magnitudes are integers, so
`|a|^2, |b|^2 in Z`. Therefore the left-hand side is congruent to `|c|^2` modulo `11`.
But `117 congruent 7 mod 11`, while `|c|^2` is either `1` or `4`. This is impossible.

Contradiction. Therefore no `(621,156,39)` difference set exists in `C_3 x C_207`.

Status of the result in this solve stage:

- mathematically, this is a clean nonexistence candidate proof;
- procedurally, it should still be treated as a solve-stage theorem candidate pending
  verification of the multiplier normalization and the quadratic-period step.

## family_affinity
Strong.

This sits exactly inside the abelian difference-set residual-row program: the argument is
not a one-off brute-force witness computation but a multiplier-plus-quotient obstruction
that explains why the specific `[3,207]` row fails.

A successful verify pass would still leave this as mostly an instance theorem, but it is
an instance with a named survey anchor and a clean family method.

## generalization_signal
Moderate.

What scales:

- The normalization on the prime quotient `C_p` when a multiplier has a large orbit on
  that quotient.
- The strategy "solve the fixed-fiber size first, then attack the small fixed fiber with a
  low-order character on the complementary Sylow part."

What does not obviously scale:

- The final contradiction uses the very specific congruence
  `117 - |c|^2 not divisible by 11` together with the forced fixed-fiber size `2`.
- The argument also leans on the order-`11` action of `13` on `C_23`, so it is not a
  general theorem for arbitrary residual rows.

## proof_template_reuse
Reusable template:

1. Split `G` as `P x C_p`.
2. Use a numerical multiplier whose action on `C_p` has few large orbits.
3. Normalize the `C_p` translation only.
4. Determine the quotient fiber-count pattern from the quotient Fourier equations.
5. Use a low-order character on `P` that is fixed by the multiplier on `P`.
6. Convert the orbit pattern into a Parseval divisibility contradiction.

This is a plausible reusable proof template for other residual rows where one quotient
prime and one small complementary Sylow character interact cleanly.

## candidate_theorem_slice
Suggested theorem slice:

`Let G = (C_3 x C_9) x C_23. There is no (621,156,39) difference set in G. More
precisely, the 13-multiplier forces the C_23-fiber counts to be (2;5^11;9^11) up to
orbit swap, and this is incompatible with the order-3 characters of C_3 x C_9.`

This slice is already theorem-shaped and is stronger than a bare "no witness found"
statement.

## smallest_param_shift_to_test
Best next parameter shifts:

1. Keep the same method on other residual rows where the natural multiplier yields a
   prime quotient with exactly two large nonzero orbits.
2. Test nearby rows whose complementary Sylow part still has a fixed low-order character
   under the multiplier action.

For this exact family, the most informative shift is not a small numerical perturbation
of `(621,156,39)` but another Table 2 row with the same multiplier-on-prime-quotient
geometry.

## why_this_is_or_is_not_publishable
If verified, this is close to publishable in the strict micro-paper lane.

- A successful solve here would already be about `77%` of a paper, consistent with the
  curation packet.
- The exact title theorem is already present.
- Minimal remaining packaging work would be:
  a short introduction tied to Gordon-Schmidt Table 2,
  a concise multiplier normalization lemma,
  the fiber-count proposition,
  and the final order-`3` character contradiction.

Why it is publishable if correct:

- it settles a named residual survey row exactly;
- the proof has a compact structural narrative, not just computation;
- the supporting slice `(2;5^11;9^11)` gives a natural internal proposition.

Why it might still fail publication if the proof breaks:

- if the multiplier normalization or the quadratic-period identity is mishandled, the
  result collapses back to an unverified instance attempt.

## paper_shape_support
What extra structure makes the result paper-shaped once the main claim closes:

- A standalone proposition on the forced `C_23` fiber-count distribution.
- One explicit lemma showing why order-`3` characters are the right complementary tool on
  `C_3 x C_9`.
- A short remark that the proof explains why the published multiplier filters stop one
  step short and how the extra character congruence finishes the row.

Immediate corollary / boundary remark:

- Any hypothetical difference set would have to realize the exact quotient profile
  `(2;5^11;9^11)` up to orbit swap, so ruling out that profile is already the decisive
  theorem-facing obstruction.

## boundary_remark
Boundary remark:

The argument looks instance-specific rather than broad-family exact. That is acceptable
for the micro-paper lane because the source literature already isolates this exact row as
paper-worthy. If verification finds a hidden general statement behind the same proof
pattern, that would be upside, not a requirement.

## likely_failure_points
Most likely places for failure:

1. The multiplier normalization must be stated carefully: only the `Q ~= C_23`
   translation is normalized away.
2. The identification of the two nonzero `13`-orbits in `Q` with the index-`2`
   cyclotomic classes must be checked cleanly.
3. The formula
   `|x + y eta_0 + z eta_1|^2 = x^2 - x(y+z) - 11yz + 6(y^2+z^2)`
   should be re-expanded line by line in verify.
4. The integrality claim for `|a|^2` and `|b|^2` should be checked explicitly from
   order-`3` character sums.

## what_verify_should_check
Verify should check:

1. The exact multiplier theorem hypothesis for the prime `13`.
2. The translation normalization `12w = v` on `C_23`.
3. The derivation of `sum_q b_q^2 = 1170`.
4. The elimination of `(13,3,10)` and `(13,10,3)` from the quotient Fourier equation.
5. The claim that `psi(4p)=psi(p)` for every order-`3` character on `C_3 x C_9`.
6. The implication `psi(u) != 1 => z_q = 0` on the two nonzero `11`-orbits.
7. The final Parseval congruence modulo `11`.

## verify_rediscovery
PASS 1: bounded rediscovery audit.

- Exact-instance searches on `(621,156,39)` together with `C_3 x C_207` and `difference set` did not surface a later construction, nonexistence theorem, or database page settling this exact row within the audit budget.
- Alternate-notation searches on `(621,156,39)` together with `[3,207]` and `Z_3 x Z_207` likewise did not produce a direct later settlement.
- The canonical-source lane still points back to Gordon-Schmidt Table 2 listing the exact row `(621,156,39)` in group `[3,207]` as open.
- A recent-status sweep on Gordon-facing pages did not expose a later paper or maintained-status entry settling the exact `[3,207]` row.
- Conservative prior-art verdict: no rediscovery was established within budget.

## verify_faithfulness
PASS 2: faithfulness.

- The intended statement is unconditional: determine whether `C_3 x C_207` admits a `(621,156,39)` difference set.
- The current solve record does not keep that exact theorem locked. It upgrades the packet's source hint "`13` is the multiplier-conjecture prime attached to this row" into the much stronger premise "the standard multiplier theorem gives `alpha(D) = D + (u,v)`."
- That is theorem drift. The working packet only justifies treating `13` as the natural multiplier-conjecture prime for the row; it does not itself certify an unconditional usable `13`-multiplier theorem for this exact instance.
- So the strongest source-faithful output from the current artifact is only a conditional variant:
  assuming a valid `13`-multiplier normalization for a hypothetical difference set, the quotient/character argument yields a contradiction.

## verify_proof
PASS 3: proof correctness.

First incorrect step:

- In `definitions` and again in `lemma_graph`, the proof assumes that `13 | n = 117` and `gcd(13,621)=1` are already enough to conclude `alpha(D) = D + (u,v)` for a hypothetical difference set.
- Within the bounded source support available to this run, that implication is not justified. The proof of the intended unconditional theorem therefore fails at its first load-bearing step.

Later arithmetic check:

- The record says the size equations alone allow both `(x,y,z) = (2,5,9)` and `(13,3,10)` up to swapping. That is false.
- Direct computation shows the system
  `x + 11y + 11z = 156`,
  `x^2 + 11y^2 + 11z^2 = 1170`
  has only `(2,5,9)` and `(2,9,5)` as integer solutions.
- This is a real mistake, but it is not the load-bearing failure. It actually strengthens the conditional orbit-count slice by making the Fourier elimination of `(13,3,10)` unnecessary.

Conditional residue after repairing the arithmetic:

- Granting a valid `13`-multiplier normalization, the internal quotient arithmetic survives this bounded check.
- The quadratic-period identities on `C_23` were rechecked numerically: `eta_0 + eta_1 = -1` and `eta_0 eta_1 = 6`.
- Under that conditional premise the quotient profile is forced to `(2;5^11;9^11)` up to orbit swap, and the final order-`3` Parseval congruence mod `11` still gives a contradiction.
- So the strongest defensible residue is a conditional nonexistence theorem slice, not the intended unconditional exact-row theorem.

## verify_adversarial
PASS 4: adversarial check.

- No checker or dedicated search code existed to rerun.
- I stress-tested the arithmetic claims directly with local Python.
- Those checks confirmed:
  only `(2,5,9)` up to swap solves the size equations;
  the quadratic-period product really is `6`;
  the Fourier magnitude for `(2,5,9)` is `117`;
  sums of two cube roots of unity have squared modulus only `1` or `4`.
- This adversarial pass breaks the record's claim that `(13,3,10)` is a genuine competing profile, but it does not break the repaired conditional contradiction.
- Adversarial verdict: the packet does not survive as an unconditional theorem, but the internal arithmetic of the conditional multiplier slice survives bounded stress testing.

## verify_theorem_worthiness
PASS 5: theorem worthiness.

- Exactness: the intended exact theorem is not verified. The current packet proves at most a conditional obstruction that still depends on an unsupported multiplier bridge.
- Novelty: no rediscovery was established within the bounded audit.
- Reproducibility: the quotient/character computations are reproducible; the unconditional theorem is not, because the source-faithful multiplier premise is missing.
- Lean readiness: no. Lean would currently formalize only a conditional slice, not a sealed publication packet for the selected exact row.
- Paper leverage: low in the verified state. The target row remains micro-paper eligible in principle, but the surviving result is not yet title-theorem strength.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No. In its verified form it is still only a conditional lemma package.
- What percentage of the paper would one solve already provide? About `30%` at best in the current repaired form, not the `70%` to `90%` target.
- What title theorem is actually visible? At most: assuming a valid `13`-multiplier normalization, no `(621,156,39)` difference set exists in `C_3 x C_207`.
- What part of the argument scales? The prime-quotient orbit decomposition, Gaussian-period bookkeeping, and low-order-character congruence template.
- What part clearly does not? The unsupported bridge from the survey's `MC prime` cue to an unconditional multiplier theorem for this exact row.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? `NONE`. The current verified residue is not yet a paper-shaped unconditional theorem packet.

## verify_verdict

- `verify_verdict = VARIANT`
- `classification = VARIANT`
- `confidence = high`
- `publication_status = NONE`
- `lean_ready = false`
- `next_action = downgrade the claim to the conditional 13-multiplier obstruction and return to solve for either a source-backed unconditional multiplier theorem or a multiplier-free contradiction.`

## minimal_repair_if_any
Tiny conservative repair available:

- Remove the unconditional nonexistence claim.
- Retain only the conditional slice:
  `Assuming a valid 13-multiplier normalization for a hypothetical (621,156,39)-difference set in C_3 x C_207, the C_23 fiber counts are forced to (2;5^11;9^11) up to swap, and order-3 characters on C_3 x C_9 then give a contradiction.`
- Delete the false aside that `(13,3,10)` is another integer solution to the fiber-count equations.
- This preserves a useful same-lane solve artifact, but it does not settle the selected problem.

## publication_prior_art_audit
PASS 1: bounded prior-art audit.

- Exact-statement and alternate-notation web searches on `2026-04-15` for
  `(621,156,39)` with `C_3 x C_207`, `[3,207]`, and `Z_3 x Z_207` did not surface a
  later construction, nonexistence theorem, or maintained database entry settling the
  exact row within the audit budget.
- Canonical-source check: Gordon-Schmidt `2016` explicitly say Table `2` gives the
  smallest open cases, and the table still lists `621 156 39 [3,207] ... 13`.
- Same-source theorem / proposition / example / corollary / observation /
  sufficient-condition check: within the bounded survey pass, the exact `[3,207]` row
  appears as an open residual case, not as a consequence of a later theorem elsewhere in
  the paper.
- Canonical-source caution: the survey also states that the `MC primes` column records
  prime factors of `n` that are multipliers under the multiplier conjecture. In this
  packet that matters: the row's `13` entry is not, by itself, a source-backed
  unconditional multiplier theorem for the selected exact case.
- One outside-source status pass: Gordon's publications page still lists the `2016`
  survey and later difference-set papers, but the `2022` paper `On Difference sets with
  small lambda` does not mention `621`, and this bounded pass found no later primary
  source settling the exact `[3,207]` row.
- Conservative prior-art verdict: no rediscovery established within budget.

## publication_statement_faithfulness
PASS 2: statement faithfulness for publication.

- The selected statement is unconditional: determine whether `C_3 x C_207` admits a
  `(621,156,39)` difference set.
- The current artifact does not support that exact theorem. Its first load-bearing move
  still depends on treating the survey's `MC primes = 13` row cue as an unconditional
  usable multiplier theorem.
- The bounded canonical-source check cuts the other way: the survey frames those primes
  under the multiplier-conjecture lane, so the packet cannot honestly advertise the
  unconditional exact-row nonexistence theorem.
- The strongest source-faithful output remains only the conditional obstruction slice:
  if a valid `13`-multiplier normalization is available for a hypothetical difference
  set, then the quotient profile is forced to `(2;5^11;9^11)` up to swap and the
  order-`3` character argument rules out that conditional case.

## publication_theorem_worthiness
PASS 3: theorem worthiness.

- Is the strongest honest claim stronger than "here is an example"? Yes, but only as a
  conditional structural obstruction theorem slice. It is not merely an example, but it
  is also not the selected exact theorem.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is
  a real conditional theorem slice. There is not yet a referee-stable title theorem for
  the exact `[3,207]` row.
- Is the proof structural or merely instance-specific? Structural within this exact row:
  the surviving argument uses quotient orbits, Gaussian periods, and order-`3`
  characters rather than hand-picked casework.
- Would this survive a referee asking "what is the theorem?" No for the selected packet.
  The immediate referee question would be why `13` is an unconditional multiplier here,
  and the present packet does not answer that from the cited source support.
- Is the claim still too dependent on hand-picked small cases? No in method; yes in
  dependence on a special row-specific multiplier premise. The weakness is not
  case-bashing but unsupported premise anchoring.

## publication_publishability
PASS 4: publishability.

- Would this result, if correct and verified in the current bounded sense, already
  constitute most of a publishable note? No. In its current honest form it is still a
  conditional lemma package, not the note's title theorem.
- What percentage of the paper would one solve already provide? About `30%`.
- Is the result still close to paper-ready, or did the candidate only look attractive
  before audit? It looked substantially better before audit. Once the multiplier bridge
  is treated conservatively, the remaining gap is not editorial polish; it is the
  missing theorem-facing bridge itself.
- If this is not yet paper-ready, is the remaining gap genuinely small? No. The gap is
  earlier than the main contradiction and load-bearing for publication.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a
  larger theorem program? Yes. Preserve the conditional artifact, but move the slug
  aside unless the exact same lane yields either an explicit source-backed unconditional
  multiplier theorem or a multiplier-free contradiction.

## publication_packet_audit
PASS 5: packet audit.

- `publication_status = NONE`
- `publication_confidence = high`
- `publication_packet_quality = preserved structural conditional slice, but not a
  publication-ready exact-row packet`
- `proof_artifacts_preserved = true`
- `lean_ready = false`
- `human_ready = false`
- Would Lean directly seal the packet, or only be optional polish / later archival
  formalization? Lean would only seal the conditional slice. It would not convert the
  selected exact-row packet into a human-ready result.

## micro_paper_audit
PASS 6: micro-paper audit.

- The original target remains micro-paper eligible in principle if the exact row is
  actually settled.
- The current verified-and-audited packet fails the strict micro-paper lane because the
  strongest honest claim is conditional and does not yet furnish the note's theorem.
- `single_solve_to_paper_fraction = 0.30`
- `title_theorem_strength = weak`
- `publication_narrative_strength = weak`
- MICRO-PAPER verdict: not close enough. The artifact is worth preserving as same-lane
  residue, but it should not block fresh discovery work or be inflated into a broader
  campaign.

## strongest_honest_claim
Assuming a valid `13`-multiplier normalization for a hypothetical
`(621,156,39)`-difference set in `C_3 x C_207`, the `C_23` quotient fibers are forced
to `(2;5^11;9^11)` up to orbit swap, and the order-`3` character argument on
`C_3 x C_9` then yields a contradiction. This is stronger than an example, but it does
not settle the unconditional exact row.

## paper_title_hint
If the preserved residue were ever written up on its own, the honest title would have to
be conditional, e.g. `A conditional orbit obstruction for the (621,156,39) row in
C_3 x C_207 under a 13-multiplier hypothesis`. That is not the recommended micro-paper
target.

## next_action
Freeze this packet as a conditional `VARIANT` artifact and move it aside rather than
expanding the theorem program. Reopen only if the same exact-row lane produces either an
explicit source-backed unconditional multiplier theorem or a multiplier-free
contradiction.
