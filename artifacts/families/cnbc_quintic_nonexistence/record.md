# Family Record: cnbc_quintic_nonexistence

## family_statement_lock

- Active family: quintic circulants `G = C_n(a,b,m)` with `n = 2m` and `1 <= a < b < m`, so the closed-neighborhood mask is `{0, +/-a, +/-b, m}`.
- Common operator: `B_{n,a,b} = I + S^a + S^(-a) + S^b + S^(-b) + S^m`.
- Common symbol: `sigma_{n,a,b}(k) = 1 + 2 cos(2 pi a k / n) + 2 cos(2 pi b k / n) + (-1)^k`.
- Locked theorem target for this pass: if `sigma_{n,a,b}(k) != 0` for every `k in Z/nZ`, then `C_n(a,b,m)` is not CNBC.
- Honest scope: this is a theorem slice, not a classification of all mixed-parity quintic circulants and not yet a two-route flagship theorem.
- Smallest clear obstruction to any broader nonexistence claim: if `a` and `b` have opposite parity and `m` is odd, the alternating vector `x_i = (-1)^i` satisfies the CNB equation because `1 + 2(-1)^a + 2(-1)^b + (-1)^m = 0`.
- Bounded evidence base for this pass: `campaigns/cnbc_quintic_nonexistence.md`, the current family record/status, `PROOFS.md`, and the three seed records `c16-4-5-8-cnbc`, `c20-2-3-10-cnbc`, and `c24-4-5-12-cnbc`. `PROOFS.md` adds no exact family entry here because none of the seeds is yet `EXACT`.

## existing_instance_inventory

- `c16-4-5-8-cnbc`
  - `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, `lean_ready = true`.
  - Shared mechanism: the full six-term symbol is nonzero at every frequency, so the `16 x 16` closed-neighborhood operator is invertible.
  - Family role: cleanest preserved Route I application.
- `c20-2-3-10-cnbc`
  - `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, `lean_ready = true`.
  - Preserved seed proof: opposite-pair summation gives a length-`10` circulant system for `y_i = x_i + x_{i+10}`, forces `x_{i+10} = -x_i`, and then a finite recurrence contradiction closes the instance.
  - Extra verifier evidence that matters for generalization: the verifier also recorded full rank `20` for the original `20 x 20` CNB matrix, so this seed is compatible with the same Route I obstruction after theorem-level repackaging even though its human proof is narrated through the antipodal reduction.
  - Family role: best source for the reusable opposite-pair lemma and likely second Route I application once the family Fourier package is written cleanly.
- `c24-4-5-12-cnbc`
  - `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, `lean_ready = true`.
  - Shared mechanism: the full symbol vanishes exactly at `k = 8,16`, so the real kernel is the primitive cube-root subspace and every real solution is `3`-periodic.
  - Family role: strongest current Route II seed, but still a single periodic-kernel example rather than a closed family theorem.

## shared_structure

- Common decomposition / invariant / construction: every seed turns a CNBC coloring into a nonzero sign vector in the kernel of the same six-term circulant operator `B_{n,a,b}`.
- Common invariant: the discrete zero set of `sigma_{n,a,b}` controls the real kernel of `B_{n,a,b}`.
- Shared proof template:
  - Route I: if the zero set is empty, then `B_{n,a,b}` is invertible, so no nonzero sign kernel vector exists.
  - Route II: if the zero set is tiny and supported on low-order characters, then every real kernel vector lies in a short-period subspace that can be ruled out at the sign level.
- Shared auxiliary construction: because the family includes the antipodal generator `m = n/2`, opposite-pair sums `y_i = x_i + x_{i+m}` give a half-length circulant reduction. This is genuinely reusable, but it is auxiliary rather than the flagship theorem.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  - proving the six residues `0, +/-a, +/-b, m` are distinct when `1 <= a < b < m`, so each closed neighborhood has size `6`;
  - translating CNBC colorings to the kernel equation `B_{n,a,b} x = 0`;
  - diagonalizing `B_{n,a,b}` by Fourier characters of `Z/nZ`;
  - concluding that a nowhere-zero symbol forces trivial real kernel;
  - showing that kernel support on characters of order `d` forces `d`-periodicity;
  - summing opposite CNB equations to obtain the half-length circulant system for `y_i = x_i + x_{i+m}`.
- Steps that are still instance-specific:
  - evaluating or factoring the symbol for a concrete tuple;
  - the `c20` complement identity on `Z/10Z` and the constant-pair-sum argument forcing `c = 0`;
  - the `c24` zero-set calculation `{8,16}` and the special `3`-periodic sign contradiction;
  - writing `c20` as a clean Route I application rather than as an exact-instance antipodal reduction.

## candidate_theorem_slices

- Slice A: Route I spectral obstruction.
  - Claim: if `sigma_{n,a,b}(k) != 0` for every `k in Z/nZ`, then `C_n(a,b,m)` is not CNBC.
  - Current support: directly matches `c16`; `c20` looks compatible after repackaging because the full operator is already verifier-certified nonsingular.
- Slice B: Route II low-order-kernel periodicity.
  - Claim: if the real kernel of `B_{n,a,b}` is supported only on characters of order `d`, then every real kernel vector is `d`-periodic; if no `+/-1` `d`-periodic pattern satisfies the induced relation, then `C_n(a,b,m)` is not CNBC.
  - Current support: cleanly explains `c24`, but only one verified seed presently supports it.
- Slice C: antipodal opposite-pair reduction lemma.
  - Claim: in `C_n(a,b,m)` with `m = n/2`, summing opposite CNB equations yields a half-length circulant system for `y_i = x_i + x_{i+m}`.
  - Current support: preserved exactly by `c20`; best treated as a reusable lemma rather than the headline theorem.
- Slice D: counterexample boundary for overbroad mixed-parity claims.
  - Claim: any unconditional mixed-parity nonexistence theorem is false because odd-`m` mixed-parity tuples admit the alternating CNBC coloring.
  - Current support: immediate from the closed-neighborhood mask and useful as the smallest obstruction boundary for publication framing.

## chosen_slice

- Chosen strongest honest slice: Slice A, the Route I spectral obstruction theorem.
- Proposed theorem slice:
  `Let n = 2m and G = C_n(a,b,m) with 1 <= a < b < m. If sigma_{n,a,b}(k) != 0 for every k in Z/nZ, then G admits no closed-neighborhood balanced coloring.`
- Why this is the strongest honest slice now:
  - it uses only the scalable six-term circulant structure;
  - it already has one direct verified seed and a second seed whose full operator is verifier-certified invertible;
  - it does not force the single-seed Route II phenomenon into the flagship claim prematurely.
- Strongest plausible extension after this slice: add Route II as a separate corollary or companion theorem beginning with the cube-root case suggested by `c24-4-5-12-cnbc`.
- Smallest likely counterexample or obstruction to overclaiming: the odd-`m` mixed-parity alternating witness. Along the two active parameter lines, the first concrete obstruction points are `c22-2-3-11-cnbc` and `c26-4-5-13-cnbc`.

## reusable_lemmas

- Six-term distinctness / cardinality lemma:
  if `n = 2m` and `1 <= a < b < m`, then `0, +/-a, +/-b, m` are pairwise distinct in `Z/nZ`, so every closed neighborhood has cardinality `6`.
- CNB-to-kernel translation lemma:
  `C_n(a,b,m)` is CNBC if and only if there exists a nonzero sign vector `x in {+1,-1}^n` with `B_{n,a,b} x = 0`.
- Fourier diagonalization lemma:
  the characters of `Z/nZ` diagonalize `B_{n,a,b}` with eigenvalues `sigma_{n,a,b}(k)`.
- Nowhere-zero symbol lemma:
  if `sigma_{n,a,b}(k) != 0` for all `k`, then `B_{n,a,b}` has trivial real kernel.
- Opposite-pair reduction lemma:
  for `m = n/2`, the variables `y_i = x_i + x_{i+m}` satisfy a half-length circulant system obtained by summing opposite CNB equations.
- Kernel-support periodicity lemma:
  if the real kernel is supported on characters of order `d`, then every real kernel vector is `d`-periodic.
- Low-period sign obstruction lemma:
  for fixed small `d`, if no `+/-1` `d`-periodic pattern satisfies the induced zero-sum relation, then no CNBC coloring exists.

## proof_plan

- Main proof path:
  1. Prove the six-term distinctness lemma so the closed-neighborhood size is exactly `6`.
  2. Translate any hypothetical CNBC coloring into a nonzero sign vector `x` with `B_{n,a,b} x = 0`.
  3. Diagonalize `B_{n,a,b}` on Fourier characters of `Z/nZ` and compute the eigenvalue `sigma_{n,a,b}(k)` at frequency `k`.
  4. Under the nowhere-zero hypothesis, conclude that `B_{n,a,b}` is invertible over `C`, hence has trivial real kernel.
  5. Contradict the existence of the nonzero sign vector `x`.
  6. Package `c16-4-5-8-cnbc` as the clean first application and rewrite `c20-2-3-10-cnbc` as the second application, with the opposite-pair proof retained only as a supporting lemma.
- Fallback path:
  1. Keep Route I as the lead theorem slice even if only `c16` is written out as the direct spectral application.
  2. Promote the `c20` opposite-pair reduction to a reusable structural lemma plus exact application.
  3. Isolate the `c24` cube-root argument as a separate Route II periodicity corollary/program.
  4. Return to one feeder on each parameter line before attempting any unified two-route theorem.

## fallback_counterexample_plan

- Overclaim to avoid: any unconditional mixed-parity quintic nonexistence theorem.
- Smallest concrete obstruction already visible: odd-`m` mixed-parity tuples admit the alternating CNBC witness; the nearest ones on the active lines are `c22-2-3-11-cnbc` and `c26-4-5-13-cnbc`.
- If `c20` resists clean Route I repackaging, do not force it into the flagship statement; keep its opposite-pair argument as a separate reusable lemma.
- If the next even-order feeder on the `(4,5,m)` line does not reproduce a low-order kernel, treat `c24` as an isolated Route II corollary rather than as evidence for a broader periodicity theorem.

## next_best_feeder_instances

- `c28-2-3-14-cnbc`
  - Smallest even continuation after `c20-2-3-10-cnbc`.
  - Best discriminator for whether the `(2,3,m)` line stays in the nowhere-zero-symbol Route I regime or whether the current proof is only an exact-instance antipodal accident.
- `c28-4-5-14-cnbc`
  - Smallest even continuation after `c24-4-5-12-cnbc`.
  - Best discriminator for whether the cube-root kernel mechanism persists on the `(4,5,m)` line or whether `n = 24` is isolated.

## publication_value

- The strongest honest publication object is now a referee-facing theorem slice, not just a list of exact counterexamples.
- Honest publication status remains `SLICE_CANDIDATE`:
  the main theorem is parameterized and structurally motivated, but the family proof package still needs the distinctness lemma, the Fourier diagonalization lemma, and the nowhere-zero-symbol implication written cleanly in the official backend.
- Strongest path forward:
  finish the Route I lemma stack, then use `c28-2-3-14-cnbc` as the first discriminator while keeping `c16` and the repackaged `c20` as the lead applications.
- Fallback path:
  publish a shorter spectral-obstruction note with Route I as the lead theorem, `c16` as the cleanest direct application, `c20` as a supporting opposite-pair application, and `c24` as a secondary periodicity corollary or future-direction section.
- Paper-shape hint:
  `A spectral obstruction to closed-neighborhood balanced colorings in quintic circulants with an antipodal generator`.

## publication_prior_art_audit

- Exact-statement search:
  targeted searches on `"closed-neighborhood balanced coloring" quintic circulant`, `"closed neighborhood balanced" circulant graph`, and the exact tuples `C_16(4,5,8)`, `C_20(2,3,10)`, `C_24(4,5,12)` did not surface a later exact-instance settlement within budget.
- Alternate-notation search:
  checked family-style notation `C_n(d_1,d_2,n/2)`, `C_n(a,b,n/2)`, and open-case phrasing around quintic CNBC circulants with `n ≡ 0 (mod 4)`; the useful hits pointed back to the same canonical 2025 source rather than to a later closure.
- Canonical source:
  the bounded audit still identifies Fox et al., `Closed Neighborhood Balanced Coloring of Graphs` (Graphs and Combinatorics, 2025), as the canonical source.
- Theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source:
  `Theorem 19` closes the `n ≡ 2 (mod 4)` quintic line by parity, `Theorem 17` gives nearby sufficient positive cases in certain `n ≡ 0,4 (mod 8)` congruence patterns, and `Question 1` asks whether the quintic CNBC circulants can be completely characterized.
  I did not find a theorem, proposition, example, corollary, observation, or sufficient-condition entry there already implying the Route I slice or settling the exact seeds `c16`, `c20`, or `c24`; all three seeds lie in the still-open `n ≡ 0 (mod 4)` mixed-parity regime rather than in the already classified `n ≡ 2 (mod 4)` regime.
- Outside-source status search:
  targeted outside-source searches on the exact tuples and alternate family notation produced no independent settlement within budget.
- Recent citation / discussion / follow-up check:
  the 2025 AWM Research Symposium abstract `Closed Neighborhood Balanced Graphs` discusses the broader CNBC program but does not advertise a closure of the open quintic `n ≡ 0 (mod 4)` cases or of the exact tuples in this campaign.
- Prior-art verdict:
  bounded evidence does not establish rediscovery. The present campaign still appears to attack a genuinely open theorem slice left outside the current canonical classification.

## publication_statement_faithfulness

- Is the strongest honest claim stronger than “here is an example”?
  Yes. The Route I claim is a parameterized obstruction theorem over all `n = 2m` with `1 <= a < b < m`, not just a restatement of one exact tuple.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here?
  Yes: the real candidate theorem slice is
  `sigma_{n,a,b}(k) != 0 for every k in Z/nZ => C_n(a,b,m) is not CNBC`.
- Is the proof structural or merely instance-specific?
  The intended proof is structural because it passes through the shared six-term operator `B_{n,a,b}`, Fourier diagonalization, and kernel triviality. However, the preserved family backend currently stops before the Fourier diagonalization and nowhere-zero-symbol lemmas, so the end-to-end structural package is not yet closed in the official backend.
- Would this survive a referee asking “what is the theorem?”
  Yes, but only if the paper leads with Route I as the headline theorem and treats `c16` plus a repackaged `c20` as applications. No, if the writeup tries to sell a full quintic classification or an already-unified two-route flagship theorem.
- Is the claim still too dependent on hand-picked small cases?
  The Route I statement itself is not small-case dependent, but the current evidence presentation still leans on three small verified seeds because `c20` is not yet rewritten as a direct spectral application and Route II still has only one seed.

## publication_theorem_worthiness

- The strongest honest claim is theorem-worthy in the slice sense, not yet in the family-classification sense.
- Why it clears the “more than an example” bar:
  it packages multiple verified open-case counterexamples under one reusable obstruction mechanism and targets a regime that the canonical 2025 paper still leaves open.
- Why it does not yet clear a stronger bar:
  Route I is close to a natural circulant linear-algebra criterion, so by itself it is too thin unless the family proof is written cleanly and the open-case applications are stated sharply.
- The proof spine is structural, but the paper spine is not finished:
  `c16` is already a clean direct application, `c20` still needs theorem-level repackaging, and `c24` is honest only as secondary Route II evidence rather than as co-headline support.
- Generalization route strong enough to merit campaign priority?
  Yes. The literature leaves exactly this congruence regime open, the seed cluster shares a real common operator backbone, and the next feeders `c28-2-3-14-cnbc` and `c28-4-5-14-cnbc` are discriminating rather than random one-offs.

## publication_publishability

- Publication verdict: keep `publication_status = SLICE_CANDIDATE`.
- Not `INSTANCE_ONLY`:
  the honest lead claim is parameterized and structural.
- Not `REDISCOVERY`:
  the bounded prior-art pass did not find a closure of the open `n ≡ 0 (mod 4)` quintic regime or of the exact seed tuples.
- Not `SLICE_EXACT`:
  the family Fourier diagonalization lemma, the nowhere-zero-symbol-to-trivial-kernel lemma, and the clean Route I repackaging of `c20` are still missing from the preserved backend story.
- Not `PAPER_READY`:
  a referee can now be told what the theorem is, but not yet be shown a fully preserved family proof package strong enough to make the note feel complete rather than merely promising.
- Best current paper shape:
  lead with the Route I spectral obstruction theorem in the open quintic `n ≡ 0 (mod 4)` regime, use `c16` as the clean direct application, repurpose `c20` as the second application once rewritten at theorem level, and keep `c24` as a companion periodicity corollary or future-direction section.

## strongest_honest_claim

- After the bounded publication audit, the strongest honest claim is still a theorem-slice candidate rather than a classification result: in the open quintic `n ≡ 0 (mod 4)` regime left outside the 2025 canonical paper, if `G = C_n(a,b,n/2)` with `1 <= a < b < n/2` has six-term symbol `sigma_{n,a,b}(k)` nonzero for every `k in Z/nZ`, then `G` has no closed-neighborhood balanced coloring.
- This is genuinely stronger than “here are three counterexamples,” because it is a structural obstruction theorem with open-case applications.
- It is not yet a finished publication theorem, because the family Fourier diagonalization and nowhere-zero-symbol closure are not yet preserved end-to-end in the official backend.

## paper_title_hint

- `A spectral obstruction for open quintic CNBC circulants with an antipodal generator`

## next_action

- Bootstrap the repo-local Lake dependencies, check the preserved Route I skeleton under `artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`, then close the six-term distinctness, Fourier diagonalization, and nowhere-zero-symbol lemmas before repackaging `C_20(2,3,10)` as a direct Route I application.
- Only after that package is checked should the campaign spend another feeder on `c28-2-3-14-cnbc`; keep Route II secondary unless another low-order-kernel seed appears.

## lean_statement

- Lean target for this pass: preserve the Route I family theorem-slice skeleton in the official backend and mirror it under the family artifact directory.
- Main theorem statement now preserved in the backend:
  `AutoMath.Families.CNBCQuinticRouteI.routeI_spectral_obstruction_skeleton`
  proves that if every six-term closed neighborhood has cardinality `6` and there is no nonzero integer kernel vector for the associated six-term operator, then `C_n(a,b,m)` admits no quintic CNBC coloring.
- Supporting reusable lemma target:
  `AutoMath.Families.CNBCQuinticRouteI.quintic_signed_sum_zero_of_cnb`
  translates any quintic CNBC coloring into the zero signed-sum relation on the six-term mask `{0, ±a, ±b, m}` under the same cardinality hypothesis.

## lean_skeleton

- Backend file added: `lean/AutoMath/Families/CNBCQuinticRouteI.lean`.
- Mirrored family file kept at:
  `artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`.
- Proof skeleton preserved in that module:
  1. define `quinticClosedNeighborhood`, `IsQuinticCNBColoring`, and the family `intendedStatement`;
  2. prove `signed_ne_zero` for the signed encoding of a red/blue coloring;
  3. prove `quintic_signed_sum_zero_of_cnb` from the half-red criterion in `AutoMath.Families.CNBCCriteria`;
  4. reduce the Route I obstruction theorem to the absence of nonzero integer kernel vectors via `routeI_spectral_obstruction_skeleton`.

## lean_result

- Preserved the family Route I module in the official backend by adding
  `lean/AutoMath/Families/CNBCQuinticRouteI.lean`
  as the backend mirror of the current family artifact module.
- Attempted repo-local Lean checks:
  - `cd lean && lake env lean ../artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`
  - `cd lean && lake build AutoMath.Families.CNBCCriteria`
- Actual outcome:
  both commands failed before theorem checking because `lake` attempted to clone `mathlib4` and exited with code `128`.
- Repo-local cause confirmed in-tree:
  `lean/.lake/packages/` exists but is empty in this worktree, so the current Lean target is preserved but not honestly checked here.
- Honest Lean-stage verdict for this pass:
  keep `classification = CANDIDATE`, `publication_status = SLICE_CANDIDATE`, and `lean_complete = false`.

## lean_blockers

- Immediate blocker:
  repo-local Lake dependencies are still unbootstrapped in this worktree, and network-disabled execution prevents `lake` from cloning `mathlib4`.
- First proof blocker after bootstrap:
  the Route I package still needs the six-term distinctness/cardinality lemma so the theorem no longer depends on an external `hcard` hypothesis.
- Main structural blocker after that:
  the family Fourier diagonalization lemma and the nowhere-zero-symbol-to-trivial-kernel implication are still absent from the official backend.
- Application blocker that remains once the structural lemmas land:
  `C_20(2,3,10)` still needs theorem-level repackaging as a direct Route I application rather than only an antipodal reduction.
