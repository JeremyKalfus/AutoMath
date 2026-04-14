## statement_lock

Active slug: `r-b10-b12-book-ramsey`.

Active title: `Determine the exact value of R(B10, B12)`.

Locked intended title theorem:

> Every graph on 45 vertices contains a copy of `B10` or its complement contains a copy of `B12`. Consequently `R(B10, B12) = 45`.

This is the right title theorem for the micro-paper lane: if correct, it is already the main theorem of a short exact-value note.

## definitions

- `B_t` denotes the book graph with `t` pages: `t` triangles sharing one common edge.
- In a graph `G`, an edge `uv` is the spine of a `B_t` exactly when `uv` has at least `t` common neighbors in `G`.
- Thus `G` is `B10`-free iff every edge of `G` has at most `9` common neighbors.
- `\bar G` is `B12`-free iff every nonedge `uv` of `G` has at most `11` common nonneighbors in `G`.
- Let `n = 45`, `m = e(G)`, `T =` number of triangles in `G`, and `A =` number of independent triples in `G`.

Ambiguities / conventions to keep fixed:

- I am using the standard convention `B_t = K_2 + \overline{K_t}`.
- All common-neighbor counts exclude the endpoints of the pair.
- `A` counts independent 3-sets in `G`, equivalently triangles in `\bar G`.

## approach_A

Structural / invariant route: force any hypothetical counterexample into a numerically rigid regime, then show that regime is impossible.

Assume for contradiction that there is a graph `G` on 45 vertices with no `B10`, and whose complement also has no `B12`.

1. Local book bounds:
   - Every edge lies in at most `9` triangles.
   - Every nonedge lies in at most `11` independent triples.

2. Triangle and anti-triangle count upper bounds:
   - `3T = sum_{uv in E(G)} codeg_G(uv) <= 9m`, so `T <= 3m`.
   - `3A = sum_{uv notin E(G)} codeg_{\bar G}(uv) <= 11(990 - m)`, so `A <= 11(990 - m)/3`.
   - Therefore
     `T + A <= 3m + 11(990 - m)/3 = 3630 - 2m/3`.

3. Degree-sum bounds on pairs:
   - If `uv` is an edge, then
     `|(N(u) \ {v}) cap (N(v) \ {u})| <= 9`,
     while `|(N(u) \ {v}) cup (N(v) \ {u})| <= 43`, hence
     `(d(u) - 1) + (d(v) - 1) <= 43 + 9`, so `d(u) + d(v) <= 54`.
   - If `uv` is a nonedge, then the number of common nonneighbors is at most `11`, and the union of nonneighbor sets has size at most `43`, so
     `(43 - d(u)) + (43 - d(v)) <= 43 + 11`, hence `d(u) + d(v) >= 32`.

4. Summing the pair bounds:
   - Over edges,
     `sum_v d(v)^2 = sum_{uv in E(G)} (d(u) + d(v)) <= 54m`.
   - Over nonedges,
     `sum_{uv notin E(G)} (d(u) + d(v)) = sum_v d(v)(44 - d(v)) >= 32(990 - m)`.
   - Since `sum_v d(v)(44 - d(v)) = 88m - sum_v d(v)^2`, the previous display and `sum_v d(v)^2 <= 54m` give
     `88m - 54m >= 32(990 - m)`,
     so `66m >= 31680`, hence `m >= 480`.

5. Baseline Goodman squeeze:
   - Goodman implies
     `T + A = 14190 - (1/2) sum_v d(v)(44 - d(v)) >= 3300`,
     because `sum_v d(v)(44 - d(v)) <= 45 * 22^2 = 21780`.
   - Combining this with `T + A <= 3630 - 2m/3` yields `m <= 495`.

6. Refined Goodman lower bound:
   - Write `m = 495 - t` with `0 <= t <= 15`.
   - Then `sum_v d(v) = 990 - 2t`.
   - For fixed sum `990 - 2t`, convexity of `x^2` shows that `sum_v d(v)^2` is minimized when exactly `2t` vertices have degree `21` and the other `45 - 2t` have degree `22`.
   - Hence
     `sum_v d(v)^2 >= 2t * 21^2 + (45 - 2t) * 22^2 = 21780 - 86t`.
   - Goodman gives
     `T + A = binom(45,3) - (1/2) sum_v d(v)(44 - d(v))`
     `= 14190 - (1/2)(88m - sum_v d(v)^2)`.
   - Therefore
     `T + A >= 14190 - (1/2)(88(495 - t) - (21780 - 86t)) = 3300 + t`.

7. Compare bounds:
   - Upper bound: `T + A <= 3630 - 2(495 - t)/3 = 3300 + 2t/3`.
   - Lower bound: `T + A >= 3300 + t`.
   - For `t > 0`, these are incompatible.
   - Thus `t = 0`, so `m = 495`.

8. Equality consequences:
   - We now have equality in the upper and lower bounds, so all intervening inequalities must be tight.
   - Equality in the convexity/Goodman step forces every degree to equal `22`; thus `G` is `22`-regular.
   - Equality in the triangle count gives every edge exactly `9` common neighbors.
   - Equality in the anti-triangle count gives every nonedge exactly `11` common nonneighbors.

9. Translate the nonedge condition into common-neighbor data:
   - For a nonedge `uv` in a `22`-regular graph on `45` vertices, if `mu(uv)` is the number of common neighbors, then
     `11 = 43 - 22 - 22 + mu(uv) = mu(uv) - 1`,
     so `mu(uv) = 12`.
   - Hence any counterexample would be a strongly regular graph with parameters `(45,22,9,12)`.

10. Spectral contradiction:
   - For a strongly regular graph with parameters `(45,22,9,12)`, the nontrivial eigenvalues satisfy
     `x^2 + (12 - 9)x + (12 - 22) = 0`,
     i.e. `x^2 + 3x - 10 = 0`,
     so the nontrivial eigenvalues are `2` and `-5`.
   - Let their multiplicities be `f` and `g`.
   - Then `f + g = 44`, and trace zero gives
     `22 + 2f - 5g = 0`.
   - Solving yields `7f = 198`, impossible.

Therefore no such counterexample graph exists, so `R(B10, B12) = 45`.

Self-check after Approach A:

- The only family input used is the one-gap window `45 <= R(B10, B12) <= 46`; the solve itself is purely local counting.
- The proof does not rely on web or search.
- The contradiction is exact and theorem-shaped, not just an instance witness.

## approach_B

Construction / extremal / contradiction route: start from the lower-bound side and ask what a 45-vertex witness would have to look like.

- A 45-vertex witness for `R(B10, B12) = 46` would have to avoid `B10`, while its complement avoids `B12`.
- The counting argument above shows such a witness cannot be loose or irregular:
  - it must have exactly `495` edges,
  - it must be `22`-regular,
  - every edge must have exactly `9` common neighbors,
  - every nonedge must have exactly `11` common nonneighbors.
- So any successful 45-vertex extension of the known 44-vertex lower-bound paradigm would automatically collapse into the unique parameter set `(45,22,9,12)`.
- That parameter set is spectrally impossible, so the constructive route fails before one even needs to identify a concrete 44-vertex seed.

Self-check after Approach B:

- This is genuinely a construction-side obstruction, not just a repackaging of the final proof.
- It explains why the recommended “extend the 44-vertex lower bound to 45” attack likely fails completely, not merely computationally.

## lemma_graph

1. Assume a 45-vertex counterexample `G`.
2. Edge condition: every edge has at most `9` common neighbors.
3. Nonedge condition: every nonedge has at most `11` common nonneighbors.
4. Count triangles / independent triples to get `T + A <= 3630 - 2m/3`.
5. Use the corrected pairwise degree-sum bounds to get `m >= 480`.
6. For `m = 495 - t` with `0 <= t <= 15`, convexity plus Goodman yields `T + A >= 3300 + t`.
7. Compare with the upper bound to force `t = 0`, hence `m = 495`.
8. Equality forces `22`-regularity, `lambda = 9`, and common nonneighbor count `11` on nonedges.
9. Therefore `mu = 12`, so `G` would be `srg(45,22,9,12)`.
10. Spectral multiplicities are nonintegral, contradiction.
11. Conclude `R(B10, B12) = 45`.

## chosen_plan

Choose Approach A as the main proof because it already gives a clean title theorem:

- local book constraints
- global triangle / anti-triangle squeeze
- exact edge count
- forced strong-regularity
- spectral nonexistence

Approach B is retained as the publication-facing motivation: it says the natural 45-vertex witness program is obstructed structurally, not merely by a failed search.

## self_checks

- Definition check: `B_t` is being used in the standard shared-spine sense.
- Counting check: `3T` and `3A` are correct because each triangle / independent triple contributes to exactly three pair counts.
- Algebra check: after correcting the endpoint bookkeeping in the pair-degree inequalities, the argument still gives `m >= 480` without hidden assumptions.
- Convexity check: once `480 <= m <= 495`, the minimum-square degree sequence uses only `21` and `22`.
- Equality check: the conclusion that all degrees are `22` uses the exact lower-bound equality case of Goodman.
- Spectral check: the trace equations give a direct integrality contradiction, so no catalog lookup is needed.

## code_used

No code used. The reasoning closes without a search, checker, or witness verification script.

## result

Best current solve-stage result:

> Candidate proof that `R(B10, B12) = 45`.

Exact title theorem if this survives verification:

> The Exact Value of `R(B10, B12)` is `45`.

What extra structure makes it paper-shaped:

- the proof is already a short standalone theorem argument;
- the construction side is addressed by showing any 45-vertex witness would have to be an impossible strongly regular graph;
- one immediate remark is that the known 44-vertex lower-bound paradigm cannot extend to 45.

Whether a successful solve would already be 70-90% of a paper:

- Yes. This is squarely in that band; I would still assess the solve-to-paper fraction at about `0.86`.

Minimal remaining packaging work if the argument checks out:

- verify the local formulas carefully against the literature convention for `B_t`;
- write a short introduction situating the one-gap window `45 <= R(B10, B12) <= 46`;
- add a brief comparison with the adjacent solved case `R(B11, B12) = 47`;
- optionally formalize the counting/spectral contradiction in Lean.

Immediate corollary / boundary remark:

- There is no 45-vertex graph whose every edge lies in at most `9` triangles and whose every nonedge lies in at most `11` independent triples.

Paper-lane assessment of the current result:

- If verified, this is already closer to a paper-shaped claim than to an instance-only claim.
- It is not too thin for the micro-paper lane.

What part of the argument scales:

- The squeeze “local book bounds -> Goodman -> forced regularity -> spectral obstruction” can transfer to other one-gap almost-diagonal book pairs.

What part does not scale automatically:

- The exact collapse to a single strongly regular parameter set depends on the specific numbers `45`, `9`, and `11`; farther from the one-gap regime the degree squeeze may be too weak.

What theorem slice is suggested:

- Any graph on 45 vertices with edge codegree at most `9` and nonedge cocodegree at most `11` must be strongly regular with impossible parameters `(45,22,9,12)`.

What parameter shifts would help most next:

- test the nearest neighboring almost-diagonal book pairs where the public bounds also differ by one;
- the most natural first shifts are `(B9, B11)` and `(B11, B13)`, because the same saturation template might either transfer or fail for a clean reason.

Current package assessment:

- This is already theorem-shaped, not merely an isolated witness.

## family_affinity

Strong. The proof sits naturally on the almost-diagonal `B_{n-2}` versus `B_n` book Ramsey line, and it uses only the local shared-spine interpretation of books plus a one-gap exact-order squeeze.

## generalization_signal

Moderate-to-strong. The template looks reusable whenever a book-Ramsey pair has:

- a one-gap order window,
- local upper bounds on edge codegrees and complement edge codegrees,
- enough rigidity to force near-regularity,
- a terminal strongly-regular obstruction or a similarly rigid extremal object.

The signal is real, but not automatic across the whole family.

## proof_template_reuse

Reusable proof template:

1. convert `B_a` / `B_b` avoidance into edge and nonedge common-neighbor bounds;
2. count triangles and independent triples;
3. combine with Goodman and convexity to force the exact edge count and regularity;
4. convert the equality case into a tiny candidate parameter set;
5. kill that parameter set spectrally or by another rigid obstruction.

## candidate_theorem_slice

Candidate slice:

> There is no graph `G` on 45 vertices such that every edge of `G` has at most `9` common neighbors and every nonedge of `G` has at most `11` common nonneighbors.

Equivalent sharpened slice:

## publication_prior_art_audit
Audit date: `2026-04-14`.

Bounded passes performed:

- exact-statement web search for quoted forms of `R(B10,B12)`, `R(B10, B12)`, and
  `R(B_{10}, B_{12})`;
- alternate-notation search for forms such as
  `R(K_2 + \overline{K_{10}}, K_2 + \overline{K_{12}})`;
- canonical-source refresh on the current Electronic Journal of Combinatorics survey page and PDF
  for Radziszowski's dynamic survey;
- theorem / proposition / example / corollary / observation / sufficient-condition check inside
  the 2025 Lidicky-McKinley-Pfender-Van Overberghe paper;
- one outside-status check on Wesley's ScienceDirect article page for `Lower bounds for book
  Ramsey numbers`, together with a bounded direct title search.

What the bounded audit found:

- the exact-statement and alternate-notation searches did not surface a separate primary-source
  theorem, proposition, corollary, observation, example, or preprint explicitly settling
  `R(B10, B12)`;
- the current EJC survey page cites Radziszowski's `Small Ramsey Numbers` as
  `DS1: Sep 6, 2024`, and its Section `5.3` still leaves this pair in the one-gap window:
  item `(g)` gives the Rousseau-Sheehan upper-bound mechanism
  `R(B_m, B_n) <= 2(m+n+1)`, which yields `R(B10, B12) <= 46`;
- the same survey page and Table `IXa` record nearby exact progress, including
  `R(B11, B12) = 47`, `R(B12, B13) = 51`, `R(B12, B14) = 53`, and `R(B15, B17) = 65`,
  but it does not list an exact value for `(10,12)`;
- the 2025 Lidicky-McKinley-Pfender-Van Overberghe paper gives the lower-bound family
  `4n - 3 <= R(B_{n-2}, B_n)` in Theorem `1`, so for `n = 12` it supplies the lower bound `45`;
  its theorem statement and bounded source check did not reveal an exact closure of `R(B10, B12)`;
- Wesley's article page places `Lower bounds for book Ramsey numbers` in `Discrete Mathematics`
  `349(5)` dated `May 2026`, with DOI `10.1016/j.disc.2025.114913`; the bounded outside-status
  pass did not reveal any metadata or follow-up page settling `(10,12)`, and the page reported
  `Cited by (0)` on `2026-04-14`;
- no extra citation or discussion pass was needed after these checks, because the bounded audit did
  not uncover a concrete ambiguity about the exact status of `(10,12)`.

Conservative prior-art verdict:

- no rediscovery was found within the bounded publication-audit budget;
- the bounded audit still supports the public window `45 <= R(B10, B12) <= 46`;
- the target still looks frontier-novel within budget and should not be demoted to `REDISCOVERY`.

## publication_statement_faithfulness
The solve and verify packet stayed on the exact selected statement.

Checks:

- the selected theorem asks for the exact value of `R(B10, B12)`;
- the proof candidate assumes a `45`-vertex witness and derives a contradiction, yielding
  `R(B10, B12) = 45`;
- the extracted theorem slice, "any counterexample would have to be `srg(45,22,9,12)`", is a
  faithful internal reduction rather than a substitute target;
- the packet uses the standard shared-spine convention for `B_t`, consistent with the canonical
  source family notation;
- no proxy theorem, weakened claim, or notation drift was introduced during solve, verify, or this
  audit.

Faithfulness verdict:

- exact match to the intended statement;
- publication audit does not need to shrink the theorem claim.

## publication_theorem_worthiness
This is stronger than "here is an example."

Why:

- the strongest honest claim is an exact Ramsey-value candidate, not an isolated witness or
  one-direction bound;
- there is a real title theorem: `The Exact Value of R(B10, B12)`;
- the proof is structural in its main body:
  local codegree bounds -> triangle / anti-triangle squeeze -> exact edge count -> forced regularity
  -> impossible strongly regular parameters;
- only the terminal obstruction to `srg(45,22,9,12)` is pair-specific; the argument is not a pile
  of hand-picked tiny cases;
- a referee asking "what is the theorem?" would get an immediate and non-embarrassing answer:
  every `45`-vertex graph contains `B10` or its complement contains `B12`.

Risks that remain:

- the theorem is still a single exact pair, so the family spillover is limited;
- the endpoint obstruction is specialized to `(45,22,9,12)`, so the final move is exact-instance
  specific even though the reduction is structural.

Theorem-worthiness verdict:

- yes, this is a genuine title-theorem packet;
- it survives audit as a narrow but legitimate one-theorem slice.

## publication_publishability
If the claim is correct and Lean-sealed, it would already constitute most of a publishable short
note.

Answers to the publication questions:

- Is the strongest honest claim stronger than "here is an example"? Yes.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  Yes, about `85%`.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Yes: the exact-value
  theorem together with the `srg(45,22,9,12)` obstruction slice.
- Is the proof structural or merely instance-specific? Structural in the reduction, instance-specific
  only at the final forbidden-parameter discharge.
- Would this survive a referee asking "what is the theorem?" Yes.
- Is the claim still too dependent on hand-picked small cases? No. The scope is small, but the
  reasoning is not an ad hoc case bash or search residue.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only
  look attractive before audit? The remaining gap is genuinely small.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem
  program? Do not expand it. Keep the one-shot lane fixed and go straight to Lean.
- Would Lean directly seal the packet, or would it only be optional polish / later archival
  formalization? Lean is the direct sealing step, not optional polish.

Conservative publishability verdict:

- the candidate did not collapse under audit;
- it remains honestly close to a paper;
- it is not yet `PAPER_READY` because the exact theorem is not formally sealed.

## publication_packet_audit
Packet quality is `strong`.

What is already present:

- exact intended statement;
- coherent structural proof candidate;
- a preserved Lean-complete obstruction slice excluding `srg(45,22,9,12)`;
- bounded prior-art positioning refreshed through `DS1: Sep 6, 2024`, the 2025 book-Ramsey paper
  published on `2025-12-12`, and Wesley's `May 2026` article page.

What is still missing before a fully sealed packet:

- Lean formalization of the bridge from a `45`-vertex counterexample to `IsSRGWith 45 22 9 12`;
- exact wrapper from that obstruction slice to the final theorem `R(B10, B12) = 45`;
- short note-level prose packaging and one comparison paragraph against the adjacent solved cases.

Packet verdict:

- this is a real publication packet, not merely a solve log;
- the remaining work is sealing and concise write-up, not broader theorem discovery.

## micro_paper_audit
Micro-paper verdict: `PASS` with conservative status.

Assessment:

- strongest honest claim is a title theorem, not an example;
- family anchor remains strong because the target sits on the almost-diagonal `B_{n-2}` versus
  `B_n` corridor;
- editorial overhead remains low;
- isolated exact-case risk remains moderate, but the narrative still holds because the gap is
  canonically posed and adjacent exact benchmarks are already in the literature;
- the candidate still sits in the intended `70-90%` band, with honest estimate `0.85`;
- the audit did not reveal a hidden feeder ladder, large packaging tail, or search-heavy residue.

Bottom line:

- this target still belongs in the strict one-shot micro-paper lane;
- the honest status stays below `PAPER_READY` until Lean seals the exact theorem.

## strongest_honest_claim
The strongest honest claim after publication audit is:

- there is a bounded-novelty-clean candidate proof that every graph on `45` vertices contains
  `B10` or its complement contains `B12`, equivalently `R(B10, B12) = 45`;
- the strongest already preserved Lean-complete exact slice is the nonexistence of a strongly
  regular graph with parameters `(45,22,9,12)`;
- if Lean seals the counterexample-to-strongly-regular reduction and the final Ramsey wrapper, the
  result is already the title theorem of a short publishable note.

## paper_title_hint
`The Exact Value of R(B10, B12)`

## next_action
Move directly to Lean formalization of the bridge
`45`-vertex counterexample `-> IsSRGWith 45 22 9 12`, then wrap the existing SRG nonexistence
slice into the exact theorem `R(B10, B12) = 45`.

Do not broaden into a larger book-Ramsey campaign unless Lean exposes a real gap in this exact
packet.

## lean_statement

Formalized target for this Lean run:

> There is no strongly regular graph with parameters `(45,22,9,12)`.

This is the strongest honest target already preserved in the candidate-local Lean packet, and it is
the exact theorem slice needed by the verified `R(B10,B12)` argument: any 45-vertex counterexample
would have to collapse to `srg(45,22,9,12)`.

Lean file targets kept in scope:

- backend: `lean/AutoMath/RB10B12BookRamsey.lean`
- mirrored artifact copy: `artifacts/r-b10-b12-book-ramsey/lean/AutoMath/RB10B12BookRamsey.lean`

Main preserved Lean statements used for the slice:

- `AutoMath.RB10B12BookRamsey.intendedStatement`
- `AutoMath.RB10B12BookRamsey.no_srg_45_22_9_12`
- `AutoMath.RB10B12BookRamsey.srg_45_22_9_12_nonexistence`

## lean_skeleton

Lean skeleton actually realized in the preserved module:

1. encode the packet-facing target as nonexistence of `G.IsSRGWith 45 22 9 12`;
2. derive the quadratic SRG adjacency-matrix identity;
3. turn that into a cubic annihilator for the adjacency matrix;
4. show every adjacency eigenvalue must lie in `{22, 2, -5}`;
5. combine trace and trace-square identities with finite counting of eigenvalue slots;
6. finish by integer arithmetic contradiction.

This is the right theorem slice for the current packet because it captures the sharp spectral
obstruction without widening scope beyond the verified dossier.

## lean_result

Lean result on 2026-04-14:

- The preserved backend module `AutoMath.RB10B12BookRamsey` checked successfully with
  `cd lean && lake build AutoMath.RB10B12BookRamsey`.
- The candidate-local mirrored file stayed aligned with the backend file for this run.
- A direct `rg` check over the in-scope backend and mirrored module found no `sorry` or `admit`.
- Therefore the SRG obstruction slice is Lean-complete and preserved.

Conservative interpretation:

- this run does **not** yet justify `classification = EXACT`;
- it **does** justify upgrading the publication-facing Lean status to a checked theorem slice;
- the strongest Lean-complete claim is the impossibility of `srg(45,22,9,12)`, not yet the full
  exact theorem `R(B10,B12) = 45`.

## lean_blockers

Remaining blocker to a full exact Lean seal:

- The verified combinatorial bridge
  “45-vertex counterexample to `R(B10,B12)=45` implies `G.IsSRGWith 45 22 9 12`”
  is not yet formalized in Lean in the preserved module.

So the packet now has a Lean-complete obstruction slice, but the title theorem still needs the
counterexample-to-SRG reduction before it can honestly flip to `EXACT` or `PAPER_READY`.

## lean_statement

Lean target advanced on 2026-04-14:

> Formalize the exact equality-regime bridge
> “`|V| = 45`, `22`-regular, edge common-neighbor count `9`, nonedge common-neighbor count `12`
>  implies `IsSRGWith 45 22 9 12`,”
> then discharge it with the preserved SRG nonexistence theorem.

This is the strongest honest theorem slice reachable without redoing the full Goodman/convexity
bridge inside Lean. It sits strictly closer to the packet than the old bare SRG nonexistence
statement, but it still stops one step short of the full Ramsey wrapper.

New checked Lean statements added in scope:

- `AutoMath.RB10B12BookRamsey.equality_profile_isSRGWith`
- `AutoMath.RB10B12BookRamsey.no_equality_profile_counterexample`

## lean_skeleton

Lean skeleton realized in this pass:

1. keep the previously checked spectral obstruction
   `AutoMath.RB10B12BookRamsey.no_srg_45_22_9_12`;
2. package the exact equality profile directly into
   `G.IsSRGWith 45 22 9 12` via `equality_profile_isSRGWith`;
3. derive the contradiction immediately with
   `no_equality_profile_counterexample`.

What remains outside Lean is now narrower and explicit:

1. the Goodman / convexity squeeze from a general `45`-vertex counterexample to the equality
   profile;
2. the short local conversion from “nonedge common nonneighbors = `11`” to
   “nonedge common neighbors = `12`” in the forced `22`-regular regime.

## lean_result

Lean result on 2026-04-14 for this pass:

- `cd lean && lake build AutoMath.RB10B12BookRamsey` succeeded after the new theorem-slice edit.
- `rg -n "\\bsorry\\b|\\badmit\\b" lean/AutoMath/RB10B12BookRamsey.lean artifacts/r-b10-b12-book-ramsey/lean/AutoMath/RB10B12BookRamsey.lean` returned no matches.
- The backend file and the mirrored artifact file remained aligned in this run.

Conservative interpretation:

- the strongest Lean-complete claim is now stronger than the raw SRG obstruction alone;
- it is still a theorem slice, not the full exact theorem `R(B10, B12) = 45`;
- this supports `publication_status = SLICE_EXACT`, not `classification = EXACT`.

## lean_blockers

Remaining blockers after this pass:

- the general counterexample-to-equality-profile bridge is still prose-only;
- the packet-facing step converting complement common-neighbor count `11` on nonedges into
  common-neighbor count `12` in `G` is still prose-only;
- because those upstream reductions are not yet checked, the exact title theorem cannot honestly be
  marked Lean-complete.

## verify_rediscovery

Bounded prior-art audit on `2026-04-14` used the required exact-instance and alternate-notation
patterns:

- exact instance: `R(B10, B12)`;
- alternate notation / reordered family notation: `R(B_{10}, B_{12})`, `R(B12,B10)`, and
  book-Ramsey phrasing;
- canonical source checks against DS1.17 and the 2025 book-Ramsey paper;
- theorem / proposition / example / corollary checks inside those same source surfaces;
- one recent-status sweep keyed to 2026 activity and the Wesley 2026 line.

What the bounded audit supported:

- DS1.17 still exposes only the upper bound `R(B10, B12) <= 46` on the books line;
- Lidický-McKinley-Pfender-Van Overberghe 2025 supports the lower bound `R(B10, B12) >= 45`;
- Wesley 2026 settles the adjacent `R(B11, B12) = 47` benchmark, not the target pair.

Within the allotted budget I did not find a paper, theorem, example, observation, or discussion
explicitly closing `R(B10, B12)` exactly. Rediscovery was not established.

## verify_faithfulness

The prose solve is faithful to the intended statement. It assumes a `45`-vertex counterexample to
the exact claim `R(B10, B12) = 45` and derives a contradiction without drifting to a weaker proxy
theorem, a different book convention, or a reordered parameter pair.

The main faithfulness caveat is artifact scope, not theorem drift:

- `record.md` argues the full Ramsey theorem;
- the Lean artifact only seals the terminal obstruction slice
  `¬ IsSRGWith 45 22 9 12` plus the equality-profile packaging around it.

So the written proof remains aligned with the intended claim, but the formal artifact is still
narrower than the title theorem.

## verify_proof

I did not find a first incorrect step in the counting argument as written.

Checks completed:

- the `B10` / complement-`B12` assumptions translate correctly into edge codegree `<= 9` and
  nonedge common-nonneighbor count `<= 11`;
- the triangle and independent-triple sums `3T` and `3A` are counted correctly;
- the pairwise degree-sum inequalities yield `d(u) + d(v) <= 54` on edges and `>= 32` on
  nonedges;
- summing those inequalities gives the claimed lower bound `m >= 480`;
- Goodman plus the triangle / anti-triangle upper bound yields `m <= 495`;
- the convexity refinement with `m = 495 - t` forces `t = 0`, hence `m = 495`;
- equality then forces `22`-regularity, edge common-neighbor count `9`, and nonedge common
  nonneighbor count `11`;
- in a `22`-regular graph on `45` vertices, that nonedge condition converts to common-neighbor
  count `12`;
- the resulting SRG parameters `(45,22,9,12)` give nonintegral spectral multiplicities.

The proof therefore survives local skeptical checking as a prose theorem argument. The unresolved
issue is not a detected mathematical flaw, but the lack of full formal sealing of the upstream
counting reduction.

## verify_adversarial

No checker, search script, or witness-verification code exists for this candidate, so the
adversarial pass was limited to algebraic stress-testing and formal-artifact rerun attempts.

Adversarial outcomes:

- rechecked the tight-equality transition from the Goodman squeeze to `22`-regularity and did not
  find a hidden case split;
- rechecked the nonedge conversion `11` common nonneighbors `-> 12` common neighbors in the
  `22`-regular `45`-vertex regime and did not find a counting defect;
- attempted to rerun the local formal slice with
  `lake build AutoMath.RB10B12BookRamsey` under [lean/](lean), but this verify environment could
  not reproduce the earlier build because Lake attempted a dependency download and failed on network
  resolution.

So this pass found no mathematical counterexample to the prose proof, but it also did not freshly
re-establish executable reproducibility of the Lean slice inside the current offline environment.

## verify_theorem_worthiness

Exactness:

- the candidate targets the exact title theorem `R(B10, B12) = 45`;
- it is not Lean-complete, so the honest harness classification remains `CANDIDATE`, not `EXACT`.

Novelty:

- bounded PASS 1 did not establish rediscovery;
- the best conservative reading is still frontier-novel pending later publication audit.

Reproducibility:

- the prose argument is compact and theorem-shaped;
- the terminal SRG obstruction has a Lean artifact;
- the full packet was not reproducibly rerun in this verify pass because the local Lean build was
  blocked by dependency fetch failure.

Lean readiness:

- yes;
- the remaining work is sharply scoped to formalizing the upstream Goodman / convexity reduction and
  the short `11` common nonneighbors `-> 12` common neighbors bridge.

Paper leverage:

- if correct and Lean-sealed, this already looks like most of a publishable short note;
- honest solve-to-paper fraction remains about `0.85`;
- the visible title theorem is exactly `R(B10, B12) = 45`.

Scaling:

- what scales: the template
  `local book bounds -> Goodman squeeze -> forced equality profile -> rigid obstruction`;
- what does not scale automatically: the collapse to the specific SRG parameter tuple
  `(45,22,9,12)` and the final multiplicity contradiction are highly instance-specific.

Best publication-status call:

- not `INSTANCE_ONLY`;
- not `PAPER_READY`;
- best honest status at verify time is `SLICE_CANDIDATE`.

## verify_verdict

- `verify_verdict = "SURVIVES_SKEPTICAL_CHECK"`
- `classification = "CANDIDATE"`
- `confidence = 0.79`
- `lean_ready = true`
- `lean_packet_seal = true`
- `publication_status = "SLICE_CANDIDATE"`
- `publication_confidence = 0.83`
- `single_solve_to_paper_fraction = 0.85`
- `next_action = "Formalize only the two remaining upstream proof bridges, rerun the Lean build in a dependency-ready environment, and keep the packet scoped to the exact theorem R(B10, B12) = 45."`

## minimal_repair_if_any

No mathematical patch was needed.

The conservative repair in this verify pass is metadata only:

- do not treat the current Lean slice as the full theorem;
- do not leave the publication status at `SLICE_EXACT`;
- keep the candidate at `CANDIDATE` / `SLICE_CANDIDATE` until the full Ramsey wrapper is formally
  sealed.
