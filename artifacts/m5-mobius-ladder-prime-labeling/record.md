# m5-mobius-ladder-prime-labeling

## statement_lock
- Active slug: `m5-mobius-ladder-prime-labeling`
- Title: `Does the Möbius ladder M_5 admit a prime labeling?`
- Locked intended statement: the standard `10`-vertex Möbius ladder `M_5` admits a prime labeling.
- Working model: write the cycle vertices as `v_0,v_1,...,v_9` modulo `10`; then `v_i` is adjacent to `v_{i-1}`, `v_{i+1}`, and `v_{i+5}`.
- Exact target: find a bijection `f : V(M_5) -> {1,...,10}` such that `gcd(f(u),f(v)) = 1` for every edge `uv`.

Self-check:
- I am using the dossier's standard `2n`-vertex convention for `M_n`, so `M_5` has `10` vertices.
- The solve target is the positive existence claim for this exact graph, not the whole odd-index Möbius-ladder family.

## definitions
- A prime labeling is a bijection from the `10` vertices to `{1,2,...,10}` with coprime labels on every edge.
- The graph is cubic, with `10` vertices and `15` edges.
- `M_5` is bipartite under the partition
  `A = {v_0,v_2,v_4,v_6,v_8}` and `B = {v_1,v_3,v_5,v_7,v_9}`.
- Distinct non-coprime label pairs inside `{1,...,10}` are:
  - every pair of even labels,
  - `(3,6)`, `(3,9)`, `(6,9)`,
  - `(5,10)`.
- It is convenient to rename the bipartition as
  `A_k = v_{2k}` and `B_k = v_{2k+1}` for `k mod 5`. Then each `A_k` is adjacent exactly to `B_{k-1}`, `B_k`, and `B_{k+2}`.

Ambiguities / conventions to keep fixed:
- The notation `M_5` can be a source of confusion across the literature; here it definitely means the `10`-vertex ladder built from `C_10` plus five opposite chords.
- The labels are exactly `{1,...,10}` with no repetitions and no offset.

Self-check:
- The adjacency rule `A_k ~ B_{k-1}, B_k, B_{k+2}` matches the cycle-plus-opposite-chord definition.
- The list of non-coprime pairs is complete and will drive the whole argument.

## approach_A
Structural / invariant route: force a parity split.

1. Any two even labels are non-coprime, so the five vertices carrying even labels form an independent set `S`.
2. Each vertex of `M_5` has degree `3`, so the sum of degrees of vertices in `S` is `5 * 3 = 15`.
3. The graph itself has only `15` edges total.
4. Therefore every edge of `M_5` must leave `S`; there can be no edge internal to `V \ S`, because that would create more than `15` incidences from the vertices of `S`.
5. So both `S` and `V \ S` are independent sets of size `5`, hence they are exactly the two bipartition classes of this connected bipartite graph.
6. Conclusion: in any prime labeling, one entire bipartition receives the even labels `{2,4,6,8,10}` and the other receives the odd labels `{1,3,5,7,9}`.

This collapses the coprimality problem sharply. Once every edge is odd-even, the only remaining bad edge types are
- `6` adjacent to `3` or `9`,
- `10` adjacent to `5`.

The pair `(3,9)` no longer matters because both labels must lie on the odd side and are therefore nonadjacent automatically.

Self-check:
- The degree count is exact, not heuristic: `5` even-labeled vertices contribute all `15` edge incidences on one side.
- This does not assume the bipartition in advance; it derives it from the prime-labeling constraints.

## approach_B
Construction / extremal route: place the restrictive labels first in the `A_k/B_k` model.

1. Put `6` on `A_0`.
2. Since `A_0` is adjacent to `B_4,B_0,B_2`, its nonneighbors on the odd side are exactly `B_1,B_3`.
3. Put the two odd labels incompatible with `6`, namely `3` and `9`, on `B_1,B_3`.
4. Put `10` on `A_1`.
5. Since `A_1` is adjacent to `B_0,B_1,B_3`, its nonneighbors on the odd side are `B_2,B_4`.
6. Put the odd label incompatible with `10`, namely `5`, on `B_4`.
7. Fill the remaining odd positions `B_0,B_2` with `1,7` in any order.
8. Fill the remaining even positions `A_2,A_3,A_4` with `2,4,8` in any order.

One concrete choice is
- `A_0=6`, `A_1=10`, `A_2=2`, `A_3=4`, `A_4=8`
- `B_0=1`, `B_1=3`, `B_2=7`, `B_3=9`, `B_4=5`

In cycle order `v_0,v_1,...,v_9`, this is the labeling
`(6,1,10,3,2,7,4,9,8,5)`.

Self-check:
- The construction is explicit and bijective.
- The only labels treated specially are exactly the ones appearing in the reduced bad-pair list.

## lemma_graph
1. Lemma 1: the five even labels must occupy an independent set of size `5`.
2. Lemma 2: in a cubic `10`-vertex graph with `15` edges, such an independent set forces every edge to run between it and its complement.
3. Lemma 3: therefore any prime labeling of `M_5` must place all evens on one bipartition class and all odds on the other.
4. Lemma 4: after this parity forcing, the only possible bad edge labels are `6-3`, `6-9`, and `10-5`.
5. Lemma 5: in the `A_k/B_k` coordinates, `A_k` has odd-side nonneighbors `B_{k+1}` and `B_{k+3}`.
6. Lemma 6: place `6` on `A_0`, so `3` and `9` can be hidden at `B_1,B_3`.
7. Lemma 7: place `10` on `A_1`, so `5` can be hidden at `B_4`.
8. Conclusion: the explicit labeling `(6,1,10,3,2,7,4,9,8,5)` is prime.

## chosen_plan
Use `approach_A` to reduce the entire problem to a bipartite placement problem, then finish with the explicit witness from `approach_B`.

Rigorous solve-stage proof:

Let the vertices of `M_5` be `v_0,...,v_9` modulo `10`, with edges `v_i v_{i+1}` and `v_i v_{i+5}`. Define
`A_k = v_{2k}` and `B_k = v_{2k+1}` for `k mod 5`. Then each `A_k` is adjacent exactly to `B_{k-1}, B_k, B_{k+2}`.

In any prime labeling, no two even labels can be adjacent. Since the even labels are exactly `{2,4,6,8,10}`, the five vertices carrying them form an independent set `S` of size `5`. Because `M_5` is cubic, the sum of degrees over `S` is `15`. But `M_5` has only `15` edges total, so every edge must have one endpoint in `S`. Hence the complement `V(M_5) \ S` is also independent, and `S` is one whole bipartition class. Therefore all even labels lie on one side and all odd labels lie on the other.

After this forcing, every edge is odd-even. The only odd-even non-coprime pairs in `{1,...,10}` are `6-3`, `6-9`, and `10-5`. So it is enough to place the labels so that those three adjacencies do not occur.

Now assign labels as follows:
- `A_0=6`, `A_1=10`, `A_2=2`, `A_3=4`, `A_4=8`
- `B_0=1`, `B_1=3`, `B_2=7`, `B_3=9`, `B_4=5`

Then the vertex carrying `6` is `A_0`, whose neighbors are `B_4,B_0,B_2`, carrying labels `5,1,7`. So `6` is not adjacent to `3` or `9`.

The vertex carrying `10` is `A_1`, whose neighbors are `B_0,B_1,B_3`, carrying labels `1,3,9`. So `10` is not adjacent to `5`.

Every other edge joins an even label to an odd label outside the bad list `6-3`, `6-9`, `10-5`, so all remaining edge pairs are coprime automatically. Thus every edge of `M_5` receives coprime endpoint labels.

Equivalently, in cycle order `v_0,v_1,...,v_9`, the explicit witness is
`(6,1,10,3,2,7,4,9,8,5)`.
Hence `M_5` is prime.

Self-check:
- The proof ends with a direct witness, not just a plausibility argument.
- The final check only needs the three reduced bad edge types, and each is handled explicitly.

## self_checks
- Statement check: still locked to the exact `10`-vertex Möbius ladder `M_5`.
- Convention check: the argument depends on the standard bipartition of the cycle-plus-opposite-chord model; verification should re-derive that model independently.
- Proof check: the only delicate step is the degree-count argument forcing the even labels onto one whole bipartition class.
- Conservatism check: despite the strong handwritten witness, solve stops at `CANDIDATE`, not `EXACT`, because Lean is still off.
- Method check: no SAT, ILP, CP-SAT, brute force, or any code was used.

## code_used
- No code used.
- Reason: the parity forcing and the explicit witness are both small enough to verify by hand on the fixed `10`-vertex graph.

## result
- Solve-stage verdict: `CANDIDATE`
- Confidence: `high`
- Current conclusion: the cycle-order labeling
  `(6,1,10,3,2,7,4,9,8,5)`
  is a rigorous prime-labeling candidate for the dossier's exact `M_5`.
- Lean remains off in this stage, but the instance now looks ready for skeptical verification.

## likely_failure_points
- The main technical risk is a notation mismatch about `M_5`; verification should confirm that the selected problem really means the `10`-vertex Möbius ladder with opposite chords.
- Verification should also recheck the adjacency formula `A_k ~ B_{k-1}, B_k, B_{k+2}`.
- The solve proof uses the fact that the graph is connected and cubic; verification should confirm no hidden edge-count mistake slipped into the parity-forcing step.
- Frontier-novelty remains unresolved here because solve ran with web disabled and the dossier already flagged moderate-to-high rediscovery risk.

## what_verify_should_check
- Re-derive the exact `M_5` convention from the dossier and check that the witness is interpreted on the correct graph.
- Reconfirm the full list of distinct non-coprime pairs in `{1,...,10}`.
- Check the degree-count argument that any valid placement of the five even labels must equal one whole bipartition class.
- Check the explicit witness `(6,1,10,3,2,7,4,9,8,5)` directly on all `15` edges.
- Run the bounded prior-art pass carefully, because this exact graph-labeling instance carries nontrivial rediscovery risk.

## verify_rediscovery
- PASS 1 used the allowed limited web budget and established rediscovery.
- The canonical Gallian survey entry still only records the older theorem that Möbius ladders `M_n` are not prime when `n` is even, so the dossier's open-status inference was understandable but incomplete.
- A later paper by M. H. M. Haque, I. Khanam, and A. H. Shahriar, titled `Prime Labeling of Möbius Ladder Graphs M_n` and posted in 2024 on the ULAB Journal of Science and Engineering site, states that it proves prime labelings for Möbius ladder graphs `M_n`.
- That family-level result directly covers the exact intended instance `M_5` under the same standard notation used in the dossier and solve artifact.
- Therefore this run is a correct-proof-of-known-result situation, not a frontier-novel resolution of an open instance.
- Short note on correctness: the current solve-stage witness still appears mathematically correct on its own merits.

## verify_faithfulness
- The solve artifact is faithful to the intended statement.
- It keeps the standard `2n`-vertex convention for Möbius ladders, so `M_5` is the `10`-vertex graph built from `C_10` plus opposite chords.
- The proof targets the exact positive existence claim for this graph and does not drift to a different family, relaxed label set, or proxy notion.
- Re-deriving the coordinates confirmed the claimed adjacency rule `A_k ~ B_{k-1}, B_k, B_{k+2}`.

## verify_proof
- No incorrect step was found in the handwritten proof.
- The key degree-count lemma is sound: if the five even labels occupy a vertex set `S`, then `S` is independent because even-even adjacency is impossible; since each vertex of `M_5` has degree `3`, the `5` vertices of `S` contribute `15` incidences, equal to the total number of edges of the graph, so every edge must cross from `S` to `V \\ S`. Hence both parts are independent and `S` is exactly one bipartition class.
- After this parity forcing, the only odd-even non-coprime pairs in `{1,...,10}` are indeed `6-3`, `6-9`, and `10-5`.
- The explicit placement avoids exactly those pairs, so the proof closes correctly.

## verify_adversarial
- A direct recomputation checked all `15` edges of the cycle-order labeling `(6,1,10,3,2,7,4,9,8,5)` and every endpoint pair had gcd `1`.
- The bipartite coordinate identity used by the proof was also recomputed independently and matched the claimed neighbor sets for all `k mod 5`.
- No hidden computational claim remained unsupported.

## verify_verdict
- `REDISCOVERY`
- Reason: PASS 1 found an existing family-level result proving prime labelings for Möbius ladder graphs `M_n`, so the exact intended instance `M_5` is already settled in the literature.
- Because rediscovery is established, this run must not advance to Lean as a frontier-novel `EXACT` target, even though the current witness appears correct.

## minimal_repair_if_any
- No repair to the mathematical argument was needed.
- The only correction is metadata: downgrade the run from frontier candidate status to `REDISCOVERY`, set `lean_ready = false`, and archive it as a rediscovery rather than sending it to Lean.
