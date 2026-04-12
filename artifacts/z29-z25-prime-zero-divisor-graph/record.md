# Solve Record: z29-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_29 × Z_25) prime?`
- Active slug: `z29-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_29 × Z_25)` admits a prime labeling, meaning a bijection from its `164` vertices to `{1,2,...,164}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_29 × Z_25`, not to the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_29` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_29^×}`, size `28`.
  - `D = {(a,5t) : a ∈ Z_29^×, t ∈ {1,2,3,4}}`, size `112`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 29` and `bd = 0 mod 25`.
- Because `Z_29` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - vertices inside `A`, `C`, and `D` may be permuted once the class label sets are fixed, because the proof is classwise;
  - the four `B` vertices form a `K_4`, so any permutation of a pairwise-coprime `B` label set also preserves the witness.
- Ambiguities or missing definitions:
  - none that block the solve; the standard zero-divisor graph convention and the four support classes are already fixed by the campaign dossier.

## approach_A

- Structural / invariant route through the support graph.
- The edge pattern is the same as in the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 29` are therefore forced:
  - `A-C = 20 · 28 = 560`;
  - `B-B = 6`;
  - `B-C = 4 · 28 = 112`;
  - `B-D = 4 · 112 = 448`.
- Total predicted edge count: `560 + 6 + 112 + 448 = 1126`.
- So the exact graph problem reduces again to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Brief self-check after Approach A:
  - vertex count check: `20 + 4 + 28 + 112 = 164`;
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`, so no new graph-theoretic obstruction appears at `p = 29`.

## approach_B

- Construction / extremal route using the fixed barrier set that emerged in the `p = 23` feeder.
- Keep the same sparse barrier set on `B`:
  `B = {1,19,23,29}`.
- Its nontrivial multiples up to `164` are exactly:
  - for `19`: `38,57,76,95,114,133,152`;
  - for `23`: `46,69,92,115,138,161`;
  - for `29`: `58,87,116,145`.
- Those `17` forced spill labels still fit inside the fixed `20` slots of `A`, leaving exactly `3` filler slots.
- The key arithmetic observation at `p = 29` is that `|C| = 28` and there are exactly `28` primes in `(29,164]`:
  `31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163`.
- So the cleaner barrier-threshold version of the template closes here with no repair language at all: put all primes greater than `29` onto `C`.
- Put on `A` the `17` nontrivial multiples of `19`, `23`, and `29` together with the `3` harmless fillers `2,3,4`:
  `A = {2,3,4,38,46,57,58,69,76,87,92,95,114,115,116,133,138,145,152,161}`.
- Why this is enough:
  - every label in `A ∪ B` is either at most `29` or a multiple of one of `19,23,29`;
  - every label in `C` is a prime strictly greater than `29`;
  - therefore no label in `A ∪ B` is divisible by any prime in `C`, so all `A-C` and `B-C` edges are automatically coprime;
  - every nontrivial multiple of `19`, `23`, or `29` has been forced into `A`, so `D` is automatically coprime to `B`.
- One explicit classwise partition suggested by this reasoning is:
  - `C = {31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163}`;
  - `B = {1,19,23,29}`;
  - `A = {2,3,4,38,46,57,58,69,76,87,92,95,114,115,116,133,138,145,152,161}`;
  - `D` gets the remaining `112` labels.
- Brief self-check after Approach B:
  - `|C| = 28` matches the number of primes in `(29,164]` exactly;
  - the forced barrier spill from `B` has size `17`, leaving `3` free `A` slots;
  - none of the chosen `A ∪ B` labels is divisible by any chosen `C` prime.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,28,112`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For this instance, it is sufficient to choose:
   - `B = {1,19,23,29}`;
   - `A` containing every nontrivial multiple of `19`, `23`, and `29` in `{1,...,164}`;
   - `C` equal to all primes in `(29,164]`;
   - `D` as the remaining complement.
7. Under that choice, every `A ∪ B` label avoids all `C` prime factors, every pair in `B` is coprime, and every `D` label avoids the barrier primes `19,23,29`.
8. Therefore any partition of `{1,...,164}` into class label sets satisfying those obligations gives a prime labeling.

## chosen_plan

- Reuse the stable four-class support decomposition.
- Preserve the fixed sparse barrier set `B = {1,19,23,29}`.
- Use the cleaner barrier-threshold formulation from `p = 23`: choose `C` from primes greater than `29`, not from a moving half-interval condition.
- Because `p = 29` is a campaign boundary case, permit only a tiny post-reasoning checker to confirm the prime count, the barrier spill count, and one explicit classwise witness on the direct ring graph.
- Brief self-check after choosing the plan:
  - this remains reasoning-first because the witness is dictated by the support reduction and divisibility structure, not by search;
  - the only justified code is bounded checking after the construction is already fixed.

## self_checks

- Statement lock:
  - the exact target is the feeder instance `Γ(Z_29 × Z_25)`;
  - the label interval length `164` matches the vertex count.
- Structural reduction:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the full graph again collapses to three arithmetic interfaces.
- Construction:
  - the barrier spill from `B` has size `17`;
  - the prime pool `(29,164]` has size `28`, exactly `|C|`;
  - the chosen `A` fillers `2,3,4` add no new conflict with `C`.
- Final witness:
  - `A`, `B`, and `C` are disjoint and have sizes `20,4,28`;
  - the remaining complement has size `112`, exactly `|D|`;
  - every nontrivial multiple of `19`, `23`, or `29` lies in `A`, not `D`;
  - every label in `A ∪ B` is coprime to every label in `C`.
- Tiny checker:
  - direct recomputation gave `164` vertices and `1126` edges;
  - the edge-type counts were exactly `{A-C: 560, B-B: 6, B-C: 112, B-D: 448}`;
  - one explicit classwise witness had `label_bijection_ok = 1` and `edge_coprime_ok = 1`.

## code_used

- Minimal code was used only after the reasoning and explicit class partition were fixed.
- The code was a tiny bounded checker run inline, not a search:
  - one short arithmetic count confirmed that the interval `(29,164]` contains exactly `28` primes and that the barrier spill from `19,23,29` inside `{1,...,164}` has size `17`;
  - one direct ring-graph checker enumerated the `164` nonzero zero-divisors of `Z_29 × Z_25`, generated edges from the zero-product rule, checked bijectivity onto `{1,...,164}`, and confirmed `gcd = 1` on every edge for one explicit classwise witness.
- Checker outputs:
  - `vertex_count = 164`
  - `edge_count = 1126`
  - `edge_type_counts = {A-C: 560, B-B: 6, B-C: 112, B-D: 448}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163` on `C` in any order;
  - put the labels `1,19,23,29` on `B` in any order;
  - put the labels `2,3,4,38,46,57,58,69,76,87,92,95,114,115,116,133,138,145,152,161` on `A` in any order;
  - put the remaining `112` labels on `D` in any order.
- Why this works:
  - `B-B` edges: `1,19,23,29` are pairwise coprime.
  - `A-C` and `B-C` edges: every label on `C` is a prime `> 29`, while every label on `A ∪ B` is either at most `29` or a multiple of `19`, `23`, or `29`; hence no `A ∪ B` label shares a prime factor with any `C` label.
  - `B-D` edges: every nontrivial multiple of `19`, `23`, and `29` up to `164` was deliberately placed in `A`, so no label in `D` is divisible by any nontrivial label on `B`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; the fixed barrier set `B = {1,19,23,29}`; and the barrier-threshold rule that `C` may be chosen from primes greater than `29`.
  - what part does not yet scale:
    the family still needs a quantified counting lemma proving both
    1. that `{1,...,5p+19}` contains at least `p - 1` primes greater than `29`, and
    2. that the total number of nontrivial multiples of `19`, `23`, and `29` inside `{1,...,5p+19}` stays at most `20`.
  - what theorem slice is suggested:
    a barrier-threshold sufficient-condition theorem for `Γ(Z_p × Z_25)` using `B = {1,19,23,29}`, `A` as the barrier-multiple reservoir, and `C` chosen from primes greater than `29`.
  - what one or two next feeder instances would help most:
    `Γ(Z_31 × Z_25)` and `Γ(Z_37 × Z_25)`, because `p = 31` is the next near-full-reservoir case and `p = 37` is the first obvious pressure point where the fixed barrier spill is likely to exceed the `20` available `A` slots.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is closer to a paper-shaped claim because it pushes the cleaner barrier-threshold template through the next named campaign boundary test.

## family_affinity

- Family affinity is high.
- This feeder sits directly on the active `Γ(Z_p × Z_25)` campaign line and is one of the explicit boundary tests named by the campaign ledger.
- Its value is not only that `p = 29` appears to survive, but that it survives with the same barrier-threshold package already visible at `p = 23`.

## generalization_signal

- Generalization signal is strong.
- At `p = 29`, the witness hits a clean equality boundary:
  the interval `(29,164]` contains exactly `28 = p - 1` usable `C` primes.
- So the relevant family invariant is now visibly
  - the prime count above the fixed threshold `29`, and
  - the spill count of the fixed barrier set `19,23,29`.
- This pushes the campaign away from ad hoc instance repair and toward a real counting-based theorem slice.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. fix the sparse barrier set `B = {1,19,23,29}`;
  4. put every nontrivial multiple of `19`, `23`, and `29` into `A`;
  5. choose `C` from primes greater than `29`;
  6. fill the remaining `A` slots with labels not divisible by any chosen `C` prime;
  7. assign the residual complement to `D`.
- The main reusable gain from this feeder is that the `p = 29` boundary still closes without reviving the older half-interval spill language.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, `Γ(Z_p × Z_25)` is prime whenever the interval `{1,...,5p+19}` admits
  - at least `p - 1` primes greater than `29`, and
  - at most `20` nontrivial multiples of `19`, `23`, and `29`,
  because then one may take
  - `B = {1,19,23,29}`,
  - `A` to be all those barrier multiples plus arbitrary safe fillers,
  - `C` to be any `p - 1` primes from `(29,5p+19]`,
  - `D` to be the remaining complement.
- The present feeder is the next clean boundary instance for that formulation because the prime count lands exactly on `p - 1` at `p = 29`.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on the four-class line is `p = 31`.
- Reason:
  it is the next odd prime after `29`, and the fixed barrier spill already rises to `19` of the `20` available `A` slots there.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage feeder, not a verified publication package, and Lean has not been used on the exact instance.
- It is publication-relevant because it extends the cleaner barrier-threshold pattern through a named campaign boundary case rather than through another low-parameter warmup.
- The likely publishable unit is still not the single `p = 29` witness, but a quantified slice controlling the prime pool above `29` and the fixed barrier spill into `A`.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the now-stable `Γ(Z_p × Z_25)` reduction.
- The arithmetic failure point would be a missed nontrivial multiple of `19`, `23`, or `29` left in `D`.
- Another arithmetic failure point would be a mistaken count of primes in `(29,164]`.
- Publication-wise, the main weakness is that the fixed barrier set may stop fitting into the `20` slots of `A` not far beyond this boundary.

## what_verify_should_check

- Recompute the `164` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `1126` edges.
- Recount the `28` primes in `(29,164]`.
- Recount the `17` nontrivial multiples of `19`, `23`, and `29` inside `{1,...,164}`.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,164}`.
- Check coprimality on every actual edge from the ring graph.
- In the bounded rediscovery pass, audit not only the exact `p = 29` instance but also whether any existing sufficient-condition theorem for `Γ(Z_p × Z_25)` already implies the barrier-threshold slice isolated here.
- If verification passes, promote `z29-z25` immediately into the family generalization dossier and then test `z31-z25` before any exact-instance Lean work.

## verify_rediscovery

- PASS 1 stayed within the bounded web budget and used searches for the exact tuple `Γ(Z_29 × Z_25)`, the ASCII variant `Z_29 x Z_25`, the alternate family notation `Γ(Z_p × Z_(q^2))`, the canonical source itself, and a same-source theorem / conjecture check.
- Those searches did not reveal an earlier theorem, proposition, example, observation, or corollary settling the exact `p = 29, q = 5` instance.
- The canonical source check again pointed to Fox and Mooney, `On prime labelings of zero-divisor graphs`, published online on `2025-11-21`. In that source, nearby solved families include cases such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))`, while the ambient `Γ(Z_p × Z_(q^2))` line is still presented as Conjecture `4.4`, not as a theorem implying `Γ(Z_29 × Z_25)`.
- I stopped the web pass there rather than spending more budget after the canonical source clearly failed to establish rediscovery.
- Verdict for PASS 1: no rediscovery established.

## verify_faithfulness

- The solve claim matches the intended statement exactly: the full simple zero-divisor graph `Γ(Z_29 × Z_25)` on its `164` nonzero zero-divisors admits a prime labeling by `{1,...,164}`.
- There is no drift to a support graph, quotient, partial labeling, or merely sufficient proxy condition. The support classes are used only to reduce the exact graph to verified arithmetic interfaces.
- The classwise "any order" claim is faithful here. Independent recomputation showed that every vertex in each of `A`, `B`, `C`, and `D` has the same class-neighborhood profile, so permutations within a fixed class preserve adjacency obligations.

## verify_proof

- I rebuilt the vertex set directly from the ring law and again obtained `|A| = 20`, `|B| = 4`, `|C| = 28`, and `|D| = 112`, for total `164` vertices.
- I independently rebuilt the edge set and again found only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `560`, `6`, `112`, and `448`, for total `1126` edges.
- Given that support graph, the proof reduces correctly to three obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly. The displayed `A`, `B`, and `C` sets are disjoint, have the required sizes, and leave exactly `112` labels for `D`. Direct gcd checks found no bad pair on `A-C`, `B-B`, `B-C`, or `B-D`.
- The arithmetic hinge is valid: every label in `A ∪ B` is either at most `29` or divisible by one of `19`, `23`, or `29`, while every label in `C` is a prime strictly greater than `29`, so no `C`-prime divides any label in `A ∪ B`.
- First incorrect step found: none.

## verify_adversarial

- No stored checker file exists in this artifact, so I reran the computation independently from scratch rather than trusting the solve log.
- That recomputation again returned `vertex_count = 164`, `edge_count = 1126`, `edge_type_counts = {'A-C': 560, 'B-B': 6, 'B-C': 112, 'B-D': 448}`, `bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I separately recounted the arithmetic reservoirs without optional libraries:
  - the interval `(29,164]` contains exactly `28` primes;
  - the nontrivial multiples of `19`, `23`, and `29` up to `164` are exactly `38,46,57,58,69,76,87,92,95,114,115,116,133,138,145,152,161`, so the forced spill size is `17`.
- I also checked that every class has a uniform neighborhood profile, which is the only place the "assign labels in any order within a class" language could have failed. It did not fail.
- I did not find a hidden edge type, a misplaced forced multiple in `D`, a bad gcd edge, or a mismatch between the direct ring graph and the classwise witness.

## verify_theorem_worthiness

- This remains a feeder instance, not a family theorem. On its own it is not publishable.
- It still points to a real theorem slice, so the best honest publication status is `SLICE_CANDIDATE` rather than `INSTANCE_ONLY`. The reason is structural: `p = 29` is the clean equality boundary where the prime pool `(29,164]` has exactly `28 = p - 1` elements, so the fixed barrier-threshold package survives at a named campaign frontier rather than by ad hoc repair.
- The part that scales is the four-class support reduction together with the fixed barrier set `B = {1,19,23,29}`, the rule that `A` absorbs all nontrivial barrier multiples, and the choice of `C` from primes greater than `29`.
- The part that does not yet scale is the quantified counting argument. The campaign still lacks a proof that `{1,...,5p+19}` always has enough primes above `29` and that the barrier spill from `19,23,29` stays within the `20` available `A` slots.
- The smallest next feeder that most tests the template is `Γ(Z_31 × Z_25)`, because it is the next odd prime after `29` and pushes the `A` reservoir closer to saturation.

## verify_verdict

- `VERIFIED`
- No rediscovery was established, the claim matches the intended instance exactly, and the explicit classwise witness survived skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed and this verifier pass does not upgrade instance evidence into a Lean-backed theorem.

## minimal_repair_if_any

- None. No conservative repair was needed.
