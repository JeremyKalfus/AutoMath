# Solve Record: Is the zero-divisor graph `Gamma(Z_7 x Z_7 x Z_2)` prime?

## statement_lock
Intended statement: the zero-divisor graph `Gamma(Z_7 x Z_7 x Z_2)` admits a prime labeling, i.e. a bijection from its `61` vertices to `{1,2,...,61}` such that adjacent vertices receive coprime labels.

I am using the standard zero-divisor graph on the nonzero zero-divisors of `R = Z_7 x Z_7 x Z_2`, with coordinatewise multiplication and adjacency defined by product `0`.

Self-check:

- `|R| = 7 * 7 * 2 = 98`.
- Units are exactly the triples with all coordinates nonzero, so there are `6 * 6 * 1 = 36` units.
- Hence the nonzero zero-divisors are `98 - 36 - 1 = 61`, matching the label set size.

## definitions
Write `U = {1,2,3,4,5,6} = Z_7^x`. The nonzero zero-divisors split into six support classes:

- `A_i = (i,0,0)` for `i in U`, size `6`
- `B_i = (0,i,0)` for `i in U`, size `6`
- `C = (0,0,1)`, size `1`
- `D_ij = (i,j,0)` for `i,j in U`, size `36`
- `E_i = (i,0,1)` for `i in U`, size `6`
- `F_i = (0,i,1)` for `i in U`, size `6`

These are exactly the nonzero elements with nonempty proper support, so they account for all `61` vertices.

Because multiplication is coordinatewise and each coordinate ring is a field, two vertices are adjacent exactly when in each coordinate at least one entry is `0`, equivalently when their supports are disjoint.

Therefore the only edge families are:

- `A` joined completely to `B`, `C`, and `F`
- `B` joined completely to `A`, `C`, and `E`
- `C` joined completely to `A`, `B`, and `D`

There are no other edges.

Ambiguities / conventions checked:

- The zero element is excluded from the vertex set.
- The graph is simple, so there are no loops.
- Vertices in the same support class are pairwise nonadjacent because their supports intersect.
- A classwise labeling is enough once the class sizes are correct, because any bijection inside a class preserves all adjacency relations.

Self-check:

- The edge count from this description is `|A||B| + |A||F| + |B||E| + |A| + |B| + |D| = 36 + 36 + 36 + 6 + 6 + 36 = 156`.
- The unique vertex `C` is the only hinge attached to the whole `D`-class.

## approach_A
Structural / invariant approach.

The support decomposition shows that `C` is the key vertex:

- every `D_ij` is a leaf adjacent only to `C`
- every vertex in `A union B` is adjacent to `C`
- the only remaining nontrivial complete bipartite interfaces are `A-B`, `A-F`, and `B-E`

So the natural invariant move is to put label `1` on `C`. Then every `C-D`, `A-C`, and `B-C` edge is automatically valid, and the `36` labels on `D` become completely unconstrained.

After that, the only arithmetic obligations are:

- every label on `A` must be coprime to every label on `B`
- every label on `A` must be coprime to every label on `F`
- every label on `B` must be coprime to every label on `E`

This suggests separating prime supports:

- let `A` use only primes from `{2,3}`
- let `B` use primes bigger than `3`
- let `E` again use only `{2,3}`
- let `F` avoid `2` and `3`

Self-check:

- This reduction is exact, not heuristic: once `C = 1`, the `D`-class is genuinely free.
- No edge ever connects `E` to `A` or `F`, or `F` to `B`, so prime overlaps there do not matter.

## approach_B
Construction / extremal approach.

Use the most constrained interfaces first.

Take

- `A <- {2,4,8,16,27,32}`
- `B <- {5,7,11,13,17,19}`

Then every `A-B` pair is coprime because the `A` labels use only primes `2,3`, while the `B` labels are primes greater than `3`.

Now make the side classes compatible with those same prime filters:

- `E <- {3,6,9,12,18,24}`
- `F <- {25,29,31,35,37,49}`

Then

- every `B-E` pair is coprime because each `E` label has prime divisors only in `{2,3}`
- every `A-F` pair is coprime because each `F` label avoids divisibility by `2` and `3`

Reserve `1` for `C`, and put the remaining `36` labels on `D`.

Self-check:

- `A`, `B`, `E`, and `F` are pairwise disjoint label sets of the right sizes.
- The chosen `F` labels are all odd and not divisible by `3`.
- The chosen `E` labels are all `2,3`-smooth, so they stay coprime to every label in `B`.

## lemma_graph
Proof skeleton:

1. Classify the `61` vertices into the six support classes `A`, `B`, `C`, `D`, `E`, `F`.
2. Show adjacency is exactly disjointness of support.
3. Deduce the only edge families are `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, and `C-D`.
4. Put label `1` on `C`; then all `A-C`, `B-C`, and `C-D` edges are automatically valid.
5. Find label sets for `A`, `B`, `E`, and `F` such that the three remaining adjacent class pairs are cross-coprime.
6. Assign the remaining `36` labels arbitrarily to `D`.
7. Conclude that every edge joins coprime labels, so the graph is prime.

## chosen_plan
Use the explicit construction from Approach B.

Assign labels to actual vertices as follows:

- `C = (0,0,1) -> 1`
- `A_1, A_2, A_3, A_4, A_5, A_6 -> 2, 4, 8, 16, 27, 32`
- `B_1, B_2, B_3, B_4, B_5, B_6 -> 5, 7, 11, 13, 17, 19`
- `E_1, E_2, E_3, E_4, E_5, E_6 -> 3, 6, 9, 12, 18, 24`
- `F_1, F_2, F_3, F_4, F_5, F_6 -> 25, 29, 31, 35, 37, 49`

The remaining labels are

- `R = {10,14,15,20,21,22,23,26,28,30,33,34,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,55,56,57,58,59,60,61}`

Assign these in lexicographic order to the `36` vertices `D_ij`; for definiteness:

- `D_11, D_12, D_13, D_14, D_15, D_16 -> 10, 14, 15, 20, 21, 22`
- `D_21, D_22, D_23, D_24, D_25, D_26 -> 23, 26, 28, 30, 33, 34`
- `D_31, D_32, D_33, D_34, D_35, D_36 -> 36, 38, 39, 40, 41, 42`
- `D_41, D_42, D_43, D_44, D_45, D_46 -> 43, 44, 45, 46, 47, 48`
- `D_51, D_52, D_53, D_54, D_55, D_56 -> 50, 51, 52, 53, 54, 55`
- `D_61, D_62, D_63, D_64, D_65, D_66 -> 56, 57, 58, 59, 60, 61`

Now verify the edge families.

1. `A-C`, `B-C`, and `C-D`:
Every such edge meets the label `1`, so all these gcds are `1`.

Self-check:

- This handles `6 + 6 + 36 = 48` edges immediately.

2. `A-B`:
Each `A` label has prime divisors only in `{2,3}`.
Each `B` label is a prime greater than `3`.
So every `A-B` gcd is `1`.

Self-check:

- No `B` label is divisible by `2` or `3`.

3. `B-E`:
Each `E` label has prime divisors only in `{2,3}`.
Each `B` label is a prime greater than `3`.
So every `B-E` gcd is `1`.

Self-check:

- The fact that `E` reuses primes `2` and `3` is harmless because `E` is not adjacent to `A`.

4. `A-F`:
Each `A` label has prime divisors only in `{2,3}`.
The `F` labels `25,29,31,35,37,49` are all free of factors `2` and `3`.
So every `A-F` gcd is `1`.

Self-check:

- The only shared odd prime that appears inside `F` is `5` or `7`, and those do not appear in `A`.

Thus every edge of the graph joins two coprime labels, so this is a prime labeling of `Gamma(Z_7 x Z_7 x Z_2)`.

## self_checks
- Vertex-count check: `61` vertices and `61` labels.
- Partition check: the displayed labels are exactly `{1,...,61}`.
- Structural check: adjacency depends only on support disjointness.
- Edge-count check: the support decomposition predicts `156` edges.
- Witness check: a tiny direct computation on the actual ring graph found `156` edges and `0` coprimality violations for the displayed assignment.

## code_used
After the reasoning and explicit witness were written down, a tiny inline Python checker was used only for witness verification. It checked:

- the `61` vertices are exactly the nonzero zero-divisors of `Z_7 x Z_7 x Z_2`
- the support-class counts are `6,6,1,36,6,6`
- the labels form a bijection from the `61` vertices to `{1,...,61}`
- the graph built from coordinatewise zero product has `156` edges
- every edge joins coprime labels

Observed output:

- class sizes `{'A': 6, 'B': 6, 'C': 1, 'D': 36, 'E': 6, 'F': 6}`
- `rest_count = 36`
- `edge_count = 156`
- `violations = 0`

No search, optimization, SAT, ILP, CP-SAT, or brute force was used.

## result
Solve-stage outcome: explicit prime-labeling candidate found for the exact intended instance.

Classification for solve: `CANDIDATE`.

## likely_failure_points
- A convention mismatch if a later stage used a nonstandard zero-divisor-graph convention, though the dossier definitions match the standard one used here.
- A transcription error in the explicit label assignment, especially in the `D_ij` list.
- A verifier may prefer the same construction rewritten as a direct support-class function rather than a lexicographic table.

## what_verify_should_check
- First do the bounded rediscovery / prior-art pass required by the harness.
- Independently re-derive the six support classes and the six edge families.
- Re-check that the displayed assignment really uses each label `1` through `61` exactly once.
- Independently check the `156` edge gcd conditions on the actual ring elements.
- If rediscovery stays unestablished, this witness looks lean-ready.

## verify_rediscovery
PASS 1 used a bounded live web audit and then stopped browsing.

Search patterns covered:

- the exact instance notation `Gamma(Z_7 x Z_7 x Z_2)` with `prime labeling`
- alternate family notation `Z_p x Z_p x Z_q` and reordered tuple phrasing
- the canonical source by title, conjecture number, and DOI `10.61091/cn236-06`
- same-source checks aimed at whether an earlier theorem / proposition / example / observation / corollary already settles the exact tuple
- one citation/status sweep for later exact-instance discussion

What the bounded pass found:

- the canonical 2025 Fox-Mooney paper is still the central source returned for this family
- the dossier's source summary remained consistent with the bounded pass: the paper proves earlier diagonal families before stating Conjecture 4.3 for the broader `Gamma(Z_p x Z_p x Z_q)` family
- no exact-instance hit for `Gamma(Z_7 x Z_7 x Z_2)` was found
- no later paper, note, or discussion within budget explicitly solved, directly implied, or exhibited the exact intended statement

Rediscovery conclusion:

- rediscovery was not established within the required bounded pass
- this remains a candidate proof of an apparently still-open exact instance, not a proof of a known settled result

## verify_faithfulness
The solve record is faithful to the intended statement.

- The vertex set is exactly the nonzero zero-divisors of `Z_7 x Z_7 x Z_2`.
- The claimed result is exactly existence of a prime labeling of that graph, not a weaker proxy such as a partial labeling, classwise heuristic, or variant graph convention.
- The support-class decomposition `A,B,C,D,E,F` matches the standard coordinatewise-zero-product definition from the dossier.
- The final construction is an explicit bijection from the `61` actual vertices to `{1,...,61}`.

No wrong-theorem drift, quantifier drift, or definition change was found.

## verify_proof
No incorrect step found.

Independent proof audit:

- The support classes are exhaustive and disjoint, with sizes `6,6,1,36,6,6`, totaling `61`.

## lean_statement
Main Lean target:

- `AutoMath.Z7Z7Z2.z7_z7_z2_zeroDivisorGraph_prime : ∃ f : Vertex → Label, IsPrimeLabeling f`

Exact formal objects used:

- `Raw = Fin 7 × Fin 7 × Fin 2`
- `Vertex = {x : Raw // IsVertex x}`, where `IsVertex` means "nonzero and has at least one zero coordinate"
- `Adj` is the exact zero-divisor-graph adjacency relation given by coordinatewise product equal to `0` modulo `7,7,2`
- `Label = Fin 61`, interpreted as the mathematical label set `{1,...,61}` through `labelValue ℓ = ℓ.val + 1`

Faithfulness audit:

- This formal statement is exactly the intended existence claim for a prime labeling of `Gamma(Z_7 x Z_7 x Z_2)`.
- It does not weaken the claim to a proxy graph, a partial labeling, or a support-class-only abstraction.
- The explicit companion theorem `AutoMath.Z7Z7Z2.z7_z7_z2_zeroDivisorGraph_prime_explicit` records the same witness in natural-number label form.

## lean_skeleton
Lean proof skeleton used:

1. Encode the exact finite vertex set of nonzero zero-divisors in `Fin 7 × Fin 7 × Fin 2`.
2. Define the exact adjacency predicate `Adj` by coordinatewise zero product modulo `7,7,2`.
3. Define `rawLabel` by the explicit witness from verification:
   - `C = (0,0,1)` gets label `1`
   - the six `A` vertices get `2,4,8,16,27,32`
   - the six `B` vertices get `5,7,11,13,17,19`
   - the six `E` vertices get `3,6,9,12,18,24`
   - the six `F` vertices get `25,29,31,35,37,49`
   - the `36` `D_ij` vertices get the remaining labels in the recorded lexicographic order
4. Prove cardinality, injectivity on vertices, and edge-coprimality by finite exhaustive checking with `decide +kernel`.
5. Use `Fintype.bijective_iff_injective_and_card` to upgrade injectivity plus `|Vertex| = 61` to bijectivity.
6. Conclude `IsPrimeLabeling label`, then package the exact existence theorem and the explicit theorem.

## lean_result
Lean-stage outcome: the exact intended statement was fully formalized and the target module checked.

Checks run:

- `cd lean && lake build AutoMath.Z7Z7Z2` succeeded.
- `cd lean && lake env lean ../artifacts/z7-z7-z2-prime-zero-divisor-graph/lean/AxiomAudit.lean` succeeded.
- The axiom audit reported only `[propext, Classical.choice, Quot.sound]` for:
  - `AutoMath.Z7Z7Z2.z7_z7_z2_zeroDivisorGraph_prime`
  - `AutoMath.Z7Z7Z2.z7_z7_z2_zeroDivisorGraph_prime_checked`
  - `AutoMath.Z7Z7Z2.z7_z7_z2_zeroDivisorGraph_prime_explicit`
- No `sorry`, `admit`, placeholder proof term, or `sorryAx` appeared in the target theorem audit.
- The mirrored artifact file `artifacts/z7-z7-z2-prime-zero-divisor-graph/lean/AutoMath/Z7Z7Z2.lean` was checked to match `lean/AutoMath/Z7Z7Z2.lean` exactly.
- `lean4checker --fresh` was unavailable on this machine.

Conclusion:

- The run earns `classification = EXACT` for this slug.
- `lean_complete = true` is justified for the exact intended statement itself.

## lean_blockers
No blocker remains for the target theorem.

Repo-level note:

- `cd lean && lake build` was also run as requested, but it failed in the pre-existing unrelated file `lean/AutoMath/C16458CNBC.lean` at line `89` with a missing `Decidable (∀ (color : Coloring), ¬IsCNBColoring color)` instance.
- That unrelated library failure does not affect the successful check of `AutoMath.Z7Z7Z2`.
- Because each coordinate ring is a field, two nonzero zero-divisors are adjacent exactly when for each coordinate at least one entry is `0`; equivalently their supports are disjoint.
- From that criterion, the only edge families are exactly `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, and `C-D`.
- Once `C` gets label `1`, every `A-C`, `B-C`, and `C-D` edge is automatically valid.
- The arithmetic checks for the remaining complete bipartite interfaces are correct:
  - every `A` label uses only primes `2,3`
  - every `B` label is a prime greater than `3`
  - every `E` label is `2,3`-smooth
  - every `F` label avoids factors `2` and `3`
- Therefore every edge in `A-B`, `B-E`, and `A-F` joins coprime labels.

The proof is short but complete for this explicit witness.

## verify_adversarial
PASS 4 reran the witness verification independently from the record and tried to break the claimed structure.

Independent checker results:

- `vertex_count = 61`
- `class_sizes = {'A': 6, 'B': 6, 'C': 1, 'D': 36, 'E': 6, 'F': 6}`
- `label_count = 61`
- `label_set_ok = True`
- `edge_count = 156`
- `violations = 0`
- `unexpected_edge_families = 0`

Additional adversarial sanity checks:

- the degree multiset came out as expected from the class picture: `36` leaves of degree `1`, `12` vertices of degree `13`, `12` vertices of degree `6`, and one hinge vertex of degree `48`
- no transcription issue was found in the explicit label partition; it is exactly `{1,...,61}`
- the `D` labels really are unconstrained once `C = 1`, because `D` is adjacent only to `C`

I did not find a counterexample edge or any mismatch between the claimed graph and the checked graph.

## verify_verdict
`VERIFIED`

Reason:

- PASS 1 did not establish rediscovery within the bounded budget
- the solve artifact matches the exact intended statement
- no proof flaw was found
- the explicit witness survived independent adversarial recomputation

Harness classification after verify remains `CANDIDATE`, not `EXACT`, because Lean has not yet checked the witness.

## minimal_repair_if_any
No repair was needed.
