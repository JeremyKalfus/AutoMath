# ruskey-savage-q6

## statement_lock
- Active slug: `ruskey-savage-q6`
- Title: `Ruskey-Savage at dimension 6`
- Locked intended statement: every matching in `Q6` extends to a Hamiltonian cycle.
- Working reformulation: a solution is a cyclic Gray code on the `64` vertices of `Q6` in which every edge of the chosen matching appears as a consecutive pair.
- Solve-stage proof standard used below: if a matching `M` extends to a Hamiltonian cycle `H`, then contracting every edge of `M` inside `H` produces a Hamiltonian cycle in the quotient graph `Q6 / M`.

Self-check:
- The target remains the exact universal statement about all matchings in `Q6`.
- I am not treating a subclass result as if it settled the full conjectural instance.

## definitions
- Write `Q6 = Q5 □ K2` when I decompose along a fixed coordinate `d`; the two `Q5` layers are the `d=0` and `d=1` faces.
- A `d`-edge is an edge parallel to coordinate `d`.
- A matching is `parallel` if all its edges lie in one dimension.
- A matching is `face-contained` if all of its vertices lie in a single codimension-`1` face, equivalently in one copy of `Q5`.
- For a matching `M`, the quotient `Q6 / M` is obtained by contracting every edge of `M`.

Self-check:
- These are only bookkeeping conventions; no definition changes the intended statement.
- The quotient language is being used only as a necessary condition for extendability.

## approach_A
Structural / invariant route: decompose the cube and try to lift exact `Q5` information.

Exact subcase 1: all-parallel matchings extend.

- Fix the matching dimension to be `d = 6` after an automorphism.
- Let `v_1, v_2, ..., v_32, v_1` be any Hamiltonian cycle of `Q5`.
- Lift it to the `64`-cycle
  `v_1^0, v_1^1, v_2^1, v_2^0, v_3^0, v_3^1, ..., v_32^1, v_32^0, v_1^0`
  in `Q6 = Q5 □ K2`.
- This cycle contains every `d`-edge `v_i^0 v_i^1`.
- Therefore any matching consisting only of `d`-edges extends to a Hamiltonian cycle of `Q6`.

Exact subcase 2: any face-contained matching extends.

- Fix a `Q5` face `F` containing the whole matching `M`.
- The dossier says every matching in `Q5` extends to a Hamiltonian cycle, so choose a Hamiltonian cycle
  `C = x_1, x_2, ..., x_32, x_1`
  of `F` containing `M`.
- Let `F'` be the opposite parallel face, and let `x_i'` be the vertex corresponding to `x_i`.
- Inside the prism `C □ K2`, the cycle
  `x_1, x_2, ..., x_32, x_32', x_31', ..., x_1', x_1`
  is Hamiltonian.
- That cycle uses every edge of the bottom rim `C`, hence it contains `M`.
- So any matching contained in one `Q5` face extends in `Q6`.

Attempted strengthening that stalled:

- The obvious next step is broader: if a matching avoids one dimension, split `Q6` into two `Q5` faces and extend the two induced matchings separately.
- The missing lemma is a compatibility statement saying the two `Q5` Hamilton cycles or Hamilton paths can be chosen so that they splice across the prism while still containing the prescribed matching edges.
- I do not see a clean proof of that compatibility from the bare dossier fact "`Q5` is solved" alone.

Immediate consequences:

- Any counterexample must use at least two edge directions.
- Any counterexample must not be contained in a proper face.

Self-check:
- The two stated subcases are complete proofs, not heuristics.
- I am explicitly not claiming the stronger omitted-dimension lemma, because the splice-compatibility step is missing.

## approach_B
Construction / extremal / contradiction route: search for a nonextendable matching by forcing an obstruction in the contraction quotient.

Rigorous obstruction lemma:

- If a matching `M` extends to a Hamiltonian cycle `H`, then `H / M` is a Hamiltonian cycle in `Q6 / M`.
- Therefore any matching whose quotient graph `Q6 / M` is disconnected, has a bridge, or has a cut-vertex cannot extend.

Why this looks promising:

- It turns the problem into building a matching whose contractions destroy enough redundancy in the cube to make Hamiltonicity impossible.
- A bridge obstruction would be especially strong, because it can be checked without solving the whole Hamiltonian-cycle problem.

Candidate families I tried to reason through:

- Near-full parallel families fail immediately as counterexamples, because the parallel case is explicitly extendable by the lifted Gray-cycle construction.
- A more subtle idea is to mix directions in different regions so that a coordinate cut is almost exhausted by matched edges.
- That naive bridge picture breaks down fast: once a matched edge across a cut is contracted, it merges the two sides instead of isolating them, and the cube typically creates new two-step detours through neighboring contracted vertices.

Current state of this route:

- The contraction lemma is exact and useful.
- I do not yet have a concrete matching `M` for which `Q6 / M` exhibits a decisive obstruction.
- So this route diagnoses what a counterexample would have to look like, but it does not produce one.

Self-check:
- The bridge/cut-vertex test is only a necessary condition, and I am using it that way.
- No claimed counterexample appears in this writeup.

## lemma_graph
1. Lemma A: any matching supported in a single dimension extends in `Q6`.
2. Lemma B: any matching contained in one `Q5` face extends in `Q6`.
3. Lemma C: if a matching `M` extends, then the quotient `Q6 / M` is Hamiltonian.
4. Consequence: a counterexample must mix dimensions and spread outside every codimension-`1` face.
5. Remaining gap: I still lack a matching-preserving splice lemma that upgrades solved `Q5` instances to arbitrary two-layer matchings in `Q6`.

## chosen_plan
- Best current path is still the decomposition route, because the dossier already gives exact `Q5` control.
- I pushed that route until it yielded two exact extension lemmas: the all-parallel case and the face-contained case.
- I then switched to the quotient-obstruction route to look for a plausible disproof mechanism and found only a necessary-condition framework, not a concrete obstruction.
- At this point minimal code is not yet justified: the next obvious computations are either generic over matchings or too weakly motivated to beat the current reasoning bottleneck.

Self-check:
- The chosen plan stayed reasoning-first and produced exact statements before considering any computation.
- Stopping before code is deliberate, not an omission.

## self_checks
- Statement check: every conclusion is still anchored to the exact intended statement for `Q6`.
- Proof check: the only complete proofs claimed are the parallel-extension lemma, the face-extension lemma, and the quotient necessary condition.
- Conservatism check: the tempting stronger claim "any matching avoiding one dimension extends" is recorded only as an unfinished idea.
- Method check: no code, brute force, SAT, or generic search was used.

## code_used
- No code used.
- Reason: the current progress is structural, and the next plausible computations would already drift toward generic search over matchings rather than a narrowly justified checker or falsifier.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Exact mathematical output from this solve pass:
  - every all-parallel matching in `Q6` extends;
  - every matching contained in a `Q5` face extends;
  - any genuine counterexample would have to survive both of those filters and also make the quotient `Q6 / M` Hamiltonian-resistant in some subtler way than an obvious bridge.
- I do not have either a proof of the full `Q6` statement or a counterexample.

## likely_failure_points
- The real hard cases may be mixed-direction matchings that meet both sides of every coordinate cut, so the proved subcases may be too easy to say much about the frontier.
- The quotient obstruction is only necessary; many nontrivial quotients with no bridge can still be non-Hamiltonian or Hamiltonian.
- The missing ingredient may be a stronger path-extension or compatible-splicing theorem for matchings in `Q5`, and I have not derived that here.
- Because I stopped before search, I have no computational evidence for or against specific normalized counterexample families.

## what_verify_should_check
- Check the two constructive cycles carefully:
  - the lifted Gray-cycle proof for all-parallel matchings;
  - the prism-cycle proof for face-contained matchings.
- Check the contraction lemma exactly: a Hamiltonian cycle through `M` really does contract to a Hamiltonian cycle in `Q6 / M`.
- Check that the stated consequences are only the safe ones:
  - counterexamples must use at least two dimensions;
  - counterexamples cannot lie in a single `Q5` face.
- Decide whether the stalled omitted-dimension splice idea can actually be repaired from known finite-`Q5` facts, or whether it genuinely needs a stronger theorem than the dossier supplies.

## verify_rediscovery
- PASS 1 used a bounded web audit focused on the exact `Q6` instance, alternate notation, the canonical source, and later partial-progress papers.
- The canonical West REGS page still poses the Ruskey-Savage conjecture as an open problem and records only partial positive cases, not a full `Q6` resolution.
- The published SAT verification found in the MathCheck/DOAJ paper settles the conjecture only through dimension `5`, not `6`.
- A later partial-progress paper on matchings in hypercubes still phrases the conjecture as open and proves extension only for restricted classes such as matchings using at most five directions in `Q_n`.
- Within the allotted budget, I did not find any theorem, proposition, example, observation, corollary, or recent status note that settles the exact intended statement "every matching in `Q6` extends to a Hamiltonian cycle."
- Rediscovery verdict: not established within budget.

## verify_faithfulness
- The solve writeup stays faithful to the intended statement overall. It does not claim the full `Q6` conjecture is proved, and it labels the run only `PARTIAL`.
- The two constructive subclaims are genuinely about the intended notion of extension inside `Q6`:
  - all-parallel matchings;
  - matchings contained in one `Q5` face.
- The writeup also explicitly marks the tempting stronger omitted-dimension splice statement as unproved, so there is no quantifier drift there.
- The only faithfulness issue is local wording inside the face-contained proof: the displayed prism cycle does not contain every bottom-rim edge of `C`; it omits exactly one bottom edge and replaces it with two vertical edges. That is a repairable indexing issue, not wrong-theorem drift.

## verify_proof
- Lemma A checks out. The lifted Gray-cycle construction is a valid Hamiltonian cycle of `Q6`, and it contains every edge in the chosen parallel dimension. A representative local checker confirmed the pattern on a standard `Q5` Gray cycle.
- First incorrect step: in the face-contained proof, the sentence "That cycle uses every edge of the bottom rim `C`, hence it contains `M`" is false as written. The prism cycle
  `x_1, x_2, ..., x_32, x_32', x_31', ..., x_1', x_1`
  omits the bottom edge `x_32 x_1`.
- This is a tiny repair, not a collapse: because `M` is a matching on a `32`-cycle, `|M| <= 16`, so at least one edge of `C` is outside `M`. Relabel the Hamiltonian cycle `C` cyclically so that the omitted closing edge is one not in `M`. Then the same prism cycle contains every edge of `M`.
- The quotient-obstruction route does not verify as written. Contracting a matching inside a Hamiltonian cycle yields a spanning `2`-regular multigraph in the quotient, but not necessarily a simple Hamiltonian cycle in the simple quotient graph. A toy counterexample is a `4`-cycle with the two opposite matching edges contracted: the image is two vertices joined by two parallel edges. So the bridge/cut-vertex obstruction does not follow from the stated argument.
- Safe conclusion after proof checking: the two extension subcases survive, with the small relabeling repair in Lemma B; the quotient-obstruction lemma should be removed or downgraded to an unverified heuristic.

## verify_adversarial
- No checker existed in the artifact, so I reran small local sanity checks instead of introducing a larger search.
- A representative local computation verified Lemma A's lifted cycle pattern on a standard `Q5` Hamilton cycle.
- A representative local computation verified the adjacency pattern of the Lemma B prism cycle and exposed the exact omitted bottom edge, which is why the relabeling repair is needed.
- I also stress-tested the contraction claim with the standard `C4` example above. That adversarial check is enough to reject the proof of the bridge/cut-vertex obstruction in its current form.
- Therefore the computation supports only the repaired subcase proofs, not the obstruction route.

## verify_verdict
- `verify_verdict = "MINOR_FIX"`
- `classification = "PARTIAL"`
- `confidence = "high"`
- `lean_ready = false`
- `next_action = "continue solve from the repaired parallel and face-contained lemmas; drop the quotient-obstruction claim as a verified tool and do not start Lean"`

## minimal_repair_if_any
- Repair Lemma B by cyclically relabeling the chosen `Q5` Hamilton cycle so that the single omitted bottom edge is not in `M`.
- Delete or explicitly downgrade Lemma C / the bridge-obstruction paragraph. As written it is not a valid verified consequence in the simple quotient graph.
