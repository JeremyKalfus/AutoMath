# Family Record: cnbc_quintic_nonexistence

## family_statement_lock

- Active `family_slug`: `cnbc_quintic_nonexistence`.
- Dossier path: `campaigns/cnbc_quintic_nonexistence.md`.
- Family artifact path: `artifacts/families/cnbc_quintic_nonexistence`.
- Sidecar proof-attempt mode: absent in `selected_problem.md`, so this GENERALIZE pass writes the canonical family outputs.
- Locked family statement:
  let `G = C_n(a,b,m)` with `n = 2m` and `1 <= a < b < m`. Encode a red/blue coloring by a sign vector `x : Z/nZ -> {+1,-1}` and define
  `B_{n,a,b} = I + S^a + S^(-a) + S^b + S^(-b) + S^m`.
  Then `G` is CNBC exactly when `B_{n,a,b} x = 0` has a nonzero sign-valued solution.
- Locked Fourier symbol:
  `sigma_{n,a,b}(k) = 1 + 2 cos(2*pi*a*k/n) + 2 cos(2*pi*b*k/n) + (-1)^k`.
- Locked theorem target for this pass:
  Route I only. If `sigma_{n,a,b}(k) != 0` for every discrete frequency `k`, then `G` is not CNBC.
- Preserved family proof shell:
  `artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`
  contains the checked CNB-to-kernel bridge `kernel_witness_of_intendedStatement`, the closure theorem `routeI_of_trivialKernel`, and the shell `routeI_spectral_obstruction_skeleton`.
- Missing scalable middle step:
  the family Fourier diagonalization of `B_{n,a,b}` and the implication
  `sigma nowhere zero -> TrivialQuinticKernel n a b m`.
- `PROOFS.md` relevance check:
  local search found no hits for `c16-4-5-8-cnbc`, `c20-2-3-10-cnbc`, or `c24-4-5-12-cnbc`, so no additional Lean-backed exact seed had to be absorbed here.
- Bounded local sources used:
  `AGENTS.md`,
  `selected_problem.md`,
  `campaigns/cnbc_quintic_nonexistence.md`,
  `artifacts/families/cnbc_quintic_nonexistence/record.md`,
  `artifacts/families/cnbc_quintic_nonexistence/status.json`,
  `PROOFS.md` by exact search only,
  `artifacts/c16-4-5-8-cnbc/record.md`,
  `artifacts/c20-2-3-10-cnbc/record.md`,
  `artifacts/c24-4-5-12-cnbc/record.md`,
  and `artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`.
- No web was used in this GENERALIZE pass.

## existing_instance_inventory

- `c16-4-5-8-cnbc`:
  `verify_verdict = VERIFIED`, `classification = COUNTEREXAMPLE`, `lean_ready = true`.
  This is the clean direct Route I seed. Its proof computes the six-term symbol
  `1 + 2 cos(k*pi/2) + 2 cos(5*k*pi/8) + (-1)^k`
  and shows it is nonzero for every `k in Z/16Z`, so the `16 x 16` closed-neighborhood operator is invertible.
- `c20-2-3-10-cnbc`:
  `verify_verdict = VERIFIED`, `classification = COUNTEREXAMPLE`, `lean_ready = true`.
  This seed uses opposite-pair compression:
  `y_i = x_i + x_{i+10}` satisfies a length-`10` circulant system with nonzero reduced eigenvalues, forcing `x_{i+10} = -x_i`; a separate finite contradiction on `Z/10Z` then closes the disproof.
  The verification artifact also reports full rank `20` for the original CNB matrix, so the tuple is structurally compatible with Route I even though that direct family-style proof is not the preserved exact proof.
- `c24-4-5-12-cnbc`:
  `verify_verdict = VERIFIED`, `classification = COUNTEREXAMPLE`, `lean_ready = true`.
  This is the clean theorem-boundary seed. Its symbol vanishes exactly at `k = 8,16`, so the real kernel is the primitive cube-root subspace; every real solution is therefore `3`-periodic, and no `{+1,-1}`-valued `3`-periodic pattern satisfies the zero-sum condition.
- Inventory verdict:
  `c16` is the lead direct Route I corollary,
  `c20` is the strongest structurally compatible support case,
  and `c24` is the clearest boundary example showing why the present headline should stay narrower than a finished two-route theorem.

## shared_structure

- Common decomposition:
  a red/blue coloring is encoded by a sign vector `x in {+1,-1}^n`.
- Common invariant:
  CNBC is equivalent to the six-term circulant kernel equation `B_{n,a,b} x = 0`.
- Common construction:
  the discrete Fourier characters of `Z/nZ` diagonalize `B_{n,a,b}` with eigenvalues `sigma_{n,a,b}(k)`.
- Shared proof template:
  translate CNBC to a nonzero kernel witness,
  diagonalize the six-term operator,
  inspect the zero set of `sigma_{n,a,b}`,
  and conclude either trivial kernel or kernel support on low-order modes forcing forbidden periodicity.
- Common family discriminator:
  the zero set of `sigma_{n,a,b}` organizes all three seed proofs.
- Route split exposed by the seeds:
  Route I is the nowhere-zero-symbol obstruction;
  Route II is the low-order-kernel-support / periodicity obstruction.

## parameter_sensitive_steps

- Steps that genuinely scale in the parameters:
  the neighborhood mask `{0, +/-a, +/-b, m}`,
  the CNB-to-kernel translation,
  the Fourier diagonalization of `B_{n,a,b}`,
  and the implication
  `sigma_{n,a,b}(k) != 0 for all k -> ker(B_{n,a,b}) = {0}`.
- Steps that plausibly scale but are not yet preserved as honest family lemmas:
  opposite-pair compression on the `(2,3,m)` line,
  and low-order spectral support forcing low-period real kernel vectors.
- Steps that are instance-specific:
  the odd/even trigonometric split in `c16`,
  the complement identity and constant-pair-sum contradiction in `c20`,
  and the exact zero set `{8,16}` plus primitive cube-root analysis in `c24`.
- Strongest plausible theorem slice:
  the Route I nowhere-zero-symbol obstruction.
- Smallest likely counterexample or obstruction to any broader slogan:
  `C_10(2,3,5)`, via the alternating witness `x_i = (-1)^i` on the odd-`m`, opposite-parity boundary.
- Honest scaling verdict:
  Route I scales cleanly now.
  The periodicity side is a real template supported by exact seeds, but it is not yet preserved as a reusable family theorem.

## candidate_theorem_slices

- Slice A: Route I spectral obstruction.
  For `G = C_n(a,b,m)` with `n = 2m` and `1 <= a < b < m`, if `sigma_{n,a,b}(k) != 0` for every discrete frequency `k`, then `G` is not CNBC.
- Slice B: opposite-pair compression theorem on the `(2,3,m)` line.
  In `C_{2m}(2,3,m)`, adding the equations at `i` and `i + m` produces a half-length circulant obstruction on `y_i = x_i + x_{i+m}`; if the reduced symbol is nowhere zero and the reduced recurrence is sign-incompatible, then the graph is not CNBC.
- Slice C: low-order-kernel periodicity theorem.
  If the zero set of `sigma_{n,a,b}` is supported only on characters of order `d`, then every real kernel vector is `d`-periodic; if no `{+1,-1}` `d`-periodic pattern satisfies the induced relation, then `G` is not CNBC.
- Slice D: method-and-boundaries package.
  Publish the general CNB-to-kernel translation and the checked Route I shell as the reusable method, with `c16` as the direct corollary, `c20` as support, and `c24` plus `C_10(2,3,5)` as explicit theorem limits.

## chosen_slice

- Chosen slice:
  Slice A, the Route I nowhere-zero-symbol obstruction.
- Proposed theorem slice:
  let `G = C_n(a,b,m)` with `n = 2m` and `1 <= a < b < m`.
  If `sigma_{n,a,b}(k) != 0` for every discrete frequency `k`, then `G` admits no closed-neighborhood balanced coloring.
- Why this is the strongest honest slice:
  it uses only the genuinely scalable part of the shared mechanism,
  it matches the preserved Lean shell exactly,
  it explains `c16` completely,
  it stays compatible with the stronger-but-differently-written `c20` evidence,
  and it respects the `c24` and alternating-coloring boundaries.
- Boundary facts that must remain explicit:
  `c24-4-5-12-cnbc` shows that zero frequencies do not imply existence;
  `C_10(2,3,5)` shows that dropping the nowhere-zero hypothesis is false.
- Honest status:
  the theorem sentence is stable, but the family Fourier diagonalization and the nowhere-zero-symbol-implies-trivial-kernel lemma are not yet preserved in checked family form.
  So the honest labels remain `classification = CANDIDATE` and `publication_status = SLICE_CANDIDATE`.

## reusable_lemmas

- Six-distinct-neighborhood lemma:
  under `n = 2m` and `1 <= a < b < m`, the closed neighborhood is exactly `{i, i +/- a, i +/- b, i + m}` and has cardinality `6`.
- CNB-to-kernel witness lemma:
  any CNBC coloring yields a nonzero integer-valued kernel witness for the six-term operator.
  This is already preserved as `kernel_witness_of_intendedStatement`.
- Fourier diagonalization lemma:
  each discrete character of `Z/nZ` is an eigenvector of `B_{n,a,b}` with eigenvalue `sigma_{n,a,b}(k)`.
- Nowhere-zero-symbol implies trivial-kernel lemma:
  if `sigma_{n,a,b}(k) != 0` for every discrete frequency `k`, then `TrivialQuinticKernel n a b m`.
  This is the main missing family lemma.
- Route I closure lemma:
  `routeI_of_trivialKernel`.
  This is already preserved and closes the theorem slice once the Fourier lemma exists.
- Opposite-pair compression lemma:
  when `n = 2m`, adding the equations at `i` and `i + m` yields a half-length circulant system on `y_i = x_i + x_{i+m}`.
  This is the strongest fallback structural lemma for the `(2,3,m)` line.
- Low-order-support periodicity lemma:
  if the real kernel is supported only on characters of order `d`, then every real kernel vector is `d`-periodic.
  This is the right Route II template, but it is not yet preserved as a reusable family theorem.
- Alternating boundary lemma:
  if `m` is odd and `a,b` have opposite parity, then `x_i = (-1)^i` is a kernel witness because
  `B_{n,a,b} x = (1 + 2(-1)^a + 2(-1)^b + (-1)^m) x = 0`.

## proof_plan

- Main proof path:
  prove the six-distinct-neighborhood lemma once for `1 <= a < b < m`,
  formalize the Fourier diagonalization of the six-term circulant `B_{n,a,b}`,
  deduce `TrivialQuinticKernel` from the nowhere-zero-symbol hypothesis,
  apply `routeI_of_trivialKernel`,
  and package `c16-4-5-8-cnbc` as the lead direct corollary.
- Strongest path forward:
  keep the campaign fixed on Route I only:
  `CNB -> nonzero kernel witness`,
  `nowhere-zero symbol -> trivial kernel`,
  `trivial kernel -> no CNBC`.
  After that closes, either absorb `c20` into the same route by a direct symbol computation or keep it as support rather than forcing it into the theorem statement.
- Fallback path:
  if the family Fourier lemma still does not close cleanly, preserve a method-and-boundaries package rather than broadening the claim:
  `c16` as the direct Route I corollary,
  `c20` as the opposite-pair support case,
  `c24` as the low-order-kernel boundary,
  and `C_10(2,3,5)` as the smallest obstruction to any overbroad nonexistence slogan.

## fallback_counterexample_plan

- Best generalized conjecture/template if the slice still does not close:
  keep Route I itself as the publication-facing claim:
  nowhere-zero six-term symbol forces nonexistence of a CNBC coloring.
- Strongest boundary mechanism:
  the odd-`m`, opposite-parity alternating-coloring witness.
- Smallest likely counterexample or obstruction:
  `C_10(2,3,5)`.
- Strongest preserved theorem-limit seed:
  `c24-4-5-12-cnbc`, where the symbol has zeros but nonexistence still follows by forced `3`-periodicity.
- If a broader two-route theorem is attempted too early:
  the missing ingredient is a reusable low-order-support lemma that actually covers both `c20` and `c24`, not another slogan.

## next_best_feeder_instances

- `c28-2-3-14-cnbc`:
  the smallest next extension of the `(2,3,m)` line.
  It best discriminates between
  "this line folds back into Route I after a direct symbol computation"
  and
  "this line still wants an opposite-pair-specific theorem shell."
- `c28-4-5-14-cnbc`:
  the smallest next extension of the `(4,5,m)` line beyond the current `c16` Route I seed and `c24` periodicity boundary.
  It tests whether that line returns to the nowhere-zero-symbol regime or keeps producing small-kernel periodicity behavior.
- Feeder priority:
  run `c28-2-3-14-cnbc` first if only one feeder fits in the next bounded cycle,
  then `c28-4-5-14-cnbc`.

## publication_value

- This campaign is already stronger than a list of exact counterexamples.
  It has one locked six-term operator, one locked spectral invariant, one preserved Route I shell, one clean direct corollary, and one explicit boundary mechanism.
- The strongest honest publication object supported by the bounded local evidence is still a theorem slice:
  a spectral obstruction to CNBC colorings of quintic circulants.
- Honest paper shape:
  Route I theorem slice in the headline,
  `c16-4-5-8-cnbc` as the lead direct corollary,
  `c20-2-3-10-cnbc` as line-discriminating support,
  and `c24-4-5-12-cnbc` together with `C_10(2,3,5)` as explicit theorem boundaries.
- Publication framing should avoid claiming a finished two-route family theorem until the periodicity side is preserved as a reusable lemma rather than only exact-case narration.
- Honest publication status remains `SLICE_CANDIDATE`.
  The campaign is stronger than `INSTANCE_ONLY`, but it is not yet `SLICE_EXACT`, `FAMILY_CANDIDATE`, or `PAPER_READY`.

## publication_prior_art_audit

- Bounded live-web audit on `2026-04-12` stayed claim-specific:
  exact Route I wording,
  alternate notation `C_n(d_1,d_2,n/2)` / `C_n(a,b,m)`,
  the exact tuples `C_16(4,5,8)`, `C_20(2,3,10)`, and `C_24(4,5,12)`,
  the canonical CNBC paper,
  one outside bibliographic/status search,
  and one recent discussion sweep.
- Exact-statement search on
  `"closed neighborhood balanced" "quintic circulant"`,
  `"closed-neighborhood balanced" "C_n(d_1,d_2,n/2)"`,
  and the exact tuple strings surfaced only the canonical CNBC paper or no independent hits.
- Alternate-notation search on
  `C_n(d_1,d_2,n/2)`,
  `C_n(a,b,m)`,
  and quintic-circulant wording again pointed back to Collins et al., *Closed Neighborhood Balanced Coloring of Graphs*, `Graphs and Combinatorics` `41` (`2025`).
- Canonical-source theorem / proposition / example / corollary / observation / sufficient-condition check:
  same-source inspection around Theorems `16`, `17`, `19`, and `Question 1` found nearby quintic families and boundary cases, but no theorem, proposition, example, corollary, observation, or sufficient-condition statement there already gives the Route I nowhere-zero-symbol slice or settles the exact tuples `c16`, `c20`, or `c24`.
- The canonical source still treats the remaining quintic mixed-parity cases around `C_n(d_1,d_2,n/2)` as open under `Question 1`, which is exactly the zone this campaign is trying to cut into.
- Outside-source status search was kept narrow:
  DBLP indexes the `2025` paper and adjacent NBC bibliography, but the bounded sweep did not surface a later paper, proceedings item, thesis chapter, or survey already closing the Route I slice or the three exact tuples.
- Recent follow-up / discussion check:
  the `2025` AWM abstract `Closed Neighborhood Balanced Graphs` discusses the topic broadly, but the bounded pass did not find a later public discussion or citation trail already resolving the active quintic line.
- Caution:
  absence of hits is not proof of novelty.
  It only means the bounded audit did not find an independent closure.
- Prior-art verdict:
  rediscovery is not established in this bounded audit.

## publication_statement_faithfulness

- Is the strongest honest claim stronger than `here is an example`:
  yes.
  It is quantified over an infinite family of `C_n(a,b,m)` with `n = 2m` and `1 <= a < b < m`.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here:
  yes.
  The real claim is the Route I slice:
  nowhere-zero six-term symbol implies no CNBC coloring.
- Is the proof structural or merely instance-specific:
  the intended mechanism is structural at the operator / Fourier level, but the preserved proof stack is not yet fully structural end to end.
  The checked family artifact is still the mirror file `artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`; the family Fourier diagonalization, the lemma `sigma nowhere zero -> TrivialQuinticKernel`, and the official backend copy claimed in `selected_problem.md` are not yet present as completed local artifacts.
- Would this survive a referee asking `what is the theorem?`:
  yes, if the paper states only the narrow Route I slice and treats `c20` and `c24` as support and theorem-boundary evidence.
  No, if it claims a finished two-route theorem or a classification of quintic circulants.
- Is the claim still too dependent on hand-picked small cases:
  at the statement level, not fatally.
  At the evidence level, still somewhat:
  `c16` is a direct Route I corollary, but `c20` and `c24` still function mainly as structurally compatible support and boundary evidence rather than as direct proofs of the same headline theorem.
- Is the generalization route strong enough to merit campaign priority:
  yes.
  The canonical source still leaves this regime open, the theorem sentence is clean, and the three verified seeds share one six-term circulant backbone.
- Faithfulness verdict:
  the theorem statement is real and referee-facing, but the campaign must stay pinned to Route I only.

## publication_theorem_worthiness

- There is a real theorem here, not just examples:
  a reusable spectral obstruction slice on a still-open family from the canonical source.
- The strongest honest claim is stronger than an example because it explains a whole parameterized obstruction mechanism:
  whenever the six-term symbol is nowhere zero, the CNBC system has only the zero kernel vector.
- The proof program is structural rather than search-heavy:
  `CNB coloring -> nonzero kernel witness -> Fourier diagonalization -> trivial kernel -> contradiction`.
- But the package is not yet referee-closed.
  The decisive family middle step is still missing in preserved form, and the locally checked family proof is still mirror-only rather than synchronized with an official backend theorem file.
- A referee asking `what is the theorem?` would receive a clean answer if the headline stays at Route I.
  A referee asking `where is the reusable family proof?` would still have a valid objection today.
- The claim is still somewhat dependent on small cases because only `c16` is presently a direct corollary, `c20` is structurally compatible support, and `c24` is best read as a theorem limit showing why Route II should not yet be in the headline.
- The generalization route is strong enough to keep campaign priority.
  It is the shortest path from verified feeder evidence to a publishable theorem slice, whereas unrelated fresh curation would dilute the strongest live structure.
- Theorem-worthiness verdict:
  real theorem slice,
  real campaign priority,
  not yet a closed paper theorem.

## publication_publishability

- Conservative publication verdict:
  `SLICE_CANDIDATE`.
- Why not `INSTANCE_ONLY`:
  the strongest honest claim is a quantified family slice, not a single tuple.
- Why not `REDISCOVERY`:
  the bounded prior-art pass did not establish an earlier closure of the slice or of the seed tuples.
- Why not `SLICE_EXACT`:
  the family Fourier diagonalization is still missing,
  the reusable implication `sigma nowhere zero -> TrivialQuinticKernel` is still missing,
  and no local official backend file `lean/AutoMath/Families/CNBCQuinticRouteI.lean` is present despite the preserved mirror shell.
- Why not `FAMILY_CANDIDATE`:
  the honest paper-facing claim is still one narrow route, not yet a broader family theorem that also closes the periodicity side.
- Why not `PAPER_READY`:
  a referee could still ask for the actual family proof, not just the right theorem sentence plus three exact dossiers and one mirror shell.
- Honest publishable shape if Route I closes:
  a short spectral-obstruction note or theorem-slice paper with `c16` as the lead corollary,
  `c20` as structurally compatible support,
  and `c24` plus `C_10(2,3,5)` as explicit theorem boundaries.
- Campaign priority verdict:
  keep this family active.
  Do not reopen broad curation unless Route I formalization stalls again after the Fourier middle step is attacked directly.

## strongest_honest_claim

- As of `2026-04-12T03:11:23-0400`, the strongest honest publication-facing claim is still a Route I theorem-slice candidate:
  for `G = C_n(a,b,m)` with `n = 2m` and `1 <= a < b < m`, if
  `sigma_{n,a,b}(k) = 1 + 2 cos(2*pi*a*k/n) + 2 cos(2*pi*b*k/n) + (-1)^k`
  is nonzero at every discrete frequency, then `G` is not CNBC.
- The CNB-to-kernel bridge `kernel_witness_of_intendedStatement`, the shell `routeI_spectral_obstruction_skeleton`, and the closure theorem `routeI_of_trivialKernel` are checked in the family mirror file
  `artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`.
- The family Fourier diagonalization, the reusable implication
  `sigma nowhere zero -> TrivialQuinticKernel`,
  and a synchronized official backend copy at `lean/AutoMath/Families/CNBCQuinticRouteI.lean`
  are not yet present in this worktree.
- Therefore the honest publication label remains `SLICE_CANDIDATE` rather than `SLICE_EXACT`.

## paper_title_hint

- `A Spectral Obstruction to Closed-Neighborhood Balanced Colorings of Quintic Circulants`

## next_action

- Keep the campaign fixed on Route I only.
- Formalize the family Fourier diagonalization of `B_{n,a,b}` and the implication
  `sigma nowhere zero -> TrivialQuinticKernel`
  in a reusable family theorem.
- Restore or create the official backend file
  `lean/AutoMath/Families/CNBCQuinticRouteI.lean`
  so the checked family shell is not mirror-only in this worktree.
- Only after that closes should `c16-4-5-8-cnbc` be packaged as the lead direct corollary.
  Keep `c20-2-3-10-cnbc` as support and keep `c24-4-5-12-cnbc` plus `C_10(2,3,5)` as explicit theorem boundaries unless a reusable Route II lemma is actually written.

## lean_statement

- Lean target chosen for this bounded LEAN pass:
  preserve the strongest honest checked Route I theorem-slice shell in the official backend, not a
  fake completion of the missing spectral theorem.
- Exact theorem statement synchronized into the official backend:
  `theorem routeI_of_trivialKernel {n a b m : Nat} (hn : 0 < n)
    (htrivial : TrivialQuinticKernel n a b m) : ¬ intendedStatement n a b m`.
- Why this is the honest target:
  the reusable family Fourier diagonalization of `B_{n,a,b}` and the implication
  `sigma nowhere zero -> TrivialQuinticKernel n a b m`
  are still unformalized in this worktree, so the strongest honest formal object is the checked
  closure theorem plus its Route I skeleton, not the full publication headline.

## lean_skeleton

- Preserved proof skeleton:
  assume `hExists : intendedStatement n a b m`,
  obtain a nonzero integer kernel witness from
  `kernel_witness_of_intendedStatement hn hExists`,
  then contradict `TrivialQuinticKernel n a b m`.
- Intermediate checked shell kept explicit:
  `routeI_spectral_obstruction_skeleton` packages the same contradiction through
  `NoNonzeroQuinticKernel n a b m`.
- Lean layout chosen for this pass:
  keep the family mirror file
  `artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`
  and synchronize the same checked shell into the official backend file
  `lean/AutoMath/Families/CNBCQuinticRouteI.lean`.

## lean_result

- Created the official backend copy
  `lean/AutoMath/Families/CNBCQuinticRouteI.lean`
  by mirroring the already checked family Route I shell.
- Local direct Lean checks succeeded on both copies:
  `lean artifacts/families/cnbc_quintic_nonexistence/lean/AutoMath/Families/CNBCQuinticRouteI.lean`
  and
  `lean lean/AutoMath/Families/CNBCQuinticRouteI.lean`.
- Honest Lean outcome:
  the CNB-to-kernel bridge `kernel_witness_of_intendedStatement`,
  the shell `routeI_spectral_obstruction_skeleton`,
  and the closure theorem `routeI_of_trivialKernel`
  are now preserved both in the family mirror and in the official backend.
- No `EXACT` upgrade was earned in this run, so `PROOFS.md` was left unchanged.

## lean_blockers

- Mathematical blocker:
  the family Fourier diagonalization of the six-term circulant operator `B_{n,a,b}` is still
  missing, as is the reusable implication
  `sigma nowhere zero -> TrivialQuinticKernel n a b m`.
- Publication blocker:
  without that middle family lemma, the honest campaign label stays
  `classification = CANDIDATE` and `publication_status = SLICE_CANDIDATE`
  even though the Route I shell is now synchronized in the official backend.
- Environment blocker:
  `cd lean && lake env lean ...` attempted to fetch `mathlib` because the local Lake dependencies
  are not materialized in this worktree, so under the no-network constraint the honest check
  available here was direct local `lean`, not a Lake build.
