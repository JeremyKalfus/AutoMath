# powers-of-two-pairs-23

## statement_lock
- Active slug: `powers-of-two-pairs-23`
- Title: `What is the exact value of A352178(23)?`
- Locked intended statement: determine the exact value of `A352178(23)`.
- Exact working formulation for this solve pass: among all `23`-element sets `S` of distinct integers, maximize
  `e(S) := #{ {x,y} subset S : x != y, x+y is a power of 2 }`.
- Immediate concrete target: either prove a global upper bound matching an explicit witness, or find a counterexample to the best local lower bound.

Self-check:
- This is the exact `n = 23` instance, not a restricted-family variant unless I label it as such later.
- In solve, any positive exact-looking proof can be at most `CANDIDATE`; `EXACT` is off-limits before Lean.

## definitions
- For each power of `2`, write `M_q` for the matching on `S` whose edges are the unordered pairs `{x,y}` with `x+y=q`.
- Distinct powers give edge-disjoint matchings, since a fixed unordered pair has only one sum.
- For distinct powers `q != r`, every connected component of `M_q union M_r` is an alternating path. The usual reason is that composing the reflections `x -> q-x` and `x -> r-x` gives the nonzero translation `x -> x + (r-q)`, so an alternating cycle cannot close on a finite integer set.
- Therefore for `n = 23`,
  `|M_q| + |M_r| <= 22`
  for every distinct powers `q,r`, because a forest on at most `23` vertices has at most `22` edges.

Ambiguities / conventions:
- `power of 2` means `2^k` for some integer `k >= 0`.
- Distinct integers may be negative, zero, or positive.
- Pairs are unordered, so `{x,y}` is counted once.
- The power `1` is technically allowed, but in same-parity constructions it contributes nothing because all pair sums are even.

Self-check:
- The matching decomposition is exact.
- The two-color path-forest lemma is rigorous and is the main structural invariant available without code.

## approach_A
- Structural / invariant route:
  1. Sort color classes by size: `m_1 >= m_2 >= ...`, where each `m_i <= 11`.
  2. Push the two-color forest constraint `m_i + m_j <= 22` as far as possible.
  3. Study the equality case `m_i = m_j = 11`: then `M_q union M_r` has exactly `22` edges on `23` vertices, so it is a single spanning alternating path.
  4. In that equality case, after labeling the path vertices `v_0,...,v_22` with alternating edge sums `q,r,q,r,...`, one gets
     `v_{2k} = a + k(r-q)` and `v_{2k+1} = q-a-k(r-q)`.
     Thus the vertex set is forced into a rigid two-progression pattern.
  5. A third color `s` on that path must satisfy one of three explicit index equations:
     - even-even edges: `2a + (i+j)(r-q) = s`
     - odd-odd edges: `2(q-a) - (i+j)(r-q) = s`
     - even-odd edges: `q + (i-j)(r-q) = s`
     so extra colors become diagonal counts on a finite index grid.
- What this route gives cleanly:
  - the `|M_q| + |M_r| <= 22` upper bound for every pair of colors;
  - a full description of the highly constrained case of two `11`-edge colors.
- Where it stalls:
  - I do not yet have a clean argument that every hypothetical `47`-edge configuration must contain two `11`-edge colors;
  - without that forcing step, the path model is a strong near-extremal heuristic rather than a complete theorem.

Self-check:
- The path parametrization in the `11 + 11` case is correct.
- The missing step is global: I still cannot force all near-extremal examples into this equality case.

## approach_B
- Construction / extremal route:
  - Test the odd step-`2` arithmetic progression
    `S_a := {a, a+2, a+4, ..., a+44}`
    with `23` terms and odd `a`.
  - For a power `2^t` with `t >= 1`, an edge `{a+2i,a+2j}` satisfies
    `2a + 2(i+j) = 2^t`,
    so
    `i+j = 2^(t-1) - a =: m_t`.
  - Hence the number of `2^t`-edges is exactly the number `F(m_t)` of pairs
    `0 <= i < j <= 22` with `i+j = m_t`.
  - For `0 <= m <= 44`,
    `F(m) = floor((min(m, 44-m) + 1)/2)`,
    and `F(m) = 0` outside that range.
- A particularly strong witness is
  `S_* = {-19,-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,17,19,21,23,25}`.
- For this set:
  - sum `2` gives `m = 20`, so `F(20) = 10`;
  - sum `4` gives `m = 21`, so `F(21) = 11`;
  - sum `8` gives `m = 23`, so `F(23) = 11`;
  - sum `16` gives `m = 27`, so `F(27) = 9`;
  - sum `32` gives `m = 35`, so `F(35) = 5`;
  - larger powers contribute `0`.
- Therefore `e(S_*) = 10 + 11 + 11 + 9 + 5 = 46`, so certainly `A352178(23) >= 46`.

Self-check:
- The witness is exact and already beats the `44`-edge lower bound from the `n = 22` family.
- The remaining question is whether any non-progression or perturbed progression can exceed `46`.

## lemma_graph
1. Every power `q` defines a matching `M_q`.
2. For distinct powers `q,r`, the union `M_q union M_r` is an alternating path forest, so `|M_q| + |M_r| <= 22`.
3. If `|M_q| = |M_r| = 11`, then `M_q union M_r` is a spanning alternating path on all `23` vertices.
4. In that case the vertex set has the explicit form
   `{a + k(r-q) : 0 <= k <= 11} union {q-a-k(r-q) : 0 <= k <= 10}`.
5. On that rigid model, any third color is forced onto index diagonals `i+j = c` or `i-j = c`, turning its edge count into a finite arithmetic count.
6. The odd step-`2` progression witness `S_*` attains `46` edges.
7. If a general forcing lemma reduced all `47+` configurations to step 3, then the problem would likely collapse to a finite diagonal-count optimization; I do not yet have that forcing lemma.

Self-check:
- Steps 1 through 6 are rigorous.
- Step 7 is only a roadmap, not an established theorem.

## chosen_plan
- Best current path:
  1. Lock the explicit `46`-edge witness by direct counting.
  2. Record the structural `11 + 11` path model because it is the clearest route to an eventual upper bound.
  3. Since the global forcing step still fails by hand, use minimal code only for tightly scoped checks:
     - direct witness verification;
     - exact scan of the odd `23`-term step-`2` progression family;
     - bounded one-swap and two-swap falsifier searches around the best progression witness in a modest fixed window.
- Rationale:
  - this remains reasoning-first;
  - the code is not a blind global optimizer;
  - it directly tests the specific progression heuristic suggested by the two-color equality case.

Self-check:
- This respects the repo rule against search-first solving.
- If the local perturbation search finds `47+`, the intended statement changes immediately; otherwise it remains evidence, not proof.

## self_checks
- Statement-lock check: still the exact `n = 23` instance.
- Lower-bound check: the explicit odd progression `S_*` has `23` distinct integers and gives `46` counted pairs by the closed-form count above.
- Structural check: the two-color and `11 + 11` path lemmas use only finite integer arithmetic.
- Current honesty check: I do not have a rigorous global upper bound matching `46`.
- Post-code check: the bounded computations below only support the witness and a restricted-family / local-neighborhood analysis; they do not test all `23`-element integer sets.

## code_used
- Used one short script:
  [`search_near_ap.py`](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/powers-of-two-pairs-23/search_near_ap.py)
- What it checked:
  - direct verification that the explicit witness `S_*` has score `46`;
  - exact scan of all odd `23`-term step-`2` arithmetic progressions `S_a = {a, a+2, ..., a+44}`;
  - bounded one-swap and two-swap improvement searches around `S_*` inside the fixed window `[-45,75]`.
- Output summary:
  - `witness_score = 46`;
  - `best_odd_progression_score = 46`;
  - family-maximizing starts in the scanned odd progression family are exactly `a = -19` and `a = -17`;
  - `best_one_swap_score = 46`;
  - `best_two_swap_score = 46`.
- Why the odd-progression scan is exhaustive for that family:
  - if `a < -43`, then even the largest pair sum `(a+42) + (a+44) = 2a + 86` is nonpositive, so there are no counted edges;
  - if `a > 65`, then every pair sum lies in an interval of length `88` above `132`, which contains at most one power of `2`, so the score is at most `11`;
  - hence any odd step-`2` progression that could compete with the `46`-edge witness is covered by the finite scan `a in {-43,-41,...,65}`.

## result
- Final solve verdict for this pass: `PARTIAL`.
- What is rigorous from this artifact:
  - exact lower bound `A352178(23) >= 46` via the explicit witness
    `S_* = {-19,-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,17,19,21,23,25}`;
  - exact restricted-family result: among odd `23`-term step-`2` arithmetic progressions, the maximum score is `46`, attained exactly at starts `a = -19` and `a = -17`;
  - structural invariant: for distinct powers `q != r`, the two-color subgraph `M_q union M_r` is a path forest, so `|M_q| + |M_r| <= 22`;
  - structural equality case: if two colors both have size `11`, their union is a spanning alternating path with the explicit parametrization recorded above.
- What is still missing:
  - a proof that every `23`-element integer set has at most `46` power-of-two pairs;
  - or an explicit counterexample with score `>= 47`.
- Bounded evidence from code:
  - no one-swap or two-swap perturbation of `S_*` inside `[-45,75]` improved on `46`.

## likely_failure_points
- The two-color invariant may still be too weak to force a global extremal structure.
- A better configuration may exist outside the odd progression family.
- Even within the `11 + 11` path model, I have not yet completed the full count optimization over all allowed powers and placements.
- The bounded local search is only evidence; a qualitatively different non-progression extremizer could still exist.

## what_verify_should_check
- Check the witness `S_*` and confirm the exact pair count `46`.
- Check the two-color path-forest lemma for `n = 23`, namely `|M_q| + |M_r| <= 22`.
- Check the `11 + 11` equality case and the path parametrization
  `v_{2k} = a + k(r-q)`, `v_{2k+1} = q-a-k(r-q)`.
- Check the arithmetic-progression counting formula
  `F(m) = floor((min(m, 44-m) + 1)/2)`
  for `0 <= m <= 44`.
- Check that the odd-progression scan is exhaustive for that family using the bounds `a < -43` and `a > 65`.
- Treat the one-swap and two-swap computation only as bounded falsifier evidence, not as a proof of the intended global theorem.

## verify_rediscovery
- PASS 1 used a bounded web audit centered on the canonical source chain and exact-instance searches.
- The source picture still looks unresolved for the exact `n = 23` instance:
  - OEIS [`A352178`](https://oeis.org/A352178) still lists exact values only through `n = 21`;
  - the cited source paper on maximizing power-of-two pair counts gives exact values through `n <= 21`, not `n = 23`;
  - no theorem, proposition, example, observation, corollary, or discussion item found in that source chain settled the exact instance `A352178(23)`.
- Rediscovery verdict for the intended statement: not established within the bounded audit budget.
- The current artifact may still contain a correct lower bound and a correct variant theorem, but it does not look like a rediscovery of a published exact solution of the intended `n = 23` problem.

## verify_faithfulness
- The solve artifact does not prove the intended statement "determine the exact value of `A352178(23)`".
- What it actually establishes is narrower:
  - an explicit witness showing `A352178(23) >= 46`;
  - the exact restricted-family result that among odd `23`-term step-`2` arithmetic progressions, the maximum score is `46`;
  - the general two-color lemma `|M_q| + |M_r| <= 22` for distinct powers `q != r`;
  - the explicit `11 + 11` equality-case parametrization.
- So the artifact is faithful as a lower bound plus nearby structural and restricted-family results, but not as a proof of the exact intended global maximum.

## verify_proof
- First incorrect step relative to the intended theorem: the artifact never derives the missing global upper bound `e(S) <= 46`.
- I found no error in the claims that are explicitly presented as proved:
  - each `M_q` is a matching, since for fixed `x` there is at most one `y = q - x`;
  - if an alternating cycle existed in `M_q union M_r` with `q != r`, composing the reflections `x -> q-x` and `x -> r-x` around the cycle would produce a nonzero translation fixing a vertex, impossible on integers, so every component is a path and `|M_q| + |M_r| <= 22`;
  - if `|M_q| = |M_r| = 11`, then `M_q union M_r` has `22` edges on `23` vertices, hence is a spanning tree; since every vertex degree is at most `2`, it is a single alternating path, yielding the stated parametrization;
  - for the progression `S_a = {a, a+2, ..., a+44}`, the count of pairs with `i+j = m` is exactly `F(m) = floor((min(m,44-m)+1)/2)` for `0 <= m <= 44`;
  - substituting the witness start `a = -19` gives contributions `10, 11, 11, 9, 5`, totaling `46`.
- Therefore the proof content is sound for the lower bound, the two-color structural lemma, the equality case, and the restricted progression variant, but incomplete for the intended exact claim.

## verify_adversarial
- Reran [`search_near_ap.py`](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/powers-of-two-pairs-23/search_near_ap.py). It again returned:
  - `witness_score = 46`;
  - `best_odd_progression_score = 46`;
  - no improvement by one-swap or two-swap perturbations inside `[-45,75]`.
- Independently recomputed all power-of-two pairs of
  `S_* = {-19,-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,17,19,21,23,25}`
  and confirmed exactly `46` such pairs, distributed as:
  - `10` pairs summing to `2`;
  - `11` pairs summing to `4`;
  - `11` pairs summing to `8`;
  - `9` pairs summing to `16`;
  - `5` pairs summing to `32`.
- Independently checked the restricted-family tie claim and confirmed that the odd `23`-term step-`2` progression family attains score `46` exactly at starts `a = -19` and `a = -17`.
- I did not find an adversarial break of the witness, the arithmetic-progression count, or the two-color lemma within their stated scope.
- However, the checker only supports a restricted family and bounded local perturbations; it does not search all `23`-element integer sets and therefore cannot justify the global theorem.

## verify_verdict
- `VERIFIED` for the artifact's actual content as a lower bound plus a restricted-family variant theorem.
- Not verified for the intended statement determining the exact value of `A352178(23)`.
- Classification should therefore be `VARIANT`, not `CANDIDATE`, not `EXACT`, and not Lean-ready.

## minimal_repair_if_any
- Minimal conservative repair: relabel the run from `PARTIAL` to `VARIANT` because the checked content is a correct nearby variant and lower bound, while the exact `n = 23` theorem remains open in this artifact.
- No proof patch small enough for verify can upgrade this run to the intended theorem; that would require a new global upper-bound argument or a counterexample with at least `47` edges.
