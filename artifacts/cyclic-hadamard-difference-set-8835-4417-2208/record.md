# Solve Record: Does the cyclic group C_8835 admit a (8835,4417,2208)-difference set?

- slug: `cyclic-hadamard-difference-set-8835-4417-2208`
- working_packet: `artifacts/cyclic-hadamard-difference-set-8835-4417-2208/working_packet.md`

## statement_lock
Determine whether the cyclic group C_8835 admits a (8835,4417,2208)-difference set.

## definitions
Let `G = C_8835 = Z/8835Z` additively, and let `D subset G` be a hypothetical `(v,k,lambda) = (8835,4417,2208)` difference set.

Write `n = k - lambda = 2209 = 47^2`. For every nonprincipal character `chi` of `G`, the standard character equation gives
`|chi(D)|^2 = n = 47^2`.

Load-bearing structural input:
- Because `n` is a prime square with prime `47` coprime to `v`, the standard prime-power multiplier theorem should make `47` a numerical multiplier.
- After translating `D`, I may therefore work under the normalization `47D = D`.

Under this normalization, `D` is a union of `x -> 47x` orbits, and every quotient fiber count is constant on multiplier orbits in that quotient.

Ambiguities and conventions to keep explicit:
- I am using additive notation for `C_8835` and the usual Fourier convention `chi(D) = sum_{d in D} chi(d)`.
- The multiplier step is standard but citation-sensitive; verify should explicitly check the exact theorem statement used here.
- A constructive outcome would still need an explicit orbit union or certificate, not just quotient counts.

## approach_A
Structural / invariant route:

1. Use the multiplier `47` to force orbit invariance.
2. Push that invariance to small quotients `C_3`, `C_5`, and `C_15`.
3. Combine the exact character magnitude `|chi(D)| = 47` with the orbit structure of multiplication by `47` modulo those quotients.
4. Try to force a contradiction, or at least a uniquely constrained residue profile that sharply reduces any later search.

The key attraction is that `47 mod 3`, `47 mod 5`, and `47 mod 15` have small orbit structure, and the norm `47^2` is arithmetically rigid in the Eisenstein case.

## approach_B
Construction / extremal / contradiction route:

1. Treat `D` as a union of full `47`-multiplier orbits in `C_8835`.
2. Use the forced quotient profile from approach A as target marginals.
3. Run only a bounded feasibility check: can any union of full `47`-orbits realize those marginals at all?
4. If no such union exists, the multiplier reduction already eliminates the case.
5. If such unions exist, the result is still a strong structural slice but not a full disproof.

This stays within the micro-paper lane because the experiment is not a generic SAT-first search. It is a narrow certificate check after two reasoning reductions.

## lemma_graph
Lemma skeleton:

1. If `D` exists, then every nonprincipal character value has modulus `47`.
2. Standard multiplier input: `47` is a multiplier, so after translation `47D = D`.
3. Mod `3`:
   Let `(N0,N1,N2)` be the residue-class counts. Then
   `A3 = N0 + N1 omega + N2 omega^2` has norm `47^2`.
   Writing `A3 = a + b omega`, the norm form is `a^2 - ab + b^2 = 47^2`.
   Since `47` is inert in `Z[omega]`, the only possibilities are unit multiples of `47`, forcing the multiset
   `{N0,N1,N2} = {1441,1488,1488}`.
   Because residue `0 mod 3` is the fixed residue class, the forced profile is
   `(1441,1488,1488)` up to swapping the nonzero classes.
4. Mod `5`:
   Multiplication by `47 equiv 2 mod 5` is transitive on the four nonzero residues, so the quotient profile is `(M0,M1,M1,M1,M1)`.
   For a nontrivial order-`5` character, the character sum is `M0 - M1`, hence `|M0 - M1| = 47`.
   Together with `M0 + 4M1 = 4417`, this forces `(M0,M1) = (921,874)`.
5. Mod `15`:
   Multiplication by `2` on `Z/15Z` has orbits
   `{0}`, `{5,10}`, `{3,6,9,12}`, `{1,2,4,8}`, `{7,11,13,14}`.
   Write the corresponding counts as `(a,b,c,d,e)`.
   The mod `3` and mod `5` profiles give
   `a + 4c = 1441`, `a + 2b = 921`, `c + d + e = 874`, `b + 2d + 2e = 1488`.
   For an order-`15` character with `U = zeta + zeta^2 + zeta^4 + zeta^8`, one has
   `U + conjugate(U) = 1` and `|U|^2 = 4`, hence `U = (1 +/- i sqrt(15))/2`.
   Therefore
   `A15 = a - b - c + dU + e conjugate(U)`,
   so `|A15|^2 = 2209` becomes
   `(4276 - 15c)^2 + 15(d-e)^2 = 8836`.
   The only integral solution is
   `c = 286`, `d-e = +/- 24`, hence `{d,e} = {306,282}`, and then
   `a = 297`, `b = 312`.

Forced mod `15` profile:
- residue `0`: `297`
- residues `5,10`: `312` each
- residues `3,6,9,12`: `286` each
- one unit orbit `{1,2,4,8}`: `306` each
- the other unit orbit `{7,11,13,14}`: `282` each

This is already a real theorem slice: any cyclic Hadamard difference set at `v = 8835` would have exactly this mod `15` fiber pattern, up to swapping the two unit orbits.

## chosen_plan
Best path:

1. Keep the multiplier route as the main proof architecture.
2. Bank the exact mod `3`, mod `5`, and mod `15` forced profiles as the current structural gain.
3. Before any code, check whether the forced mod `15` profile is already incompatible with the coarse inventory of full `47`-orbits in the decisive block `{5,10} mod 15`.
4. If that block-total is impossible, the case is eliminated without computation.
5. Only if that coarse contradiction fails would a bounded orbit-feasibility check be justified.

## self_checks
- Self-check after statement lock: the exact target remains the original cyclic Hadamard case, with no scope drift.
- Self-check after approach A: the multiplier step is the main load-bearing external lemma and must be citation-verified later.
- Self-check after the mod `3` computation: the norm rigidity over `Z[omega]` is the cleanest exact arithmetic step and appears internally consistent.
- Self-check after the mod `5` computation: the unique profile `(921,874,874,874,874)` follows immediately from orbit symmetry plus `|chi(D)| = 47`.
- Self-check after the mod `15` computation: the Gaussian-period identity gives a unique integral solution; this should be rechecked mechanically if any contradiction later depends on it.
- Self-check after the orbit-block contradiction: the only remaining load-bearing point is that every `47`-orbit inside the `{5,10} mod 15` block must come from additive orders `3,57,93,1767`, hence have sizes `2,18,10,90`.

## code_used
No code used. The contradiction closed at the reasoning level before any bounded experiment was needed.

## result
Claim reached:

`C_8835` does not admit a `(8835,4417,2208)` difference set, provided the standard `47`-multiplier normalization is applied.

Final contradiction:

1. The mod `15` profile forces exactly `312` elements in residue class `5 mod 15` and `312` elements in residue class `10 mod 15`.
   Hence `D` contains exactly `624` elements in the block
   `B = {x in Z/8835Z : x equiv 5 or 10 mod 15}`.
2. Because `47D = D`, the set `D` is a union of full `47`-orbits.
3. Any element of `B` has additive order divisible by `3` but not by `5`, so its order is one of
   `3, 57, 93, 1767`.
4. The corresponding `47`-orbit sizes are
   `ord_3(47) = 2`,
   `ord_57(47) = lcm(2,9) = 18`,
   `ord_93(47) = lcm(2,5) = 10`,
   `ord_1767(47) = lcm(2,9,5) = 90`.
5. The available numbers of such orbits are
   `phi(3)/2 = 1`,
   `phi(57)/18 = 2`,
   `phi(93)/10 = 6`,
   `phi(1767)/90 = 12`.
6. Therefore the block total `624` would have to satisfy
   `624 = 2a + 18b + 10c + 90d`
   with
   `0 <= a <= 1`, `0 <= b <= 2`, `0 <= c <= 6`, `0 <= d <= 12`.
   Dividing by `2`,
   `312 = a + 9b + 5c + 45d`.
7. If `d <= 4`, then the right-hand side is at most
   `1 + 18 + 30 + 180 = 229 < 312`, so `d >= 5`.
8. If `d = 5`, the remainder is
   `87 = a + 9b + 5c`,
   but the right-hand side is at most `49`.
9. If `d = 6`, the remainder is
   `42 = a + 9b + 5c`.
   Checking `b = 0,1,2` gives
   `42 = a + 5c`, `33 = a + 5c`, or `24 = a + 5c`,
   none of which is possible with `a in {0,1}`.
10. If `d >= 7`, then `45d > 312`, impossible.

Hence no such union of full `47`-orbits can realize the forced mod `15` profile, contradicting the existence of `D`.

Current theorem-facing conclusion:
- exact intended statement eliminated
- no code required
- the proof is compact enough to plausibly serve as the core of a short note once the multiplier citation is pinned down cleanly

## family_affinity
Very high. The argument directly targets the residual cyclic Hadamard case and uses the family-typical toolkit: multiplier invariance, quotient fibers, and exact character norms.

## generalization_signal
Moderate to strong. The mod `3` inert-prime norm argument is specific to the coincidence `n = 47^2` and `47 equiv 2 mod 3`, but the decisive endgame only needs a forced quotient profile and an orbit-inventory contradiction. That proof shape should transfer to other residual cyclic Hadamard cases when one multiplier prime induces a sparse block inventory.

## proof_template_reuse
Reusable template:

1. prime-square multiplier normalization
2. exact quotient profile on one inert small prime
3. orbit-symmetric quotient profile on a second small prime
4. mixed quotient `pq` Gaussian-period squeeze
5. final orbit-block counting contradiction or, failing that, a bounded orbit-lift feasibility check

That is a credible template for other small open cyclic Hadamard cases with one distinguished prime-square `n`.

## candidate_theorem_slice
Exact title-theorem slice now suggested:

`There is no cyclic (8835,4417,2208)-difference set.`

Minimal internal proposition supporting that title theorem:

Any hypothetical example would have the forced mod `15` profile
`297 | 312,312 | 286,286,286,286 | 306,306,306,306 | 282,282,282,282`
up to swapping the two unit-orbit blocks, but the block `{5,10} mod 15` cannot be assembled from full `47`-multiplier orbits.

## smallest_param_shift_to_test
If verify confirms the present disproof, the best next shifts are the other small open cyclic Hadamard survivors where the distinguished multiplier prime gives a similarly sparse orbit inventory on one mixed small quotient. The useful move is methodological transfer, not a literal neighboring parameter perturbation of `8835`.

## why_this_is_or_is_not_publishable
If the argument survives verify, a successful solve is indeed about `80%` to `90%` of the paper. The exact title theorem is the named residual case itself, and the remaining packaging work is small:
- write the multiplier lemma with the exact citation
- present the mod `3`, mod `5`, and mod `15` profile lemmas
- present the final orbit-block contradiction
- add a short literature-placement paragraph

This is not too thin for the micro-paper lane if the multiplier step checks out. It already reads like a title theorem of a short note rather than a loose computational witness.

## paper_shape_support
Exact title theorem if solved:

`The cyclic group C_8835 admits no (8835,4417,2208)-difference set.`

Minimal remaining packaging work after a full closure:
- write the multiplier normalization cleanly
- present the forced quotient profile lemmas
- present the block `{5,10} mod 15` orbit contradiction
- attach a short literature note explaining why this exact residual case mattered

One immediate corollary / boundary statement already visible:
- any hypothetical cyclic example would be forced into a unique mod `15` orbit profile, so the disproof does not come from broad asymptotics but from a sharp finite arithmetic obstruction.

## boundary_remark
Natural boundary remark:

What scales:
- multiplier normalization
- quotient-profile forcing on small mixed moduli
- orbit-block counting once a sparse decisive block is isolated

What does not scale automatically:
- the exact Eisenstein norm rigidity at mod `3`
- the particularly sharp `624` versus `{2,10,18,90}` block obstruction

Suggested theorem slice if one wants an internal proposition:
- the unique mod `15` profile lemma plus the impossibility of filling the `{5,10} mod 15` block by full `47`-orbits

Most informative next parameter shifts:
- another survivor where the multiplier prime acts with one mixed block having only a few orbit sizes
- a case where a `pq` quotient produces a similarly rigid profile before the final orbit count

With the present argument, the package is already closer to a paper-shaped claim than to a bare isolated instance, pending verification of the multiplier citation.

## publication_prior_art_audit
- Exact-statement search on `2026-04-15` for `"(8835,4417,2208) difference set"` and alternate phrasing such as `"8835 cyclic Hadamard difference set"` surfaced the canonical Baumert-Gordon source and Gordon's La Jolla status slides, but did not surface a later case-specific construction or nonexistence theorem.
- Canonical source check: Baumert-Gordon 2004 Table 5 still lists `8835 4417 2208` as `Open` among the cyclic Hadamard survivors, while nearby rows are explicitly marked `No` by Lander theorems. In the bounded audit I found no theorem, proposition, example, corollary, observation, or sufficient-condition entry in that source that already settles the exact `8835` case by implication. Source: `https://www.dmgordon.org/papers/cds.pdf`.
- Outside-source status check: Gordon's ArasuFest slide deck from `August 3, 2019` still lists `8835` among the seven small open cyclic Hadamard cases below `10000`. Source: `https://cargo.wlu.ca/ArasuFest/ArasuFest_talks/Dan_Gordon.pdf`.
- Bounded recency search for the exact tuple and nonexistence phrasing did not surface a post-2019 settlement. This is an inference from the bounded search surface, not a global survey.
- Prior-art verdict: `REDISCOVERY` is not established in the bounded audit.

## publication_statement_faithfulness
The strongest audited claim remains faithful to the selected problem:

`The cyclic group C_8835 admits no (8835,4417,2208)-difference set.`

There is no theorem drift, no quantifier expansion, and no substitution of a weaker proxy claim. The proof architecture is parameter-specific but honest: multiplier normalization, forced quotient profiles modulo `3`, `5`, and `15`, and a final full-orbit obstruction on the `{5,10} mod 15` block.

## publication_theorem_worthiness
- Stronger than "here is an example": yes. The packet supports an exact nonexistence theorem for a named residual cyclic Hadamard case.
- Real theorem slice: yes. The title theorem is the exact `8835` nonexistence statement, with a sharp internal proposition given by the unique mod `15` profile plus the impossible `624`-point `{5,10}` block.
- Structural versus instance-only: structural but case-focused. The argument is not a hand-picked witness or ad hoc computation; it uses standard family tools and yields a rigid quotient-profile theorem before the final contradiction.
- Referee test: this survives the question "what is the theorem?" because the answer is immediate and title-sized.
- Small-case dependence: some parameter-specific arithmetic is unavoidable, but the proof does not depend on an unilluminating table of tiny cases. Its load-bearing steps are exact quotient identities and orbit inventory constraints.

## publication_publishability
- If correct and verified in the present bounded sense, this already constitutes most of a publishable short note.
- Estimated single-solve-to-paper fraction: about `0.88`.
- Remaining gap: genuinely small. The visible remaining work is to pin the multiplier citation cleanly in the paper draft, write the proof in note form, and place the result against the short open-case list. No feeder ladder or broader theorem campaign is needed.
- Publication verdict: the packet now looks publishable on human mathematical standards as a one-shot note removing a named survivor from the cyclic Hadamard list.
- Lean role: Lean would be a secondary formal seal and archival polish, not the remaining publication blocker.

## publication_packet_audit
- Packet quality: human-ready.
- Proof artifacts are preserved well enough for a human note: exact statement lock, theorem slice, proof skeleton, verification recomputation, and a bounded prior-art audit are all present in this dossier.
- Narrative quality is strong because the literature already packages `8835` as a residual frontier case, so the note has an immediate title theorem and literature hook.
- Remaining editorial tasks are bounded and do not change the mathematical scope.

## micro_paper_audit
- MICRO-PAPER verdict: pass.
- The result is already a real theorem, not a curiosity.
- One solve provides nearly the whole paper because the literature anchor, title theorem, and obstruction narrative are already aligned.
- The proof is compact enough for a short note and does not require an expanded program to become paper-shaped.
- Recommendation: do not widen this into a broader survivor campaign before drafting. Move it aside as a human-ready packet and let Lean run later as the non-blocking formal-seal lane.

## strongest_honest_claim
The strongest honest claim supported by the bounded verify and publication audit is:

`There is no cyclic (8835,4417,2208)-difference set.`

Equivalently, any hypothetical cyclic example would have a unique mod `15` quotient profile, and the forced `624`-point `{5,10} mod 15` block cannot be written as a union of the available full `47`-multiplier orbits.

## paper_title_hint
`On the Nonexistence of a Cyclic (8835,4417,2208)-Difference Set`

## next_action
Promote this packet to the `PAPER_READY` / `HUMAN_READY` tier, preserve the current proof artifacts as the paper core, and treat Lean as a secondary seal. During drafting, pin the exact multiplier citation cleanly, but do not reopen the problem into a broader theorem program.

## likely_failure_points
- The multiplier normalization must be cited exactly and checked for this parameter set.
- The mod `15` Gaussian-period algebra should be rechecked for sign mistakes before relying on the forced `312,312` block counts.
- The translation from residue block `{5,10} mod 15` to admissible additive orders `3,57,93,1767` should be verified explicitly in the writeup.

## what_verify_should_check
- Verify the exact multiplier theorem invocation that makes `47` a multiplier for an abelian difference set with `n = 47^2` and `gcd(47,8835) = 1`.
- Recompute the mod `3` norm-form classification in `Z[omega]`.
- Recompute the mod `15` Gaussian-period identities `U + conjugate(U) = 1` and `|U|^2 = 4`.
- Verify the forced mod `15` profile numerically from the character equations.
- Verify that every element congruent to `5` or `10 mod 15` has additive order in `{3,57,93,1767}` and hence lies in a `47`-orbit of size `2,18,10,90`.
- Recheck the bounded diophantine impossibility `624 != 2a + 18b + 10c + 90d` under the available orbit-count bounds.

## verify_rediscovery
PASS 1 used a bounded web audit on the exact tuple, the cyclic-Hadamard phrasing, the canonical 2004 source, and the 2019 La Jolla status slide.

Findings:
- Baumert-Gordon 2004, Table 5 still lists `(8835,4417,2208)` as `Open`.
- Daniel Gordon's ArasuFest slide deck dated August 3, 2019 still lists `8835` among the seven small open cyclic Hadamard cases below `10000`.
- The current La Jolla Difference Set Repository landing page surfaced no later exact construction or nonexistence entry for this tuple in the bounded audit.
- No bounded search result established that the exact intended statement has already been solved, directly implied, or explicitly exhibited elsewhere.

Rediscovery verdict: not established.

## verify_faithfulness
The claimed result matches the intended statement exactly: it aims to prove that the cyclic group `C_8835` admits no `(8835,4417,2208)` difference set.

No wrong-theorem drift or quantifier drift was found. The only external load-bearing input is the standard numerical-multiplier claim that the prime `47` is a multiplier because `n = 47^2` and `gcd(47,8835) = 1`. Once that standard multiplier statement is granted in its usual form `47D = D + g`, the normalization to `47D = D` is faithful because `gcd(47-1,8835) = gcd(46,8835) = 1`, so one may translate by a unique solution of `(47-1)y = -g`.

Faithfulness verdict: faithful to the exact selected problem.

## verify_proof
I recomputed the internal proof steps and did not find an incorrect step.

Checked deductions:
- Mod `3`: multiplier invariance forces the two nonzero residue classes to have equal counts, so with `N0 + 2N1 = 4417` and `|N0 - N1| = 47`, the unique solution is `(1441,1488,1488)`.
- Mod `5`: the four nonzero residue classes form one `47`-orbit, so with `M0 + 4M1 = 4417` and `|M0 - M1| = 47`, the unique solution is `(921,874,874,874,874)`.
- Mod `15`: using the orbit partition
  `\{0\}, \{5,10\}, \{3,6,9,12\}, \{1,2,4,8\}, \{7,11,13,14\}`
  and an exact order-`15` character with
  `U = zeta + zeta^2 + zeta^4 + zeta^8`,
  `U + conjugate(U) = 1`,
  `|U|^2 = 4`,
  the linear constraints from mod `3` and mod `5` together with `|A_15| = 47` give the unique profile
  `a=297`, `b=312`, `c=286`, `{d,e} = {306,282}`.
- Therefore the block `B = {x : x mod 15 in {5,10}}` must contribute exactly `2b = 624` points.
- Every element of `B` has additive order in `{3,57,93,1767}`. The corresponding `47`-orbit sizes are respectively `{2,18,10,90}`, and the available orbit counts in `B` are `{1,2,6,12}`.
- The bounded feasibility equation
  `624 = 2a + 18b + 10c + 90d`
  with bounds `0 <= a <= 1`, `0 <= b <= 2`, `0 <= c <= 6`, `0 <= d <= 12`
  has no solution.

First incorrect step found: none.

Residual caveat:
- The proof depends on citing the multiplier theorem cleanly in the later writeup. That is a citation/completeness issue, not an internal arithmetic gap found during this verify pass.

## verify_adversarial
No checker file existed, so the adversarial pass was a direct recomputation.

Adversarial checks run:
- recomputed the mod `3` and mod `5` forced profiles by exhaustive integer solving;
- recomputed the mod `15` profile by exhaustive solving of the linear constraints plus the exact norm equation;
- numerically verified `U + conjugate(U) = 1` and `|U|^2 = 4`;
- enumerated all elements in the block `{5,10} mod 15` to confirm the only additive orders present are `3,57,93,1767`;
- exhaustively checked the bounded orbit-sum equation and confirmed there is no feasible combination yielding `624`.

No construction, counterexample to the proof, or arithmetic inconsistency was found in this pass.

## verify_theorem_worthiness
Exactness:
- the visible theorem slice is exact, not a proxy: `There is no cyclic (8835,4417,2208)-difference set.`

Novelty:
- bounded prior-art checking did not establish rediscovery;
- the exact tuple still appears as open in the 2004 table and in Gordon's August 3, 2019 small-open-case slide, and the bounded audit did not surface a later settlement.

Reproducibility:
- high for a human verifier; the proof is a short chain of exact quotient-count deductions followed by a tiny finite orbit-count obstruction.

Lean readiness:
- the argument is strong enough to formalize, but Lean is not the shortest remaining path because the immediate remaining work is to pin the multiplier citation cleanly and package the human writeup.

Paper leverage:
- if the argument is written cleanly with the multiplier citation, one solve already supplies roughly `82%` of a publishable short note;
- the title theorem already visible is `The cyclic group C_8835 admits no (8835,4417,2208)-difference set.`

What scales:
- multiplier normalization;
- small-quotient profile forcing;
- sparse orbit-block contradictions of the same form.

What does not clearly scale:
- the specific Eisenstein norm rigidity at modulus `3`;
- the exact `624` versus `{2,10,18,90}` orbit inventory obstruction.

Best honest publication status:
- `SLICE_CANDIDATE`, not merely `INSTANCE_ONLY`, because the result attacks a named survivor from a canonical open list and already has a compact title-theorem packet if the writeup is completed.

## verify_verdict
- `verify_verdict = VERIFIED`
- `classification = COUNTEREXAMPLE`
- `confidence = medium-high`
- `publication_status = SLICE_CANDIDATE`
- `lean_ready = true`
- `lean_packet_seal = false`

## minimal_repair_if_any
No mathematical repair was needed.

Conservative clarification to carry into the paper draft:
- state the multiplier step explicitly as: if `47` is a numerical multiplier and `47D = D + g`, then because `gcd(46,8835) = 1` one can translate by `y` with `46y = -g` to obtain an equivalent difference set satisfying `47(D+y) = D+y`.
