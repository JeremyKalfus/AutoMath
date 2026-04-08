# Solve Record: z3-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_3 × Z_25) prime?`
- Locked target statement: the exact claim is that the zero-divisor graph `Γ(Z_3 × Z_25)` admits a prime labeling, meaning a bijection from its `34` vertices to `{1,2,...,34}` such that adjacent vertices receive coprime labels.
- I am solving only this exact instance `Z_3 × Z_25`, not the broader family `Γ(Z_p × Z_{q^2})`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_3` and `b ∈ Z_25`.
- A nonzero zero-divisor of `Z_3 × Z_25` is exactly a nonzero pair with either `a = 0` or `b` a multiple of `5`.
- The nonzero zero-divisors therefore split into:
  - `A = {(0,b) : b = 1,2,...,24}`, size `24`.
  - `B = {(a,5t) : a ∈ {1,2}, t ∈ {0,1,2,3,4}}`, size `10`.
- Further split:
  - `M = {(0,5),(0,10),(0,15),(0,20)}`, the four vertices in `A` with second coordinate a nonzero multiple of `5`.
  - `N = {(0,b) : 1 ≤ b ≤ 24 and 5 ∤ b}`, size `20`.
  - `U = {(1,0),(2,0)}`, size `2`.
  - `W = {(1,5),(1,10),(1,15),(1,20),(2,5),(2,10),(2,15),(2,20)}`, size `8`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0` in `Z_3` and `bd = 0` in `Z_25`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Ambiguity check:
  - The graph is simple, so there are no loops.
  - The labeling is on vertices, not on elements with multiplicity or on associate classes.

## approach_A

Structural / invariant approach via vertex-class decomposition.

- For two vertices in `A`, the first coordinates are both `0`, so adjacency is decided entirely in `Z_25`.
- Hence two vertices of `A` are adjacent iff both second coordinates are nonzero multiples of `5`.
- Therefore `M` induces `K_4`, and every vertex of `N` is isolated inside `A`.
- A vertex of `U` is adjacent to every vertex of `A`, because its second coordinate is `0`.
- A vertex of `W` is adjacent exactly to the vertices of `M`, because its second coordinate is a nonzero multiple of `5`.
- No two vertices of `B` are adjacent, because both first coordinates are nonzero in `Z_3`, so their first-coordinate product cannot be `0`.
- So the whole graph has this rigid form:
  - `M` is a `4`-clique.
  - `U` is an independent `2`-set joined to all `24` vertices of `A`.
  - `W` is an independent `8`-set joined only to `M`.
  - `N` is an independent `20`-set joined only to `U`.
- This reduces prime labeling to a number-placement problem on four adjacency classes.

## approach_B

Construction / extremal approach by forcing the two universal-to-`A` vertices first.

- Since each vertex of `U` is adjacent to all `24` vertices of `A`, the labels on `U` should have very few non-coprime conflicts.
- A good choice is `13` and `17`, because among `1,...,34` their only non-coprime multiples are
  `13, 26` and `17, 34`.
- Thus if `U` gets labels `13` and `17`, then the `24` labels used on `A` only need to avoid `13,17,26,34`.
- Next, because `M` induces `K_4`, its four labels must be pairwise coprime. A compact choice is `1,3,5,7`.
- Any vertex of `W` is adjacent exactly to the four vertices of `M`, so every label on `W` only needs to be coprime to `1,3,5,7`, i.e. not divisible by `3`, `5`, or `7`.
- This leaves plenty of choices for `W`, including the leftover forbidden labels `26` and `34`, which is useful because those labels cannot go on `A` once `U` is fixed as `13,17`.

## lemma_graph

1. Classify the `34` vertices as `M ⊔ N ⊔ U ⊔ W` with sizes `4,20,2,8`.
2. Prove the adjacency pattern:
   `M` induces `K_4`, `U` is complete to `M ∪ N`, `W` is complete to `M`, and there are no other edges.
3. Choose labels on `U` so that only a very small set of labels is forbidden on `A`.
4. Choose pairwise coprime labels on `M`.
5. Place on `W` labels coprime to all labels on `M`, making sure any labels forbidden for `A` are absorbed into `B = U ∪ W`.
6. Put the remaining `20` labels on `N`; they only need to be coprime to the labels on `U`.
7. Check the three edge types: `M-M`, `U-A`, and `W-M`.

## chosen_plan

- Use Approach A to turn the graph into a small structured split graph with one internal clique.
- Use Approach B to build an explicit labeling on the four classes.
- Only after the full witness is written down, run a tiny local checker tied to this exact witness.

## self_checks

- Statement lock check: the target is the exact prime-labeling question for `Γ(Z_3 × Z_25)`.
- Definitions check: the count `24 + 10 = 34` matches the dossier.
- Structural check: the only internal edges in `A` come from the four nonzero multiples of `5`.
- Construction check: labels on `U` must be chosen before labels on `N`, because `U` controls every edge incident to `N`.
- Witness check: the proposed label sets are disjoint and together use every label in `{1,...,34}` exactly once.
- Tiny checker check: direct enumeration of the ring graph found `34` vertices, `86` edges, and `0` edges whose endpoint labels fail the coprimality condition.

## code_used

- A tiny one-off local witness checker was used after the reasoning was written.
- It enumerated the `34` nonzero zero-divisors of `Z_3 × Z_25`, generated edges by zero product, and checked the proposed labeling on all `86` edges.
- Result: `0` bad edges.

## result

Candidate exact construction:

- Label `U = {(1,0),(2,0)}` by `13,17`.
- Label `M = {(0,5),(0,10),(0,15),(0,20)}` by `1,3,5,7` in any order.
- Label `W` by `2,4,8,11,16,22,26,34` in any order.
- Label the `20` vertices of `N` by the remaining `20` labels
  `6,9,10,12,14,15,18,19,20,21,23,24,25,27,28,29,30,31,32,33`
  in any order.

Why this works:

- `M-M` edges:
  the labels on `M` are `1,3,5,7`, which are pairwise coprime.
- `U-A` edges:
  every label used on `A = M ∪ N` avoids `13,17,26,34`, so every such label is coprime to both `13` and `17`.
- `W-M` edges:
  every label used on `W` is coprime to `1,3,5,7`, because none of
  `2,4,8,11,16,22,26,34`
  is divisible by `3`, `5`, or `7`.
- There are no other edges.
- Direct local checking on the explicit ring graph also found no coprimality violation.

Therefore this is a prime labeling of `Γ(Z_3 × Z_25)`, so the intended statement appears true.

## likely_failure_points

- A mistaken adjacency classification between the four classes would invalidate the construction.
- The set assigned to `N` must really be exactly the complement of the `14` labels used on `M ∪ U ∪ W`.
- The labels on `W` only need to be checked against `M`, not against `U` or against one another.
- Because the source-level open-status risk is nonzero, solve should still be conservative about calling this `EXACT` before verification.

## what_verify_should_check

- Recompute the zero-divisor classes of `Z_3 × Z_25` and confirm there are `34` vertices.
- Re-derive the adjacency pattern `M-M`, `U-A`, `W-M`, and no others.
- Check that the proposed label sets are disjoint and cover exactly `{1,...,34}`.
- Verify coprimality on each actual edge.
- Audit whether the exact instance is already settled in the literature before any Lean work.

## verify_rediscovery

- PASS 1 used a bounded web audit on the exact instance, alternate notation, the canonical source, and follow-up/status queries.
- Exact-instance and alternate-notation searches for `Γ(Z_3 × Z_25)`, `Z_3 x Z_25`, and `zero-divisor graph` with `prime labeling` did not produce any hit asserting that this exact instance had already been solved.
- The canonical source `On prime labelings of zero-divisor graphs` (Congressus Numerantium 236, 2025, DOI `10.61091/cn236-06`) still appears to leave the family at Conjecture 4.4 and does not, from the checked source-level audit, already state this exact `p=3, q=5` instance as a theorem, proposition, example, observation, or corollary.
- A brief follow-up citation/status search also did not reveal a later paper, note, or discussion explicitly settling `Γ(Z_3 × Z_25)`.
- Rediscovery was therefore not established within the bounded budget.

## verify_faithfulness

- The candidate claim matches the intended statement exactly: a prime labeling of the vertex set of the zero-divisor graph `Γ(Z_3 × Z_25)`.
- There is no wrong-theorem drift to the broader family `Γ(Z_p × Z_{q^2})`; the construction is explicitly for the single instance `Z_3 × Z_25`.
- The definition of the graph used in the solve record matches the standard one in the dossier: vertices are the nonzero zero-divisors, and adjacency is by zero product.
- The labeling target is also exact: a bijection from the `34` vertices to `{1,2,...,34}` with coprime labels on adjacent vertices.
- I found no quantifier drift, proxy statement, or definition mismatch.

## verify_proof

- I did not find an incorrect step.
- The main possible weak point was the structural decomposition of the graph. Re-deriving the ring-product condition confirms:
  - `M` induces `K_4`;
  - `U` is complete to all of `A = M ∪ N`;
  - `W` is complete exactly to `M`;
  - there are no other edges.
- Given that decomposition, the number-theoretic argument is adequate:
  - labels `13,17` on `U` force only `13,26,17,34` to be excluded from `A`;
  - labels `1,3,5,7` on `M` are pairwise coprime;
  - labels on `W` avoid divisibility by `3,5,7`, which is exactly what is needed against `M`;
  - labels on `N` need only be coprime to `13` and `17`, and the remaining set satisfies that.
- The proof is therefore sound as an explicit witness proof, assuming the bounded PASS 1 audit did not miss prior art.

## verify_adversarial

- I reran a fresh local checker directly from the ring definition, without relying on the solver's earlier summary.
- The checker found:
  - `34` vertices;
  - `86` edges;
  - edge-type counts `M-M = 6`, `M-U = 8`, `M-W = 32`, `N-U = 40`;
  - the proposed labels form a bijection onto `{1,...,34}`;
  - `0` bad edges with non-coprime endpoint labels;
  - `0` mismatches against the claimed class-level adjacency pattern.
- I also checked the converse pattern claim, not just existing edges, and found no missing or extra edge classes.
- No adversarial break of the witness was found.

## verify_verdict

- `VERIFIED`
- The intended statement appears to be proved by a correct explicit labeling.
- PASS 1 did not establish rediscovery, so the run should not be marked `REDISCOVERY`.
- Because the claim is exact, non-variant, and survived adversarial checking, this artifact is ready for Lean from the verification standpoint.

## minimal_repair_if_any

- None.

## final_reclassification

- Under the patched global harness rule, this result counted only as a `CANDIDATE` until the Lean stage actually completed.
- In this patch session, the exact instance was then upgraded to `EXACT` because the Lean formalization and build checks finished successfully.

## lean_statement

- Lean project root: `lean/`
- Formalized theorem: `AutoMath.Z3Z25.z3_z25_zeroDivisorGraph_prime`
- The theorem states that the exact zero-divisor graph `Γ(Z_3 × Z_25)` admits a prime labeling, using the explicit 34-vertex witness from this artifact.

## lean_skeleton

- Model vertices as the nonzero zero-divisors of `Fin 3 × Fin 25`.
- Encode the explicit labeling witness as `rawLabel`.
- Prove the vertex count, injectivity of the witness, and edge-coprimality on the exact instance by exhaustive kernel `decide` checks.
- Package those checks into `IsPrimeLabeling label` and the existential theorem.

## lean_result

- `lake build` succeeded in the local `lean/` project.
- `#print axioms AutoMath.Z3Z25.z3_z25_zeroDivisorGraph_prime` reported only `propext`, `Classical.choice`, and `Quot.sound`; there was no `sorry`, `sorryAx`, or `native_decide` residue.
- `lean4checker --fresh` was not available on this machine, so that extra audit could not be run.
- Practical outcome: the exact instance-level claim is now formalized and checked in Lean.

## lean_blockers

- No blocker remained for this exact instance.
- The only missing extra audit tool on this machine was `lean4checker`.

## provenance_note

- Lean completed for the exact instance `Γ(Z_3 × Z_25)` in the local AutoMath backend, and the checked witness is being preserved as-is.
- External novelty review is being handled outside the harness, so this artifact should be read as an exact checked instance whose frontier status is being tracked separately.
