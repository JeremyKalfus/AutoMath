# statement_lock

Target slug: `paley-graph-internal-partition`

Title theorem candidate:

> For every prime power `q ≡ 1 (mod 4)`, the Paley graph `P(q)` admits an internal partition. In fact, if `Q` is the set of nonzero quadratic residues in `F_q`, then the partition
> `A = Q ∪ {0}`, `B = F_q^\times \ Q`
> is internal.

This is stronger than bare existence because it gives a canonical family-uniform partition.

If correct, a successful solve would already be about `0.85` to `0.9` of a short paper: the exact title theorem is already visible, and the remaining packaging is mostly proof polishing, novelty verification, and a brief comparison with the regular-graph literature.

# definitions

- `P(q)` means the Paley graph on `F_q` for prime powers `q ≡ 1 (mod 4)`, with `x ~ y` iff `x-y` is a nonzero square.
- Let `Q = {u in F_q^\times : u is a square}` and `N = F_q^\times \ Q`.
- `P(q)` is `(q-1)/2`-regular, so the internal threshold is `(q-1)/4`.
- Internal partition convention used here: a nontrivial vertex partition `V = A ⊔ B` such that every vertex has at least as many neighbors on its own side as across.

Ambiguities / conventions to keep explicit:

- The partition need not be perfectly balanced in size. Here `|A| = (q+1)/2`, `|B| = (q-1)/2`.
- Because `q ≡ 1 (mod 4)`, `-1` is a square, which is used repeatedly when deciding whether `0` is adjacent to a given nonzero vertex.
- The argument uses standard Paley common-neighbor counts, equivalently the standard quadratic-character sum `sum_y chi(y(y-x)) = -1` for `x != 0`.

# approach_A

Structural / invariant approach: use the standard strongly regular structure of Paley graphs.

1. Put `A = Q ∪ {0}` and `B = N`.
2. Vertex `0` is adjacent exactly to the vertices of `Q`, so `0` has all `(q-1)/2` neighbors inside `A`.
3. If `x in Q`, then `0 ~ x`. Common neighbors of `0` and `x` are exactly the vertices `y in Q` with `y-x in Q`. In a Paley graph, adjacent pairs have `lambda = (q-5)/4` common neighbors. Hence `x` has `(q-5)/4` neighbors in `Q`, plus the neighbor `0`, for a total of `(q-1)/4` neighbors in `A`.
4. If `x in N`, then `0` is not adjacent to `x`. Common neighbors of `0` and `x` are again the vertices `y in Q` with `y-x in Q`, and nonadjacent pairs in a Paley graph have `mu = (q-1)/4` common neighbors. Since `0` is not adjacent to `x`, this means `x` has exactly `(q-1)/4` neighbors in `A`, hence also `(q-1)/4` neighbors in `B`.
5. Therefore every vertex has at least `(q-1)/4` same-side neighbors, so the partition is internal.

This route is short, but it leans on importing the full strongly regular parameter package.

# approach_B

Construction / direct-count approach: verify the same partition by quadratic-character counts.

Let `chi` be the quadratic character on `F_q`, extended by `chi(0) = 0`.

For `x != 0`, define

`N(x) = |{y in Q : y-x in Q}|`.

Then

`4 N(x) = sum_{y notin {0,x}} (1 + chi(y))(1 + chi(y-x))`.

Expanding gives

`4 N(x) = (q-2) + sum_{y notin {0,x}} chi(y) + sum_{y notin {0,x}} chi(y-x) + sum_y chi(y(y-x))`.

Now:

- `sum_{y notin {0,x}} chi(y) = -chi(x)`,
- `sum_{y notin {0,x}} chi(y-x) = -chi(-x) = -chi(x)` because `chi(-1) = 1`,
- `sum_y chi(y(y-x)) = -1` for every `x != 0`.

So

`4 N(x) = q - 3 - 2 chi(x)`.

Hence

- if `x in Q`, then `chi(x) = 1` and `N(x) = (q-5)/4`,
- if `x in N`, then `chi(x) = -1` and `N(x) = (q-1)/4`.

Interpretation:

- for `x in Q`, the neighbors of `x` inside `Q` are exactly `N(x) = (q-5)/4`, and `0` is also adjacent to `x`, so `x` has `(q-1)/4` neighbors in `A`,
- for `x in N`, the vertices of `A` adjacent to `x` are exactly those counted by `N(x)`, and `0` is not adjacent to `x`, so `x` has `(q-1)/4` neighbors in `A`.

This gives the same conclusion as Approach A, but in a more self-contained way.

# lemma_graph

Small proof skeleton:

1. `Paley regularity`: every vertex has degree `(q-1)/2`.
2. `Canonical split`: define `A = Q ∪ {0}`, `B = N`.
3. `Zero vertex lemma`: `0` has all neighbors in `A`.
4. `Residue count lemma`: for `x in Q`, `|Q ∩ (x+Q)| = (q-5)/4`.
5. `Nonresidue count lemma`: for `x in N`, `|Q ∩ (x+Q)| = (q-1)/4`.
6. `Threshold check`: convert the previous two counts into same-side degree counts and compare with `(q-1)/4`.
7. `Conclusion`: `A | B` is an internal partition for every Paley graph.

If a paper packet is needed, the cleanest theorem slice is actually stronger:

> Every Paley graph has a canonical internal partition in which every nonzero vertex has exactly half of its neighbors on each side.

# chosen_plan

Best path: use Approach B as the main proof because it is explicit and family-uniform, then cite Approach A as a structural sanity check.

Reason for choosing it:

- it does not need any search,
- it produces an explicit partition rather than a bare existence argument,
- it gives a stronger local statement for all nonzero vertices,
- it is already close to theorem-proof-corollary paper form.

What extra structure makes this paper-shaped if the main claim closes:

- emphasize canonicity of the partition,
- isolate the exact local count statement for nonzero vertices,
- add one remark that the side sizes differ by one but all nonzero vertices are perfectly balanced,
- add one short comparison with the general internal-partition problem for regular graphs.

# self_checks

- Check after statement lock: the theorem is family-wide, not just an instance claim.
- Check after definitions: the internal threshold really is `(q-1)/4`.
- Check after the candidate construction: both sides are nonempty for the smallest case `q = 5`.
- Check after the count formula: substituting `chi(x) = 1` and `chi(x) = -1` gives integers `(q-5)/4` and `(q-1)/4`.
- Check after the final threshold comparison: vertices in `N` are exactly balanced; vertices in `Q` are exactly balanced once the neighbor `0` is included; vertex `0` is strictly internal.
- Check on scope: this is a candidate full-family proof, so classification should stay `CANDIDATE` until verify and Lean decisions happen.

# code_used

No code used. The solve closed at the reasoning stage with an explicit partition and exact local counts.

# result

Candidate full-family solve:

Let `Q` be the nonzero quadratic residues in `F_q`, and let `N` be the nonresidues. Set

`A = Q ∪ {0}`, `B = N`.

Then:

- `0` has degree `(q-1)/2`, and every one of those neighbors lies in `Q`, hence in `A`.
- If `x in Q`, then `0 ~ x` and
  `|Q ∩ (x+Q)| = (q-5)/4`.
  Therefore `x` has `(q-5)/4 + 1 = (q-1)/4` neighbors in `A`, namely the `Q`-neighbors plus `0`.
- If `x in N`, then `0` is not adjacent to `x` and
  `|Q ∩ (x+Q)| = (q-1)/4`.
  Therefore `x` has exactly `(q-1)/4` neighbors in `A`, so also exactly `(q-1)/4` neighbors in `B`.

Since every vertex has at least `(q-1)/4` same-side neighbors, this is an internal partition.

Immediate stronger statement:

- every nonzero vertex is exactly balanced across the partition,
- only the vertex `0` is strictly biased toward its own side.

What scales:

- the argument scales cleanly across the full Paley family because it depends only on the order-2 cyclotomic counts and the fact that `-1` is a square.

What does not obviously scale:

- the exact partition rule is tied to the Paley residue/nonresidue decomposition,
- the proof uses the very specific two-class quadratic-character structure, not a generic pseudorandom-graph argument.

Suggested theorem slice if the full claim needs to be packaged more tightly:

> In every Paley graph `P(q)`, the canonical quadratic-character partition `Q ∪ {0} | N` is internal, and every nonzero vertex has exactly `(q-1)/4` neighbors on each side.

Next parameter shifts that would help most:

- test whether the same residue-class split works in Peisert graphs,
- test generalized Paley graphs where the connection set is a different multiplicative subgroup.

Paper-shape assessment at this stage:

- if the proof and novelty check hold, this is much closer to a paper-shaped family theorem than to a thin one-instance result,
- if the construction is folklore, the current package could collapse to rediscovery despite being mathematically clean.

# family_affinity

Strong. The proof is not an isolated witness; it is a canonical family-uniform construction defined directly from the Paley field model.

# generalization_signal

Medium. The residue/nonresidue partition suggests a reusable template for other order-2 cyclotomic Cayley graphs, but the exact count identity is distinctly Paley-specific. The strongest immediate signal is not a broad campaign theorem, but a nearby family comparison result.

# proof_template_reuse

Reusable template:

1. choose the canonical multiplicative-coset partition suggested by the Cayley connection set,
2. reduce same-side degree counts to cyclotomic intersection numbers,
3. convert those counts into an internal-threshold check.

This looks reusable for close relatives of Paley graphs, but not yet for arbitrary regular Cayley graphs.

# candidate_theorem_slice

Candidate theorem slice:

> For every prime power `q ≡ 1 (mod 4)`, the partition `F_q = (Q ∪ {0}) ⊔ N` is an internal partition of the Paley graph `P(q)`. Moreover, every nonzero vertex has exactly `(q-1)/4` neighbors in each part.

# smallest_param_shift_to_test

Most informative next shifts:

- Peisert graphs of order `q ≡ 1 (mod 4)`,
- generalized Paley graphs with a connection set of index `2` or another small index.

These would test whether the proof is truly residue-structure driven or only Paley-specific.

# why_this_is_or_is_not_publishable

If correct and novel, this is publishable in the micro-paper lane.

- The exact title theorem is already visible: `Internal Partitions in Paley Graphs`.
- A successful solve here is already about 70-90% of the paper because the problem was curated as a named open family theorem and the proof gives an explicit canonical partition.
- Minimal remaining packaging work:
  background paragraph on internal partitions and Paley graphs,
  one polished proof section,
  one novelty/prior-art check on whether this partition was already observed,
  one short concluding remark about nearby Paley-type families.

If the literature already contains this partition, then the mathematical result is real but the package is too thin for frontier publication and would become a rediscovery rather than a paper.

# paper_shape_support

What makes the result paper-shaped rather than just a witness:

- the claim is family-wide, not a single instance,
- the partition is explicit and canonical,
- the proof naturally yields a stronger local balancing statement,
- one immediate corollary is available: every Paley graph has an internal partition with side sizes differing by exactly one,
- the narrative is already tight because the source literature posed exactly this family theorem.

# boundary_remark

The partition is not a perfect size bisection: one side is larger by the vertex `0`. But the nonzero vertices are exactly balanced across the cut, so the asymmetry is concentrated entirely at `0`. That is the clean boundary feature of the construction.

# likely_failure_points

- The count identity `sum_y chi(y(y-x)) = -1` should be checked carefully in the exact normalization being used.
- The translation from `|Q ∩ (x+Q)|` to same-side degree counts must keep track of whether `0` is adjacent to `x`.
- The proof uses `chi(-1) = 1`, so the `q ≡ 1 (mod 4)` hypothesis is essential.
- Novelty risk remains nonzero because the construction is very natural and may be folklore even if the 2024 note still posed the problem.

# what_verify_should_check

- Verify the quadratic-character computation line by line, or rederive the same counts from standard Paley strongly regular parameters.
- Check the smallest case `q = 5` explicitly against the claimed partition.
- Confirm the internal-partition convention used in the 2024 note matches the threshold interpretation here.
- Run a bounded prior-art search for the exact partition `Q ∪ {0} | N` in Paley graphs and for equivalent formulations via common-neighbor counts.
- If novelty holds, check whether the stronger balanced-nonzero-vertices statement deserves to be elevated into the theorem statement.

# verify_rediscovery

Bounded PASS 1 result: rediscovery not established.

- Search patterns covered the exact Paley/internal-partition phrasing, the explicit partition `Q ∪ {0} | N`, alternate wording through quadratic residues / nonresidues, the 2024 source itself, theorem / proposition / example checks around that source, and a later-status check.
- The 2024 Bärnkopf-Nagy-Paulovics paper still appears to pose the Paley-family statement as an open problem; within the capped search budget I did not find a later paper, preprint, or note explicitly settling the exact theorem or exhibiting the canonical partition.
- I did not find an earlier theorem / proposition / example in the cited 2024 source that already implies the Paley claim outright.
- Residual folklore risk remains because the argument is short and natural, especially once rewritten through common-neighbor counts, so publication audit should still do one focused positioning pass before Lean.

Conservative conclusion: keep the run non-rediscovery, but treat folklore risk as the main remaining novelty hazard.

# publication_prior_art_audit

Bounded publication audit run on April 13, 2026.

Passes executed:

- exact statement search on `Paley graph` plus `internal partition`,
- alternate notation search on the canonical residue cut `Q ∪ {0} | N` and on the conference-graph phrasing `N[v] | (V \\ N[v])`,
- canonical source check on the Springer version of Bärnkopf-Nagy-Paulovics (published March 23, 2024),
- one outside-status pass for 2025-2026 paper / preprint hits and nearby Ban-Linial-level internal-partition metadata.

Canonical-source findings:

- The source defines `N[v]` in its preliminaries.
- In Section 4 it defines Paley graphs and states only the bounded computational claim that every Paley graph of order less than `500` has an internal partition.
- It then states `Problem 7: Prove that every Paley graph has an internal partition.`
- In the source page I did not find a theorem, proposition, example, corollary, observation, or sufficient-condition statement already implying the full Paley-family claim.
- I also did not find the word `conference` in the source page, so the present conference-graph reframing is not visibly supplied by the canonical source itself.

Outside-status findings:

- Within the bounded web pass, I did not find a later paper or preprint explicitly settling the exact Paley theorem, the residue/nonresidue partition `Q ∪ {0} | N`, or the broader conference-graph closed-neighborhood statement.
- The Springer page reports `3` citations as of April 13, 2026, so the follow-up surface still looks small.
- This still does not positively clear folklore risk, because the current argument collapses to a very short strongly-regular / conference-graph parameter check once the right abstraction is named.

Conservative verdict:

- `REDISCOVERY` is not established by the bounded audit.
- The remaining load-bearing risk is publication positioning, not mathematical shape.
- Honest label: real theorem slice, but novelty-fragile.

# publication_statement_faithfulness

If the packet proof is correct, it does answer the selected Paley problem. The issue is not drift away from the target; the issue is that the proof appears to establish a cleaner structural theorem than the Paley-only wording advertises.

What the proof actually uses is only:

- a graph with parameters `k = (n-1)/2`, `λ = (n-5)/4`, `μ = (n-1)/4`,
- one chosen vertex `v`,
- the closed-neighborhood partition `A = N[v]`, `B = V \\ N[v]`.

So the strongest faithful theorem slice is:

> In every conference graph `G` and for every vertex `v`, the partition `N[v] | (V(G) \\ N[v])` is internal. Consequently every Paley graph has an internal partition.

That is a strengthening, not a faithfulness failure. The selected Paley theorem remains a direct corollary, but the honest publication-facing statement should be the conference-graph slice, not only the Paley instance.

# publication_theorem_worthiness

Answers to the required theorem-worthiness questions:

- Is the strongest honest claim stronger than “here is an example”? Yes. It is a family-wide theorem slice, not an isolated witness.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Yes. The visible title theorem is the conference-graph closed-neighborhood statement, with the Paley problem answered as a corollary.
- Is the proof structural or merely instance-specific? Structural. The proof uses only the conference-graph parameter identities and does not depend on hand-picked small cases.
- Would this survive a referee asking “what is the theorem?” Yes, but only if the theorem is stated at the conference-graph level. As a Paley-only note, the theorem would look underframed because the proof barely uses Paley-specific structure.
- Is the claim still too dependent on small cases? No. The `<500` computations in the source are only sanity context now; the packet proof is family-uniform.

The downgrade from curation is therefore not theorem weakness. It is that the true theorem appears simpler, broader, and more folklore-sensitive than the original Paley branding suggested.

# publication_publishability

Current publication judgment: not `PAPER_READY` yet.

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? Probably yes, but only if the conference-graph positioning survives prior-art checking.
- What percentage of the paper would one solve already provide? About `0.68`.
- Is there a real title theorem here? Yes, but it is the conference-graph theorem, not merely the selected Paley sentence.
- Is the remaining gap genuinely small, or did the candidate only look attractive before audit? The mathematical gap is small; the publication gap is still real because novelty / attribution may decide the entire packet.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. If prior art turns up, retire it as `REDISCOVERY`; do not broaden into a strongly-regular-graph campaign.
- Would Lean directly seal the packet, or would it only be optional polish? Lean would seal the mathematics once the theorem slice is frozen, but right now it is optional relative to the remaining novelty gate.

# publication_packet_audit

Packet shape after audit:

- likely title theorem: a closed-neighborhood internal-partition theorem for conference graphs,
- immediate corollary: every Paley graph has an internal partition,
- proof type: one short structural parameter argument,
- main risk: novelty collapse, not correctness collapse,
- packet quality: strong mathematically, fragile editorially.

So the packet is not instance-only, but it is also not ready for automatic stop. Its value depends on whether the short conference-graph observation is still absent from print.

# micro_paper_audit

Micro-paper verdict: conditional, skeptical pass.

- Would one solve already constitute most of a publishable note? Yes, but only at roughly `0.68`, not `0.80+`.
- Why lower than before? Because the packet now looks like a very short conference-graph note whose publication fate turns on prior-art clearance rather than additional mathematics.
- Did the candidate only look attractive before audit? Partly yes. The Paley branding made the result look more bespoke than it now appears.
- Should it stay active if it is not paper-ready today? Only as a tightly bounded one-theorem packet. If prior art appears, move it aside immediately rather than inflating it into a broader program.

This remains micro-paper-lane eligible, but only under a strict no-expansion rule.

# strongest_honest_claim

The current packet appears to establish the structural statement that in any conference graph `G` and for any vertex `v`, the partition `N[v] | (V(G) \\ N[v])` is internal. Hence every Paley graph `P(q)` admits an internal partition. This is stronger than an example and strong enough to serve as a title-theorem slice, but the bounded audit does not yet justify claiming that this conference-graph observation is frontier-novel.

# paper_title_hint

Closed-Neighborhood Internal Partitions in Conference Graphs

# next_action

Do one last source-level prior-art check targeted at the conference-graph / strongly-regular / Ban-Linial vicinity of the theorem. If that remains clear, freeze the conference-graph theorem slice exactly as stated here and send this packet to Lean. If a prior source is found, mark the packet `REDISCOVERY` and retire it rather than broadening scope.

# verify_faithfulness

PASS 2 result: faithful to the intended statement.

- The solver’s claimed theorem is still the intended family-wide Paley statement, not a weaker proxy, an instance-only slice, or a changed definition.
- The stronger claim that `A = Q ∪ {0}`, `B = N` is a canonical internal partition is a genuine strengthening of the intended existence theorem, not a drift away from it.
- The internal-partition threshold is used correctly: in the `(q-1)/2`-regular Paley graph, the same-side requirement is at least `(q-1)/4`.
- I found no quantifier drift, wrong-theorem drift, or mismatch between the prose claim and the actual proof target.
- Scope correction only: the proof packet naturally establishes a stronger conference-graph theorem with the Paley claim as a corollary, but that is a strengthening, not a faithfulness failure.

# verify_proof

PASS 3 result: no incorrect step found in the common-neighbor / strongly-regular proof.

- The clean verification route is `approach_A`, not the character-sum expansion. For `0`, all neighbors lie in `Q`, so `0` is strictly internal.
- For `x in Q`, the proof uses that `0 ~ x` and that adjacent vertices in a Paley graph have exactly `lambda = (q-5)/4` common neighbors. Those common neighbors are exactly the vertices of `Q` adjacent to `x`, so adding `0` gives same-side degree `(q-1)/4`.
- For `x in N`, the proof uses that `0` is not adjacent to `x` and that nonadjacent pairs have exactly `mu = (q-1)/4` common neighbors. Those are exactly the neighbors of `x` lying in `Q`, hence the cross-side degree into `A`; the same-side degree in `B` is also `(q-1)/4`.
- This establishes the internal inequality for every vertex. I did not find a hidden assumption beyond the standard Paley/common-neighbor parameters and the hypothesis `q ≡ 1 (mod 4)`.
- The most delicate part of the original packet is the character-sum normalization in `approach_B`. I did not find an error there, but it is unnecessary for verification because the common-neighbor argument already closes the theorem more robustly.

First incorrect step found: none.

# verify_adversarial

PASS 4 result: no break found.

- I checked the smallest sanity case `q = 5` explicitly; the claimed partition is internal.
- I also ran a direct local-neighbor-count checker for prime Paley graphs at `q = 5, 13, 17, 29`, and the canonical partition passed in every case tested.
- These computations are only sanity checks. They do not verify prime-power orders such as `9, 25, 49`, and they are not needed for the proof because the argument is symbolic and uses only the standard common-neighbor parameters.
- I did not find a computational contradiction, a broken witness, or a threshold mismatch.

# verify_theorem_worthiness

PASS 5 result: mathematically strong, publication-facing status still conditional on positioning.

- Exactness: the packet now contains a candidate full-family theorem, not an instance-only witness. It should still remain `CANDIDATE`, not `EXACT`, because Lean is not complete.
- Novelty: bounded PASS 1 did not establish rediscovery, but the theorem may be close to a generic conference-graph closed-neighborhood observation, so novelty / framing remains load-bearing.
- Reproducibility: high. The partition is explicit, the verification condition is local, and the common-neighbor proof is short.
- Lean readiness: not yet. The claim is precise enough to formalize, but Lean is not the shortest remaining path because publication audit still needs to clear the folklore / theorem-positioning issue.
- Paper leverage: if the claim is novel in the relevant sense, one correct solve already provides most of a publishable note.

Direct answers required by this stage:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? Yes, if the Paley or conference-graph positioning survives publication audit.
- What percentage of the paper would one solve already provide? About `0.75`.
- What title theorem is actually visible? The honest visible theorem is the conference-graph statement: `In any conference graph G and any vertex v, the partition N[v] | (V(G) \\ N[v]) is internal`, with the Paley theorem as a corollary.
- What part of the argument scales? The proof appears to use only the conference-graph common-neighbor counts attached to a closed neighborhood of a vertex.
- What part clearly does not? The present packet does not yet justify a broader publication claim beyond the Paley slice, and the literature status of the broader conference-graph framing has not been cleared here.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? No. The best honest status at verify is `SLICE_CANDIDATE`.

# verify_verdict

- `verify_verdict = CANDIDATE`
- `classification = CANDIDATE`
- `publication_status = SLICE_CANDIDATE`
- `lean_ready = false`
- `lean_packet_seal = false`
- `next_action = publication_audit on novelty / folklore / conference-graph positioning; do not Lean until that clears`

# minimal_repair_if_any

Tiny conservative repair only:

- Make the common-neighbor / strongly-regular proof the primary verified argument.
- Retitle the honest theorem slice at the conference-graph level, with the Paley statement presented as the corollary answering the selected problem.
- Keep the quadratic-character computation as an optional remark or appendix-level rederivation, since it is correct-looking but less robust than the short parameter proof.
