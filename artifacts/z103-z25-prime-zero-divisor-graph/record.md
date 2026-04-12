# Solve Record: z103-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_103 × Z_25) prime?`
- Active slug: `z103-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_103 × Z_25)` admits a prime labeling, meaning a bijection from its `534` vertices to `{1,2,...,534}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_103 × Z_25`, not to a full all-primes theorem for `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_103` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the campaign's four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_103^×}`, size `102`.
  - `D = {(a,5t) : a ∈ Z_103^×, t ∈ {1,2,3,4}}`, size `408`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 103` and `bd = 0 mod 25`.
- Because `Z_103` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - labels may be permuted freely inside `A`, `C`, and `D` once the class label sets are fixed, because those classes have uniform neighborhoods;
  - the four `B` vertices form a `K_4`, so any injective assignment of a pairwise-coprime `B` label set works.
- Ambiguities or missing definitions:
  - none that block the solve; the active family dossier and the existing `F25` ring-support bridge already fix the graph convention and the support classes.

## approach_A

- Structural / invariant route through the exact support graph.
- The support-level adjacency pattern is the same as in the earlier `Γ(Z_p × Z_25)` feeders:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- At `p = 103`, the forced edge counts are:
  - `A-C = 20 · 102 = 2040`;
  - `B-B = 6`;
  - `B-C = 4 · 102 = 408`;
  - `B-D = 4 · 408 = 1632`.
- Total predicted edge count: `2040 + 6 + 408 + 1632 = 4086`.
- So the exact graph problem again reduces to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Brief self-check after Approach A:
  - vertex count check: `20 + 4 + 102 + 408 = 534`;
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`, so there is no new graph-theoretic obstruction at `p = 103`.

## approach_B

- Construction / extremal route using the late high-barrier complementary-support wrapper rather than the earlier small-spill barrier-multiple template.
- The old low-barrier pattern from `p = 17,19,23` is no longer credible here:
  - with label interval `{1,...,534}`, the nontrivial multiples of `19`, `23`, and `29` already far exceed the fixed `20` slots of `A`;
  - so a late-regime solution must avoid forcing `A` to absorb those barrier multiples.
- The checked family wrapper suggests the right late package:
  - keep `A` equal to the fixed `2,3`-smooth reservoir
    `A0 = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`;
  - choose the high barrier set
    `B = {1,293,307,311}`;
  - choose `C` from labels whose prime support avoids `{2,3,293,307,311}`;
  - let `D` be the remaining complement.
- Why the barrier set is attractive at `p = 103`:
  - `5p + 19 = 534`;
  - `534 < 2·293 = 586`, `534 < 2·307 = 614`, and `534 < 2·311 = 622`;
  - hence every interval label divisible by `293`, `307`, or `311` must equal that barrier prime itself.
- Therefore:
  - the `B-D` interface becomes automatic once `D` avoids the four barrier labels;
  - `B-B` is automatic because `1,293,307,311` are pairwise coprime.
- The remaining issue is supply for `C`, where `|C| = 102`.
- The preserved fixed late window is
  `C0 = {n : 2 ≤ n ≤ 291 and gcd(n,6) = 1}`.
- Count for `C0`:
  - the numbers in `{1,...,291}` coprime to `6` are
    `291 - floor(291/2) - floor(291/3) + floor(291/6) = 291 - 145 - 97 + 48 = 97`;
  - removing `1` leaves `|C0| = 96`.
- So `p = 103` needs exactly `102 - 96 = 6` additional complementary-support labels beyond the preserved `C0` window.
- A clean six-label extension is
  `E = {295,301,305,313,317,319}`.
- These six labels all lie in `{1,...,534}` and each has prime support avoiding `{2,3,293,307,311}`:
  - `295 = 5·59`;
  - `301 = 7·43`;
  - `305 = 5·61`;
  - `313` is prime;
  - `317` is prime;
  - `319 = 11·29`.
- Hence a candidate `C` block is
  `C_lab = C0 ∪ E`.
- This gives exactly `96 + 6 = 102` labels for `C`, with the required support avoidance.
- Brief self-check after Approach B:
  - the late wrapper really is the relevant regime here; the older `A`-absorbs-barrier-multiples pattern is no longer competitive at `p = 103`;
  - the six extra labels are all explicit and support-safe;
  - `A`, `B`, and `C_lab` are visibly disjoint.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,102,408`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. Every label in `A0` has prime support contained in `{2,3}`.
4. Every label in `C_lab = C0 ∪ E` has prime support avoiding `{2,3,293,307,311}`.
5. Therefore every label in `A0` is coprime to every label in `C_lab`.
6. The labels `1,293,307,311` are pairwise coprime.
7. Because each of `293,307,311` is above half the interval `{1,...,534}`, any other interval label is automatically coprime to it.
8. Therefore any partition of `{1,...,534}` into `A0`, `B`, `C_lab`, and the residual complement `D_lab` gives a prime labeling of `Γ(Z_103 × Z_25)`.

## chosen_plan

- Use the stable four-class support reduction from the campaign.
- Abandon the early low-barrier arithmetic template and instead work directly in the checked high-barrier complementary-support language.
- Freeze
  - `A = A0`,
  - `B = {1,293,307,311}`,
  - `C = C0 ∪ {295,301,305,313,317,319}`,
  - `D` as the remaining complement.
- Because every required coprimality interface is then handled by structural support-avoidance rather than search, no code is justified unless the arithmetic bookkeeping later reveals a gap.
- Brief self-check after choosing the plan:
  - this is still reasoning-first;
  - the construction is not an optimization artifact;
  - the only finite arithmetic burden is the exact `96 + 6 = 102` count for `C`.

## self_checks

- Statement lock:
  - the exact target is the feeder instance `Γ(Z_103 × Z_25)`;
  - the label interval length `534` matches the vertex count.
- Structural reduction:
  - no new edge family appears beyond `A-C`, `B-B`, `B-C`, `B-D`;
  - the graph again collapses to three arithmetic interfaces.
- Late wrapper choice:
  - the old low-barrier reservoir logic is not the right template at this parameter;
  - the high-barrier choice `293,307,311` is valid because all three exceed half the interval.
- `C`-supply count:
  - `|C0| = 96`;
  - the six explicit extras `295,301,305,313,317,319` are distinct, in range, and support-safe;
  - so `|C_lab| = 102 = |C|`.
- Final partition count:
  - `|A| + |B| + |C| = 20 + 4 + 102 = 126`;
  - the residual complement has size `534 - 126 = 408 = |D|`.

## code_used

- No code used.
- Minimal code is not needed in this solve pass because the support graph, the barrier inequalities, the `C0` count, and the six extra complementary-support labels are all explicit and checkable by hand.

## result

- Current best solve-stage candidate:
  - put the labels
    `2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108`
    on `A` in any order;
  - put the labels `1,293,307,311` on `B` in any injective order;
  - put on `C` all labels in
    `C0 ∪ {295,301,305,313,317,319}`,
    where
    `C0 = {n : 2 ≤ n ≤ 291 and gcd(n,6) = 1}`;
  - put the remaining `408` labels on `D` in any order.
- Why this works:
  - `B-B` edges:
    `1,293,307,311` are pairwise coprime.
  - `A-C` edges:
    every label in `A` is `2,3`-smooth, while every label in `C` has prime support avoiding `2` and `3`.
  - `B-C` edges:
    every label in `C` has prime support avoiding `293`, `307`, and `311`.
  - `B-D` edges:
    every label in `D` differs from `293`, `307`, and `311`, and each of those primes is above half the interval `{1,...,534}`, so no other interval label can be divisible by them.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support reduction; the fixed `A0` reservoir; the high-barrier choice `B = {1,293,307,311}`; and the late complementary-support rule that `C` may contain any labels whose prime support avoids `{2,3,293,307,311}`.
  - what part does not yet scale:
    the argument still needs a counted supply lemma producing enough complementary-support labels beyond the preserved `C0` window once `p > 97`;
    here that shortage is filled by six hand-picked labels.
  - what theorem slice is suggested:
    a late-regime `Γ(Z_p × Z_25)` wrapper corollary of the form:
    if one can supply `p - 97` extra labels in `(291,5p+19]` whose prime support avoids `{2,3,293,307,311}`, then the fixed-data high-barrier wrapper yields a prime labeling.
  - what one or two next feeder instances would help most:
    `Γ(Z_101 × Z_25)` if the missing neighboring artifact still needs preservation in this worktree, and `Γ(Z_107 × Z_25)` as the next true parameter shift after the present `p = 103` solve.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still an instance-level candidate, but it is much closer to a paper-shaped claim because it explicitly extends the preserved `p ≤ 97` wrapper frontier by the exact amount `p - 97 = 6`.

## family_affinity

- Family affinity is very high.
- This feeder is not a random exact instance; it is the first active post-`97` stress test for the late `F25` complementary-support wrapper.
- The main publication value is that the solve package isolates the live blocker precisely: not the support reduction, but the counted supply of extra complementary-support labels beyond `C0`.

## generalization_signal

- Generalization signal is strong.
- The `p = 103` solve shows that the preserved late wrapper does not fail immediately beyond `97`; it only needs six additional support-safe `C` labels.
- That strongly suggests a quantified extension problem of the form
  `need p - 97 extra labels beyond C0`
  rather than a new graph-theoretic obstruction.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. use the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. freeze `A` at the `2,3`-smooth set `A0`;
  4. freeze `B` at a high-barrier set `{1,b1,b2,b3}` with each barrier prime above half the active interval;
  5. choose `C` from labels whose prime support avoids `{2,3,b1,b2,b3}`;
  6. assign the residual complement to `D`.
- For the present instance the only new ingredient beyond the preserved `p ≤ 97` wrapper is the six-label extension
  `{295,301,305,313,317,319}`.

## candidate_theorem_slice

- Candidate slice:
  for odd prime `p ≥ 59`, if the interval `{292,...,5p+19}` contains at least `p - 97` labels whose prime support avoids `{2,3,293,307,311}`, then `Γ(Z_p × Z_25)` is prime via
  - `A = A0`,
  - `B = {1,293,307,311}`,
  - `C = C0` plus any such `p - 97` extra labels,
  - `D` the remaining complement.
- The `p = 103` feeder is the first explicit local witness for this post-`97` extension statement.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this line is `p = 107`.
- Reason:
  the present solve already handles `p = 103`, and the next odd prime tests whether the same late wrapper can absorb `p - 97 = 10` extra complementary-support labels rather than just `6`.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder with no verify pass and no Lean closure for the new arithmetic extension.
- It is publication-relevant because it sharpens the open arithmetic frontier:
  the preserved structural slice remains intact, and the only live question exposed by `p = 103` is quantified complementary-support supply beyond `C0`.
- The likely publishable unit is still a family corollary or counted supply lemma, not the single `p = 103` witness by itself.

## likely_failure_points

- The structural failure point would be a missed edge type in the support decomposition, though that would contradict the stable `F25` bridge already used throughout the campaign.
- The arithmetic failure point would be a mistaken count for `|C0|`, since the exact witness depends on needing exactly six extras beyond the preserved window.
- Another arithmetic failure point would be an overlooked forbidden prime factor in one of `295,301,305,313,317,319`, though each factorization is short and explicit.
- Publication-wise, the main weakness is that the solve still hand-picks the extra complementary-support labels instead of proving a general supply theorem.

## what_verify_should_check

- Recompute the `534` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `4086` edges.
- Check that
  - `A = A0`,
  - `B = {1,293,307,311}`,
  - `C = C0 ∪ {295,301,305,313,317,319}`
  are pairwise disjoint and have sizes `20,4,102`.
- Confirm that every label in `C` has prime support avoiding `{2,3,293,307,311}`.
- Confirm that every label in `D` avoids the barrier labels and hence is coprime to `293,307,311`.
- In generalize, test whether the right family statement is exactly the `p - 97` extra-label supply lemma suggested here.

## verify_rediscovery

- PASS 1 used a bounded live-web audit aimed at the exact tuple `Γ(Z_103 × Z_25)`, ASCII variants such as `Gamma(Z_103 x Z_25)` and `Z_103 x Z_25`, the broader family notation `Γ(Z_p × Z_(q^2))`, the canonical source itself, and a bounded later-status check.
- The exact-instance and alternate-notation searches did not reveal an earlier theorem, proposition, example, observation, or corollary settling this exact `p = 103, q = 5` case within budget.
- The canonical-source check again pointed to the 2025 Combinatorial Press paper `On prime labelings of zero-divisor graphs`. In that source, nearby solved cases include families such as `Γ(Z_p × Z_9)` and `Γ(Z_2 × Z_(p^2))`, while the ambient family `Γ(Z_p × Z_(q^2))` is still presented as Conjecture `4.4`, not as a theorem implying `Γ(Z_103 × Z_25)`.
- The bounded later-status check did not uncover a newer published closure of either the exact `p = 103, q = 5` instance or the full `Γ(Z_p × Z_(q^2))` line.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The claimed result matches the exact intended mathematical statement: the full simple zero-divisor graph `Γ(Z_103 × Z_25)` on its `534` nonzero zero-divisors admits a prime labeling by `{1,...,534}`.
- There is no wrong-theorem drift to a support graph, quotient graph, or weaker proxy statement. The support classes are used only as a proof reduction for the exact graph.
- The feeder framing in `selected_problem.md` is campaign metadata, not a changed theorem statement. The solve record stays locked to the exact instance claim.
- The "any order" language inside support classes is faithful here because vertices inside each of `A`, `B`, `C`, and `D` have identical neighborhoods under the ring-based adjacency rule.

## verify_proof

- I recomputed the vertex partition directly from the ring definition and again recovered `|A| = 20`, `|B| = 4`, `|C| = 102`, and `|D| = 408`, for total `534` vertices.
- I independently recomputed the exact edge set and again obtained only the four edge families `A-C`, `B-B`, `B-C`, and `B-D`, with counts `2040`, `6`, `408`, and `1632`, for total `4086` edges.
- Given that support graph, the proof reduces correctly to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Those obligations hold for the displayed witness:
  - every label in `A0` is `2,3`-smooth;
  - every label in `C0 ∪ {295,301,305,313,317,319}` avoids the prime set `{2,3,293,307,311}`;
  - `B = {1,293,307,311}` is pairwise coprime;
  - `534 < 2·293`, `534 < 2·307`, and `534 < 2·311`, so the only labels in `{1,...,534}` divisible by `293`, `307`, or `311` are those barrier primes themselves, which are already assigned to `B`.
- The one sentence that needs cautious reading is lemma item `8`: it is correct only as "any within-class bijection using the fixed label sets `A0`, `B`, `C_lab`, and the residual complement `D_lab`," not as an arbitrary repartition of labels among the classes. The surrounding solve record already fixes those sets, so this is a prose ambiguity rather than a mathematical gap.
- First incorrect step found: none.

## verify_adversarial

- There was no preserved artifact checker for this dossier, so I ran an independent one-off computation directly from the ring law and the proposed label partition.
- That computation reported `vertex_count = 534`, `edge_count = 4086`, `edge_type_counts = {'A-C': 2040, 'B-B': 6, 'B-C': 408, 'B-D': 1632}`, `C0_size = 96`, `extra_labels = [295,301,305,313,317,319]`, and `bad_edges = 0`.
- I also separately checked the key arithmetic invariants: every `A0` label is `2,3`-smooth, every `C` label avoids `{2,3,293,307,311}`, the `B` labels are pairwise coprime, and the three barrier primes all lie above half the interval.
- I did not find a candidate counterexample edge, a mislabeled vertex, a hidden edge type, or a computational mismatch between the ring graph and the displayed witness.

## verify_theorem_worthiness

- This is not a paper-ready theorem and not an `EXACT` result. It remains a verified exact feeder pending later generalize and Lean stages.
- It is not merely an isolated instance either. Relative to the preserved `p <= 97` wrapper frontier, the verified `p = 103` witness isolates a real post-`97` arithmetic question: can one always supply the extra `p - 97` complementary-support labels beyond the fixed `C0` window?
- The structural part that scales is the four-class support reduction together with the fixed `A0` reservoir, the high-barrier set `B = {1,293,307,311}`, and the complementary-support rule for `C`.
- The part that does not yet scale automatically is the counted supply argument beyond `C0` and the final injective interval packaging. In this feeder those six extra labels are still hand-picked.
- The best honest publication status is therefore `SLICE_CANDIDATE`, not `PAPER_READY`, because this feeder points to a real theorem-slice question but does not itself prove the slice.
- The smallest next discriminator for the claimed template is `Γ(Z_107 × Z_25)`, which tests whether the same late wrapper can absorb `10` extra complementary-support labels rather than `6`.

## verify_verdict

- `VERIFIED`
- No rediscovery was established in the bounded prior-art pass, the claim matches the intended exact instance, and the explicit witness survived skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- No mathematical repair was needed.
- The only conservative clarification is interpretive: lemma item `8` should be read as a within-class relabeling statement for the already fixed label sets, not as license to repartition the interval arbitrarily across classes.
