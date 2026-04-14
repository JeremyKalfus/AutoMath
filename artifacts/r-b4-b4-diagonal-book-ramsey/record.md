# statement_lock

We lock the intended theorem as follows, subject to the standard book-graph indexing used in the active packet:

**Candidate title theorem.** `R(B4, B4) = 18`, where `B4` is the 4-page book graph, i.e. 4 triangles sharing a common spine edge.

Equivalent red/blue formulation:

- a red `B4` is a red edge whose red common neighborhood has size at least `4`
- a blue `B4` is a blue edge whose blue common neighborhood has size at least `4`

So a coloring of `K_17` avoids monochromatic `B4` exactly when every monochromatic edge has same-color codegree at most `3`.

This solve attempt therefore targets:

1. an explicit `K_17` coloring with monochromatic codegree at most `3` in both colors, and
2. combination with the packet lemma `R(B4,B4) <= 18`.

If both hold under the same notation, the exact value is forced to be `18`.

# definitions

- `B4`: the graph of 4 triangles sharing one common edge.
- For a graph `G`, an edge `uv` supports a copy of `B4` iff `|N_G(u) ∩ N_G(v)| >= 4`.
- Let `Q = {1, 2, 4, 8, 9, 13, 15, 16}` be the nonzero quadratic residues mod `17`.
- Define a red graph `G` on vertex set `Z/17Z` by declaring `xy` red iff `x-y in Q`; otherwise blue.

Ambiguities and load-bearing conventions:

- The packet uses standard language "4-page book graph `B4`"; this attempt assumes the usual indexing by number of pages.
- The exact closure relies on the packet claim `17 <= R(B4,B4) <= 18`, especially the upper bound `<= 18`.
- A major verification point is whether the source theorem and this packet use exactly the same `B_n` indexing convention.

# approach_A

Structural / invariant route:

1. Translate the book condition into a same-color codegree condition.
2. Look for a nearly symmetric `17`-vertex coloring where every monochromatic edge has codegree exactly `3`.
3. Since the open interval is only one step wide, any such `K_17` witness immediately proves `R(B4,B4) = 18` once the imported upper bound is trusted.

Why this route is natural:

- `17 = 4*4 + 1`, the exceptional arithmetic size in the packet.
- A balanced self-complementary object on `17` vertices would fit the diagonal nature of the problem.
- The parameters one wants are exactly the Paley / strongly-regular pattern `(17, 8, 3, 4)`, because `lambda = 3` is the threshold just below a `B4`.

Self-check after Approach A:

- This route is theorem-shaped, not just search-shaped.
- It matches the packet's "short solve-to-publication distance" criterion.
- The main risk is not mathematical complexity but notation / prior-art mismatch.

# approach_B

Construction / extremal route:

1. Use the explicit quadratic-residue coloring on `Z/17Z`.
2. For a red edge, affine normalization should reduce the common-neighbor count to the fixed pair `(0,1)`.
3. Compute `Q ∩ (Q+1)` explicitly; if its size is `3`, then every red edge lies in exactly `3` red triangles.
4. Use a nonresidue multiplier to swap red and blue, proving the same statement for blue edges.

Why this is preferable to an `18`-vertex contradiction proof:

- It is explicit, compact, and certificate-friendly.
- It produces the lower-bound witness in a single page.
- It preserves a clean micro-paper title theorem if the imported upper bound is sound.

Self-check after Approach B:

- This is the best path because it can settle the case with a short exact argument.
- It uses no heavy search.
- It leaves one clean verification artifact: the explicit residue coloring on `17` vertices.

# lemma_graph

Proof skeleton:

1. Packet lemma: `R(B4,B4) <= 18`.
2. Construction lemma: color `K_17` by quadratic residues mod `17`.
3. Edge-normalization lemma: every red edge is affine-equivalent to `(0,1)`.
4. Count lemma: `Q ∩ (Q+1) = {2, 9, 16}`, so each red edge has exactly `3` red common neighbors.
5. Complement-symmetry lemma: multiplication by a fixed nonresidue swaps residues and nonresidues, so the blue graph is isomorphic to the red graph.
6. Therefore every blue edge also has exactly `3` blue common neighbors.
7. Hence the coloring of `K_17` contains no monochromatic `B4`.
8. Therefore `R(B4,B4) >= 18`.
9. Combine with step 1 to get the candidate exact value `R(B4,B4) = 18`.

Self-check after lemma graph:

- The skeleton is short enough to be the core of a micro-paper.
- The only imported ingredient is the upper bound.
- The lower-bound side is fully explicit and independently checkable.

# chosen_plan

Chosen path: Approach B.

Concrete plan:

1. Prove the residue-coloring lower bound cleanly.
2. Run a tiny witness check to confirm the monochromatic codegree bound numerically.
3. Record the exact candidate theorem and isolate the verification risks.

Why this is the best path:

- It is exact, short, and paper-shaped.
- If correct, the successful solve is already about `85%` to `90%` of a short paper.
- Minimal remaining packaging work would be:
  - cite the imported upper bound precisely
  - present the `17`-vertex Paley witness as the lower bound
  - add a short paragraph explaining why this closes the first one-step diagonal book gap in the packet's family line

# self_checks

Current self-check log:

- Statement lock check: the solve target is exact and title-theorem shaped.
- Definition check: the entire attempt hinges on the standard equivalence between `B4` and same-color codegree `>= 4`.
- Strategy check: the solve does not drift into search-heavy or campaign-building work.
- Risk check: the biggest failure mode is that the candidate packet may have a notation or already-known-construction mismatch.
- Witness check: a bounded script on the explicit residue coloring reports `max_red_common = 3`, `max_blue_common = 3`, and no monochromatic edge with same-color codegree `>= 4`.

# code_used

Minimal code used: a tiny local verification script checked the explicit `Z_17` residue coloring and confirmed that the maximum same-color common-neighbor count is `3` in both colors. This was witness verification only, not search.

# result

Provisional exact candidate:

Let the vertices be `0,1,...,16` modulo `17`, and color `xy` red when `x-y` is a nonzero square modulo `17`, blue otherwise.

The residue set is

`Q = {1, 2, 4, 8, 9, 13, 15, 16}`.

For the red edge `(0,1)`, common red neighbors are the `z` such that both `z` and `z-1` lie in `Q`. Since

`Q+1 = {0, 2, 3, 5, 9, 10, 14, 16}`,

we get

`Q ∩ (Q+1) = {2, 9, 16}`,

so `(0,1)` has exactly `3` red common neighbors.

Now let `uv` be any red edge. Then `d = v-u in Q`, so multiplication by `d^{-1}` and translation by `-u` give an affine automorphism sending `u,v` to `0,1` and preserving the red graph. Therefore every red edge has exactly `3` red common neighbors, so there is no red `B4`.

Because `17 ≡ 1 (mod 4)`, `-1` is a square mod `17`, so the coloring is undirected. Also, multiplication by any fixed nonresidue swaps residues and nonresidues, giving an isomorphism between the red and blue graphs. Hence every blue edge also has exactly `3` blue common neighbors, so there is no blue `B4`.

Therefore this construction gives a `B4`-free red/blue coloring of `K_17`, hence

`R(B4,B4) >= 18`.

Combining with the packet's imported upper bound `R(B4,B4) <= 18`, the candidate exact conclusion is

`R(B4,B4) = 18`.

Immediate corollary / boundary remark if this closes:

- the exact title theorem is `R(B4,B4) = 18`
- the minimal remaining packaging is a short proof note plus verification of notation and novelty
- this is not merely "some exact witness"; it is an exact family closure at a one-step frontier

# family_affinity

This candidate is tightly aligned with the diagonal book Ramsey family. If the packet's upper bound is sound under the same indexing, then the solve is already around `0.86` to `0.90` of a short paper: the title theorem is exact, the family anchor is strong, and the remaining work is mostly verification and packaging rather than new mathematics.

# generalization_signal

The scalable part of the argument is the Paley-template lower bound:

- if `q = 4n+1` is a prime power with `q ≡ 1 (mod 4)`, the Paley graph on `q` vertices has parameters `(q, 2n, n-1, n)`
- hence every edge in either color lies in exactly `n-1` monochromatic triangles
- therefore the Paley coloring on `q` vertices avoids monochromatic `B_n`
- so `R(B_n, B_n) >= 4n+2` whenever such a Paley graph exists

What scales:

- affine normalization
- residue / nonresidue symmetry
- same-color codegree counting

What does not scale automatically:

- the exact closure, because that still needs a matching upper bound `R(B_n,B_n) <= 4n+2`
- the micro-paper claim, because for larger `n` the result might be only a lower bound, not a full exact theorem

# proof_template_reuse

Reusable proof template:

1. translate a diagonal book-Ramsey instance into same-color codegree bounds
2. choose a self-complementary arithmetic coloring
3. normalize edges by affine symmetries
4. count the relevant residue intersection once
5. transfer the count to the other color by a nonresidue multiplier

This template is compact and well suited to exact one-step diagonal cases where the upper bound is already available from prior work.

# candidate_theorem_slice

Smallest theorem slice suggested by the current argument:

**Slice.** The Paley coloring on `17` vertices is monochromatic-`B4`-free; equivalently, every monochromatic edge in that coloring lies in exactly `3` monochromatic triangles.

This slice is independently checkable and is the decisive new lower-bound certificate needed for the exact closure.

# smallest_param_shift_to_test

Most useful next parameter shifts if this exact closure survives verification:

1. test the same Paley-template statement at `q = 13` (`n = 3`) as a sanity check against smaller diagonal book cases
2. test `q = 25` (`n = 6`) to see whether the same lower-bound template gives a clean arithmetic family note, even if exact closure there is unavailable

These shifts help separate the genuinely special `n = 4` exact closure from the broader lower-bound mechanism.

# why_this_is_or_is_not_publishable

If verification confirms the packet's upper bound, the notation, and novelty status, then this is publishable in the micro-paper lane.

Why it is paper-shaped:

- the exact title theorem is immediate: `The Exact Value of R(B4, B4)`
- a successful solve is already about `70%` to `90%` of the paper, and here likely near the top of that range
- the family context is already present in the packet
- editorial overhead is low because the lower-bound certificate is explicit and compact

Why caution is still required:

- the result could collapse into rediscovery if the Paley-17 witness is already standard in the cited literature
- the packet may have a notation mismatch, and that would change the meaning of `B4`
- without verification, this is still a solve-stage exact candidate rather than a settled publication packet

Current assessment:

- mathematically strong enough to be more than an instance
- likely already `70%` to `90%` of a short paper if verify confirms the packet assumptions
- minimal remaining packaging work is: one precise citation for the upper bound, one short construction proof, and one novelty / notation check
- not yet safe to call fully publishable until verification checks the source conventions and prior-art status

# paper_shape_support

What extra structure makes this paper-shaped once the main claim closes:

- one explicit theorem statement: `R(B4,B4)=18`
- one short construction section giving the residue coloring on `Z_17`
- one compact proof that every monochromatic edge has codegree `3`
- one sentence importing the known upper bound `<= 18`
- one brief closing remark that this settles the first unresolved small diagonal book case in the packet's family line

Natural corollary / remark:

- the arithmetic Paley witness explains why the `4n+1` exceptional case at `17` is not merely a nuisance exception but an actual lower-bound obstruction at the next integer

# boundary_remark

Boundary of the current result:

- the lower-bound argument is exact and explicit
- the exact-value conclusion depends on an imported upper bound from the packet, not on a new `K_18` contradiction proof
- so the result is very close to a paper-shaped closure, but the exact closure remains conditional on verification of the packet's indexing and citation accuracy

In short:

- the construction part scales
- the exact closure does not scale without matching upper bounds
- the present package is closer to a paper-shaped claim than to a bare instance

# likely_failure_points

1. The packet's `B4` notation could differ from the usual 4-page book convention.
2. The source theorem quoted in the packet might already encode this `17`-vertex arithmetic construction, in which case the exact value may already be known or the open interval may be misstated.
3. The upper bound `R(B4,B4) <= 18` must be checked against the same indexing convention.
4. If the active literature already recognized the Paley-17 witness as the sharp lower bound, then the novelty claim weakens or vanishes.

# what_verify_should_check

1. Confirm from the cited source that `B4` really means a book with `4` pages.
2. Confirm that the source upper bound is exactly `R(B4,B4) <= 18` under that same notation.
3. Check whether the lower-bound construction on `17` vertices is already explicitly present in the cited 2025 or 2026 papers.
4. Verify the residue-coloring certificate independently, preferably with a compact script and then a human-readable witness summary.
5. Decide whether the theorem is frontier-novel or already a rediscovery once the Paley observation is compared to the literature.

# verify_rediscovery

PASS 1 establishes rediscovery.

Bounded web audit used the required patterns: exact instance notation (`R(B4,B4)` / `R(B_4,B_4)`), alternate family notation, the packet's claimed canonical-source citation, and a recent family-context source. The decisive hit was William J. Wesley, *Lower bounds for book Ramsey numbers* (Discrete Mathematics 349(5), 2026), which states that Rousseau and Sheehan proved `R(B_n,B_n) = 4n + 2` whenever `q = 4n + 1` is a prime power. Taking `n = 4` gives `q = 17`, which is prime, so the exact intended statement is already settled: `R(B4,B4) = 18`.

This same recent source also places Paley-graph lower bounds squarely inside the existing book-Ramsey literature, so the `K_17` quadratic-residue witness is not a new frontier certificate. The packet's claim that public sources stop at `17 <= R(B4,B4) <= 18` is therefore not reliable as an openness certificate, and the cited 2025 EJC source anchor appears mismatched.

Conclusion for PASS 1:

- exact intended statement already solved in prior art
- current run must be classified as `REDISCOVERY`
- no frontier publication packet remains on this exact target

# verify_faithfulness

The local solve artifact is mathematically aimed at the correct intended statement: determine the least `n` such that every red/blue coloring of `K_n` contains a monochromatic `B4`, where `B4` is the 4-page book. The equivalence used in the record,

- monochromatic `B4` on an edge `uv` iff that edge has same-color codegree at least `4`,

matches the standard definition and shows no quantifier drift or proxy-statement drift.

The faithfulness failure is not in the lower-bound slice itself; it is in the frontier framing. The record treats the case as open conditional on an imported packet lemma `R(B4,B4) <= 18`, but PASS 1 shows the exact value is already known in the literature. So the theorem statement being pursued is faithful, while the packet's open-problem narrative is not.

# verify_proof

For the lower-bound slice

- the quadratic-residue coloring on `Z/17Z` is well defined,
- `Q ∩ (Q+1) = {2, 9, 16}` is correct,
- affine normalization of red edges is valid,
- nonresidue multiplication swaps the two color classes,
- and the conclusion that every monochromatic edge has same-color codegree exactly `3` is sound.

No incorrect mathematical step was found in that lower-bound argument.

The first unsupported step in the exact-value proof as written is Step 1 of the lemma graph, namely the imported packet assertion `R(B4,B4) <= 18`, because the packet's claimed source anchor is not a trustworthy justification for openness or for the exact frontier status. That step happens to be true, but the correct literature fact is stronger: prior work already gives the exact equality `R(B4,B4) = 18`. So the proof artifact is best understood as a correct rederivation of a known lower-bound witness, not a new exact-proof packet.

# verify_adversarial

Independent adversarial rerun of the witness computation on the stated residue coloring returned:

- `max_red_common = 3`
- `max_blue_common = 3`
- no monochromatic edge with same-color codegree at least `4`
- `Q ∩ (Q+1) = {2, 9, 16}`

This confirms the local construction really is `B4`-free in both colors on `K_17`. No computational contradiction or hidden bad edge was found. The failure mode is rediscovery, not a broken checker or broken witness.

# verify_theorem_worthiness

Exactness:

- the exact theorem `R(B4,B4) = 18` is already present in prior art
- the current run does not produce a new exact frontier result

Novelty:

- no frontier novelty remains on this exact target
- the Paley-17 witness is family-standard rather than a fresh micro-paper closure

Reproducibility:

- high, because the `K_17` witness is explicit and independently checkable

Lean readiness:

- `lean_ready = false`
- `lean_packet_seal = false`
- Lean would formalize a rediscovery, not seal a near-paper frontier packet

Explicit publication answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No. The exact theorem is already known, so Lean would not restore novelty.
- What percentage of the paper would one solve already provide? For frontier publication, effectively `0%`; the mathematical content is already in the literature.
- What title theorem is actually visible? `R(B4,B4) = 18`, but as a preexisting theorem, not as a new note.
- What part of the argument scales? The Paley lower-bound mechanism for `q = 4n + 1` prime powers and its same-color codegree interpretation.
- What part clearly does not? The claim of novelty, the "first unresolved diagonal case" narrative, and any publication packet premised on this exact target still being open.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? Neither; the correct status is `REDISCOVERY`.

Overall worthiness assessment:

- mathematically correct lower-bound witness
- exact theorem already known
- micro-paper lane fails on novelty rather than on correctness

# verify_verdict

`REDISCOVERY`

The exact intended statement `R(B4,B4) = 18` is already settled in prior art. The current artifact correctly rederives a known `K_17` Paley witness but does not shorten the frontier solve-to-publication distance because there is no remaining frontier gap on this instance.

# minimal_repair_if_any

No mathematical repair is needed for the local Paley witness.

The only conservative repair is archival:

- relabel the run as `REDISCOVERY`
- replace the packet's open-status narrative with the prior-art status `R(B4,B4) = 18`
- preserve the explicit `K_17` witness only as known supporting context, not as a new theorem packet
