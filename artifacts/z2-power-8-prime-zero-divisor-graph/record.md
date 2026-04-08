# Solve Record: z2-power-8-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_2^8) prime?`
- Active slug: `z2-power-8-prime-zero-divisor-graph`
- Locked target statement: prove or disprove the exact instance-level claim that the zero-divisor graph `Γ(Z_2^8)` admits a prime labeling, i.e. a bijection from its `254` vertices to `{1,2,...,254}` such that adjacent vertices receive coprime labels.
- Using the standard subset model, the target graph is the simple graph on all nonempty proper subsets of `[8] = {1,2,3,4,5,6,7,8}`, with adjacency `A ~ B` iff `A ∩ B = ∅`.
- I am not claiming anything here about the full family `Γ(Z_2^n)` beyond the exact `n = 8` instance.

## definitions

- Vertex set: all `A ⊆ [8]` with `A ≠ ∅` and `A ≠ [8]`. Count: `2^8 - 2 = 254`.
- Edge relation: `A ~ B` iff `A` and `B` are disjoint.
- A prime labeling is a bijection `L : V -> {1,...,254}` such that `gcd(L(A), L(B)) = 1` for every edge `A ~ B`.
- Key reformulation: if a prime `p` divides two labels `L(A)` and `L(B)`, then `A` and `B` must intersect. So every prime factor may only appear on an intersecting family of vertices.
- Natural intersecting families in this graph are the stars `F_i = {A : i in A}`. Each has size `127`.
- Ambiguities / conventions:
  - The graph is simple, so no loops.
  - The empty set and the full set are excluded from the vertex set.
  - The label set is exactly `{1,...,254}` with no repetitions and no omissions.
  - Complements are also vertices, and complementary pairs are adjacent.

## approach_A

Structural / invariant approach via prime ownership.

- Assign each prime `p <= 254` to one coordinate `owner(p) in [8]`.
- For an integer label `m`, define its required coordinate set
  `R(m) = { owner(p) : p prime, p | m }`.
- If a label `m` is placed on a vertex `A` with `R(m) ⊆ A`, then every prime divisor of `m` is witnessed inside `A`.
- Therefore, if two disjoint vertices `A` and `B` received labels `m` and `n` and shared a prime factor `p`, then `owner(p)` would lie in both `A` and `B`, impossible. So a labeling satisfying `R(m) ⊆ A` for every assigned pair is automatically prime.
- This converts the problem into a containment-matching problem: can one assign each number `m in {1,...,254}` to a distinct proper nonempty subset `A` with `R(m) ⊆ A`?
- Capacity heuristic:
  - A fixed coordinate `i` is contained in `127` vertices, so the numbers whose required set contains `i` must total at most `127`.
  - A fixed pair `{i,j}` is contained in `63` vertices.
  - A fixed triple is contained in `31` vertices.
  - Numbers with many small prime factors should therefore be routed to larger subsets, while primes and prime powers can live on small subsets.
- Immediate structural observation: the even numbers are exactly `127` labels, so if `2` owns one coordinate by itself, those labels fit perfectly into one full star. That looks more like a feature than a coincidence.

## approach_B

Construction / extremal approach by slicing on coordinate `8`.

- Split the vertices into two halves:
  - `X = {A : 8 not in A}`, size `127`.
  - `Y = {A : 8 in A}`, size `127`.
- The `X` side contains the old `n = 7` graph on the nonempty proper subsets of `[7]`, plus the extra vertex `[7]`.
- The `Y` side is another copy of the nonempty subsets of `[7]`, except that the full set `[8]` is forbidden.
- This suggests trying to extend an `n = 7` labeling to `n = 8` by placing one arithmetic type on `X` and another on `Y`, for example odd versus even labels or two transformed copies of a smaller construction.
- The obstruction is that cross-edges between `X` and `Y` are not sparse: if `A in X` and `B = C union {8} in Y`, then `A ~ B` iff `A ∩ C = ∅`. So parity alone is too weak, because an even label on `Y` can still share odd prime factors with many labels on `X`.
- This route still gives useful guidance: any successful extension must control prime factors coordinate-by-coordinate, not only by a coarse bipartition.

## lemma_graph

1. The graph is the disjointness graph on nonempty proper subsets of `[8]`.
2. If a prime `p` divides labels on two vertices, those two vertices must intersect.
3. A sufficient way to guarantee item 2 is to assign each prime `p` to one coordinate `owner(p)` and place each integer `m` only on a vertex containing every coordinate in `R(m)`.
4. For any fixed `T ⊆ [8]` with `T ≠ ∅`, the number of available vertices containing `T` is `2^(8-|T|) - 1`.
5. Thus, if the ownership map keeps the required-set multiplicities small enough, the remaining task is a finite containment matching.
6. The main risk is not local coprimality but a global overload of one star or one low-codimension intersection.

## chosen_plan

- Pursue Approach A.
- First choose and justify a concrete ownership map for the prime divisors of `1,...,254`.
- Then, only if the reasoning supports it, run a small exact experiment that:
  - computes `R(m)` for each label,
  - builds the bipartite graph `m -> {A : R(m) ⊆ A}`,
  - searches for a perfect matching,
  - and checks `gcd = 1` on every disjoint pair for the resulting labeling.
- I am explicitly avoiding generic SAT / ILP / CP-SAT. If code is needed, it should only verify this containment-based construction.

## self_checks

- Statement-lock check: the target is the exact `254`-vertex instance, not the whole family.
- Model check: the subset/disjointness model matches the dossier exactly.
- Structural check: the prime-ownership lemma is sufficient, because a common prime factor would force a common owned coordinate.
- Capacity check for the chosen ownership map:
  - singleton loads are `127, 102, 68, 53, 38, 33, 27, 26`, all within the star capacity `127`;
  - the heaviest pair load is `50`, within the pair capacity `63`;
  - the heaviest triple load is `10`, within the triple capacity `31`;
  - the only size-4 required set comes from `210 = 2 * 3 * 5 * 7`, still within the size-4 capacity `15`.
- Matching check: the exact containment graph on labels versus vertices has a perfect matching of size `254`.
- Coprimality check: the matched labeling has `0` gcd violations on all disjoint vertex pairs.
- Conservatism check: the remaining gap is not arithmetic correctness of the witness but the lack of a hand proof for the perfect-matching step.

## code_used

- A single local script `check_witness.py` was used, tied directly to the ownership construction above.
- The script:
  - assigns `2` to coordinate `1`;
  - assigns the odd primes in increasing order cyclically to coordinates `2,3,4,5,6,7,8,2,3,...`;
  - computes each required set `R(m)`;
  - builds the containment graph `m -> {A : R(m) ⊆ A}`;
  - finds a perfect matching with Hopcroft-Karp;
  - checks `gcd = 1` on every disjoint pair;
  - writes the explicit matched witness to `witness.json`.
- Script output:
  - `matching = 254`
  - `coprime_ok = 1`
  - `allowed_size_min = 15`
  - `allowed_size_max = 254`
  - `required_set_size_hist = {0: 1, 1: 75, 2: 136, 3: 41, 4: 1}`

## result

- Strong solve-stage candidate for a prime labeling of `Γ(Z_2^8)` found.
- The ownership partition is:
  - coordinate `1`: `{2}`
  - coordinate `2`: `{3,23,53,83,113,157,193,233}`
  - coordinate `3`: `{5,29,59,89,127,163,197,239}`
  - coordinate `4`: `{7,31,61,97,131,167,199,241}`
  - coordinate `5`: `{11,37,67,101,137,173,211,251}`
  - coordinate `6`: `{13,41,71,103,139,179,223}`
  - coordinate `7`: `{17,43,73,107,149,181,227}`
  - coordinate `8`: `{19,47,79,109,151,191,229}`
- For each label `m in {1,...,254}`, define `R(m)` as the set of coordinates owning the prime divisors of `m`.
- The explicit witness is then the deterministic perfect matching written to `witness.json`, where each subset `A` receives a label `m` with `R(m) ⊆ A`.
- This is enough because if disjoint subsets `A` and `B` had labels with a common prime factor `p`, then `owner(p)` would lie in both `A` and `B`, contradiction.
- The script found a full matching and directly checked every edge, so the intended statement now has a strong exact-instance witness.
- Solve-stage verdict: `CANDIDATE`, not `EXACT`, because Lean is still off and the matching step is currently supported computationally rather than by a clean hand proof.

## likely_failure_points

- Verification should not trust the perfect matching just because the capacities look good; it should recompute the matching or verify the explicit `witness.json` bijection directly.
- The construction is exact but not especially human-transparent: the hardest point to audit manually is the existence and correctness of the `254 x 254` containment matching.
- If verification wants a cleaner proof, the main mathematical task is to replace the matching computation by a Hall-style or greedy monotone argument.
- Frontier novelty is still unresolved here because solve ran with web off.

## what_verify_should_check

- Re-derive the subset model and the exact vertex count `254`.
- Check whether the ownership-based reasoning is faithful: `R(m) ⊆ A` really is sufficient for edge coprimality.
- Verify the exact ownership partition above, or equivalently rerun `check_witness.py` and confirm that it reproduces the same `witness.json`.
- Check that `witness.json` is a bijection between the `254` nonempty proper subsets and the labels `{1,...,254}`.
- Check `gcd = 1` on every disjoint pair directly from `witness.json`, not only from the ownership summary.
- Because this is solve-stage only and web is off, the correct positive classification remains `CANDIDATE` until verification rechecks prior-art risk and the witness independently.

## verify_rediscovery

- PASS 1 used a bounded web audit on `2026-04-08` with exact-instance queries, alternate notation queries, the canonical Fox-Mooney source, and source-internal checks around Conjecture 4.2.
- The canonical source remains Fox and Mooney, *On prime labelings of zero-divisor graphs*, Congressus Numerantium 236 (2025), DOI `10.61091/cn236-06`.
- No instance-specific prior solution for `Γ(Z_2^8)` was found in the bounded search. The source still presents the family statement as Conjecture 4.2 and the dossier's earlier reading that the paper handles `n <= 7` but not `n = 8` remained consistent with the PASS 1 audit.
- I did not find a theorem, proposition, example, observation, or corollary in the same source that explicitly settles the exact `n = 8` instance.
- Rediscovery is therefore not established within the allowed budget.

## verify_faithfulness

- The intended statement is the exact instance claim that the disjointness graph on all nonempty proper subsets of `[8]` admits a prime labeling by `{1,...,254}`.
- The solver's construction targets exactly that graph: `254` vertices, adjacency by disjointness, and a bijection to the full label set `{1,...,254}`.
- There is no wrong-theorem drift or quantifier drift here. The witness is not for the whole family `Γ(Z_2^n)` and does not change the definition of prime labeling.
- The ownership condition `R(m) ⊆ A` is a sufficient condition for the exact graph-theoretic requirement: if disjoint `A,B` had labels with a common prime divisor `p`, then the owner coordinate of `p` would lie in both `A` and `B`, impossible.

## verify_proof

- I found no incorrect mathematical step in the exact-instance argument.
- The main proof is computational rather than hand-written: the witness is an explicit labeling certified by local checking.
- I independently reran `artifacts/z2-power-8-prime-zero-divisor-graph/check_witness.py`, which reproduced:
  - `matching = 254`
  - `coprime_ok = 1`
- I then checked `witness.json` independently of the matching routine:
  - its keys cover exactly the `254` nonempty proper subsets of `[8]`;
  - its values are exactly the labels `{1,...,254}`;
  - every assigned label's required set is contained in its assigned subset;
  - every disjoint pair of subsets has coprime assigned labels.
- So the first incorrect step is: none found.
- The remaining limitation is proof style, not correctness: the exact witness is verified computationally but not yet formalized in Lean.

## verify_adversarial

- I reran the local checker from scratch after PASS 1 with web disabled.
- I performed an independent adversarial audit directly from `witness.json` rather than trusting the ownership summary:
  - exact vertex-set match: passed;
  - exact label-set bijection: passed;
  - containment of required sets: passed for all `254` labels;
  - edgewise gcd test on all disjoint pairs: passed with `0` violations.
- I also checked the stronger failure mode "some disjoint pair shares any common factor" directly from the exported witness; no such pair exists.
- No conservative repair was needed.

## verify_verdict

- `VERIFIED`
- Classification after verification: `CANDIDATE`.
- Reason: the exact intended statement now looks correct and still frontier-novel within the bounded rediscovery pass, but it is not `EXACT` because Lean has not yet checked the witness.
- `lean_ready = true` because the witness is explicit, finite, and already independently rechecked.

## minimal_repair_if_any

- None.

## lean_build

- `lake build AutoMath.Z2Power8` succeeded after the worker timeout, taking 288 seconds in the local Lean backend.
- The exact theorem file is now mirrored at `artifacts/z2-power-8-prime-zero-divisor-graph/lean/AutoMath/Z2Power8.lean`.

## lean_axioms

- A standalone `#print axioms` audit for `AutoMath.Z2Power8.z2_power_8_zeroDivisorGraph_prime`, `AutoMath.Z2Power8.z2_power_8_zeroDivisorGraph_prime_checked`, and `AutoMath.Z2Power8.z2_power_8_zeroDivisorGraph_prime_explicit` reported only the standard Lean axioms `[propext, Classical.choice, Quot.sound]`.

## lean_verdict

- `EXACT`
- The exact intended statement for `Γ(Z_2^8)` is now Lean-checked in the local AutoMath backend.
