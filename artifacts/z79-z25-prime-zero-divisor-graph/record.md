# Solve Record: z79-z25-prime-zero-divisor-graph

## statement_lock

- Active title: `Is the zero-divisor graph Γ(Z_79 × Z_25) prime?`
- Active slug: `z79-z25-prime-zero-divisor-graph`
- Locked target statement: determine whether the zero-divisor graph `Γ(Z_79 × Z_25)` admits a prime labeling, meaning a bijection from its `414` vertices to `{1,2,...,414}` such that adjacent vertices receive coprime labels.
- This solve pass is locked to the exact feeder instance `Z_79 × Z_25`, but it is being used as a campaign discriminator for the live fixed-`A₀` / high-barrier / complementary-support `Γ(Z_p × Z_25)` slice.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_79` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the four standard `F25` support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_79^×}`, size `78`.
  - `D = {(a,5t) : a ∈ Z_79^×, t ∈ {1,2,3,4}}`, size `312`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 79` and `bd = 0 mod 25`.
- Because `Z_79` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions locked for this solve:
  - the graph is simple, so there are no loops;
  - `(0,0)` is excluded from the vertex set;
  - labels may be permuted freely inside `A`, `C`, and `D` once the class label sets are fixed because those classes have uniform neighborhoods;
  - the four vertices in `B` form a `K_4`, so any permutation of a pairwise-coprime `B` label set is also valid.
- Ambiguities or missing definitions:
  - none that block the solve; the support decomposition, graph convention, and family notation are already fixed by the campaign dossier and the Lean bridge theorem names.

## approach_A

- Structural / invariant route through the exact support graph.
- The edge pattern is the same `F25` pattern used throughout the campaign:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- Edge counts at `p = 79` are therefore forced:
  - `A-C = 20 · 78 = 1560`;
  - `B-B = 6`;
  - `B-C = 4 · 78 = 312`;
  - `B-D = 4 · 312 = 1248`.
- Total predicted edge count: `1560 + 6 + 312 + 1248 = 3126`.
- So the full graph again reduces to three classwise coprimality obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- Brief self-check after Approach A:
  - vertex count check: `20 + 4 + 78 + 312 = 414`;
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`, so there is no new graph-theoretic obstruction at `p = 79`;
  - this is the same structural surface already formalized in the family reduction theorems.

## approach_B

- Construction / extremal route using the live complementary-support theorem shape rather than the older prime-only front.
- The campaign already treats `p = 71` as evidence that the strict prime-only `C` pool is too narrow, so the honest late-family move is:
  - freeze the fixed reservoir
    `A₀ = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`;
  - choose a high barrier
    `B = {1,b₁,b₂,b₃}`
    with distinct primes above half the active interval;
  - choose `C` from labels whose prime support avoids `{2,3,b₁,b₂,b₃}`;
  - let `D` be the complement.
- Here `N = 5p + 19 = 414`, so half the interval is `207`.
- A clean barrier choice is
  `B = {1,211,223,227}`.
  These are distinct primes and satisfy
  `414 < 2·211`,
  `414 < 2·223`,
  and
  `414 < 2·227`,
  so the high-barrier zero-spill lemma applies.
- For `C`, use the explicit complementary-support block
  `C_lab = {n ∈ {1,...,245} : gcd(n,6) = 1} \ {1,211,223,227}`.
- Why this has the right size:
  - the numbers in `{1,...,245}` not divisible by `2` or `3` are
    `245 - ⌊245/2⌋ - ⌊245/3⌋ + ⌊245/6⌋ = 245 - 122 - 81 + 40 = 82`;
  - among those `82`, exactly four must be removed:
    `1`, `211`, `223`, and `227`;
  - hence `|C_lab| = 82 - 4 = 78 = p - 1`.
- Why every `c ∈ C_lab` has the required prime support:
  - `gcd(c,6) = 1` rules out prime divisors `2` and `3`;
  - `c ≤ 245`, while `2·211`, `2·223`, and `2·227` all exceed `414`, so no number in the active interval can be a nontrivial multiple of one of the barrier primes;
  - therefore the only labels in `{1,...,414}` divisible by `211`, `223`, or `227` are `211`, `223`, and `227` themselves, and those were removed from `C_lab`.
- So the candidate classwise partition is:
  - `A_lab = A₀`;
  - `B_lab = {1,211,223,227}`;
  - `C_lab = {n ∈ {1,...,245} : gcd(n,6) = 1} \ {1,211,223,227}`;
  - `D_lab = {1,...,414} \ (A_lab ∪ B_lab ∪ C_lab)`.
- Brief self-check after Approach B:
  - `A_lab`, `B_lab`, and `C_lab` are visibly disjoint;
  - the count for `C_lab` lands exactly at `78`, not merely “at least” `78`;
  - this construction explicitly includes many composite-support labels in `C`, so it tests the widened theorem slice rather than the obsolete prime-only front.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,78,312`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. Every element of `A_lab = A₀` has prime support contained in `{2,3}`.
4. Every element of `C_lab` has prime support avoiding `{2,3,211,223,227}`.
5. Therefore every label in `A_lab` is coprime to every label in `C_lab`.
6. The barrier labels `1,211,223,227` are pairwise coprime, so every `B-B` edge is valid.
7. Because `211`, `223`, and `227` lie above half the interval `{1,...,414}`, every interval label outside `B_lab` is automatically coprime to every label in `B_lab`.
8. Hence every `B-C` and every `B-D` edge is valid.
9. Therefore any classwise bijection from `A,B,C,D` onto `A_lab,B_lab,C_lab,D_lab` is a prime labeling of `Γ(Z_79 × Z_25)`.

## chosen_plan

- Use the already exact support reduction as the graph-theoretic core.
- Do not try to resurrect the old small-spill or prime-only `C` stories; this feeder is specifically about the widened complementary-support slice.
- Freeze the clean late-family choice
  `A_lab = A₀`,
  `B_lab = {1,211,223,227}`,
  and
  `C_lab = {n ≤ 245 : gcd(n,6)=1} \ {1,211,223,227}`.
- Only after this reasoning package is fixed, decide whether a tiny checker is worth using to verify the explicit witness against the ring graph.
- Brief self-check after choosing the plan:
  - the solve remains reasoning-first because the candidate witness is dictated by a theorem-shaped support-avoidance argument and an exact counting identity, not by search;
  - if code is used at all, it should be only a post-construction witness checker.

## self_checks

- Statement lock:
  - the active target is the exact feeder `Γ(Z_79 × Z_25)`;
  - the label interval length `414` matches the vertex count.
- Structural reduction:
  - no new support class or edge family appears at `p = 79`;
  - the full graph again collapses to the three classwise coprimality obligations.
- Construction:
  - the high barrier is genuinely above half the interval;
  - the `C_lab` count is exact: `82 - 4 = 78`;
  - every `C_lab` label avoids prime support `2`, `3`, `211`, `223`, and `227`.
- Pre-code decision:
  - the argument is already explicit enough to be a serious exact-instance candidate;
  - one tiny checker is still justified because this is a fresh feeder and the classwise witness is easy to verify directly.

## code_used

- No code was used to find the construction.
- After the reasoning package was fixed, a minimal checker `check_witness.py` was used only for post-construction witness verification.
- The checker enumerates the `414` nonzero zero-divisors of `Z_79 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,414}`, and tests `gcd = 1` on every edge.
- Checker result:
  - `vertex_count = 414`
  - `edge_count = 3126`
  - `edge_type_counts = {A-C: 1560, B-B: 6, B-C: 312, B-D: 1248}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - assign `A` the fixed reservoir
    `A_lab = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`;
  - assign `B` the high barrier
    `B_lab = {1,211,223,227}`;
  - assign `C` the complementary-support block
    `C_lab = {n ∈ {1,...,245} : gcd(n,6) = 1} \ {1,211,223,227}`;
  - assign `D` the remaining labels
    `D_lab = {1,...,414} \ (A_lab ∪ B_lab ∪ C_lab)`.
- Why this should work:
  - `A-C`:
    every `a ∈ A_lab` has prime support in `{2,3}`, while every `c ∈ C_lab` avoids `2` and `3`;
  - `B-B`:
    `1,211,223,227` are pairwise coprime;
  - `B-C` and `B-D`:
    the barrier primes lie above half the interval, so any other active label is automatically coprime to them;
  - there are no other edges by the support decomposition.
- The explicit witness also survives the local checker with the expected edge counts
  `1560`, `6`, `312`, and `1248` on `A-C`, `B-B`, `B-C`, and `B-D`.
- Strong-result extraction:
  - what part of the argument scales:
    the fixed support decomposition, the fixed `A₀` reservoir, the high-barrier zero-spill move, and the support-avoidance criterion for `C`;
  - what part does not yet scale automatically:
    an all-`p` supply theorem still has to guarantee enough complementary-support labels for `C`;
  - what theorem slice is suggested:
    the exact live slice already named by the campaign, namely a fixed-`A₀` / high-barrier / complementary-support label-set theorem for `Γ(Z_p × Z_25)`;
  - what one or two next feeder instances would help most:
    if `z79` survives, the next useful pressure is probably no longer another random feeder but theorem packaging; if one more discriminator is still needed, it should be chosen to test the first place where the simple `n ≤ 245`, `gcd(n,6)=1` reservoir is no longer the natural complementary-support source;
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still instance-level evidence, but it is much closer to the paper-shaped claim than the earlier small-spill records because the witness is built directly from the live referee-facing theorem form rather than from ad hoc repair arithmetic.

## family_affinity

- Family affinity is very high.
- This feeder is not a one-off exact test; it is a direct discriminator for the current publication lead on the `Γ(Z_p × Z_25)` line.
- In particular, it tests whether the widened complementary-support `C` clause remains clean at `p = 79` after the prime-only front already failed arithmetically at `p = 71`.

## generalization_signal

- Generalization signal is strong.
- The key gain over the earlier feeders is conceptual:
  the solve package no longer needs a fragile “pick some special spill primes” story.
- Instead, it uses a theorem-shaped reservoir:
  a fixed `A₀`, a high barrier above half the interval, and a whole block `C_lab` defined by support avoidance rather than primality.
- The main generalization question left open is not correctness of the support logic, but supply:
  how large a complementary-support pool can be guaranteed inside `{1,...,5p+19}` on a publication range?

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. use the ring-to-support reduction to reduce to the interfaces `A-C`, `B-B`, `B-C`, `B-D`;
  3. freeze `A_lab = A₀`;
  4. choose `B_lab = {1,b₁,b₂,b₃}` with the barrier primes above half the interval;
  5. choose `C_lab` from labels whose prime support avoids `{2,3,b₁,b₂,b₃}`;
  6. let `D_lab` be the complement;
  7. discharge `A-C` from support avoidance, `B-B` from pairwise coprimality, and `B-C`,`B-D` from the high-barrier zero-spill lemma.
- Relative to the earlier feeders, the reusable gain is that the witness is now phrased in the same language as the intended theorem, not in a specialized finite list of primes and spill doubles.

## candidate_theorem_slice

- Candidate slice:
  let `N = 5p + 19` and let
  `A₀ = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
  If
  - `p ≥ 19` is an odd prime,
  - `B_lab = {1,b₁,b₂,b₃}` with distinct prime `bᵢ` satisfying `N < 2bᵢ`,
  - `C_lab` has size `p - 1` and every prime divisor of every `c ∈ C_lab` avoids `{2,3,b₁,b₂,b₃}`,
  - `D_lab` is the interval complement,
  then any classwise bijection onto those label sets gives a prime labeling of `Γ(Z_p × Z_25)`.
- The `z79` construction is a direct instance of that slice with
  `b₁,b₂,b₃ = 211,223,227`.

## smallest_param_shift_to_test

- The smallest next parameter shift should not be chosen mechanically.
- If `z79` verifies, the more valuable next step is to package the complementary-support theorem before spending more feeder budget.
- If one more feeder is still required, it should be the smallest odd prime where the simple cutoff construction
  `C_lab = {n ≤ T : gcd(n,6)=1} \ barrier`
  stops giving a clean size-`p - 1` block without extra bookkeeping.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still one solve-stage instance with no rediscovery audit in this pass and no exact-instance Lean closure.
- It is unusually publication-relevant because the witness is built directly from the live family theorem shape, not from an isolated ad hoc pattern.
- So the likely publishable unit is not “`Γ(Z_79 × Z_25)` is prime” by itself, but rather the complementary-support wrapper theorem that this feeder is testing.

## likely_failure_points

- A structural failure would have to come from a missed edge type in the support decomposition, but that would contradict the already exact family reduction theorems.
- The main arithmetic failure risk is a counting mistake in `|C_lab|`.
- Another arithmetic risk would be accidentally leaving a barrier prime inside `C_lab` or missing some hidden barrier-prime divisor in `C_lab`, though the high-barrier size inequalities make that unlikely.
- The publication risk is overreading this instance as an all-`p` supply theorem; the construction proves one feeder, not the full existence range.

## what_verify_should_check

- Recompute the `414` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the support pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `3126` edges.
- Check that `A_lab`, `B_lab`, `C_lab`, and `D_lab` are disjoint and cover exactly `{1,...,414}`.
- Check that `|C_lab| = 78`.
- Check that every `c ∈ C_lab` has prime support avoiding `{2,3,211,223,227}`.
- Check coprimality on every actual edge of the ring graph.
- During verify, audit this instance against the live complementary-support theorem slice, not against the obsolete prime-only front.

## verify_rediscovery

- PASS 1 used a bounded web audit on the exact instance notation, ASCII alternate notation, the family notation `Γ(Z_p × Z_25)`, the canonical source, and one later status check.
- The main source found was Fox-Mooney, `On prime labelings of zero-divisor graphs` (`Congressus Numerantium` 236, online November 21, 2025). On the available budget, that source still treats the broader distinct-prime family `Γ(Z_p × Z_(q^2))` as conjectural rather than settled, so it does not establish rediscovery of the exact `p = 79`, `q = 5` instance.
- I did not find a theorem, proposition, example, observation, or corollary in the canonical source explicitly exhibiting `Γ(Z_79 × Z_25)` or otherwise directly implying this exact instance.
- I also did not find a later citation or discussion within the audit budget that already settles this exact feeder.
- Rediscovery is therefore not established on the available budget.

## verify_faithfulness

- The solver's mathematical claim is the exact canonical statement: `Γ(Z_79 × Z_25)` admits a prime labeling on all `414` nonzero zero-divisors.
- The `selected_problem.md` intended statement is campaign-facing feeder language, but the solved claim is the right mathematical content for that feeder and does not drift to a weaker proxy.
- I found no wrong-theorem drift, quantifier drift, definition change, or switch to a different graph model.
- The record stays at instance level while explicitly identifying the family slice it tests, which is the honest framing.

## verify_proof

- I re-derived the nonzero zero-divisors from the ring law: `(a,b)` is a vertex exactly when `(a,b) ≠ (0,0)` and either `a = 0` or `5 | b`. This gives class sizes `20,4,78,312`, hence `414` vertices total.
- I rechecked adjacency from coordinatewise zero product. Since `Z_79` is a field and the only nonzero zero-divisors in `Z_25` are the multiples of `5`, the only edge families are exactly `A-C`, `B-B`, `B-C`, and `B-D`.
- The arithmetic witness then reduces to the stated classwise coprimality obligations. Those obligations are satisfied:
  - `A_lab = A₀` uses only primes `2` and `3`;
  - every `c ∈ C_lab` avoids prime divisors `2`, `3`, `211`, `223`, and `227`;
  - `B_lab = {1,211,223,227}` is pairwise coprime;
  - the only multiples of `211`, `223`, and `227` in `{1,...,414}` are the primes themselves, so every label outside `B_lab` is coprime to the nontrivial barrier labels.
- I found no incorrect step. The main risk was an arithmetic or partitioning slip, not a conceptual gap, and the checks below remove that risk.

## verify_adversarial

- I reran `python3 artifacts/z79-z25-prime-zero-divisor-graph/check_witness.py`.
- The checker again reported:
  - `vertex_count = 414`
  - `edge_count = 3126`
  - `edge_type_counts = {'A-C': 1560, 'B-B': 6, 'B-C': 312, 'B-D': 1248}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`
- I also independently rechecked the arithmetic partition:
  - `|A_lab| = 20`, `|B_lab| = 4`, `|C_lab| = 78`, `|D_lab| = 312`;
  - the four label blocks are disjoint and cover exactly `{1,...,414}`;
  - every `c ∈ C_lab` avoids divisibility by `2`, `3`, `211`, `223`, and `227`;
  - the only interval multiples of `211`, `223`, and `227` are `211`, `223`, and `227` themselves.
- I did not find a way to break the witness or reinterpret the code as checking a weaker surrogate claim.

## verify_theorem_worthiness

- This is not just an isolated pretty labeling. The argument uses the live fixed-`A₀` / high-barrier / complementary-support template rather than a hand-tuned one-off assignment, so it is genuine feeder evidence for the family campaign.
- What scales structurally:
  - the four support classes and the exact interface graph;
  - the fixed `A₀` reservoir;
  - the high-barrier zero-spill move for `B`;
  - the principle that `C` should be chosen from labels whose prime support avoids the `A ∪ B` prime support.
- What does not yet scale automatically:
  - a family-level supply theorem giving `p - 1` admissible `C` labels for a publication range;
  - a referee-ready rule for choosing the cutoff or reservoir once the simple `n ≤ 245` block saturates.
- The best honest publication status is still `SLICE_CANDIDATE`, not `INSTANCE_ONLY`, because this feeder directly validates the current theorem slice language and identifies the next real bottleneck.
- The smallest parameter shift that most tests the claimed template is `p = 83`: the present cutoff block contributes exactly `78` admissible `C` labels, so the `p = 79` witness is saturated and the next odd prime already forces a new complementary-support supply move.

## verify_verdict

- `VERIFIED`
- The bounded prior-art audit did not establish rediscovery, the solved claim matches the intended mathematical statement, I found no incorrect step, and the explicit witness survives direct recomputation.
- This must remain `CANDIDATE`, not `EXACT`, because Lean has not been completed.
- `lean_ready = true` is now justified for the instance-level artifact, but workflow should still send the campaign through `generalize` before spending effort on isolated exact-instance Lean.

## minimal_repair_if_any

- None. No proof patch or witness repair was needed.
