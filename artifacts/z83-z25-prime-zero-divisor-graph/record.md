# Solve Record: z83-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_83 × Z_25) prime?`
- Active slug: `z83-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_83 × Z_25)` admits a prime labeling, meaning a bijection from its `434` vertices to `{1,2,...,434}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_83 × Z_25`, not to a full all-`p` family theorem.
- Brief self-check:
  - `|V| = 20 + 4 + 82 + 328 = 434`, so the label interval length matches the vertex count.
  - The solve target is the full simple zero-divisor graph, not only the support graph or a proxy template.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_83` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the usual four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_83^×}`, size `82`.
  - `D = {(a,5t) : a ∈ Z_83^×, t ∈ {1,2,3,4}}`, size `328`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 83` and `bd = 0 mod 25`.
- Because `Z_83` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions and ambiguities locked here:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - labels may be permuted arbitrarily inside `A`, `C`, and `D` once the class label sets are fixed, because those classes have uniform neighborhoods;
  - labels may also be permuted inside `B` because the four `B` vertices form a `K_4` and the chosen `B` labels are pairwise coprime.
- Brief self-check:
  - no missing graph convention remains that changes the support partition or the edge set.
  - the late-regime family notation from the active campaign fits this exact instance without modification.

## approach_A

- Structural / invariant route through the support graph.
- The exact edge pattern is the standard `Γ(Z_p × Z_25)` pattern:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 83` are therefore forced:
  - `A-C = 20 · 82 = 1640`;
  - `B-B = 6`;
  - `B-C = 4 · 82 = 328`;
  - `B-D = 4 · 328 = 1312`.
- Total predicted edge count: `1640 + 6 + 328 + 1312 = 3286`.
- Therefore the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- The campaign-relevant late-regime insight is that the fixed reservoir
  `A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`
  already solves the `A` side, so the remaining burden is only to choose a high barrier `B` and a size-`82` complementary-support set `C`.
- Brief self-check:
  - the structural reduction is unchanged from the family dossier, so any failure at `p = 83` would have to be arithmetic, not graph-theoretic.
  - the support graph still exposes only the three classwise coprimality interfaces above.

## approach_B

- Construction / extremal / contradiction route using the live high-barrier complementary-support wrapper.
- Let `N = 5p + 19 = 434`, so `N/2 = 217`.
- Choose the high barrier
  `B = {1,223,227,229}`,
  where `223`, `227`, and `229` are distinct primes strictly above `217`.
- Because each nontrivial barrier prime is above half the interval, every multiple `m b_i` with `m ≥ 2` already exceeds `N`; hence no label in `{1,...,434} \ B` is divisible by `223`, `227`, or `229`.
- Freeze
  `A = A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
  Every element of `A0` has prime support contained in `{2,3}`.
- So any label whose prime support avoids `{2,3,223,227,229}` is automatically coprime to every label in `A ∪ B`.
- Count such labels:
  - numbers in `{1,...,434}` coprime to `6` number
    `434 - floor(434/2) - floor(434/3) + floor(434/6) = 434 - 217 - 144 + 72 = 145`;
  - among these, `1`, `223`, `227`, and `229` are reserved for `B`;
  - therefore there remain `145 - 4 = 141` labels in the interval whose prime support avoids `{2,3,223,227,229}` and which are not in `B`.
- Since `141 > 82 = |C|`, the complementary-support pool is far larger than needed. In particular, the first `82` such labels give an explicit candidate:
  `C = {5,7,11,13,17,19,23,25,29,31,35,37,41,43,47,49,53,55,59,61,65,67,71,73,77,79,83,85,89,91,95,97,101,103,107,109,113,115,119,121,125,127,131,133,137,139,143,145,149,151,155,157,161,163,167,169,173,175,179,181,185,187,191,193,197,199,203,205,209,211,215,217,221,233,235,239,241,245,247,251,253,257}`.
- Let `D` be the residual complement
  `{1,...,434} \ (A ∪ B ∪ C)`.
- Brief self-check:
  - the argument does not depend on any search-heavy optimization; the only real count is `145 - 4 = 141`.
  - the chosen `C` labels include composites such as `25`, `35`, and `49`, which is allowed because only prime-support avoidance matters in the late wrapper, not primality of each `C` label.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,82,328`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For `B = {1,223,227,229}`, the nontrivial barrier labels are pairwise coprime and have no multiples in `{1,...,434}` outside `B` itself because each exceeds `434/2`.
7. For `A = A0`, every label in `A` has prime support contained in `{2,3}`.
8. Every label in the chosen `C` set has prime support avoiding `{2,3,223,227,229}`.
9. Therefore every label in `C` is coprime to every label in `A ∪ B`.
10. Every label in `D` lies outside `B`, so no label in `D` is divisible by `223`, `227`, or `229`; hence every label in `D` is coprime to every nontrivial label on `B`.
11. Therefore the classwise coprimality obligations all hold, and any bijection within classes gives a prime labeling of the full graph.

## chosen_plan

- Use the exact four-class support reduction from the campaign.
- Freeze the late-regime reservoir `A = A0`.
- Choose the smallest convenient barrier primes above half the interval:
  `223`, `227`, `229`.
- Fill `C` by explicit complementary-support labels, not by a prime-only pool.
- Let `D` absorb the residual complement.
- Only after the full reasoning and explicit class partition are fixed, use one tiny bounded verifier to check the witness directly on the ring graph.
- Brief self-check:
  - this matches the active publication-mode wrapper language exactly.
  - it tests the live supply statement at `p = 83` without reopening the obsolete small-spill regime.

## self_checks

- Statement lock:
  - the exact target is the feeder instance `Γ(Z_83 × Z_25)`;
  - the label interval `{1,...,434}` matches the vertex count.
- Structural reduction:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the predicted edge count is `3286`.
- High barrier:
  - `223`, `227`, `229` are distinct primes above half the interval;
  - therefore they create zero spill outside `B`.
- Complementary-support count:
  - there are `145` labels in `{1,...,434}` coprime to `6`;
  - after reserving `1,223,227,229` for `B`, `141` labels remain for `C`, well above the needed `82`.
- Explicit witness:
  - `A`, `B`, and `C` are pairwise disjoint and have sizes `20,4,82`;
  - the residual complement has size `328`, exactly `|D|`;
  - every `c ∈ C` is coprime to every label in `A ∪ B`;
  - every `d ∈ D` is coprime to the nontrivial barrier labels `223`, `227`, and `229`.

## code_used

- Minimal code was used only after the reasoning and explicit class partition were fixed.
- A tiny inline Python verifier:
  - generated the `434` nonzero zero-divisors of `Z_83 × Z_25`;
  - regenerated edges directly from the ring multiplication rule;
  - assigned labels classwise using the explicit sets `A`, `B`, `C`, and `D`;
  - checked bijectivity onto `{1,...,434}` and `gcd = 1` on every edge.
- Verifier output:
  - `vertex_count = 434`
  - `class_sizes = 20, 4, 82, 328`
  - `edge_count = 3286`
  - `edge_type_counts = {A-C: 1640, B-B: 6, B-C: 328, B-D: 1312}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - `A = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`;
  - `B = {1,223,227,229}`;
  - `C = {5,7,11,13,17,19,23,25,29,31,35,37,41,43,47,49,53,55,59,61,65,67,71,73,77,79,83,85,89,91,95,97,101,103,107,109,113,115,119,121,125,127,131,133,137,139,143,145,149,151,155,157,161,163,167,169,173,175,179,181,185,187,191,193,197,199,203,205,209,211,215,217,221,233,235,239,241,245,247,251,253,257}`;
  - `D = {1,...,434} \ (A ∪ B ∪ C)`.
- Why this works:
  - `B-B`: `1,223,227,229` are pairwise coprime.
  - `A-C` and `B-C`: every `c ∈ C` has prime support avoiding `{2,3,223,227,229}`, while every label in `A ∪ B` has prime support contained in that set.
  - `B-D`: because `223`, `227`, and `229` exceed half the interval, no label in `D` is divisible by any nontrivial barrier prime.
  - there are no other edges by the exact support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the exact support reduction; the fixed reservoir `A = A0`; the high-barrier choice `B = {1,b1,b2,b3}` above half the interval; and the complementary-support criterion for `C`.
  - what part does not yet scale:
    this record does not prove a general existence theorem for choosing enough `C` labels for all odd primes; it only shows the widened `C`-pool still has ample room at `p = 83`.
  - what theorem slice is suggested:
    the fixed-`A0`, high-barrier, complementary-support wrapper theorem already emphasized in the family dossier, with the distinct-vertex `B-B` bridge as the remaining packaging gap.
  - what one or two next feeder instances would help most:
    only if feeder work is reopened after packaging stalls, `Γ(Z_89 × Z_25)` and `Γ(Z_97 × Z_25)` are the natural next supply-pressure tests for the same late wrapper.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is materially closer to the paper-shaped family claim because it clears the first post-`z79` pressure test in exactly the live wrapper regime rather than in an obsolete local template.

## family_affinity

- Family affinity is high.
- This feeder was chosen only because theorem packaging stalled and the campaign needed one more honest pressure test after preserved successes through `p = 79`.
- The solve package directly supports the live `Γ(Z_p × Z_25)` publication target: fixed `A0`, high barrier above half the interval, complementary-support `C`, and residual `D`.

## generalization_signal

- Generalization signal is strong.
- At `p = 83`, the widened `C` clause is not close to exhausted: the interval supplies `141` admissible complementary-support labels while only `82` are needed.
- So the main publication blocker still does not look like raw late-regime supply at this parameter. The more honest blocker remains theorem packaging:
  the distinct-vertex `B-B` bridge and the final referee-facing wrapper statement.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. use the exact bridge so only `A-C`, `B-B`, `B-C`, and `B-D` matter;
  3. freeze `A = A0`;
  4. choose `B = {1,b1,b2,b3}` with distinct barrier primes above half the active interval;
  5. choose `C` as any size-`p-1` set of labels whose prime support avoids `{2,3,b1,b2,b3}`;
  6. let `D` be the residual complement.
- Relative to the earlier feeders, the reusable gain here is that no spill-management bookkeeping is needed at all once the barrier is above half the interval and `C` is allowed to use complementary-support composites.

## candidate_theorem_slice

- Candidate slice:
  let `N = 5p + 19` and fix
  `A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
  If there are distinct primes `b1,b2,b3 > N/2` and a set `C_lab ⊆ {1,...,N} \ (A0 ∪ {1,b1,b2,b3})` of size `p-1` such that every prime divisor of every `c ∈ C_lab` avoids `{2,3,b1,b2,b3}`, then with
  `A = A0`,
  `B = {1,b1,b2,b3}`,
  and
  `D = {1,...,N} \ (A ∪ B ∪ C_lab)`,
  the graph `Γ(Z_p × Z_25)` is prime.
- The current feeder exactly instantiates this slice with
  `p = 83`,
  `N = 434`,
  and
  `(b1,b2,b3) = (223,227,229)`.

## smallest_param_shift_to_test

- The smallest next parameter shift worth testing is not immediate feeder churn but theorem packaging.
- If feeder work is forced to continue, the next useful parameter is `p = 89`, because it preserves the same late high-barrier regime while increasing the required `C` pool from `82` to `88`.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder with no verify-stage rediscovery audit in this pass and no Lean closure on the exact instance.
- It is publication-relevant because it closes exactly in the live late-regime wrapper language and suggests that the family bottleneck is still statement packaging rather than arithmetic collapse at `p = 83`.
- The likely publishable unit is the family theorem slice, not the single `p = 83` witness by itself.

## likely_failure_points

- The main mathematical failure point would be a hidden edge type outside `A-C`, `B-B`, `B-C`, `B-D`, though that would contradict the exact family support decomposition.
- The main arithmetic failure point would be accidentally placing into `C` a label divisible by `2`, `3`, `223`, `227`, or `229`.
- Another arithmetic failure point would be accidentally placing one of the barrier primes into `D`, though the explicit partition rules this out.
- Publication-wise, the real weakness is not this instance but the absence of a frozen referee-facing wrapper theorem with the corrected distinct-vertex `B-B` clause.

## what_verify_should_check

- Recompute the `434` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `3286` edges.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,434}`.
- Recheck that every `c ∈ C` has prime support avoiding `{2,3,223,227,229}`.
- Verify coprimality on every actual edge of the ring graph.
- In the bounded rediscovery pass, audit both the exact `p = 83` instance and whether any existing sufficient-condition theorem already implies the fixed-`A0`, high-barrier, complementary-support slice used here.
- If verification passes, return immediately to family packaging rather than escalating this exact instance alone to Lean.

## verify_rediscovery

- PASS 1 used a bounded live web audit and then stopped browsing.
- Search patterns covered:
  - the exact instance notation `Γ(Z_83 × Z_25)` and ASCII variants such as `Gamma(Z_83 x Z_25)` together with `prime labeling` and `zero-divisor graph`;
  - alternate family notation such as `Γ(Z_p × Z_25)` and `Γ(Z_p × Z_{q^2})`;
  - the canonical source `On Prime Labelings of Zero-Divisor Graphs` by Fox and Mooney;
  - theorem / proposition / example / observation / corollary checks within that same source;
  - one bounded later status / citation sweep.
- What the bounded pass found:
  - no hit within budget explicitly settled the exact feeder `Γ(Z_83 × Z_25)`;
  - the canonical Fox-Mooney source was still the closest on-topic source returned;
  - within that source, the ambient `Γ(Z_p × Z_{q^2})` direction still appeared as a conjectural/open family rather than a theorem already covering `(p,q) = (83,5)`;
  - no later paper, proposition, example, corollary, or sufficient-condition statement was found within budget that directly implies the exact `p = 83` instance or the fixed-`A0`, high-barrier, complementary-support wrapper used here.
- Rediscovery conclusion:
  - rediscovery was not established within the required bounded pass;
  - this remains a candidate proof of an apparently frontier-open feeder instance, not a proof of a clearly known settled result.

## verify_faithfulness

- The solve record stays locked to the exact intended graph-theoretic statement: existence of a prime labeling for the full zero-divisor graph `Γ(Z_83 × Z_25)` on all `434` nonzero zero-divisors.
- The graph convention and label interval are the right ones:
  - vertices are exactly the nonzero zero-divisors of `Z_83 × Z_25`;
  - adjacency is exact coordinatewise zero product in the ring;
  - the target labeling is a bijection onto `{1,...,434}`.
- I found no wrong-theorem drift, quantifier drift, or replacement of the target by a support-graph proxy. The family-wrapper discussion is presented as campaign interpretation on top of the instance witness, not as the proved claim itself.

## verify_proof

- I independently recomputed the four support classes from the ring law:
  - `|A| = 20`;
  - `|B| = 4`;
  - `|C| = 82`;
  - `|D| = 328`;
  - total `434`.
- I independently recomputed adjacency from coordinatewise multiplication modulo `83` and `25`. The only edge families are exactly:
  - `A-C`;
  - `B-B`;
  - `B-C`;
  - `B-D`;
  with total edge count `3286`.
- Given that exact edge pattern, the arithmetic reduction is correct:
  - `B = {1,223,227,229}` is pairwise coprime, so the `B` clique is valid;
  - every label in `A = A0` has prime support contained in `{2,3}`;
  - every label in the displayed `C` set avoids prime divisors in `{2,3,223,227,229}`, so every `A-C` and `B-C` edge joins coprime labels;
  - because `223`, `227`, and `229` all exceed `434/2`, no label outside `B` is divisible by any nontrivial barrier prime, so every `B-D` edge is automatically coprime.
- First incorrect step found: none in the mathematical argument.

## verify_adversarial

- PASS 4 reran the witness verification independently from the record and tried to break the construction on the full ring graph, not just on the support abstraction.
- Independent checker results:
  - `vertex_count = 434`;
  - `class_sizes = {A: 20, B: 4, C: 82, D: 328}`;
  - `edge_count = 3286`;
  - `edge_type_counts = {A-C: 1640, B-B: 6, B-C: 328, B-D: 1312}`;
  - the displayed `A`, `B`, and `C` label sets are disjoint and the residual set for `D` has exactly `328` labels;
  - the final assignment is a bijection onto `{1,...,434}`;
  - `bad_edges = 0`.
- Additional adversarial checks:
  - I verified the full edge set directly from the ring multiplication law instead of trusting the class summary;
  - I verified independently that every displayed `c ∈ C` avoids prime divisors in `{2,3,223,227,229}`;
  - I verified that `D` contains none of the nontrivial barrier labels `223,227,229`.
- I did not find a hidden edge family, duplicated label, or computation/prose mismatch that breaks the witness.

## verify_theorem_worthiness

- This feeder does suggest a real theorem slice rather than a purely hand-picked isolated exact.
- What clearly scales:
  - the four-class support decomposition of `Γ(Z_p × Z_25)`;
  - the fixed reservoir `A = A0`;
  - the high-barrier choice `B = {1,b1,b2,b3}` with `b1,b2,b3 > N/2`;
  - the complementary-support criterion for `C`;
  - the residual-complement role of `D`.
- What does not yet scale automatically:
  - a referee-facing existence statement guaranteeing enough `C` labels over a genuine prime range;
  - the graph-faithful bridge replacing the current all-pairs `B-B` premise by the distinct-vertex version;
  - any claim that the current feeder alone proves a full odd-prime family theorem.
- Best honest publication status is not merely `INSTANCE_ONLY` in campaign context. This verified feeder is the first post-`z79` pressure test named by the active family status file, and it confirms that the live fixed-`A0`, high-barrier, complementary-support wrapper still works at `p = 83`. That is enough theorem leverage for `SLICE_CANDIDATE`, but not for `SLICE_EXACT` or `FAMILY_CANDIDATE`.
- The smallest next feeder that most sharply tests the same wrapper, if feeder work is forced to continue, is `Γ(Z_89 × Z_25)`.

## verify_verdict

- `verify_verdict = "VERIFIED"`
- The exact intended statement appears to be proved correctly by the current explicit witness, and the bounded rediscovery pass did not establish prior-art settlement of this exact instance.
- Because Lean has not been completed, the harness classification must remain `CANDIDATE`, not `EXACT`.
- `lean_ready = true`

## minimal_repair_if_any

- No mathematical repair to the witness was needed.
- One conservative metadata repair is necessary: do not leave this run labeled `EXACT`, and do not treat the family-wrapper language as already proved by the instance alone.
