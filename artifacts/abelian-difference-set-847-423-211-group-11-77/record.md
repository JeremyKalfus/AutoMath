# Solve Record: On the (847,423,211) Difference-Set Problem in C_11 x C_77

- slug: `abelian-difference-set-847-423-211-group-11-77`
- working_packet: `artifacts/abelian-difference-set-847-423-211-group-11-77/working_packet.md`

## statement_lock
Active slug: `abelian-difference-set-847-423-211-group-11-77`.

Active title theorem target: determine whether the abelian group `C_11 x C_77` admits a `(847,423,211)` difference set.

I will treat `G = C_11 x C_77 ≅ C_11^2 x C_7` and the exact intended statement as:

> There does not exist, or there does exist, a subset `D ⊂ G` of size `423` such that every nonzero group element has exactly `211` representations as `d_1 - d_2` with `d_1,d_2 ∈ D`.

Parameter check:

- `v = 847 = 7 * 11^2`
- `k = 423 = (v-1)/2`
- `lambda = 211 = (v-3)/4`
- `n = k-lambda = 212 = 4 * 53`

So this is a Paley/skew-Hadamard parameter set at odd order `847`, but in a noncyclic abelian group.

## definitions
Let `D` denote the formal group-ring sum of the putative subset.

Difference-set identity:

`D D^(-1) = k + lambda (G - 1)`.

Hence for every nonprincipal character `chi` of `G`,

`|chi(D)|^2 = n = 212`.

Two quotient models will be used.

1. Order-11 quotient model.
Choose any quotient `pi_11 : G -> Q` with `Q ≅ C_11`; its kernel has size `77`.
Let `c_i` be the number of points of `D` in the `i`th coset of `ker(pi_11)`.
Then:

- `sum_i c_i = 423`
- `sum_i c_i^2 = k + lambda(77-1) = 423 + 211*76 = 16459`
- `sum_i c_i c_{i+t} = lambda*77 = 16247` for each nonzero `t in C_11`

Writing `c_i = 38 + a_i` gives the centered equations

- `sum_i a_i = 5`
- `sum_i a_i^2 = 195`
- `sum_i a_i a_{i+t} = -17` for each nonzero `t`

Equivalently every nontrivial Fourier coefficient of `a` on `C_11` has squared modulus `212`.

2. Order-121 quotient / 7-fiber model.
Let `H ≅ C_11^2` and write `G = H x C_7`.
For each `h in H`, let `y_h = |D ∩ ({h} x C_7)|`, so `0 <= y_h <= 7`.
Then:

- `sum_h y_h = 423`
- `sum_h y_h^2 = k + lambda(7-1) = 423 + 211*6 = 1689`

Writing `y_h = 3 + z_h` gives

- `sum_h z_h = 60`
- `sum_h z_h^2 = 240`

and every nontrivial character of `H` again sees squared modulus `212`.

## approach_A
Structural / invariant approach: push to an order-11 quotient and work with the exact autocorrelation equations there.

Why this is promising:

- the quotient data has only `11` integer unknowns;
- the difference-set condition collapses to a rigid constant-correlation system;
- if the system has no integral solution, nonexistence in `G` follows immediately;
- even if solutions exist, they become a short finite list of admissible quotient profiles, which is useful paper-facing structure.

Concrete target:

Prove that no integer vector `(c_0,...,c_10)` with `0 <= c_i <= 77` satisfies the three equations above, or reduce all solutions to a tiny list.

Self-check after Approach A:

- this uses only exact quotient counting and the standard character identity;
- no multiplier theorem is being assumed without proof;
- the argument stays theorem-facing even if it only yields a sharp quotient obstruction.

## approach_B
Construction / extremal / contradiction approach: analyze the `121` fibers over the `C_7` factor.

The centered variables `z_h = y_h - 3` satisfy `sum z_h = 60` and `sum z_h^2 = 240`, so the fibers are forced to stay close to `3` or `4`, but not too close: the square budget is materially above the balanced `3/4` mixture. If a solution exists, it should induce a very rigid weighted subset of `C_11^2` with flat nontrivial spectrum `212`.

Why this is promising:

- the weights are bounded in `{0,1,...,7}`, so any admissible profile is highly constrained;
- line sums along the `12` order-11 quotients of `C_11^2` must each satisfy the same order-11 quotient equations from Approach A;
- this can turn a global existence problem into a compatibility problem among small quotient profiles.

Extremal angle:

The baseline balanced profile would be `60` fibers of size `4` and `61` of size `3`, whose square sum is only `1509`; the true square sum is `1689`, so any solution needs an additional `180` units of quadratic variance. That makes the configuration much less "random" than the average count suggests.

Self-check after Approach B:

- this does not yet solve the problem, but it identifies a genuine rigidity source;
- it also explains what additional structure would make the final theorem paper-shaped: a clean incompatibility between the order-11 quotient profiles and the bounded `0..7` fiber model.

## lemma_graph
Lemma skeleton currently in play:

1. If `D` is a `(847,423,211)` difference set in `G`, then every nonprincipal character value has squared modulus `212`.
2. Therefore the image of `D` in any quotient `Q ≅ C_11` yields an integer `11`-tuple with constant off-zero autocorrelation `16247`.
3. After centering, this becomes an integer vector on `C_11` with sum `5`, square sum `195`, and every nontrivial cyclic shift inner product `-17`.
4. If no such `11`-tuple exists, then no difference set exists in `G`.
5. Independently, the `C_7`-fiber counts over `H ≅ C_11^2` give a bounded-weight function with sum `423`, square sum `1689`, and the same nontrivial spectral magnitude `212`.
6. Any admissible global solution must therefore satisfy both the `11`-quotient and `121`-fiber rigidity packages simultaneously.

## chosen_plan
Best path: start with Approach A and treat the order-11 quotient equations as the primary obstruction candidate.

Reason for choosing it:

- it is the smallest exact reduction;
- it gives a finite bounded experiment if pure hand reasoning stalls;
- a contradiction there would already be theorem-shaped and would leave only light packaging work.

Planned next step:

Run a tiny exact enumeration for the centered `11`-tuple system

- `sum a_i = 5`
- `sum a_i^2 = 195`
- `sum a_i a_{i+t} = -17` for `t = 1,...,10`

before spending effort on deeper `C_11^2` compatibility arguments.

## self_checks
- Statement lock check: the active packet and working packet agree on the exact target and publication frame.
- Parameter check: `423 * 422 = 847 * 211`, so the standard parameter identity holds.
- Quotient-count check for `|ker| = 77`: diagonal total `423 + 211*76 = 16459`, off-diagonal total `211*77 = 16247`.
- Fiber-count check for `|C_7| = 7`: diagonal total `423 + 211*6 = 1689`.
- Scope check: no code yet, no web, no broad repo replay.
- Post-experiment check: the bounded searches were only on quotient shadows, not on the full `847`-point ambient group.
- Parity check: the `2`-adic argument uses only that `2` is inert in `Q(zeta_11)` because `ord_11(2)=10`.
- Incidence check: the affine-plane parity lemma was verified by exact Gaussian elimination over `F_2` on the `121` point variables and `132` affine-line equations.
- Enumeration check: the `C_7` and `C_11` quotient profile searches were exhaustive within the exact centered equations written above.

## code_used
Yes, but only as bounded exact checking.

Three tiny inline `python3` computations were used:

1. exhaustive search of the `C_7` quotient profile equations;
2. exact `F_2` linear algebra on the `121` points of `C_11^2` to determine the unique parity pattern compatible with odd line sums;
3. exhaustive search of the odd `C_11` quotient profile equations, including orbit reduction.

No brute force was attempted on the full ambient group.

## result
No full existence or nonexistence proof yet, but the solve pass produced a real structural slice.

Main exact findings:

1. `C_7` quotient shadow.
If `x_0,...,x_6` are the counts on the seven cosets of `C_11^2`, then after centering `x_i = 60 + b_i` the exact equations are

- `sum b_i = 3`
- `sum b_i^2 = 183`
- `sum b_i b_{i+t} = -29` for each nonzero `t in C_7`

and exhaustive search shows that, up to cyclic shift and reversal, only three quotient profiles occur:

- `48,62,62,63,62,63,63`
- `55,55,60,66,66,55,66`
- `55,55,63,55,63,63,69`

So the order-7 shadow is rigid, but not contradictory.

2. Parity theorem on the `C_11^2` fibers.
For `y_h = |D ∩ ({h} x C_7)|`, every order-11 quotient line sum must be odd. The reason is:

- for any quotient `Q ≅ C_11`, the quotient character value `C(zeta_11)` has squared modulus `212 = 4 * 53`;
- `2` is inert in `Q(zeta_11)`, so the unique prime above `2` divides `C(zeta_11)`;
- therefore every order-11 quotient intersection number is odd.

Reducing modulo `2`, this says that the parity pattern `b_h := y_h mod 2` has line sum `1` on every affine line of `AG(2,11)`. Exact linear algebra over `F_2` shows the only such pattern is the all-ones pattern. Hence:

> Every fiber count `y_h` is odd.

So every `y_h` lies in `{1,3,5,7}`.

3. Consequent odd-fiber count parameterization.
Let `n_1,n_3,n_5,n_7` count how many fibers have sizes `1,3,5,7`. From

- `n_1+n_3+n_5+n_7 = 121`
- `n_1+3n_3+5n_5+7n_7 = 423`
- `n_1+9n_3+25n_5+49n_7 = 1689`

one gets the exact one-parameter family

- `n_1 = 15-r`
- `n_3 = 61+3r`
- `n_5 = 45-3r`
- `n_7 = r`

for `0 <= r <= 15`.

4. `C_11` quotient shadow.
If `c_0,...,c_10` are the counts on an order-11 quotient and `c_i = 38 + a_i`, then the exact equations are

- `sum a_i = 5`
- `sum a_i^2 = 195`
- `sum a_i a_{i+t} = -17` for each nonzero `t in C_11`

and, after the parity reduction above, exhaustive search shows there is exactly one signed multiset and one dihedral orbit:

- centered multiset: one `-5`, five `-3`, five `+5`;
- orbit representative:
  `(-5,-3,5,-3,-3,-3,5,5,5,-3,5)`.

So the actual order-11 quotient counts are, up to cyclic order and reversal,

`33,35,43,35,35,35,43,43,43,35,43`.

This is again highly rigid, but not yet contradictory.

Bottom line:

- the first quotient obstruction route fails as a direct nonexistence proof;
- the candidate now has a sharply narrowed compatibility problem rather than a vague open search.

## family_affinity
Strong. This sits in the abelian skew-Hadamard / Paley-parameter lane, but for a specific noncyclic survivor `C_11 x C_77 ≅ C_11^2 x C_7`. The quotient package is consistent with the standard "open table row" narrative.

## generalization_signal
Moderate. Two parts plausibly scale:

- the inert-prime parity argument for small prime-order quotients;
- the "flat spectrum plus bounded fibers" reduction to a finite quotient-profile problem.

What does not yet scale automatically is the final compatibility step across all quotient directions in `C_11^2`; that part is currently instance-specific.

## proof_template_reuse
If this closes by quotient obstruction, the reusable template is:

1. push to a small prime-order quotient,
2. derive exact centered autocorrelation equations,
3. use inert-prime or congruence arguments to force parity or residue restrictions,
4. enumerate the surviving quotient profiles exactly,
5. either show no profile survives or show the surviving profiles are globally incompatible.

That template looks reusable on nearby unresolved rows with quotient orders `7`, `11`, or similar.

## candidate_theorem_slice
Candidate slice visible already:

> Any `(847,423,211)` difference set in `C_11 x C_77` would have odd `C_7`-fiber counts over `C_11^2`; equivalently, every fiber size lies in `{1,3,5,7}`. Moreover, on every quotient of order `11`, the quotient intersection numbers are, up to dihedral symmetry, exactly `33,35,43,35,35,35,43,43,43,35,43`.

This is a real theorem-facing slice: it turns the open row into a concrete compatibility problem inside `AG(2,11)`.

## smallest_param_shift_to_test
The most informative nearby shifts are not new global parameter sets first; they are the smaller structural shadows of the same instance:

1. compatibility of the unique order-11 line-sum orbit with odd point weights in `{1,3,5,7}` on `AG(2,11)`;
2. compatibility of that order-11 orbit with the three allowed order-7 quotient profiles;
3. the one-parameter odd-fiber census `n_1,n_3,n_5,n_7`.

Those are the right "parameter shifts" because they stay inside the same theorem packet.

## why_this_is_or_is_not_publishable
If the main claim closes from the quotient obstruction, it is probably already `70-90%` of a paper. The exact title theorem would simply be the nonexistence or existence of a `(847,423,211)` difference set in `C_11 x C_77`. Remaining packaging would be light:

- brief source framing around the Gordon-Schmidt table row,
- the quotient-count lemmas,
- one short boundary remark about why the standard table machinery did not already force the contradiction.

At the current stage, the package is stronger than a generic instance note but still too thin for the micro-paper lane. It is best described as a `SLICE_CANDIDATE`: there is a genuine theorem slice, but not yet the title theorem.

## paper_shape_support
What would make the note paper-shaped if the main claim closes:

- one exact incompatibility between the unique order-11 line-sum orbit and odd point weights on `AG(2,11)`, or
- one exact incompatibility between that order-11 orbit and the three order-7 quotient profiles.

Either would give:

- a title theorem,
- a smallest supporting lemma slice,
- a natural remark on why this row resisted generic multiplier filters.

Immediate corollary / natural remark already visible:

> Any solution would force a very special weighted configuration on `AG(2,11)`: all point weights odd, only sizes `1,3,5,7` occur, every order-11 quotient has the same unique `33/35/43` line-sum pattern, and every order-7 quotient sits in one of three tiny orbit classes.

## boundary_remark
What scales:

- the inert-prime parity step on prime-order quotients;
- the centered autocorrelation reduction.

What does not yet scale automatically:

- the final affine-plane compatibility problem, which uses the special decomposition `847 = 7 * 11^2` and the `AG(2,11)` geometry.

So the current package is closer to a paper-shaped claim than a raw instance search, but it is still an instance-level structural packet until the final compatibility step closes.

## likely_failure_points
- The order-11 quotient system does admit a profile, so the first obstruction is definitely too weak by itself.
- The remaining step is a global compatibility problem on `AG(2,11)`, not a one-quotient obstruction.
- A pure character-value obstruction may require a multiplier theorem or cyclotomic argument stronger than I can justify locally without a source text.

## what_verify_should_check
- Recheck the quotient-count equations carefully, especially the kernel-size factors `77` and `7`.
- Verify the inert-prime step: `ord_11(2)=10`, hence `(2)` is prime in `Z[zeta_11]`, and from `C(zeta_11) * conjugate(C(zeta_11)) = 212` it follows that every order-11 quotient character value is divisible by `2`.
- Verify the `F_2` affine-plane claim that the only point-parity pattern with odd sum on every affine line of `AG(2,11)` is the all-ones pattern.
- Verify that the exact searches were exhaustive for:
  - the centered `C_7` quotient equations, and
  - the odd centered `C_11` quotient equations.
- Prior-art verification should specifically ask whether this exact quotient-obstruction argument is already implicit in the literature for the `[11,77]` row.

## verify_rediscovery
Bounded prior-art audit run on `2026-04-15` with limited web and the exact tuple as the anchor.

Search focus used:

- the exact tuple `(847,423,211)` with `C_11 x C_77`;
- alternate notation using group tag `[11,77]`;
- the canonical source title `A Survey of the Multiplier Conjecture`;
- same-source Table 2 coverage for the exact row;
- one bounded recent-status sweep for a later direct settlement.

What surfaced:

- the Gordon-Schmidt survey PDF still lists the exact row `(847,423,211)` in group `[11,77]` as open in Table 2;
- the bounded exact-tuple sweep did not surface a later paper, preprint, repository entry, proposition, example, or corollary explicitly settling this exact group-specific instance;
- no clear rediscovery evidence was established inside the time/browse budget.

Verification conclusion for PASS 1:

- `REDISCOVERY` was not established;
- the novelty basis remains source-table-based and should still be treated conservatively until a broader publication audit.

## verify_faithfulness
The solve artifact is faithful only as a structural slice, not as a solution of the intended statement.

What matches:

- the active packet, working packet, and solve record all target the exact intended statement: whether `C_11 x C_77` admits a `(847,423,211)` difference set;
- the quotient equations, fiber equations, and parity discussion are genuinely about that exact instance.

What must not be overstated:

- the artifact does **not** prove existence or nonexistence of the target difference set;
- it proves, at best, necessary conditions that any putative solution would have to satisfy;
- accordingly the run must remain `classification = PARTIAL`, not `EXACT`, not `CANDIDATE` for the title theorem, and not `VARIANT`.

## verify_proof
Arithmetic and reduction checks:

- the parameter identity `423 * 422 = 847 * 211` is correct;
- the order-11 quotient equations and the `C_11^2 x C_7` fiber equations are derived with the right kernel sizes and centered constants;
- the displayed order-11 representative `(-5,-3,5,-3,-3,-3,5,5,5,-3,5)` indeed has sum `5`, square sum `195`, and cyclic correlations `-17` for all nonzero shifts.

First substantive gap found:

- as written, the parity argument jumps too quickly from “the prime above `2` divides `C(zeta_11)`” to “every order-11 quotient coefficient is odd”;
- that implication is not immediate without the mod-`2` polynomial step.

Minimal conservative repair:

- write the quotient polynomial as `C(x) = sum_i c_i x^i` with `deg C <= 10`;
- because `ord_11(2) = 10`, the reduction of `Phi_11(x)` is irreducible over `F_2` and is the minimal polynomial of the image of `zeta_11` in `Z[zeta_11]/(2)`;
- divisibility of `C(zeta_11)` by the unique prime above `2` therefore implies that `C(x) mod 2` vanishes at a root of `Phi_11`, hence `Phi_11(x)` divides `C(x) mod 2`;
- since `deg C <= 10`, this forces `C(x) mod 2` to be either `0` or `Phi_11(x)`;
- but `C(1) = sum_i c_i = 423` is odd, so `C(x) mod 2` cannot be `0`;
- therefore `C(x) mod 2 = Phi_11(x) = 1 + x + ... + x^10`, and every `c_i` is odd.

With that repair inserted, the odd-line-sum and odd-fiber consequences are supported.

Residual caution:

- I independently rechecked the displayed order-11 orbit representative, but I did not rederive the full uniqueness-of-orbit claim from scratch inside this bounded verify pass;
- so the safe verified core is the odd-fiber theorem plus the validity of the displayed admissible order-11 profile, not a fresh independent proof that no other order-11 orbit exists.

## verify_adversarial
Reruns completed:

- exact `C_7` quotient search: rerunning the centered `7`-tuple system reproduced `42` raw solutions collapsing to exactly the same `3` dihedral classes recorded in the solve artifact:
  - `48,62,62,63,62,63,63`
  - `55,55,60,66,66,55,66`
  - `55,55,63,55,63,63,69`
- affine-plane parity check: exact Gaussian elimination over `F_2` on the `121` point variables and `132` affine-line equations gave rank `121`, consistent system, nullity `0`, so the all-ones parity pattern is unique;
- odd-fiber census: the one-parameter formulas for `(n_1,n_3,n_5,n_7)` reproduce the exact totals `121`, `423`, and `1689` for every `0 <= r <= 15`;
- displayed order-11 quotient profile: direct substitution confirms all ten nonzero cyclic correlations equal `-17`.

Adversarial conclusion:

- no counterexample to the checked structural claims was found;
- the only repair needed was to make the inert-prime-to-odd-coefficients step explicit.

## verify_theorem_worthiness
Exactness:

- the current artifact is not an exact proof of existence or nonexistence;
- it is a necessary-condition packet for a single exact instance.

Novelty:

- bounded PASS 1 did not establish rediscovery;
- however the novelty basis is still only “canonical row still appears open plus no direct later settlement surfaced,” so publication claims should remain cautious.

Reproducibility:

- moderate for the checked slice: the quotient arithmetic, the `C_7` exact search, the parity linear algebra, and the displayed order-11 profile are all reproducible with small local scripts;
- weaker for the stronger order-11 uniqueness wording, because that exact exhaustive rerun was not fully reconstructed here from a saved checker artifact.

Lean readiness:

- `false`;
- Lean is not the shortest remaining path, because the title theorem is still open and the main remaining work is mathematical compatibility, not formal sealing.

Paper leverage:

- if the exact title theorem were solved and novelty survived audit, one solve would still supply roughly `70-75%` of a publishable note;
- the currently verified slice alone is materially below that threshold and looks closer to `30-40%` of a note.

Title theorem actually visible now:

- the strongest honest theorem-shaped statement visible is:
  “Any `(847,423,211)` difference set in `C_11 x C_77` has odd `C_7`-fiber counts over `C_11^2`, hence fiber sizes only in `{1,3,5,7}`, and its small quotient shadows are extremely rigid.”

What scales:

- the inert-prime parity mechanism on prime-order quotients;
- the reduction of flat-spectrum conditions to small exact quotient-profile searches.

What clearly does not yet scale:

- the final global compatibility step in `AG(2,11)`;
- the unpublished order-11 uniqueness enumeration unless it is recorded as a durable checker or replaced by a cleaner proof.

Publication-status verdict:

- the target remains micro-paper-lane eligible **if the title theorem closes**;
- the current verified output is still publication-distant, so the best honest publication status for the present artifact is `NONE`, not `INSTANCE_ONLY` and not `SLICE_CANDIDATE`.

## verify_verdict
`MINOR_FIX`

Reason:

- no rediscovery was established;
- no checked structural claim failed;
- one proof step needed a conservative repair before the parity theorem could be accepted;
- the title theorem remains unsolved, so the run stays `classification = PARTIAL`.

## minimal_repair_if_any
Insert the explicit mod-`2` polynomial argument in the parity section:

1. define `C(x) = sum_i c_i x^i` for an order-11 quotient profile;
2. use the inertness of `2` to conclude `C(zeta_11)` reduces to `0` modulo the unique prime above `2`;
3. infer `Phi_11(x) | C(x) mod 2`;
4. use `deg C <= 10` and `C(1) = 423` odd to conclude `C(x) mod 2 = 1 + x + ... + x^10`;
5. conclude all quotient coefficients `c_i` are odd.

No broader edit is warranted in verify.

## publication_prior_art_audit
Bounded prior-art pass only.

Exact statement search:

- searched the exact tuple in bounded form: `"847,423,211" difference set`, `"847 423 211" difference set "11,77"`;
- surfaced the Gordon-Schmidt survey and no later page asserting existence or nonexistence for the exact row.

Alternate notation search:

- checked `"[11,77]" difference set`, `"C_11 x C_77" difference set`, and `"C_11^2 x C_7" difference set 847`;
- again surfaced the survey framing and no direct later settlement.

Canonical source check:

- Gordon-Schmidt, *A Survey of the Multiplier Conjecture* (2015), Table 2, still lists the exact row `(847,423,211)` in group `[11,77]` as open;
- bounded PDF checking surfaced the row itself but no theorem / proposition / example / corollary / observation in that source settling the exact group-specific case.

Outside-source status pass:

- the Dan Gordon difference-set repository remains a live status surface for difference-set data, but the bounded pass surfaced no row-specific update or later claim resolving `(847,423,211)` in `C_11 x C_77`.

Audit verdict:

- no rediscovery was established in the bounded audit;
- however the novelty basis is still narrow: “canonical open row plus no later direct settlement surfaced.”

## publication_statement_faithfulness
The current artifact is faithful to the intended statement only as a conditional structural reduction.

- faithful: it studies the exact intended row `(847,423,211)` in `C_11 x C_77`;
- faithful: it does not overclaim existence or nonexistence;
- not yet faithful to a title-theorem announcement of the form “we determine whether ...”, because the row is still unsolved in the current packet;
- the strongest safe wording is necessary-condition language for any putative difference set, not closure of the Table 2 row.

## publication_theorem_worthiness
The strongest honest claim is stronger than “here is an example,” but weaker than the hoped-for title theorem.

- theorem slice visible: odd `C_7`-fiber parity over `C_11^2` together with sharply restricted order-`7` and order-`11` quotient profiles;
- structural content: the parity argument is structural and conceptually reusable;
- instance dependence: the surviving quotient-profile package is still heavily tuned to this one row and to the unresolved `AG(2,11)` compatibility step;
- referee test: there is an answer to “what is the theorem?”, but today it reads as a preparatory obstruction theorem, not yet as the obvious title theorem of a micro-paper;
- proof-state caveat: the parity argument needs the explicit mod-`2` repair from verify absorbed into the permanent record before even that slice should be treated as stable.

## publication_publishability
This is not yet most of a publishable note.

- would the current bounded result already constitute most of a paper: no;
- estimated current single-solve-to-paper fraction: about `0.38`, not the pre-audit `0.74`;
- title theorem / theorem slice: a real slice exists, but it is not the row-closing theorem the packet was selected for;
- proof character: partly structural, partly instance-specific;
- dependence on hand-picked small cases: still material, because the surviving quotient classes and the unresolved global compatibility step remain highly instance-bound;
- referee risk: a referee asking “what is the theorem?” would get a real answer, but likely also ask why the row itself remains open and why the current slice alone warrants publication.

Bottom line:

- the candidate looked close to paper before audit because a full solve of the exact row would indeed be paper-shaped;
- the current packet is farther away than that pre-audit picture suggested;
- if this does not close by a short same-lane compatibility argument, it should be moved aside rather than expanded into a broader theorem program.

## publication_packet_audit
Packet verdict for the current artifact:

- publication status: `NONE`;
- publication confidence: `medium`;
- publication packet quality: `partial`;
- proof artifacts preserved: `true`;
- human-ready: `false`;
- Lean would not directly seal the packet into a publishable result; it would only formalize a still-subtitle-level slice.

## micro_paper_audit
Micro-paper leverage remains conditional on closing the exact row.

- if the exact existence/nonexistence theorem were proved, the original curation logic would still be sound and the note would likely be short;
- for the current packet alone, the leverage is below micro-paper threshold;
- the safe micro-paper assessment is: lane-eligible at the target level, but not yet paper-shaped at the achieved-result level;
- do not widen this into a feeder-ladder or broader program; only continue if the same exact row admits a short compatibility closure from the present slice.

## strongest_honest_claim
The current packet gives a nontrivial necessary-condition reduction for the exact open row: any putative `(847,423,211)` difference set in `C_11 x C_77` would have odd `C_7`-fiber counts over `C_11^2`, hence fiber sizes only in `{1,3,5,7}`, and would have extremely rigid small-quotient shadows. This is theorem-shaped progress, but it is not yet a determination of existence or nonexistence for the row itself.

## paper_title_hint
Necessary Conditions for a `(847,423,211)` Difference Set in `C_11 x C_77`

## next_action
Either close the remaining global compatibility obstruction in the same exact row, or cool this candidate and move it aside. Do not broaden into a larger theorem program, and do not spend the next cycle on Lean-first formalization.
