# Solve Record: szymanski-q5

## statement_lock

- Active title: `Does Szymanski's routing conjecture hold for Q_5?`
- Active slug: `szymanski-q5`
- Locked intended statement: for every permutation `sigma` of the `32` vertices of `Q_5`, there exist directed paths `P_v` from `v` to `sigma(v)` in the doubly directed `5`-cube such that no directed edge is used by two distinct paths.
- Working model: `V(Q_5) = {0,1}^5`, and for each vertex `x` and coordinate `i in {1,2,3,4,5}` there is one directed edge `x -> x xor e_i` and one directed edge `x xor e_i -> x`.
- I am solving only this exact finite universal statement for `Q_5`, not the full all-dimensions conjecture.

Self-check:
- The target is the exact `Q_5` permutation-routing statement from `selected_problem.md`.
- I am not weakening the problem to a special class of permutations.

## definitions

- `d(x,y)` denotes Hamming distance.
- For a fixed coordinate `i`, write `H_i^0 = {x : x_i = 0}` and `H_i^1 = {x : x_i = 1}`; each is a copy of `Q_4`.
- `mate_i(x) = x xor e_i` is the neighbor across coordinate `i`.
- A path of length `0` is allowed when `sigma(v) = v`; if verification prefers a different fixed-point convention, this is only a harmless bookkeeping choice.
- "Pairwise edge-disjoint" is interpreted on directed edges. So one path may use `x -> y` while another uses `y -> x`; those are different arcs in the bidirected cube.
- A shortest path from `x` to `y` flips each differing coordinate exactly once, in some order.

Self-check:
- These conventions match the dossier's directed-cube model.
- The directed-edge interpretation matters and is explicitly fixed here.

## approach_A

Structural / invariant route: show that every obvious capacity obstruction already vanishes.

- For each coordinate `i`, define
  `m_i = |{x : sigma(x)_i != x_i}|`.
  Then
  `sum_x d(x,sigma(x)) = m_1 + m_2 + m_3 + m_4 + m_5`.
  Since each `m_i <= 32`, every permutation satisfies
  `sum_x d(x,sigma(x)) <= 160`,
  exactly the total number of directed edges in the bidirected `Q_5`.
- More precisely, let
  `m_i^+ = |{x : x_i = 0 and sigma(x)_i = 1}|`
  and
  `m_i^- = |{x : x_i = 1 and sigma(x)_i = 0}|`.
  Because `sigma` is a permutation and each half `H_i^0`, `H_i^1` has size `16`, we have `m_i^+ = m_i^- <= 16`.
  So even coordinate-by-coordinate, every permutation respects the raw directional capacities across the `i`-cut.
- For any subset `X ⊆ V(Q_5)`, let
  `c_sigma(X) = |{x in X : sigma(x) not in X}|`.
  Since `sigma(X)` has the same size as `X`,
  `c_sigma(X) <= min(|X|, 32 - |X|)`.
- In `Q_5`, the edge boundary satisfies
  `|delta(X)| >= min(|X|, 32 - |X|)`.
  One standard way to see this is the cube inequality
  `e(X) <= |X| log_2 |X| / 2` for `|X| <= 16`, which gives
  `|delta(X)| = 5|X| - 2e(X) >= |X|`,
  and then apply complement symmetry for `|X| > 16`.
- Therefore every cut inequality that a putative edge-disjoint routing would have to satisfy already holds automatically for every permutation of `Q_5`.

Why this matters:
- Any counterexample would have to be subtler than a simple cut shortage, parity issue, or total-length overload.
- Any positive proof also needs something stronger than checking the standard necessary conditions.

Self-check:
- The identities for `sum_x d(x,sigma(x))` and `m_i^+ = m_i^-` are exact.
- The cut-bound step uses a standard cube isoperimetric fact; it is plausible but should be independently checked in verification if it becomes load-bearing later.

## approach_B

Construction / decomposition route: split the cube into two `Q_4` halves along one coordinate and lift the solved `Q_4` case where possible.

Fix a coordinate `i` and write `Q_5 = H_i^0 ∪ H_i^1` with `16` vertical `i`-edges joining `x` to `mate_i(x)`.

Exact subcase 1: `sigma` preserves coordinate `i`.

- If `sigma(H_i^0) = H_i^0` and `sigma(H_i^1) = H_i^1`, then `sigma` restricts to two permutations `sigma_0` on `H_i^0` and `sigma_1` on `H_i^1`.
- By the dossier's solved `Q_4` case, each `sigma_t` has a routing inside its half.
- The two half-routings use disjoint edge sets because the halves are edge-disjoint.
- Their union is therefore a routing of `sigma` in `Q_5`.

Exact subcase 2: `sigma` flips coordinate `i` for every vertex.

- If `sigma(H_i^0) = H_i^1` and `sigma(H_i^1) = H_i^0`, start every path with the vertical edge across coordinate `i`.
- For `x in H_i^0`, after the first edge `x -> mate_i(x)`, the remaining target `sigma(x)` lies in `H_i^1`.
  This defines a permutation `tau_1` of `H_i^1` by
  `tau_1(mate_i(x)) = sigma(x)`.
- Similarly, for `y in H_i^1`, define a permutation `tau_0` of `H_i^0` by
  `tau_0(mate_i(y)) = sigma(y)`.
- Route `tau_0` inside `H_i^0` and `tau_1` inside `H_i^1` using the solved `Q_4` case, then concatenate with the initial vertical edge.
- These path families are edge-disjoint because the vertical `i`-edges are disjoint from all internal half-edges, and the two half-routings live in disjoint halves.

Attempted mixed-case lift, where the argument stalls:

- Let `A = {x in H_i^0 : sigma(x) in H_i^1}` and `B = {y in H_i^1 : sigma(y) in H_i^0}`.
  Then `|A| = |B| = k`, with `0 < k < 16` in the genuinely mixed case.
- The natural idea is to send the `k` crossers through `k` vertical edges and route everything else inside the halves.
- The problem is that after choosing those vertical edges, the residual demand in each half is no longer an ordinary permutation-routing instance on `16` vertices. It becomes a balanced demand with repeated intermediate sources or repeated intermediate targets.
- The solved `Q_4` statement only gives routings for permutations, not for these more general half-demands.
- I do not currently see a clean compatibility condition on the chosen vertical crossing set that always turns the mixed case back into two honest `Q_4` permutations.

Self-check:
- The preserve-a-coordinate and flip-a-coordinate-everywhere lemmas are complete proofs.
- The mixed-case reduction is recorded only as a stalled idea, not as a proved reduction.

## lemma_graph

1. Exact Lemma A: if `sigma` preserves some coordinate half-decomposition, then `sigma` is routable in `Q_5`.
2. Exact Lemma B: if `sigma` flips some fixed coordinate for every vertex, then `sigma` is routable in `Q_5`.
3. Necessary-condition Lemma C: every permutation of `Q_5` already satisfies the total-length, directional-capacity, and cut-capacity tests.
4. Therefore any unresolved permutation must, for every coordinate `i`, mix both behaviors: some vertices preserve `i`, some vertices flip `i`, and crossers occur in both directions.
5. Remaining gap: reduce this fully mixed regime to smaller solved pieces without reusing edges or leaving the class of permutation-routing instances.

## chosen_plan

- The structural route was the best first pass because it can rule out trivial obstructions without computation.
- The decomposition route was the best constructive route because the dossier already says `Q_4` is solved, so any honest reduction to halves would be valuable.
- This produced two exact routable classes and a clear diagnosis of the remaining bottleneck.
- I chose not to start code because the next obvious step is generic search over mixed permutations, not a narrowly justified checker, falsifier, or witness verification.

Self-check:
- The plan stayed reasoning-first and extracted exact theorems before considering computation.
- Stopping before code is deliberate: the unresolved step is a structural reduction problem, not yet a sharply targeted finite witness check.

## self_checks

- Statement-lock check: every conclusion is about the exact universal permutation-routing statement on the bidirected `Q_5`.
- Definitions check: the half-decomposition and directed-edge conventions are consistent with the selected problem file.
- Approach A check: the coordinate-balance identity and total-length formula are exact; the only imported ingredient is the standard cube boundary lower bound.
- Approach B check: the two broad subcases are completely solved from the `Q_4` dossier fact alone.
- Conservatism check: I am not claiming that the mixed case reduces to `Q_4`; that is precisely the open step left in this artifact.
- Method check: no code, brute force, SAT, ILP, CP-SAT, or generic optimization was used.

## code_used

- No code used.
- Reason: after the handwritten analysis, the next unresolved step is not a specific witness or counterexample hypothesis but the general mixed-case reduction. Immediate computation would drift toward broad search rather than a minimal checker.

## result

- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Exact outputs from this solve pass:
  - every permutation that preserves some coordinate is routable;
  - every permutation that flips some fixed coordinate for every vertex is routable;
  - every permutation automatically passes the obvious total-length, directional, and cut necessary conditions.
- The unresolved regime is the first genuinely hard one: permutations that are mixed on every coordinate.
- I do not have either a full proof of the `Q_5` statement or a counterexample permutation.

## likely_failure_points

- The cut-capacity discussion in `approach_A` uses a standard cube inequality and should be checked rather than trusted blindly.
- The solved `Q_4` case may need a stronger compatibility or splice theorem than mere existence of a routing if one wants to finish the mixed case recursively.
- A real obstruction, if one exists, is likely invisible to single-coordinate counts and single-cut tests.
- If the conjecture is true, the missing ingredient is probably a nontrivial normalization of mixed permutations, not another basic capacity lemma.

## what_verify_should_check

- Check the preserve-a-coordinate and flip-a-coordinate-everywhere constructions carefully and confirm that the concatenated path families are truly edge-disjoint.
- Check the identities `m_i^+ = m_i^-` and `sum_x d(x,sigma(x)) <= 160`.
- Check the cited boundary inequality `|delta(X)| >= min(|X|, 32 - |X|)` for `Q_5` if the cut discussion is going to be reused.
- Decide whether the mixed-half reduction can be repaired by a stronger local theorem on `Q_4`, or whether a bounded reduced search over normalized mixed permutations is now justified.
- Keep the classification conservative unless the mixed regime itself is actually resolved.

## verify_rediscovery

- PASS 1 used a bounded web audit aimed at the exact `Q_5` instance, notation variants, the canonical REGS source, and later status mentions.
- The canonical REGS page still presents Szymanski's conjecture as proved through dimension `4` and points to dimension `5` as the first unresolved case.
- The bounded audit did not locate a later paper, theorem, proposition, example, or survey item settling the exact `Q_5` permutation-routing statement.
- Verdict for PASS 1: no rediscovery established within budget. The current artifact should therefore not be reclassified as `REDISCOVERY`.

## verify_faithfulness

- The solve artifact is faithful about what it actually proved: it records two exact routable subfamilies and one package of necessary conditions, and it explicitly keeps the overall run at `PARTIAL`.
- There is no wrong-theorem drift in the final solve-stage verdict. The writeup does not claim the full intended statement for all permutations of `Q_5`.
- The only caution is interpretive: Lemmas A and B are exact subresults about the intended model, not a proof of the intended universal statement itself.

## verify_proof

- First incorrect step found: none in the material actually claimed as proved.
- Lemma A is sound. If `sigma` preserves some coordinate split `H_i^0 union H_i^1`, then the restrictions to the two halves are genuine permutations of two disjoint copies of `Q_4`; combining the two known `Q_4` routings cannot create edge conflicts because no edge joins the halves except coordinate-`i` edges, which are unused.
- Lemma B is also sound. When every vertex flips coordinate `i`, the map `x -> mate_i(x)` is a bijection between the halves, so `tau_1(mate_i(x)) = sigma(x)` and `tau_0(mate_i(y)) = sigma(y)` define honest permutations of `H_i^1` and `H_i^0`. Concatenating the unique initial vertical edge with an internal half-routing gives the required source-target paths, and edge-disjointness is preserved because internal half-edges never use coordinate `i`.
- The identities `sum_x d(x,sigma(x)) = sum_i m_i` and `m_i^+ = m_i^- <= 16` are correct.
- The cut discussion is acceptable as a necessary-condition note, not as a decisive step toward the full theorem. For `|X| <= 16`, the standard cube estimate `e(X) <= |X| log_2 |X| / 2 <= 2|X|` gives `|delta(X)| = 5|X| - 2e(X) >= |X|`; complement symmetry gives `|delta(X)| >= 32 - |X|` for larger `X`. This supports the stated cut-capacity heuristic.

## verify_adversarial

- No checker or search code exists in this artifact, so PASS 4 reduced to adversarial stress-testing of the written constructions.
- I tried to break Lemma B by looking for possible reuse of vertical directed edges or accidental entry of the half-routings onto coordinate-`i` edges. That failure mode does not occur: each path uses exactly one initial vertical directed edge, those `32` directed edges are pairwise distinct, and the remaining path stays entirely inside one half.
- I also checked the fixed-point convention. Allowing length-`0` paths is harmless here because the problem only forbids repeated directed-edge use, and a zero-length path uses none.
- No adversarial counterexample was found against the claims actually made in the solve artifact.

## verify_verdict

- `verify_verdict = VERIFIED`
- `classification = PARTIAL`
- `confidence = medium`
- `lean_ready = false`
- Reason: the artifact's exact sublemmas and necessary-condition package survived skeptical checking, but they still do not resolve the fully mixed-coordinate regime, so the exact intended `Q_5` statement remains open in this run.

## minimal_repair_if_any

- No repair was needed.
- The only conservative clarification is that the cut-bound discussion should continue to be treated as background necessary-condition analysis, not as progress on the unresolved mixed case by itself.
