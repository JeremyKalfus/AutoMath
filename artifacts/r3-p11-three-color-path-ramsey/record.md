# Solve Record: r3-p11-three-color-path-ramsey

## statement_lock
We work with `P11` as the path on `11` vertices. The exact target is:

- upper-bound route: prove every 3-coloring of `K21` contains a monochromatic `P11`, which would establish `R(P11,P11,P11)=21`;
- disproof route: construct a 3-coloring of `K21` with no monochromatic `P11`, which would force `R(P11,P11,P11) >= 22`.

If the upper-bound route closes, the exact title theorem is:

`Every 3-coloring of K21 contains a monochromatic P11; equivalently R(P11,P11,P11)=21.`

Publication relevance check: a clean exact determination here would still be about `70-90%` of a short paper. The remaining packaging would be exposition, comparison with nearby small cases, and presentation of either the forcing argument or the extremal coloring.

## definitions
- Let `G_r`, `G_b`, `G_g` be the red, blue, and green spanning subgraphs of a 3-coloring of `K21`.
- A monochromatic component is `traceable` if it has a Hamiltonian path on all of its vertices.
- A standard `K20` lower-bound template is the 4-block pattern with blocks `A,B,C,D` of size `5` and inter-block colors
  - `AB, CD` red,
  - `AC, BD` blue,
  - `AD, BC` green.
- In the explicit dense version of that template, all intra-block edges are red. Then every vertex lies in a red `K10`, hence in a traceable red 10-vertex component.

Ambiguities / conventions / missing definitions:

- The packet does not specify a required extremal-template normal form, so I treat the 4-block `K20` pattern only as a guide, not as a canonical classification theorem.
- I am not assuming any unpublished mixed Ramsey values such as `R(P10,P11,P11)`.
- Solve runs with web disabled, so novelty and literature closure remain for later verification.

## approach_A
Structural / invariant route.

Assume a counterexample coloring of `K21` with no monochromatic `P11`.

1. The naive edge-count route is too weak. By Erdős-Gallai, a `P11`-free graph on `21` vertices can still have up to `94` edges, while a color class in a 3-coloring of `K21` only needs average size `70`.
2. So the right invariant is not raw density but the shape of large monochromatic components.
3. Any monochromatic component on `11` or more vertices that is traceable already gives the target path. Therefore a counterexample must force every large monochromatic component to be non-traceable in a very specific way.
4. This pushes the search toward a stability statement: any surviving counterexample must differ substantially from the usual 4-block lower-bound geometry, because the usual geometry is built from 10-vertex monochromatic pieces that are themselves traceable.

Self-check after approach A: this is a legitimate structural filter, but not yet an upper-bound proof. The gap is that I do not have a theorem forcing a traceable monochromatic component on `11` vertices in every 3-coloring of `K21`.

## approach_B
Construction / extremal / contradiction route.

Start from the natural `K20` lower-bound picture and ask whether a 21st vertex can be attached without immediately creating a monochromatic `P11`.

Key lemma candidate:

`If H is a 3-colored K20 in which every vertex belongs to some traceable monochromatic 10-vertex component, then every 3-coloring obtained by adding one new vertex x to H contains a monochromatic P11.`

Reason: choose any edge `xv` and let its color be `c`. By hypothesis, `v` lies in a traceable monochromatic `c`-component on `10` vertices. Taking a Hamiltonian path in that component with endpoint `v`, and prepending `x`, yields a monochromatic `P11`.

This immediately rules out the explicit dense 4-block `K20` template described above as a source of a `K21` counterexample.

What this does and does not prove:

- It proves that the most obvious one-vertex extension of the standard lower-bound picture cannot work.
- It does not prove that every `K20` extremal coloring has the saturation property above.
- So it isolates a real obstruction slice, but not the full exact value.

Self-check after approach B: this is rigorous once written carefully, but it only excludes a natural template family. It does not yet settle `R(P11,P11,P11)`.

## lemma_graph
Planned proof skeleton:

1. Lower-bound geometry for `K20`: the familiar 4-block construction explains why `20` is the natural near-extremal size.
2. Saturation lemma: a traceable monochromatic 10-vertex component cannot receive an external edge of the same color without creating a monochromatic `P11`.
3. Template obstruction: the explicit dense 4-block `K20` construction is saturated in exactly that sense, so it cannot extend to a `K21` counterexample.
4. Exact-value gap: any genuine `K21` counterexample must therefore abandon the obvious lower-bound template and use a more delicate non-traceable component structure.
5. Paper-shaped support if the main theorem closes: the obstruction lemma and template-failure remark are the smallest structural add-ons that would naturally sit beside an exact-value theorem.

Self-check after the lemma graph: the slice is coherent and theorem-facing. What is missing is a forcing mechanism showing that every counterexample candidate collapses back to the saturated regime.

## chosen_plan
Best current path:

1. Keep the rigorous saturation lemma as the main solved slice.
2. Use one bounded checker only to test whether nearby block-structured `K21` deformations survive. This is justified now because two reasoning routes have already been tried and the code is serving as a tiny falsifier for the remaining structured gap, not as a replacement for proof.
3. If that bounded experiment also fails to find a structured counterexample, record the honest state as:
   - strong evidence for the conjectural upper bound `21`,
   - one rigorous obstruction slice,
   - but no full proof or full counterexample.

Self-check before code: this remains reasoning-first. The code target is narrow, candidate-local, and interpretable.

## self_checks
- Statement lock check: the exact intended theorem is fixed, and I am not shifting to a weaker witness-only goal.
- Publication check: if `R(P11,P11,P11)=21` were proved here, that would still be roughly `0.74` of a paper, with only low-overhead packaging left.
- Rigor check: the only current theorem-level content is the saturation lemma for traceable 10-vertex components; everything beyond that is still exploratory.
- Search-policy check: no SAT / ILP / CP-SAT / brute force has been used before the two manual approaches above.
- Post-code check: the code result is only being used as an exact structured-family exclusion, not as evidence for the full coloring space.

## code_used
A tiny candidate-local checker was used: [structured_family_check.py](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/r3-p11-three-color-path-ramsey/structured_family_check.py).

What it checked exactly:

- all `19,683` block-constant colorings in the `5+5+5+5+1` family built from the canonical `K20` four-block pattern, with arbitrary monochromatic intra-block colors and arbitrary colors from the singleton block to each of the four size-5 blocks;
- all `324` block-constant colorings in the `6+5+5+5` absorbed-vertex variant with the same canonical inter-block pattern and arbitrary monochromatic intra-block colors.

Observed result:

- `0` survivors in the `5+5+5+5+1` family;
- `0` survivors in the `6+5+5+5` family.

Interpretation: the closest natural one-step deformations of the standard `K20` template do not produce a `K21` counterexample. This is supportive evidence for the upper bound `21`, but it is not a proof beyond those explicitly tested families.

## result
Best honest solve output:

- No exact proof of `R(P11,P11,P11)=21` was obtained.
- No explicit 21-vertex counterexample was obtained.
- A rigorous theorem-facing slice was isolated: any `K20` coloring in which every vertex lies in a traceable monochromatic 10-vertex component is saturated against one-vertex extension.
- The explicit dense `5+5+5+5` lower-bound template is one such saturated configuration, so it cannot extend to a `K21` counterexample.
- The bounded checker then ruled out the nearest block-constant `K21` deformations that preserve that canonical geometry.

Current mathematical state:

- strongest rigorous claim: the saturation lemma and the non-extendability of the explicit dense `K20` template;
- strongest heuristic direction: `R(P11,P11,P11)=21` still looks plausible;
- exact-value status: unresolved in this solve pass.

Paper-shape consequence:

- if the main upper bound later closes, the saturation lemma plus the structured-family exclusion becomes a natural support section and boundary remark;
- standing alone, the current package is still too thin for the micro-paper lane.

## family_affinity
This sits cleanly inside the exact small-parameter three-color path Ramsey family. The strongest current slice is a stability-style obstruction about how a `K20` near-extremal template fails when one extra vertex is added.

## generalization_signal
Moderate. The saturation lemma scales verbatim:

`Any k-color lower-bound template built from traceable monochromatic components of order n-1 becomes fragile when one new vertex is added by an edge of the same color.`

What does not yet scale is the forcing step from an arbitrary coloring to that saturated template.

## proof_template_reuse
Reusable proof move:

- identify a near-extremal monochromatic component of order `n-1`,
- prove it is traceable,
- show any same-color external attachment forces `Pn`.

This template should reuse for nearby exact path problems whenever the extremal construction decomposes into dense, traceable monochromatic blocks.

## candidate_theorem_slice
Candidate slice:

`No 21-vertex counterexample can arise by adding one vertex to a K20 coloring in which every vertex already lies in a traceable monochromatic 10-vertex component. In particular, the explicit dense 4-block 5+5+5+5 lower-bound template does not extend to a counterexample on K21.`

Tested extension of the slice:

`Within the block-constant 5+5+5+5+1 and 6+5+5+5 deformations of the canonical four-block template checked above, no counterexample survives.`

## smallest_param_shift_to_test
The most informative nearby shifts are:

- `P10`: compare whether the same saturation idea explains why the preserved `P10` residue behaves differently;
- `P12`: test whether the same block-saturation obstruction persists one step higher, even if the exact value remains out of reach.

## why_this_is_or_is_not_publishable
Current state is not yet publishable. The rigorous content is a useful obstruction lemma plus a template-failure remark, but that is still too thin for the micro-paper lane by itself. Without the exact value or a visibly stronger theorem slice, this is still sub-paper.

## paper_shape_support
If the main claim closes, the smallest natural support package is:

- the saturation lemma above,
- one paragraph explaining why the standard `K20` lower-bound geometry cannot be extended,
- one immediate corollary or boundary remark identifying what a true `K21` counterexample would have to look like,
- the exact structured-family exclusion from the `5+5+5+5+1` and `6+5+5+5` template neighborhoods.

## boundary_remark
The clean boundary remark is:

`The standard 4-block lower-bound geometry for K20 is already saturated against one-vertex extension. So any 21-vertex counterexample, if it exists, must be structurally subtler than the obvious blow-up construction.`

Natural corollary / remark:

`Any successful 21-vertex construction must break the traceable 10-vertex monochromatic-component mechanism rather than merely perturb the canonical 5+5+5+5 lower-bound template.`

## likely_failure_points
- The main risk is that the exact upper bound needs a genuinely global structural theorem, not just local saturation around near-extremal components.
- A counterexample, if it exists, may use large but non-traceable monochromatic components, so component order alone is not enough.
- A bounded structured search can only refute nearby templates, not settle the full 3-coloring space.
- The current code only treats block-constant deformations, so it leaves open irregular attachments inside or across the 5-vertex blocks.

## what_verify_should_check
- Check the saturation lemma wording carefully, especially that the traced 10-vertex monochromatic path can be chosen with the attachment vertex as an endpoint.
- Check whether the “explicit dense 4-block template” is the right standard lower-bound model for `K20`.
- If code is used, verify that the tested family is stated exactly and not overclaimed.
- Re-run the exact checker and confirm the reported counts `19,683` and `324` with `0` survivors.
- Later prior-art check: confirm whether this saturation / non-extendability observation already appears implicitly in the small-path literature.
