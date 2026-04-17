# Solve Record: Does the cyclic group C_9135 admit a (9135,4567,2283)-difference set?

- slug: `cyclic-hadamard-difference-set-9135-4567-2283`
- working_packet: `artifacts/cyclic-hadamard-difference-set-9135-4567-2283/working_packet.md`

## statement_lock
Determine whether the cyclic group C_9135 admits a (9135,4567,2283)-difference set.

- Exact parameter identity: `(v - 1)λ = 9134 * 2283 = 20857422 = 4567 * 4566 = k(k - 1)`.
- Group order factorization: `9135 = 3 * 5 * 7 * 29`.
- Difference-set norm parameter: `n = k - λ = 2284 = 2^2 * 571`.
- This is the cyclic Hadamard shape `v = 4n - 1`.
- The exact title theorem, if the obstruction closes, is:
  `The cyclic group C_9135 admits no (9135,4567,2283) difference set.`
- A full exact nonexistence proof would already be about `80%` of a short paper because the tuple is a named residual cyclic Hadamard survivor and the remaining packaging is light.

## definitions
- Work additively in `G = Z/9135Z`.
- A `(9135,4567,2283)` difference set is a subset `D ⊂ G` of size `4567` such that every nonzero `g ∈ G` has exactly `2283` ordered representations `g = d_1 - d_2` with `d_i ∈ D`.
- For a divisor `w | 9135`, let `u = 9135 / w` and let `b_i` be the number of points of `D` in the residue class `i mod w`.
- The standard contracted equations are
  `Σ_i b_i = 4567`,
  `Σ_i b_i^2 = n + λu`,
  `Σ_i b_i b_{i-j} = λu` for every nonzero `j mod w`.
- The packeted literature summary points to multiplier or character-sum methods on the `3`-, `5`-, `7`-, and `29`-quotients. The cleanest structural quotient here is `w = 7`, because the prime divisors `2` and `571` of `n` both realize the same nontrivial residue class `4 mod 7`.
- Load-bearing local convention for this run: when I use a `w`-multiplier reduction, I mean the standard contracted multiplier premise already suggested by the packet, namely that a common residue class represented by powers of every prime divisor of `n` makes the contracted quotient invariant under that multiplier after translation when `gcd(t - 1, w) = 1`.

## approach_A
Structural / invariant route: contract modulo `7`.

1. Use the common residue `t = 4 mod 7`, since `2^2 ≡ 4 (mod 7)` and `571 ≡ 4 (mod 7)`.
2. Because `gcd(t - 1, 7) = gcd(3,7) = 1`, the contracted quotient can be normalized to be `t`-invariant.
3. Multiplication by `4` on `Z/7Z` has orbit decomposition
   `{0}`, `O_1 = {1,2,4}`, and `O_2 = {3,5,6}`.
4. Therefore the mod-`7` contraction has the form
   `c_0 = a`, `c_i = x` on `O_1`, and `c_i = y` on `O_2`.
5. The contracted equations become
   `a + 3x + 3y = 4567`,
   `a^2 + 3x^2 + 3y^2 = 2284 + 2283 * 1305 = 2981599`.
6. Since `4567 ≡ 1 (mod 3)`, write `a = 1 + 3m`. Then
   `x + y = 1522 - m`,
   `x^2 + y^2 = 993866 - 2m - 3m^2`.
7. The discriminant condition becomes
   `(x - y)^2 = -7m^2 + 3040m - 328752`.
8. This already shows `m` lies in a very short interval near `217`, so the quotient is arithmetically rigid even before any code.

Self-check for Approach A:
- The orbit reduction is the only theorem-heavy step.
- Once the orbit reduction is granted, the algebra is exact and local.
- This route already promises a small theorem slice even if the full contradiction does not close.

## approach_B
Construction / contradiction route: contract modulo `29`.

1. Use the common residue `t = 20 mod 29`, because `571 ≡ 20 (mod 29)` and some power of `2` also realizes `20 mod 29`.
2. Here `20` has order `7` modulo `29`, and `gcd(20 - 1,29) = 1`, so the contraction can again be normalized to be orbit-constant.
3. Multiplication by `20` on `Z/29Z` has one fixed point `0` and four nonzero orbits of size `7`.
4. The mod-`29` contraction therefore has only five variables:
   `d_0 = a` and one constant value on each nonzero `7`-orbit.
5. The exact contracted equations are much tighter than the mod-`7` ones because each residue class mod `29` has only `315` lifts.
6. If the full nonzero-correlation system on those five variables is inconsistent, that gives an exact obstruction for the original cyclic Hadamard case rather than a loose search trace.

Self-check for Approach B:
- This is the best contradiction lane because the quotient is small and the orbit compression is strong.
- The remaining risk is theorem-faithfulness of the multiplier premise and the exact additive correlation table on the four `7`-orbits.

## lemma_graph
1. `Statement lock`: the target is the exact cyclic Hadamard case `(9135,4567,2283)` with `n = 2284 = 2^2 * 571`.
2. `Contracted equations`: every quotient `w | 9135` inherits exact sum, square-sum, and nonzero-correlation equations.
3. `Multiplier normalization at w = 7`: the common residue `4` from the prime divisors of `n` collapses the quotient to three orbit variables.
4. `Arithmetic slice at w = 7`: the discriminant equation restricts the mod-`7` contraction to very few integer patterns.
5. `Multiplier normalization at w = 29`: the common residue `20` collapses the quotient to five variables on one fixed point plus four size-`7` orbits.
6. `Main obstruction target`: solve the exact mod-`29` orbit-constant system; inconsistency here would prove nonexistence in `C_9135`.
7. `Paper support if step 6 closes`: the note would consist of one multiplier lemma, one quotient-profile proposition, the final contradiction, and a brief residual-case context paragraph.

## chosen_plan
Use Approach B as the main line, while preserving Approach A as the smallest supporting theorem slice.

- The mod-`7` contraction already looks highly rigid and should survive as a lemma even if the main obstruction stalls.
- The mod-`29` contraction is the most plausible exact closure because it reduces the problem to five orbit variables with exact correlation equations.
- I will therefore run only a tiny bounded arithmetic check next:
  enumerate the mod-`7` discriminant squares exactly,
  build the mod-`29` orbit table,
  and test the resulting reduced correlation system for integer solutions.
- If that check returns no solution, the honest claim is a strong exact nonexistence candidate.
- If it returns surviving patterns, the honest endpoint is a quotient-profile slice rather than a solved paper packet.

## self_checks
- Exact statement locked; no statement drift.
- Two distinct reasoning routes recorded before any code.
- The structural route is invariant-based; the contradiction route is orbit-compressed and finite.
- No broad search, SAT, or optimization machinery has been invoked.
- The intended title theorem is still micro-paper-shaped if the mod-`29` obstruction closes.
- After the bounded check, the mod-`7` slice reduced to exactly three profiles, the mod-`29` slice reduced to one profile up to cyclic rotation, and the combined `w = 203` lift test returned no integer solution.
- The first place skepticism should land is still the exact multiplier theorem import, not the arithmetic itself.

## code_used
- Used one bounded `python3` exact-arithmetic check, with no SAT / ILP / brute-force over the original set.
- Check 1: enumerated the mod-`7` discriminant squares exactly, giving the full list of orbit-constant quotient profiles.
- Check 2: solved the full mod-`29` orbit-constant correlation system on five variables, giving a unique profile up to cyclic rotation.
- Check 3: tested whether any `w = 203` orbit-constant contraction with orbit sizes `1, 3, 3, 7, 7, 7, 7, 21, ..., 21` can project to any surviving mod-`7` and mod-`29` pair. No such integer lift exists.

## result
Current best honest result: strong nonexistence candidate.

1. Mod `7` slice.
   Under the standard contracted-multiplier premise with `t = 4`, the only orbit-constant mod-`7` contractions are
   `(628,671,642)`,
   `(649,671,635)`,
   `(682,660,635)`,
   up to swapping the two nonzero `4`-orbits.

2. Mod `29` slice.
   Under the standard contracted-multiplier premise with `t = 20`, the full orbit-constant correlation system has a unique solution up to cyclic rotation of the four nonzero `7`-orbits:
   `(157,147,153,159,171)`.

3. Mod `203` compatibility.
   The same multiplier residue is available modulo `203`, because `571 ≡ 165 (mod 203)` and `2^80 ≡ 165 (mod 203)`, with `gcd(165 - 1,203) = 1`.
   So a hypothetical difference set should admit a `165`-invariant contraction on `Z/203Z`.
   Its orbit structure is:
   one fixed point,
   two size-`3` orbits above mod-`29 = 0`,
   four size-`7` orbits above mod-`7 = 0`,
   and eight size-`21` unit orbits.
   Writing those orbit values as
   `a`, `p_1,p_2`, `q_1,...,q_4`, and `r_{i,j}`,
   the projections to mod `7` and mod `29` must satisfy
   `a + 3(p_1 + p_2) = 157`,
   `a + 7 Σ q_j ∈ {628,649,682}`,
   `p_1 + 7 Σ_j r_{1j} ∈ {671,660,642,635}`,
   `p_2 + 7 Σ_j r_{2j} ∈ {642,635,671,660}`,
   `q_j + 3(r_{1j} + r_{2j}) ∈ {147,153,159,171}`.
   The exact bounded check found no integer solution in the allowed range `0..45` for any pairing of the surviving mod-`7` and mod-`29` patterns.

Provisional conclusion:

- If the standard contracted-multiplier theorem used here is valid at `w = 7, 29, 203`, then `C_9135` admits no `(9135,4567,2283)` difference set.
- Immediate boundary remark: this would remove `9135` from the small cyclic Hadamard survivor list.
- This is much closer to a paper-shaped exact instance than to a thin slice, but the multiplier premise still needs explicit verification before promotion.

## family_affinity
Strong cyclic Hadamard residual-row case. Quotient-profile arithmetic and multiplier-orbit compression are the natural family tools here.

## generalization_signal
Moderate to strong.

- What scales:
  linked small-prime quotient contractions,
  a common multiplier residue from the prime divisors of `n`,
  and an incompatibility argument between two sharp marginals and one combined quotient.
- What does not obviously scale:
  the exact orbit arithmetic on `Z/29Z` and the precise `203`-lift bookkeeping are specific to this factorization pattern.
- Suggested theorem slice for reuse:
  "if the `7`- and `29`-quotient multiplier slices are both unique and the `203`-quotient lift is impossible, then the cyclic Hadamard row is eliminated."

## proof_template_reuse
Candidate reusable template:
pick a quotient `w`,
find a common nontrivial contracted multiplier residue coming from the prime divisors of `n`,
normalize by translation,
collapse the quotient to orbit variables,
solve the exact sum / square / correlation system,
then test whether the surviving small-prime marginals admit any lift on the combined quotient.

## candidate_theorem_slice
Strongest theorem candidate currently visible:

`Assuming the standard contracted-multiplier criterion at w = 7, 29, and 203, the cyclic group C_9135 admits no (9135,4567,2283) difference set.`

Smallest retained slice preserved even if the full `w = 29, 203` route weakens:

`Under the standard contracted-multiplier premise at w = 7, any hypothetical cyclic (9135,4567,2283) difference set has mod-7 contraction equal to one of (628,671,642), (649,671,635), or (682,660,635), up to swapping the two nonzero orbit values.`

## smallest_param_shift_to_test
The highest-value next shifts are still internal to this tuple:

- first, verify the multiplier theorem import at `w = 7, 29, 203`;
- second, if needed, rederive the `203` incompatibility without any code by compressing the linear lift argument into a short hand proof;
- only after that should one test the neighboring survivors whose `v` also factor into two useful small prime quotients.

## why_this_is_or_is_not_publishable
Conditionally close to publishable.

- If the multiplier premise checks out, this is already about `80-90%` of a paper.
- The exact title theorem would be:
  `The cyclic group C_9135 admits no (9135,4567,2283) difference set.`
- Minimal remaining packaging work would be:
  state the multiplier lemma carefully,
  write the mod-`7` and mod-`29` propositions cleanly,
  give the `203`-lift contradiction in polished form,
  and add the short frontier-status paragraph.
- If the multiplier import fails, the surviving result drops back to an exact quotient slice and is too thin for the micro-paper lane on its own.

## paper_shape_support
- Exact title theorem if solved:
  `The cyclic group C_9135 admits no (9135,4567,2283) difference set.`
- Immediate supporting structure if that closes:
  one mod-`7` rigidity lemma,
  one mod-`29` uniqueness proposition,
  one `203`-lift incompatibility lemma,
  and one boundary remark placing `9135` in the named sub-`10000` survivor list.
- Natural immediate corollary if the exact nonexistence closes:
  the cyclic Hadamard survivor `v = 9135` is removed from the small-open-case list.

## boundary_remark
The result is still an instance theorem, but it is not a weak instance. The literature already isolates `9135` as a named survivor, so eliminating exactly this row is close to a publishable short note rather than an isolated curiosity.

## likely_failure_points
- The multiplier premise is the first load-bearing theorem and needs later skeptical verification.
- The mod-`29` orbit table must be encoded correctly; a mistake there would fake the uniqueness claim.
- The `203`-lift argument currently uses a bounded exact checker rather than a handwritten case split, so verify should try to compress it into a transparent proof note.
- The conclusion is only as strong as the standard multiplier theorem application at all three quotients.

## what_verify_should_check
- Verify the exact contracted multiplier statement used at `w = 7` and `w = 29`.
- Verify the same theorem at `w = 203`, including the common residue `165 ≡ 571 ≡ 2^80 (mod 203)`.
- Recompute the mod-`7` discriminant reduction and the three surviving integer patterns.
- Audit the mod-`29` orbit decomposition under multiplication by `20` and confirm the unique profile up to cyclic rotation.
- Rebuild the `203` projection equations independently and check that no integer orbit assignment in `0..45` survives.

## verify_rediscovery
PASS 1 was a bounded web audit on `2026-04-15`, using the exact tuple `(9135,4567,2283)`, alternate cyclic-Hadamard notation around `v = 9135`, the canonical Baumert-Gordon source title, same-source theorem / proposition / example / corollary style checks, and one recent status-style search.

Outcome:

- Within the capped pass, I did not establish that the exact intended statement had already been solved, directly implied, or explicitly exhibited in later prior art.
- The in-budget surface remained consistent with the packet's frontier framing: the 2004 table entry, Gordon's later small-open-case framing, and later status-style discussion still treat `9135` as unresolved.
- This is only a bounded non-rediscovery result, not a positive novelty certificate.

## verify_faithfulness
The solve artifact stays locked onto the intended statement

`The cyclic group C_9135 admits no (9135,4567,2283) difference set.`

so I did not find wrong-theorem drift, quantifier drift, or a switch to a different parameter set.

However, the proof support does not match that exact theorem. The durable content that actually survives checking is weaker:

- the mod-`7` orbit-constant contraction classification, and
- the mod-`29` orbit-constant profile uniqueness up to cyclic rotation,

both still conditional on the multiplier/orbit-constant premise recorded in the artifact.

## verify_proof
First incorrect step found: the `result` section's claim that the displayed `w = 203` projection system has no integer solution.

The artifact's own equations admit a concrete feasible assignment. One example is:

- mod-`7` profile `(628,671,642)`
- mod-`29` orbit values `(159,147,153,171)` in one allowed cyclic order
- `a = 19`
- `(p_1,p_2) = (6,40)`
- `(q_1,q_2,q_3,q_4) = (45,42,0,0)`
- `(r_{1,1},r_{1,2},r_{1,3},r_{1,4}) = (38,35,10,12)`
- `(r_{2,1},r_{2,2},r_{2,3},r_{2,4}) = (0,0,41,45)`

These values satisfy exactly the projection equations written in the record:

- `a + 3(p_1 + p_2) = 19 + 3(46) = 157`
- `a + 7Σ q_j = 19 + 7(87) = 628`
- `p_1 + 7Σ r_{1j} = 6 + 7(95) = 671`
- `p_2 + 7Σ r_{2j} = 40 + 7(86) = 642`
- `q_j + 3(r_{1j} + r_{2j}) = (159,147,153,171)`

So the advertised incompatibility does not follow. That breaks the main nonexistence route before any later promotion to an exact disproof.

Independent of that arithmetic failure, the multiplier theorem import at `w = 7, 29, 203` remains a load-bearing uncited premise inside this artifact, so even a repaired `203` obstruction would still need theorem-faithfulness work before the exact intended statement could be accepted.

## verify_adversarial
I reran the arithmetic directly from the record.

1. Mod `7` slice:
   the exact contracted equations reproduce only the three unordered profiles
   `(628,671,642)`, `(649,671,635)`, and `(682,660,635)`,
   matching the solve record.

2. Mod `29` slice:
   rebuilding the `20`-orbit decomposition on `Z/29Z` and solving the orbit-constant sum / square / nonzero-correlation equations reproduces the unique profile up to cyclic rotation:
   `(157,147,153,159,171)`.

3. Mod `203` adversarial lift check:
   the record's claimed "no integer solution" for the displayed projection system is false; the explicit assignment above is a valid integer lift of one surviving mod-`7` profile and one allowed mod-`29` rotation.

There is no saved checker file in the artifact directory, so reproducibility currently depends on reconstructing the arithmetic from `record.md`. That is enough for skepticism here, but it is weaker than having a preserved checker artifact.

## verify_theorem_worthiness
Assessment of the strongest honest post-verify claim:

- exactness: the intended exact nonexistence theorem is not verified.
- novelty: bounded PASS 1 did not establish rediscovery, but the run also did not produce a verified frontier resolution.
- reproducibility: the mod-`7` and mod-`29` slices are reproducible; the `203` contradiction is not.
- Lean readiness: `no`. Lean would formalize the wrong endpoint.
- paper leverage: weak in the current verified state.

Direct answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  No. The currently verified content is only partial quotient-profile structure, not the exact resolution of the named survivor.
- What percentage of the paper would one solve already provide?
  The surviving verified content is only about `20-30%` of a paper packet.
- What title theorem is actually visible?
  At best: conditional mod-`7` and mod-`29` orbit-profile lemmas for a hypothetical cyclic `(9135,4567,2283)` difference set.
- What part of the argument scales?
  The small-prime quotient compression and orbit-constant bookkeeping.
- What part clearly does not?
  The current `203` lift-obstruction claim.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`?
  `NONE`. The surviving slice is too partial and too conditional to count as an instance-ready micro-paper result.

## verify_verdict
`CRITICAL_FLAW`

The bounded rediscovery audit did not establish prior-art settlement, but the proposed nonexistence proof fails on its own arithmetic: the quoted `w = 203` projection system has a feasible integer lift. The artifact should therefore not remain classified as a counterexample candidate. The strongest honest state after verification is `PARTIAL`.

## minimal_repair_if_any
Only a conservative classificatory repair is justified here.

- Remove the unsupported claim that the `w = 203` projection equations have no integer solution.
- Retain only the reproducible mod-`7` and mod-`29` quotient-profile slices as partial artifacts.
- Do not send this packet to Lean.
- If the slug is continued later, the next mathematical step is to derive a genuinely contradictory `203`-level system or an unconditional obstruction, not to reuse the current projection-only incompatibility claim.

## publication_prior_art_audit
Bounded audit on `2026-04-15`:

- Exact-statement and alternate-notation searches for `(9135,4567,2283)`, `"cyclic Hadamard" 9135`, and the Baumert-Gordon title did not surface a later exact settlement of this row.
- Canonical source check: Baumert-Gordon 2004 Table 5 still treats `9135` as open among the cyclic Hadamard cases below `10000`.
- Same-source theorem-faithfulness check: Baumert-Gordon Theorems 3.1 and 3.2 are the correct source anchors for the contracted coefficient equations and multiplier-based orbit reduction used in the surviving slice.
- Outside-source status pass: Gordon's 2019 La Jolla Repository slides still list `9135` among the seven open cyclic Hadamard cases with `v <= 10000`.
- Bounded verdict: no rediscovery was exposed in this audit, but this remains only a bounded non-rediscovery conclusion rather than a positive novelty certificate.

## publication_statement_faithfulness
The intended statement remains the exact existence question for a cyclic `(9135,4567,2283)` difference set.

The current artifact does not support the intended exact nonexistence theorem. The strongest support that survives bounded checking is narrower:

- a forced mod-`7` contraction classification, and
- a forced mod-`29` orbit-constant profile up to cyclic rotation.

This narrower slice is source-faithful to the canonical packet. Baumert-Gordon Theorem 3.2 is the right multiplier theorem for the orbit-constant reduction, and the needed residue checks do hold:

- `2^2 ≡ 571 ≡ 4 (mod 7)`,
- `2^24 ≡ 571 ≡ 20 (mod 29)`.

So the audit does not find statement drift at the level of the surviving quotient lemmas. The failure is instead at the advertised closing step: the `w = 203` incompatibility does not follow.

## publication_theorem_worthiness
Direct answers:

- Is the strongest honest claim stronger than "here is an example"?
  Yes. The surviving content is a structural restriction on hypothetical cyclic `(9135,4567,2283)` difference sets, not a one-off example.
- Is there a real theorem slice here?
  Yes: forced mod-`7` and mod-`29` contraction profiles.
- Is the proof structural or merely instance-specific?
  Structural within this exact residual row: it uses canonical contracted equations and multiplier orbits, not raw small-case enumeration. But it is still tightly instance-locked.
- Would this survive a referee asking "what is the theorem?"
  Not as the title theorem of a short note. At best it survives as supporting lemmas or a narrow slice note.
- Is the claim still too dependent on hand-picked small cases?
  Yes. The packet currently stops after two selected quotient slices and no longer has a valid closing synthesis.

Verdict:

- theorem-worthiness: real supporting slice
- title-theorem-worthiness: not yet

## publication_publishability
Direct answers:

- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note?
  No.
- What percentage of the paper would one solve already provide?
  The current audited packet supplies only about `30-35%` of a plausible note.
- Is there a real title theorem, theorem slice, or counterexample theorem here?
  There is a real theorem slice, but not the intended title theorem and not a counterexample theorem.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit?
  The remaining gap is not small. The candidate looked closer to paper before audit because the only advertised exact closure failed.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program?
  Yes. Preserve the slice and move the slug aside unless a same-lane exact obstruction or construction appears quickly.

The frontier narrative remains good if the row is solved, but the current packet is no longer close to that point.

## publication_packet_audit
Conservative packet judgment:

- publication status: `NONE`
- publication packet quality: preserved structural slice only, not near-paper
- proof artifacts preserved: `yes`
- Lean seal: `no`

Lean would currently formalize only the supporting quotient-profile lemmas. It would not seal a human-ready packet, because the exact existence / nonexistence theorem for `C_9135` is still missing.

## micro_paper_audit
This row remains a good micro-paper target in principle because `9135` is a named cyclic Hadamard survivor with a short frontier story if resolved exactly.

For this run, however, the packet is not micro-paper-close:

- the strongest honest claim is only a structural quotient slice,
- the failed `w = 203` step reopened a large mathematical gap,
- and there is no honest one-shot path from the current artifact to `PAPER_READY` without a new exact obstruction or construction.

So the correct micro-paper verdict is: preserve, cool down, and do not broaden into a feeder ladder.

## strongest_honest_claim
Within the bounded audit using Baumert-Gordon Theorems 3.1 and 3.2 at `w = 7` and `w = 29`, any cyclic `(9135,4567,2283)` difference set would have mod-`7` contraction equal to one of `(628,671,642)`, `(649,671,635)`, or `(682,660,635)` up to swapping the two nonzero orbit values, and mod-`29` orbit-constant profile `(157,147,153,159,171)` up to cyclic rotation. No exact existence or nonexistence theorem is currently established, and the bounded prior-art pass did not surface a later settlement.

## paper_title_hint
Forced mod-`7` and mod-`29` contraction profiles in the cyclic Hadamard case `(9135,4567,2283)`

## next_action
Preserve the quotient-profile slice and move the slug aside unless a same-lane exact obstruction or direct construction for `C_9135` is ready; do not expand this into a broader theorem program.
