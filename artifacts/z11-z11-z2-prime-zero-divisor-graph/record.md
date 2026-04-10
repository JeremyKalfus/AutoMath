# Solve Record: Is the zero-divisor graph `Γ(Z_11 × Z_11 × Z_2)` prime?

## statement_lock
- Active title: `Is the zero-divisor graph Γ(Z_11 × Z_11 × Z_2) prime?`
- Active slug: `z11-z11-z2-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_11 × Z_11 × Z_2)` admits a prime labeling, meaning a bijection from its `141` vertices to `{1,2,...,141}` such that adjacent vertices receive coprime labels.
- This solve pass is locked to the exact feeder instance `Γ(Z_11 × Z_11 × Z_2)`, not the full family `Γ(Z_p × Z_p × Z_2)`.

Self-check:

- `|Z_11 × Z_11 × Z_2| = 11 * 11 * 2 = 242`.
- Units are exactly the triples with all coordinates nonzero, so there are `10 * 10 * 1 = 100` units.
- Hence the nonzero zero-divisors are `242 - 100 - 1 = 141`, matching the label interval.

## definitions
- Write `U = Z_11^× = {1,2,...,10}`.
- The nonzero zero-divisors split into six support classes:
  - `A_i = (i,0,0)` for `i in U`, size `10`.
  - `B_i = (0,i,0)` for `i in U`, size `10`.
  - `C = (0,0,1)`, size `1`.
  - `D_ij = (i,j,0)` for `i,j in U`, size `100`.
  - `E_i = (i,0,1)` for `i in U`, size `10`.
  - `F_i = (0,i,1)` for `i in U`, size `10`.
- Because multiplication is coordinatewise and each coordinate ring is a field, two vertices are adjacent exactly when in each coordinate at least one entry is `0`, equivalently when their supports are disjoint.
- Therefore the only edge families are:
  - `A-B`
  - `A-C`
  - `A-F`
  - `B-C`
  - `B-E`
  - `C-D`
- There are no other edges, and vertices inside a fixed support class are pairwise nonadjacent.

Self-check:

- The class sizes sum to `10 + 10 + 1 + 100 + 10 + 10 = 141`.
- The support graph edge count is `|A||B| + |A||F| + |B||E| + |A| + |B| + |D| = 100 + 100 + 100 + 10 + 10 + 100 = 420`.
- A classwise label partition is enough, because vertices inside one support class have identical neighborhoods.

## approach_A
Structural / invariant approach.

- The singleton `C` is the hinge vertex: it is adjacent to all of `A ∪ B ∪ D`, and every vertex of `D` is adjacent only to `C`.
- So the natural move is to assign label `1` to `C`. Then all `A-C`, `B-C`, and `C-D` edges are automatically valid, and the entire `D` class becomes unconstrained.
- After fixing `C = 1`, only three cross-class interfaces remain:
  - `A-B`
  - `A-F`
  - `B-E`
- A clean way to force all three is to let `A ∪ E` use only prime factors from `{2,3}`, while `B ∪ F` uses labels coprime to `6`.
- For `N = 141`, the nontrivial `{2,3}`-smooth numbers are
  `2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108,128`,
  so there are `21` of them.
- Since `|A ∪ E| = 20`, this already gives enough room to fill both smooth classes without search.
- Also, there are far more than `20` labels in `{2,...,141}` coprime to `6`, so `B ∪ F` can be chosen from that complement.

Self-check:

- This reduction is exact, not heuristic: once `C = 1`, the `D` class really is free.
- The only remaining burden is a finite interval-partition problem on `40` labels, not the full `141`-vertex graph.
- The smooth-count closes at `p = 11` with one spare label, so no brute force is justified here.

## approach_B
Construction / extremal approach.

- Use the count from Approach A to write an explicit classwise witness:
  - `C <- {1}`
  - `A <- {2,3,4,6,8,9,12,16,18,24}`
  - `E <- {27,32,36,48,54,64,72,81,96,108}`
  - `B <- {5,7,11,13,17,19,23,25,29,31}`
  - `F <- {35,37,41,43,47,49,53,55,59,61}`
- Every label in `A ∪ E` is `{2,3}`-smooth.
- Every label in `B ∪ F` is coprime to `6`.
- Therefore:
  - every `A-B` pair is coprime;
  - every `A-F` pair is coprime;
  - every `B-E` pair is coprime.
- The remaining `100` unused labels may be assigned arbitrarily to the `100` vertices of `D`.

Self-check:

- The displayed class sets are pairwise disjoint.
- The constrained classes use exactly `1 + 10 + 10 + 10 + 10 = 41` labels, leaving `141 - 41 = 100` labels for `D`.
- No label in `B ∪ F` is divisible by `2` or `3`, so the three required interfaces are all safe.

## lemma_graph
Proof skeleton:

1. Classify the `141` vertices into the six support classes `A,B,C,D,E,F`.
2. Prove adjacency is exactly disjointness of support.
3. Deduce the exact edge pattern `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`.
4. Assign label `1` to `C`; this settles every edge incident to `C` and frees the whole `D` class.
5. Partition the remaining labels so that `A ∪ E` is `{2,3}`-smooth and `B ∪ F` is coprime to `6`.
6. Check only the three remaining interfaces `A-B`, `A-F`, and `B-E`.
7. Assign the residual `100` labels arbitrarily to `D` and conclude that every edge joins coprime labels.

Self-check:

- No omitted edge family remains after Step 3.
- Steps 4 through 7 use only classwise arguments, so no vertex-by-vertex search is needed.

## chosen_plan
- Use Approach A to lock the support graph and isolate the three true arithmetic interfaces.
- Use Approach B to give an explicit witness with `C = 1`, a `{2,3}`-smooth reservoir for `A ∪ E`, and labels coprime to `6` for `B ∪ F`.
- Use only a tiny post-reasoning arithmetic checker to guard against transcription mistakes in the displayed sets and to record the `p = 13` breakpoint count for the naive `{2,3}`-smooth reservoir.

Self-check:

- This remains reasoning-first: the witness is dictated by the support decomposition and a transparent counting argument.
- The code decision comes only after the proof skeleton and witness were already fixed.

## self_checks
- Statement-lock check: the target stayed the exact feeder instance `Γ(Z_11 × Z_11 × Z_2)`.
- Structural check: the six support classes are correct, and the active family dossier captures the same reduction after `C = 1`, though its campaign summary omits the harmless edge families `A-C` and `B-C`.
- Count check: `A ∪ E` needs `20` labels, and there are `21` nontrivial `{2,3}`-smooth labels up to `141`.
- Residual check: the constrained classes use `41` labels, leaving exactly `100` labels for `D`.
- Conservatism check: this is still solve-stage `CANDIDATE`, not `EXACT`, because Lean is off and verify has not run.

## code_used
- A tiny inline arithmetic checker was used only after the reasoning and explicit class partition were fixed.
- It checked:
  - the list of nontrivial `{2,3}`-smooth labels up to `141`;
  - that the chosen `A,E,B,F,C` sets are disjoint;
  - that the three required interface conditions `gcd(A,B)=gcd(A,F)=gcd(B,E)=1` hold classwise;
  - that exactly `100` labels remain for `D`;
  - and that the same naive `{2,3}`-smooth reservoir has size `24` up to `193`, exactly matching the `p = 13` requirement of `24`.
- No search, optimization, SAT, ILP, CP-SAT, or brute force was used.

## result
- Current best solve-stage result: an explicit prime-labeling candidate exists for `Γ(Z_11 × Z_11 × Z_2)`.
- Assign labels as follows, in any order within each support class:
  - `C <- {1}`
  - `A <- {2,3,4,6,8,9,12,16,18,24}`
  - `E <- {27,32,36,48,54,64,72,81,96,108}`
  - `B <- {5,7,11,13,17,19,23,25,29,31}`
  - `F <- {35,37,41,43,47,49,53,55,59,61}`
  - `D <-` the remaining `100` labels in `{1,...,141}`
- Why this works:
  - every edge incident to `C` is valid because `C` has label `1`;
  - every `A-B` and `A-F` edge is valid because each `A` label has prime support contained in `{2,3}`, while each `B` and `F` label is coprime to `6`;
  - every `B-E` edge is valid for the same reason;
  - there are no other edges.
- Solve-stage classification: `CANDIDATE`.

- What part of the argument scales:
  - the six-class support decomposition;
  - the `C = 1` hinge trick that frees `D`;
  - the reduction to the three interfaces `A-B`, `A-F`, `B-E`;
  - the idea of treating `A ∪ E` as a smooth reservoir and `B ∪ F` as its coprime complement.
- What part does not yet scale automatically:
  - the specific choice of the prime-support set `{2,3}`;
  - the finite count showing enough smooth labels for `A ∪ E`;
  - the fact that the naive `{2,3}`-smooth reservoir closes at `p = 11` and becomes exactly tight at `p = 13`.
- Suggested theorem slice:
  - a sufficient-condition slice for `Γ(Z_p × Z_p × Z_2)` saying that if `{1,...,p^2+2p-2}` contains `2(p-1)` nontrivial labels supported on a fixed small prime set `S`, and another `2(p-1)` labels coprime to every prime in `S`, then the graph is prime after setting `C = 1`.
- Highest-value next feeder instances:
  - `Γ(Z_13 × Z_13 × Z_2)`, because the naive `{2,3}`-smooth reservoir is already zero-slack there and forces either a refined template or an exact tight packing;
  - `Γ(Z_13 × Z_25)`, because it is the parallel next tight feeder on the paired campaign.
- Current publication shape:
  - this is still an instance-level witness package, but it is closer to a paper-shaped claim than a random one-off because it isolates a concrete family mechanism and a concrete first place where the naive version becomes tight.

Self-check:

- The witness is explicit at the class level and uses exactly the right number of labels.
- The supporting generalization claim is modest: it is about the current template, not about all odd primes.

## family_affinity
- Family affinity is high.
- This is the campaign-designated decisive feeder for the six-class `Γ(Z_p × Z_p × Z_2)` line at `p = 11`.
- The proof uses exactly the support-template mechanism already identified in the family record, so it directly strengthens the paired publication campaign rather than adding an unrelated exact.

## generalization_signal
- Generalization signal is strong.
- The `p = 11` feeder shows that the cleanest current arithmetic template actually survives the first designated breakpoint on the `Γ(Z_p × Z_p × Z_2)` side.
- It also exposes the first honest tension point: the same naive `{2,3}`-smooth reservoir has size `24` up to `193`, exactly matching the `p = 13` requirement of `24`, so the next step really does need either an exact tight packing or a refined reservoir argument.

## proof_template_reuse
- Reusable proof template:
  1. classify the six support classes `A,B,C,D,E,F`;
  2. prove the edge pattern `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`;
  3. set `C = 1` so `D` becomes free;
  4. choose a small prime-support reservoir for `A ∪ E`;
  5. choose `B ∪ F` from labels avoiding that prime support;
  6. dump the residual complement into `D`.
- This is reusable both for later feeders and for a support-template theorem statement.

## candidate_theorem_slice
- Candidate slice: for odd prime `p`, if the interval `{1,...,p^2+2p-2}` admits
  - a set `L_A ∪ L_E` of size `2(p-1)` supported on a fixed small prime set `S`,
  - a set `L_B ∪ L_F` of size `2(p-1)` coprime to every prime in `S`,
  - and `L_C = {1}`,
  then the exact support-template reduction yields a prime labeling of `Γ(Z_p × Z_p × Z_2)`.
- The present `p = 11` witness realizes this with `S = {2,3}`.

## smallest_param_shift_to_test
- The smallest next parameter shift to test is `p = 13`.
- Reason: the current naive `{2,3}`-smooth reservoir succeeds at `p = 11` with one spare label and becomes exactly tight at `p = 13`, so that is the first sharp discriminator between a real family theorem and a merely local template.

## why_this_is_or_is_not_publishable
- This is not publishable on its own yet because it is still a single exact feeder result with no verify-stage rediscovery audit and no Lean formalization.
- It is publication-relevant because it does more than settle one instance: it shows the six-class campaign template survives the exact feeder where the paired family program said it had to survive.
- The extra value is that it also identifies an honest next theorem-slice question: whether the current smooth-reservoir mechanism can be generalized past `p = 11`, or whether `p = 13` is the first failure of that naive template.

## likely_failure_points
- A support-graph mistake would be fatal, especially if some omitted edge family existed beyond `A-B`, `A-C`, `A-F`, `B-C`, `B-E`, `C-D`.
- An arithmetic transcription error in one of the displayed class sets could invalidate the witness.
- The publication-facing overreach risk would be claiming anything stronger than a `p = 11` feeder plus a template observation; the current record avoids that.

## what_verify_should_check
- First do the bounded rediscovery / prior-art pass required by the harness.
- Re-derive the six support classes and the exact edge pattern directly from coordinatewise zero product.
- Check that the displayed classwise label sets are disjoint and cover exactly `41` constrained labels, leaving `100` for `D`.
- Verify the three classwise coprimality interfaces `A-B`, `A-F`, and `B-E` independently.
- Audit the publication-facing side separately: confirm that the claimed `p = 13` note is a tightness statement for the naive `{2,3}`-smooth reservoir, not a claim that `Γ(Z_13 × Z_13 × Z_2)` itself is non-prime.

## verify_rediscovery

- PASS 1 used a bounded live web audit and then stopped browsing.
- Search patterns covered:
  - the exact instance notation `Γ(Z_11 × Z_11 × Z_2)` and `Gamma(Z_11 x Z_11 x Z_2)` with `prime labeling`
  - alternate family notation `Γ(Z_p × Z_p × Z_2)` and reordered tuple phrasing
  - the most relevant canonical recent source by title, `On Prime Labelings of Zero-Divisor Graphs`
  - theorem / proposition / example / observation / corollary checks inside that same source
  - one later status sweep for citations or follow-up discussion within budget
- What the bounded pass found:
  - the 2025 Fox-Mooney paper `On Prime Labelings of Zero-Divisor Graphs` remained the main on-topic source returned for this family
  - within that source, the broader family `Γ(Z_p × Z_p × Z_q)` still appears as an open conjectural direction rather than a settled theorem for the exact `p = 11`, `q = 2` tuple
  - no paper, theorem, proposition, example, or corollary within budget explicitly settled `Γ(Z_11 × Z_11 × Z_2)`
  - no later source within budget clearly implied or exhibited this exact instance either
- Rediscovery conclusion:
  - rediscovery was not established within the required bounded pass
  - this remains a candidate proof of an apparently frontier-open exact feeder instance, not a proof of a known settled result

## verify_faithfulness

- The solve record stays locked to the exact intended statement: existence of a prime labeling for the full zero-divisor graph `Γ(Z_11 × Z_11 × Z_2)`.
- The vertex set, graph convention, and label set are the right ones:
  - vertices are exactly the `141` nonzero zero-divisors of `Z_11 × Z_11 × Z_2`
  - adjacency is the exact coordinatewise-zero-product relation
  - the target is a bijection onto `{1,...,141}`
- The proof does not drift to a quotient graph, support graph proxy, partial labeling, or family statement. It gives a full classwise witness for all vertices.
- One dossier-consistency note is real but not fatal: the campaign summary tracks the three nontrivial arithmetic interfaces after fixing `C = 1`, but it omits the genuine edge families `A-C` and `B-C`. The solve artifact itself does not rely on omitting those edges, because `C` is labeled `1`.
- No wrong-theorem drift, quantifier drift, or definition change was found.

## verify_proof

- I independently recomputed the six support classes from the ring definition:
  - `|A| = 10`
  - `|B| = 10`
  - `|C| = 1`
  - `|D| = 100`
  - `|E| = 10`
  - `|F| = 10`
  - total `141`
- I independently recomputed adjacency from coordinatewise multiplication modulo `11,11,2`. The only edge families are exactly:
  - `A-B`
  - `A-C`
  - `A-F`
  - `B-C`
  - `B-E`
  - `C-D`
  with total edge count `420`.
- Given that edge pattern, the mathematical reduction is correct:
  - once `C` gets label `1`, every `A-C`, `B-C`, and `C-D` edge is automatically valid
  - every vertex of `D` is adjacent only to `C`, so the remaining `100` labels really are free on `D`
  - the only nontrivial arithmetic obligations are then `A-B`, `A-F`, and `B-E`
- Those obligations hold exactly as claimed:
  - every label in `A ∪ E` is supported on primes `{2,3}`
  - every label in `B ∪ F` is coprime to `6`
  - therefore every edge across `A-B`, `A-F`, and `B-E` joins coprime labels
- First incorrect step found: none in the mathematical argument. The only issue I found was the minor campaign-summary wording above, which does not affect the witness or the proof.

## verify_adversarial

- PASS 4 reran the witness verification independently from the record and tried to break the construction on the full graph, not just on the support graph abstraction.
- Independent checker results:
  - `vertex_count = 141`
  - `edge_count = 420`
  - `edge_families = {A-B, A-C, A-F, B-C, B-E, C-D}`
  - the displayed `A,B,C,E,F` label sets are pairwise disjoint and use exactly `41` labels
  - the residual set for `D` has exactly `100` labels
  - the final assignment is a bijection onto `{1,...,141}`
  - `bad_edges = 0`
- Additional adversarial checks:
  - I verified the full edge set directly from the ring multiplication law instead of trusting the class decomposition
  - I verified the claimed `{2,3}`-smooth reservoir count independently: there are `21` such nontrivial labels up to `141`
  - I verified the `p = 13` breakpoint claim in corrected form: the same naive `{2,3}`-smooth reservoir has size `24` up to `193`, exactly matching `2(p-1) = 24`, so this is a zero-slack tightness point, not a proof that `Γ(Z_13 × Z_13 × Z_2)` is non-prime
- I did not find a counterexample edge, a hidden omitted edge family, or a computation/prose mismatch that breaks the `p = 11` witness.

## verify_theorem_worthiness

- This feeder does suggest a real theorem slice rather than a purely hand-picked isolated exact.
- What clearly scales:
  - the six-class support decomposition
  - the hinge move `C = 1`
  - the reduction from the full graph to the three nontrivial interfaces `A-B`, `A-F`, and `B-E`
  - the sufficient-condition template "`A ∪ E` supported on a small prime set, `B ∪ F` avoiding that prime support"
- What does not yet scale automatically:
  - the specific choice `S = {2,3}`
  - the finite supply count for enough `S`-smooth labels in `{1,...,p^2+2p-2}`
  - the choice of a good complementary reservoir for `B ∪ F` once the naive smooth count tightens
- Best honest publication status is not merely `INSTANCE_ONLY`. This verified feeder directly strengthens an active family campaign and isolates a reusable support-template mechanism, so the honest status is `SLICE_CANDIDATE`, not `SLICE_EXACT` and not `FAMILY_CANDIDATE`.
- The smallest next feeder instance that most sharply tests the claimed template is `Γ(Z_13 × Z_13 × Z_2)`, because `p = 13` is exactly where the naive `{2,3}`-smooth reservoir first becomes zero-slack.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- The exact intended statement appears to be proved correctly by the current explicit witness, and the bounded rediscovery pass did not establish prior-art settlement of this exact instance.
- Because Lean has not been completed, the harness classification must remain `CANDIDATE`, not `EXACT`.
- `lean_ready = true`

## minimal_repair_if_any

- I made one tiny conservative repair to the solve record: a self-check sentence no longer claims that the campaign dossier explicitly listed all six edge families. The dossier only listed the reduced arithmetic interfaces after fixing `C = 1`.
- No mathematical repair to the witness or proof was needed.
