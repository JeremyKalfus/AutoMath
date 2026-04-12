# Solve Record: z31-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_31 × Z_25) prime?`
- Active slug: `z31-z25-prime-zero-divisor-graph`.
- Locked exact intended statement: determine whether the full simple zero-divisor graph `Γ(Z_31 × Z_25)` admits a prime labeling, meaning a bijection from its `174` nonzero zero-divisors to `{1,2,...,174}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_31 × Z_25`, not to a broader all-`p` family theorem.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_31` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`;
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`;
  - `C = {(a,0) : a ∈ Z_31^×}`, size `30`;
  - `D = {(a,5t) : a ∈ Z_31^×, t ∈ {1,2,3,4}}`, size `120`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 31` and `bd = 0 mod 25`.
- Because `Z_31` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - labels may be permuted freely inside `A`, `C`, and `D` once those class label sets are fixed because vertices in each of those classes have identical neighborhoods;
  - the four `B` vertices form a `K_4`, so any permutation of a pairwise-coprime `B` label set also preserves the witness.
- Ambiguities, conventions, or missing definitions:
  - no blocking ambiguity remains after fixing the standard campaign convention that `Γ(R)` is the simple graph on nonzero zero-divisors with adjacency by zero product;
  - the only scope caution is publication-facing: a positive exact witness here is still feeder evidence until a family slice or Lean closure is packaged separately.

## approach_A

- Structural / invariant route through the support graph.
- The exact support-level edge pattern is the same as in the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 31` are therefore forced:
  - `A-C = 20 · 30 = 600`;
  - `B-B = 6`;
  - `B-C = 4 · 30 = 120`;
  - `B-D = 4 · 120 = 480`.
- Total predicted edge count: `600 + 6 + 120 + 480 = 1206`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.

## approach_B

- Construction / extremal route using the cleaner fixed-barrier threshold that emerged at `p = 23`.
- Keep the stable sparse barrier set
  `B = {1,19,23,29}`.
- Its nontrivial multiples up to `174` are exactly:
  - for `19`: `38,57,76,95,114,133,152,171`;
  - for `23`: `46,69,92,115,138,161`;
  - for `29`: `58,87,116,145,174`.
- These are pairwise distinct because the pairwise least common multiples `19·23`, `19·29`, and `23·29` all exceed `174`.
- Therefore the fixed barrier contributes exactly `8 + 6 + 5 = 19` forced spill labels into `A`, leaving exactly one free `A` slot.
- Next count the candidate `C` labels.
- The interval `(29,174]` contains exactly `30 = p - 1` primes:
  `31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173`.
- So at `p = 31` the clean barrier-threshold package closes on the nose:
  - `C` can be all primes greater than `29`;
  - `A` can contain the `19` nontrivial multiples of `19,23,29` together with one harmless filler, say `2`;
  - `D` can be the remaining complement.
- One explicit classwise partition suggested by this reasoning is:
  - `B = {1,19,23,29}`;
  - `C = {31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173}`;
  - `A = {2,38,46,57,58,69,76,87,92,95,114,115,116,133,138,145,152,161,171,174}`;
  - `D` gets the remaining `120` labels.
- Why this is plausible without search:
  - every label in `C` is prime and strictly greater than every nontrivial prime factor used in `A ∪ B`;
  - every label in `A ∪ B` is either `1`, `2`, or a multiple of one of the barrier primes `19,23,29`;
  - every label in `D` avoids divisibility by `19`, `23`, and `29` because all such nontrivial multiples were already placed in `A`.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,30,120`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For this instance, it is sufficient to choose:
   - `B = {1,19,23,29}`;
   - `A` containing every nontrivial multiple of `19`, `23`, and `29` in `{1,...,174}`;
   - `C` equal to all primes in `(29,174]`;
   - `D` as the remaining complement.
7. Under that choice:
   - `B` is pairwise coprime;
   - every label in `A ∪ B` avoids all prime factors from `C`;
   - every label in `D` avoids the barrier primes `19`, `23`, and `29`.
8. Therefore any partition of `{1,...,174}` into class label sets satisfying those obligations yields a prime labeling of `Γ(Z_31 × Z_25)`.

## chosen_plan

- Use the stable four-class support reduction rather than any search-heavy method.
- Keep the campaign barrier set `B = {1,19,23,29}` fixed.
- Try the strongest clean path first:
  take `C` to be exactly the `30` primes in `(29,174]`, put all `19` barrier multiples into `A`, use `2` as the only filler in `A`, and let `D` be the complement.
- Only after the explicit class partition is fixed, use one tiny checker to validate the witness directly from the ring definition.

## self_checks

- After statement lock:
  - the target is the exact feeder instance `Γ(Z_31 × Z_25)`;
  - the vertex count `20 + 4 + 30 + 120 = 174` matches the label interval.
- After Approach A:
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`;
  - no new edge family appears at `p = 31`.
- After Approach B:
  - the barrier spill count is exactly `19`, so the fixed `20`-slot reservoir `A` is nearly saturated but not overfull;
  - the prime pool `(29,174]` has exactly `30` elements, so `C` also closes on the nose;
  - the two critical counts both hit near-boundary equality, which makes this feeder structurally informative rather than a slack-rich one-off.
- After the lemma graph:
  - the proof burden really is reduced to the three classwise coprimality obligations;
  - there is no hidden need for SAT, ILP, brute force, or generic optimization.
- After the chosen plan:
  - the witness is determined by explicit divisibility bookkeeping, not by search;
  - minimal code is justified only as post-construction witness verification.
- After code use:
  - the checker confirmed the predicted vertex count, edge count, edge-type counts, bijection, and edgewise coprimality.

## code_used

- Minimal code was used only after the reasoning and explicit class partition were fixed.
- A tiny local checker `check_witness.py` enumerates the `174` nonzero zero-divisors of `Z_31 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,174}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 174`
  - `edge_count = 1206`
  - `edge_type_counts = {A-C: 600, B-B: 6, B-C: 120, B-D: 480}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `1,19,23,29` on `B` in any order;
  - put the labels `31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173` on `C` in any order;
  - put the labels `2,38,46,57,58,69,76,87,92,95,114,115,116,133,138,145,152,161,171,174` on `A` in any order;
  - put the remaining `120` labels on `D` in any order.
- Why this works:
  - `B-B` edges: `1,19,23,29` are pairwise coprime.
  - `A-C` and `B-C` edges: every label on `C` is a prime greater than `29`, while every label on `A ∪ B` is either `1`, `2`, or divisible only by `19`, `23`, or `29`; hence no label in `A ∪ B` shares a prime factor with any label in `C`.
  - `B-D` edges: every nontrivial multiple of `19`, `23`, and `29` up to `174` was deliberately placed in `A`, so no label in `D` is divisible by any nontrivial label on `B`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; the fixed barrier set `B = {1,19,23,29}`; and the cleaner rule that `C` may be chosen from primes greater than the barrier threshold `29`.
  - what part does not yet scale:
    the family still lacks a proved counting theorem controlling both the prime supply in `(29,5p+19]` and the barrier spill size inside the fixed `20` slots of `A`;
    this exact positive witness does not by itself settle what happens once the barrier spill exceeds `20`.
  - what theorem slice is suggested:
    a barrier-threshold sufficient-condition slice for `Γ(Z_p × Z_25)` using `B = {1,19,23,29}`, `A` as the reservoir for all nontrivial barrier multiples, `C` chosen from primes greater than `29`, and `D` as the complement.
  - what one or two next feeder instances would help most:
    `Γ(Z_37 × Z_25)` as the first post-`31` stress test, because the fixed barrier spill rises to `22 > 20` there, and a companion revisit of `Γ(Z_29 × Z_25)` if its sidecar result is not yet canonical in this worktree.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is closer to a paper-shaped claim because `p = 31` is a near-sharp positive boundary point for the current fixed-barrier wrapper rather than a slack-rich example.

## family_affinity

- Family affinity is high.
- This feeder sits directly on the live `Γ(Z_p × Z_25)` campaign line and tests the exact barrier-threshold wrapper named by the current family status.
- The main campaign value is that `p = 31` closes at near-saturation on both critical counts: the `C` prime pool is exactly full and the `A` reservoir has only one spare slot.

## generalization_signal

- Generalization signal is strong.
- At `p = 31`, the clean barrier-threshold package survives without any repaired spill bookkeeping:
  `C` is exactly the set of primes greater than `29`, and `A` is almost exactly the set of nontrivial multiples of `19,23,29`.
- This suggests the right family question is now sharper than before:
  determine the exact parameter range in which the fixed barrier `B = {1,19,23,29}` simultaneously gives enough primes for `C` and keeps the barrier spill within the `20`-slot reservoir `A`.
- The current feeder points toward a threshold-style slice or breakpoint theorem, not just another isolated witness.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. fix the sparse pairwise-coprime barrier set `B = {1,19,23,29}`;
  4. put every nontrivial multiple of `19`, `23`, and `29` into `A`;
  5. choose `C` from primes greater than `29`;
  6. fill any remaining `A` capacity with safe labels that avoid the `C` prime factors;
  7. assign the residual complement to `D`.
- Relative to the earlier four-class feeders, the reusable gain here is near-sharpness:
  the same template now survives at a point where both the `C` supply and the `A` spill budget are almost tight.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p`, `Γ(Z_p × Z_25)` is prime whenever the interval `{1,...,5p+19}` contains
  - at least `p - 1` primes greater than `29`, and
  - at most `20` nontrivial multiples of `19`, `23`, and `29`,
  because then one may take
  - `B = {1,19,23,29}`,
  - `A` to be those barrier multiples plus any safe fillers,
  - `C` to be any `p - 1` primes from `(29,5p+19]`,
  - `D` to be the remaining complement.
- The `p = 31` feeder is important because it shows this slice surviving almost exactly at its arithmetic boundary rather than only in earlier slack regimes.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this line is `p = 37`.
- Reason:
  `p = 31` appears to be a near-saturation positive case for the current fixed-barrier wrapper, while at `p = 37` the same barrier contributes `9 + 7 + 6 = 22` nontrivial multiples, which would exceed the `20` available slots of `A` and therefore stress or break the present wrapper.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder, with no bounded rediscovery pass in this turn and no Lean closure.
- It is publication-relevant because it is not a random positive instance: it is a near-sharp positive boundary case for the live `Γ(Z_p × Z_25)` wrapper named in the family dossier.
- The likely publishable object is still a theorem slice or breakpoint theorem about the fixed barrier-threshold package, not the isolated `p = 31` witness by itself.

## likely_failure_points

- The structural failure point would be a missed support-class edge type, though that would contradict the now-stable four-class reduction.
- The arithmetic failure point would be an omitted nontrivial multiple of `19`, `23`, or `29` accidentally left in `D`.
- Another arithmetic failure point would be an accidental `A ∪ B` label sharing a prime factor with one of the chosen `C` primes, though the threshold choice `C = {primes > 29}` avoids that cleanly here.
- Publication-wise, the main weakness is that the wrapper is still justified by exact-instance arithmetic rather than by a proved family counting lemma.

## what_verify_should_check

- Recompute the `174` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `1206` edges.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,174}`.
- Check coprimality on every actual edge from the ring graph.
- In the bounded rediscovery pass, audit not only the exact `p = 31` instance but also whether any existing sufficient-condition theorem already implies this fixed-barrier threshold witness.
- If verification passes, fold this feeder into generalize before any exact-instance Lean work.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact tuple `Γ(Z_31 × Z_25)`, ASCII variants such as `Gamma(Z_31 x Z_25)`, the family notation `Γ(Z_p × Z_(q^2))`, the canonical source title `On prime labelings of zero-divisor graphs`, same-source theorem / proposition / corollary checks, and one bounded later-status search.
- Exact-instance and alternate-notation searches did not reveal an earlier theorem, proposition, example, observation, or corollary settling this exact `p = 31, q = 5` case.
- The canonical source check pointed to the Combinatorial Press paper `On prime labelings of zero-divisor graphs`, published online on `2025-11-21`. Within that source, nearby solved families include results such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))`, while the broader family `Γ(Z_p × Z_(q^2))` is presented as Conjecture `4.4`, not as a theorem implying `Γ(Z_31 × Z_25)`.
- The bounded later-status search did not produce a newer published closure of either the exact `p = 31, q = 5` instance or the full `Γ(Z_p × Z_(q^2))` line.
- Verdict for PASS 1: no rediscovery established within the allotted audit.

## verify_faithfulness

- The solve record targets the exact intended statement: the full simple zero-divisor graph `Γ(Z_31 × Z_25)` on its `174` nonzero zero-divisors admits a prime labeling by a bijection to `{1,...,174}`.
- There is no wrong-theorem drift to a support graph, quotient graph, or partial labeling. The support classes are used only as a reduction device for the exact graph.
- The witness description is faithful at the vertex level: labels may be permuted inside `A`, `C`, and `D` because those classes have uniform neighborhoods, while `B` is handled separately by the fact that its four vertices form a `K_4` with pairwise-coprime labels.
- I did not find quantifier drift, changed definitions, or a mismatch between the prose claim and the actual solved object.

## verify_proof

- I recomputed the vertex partition directly from the ring definition and again recovered `|A| = 20`, `|B| = 4`, `|C| = 30`, and `|D| = 120`, for total `174` vertices.
- I independently recomputed the edge set and again obtained only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `600`, `6`, `120`, and `480`, for total `1206` edges.
- Given that support graph, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- I checked those obligations directly. The displayed `A`, `B`, and `C` sets are disjoint, have the required sizes, and leave exactly `120` labels for `D`. Every nontrivial multiple of `19`, `23`, or `29` up to `174` lies in `A`, not `D`.
- The key arithmetic sentence is valid here: every label in `A ∪ B` is either `1`, `2`, or has all prime factors in `{19,23,29}`, while every label in `C` is a prime greater than `29`; hence no `C`-prime divides any label in `A ∪ B`.
- First incorrect step found: none.

## verify_adversarial

- I reran `artifacts/z31-z25-prime-zero-divisor-graph/check_witness.py`. It again reported `vertex_count = 174`, `edge_count = 1206`, `edge_type_counts = {'A-C': 600, 'B-B': 6, 'B-C': 120, 'B-D': 480}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran an independent recomputation outside the artifact checker to confirm:
  - the four class label sets are disjoint and cover exactly `{1,...,174}`;
  - the complement assigned to `D` has size `120`;
  - no nontrivial multiple of `19`, `23`, or `29` lands in `D`;
  - direct gcd checks on `A-C`, `B-B`, and `B-D` found no bad pair;
  - there is no hidden edge type beyond `A-C`, `B-B`, `B-C`, and `B-D`.
- I did not find a counterexample edge, a mislabeled vertex, or a computational mismatch between the ring graph and the arithmetic witness.

## verify_theorem_worthiness

- This is still one verified feeder instance, not a theorem slice by itself.
- It does materially strengthen the live `Γ(Z_p × Z_25)` campaign because `p = 31` is a near-boundary positive case for the fixed barrier `B = {1,19,23,29}`: the barrier spill occupies `19` of the `20` available `A` slots, and the interval `(29,174]` contains exactly `30 = p - 1` usable primes for `C`.
- The structural part that scales is the four-class support reduction together with the fixed sparse barrier set and the rule that `A` absorbs all nontrivial multiples of the barrier labels while `C` is taken from primes greater than `29`.
- The part that does not yet scale automatically is the family counting lemma. The current proof does not prove, for general `p`, that the barrier spill stays within the `20` slots of `A` and that `(29,5p+19]` always contains at least `p - 1` usable primes.
- The best honest publication status is therefore `SLICE_CANDIDATE`, not `PAPER_READY`: this instance is still feeder evidence, but it is strong feeder evidence because it sits almost exactly at the arithmetic threshold of the current wrapper.
- The smallest next parameter shift that most tests the claimed template is `Γ(Z_37 × Z_25)`, where the same fixed barrier produces `22` nontrivial multiples and therefore should stress or break the present `20`-slot reservoir argument.

## verify_verdict

- `VERIFIED`
- No rediscovery was established in PASS 1, the claim matches the intended instance exactly, and the explicit witness survived skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- None. No conservative repair was needed.
