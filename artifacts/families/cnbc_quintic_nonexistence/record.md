# Family Record: cnbc_quintic_nonexistence

## family_statement_lock

- Active `family_slug`: `cnbc_quintic_nonexistence`.
- Dossier path: `campaigns/cnbc_quintic_nonexistence.md`.
- Family artifact path: `artifacts/families/cnbc_quintic_nonexistence`.
- Locked family statement: let `G = C_n(a,b,m)` with `n = 2m` and `1 <= a < b < m`. The closed-neighborhood operator is
  `B_{n,a,b} = I + S^a + S^(-a) + S^b + S^(-b) + S^m`,
  with Fourier symbol
  `sigma_{n,a,b}(k) = 1 + 2 cos(2*pi*a*k/n) + 2 cos(2*pi*b*k/n) + (-1)^k`.
- Locked theorem target for this pass: Route I only.
  If `sigma_{n,a,b}(k) != 0` for every `k in Z/nZ`, then `C_n(a,b,m)` is not CNBC.
- Bounded local read set used in this pass:
  `selected_problem.md`,
  `campaigns/cnbc_quintic_nonexistence.md`,
  `artifacts/families/cnbc_quintic_nonexistence/record.md`,
  `artifacts/families/cnbc_quintic_nonexistence/status.json`,
  `PROOFS.md`,
  `artifacts/c16-4-5-8-cnbc/record.md`,
  `artifacts/c20-2-3-10-cnbc/record.md`,
  `artifacts/c24-4-5-12-cnbc/record.md`.
- `PROOFS.md` mattered only as a repository-state check. It does not preserve these seeds as completed Lean exacts; it only notes legacy CNBC Lean build failures such as `lean/AutoMath/C16458CNBC.lean` and `lean/AutoMath/C244512CNBC.lean`.
- No web was used. The local dossier and seed artifacts were sufficient to preserve the family statement cleanly.

## existing_instance_inventory

- `c16-4-5-8-cnbc`: `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, `lean_ready = true`. This is the lead direct Route I seed. Its proof uses the full six-term circulant operator, computes the family symbol exactly, and shows the symbol is nowhere zero, so the operator has trivial real kernel.
- `c20-2-3-10-cnbc`: `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, `lean_ready = true`. This is the strongest infrastructure seed. Its preserved argument uses the same CNB-to-circulant setup, then an opposite-pair reduction `y_i = x_i + x_{i+10}` to force `x_{i+10} = -x_i`, followed by a finite contradiction on `Z/10Z`. Verification also records full rank `20` for the original operator, so the seed is Route I compatible even though its written proof is reduction-first.
- `c24-4-5-12-cnbc`: `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, `lean_ready = true`. This is the periodicity companion seed. Its proof finds that the only zero frequencies are `k = 8,16`, so every real kernel vector lies in the primitive cube-root subspace and is therefore `3`-periodic, which no `{+1,-1}` pattern can satisfy.
- Inventory summary:
  `c16` is the clean direct corollary,
  `c20` is the reusable antipodal-reduction support case,
  `c24` is the clean low-order-kernel periodicity case.
- Explicit overclaim boundary already fixed by the campaign: `C_22(2,3,11)`.

## shared_structure

- Common decomposition / invariant / construction:
  encode a red/blue coloring by a sign vector `x in {+1,-1}^n`;
  then CNBC is equivalent to the kernel equation `B_{n,a,b} x = 0`.
- Common operator:
  `B_{n,a,b}` is the six-term circulant operator with mask `{0, +/-a, +/-b, m}`.
- Common spectral invariant:
  the Fourier characters of `Z/nZ` diagonalize `B_{n,a,b}` with eigenvalues `sigma_{n,a,b}(k)`.
- Common proof template:
  `CNB coloring -> nonzero sign vector in ker(B_{n,a,b}) -> spectral control of ker(B_{n,a,b}) -> contradiction`.
- Shared Route I mechanism:
  if the symbol is nowhere zero, then `B_{n,a,b}` is invertible and CNBC is impossible.
- Shared Route II mechanism:
  if the zero set is small and lies on low-order characters, then every kernel vector has forced short period, and the sign constraints can become impossible.
- Shared reduction mechanism from the antipodal generator:
  because `m = n/2`, opposite-pair sums `y_i = x_i + x_{i+m}` always collapse the CNB equations to a half-length circulant system. This is genuinely reusable, even though only the `(2,3,10)` seed currently carries the full contradiction through.

## parameter_sensitive_steps

- Genuinely scalable steps:
  for `1 <= a < b < m`, the residues `0, +/-a, +/-b, m` are pairwise distinct in `Z/nZ`, so each closed neighborhood has size `6`;
  CNBC translates exactly to `B_{n,a,b} x = 0` for a nonzero sign vector;
  Fourier characters diagonalize the family operator with eigenvalues `sigma_{n,a,b}(k)`;
  the nowhere-zero condition on `sigma_{n,a,b}` forces `ker(B_{n,a,b}) = {0}`;
  kernel support on characters of order `d` forces every real kernel vector to be `d`-periodic;
  opposite-pair summation always produces a half-length circulant reduction when `n = 2m`.
- Instance-specific steps:
  `c16` uses an exact odd/even trigonometric split to show the concrete symbol never vanishes;
  `c20` uses the exact complement identity on `Z/10Z`, the constant-pair-sum step `b_i = a_i + a_{i+5}`, and the seed-specific recurrence `a_{i+2} = -a_i`;
  `c24` uses the exact zero set `{8,16}`, the primitive cube-root kernel description, and the final `3`-periodic sign contradiction.
- Which steps genuinely scale in the parameters:
  the CNB-to-kernel translation,
  six-term distinctness,
  the family Fourier diagonalization,
  the nowhere-zero-symbol obstruction,
  and the general periodicity-from-kernel-support lemma.
- Which steps do not yet scale honestly:
  the seed-level trigonometric nonvanishing check for the `(4,5,8)` tuple,
  the `Z/10Z` complement trick in the `(2,3,10)` seed,
  and the exact cube-root identification in the `(4,5,12)` seed.
- Smallest likely counterexample or obstruction:
  if `m` is odd and `a,b` have opposite parity, then the alternating vector `x_i = (-1)^i` satisfies
  `B_{n,a,b} x = [1 + 2(-1)^a + 2(-1)^b + (-1)^m] x = 0`.
  The smallest campaign-relevant example is `C_22(2,3,11)`.

## candidate_theorem_slices

- Slice A: Route I spectral obstruction.
  If `sigma_{n,a,b}(k) != 0` for every `k in Z/nZ`, then `C_n(a,b,m)` is not CNBC.
- Slice B: low-order-kernel periodicity obstruction.
  If `ker(B_{n,a,b})` is supported only on characters of order `d`, and the induced `d`-periodic sign system has no `{+1,-1}` solution, then `C_n(a,b,m)` is not CNBC.
- Slice C: opposite-pair reduction infrastructure.
  For `n = 2m`, the quantities `y_i = x_i + x_{i+m}` satisfy a half-length circulant system; invertibility there can force `x_{i+m} = -x_i`.
- Slice D: alternating-witness counterexample boundary.
  If `m` is odd and `a,b` have opposite parity, then `x_i = (-1)^i` is a CNBC witness.
- Strongest plausible theorem slice:
  Slice A is the cleanest theorem statement now,
  Slice B is the strongest next theorem candidate,
  and Slice D is the smallest honest obstruction boundary that blocks wider rhetoric.

## chosen_slice

- Chosen slice: Slice A, the narrow Route I spectral obstruction theorem.
- Proposed theorem slice:
  let `n = 2m` and `G = C_n(a,b,m)` with `1 <= a < b < m`.
  If `sigma_{n,a,b}(k) != 0` for every `k in Z/nZ`, then `G` admits no closed-neighborhood balanced coloring.
- Why this is the strongest honest slice:
  `c16-4-5-8-cnbc` is already a direct application;
  `c20-2-3-10-cnbc` supports the same family mechanism but still reaches contradiction through a seed-specific reduction narrative;
  `c24-4-5-12-cnbc` is genuine evidence for a later periodicity theorem, not a direct Route I corollary;
  and `C_22(2,3,11)` blocks any blanket mixed-parity nonexistence claim.
- Strongest plausible theorem slice beyond this pass:
  a two-route spectral/periodicity theorem with Slice C as infrastructure and Slice D as an explicit boundary.
  That is not yet the strongest honest claim.

## reusable_lemmas

- Six-term distinctness lemma:
  for `n = 2m` and `1 <= a < b < m`, the residues `0, +/-a, +/-b, m` are pairwise distinct in `Z/nZ`.
- CNB-to-kernel lemma:
  `C_n(a,b,m)` is CNBC if and only if there exists a nonzero sign vector `x in {+1,-1}^n` with `B_{n,a,b} x = 0`.
- Family Fourier diagonalization lemma:
  every Fourier character of `Z/nZ` is an eigenvector of `B_{n,a,b}` with eigenvalue `sigma_{n,a,b}(k)`.
- Nowhere-zero symbol lemma:
  if `sigma_{n,a,b}(k) != 0` for every `k`, then `B_{n,a,b}` has trivial complex, hence real, kernel.
- Opposite-pair reduction lemma:
  for `n = 2m`, adding the CNB equations at `i` and `i+m` yields a half-length circulant system for `y_i = x_i + x_{i+m}`.
- Kernel-support periodicity lemma:
  if the real kernel is supported only on characters of order `d`, then every real kernel vector is `d`-periodic.
- Low-period sign obstruction lemma:
  if the induced `d`-periodic sign system has no `{+1,-1}` solution, then no CNBC coloring exists.
- Alternating boundary lemma:
  if `m` is odd and `a,b` have opposite parity, then `x_i = (-1)^i` is a nonzero kernel vector.

## proof_plan

- Main proof path:
  prove six-term distinctness;
  translate a hypothetical CNBC coloring into `B_{n,a,b} x = 0`;
  diagonalize `B_{n,a,b}` by Fourier characters;
  compute the family symbol `sigma_{n,a,b}(k)`;
  invoke the nowhere-zero hypothesis to force `ker(B_{n,a,b}) = {0}`;
  contradict the existence of a nonzero sign vector.
- Lead direct application:
  present `c16-4-5-8-cnbc` as the flagship corollary of the Route I theorem.
- Supporting application path:
  keep `c20-2-3-10-cnbc` as evidence that the same operator backbone also yields a reusable opposite-pair reduction lemma, even before the full family theorem package is formalized.
- Fallback path:
  if the family proof still does not close statement-faithfully, freeze the claim at a short Route I spectral-obstruction note with `c16` as the lead corollary, `c20` as infrastructure, `c24` as the periodicity companion, and `C_22(2,3,11)` as the explicit boundary.

## fallback_counterexample_plan

- Do not weaken the Route I hypothesis.
  The odd-`m`, opposite-parity alternating witness line is a genuine obstruction to broader blanket statements.
- Strongest fallback counterexample template:
  if `m` is odd and `a,b` have opposite parity, then the alternating coloring `x_i = (-1)^i` is a CNBC witness.
- Smallest likely counterexample:
  `C_22(2,3,11)`.
- If Route I stalls, keep two claims separate:
  the Route I spectral nonexistence slice on the one hand,
  and the alternating-witness counterexample boundary on the other.
- If a future feeder has a nontrivial zero set that is neither nowhere-zero nor low-order periodic, treat it as evidence against the current theorem template rather than forcing family-level rhetoric.

## next_best_feeder_instances

- `c28-2-3-14-cnbc`:
  smallest even-`m` continuation of the `(2,3,m)` line after `c20`;
  best discriminator for whether that line is genuinely Route I spectral at the full-operator level or remains reduction-first.
- `c28-4-5-14-cnbc`:
  smallest even-`m` continuation of the `(4,5,m)` line after `c16` and `c24`;
  best discriminator for whether the line stays in the nowhere-zero-symbol regime or flips back into the low-order-kernel periodicity regime.
- Boundary note:
  `c22-2-3-11-cnbc` is not a feeder for the flagship theorem.
  It is the obstruction boundary that keeps the theorem statement honest.

## publication_value

- Publication value is real because the campaign already supports a parameterized structural theorem slice, not just three isolated exact disproofs.
- The common backbone is reusable:
  CNB-to-kernel translation,
  a six-term circulant operator,
  Fourier diagonalization,
  and either invertibility or forced short-period kernel structure.
- The strongest honest publication package remains narrow:
  the Route I spectral obstruction theorem as the headline,
  `c16` as the direct corollary,
  `c20` as reusable infrastructure,
  `c24` as the periodicity companion,
  and `C_22(2,3,11)` as the explicit counterexample boundary.
- Honest publication status is still `SLICE_CANDIDATE`, not `SLICE_EXACT` or `PAPER_READY`, because the family proof stack is not yet closed end to end in one reusable theorem package.

## publication_prior_art_audit

- Bounded live-web audit on `2026-04-11` focused only on the narrow Route I slice, the three preserved seeds `c16`, `c20`, `c24`, and the explicit boundary `C_22(2,3,11)`.
- Exact-statement search used the claim-facing phrases
  `"closed neighborhood balanced" "quintic circulant"`,
  `"closed-neighborhood balanced" "C_n(d_1,d_2,n/2)"`,
  `"closed-neighborhood balanced" "Question 1" quintic`,
  and the exact seed notations `C_16(4,5,8)`, `C_20(2,3,10)`, and `C_24(4,5,12)`.
- Alternate-notation search used
  `"CNB-coloring" circulant`,
  `"closed-neighborhood balanced coloring of graphs" circulant`,
  family-style `C_n(a,b,m)` wording,
  and `C_n(S)`-style quintic circulant wording.
- Canonical source identified by the bounded pass:
  Collins, Bowie, Fox, Freyberg, Hauenstein, Marr, Minnich, Snyder, Trent, and Twombly,
  *Closed Neighborhood Balanced Coloring of Graphs*,
  Graphs and Combinatorics `41` (`2025`), article `107`,
  published online `2025-07-02` and corrected `2025-07-12`.
- Canonical-source theorem / proposition / example / corollary / observation / sufficient-condition check:
  Theorem `16` and Theorem `17` give CNBC existence families for some quintic circulants but not the present open mixed-parity `n ≡ 0 (mod 4)` line;
  Theorem `19` handles the `n ≡ 2 (mod 4)` opposite-parity line and matches the alternating-witness boundary already visible here;
  Question `1` explicitly asks the remaining `n ≡ 0 (mod 4)` cases, including the campaign line with `d_1 ≡ 0 (mod 4)` and `d_2` odd.
  Within that source I did not find a theorem, proposition, example, observation, corollary, or sufficient-condition statement giving the Route I spectral obstruction slice or settling `c16`, `c20`, or `c24`.
- Outside-source status search:
  DBLP indexes the `2025` paper, but the bounded outside-source pass did not surface a separate later paper, proceedings item, or thesis chapter closing Question `1` or stating the present Route I slice.
- Recent citation / discussion / follow-up check:
  the Springer article page showed `1` citation at access time, and the bounded follow-up / discussion pass only surfaced the project-level AWM abstract rather than a later public resolution of the open quintic `n ≡ 0 (mod 4)` line.
- Prior-art verdict:
  rediscovery is not established in this bounded audit.

## publication_statement_faithfulness

- Is the strongest honest claim stronger than `here is an example`:
  yes.
  It is a quantified theorem slice over an infinite class of `C_n(a,b,m)`, not a report about one hand-picked seed.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here:
  yes.
  The real claim is the narrow Route I statement: nowhere-zero family symbol implies nonexistence of a CNBC coloring.
- Is the proof structural or merely instance-specific:
  the intended mechanism is structural, but the preserved proof stack is mixed.
  Exact Lean artifacts exist at `lean/AutoMath/C16458CNBC.lean`, `lean/AutoMath/C202310CNBC.lean`, and `lean/AutoMath/C244512CNBC.lean`;
  however `c16` and `c20` are formalized by `native_decide`, `c24` is formalized by an exact instance-specific linear-combination argument, and the reusable family file exists only as a mirror under `artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`, not at the root build path.
- Would this survive a referee asking `what is the theorem?`:
  yes, if the paper states exactly the Route I spectral slice and treats `c20` and `c24` as supporting structure and boundary evidence.
  No, if it claims a finished two-route theorem or a broad classification of quintic circulants.
- Is the claim still too dependent on hand-picked small cases:
  less so at the statement level than at the preserved-proof level.
  The theorem statement itself is not instance-only, but the current written and formal support still leans on three small exact instances, with only `c16` being a direct Route I corollary in its preserved narrative.
- Is the generalization route strong enough to merit campaign priority:
  yes.
  The canonical source leaves the line open, the theorem statement is clean, and `C_22(2,3,11)` gives an honest boundary that prevents overclaim.
- Faithfulness verdict:
  the theorem statement is real and referee-facing, but the campaign must stay pinned to the narrow Route I slice.

## publication_theorem_worthiness

- This is stronger than an example because it isolates a reusable obstruction mechanism on an open parameter line, not just three isolated counterexamples.
- There is a real referee-facing theorem here:
  if the six-term circulant symbol is nowhere zero, then the CNBC equation has only the zero kernel vector, so the graph is not CNBC.
- The theorem is worth campaign priority because it converts the seed wins into one structural statement with a clean lead corollary (`c16`) and an explicit overclaim boundary (`C_22(2,3,11)`).
- The proof direction is mathematical and structural rather than search-heavy, but the preserved package is not yet publication-closed because the reusable family proof is not written once in a single statement-faithful module.
- The best honest medium-term claim is still a theorem slice, not a finished family theorem:
  Route I is coherent;
  Route II remains promising but unclosed;
  the combined two-route package is not ready for the headline.
- Theorem-worthiness verdict:
  real theorem slice,
  real campaign priority,
  not yet a finished paper claim.

## publication_publishability

- Conservative publication verdict: `SLICE_CANDIDATE`.
- Why not `INSTANCE_ONLY`:
  the strongest honest claim is parameterized and stronger than any single seed.
- Why not `REDISCOVERY`:
  bounded prior-art checking still points to Question `1` in the `2025` canonical source as open, and no later public closure surfaced within budget.
- Why not `SLICE_EXACT`:
  the family proof stack is not yet preserved end to end.
  `lean/AutoMath/Families/CNBCQuinticRouteI.lean` is absent in this worktree,
  `lean/.lake/packages` is absent,
  and the current exact Lean files are instance-level proofs rather than a reusable formalization of the Route I theorem slice.
- Why not `PAPER_READY`:
  a referee could still ask for the actual family proof, not just the right statement plus three good dossiers and a mirror skeleton.
- Publishable shape if closed:
  a short spectral-obstruction note or slice paper centered on the open quintic line from Question `1`,
  with `c16` as the lead corollary,
  `c20` as opposite-pair infrastructure,
  `c24` as the periodicity companion,
  and `C_22(2,3,11)` as the explicit boundary.
- Campaign priority verdict:
  keep this family active and ahead of unrelated fresh curation until the Route I closure either lands or fails honestly.

## strongest_honest_claim

- For the open quintic CNBC line left unresolved by Question `1` in the `2025` canonical source, the strongest honest claim is the narrow Route I theorem slice:
  if `n = 2m`, `1 <= a < b < m`, and
  `sigma_{n,a,b}(k) = 1 + 2 cos(2*pi*a*k/n) + 2 cos(2*pi*b*k/n) + (-1)^k`
  is nonzero for every `k in Z/nZ`, then `C_n(a,b,m)` is not CNBC.
- `c16-4-5-8-cnbc` is the lead direct corollary.
- `c20-2-3-10-cnbc` and `c24-4-5-12-cnbc` are supporting structural evidence, not additional headline corollaries.

## paper_title_hint

- `A spectral obstruction theorem slice for open quintic closed-neighborhood balanced circulants`

## next_action

- Restore a buildable root family module at `lean/AutoMath/Families/CNBCQuinticRouteI.lean` from the mirrored family artifact.
- Restore Lean dependencies so the family path can actually be built again.
- Replace the current instance-level dependence with reusable Route I lemmas:
  six-term distinctness,
  CNB-to-kernel,
  family Fourier diagonalization,
  and nowhere-zero-symbol implies trivial kernel.
- Keep the paper statement fixed at the narrow Route I slice while that closes.
- Only after that closure should the campaign spend new effort on `c28-2-3-14-cnbc` and `c28-4-5-14-cnbc` as discriminating feeders for Route II.
