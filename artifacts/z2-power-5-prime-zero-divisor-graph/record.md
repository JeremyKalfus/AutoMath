# Solve Record: z2-power-5-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Gamma((Z_2)^5) prime?`
- Active slug: `z2-power-5-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Gamma((Z_2)^5)` admits a prime labeling, meaning a bijection from its `31` vertices to `{1,2,...,31}` such that adjacent vertices receive coprime labels.
- Working model: identify each vertex with a nonempty subset `A` of `[5] = {1,2,3,4,5}`; two distinct vertices `A, B` are adjacent exactly when `A ∩ B = ∅`.
- This solve pass is only about the exact `n = 5` instance, not the full family.

## definitions

- Vertex set: all nonempty subsets of `[5]`. Count: `2^5 - 1 = 31`.
- Edge relation: `A ~ B` iff `A ∩ B = ∅`.
- Prime labeling: a bijection `L : V -> {1,...,31}` with `gcd(L(A), L(B)) = 1` for every edge `A ~ B`.
- Equivalent arithmetic condition: for every prime `p`, the vertices whose labels are divisible by `p` must form an intersecting family.
- Degree by support size:
  - `|A| = 1`: degree `15`
  - `|A| = 2`: degree `7`
  - `|A| = 3`: degree `3`
  - `|A| = 4`: degree `1`
  - `|A| = 5`: degree `0`
- Ambiguities / conventions to lock:
  - The full support `[5]` is a vertex, because every nonzero element of `(Z_2)^5` is a zero-divisor.
  - The empty set is excluded.
  - The labeling uses every integer from `1` to `31` exactly once.
  - The graph is simple: no loops, no multi-edges.

## approach_A

Structural / invariant approach via coordinate ownership of repeated primes.

- The only primes that divide at least two labels in `{1,...,31}` are `2, 3, 5, 7, 11, 13`.
- If each such repeated prime is assigned an owner coordinate in `[5]`, and each label `m` is placed on a subset containing the owner coordinates of all repeated prime divisors of `m`, then any two labels with a common repeated prime are forced to lie on intersecting subsets.
- A concrete ownership map with only five coordinates is:
  - coordinate `1` owns `2`
  - coordinate `2` owns `3`
  - coordinate `3` owns `5`
  - coordinate `4` owns `7`
  - coordinate `5` owns both `11` and `13`
- For a label `m`, define `R(m)` as the set of owner coordinates of the repeated primes dividing `m`.
- If `R(m) ⊆ A` for the subset `A` carrying label `m`, then disjoint subsets cannot receive labels with a common repeated prime factor. Since every common factor greater than `1` has some prime divisor, this is sufficient for a prime labeling.
- This turns the problem into a finite containment matching:
  - left side: labels `1,...,31`
  - right side: nonempty subsets of `[5]`
  - edge `m -> A` when `R(m) ⊆ A`
- The arithmetic burden is now tiny enough that a short checker could validate a proposed matching if the hand construction gets close.

## approach_B

Construction / extremal approach using degree classes and near-saturation of stars.

- The `15` even labels must occupy an intersecting family of size `15`.
- A star `F_i = {A : i in A}` has size `16`, so the even labels nearly fill one star. This strongly suggests that a successful construction should anchor parity to one coordinate.
- Likewise:
  - multiples of `3` give a size-`10` intersecting family,
  - multiples of `5` give size `6`,
  - multiples of `7` give size `4`,
  - pairs sharing `11` or `13` only need size `2` intersecting families.
- Independently of a full ownership proof, the degree pattern says the most composite labels should live on large subsets:
  - `[5]` is isolated, so it can absorb a highly composite label with no edge constraints;
  - `4`-subsets have only one neighbor, so they can carry labels like `22, 26, 28`;
  - singletons should preferably get `1` or primes, because they see `15` neighbors.
- This route does not by itself produce a full witness, but it supports the same qualitative design as Approach A: small repeated primes should be coordinated by stars, while heavy composites should be pushed to large supports.

## lemma_graph

1. The graph is the disjointness graph on the `31` nonempty subsets of `[5]`.
2. If two labels share a prime divisor `p`, their vertices must intersect.
3. A sufficient condition for item 2 is: assign each repeated prime an owner coordinate, and place each label `m` on a subset containing `R(m)`.
4. Under the concrete ownership map
   - `2 -> 1`, `3 -> 2`, `5 -> 3`, `7 -> 4`, `11,13 -> 5`,
   every disjoint pair of subsets automatically receives coprime labels provided each assigned label respects `R(m) ⊆ A`.
5. Therefore the remaining task is to find a bijection between labels and nonempty subsets satisfying that containment rule.
6. If such a bijection exists, it is already a rigorous exact-instance witness; only the existence of the bijection may need computational help.

## chosen_plan

- Pursue Approach A as the main proof path.
- First lock the ownership map and derive the required-set multiset `R(m)` for labels `1..31`.
- Then try to build an explicit containment-respecting labeling by hand.
- If the hand placement becomes bookkeeping-heavy, use a tiny local matching/checker script restricted to this exact containment construction.
- If a witness is found, keep the solve-stage classification conservative: `CANDIDATE`, not `EXACT`, because Lean stays off here.

## self_checks

- Statement check: the target is exactly the `31`-vertex disjointness graph on nonempty subsets of `[5]`.
- Sufficiency check: the ownership rule is enough, because any shared factor `> 1` contributes a shared repeated prime owner.
- Scope check: no web, no prior-art claim, no Lean claim.
- Required-set check:
  - `R = ∅` for `1, 17, 19, 23, 29, 31`
  - `R = {1}` for `2, 4, 8, 16`
  - `R = {2}` for `3, 9, 27`
  - `R = {3}` for `5, 25`
  - `R = {4}` for `7`
  - `R = {5}` for `11, 13`
  - `R = {1,2}` for `6, 12, 18, 24`
  - `R = {1,3}` for `10, 20`
  - `R = {1,4}` for `14, 28`
  - `R = {2,3}` for `15`
  - `R = {2,4}` for `21`
  - `R = {1,5}` for `22, 26`
  - `R = {1,2,3}` for `30`
- Matching check: `check_witness.py` found a perfect containment matching of size `31`.
- Edgewise check: the same script then tested every disjoint pair of subsets and found `0` gcd violations.

## code_used

- A single local script `check_witness.py` was used after the reasoning reduction was locked.
- The script does only three bounded tasks inside the justified containment model:
  - compute `R(m)` for each `m in {1,...,31}`;
  - find a perfect matching between labels and nonempty subsets satisfying `R(m) ⊆ A`;
  - verify directly that every disjoint pair receives coprime labels.
- Script output:
  - `matching = 31`
  - `coprime_ok = 1`
  - `required_set_hist = {0: 6, 1: 12, 2: 12, 3: 1}`
- The explicit witness was written to `witness.json`.

## result

- Solve-stage candidate found: `Gamma((Z_2)^5)` appears to be prime.
- The explicit labeling exported to `witness.json` is:
  - size `1`:
    - `{1} -> 31`, `{2} -> 29`, `{3} -> 23`, `{4} -> 19`, `{5} -> 17`
  - size `2`:
    - `{1,2} -> 16`, `{1,3} -> 4`, `{2,3} -> 1`, `{1,4} -> 8`, `{2,4} -> 7`
    - `{3,4} -> 5`, `{1,5} -> 26`, `{2,5} -> 3`, `{3,5} -> 11`, `{4,5} -> 13`
  - size `3`:
    - `{1,2,3} -> 10`, `{1,2,4} -> 28`, `{1,3,4} -> 2`, `{2,3,4} -> 27`, `{1,2,5} -> 12`
    - `{1,3,5} -> 22`, `{2,3,5} -> 9`, `{1,4,5} -> 14`, `{2,4,5} -> 21`, `{3,4,5} -> 25`
  - size `4`:
    - `{1,2,3,4} -> 6`, `{1,2,3,5} -> 24`, `{1,2,4,5} -> 18`, `{1,3,4,5} -> 20`, `{2,3,4,5} -> 15`
  - size `5`:
    - `{1,2,3,4,5} -> 30`
- Why this works:
  - every assigned label `m` satisfies `R(m) ⊆ A` for its subset `A`;
  - if disjoint subsets `A` and `B` had labels with gcd `> 1`, choose a prime `p` dividing both labels;
  - because the labels are distinct and at most `31`, such a repeated prime must be one of `2, 3, 5, 7, 11, 13`;
  - the owner coordinate of `p` then lies in both `R(L(A))` and `R(L(B))`, hence in both `A` and `B`, contradicting `A ∩ B = ∅`.
- So the witness is an exact instance-level prime labeling for the intended graph.
- Solve-stage verdict: `CANDIDATE`, not `EXACT`, because Lean has not checked the witness yet and solve does not decide rediscovery risk.

## likely_failure_points

- The only substantial remaining gap is proof style, not local correctness: the existence of the explicit witness is currently certified by a tiny matching/checking script rather than a handwritten Hall-style argument.
- Verification should not trust the ownership idea abstractly; it should re-check the exported witness directly.
- Solve ran with web off, so frontier novelty is still unresolved here even if the instance labeling is correct.

## what_verify_should_check

- Re-derive the subset/disjointness model and the `31`-vertex count.
- Re-check that the repeated-prime ownership lemma is genuinely sufficient.
- Rerun `check_witness.py` and confirm it reproduces `matching = 31` and `coprime_ok = 1`.
- Audit `witness.json` directly:
  - its keys should be exactly the `31` nonempty subsets of `[5]`;
  - its values should be exactly the labels `{1,...,31}`;
  - every assigned pair should satisfy `R(m) ⊆ A`;
  - every disjoint pair of subsets should receive coprime labels.
- Treat the correct positive classification as `CANDIDATE` unless and until prior-art risk is checked and Lean verifies the exact witness.

## verify_rediscovery

- PASS 1 used limited web and stopped early once rediscovery was clearly established.
- The canonical source itself, Fox and Mooney, *On prime labelings of zero-divisor graphs* (Congressus Numerantium 236, 2025), already settles the exact intended instance.
- In the paper's Section 4, `Example 4.1` explicitly states that `Gamma(Z_2^5)` is prime and provides a concrete labeling table for the `31` nonzero zero-divisors of `(Z_2)^5`.
- That is enough to classify the present run as `REDISCOVERY`: even if the current witness is correct, it is not a frontier-novel solution of an open exact instance.
- Short note on current proof quality: the local witness produced in this run still appears mathematically correct after skeptical checking below; the problem is novelty, not correctness.

## verify_faithfulness

- The solve-stage claim matches the intended statement exactly.
- The artifact works with the same object as the problem statement: the zero-divisor graph on the `31` nonempty subsets of `[5]`, with adjacency given by disjointness.
- The claimed conclusion is exactly existence of a prime labeling on this graph, not a weaker proxy such as a partial labeling, a large induced subgraph, or a different family member.
- No quantifier drift or definition drift was found.

## verify_proof

- First incorrect step found: none.
- The core sufficiency lemma is sound. If two disjoint subsets received labels with gcd greater than `1`, some prime `p` would divide both labels. Because labels are distinct and lie in `{1,...,31}`, any such shared prime must be one of the repeated primes `2,3,5,7,11,13`, and the owner-coordinate rule forces both subsets to contain the owner of `p`, contradicting disjointness.
- The remaining burden is only witness existence and witness correctness, both of which were checked computationally in bounded finite form.
- This is not a Lean-level proof yet, but for ordinary mathematical verification of the explicit finite witness no critical gap was found.

## verify_adversarial

- Reran `python3 artifacts/z2-power-5-prime-zero-divisor-graph/check_witness.py`.
- Output reproduced the solve-stage claims: `matching = 31`, `coprime_ok = 1`, `required_set_hist = {0: 6, 1: 12, 2: 12, 3: 1}`.
- Independently audited `witness.json` with a separate one-off script:
  - all `31` nonempty subsets of `[5]` appear exactly once;
  - the labels are exactly `{1,...,31}`;
  - direct edgewise checking found `0` disjoint-pair gcd violations.
- No adversarial break of the candidate labeling was found.

## verify_verdict

- `REDISCOVERY`
- Reason: the exact intended statement `Gamma((Z_2)^5) is prime` is already explicitly solved in the canonical 2025 source, so this run cannot remain a frontier-novel candidate.
- Classification must therefore be `REDISCOVERY`, not `CANDIDATE` or `EXACT`.
- `lean_ready = false` because Lean is not a stop condition for rediscoveries.

## minimal_repair_if_any

- No mathematical repair to the witness or proof was needed.
- The only conservative repair is classification-level: downgrade the run from `CANDIDATE` to `REDISCOVERY` and archive it as such.
