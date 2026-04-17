# Solve Record: The Exact Value of R(B12, B14)

- slug: `r-b12-b14-book-ramsey`
- working_packet: `artifacts/r-b12-b14-book-ramsey/working_packet.md`

## statement_lock
Target theorem: `R(B12, B14) = 53`.

Locked exact statement for this solve attempt: every graph `G` on `53` vertices contains a `B12`, or its complement `\bar G` contains a `B14`.

Equivalent counterexample formulation: there is no graph `G` on `53` vertices such that
- every edge of `G` has at most `11` common neighbors, and
- every edge of `\bar G` has at most `13` common neighbors.

If this closes, the exact title theorem is: `The Exact Value of R(B12, B14)`.

## definitions
`B_t` denotes the book graph with `t` pages, i.e. `t` triangles sharing a common spine edge.

For an edge `uv` in `G`, write `c_G(u,v) = |N_G(u) ∩ N_G(v)|`. Then `G` contains `B12` iff some edge has `c_G(u,v) >= 12`.

For a nonedge `uv` in `G`, the corresponding edge in `\bar G` has
`c_{\bar G}(u,v) = |N_{\bar G}(u) ∩ N_{\bar G}(v)|`,
which is the number of vertices adjacent to neither `u` nor `v` in `G`. Thus `\bar G` contains `B14` iff some nonedge `uv` of `G` has `c_{\bar G}(u,v) >= 14`.

Notation used below:
- `n = 53`
- `e = e(G)`
- `T = #` triangles of `G`
- `\bar T = #` triangles of `\bar G`
- `d_1, ..., d_53` are the vertex degrees in `G`
- `S_1 = \sum_i d_i = 2e`
- `S_2 = \sum_i d_i^2`

Ambiguities/conventions fixed for this attempt:
- the book parameter counts pages, so the local edge threshold is `11` for avoiding `B12` and `13` for avoiding `B14` in the complement
- the solve uses only the stated one-gap window `53 <= R(B12, B14) <= 54` as input
- no search witness is pursued unless the structural proof fails

## approach_A
Structural / invariant approach.

Start from local book bounds and global triangle counting.

1. Since every edge of `G` lies in at most `11` triangles,
   `3T = \sum_{uv in E(G)} c_G(u,v) <= 11e`.
   Hence `T <= 11e/3`.

2. Since every edge of `\bar G` lies in at most `13` triangles,
   `3\bar T <= 13 e(\bar G) = 13(\binom{53}{2} - e)`.

3. Goodman's identity gives
   `T + \bar T = \binom{53}{3} - (1/2)\sum_i d_i(52 - d_i)`.

4. Combining the previous three displays yields
   `3S_2 - 154S_1 + 104728 <= 0`.

5. Recenter at degree `26`: write `d_i = 26 + x_i`. Then
   `3S_2 - 154S_1 + 104728 = 3\sum_i x_i^2 + 2\sum_i x_i`.

6. Therefore
   `3\sum_i x_i^2 + 2\sum_i x_i <= 0`.
   Since each `x_i` is an integer, `\sum_i x_i^2 >= \sum_i |x_i| >= |\sum_i x_i|`.
   If `\sum_i x_i < 0`, then
   `3\sum_i x_i^2 >= 3|\sum_i x_i| > 2|\sum_i x_i|`,
   contradiction.
   If `\sum_i x_i > 0`, the left side is already positive.
   Hence `\sum_i x_i = 0`, and then the inequality forces `\sum_i x_i^2 = 0`.

Conclusion of Approach A: any counterexample would have to be exactly `26`-regular, and all global inequalities above are actually equalities.

Self-check after Approach A: the algebra is tight and integral; there is no asymptotic step and no hidden dependence on outside literature beyond the known one-gap window.

## approach_B
Construction / contradiction approach.

Assume a `53`-vertex counterexample exists and push the equality case to a rigid parameter set.

From Approach A, the graph would have to be `26`-regular and equality must hold in
- `T <= 11e/3`, so every edge of `G` lies in exactly `11` triangles
- `\bar T <= 13e(\bar G)/3`, so every edge of `\bar G` lies in exactly `13` triangles

Translate the complement condition back to `G`.

For a nonedge `uv` of a `26`-regular graph on `53` vertices, among the other `51` vertices:
- `c_G(u,v)` are adjacent to both
- `26 - c_G(u,v)` are adjacent only to `u`
- `26 - c_G(u,v)` are adjacent only to `v`
- the remainder are adjacent to neither

So the number adjacent to neither is
`51 - [c_G(u,v) + (26 - c_G(u,v)) + (26 - c_G(u,v))] = c_G(u,v) - 1`.

Because every edge of `\bar G` lies in exactly `13` complement triangles, every nonedge of `G` has exactly `13` common nonneighbors, hence `c_G(u,v) = 14` for every nonedge.

Therefore any counterexample would satisfy:
- degree `k = 26`
- every edge has `lambda = 11` common neighbors
- every nonedge has `mu = 14` common neighbors

That is exactly a strongly regular parameter package `(53, 26, 11, 14)`.

Now let `A` be the adjacency matrix. Standard counting gives
`A^2 = (k - mu)I + (lambda - mu)A + mu J = 12I - 3A + 14J`.
On the `52`-dimensional subspace orthogonal to the all-ones vector, `J` vanishes, so `A` satisfies
`x^2 + 3x - 12 = 0`.

This polynomial has discriminant `57`, so it is irreducible over `\mathbf{Q}`. Hence its two roots must occur with equal multiplicity in the rational characteristic polynomial of `A`. Since the orthogonal subspace has dimension `52`, each root would have multiplicity `26`.

But the sum of those two roots is `-3`, so the trace contributed by that subspace would be `26(-3) = -78`. The all-ones eigenvalue contributes `26`, so the total trace would be `-52`, contradicting `trace(A) = 0`.

Conclusion of Approach B: the equality-case counterexample cannot exist.

Self-check after Approach B: the contradiction uses only exact linear algebra on an integer matrix; the only delicate step is the equal-multiplicity claim for the two irrational conjugate roots, which is standard because the characteristic polynomial has rational coefficients.

## lemma_graph
Proof skeleton.

Lemma 1. If `G` avoids `B12`, then `T <= 11e/3`.

Lemma 2. If `\bar G` avoids `B14`, then `\bar T <= 13(\binom{53}{2} - e)/3`.

Lemma 3. Goodman plus Lemmas 1 and 2 imply
`3S_2 - 154S_1 + 104728 <= 0`.

Lemma 4. Recenter degrees by `d_i = 26 + x_i`. Then Lemma 3 becomes
`3\sum_i x_i^2 + 2\sum_i x_i <= 0`, forcing `x_i = 0` for all `i`.

Lemma 5. Equality in Lemmas 1 and 2 implies every edge has exactly `11` common neighbors and every nonedge has exactly `14` common neighbors.

Lemma 6. No graph with parameters `(53, 26, 11, 14)` exists, by the adjacency-matrix trace contradiction above.

Theorem. No `53`-vertex counterexample exists, so every `53`-vertex graph forces `B12` or complement `B14`. Together with the known lower bound `53 <= R(B12, B14)`, this gives `R(B12, B14) = 53`.

Self-check after Lemma Graph: the chain is theorem-shaped already; there is no missing computational residue if Lemma 6 is accepted.

## chosen_plan
Choose Approach A as the main line, with Approach B as the equality-case contradiction.

Reason:
- it stays reasoning-first and avoids search
- it produces a clean title theorem rather than an isolated witness
- it naturally packages as a short paper: local book bounds -> Goodman rigidity -> forbidden strongly-regular parameters

What extra structure makes the result paper-shaped if the main claim closes:
- one explicit rigidity lemma stating that any `53`-vertex counterexample must be `26`-regular
- one short equality-case proposition translating the triangle equalities into `(53,26,11,14)`
- one boundary remark comparing the solved target to the neighboring exact case `R(B13, B14) = 55`

## self_checks
- Statement lock check: the solve is aimed at the exact title theorem `R(B12, B14) = 53`, not a weaker witness statement.
- Definition check: the page counts were translated correctly into common-neighbor thresholds `11` and `13`.
- Invariant check: Goodman is being used only as an exact identity, not as a heuristic bound.
- Equality-case check: the move from global equality to per-edge exact triangle counts is valid because each local count has a uniform upper bound.
- Spectral check: the contradiction is trace-based and does not require Lean or floating-point computation.

## code_used
No code used in this attempt.

Reason for not using code: the structural proof candidate closes the target without bounded search. Minimal code would only duplicate exact arithmetic already handled transparently in the manuscript-style derivation.

## result
Best current solve result: strong exact proof candidate for `R(B12, B14) = 53`.

Proposed proof.

Assume for contradiction that `G` is a `53`-vertex graph with no `B12` and whose complement has no `B14`.

For `G`, each edge lies in at most `11` triangles, so `T <= 11e/3`.
For `\bar G`, each edge lies in at most `13` triangles, so
`\bar T <= 13(\binom{53}{2} - e)/3`.
Goodman's identity gives
`T + \bar T = \binom{53}{3} - (1/2)\sum_i d_i(52 - d_i)`.

Combining these yields
`3S_2 - 154S_1 + 104728 <= 0`.
Write `d_i = 26 + x_i`. Then the left side is exactly
`3\sum_i x_i^2 + 2\sum_i x_i`.
If `\sum_i x_i > 0`, this is positive. If `\sum_i x_i < 0`, then
`3\sum_i x_i^2 >= 3|\sum_i x_i| > 2|\sum_i x_i|`,
again making the expression positive. Therefore `\sum_i x_i = 0`, and then `\sum_i x_i^2 = 0`. So every degree is `26`.

Hence equality holds in the triangle bounds. Therefore every edge of `G` has exactly `11` common neighbors, and every edge of `\bar G` has exactly `13` common neighbors. In a `26`-regular graph on `53` vertices, that means every nonedge of `G` has exactly `14` common neighbors in `G`. So `G` would have strongly regular parameters `(53,26,11,14)`.

Let `A` be its adjacency matrix. On the orthogonal complement of the all-ones vector,
`A` would satisfy `x^2 + 3x - 12 = 0`.
The two roots are irrational conjugates, so over a rational characteristic polynomial they must occur with equal multiplicity. Since the orthogonal complement has dimension `52`, each would occur `26` times. Their total trace contribution would then be `26(r+s) = 26(-3) = -78`, while the principal eigenvalue contributes `26`, giving total trace `-52`, impossible because adjacency matrices have trace `0`.

Therefore the assumed `53`-vertex counterexample does not exist. Since the lower bound `53 <= R(B12, B14)` is already known from the packet, the exact value is
`R(B12, B14) = 53`.

Smallest supporting theorem slice extracted from the proof:
any `53`-vertex graph with no `B12` and no complement `B14` would have to be a nonexistent strongly regular graph with parameters `(53,26,11,14)`.

Natural corollary / immediate remark:
the one-gap window collapses on the upper side; the lower-bound construction at `52` is therefore optimal for this pair.

What scales:
- the Goodman-rigidity step should transfer to other one-gap book cases where the midpoint degree is forced and the equality case predicts a nonexistent strongly regular parameter set.

What does not obviously scale:
- the final contradiction uses the very specific parameter package `(53,26,11,14)` and may fail when the forced equality polynomial has rational roots or a realizable parameter set.

Self-check after Result: the proof is paper-facing and theorem-shaped. The main remaining risk is line-by-line verification of the Goodman algebra and the nonedge-to-`mu=14` translation.

## family_affinity
Strong family affinity.

This is not an isolated curiosity; it sits exactly on the named almost-diagonal book-Ramsey line `B_{n-2}` versus `B_n`. The argument also explains why the target is structurally close to the solved neighbor `R(B13, B14) = 55` while still requiring a separate endpoint argument.

If verified, a successful solve would already be roughly `80-90%` of a micro-paper: the exact title theorem is present, the proof is short, and only light contextual packaging remains.

## generalization_signal
Moderate positive signal.

The reusable pattern is:
- local book constraints bound `T` and `\bar T`
- Goodman collapses the degree sequence to a midpoint-regularity equality case
- the equality case is tested against a strongly-regular obstruction

This suggests checking nearby unresolved pairs where the forced regular degree and `(v,k,lambda,mu)` package are similarly rigid.

## proof_template_reuse
Reusable proof template:

1. convert book avoidance into per-edge triangle caps in `G` and `\bar G`
2. combine those caps with Goodman
3. recenter degrees at the midpoint and exploit integrality
4. identify the forced equality case
5. rule it out spectrally

This template looks strongest for one-gap or near-one-gap book cases with `n` odd and midpoint degree near `(n-1)/2`.

## candidate_theorem_slice
Candidate theorem slice:

If `G` is a graph on `53` vertices with no edge contained in `12` triangles and no nonedge whose endpoints have `14` common nonneighbors, then `G` must be `26`-regular; in fact it would force a nonexistent strongly regular parameter set `(53,26,11,14)`.

That slice is theorem-shaped even before the final Ramsey-language repackaging.

## smallest_param_shift_to_test
Most informative next parameter shifts:
- `R(B11, B13)`, to see whether the same midpoint-rigidity mechanism survives one step down the line
- `R(B13, B15)`, to test whether the same Goodman-plus-SRG obstruction appears one step up

These are better than broad generalization because they keep the proof template local and falsifiable.

## why_this_is_or_is_not_publishable
If the argument checks, this is publishable in the micro-paper lane.

Why:
- the exact title theorem is clean and honest
- the result closes a named one-gap frontier case
- the proof is short and structural, not an opaque search certificate
- the remaining packaging is light: introduce notation, cite the known lower/upper window, present the rigidity proof, and add a short comparison with `R(B13, B14) = 55`

Minimal remaining packaging work if the proof is correct:
- polish the Goodman derivation into lemma form
- state the equality-case SRG contradiction as a standalone proposition
- add a brief literature-positioning paragraph and one boundary remark

If the proof breaks at verification, the current package would drop back to `PARTIAL`; there is no fallback witness in hand.

## paper_shape_support
Paper-shape support presently available:
- title theorem: `The Exact Value of R(B12, B14)`
- one supporting rigidity lemma: counterexamples are forced to be `26`-regular
- one obstruction proposition: the equality case would imply a nonexistent `(53,26,11,14)` strongly regular graph
- one immediate boundary remark: the target is not subsumed by `R(B13, B14) = 55`, but it now aligns cleanly beside it

This is enough structure that, if verified, the solve is already close to the full note.

## boundary_remark
Boundary remark.

The proof is genuinely endpoint-specific. It does not claim a full theorem for all `R(B_{n-2}, B_n)`. What it shows is that for the exact residue `53 <= R(B12, B14) <= 54`, the upper endpoint is incompatible with the only possible equality-case structure.

That keeps the claim honest: closer to a paper-shaped exact case than to a broad family theorem.

## likely_failure_points
- Arithmetic check in the Goodman rearrangement leading to `3S_2 - 154S_1 + 104728 <= 0`.
- Equality propagation: confirming that degree rigidity indeed forces equality in both triangle-count bounds.
- Nonedge translation in the regular case: verifying carefully that `13` common nonneighbors in `\bar G` corresponds to `14` common neighbors in `G`.
- Spectral contradiction presentation: the equal-multiplicity claim for irrational conjugate roots should be written in a way a referee will accept immediately.

## what_verify_should_check
- Recompute the Goodman algebra from scratch.
- Confirm that the solve-stage lower bound used here is exactly `53 <= R(B12, B14)`.
- Check each equality implication separately:
  `T = 11e/3`, `\bar T = 13e(\bar G)/3`, and the resulting exact local counts.
- Validate the `(53,26,11,14)` obstruction independently, ideally both by the trace argument and by the standard strongly-regular multiplicity formulas.
- Audit whether the proof remains purely internal and does not rely on any unstated theorem beyond Goodman and elementary spectral facts.

## verify_rediscovery
Bounded prior-art audit completed with limited web only.

Search focus used:
- exact instance notation for `R(B12, B14)`
- alternate notation for the almost-diagonal `B_{n-2}` versus `B_n` line
- the canonical sources named in the packet
- theorem/example/corollary checks aimed at the same source family
- one recent-status sweep for a later exact determination

Verdict from PASS 1:
- no exact determination of `R(B12, B14)` was found in the bounded audit
- the public record still appears to support only the window `53 <= R(B12, B14) <= 54`
- no theorem, proposition, example, or explicit witness was found that already settles the exact pair

Conservative note:
- this is only a bounded rediscovery audit, not an exhaustive literature search
- within that budget, rediscovery was not established

## verify_faithfulness
The solve-stage claim is faithful to the intended statement.

Checks:
- the attempted theorem is exactly the `53` branch of the locked dichotomy: prove every `53`-vertex graph contains `B12` or its complement contains `B14`
- the proof does not drift to a weaker proxy such as an asymptotic estimate or a nearby parameter pair
- the final exact-value sentence `R(B12, B14) = 53` still depends on the imported literature lower bound `53 <= R(B12, B14)`; the local proof only supplies the upper bound side

No quantifier drift or definition drift found.

## verify_proof
No incorrect step found in the current proof candidate.

Independent checks performed:
- recomputed the Goodman combination and confirmed the inequality
  `3S_2 - 154S_1 + 104728 <= 0`
- recomputed the recentering at `26` and confirmed that the left side becomes
  `3 \\sum_i x_i^2 + 2 \\sum_i x_i`
- checked the integrality argument forcing `\\sum_i x_i = 0` and then `x_i = 0` for all `i`
- checked the regular-case translation for a nonedge `uv`:
  the number of common nonneighbors is `c_G(u,v) - 1`, so `13` complement triangles force `c_G(u,v) = 14`
- checked the strongly regular package `(53,26,11,14)` and the restricted polynomial
  `x^2 + 3x - 12`
- checked the spectral obstruction: the irrational conjugate restricted eigenvalues must occur with equal multiplicity over a rational characteristic polynomial, so multiplicities would be `26` and `26`, yielding total trace `26 + 26(-3) = -52`, impossible

First incorrect step found: none.

## verify_adversarial
Adversarial pass completed.

Findings:
- no local checker or search artifact exists for this slug beyond the canonical `record.md` / `status.json` / working packet
- a minimal exact-arithmetic sanity check reproduced the core constants:
  `\\binom{53}{2} = 1378`, `\\binom{53}{3} = 23426`, and the recentered constant term vanishes at degree `26`
- the spectral obstruction was rechecked independently at the level of trace arithmetic
- there is no explicit witness construction to attack, so the adversarial burden here is purely on the derivation chain; that chain survived the bounded check

No computational contradiction found.

## verify_theorem_worthiness
Assessment:
- exactness: yes, conditional on the imported lower bound and pending formal sealing
- novelty: bounded audit suggests frontier-novel, with no rediscovery found in-budget
- reproducibility: high at manuscript level; the argument is short and exact, with no hidden computation
- Lean readiness: the mathematics is formalizable, but Lean is not yet the shortest remaining path to a sealed publication packet
- paper leverage: strong enough for the micro-paper lane if the bounded novelty picture holds

Direct answers:
- would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  yes
- what percentage of the paper would one solve already provide?
  about `0.8`
- what title theorem is actually visible?
  `The Exact Value of R(B12, B14)`
- what part of the argument scales?
  the Goodman-to-midpoint-rigidity step and the equality-case reduction to a strongly regular obstruction
- what part clearly does not?
  the final spectral contradiction is tightly tied to the specific forced parameter set `(53,26,11,14)`
- is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`?
  no; the best honest current status is `SLICE_CANDIDATE`

Conservative publication judgment:
- this is stronger than `INSTANCE_ONLY` because the exact theorem is title-level and sits on a named frontier slice
- it is not yet `PAPER_READY` at verify stage because the rediscovery audit was bounded and the publication packet still needs serial publication-stage review

## verify_verdict
`VERIFIED`

Current verify-stage conclusion:
- bounded PASS 1 did not establish rediscovery
- the solve-stage theorem matches the intended statement
- no proof error was found in the Goodman-rigidity to strongly-regular-obstruction chain
- the run must remain `CANDIDATE`, not `EXACT`, because Lean has not completed

## minimal_repair_if_any
Tiny conservative repair recommended for later writeup, but not required to preserve correctness:

- state explicitly that once the recentered inequality gives equality, the combined bound
  `T + \\bar T <= 11e/3 + 13e(\\bar G)/3`
  is tight, so both triangle-count bounds are individually tight; this makes the passage to exact `\\lambda = 11` and exact complement-triangle count `13` referee-proof in one sentence
- keep the literature lower bound visibly separated from the internal proof of the `53` upper bound so the exact-value conclusion remains fully faithful

## publication_prior_art_audit
Bounded publication-stage literature pass completed with limited web only.

Exact-statement search:
- direct searches on `R(B12, B14)` and nearby phrase variants did not surface a dedicated exact-value paper keyed by that exact pair-string

Alternate-notation search:
- the almost-diagonal search on the `B_{n-2}` versus `B_n` line led back to Lidicky-McKinley-Pfender-Van Overberghe 2025, whose Theorem 1 gives `4n - 3 <= R(B_{n-2}, B_n)` for `4 <= n <= 21`
- specializing to `n = 14` yields the lower bound `53 <= R(B12, B14)`

Canonical-source check:
- the 2025 canonical paper is faithful as a lower-bound source, but it does not by itself present a separate exact theorem for `R(B12, B14)`
- the latest accessible Radziszowski survey page is revision `#18`, dated `April 24, 2026`, and item `5.3(j)` explicitly records `R(B12, B14) = 53` while citing `[We2]`
- the same survey reference list identifies `[We2]` as William J. Wesley, `Lower Bounds for Book Ramsey Numbers`, `Discrete Mathematics 349(5)` (2026), article `114913`

Theorem / proposition / observation check inside the canonical source family:
- the 2025 theorem gives the lower-bound half only
- the survey's `5.3(j)` line is the first bounded-source location in this audit that explicitly collapses the target to the exact value

Outside-status check:
- the official ScienceDirect article page confirms Wesley's 2026 paper exists as a published open-access article in `Discrete Mathematics 349(5)`

Date caution:
- the survey revision `#18` is dated `April 24, 2026`, which is later than both the packet's `open_status_checked_on = 2026-04-15` and this run's nominal date `2026-04-15`
- nevertheless, it is the latest accessible public status source in the bounded audit, so it defeats frontier safety for this candidate

Publication-stage verdict from the bounded audit:
- under the latest accessible public record, the exact target is already solved / implied in prior art and should be treated as `REDISCOVERY` for the micro-paper lane

## publication_statement_faithfulness
The local proof packet is faithful to the mathematical upper-bound task, but the frontier framing is now stale.

Checks:
- the solve record really does target the upper-bound side `R(B12, B14) <= 53`
- combined with the literature lower bound, that would yield the exact value `R(B12, B14) = 53`
- however, the latest accessible survey now already logs that exact value

Therefore the strongest faithful framing is no longer "new exact determination of `R(B12, B14)`" but rather:
- at most an independent structural proof of the already-known upper-bound side, hence an alternate derivation of a known exact value

## publication_theorem_worthiness
Direct answers:
- is the strongest honest claim stronger than "here is an example"?
  yes
- is there a real title theorem, theorem slice, or counterexample theorem here?
  yes, mathematically the proof candidate gives a genuine structural theorem slice
- is the proof structural or merely instance-specific?
  structural
- would this survive a referee asking "what is the theorem?"
  on mathematical content, yes; on publication posture, no referee would ignore the rediscovery problem
- is the claim still too dependent on hand-picked small cases?
  not in proof form, but yes in target selection because it is a single exact pair

Judgment:
- theorem-worthiness is real at the mathematical level
- publication-worthiness under the active frontier objective is not, because the title claim is no longer novel in the latest accessible public record

## publication_publishability
Direct answers:
- would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note?
  no under the active one-shot frontier objective
- what percentage of the paper would one solve already provide?
  about `0.15` once the rediscovery hit is accounted for
- if this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit?
  it only looked attractive before audit; the blocking gap is novelty, not polishing
- if this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program?
  yes
- would Lean directly seal the packet, or would it only be optional polish / later archival formalization?
  only optional archival formalization; Lean would not repair rediscovery

Conservative verdict:
- this is not `PAPER_READY`
- under the current lane it should not be expanded into a broader book-Ramsey campaign or alternate-proof project without explicit approval

## publication_packet_audit
Packet assessment:
- proof artifacts are preserved and still valuable as an independent derivation candidate
- the title claim is no longer frontier-safe
- the packet is therefore stale as a live micro-paper target

Best honest packet reading now:
- publication status: `REDISCOVERY`
- packet quality: stale due to rediscovery, not due to missing proof artifacts
- residual value: preserve as an alternate-proof packet in case such work is later requested explicitly

## micro_paper_audit
Direct answers for the micro-paper lane:
- is the strongest honest claim stronger than "here is an example"?
  yes
- would this result already constitute most of a publishable note?
  no, not after the rediscovery audit
- what percentage of the paper would one solve already provide?
  about `0.15`
- is there a real title theorem here?
  mathematically yes, frontier-wise no
- is the proof structural?
  yes
- would this survive a referee asking "what is the theorem?"
  only as an alternate proof of a known result
- is the claim too dependent on hand-picked small cases?
  no on proof shape, yes on target scope
- if not paper-ready, should it be moved aside rather than expanded?
  yes

Assessment:
- fail the active micro-paper lane
- the packet no longer optimizes solve-to-publication distance because the novelty surface collapsed during publication audit

## strongest_honest_claim
If correct, the local Goodman-plus-strongly-regular obstruction argument gives an independent structural proof that `R(B12, B14) <= 53`. Combined with published lower-bound literature, that rederives the now-public exact value `R(B12, B14) = 53`. Under the current frontier-novel micro-paper objective, this makes the packet a rediscovery / alternate-proof packet rather than a new one-shot paper.

## paper_title_hint
No frontier-safe title remains under the active objective. At most: `A Structural Proof of the Known Value R(B12, B14)=53`.

## next_action
Mark the slug as `REDISCOVERY`, preserve the proof artifacts, and move it aside/off the live micro-paper queue. Do not broaden into a larger book-Ramsey program or an alternate-proof lane without explicit approval.
