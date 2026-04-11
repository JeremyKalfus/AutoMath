# Family Record: cnbc_quintic_nonexistence

## family_statement_lock

- Active `family_slug`: `cnbc_quintic_nonexistence`.
- Dossier path: `campaigns/cnbc_quintic_nonexistence.md`.
- Family artifact path: `artifacts/families/cnbc_quintic_nonexistence`.
- GENERALIZE target for this pass: close the narrow Route I slice only.
- Locked family statement: let `G = C_n(a,b,m)` with `n = 2m` and `1 <= a < b < m`; then the closed-neighborhood operator is
  `B_{n,a,b} = I + S^a + S^(-a) + S^b + S^(-b) + S^m`
  and its Fourier symbol is
  `sigma_{n,a,b}(k) = 1 + 2 cos(2*pi*a*k/n) + 2 cos(2*pi*b*k/n) + (-1)^k`.
- Locked theorem target: if `sigma_{n,a,b}(k) != 0` for every `k in Z/nZ`, then `C_n(a,b,m)` is not CNBC.
- Bounded local read set used in this pass:
  `selected_problem.md`,
  `campaigns/cnbc_quintic_nonexistence.md`,
  the current family `record.md`,
  the current family `status.json`,
  `PROOFS.md`,
  and exactly the three dossier-named seed records
  `artifacts/c16-4-5-8-cnbc/record.md`,
  `artifacts/c20-2-3-10-cnbc/record.md`,
  `artifacts/c24-4-5-12-cnbc/record.md`.
- `PROOFS.md` was relevant only as a negative check: it has no exact solved sections for these CNBC seeds, only build-note mentions of legacy instance Lean files such as `lean/AutoMath/C16458CNBC.lean` and `lean/AutoMath/C244512CNBC.lean`.
- One bounded discriminator search was used locally after the seed read: `lean/AutoMath/Families/CNBCQuinticRouteI.lean` is absent in this repo state, while the mirrored family Lean artifact still exists under `artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`.
- No web was used. The dossier and local artifacts were sufficient to lock the family statement honestly.

## existing_instance_inventory

- `c16-4-5-8-cnbc`: `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, `lean_ready = true`. This is the lead direct Route I seed. Its preserved proof diagonalizes the full six-term circulant operator directly, shows the symbol is nonzero at every frequency, and verification also preserved full rank `16`.
- `c20-2-3-10-cnbc`: `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, `lean_ready = true`. This is supporting Route I-compatible evidence. The preserved proof uses opposite-pair sums `y_i = x_i + x_{i+10}` to reduce to a length-`10` circulant obstruction and then a finite sign contradiction; verification also reports full rank `20` for the original `20 x 20` operator, so the instance is compatible with the headline Route I story even though its narrative is reduction-first.
- `c24-4-5-12-cnbc`: `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, `lean_ready = true`. This is the periodicity companion. Its preserved proof finds that the six-term operator has kernel only at frequencies `8` and `16`, so every real kernel vector lies in the primitive cube-root subspace, hence is `3`-periodic, which is incompatible with `+/-1` signs.
- Exact inventory summary: one clean direct spectral corollary (`c16`), one antipodal-reduction support case (`c20`), and one clean low-order-kernel periodicity case (`c24`).
- Explicit overclaim boundary in scope: `C_22(2,3,11)`, already identified in `selected_problem.md`, remains the smallest campaign-relevant obstruction to any broader mixed-parity nonexistence rhetoric.

## shared_structure

- Common decomposition / invariant / construction: encode a red/blue coloring by a sign vector `x in {+1,-1}^n`; then CNBC is equivalent to the kernel equation `B_{n,a,b} x = 0`.
- Common operator: `B_{n,a,b}` is the six-term circulant operator with mask `{0, +/-a, +/-b, m}`.
- Common Fourier invariant: for the character `chi_k(j) = exp(2*pi*i*k*j/n)`, the eigenvalue is exactly `sigma_{n,a,b}(k)`.
- Common proof template: `CNB coloring -> nonzero sign vector in ker(B_{n,a,b}) -> Fourier control of ker(B_{n,a,b}) -> contradiction`.
- Route I structure already realized by `c16` and compatible with `c20`: if `sigma_{n,a,b}` is nowhere zero, then the operator is invertible and no CNBC coloring exists.
- Route II structure already realized by `c24`: if the zero set is tiny and supported on low-order modes, then every kernel vector has a forced short period that can be incompatible with `+/-1` signs.
- `c20` adds one more genuinely reusable invariant: because `m = n/2`, opposite-pair sums `y_i = x_i + x_{i+m}` always collapse the CNBC equations to a half-length circulant system. That mechanism scales, but the contradiction presently preserved after the reduction is still specific to the `(2,3,10)` seed.

## parameter_sensitive_steps

- Genuinely scalable step: under `1 <= a < b < m`, the six residues `0, +/-a, +/-b, m` are pairwise distinct in `Z/nZ`, so every closed neighborhood has size `6`.
- Genuinely scalable step: CNBC is equivalent to the existence of a nonzero sign vector `x in {+1,-1}^n` with `B_{n,a,b} x = 0`.
- Genuinely scalable step: Fourier characters diagonalize `B_{n,a,b}` with eigenvalues `sigma_{n,a,b}(k)`.
- Genuinely scalable step: `sigma_{n,a,b}(k) != 0` for every `k` implies `ker(B_{n,a,b}) = {0}`, which immediately rules out CNBC.
- Genuinely scalable step: if the kernel is supported only on characters of order `d`, then every real kernel vector is `d`-periodic.
- Genuinely scalable step: because `m = n/2`, opposite-pair summation always yields a half-length circulant reduction, even though the post-reduction contradiction may depend on the parameter line.
- Instance-specific step in `c16`: the odd/even trigonometric split proving that the concrete symbol `1 + 2 cos(k*pi/2) + 2 cos(5k*pi/8) + (-1)^k` never vanishes.
- Instance-specific step in `c20`: the complement identity on `Z/10Z`, the constant pair-sum reduction `b_i = a_i + a_{i+5}`, and the forced recurrence `a_{i+2} = -a_i`.
- Instance-specific step in `c24`: the exact zero set `{8,16}`, the primitive cube-root subspace description, and the final `3`-periodic sign contradiction.
- Smallest likely counterexample or obstruction: if `m` is odd and `a,b` have opposite parity, then the alternating vector `x_i = (-1)^i` satisfies
  `B_{n,a,b} x = [1 + 2(-1)^a + 2(-1)^b + (-1)^m] x = 0`.
  The first campaign-relevant witness is `C_22(2,3,11)`.

## candidate_theorem_slices

- Slice A, Route I spectral obstruction theorem:
  if `sigma_{n,a,b}(k) != 0` for every `k in Z/nZ`, then `C_n(a,b,m)` is not CNBC.
- Slice B, low-order-kernel periodicity theorem:
  if `ker(B_{n,a,b})` is supported only on characters of order `d`, and the induced `d`-periodic sign system has no `+/-1` solution, then `C_n(a,b,m)` is not CNBC.
- Slice C, opposite-pair reduction lemma:
  for `n = 2m`, the sums `y_i = x_i + x_{i+m}` turn the CNBC equations into a half-length circulant obstruction.
- Slice D, mixed-parity odd-`m` counterexample boundary:
  if `m` is odd and `a,b` have opposite parity, then the alternating coloring `x_i = (-1)^i` is a CNBC witness. `C_22(2,3,11)` is the first explicit boundary instance.
- Strongest plausible medium-term package: a two-route spectral/periodicity theorem supported by Slice C as infrastructure and Slice D as the explicit boundary. The current preserved seed proofs do not yet justify promoting that wider package to the headline claim.

## chosen_slice

- Strongest honest slice now: Slice A, the narrow Route I spectral obstruction theorem.
- Proposed theorem slice:
  `Let n = 2m and G = C_n(a,b,m) with 1 <= a < b < m. If sigma_{n,a,b}(k) != 0 for every k in Z/nZ, then G admits no closed-neighborhood balanced coloring.`
- Why this is the strongest honest slice:
  `c16-4-5-8-cnbc` is already a direct corollary;
  `c20-2-3-10-cnbc` supports the same family operator but still relies on a seed-specific reduction narrative;
  `c24-4-5-12-cnbc` is a clean companion for a future Route II theorem, not a direct corollary of the headline Route I statement;
  and `C_22(2,3,11)` blocks any careless attempt to widen the claim to a blanket mixed-parity nonexistence theorem.
- Strongest path forward: close Route I statement-faithfully first, then reuse `c20` and `c24` to justify a later two-route expansion if the family proof stack survives.
- Strongest likely obstruction if the theorem is widened too early: the odd-`m`, mixed-parity alternating witness line, with `C_22(2,3,11)` as the smallest explicit example currently in scope.

## reusable_lemmas

- Six-term distinctness lemma: for `n = 2m` and `1 <= a < b < m`, the residues `0, +/-a, +/-b, m` are pairwise distinct in `Z/nZ`.
- CNB-to-kernel lemma: `C_n(a,b,m)` is CNBC if and only if there exists a nonzero sign vector `x in {+1,-1}^n` with `B_{n,a,b} x = 0`.
- Family Fourier diagonalization lemma: the Fourier characters of `Z/nZ` diagonalize `B_{n,a,b}` with eigenvalues `sigma_{n,a,b}(k)`.
- Nowhere-zero symbol lemma: if `sigma_{n,a,b}(k) != 0` for every `k`, then `B_{n,a,b}` has trivial real kernel.
- Opposite-pair reduction lemma: for `m = n/2`, adding the CNBC equations at `i` and `i + m` yields a half-length circulant system for `y_i = x_i + x_{i+m}`.
- Kernel-support periodicity lemma: if the real kernel is supported only on characters of order `d`, then every real kernel vector is `d`-periodic.
- Low-period sign obstruction lemma: if the induced `d`-periodic sign equations have no `+/-1` solution, then no CNBC coloring exists.
- Alternating boundary lemma: if `m` is odd and `a,b` have opposite parity, then `x_i = (-1)^i` is a nonzero kernel vector and hence a CNBC witness.

## proof_plan

- Main proof path: prove six-term distinctness, translate a hypothetical CNBC coloring into `B_{n,a,b} x = 0`, diagonalize `B_{n,a,b}` by Fourier characters, compute the family symbol `sigma_{n,a,b}(k)`, invoke the nowhere-zero hypothesis to get `ker(B_{n,a,b}) = {0}`, and contradict the existence of a nonzero sign vector. Present `c16-4-5-8-cnbc` as the lead direct corollary.
- Fallback proof path: if the family Fourier closure stalls, keep the headline theorem unchanged but publish the method shape honestly: Route I spectral obstruction theorem slice led by `c16`, `c20` as a reusable opposite-pair reduction support case, and `c24` as the periodicity companion that motivates a later Route II theorem rather than expanding the flagship claim now.
- Immediate repo-state blocker on the formal side: the mirrored family Lean file exists, but the buildable root path `lean/AutoMath/Families/CNBCQuinticRouteI.lean` is absent in this worktree, so even after dependencies are restored the Route I module must be reinstated at root before the theorem slice can be closed in Lean.

## fallback_counterexample_plan

- Do not weaken the Route I hypothesis. The mixed-parity odd-`m` alternating witness line is a genuine structural obstruction to stronger blanket rhetoric.
- Preserve `C_22(2,3,11)` as the explicit overclaim boundary every time a broader theorem is proposed.
- If the campaign later pivots from a nonexistence slice to a counterexample slice, the strongest honest counterexample template already visible is:
  odd `m` plus opposite parity of `a` and `b` gives a CNBC witness via `x_i = (-1)^i`.
- If Route I still does not close statement-faithfully, freeze the campaign at the honest note:
  one narrow spectral obstruction theorem slice,
  one supporting antipodal-reduction seed (`c20`),
  one periodicity companion (`c24`),
  and one explicit obstruction boundary (`C_22(2,3,11)`).
- If a future feeder has a nontrivial zero set that is neither nowhere-zero nor low-order-periodic, treat that as evidence against the current theorem template rather than forcing a family claim.

## next_best_feeder_instances

- `c28-2-3-14-cnbc`: smallest even-`m` continuation of the `(2,3,m)` line after `c20`; it maximally discriminates whether that line is genuinely Route I spectral at the full operator level or merely a reduction-first phenomenon.
- `c28-4-5-14-cnbc`: smallest even-`m` continuation of the `(4,5,m)` line after `c16` and `c24`; it maximally discriminates whether the line stays in the nowhere-zero-symbol regime or flips again into the low-order-kernel periodicity regime.
- Boundary note: `c22-2-3-11-cnbc` should remain tagged as the obstruction line, not as a feeder for the flagship theorem.

## publication_value

- The campaign supports a real theorem slice, not just three isolated exact disproofs: the CNB-to-kernel translation and the circulant/Fourier obstruction are genuinely parameterized over an infinite class of quintic circulants.
- The strongest honest publication shape is still narrow:
  the Route I spectral obstruction theorem as the headline,
  `c16-4-5-8-cnbc` as the direct corollary,
  `c20-2-3-10-cnbc` as supporting antipodal infrastructure,
  `c24-4-5-12-cnbc` as the periodicity companion,
  and `C_22(2,3,11)` as the explicit boundary against overclaiming.
- Honest publication status remains `SLICE_CANDIDATE`, not `SLICE_EXACT` or `PAPER_READY`, because the reusable family proof stack is not yet closed end to end and the buildable root Lean family module is currently missing in this repo state.

## publication_prior_art_audit

- Bounded live-web audit on `2026-04-11` focused only on the Route I claim and the quintic `C_n(d_1,d_2,n/2)` line.
- Exact-statement search used the claim-specific phrases
  `"closed neighborhood balanced" "quintic circulant"`,
  `"closed neighborhood balanced" "C_n(d_1,d_2,n/2)"`,
  `"closed neighborhood balanced" "quintic circulants"`,
  and the exact seed notations `C_16(4,5,8)`, `C_20(2,3,10)`, and `C_24(4,5,12)`.
- Alternate-notation search used
  `"CNB-coloring" circulant`,
  `"closed-neighborhood balanced" circulant`,
  and family-style `C_n(a,b,m)` / `C_n(S)` notation.
- Canonical source identified by the bounded pass:
  Collins, Bowie, Fox, Freyberg, Hauenstein, Marr, Minnich, Snyder, Trent, and Twombly,
  *Closed Neighborhood Balanced Coloring of Graphs*,
  Graphs and Combinatorics `41` (`2025`), article `107`,
  published online `2025-07-02` and corrected `2025-07-12`.
- Canonical-source check:
  Theorems `15` to `17` supply positive CNBC families for some quintic circulants;
  Theorem `19` handles the `n ≡ 2 (mod 4)` opposite-parity line and matches the alternating-witness boundary already visible here;
  and `Question 1` explicitly leaves open the `n ≡ 0 (mod 4)` quintic cases containing the campaign seeds.
  No theorem, proposition, example, corollary, observation, or sufficient-condition statement located in that source gives the present Route I spectral obstruction slice or settles `c16`, `c20`, or `c24`.
- Outside-source status search:
  DBLP indexes the `2025` paper, but the bounded outside-source pass did not surface a separate paper or proceedings item closing `Question 1` or announcing the current spectral theorem slice.
- Recent follow-up check:
  a `2026-03-09` arXiv preprint by Collins et al.,
  *Color 2-switches and neighborhood λ-balanced graphs with k colors*,
  shows active follow-up in the neighborhood-balanced line, but within this bounded pass it did not advertise a resolution of the open quintic `n ≡ 0 (mod 4)` cases or of the Route I statement.
- Prior-art verdict:
  within this bounded audit, the Route I slice does not read as a rediscovery, and the seed instances remain consistent with an open-family advance rather than a known corollary.

## publication_statement_faithfulness

- Is the strongest honest claim stronger than `here is an example`:
  yes.
  It is a quantified theorem slice over all `n = 2m`, `1 <= a < b < m` satisfying the nowhere-zero symbol hypothesis.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here:
  yes, but only as the narrow Route I spectral obstruction theorem.
  The current materials do not honestly support selling a full two-route theorem or a broader family classification.
- Is the proof structural or merely instance-specific:
  structural in mechanism.
  The core route is `CNB coloring -> kernel witness -> circulant Fourier diagonalization -> trivial kernel`.
  However, the reusable family writeup is still incomplete:
  `c16` is already a direct corollary,
  while `c20` and `c24` are still supporting structural evidence rather than headline corollaries.
- Would this survive a referee asking `what is the theorem?`:
  yes, if the paper states exactly the Route I spectral obstruction slice and labels `c20` as supporting infrastructure and `c24` as the periodicity companion.
  No, if the paper tries to claim a blanket nonexistence theorem for quintic circulants.
- Is the claim still too dependent on hand-picked small cases:
  not for the narrow Route I statement once the family proof closes,
  but yes for any broader rhetoric.
  `C_22(2,3,11)` remains the explicit boundary against that overclaim.
- Faithfulness verdict:
  the theorem statement is clean and referee-facing, but the campaign narrative must stay narrower than the three-seed dossier alone might tempt us to say.

## publication_theorem_worthiness

- This is not just a curiosity example.
  It isolates a reusable obstruction criterion on an infinite parameter family that the canonical `2025` source leaves open.
- The theorem is worth campaign priority because it converts three exact nonexistence proofs into one spectral statement with a clean lead corollary (`c16`) and a clear structural boundary (`C_22(2,3,11)`).
- The best honest package right now is still a theorem slice, not a finished family theorem:
  Route I is coherent,
  Route II is promising,
  and the combined two-route story is premature.
- The proof direction is structural rather than computational:
  no search-heavy core,
  no brute-force dependence,
  and the central ingredients are standard circulant/Fourier facts plus the CNB-to-kernel translation.
- Is the generalization route strong enough to merit campaign priority:
  yes, but only with disciplined scope.
  Finish Route I first; use new feeders only to test whether Route II deserves later theorem-slice promotion.

## publication_publishability

- Conservative publication verdict: `SLICE_CANDIDATE`.
- Why not `INSTANCE_ONLY`:
  the strongest honest claim is genuinely parameterized and stronger than the exact seeds.
- Why not `REDISCOVERY`:
  the bounded prior-art pass found the ambient quintic line still posed as open in the canonical `2025` paper, and no later public closure surfaced within budget.
- Why not `SLICE_EXACT`:
  the reusable family proof stack is not yet closed end to end.
  The mirrored Lean skeleton exists, but `lean/AutoMath/Families/CNBCQuinticRouteI.lean` is absent in this worktree,
  `lean/.lake/packages` is absent,
  and the six-term distinctness plus family Fourier / invertibility lemmas are not yet formalized in one buildable module.
- Why not `PAPER_READY`:
  a referee could still ask for the actual closed family proof rather than three strong dossiers plus a skeleton.
  The paper shape is visible, but the theorem slice is not yet expositionally or formally finished.
- Publishable shape if closed:
  a short spectral-obstruction note or theorem-slice paper anchored by the open-case status from `Question 1`,
  with `c16` as the flagship corollary and `c20` / `c24` as supporting mechanism and boundary evidence.
- Campaign priority verdict:
  keep this family active.
  Route I closure is publication-worthy enough to outrank unrelated fresh curation, but it does not justify automatic stop or `PAPER_READY`.

## strongest_honest_claim

- The strongest honest claim is the narrow Route I theorem slice:
  if `n = 2m`, `1 <= a < b < m`, and
  `sigma_{n,a,b}(k) = 1 + 2 cos(2*pi*a*k/n) + 2 cos(2*pi*b*k/n) + (-1)^k`
  is nonzero for every `k in Z/nZ`, then `C_n(a,b,m)` is not CNBC.
- Publication-facing caveat:
  this is stronger than a single example and is structurally motivated,
  but today it is still a slice candidate rather than a closed paper theorem.
  `c16-4-5-8-cnbc` is the lead direct corollary;
  `c20-2-3-10-cnbc` and `c24-4-5-12-cnbc` remain supporting evidence rather than additional headline corollaries.

## paper_title_hint

- `A spectral obstruction theorem slice for open quintic closed-neighborhood balanced circulants`

## next_action

- Restore a buildable Route I family module at `lean/AutoMath/Families/CNBCQuinticRouteI.lean`, restore Lean dependencies, and formalize six-term distinctness plus the family Fourier diagonalization / nowhere-zero-symbol implies trivial-kernel lemmas.
- Keep the paper statement fixed at the narrow Route I slice while that work closes.
- Only after the Route I module builds cleanly should the campaign spend new effort on `c28-2-3-14-cnbc` and `c28-4-5-14-cnbc` as discriminating feeders for whether Route II deserves theorem-slice promotion.
