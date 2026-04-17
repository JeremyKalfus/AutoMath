# Solve Record: Does the cyclic group C_1801 admit a (1801,225,28)-difference set?

- slug: `cyclic-difference-set-1801-225-28`
- working_packet: `artifacts/cyclic-difference-set-1801-225-28/working_packet.md`

## statement_lock
Determine whether the cyclic group C_1801 admits a (1801,225,28)-difference set.

Exact intended theorem for this solve pass: either prove that no cyclic difference set with parameters `(1801,225,28)` exists, or isolate a sharply bounded orbit-level obstruction package that makes one remaining finite check the only unresolved step. If the negative result closes, the exact title theorem would be: `The cyclic group C_1801 does not admit a (1801,225,28)-difference set.`

Micro-paper test at solve start: a real disproof here would already be about `70-90%` of a short paper, because the row is a source-isolated residual cyclic case and the remaining packaging would mostly be a short source comparison plus proof exposition.

## definitions
Work additively in `G = Z/1801Z`. A `(1801,225,28)` difference set is a subset `D ⊂ G` of size `225` such that every nonzero element of `G` has exactly `28` representations as `d1 - d2` with `d1,d2 ∈ D`.

Set `n = k - λ = 197`, which is prime. The active source packet points to Baumert-Gordon Theorem `3.2` as the multiplier input for rows with `n = 197`.

Important arithmetic facts for this row:

- `1801` is prime, so the only additive quotients of `G` are trivial and full. This removes the usual small-divisor contraction lane.
- `gcd(197 - 1, 1801) = gcd(196, 1801) = 1`. Therefore, if Theorem `3.2` yields `197D = D + s`, then translation by a suitable `y` with `(197 - 1)y = s` normalizes the situation to exact invariance `197(D - y) = D - y`.
- Direct modular arithmetic gives `197^4 ≡ 2 (mod 1801)` and `2^25 ≡ 1 (mod 1801)` with `2^5 ≠ 1`, so `ord_1801(2) = 25`. Since `197 = 2^19 (mod 1801)`, also `ord_1801(197) = 25`.
- Thus, after normalization to exact `197`-invariance, the nonzero elements of `G` split into `72 = 1800 / 25` multiplier orbits of size `25`, and `0` is the only fixed point.
- Because `225` is divisible by `25`, any exactly `197`-invariant candidate must be a union of exactly `9` nonzero `25`-orbits, and in particular `0 ∉ D`.

Conventions and ambiguities:

- I am treating the multiplier conclusion as source-licensed but still solve-stage provisional until verify checks the exact theorem statement.
- Since `v` is prime, any progress here has to come from full-group orbit structure, additive character sums, or finite orbit algebra. There is no honest small-quotient contraction shortcut available.

## approach_A
Structural / invariant route.

1. Use the source-indicated multiplier theorem with `n = 197` to normalize to exact `197`-invariance.
2. Replace the unknown `225`-set by a much smaller object: a choice of `9` among the `72` nonzero `25`-orbits.
3. Push the difference-set equations onto this orbit algebra. Since the full difference multiset is uniform and the multiplier subgroup preserves differences, the ordered-difference count depends only on the `72` orbit classes.
4. Try to force a contradiction from exact orbit-level bookkeeping before any wide search:
   - `0 ∉ D`
   - each additive character sum is constant on the same `25`-orbits in the dual group
   - the orbit indicator has only `9` active classes among `72`
5. If needed, do one bounded exact experiment on the orbit algebra or on the induced character equations, but only after the theorem-facing skeleton is written down.

Self-check after approach A: this is the natural source-aligned lane. Prime `v` removes the contraction machinery, so the multiplier orbit structure has to carry most of the proof.

## approach_B
Construction / extremal / contradiction route.

Exploit exact orbit invariance to derive vanishing additive power sums in `F_1801`. If `D` is a union of `25`-orbits under multiplication by `197`, then for each `1 <= r <= 24`,

- `sum_{d in D} d^r = 0 (mod 1801)`

because each orbit is a multiplicative coset of a subgroup of order `25`, whose `r`-th power sum vanishes unless `25 | r`.

Then combine these vanishings with the difference-set moment identities

- `sum_{x,y in D} (x - y)^m = 28 * sum_{g != 0} g^m`

for carefully chosen exponents `m`, starting with multiples of `25`. This compresses the problem to moment data of a `9`-point subset in the `72`-element quotient `F_1801^× / <197>`.

Potential gain:

- this route may turn the full difference-set condition into a rigid recurrence on orbit moments without ever enumerating subsets of `G`.

Risk:

- the resulting moment system may still leave multiple orbit-level survivors, in which case it becomes only a theorem slice rather than a full disproof.

Self-check after approach B: this is genuinely different from approach A. It trades direct orbit-counting for finite-field moment identities and may reveal a hidden obstruction if the raw orbit algebra stays loose.

## lemma_graph
Current proof skeleton:

1. Source multiplier input: because `197 | n` and `gcd(197,1801)=1`, Baumert-Gordon Theorem `3.2` should imply `197D = D + s`.
2. Since `gcd(197 - 1,1801)=1`, translate by `y` with `(197 - 1)y = s` to get exact invariance `197D = D`.
3. Compute the multiplier order:
   - `197^4 ≡ 2 (mod 1801)`
   - `2^25 ≡ 1 (mod 1801)` and `2^5 ≠ 1`
   - hence `ord_1801(197) = 25`
4. Therefore `D` is a union of one fixed-point orbit `{0}` and some number of nonzero `25`-orbits. Since `225 ≡ 0 (mod 25)`, exact invariance forces `0 ∉ D` and `D` to be a union of exactly `9` nonzero multiplier orbits.
5. The difference-set equations now live on the `72` nonzero orbit classes. Any proof must either:
   - show that no `9`-orbit union has uniform nonzero difference count `28`, or
   - show that the induced character or moment constraints on such a union are impossible.
6. If the main disproof closes, the smallest natural supporting theorem slice is: `Any cyclic (1801,225,28) difference set can be translated to a union of exactly nine nonzero 25-cycles under multiplication by 197.`

Self-check after lemma graph: this is a real, row-specific theorem slice and not just rephrased packet metadata. It sharply reduces the search space from `225` unknown elements to `9` orbit classes.

## chosen_plan
Choose approach A first, with approach B as the fallback if the orbit algebra remains underdetermined.

Reason:

- the prime-order setting leaves no small quotient to exploit, so exact multiplier invariance is the cleanest structural reduction available;
- the order-`25` orbit decomposition is already strong enough to force `0 ∉ D` and reduce the candidate to a `9`-orbit union;
- if a contradiction appears at that orbit level, the result is immediately paper-shaped;
- if not, the moment route in approach B is the next honest refinement rather than a concept drift into broad search.

Extra structure that would make the result paper-shaped if the main claim closes:

- the exact normalization lemma `197D = D` after translation,
- the orbit-count lemma `D` is a union of exactly nine nonzero `25`-orbits,
- one finite obstruction proposition on the `72` orbit classes or their induced moments,
- one short remark explaining why prime `v = 1801` forces the proof away from contraction and into full-group orbit algebra.

## self_checks
- Arithmetic check: `1801` is prime, so there is no hidden nontrivial additive quotient available for a contraction argument.
- Multiplier-normalization check: `gcd(196,1801)=1`, so exact invariance really is obtainable from an affine multiplier claim.
- Orbit-size check: `197 = 2^19 (mod 1801)` and `ord(2)=25`, so the nonzero multiplier orbits do have size `25`.
- Size check: `225 = 9 * 25`, so exact invariance forces exclusion of the fixed point `0`.
- Orbit-algebra check after the bounded experiment: for the `72` indexed nonzero `25`-orbits `C_i`, each ordered pair kernel `C_a - C_b` contributes counts that are all multiples of `25`, and the reduced kernel satisfies the exact translation law `K_{a,b}(j) = K_{0,b-a}(j-a)`. So an exact search on the `72` orbit classes is mathematically faithful to the full difference-set condition after multiplier normalization.
- Publication check: if the solve ends only at the “nine multiplier orbits” lemma, that is still too thin for the micro-paper lane by itself; it needs either a contradiction or a much sharper orbit obstruction.

## code_used
Minimal code was used after the reasoning checkpoint.

Bounded experiments performed:

1. Exact orbit construction under multiplication by `197` in `F_1801^×`.
   - confirmed there are exactly `72` nonzero orbits, each of size `25`;
   - confirmed the reduced difference kernels between orbit pairs are integral after division by `25`.
2. Exact reduced-kernel inspection.
   - self-difference of one orbit hits exactly `24` target orbit classes, with reduced count `1` on each;
   - distinct ordered orbit pairs produce reduced kernels with support sizes between `13` and `23`, and coefficient values in `{1,2,3,4}`;
   - the pair kernels obey the translation law expected from cyclotomic indexing, so the whole obstruction lives naturally on `Z/72Z`.
3. Bounded exact backtracking on the `72` orbit classes, normalized by fixing one selected orbit.
   - target: choose `9` orbit classes whose exact reduced difference counts are `28` on every target orbit class;
   - the search explored `27,531` nodes in `20` seconds and reached depth `8` without finding a solution or proving infeasibility.

This was an orbit-level checker only. No SAT, ILP, CP-SAT, or full-group brute force was used.

## result
Current strongest honest result:

- conditional on the source multiplier input, any cyclic `(1801,225,28)` difference set can be translated to an exactly `197`-invariant set;
- such a normalized set must be a union of exactly `9` nonzero multiplier orbits of size `25`;
- the prime-order nature of `v = 1801` means the remaining work is full-group orbit algebra or moment obstruction, not quotient contraction;
- the orbit reduction is exact: after dividing by `25`, the full difference-set condition becomes a `72`-class reduced-kernel problem with target count `28` on each orbit class.

New exact but nondecisive information from the bounded experiment:

- for the indexed nonzero orbit classes `C_i`, the self-kernel `C_i - C_i` has reduced support size `24` and reduced value `1` on each supported class;
- distinct ordered orbit pairs have reduced support sizes in `{13,18,20,21,22,23}` and reduced coefficient patterns built from values `1,2,3,4}`;
- a straightforward exact backtracking pass on the `72`-class system did not close the row within the bound.

This is theorem-facing but not yet a solve. At this checkpoint the classification remains a structural partial, now sharpened to an exact orbit-scheme obstruction problem.

## family_affinity
High affinity with residual cyclic-row nonexistence problems solved by a prime multiplier plus orbit compression. The unusual feature here is that the whole obstruction must occur on the full prime-order group rather than on a helpful proper quotient.

## generalization_signal
Moderate positive signal.

What clearly scales:

- using a prime divisor of `n` to get a numerical multiplier,
- killing the translation parameter when `gcd(t - 1, v) = 1`,
- reducing the candidate to a union of full multiplier orbits.

What does not obviously scale:

- the specific order computation `ord_1801(197) = 25`,
- any later orbit-algebra contradiction on `72` classes,
- any finite moment obstruction tied to the exact pair `(v,n) = (1801,197)`.

If a disproof closes, the scalable part is the normalization-and-orbit template. The row-specific part is whatever finally kills the `9` orbit classes.

## proof_template_reuse
Reusable template visible already:

1. identify a prime multiplier from `n`,
2. normalize affine multiplier symmetry to exact multiplier symmetry using `gcd(t - 1, v) = 1`,
3. compute the resulting orbit sizes on the full cyclic group,
4. convert the target into a small orbit-selection problem,
5. finish with either orbit algebra or a bounded finite-field moment obstruction.

This template is most reusable for prime-order cyclic rows where small-divisor contraction is unavailable and the multiplier order is moderate.

## candidate_theorem_slice
Candidate theorem slice:

Let `D ⊂ C_1801` be a cyclic `(1801,225,28)` difference set. Assuming the Baumert-Gordon multiplier conclusion for `n = 197`, there is a translate of `D` that is fixed by multiplication by `197`. For that normalized translate, `0 ∉ D` and `D` is a union of exactly `9` nonzero `25`-element orbits of the action `x -> 197x`.

Sharper current slice:

After choosing a primitive-root indexing `C_0,...,C_71` of those nonzero `25`-orbits, the exact difference-set condition is equivalent to selecting `9` indices such that the reduced ordered-difference kernel on orbit classes is identically `28` on every target class.

This is a real structural slice, but still not enough on its own for publication because the final orbit-scheme contradiction is still missing.

## smallest_param_shift_to_test
The smallest informative parameter shift would be another prime-order cyclic row where:

- `v` is prime,
- `n` has a prime multiplier `t`,
- `ord_v(t)` is moderate and forces a small number of full nonzero orbits.

Within the current row, the immediate internal “parameter shift” is not a new tuple but a sharper invariant: move from the raw `9`-orbit decomposition to one induced quotient object on the `72` multiplicative orbit classes.

The best next internal shift is to replace naive backtracking by a more structured cyclotomic or moment compression on the `72`-class orbit scheme.

## why_this_is_or_is_not_publishable
Not publishable yet.

The current packet has a genuine theorem slice and a strong route, but it does not yet settle the main row or produce a sufficiently sharp obstruction theorem. If the solve stopped here, the output would still be too thin for the micro-paper lane.

If the main disproof closes from this setup, the solve would likely already be around `70-90%` of a paper. The minimal remaining packaging would be:

- cite the exact Baumert-Gordon multiplier input,
- state the normalization lemma and orbit-count proposition cleanly,
- present the final orbit obstruction,
- add one short boundary remark on why prime `v` prevents the standard contraction lane.

## paper_shape_support
Paper-shape support if the main claim closes:

- exact title theorem: `The cyclic group C_1801 does not admit a (1801,225,28)-difference set.`
- immediate theorem support already visible: normalization to exact `197`-invariance and reduction to nine nonzero `25`-orbits.
- natural immediate remark: the case is not killed by routine small-divisor contraction because `1801` is prime; the proof has to happen directly in the full cyclic group.
- natural paper narrative: one residual Table 3 row survives the standard filters, but the prime multiplier forces an orbit configuration that the final orbit algebra or moment argument rules out.

## boundary_remark
Boundary remark currently visible:

The reduction to nine multiplier orbits is strong but not by itself decisive. The bounded experiment shows that the row is not killed by an immediate shallow backtracking on the `72` orbit classes. If the eventual obstruction comes from a compact cyclotomic identity or moment lemma on that `72`-class scheme, the package stays close to paper-shaped. If it ultimately needs a large exhaustive subset search on orbit classes, the result becomes thinner and publication value drops.

## likely_failure_points
- The exact statement of the Baumert-Gordon multiplier theorem still needs verify-stage auditing.
- The orbit reduction may still leave too many `9`-orbit unions, forcing a search-heavy residue problem rather than a clean contradiction.
- The moment equations may constrain but not uniquely kill the quotient data.
- The current exact backtracking on the orbit scheme is too weak to decide the row; without a sharper pruning invariant, the solve can stall short of a theorem.
- Because `v` is prime, there is no easy fallback to a lower-order contraction theorem; if the full-group orbit lane fails, this solve pass may end only at a structural slice.

## what_verify_should_check
- Verify that Baumert-Gordon Theorem `3.2` really licenses the affine multiplier statement for `t = 197` in the cyclic `(1801,225,28)` row.
- Verify the exact normalization step from `197D = D + s` to `197D = D`.
- Recheck the modular arithmetic:
  - `197^4 ≡ 2 (mod 1801)`
  - `2^25 ≡ 1 (mod 1801)`
  - `ord_1801(197) = 25`
- Verify the orbit-kernel claims:
  - reduced pair-kernel counts are divisible by `25`,
  - the indexed kernels satisfy the translation law on `Z/72Z`,
  - the bounded search was only on the exact `72`-class reduced system and not on the full group.

## verify_rediscovery

- PASS 1 used a bounded live web audit on 2026-04-15 over the exact tuple `(1801,225,28)`, alternate notation such as `1801 225 28` and `cyclic (1801,225,28) difference set`, the canonical Baumert-Gordon 2004 source, same-source checks around Table `3` / Theorem `3.1` / Theorem `3.2`, and the current DM Gordon difference-set surface.
- Within that budget I did not find a later paper, theorem, proposition, example, observation, corollary, or repository entry explicitly settling the exact cyclic row `(1801,225,28)`.
- The canonical source still appears to be the frontier anchor for this exact row, and the bounded audit did not establish rediscovery.
- Conclusion for PASS 1: `verify_verdict` is not `REDISCOVERY`.

## verify_faithfulness

- The artifact is mostly faithful about scope: it does not claim to have proved the intended statement `Does the cyclic group C_1801 admit a (1801,225,28)-difference set?`
- The actual mathematical content is narrower and conditional. What is really supported is an orbit-reduction package of the form: if the Baumert-Gordon multiplier input applies as stated, then a putative difference set can be translated to an exactly `197`-invariant union of nine nonzero `25`-orbits.
- I did not find wrong-theorem drift, quantifier drift, changed definitions, or a swap to a nearby tuple. The main faithfulness issue is classificatory: the current record sometimes reads like theorem-facing progress toward nonexistence, but the verified content is still only a conditional structural slice.
- Because the exact intended statement is unresolved, the classification cannot exceed `PARTIAL` at this stage.

## verify_proof

- First incorrect step found: none in the checked arithmetic and orbit-structure claims after assuming exact `197`-invariance.
- Fresh local checks confirmed:
  - `197^4 ≡ 2 (mod 1801)`,
  - `2^25 ≡ 1 (mod 1801)` and `2^5 = 32 != 1`,
  - `ord_1801(2) = ord_1801(197) = 25`,
  - `gcd(197 - 1,1801) = 1`,
  - the nonzero residues split into exactly `72` multiplier orbits of size `25`.
- The normalization step from an affine multiplier relation `197D = D + s` to exact invariance is mathematically correct: if `(197-1)y = s`, then `197(D-y) = D-y`.
- The main proof gap is still decisive rather than local: this record does not prove nonexistence, and this verification run did not re-establish from a local source copy that Baumert-Gordon Theorem `3.2` applies to this row exactly as needed. So the strongest honest claim remains conditional.

## verify_adversarial

- There is no checked-in local solver script or checker file in this artifact directory to rerun directly, so I reproduced the key finite computations from scratch in a fresh shell script.
- The fresh computation confirmed the orbit arithmetic claimed in the record:
  - the `197`-action on `(Z/1801Z)^x` has `72` orbits, all of size `25`,
  - with a primitive-root coset indexing, the reduced pair-kernel translation law on `Z/72Z` holds exactly,
  - every nonzero reduced pair-kernel coefficient is integral after division by `25`,
  - self-kernels have support size `24` with reduced value `1`,
  - distinct pair kernels have support sizes in `{13,18,20,21,22,23}` with reduced coefficient values in `{1,2,3,4}`.
- Adversarial conclusion: the local orbit computations survive skeptical rerun, but they still support only a conditional reduction, not a proof or disproof of the tuple.

## verify_theorem_worthiness

- Exactness: the target theorem is exact and still micro-paper-shaped if solved, but the current verified artifact is not an exact theorem or exact counterexample.
- Novelty: bounded PASS 1 checking did not establish rediscovery, so the row still looks plausibly frontier-novel within audit budget.
- Reproducibility: the arithmetic/orbit package is reproducible from scratch, but the decisive source-licensed multiplier step still needs explicit source anchoring in the artifact before this becomes a stable theorem packet.
- Lean readiness: `false`. Lean is not the shortest remaining path because the missing work is mathematical closure and source-faithful theorem locking, not formal sealing.
- Paper leverage: if the exact row were solved cleanly, one solve would still likely provide about `70-80%` of a publishable short note. But the present packet is materially short of that threshold.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No. Lean-sealing the current packet would only formalize a conditional orbit reduction, not the title theorem.
- What percentage of the paper would one solve already provide? Still about `0.72` for the underlying target, but the current verified artifact supplies substantially less than that because the contradiction or witness is missing.
- What title theorem is actually visible? Only the conditional slice: assuming the Baumert-Gordon multiplier conclusion, any cyclic `(1801,225,28)` difference set can be translated to a union of exactly nine nonzero `25`-orbits under multiplication by `197`.
- What part of the argument scales? The affine-multiplier normalization, orbit-size computation, and reduction to an orbit-class kernel system.
- What part clearly does not? Any eventual contradiction on the exact `72`-class reduced system looks row-specific, and the present bounded search does not yet isolate a publication-ready obstruction.
- Best honest publication status now: `NONE`, not `INSTANCE_ONLY` and not `SLICE_CANDIDATE`, because the current verified packet is still a conditional structural reduction rather than a near-complete theorem note.

## verify_verdict

- `UNVERIFIED`
- Classification remains `PARTIAL`.
- Reason: PASS 1 did not establish rediscovery, the local arithmetic/orbit computations check out, but the artifact still does not prove the intended exact statement and the key source multiplier input remains only conditionally invoked in this run.
- `lean_ready` must remain `false`, and `lean_packet_seal` must remain `false`.

## minimal_repair_if_any

- No mathematical repair was applied.
- Verify-stage conservative repair was classificatory:
  - keep the slug at `PARTIAL`,
  - do not send this packet to Lean.
- Publication audit below resolves the source-faithfulness hinge for Baumert-Gordon Theorem `3.2` and supersedes the earlier conditional-publication reading.

## publication_prior_art_audit

Bounded publication audit completed on 2026-04-15.

- Exact-statement web search using the exact tuple `(1801,225,28)` together with cyclic-language variants did not surface a later paper, note, or repository page explicitly settling the exact cyclic `C_1801` row.
- Alternate-notation search using bare parameter strings such as `1801 225 28`, together with `C_1801`, `n = 197`, and `cyclic difference set`, was noisy but did not produce a mathematically relevant later settlement; the useful hits collapsed back to the Baumert-Gordon / Gordon web surface.
- Canonical-source check: Baumert-Gordon 2004 Theorem `3.2` states that if `w | v`, `gcd(t,w) = 1`, and for each prime factor `p_i` of `n` there is `j = j(i)` with `p_i^j ≡ t (mod w)`, then `t` is a `w`-multiplier. For this row, `w = v = 1801`, `n = 197`, the only prime factor of `n` is `197`, and `t = 197`, so the theorem directly licenses `197` as an `1801`-multiplier for any cyclic `(1801,225,28)` difference set.
- The same canonical source still lists `1801 225 28 197` in Table `3` among the remaining possible cyclic cases with `150 <= k <= 300` and `gcd(v,n) = 1`.
- Same-source theorem / proposition / example / corollary / observation / sufficient-condition check: Baumert-Gordon 2004 does prove neighboring explicit nonexistence theorems such as Theorem `3.3` for `(429,108,27)` and `(303,151,75)`, but in the bounded read I did not find any theorem, proposition, corollary, observation, example, or sufficient condition in that paper already settling the exact cyclic row `(1801,225,28)`.
- Outside-source status pass: Gordon's current Difference Sets page still presents a maintained searchable database with a status filter including `open`, and Gordon's publications page still serves as the live outside-source surface for later difference-set work. Inference: within this bounded outside-source pass, I did not see any post-2004 Gordon web surface exposing an explicit settlement of `(1801,225,28)`.
- Recent follow-up check, used only because the frontier anchor is from 2004: Gordon's publications page lists the 2022 paper `On difference sets with small lambda`, but a direct text check of that PDF found no occurrence of `1801`, so the bounded recent pass did not reveal a later exact discharge of this row there either.

Audit verdict: no rediscovery surfaced in the bounded pass. This remains a narrow exact-row audit rather than an exhaustive literature guarantee.

## publication_statement_faithfulness

- The intended statement stays locked to the exact row: determine whether the cyclic group `C_1801` admits a `(1801,225,28)` difference set.
- The main faithfulness repair relative to verify is now complete: the multiplier step is no longer merely assumed. Baumert-Gordon Theorem `3.2` does apply directly to this exact row, so the affine `197`-multiplier claim is source-faithful within the bounded audit.
- Therefore the strongest local content is now an unconditional theorem slice, not a conditional one: any cyclic `(1801,225,28)` difference set can be translated to an exactly `197`-invariant set; since `ord_1801(197) = 25`, that normalized set is a union of exactly `9` nonzero `25`-element multiplier orbits.
- There is no tuple drift, quantifier drift, or theorem drift. The unresolved issue is only that this exact reduction theorem still stops short of settling existence or nonexistence.

## publication_theorem_worthiness

- The strongest honest claim is stronger than “here is an example.” It is a real exact-row structural theorem slice.
- A referee asking “what is the theorem?” can now be answered cleanly:

  `Any cyclic (1801,225,28) difference set is, up to translation, a union of exactly nine nonzero 25-cycles under multiplication by 197; equivalently, the row reduces to an exact 72-class reduced-kernel equation.`

- The proof is structural rather than a hand-picked small-case computation. It uses a canonical multiplier theorem, affine normalization, multiplicative orbit structure in the full prime-order group, and exact orbit-kernel bookkeeping.
- Even so, this is not yet the title theorem of the desired micro-paper. The missing step is still the row-closing obstruction on the exact `72`-class system, and that remaining step is the mathematical core rather than light exposition.
- The claim is not overly dependent on hand-picked tiny cases, but it is still arithmetic-specific to one row's order-`25` orbit scheme.
- Best theorem-worthiness verdict: exact and theorem-real slice, but still a slice rather than the final residual-case theorem.

## publication_publishability

- If the exact row were solved cleanly, the original leverage story still survives audit: one solve would likely provide about `0.72` of a short publishable note.
- The current audited packet does not already constitute most of such a note. It supplies an exact structural reduction theorem, but not the decisive nonexistence proof or construction.
- So the candidate did not merely look attractive before audit. The target is still genuinely paper-worthy if closed. What changed is that the current packet is better than a conditional scaffold but still materially short of a publishable row-closing note.
- The remaining gap is not tiny. It is smaller and cleaner than before because the multiplier hinge is closed, but it is still the hard last obstruction, not just editorial cleanup.
- If the row does not close in one more bounded same-lane pass, this packet should be moved aside rather than expanded into a broader theorem program.
- Lean would not directly seal the intended publication packet today. Formalization would presently seal only the orbit-reduction theorem slice, so Lean is optional archival polish rather than the next blocking step.

## publication_packet_audit

- Best honest publication status now: `SLICE_EXACT`.
- `PAPER_READY` is not justified because the title theorem `C_1801` nonexistence/existence question is still unresolved.
- `NONE` is now too pessimistic, because the source audit upgrades the packet from a conditional reduction to an exact theorem slice with a clean statement.
- Packet quality verdict: exact structural slice preserved, but not note-shaped.
- Proof artifacts are preserved well enough for continuation: the record contains the source-anchored multiplier theorem use, the exact affine-normalization step, the orbit computation, and the reduced-kernel formulation.

## micro_paper_audit

- Is the strongest honest claim stronger than “here is an example”? Yes.
- Would one correct solve already constitute most of a publishable note? Yes, still about `72%`.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Yes: there is a real exact theorem slice, but not yet the intended title theorem.
- Is the proof structural or merely instance-specific? Structural, though row-specific.
- Would this survive a referee asking “what is the theorem?” Yes, as a reduction theorem; no, not yet as the final residual-case note.
- Is the claim still too dependent on hand-picked small cases? No in method, though yes in the sense that the remaining obstruction is specific to one `72`-class orbit scheme.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? The candidate still looks genuinely attractive, but the remaining gap is not genuinely small; it is still the decisive last obstruction.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes, if one more bounded same-lane attempt does not close the `72`-class system quickly.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Only optional later archival formalization for the slice.

MICRO-PAPER verdict: the target remains lane-eligible, and this audit upgrades the packet to an exact theorem slice. But it is still below HUMAN_READY because the selected row itself is not yet settled.

## strongest_honest_claim

Any cyclic `(1801,225,28)` difference set can, by Baumert-Gordon Theorem `3.2`, be translated to an exactly `197`-invariant subset of `C_1801`. Since `ord_1801(197) = 25`, the normalized set must be a union of exactly `9` nonzero `25`-element multiplier orbits. Equivalently, the existence problem for the selected row reduces exactly to a `72`-class reduced-kernel difference equation with target value `28` on every orbit class.

## paper_title_hint

A `197`-Multiplier Orbit Reduction for the Cyclic `(1801,225,28)` Difference-Set Problem

## next_action

Do not promote this packet to HUMAN_READY. Run at most one more bounded same-lane pass aimed at a clean contradiction on the exact `72`-class reduced system, preferably via a cyclotomic or moment obstruction rather than wider search. If that pass does not close quickly, cool the slug and preserve this exact slice rather than enlarging the theorem program.
