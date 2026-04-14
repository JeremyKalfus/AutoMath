# Solve Record: Determine the exact value of R(C4, C4, K4)

## statement_lock
We work with a 3-edge-coloring of `K20` in colors `R`, `B`, `G`.
The intended statement is exact and binary:
- either every such coloring contains a red `C4`, a blue `C4`, or a green `K4`, proving `R(C4, C4, K4) = 20`;
- or there exists one coloring of `K20` with no red `C4`, no blue `C4`, and no green `K4`, proving `R(C4, C4, K4) = 21`.

The honest title theorem, if solved, would be:
`The Exact Value of R(C4, C4, K4)`.

If this closes, it is already about `81%` of a short paper. Minimal remaining packaging would be:
- a clean extremal proof or explicit critical coloring,
- a short comparison with the neighboring `K4-e` case,
- one compact remark on how the argument interfaces with the existing `C4` upper-bound machinery.

## definitions
- `R`, `B`, `G` denote the red, blue, and green spanning subgraphs on the same 20-vertex set.
- `C4` means a simple 4-cycle.
- `K4` means a 4-clique.
- For a graph `H`, `N_H(v)` is the neighborhood of `v` in `H`, `d_H(v) = |N_H(v)|`, and `e(H)` is its edge count.
- In a `C4`-free graph, every pair of vertices has at most one common neighbor.
- Equivalent counting form: for a `C4`-free graph `H` on 20 vertices,
  `sum_v binom(d_H(v), 2) <= binom(20, 2) = 190`.
- Local neighborhood fact: if `H` is `C4`-free and `x in V(H)`, then `H[N_H(x)]` has maximum degree at most 1.
  Reason: a path of length 2 inside `N_H(x)` together with `x` creates a 4-cycle.

Ambiguities and conventions:
- I treat colors as labeled; swapping red and blue is allowed only as a symmetry in reasoning.
- I use only exact local deductions available from the packet and elementary extremal arguments; I am not importing outside tables during solve.
- The already-known upper bound `<= 21` is input, not reproved here.

## approach_A
Structural / invariant route toward proving `R(C4, C4, K4) = 20`.

Step A1. For each of `R` and `B`,
`sum_v binom(d(v), 2) <= 190`.
By Jensen,
`20 * binom(avg_d, 2) <= 190`,
so `avg_d(avg_d - 1) <= 19` and hence
`avg_d <= (1 + sqrt(77)) / 2 < 4.89`.
Therefore
`e(R) <= 48` and `e(B) <= 48`.

Step A2. Since `e(K20) = 190`, we get
`e(G) >= 190 - 48 - 48 = 94`.
Hence the average green degree is at least `9.4`, so some vertex `v` satisfies
`d_G(v) >= 10`.

Step A3. On the green neighborhood `N_G(v)`, the induced 3-coloring has:
- no red `C4`,
- no blue `C4`,
- no green `K3` (because a green triangle inside `N_G(v)` together with `v` would form a green `K4`).

So any counterexample on 20 vertices forces a 10-vertex local coloring with forbidden triple `(C4, C4, K3)`.

This gives a clean conditional reduction:
if `R(C4, C4, K3) <= 10`, then `R(C4, C4, K4) = 20`.

Why this route is attractive:
- it converts the 20-vertex target into one smaller exact local obstruction;
- it matches the paper shape of an upper-bound note, because the final proof could be "global density forces a 10-vertex green neighborhood; local `(C4, C4, K3)` obstruction finishes."

Why it stalls at present:
- the current argument does not itself prove the needed 10-vertex local obstruction;
- the edge count `48 + 48 + 94 = 190` is consistent, so counting alone does not close the case.

Self-check after Approach A:
- the reduction is rigorous;
- the bottleneck is explicit;
- no unsupported exact local Ramsey value has been assumed.

## approach_B
Construction / extremal route toward proving `R(C4, C4, K4) = 21`.

Rephrase the target. Let `H = R union B`.
Then a 20-vertex lower-bound construction is equivalent to a graph `H` on 20 vertices such that:
- `alpha(H) <= 3` (equivalently, the green complement has no `K4`),
- the edges of `H` can be partitioned into two `C4`-free graphs `R` and `B`.

A natural dense seed is a partition into four 5-vertex blocks.
Inside each `K5`, there is an obvious dense 2-coloring with no monochromatic `C4`: color one 5-cycle red and its complementary 5-cycle blue.
This gives four dense local packets that are individually safe for the `C4` constraint.

But this seed alone is far from enough:
- if `H` were just the union of four colored `K5` blocks, then `alpha(H) = 4` by taking one vertex from each block;
- equivalently, the green complement would contain many 4-cliques across the four blocks.

Therefore any 21-construction must add carefully engineered inter-block non-green edges that do two jobs at once:
- destroy every independent transversal across the four 5-blocks;
- avoid creating a red or blue `C4` globally.

This is a severe compatibility constraint. A naive complete or near-complete same-color bipartite join between two 5-blocks is impossible because it instantly creates many monochromatic `C4`s. So the inter-block layer must be very sparse and highly structured, plausibly matching-like or incidence-like.

Self-check after Approach B:
- the reformulation through `H = R union B` is exact;
- the four-`K5` seed is a legitimate dense local model;
- the missing ingredient is a transversal-killing sparse interface, not merely more density.

## lemma_graph
Candidate proof skeleton:

L1. In any `C4`-free graph, each pair of vertices has at most one common neighbor.

L2. Therefore for each of `R` and `B`,
`sum_v binom(d(v), 2) <= 190`, so `e(R), e(B) <= 48`.

L3. Hence `e(G) >= 94`, so some vertex has green degree at least `10`.

L4. For such a vertex `v`, the induced coloring on `N_G(v)` avoids `(C4, C4, K3)`.

L5. Therefore:
`R(C4, C4, K3) <= 10  =>  R(C4, C4, K4) = 20`.

L6. On the lower-bound side, any 20-vertex construction must produce a graph `H = R union B` with `alpha(H) <= 3` that still admits a decomposition into two `C4`-free color classes.

L7. A simple dense block decomposition must solve an inter-block independent-transversal problem under monochromatic-`C4` avoidance.

## chosen_plan
Best current path:
- keep the upper-bound route as the primary mathematical spine because it isolates one exact local obstruction `(C4, C4, K3)` on 10 vertices;
- treat the lower-bound route as a stress test for plausibility, not as the main proof;
- run one tiny bounded experiment on the simplest four-`K5` block template with cyclic shift matchings between blocks.

The purpose of the experiment is narrow:
- not to prove or disprove the full theorem;
- only to test whether the most naive 4x5 construction family can even eliminate all 4-block independent transversals before one worries about red/blue `C4`s.

## self_checks
- Statement lock: exact and unchanged from the packet.
- Publication check: a full closure here would still be `70-90%` of a paper, because the title theorem is already exact and canonical.
- Scope check: no broad ledger replay, no unrelated dossiers, no Lean.
- Mathematical honesty check: current solve has a rigorous reduction and a lower-bound obstacle analysis, but not an exact proof or disproof.
- Post-experiment check: the code only tested a sharply restricted lower-bound template; the negative outcome rules out that template, not all 21-constructions.

## code_used
One tiny bounded experiment was used after the reasoning was written:
- model: four 5-vertex blocks, with one cyclic shift matching between each pair of blocks;
- goal: check whether this simplest `4 x 5` template can eliminate every 4-block independent transversal, which is necessary before the green complement can become `K4`-free;
- method: exhaustive search over all `5^6 = 15625` choices of the six inter-block shifts.

Outcome:
- no shift assignment works;
- so this simplest cyclic block family cannot even remove all candidate green `K4`s, before any red/blue `C4` check is imposed.

## result
Current strongest honest result:
- rigorous reduction of the 20-vertex upper-bound problem to a 10-vertex local obstruction `(C4, C4, K3)` arising inside a large green neighborhood;
- explicit diagnosis that any 21-construction must solve a sparse inter-block transversal-cover problem while keeping both non-green colors `C4`-free;
- negative bounded experiment: the most naive cyclic four-`K5` block template with one shift-matching per block pair does not achieve the needed transversal cover.

This is theorem-facing but not a closure.
The exact value remains open inside this solve attempt.

## family_affinity
Strong.
The argument already sits inside the exact `C4/C4/K4` three-color family and interfaces naturally with the neighboring `K4-e` benchmark and with local-neighborhood Ramsey reductions.

## generalization_signal
Moderate.
The green-neighborhood reduction pattern should extend to other triples `(C4, C4, K_t)` where dense complement plus local `K_{t-1}` avoidance can force a smaller mixed Ramsey obstruction.
What does not automatically generalize is the sharp edge accounting needed to make the local neighborhood large enough, and the failed cyclic block template does not by itself say much about less symmetric constructions.

## proof_template_reuse
Reusable template:
- convert two `C4`-free color classes into a global edge lower bound for the remaining color;
- take a maximum-degree vertex in the remaining color;
- reduce to a smaller mixed Ramsey problem on its neighborhood;
- close locally if the smaller mixed number is exact and sharp enough.

## candidate_theorem_slice
Conditional theorem slice:
If every 10-vertex 3-coloring with no red `C4` and no blue `C4` contains a green triangle, then every 20-vertex 3-coloring contains a red `C4`, a blue `C4`, or a green `K4`; hence `R(C4, C4, K4) = 20`.

This is a real theorem slice, but it is still conditional on the unresolved local obstruction.

Construction-side boundary slice:
the simplest cyclic four-`K5` block model with one shift-matching between each pair of blocks cannot serve as a 20-vertex lower-bound template, because it leaves at least one fully green 4-block transversal.

## smallest_param_shift_to_test
Most valuable nearby shifts:
- determine or re-derive the exact local value `R(C4, C4, K3)`;
- test the same neighborhood reduction for `R(C4, C4, K4-e)` to see exactly where the proof becomes cheaper there;
- if the lower-bound side is revisited, move one notch beyond the failed shift-only model to affine or incidence-style inter-block matchings rather than broad unconstrained search.

## why_this_is_or_is_not_publishable
Not yet publishable.
At the moment the package is still too thin for the micro-paper lane because:
- there is no exact solve of the intended statement;
- the conditional theorem slice is honest but not independent enough to be the title result;
- the construction-side analysis exposes obstruction geometry but does not produce a critical coloring.

If the local 10-vertex obstruction closed cleanly, this would immediately become paper-shaped again.
Right now the package is still too thin for the micro-paper lane.

## paper_shape_support
If the main claim closes, the smallest supporting structure I would keep is:
- the density-to-neighborhood reduction `20 -> 10`,
- one clean local lemma explaining why green neighborhoods are triangle-free in a counterexample,
- one short comparison remark with the neighboring `K4-e` case,
- one remark on why the result matters as the smallest remaining one-gap `C4/C4/K4` benchmark.

One immediate natural remark already falling out is:
any eventual 21-construction must be less naive than the cyclic four-`K5` shift-matching template; the lower-bound side is not going to come from the first symmetric block ansatz.

## boundary_remark
Natural boundary remark:
the current solve isolates a plausible threshold phenomenon.
The global problem appears to hinge on whether the local mixed number `(C4, C4, K3)` already blocks a 10-vertex green neighborhood. If yes, the value should be `20`; if not, any 21-construction still has to overcome a hard transversal-cover obstruction.

What scales:
- the density-to-neighborhood reduction mechanism.

What does not currently scale:
- the simplest cyclic block construction model fails before the monochromatic-`C4` constraints are even enforced.

Closest current package assessment:
- closer to a theorem-facing structural note than to a random instance computation,
- but still not close enough to be paper-shaped without the local 10-vertex closure or a genuine 20-vertex construction.

## likely_failure_points
- The bound `e(R), e(B) <= 48` may be too weak to force enough green degree without an exact local result.
- A lower-bound construction might exist outside the simple four-`K5` block intuition.
- Even if the local number `(C4, C4, K3)` is small, proving it from scratch may itself be the real work.

## what_verify_should_check
- Whether the conditional reduction `R(C4, C4, K3) <= 10 => R(C4, C4, K4) = 20` is stated in the cleanest exact form.
- Whether the edge bound `e(H) <= 48` for 20-vertex `C4`-free graphs is acceptable as written from the common-neighbor count.
- Whether the neighborhood claim "green triangle inside `N_G(v)` gives a green `K4`" is recorded clearly enough for reuse.
- Whether any later solve should prioritize the exact local number `(C4, C4, K3)` over broad 20-vertex search.
