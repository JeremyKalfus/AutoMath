# Solve Record: z59-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_59 × Z_25) prime?`
- Active slug: `z59-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_59 × Z_25)` admits a prime labeling, meaning a bijection from its `314` vertices to `{1,2,...,314}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_59 × Z_25`, not the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_59` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_59^×}`, size `58`.
  - `D = {(a,5t) : a ∈ Z_59^×, t ∈ {1,2,3,4}}`, size `232`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 59` and `bd = 0 mod 25`.
- Because `Z_59` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - vertices inside `A`, `C`, and `D` have identical neighborhoods, so labels may be permuted freely inside those classes once the class label sets are fixed;
  - the four `B` vertices form a `K_4`, so any permutation of a pairwise-coprime `B` label set also preserves the witness even though the individual open neighborhoods are not literally identical as sets.
- Ambiguities, conventions, or missing definitions:
  - none that block the solve; the campaign dossier already fixes the standard zero-divisor graph convention and the four support classes.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is unchanged from the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 59` are therefore forced:
  - `A-C = 20 · 58 = 1160`;
  - `B-B = 6`;
  - `B-C = 4 · 58 = 232`;
  - `B-D = 4 · 232 = 928`.
- Total predicted edge count: `1160 + 6 + 232 + 928 = 2326`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Brief self-check after Approach A:
  - vertex count check: `20 + 4 + 58 + 232 = 314`;
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`, so no new graph-theoretic obstruction appears at `p = 59`.

## approach_B

- Construction / extremal route by changing the barrier regime rather than stretching the old one.
- First, reject the previously successful frozen barrier `B = {1,19,23,29}` for this instance:
  - up to `314`, the nontrivial multiples of `19` are `38,57,76,95,114,133,152,171,190,209,228,247,266,285,304`, so spill size `15`;
  - the nontrivial multiples of `23` are `46,69,92,115,138,161,184,207,230,253,276,299`, so spill size `12`;
  - the nontrivial multiples of `29` are `58,87,116,145,174,203,232,261,290`, so spill size `9`.
- These spill sets are disjoint below `314`, so the old barrier would require `15 + 12 + 9 = 36` labels in `A`, but `|A| = 20`. Therefore the old barrier cannot drive this instance.
- The natural repair is to choose the nontrivial barrier labels above half the interval, so they create no spill at all.
- Take
  `B = {1,163,167,173}`.
- These four labels are pairwise coprime, and since each of `163,167,173` is greater than `314/2 = 157`, none has a nontrivial multiple in `{1,...,314}`.
- So `B-D` becomes automatic once those labels are excluded from `D`.
- Next, build `A` from a tiny smooth palette and let `C` absorb all remaining primes.
- The interval `{1,...,314}` contains exactly `65` primes:
  `2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313`.
- Exclude the seven primes
  `2,3,5,7,163,167,173`.
  The remaining `65 - 7 = 58` primes fit `C` exactly.
- Hence choose
  `C = {11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313}`.
- Build `A` from numbers whose prime factors are contained in `{2,3,5,7}`:
  `A = {2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,21,24,25,27,28}`.
- Every label in `A` is then automatically coprime to every label in `C`, because `C` avoids the prime factors `2,3,5,7`.
- Every nontrivial label in `B` is also coprime to every label in `C`, because `163,167,173` were excluded from `C`.
- Therefore one explicit classwise partition suggested by this reasoning is:
  - `B = {1,163,167,173}`;
  - `A = {2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,21,24,25,27,28}`;
  - `C` equal to the `58` primes listed above;
  - `D` equal to the remaining `232` labels.
- Brief self-check after Approach B:
  - the old frozen barrier really is impossible here because its spill is `36 > 20`;
  - the new barrier has spill `0`;
  - the prime count `65 - 7 = 58` matches `|C|` exactly;
  - the proposed `A` set has size `20` and uses only the excluded small-prime palette.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,58,232`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. If the nontrivial labels in `B` are all greater than half the interval `{1,...,314}`, then they have no nontrivial in-interval multiples, so the `B-D` obligation is automatic once those labels themselves stay inside `B`.
7. If `A` is built from a small excluded prime palette and `C` is the complementary set of all remaining primes, then the `A-C` and `B-C` obligations reduce to factor-palette separation rather than spill bookkeeping.
8. Therefore any partition of `{1,...,314}` into class label sets satisfying those obligations gives a prime labeling.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Reject the old frozen barrier immediately because its spill already exceeds the fixed `20` slots of `A`.
- Switch to a zero-spill barrier by placing three pairwise-coprime barrier labels above half the interval.
- Let `A` use a tiny smooth palette `{2,3,5,7}` and let `C` absorb every other prime.
- Only after fixing the full explicit witness, use one tiny checker to validate the class partition against the ring definition.
- Brief self-check after choosing the plan:
  - this remains reasoning-first because the witness is dictated by the support reduction and a clean factor-palette split, not by search;
  - minimal code is justified only as post-construction witness verification.

## self_checks

- Statement lock:
  - the exact target is the feeder instance `Γ(Z_59 × Z_25)`;
  - the label interval length `314` matches the vertex count.
- Structural reduction:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the full graph again collapses to three arithmetic interfaces.
- Barrier analysis:
  - the old fixed barrier `B = {1,19,23,29}` is no longer viable because its spill count is `36`;
  - the new barrier `B = {1,163,167,173}` has zero spill.
- Prime-pool analysis:
  - the prime inventory up to `314` has size `65`;
  - after excluding exactly seven primes for the `A` palette and the `B` barrier, the complementary prime pool has size `58 = |C|`.
- Witness shape:
  - `A`, `B`, and `C` are pairwise disjoint and have sizes `20,4,58`;
  - the remaining complement has size `232`, exactly `|D|`;
  - every label in `A ∪ B` is coprime to every label in `C` by construction.

## code_used

- No code was used to design the witness.
- After the reasoning and explicit class partition were fixed, one tiny local checker was used for witness verification.
- The checker enumerated the `314` nonzero zero-divisors of `Z_59 × Z_25`, generated edges directly from the ring multiplication rule, checked bijectivity onto `{1,...,314}`, and tested `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 314`
  - `edge_count = 2326`
  - `edge_type_counts = {A-C: 1160, B-B: 6, B-C: 232, B-D: 928}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `1,163,167,173` on `B` in any order;
  - put the labels `2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,21,24,25,27,28` on `A` in any order;
  - put the labels `11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313` on `C` in any order;
  - put the remaining `232` labels on `D`.
- Why this works:
  - `B-B` edges: `1,163,167,173` are pairwise coprime.
  - `A-C` edges: every label in `A` has prime factors only in `{2,3,5,7}`, while every label in `C` is a prime outside that set.
  - `B-C` edges: the nontrivial `B` labels are the excluded primes `163,167,173`, so no label in `C` shares a factor with them.
  - `B-D` edges: since `163,167,173 > 157`, they have no nontrivial multiples in `{1,...,314}`, so no label in `D` can be divisible by a nontrivial `B` label.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; and the zero-spill barrier idea of placing the nontrivial `B` labels above half the interval so `B-D` becomes automatic.
  - what part does not yet scale:
    the instance does not yet prove a quantified prime-count theorem guaranteeing that, after excluding a small factor palette and three high barrier primes, at least `p - 1` complementary primes remain for `C`.
  - what theorem slice is suggested:
    a zero-spill high-barrier sufficient-condition theorem for `Γ(Z_p × Z_25)` in which `B = {1,b_1,b_2,b_3}` with `b_i > (5p+19)/2`, `A` is built from a small safe factor palette, and `C` is filled by the complementary prime pool.
  - what one or two next feeder instances would help most:
    `Γ(Z_61 × Z_25)` as the immediate local persistence test for the new regime, and `Γ(Z_53 × Z_25)` only if the campaign wants the nearest smaller unresolved point tied back to the current blocker language.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still instance-level evidence, but it is materially closer to a paper-shaped claim because it points to a cleaner asymptotic `F25` theorem slice than the earlier spill-management witnesses alone.

## family_affinity

- Family affinity is high.
- This feeder sits directly on the live `Γ(Z_p × Z_25)` publication line and attacks the current arithmetic blocker rather than a one-off exact curiosity.
- The main family relevance is that it forces a new barrier regime: the old fixed low barrier is no longer tenable, but a zero-spill high barrier appears to work cleanly.

## generalization_signal

- Generalization signal is strong.
- The solve package suggests a second family regime beyond the preserved low- and mid-`p` moved-barrier stories:
  instead of trying to keep barrier spill inside `A`, one can eliminate barrier spill entirely by placing the nontrivial `B` labels above half the interval.
- In that regime, the arithmetic problem becomes:
  choose three pairwise-coprime labels above `(5p+19)/2`, reserve a tiny smooth palette for `A`, and let `C` absorb the complementary prime pool.
- What is still missing is a quantified theorem proving that the complementary prime pool has size at least `p - 1` for the desired `p` range.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. choose `B = {1,b_1,b_2,b_3}` with pairwise-coprime `b_i > (5p+19)/2`, so the barrier has zero spill;
  4. reserve a small excluded prime palette, here `{2,3,5,7,b_1,b_2,b_3}`;
  5. label `A` by safe numbers supported only on the small palette;
  6. label `C` by the complementary primes in `{1,...,5p+19}`;
  7. assign the residual complement to `D`.
- Relative to the earlier feeders, the reusable gain is conceptual:
  the arithmetic front end can be driven by factor-palette separation with a zero-spill barrier, not only by a moved sparse barrier whose spill must be packed into `A`.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, `Γ(Z_p × Z_25)` is prime whenever the interval `{1,...,5p+19}` admits
  - three pairwise-coprime labels `b_1,b_2,b_3 > (5p+19)/2`,
  - a set of `20` labels for `A` whose prime factors lie in a fixed small excluded palette disjoint from the chosen `C` primes,
  - and at least `p - 1` primes outside that excluded palette.
- Under those conditions one may take
  - `B = {1,b_1,b_2,b_3}`,
  - `A` from the safe small-prime palette,
  - `C` as the complementary prime pool,
  - `D` as the residual complement.
- This exact `p = 59` feeder is the first local record in this worktree where that zero-spill high-barrier slice is cleaner than the earlier spill-management formulations.

## smallest_param_shift_to_test

- The smallest next parameter shift to test for this new regime is `p = 61`.
- Reason:
  the construction here uses only the interval length `5p + 19`, the availability of three pairwise-coprime labels above half the interval, and a complementary prime pool count; `p = 61` is therefore the nearest local stress test of whether this zero-spill barrier regime persists immediately beyond `59`.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage feeder instance with no bounded rediscovery pass in this turn and no Lean closure.
- It is publication-relevant because it changes the shape of the arithmetic existence story on the `F25` line:
  the instance does not merely continue the moved-barrier pattern, it suggests a cleaner asymptotic zero-spill barrier regime.
- The likely publishable unit is still a theorem slice or companion arithmetic theorem, not the single `p = 59` witness by itself.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the now-stable `Γ(Z_p × Z_25)` support reduction.
- The arithmetic failure point would be an incorrect prime count up to `314` or an omitted overlap between the proposed class label sets.
- Another arithmetic failure point would be accidentally putting into `D` a label divisible by `163`, `167`, or `173`, but this should be impossible because those primes have no nontrivial multiples in the interval.
- Publication-wise, the main weakness is that the new high-barrier regime is still an observed instance-level pattern rather than a quantified family theorem.

## what_verify_should_check

- Recompute the `314` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `2326` edges.
- Check that the displayed classwise label sets are disjoint and cover exactly `{1,...,314}`.
- Check coprimality on every actual edge from the ring graph.
- Check the prime count `π(314) = 65` and the exact size `58` of the chosen `C` prime pool.
- In the later bounded rediscovery pass, audit not only the exact instance but also whether any existing sufficient-condition theorem already implies this high-barrier regime.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact instance notation `Γ(Z_59 × Z_25)`, ASCII and reordered variants such as `Z_59 x Z_25` and `Z_59 x Z_5^2`, the family notation `Γ(Z_p × Z_(q^2))`, and the canonical topic paper `On Prime Labelings of Zero-Divisor Graphs`.
- Within that budget, I did not find an earlier theorem, proposition, example, observation, or corollary settling this exact `p = 59, q = 5` case.
- The canonical-source pass instead pointed back to the 2025 Combinatorial Press paper on zero-divisor prime labelings, whose nearby solved cases are different families, while the ambient `Γ(Z_p × Z_(q^2))` line was still presented there as conjectural/open rather than closed by a result implying `Γ(Z_59 × Z_25)`.
- No later status check within the bounded pass produced a contrary rediscovery signal.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The solve record addresses the exact intended mathematical claim: a bijective prime labeling of the full simple zero-divisor graph `Γ(Z_59 × Z_25)` on the `314` nonzero zero-divisors.
- There is no drift to a support graph, subgraph, or weaker proxy statement. The support classes `A,B,C,D` are used only as a reduction device for the exact graph.
- I made one tiny wording repair in the conventions section: only `A`, `C`, and `D` have identical neighborhoods. The `B` vertices are handled instead by the fact that they form a `K_4`, so any permutation of a pairwise-coprime `B` label set still preserves the witness.
- With that repair, the claimed result matches the intended statement exactly.

## verify_proof

- I recomputed the vertex partition directly from the ring definition and again obtained `|A| = 20`, `|B| = 4`, `|C| = 58`, and `|D| = 232`, for total `314` vertices.
- I independently recomputed the edge set and again found only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `1160`, `6`, `232`, and `928`, for total `2326` edges.
- Given that support graph, the proof really does reduce to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly. The `C` block is exactly the complementary prime pool after excluding `2,3,5,7,163,167,173`, and the nontrivial `B` labels `163,167,173` have no in-interval multiples beyond themselves because each is greater than `314/2`.
- First incorrect step found: none. After the wording repair above, the proof is a correct instance-level witness argument.

## verify_adversarial

- This artifact does not preserve a local `check_witness.py`, so I reran the witness with an independent one-off verifier script rather than trusting the solve summary.
- That script again reported:
  - `vertex_count = 314`
  - `edge_count = 2326`
  - `edge_type_counts = {A-C: 1160, B-B: 6, B-C: 232, B-D: 928}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`
- I also checked the arithmetic pressure points directly:
  - `π(314) = 65`;
  - the chosen `C` set is exactly the remaining `58` primes after excluding `2,3,5,7,163,167,173`;
  - `163`, `167`, and `173` have no nontrivial multiples in `{1,...,314}`;
  - no nontrivial multiple of any chosen `C` prime lands in `A ∪ B`.
- I did not find a hidden divisibility obstruction, mislabeled class, or missing edge type that breaks the witness.

## verify_theorem_worthiness

- This is still an instance result, not a theorem slice by itself. The structural part that clearly scales is the four-class support reduction together with the zero-spill high-barrier idea: place three pairwise-coprime `B` labels above half the interval, keep `A` on a tiny fixed smooth palette, and let `C` use the complementary prime pool.
- The part that does not yet scale automatically is the quantified supply argument. The proof still needs a real lemma guaranteeing at least `p - 1` complementary primes after excluding the small `A` palette and the three high barrier primes.
- Relative to the earlier bounded-spill feeders, this instance is campaign-significant because it changes the arithmetic regime rather than merely extending the old one: the barrier spill disappears entirely, and the bookkeeping collapses to prime-pool supply.
- The best honest publication status for this artifact is therefore `SLICE_CANDIDATE`, not `INSTANCE_ONLY`, because it is still only feeder evidence but it does point to a genuine family theorem slice.
- The smallest next discriminator for the claimed template is `Γ(Z_61 × Z_25)`, which tests whether the zero-spill complementary-prime-pool regime persists immediately beyond `p = 59`.

## verify_verdict

- `VERIFIED`
- No rediscovery was established in PASS 1, the claim matches the intended instance after a tiny wording repair, and the explicit witness survived independent skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- Repaired one sentence in the solve conventions: only `A`, `C`, and `D` have identical neighborhoods; `B` is handled instead by the `K_4` symmetry plus pairwise-coprime labels.
- No mathematical repair to the witness itself was needed.
