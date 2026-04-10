# Solve Record: z17-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_17 × Z_25) prime?`
- Active slug: `z17-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_17 × Z_25)` admits a prime labeling, meaning a bijection from its `104` vertices to `{1,2,...,104}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_17 × Z_25`, not the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_17` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the same four support classes used throughout the `Γ(Z_p × Z_25)` campaign:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_17^×}`, size `16`.
  - `D = {(a,5t) : a ∈ Z_17^×, t ∈ {1,2,3,4}}`, size `64`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 17` and `bd = 0 mod 25`.
- Because `Z_17` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - once a classwise label set is chosen, labels may be assigned inside each class in any order because vertices in the same support class have the same neighborhood.

## approach_A

Structural / invariant approach through the support graph.

- The support-level proof is unchanged from the earlier feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- The edge counts at `p = 17` are forced:
  - `A-C = 20 · 16 = 320`;
  - `B-B = 6`;
  - `B-C = 4 · 16 = 64`;
  - `B-D = 4 · 64 = 256`.
- Total predicted edge count: `320 + 6 + 64 + 256 = 646`.
- Therefore the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.

## approach_B

Construction / extremal approach by extending the refined small-spill `C` block.

- The old upper-half-prime-only `C` subtemplate is now even further short:
  - `|C| = 16`;
  - the interval `[53,104]` contains only `12` primes:
    `53,59,61,67,71,73,79,83,89,97,101,103`.
- So the pure “all `C` primes above half the interval” rule cannot work at `p = 17`.
- The natural continuation of the verified `p = 13` repair is to allow several primes below half the interval whose only extra multiples are doubles sent to `D`.
- Four such primes fit cleanly:
  `37,41,43,47`.
- Their only nontrivial multiples in `{1,...,104}` are:
  - `74 = 2·37`;
  - `82 = 2·41`;
  - `86 = 2·43`;
  - `94 = 2·47`.
- Hence a candidate `C` block is
  `C = {37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103}`.
- Keep the same sparse barrier set used successfully at `p = 11` and `p = 13`:
  `B = {1,19,23,29}`.
- Its nontrivial multiples up to `104` are:
  - for `19`: `38,57,76,95`;
  - for `23`: `46,69,92`;
  - for `29`: `58,87`.
- Those nine spill labels still fit inside the `20` available `A` slots.
- So one explicit classwise partition suggested by this logic is:
  - `C = {37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103}`.
  - `B = {1,19,23,29}`.
  - `A = {2,3,4,5,6,7,8,9,10,11,12,38,46,57,58,69,76,87,92,95}`.
  - `D` gets the remaining `64` labels.
- The key point is that the new `C` exceptions create only four extra forbidden labels for `A ∪ B`, while the old barrier set contributes nine required spill labels to `A`; together they still consume only a controlled part of the fixed `20`-slot `A` reservoir.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,16,64`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. A sufficient arithmetic sublemma for this instance is:
   if `C` is labeled by primes whose nontrivial multiples inside `{1,...,104}` all land in `D`, and if the nontrivial multiples of the pairwise-coprime barrier set `B` all land in `A`, then the classwise coprimality obligations are satisfied.
7. Therefore any partition of `{1,...,104}` into class label sets satisfying those obligations gives a prime labeling.

## chosen_plan

- Reuse the already stable four-class support decomposition.
- Preserve the successful sparse barrier set `B = {1,19,23,29}` unless it visibly breaks.
- Extend the refined `p = 13` idea by allowing four sub-half primes in `C`, not just two, provided their doubles stay out of `A ∪ B`.
- Only after the full witness is fixed, use one tiny checker to validate the explicit labeling against the ring definition.

## self_checks

- After statement lock:
  - the target remains the exact feeder instance `Γ(Z_17 × Z_25)`;
  - the vertex count `20 + 4 + 16 + 64 = 104` matches the intended label interval.
- After Approach A:
  - the support graph is still exactly the campaign template `A-C`, `B-B`, `B-C`, `B-D`;
  - no new edge family appears at `p = 17`.
- After Approach B:
  - the upper-half-prime-only `C` rule is genuinely too small by `4`, so a repair is necessary rather than cosmetic;
  - the proposed four exception primes `37,41,43,47` each generate only one extra conflict, namely their doubles;
  - the barrier spill set for `B = {1,19,23,29}` has size `9`, which still fits inside `A`.
- After choosing the plan:
  - this remains reasoning-first because the witness is dictated by the support reduction and finite divisibility bookkeeping, not by optimization search;
  - minimal code is justified only as post-construction witness verification.

## code_used

- After the reasoning and explicit class partition were fixed, a tiny local checker `check_witness.py` was used for witness verification.
- The checker enumerates the `104` nonzero zero-divisors of `Z_17 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,104}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 104`
  - `edge_count = 646`
  - `edge_type_counts = {A-C: 320, B-B: 6, B-C: 64, B-D: 256}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

Current best solve-stage candidate:

- Put the labels `37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103` on `C` in any order.
- Put the labels `1,19,23,29` on `B` in any order.
- Put the labels `2,3,4,5,6,7,8,9,10,11,12,38,46,57,58,69,76,87,92,95` on `A` in any order.
- Put the remaining `64` labels
  `13,14,15,16,17,18,20,21,22,24,25,26,27,28,30,31,32,33,34,35,36,39,40,42,44,45,48,49,50,51,52,54,55,56,60,62,63,64,65,66,68,70,72,74,75,77,78,80,81,82,84,85,86,88,90,91,93,94,96,98,99,100,102,104`
  on `D` in any order.

Why this works:

- `B-B` edges:
  `1,19,23,29` are pairwise coprime.
- `A-C` and `B-C` edges:
  every label on `C` is prime, and the only extra forbidden labels below `104` are `74,82,86,94`, the doubles of the four sub-half `C` primes. None of those labels is used on `A ∪ B`.
- `B-D` edges:
  every nontrivial multiple of `19,23,29` up to `104` is one of
  `38,46,57,58,69,76,87,92,95`, and those nine labels were deliberately placed in `A`.
- There are no other edges by the support decomposition.

Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.

Strong-result extraction:

- What part of the argument scales:
  the four-class support decomposition; the reduction to `A-C`, `B-B`, `B-C`, `B-D`; the fixed sparse barrier set on `B`; and the refined rule that `C` may use a bounded number of below-half primes provided their nontrivial multiples are pushed into `D`.
- What part does not yet scale automatically:
  the exact count of allowable below-half `C` exceptions and the exact prime choices still depend on interval arithmetic inside `{1,...,5p+19}`; this is not yet a closed all-`p` supply lemma.
- What theorem slice is suggested:
  a refined sufficient-condition theorem for `Γ(Z_p × Z_25)` where the `C` block is allowed a bounded small-spill set of prime labels below the half-interval threshold, with all resulting multiples excluded only from `A ∪ B`, not from the whole labeling.
- What one or two next feeder instances would help most:
  `Γ(Z_19 × Z_25)` as the immediate next four-class arithmetic stress test, and `Γ(Z_17 × Z_17 × Z_2)` as the matching campaign feeder on the parallel six-class line.
- Whether the current package is still just an instance or already closer to a paper-shaped claim:
  it is still an instance-level candidate, but it is materially closer to a paper-shaped claim because it promotes the `p = 13` repair into a genuine four-exception refinement of the family slice rather than a one-off patch.

## family_affinity

- Family affinity is high.
- This instance is the campaign-designated first post-`13` stress test on the four-class `Γ(Z_p × Z_25)` line.
- The solve package directly strengthens the publication target because it keeps the same support proof and shows the refined small-spill `C` program survives one more odd prime.

## generalization_signal

- Generalization signal is strong.
- The `p = 17` witness shows the refined `C` block is not merely a two-exception `p = 13` repair.
- The honest family-level signal is: at least through `p = 17`, the four-class line can tolerate a bounded number of below-half primes in `C` as long as their doubles move to `D` and the barrier spill from `B` still fits inside `A`.
- What is still missing is a reusable counting lemma that predicts how many such exceptions are available for general `p`.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into the support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. put on `B` a fixed sparse pairwise-coprime barrier set such as `1,19,23,29`;
  4. put on `C` a prime block consisting of all sufficiently high primes in the interval plus a bounded spill set of lower primes whose multiples are sent to `D`;
  5. put every nontrivial multiple of the barrier labels into `A`;
  6. assign the residual complement to `D`.
- Relative to the `p = 13` feeder, the only new reusable ingredient is that the spill size on `C` can now be at least `4`, not merely `2`.

## candidate_theorem_slice

- Candidate slice: for odd primes `p`, `Γ(Z_p × Z_25)` is prime whenever the interval `{1,...,5p+19}` admits
  - a set `C` of `p-1` prime labels such that every nontrivial multiple of a `C`-prime lying in the interval stays out of `A ∪ B`;
  - a `4`-element pairwise-coprime barrier set `B` whose nontrivial multiples outside `B` occupy at most `20` labels;
  - an `A` reservoir large enough to absorb those barrier multiples.
- The `p = 17` feeder suggests strengthening the slice to explicitly allow a bounded small-spill set of below-half `C` primes rather than insisting all `C` primes lie above half the interval.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this line is `p = 19`.
- Reason: `p = 17` now appears to survive with four `C` exceptions, so `p = 19` is the next honest discriminator for whether the refined small-spill arithmetic is still scaling.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still one exact feeder instance, solve-only, with no rediscovery audit and no Lean closure.
- It is publication-relevant because it converts the current family story from “the `p = 13` repair exists” to “the refined four-class arithmetic survives at least one further prime.”
- That is substantially closer to a theorem-slice claim than a random exact win, but the publishable unit is still the family reduction plus a quantified spill lemma, not the single `p = 17` witness by itself.

## likely_failure_points

- The structural failure point would be an omitted edge type in the support decomposition, though that would contradict the already stable `Γ(Z_p × Z_25)` template.
- The arithmetic failure point would be a missed nontrivial multiple of `19`, `23`, or `29` left inside `D`.
- A second arithmetic failure point would be accidentally placing one of the four doubled `C` exceptions `74,82,86,94` into `A ∪ B`.
- Publication-wise, the main weakness is that the argument still relies on hand-picked finite prime sets rather than a proven family supply theorem.

## what_verify_should_check

- Recompute the `104` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `646` edges.
- Check that the four classwise label sets are disjoint and cover exactly `{1,...,104}`.
- Check coprimality on every actual edge from the ring graph.
- In the bounded rediscovery pass, audit not only the exact instance but also whether any existing sufficient-condition theorem for `Γ(Z_p × Z_25)` already implies this `p = 17` case.
- If verification passes, treat this as a strong feeder for generalization before any Lean work on the exact instance.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact tuple, alternate notation, the family notation, and the canonical source itself.
- Exact-instance searches on `Γ(Z_17 × Z_25)` and ASCII variants such as `Z_17 x Z_25` with `zero-divisor graph` and `prime labeling` did not reveal an earlier theorem, proposition, example, observation, or corollary settling this exact case within budget.
- I rechecked the canonical 2025 source `On prime labelings of zero-divisor graphs`. Its open-problems section still states Conjecture 4.4 for the full family `Γ(Z_p × Z_{q^2})`, so the paper does not already present the `p = 17, q = 5` instance as a solved theorem. The same-source theorem checks also only surfaced nearby results such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_{p^2})`, not the present `Γ(Z_17 × Z_25)` case.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The claimed result matches the intended feeder statement exactly: existence of a prime labeling for the full simple zero-divisor graph `Γ(Z_17 × Z_25)` on the nonzero zero-divisors, with labels bijectively covering `{1,...,104}`.
- There is no wrong-theorem drift to a quotient graph, support graph, or partial labeling. The support decomposition is used only as a proof reduction for the exact graph.
- The solve record's statement that labels may be assigned "in any order" within a support class is faithful, because vertices inside each of `A`, `B`, `C`, and `D` have identical neighborhoods under the ring-based adjacency rule.

## verify_proof

- I recomputed the vertex partition from the ring definition and recovered class sizes `|A| = 20`, `|B| = 4`, `|C| = 16`, `|D| = 64`.
- I independently recomputed the exact edge families and obtained only `A-C`, `B-B`, `B-C`, and `B-D`, with counts `320`, `6`, `64`, and `256`, for total `646` edges.
- Given that edge pattern, the proof correctly reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the displayed witness:
  - the only nontrivial multiples in `{1,...,104}` of the `C`-primes are `74,82,86,94`, coming from `37,41,43,47`, and all four are outside `A ∪ B`;
  - `B = {1,19,23,29}` is pairwise coprime;
  - the nontrivial multiples of `19`, `23`, and `29` up to `104` are exactly `38,57,76,95`, `46,69,92`, and `58,87`, all placed in `A`, not `D`.
- First incorrect step found: none.

## verify_adversarial

- I reran the checker `artifacts/z17-z25-prime-zero-divisor-graph/check_witness.py`.
- It again reported `vertex_count = 104`, `edge_count = 646`, `edge_type_counts = {'A-C': 320, 'B-B': 6, 'B-C': 64, 'B-D': 256}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran an independent computation outside the artifact checker to confirm:
  - the four label classes are disjoint and cover exactly `{1,...,104}`;
  - the only nontrivial multiples of `C` inside the label interval are `74,82,86,94`;
  - no nontrivial multiple of `19`, `23`, or `29` lands in `D`;
  - there is no hidden edge type beyond `A-C`, `B-B`, `B-C`, `B-D`.
- I did not find a candidate counterexample edge, mislabeled vertex, or missed divisibility obstruction.

## verify_theorem_worthiness

- This is not only an isolated exact witness. Relative to the verified `p = 13` feeder, it shows the four-class `Γ(Z_p × Z_25)` line survives one more arithmetic stress test with four below-half `C` exceptions rather than two.
- The structural part that scales is the support decomposition and the reduction to the three classwise coprimality obligations. The fixed sparse barrier set `B = {1,19,23,29}` also still looks reusable.
- The part that does not yet scale automatically is the finite supply argument for the `C` block: the proof still hand-picks the exceptional primes `37,41,43,47` rather than deriving a quantified all-`p` spill lemma.
- The best honest publication status is therefore still `SLICE_CANDIDATE`, not `PAPER_READY` and not merely `INSTANCE_ONLY`, because this feeder does appear to strengthen a real family campaign.
- The smallest next discriminator for the claimed template is still `Γ(Z_19 × Z_25)`, which tests whether the small-spill `C` arithmetic remains viable past the first four-exception case.

## verify_verdict

- `VERIFIED`
- No rediscovery was established within the bounded prior-art pass, the candidate matches the intended statement, and the explicit witness survived skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- None. No conservative repair was needed.

## publication_prior_art_audit

- Audit date and scope:
  - On `2026-04-10` I ran a bounded web pass restricted to the exact instance `Γ(Z_17 × Z_25)`, the alternate notations `Z_17 × Z_25` and `Z_17 × Z_5^2`, the family notation `Γ(Z_p × Z_(q^2))`, the canonical source for prime-labeled zero-divisor graphs, and one recent discussion / status check.
- Exact statement search:
  - Searches on `Γ(Z_17 × Z_25)` with `prime labeling` and `zero-divisor graph` did not reveal an earlier theorem, proposition, example, or corollary settling this exact case within budget.
- Alternate notation search:
  - Searches on `Z_17 × Z_25`, `Z_17 × Z_5^2`, and `Γ(Z_p × Z_(q^2))` with the same prime-labeling keywords again led either back to the Fox-Mooney paper or to no relevant exact-match result within budget.
- Canonical source search:
  - The canonical source remains Fox and Mooney, `On Prime Labelings of Zero-Divisor Graphs` (2025).
  - Inside that paper, the nearby settled cases are still Theorem `2.14` for `Γ(Z_p × Z_9)` and Theorem `2.15` for `Γ(Z_2 × Z_(p^2))`.
  - The same paper still leaves the ambient family open in Conjecture `4.4` for `Γ(Z_p × Z_(q^2))`.
  - I checked inside the canonical source for a theorem / proposition / example / corollary / observation / sufficient-condition entry covering `Z_25`, `p = 17`, or a directly implying sufficient condition, and found none within budget.
- One outside-source status search:
  - A separate bounded search in adjacent zero-divisor-graph literature found structural papers on zero-divisor graphs of direct products and semisimple rings, which is enough to treat the raw support decomposition as standard background rather than the likely novelty claim here.
  - That outside pass did not produce an independent paper settling prime labelings of `Γ(Z_17 × Z_25)` or the full `Γ(Z_p × Z_(q^2))` family within budget.
- One recent citation / discussion / follow-up check:
  - The topic was still being presented publicly on `2025-03-09` at the AMS Southeastern Sectional Meeting under the title `On Prime Labelings of Zero-Divisor Graphs`.
  - Within the bounded `2026-04-10` pass, I did not find a later published closure of the exact `p = 17, q = 5` case or of the broader `Γ(Z_p × Z_(q^2))` line.
- Prior-art verdict:
  - No rediscovery was established within budget.
  - No evidence was found that this exact feeder has already been absorbed into a published family theorem.

## publication_statement_faithfulness

- The faithful claim is not `Γ(Z_p × Z_25)` prime for all odd primes and not even “the four-exception spill theorem is now proved.”
- The faithful claim is narrower:
  - `Γ(Z_17 × Z_25)` has a verified explicit prime-labeling witness;
  - the same witness reuses the campaign's four-class support reduction;
  - and at `p = 17` the working `C` block can absorb four below-half primes `37,41,43,47` whose doubles move to `D`.
- That four-exception observation is evidence for a future family spill lemma, not itself a quantified parameterized theorem.
- There is no theorem drift to a quotient graph or support graph:
  the claim remains about the full simple zero-divisor graph on the nonzero zero-divisors.
- Because neither the `F25` ring-to-support bridge nor a quantified all-`p` spill lemma is closed, stronger family wording would overstate the current proof surface.

## publication_theorem_worthiness

- Is the strongest honest claim stronger than “here is an example”?
  - No as a standalone publication claim.
  - The extra content is a reusable arithmetic pattern, but the preserved proof still culminates in one exact instance.
- Is there a real parameterized theorem, theorem slice, or counterexample theorem here?
  - Not in this feeder artifact alone.
  - It points toward a real `Γ(Z_p × Z_25)` theorem slice in the campaign, but this record does not itself close one.
- Is the proof structural or merely instance-specific?
  - Mixed.
  - The support reduction is structural, but the successful arithmetic closure is still instance-specific and hand-tuned.
- Would this survive a referee asking “what is the theorem?”
  - No.
  - The best honest answer would still be “here is the verified `p = 17` feeder and the four-exception pattern it suggests.”
- Is the claim still too dependent on hand-picked small cases?
  - Yes.
  - The proof depends on the explicit prime choices `37,41,43,47` and the fixed barrier set `1,19,23,29`, without a quantified family supply lemma.
- Is the generalization route strong enough to merit campaign priority?
  - Yes.
  - Clearing `p = 17` matters because the canonical family remains open and this is the first post-`13` arithmetic stress test on the active four-class line.
- Theorem-worthiness verdict:
  - For this artifact, the honest publication classification is `INSTANCE_ONLY`.
  - The theorem-slice status belongs at the campaign level until the quantified spill lemma and the `F25` ring-to-support bridge are closed.

## publication_publishability

- Publication status verdict:
  - set `publication_status = INSTANCE_ONLY`.
- Why not `REDISCOVERY`:
  - the bounded prior-art pass did not establish an earlier exact solution or a directly implying published theorem.
- Why not `SLICE_CANDIDATE` on this artifact:
  - the parameterized theorem statement is still external to this record;
  - this record contributes evidence toward that slice rather than a proved slice of its own.
- Why not `PAPER_READY`:
  - there is no closed theorem slice, no family proof, and no standalone paper story beyond one exact feeder with a promising pattern.
- Strongest publishable role for this artifact:
  - as a feeder/example inside a future `Γ(Z_p × Z_25)` theorem-slice paper section;
  - or as evidence motivating a quantified small-spill `C`-block lemma.
- Publishability verdict:
  - valuable campaign evidence, not yet a standalone theorem unit.

## strongest_honest_claim

- The strongest honest claim is that `Γ(Z_17 × Z_25)` admits an explicit verified prime labeling and that this instance shows the active four-class `Γ(Z_p × Z_25)` construction can absorb at least four below-half `C`-primes at `p = 17` while keeping the same sparse barrier set on `B`.
- That materially strengthens the family campaign, but it is still feeder evidence for a future spill lemma rather than a proved theorem slice.

## paper_title_hint

- `Verified p = 17 evidence for a small-spill C-block theorem on Γ(Z_p × Z_25)`

## next_action

- Fold the `p = 17` four-exception arithmetic into `artifacts/families/zero_divisor_prime_labelings/`, then run `Γ(Z_19 × Z_25)` as the next discriminator while prioritizing the missing `F25` ring-to-support bridge and a quantified spill-count lemma.
- Do not spend standalone Lean effort on the exact `p = 17` instance unless it becomes needed as a formal test case for the family lemmas.
