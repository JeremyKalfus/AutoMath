# Solve Record: Is the zero-divisor graph `Γ(Z_5 × Z_5 × Z_2)` prime?

## statement_lock
Intended statement: the zero-divisor graph `Γ(Z_5 × Z_5 × Z_2)` admits a prime labeling, i.e. a bijection from its `33` vertices to `{1,2,...,33}` such that adjacent vertices receive coprime labels.

I am using the standard zero-divisor graph on the nonzero zero-divisors of `R = Z_5 × Z_5 × Z_2`, with coordinatewise multiplication and adjacency defined by product `0`.

Self-check:

- `|R| = 5 * 5 * 2 = 50`.
- Units are exactly the triples with all coordinates nonzero, so there are `4 * 4 * 1 = 16` units.
- Hence the nonzero zero-divisors are `50 - 16 - 1 = 33`, matching the label set size.

## definitions
Write `U = {1,2,3,4} = Z_5^×`. The nonzero zero-divisors split into six support classes:

- `A_i = (i,0,0)` for `i in U`, size `4`
- `B_i = (0,i,0)` for `i in U`, size `4`
- `C = (0,0,1)`, size `1`
- `D_{ij} = (i,j,0)` for `i,j in U`, size `16`
- `E_i = (i,0,1)` for `i in U`, size `4`
- `F_i = (0,i,1)` for `i in U`, size `4`

These are all the nonzero elements with at least one zero coordinate and at least one nonzero coordinate, so they account for all `33` vertices.

Because multiplication is coordinatewise and each coordinate ring is a field, two vertices are adjacent exactly when in each coordinate at least one of the two entries is `0`, equivalently when their supports are disjoint.

Therefore the only edge families are:

- `A` joined completely to `B`, `C`, and `F`
- `B` joined completely to `A`, `C`, and `E`
- `C` joined completely to `A`, `B`, and `D`

There are no other edges.

Ambiguities / conventions checked:

- The zero element is excluded from the vertex set.
- Vertices in the same support class are pairwise nonadjacent because their supports intersect.
- A support-class labeling is enough once the class sizes are correct, because any bijection inside a class preserves all adjacency relations.

Self-check:

- The edge count from this description is `|A||B| + |A||F| + |B||E| + |A| + |B| + |D| = 16 + 16 + 16 + 4 + 4 + 16 = 72`.
- The graph is sparse enough that an explicit construction should be feasible.

## approach_A
Structural / invariant approach.

The support decomposition shows that `C` is the unique high-degree hinge: it is adjacent to all `4 + 4 + 16 = 24` vertices in `A ∪ B ∪ D`, while every `D_{ij}` is a leaf adjacent only to `C`.

So the natural invariant move is to put label `1` on `C`. Then every `D_{ij}` becomes unconstrained, since `gcd(1,n) = 1` for all `n`.

After that, the only nontrivial coprimality constraints are:

- every label on `A` must be coprime to every label on `B`
- every label on `A` must be coprime to every label on `F`
- every label on `B` must be coprime to every label on `E`

This suggests separating prime supports:

- put powers of `2` on `A`
- put odd labels on `B` and `F`
- choose the `B` labels to use only primes `3` and `5`
- then choose the `E` labels to avoid divisibility by `3` and `5`

Self-check:

- This reduction is exact, not heuristic: once `C = 1`, the `D`-class really becomes free.
- The problem reduces to finding four labels for each of `A`, `B`, `E`, and `F` with the stated divisibility filters.

## approach_B
Construction / extremal approach.

Use the hardest complete bipartite pieces first.

Take

- `A <- {2,4,8,16}`

Then every label adjacent to `A` must merely be odd. So both `B` and `F` may be chosen from odd labels. To make `E` easy later, take

- `B <- {3,5,9,25}`

Now every `E` label only needs to avoid divisibility by `3` and `5`, so a clean choice is

- `E <- {14,22,26,32}`

Finally choose any four unused odd labels for `F`, for example

- `F <- {7,11,13,17}`

and reserve `1` for `C`. The `16` remaining labels can all be dumped onto `D`, since those vertices only see `C`.

Self-check:

- `A-B` is safe because even vs odd.
- `A-F` is safe because even vs odd.
- `B-E` is safe because every `B` label has prime factors only in `{3,5}`, while every `E` label avoids `3` and `5`.

## lemma_graph
Proof skeleton:

1. Classify the `33` vertices into the six support classes `A`, `B`, `C`, `D`, `E`, `F`.
2. Show adjacency is exactly disjointness of support.
3. Deduce the only edge families are `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, and `C-D`.
4. If the labels assigned to the six classes partition `{1,...,33}` with the correct class sizes, and every pair of adjacent classes is cross-coprime, then any bijection within each class is a prime labeling.
5. Exhibit such a partition.

## chosen_plan
Use the explicit construction from Approach B.

Assign labels to actual vertices as follows:

- `C = (0,0,1) -> 1`
- `A_1, A_2, A_3, A_4 -> 2, 4, 8, 16`
- `B_1, B_2, B_3, B_4 -> 3, 5, 9, 25`
- `E_1, E_2, E_3, E_4 -> 14, 22, 26, 32`
- `F_1, F_2, F_3, F_4 -> 7, 11, 13, 17`

The remaining labels are

- `R = {6,10,12,15,18,19,20,21,23,24,27,28,29,30,31,33}`

Assign these arbitrarily to the `16` vertices `D_{ij}`; for definiteness, use lexicographic order:

- `D_11, D_12, D_13, D_14 -> 6, 10, 12, 15`
- `D_21, D_22, D_23, D_24 -> 18, 19, 20, 21`
- `D_31, D_32, D_33, D_34 -> 23, 24, 27, 28`
- `D_41, D_42, D_43, D_44 -> 29, 30, 31, 33`

Now verify the edge families.

1. `A-C`, `B-C`, and `C-D`:
Every such edge meets the label `1`, so all these gcds are `1`.

Self-check:

- This handles `4 + 4 + 16 = 24` edges immediately.

2. `A-B`:
Every `A` label is a power of `2`, and every `B` label is odd. Hence every cross-gcd is `1`.

Self-check:

- No `B` label is divisible by `2`.

3. `A-F`:
Again, every `A` label is a power of `2`, and every `F` label is odd. Hence every cross-gcd is `1`.

Self-check:

- No extra condition on `F` is needed beyond oddness.

4. `B-E`:
Every `B` label has prime factors contained in `{3,5}`.
Each `E` label is `14,22,26,32`, none of which is divisible by `3` or `5`.
So every `B-E` gcd is `1`.

Self-check:

- `32` is allowed because `E` is not adjacent to `A`.

Thus every edge of the graph joins two coprime labels, so this is a prime labeling of `Γ(Z_5 × Z_5 × Z_2)`.

## self_checks
- Vertex-count check: `33` vertices, `33` labels.
- Partition check: the displayed labels are exactly `{1,...,33}`.
- Structural check: adjacency really depends only on support disjointness.
- Proof-risk check: the only realistic failure mode is a transcription mistake in the explicit assignment.

## code_used
After the reasoning and explicit witness were written down, a tiny local checker was used only for witness verification. It checked:

- the labels form a bijection from the `33` vertices to `{1,...,33}`
- the graph built from coordinatewise zero product has `72` edges
- every edge joins coprime labels

No search, optimization, SAT, ILP, CP-SAT, or brute force was used.

## result
Solve-stage outcome: explicit prime-labeling candidate found for the exact intended instance.

Classification for solve: `CANDIDATE`.

## likely_failure_points
- A convention mismatch if some later stage used a nonstandard zero-divisor-graph convention, though the dossier definitions match the standard one used here.
- A transcription error in the explicit `D_{ij}` label list.
- A verifier may prefer the same construction rewritten directly as a Lean-friendly function on the six support classes.

## what_verify_should_check
- First do the bounded rediscovery / prior-art pass required by the harness.
- Independently re-derive the six support classes and the six edge families.
- Re-check that the displayed assignment really uses each label `1` through `33` exactly once.
- Independently check the `72` edge gcd conditions on the actual ring elements.
- If rediscovery stays unestablished, this witness looks Lean-ready.

## verify_rediscovery
Bounded PASS 1 completed within budget using targeted searches for the exact instance, reordered notation, the family statement, the Fox-Mooney source, and possible same-source theorem/example/corollary coverage.

Searches checked included the exact instance forms `Γ(Z_5 × Z_5 × Z_2)` and `Z_5 × Z_5 × Z_2`, the reordered form `Z_2 × Z_5 × Z_5`, the canonical source title and DOI `10.61091/cn236-06`, and a follow-up citation/status search.

Outcome: no clear rediscovery found. The canonical source still presents the broader family `Γ(Z_p × Z_p × Z_q)` as Conjecture 4.3, and the bounded audit did not uncover an earlier theorem, proposition, example, observation, or corollary that already settles the exact `Z_5 × Z_5 × Z_2` instance. I therefore do not classify this run as `REDISCOVERY`.

Short note on the current proof: independently of novelty, the displayed construction appears mathematically correct.

## verify_faithfulness
The solve-stage claim matches the intended statement exactly.

- Same graph convention: vertices are the nonzero zero-divisors of `Z_5 × Z_5 × Z_2`, with adjacency defined by coordinatewise product `0`.
- Same target property: a bijection from the `33` vertices to `{1,...,33}` with coprime labels on every edge.
- No quantifier drift: this is the single concrete instance `Γ(Z_5 × Z_5 × Z_2)`, not a weaker family fragment or a nearby variant.

I found no wrong-theorem drift, no changed definitions, and no proxy statement replacing the intended claim.

## verify_proof
I re-derived the structure from scratch and found no incorrect step.

Key checks:

- Vertex count: `|Z_5 × Z_5 × Z_2| = 50`, units are exactly the triples with all coordinates nonzero, so there are `4 * 4 * 1 = 16` units and hence `50 - 16 - 1 = 33` nonzero zero-divisors.
- Support classes: every nonzero zero-divisor has support one of `A = (*,0,0)`, `B = (0,*,0)`, `C = (0,0,1)`, `D = (*,*,0)`, `E = (*,0,1)`, `F = (0,*,1)`, with sizes `4,4,1,16,4,4`.
- Adjacency criterion: because each coordinate ring is a field, coordinatewise product is `0` exactly when in each coordinate at least one entry is `0`, so adjacency is equivalent to disjoint supports.
- Edge families: this yields exactly `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, and `C-D`, and no others.
- Witness logic: putting label `1` on `C` makes all `C-D`, `A-C`, and `B-C` edges automatically valid; the remaining cross-constraints reduce to `A-B`, `A-F`, and `B-E`, which are handled by parity and by excluding factors `3,5` from the `E` labels.

I found no hidden assumption beyond the standard graph convention already fixed in the dossier. The proof is short but complete once the support-class adjacency description is established.

## verify_adversarial
I reran the local checker in `artifacts/z5-z5-z2-prime-zero-divisor-graph/check_witness.py`.

Observed output:

- `vertex_count = 33`
- `edge_count = 72`
- `violations = []`

I also checked the checker itself for scope mismatch. It builds the actual vertex set of nonzero zero-divisors in `Z_5 × Z_5 × Z_2`, uses the coordinatewise-zero-product adjacency test, verifies the labels are exactly `{1,...,33}`, and then checks `gcd = 1` on every edge. That is the right computation for the intended claim.

I did not find a candidate-breaking case. In particular, the only potentially delicate part, the `B-E` interface, is safe because `B = {3,5,9,25}` uses only primes `3` and `5`, while `E = {14,22,26,32}` avoids both.

## verify_verdict
`VERIFIED`

The candidate survives faithfulness, proof, and adversarial checking, and bounded PASS 1 did not establish rediscovery. This should remain classified as `CANDIDATE`, not `EXACT`, until Lean verification is completed.

## minimal_repair_if_any
None. No conservative repair was needed.

## lean_statement
Lean formalization target:

- `AutoMath.Z5Z5Z2.z5_z5_z2_zeroDivisorGraph_prime : ∃ f : Vertex → Label, IsPrimeLabeling f`

Here:

- `Vertex` is the subtype of standard representatives `(a,b,c) ∈ Fin 5 × Fin 5 × Fin 2` that are exactly the nonzero zero-divisors of `Z_5 × Z_5 × Z_2`.
- `Adj` is the exact zero-divisor-graph adjacency relation: distinct vertices with coordinatewise product `0`, encoded as the modular equalities mod `5`, `5`, and `2`.
- `Label = Fin 33`, interpreted as the mathematical label set `{1,...,33}` through `labelValue i = i + 1`.
- `IsPrimeLabeling f` means `f` is bijective and every adjacent pair gets coprime natural-number labels.

This is faithful to the intended statement: it is the exact `33`-vertex graph `Γ(Z_5 × Z_5 × Z_2)` and the exact prime-labeling condition on `{1,...,33}`.

## lean_skeleton
Proof skeleton used in Lean:

1. Encode the graph on the exact vertex set `Vertex` of nonzero zero-divisors.
2. Define the explicit witness `rawLabel` by case-splitting on the six support classes:
   - `(i,0,0) ↦ 2,4,8,16`
   - `(0,i,0) ↦ 3,5,9,25`
   - `(0,0,1) ↦ 1`
   - `(i,j,0) ↦ 6,10,12,15,18,19,20,21,23,24,27,28,29,30,31,33`
   - `(i,0,1) ↦ 14,22,26,32`
   - `(0,i,1) ↦ 7,11,13,17`
3. Prove by kernel decision:
   - `Fintype.card Vertex = 33`
   - the witness is injective on vertices
   - every adjacent pair gets coprime labels
4. Upgrade injectivity to bijectivity using the cardinality match `|Vertex| = |Fin 33|`.
5. Package the witness as the exact theorem `z5_z5_z2_zeroDivisorGraph_prime`.

## lean_result
Lean backend used: the existing project under `lean/`.

Files written:

- `lean/AutoMath/Z5Z5Z2.lean`
- `artifacts/z5-z5-z2-prime-zero-divisor-graph/lean/AutoMath/Z5Z5Z2.lean`
- `artifacts/z5-z5-z2-prime-zero-divisor-graph/lean/AxiomAudit.lean`

Checks run:

- `cd lean && lake build`
- `cd lean && lake env lean ../artifacts/z5-z5-z2-prime-zero-divisor-graph/lean/AxiomAudit.lean`

Observed Lean outcome:

- `lake build` succeeded and built `AutoMath.Z5Z5Z2`.
- `#print axioms` for `z5_z5_z2_zeroDivisorGraph_prime`, `..._checked`, and `..._explicit` reported only `[propext, Classical.choice, Quot.sound]`.
- No `sorry`, `admit`, placeholders, or `sorryAx` appeared in the proved theorem audit.

Conclusion:

- The exact intended statement was formalized and checked in Lean.
- This run now meets the harness stop condition for `EXACT`.

## lean_blockers
- `lean4checker --fresh` was not available on this machine (`command -v lean4checker` returned nothing), so that optional extra audit could not be run.
- This was not blocking because the official `lake build` succeeded and the axiom audit showed no `sorryAx`.
