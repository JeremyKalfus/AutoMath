## statement_lock
Target slug: `r-b12-b12-diagonal-book-ramsey`.

Active title: `Determine the exact value of R(B12, B12)`.

Exact intended theorem for this solve attempt:

`R(B12, B12) = 50`, where `B12` is the book graph with 12 pages, i.e. 12 triangles sharing a common spine edge.

Equivalent Ramsey formulation:

`50` is the least `n` such that every red-blue coloring of `K_n` contains an edge whose same-color common neighborhood has size at least `12`.

Proposed title theorem if this closes:

`The Exact Value of R(B12, B12)`.

Self-check:
- This locks the right endpoint question from the packet: the only remaining possibilities are `49` or `50`.
- The endpoint needed for a publishable note is an exact value, not just another witness or heuristic.

## definitions
Let `G` be the red graph of a red-blue coloring of `K_N`, and let `\bar G` be the blue graph.

For an edge `uv` of `G`, the number of red triangles on spine `uv` is `|N_G(u) ∩ N_G(v)|`. So `G` contains a red `B12` iff some red edge has at least `12` red common neighbors.

Likewise, `\bar G` contains a blue `B12` iff some blue edge has at least `12` blue common neighbors.

Thus a coloring of `K_N` avoids monochromatic `B12` exactly when:

- every red edge has at most `11` red common neighbors, and
- every blue edge has at most `11` blue common neighbors.

For the lower-bound construction, write `P(49)` for the Paley graph on the field `F_49`, with adjacency `x ~ y` iff `x - y` is a nonzero square.

Self-check:
- The book parameter is the number of same-color common neighbors of a spine edge.
- This matches the packet language about “tracking common-neighborhood restrictions along candidate spine edges.”

## approach_A
Structural / invariant approach:

Try to realize the critical `49`-vertex coloring as a self-complementary highly regular graph. For a diagonal book problem at the `4n+1` / `4n+2` frontier, the natural extremal target is a graph on `49 = 4*12 + 1` vertices where:

- each vertex has degree close to `24`,
- each red edge lies in exactly `11` red triangles, and
- each blue edge lies in exactly `11` blue triangles.

Those are exactly the common-neighborhood statistics of a self-complementary strongly regular graph with parameters `(49,24,11,12)`.

The Paley graph `P(49)` is the canonical candidate. If it indeed has parameters `(49,24,11,12)`, then:

- every red edge has exactly `11` red common neighbors, so there is no red `B12`,
- its complement has the same parameters, so every blue edge has exactly `11` blue common neighbors, so there is no blue `B12`.

That would give a `49`-vertex witness immediately, which is the shorter path to an exact value because the packet already imports the upper bound `R(B12, B12) <= 50`.

Self-check:
- This path is publication-aligned: it aims directly at the one missing endpoint.
- It uses structure before computation and does not need a broad search campaign.

## approach_B
Construction / extremal / contradiction approach:

Try to prove `R(B12, B12) = 49` by forcing a monochromatic `B12` in every coloring of `K_49`.

The obstacle is that the packet already flags a known lower interval `49 <= R(B12, B12) <= 50`, so a `49`-forcing proof would have to refute the possibility of a highly balanced critical graph on `49` vertices. The natural extremal numerology on `49` vertices points toward a `24`-regular self-complementary object with book size exactly `11`, not toward instability.

So the contradiction route appears weaker than the constructive route: the most symmetric candidate on the critical order is plausible, compact, and known in adjacent Ramsey settings.

Self-check:
- This is a genuine alternate approach, but it does not currently dominate the construction route.
- No silent fallback: I am explicitly rejecting the `49`-forcing route because the extremal structure points the other way.

## lemma_graph
1. In any coloring, a monochromatic `B12` appears exactly when some same-color edge has at least `12` same-color common neighbors.
2. If `P(49)` has strongly regular parameters `(49,24,11,12)`, then each red edge has exactly `11` red common neighbors.
3. Because `P(49)` is self-complementary, each blue edge also has exactly `11` blue common neighbors.
4. Therefore the red-blue coloring from `P(49)` avoids monochromatic `B12` on `49` vertices.
5. Hence `R(B12, B12) >= 50`.
6. The selected packet imports the literature upper bound `R(B12, B12) <= 50`.
7. Therefore the exact-value candidate is `R(B12, B12) = 50`.

Self-check:
- The proof skeleton is short and theorem-shaped.
- The only serious load-bearing point is the Paley parameter count.

## chosen_plan
Use the Paley graph on `49` vertices as the lower-bound witness, and make the parameter computation explicit enough that the remaining verification task is narrow.

Take `F_49` with quadratic character `χ`, extended by `χ(0)=0`. In `P(49)`, vertices `x,y` are adjacent when `χ(x-y)=1`.

Facts:

- Degree: each vertex has `(49-1)/2 = 24` neighbors.
- Undirectedness: since `49 ≡ 1 (mod 4)`, `-1` is a square, so `χ(x-y)=χ(y-x)`.
- Common-neighborhood count: by translation, for distinct vertices it is enough to count common neighbors of `0` and `d != 0`.

Let

`N(d) = |{ z in F_49 : χ(z)=1 and χ(z-d)=1 }|`.

Expanding the square-indicator and using the standard quadratic-character identity

`Σ_z χ(z(z-d)) = -1` for `d != 0`,

one gets

`4N(d) = 49 - 3 - 2χ(d)`.

Hence:

- if `d` is a square, `N(d) = (49-5)/4 = 11`,
- if `d` is a nonsquare, `N(d) = (49-1)/4 = 12`.

So `P(49)` has parameters `(49,24,11,12)`.

Now interpret this for books:

- a red edge is an edge of `P(49)`, hence has exactly `11` red common neighbors,
- a blue edge is a nonedge of `P(49)`, and in the complement it also has exactly `11` blue common neighbors.

Therefore the Paley coloring of `K_49` avoids monochromatic `B12`, giving `R(B12, B12) >= 50`. Combined with the imported upper bound `R(B12, B12) <= 50`, this yields the exact-value candidate

`R(B12, B12) = 50`.

Self-check:
- This is a full lower-bound witness plus a short closure argument using the packet’s upper bound.
- The proof remains compact enough to read like the body of a micro-paper.

## self_checks
- Statement lock check: the solve target stayed on the exact endpoint `49` versus `50`.
- Definition check: the book count is the common-neighborhood count of the spine edge.
- Structural check: the critical-order numerology matches `P(49)` exactly.
- Proof check: the only imported external ingredient beyond standard Paley facts is the packet’s upper bound `R(B12, B12) <= 50`.
- Risk check: if the notation for `B12` were shifted in a source, the argument would fail, so verify must confirm the page-count convention.
- Packaging check: this is not just an instance witness; if verified, it closes the named frontier and already looks like a title theorem.

## code_used
Minimal code only, used after the reasoning stage as witness verification.

A bounded Python script modeled `F_49 = F_7[u]/(u^2+1)`, built the Paley graph, and checked:

- there are exactly `24` nonzero squares,
- every red edge has exactly `11` red common neighbors,
- every blue edge has exactly `11` blue common neighbors.

So the computational check matches the structural claim `(49,24,11,12)` and confirms book size `11` in each color.

## result
Strong exact-value candidate:

`R(B12, B12) = 50`.

Reason:

1. The Paley graph `P(49)` gives a red-blue coloring of `K_49`.
2. In that coloring, every edge of either color lies in exactly `11` monochromatic triangles.
3. Therefore neither color contains `B12`.
4. Hence `R(B12, B12) >= 50`.
5. The active packet imports the literature bound `R(B12, B12) <= 50`.
6. Therefore the exact value is forced to be `50`.

Immediate supporting theorem slice:

`The Paley graph P(49) is a 49-vertex critical coloring for B12, with maximum monochromatic book size exactly 11 in each color.`

Natural corollary / remark:

The lower-bound side is not merely existential: it is realized by a rigid self-complementary strongly regular graph, so the endpoint is explained by structure rather than by ad hoc search.

What part of the argument scales:

- The Paley construction scales to any prime power `q ≡ 1 (mod 4)`.
- For such `q`, `P(q)` gives a diagonal-book lower bound because each edge lies in exactly `(q-5)/4` same-color triangles.

What part does not scale automatically:

- Exact closure still needs a matching upper bound at the same parameter.
- The present note closes `n=12` only because the packet already imports the one-step upper bound `R(B12, B12) <= 50`.

What theorem slice is suggested:

`For q = 4n + 1` a prime power with a known upper bound `R(B_n, B_n) <= q + 1`, the Paley graph `P(q)` is the natural critical witness for the matching lower bound `R(B_n, B_n) >= q + 1`.

What one or two next parameter shifts would help most:

- `n = 13`, where `4n+1 = 53` is also a prime and the same Paley lower-bound template applies.
- Any nearby diagonal case where the literature already leaves only a one-step gap `4n+1` versus `4n+2`.

Whether the current package is still just an instance or already closer to a paper-shaped claim:

It is closer to a paper-shaped claim. The main remaining work is verification and packaging, not new mathematical exploration.

## family_affinity
High.

This candidate sits directly inside the diagonal book Ramsey family, and the witness is the standard finite-field extremal object one would expect at the `4n+1` threshold. The result is not a disconnected curiosity; it is anchored to the same family numerology as the neighboring exact diagonal and almost-diagonal book values.

## generalization_signal
Moderate but real.

The construction suggests the reusable template:

`P(q)` with `q ≡ 1 (mod 4)` avoids monochromatic `B_n` when `n = (q-1)/4`.

That does not by itself produce new exact values, but it gives a sharp lower-bound mechanism whenever a one-step upper bound is available. So the argument is not a one-off trick even though the current exact closure is still an instance-level note.

## proof_template_reuse
Reusable template:

1. Pick `q = 4n + 1` a prime power.
2. Use the Paley graph `P(q)` as the candidate critical coloring.
3. Compute the book size from the strongly regular parameters `(q, (q-1)/2, (q-5)/4, (q-1)/4)`.
4. Pair that lower bound with any independent upper bound `R(B_n, B_n) <= q + 1`.

This template is highly reusable on the lower-bound side, but the exact-value closure remains family-specific because the upper bound is the nonautomatic step.

## candidate_theorem_slice
Best exact theorem slice visible from this solve:

`In the Paley coloring of K_49, every monochromatic book has at most 11 pages. Consequently K_49 admits a red-blue coloring with no monochromatic B12.`

Combined with the imported upper bound, this slice upgrades to the exact-value candidate `R(B12, B12) = 50`.

## smallest_param_shift_to_test
Most informative next shifts:

- `B13` via `q = 53`, because the same Paley witness exists and could matter if the literature leaves a one-step gap there.
- `B9` or another nearby diagonal value with `4n+1` a prime power and a thin upper-bound gap, to test whether this is a recurring micro-paper lane rather than a single isolated closure.

## why_this_is_or_is_not_publishable
If the Paley-based closure is verified against the literature notation and the existing upper bound, this is publishable in the micro-paper lane.

Why:

- a successful solve is already about `80-90%` of a short paper,
- the exact title theorem is a named diagonal Ramsey endpoint,
- the witness is compact, conceptual, and finite-field structured,
- the remaining packaging work is minimal: state the Paley construction, record the `(49,24,11,12)` common-neighborhood counts, cite the existing upper bound, and compare with nearby exact book values.

Current honesty check:

- the result is strong enough to be paper-shaped if verified,
- but at solve stage it is still a `CANDIDATE`, not a Lean-complete exact closure,
- the note would be too thin only if the Paley argument were already implicit in the cited upper-bound source or if the source uses a conflicting book notation.

## paper_shape_support
What extra structure makes this result paper-shaped once the main claim closes:

- one clean proposition isolating the Paley witness as a `B12`-critical coloring of `K_49`,
- one short theorem combining that proposition with the imported upper bound to conclude `R(B12, B12) = 50`,
- one boundary remark explaining that the argument scales as a lower-bound template for `q = 4n + 1` prime powers but exact closure still depends on matching upper bounds.

Minimal remaining packaging work:

- verify the notation and citation alignment,
- write the common-neighborhood computation in paper prose,
- include the tiny comparison paragraph with `R(B11,B12)=47` and the smaller exact diagonal benchmark from the packet.

## publication_prior_art_audit
Bounded publication audit date: `2026-04-14`.

Exact-statement search:

- A bounded web search for the exact diagonal statement using combinatorics-qualified forms of `R(B12, B12)` did not surface any later exact-value paper.
- Because raw `B12` queries collide heavily with vitamin-B12 pages, I treated those searches as noisy and only kept hits that also contained Ramsey / book-graph context.

Alternate-notation search:

- I checked the same claim under alternate book-graph language such as `B_{12}`, `K_2 + \overline{K}_{12}`, and the general “book Ramsey” wording.
- The bounded alternate-notation pass still converged to the same relevant sources rather than to a later exact diagonal closure.

Canonical source check:

- In the accessible 2025 EJC source, the load-bearing source anchor is `Theorem 1`, not `Lemma 1`.
- `Theorem 1` states `4n + 1 <= R(B_n, B_n) <= 4n + 2` for `4 <= n <= 21`, so the canonical source still leaves `49 <= R(B12, B12) <= 50`.
- The same source also records nearby exact values such as `R(B8, B8) = 33` and discusses independent work on book-Ramsey results and a generalization of `R(B_{n-1}, B_n) = 4n - 1`, but that discussion is off-diagonal and does not collapse the diagonal `B12` endpoint.

Outside-source status check:

- Wesley (Discrete Mathematics, 2026) is a valid bounded recent-status source because it studies lower bounds and exact almost-diagonal book results in the same family.
- Its abstract and article page did not advertise an exact diagonal closure for `R(B12, B12)`.
- On `2026-04-14`, the article page showed `Cited by (0)`, so this bounded follow-up check did not reveal a later paper already claiming the exact value.

Conservative prior-art verdict:

- No rediscovery was found in this bounded audit.
- The literature still appears to stop at the one-step diagonal interval `49 <= R(B12, B12) <= 50`.

## publication_statement_faithfulness
The packet’s mathematical target is source-faithful, but one citation label needs correction.

- The intended object is the book graph `B12` with `12` pages, equivalently `12` triangles sharing a common spine edge.
- That matches the source-family usage of `B_n = K_2 + \overline{K}_n`; there is no evidence here of a notation shift that would reinterpret `B12` as a vertex count rather than a page count.
- The active packet correctly treats the public frontier as a one-step diagonal question, not as an off-diagonal or asymptotic statement.
- The source-faithfulness issue is bibliographic: the diagonal interval appears in `Theorem 1` of the canonical EJC paper, whereas the active selected packet cites it as `Lemma 1`.
- The solve record’s intended theorem is faithful to the public frontier if phrased as: combine a `49`-vertex Paley witness with the published upper bound to close the exact value.

## publication_theorem_worthiness
This is stronger than “here is an example.”

- Strongest honest theorem slice: the Paley graph `P(49)` is a structural `49`-vertex critical coloring for `B12`, with maximum monochromatic book size `11` in each color.
- If that slice is written source-faithfully and sealed, it immediately yields the title theorem `R(B12, B12) = 50`.
- That is a real theorem, not a hand-picked isolated example, because the proof mechanism is structural: self-complementary strongly regular numerology and common-neighborhood counts explain the whole witness.
- A referee asking “what is the theorem?” would get a clean answer: an exact diagonal book Ramsey value, with one proposition for the Paley witness and one theorem closing the interval.
- The theorem is still narrow. The exact closure depends on one finite parameter and one imported upper bound, so this is a micro-paper slice rather than a broad program theorem.

## publication_publishability
If the solve packet is correct and later Lean-sealed, it would already constitute most of a short publishable note.

- Estimated one-solve-to-paper fraction: about `80%`.
- The result already has a plausible title theorem, a standard family anchor, and low editorial overhead.
- The proof is mostly structural rather than brute-force, so the note would read like a genuine exact-value paper instead of a search dump.
- The remaining gap is genuinely small: preserve a durable candidate-local checker or explicit witness certificate, write the Paley common-neighborhood argument in source-faithful prose, and then decide whether Lean is the efficient sealing step.
- This is not yet `PAPER_READY` because the current artifact folder preserves only the prose proof packet, not a durable executable checker or Lean-ready formal statement.
- If the packet stalls at that preservation step, it should be moved aside rather than expanded into a broader diagonal-book program.

## publication_packet_audit
Packet quality after audit: `moderate`.

- What is already preserved: the canonical `record.md` contains the theorem lock, the Paley-parameter proof skeleton, and the exact-value candidate.
- What is missing: the artifact folder does not currently preserve the bounded checker mentioned in `code_used`, nor an explicit witness file or polished proof note separate from the running record.
- So the packet is theorem-worthy but not yet sealed as a referee-facing micro-paper packet.
- Lean would directly seal the packet only after those local proof artifacts are frozen. Right now Lean would be premature and would function more as archival polish than as the shortest next step.

## micro_paper_audit
Micro-paper verdict: pass, but not stop-ready.

- Is the strongest honest claim stronger than an example? `Yes`.
- Would a correct and Lean-sealed solve already constitute most of a publishable note? `Yes`.
- What percentage of the paper would one solve already provide? About `80%`.
- Is there a real title theorem or theorem slice here? `Yes`: the exact diagonal value or, conservatively, the Paley-critical-coloring slice.
- Is the proof structural or merely instance-specific? Mostly structural on the lower-bound side, with an instance-specific closure via the known one-step upper bound.
- Would this survive a referee asking “what is the theorem?” `Yes`, if the witness computation is frozen cleanly.
- Is the claim still too dependent on hand-picked small cases? `No` in method, though `Yes` in scope because the note is still one exact parameter.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? The remaining gap is genuinely small.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? `Yes`.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Lean can be the seal step later, but only after the local proof packet is frozen more cleanly than it is now.

## strongest_honest_claim
Bounded publication audit supports the following conservative claim:

No bounded prior-art check found that `R(B12, B12)` was already exactly determined after the 2025 source interval. The local solve packet gives a credible structural route in which the Paley graph `P(49)` supplies a `49`-vertex coloring with maximum monochromatic book size `11` in each color; paired with the published upper bound, that would settle the exact value `R(B12, B12) = 50`. At publication-audit time, however, this remains an exact-value `CANDIDATE` rather than a sealed exact theorem, because the packet is preserved only as a running proof record and not yet as a durable checker-plus-proof bundle ready for Lean or direct paper packaging.

## paper_title_hint
`The Exact Value of R(B12, B12)`

## next_action
Freeze this packet before broadening anything else:

- correct the source anchor from `Lemma 1` to `Theorem 1`,
- preserve a candidate-local Paley(49) checker or explicit witness certificate under the slug,
- extract the two-step proof packet “Paley critical coloring on 49 vertices” plus “published upper bound implies exact value,”
- only then hand the packet to Lean or, if that preservation step does not stabilize quickly, move the candidate aside instead of expanding into a wider book-Ramsey program.

## boundary_remark
Boundary remark:

The present argument closes the endpoint by supplying the missing `49`-vertex critical coloring. It does not produce a new upper-bound method, and it does not automatically settle neighboring diagonal book numbers. So the result is structurally meaningful but still tightly localized to the `n=12` endpoint unless paired with other upper bounds.

## likely_failure_points
- The load-bearing point is the Paley parameter computation `(49,24,11,12)`.
- Verify must confirm that `B12` means exactly 12 triangles on one spine edge, with no notation shift.
- Verify must confirm that the imported upper bound `R(B12, B12) <= 50` is stated for the same book graph convention.
- Verify should check whether the 2025 source already mentions the `49`-vertex Paley witness explicitly; if it does and already closes the interval implicitly, this becomes a rediscovery risk rather than a new solve.

## what_verify_should_check
- Recompute the Paley-49 witness independently, preferably with an explicit adjacency list or a second checker.
- Confirm the field model `F_49 = F_7[u]/(u^2+1)` and the square set used in the witness verification.
- Confirm that both colors have maximum book size exactly `11`.
- Check the 2025 paper carefully for whether the lower-bound construction for `49 <= R(B12,B12)` is already this Paley graph or an equivalent polycirculant witness.
- Confirm the upper-bound statement `R(B12, B12) <= 50` exactly as used here.
- Decide whether the publication status should remain `SLICE_CANDIDATE` or upgrade later after novelty and exact-source checks.

## verify_rediscovery
Bounded prior-art audit run on `2026-04-14`.

Search patterns used:

- exact instance notation: `"R(B12, B12)"`
- alternate notation: `"R(B_{12}, B_{12})"` and `"diagonal book Ramsey" 49 50 B12`
- canonical source: `"Small Ramsey numbers for books, wheels, and generalizations"`
- theorem / proposition / example / corollary checks inside the same source family: title search on the 2025 EJC paper plus theorem-level search on the classical diagonal-book formula
- recent-status check: `"Lower bounds for book Ramsey numbers" "B12" "R(B12, B12)"`

Outcome:

- Rediscovery is established within budget.
- The bounded recent-status search surfaced William J. Wesley, `"Lower bounds for book Ramsey numbers"` (Discrete Mathematics 349(5), 2026), which cites the older Rousseau-Sheehan diagonal theorem: `R(B_n,B_n) = 4n + 2` whenever `4n + 1` is a prime power.
- Applying that published theorem at `n = 12` gives `4n + 1 = 49`, and `49 = 7^2` is a prime power, so the exact value `R(B12, B12) = 50` is already implied in prior art.
- A second bounded theorem-level search returned the same prime-power formula in later literature discussions, which confirms this is not an isolated indexing artifact.
- The 2025 EJC interval `49 <= R(B12, B12) <= 50` is therefore not the true frontier basis for this exact tuple. Even if that paper only states the interval locally, the exact statement is already settled by older published work.

Verifier judgment:

- `verify_verdict = "REDISCOVERY"` is mandatory.
- `classification = "REDISCOVERY"` and `publication_status = "REDISCOVERY"` follow because the exact intended statement is already solved in the literature.

## verify_faithfulness
The local mathematical claim matches the intended packet statement, but the packet's frontier framing is not faithful to the literature.

- Intended statement: determine the least `n` such that every red-blue coloring of `K_n` contains a monochromatic book `B12`.
- Solver claim: produce a `49`-vertex coloring with no monochromatic `B12`, then combine it with the sourced upper bound `R(B12, B12) <= 50` to conclude the exact value `50`.

Checks:

- The packet and the source use the standard book convention: `B12` means `12` triangles sharing one spine edge.
- The solver did not drift to a weaker proxy such as a bound on average book size or a different book parameter.
- The proof is genuinely for the diagonal pair `R(B12, B12)`, not an adjacent off-diagonal case.
- The real faithfulness failure is novelty/source faithfulness: the packet treated the tuple as an open one-step gap even though older literature already yields the exact value.

Faithfulness verdict:

- No wrong-theorem drift or quantifier drift found in the mathematics.
- The run is nevertheless not a frontier solve. The honest label is `REDISCOVERY`, not `CANDIDATE`.

## verify_proof
No incorrect step was found in the local rederivation.

Load-bearing proof chain checked:

1. In a two-coloring, a monochromatic `B12` is equivalent to some same-color edge having at least `12` same-color common neighbors.
2. For the Paley graph `P(49)`, the claimed parameter set is `(49,24,11,12)`.
3. Therefore each red edge has exactly `11` red common neighbors.
4. The complement coloring likewise gives each blue edge exactly `11` blue common neighbors.
5. So the `49`-vertex coloring avoids monochromatic `B12`, giving `R(B12, B12) >= 50`.
6. Combined with any correct published upper bound at `50`, the exact value is `R(B12, B12) = 50`.

Proof-risk assessment:

- The character-sum step in `chosen_plan` is compressed and would need cleaner writeup in a paper packet.
- That compression did not produce a detected contradiction: the resulting parameter values agree with an independent reconstruction of the graph.
- No hidden case split or notation mismatch was found in the argument actually needed for `n = 12`.
- The proof does not create new mathematics here; it independently recovers a result already implied by prior art.

First incorrect step:

- None found.

## verify_adversarial
No candidate-local checker file existed in the artifact directory, so the adversarial pass used an independent fresh recomputation.

Independent recomputation performed:

- modeled `F_49` as `F_7[u]/(u^2+1)`,
- enumerated the nonzero squares,
- built the Paley adjacency relation on all `49` vertices,
- checked all `588` red edges and all `588` blue edges.

Observed output:

- every vertex has degree `24`,
- every red edge has exactly `11` red common neighbors,
- every blue edge has exactly `11` blue common neighbors.

Adversarial verdict:

- The witness survives the direct break attempt.
- The main reproducibility weakness is still that this recomputation is not yet preserved as a durable candidate-local checker artifact.
- That weakness no longer controls stage status, because rediscovery has already closed the verify decision.

## verify_theorem_worthiness
Exactness:

- The strongest visible mathematical claim is the exact statement `R(B12, B12) = 50`.
- In this run, exactness does not help publication status because the exact statement is already known.

Novelty:

- Novelty fails.
- The exact intended statement is already implied by published prior art via the Rousseau-Sheehan prime-power theorem surfaced in the bounded audit.

Reproducibility:

- Moderate, not high.
- The core witness was independently recomputed during verify, but the repo does not yet preserve that checker as a durable local artifact tied to this slug.

Lean readiness:

- Not Lean-ready as the next step.
- Lean would only formalize a rediscovery. It is not the shortest remaining path to a sealed frontier packet.

Paper leverage:

- For the active micro-paper lane, leverage is effectively zero because the theorem is already known.
- If the local argument were correct and Lean-sealed, it would still not constitute most of a publishable frontier note under the repo objective.
- Best current estimate for frontier-publication fraction: `0-10%`.
- The title theorem actually visible is a rederivation of the known exact value `R(B12, B12) = 50`.
- What scales: the Paley lower-bound template, and more importantly the already-published prime-power exact theorem for diagonal books.
- What clearly does not scale as a publication claim: the novelty narrative for this exact tuple.

Publication-status judgment:

- Best honest publication status is `REDISCOVERY`.
- This is not `INSTANCE_ONLY`, `SLICE_CANDIDATE`, or `PAPER_READY` for the live lane.
- Explicit answers required by the verify brief:
  - Would this result, if correct and Lean-sealed, already constitute most of a publishable note? `No`, because the exact statement is already in prior art.
  - What percentage of the paper would one solve already provide? `0-10%` for a frontier note under the current objective.
  - What title theorem is actually visible? `A rederivation of the known value R(B12, B12) = 50`.
  - What part of the argument scales? `The Paley witness template and the classical prime-power diagonal-book theorem`.
  - What part clearly does not? `The novelty and publication narrative for the B12 diagonal endpoint`.
  - Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? `Neither`; for this harness taxonomy it is `REDISCOVERY`.

## verify_verdict
`verify_verdict = "REDISCOVERY"`

Summary judgment:

- Bounded prior-art checking established rediscovery.
- The local mathematics appears to be a correct rederivation of a known result.
- Independent recomputation supports the Paley(49) witness and the claimed book-size bound `11` in each color.
- The run must not remain labeled as a frontier candidate. The honest post-verify state is `REDISCOVERY`, with `next_action = "archive_as_rediscovery"`.

## minimal_repair_if_any
No mathematical repair was needed to the local argument.

Small conservative repair recommended for the record:

- record the rediscovery anchor explicitly in the candidate memory and archive path: Rousseau-Sheehan's prime-power theorem already implies `R(B12, B12) = 50`.
- if this slug is ever revisited for expository or formalization purposes, preserve the independent Paley(49) checker under the slug as a historical verification artifact rather than a frontier-proof artifact.
