# Solve Record: z5-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_5 × Z_25) prime?`
- Active slug: `z5-z25-prime-zero-divisor-graph`
- Locked target statement: prove or disprove the exact instance-level claim that the zero-divisor graph `Γ(Z_5 × Z_25)` admits a prime labeling, i.e. a bijection from its `44` vertices to `{1,2,...,44}` such that adjacent vertices receive coprime labels.
- I am not solving the full family `Γ(Z_p × Z_{q^2})`; only the exact case `p = q = 5`.

## definitions

- Write vertices as pairs `(a,b)` with `a in Z_5` and `b in Z_25`.
- In `Z_5`, the only zero-divisor is `0`.
- In `Z_25`, the zero-divisors are exactly the multiples of `5`, namely `0,5,10,15,20`.
- Therefore the nonzero zero-divisors of `Z_5 x Z_25` are exactly the nonzero pairs with either `a = 0` or `b` a multiple of `5`.
- Split the `44` vertices into four natural classes:
  - `A = {(0,u) : u in Z_25^x}` where `u` is not divisible by `5`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(1,0),(2,0),(3,0),(4,0)}`, size `4`.
  - `D = {(a,5t) : a in {1,2,3,4}, t in {1,2,3,4}}`, size `16`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 5` and `bd = 0 mod 25`.
- Ambiguities / conventions:
  - The graph is simple: no loops.
  - The zero element `(0,0)` is excluded from the vertex set.
  - A prime labeling is on vertices, not on associate classes or orbit classes.
  - Vertices inside the same class have identical neighborhoods, so labels may be assigned in any order within a class once the class label set is fixed.

## approach_A

Structural / invariant decomposition.

- If `x,y in A`, then their second coordinates are units mod `25`, so `xy` cannot have second coordinate `0`; hence there are no `A-A` edges.
- If `x in A` and `y in C`, then `0 * a = 0 mod 5` and `u * 0 = 0 mod 25`, so every `A` vertex is adjacent to every `C` vertex. Thus `A-C` is complete bipartite.
- If `x in A` and `y in B or D`, then the second-coordinate product is `u * 5t`, which is nonzero mod `25` because `u` is a unit. So there are no `A-B` or `A-D` edges.
- If `x,y in B`, then both second coordinates are nonzero multiples of `5`, so their product is `0 mod 25`, and both first coordinates are `0`; thus `B` induces `K_4`.
- If `x in B` and `y in C`, then `(0,5t)(a,0) = (0,0)`, so `B-C` is complete bipartite.
- If `x in B` and `y in D`, then again the first-coordinate product is `0` and the second-coordinate product is `5t * 5s = 0 mod 25`, so `B-D` is complete bipartite.
- If `x,y in C`, or `x in C` and `y in D`, or `x,y in D`, then both first coordinates are nonzero in `Z_5`, so their first-coordinate product is nonzero mod `5`; hence there are no such edges.

So the only edge types are:

- `A-C`, with `20 * 4 = 80` edges.
- `B-B`, with `binom(4,2) = 6` edges.
- `B-C`, with `4 * 4 = 16` edges.
- `B-D`, with `4 * 16 = 64` edges.

Total predicted edge count: `80 + 6 + 16 + 64 = 166`.

## approach_B

Construction / extremal coprimality packing.

- Every vertex of `C` is adjacent to every vertex of `A union B`, so each label placed on `C` should have as few forbidden multiples in `1,...,44` as possible.
- Large odd primes are ideal here. Choose the `C` labels as `11,23,29,31`.
- The only numbers in `1,...,44` that fail to be coprime to at least one of these are
  `11,22,23,29,31,33,44`.
  So if all labels on `A union B` avoid exactly those seven numbers, then all `A-C` and `B-C` edges are automatically good.
- Next, `B` is a `4`-clique and is also adjacent to all of `D`, so labels on `B` must be pairwise coprime and should also create very few restrictions on `D`.
- Choose the `B` labels as `1,37,41,43`.
- These are pairwise coprime, and among `1,...,44` the only numbers not coprime to one of `37,41,43` are the numbers `37,41,43` themselves.
- Therefore any labels left over after fixing `A union B union C` may safely go on `D`, as long as `37,41,43` stay on `B`.

This suggests a full labeling by classes.

## lemma_graph

1. The vertex set is exactly `A disjoint-union B disjoint-union C disjoint-union D` with sizes `20,4,4,16`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`, with no other edges.
3. If every label on `A union B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. Therefore an explicit classwise partition of `{1,...,44}` satisfying those arithmetic conditions is enough to prove prime labelability.

## chosen_plan

- Use Approach A to lock the graph structure exactly.
- Use Approach B to build a classwise witness that only has to satisfy three coprimality checks: `A` versus `C`, `B` versus `C`, and `D` versus `B`, plus pairwise coprimality inside `B`.
- After the witness is written down, run one tiny local checker tied to this exact instance and this exact labeling.

## self_checks

- Statement-lock check: this is the exact `44`-vertex instance `Γ(Z_5 × Z_25)`.
- Counting check: `20 + 4 + 4 + 16 = 44`, matching the dossier.
- Structural check: every forbidden edge type fails already in the first coordinate or second coordinate as described above.
- Edge-count check: the class decomposition predicts exactly `166` edges.
- Arithmetic-plan check: choosing `C = {11,23,29,31}` forbids only seven labels on `A union B`, and choosing `B = {1,37,41,43}` imposes almost no restriction on `D`.
- Local-checker check: direct enumeration confirmed `44` vertices, `166` edges, edge-type counts `A-C = 80`, `B-B = 6`, `B-C = 16`, `B-D = 64`, and `0` coprimality violations.

## code_used

- A tiny local checker `check_witness.py` is included for this artifact.
- It enumerates the `44` nonzero zero-divisors of `Z_5 x Z_25`, generates edges directly from the ring multiplication rule, checks that the proposed labeling is a bijection onto `{1,...,44}`, and tests `gcd = 1` on every edge.
- Output from the checker:
  - `vertex_count = 44`
  - `edge_count = 166`
  - `edge_type_counts = {A-C: 80, B-B: 6, B-C: 16, B-D: 64}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

Candidate exact witness:

- Put the four labels `11,23,29,31` on `C = {(1,0),(2,0),(3,0),(4,0)}` in any order.
- Put the four labels `1,37,41,43` on `B = {(0,5),(0,10),(0,15),(0,20)}` in any order.
- Put the twenty labels
  `2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,24`
  on the twenty vertices of `A` in any order.
- Put the remaining sixteen labels
  `22,25,26,27,28,30,32,33,34,35,36,38,39,40,42,44`
  on the sixteen vertices of `D` in any order.

Proof that this works:

- `B-B` edges:
  the labels `1,37,41,43` are pairwise coprime, so the clique on `B` is labeled correctly.
- `A-C` edges:
  each label on `C` is one of the primes `11,23,29,31`.
  No label used on `A` is divisible by any of those primes, so every `A-C` pair has gcd `1`.
- `B-C` edges:
  the labels on `B` are `1,37,41,43`, each coprime to `11,23,29,31`.
  So every `B-C` edge is good.
- `B-D` edges:
  every label on `D` is at most `44` and is not equal to `37,41,43`.
  Since `37,41,43` are primes greater than `22`, they have no other positive multiples at most `44`.
  Hence every label on `D` is coprime to `37,41,43`, and of course to `1`.
  So every `B-D` edge is good.
- There are no other edges by the structural decomposition.

Therefore this is a prime labeling of `Γ(Z_5 × Z_25)`.

Solve-stage verdict:

- The intended statement appears true.
- Because Lean is still off in this stage, the correct solve-stage classification is `CANDIDATE`, not `EXACT`.

## likely_failure_points

- A mistaken classification of the zero-divisor vertices would break both the edge count and the witness.
- The key graph fact is that `A` has edges only to `C`, while `D` has edges only to `B`; verification should re-derive that from the ring law, not trust the summary.
- The argument that `37,41,43` create no extra conflicts on `D` relies on the bound `44 < 2 * 37`.
- The construction is exact for this instance, but solve has not yet done the bounded prior-art audit, so the harness must still remain conservative about frontier novelty.

## what_verify_should_check

- Recompute the `44` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the `166`-edge class pattern `A-C`, `B-B`, `B-C`, `B-D`.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,44}`.
- Check coprimality on every actual edge, preferably from the explicit ring graph rather than only from the class summary.
- Run the bounded rediscovery / prior-art search before any Lean work.
- If the witness survives verification, this looks Lean-ready as a finite exact-instance construction.

## verify_rediscovery

- PASS 1 used a bounded web audit centered on the exact instance, alternate ASCII and family notation, the canonical paper, and later citation/status checks.
- The search returned the canonical Fox-Mooney 2025 paper and generic archive/index pages, but I did not find any later paper, theorem, proposition, example, observation, corollary, or discussion explicitly settling the exact instance `Γ(Z_5 × Z_25)`.
- The nearby solved results in the canonical source appear to concern other families and do not directly imply this `p = q = 5` case.
- Rediscovery is therefore not established on the available budget.

## verify_faithfulness

- The solver's claim matches the intended statement exactly: a prime labeling of the full zero-divisor graph `Γ(Z_5 × Z_25)` on all `44` nonzero zero-divisors.
- I found no quantifier drift, definition change, or replacement of the target by a weaker proxy.
- The proof is instance-level only and does not overclaim the full family `Γ(Z_p × Z_{q^2})`.

## verify_proof

- I re-derived the vertex partition from the ring law. The nonzero zero-divisors are exactly the nonzero pairs `(a,b)` with `a = 0` or `5 | b`, giving the claimed class sizes `20,4,4,16`.
- I rechecked adjacency from `(a,b)(c,d) = (0,0)` iff `ac = 0 mod 5` and `bd = 0 mod 25`. This yields exactly the edge types `A-C`, `B-B`, `B-C`, and `B-D`, with no others.
- Given that structure, the labeling argument is sound:
  - `B = {1,37,41,43}` is pairwise coprime, so the `B` clique is valid.
  - `C = {11,23,29,31}` is coprime to every `A` and `B` label used.
  - Every `D` label is different from `37,41,43`, and no multiple of those primes besides themselves lies in `{1,...,44}`, so all `B-D` edges are coprime.
- I found no incorrect step.

## verify_adversarial

- I reran `python3 artifacts/z5-z25-prime-zero-divisor-graph/check_witness.py`.
- The checker again reported:
  - `vertex_count = 44`
  - `edge_count = 166`
  - `edge_type_counts = {'A-C': 80, 'B-B': 6, 'B-C': 16, 'B-D': 64}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`
- The code directly enumerates vertices and edges from the ring multiplication rule, so it supports the exact mathematical claim rather than a surrogate claim.

## verify_verdict

- `VERIFIED`
- The candidate witness survives skeptical checking on faithfulness, proof correctness, and adversarial recomputation.
- This is still not `EXACT` because no Lean proof has been completed.
- Current harness classification should remain `CANDIDATE`, with `lean_ready = true`.

## minimal_repair_if_any

- None. I did not need to patch the proof or witness.

## lean_statement

- Exact Lean target theorem:

```lean
theorem z5_z25_zeroDivisorGraph_prime : ∃ f : Vertex → Label, IsPrimeLabeling f
```

- Faithfulness audit of the statement:
  - `Raw = Fin 5 × Fin 25` encodes the standard representatives of `Z_5 × Z_25`.
  - `IsVertex` is exactly the nonzero zero-divisor predicate: `(a,b) ≠ (0,0)` and `a = 0 ∨ 5 ∣ b`.
  - `Adj` is exactly the simple zero-product adjacency relation: distinct vertices with coordinatewise products `0 mod 5` and `0 mod 25`.
  - `Label = Fin 44` is the exact label set `{1,…,44}` via `labelValue i = i + 1`.
  - So the theorem is the intended instance-level statement that `Γ(Z_5 × Z_25)` admits a prime labeling, not a proxy graph.

## lean_skeleton

- Define the exact encoded graph:
  - `Raw`, `IsVertex`, `Vertex`, coordinate projections, and `Adj`.
- Define the exact witness:
  - `Label := Fin 44`, `labelValue`, and `rawLabel` matching the verified classwise labeling from `check_witness.py`.
- Reduce the proof to two finite checks:
  - `raw_label_injective_on_vertices`
  - `raw_label_edgeCoprime`
- Discharge those checks by exhaustive `decide +kernel` over the finite search space.
- Lift the raw facts to `label_injective` and `label_edgeCoprime`, then conclude `IsPrimeLabeling label`.

## lean_result

- Lean source written to `lean/AutoMath/Z5Z25.lean` and mirrored byte-for-byte at `artifacts/z5-z25-prime-zero-divisor-graph/lean/Z5Z25.lean`.
- The checked module imports into the local AutoMath backend through `lean/AutoMath.lean`.
- Build results:
  - `lake build AutoMath.Z5Z25` succeeded.
  - `lake build` succeeded.
- Axiom audit:
  - `lake env lean ../artifacts/z5-z25-prime-zero-divisor-graph/lean/Z5Z25AxiomAudit.lean` succeeded.
  - `#print axioms` for `z5_z25_zeroDivisorGraph_prime`, `z5_z25_zeroDivisorGraph_prime_checked`, and `z5_z25_zeroDivisorGraph_prime_explicit` reported only the standard Lean/mathlib axioms `[propext, Classical.choice, Quot.sound]`.
  - No `sorry`, `admit`, or `sorryAx` was found in the source or the printed axiom audit.
- Lean conclusion:
  - The exact intended statement is fully formalized and checked in the local Lean backend.
  - The correct post-Lean harness classification is `EXACT`.

## lean_blockers

- No proof blocker remained.
- Operational limitation only: `lean4checker --fresh` is not installed on this machine, so that optional fresh-kernel audit could not be run.
