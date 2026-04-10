# Solve Record: Is the zero-divisor graph `Γ(Z_13 × Z_13 × Z_2)` prime?

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_13 × Z_13 × Z_2) prime?`
- Active slug: `z13-z13-z2-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_13 × Z_13 × Z_2)` admits a prime labeling, meaning a bijection from its `193` vertices to `{1,2,...,193}` such that adjacent vertices receive coprime labels.
- This solve pass is locked to the exact feeder instance `Γ(Z_13 × Z_13 × Z_2)`, not the full family `Γ(Z_p × Z_p × Z_2)`.

Self-check:

- `|Z_13 × Z_13 × Z_2| = 13 * 13 * 2 = 338`.
- Units are exactly the triples with all coordinates nonzero, so there are `12 * 12 * 1 = 144` units.
- Hence the nonzero zero-divisors are `338 - 144 - 1 = 193`, matching the label interval.

## definitions

- Write `U = Z_13^× = {1,2,...,12}`.
- The nonzero zero-divisors split into six support classes:
  - `A_i = (i,0,0)` for `i in U`, size `12`.
  - `B_i = (0,i,0)` for `i in U`, size `12`.
  - `C = (0,0,1)`, size `1`.
  - `D_ij = (i,j,0)` for `i,j in U`, size `144`.
  - `E_i = (i,0,1)` for `i in U`, size `12`.
  - `F_i = (0,i,1)` for `i in U`, size `12`.
- Because multiplication is coordinatewise and each factor is a field, two vertices are adjacent exactly when in each coordinate at least one entry is `0`, equivalently when their support sets are disjoint.
- Therefore the only edge families are:
  - `A-B`
  - `A-C`
  - `A-F`
  - `B-C`
  - `B-E`
  - `C-D`
- There are no other edges, and vertices inside a fixed support class are pairwise nonadjacent.

Self-check:

- The class sizes sum to `12 + 12 + 1 + 144 + 12 + 12 = 193`.
- The support-graph edge count is `|A||B| + |A||F| + |B||E| + |A| + |B| + |D| = 144 + 144 + 144 + 12 + 12 + 144 = 600`.
- A classwise label partition is enough, because vertices inside one support class have identical neighborhoods.

## approach_A

Structural / invariant approach.

- The singleton `C` is the hinge vertex: it is adjacent to all of `A ∪ B ∪ D`, and every vertex of `D` is adjacent only to `C`.
- So the clean family move is to assign label `1` to `C`. Then all `A-C`, `B-C`, and `C-D` edges are automatic, and the whole `D` class becomes unconstrained.
- After fixing `C = 1`, only three cross-class interfaces remain:
  - `A-B`
  - `A-F`
  - `B-E`
- The standard six-class template is to let `A ∪ E` use only prime factors from `{2,3}`, while `B ∪ F` uses labels coprime to `6`.
- For `N = 193`, the nontrivial `{2,3}`-smooth numbers are exactly
  `2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108,128,144,162,192`.
- There are `24` such labels, and `|A ∪ E| = 24`, so the naive `{2,3}`-smooth reservoir is exactly zero-slack at `p = 13`.
- Any choice of `24` labels coprime to `6` can then fill `B ∪ F`; there is no `B-B`, `F-F`, or `B-F` constraint in the support graph.

Self-check:

- This reduction is exact, not heuristic: once `C = 1`, the `D` class really is free.
- The arithmetic story is now at its first zero-slack boundary on the six-class line, so success here materially strengthens the family template instead of merely repeating the `p = 11` feeder.

## approach_B

Construction / extremal approach.

- Use the exact zero-slack `{2,3}`-smooth reservoir on `A ∪ E`:
  - `A <- {2,3,4,6,8,9,12,16,18,24,27,32}`
  - `E <- {36,48,54,64,72,81,96,108,128,144,162,192}`
- Set the hinge class to
  - `C <- {1}`.
- Choose any `24` labels coprime to `6` for `B ∪ F`. One explicit split is:
  - `B <- {5,7,11,13,17,19,23,25,29,31,35,37}`
  - `F <- {41,43,47,49,53,55,59,61,65,67,71,73}`
- Put every remaining label in `{1,...,193}` on `D`.

Why this should work:

- Every label on `A ∪ E` has prime support contained in `{2,3}`.
- Every label on `B ∪ F` is coprime to `6`, hence coprime to every label on `A ∪ E`.
- Since `C = 1`, every edge touching `C` is automatic.
- There are no other edges.

Self-check:

- The displayed class sets are pairwise disjoint.
- They use exactly `12 + 12 + 1 + 12 + 12 = 49` constrained labels, leaving `144` labels for `D`, exactly matching `|D|`.
- The construction uses all `24` nontrivial `{2,3}`-smooth labels up to `193`, so there is no hidden slack.

## lemma_graph

Proof skeleton:

1. Classify the `193` vertices into the six support classes `A,B,C,D,E,F`.
2. Prove adjacency is exactly disjointness of support.
3. Deduce the exact edge pattern `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`.
4. Assign label `1` to `C`; this settles every edge incident to `C` and frees the whole `D` class.
5. Fill `A ∪ E` with the full `{2,3}`-smooth reservoir up to `193`.
6. Fill `B ∪ F` with labels coprime to `6`.
7. Assign the residual `144` labels arbitrarily to `D` and conclude that every edge joins coprime labels.

## chosen_plan

- Use Approach A to lock the support graph and the exact zero-slack count.
- Use Approach B to give an explicit witness with `C = 1`, all `24` nontrivial `{2,3}`-smooth labels on `A ∪ E`, and a `24`-label complement block coprime to `6` on `B ∪ F`.
- Use only a tiny post-reasoning checker to guard against transcription errors and to verify the classwise witness against the ring definition.

## self_checks

- Statement-lock check: the target stayed the exact feeder instance `Γ(Z_13 × Z_13 × Z_2)`.
- Structural check: the six support classes and the edge pattern match the active family dossier and the new Lean support module.
- Count check: `A ∪ E` needs `24` labels, and there are exactly `24` nontrivial `{2,3}`-smooth labels up to `193`.
- Residual check: the constrained classes use `49` labels, leaving exactly `144` labels for `D`.
- Conservatism check: even if the witness survives direct checking and rediscovery audit, this is still feeder evidence until Lean closes either the exact instance or the family theorem slice.

## code_used

- A tiny local checker will be used only after the reasoning and explicit class partition are fixed.
- It should check:
  - the full `193`-vertex set from the ring definition;
  - the exact support-class counts and edge count `600`;
  - the disjointness and coverage of the displayed classwise label sets;
  - bijectivity onto `{1,...,193}`;
  - and `gcd = 1` on every edge.

## expected_result

- Current best solve-stage expectation: the exact feeder `Γ(Z_13 × Z_13 × Z_2)` should admit a prime labeling via the displayed zero-slack support-template witness.
- Campaign-relevant interpretation if the checker agrees:
  - the six-class `Γ(Z_p × Z_p × Z_2)` line does not break at the first zero-slack `p = 13` boundary;
  - the naive `{2,3}`-smooth reservoir survives through the whole zero-slack case rather than merely up to `p = 11`;
  - the next honest paired feeder should then move to `Γ(Z_17 × Z_25)`.

## family_affinity

- Family affinity is maximal.
- This is the campaign-designated decisive six-class feeder after the verified refined `F25(13)` checkpoint.
- Success or failure here directly changes the scope of the zero-divisor theorem-slice narrative.

## verify_rediscovery

- PASS 1 used a bounded live web audit and then stopped browsing.
- Search patterns covered:
  - the exact instance notation `Γ(Z_13 × Z_13 × Z_2)` and `Gamma(Z_13 x Z_13 x Z_2)` with `prime labeling`;
  - the broader family notation `Γ(Z_p × Z_p × Z_2)` with `prime labeling` and `zero-divisor graph`;
  - the current canonical source [Fox and Mooney, *On Prime Labelings of Zero-Divisor Graphs* (2025)](https://combinatorialpress.com/article/cn/volume%20236/on-prime-labelings-of-zero-divisor-graphs.pdf).
- What the bounded pass found:
  - no search hit within budget explicitly settled `Γ(Z_13 × Z_13 × Z_2)`;
  - Fox and Mooney remains the closest canonical source, but its open-problem section still treats the broader `Γ(Z_p × Z_p × Z_q)` direction as open rather than settled;
  - the source does list small nearby exact examples such as `Γ(Z_2 × Z_3 × Z_3)`, so the notation and venue are clearly on-topic, but no proposition/example/corollary within budget implied this exact feeder.
- Rediscovery conclusion:
  - rediscovery was not established within the required bounded pass;
  - this remains a candidate proof of an apparently frontier-open exact feeder instance, not a proof of a known settled result.

## verify_faithfulness

- The record stays locked to the exact intended statement: existence of a prime labeling for the full zero-divisor graph `Γ(Z_13 × Z_13 × Z_2)`.
- The graph convention and label interval are the right ones:
  - vertices are exactly the `193` nonzero zero-divisors of `Z_13 × Z_13 × Z_2`;
  - adjacency is the exact coordinatewise zero-product relation;
  - the target is a bijection onto `{1,...,193}`.
- The proof does not drift to a quotient graph, partial labeling, or family-only statement. It gives a full classwise witness for all vertices and uses the support graph only as an exact reduction justified by the ring law.

## verify_proof

- I independently recomputed the six support classes from the ring definition:
  - `|A| = 12`;
  - `|B| = 12`;
  - `|C| = 1`;
  - `|D| = 144`;
  - `|E| = 12`;
  - `|F| = 12`;
  - total `193`.
- I independently recomputed adjacency from coordinatewise multiplication modulo `13,13,2`. The only edge families are exactly:
  - `A-B`;
  - `A-C`;
  - `A-F`;
  - `B-C`;
  - `B-E`;
  - `C-D`;
  with total edge count `600`.
- Given that edge pattern, the mathematical reduction is correct:
  - once `C` gets label `1`, every `A-C`, `B-C`, and `C-D` edge is automatically valid;
  - every vertex of `D` is adjacent only to `C`, so the remaining `144` labels really are free on `D`;
  - the only nontrivial arithmetic obligations are then `A-B`, `A-F`, and `B-E`.
- Those obligations hold exactly as claimed:
  - every label in `A ∪ E` is supported on primes `{2,3}`;
  - every label in `B ∪ F` is coprime to `6`;
  - therefore every edge across `A-B`, `A-F`, and `B-E` joins coprime labels.
- First incorrect step found: none in the mathematical argument.

## verify_adversarial

- PASS 4 reran the witness verification independently from the record and tried to break the construction on the full graph, not just on the support-graph abstraction.
- Independent checker results from `check_witness.py`:
  - `vertex_count = 193`;
  - `class_sizes = {A: 12, B: 12, C: 1, D: 144, E: 12, F: 12}`;
  - `edge_count = 600`;
  - `edge_families = {A-B, A-C, A-F, B-C, B-E, C-D}`;
  - the displayed `A,B,C,E,F` label sets are pairwise disjoint and use exactly `49` labels;
  - the residual set for `D` has exactly `144` labels;
  - the final assignment is a bijection onto `{1,...,193}`;
  - `bad_edges = 0`.
- Additional adversarial checks:
  - I verified the full edge set directly from the ring multiplication law instead of trusting the class decomposition;
  - I verified the claimed nontrivial `{2,3}`-smooth reservoir count independently: there are exactly `24` such labels up to `193`;
  - I verified that this is a genuine zero-slack success, not a hidden slack argument.
- I did not find a counterexample edge, a hidden omitted edge family, or a computation/prose mismatch that breaks the `p = 13` witness.

## verify_theorem_worthiness

- This feeder materially strengthens a real theorem slice rather than merely adding one more isolated instance.
- What clearly scales:
  - the six-class support decomposition;
  - the hinge move `C = 1`;
  - the reduction from the full graph to the three nontrivial interfaces `A-B`, `A-F`, and `B-E`;
  - the sufficient-condition template "`A ∪ E` supported on a small prime set, `B ∪ F` avoiding that prime support".
- What does not yet scale automatically:
  - the exact choice of the support prime set `S`;
  - the supply lemma that would guarantee enough `S`-smooth labels for all odd primes;
  - the bridge from the current abstract Lean support theorems to family-specific ring-level decomposition statements.
- Best honest publication status is not merely `INSTANCE_ONLY`. This verified feeder closes the first zero-slack `p = 13` test on the six-class line and upgrades the active family campaign, so the honest status is `SLICE_CANDIDATE`, not `SLICE_EXACT` and not yet `FAMILY_CANDIDATE`.
- The next paired feeder that most sharply tests the upgraded campaign is `Γ(Z_17 × Z_25)`, because the four-class line has already required one honest `p = 13` refinement and now needs its next post-`13` stress test.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- The exact intended statement appears to be proved correctly by the current explicit witness, and the bounded rediscovery pass did not establish prior-art settlement of this exact instance.
- Because Lean has not been completed, the harness classification must remain `CANDIDATE`, not `EXACT`.
- `lean_ready = true`

## minimal_repair_if_any

- No mathematical repair to the witness or proof was needed.
