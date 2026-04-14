# statement_lock

- Active slug: `r3-c12-even-cycle-ramsey`.
- Active title: `Determine the exact value of R(C12, C12, C12)`.
- Exact intended theorem/disproof for this solve pass:
  - either prove `R(C12, C12, C12) = 24`, i.e. every 3-coloring of `K24` has a monochromatic `C12`;
  - or disprove that target by giving a 3-coloring of `K24` with no monochromatic `C12`, which would imply `R(C12, C12, C12) >= 25`.
- Ramsey convention used here: `R(C12, C12, C12)` is the least `N` such that every 3-edge-coloring of `K_N` contains a monochromatic simple cycle on 12 distinct vertices.
- Title theorem if the upper-bound path closes: `The Exact Value of R(C12, C12, C12)`.

# definitions

- `C12` means a simple cycle with exactly 12 distinct vertices.
- A "counterexample on 24 vertices" means a 3-edge-coloring of `K24` with no monochromatic `C12`.
- A "balanced `K4` blow-up" means a partition of `V(K24)` into four 6-vertex parts, with all edges between each pair of parts monochromatic and the reduced graph on the four parts equal to the proper 3-edge-coloring of `K4` whose color classes are the three perfect matchings.
- The only exact local source packet available in-scope is the working packet; the exact published 23-vertex lower-bound witness is not present in this artifact directory.
- Ambiguity / missing definition that matters:
  - the working packet says the standard `4n`-type lower-bound template motivates 24, but it does not include the explicit 23-vertex construction;
  - without that exact witness, any "add one vertex to the known extremal example" argument stays heuristic unless it can be phrased independently of the missing details.

# approach_A

Structural / invariant route: force the putative 24-vertex counterexample into a near-extremal template, then show that the template already creates a monochromatic `C12`.

Core observation:

1. In the proper 3-edge-coloring of `K4`, each color class is a perfect matching.
2. If each of the four blown-up parts has size 6, then for each color there is a monochromatic complete bipartite `K_{6,6}` between one matched pair of parts.
3. `K_{6,6}` contains a 12-cycle by alternating between the two sides.

So the naive balanced `4 x 6` version of the conjectural `4n` lower-bound picture cannot be a counterexample on 24 vertices.

What this route would need for the full theorem:

- a stability statement saying that every 24-vertex coloring with no monochromatic `C12` must reduce, after coarse partitioning, to the standard 4-part lower-bound geometry;
- or a weaker reduction saying that some monochromatic `K_{6,6}` pair is unavoidable in any `K24` counterexample.

Self-check after Approach A:

- The `K_{6,6} -> C12` step is rigorous.
- The deduction only kills one natural template family; it does not yet settle arbitrary 3-colorings of `K24`.
- This is theorem-facing, but not a proof of `R(C12, C12, C12) = 24`.

# approach_B

Construction / extremal / contradiction route: try to extend the presumed 23-vertex lower-bound mechanism to 24 vertices and see where it necessarily breaks.

Heuristic picture:

1. The candidate packet points to a standard `4n`-type lower-bound template for the lower bound just below 24.
2. Passing from the sharp lower-bound size to 24 should force some side of size 5 to become size 6.
3. Once a monochromatic complete bipartite pair reaches side sizes `(6,6)`, a monochromatic `C12` appears immediately.

This makes the upper-bound direction plausible: the extra vertex should be exactly where the old template loses control.

Blocker:

- the exact 23-vertex template is not present in the allowed local packet, so I cannot rigorously prove that every 24th-vertex extension creates a monochromatic `K_{6,6}` or an equivalent `C12`-forcing configuration;
- without that explicit template, the construction path is suggestive rather than exact.

Self-check after Approach B:

- Good micro-paper intuition: 24 looks like the first place where the extremal template should become cycle-forcing.
- Bad rigor status: the missing explicit 23-vertex witness prevents a clean contradiction argument.

# lemma_graph

- Lemma 1: `K_{6,6}` contains a copy of `C12`.
- Lemma 2: In a balanced 4-part blow-up of the proper 3-coloring of `K4` with part sizes `(6,6,6,6)`, each color contains a monochromatic `K_{6,6}`.
- Lemma 3: Therefore that balanced blow-up family cannot witness `R(C12, C12, C12) >= 25`.
- Missing Lemma 4: Every 24-vertex counterexample must admit a reduction to that family, or at least must contain an unavoidable monochromatic `K_{6,6}`-type pair.
- Missing Lemma 5: A one-vertex extension of the sharp 23-vertex lower-bound witness necessarily creates the missing Lemma 4 configuration.

# chosen_plan

I chose the structural upper-bound path.

Reason:

- the selection packet is already biased toward `24` as the sharp value;
- the most paper-relevant obstruction I can prove locally is that the naive balanced extremal template already fails on 24;
- the construction path depends on a missing exact 23-vertex witness, so it does not currently support a rigorous disproof.

Attempted rigorous core:

- prove a clean exact slice about the balanced `K4` blow-up family;
- extract the strongest honest inference: any real 24-vertex counterexample must look substantially less naive than the standard balanced lower-bound picture.

Self-check after choosing the plan:

- This is the highest-signal local move that stays reasoning-first and avoids drifting into unjustified brute force.
- It still leaves the main theorem open.

# self_checks

- Statement lock check: the target stayed fixed on the exact `K24` upper bound versus explicit `K24` witness disproof.
- Scope check: I used only the active selection packet and its local working packet, then wrote candidate-local artifacts.
- Rigor check: every proved sentence below is explicitly limited to the balanced blow-up slice.
- Solve-stage check: I do not claim `EXACT`; I do not claim rediscovery; I do not invoke Lean.

# code_used

- No code used.
- Decision: minimal code is not yet justified here.
- Reason: the bottleneck is a missing structural reduction, not witness verification. A generic search at this point would be drift into search-heavy mode without first isolating a sharply justified template family.

# result

Main claim status:

- I did not prove `R(C12, C12, C12) = 24`.
- I did not construct a `K24` counterexample.

Strongest exact result obtained in this pass:

- Any 3-coloring of `K24` that is a balanced 4-part blow-up of the proper 3-edge-coloring of `K4` necessarily contains a monochromatic `C12`.

Proof:

1. Partition the 24 vertices into four parts `V1,V2,V3,V4`, each of size 6.
2. Assume every edge between parts is monochromatic and the reduced graph on `{V1,V2,V3,V4}` is the proper 3-coloring of `K4`.
3. In that reduced graph, each color is a perfect matching on the four parts, so for some color, say red, the red cross-edges include all edges of `V1-V2` and all edges of `V3-V4`.
4. The red graph therefore contains the complete bipartite graph `K_{6,6}` on `V1 union V2`.
5. Alternating between the two 6-vertex sides gives a red `C12`.
6. Hence the coloring is not a counterexample.

Immediate corollary / remark:

- A `K24` counterexample, if it exists, cannot come from the most naive balanced `4n` blow-up template; it must break the standard 4-part geometry in an essential way before verification even starts.

Why the instance matters if the main claim closes:

- If the full upper bound closes, the title theorem is already `The Exact Value of R(C12, C12, C12)`, which is 70-90% of a short paper by the packet's own leverage estimate.
- Minimal remaining packaging would then be a clean proof writeup, a short comparison with the neighboring even-cycle cases, and one table-level corollary recording the exact entry.

Current package assessment:

- The current result is still too thin for the micro-paper lane by itself.
- It is a real obstruction lemma, not yet a paper-shaped exact theorem.

What part of the argument scales:

- The blow-up obstruction scales directly: for `R(C_{2n}, C_{2n}, C_{2n})`, a balanced 4-part blow-up with part size `n` automatically contains a monochromatic `K_{n,n}`, hence a monochromatic `C_{2n}`.

What part does not scale:

- The missing stability step is the hard part; nothing here yet shows that every counterexample must resemble the balanced 4-part template.

What theorem slice is suggested:

- "Balanced 4-part lower-bound templates cannot witness the sharp 3-color even-cycle value at the conjectured threshold."

What one or two next parameter shifts would help most:

- test the analogous obstruction at `C14`, where the same balanced-template argument produces a forced monochromatic `K_{7,7}`;
- recover the explicit 23-vertex `C12` lower-bound witness locally and test whether every one-vertex extension creates a `K_{6,6}`-type obstruction.

Instance-vs-paper status:

- Right now this is still only a supporting slice; it is closer to a paper-shaped claim than a random exact witness, but it is not yet the title theorem.

# family_affinity

- Strong.
- This attempt is genuinely family-anchored: the obstruction comes from the conjectural `R(C_{2n}, C_{2n}, C_{2n}) = 4n` picture and targets the first place where a balanced 4-part blow-up would hit side size `n = 6`.
- If the full claim closes, the family narrative is immediate rather than retrofitted.

# generalization_signal

- Moderate.
- The exact local lemma generalizes cleanly: a balanced 4-part blow-up at the conjectured threshold `4n` fails for every `n` because one color contains `K_{n,n}`, hence `C_{2n}`.
- What does not yet generalize is the stability reduction from an arbitrary coloring to that blow-up family.

# proof_template_reuse

- Reusable template: convert a conjectured lower-bound construction into an upper-bound obstruction by identifying the first parameter where a monochromatic complete bipartite piece reaches the target cycle length.
- This reuse looks strongest for multicolor even-cycle exact problems whose folklore lower bounds come from coarse blow-up constructions.

# candidate_theorem_slice

- Candidate exact slice:
  - In any balanced 4-part blow-up of the proper 3-coloring of `K4` with part size 6, there is a monochromatic `C12`.
- Suggested stronger slice if the missing reduction can be supplied:
  - Any 24-vertex 3-coloring with no monochromatic `C12` must avoid every stability reduction to the standard 4-part `4n` template; equivalently, every such coloring is structurally far from the conjectural extremal geometry.

# smallest_param_shift_to_test

- First shift: `R(C14, C14, C14)` at the balanced threshold 28. The same reduced-graph obstruction becomes `K_{7,7} -> C14`.
- Local structural shift: characterize one-vertex extensions of the sharp 23-vertex `C12` lower-bound witness and see whether each extension forces a monochromatic `K_{6,6}` or an equivalent 12-cycle.

# why_this_is_or_is_not_publishable

- If the main theorem `R(C12, C12, C12) = 24` closes, yes: that would already be about `0.75` of a paper, with low editorial overhead and an immediate table-level consequence.
- The current output is not publishable on its own.
- Reason: the exact slice proved here is too small to stand as the title theorem of a note. It is a useful obstruction lemma, but it does not yet determine the Ramsey number or provide a complete counterexample.

# paper_shape_support

- Extra structure that would make the result paper-shaped if the main claim closes:
  - one stability proposition reducing arbitrary `K24` counterexamples to a narrow family extending the standard lower-bound template;
  - one exact elimination of that remaining family.
- Exact paper title if the solve closes: `The Exact Value of R(C12, C12, C12)`.
- Whether a successful solve would already be 70-90% of a paper: yes, that is still the right estimate.
- Minimal remaining packaging work after a successful close:
  - clean presentation of the extremal obstruction / upper-bound proof;
  - one short comparison paragraph with the smaller even-cycle exact table entries;
  - one corollary fixing the `C12` table entry in the 3-color even-cycle family.
- One immediate corollary if the full theorem closes:
  - the exact three-color even-cycle table gains the entry `R(C12, C12, C12) = 24`.
- Current thinness verdict:
  - the present slice is still too thin for the micro-paper lane.

# boundary_remark

- Boundary remark: the balanced threshold itself is already cycle-forcing for the naive `4n` blow-up mechanism. So if `R(C12, C12, C12)` is larger than 24, the counterexample cannot be a straightforward balanced extrapolation of the standard extremal picture.

# likely_failure_points

- The main unresolved point is the missing stability reduction from arbitrary 3-colorings of `K24` to a coarse 4-part template.
- The exact sharp 23-vertex lower-bound construction is not present in the allowed local packet, so the "add one vertex" contradiction remains incomplete.
- A real 24-vertex counterexample, if it exists, may be highly asymmetric and not visibly related to the naive blow-up model.
- Because solve is web-disabled and the working packet is intentionally thin, I cannot safely assert any stronger family theorem than the explicit slice above.

# what_verify_should_check

- Verify whether the exact 23-vertex lower-bound construction for the `C12` case is known explicitly in the cited survey references and whether its one-vertex extensions have already been analyzed.
- Verify whether the balanced-blow-up obstruction lemma is folklore / implicit in the even-cycle Ramsey literature or worth keeping only as an internal proof hint.
- Verify whether any published result after the survey already settles `R(C12, C12, C12)` exactly.
- If the manager wants a next solve pass, supply the explicit 23-vertex witness or a more detailed local dossier for the lower-bound template; that is the shortest path to converting this obstruction into a real theorem attempt.
