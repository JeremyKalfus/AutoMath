# powers-of-two-pairs-22

## statement_lock
- Active slug: `powers-of-two-pairs-22`
- Title: `Is A352178(22) = 44?`
- Locked intended statement: `A352178(22) = 44`.
- Exact working formulation for this solve pass: among all `22`-element sets `S` of distinct integers, the number
  `e(S) := #{ {x,y} subset S : x != y, x+y is a power of 2 }`
  is at most `44`, with equality achieved by some explicit `S`.

Self-check:
- The target is the exact `n = 22` instance, not an asymptotic statement and not a restricted family unless stated explicitly later.
- I can already re-derive the lower bound `e(S) >= 44` from an explicit witness found locally, so the unresolved direction is the upper bound `e(S) <= 44`.

## definitions
- For each power of `2`, write `M_q` for the matching on `S` whose edges are the unordered pairs `{x,y}` with `x+y=q`.
- Distinct powers give edge-disjoint matchings, because a fixed pair cannot sum to two different integers.
- If `q != r`, then the composition of reflections `x -> q-x` and `x -> r-x` is the translation `x -> x + (r-q)`.
- Therefore every connected component of `M_q union M_r` is an alternating path; no alternating cycle can occur in a finite integer set unless `q = r`.
- In particular, for any two distinct powers `q,r`,
  `|M_q| + |M_r| <= 21`,
  because a forest on at most `22` vertices has at most `21` edges.

Ambiguities / conventions:
- I count unordered pairs only, so `{x,y}` and `{y,x}` are the same edge.
- `power of 2` means `2^k` for some integer `k >= 0`.
- Distinct integers are allowed to be negative, zero, or positive.

Self-check:
- The matching decomposition is exact.
- The two-color alternating-path lemma is rigorous and will be the main structural invariant.

## approach_A
- Structural / invariant route:
  1. Decompose the full graph into matchings `M_q`.
  2. Use the two-color lemma: for distinct powers `q,r`, the graph `M_q union M_r` is a path forest, hence `|M_q| + |M_r| <= 21`.
  3. When equality `|M_q| + |M_r| = 21` occurs, the union is a single spanning path on all `22` vertices, forcing the vertex set to line up along an arithmetic progression with common difference `|q-r|`.
  4. Try to show that any hypothetical configuration with `> 44` edges must have two large color classes, hence must already be close to an arithmetic progression, after which the remaining colors can be counted explicitly.
- What I could prove cleanly by hand:
  - the two-color bound `|M_q| + |M_r| <= 21`;
  - a strong hint that near-extremal configurations should look progression-like.
- What I could not close cleanly by hand:
  - a full deduction from the pairwise forest constraints alone to the global upper bound `44`.

Self-check:
- This route explains why arithmetic progressions are natural.
- At this point it is not yet a complete proof of the intended statement.

## approach_B
- Construction / extremal route:
  - Try the odd arithmetic progression
    `S_a := {a, a+2, a+4, ..., a+42}`
    with `22` terms.
  - For a power `2^t`, an edge `{a+2i, a+2j}` satisfies
    `2a + 2(i+j) = 2^t`,
    so
    `i+j = 2^(t-1) - a =: m_t`.
  - Thus the number of `2^t`-edges in `S_a` is exactly the number `F(m_t)` of pairs
    `0 <= i < j <= 21` with `i+j = m_t`.
  - For `0 <= m <= 42`,
    `F(m) = floor((min(m, 42-m) + 1)/2)`,
    and `F(m) = 0` outside that range.
- For `a = -17`, the relevant values are
  - `m_1 = 18`, giving `F(18) = 9` pairs summing to `2`;
  - `m_2 = 19`, giving `F(19) = 10` pairs summing to `4`;
  - `m_3 = 21`, giving `F(21) = 11` pairs summing to `8`;
  - `m_4 = 25`, giving `F(25) = 9` pairs summing to `16`;
  - `m_5 = 33`, giving `F(33) = 5` pairs summing to `32`;
  - larger powers contribute `0`.
- Therefore the explicit set
  `S_* = {-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,17,19,21,23,25}`
  has
  `9 + 10 + 11 + 9 + 5 = 44`
  power-of-two pairs.

Self-check:
- The witness is exact and easy to verify directly.
- This independently recovers the lower bound `A352178(22) >= 44`.

## lemma_graph
1. Every power `q` defines a matching `M_q`.
2. For distinct powers `q,r`, the union `M_q union M_r` is an alternating path forest, so `|M_q| + |M_r| <= 21`.
3. Near equality in step 2 forces the vertex set to be progression-like with common difference `|q-r|`.
4. The explicit odd progression `S_*` attains `44` edges.
5. If a global upper bound `44` is true, the progression witness is already optimal.
6. If the upper bound stalls, the most justified code is a bounded falsifier search around the progression witness and over the arithmetic-progression family.

Self-check:
- Steps 1, 2, and 4 are rigorous.
- Step 3 is a strong structural heuristic; I did not fully formalize the exact classification of the equality case.

## chosen_plan
- Best handwritten path:
  1. Lock the explicit `44`-edge witness.
  2. Push the two-color forest invariant as far as possible toward an upper bound.
  3. If that still does not close the theorem, run only a tiny bounded experiment that is directly tied to the progression ansatz:
     - exact scan of all `22`-term step-`2` arithmetic progressions;
     - bounded one-swap and two-swap improvement search around the best progression witness in a modest odd window.
- Rationale:
  - this is not generic optimization;
  - it directly tests the specific structural hypothesis suggested by the two-color lemma;
  - if a simple perturbation beats `44`, the intended statement is probably false.

Self-check:
- This keeps reasoning first and code second.
- The code, if used, will be a bounded falsifier / witness-checker, not a full blind search.

## self_checks
- Statement-lock check: still the exact `n = 22` instance.
- Lower-bound check: the explicit odd progression `S_*` really has `22` distinct integers and gives `44` counted pairs by the closed-form count above.
- Structural check: the two-color argument uses only finite-set arithmetic and does not appeal to any external source.

## code_used
- Used one short script:
  [`search_near_ap.py`](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/powers-of-two-pairs-22/search_near_ap.py)
- What it checked:
  - direct verification that the explicit witness `S_*` has score `44`;
  - exact scan of all odd `22`-term step-`2` arithmetic progressions `S_a = {a, a+2, ..., a+42}`;
  - exact one-swap and two-swap improvement search around `S_*` inside the fixed window `[-40,70]`.
- Output summary:
  - `witness_score = 44`;
  - `best_odd_progression_score = 44`, uniquely at start `a = -17` in the scanned family;
  - `best_one_swap_score = 44`;
  - `best_two_swap_score = 44`.
- Why the odd-progression scan is exhaustive for that family:
  - if `a < -41`, then even the largest pair sum `(a+40) + (a+42) = 2a + 82` is nonpositive, so there are no edges;
  - if `a > 63`, then every pair sum lies in an interval of length `80` above `128`, which contains at most one power of `2`, so the total score is at most `11`;
  - hence any odd step-`2` progression that could compete with the `44`-edge witness is covered by the finite scan `a in {-41,-39,...,63}`.

## result
- Final solve verdict for this pass: `PARTIAL`.
- What is rigorous from this artifact:
  - exact lower bound `A352178(22) >= 44` via the explicit witness
    `S_* = {-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,17,19,21,23,25}`;
  - exact variant theorem: among odd `22`-term step-`2` arithmetic progressions, the maximum score is `44`, attained by `S_*`;
  - structural invariant: for distinct powers `q,r`, the two-color subgraph `M_q union M_r` is a path forest, so `|M_q| + |M_r| <= 21`.
- What is still missing:
  - a proof that every `22`-element integer set is progression-like enough to fall under the exact variant count;
  - or an explicit counterexample with score `>= 45`.
- Bounded evidence from code:
  - inside the fixed local window `[-40,70]`, no one-swap or two-swap perturbation of `S_*` improved on `44`.

## likely_failure_points
- The two-color forest invariant is strong but may still be too weak by itself to force the exact global maximum.
- A non-progression extremal set could exist even if the arithmetic-progression family tops out at `44`.
- Negative entries matter, so naive interval-compression arguments are not obviously valid without more work.
- The local one-swap and two-swap search is only bounded evidence; a better witness could exist farther away or in a qualitatively different family.

## what_verify_should_check
- Check the explicit witness `S_*` and confirm the pair count `44`.
- Check the two-color lemma carefully:
  - each `M_q` is a matching;
  - `M_q union M_r` is a path forest for `q != r`;
  - hence `|M_q| + |M_r| <= 21`.
- Check the arithmetic-progression counting formula
  `F(m) = floor((min(m, 42-m) + 1)/2)`
  for `0 <= m <= 42`.
- Check that the odd-progression scan is genuinely exhaustive for that family using the bounds on `a < -41` and `a > 63`.
- Treat the one-swap and two-swap search only as bounded evidence, not as a proof of the intended global theorem.

## verify_rediscovery
- PASS 1 used a bounded web audit against the canonical sources only.
- The primary-source picture remains:
  - `A352178` still lists exact values only through `n = 21`;
  - `A347301` still gives the lower bound `44` at `n = 22`;
  - `A006855` still gives the `C4`-free upper bound `52` at `n = 22`;
  - the cited 2023 paper on maximizing power-of-two pair counts determines exact values only for `n <= 21`, not `n = 22`.
- I found no theorem, proposition, example, observation, or corollary in the canonical source chain that settles the exact instance `A352178(22)`.
- Rediscovery verdict for the intended statement: not established. The exact `n = 22` instance still appears open within the bounded audit budget.

## verify_faithfulness
- The solver did not actually prove the intended statement `A352178(22) = 44`.
- What the artifact really establishes is narrower:
  - an explicit witness showing `A352178(22) >= 44`;
  - the exact restricted-family result that among odd `22`-term step-`2` arithmetic progressions, the maximum score is `44`;
  - the general two-color lemma `|M_q| + |M_r| <= 21` for distinct powers `q != r`.
- So the solve artifact is faithful only as a lower bound plus a nearby variant theorem. It is not faithful to the exact intended statement.

## verify_proof
- First incorrect step relative to the intended theorem: there is no derivation of the missing global upper bound `e(S) <= 44`.
- I found no flaw in the claims that are explicitly presented as proved:
  - each `M_q` is a matching, since for fixed `x` there is at most one `y = q-x`;
  - if an alternating cycle existed in `M_q union M_r` with `q != r`, composing the two reflections around the cycle would yield a nonzero translation fixing a finite vertex, impossible; hence every component is a path and `|M_q| + |M_r| <= 21`;
  - for the progression `S_a = {a,a+2,...,a+42}`, the count of pairs with `i+j=m` is exactly `F(m) = floor((min(m,42-m)+1)/2)` for `0 <= m <= 42`;
  - substituting `a = -17` gives contributions `9,10,11,9,5`, totaling `44`.
- Therefore the proof is sound for the lower bound and the restricted progression variant, but incomplete for the intended exact claim.

## verify_adversarial
- Reran [`search_near_ap.py`](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/powers-of-two-pairs-22/search_near_ap.py). It again returned:
  - `witness_score = 44`;
  - `best_odd_progression_score = 44` at start `-17`;
  - no improvement by one-swap or two-swap perturbations inside `[-40,70]`.
- Independently recomputed all power-of-two pairs of
  `S_* = {-17,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,17,19,21,23,25}`
  and confirmed exactly `44` such pairs.
- I did not find an adversarial break of the witness or the checker within its stated scope.
- However, the checker only supports the restricted-family and local-perturbation evidence; it does not test all `22`-element integer sets and therefore cannot justify the global theorem.

## verify_verdict
- `VERIFIED` for the artifact's actual mathematical content as a lower bound plus variant.
- Not verified for the intended statement `A352178(22) = 44`.
- Classification should therefore be `VARIANT`, not `EXACT` and not Lean-ready.

## minimal_repair_if_any
- Minimal conservative repair: relabel the run from `PARTIAL` to `VARIANT` because the exact restricted-family theorem appears correct and was checked, while the intended global statement remains open in this artifact.
- No proof patch can upgrade this run to the intended theorem without a new argument establishing the missing global upper bound.
