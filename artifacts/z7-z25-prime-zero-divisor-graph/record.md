# Solve Record: z7-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Gamma(Z_7 x Z_25) prime?`
- Active slug: `z7-z25-prime-zero-divisor-graph`
- Locked target statement: prove or disprove the exact instance-level claim that the zero-divisor graph `Gamma(Z_7 x Z_25)` admits a prime labeling, meaning a bijection from its `54` vertices to `{1,2,...,54}` such that adjacent vertices receive coprime labels.
- I am solving only the exact case `Z_7 x Z_25`, not the full family `Gamma(Z_p x Z_(q^2))`.

## definitions

- Write vertices as pairs `(a,b)` with `a in Z_7` and `b in Z_25`.
- In `Z_7`, the only zero-divisor is `0`.
- In `Z_25`, the zero-divisors are exactly the multiples of `5`, namely `0,5,10,15,20`.
- Therefore the nonzero zero-divisors of `Z_7 x Z_25` are exactly the nonzero pairs with either `a = 0` or `5 | b`.
- Split the `54` vertices into four natural classes:
  - `A = {(0,u) : u in Z_25^x}`, where `u` is not divisible by `5`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a in {1,2,3,4,5,6}}`, size `6`.
  - `D = {(a,5t) : a in {1,2,3,4,5,6}, t in {1,2,3,4}}`, size `24`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 7` and `bd = 0 mod 25`.
- Ambiguities / conventions to lock:
  - The graph is simple, so there are no loops.
  - The zero element `(0,0)` is excluded from the vertex set.
  - The labeling is on individual vertices, not on orbit classes.
  - Since vertices inside each class have the same neighborhood, once a classwise label set is found the labels may be assigned inside the class in any order.

## approach_A

Structural / invariant decomposition.

- If `x,y in A`, then both second coordinates are units mod `25`, so their second-coordinate product is nonzero mod `25`. Hence there are no `A-A` edges.
- If `x in A` and `y in C`, then `0 * a = 0 mod 7` and `u * 0 = 0 mod 25`, so every `A` vertex is adjacent to every `C` vertex. Thus `A-C` is complete bipartite.
- If `x in A` and `y in B or D`, then the second-coordinate product is `u * 5t`, which is a nonzero multiple of `5` mod `25`, not `0`. So there are no `A-B` or `A-D` edges.
- If `x,y in B`, then their first coordinates are both `0` and their second coordinates are nonzero multiples of `5`, so the product is `0` in both coordinates. Thus `B` induces `K_4`.
- If `x in B` and `y in C`, then `(0,5t)(a,0) = (0,0)`, so `B-C` is complete bipartite.
- If `x in B` and `y in D`, then the first-coordinate product is `0`, and the second-coordinate product is `5t * 5s = 25ts = 0 mod 25`, so `B-D` is complete bipartite.
- If `x,y in C`, or `x in C` and `y in D`, or `x,y in D`, then both first coordinates are nonzero in the field `Z_7`, so their first-coordinate product is nonzero mod `7`. Hence there are no `C-C`, `C-D`, or `D-D` edges.

So the only edge types are:

- `A-C`, with `20 * 6 = 120` edges.
- `B-B`, with `binom(4,2) = 6` edges.
- `B-C`, with `4 * 6 = 24` edges.
- `B-D`, with `4 * 24 = 96` edges.

Total predicted edge count: `120 + 6 + 24 + 96 = 246`.

## approach_B

Construction / extremal / contradiction approach.

- Every vertex of `C` is adjacent to every vertex of `A union B`, so labels on `C` should create as few divisibility exclusions as possible on the other `24` labels used there.
- A natural choice is to put six large primes on `C`, all greater than `27`. Then within `{1,...,54}` the only multiples of those primes are the primes themselves.
- Choose
  `C = {29,31,37,41,43,47}`.
  Then a label on `A union B` only has to avoid these six numbers.
- The class `B` is a `4`-clique and is also adjacent to all of `D`, so the labels on `B` must be pairwise coprime and should collectively exclude only a manageable set of labels from `D`.
- A compact choice is
  `B = {1,11,13,17}`.
  These are pairwise coprime.
- A label on `D` must be coprime to `11,13,17`, so the only forbidden labels in `{1,...,54}` are the multiples
  - of `11`: `11,22,33,44`,
  - of `13`: `13,26,39,52`,
  - of `17`: `17,34,51`.
- Excluding the `B` labels themselves, the extra numbers forbidden on `D` are
  `{22,26,33,34,39,44,51,52}`.
- This is still workable, because `A` has `20` slots and only needs to avoid the six `C` labels. So `A` can absorb these eight `B`-conflicting labels, along with twelve more harmless labels.

This suggests the explicit classwise partition:

- `C` gets `29,31,37,41,43,47`.
- `B` gets `1,11,13,17`.
- `A` gets
  `2,3,4,5,6,7,8,9,10,12,14,15,22,26,33,34,39,44,51,52`.
- `D` gets the remaining `24` labels
  `16,18,19,20,21,23,24,25,27,28,30,32,35,36,38,40,42,45,46,48,49,50,53,54`.

## lemma_graph

1. The vertex set is exactly `A disjoint-union B disjoint-union C disjoint-union D` with sizes `20,4,6,24`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`, with no other edges.
3. If every label on `A union B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. Therefore an explicit partition of `{1,...,54}` into class label sets with those arithmetic properties proves prime labelability.

## chosen_plan

- Use Approach A to lock the graph structure exactly.
- Use Approach B to build a concrete witness by classwise number placement.
- The key arithmetic idea is asymmetric packing:
  - give `C` large primes so `A union B` only avoids a tiny set,
  - give `B` pairwise coprime labels with only a moderate forbidden-multiple set,
  - absorb those forbidden multiples into `A`,
  - leave `D` as the clean complement.
- Because this is an exact finite instance, a tiny direct checker is justified after the reasoning stage to validate the explicit witness edge-by-edge.

## self_checks

- Statement-lock check: this is the exact `54`-vertex instance `Gamma(Z_7 x Z_25)`.
- Counting check: `20 + 4 + 6 + 24 = 54`, matching the dossier.
- Structural check: every forbidden edge type already fails in one coordinate.
- Edge-count check: the decomposition predicts exactly `246` edges.
- Arithmetic-plan check:
  - the `C` labels are six primes greater than `27`, so among `1,...,54` their only multiples are themselves;
  - the `B` labels are pairwise coprime;
  - the listed `D` labels avoid every multiple of `11`, `13`, and `17`.
- Tiny-checker check: direct enumeration confirmed `54` vertices, `246` edges, edge-type counts `A-C = 120`, `B-B = 6`, `B-C = 24`, `B-D = 96`, bijection onto `{1,...,54}`, and `0` coprimality violations.

## code_used

- A tiny local checker `check_witness.py` was used after the reasoning was written.
- It enumerates the `54` nonzero zero-divisors of `Z_7 x Z_25`, generates edges directly from the ring multiplication rule, checks that the proposed labeling is a bijection onto `{1,...,54}`, and tests `gcd = 1` on every edge.
- Output from the checker:
  - `vertex_count = 54`
  - `edge_count = 246`
  - `edge_type_counts = {A-C: 120, B-B: 6, B-C: 24, B-D: 96}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

Current best solve-stage candidate:

- Put the labels `29,31,37,41,43,47` on `C` in any order.
- Put the labels `1,11,13,17` on `B` in any order.
- Put the labels
  `2,3,4,5,6,7,8,9,10,12,14,15,22,26,33,34,39,44,51,52`
  on the twenty vertices of `A` in any order.
- Put the labels
  `16,18,19,20,21,23,24,25,27,28,30,32,35,36,38,40,42,45,46,48,49,50,53,54`
  on the twenty-four vertices of `D` in any order.

Reason this should work:

- `B-B` edges:
  `1,11,13,17` are pairwise coprime.
- `A-C` and `B-C` edges:
  each `C` label is a prime greater than `27`, so within `{1,...,54}` the only positive multiple of that prime is itself. No label used on `A union B` equals any of those six primes, so every `A-C` and `B-C` pair is coprime.
- `B-D` edges:
  every `D` label avoids the multiples of `11`, `13`, and `17` up to `54`, so every `D` label is coprime to every label in `B`.
- There are no other edges.

Therefore this is a prime labeling of `Gamma(Z_7 x Z_25)`.

Solve-stage verdict:

- The intended statement appears true for this exact instance.
- Because Lean is still off in this stage, the correct solve-stage classification is `CANDIDATE`, not `EXACT`.

## likely_failure_points

- A mistaken vertex-class decomposition would invalidate both the edge count and the witness.
- The key arithmetic claim is that the listed `D` set contains no multiples of `11`, `13`, or `17`; verification should recompute this rather than trust the prose.
- The `A-C` and `B-C` arguments rely on the fact that all chosen `C` labels are primes greater than `27`, so their only multiples in `{1,...,54}` are themselves.
- Novelty is still unresolved in solve; even a correct exact witness should remain below `EXACT` until later stages.

## what_verify_should_check

- Recompute the `54` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,54}`.
- Check coprimality on every actual edge from the explicit ring graph.
- Audit the exact instance for rediscovery before any Lean work.
- If the witness survives, this should be lean-ready as a finite exact-instance construction.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact instance, alternate notation, the canonical source, and internal theorem/proposition/example/corollary checks.
- Exact-instance searches on `Gamma(Z_7 x Z_25)`, `Gamma(Z_7 x Z_(5^2))`, `Z_7 x Z_25` with `zero-divisor graph`, and related family notation did not produce a theorem, proposition, example, observation, or corollary settling this exact case.
- The canonical source still appears to leave the family `Gamma(Z_p x Z_(q^2))` as Conjecture 4.4 rather than a proved theorem. In the bounded audit, I did not find a later paper or status page proving the exact `p = 7, q = 5` instance or giving a family theorem that directly implies it.
- Verdict for PASS 1: no rediscovery established within budget.
- Short note on current proof status: independent of novelty, the current witness appears mathematically coherent and computationally valid.

## verify_faithfulness

- The solve record stays locked to the exact intended statement: existence of a prime labeling for the zero-divisor graph `Gamma(Z_7 x Z_25)`.
- The graph definition used in solve matches the dossier definition: nonzero zero-divisors of `Z_7 x Z_25`, simple graph, adjacency by zero product in both coordinates, labels a bijection onto `{1,...,54}`.
- The argument does not drift to a weaker family-level statement or to a relabeled quotient/orbit graph. It constructs a labeling for the full `54`-vertex graph itself.
- No quantifier drift found. The claimed result is exactly "this specific graph is prime."

## verify_proof

- I recomputed the structural decomposition from the ring definition. The vertex counts are `|A| = 20`, `|B| = 4`, `|C| = 6`, `|D| = 24`, totaling `54`.
- I independently recomputed edge types from ring multiplication. The only edges are `A-C`, `B-B`, `B-C`, and `B-D`, with counts `120`, `6`, `24`, and `96` respectively, total `246`.
- Given that edge pattern, the proof reduces correctly to three arithmetic obligations:
  - every label on `A union B` is coprime to every label on `C`;
  - the `B` labels are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the proposed label sets:
  - `C = {29,31,37,41,43,47}` are primes greater than `27`, so their only multiples in `{1,...,54}` are themselves, and none of those primes lies in `A union B`;
  - `B = {1,11,13,17}` is pairwise coprime;
  - `D` omits all multiples of `11`, `13`, and `17` up to `54`.
- First incorrect step found: none.

## verify_adversarial

- I reran the provided checker `artifacts/z7-z25-prime-zero-divisor-graph/check_witness.py`. It reported:
  - `vertex_count = 54`
  - `edge_count = 246`
  - `edge_type_counts = {'A-C': 120, 'B-B': 6, 'B-C': 24, 'B-D': 96}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`
- I also ran an independent one-off computation outside the checker logic to verify:
  - the four label sets are disjoint and cover exactly `{1,...,54}`;
  - the class counts are `20,4,6,24`;
  - the edge types match the claimed decomposition;
  - no hidden gcd violation appears in the classwise obligations.
- I did not find an adversarial break of the candidate construction.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- The exact intended statement appears to be proved correctly by the current explicit witness, and the bounded rediscovery pass did not show that this exact result is already in the literature.
- Because Lean has not yet been run, the harness classification must remain `CANDIDATE`, not `EXACT`.
- `lean_ready = true`

## minimal_repair_if_any

- None. No conservative patch to the mathematical content was needed.

## lean_statement

- Backend file: `lean/AutoMath/Z7Z25.lean`
- Main exact theorem:
  `AutoMath.Z7Z25.z7_z25_zeroDivisorGraph_prime :
  ∃ f : Vertex → Label, IsPrimeLabeling f`
- Explicit witness theorem:
  `AutoMath.Z7Z25.z7_z25_zeroDivisorGraph_prime_explicit :
  ∃ f : Vertex → Label,
    Function.Bijective f ∧
    (∀ x, 1 ≤ labelValue (f x) ∧ labelValue (f x) ≤ 54) ∧
    (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y)))`
- Faithfulness audit:
  `Vertex` is exactly the subtype of nonzero zero-divisors of `Fin 7 × Fin 25`;
  `Adj` is exactly distinctness plus zero product in both coordinates modulo `7` and `25`;
  `Label = Fin 54` is interpreted as `{1,...,54}` by `labelValue i = i + 1`.
  This matches the intended statement without weakening to a quotient graph, orbit graph, or family-level claim.

## lean_skeleton

- Define `Raw := Fin 7 × Fin 25`, then define `IsVertex` as the exact nonzero zero-divisor predicate for the intended ring instance.
- Define `Vertex := {x : Raw // IsVertex x}` and `Adj` by exact coordinatewise zero-product conditions modulo `7` and `25`.
- State the exact target theorem first:
  `z7_z25_zeroDivisorGraph_prime : ∃ f : Vertex → Label, IsPrimeLabeling f`.
- Encode the explicit witness as `rawLabel : Raw → Fin 54` by case split on the `54` valid raw representatives.
- Prove finite injectivity of the witness on vertices with `raw_label_injective_on_vertices`.
- Prove edgewise coprimality of the witness with `raw_label_edgeCoprime`.
- Assemble the final exact theorem from these two ingredients via `Fintype.bijective_iff_injective_and_card`.

## lean_result

- Lean module added and mirrored:
  `lean/AutoMath/Z7Z25.lean`
  `artifacts/z7-z25-prime-zero-divisor-graph/lean/Z7Z25.lean`
- Axiom audit file added:
  `artifacts/z7-z25-prime-zero-divisor-graph/lean/Z7Z25AxiomAudit.lean`
- Command run: `lake build AutoMath.Z7Z25`
  Result: success.
- Command run: `lake build`
  Result: success.
- Command run:
  `lake env lean ../artifacts/z7-z25-prime-zero-divisor-graph/lean/Z7Z25AxiomAudit.lean`
  Result:
  `z7_z25_zeroDivisorGraph_prime`,
  `z7_z25_zeroDivisorGraph_prime_checked`, and
  `z7_z25_zeroDivisorGraph_prime_explicit`
  each depend only on `[propext, Classical.choice, Quot.sound]`.
- Additional audit:
  `rg -n "\\bsorry\\b|\\badmit\\b|sorryAx" lean/AutoMath/Z7Z25.lean artifacts/z7-z25-prime-zero-divisor-graph/lean/Z7Z25.lean artifacts/z7-z25-prime-zero-divisor-graph/lean/Z7Z25AxiomAudit.lean`
  returned no matches.
- Lean verdict:
  the exact intended statement for `Gamma(Z_7 x Z_25)` is fully formalized and checked in the repo Lean backend, so this run now earns `classification = "EXACT"` with `lean_complete = true`.

## lean_blockers

- None for the theorem itself.
- Extra audit limitation only:
  `lean4checker --fresh` is unavailable on this machine, so that optional fresh-kernel pass could not be run.
