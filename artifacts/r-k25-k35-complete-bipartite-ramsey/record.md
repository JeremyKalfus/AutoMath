# Solve Record: The Exact Value of R(K2,5, K3,5)

## statement_lock

- Active slug: `r-k25-k35-complete-bipartite-ramsey`.
- Active title: `Determine the exact value of R(K2,5, K3,5)`.
- Exact intended statement for this solve run: determine whether every red-blue coloring of `K_22` already contains a red `K_{2,5}` or a blue `K_{3,5}`. Equivalently, decide whether `R(K_{2,5}, K_{3,5}) = 22` or `23`.
- Working convention: encode a coloring by its red graph `G` on `n` vertices; the blue graph is the complement `\bar G`.
- One-shot publication target if the main claim closes: **The Exact Value of `R(K2,5, K3,5)`**.
- If closed honestly, this would still be about `84%` of a short paper: the exact endpoint is already the title theorem, and the remaining packaging is mainly the witness or forcing proof plus a short prior-work comparison.

## definitions

- `G` is the red graph on `n` vertices.
- `\bar G` is the blue graph.
- “No red `K_{2,5}`” means every vertex-pair in `G` has at most `4` common red neighbors.
- “No blue `K_{3,5}`” means every vertex-triple in `\bar G` has at most `4` common blue neighbors.
- For a vertex `v`, write `d_R(v)` and `d_B(v)` for red and blue degree.
- If a `22`-vertex counterexample exists, then deleting any vertex gives a `21`-vertex coloring still avoiding red `K_{2,5}` and blue `K_{3,5}`.

## approach_A

Structural / invariant route: count common neighborhoods globally, then push with convexity.

1. If `G` has no red `K_{2,5}`, then
   `sum_v C(d_R(v), 2) = sum_{ {x,y} } |N_R(x) ∩ N_R(y)| <= 4 C(n,2)`.
2. If `\bar G` has no blue `K_{3,5}`, then
   `sum_v C(d_B(v), 3) = sum_{ {x,y,z} } |N_B(x) ∩ N_B(y) ∩ N_B(z)| <= 4 C(n,3)`.
3. Since `C(x,2)` and `C(x,3)` are convex, Jensen gives degree-corridor constraints.

For `n = 22` this yields:

- `sum_v C(d_R(v),2) <= 924`, hence `22 C(\bar d_R,2) <= 924`, so `\bar d_R < 9.679`, hence `e(G) <= 106`.
- `sum_v C(d_B(v),3) <= 6160`, and if `e(G) <= 88`, then `e(\bar G) >= 143`, so `\bar d_B >= 13`; Jensen would then force
  `sum_v C(d_B(v),3) >= 22 C(13,3) = 6292 > 6160`, contradiction.
- Therefore any `22`-vertex counterexample must satisfy
  `89 <= e(G) <= 106`.

The same method for a hypothetical `23`-vertex counterexample gives:

- `sum_v C(d_R(v),2) <= 1012`, hence `e(G) <= 113`.
- A tiny sanity check on the Jensen lower bound for blue triples shows `e(G) >= 101`.
- So any `23`-vertex counterexample to the known upper bound would have to live in the narrow window
  `101 <= e(G) <= 113`.

Local inheritance from the forbidden subgraphs:

- For every vertex `v`, the red graph on `N_R(v)` has maximum degree at most `4`. Otherwise some `u in N_R(v)` would share at least `5` red neighbors with `v`, giving a red `K_{2,5}`.
- For every vertex `v`, the blue graph on `N_B(v)` is `K_{2,5}`-free. Otherwise a blue `K_{2,5}` inside `N_B(v)` together with `v` would give a blue `K_{3,5}`.

This does not close `22` versus `23`, but it produces a rigorous structural slice.

## approach_B

Construction / extremal / contradiction route: reduce the one-step gap to a one-vertex extension problem.

Assume a `22`-vertex counterexample exists, and delete a vertex `x`. The remaining `21`-vertex coloring is a witness for the known lower bound `R(K_{2,5}, K_{3,5}) >= 22`. To reattach `x` without creating a forbidden copy:

- Let `S = N_R(x)`. Then `G[S]` must have maximum degree at most `4`.
- Let `T = N_B(x)`. Then `\bar G[T]` must be `K_{2,5}`-free.

So the endpoint question can be restated as:

> Does some `21`-vertex critical coloring admit an attachment partition `V = S ∪ T` with `Δ(G[S]) <= 4` and `\bar G[T]` `K_{2,5}`-free?

This is the cleanest contradiction route because the public frontier is already one step wide. If every `21`-vertex witness fails this admissible-extension test, then `R(K_{2,5}, K_{3,5}) = 22`. If one witness passes, then `R(K_{2,5}, K_{3,5}) = 23`.

The blocker is concrete: the repository does not contain the actual `21`-vertex lower-bound coloring, so this route cannot be completed honestly inside the current local file budget without drifting into blind graph search.

## lemma_graph

1. Global pair count:
   no red `K_{2,5}` -> `sum_v C(d_R(v),2) <= 4 C(n,2)`.
2. Global triple count:
   no blue `K_{3,5}` -> `sum_v C(d_B(v),3) <= 4 C(n,3)`.
3. Convexity:
   Lemmas 1 and 2 -> global red-edge corridor for `n = 22`.
4. Red-neighborhood lemma:
   `v` fixed -> `Δ(G[N_R(v)]) <= 4`.
5. Blue-neighborhood lemma:
   `v` fixed -> `\bar G[N_B(v)]` is `K_{2,5}`-free.
6. Extension lemma:
   a `22`-vertex counterexample exists iff some `21`-vertex witness admits a new vertex satisfying Lemmas 4 and 5.

## chosen_plan

The best paper-facing path is the extension lemma, not a blind global search.

- Reason: the frontier is exactly one step wide, so the mathematically right object is the admissible extension of a `21`-vertex critical witness.
- What I could prove immediately: the degree corridor and the two neighborhood constraints above.
- What I could not finish locally: the actual extension test, because the concrete `21`-vertex witness is not present in the repository packet.
- Why I did not escalate to graph search: this target is explicitly marked `search_heavy = False`, and blind search without the published witness would violate the reasoning-first rule.

## self_checks

- Statement lock check: the packet consistently frames the endpoint as `22` versus `23`; no scope drift was introduced.
- Approach A check: the pair-count and triple-count identities are exact, and the `89 <= e(G) <= 106` corridor for `n = 22` is rigorous.
- Approach B check: the extension reformulation is exact, not heuristic; the missing ingredient is only the explicit `21`-vertex witness.
- Code check: no search or optimization was used to drive the argument. The only code was a tiny numeric sanity check after the reasoning was already fixed.
- Publication check: current progress is theorem-facing, but still too thin to count as a micro-paper result by itself.

## code_used

- Minimal code only.
- I used one tiny local Python sanity check to confirm the Jensen-based lower edge threshold numerically:
  - for `n = 22`, the blue-triple bound first becomes consistent at `e(G) = 89`;
  - for `n = 23`, it first becomes consistent at `e(G) = 101`.
- No graph search, SAT, ILP, CP-SAT, or brute-force coloring search was run.

## result

- No exact closure was obtained in this solve run; the local status remains `R(K_{2,5}, K_{3,5}) in {22,23}`.
- Rigorous theorem slice obtained:
  - If a `22`-vertex counterexample exists, then its red graph `G` satisfies `89 <= e(G) <= 106`.
  - For every vertex `v`, `Δ(G[N_R(v)]) <= 4`.
  - For every vertex `v`, the blue graph on `N_B(v)` is `K_{2,5}`-free.
- Secondary slice for the known `n = 23` forcing side:
  - any hypothetical `23`-vertex counterexample would satisfy `101 <= e(G) <= 113`.
- What scales:
  - the global pair/triple counting method scales directly to nearby mixed complete-bipartite gaps;
  - the admissible-extension viewpoint scales whenever the public frontier is one-step wide.
- What does not scale:
  - the current argument does not distinguish `22` from `23` without a concrete `21`-vertex witness or a sharper local obstruction.
- Suggested theorem slice:
  - “Any `22`-vertex coloring avoiding red `K_{2,5}` and blue `K_{3,5}` has red edge count in `[89,106]`, red neighborhoods of maximum internal red degree `4`, and blue neighborhoods that are `K_{2,5}`-free.”
- Best next parameter shifts:
  - first, test the actual `21`-vertex witness for admissible one-vertex extensions to `22`;
  - second, if that fails analytically, examine whether the same extension template sharpens for the nearest upward family member with a one-step gap.
- Current package assessment:
  - stronger than a vague partial note, but still an instance-level structural narrowing rather than a paper-shaped exact claim.

## family_affinity

This sits cleanly in the mixed complete-bipartite Ramsey corridor. The method naturally talks to one-step endpoint gaps of the form `R(K_{2,t}, K_{3,s})`, especially when a published lower-bound witness and a published one-step upper bound already exist.

## generalization_signal

Moderate. The pair/triple common-neighborhood inequalities and the one-vertex extension lemma should transfer to nearby mixed bipartite pairs, but the final obstruction is still witness-specific rather than obviously family-uniform.

## proof_template_reuse

High reuse value for one-step finite gaps:

- translate the coloring into a red graph plus blue complement;
- count pair-common red neighbors and triple-common blue neighbors;
- derive a narrow global density corridor by convexity;
- reduce the endpoint decision to admissible extension of the last known lower-bound witness.

## candidate_theorem_slice

Candidate theorem slice:

> Let `G` be the red graph of a red-blue coloring of `K_22` with no red `K_{2,5}` and no blue `K_{3,5}`. Then `89 <= e(G) <= 106`. Moreover, for every vertex `v`, the induced red graph on `N_R(v)` has maximum degree at most `4`, and the induced blue graph on `N_B(v)` is `K_{2,5}`-free.

This is exact, rigorous, and directly relevant to the endpoint question, but not yet enough to separate `22` from `23`.

## smallest_param_shift_to_test

The smallest useful shift is not a broad family jump; it is the one-vertex extension itself.

- Immediate shift to test: take the concrete `21`-vertex lower-bound witness and classify all admissible attachments of a `22`nd vertex under `Δ(G[S]) <= 4` and `\bar G[T]` `K_{2,5}`-free`.
- If a family move is needed after that, the nearest useful structural shift is the next mixed pair where the same one-step extension mechanism survives, rather than a broad campaign over many bipartite tuples.

## why_this_is_or_is_not_publishable

- If the exact value closed here, the result would still be publication-grade: the title theorem would be **The Exact Value of `R(K2,5, K3,5)`**, and the remaining packaging would be minimal.
- Minimal remaining packaging work after an exact solve:
  - write the explicit `22`-vertex witness or the forcing proof at `22`;
  - add the short comparison `22 <= R(K_{2,5}, K_{3,5}) <= 23` from prior work;
  - include one boundary remark explaining why neighboring exact bipartite cases do not force the mixed pair.
- Current result is not yet publishable in the micro-paper lane.
- Reason: it narrows the shape of any counterexample, but it does not determine the exact endpoint and does not yet yield a standalone title theorem.

## paper_shape_support

If the main claim closes, the smallest supporting structure that already makes the note feel paper-shaped is:

- the global density corridor `89 <= e(G) <= 106` for a `22`-vertex counterexample;
- the local extension constraints `Δ(G[S]) <= 4` and `\bar G[T]` `K_{2,5}`-free for the attaching vertex;
- one immediate remark: every `22`-vertex counterexample must arise as a highly constrained one-vertex extension of a `21`-vertex witness.

Natural corollary / remark if the main claim closes:

- If `R(K_{2,5}, K_{3,5}) = 22`, then no published `21`-vertex witness extends by a single vertex subject to the above local constraints.

## boundary_remark

The current structural slice is honest but coarse. Global convexity still leaves room for both endpoints, and the real difficulty is local: the last admissible extension of the `21`-vertex witness may fail for a highly configuration-specific reason that these averaged inequalities cannot see.

## likely_failure_points

- The pair/triple counting inequalities may be too weak to distinguish the last critical configurations.
- Without the concrete `21`-vertex witness, the extension lemma cannot be cashed out.
- A proof that `R(K_{2,5}, K_{3,5}) = 22` may depend on witness-specific symmetry or computer verification not visible in the current packet.
- A proof that `R(K_{2,5}, K_{3,5}) = 23` would require an explicit `22`-vertex coloring, which is absent locally.

## what_verify_should_check

- Verify the pair-count and triple-count identities and the resulting edge corridors.
- Recover the actual `21`-vertex lower-bound construction from the 2025 source and test the admissible-extension lemma against it.
- Check whether the neighborhood lemmas or the `89 <= e(G) <= 106` corridor already appear implicitly in prior work.
- Check whether the 2021 upper-bound computation exposes extra certificate structure that can sharpen the local obstruction on `22` vertices.
