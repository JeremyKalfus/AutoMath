# Solve Record: The Exact Value of R(B21, B21)

## statement_lock
- Active slug: `r-b21-diagonal-book-ramsey`.
- Active title: `Determine the exact value of R(B21, B21)`.
- I use `B21` to mean the book graph consisting of 21 triangles sharing one common edge.
- Exact target: decide whether `R(B21, B21) = 85` or `R(B21, B21) = 86`.
- Equivalent extremal form: on 85 vertices, either
  - every graph has an edge contained in at least 21 triangles or a complement-edge contained in at least 21 complement-triangles, giving `R(B21, B21)=85`, or
  - there exists a graph `G` on 85 vertices such that every edge of `G` has at most 20 common neighbors and every edge of `G^c` has at most 20 common neighbors, giving `R(B21, B21)=86`.
- If the main claim closes, the exact title theorem is simply: `The Exact Value of R(B21, B21)`.

## definitions
- Let `G` be a graph on `v=85` vertices.
- For a vertex `x`, write `d(x)` for its degree in `G`.
- For distinct vertices `u,v`, write `c(u,v) = |N(u) ∩ N(v)|`.
- If `uv` is an edge of `G`, then `c(u,v)` is the number of triangles of `G` using the edge `uv`.
- If `uv` is a nonedge of `G`, then the number of common neighbors of `u,v` in the complement is
  `83 - d(u) - d(v) + c(u,v)`.
- Ambiguities/conventions to lock now:
  - common-neighbor counts exclude the endpoints themselves;
  - the packet already supplies the one-gap window `85 <= R(B21,B21) <= 86`, and solve treats that literature input as given;
  - the extremal 85-vertex object, if it exists, is a witness for `R(B21,B21)=86`, not yet a Lean-complete exact result.

## approach_A
Structural / invariant route: force any 85-vertex witness into an extremely rigid parameter set.

Assume `G` on 85 vertices avoids `B21` in both colors.

1. Pairwise constraints.
   - If `uv` is an edge, then `c(u,v) <= 20`.
   - If `uv` is a nonedge, then `uv` is an edge of `G^c`, so
     `83 - d(u) - d(v) + c(u,v) <= 20`,
     hence
     `c(u,v) <= d(u) + d(v) - 63`.

2. Global common-neighbor sum.
   - Let `m = e(G)`.
   - Let `q = C(85,2) = 3570`.
   - Let `s1 = sum_x d(x) = 2m`.
   - Let `s2 = sum_x d(x)^2`.
   - Double counting 2-paths gives
     `T := sum_{ {u,v} } c(u,v) = sum_x C(d(x),2) = (s2 - s1)/2 = (s2 - 2m)/2`.

3. Upper bound `T` using the pairwise constraints.
   - Summing over edges contributes at most `20m`.
   - Summing over nonedges contributes at most
     `sum_{uv nonedge} (d(u)+d(v)-63)`.
   - Also
     `sum_{uv nonedge} (d(u)+d(v)) = sum_x d(x)(84-d(x)) = 84s1 - s2 = 168m - s2`.
   - Therefore
     `T <= 20m + (168m - s2) - 63(q-m) = 251m - s2 - 63q`.

4. Compare the two expressions for `T`.
   - From `(s2 - 2m)/2 <= 251m - s2 - 63q`, we get
     `3s2 <= 504m - 126q`.
   - Since `q=3570`, this is
     `3s2 <= 504m - 449820`.

5. Force equality by Cauchy.
   - Cauchy gives
     `s2 >= s1^2 / 85 = 4m^2 / 85`.
   - Combining with the previous inequality yields
     `12m^2/85 <= 504m - 449820`.
   - Multiplying through by 85 and simplifying gives
     `4m^2 - 14280m + 12744900 <= 0`,
     i.e.
     `4(m - 1785)^2 <= 0`.
   - Hence necessarily `m = 1785`.

6. Degree regularity.
   - Now `s1 = 3570`.
   - Equality in Cauchy forces all degrees equal, so every vertex has degree `42`.

7. Equality propagation to every pair.
   - With `d(u)=d(v)=42`, every nonedge satisfies `c(u,v) <= 21`.
   - Since the total upper bound on `T` is attained exactly, every edge term and every nonedge term must attain equality:
     - if `uv` is an edge, then `c(u,v) = 20`;
     - if `uv` is a nonedge, then `c(u,v) = 21`.

Conclusion of Approach A:
- Any 85-vertex witness for `R(B21,B21)=86` must be a strongly regular graph with parameters
  `srg(85,42,20,21)`.
- Equivalently, the extremal witness problem is exactly the existence problem for a conference graph on 85 vertices.

Self-check after Approach A:
- The nonedge inequality sign was checked carefully; it is an upper bound, not a lower bound.
- The quadratic collapse really is exact: `4(m-1785)^2 <= 0`.
- The resulting parameter set is internally consistent with the book constraints:
  adjacent pairs have exactly 20 common neighbors, nonadjacent pairs exactly 21.

## approach_B
Construction / extremal route: once the structural reduction is known, the only honest lower-bound lane is to construct an `srg(85,42,20,21)` candidate or prove none exists.

Reasoning:
- The reduction above eliminates irregular or ad hoc witnesses.
- So a successful `R(B21,B21)=86` proof now has to pass through a conference-graph object.
- Natural first constructions should come from the `85 = 5 * 17` factorization, because both 5 and 17 support Paley/conference behavior individually.

Bounded experiment performed only after the reasoning stage:
- I tested one natural Cayley family on `Z_5 x Z_17` built from matching quadratic-character classes. It is 42-regular, but edge common-neighbor counts hit `{20,21,22,24}`, so it fails.
- I tested the obvious conference-matrix product ansatz `((S_5 + I) ⊗ (S_17 + I)) - I`. It is again 42-regular, but nonedge common-neighbor counts reach `{21,22,23,25}`, so it fails.
- I then exhausted the 24 symmetry-respecting union-of-cells class-union Cayley families obtained from the eight coordinate classes
  `0R, 0N, R0, N0, RR, RN, NR, NN`
  with total valency 42. None satisfy the target bound; the best cases still overshoot by 4.

Conclusion of Approach B:
- No simple product-style algebraic witness appeared.
- This does not rule out an `srg(85,42,20,21)`; it only says the first easy `5 x 17` templates fail.

Self-check after Approach B:
- The experiment was deliberately bounded and structural, not a generic brute-force search over graphs.
- Failure of these templates is evidence against an easy witness, not a nonexistence proof.

## lemma_graph
1. Extremal witness assumption on 85 vertices.
2. Edge constraint: `c(u,v) <= 20`.
3. Complement-edge constraint on nonedges: `c(u,v) <= d(u)+d(v)-63`.
4. Double-counting common neighbors gives a global inequality in `m` and `sum d(x)^2`.
5. Cauchy collapses the inequality to equality, forcing `m=1785` and `d(x)=42` for all `x`.
6. Equality propagation forces every edge to have 20 common neighbors and every nonedge to have 21.
7. Therefore any witness is exactly an `srg(85,42,20,21)`.
8. Main problem reduced to existence/nonexistence of that conference graph.

## chosen_plan
- Best path: keep the exact intended statement locked, prove the strongest rigorous structural reduction available, then check whether a trivial algebraic witness survives.
- This was better than starting with search because the packet marks the target as non-search-heavy and the reduction sharply compresses the witness space.
- Current honest stopping point: the reduction is rigorous, the easy witness lane failed, and I do not yet have either a construction or a nonexistence proof for `srg(85,42,20,21)`.

## self_checks
- Statement check: the solve target remained the exact 85-vs-86 question throughout; no concept drift into a broader family claim.
- Proof check: every inequality used in the reduction has been re-expanded symbolically and matches the extremal interpretation.
- Scope check: the bounded code only tested natural structured witness families after the reasoning-first stage.
- Publication check: the current output is theorem-facing and useful, but it is not yet the title theorem.

## code_used
- Yes, but only minimally and after the reasoning stage.
- Type: tiny bounded witness-verification experiments.
- Used for:
  - checking a natural `Z_5 x Z_17` quadratic-character Cayley candidate;
  - checking a simple conference-matrix composition ansatz;
  - exhausting the 24 symmetry-respecting class-union Cayley families of that product type.
- Code was not used for a generic SAT/ILP/brute-force graph search.

## result
- Strong partial result:
  any 85-vertex graph with neither `G` nor `G^c` containing `B21` must be an `srg(85,42,20,21)`.
- Equivalently:
  `R(B21,B21)=86` if and only if there exists a strongly regular conference graph with parameters `(85,42,20,21)`.
- I did not prove existence or nonexistence of that graph.
- Therefore I did not close the exact value.

Self-check after result:
- This is a real theorem slice, not an exact solve of the selected problem.
- The slice is sharp: it leaves no irregular 85-vertex witness lane open.

## family_affinity
- Strong.
- The reduction sits exactly on the diagonal one-gap book Ramsey mechanism: a `4n+1`-vertex witness would have to saturate the pairwise book bounds everywhere.
- Here that gives the clean conference-graph residue at `n=21`.

## generalization_signal
- The proof template appears to generalize formally to any diagonal one-gap instance on `4n+1` vertices:
  if a graph on `4n+1` vertices avoids `Bn` in both colors, the same common-neighbor summation should force the conference parameters `(4n+1, 2n, n-1, n)`.
- I am not claiming that as a finished general theorem here, but the algebraic pattern is clear and reusable.
- What scales:
  the pairwise common-neighbor bounds, the global 2-path count, and the Cauchy equality collapse.
- What does not scale automatically:
  converting the resulting conference-graph existence problem into an exact Ramsey value.

## proof_template_reuse
- Reusable template:
  1. encode book avoidance as edge/nonedge common-neighbor inequalities;
  2. sum over all vertex pairs;
  3. rewrite the nonedge degree sum in terms of `sum d(x)^2`;
  4. combine with Cauchy to force equality;
  5. read off the conference-graph parameters.
- This is exactly the sort of proof skeleton worth reusing on other diagonal book residues with a one-gap window.

## candidate_theorem_slice
- Candidate theorem slice:
  `If G is a graph on 85 vertices such that neither G nor its complement contains B21, then G is strongly regular with parameters (85,42,20,21).`
- This is the smallest clean theorem-facing statement I can currently justify rigorously.
- It is strong enough to turn the selected problem into a pure conference-graph existence/nonexistence question.

## smallest_param_shift_to_test
- For this exact problem, the smallest useful shift is structural rather than numerical:
  test the witness question inside the conference-graph lane before any broader search.
- Immediate next shifts that would help most:
  - search for an `srg(85,42,20,21)` within more structured families than the naive `Z_5 x Z_17` class-union constructions;
  - in the family direction, test whether the same reduction can be written cleanly for the next unresolved diagonal residue of the form `4n+1` that is a sum of two squares but not a prime power.

## why_this_is_or_is_not_publishable
- If the main claim closes, yes: this is still a genuine micro-paper lane and a successful solve would already be roughly 70-90% of a paper.
- Exact title theorem if closed:
  `The Exact Value of R(B21, B21)`.
- Minimal remaining packaging if closed:
  - one short introduction situating the `85 <= R <= 86` gap;
  - the exact-value proof or witness;
  - a compact explanation of why `85` sits outside the standard exact criteria;
  - the conference-graph reduction as the main extremal structure lemma.
- Current output alone is probably too thin for the micro-paper lane unless verification shows the reduction is genuinely absent from the literature.
- So the honest assessment is:
  theorem-facing and useful, but not yet paper-ready and not yet enough to claim the selected exact value.

## paper_shape_support
- What extra structure would make the result paper-shaped if the main claim closes?
  - the exact witness or exact impossibility argument for `(85,42,20,21)`;
  - one concise structural lemma reducing the Ramsey problem to the conference-graph residue;
  - one short boundary remark comparing `n=21` with the already-settled prime-power and non-sum-of-two-squares diagonal cases.
- One immediate corollary / remark that already falls out:
  any 85-vertex extremal witness would necessarily be 42-regular and meet the book threshold with equality on every pair.
- Current package status:
  closer to a paper-shaped claim than a random partial computation, but still just a slice until the existence question is resolved.

## boundary_remark
- The `n=21` case is exactly the boundary where the standard diagonal criteria stop helping:
  `4n+1 = 85` is a sum of two squares, so the upper criterion does not collapse the value to `4n+1`,
  but `85` is not a prime power, so the usual Paley lower-bound mechanism does not automatically give `4n+2`.
- The present reduction shows that the entire remaining difficulty is concentrated in one conference-graph residue.

## likely_failure_points
- The structural reduction may already be implicit in the existing book-Ramsey or conference-graph literature.
- The bounded construction failures do not rule out more sophisticated conference-graph constructions.
- A later verifier may find that `srg(85,42,20,21)` is already known to exist or not exist in design-theory sources.
- If so, the real mathematical work in this solve record is the reduction, not yet the exact Ramsey closure.

## what_verify_should_check
- Check whether the theorem slice
  `85-vertex extremal witness => srg(85,42,20,21)`
  is already stated or immediate in prior book Ramsey papers.
- Check whether `srg(85,42,20,21)` or an equivalent symmetric conference matrix of order 86 is already known to exist or be impossible.
- Check whether the failed `Z_5 x Z_17` class-union families correspond to named constructions that are already understood.
- Check whether the general `4n+1` equality-collapse template is already standard folklore in the diagonal book-Ramsey literature.

## verify_rediscovery
- PASS 1 was kept bounded to the required rediscovery audit.
- Query patterns used:
  - exact notation: `R(B21,B21)`;
  - alternate notation / family phrasing: `R(B_21,B_21)`, `R(B_{21},B_{21})`, and `"book Ramsey" 21 85 86`;
  - canonical-source check: the 2025 Lidicky-McKinley-Pfender-Van Overberghe paper and its `B21` / theorem-level occurrences;
  - source-internal theorem/example/corollary check inside that source;
  - a recent-status check for 2026 or later exact determinations;
  - a residue-equivalence check via `srg(85,42,20,21)` / `conference graph 85`.
- Outcome of the bounded audit:
  - the exact-value searches did not surface a paper or preprint claiming `R(B21,B21)=85` or `R(B21,B21)=86`;
  - the 2025 book-Ramsey source still supports only the one-gap window `85 <= R(B21,B21) <= 86`;
  - the Wesley 2026 source did not surface an exact diagonal closure at `n=21` in the bounded pass;
  - the conference-graph searches returned only reference-level discussion, not a primary-source theorem settling existence or nonexistence of `srg(85,42,20,21)`.
- Conservative rediscovery conclusion:
  - bounded PASS 1 did not establish rediscovery of the exact intended statement;
  - bounded PASS 1 also did not prove novelty of the reduction itself.
- PASS 1 verdict:
  - `verify_verdict` is not `REDISCOVERY`.
  - The slug must not be labeled `EXACT`; the exact Ramsey value remains unsettled in the audited source chain.

## verify_faithfulness
- The selected problem asks for the exact value of `R(B21,B21)`, namely a proof of `85` or a witness forcing `86`.
- The solve artifact does not claim that the exact value was settled; its strongest explicit mathematical content is the structural reduction
  `85-vertex two-color B21-avoider => srg(85,42,20,21)`.
- That makes the packet faithful at the prose level in one sense:
  - it clearly distinguishes the target exact theorem from the proved slice;
  - it does not pretend that the exact Ramsey number is already known.
- But it is not faithful as an exact-solve packet:
  - the verified theorem is a nearby structural slice, not the intended exact-value theorem;
  - the honest classification therefore cannot remain a positive exact-solve label.
- Tiny conservative framing repair:
  - the strongest honest statement is slightly sharper than the one-way slice recorded in solve:
    `R(B21,B21)=86` if and only if there exists an `srg(85,42,20,21)`.
  - This is immediate because such a strongly regular graph has `20` common neighbors on each edge, and its complement has the same parameters.
- Faithfulness verdict:
  - the artifact survives as a `VARIANT`, not as a verification of the intended exact statement.

## verify_proof
- I did not find an incorrect step in the reduction recorded in `approach_A`.
- Skeptical check of the key moves:
  - the complement-edge book constraint on a nonedge `uv`,
    `83 - d(u) - d(v) + c(u,v) <= 20`,
    rearranges correctly to
    `c(u,v) <= d(u) + d(v) - 63`;
  - the global identity
    `T = sum_{ {u,v} } c(u,v) = sum_x C(d(x),2) = (s2 - 2m)/2`
    is the standard count of length-2 paths by center vertex;
  - the nonedge degree-sum rewrite
    `sum_{uv nonedge} (d(u)+d(v)) = sum_x d(x)(84-d(x)) = 168m - s2`
    is correct;
  - combining the pairwise bounds gives
    `3s2 <= 504m - 126q`, with `q = C(85,2) = 3570`;
  - inserting Cauchy,
    `s2 >= 4m^2/85`,
    yields
    `4(m-1785)^2 <= 0`, so necessarily `m = 1785`;
  - equality in Cauchy forces all degrees to be equal, hence `d(x)=42` for every vertex;
  - equality in the summed upper bound then forces every edge to have exactly `20` common neighbors and every nonedge exactly `21`.
- First incorrect step found: none.
- What is proved, if the reduction is read literally:
  - any 85-vertex witness for `R(B21,B21)=86` must be an `srg(85,42,20,21)`;
  - conversely, any `srg(85,42,20,21)` would be such a witness, so the residue is exactly the conference-graph existence problem at order `85`.
- Proof-status conclusion:
  - the reduction itself appears mathematically correct;
  - the exact Ramsey value is still unproved because conference-graph existence/nonexistence is not resolved in the packet.

## verify_adversarial
- There is no separate checker or code artifact in this slug to rerun.
- Adversarial checking was therefore limited to breaking the recorded mathematics and rechecking the symbolic arithmetic.
- Local rerun performed:
  - verified `q = 3570`;
  - verified the quadratic-collapse arithmetic leading from
    `3s2 <= 504m - 126q`
    and Cauchy to
    `4(m-1785)^2 <= 0`;
  - verified that the complement of an `srg(85,42,20,21)` again has parameters `(85,42,20,21)`, so such a graph really would avoid `B21` in both colors.
- The local rerun returned `algebra_ok`.
- Adversarial break attempt result:
  - no arithmetic break was found;
  - no hidden counterexample to the reduction was produced from the recorded formulas;
  - the unresolved point is source-level and theorem-level, not computational: existence or nonexistence of the conference graph itself is still open in the current packet.

## verify_theorem_worthiness
- Exactness:
  - fails for the intended statement.
  - The exact Ramsey value `R(B21,B21)` is not determined here.
- Novelty:
  - no rediscovery of the exact target was found in bounded PASS 1;
  - bounded PASS 1 also did not establish that the reduction itself is new.
- Reproducibility:
  - strong for the reduction; the argument is short, symbolic, and locally checkable;
  - weak as a publication packet for the selected problem because the remaining gap is still the main theorem-sized residue.
- Lean readiness:
  - no.
  - Lean would formalize a structural helper theorem, but Lean is not the shortest remaining path to a sealed publication packet because the central existence/nonexistence question for `srg(85,42,20,21)` is still unresolved.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  - No.
  - It would likely be an important lemma in such a note, but not most of the note.
- Best estimate of paper fraction already supplied by the verified content:
  - about `0.38`.
- Title theorem actually visible now:
  - `Diagonal B21-extremal 85-vertex graphs are exactly strongly regular graphs with parameters (85,42,20,21)`.
- What scales:
  - the pairwise common-neighbor inequalities;
  - the global two-path sum;
  - the Cauchy-equality collapse on one-gap diagonal `4n+1` book-Ramsey residues.
- What clearly does not:
  - turning the conference-graph residue into an exact Ramsey value;
  - any claim that the specific residue `(85,42,20,21)` is already resolved.
- Best honest publication status:
  - `NONE`.
  - The packet has theorem leverage, but the remaining gap is still theorem-sized rather than editorial.

## verify_verdict
- `verify_verdict = "VARIANT"`
- `classification = "VARIANT"`
- `confidence = 0.89`

Reason:

- bounded PASS 1 did not show rediscovery of the intended exact theorem;
- the recorded reduction survives skeptical proof checking;
- the surviving result is a nearby structural theorem slice, not the selected exact-value theorem.

## minimal_repair_if_any
- No mathematical repair to the reduction was needed.
- Conservative packet repair only:
  - relabel the slug from `PARTIAL` to `VARIANT`;
  - keep the strongest honest claim as the conference-graph equivalence at order `85`;
  - keep `lean_ready = false` and `lean_packet_seal = false`;
  - route the next solve step strictly into the `srg(85,42,20,21)` existence/nonexistence lane rather than treating the slug as near-publication.

## publication_prior_art_audit
- Exact-statement search:
  - bounded web checks on `R(B21,B21)` and alternate notation did not surface a primary-source paper or preprint claiming `R(B21,B21)=85` or `R(B21,B21)=86`;
  - a targeted arXiv pass for `R(B21,B21)`, `R(B_{21},B_{21})`, and `book Ramsey 21 85 86` returned no relevant results.
- Canonical-source check:
  - the current DS1 survey entry for books still records only
    `4n + 1 <= R(Bn, Bn) <= 4n + 2` for `n <= 21`,
    together with the exact special cases
    `R(Bn, Bn) = 4n + 2` when `4n + 1` is a prime power and
    `R(Bn, Bn) <= 4n + 1` when `4n + 1` is not a sum of two squares;
  - at `n = 21`, this leaves exactly the one-gap window `85 <= R(B21,B21) <= 86`, since `85 = 2^2 + 9^2` is a sum of two squares and is not a prime power.
- Canonical-source internal theorem / proposition / corollary / observation check:
  - Lidicky-McKinley-Pfender-Van Overberghe 2025, Lemma 1 states
    `4n + 1 <= R(Bn, Bn) <= 4n + 2` for all `4 <= n <= 21`;
  - the note after Lemma 1 restates the older sufficient condition
    `R(Bn, Bn) <= 4n - 1` when `4n + 1` is not a sum of two squares;
  - no theorem, proposition, example, corollary, or observation in that bounded source pass gave the exact value at `n = 21`.
- One outside-source status pass:
  - Wesley 2026 reports new lower bounds and an infinite exact family for `R(B_{n-1}, B_n)`, but the bounded pass did not find any theorem there closing the diagonal `n = 21` case;
  - on the equivalent residue side, the bounded conference-matrix / strongly-regular-graph pass still treated the order-`85` conference residue as unsettled rather than closed by a standard existence theorem.
- Prior-art conclusion:
  - bounded audit did not establish rediscovery of the exact intended statement;
  - bounded audit also did not establish that the reduction to `srg(85,42,20,21)` is itself new.

## publication_statement_faithfulness
- The selected one-shot target is still the exact-value theorem `R(B21,B21) in {85,86}`.
- The strongest surviving audited claim is not that exact theorem.
- The faithful audited packet must therefore pivot from
  `The Exact Value of R(B21, B21)` to the structural slice
  `85-vertex two-color B21-avoiders are exactly the conference-graph residue`.
- Stronger than "here is an example":
  - Yes.
  - The surviving claim is a quantified structural theorem, not an isolated construction or computation.
- Strongest faithful statement:
  - if `G` is a graph on `85` vertices such that neither `G` nor `G^c` contains `B21`, then `G` is strongly regular with parameters `(85,42,20,21)`;
  - equivalently, `R(B21,B21)=86` if and only if an `srg(85,42,20,21)` exists.
- Faithfulness verdict:
  - faithful as a structural-slice packet;
  - not faithful as a solved exact-value packet.

## publication_theorem_worthiness
- Is there a real theorem here?
  - Yes, but it is a theorem slice rather than the intended title theorem.
- Is the proof structural or merely instance-specific?
  - Structural.
  - The argument is an equality-collapse from pairwise common-neighbor bounds, a global two-path count, and Cauchy; it is not a hand-picked finite-case verification.
- Would this survive a referee asking "what is the theorem?"
  - At the theorem-slice level, yes:
    `Any 85-vertex diagonal B21-extremal witness must be an srg(85,42,20,21)`.
  - As a standalone paper claim in the present lane, probably not yet, because the referee's immediate follow-up would be why this is more than a helper lemma for the unresolved exact value.
- Is the claim still too dependent on hand-picked small cases?
  - No for the reduction itself.
  - The failed product-style witness experiments are side evidence only and are not load-bearing for the theorem slice.
- Title-theorem strength:
  - moderate.
  - There is a crisp theorem sentence, but it is not the selected exact-value title theorem and it does not by itself close the residue.

## publication_publishability
- Would the current bounded-verified result already constitute most of a publishable note?
  - No.
- Best estimate of paper fraction already supplied by the current strongest honest claim:
  - about `0.40`.
- What percentage would a full one-shot exact solve have supplied?
  - still roughly the originally advertised `0.78`, but that solve did not happen here.
- Is the remaining gap genuinely small?
  - No.
  - The remaining gap is still theorem-sized: existence or nonexistence of the conference-graph residue `srg(85,42,20,21)`.
- Did the candidate look closer to a paper before audit than it does after audit?
  - Yes.
  - The candidate remains a strong micro-paper target if the exact value is closed, but the current slice does not honestly leave only light packaging.
- If this is not paper-ready, should it be moved aside rather than expanded into a larger theorem program?
  - Yes.
  - It should be cooled as an exact-value publication target unless future work directly settles the conference-graph residue.
- Would Lean directly seal the packet?
  - No.
  - Lean would only formalize the helper reduction; it would not remove the main publication blocker.

## publication_packet_audit
- Publication-status verdict:
  - `NONE`.
- Why not `INSTANCE_ONLY`:
  - the claim is stronger than a single example or explicit witness.
- Why not `SLICE_CANDIDATE`:
  - the remaining publication gap is not genuinely small; the missing step is still the title-theorem-sized residue.
- Why not `SLICE_EXACT`:
  - although the reduction itself appears correct, bounded audit did not establish sufficient standalone novelty or near-paper sufficiency for this one-shot lane.
- Why not `PAPER_READY`:
  - the exact Ramsey value is still open and the surviving theorem slice does not yet read like most of a publishable note.
- Publication-packet quality:
  - moderate structural slice, not a near-paper packet.
- Proof artifacts preserved:
  - Yes.
  - The reduction, equivalence statement, and bounded witness-failure notes are preserved well enough for later reuse.

## micro_paper_audit
- MICRO-PAPER lane verdict on the current audited packet:
  - fail in current form.
- Reason:
  - the one-shot lane was attractive because an exact solve would have been most of a paper;
  - the audited output falls materially short of that threshold and leaves a central theorem-sized residue.
- Is there a real title theorem, theorem slice, or counterexample theorem here?
  - There is a real theorem slice.
- Would this result already support a short note with only light write-up left?
  - No.
- Publication narrative strength after audit:
  - moderate.
  - The narrative is clear, but it still points to an unresolved endpoint rather than a closed note.
- Lean role:
  - optional later archival formalization only, and only after the exact-value blockage is removed.

## strongest_honest_claim
- `If G is a graph on 85 vertices such that neither G nor its complement contains B21, then G is strongly regular with parameters (85,42,20,21). Equivalently, R(B21,B21)=86 if and only if an srg(85,42,20,21) exists.`

## paper_title_hint
- `A Conference-Graph Reduction for the Remaining Diagonal Book Ramsey Residue at n = 21`

## next_action
- Set `publication_status = NONE`, keep `human_ready = false`, and do not send this packet to the Lean queue.
- Preserve the current proof artifacts, but cool the slug as an exact-value publication target.
- Reopen only on one of two narrow paths:
  - a direct solve of the `srg(85,42,20,21)` existence/nonexistence residue;
  - a separate tightly bounded curation decision that the reduction itself, rather than the exact value, is the primary target.
