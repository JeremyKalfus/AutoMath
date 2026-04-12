# Solve Record: z71-z25-prime-zero-divisor-graph

## statement_lock

- Active title from `selected_problem.md`: `Is the zero-divisor graph Gamma(Z_71 x Z_25) prime?`
- Active slug: `z71-z25-prime-zero-divisor-graph`.
- Normalized graph statement: determine whether the zero-divisor graph `Γ(Z_71 × Z_25)` admits a prime labeling, meaning a bijection from its `374` vertices to `{1,2,...,374}` such that adjacent vertices receive coprime labels.
- This pass is locked to the exact feeder instance `Z_71 × Z_25`, not the full family `Γ(Z_p × Z_25)`.

## definitions

- Write vertices as pairs `(a,b)` with `a ∈ Z_71` and `b ∈ Z_25`.
- A nonzero zero-divisor is exactly a nonzero pair with either `a = 0` or `5 | b`.
- The nonzero zero-divisors split into the usual four support classes:
  - `A = {(0,u) : u ∈ Z_25^× and 5 ∤ u}`, size `20`.
  - `B = {(0,5),(0,10),(0,15),(0,20)}`, size `4`.
  - `C = {(a,0) : a ∈ Z_71^×}`, size `70`.
  - `D = {(a,5t) : a ∈ Z_71^×, t ∈ {1,2,3,4}}`, size `280`.
- Adjacency is by zero product:
  `(a,b) ~ (c,d)` iff `ac = 0 mod 71` and `bd = 0 mod 25`.
- Because `Z_71` is a field, the first-coordinate product vanishes iff at least one first coordinate is `0`.
- In `Z_25`, the product of two nonzero elements is `0` iff both are multiples of `5`.
- Conventions and ambiguities locked before solving:
  - `Γ` means the simple graph on the nonzero zero-divisors, so `(0,0)` is excluded and loops are not allowed.
  - Vertices inside `A`, `C`, and `D` have identical neighborhoods, so labels may be permuted inside those classes once the class label sets are fixed.
  - The four vertices of `B` induce `K_4`, so any permutation of a pairwise-coprime `B` label set also preserves the witness.
  - No further ambiguity blocks the solve; the family dossier already fixes the support notation and graph convention.

## approach_A

- Structural / invariant route through the support graph and the current `A₀` publication template.
- The exact support graph is unchanged from every earlier `Γ(Z_p × Z_25)` feeder:
  - `A-C` is complete bipartite;
  - `B-B` induces `K_4`;
  - `B-C` is complete bipartite;
  - `B-D` is complete bipartite;
  - no other edge types occur.
- The forced edge counts at `p = 71` are therefore:
  - `A-C = 20 · 70 = 1400`;
  - `B-B = 6`;
  - `B-C = 4 · 70 = 280`;
  - `B-D = 4 · 280 = 1120`.
- Total predicted edge count: `1400 + 6 + 280 + 1120 = 2806`.
- This reduces the exact graph problem to three arithmetic obligations:
  - every label on `A ∪ B` is coprime to every label on `C`;
  - the four labels on `B` are pairwise coprime;
  - every label on `D` is coprime to every label on `B`.
- The live family theorem slice suggests freezing
  `A = A₀ = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
  Every label in `A₀` has prime support contained in `{2,3}`.
- Use the high-barrier zero-spill set
  `B = {1,191,193,197}`.
  Here `N = 5p + 19 = 374`, so `N/2 = 187`, and each nontrivial barrier prime lies above half the interval.
  Hence every interval label different from `191,193,197` is automatically coprime to each barrier prime, so `B-D` becomes automatic once `D` avoids the four barrier labels themselves.

## approach_B

- Construction / extremal route by testing the exact prime-only `C` pool and then repairing the first shortfall minimally.
- Under the frozen `A₀` plus high-barrier choice above, a prime-only `C` block may use only primes outside `{2,3,191,193,197}`.
- A direct count gives `π(374) = 74`, so the usable prime-only pool has size
  `74 - 5 = 69`.
- But `|C| = 70`, so the prime-only complementary-prime-pool template is short by exactly one label at `p = 71`.
- This matches the family dossier: `p = 71` is the first predicted arithmetic obstruction to the strict prime-only zero-spill front end, not to the graph itself.
- The obstruction is local and suggestive: nothing in the support reduction requires `C` to be prime-only. It only requires every label on `C` to be coprime to every label on `A ∪ B`.
- Because every label in `A ∪ B` has prime support contained in `{2,3,191,193,197}`, any complementary-support label whose prime factors avoid that palette may be added to `C`.
- The smallest convenient repair is `25 = 5^2`.
  It is not in `A₀`, it is not a barrier label, and it is coprime to every label in `A₀ ∪ B`.
- So a natural exact-instance candidate is:
  - `A = A₀`;
  - `B = {1,191,193,197}`;
  - `C =` the `69` primes in `{1,...,374}` outside `{2,3,191,193,197}`, together with `25`;
  - `D` = the remaining `280` labels.

## lemma_graph

1. The vertex set is exactly `A ⊔ B ⊔ C ⊔ D` with sizes `20,4,70,280`.
2. The exact edge pattern is `A-C`, `B-B`, `B-C`, and `B-D`.
3. If every label on `A ∪ B` is coprime to every label on `C`, then all `A-C` and `B-C` edges are valid.
4. If the four labels on `B` are pairwise coprime, then all `B-B` edges are valid.
5. If every label on `D` is coprime to every label on `B`, then all `B-D` edges are valid.
6. For `B = {1,191,193,197}`, the nontrivial barrier labels are above half the interval `{1,...,374}`, so every other active label is automatically coprime to them; thus `B-D` is discharged by the high-barrier zero-spill package.
7. Every label in `A₀` has prime support only in `{2,3}`.
8. Therefore any label placed in `C` whose prime support avoids `{2,3,191,193,197}` is automatically coprime to every label in `A ∪ B`.
9. Hence the exact instance closes if we can choose `70` labels for `C` from the complementary-support pool against `{2,3,191,193,197}`.

## chosen_plan

- Use Approach A to lock the exact ring graph and reduce the instance to the three standard arithmetic interfaces.
- Use Approach B to isolate the honest point of failure of the strict prime-only `C` pool.
- Repair only that one failure by adding the single complementary-support label `25` to `C`.
- Keep `A = A₀` and `B = {1,191,193,197}` frozen, because that is the publication-facing structure the current family dossier is trying to stabilize.
- Only after the explicit class partition is fixed, use one tiny checker to validate the witness against the full ring graph.

## self_checks

- After statement lock:
  - the target is still the exact feeder instance `Γ(Z_71 × Z_25)`;
  - the vertex count is `20 + 4 + 70 + 280 = 374`.
- After Approach A:
  - the support graph is still exactly `A-C`, `B-B`, `B-C`, `B-D`;
  - the barrier primes `191,193,197` all satisfy `374 < 2b`, so the zero-spill `B-D` package is applicable.
- After Approach B:
  - the prime-only pool count is genuinely short by one: `69 < 70`;
  - `25` is a legal repair because its only prime factor is `5`, which lies outside `{2,3,191,193,197}`.
- After fixing the candidate witness:
  - `A`, `B`, and `C` are pairwise disjoint and have sizes `20,4,70`;
  - the residual complement has size `280`, exactly `|D|`;
  - the solve package remains reasoning-first because the checker is used only after the full class partition is fixed.

## code_used

- Minimal code was used only after the reasoning and explicit class partition were fixed.
- A tiny local checker `check_witness.py` enumerates the `374` nonzero zero-divisors of `Z_71 × Z_25`, generates edges directly from the ring multiplication rule, checks bijectivity onto `{1,...,374}`, and tests `gcd = 1` on every edge.
- Result after running the checker:
  - `vertex_count = 374`
  - `edge_count = 2806`
  - `edge_type_counts = {A-C: 1400, B-B: 6, B-C: 280, B-D: 1120}`
  - `label_bijection_ok = 1`
  - `edge_coprime_ok = 1`

## result

- Current best solve-stage candidate:
  - put the labels `2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108` on `A` in any order;
  - put the labels `1,191,193,197` on `B` in any order;
  - put the labels `5,7,11,13,17,19,23,25,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373` on `C` in any order;
  - put the remaining `280` labels
    `10,14,15,20,21,22,26,28,30,33,34,35,38,39,40,42,44,45,46,49,50,51,52,55,56,57,58,60,62,63,65,66,68,69,70,74,75,76,77,78,80,82,84,85,86,87,88,90,91,92,93,94,95,98,99,100,102,104,105,106,110,111,112,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,132,133,134,135,136,138,140,141,142,143,144,145,146,147,148,150,152,153,154,155,156,158,159,160,161,162,164,165,166,168,169,170,171,172,174,175,176,177,178,180,182,183,184,185,186,187,188,189,190,192,194,195,196,198,200,201,202,203,204,205,206,207,208,209,210,212,213,214,215,216,217,218,219,220,221,222,224,225,226,228,230,231,232,234,235,236,237,238,240,242,243,244,245,246,247,248,249,250,252,253,254,255,256,258,259,260,261,262,264,265,266,267,268,270,272,273,274,275,276,278,279,280,282,284,285,286,287,288,289,290,291,292,294,295,296,297,298,299,300,301,302,303,304,305,306,308,309,310,312,314,315,316,318,319,320,321,322,323,324,325,326,327,328,329,330,332,333,334,335,336,338,339,340,341,342,343,344,345,346,348,350,351,352,354,355,356,357,358,360,361,362,363,364,365,366,368,369,370,371,372,374`
    on `D` in any order.
- Why this works:
  - `B-B` edges: `1,191,193,197` are pairwise coprime.
  - `B-D` edges: the only labels in `{1,...,374}` divisible by `191`, `193`, or `197` are the barrier labels themselves, because each lies above half the interval. So every `D` label is automatically coprime to every nontrivial label in `B`.
  - `A-C` and `B-C` edges: every label in `A ∪ B` has prime support contained in `{2,3,191,193,197}`, while every label in `C` has prime support outside that palette. Hence every `C` label is coprime to every label in `A ∪ B`.
  - there are no other edges by the support decomposition.
- Therefore the intended statement appears true for this exact feeder instance, with an explicit prime-labeling witness.
- Strong-result extraction:
  - what part of the argument scales:
    the four-class support decomposition, the fixed `A₀` reservoir, the zero-spill high-barrier package for `B`, and the complementary-support viewpoint for `C`.
  - what part does not yet scale automatically:
    the exact count and admissible form of the non-prime supplements to `C`; here one label `25` suffices, but the family theorem still needs a quantified existence statement rather than one hand-picked repair.
  - what theorem slice is suggested:
    a one-supplement high-barrier / complementary-support slice for `Γ(Z_p × Z_25)`: if the prime-only complementary pool is short by at most one and there exists one additional label whose prime support avoids `{2,3,b₁,b₂,b₃}`, then the same frozen `A₀` and high-barrier `B` package still yields a prime labeling.
  - what one or two next feeder instances would help most:
    `Γ(Z_73 × Z_25)` as the immediate next test of the one-supplement regime, and `Γ(Z_79 × Z_25)` as the first likely test where more than one complementary-support supplement may be needed.
  - whether the current package is still just an instance or already closer to a paper-shaped claim:
    it is still instance-level evidence, but it is materially closer to a paper-shaped claim because it cleanly separates
    “prime-only complementary pool fails”
    from
    “the exact graph still labels after a single complementary-support repair.”

## family_affinity

- Family affinity is high.
- This feeder sits exactly at the family-predicted first obstruction to the strict prime-only `A₀` / zero-spill / complementary-prime-pool route.
- The main campaign value is not merely another exact witness; it is that `p = 71` appears to force the theorem language to widen from prime-only `C` to complementary-support `C`.

## generalization_signal

- Generalization signal is strong.
- The structural package `A = A₀` and high barriers above half the interval still survives intact at `p = 71`.
- What fails is only the narrow supply hypothesis “`C` may be chosen prime-only.”
- The exact-instance lesson is sharper than a raw witness:
  one complementary-support label can rescue the feeder without changing the support proof, the `A₀` reservoir, or the zero-spill barrier lemma.

## proof_template_reuse

- Reusable proof template:
  1. decompose `Γ(Z_p × Z_25)` into support classes `A,B,C,D`;
  2. prove the exact edge pattern `A-C`, `B-B`, `B-C`, `B-D`;
  3. freeze `A` as the fixed `A₀` reservoir with prime support only in `{2,3}`;
  4. choose `B = {1,b₁,b₂,b₃}` with each barrier prime above half the active interval, so `B-D` is automatic;
  5. choose `C` from labels whose prime support avoids `{2,3,b₁,b₂,b₃}`;
  6. let `D` be the remaining complement.
- Relative to the `z67` boundary story, the reusable gain is explicit:
  the first post-boundary repair can keep the same front end and change only the `C`-supply clause.

## candidate_theorem_slice

- Candidate slice:
  let `N = 5p + 19` and
  `A₀ = {2,3,4,6,8,9,12,16,18,24,27,32,36,48,54,64,72,81,96,108}`.
  If there exist primes `b₁,b₂,b₃` with `N < 2bᵢ` for each `i`, and if the interval `{1,...,N}` contains at least `p - 2` primes outside `{2,3,b₁,b₂,b₃}` together with at least one additional label whose prime support also avoids `{2,3,b₁,b₂,b₃}`, then assigning
  - `A = A₀`,
  - `B = {1,b₁,b₂,b₃}`,
  - `C` from that complementary-support pool,
  - `D` as the remaining complement
  gives a prime labeling of `Γ(Z_p × Z_25)`.
- The `p = 71` feeder is the first clean evidence for this one-supplement version of the slice.

## smallest_param_shift_to_test

- The smallest next parameter shift to test on this line is `p = 73`.
- Reason:
  it is the next odd prime after `71`, and the local prime-only complementary-pool count is still short there, so it is the immediate discriminator for whether the one-supplement repair is stable rather than isolated.

## why_this_is_or_is_not_publishable

- This is not publishable on its own yet because it is still a solve-stage exact feeder, with no rediscovery audit in this pass and no Lean closure for the exact instance.
- It is publication-relevant because it appears to be the first exact feeder that separates two honest theorem candidates:
  - the stricter prime-only complementary-prime-pool slice;
  - the wider one-supplement complementary-support slice.
- That is a real campaign discriminator and much closer to a referee-facing family statement than a random isolated witness would be.

## likely_failure_points

- The structural failure point would be a missed edge family in the support decomposition, though that would contradict the now-stable ring bridge.
- The arithmetic failure point would be a mistaken prime count `π(374)` or a mistaken claim that the prime-only pool has size `69`.
- Another arithmetic failure point would be an overlooked common factor between the supplement `25` and some label in `A ∪ B`; the chosen `A₀` and high barriers were selected precisely to avoid that.
- Publication-wise, the main weakness is that the one-supplement repair is still an observed exact pattern, not yet a quantified family lemma.

## what_verify_should_check

- Recompute the `374` vertices directly from the ring definition.
- Recompute the exact edge set and confirm the class pattern `A-C`, `B-B`, `B-C`, `B-D`, with total `2806` edges.
- Check that `A`, `B`, and `C` are disjoint and cover `94` labels, leaving exactly `280` for `D`.
- Check that `191`, `193`, and `197` are indeed above half the interval `{1,...,374}`, so `B-D` is zero-spill.
- Check that every label in `C` has prime support outside `{2,3,191,193,197}`, especially the non-prime supplement `25`.
- Check coprimality on every actual edge from the ring graph.
- In verify, audit whether the one-supplement `p = 71` package is already implied by any existing family theorem or proposition rather than being treated as new frontier evidence.

## verify_rediscovery

- PASS 1 used a bounded web audit on the exact tuple `Γ(Z_71 × Z_25)`, ASCII / reordered notation such as `Z_71 x Z_25`, the broader family notation `Γ(Z_p × Z_(q^2))`, the canonical Fox-Mooney source itself, and one recent status follow-up.
- Exact-instance and alternate-notation searches did not reveal an earlier theorem, proposition, example, observation, or corollary settling `Γ(Z_71 × Z_25)` within budget.
- In the canonical source `On prime labelings of zero-divisor graphs` (published online `2025-11-21`), the same-source theorem / proposition / example / observation / corollary check still leaves the ambient family open as Conjecture `4.4` for `Γ(Z_p × Z_(q^2))`. The nearby settled cases there are not the present `q = 5` line.
- The bounded recent-status check did not expose any later paper or announcement closing either the exact `p = 71, q = 5` case or the broader `Γ(Z_p × Z_25)` family.
- Verdict for PASS 1: no rediscovery established within budget.

## verify_faithfulness

- The saved solve claim matches the exact mathematical statement: existence of a prime labeling for the full simple zero-divisor graph on the `374` nonzero zero-divisors of `Z_71 × Z_25`, with labels bijectively covering `{1,...,374}`.
- There is no drift to a support graph, quotient graph, or weaker proxy statement. The class decomposition is used only as a reduction for the full graph.
- The meta sentence in `selected_problem.md` describing this as a campaign feeder does not create theorem drift, because the solve record stays locked to the canonical graph-theoretic claim.
- The statement that labels may be assigned in any order inside each support class is faithful: all vertices in each of `A`, `B`, `C`, and `D` have identical neighborhoods under the ring-based adjacency rule.

## verify_proof

- I independently recomputed the vertex partition from the ring definition and recovered the claimed class sizes `|A| = 20`, `|B| = 4`, `|C| = 70`, `|D| = 280`.
- I independently recomputed the exact edge families and again found only `A-C`, `B-B`, `B-C`, and `B-D`, with counts `1400`, `6`, `280`, and `1120`, for total `2806` edges.
- I separately recomputed the arithmetic front:
  - `π(374) = 74`;
  - removing `{2,3,191,193,197}` leaves exactly `69` usable primes for a prime-only `C` block;
  - the displayed `C` set is exactly that `69`-prime pool together with the one supplement `25`;
  - every label in `C` is coprime to every label in `A ∪ B`;
  - the four labels in `B = {1,191,193,197}` are pairwise coprime.
- The zero-spill step is justified: since `191`, `193`, and `197` are all greater than `374/2 = 187`, no other label in `{1,...,374}` is divisible by any of them, so every `D` label is automatically coprime to the nontrivial barrier labels.
- First incorrect step found: none.

## verify_adversarial

- I reran `artifacts/z71-z25-prime-zero-divisor-graph/check_witness.py`. It again reported `vertex_count = 374`, `edge_count = 2806`, `edge_type_counts = {'A-C': 1400, 'B-B': 6, 'B-C': 280, 'B-D': 1120}`, `label_bijection_ok = 1`, and `edge_coprime_ok = 1`.
- I also ran an independent scratch computation outside the saved checker to confirm the class sizes, the exact edge-type counts, the prime count `π(374) = 74`, the `69`-prime shortfall computation, and the disjointness / coprimality of the displayed `A`, `B`, and `C` label sets.
- I specifically tried to break the witness at the vulnerable points named in the solve record:
  - a missed edge family in the support graph;
  - a mistaken prime count at `374`;
  - a hidden common factor between the supplement `25` and some label in `A ∪ B`;
  - a hidden multiple of `191`, `193`, or `197` inside `D`.
- I did not find a bad edge, mislabeled vertex, or arithmetic obstruction.

## verify_theorem_worthiness

- This feeder is stronger than a generic exact instance because it marks the first clean point where the strict prime-only complementary pool fails while the exact graph still labels after one complementary-support repair.
- What scales structurally:
  - the four-class support decomposition;
  - the fixed `A₀` reservoir;
  - the high-barrier zero-spill package on `B`;
  - the complementary-support interpretation of the `C` block.
- What does not yet scale automatically:
  - the existence and count of suitable non-prime supplements for `C`;
  - the proof still uses the hand-picked supplement `25` rather than a quantified family lemma.
- The best honest publication status is therefore `SLICE_CANDIDATE`, not merely `INSTANCE_ONLY`, because this exact feeder cleanly distinguishes two live theorem candidates on the `q = 5` line:
  - the stricter prime-only complementary-pool slice;
  - the wider one-supplement complementary-support slice.
- It is still not stronger than `SLICE_CANDIDATE`, because the family-level existence statement for the supplement is not proved and nothing here is Lean-complete.
- The smallest parameter shift that most tests the claimed template is `p = 73`, the next odd prime after `71`.

## verify_verdict

- `VERIFIED`
- No rediscovery was established within the bounded prior-art pass, the claim is faithful to the exact intended graph statement, and the explicit witness survived independent skeptical recomputation.
- The classification must remain `CANDIDATE`, not `EXACT`, because Lean has not completed.

## minimal_repair_if_any

- None. No conservative repair was needed.
