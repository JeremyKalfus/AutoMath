# Solve Record: c20-2-3-10-cnbc

## statement_lock

- Active title: `Is the quintic circulant C_20(2,3,10) a CNBC graph?`
- Locked target statement: let `G = C_20(2,3,10)` be the simple undirected graph on `Z/20Z` with edges from `i` to `i +/- 2`, `i +/- 3`, and `i + 10` modulo `20`. The exact claim to prove or disprove is:
  `G` admits a red/blue coloring such that every closed neighborhood `N[i] = {i, i +/- 2, i +/- 3, i + 10}` contains exactly three red and three blue vertices.
- Equivalent `+/-1` formulation: write `x_i = 1` for red and `x_i = -1` for blue. Then the CNB condition is
  `x_i + x_{i-2} + x_{i+2} + x_{i-3} + x_{i+3} + x_{i+10} = 0`
  for every `i mod 20`.
- Self-check: `10 == -10 (mod 20)`, so it contributes one antipodal neighbor, not two; the graph is quintic and each closed neighborhood has size `6`, so signed sum `0` is exactly the balance condition.

## definitions

- Graph convention: simple undirected graph on `Z/20Z`; no loops and no multiple edges.
- The generator `10` is antipodal, so the neighbor set of `i` is exactly `i +/- 2`, `i +/- 3`, and `i + 10`.
- A CNB-coloring means equal red and blue counts in each closed neighborhood. Since the closed neighborhood size is `6`, this means exactly `3` red and `3` blue vertices.
- I am treating only the exact instance `C_20(2,3,10)`, not a broader family statement.
- Ambiguities to lock:
  - Indexing is always modulo `20`.
  - `i +/- 2` and `i +/- 3` contribute four distinct neighbors.
  - `i + 10` contributes one distinct antipodal neighbor.
- Self-check: no alternate graph convention or weaker balance notion is being used.

## approach_A

Structural / invariant approach via opposite-pair sums.

- Let `E_i` denote the CNB equation
  `x_i + x_{i-2} + x_{i+2} + x_{i-3} + x_{i+3} + x_{i+10} = 0`.
- Define `y_i = x_i + x_{i+10}` for `i mod 10`.
- Adding `E_i` and `E_{i+10}` gives
  `2 y_i + y_{i-2} + y_{i+2} + y_{i-3} + y_{i+3} = 0`
  for every `i mod 10`.
- This is a circulant linear system on `Z/10Z`. Its Fourier eigenvalues are
  `lambda_k = 2 + 2 cos(4 pi k / 10) + 2 cos(6 pi k / 10)`.
- Direct evaluation for `k = 0, ..., 9` gives the set of values
  `{6, 2, 1 + sqrt(5), 1 - sqrt(5)}`,
  all nonzero.
- Therefore the only solution is `y_i = 0` for all `i`, hence
  `x_{i+10} = -x_i` for every `i`.
- Self-check: this uses only the exact neighborhood mask `{0, +/-2, +/-3, 10}` and the standard Fourier diagonalization of a length-`10` circulant.

## approach_B

Construction / extremal / contradiction approach on the reduced `10`-term sign pattern.

- Once `x_{i+10} = -x_i`, write `a_i = x_i` for `i mod 10`.
- The CNB equations reduce to
  `a_{i-2} + a_{i+2} + a_{i-3} + a_{i+3} = 0`
  for every `i mod 10`.
- Let `T = sum_{j mod 10} a_j`. The four indices `i +/- 2, i +/- 3` are exactly the complement of `{i-1, i, i+1, i+5}` in `Z/10Z`, so the reduced equation is equivalent to
  `a_{i-1} + a_i + a_{i+1} + a_{i+5} = T`.
- Subtract consecutive equations:
  `a_{i-1} + a_{i+5} = a_{i+2} + a_{i+6}`.
  Defining `b_i = a_i + a_{i+5}`, this becomes `b_{i-1} = b_{i+2}`.
- On `Z/5Z`, shifting by `3` generates every residue class, so every `b_i` is the same constant `c`.
- Then `T = sum_{i=0}^4 b_i = 5c`, while `a_{i+5} = c - a_i`.
- Substituting back gives
  `a_{i-1} + a_{i+1} = 4c`.
  The left side lies in `{-2, 0, 2}` because each `a_j` is `+/-1`, while `c` lies in `{-2, 0, 2}`. So the only possible value is `c = 0`.
- Hence `a_{i+1} = -a_{i-1}` for all `i`, equivalently `a_{i+2} = -a_i`.
- Iterating five times yields `a_{i+10} = -a_i`, contradicting the `10`-periodicity `a_{i+10} = a_i`.
- So no reduced `+/-1` pattern exists.
- Self-check: this route is now a full contradiction once the antipodal cancellation from Approach A is established.

## lemma_graph

1. A CNB-coloring is equivalent to a `+/-1` solution of the `20` equations `E_i`.
2. Adding opposite equations produces a length-`10` circulant system for `y_i = x_i + x_{i+10}`.
3. That circulant has no zero Fourier eigenvalue, so `y_i = 0` for all `i`.
4. Therefore every antipodal pair has opposite colors: `x_{i+10} = -x_i`.
5. The original equations reduce to a length-`10` sign system for `a_i = x_i`.
6. The reduced system forces the pair sums `a_i + a_{i+5}` to be constant.
7. That constant must be `0`, which forces `a_{i+2} = -a_i`.
8. Period `10` then contradicts `a_{i+10} = -a_i`.
9. Therefore no CNB-coloring exists.

## chosen_plan

- Use Approach A first to force antipodal cancellation `x_{i+10} = -x_i`.
- Then use Approach B to show the reduced half-length sign pattern cannot exist.
- Do not use code in solve. The argument closes on paper and is stronger than a bounded search.
- Self-check: this stays within the reasoning-first rule and avoids unnecessary computation.

## self_checks

- Statement lock check: the exact target is the intended instance `C_20(2,3,10)`, not a family-level variant.
- Translation check: the signed CNB equation uses exactly the closed-neighborhood mask `{0, +/-2, +/-3, 10}`.
- Opposite-pair check: the length-`10` eigenvalue formula was recomputed from `2I + A^{2} + A^{-2} + A^{3} + A^{-3}` and has no zero frequency.
- Reduced-system check: on `Z/10Z`, the complement of `{i +/- 2, i +/- 3}` is exactly `{i-1, i, i+1, i+5}`.
- Contradiction check: once `c = 0`, the recurrence `a_{i+2} = -a_i` is incompatible with period `10`.
- Code decision check: no checker, search, or brute force was needed.

## code_used

- Solve stage: none.
- Reason: the handwritten reduction already gives a direct contradiction for the exact instance.

## result

Claim: the intended statement is false. `C_20(2,3,10)` is not a CNBC graph.

Candidate exact disproof:

Let `x_i in {+1, -1}` encode a red/blue coloring of the vertices `i in Z/20Z`, with `+1 = red` and `-1 = blue`. Because each closed neighborhood has size `6`, the CNB condition is equivalent to

`x_i + x_{i-2} + x_{i+2} + x_{i-3} + x_{i+3} + x_{i+10} = 0`

for every `i mod 20`.

First define `y_i = x_i + x_{i+10}` for `i mod 10`. Adding the equations for `i` and `i+10` yields

`2 y_i + y_{i-2} + y_{i+2} + y_{i-3} + y_{i+3} = 0`

for every `i mod 10`.

This is a circulant linear system. For the Fourier mode `exp(2 pi i k j / 10)`, the eigenvalue is

`lambda_k = 2 + 2 cos(4 pi k / 10) + 2 cos(6 pi k / 10)`.

Checking `k = 0, ..., 9`, the only values that occur are `6`, `2`, `1 + sqrt(5)`, and `1 - sqrt(5)`, none of which is `0`. Hence the only solution is `y_i = 0` for all `i`, so

`x_{i+10} = -x_i`

for every `i`.

Now write `a_i = x_i` for `i mod 10`. The original CNB equations reduce to

`a_{i-2} + a_{i+2} + a_{i-3} + a_{i+3} = 0`

for every `i mod 10`.

Let `T = sum_{j mod 10} a_j`. Since the four vertices `i +/- 2, i +/- 3` are exactly the complement of `{i-1, i, i+1, i+5}` in `Z/10Z`, this becomes

`a_{i-1} + a_i + a_{i+1} + a_{i+5} = T`.

Subtract the equation for `i+1` from the equation for `i`:

`a_{i-1} + a_{i+5} = a_{i+2} + a_{i+6}`.

Set `b_i = a_i + a_{i+5}`. Then `b_{i-1} = b_{i+2}` for all `i`, so on `Z/5Z` every `b_i` is the same constant `c`.

Therefore `T = sum_{i=0}^4 b_i = 5c`, and since `a_{i+5} = c - a_i`, the relation

`a_{i-1} + a_i + a_{i+1} + a_{i+5} = T`

becomes

`a_{i-1} + a_{i+1} = 4c`.

But each `a_j` is `+/-1`, so the left-hand side lies in `{-2, 0, 2}`. Also `c = a_i + a_{i+5}` lies in `{-2, 0, 2}`, so `4c` lies in `{-8, 0, 8}`. The only possible overlap is `0`, hence `c = 0`.

So `a_{i-1} + a_{i+1} = 0` for every `i`, equivalently

`a_{i+2} = -a_i`

for every `i`.

Iterating five times gives `a_{i+10} = -a_i`, but the sequence is `10`-periodic, so also `a_{i+10} = a_i`. This is impossible.

Therefore no red/blue coloring can satisfy the CNB condition on every closed neighborhood. Hence `C_20(2,3,10)` is not a CNBC graph.

Practical solve-stage classification: this is a strong exact disproof candidate, so the artifact should be treated as `COUNTEREXAMPLE` pending skeptical verification and any later Lean formalization.

## likely_failure_points

- A sign or indexing mistake in the initial CNB equation would invalidate both reductions.
- The verification pass should independently recheck the length-`10` eigenvalues for the `y_i` system.
- The complement identity on `Z/10Z` should be re-derived carefully: the four indices `i +/- 2, i +/- 3` really do complement `{i-1, i, i+1, i+5}`.
- The contradiction depends on `b_i = a_i + a_{i+5}` being constant on `Z/5Z`; verification should reproduce that step independently.
- The proof is exact-instance only; verification should confirm there was no drift to a nearby quintic circulant.

## what_verify_should_check

- Re-derive the `+/-1` CNB equations from the exact graph definition in `selected_problem.md`.
- Independently recompute the Fourier eigenvalues `lambda_k = 2 + 2 cos(4 pi k / 10) + 2 cos(6 pi k / 10)` and confirm none is zero.
- Check that `x_{i+10} = -x_i` really follows from the opposite-pair sum system.
- Re-derive the reduced `10`-term contradiction, especially the constant-pair-sum step and the forced recurrence `a_{i+2} = -a_i`.
- Optionally use a small local checker only as adversarial confirmation, not as the main proof.
- If the proof survives skeptical review, consider formalizing the finite contradiction in Lean rather than formalizing the Fourier step directly.

## verify_rediscovery

- Pass 1 result: no rediscovery established within the bounded audit.
- Bounded live-web search covered the exact instance notation `C_20(2,3,10)`, alternate tuple-style and family-style notation, the canonical 2025 CNBC source, and theorem-level checks against the source's own `Question 1` / `Theorem 16` / `Theorem 17` / `Theorem 19` discussion.
- Within that budget, I did not find any later theorem, proposition, example, observation, corollary, or citation trail settling this exact instance.
- The canonical source still appears to leave this mixed-parity quintic `n = 20` case open for the exact tuple under discussion.
- Practical conclusion for PASS 1: this run does not look like a rediscovery on current bounded evidence, so novelty remains plausible enough to continue verification.

## verify_faithfulness

- Pass 2 result: faithful.
- The intended statement in [selected_problem.md](/Users/jeremykalfus/CodingProjects/AutoMath/selected_problem.md) is the exact existential claim that `C_20(2,3,10)` admits a CNB-coloring.
- The solve record locks the same graph: vertices in `Z/20Z` with neighbors `i +/- 2`, `i +/- 3`, and `i + 10`, counting the antipodal generator `10` once.
- The proof addresses the exact closed-neighborhood balance condition, not a different balance notion and not a nearby circulant.
- Since the solver concludes nonexistence for this exact graph and this exact CNB definition, there is no wrong-theorem drift or variant drift here.

## verify_proof

- Pass 3 result: no incorrect step found.
- The `+/-1` translation is correct: because each closed neighborhood has size `6`, CNB is equivalent to the signed neighborhood sum being `0`.
- Re-adding the equations for `i` and `i + 10` does produce the `10`-variable circulant system
  `2 y_i + y_{i-2} + y_{i+2} + y_{i-3} + y_{i+3} = 0`
  for `y_i = x_i + x_{i+10}`.
- Independent recomputation of the Fourier eigenvalues gives
  `lambda_k = 2 + 2 cos(4 pi k / 10) + 2 cos(6 pi k / 10)`,
  with values `6`, `2`, `1 + sqrt(5)`, and `1 - sqrt(5)` up to repetition; none is `0`.
- Therefore the opposite-pair system has only the zero solution, so `x_{i+10} = -x_i` for every `i`.
- Substituting `a_i = x_i` on `Z/10Z` correctly reduces the CNB equations to
  `a_{i-2} + a_{i+2} + a_{i-3} + a_{i+3} = 0`.
- The complement identity in `Z/10Z` is correct: those four indices are exactly the complement of `{i-1, i, i+1, i+5}`, so the reduced equation is equivalent to
  `a_{i-1} + a_i + a_{i+1} + a_{i+5} = T`,
  where `T = sum_j a_j`.
- Subtracting consecutive equations yields `b_{i-1} = b_{i+2}` for `b_i = a_i + a_{i+5}`. Since this is a step of `3` modulo `5`, all `b_i` are equal to a constant `c`.
- The deduction `a_{i-1} + a_{i+1} = 4c` is correct, and comparing value ranges forces `c = 0`.
- Hence `a_{i+2} = -a_i` for all `i`, which iterated five times gives `a_{i+10} = -a_i`, contradicting `10`-periodicity.
- I do not see a hidden assumption, missing case, or unjustified algebraic jump in the handwritten disproof.

## verify_adversarial

- Pass 4 result: the counterexample claim resisted adversarial checks.
- No saved checker existed in [artifacts/c20-2-3-10-cnbc](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/c20-2-3-10-cnbc), so I ran independent one-off verifier computations only.
- Exhaustive enumeration over all `2^20 = 1,048,576` red/blue colorings found `0` CNB-colorings for the exact neighborhood mask `{0, +/-2, +/-3, 10}`.
- Independent exact row-reduction of the `20 x 20` CNB linear system over `Q` gave full rank `20`, which is consistent with the nonexistence claim.
- Independent recomputation of the opposite-pair eigenvalues found minimum absolute value about `1.2360679775`, so the claimed antipodal-reduction step is numerically well separated from singularity.
- These computations do not replace the proof, but they do support the exact mathematical claim being made and did not expose any counterexample or mismatch.

## verify_verdict

- `verify_verdict`: `VERIFIED`
- `classification`: `COUNTEREXAMPLE`
- `confidence`: `high`
- `lean_ready`: `true`
- Reason: the bounded rediscovery pass did not establish that the exact instance was already solved, the solve artifact matches the intended statement exactly, no incorrect proof step was found, and adversarial computation found no CNB-coloring. This is therefore a strong exact disproof candidate that is ready for Lean, but it must remain `COUNTEREXAMPLE` rather than `EXACT` until Lean completes.

## minimal_repair_if_any

- No repair was needed.
- Conservative Lean recommendation: formalize the finite contradiction after deriving `x_{i+10} = -x_i`; that keeps the proof exact and avoids unnecessary search.
