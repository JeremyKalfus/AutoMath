# Solve Record: Is the zero-divisor graph `Γ(Z_5 × Z_5 × Z_3)` prime?

## statement_lock
Intended statement: the zero-divisor graph `Γ(Z_5 × Z_5 × Z_3)` admits a prime labeling, meaning a bijection from its `42` vertices to `{1,2,...,42}` such that adjacent vertices receive coprime labels.

I will use the standard graph on nonzero zero-divisors of the ring `Z_5 × Z_5 × Z_3`, with coordinatewise multiplication and adjacency defined by product `0`.

## definitions
Write a vertex by its support, meaning the set of coordinates in which it is nonzero.

For `R = Z_5 × Z_5 × Z_3`, a nonzero zero-divisor has support equal to one of the six nonempty proper subsets of `{1,2,3}`:

- `V1 = {(a,0,0) : a in Z_5^×}`, size `4`
- `V2 = {(0,b,0) : b in Z_5^×}`, size `4`
- `V3 = {(0,0,c) : c in Z_3^×}`, size `2`
- `V12 = {(a,b,0) : a,b in Z_5^×}`, size `16`
- `V13 = {(a,0,c) : a in Z_5^×, c in Z_3^×}`, size `8`
- `V23 = {(0,b,c) : b in Z_5^×, c in Z_3^×}`, size `8`

This gives `4 + 4 + 2 + 16 + 8 + 8 = 42` vertices.

Because multiplication is coordinatewise and each nonzero field element stays nonzero under multiplication, two vertices are adjacent exactly when their supports are disjoint.

Hence the only edge families are:

- `V1` joined completely to `V2`, `V3`, `V23`
- `V2` joined completely to `V1`, `V3`, `V13`
- `V3` joined completely to `V1`, `V2`, `V12`

There are no other edges.

Ambiguities checked:

- I am using `Γ(R)` on nonzero zero-divisors only, not including the zero element.
- “Prime labeling” is the usual coprime-on-edges bijection to `{1,...,|V|}`.
- Support classes are independent sets because equal supports are never disjoint.

## approach_A
Structural / invariant approach.

Exploit the support decomposition. Since adjacency depends only on disjoint support, the graph is a blow-up of a six-vertex support graph. So it is enough to assign disjoint label blocks to the six support classes and verify only the six complete bipartite edge families above.

The key invariant is prime-support separation on the core classes `V1`, `V2`, `V3`:

- every label on `V1` must be coprime to every label on `V2` and `V3`
- every label on `V2` must be coprime to every label on `V3`

So it is natural to choose:

- `V1` from numbers using only primes `2` and `3`
- `V2` from numbers using only primes `5` and `13` plus possibly `1`
- `V3` from numbers using only primes `7` and `11`

These prime sets are pairwise disjoint, so the three core complete bipartite pieces are automatically safe. Then the satellite classes only need unary avoidance conditions:

- `V23` must avoid primes `2,3`
- `V13` must avoid primes `5,13`
- `V12` must avoid primes `7,11`

This suggests a full partition of `{1,...,42}` by admissibility.

Self-check after Approach A:

- The support-class reduction is exact, not heuristic.
- If I can partition the labels into the six class sizes with those avoidance rules, that is already a full proof.

## approach_B
Construction / extremal / contradiction approach.

Try to place the hardest composite labels first and force the rest.

If `V1` is chosen as multiples of `6`, then any label in `V23` must be odd and not divisible by `3`. Among `{1,...,42}`, there are only fourteen such labels, and once `V2` and `V3` consume `1,5,7,11,13,25`, the remaining admissible labels are exactly:

- `17,19,23,29,31,35,37,41`

That already gives a clean forced `8`-set for `V23`. Then the remaining `24` labels can be split by the two simpler filters:

- `V13`: not divisible by `5` or `13`
- `V12`: not divisible by `7` or `11`

This is promising because the `V12` filter is very loose, so `V13` can absorb the few labels excluded from `V12`, namely the remaining multiples of `7` or `11`.

Self-check after Approach B:

- The forced `V23` set is a good sign because it removes guesswork.
- The main risk is bookkeeping: I still need an exact partition of the remaining `24` labels into `8 + 16`.

## lemma_graph
Lemma skeleton:

1. Every nonzero zero-divisor in `Z_5 × Z_5 × Z_3` has one of the six support types above.
2. Two vertices are adjacent iff their supports are disjoint.
3. Therefore the graph is determined by the six complete bipartite edge families listed in `definitions`.
4. If each class is assigned a label set of the correct size, the six sets partition `{1,...,42}`, and every pair of labels across each adjacent class pair is coprime, then the resulting bijection is a prime labeling.
5. Exhibit such six label sets.

## chosen_plan
Use Approach A with the explicit partition discovered through Approach B.

Assign labels by support class as follows:

- `V1 <- {6,12,18,24}`
- `V2 <- {1,5,13,25}`
- `V3 <- {7,11}`
- `V12 <- {2,8,9,10,15,16,20,26,27,30,32,34,36,38,39,40}`
- `V13 <- {3,4,14,21,22,28,33,42}`
- `V23 <- {17,19,23,29,31,35,37,41}`

These six sets have sizes `4,4,2,16,8,8` respectively and partition `{1,...,42}`.

Now check all adjacent class pairs.

1. `V1` with `V2`:
Every label in `V1` has prime factors contained in `{2,3}`.
Every non-`1` label in `V2` has prime factors contained in `{5,13}`.
So all cross-gcds are `1`.

Self-check:

- `6,12,18,24` are indeed not divisible by `5` or `13`.

2. `V1` with `V3`:
`7` and `11` are coprime to each of `6,12,18,24`.

Self-check:

- No hidden issue here; these are direct gcd checks.

3. `V1` with `V23`:
Each label in `V23` is odd and not divisible by `3`, hence coprime to every label in `V1`, whose only prime factors are `2` and `3`.

Self-check:

- `35` is the only composite in `V23`, and `gcd(35,6) = gcd(35,12) = gcd(35,18) = gcd(35,24) = 1`.

4. `V2` with `V3`:
The labels `1,5,13,25` are all coprime to `7` and `11`.

Self-check:

- `25` still causes no issue since neither `7` nor `11` divides it.

5. `V2` with `V13`:
Each label in `V13` avoids divisibility by `5` and `13`, so it is coprime to every label in `V2`.

Self-check:

- The largest label `42` is allowed here because it is divisible by `2,3,7` only.

6. `V3` with `V12`:
Each label in `V12` avoids divisibility by `7` and `11`, so it is coprime to both `7` and `11`.

Self-check:

- This is the loosest constraint, and every listed `V12` label satisfies it.

Therefore every edge joins two coprime labels, so this is a prime labeling of `Γ(Z_5 × Z_5 × Z_3)`.

## self_checks
- Vertex count check: `42` labels for `42` vertices.
- Partition check: each number from `1` to `42` appears exactly once in the six displayed sets.
- Graph-model check: adjacency was reduced to disjoint support, which is exact in a direct product of fields.
- Proof-risk check: the only realistic failure mode is a transcription mistake in the displayed partition, not a gap in the structural argument.

## code_used
Minimal code is justified only as witness verification. After the reasoning and explicit construction were complete, a tiny checker was used to confirm:

- the six label sets partition `{1,...,42}`
- every cross-edge between adjacent support classes has gcd `1`

No search, optimization, SAT, ILP, CP-SAT, or brute force was used.

## result
Solve-stage outcome: explicit prime-labeling candidate found.

Candidate labeling by support class:

- `V1 = {6,12,18,24}`
- `V2 = {1,5,13,25}`
- `V3 = {7,11}`
- `V12 = {2,8,9,10,15,16,20,26,27,30,32,34,36,38,39,40}`
- `V13 = {3,4,14,21,22,28,33,42}`
- `V23 = {17,19,23,29,31,35,37,41}`

Classification for solve: `CANDIDATE`.

## likely_failure_points
- A convention mismatch in the zero-divisor graph definition, especially if some source used a nonstandard vertex set. I do not see evidence of that here.
- A bookkeeping error in translating the support classes to an explicit bijection on the `42` actual vertices.
- A later verifier may want the labeling written as an explicit list on concrete ring elements rather than only on support classes, although support-class symmetry already suffices mathematically.

## what_verify_should_check
- First do the bounded rediscovery / prior-art pass required by the harness.
- Independently re-derive the support-class decomposition and confirm the six edge families.
- Re-check that the displayed sets partition `{1,...,42}`.
- Run an independent gcd checker on the six adjacent class pairs.
- If the prior-art pass stays clean, this looks Lean-ready: formalize the six support classes and the coprimality checks.

## verify_rediscovery
Bounded PASS 1 web audit completed within budget.

Searches covered:

- the exact instance notation `Γ(Z_5 × Z_5 × Z_3)` with prime-labeling terms
- ASCII / reordered notation such as `Z_5 x Z_5 x Z_3`
- the canonical source DOI `10.61091/cn236-06`
- the canonical paper title and `Conjecture 4.3`
- checks inside the same source for theorem / proposition / example / observation / corollary level resolutions
- a brief sequel / citation-status check for later visible follow-up

Outcome:

- I found the 2025 Fox-Mooney paper as the canonical source.
- I did not find any instance-specific paper, note, preprint, example, proposition, or corollary settling `Γ(Z_5 × Z_5 × Z_3)`.
- The canonical source still presents the broader family `Γ(Z_p × Z_p × Z_q)` as Conjecture 4.3 rather than as a theorem, and the bounded follow-up search did not surface a later resolution of the exact `(5,5,3)` instance.

Rediscovery verdict for PASS 1: not established.

## verify_faithfulness
The solve-stage claim matches the intended statement exactly.

- The object is the standard zero-divisor graph on nonzero zero-divisors of `Z_5 × Z_5 × Z_3`.
- The target property is exactly a prime labeling by a bijection to `{1,...,42}` with coprime labels on adjacent vertices.
- The proof does not drift to a weaker proxy. It gives an explicit partition of all `42` labels among the six support classes whose sizes are exactly `4,4,2,16,8,8`.

I independently re-derived the graph on actual ring elements. There are exactly `42` nonzero zero-divisors, their support-class sizes match the claimed six classes, and adjacency is exactly disjointness of supports. The only edge families are:

- `V1` with `V2`, `V3`, `V23`
- `V2` with `V1`, `V3`, `V13`
- `V3` with `V1`, `V2`, `V12`

So the statement proved is the intended statement, not a nearby variant.

## verify_proof
First incorrect step found: none.

The proof is short enough to audit directly once the support-class model is confirmed.

Independent checks:

- Enumerating the ring elements confirms the six support classes and their sizes exactly.
- Enumerating all pairs of vertices confirms that adjacency is equivalent to disjoint support, with `0` mismatches.
- The resulting graph has `128` edges, matching the six complete bipartite edge families:
  `4·4 + 4·2 + 4·8 + 4·2 + 4·8 + 2·16 = 128`.
- The displayed label sets partition `{1,...,42}` exactly.
- Every required cross-class gcd is `1`.

The logical structure is valid: because each support class is an independent set, a partition of labels by support class with pairwise coprimality across each adjacent class pair is sufficient for a full prime labeling. No hidden case split or missing vertex-level distinction remains, since all vertices in the same support class have identical neighborhoods.

## verify_adversarial
I reran the supplied checker at [check_witness.py](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z5-z5-z3-prime-zero-divisor-graph/check_witness.py), and it passed:

- `partition_ok=1`
- `edge_coprime_ok=1`
- `edge_count=128`

I also ran an independent script from the actual ring definition rather than the support-class abstraction. That script confirmed:

- `42` vertices
- support counts `(1):4`, `(2):4`, `(3):2`, `(1,2):16`, `(1,3):8`, `(2,3):8`
- `0` mismatches between adjacency and disjoint support
- `128` total edges in the claimed six families

Finally, I tried a small adversarial perturbation: replacing one `V23` label by `15`. This immediately creates gcd violations with every label in `V1`, which is consistent with the claimed avoidance logic and suggests the witness is not passing by accident.

## verify_verdict
`VERIFIED`

Interpretation:

- PASS 1 did not establish rediscovery.
- The solve-stage witness appears mathematically correct for the exact intended statement.
- Under harness rules this remains a `CANDIDATE`, not `EXACT`, until Lean verification is complete.
- The candidate is strong enough to be Lean-ready.

## minimal_repair_if_any
None.

## final_reclassification

- Under the harness rule, this result remained a `CANDIDATE` through verification and could become `EXACT` only after the Lean stage finished.
- In this Lean-stage run, the exact instance was upgraded to `EXACT` because the formalization, build, and axiom audit completed successfully in the local AutoMath backend.

## lean_statement

- Lean project root: `lean/`
- Formalized theorem: `AutoMath.Z5Z5Z3.z5_z5_z3_zeroDivisorGraph_prime`
- Exact statement encoded: the zero-divisor graph on the nonzero zero-divisors of `Z_5 × Z_5 × Z_3` admits a prime labeling by a bijection to `{1,...,42}` with coprime labels on adjacent vertices.
- Faithfulness audit: `Vertex` is the exact subtype of triples in `Fin 5 × Fin 5 × Fin 3` with at least one nonzero coordinate and at least one zero coordinate, and `Adj` is exact coordinatewise zero-product modulo `5,5,3`, so this formalization matches the intended graph rather than a proxy support-class model.

## lean_skeleton

- Model the exact instance with raw representatives `Fin 5 × Fin 5 × Fin 3` and subtype out precisely the nonzero zero-divisors.
- State the target theorem first as `∃ f : Vertex → Label, IsPrimeLabeling f` with `Label = Fin 42` interpreted as `{1,...,42}` by `labelValue i = i + 1`.
- Encode the verified witness as an explicit `rawLabel` on the `42` actual vertices, mirroring the six support classes from the solve and verify stages.
- Prove `vertex_card`, witness injectivity, and edge coprimality by finite exhaustive kernel checks, then package those into `z5_z5_z3_zeroDivisorGraph_prime_checked` and the final existential theorem.

## lean_result

- Added the backend source at [lean/AutoMath/Z5Z5Z3.lean](/Users/jeremykalfus/CodingProjects/AutoMath/lean/AutoMath/Z5Z5Z3.lean) and mirrored it at [artifacts/z5-z5-z3-prime-zero-divisor-graph/lean/AutoMath/Z5Z5Z3.lean](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z5-z5-z3-prime-zero-divisor-graph/lean/AutoMath/Z5Z5Z3.lean).
- `lake build AutoMath.Z5Z5Z3` succeeded.
- `lake build` succeeded in the local `lean/` project after importing the new module.
- The audit file [artifacts/z5-z5-z3-prime-zero-divisor-graph/lean/AxiomAudit.lean](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/z5-z5-z3-prime-zero-divisor-graph/lean/AxiomAudit.lean) ran successfully with `#print axioms` on the target theorem and reported only the standard axioms `[propext, Classical.choice, Quot.sound]`.
- A source scan found no `sorry`, `admit`, or `sorryAx`.
- Practical outcome: the exact intended statement is now formalized and checked in Lean, so this instance qualifies as `EXACT` under the harness rules.

## lean_blockers

- No proof blocker remained for this exact instance.
- `lean4checker --fresh` was not available on this machine, so that extra audit could not be run.
- The axiom audit showed only the standard `[propext, Classical.choice, Quot.sound]` dependencies and no `sorryAx`.
