# Solve Record: c24-4-5-12-cnbc

## statement_lock

- Active title: `Is the quintic circulant C_24(4,5,12) a CNBC graph?`
- Locked target statement: let `G = C_24(4,5,12)` be the simple undirected graph on `Z/24Z` with edges from `i` to `i +/- 4`, `i +/- 5`, and `i + 12` modulo `24`. The exact claim to prove or disprove is:
  `G` admits a red/blue coloring such that every closed neighborhood `N[i] = {i, i +/- 4, i +/- 5, i + 12}` contains exactly three red and three blue vertices.
- Equivalent `+/-1` formulation: write `x_i = 1` for red and `x_i = -1` for blue. Then the CNB condition is
  `x_i + x_{i-4} + x_{i+4} + x_{i-5} + x_{i+5} + x_{i+12} = 0`
  for every `i mod 24`.
- Self-check: `12 == -12 (mod 24)`, so it contributes one antipodal neighbor, not two. The graph is quintic, each closed neighborhood has size `6`, and signed sum `0` is exactly the `3` red / `3` blue condition.

## definitions

- Graph convention: simple undirected graph on `Z/24Z`; no loops and no multiple edges.
- The neighbors of `i` are exactly `i +/- 4`, `i +/- 5`, and `i + 12`.
- Because `12` is antipodal, it contributes one neighbor, while `+/-4` and `+/-5` contribute four more distinct neighbors. So each closed neighborhood has size `6`.
- A CNB-coloring means equal red and blue counts in each closed neighborhood, hence exactly `3` red and `3` blue vertices here.
- Ambiguities to lock:
  - indexing is always modulo `24`;
  - this is only the exact instance `C_24(4,5,12)`, not a family-level claim;
  - the signed linear system is over the real numbers, but a valid coloring additionally requires every coordinate to lie in `{+1,-1}`.
- Self-check: no alternate graph convention or weaker balance notion has been introduced.

## approach_A

Structural / invariant approach via the circulant closed-neighborhood operator.

- Let `B` be the linear operator on real `24`-periodic sequences defined by
  `(Bx)_i = x_i + x_{i-4} + x_{i+4} + x_{i-5} + x_{i+5} + x_{i+12}`.
  A CNB-coloring is exactly a `{+1,-1}` vector in `ker(B)`.
- Since `B` is circulant, the Fourier characters `phi_k(j) = omega^(kj)` with `omega = exp(2 pi i / 24)` diagonalize it:
  `B phi_k = lambda_k phi_k`, where
  `lambda_k = 1 + omega^(4k) + omega^(-4k) + omega^(5k) + omega^(-5k) + omega^(12k)`.
- Simplifying,
  `lambda_k = 1 + 2 cos(k pi / 3) + 2 cos(5 k pi / 12) + (-1)^k`.
- For odd `k`, the first and last terms cancel, so
  `lambda_k = 2 cos(k pi / 3) + 2 cos(5 k pi / 12)`.
  Using `cos A + cos B = 2 cos((A+B)/2) cos((A-B)/2)`, this becomes
  `lambda_k = 4 cos(3 k pi / 8) cos(k pi / 24)`.
  Here `cos(k pi / 24) != 0` for odd `k`, and `cos(3 k pi / 8) = 0` would force `3k = 4 + 8m`, hence `k == 4 (mod 8)`, impossible for odd `k`. So no odd frequency lies in the kernel.
- For even `k = 2m`, we get
  `lambda_(2m) = 2 + 2 cos(2 m pi / 3) + 2 cos(5 m pi / 6)`.
  Checking the finite set `m = 0,1,...,11` gives
  `6, 1 - sqrt(3), 2, 4, 0, 1 + sqrt(3), 2, 1 + sqrt(3), 0, 4, 2, 1 - sqrt(3)`.
  Hence the only zero eigenvalues occur at `k = 8` and `k = 16`.
- Therefore every real solution of `Bx = 0` lies in the real span of `phi_8` and `phi_16`.
- But `phi_8(j) = exp(2 pi i j / 3)` and `phi_16(j) = exp(4 pi i j / 3)`, so every such solution satisfies
  `x_i + x_{i+1} + x_{i+2} = 0`
  for every `i`, because `1 + z + z^2 = 0` for each primitive cube root `z`.
- Subtracting the equation at `i+1` from the equation at `i` gives `x_{i+3} = x_i`, so every real solution is `3`-periodic and its three residue-class values sum to `0`.
- A `{+1,-1}`-valued `3`-periodic sequence would have three class values `a,b,c in {+1,-1}` with `a + b + c = 0`, which is impossible.
- Hence no CNB-coloring exists.
- Self-check: the proof uses the exact mask `{0, +/-4, +/-5, 12}` and only exact trigonometric values at the `24` discrete Fourier frequencies.

## approach_B

Construction / extremal / contradiction approach guided by the visible `mod 3` structure.

- The jumps satisfy `4 == 1 (mod 3)`, `5 == -1 (mod 3)`, and `12 == 0 (mod 3)`.
- So the most natural witness shape is a coloring constant on residue classes modulo `3`: `x_i = a_(i mod 3)`.
- Under that ansatz, the CNB equation at any vertex becomes
  `2 a_r + 2 a_(r+1) + 2 a_(r-1) = 0`,
  hence
  `a_0 + a_1 + a_2 = 0`.
- But `a_0, a_1, a_2` would each lie in `{+1,-1}`, and three signs cannot sum to `0`.
- So the most obvious period-`3` construction fails immediately.
- This is not by itself a complete disproof, because a priori a CNB-coloring need not be residue-class constant modulo `3`. Its value is that it matches the kernel shape later forced by Approach A.
- Self-check: this route is only a sanity-check obstruction, not the final proof.

## lemma_graph

1. A CNB-coloring is equivalent to a `{+1,-1}` solution of `Bx = 0` for the circulant operator with mask `{0, +/-4, +/-5, 12}`.
2. Fourier characters of `Z/24Z` diagonalize `B`.
3. The eigenvalues are `lambda_k = 1 + 2 cos(k pi / 3) + 2 cos(5 k pi / 12) + (-1)^k`.
4. These eigenvalues vanish only for `k = 8` and `k = 16`.
5. Therefore `ker(B)` is the real span of the primitive cube-root modes.
6. Every real solution of `Bx = 0` satisfies `x_i + x_{i+1} + x_{i+2} = 0`, hence also `x_{i+3} = x_i`.
7. No `3`-periodic `{+1,-1}` sequence can have `a + b + c = 0`.
8. Therefore no CNB-coloring exists for `C_24(4,5,12)`.

## chosen_plan

- Use Approach A as the main proof, because the exact graph is circulant and the Fourier spectrum is small enough to determine the full real kernel explicitly.
- Keep Approach B as a sanity check showing that the only natural period-`3` construction already fails at the sign level.
- Do not use code in solve. The argument closes on paper once the two zero frequencies are identified.
- Self-check: this stays within the reasoning-first and minimal-code rules.

## self_checks

- Statement-lock check: the target stayed the exact intended statement "`C_24(4,5,12)` is a CNBC graph", now attacked as a disproof.
- Translation check: the signed CNB equation uses exactly the neighborhood mask `{0, +/-4, +/-5, 12}`.
- Spectral check: the odd-frequency factorization and the even-frequency table agree that the only kernel frequencies are `8` and `16`.
- Kernel-shape check: the `k = 8,16` modes are exactly the primitive cube-root modes, so `x_i + x_{i+1} + x_{i+2} = 0` is the right recurrence.
- Sign check: three values in `{+1,-1}` cannot sum to `0`, so the final contradiction is exact.
- Code decision check: no checker, search, or brute force was needed.

## code_used

- Solve stage: none.
- Reason: the handwritten kernel-structure argument already gives a direct contradiction for the exact instance.

## result

Claim: the intended statement is false. `C_24(4,5,12)` is not a CNBC graph.

Candidate exact disproof:

Let `x_i in {+1,-1}` encode a red/blue coloring of the vertices `i in Z/24Z`, with `+1 = red` and `-1 = blue`. Since every closed neighborhood has size `6`, the CNB condition is equivalent to

`x_i + x_{i-4} + x_{i+4} + x_{i-5} + x_{i+5} + x_{i+12} = 0`

for every `i mod 24`.

Define the circulant linear operator `B` by the left-hand side. For the Fourier character `phi_k(j) = omega^(kj)` with `omega = exp(2 pi i / 24)`, we have

`B phi_k = lambda_k phi_k`

with

`lambda_k = 1 + omega^(4k) + omega^(-4k) + omega^(5k) + omega^(-5k) + omega^(12k)`
`         = 1 + 2 cos(k pi / 3) + 2 cos(5 k pi / 12) + (-1)^k`.

We now determine exactly when `lambda_k = 0`.

If `k` is odd, then `1 + (-1)^k = 0`, so

`lambda_k = 2 cos(k pi / 3) + 2 cos(5 k pi / 12)`
`         = 4 cos(3 k pi / 8) cos(k pi / 24)`.

For odd `k`, the factor `cos(k pi / 24)` is nonzero. Also `cos(3 k pi / 8) = 0` would mean

`3 k pi / 8 = pi / 2 + m pi`,

so `3k = 4 + 8m`, hence `k == 4 (mod 8)`, impossible for odd `k`. Therefore `lambda_k != 0` for every odd `k`.

If `k = 2m` is even, then

`lambda_(2m) = 2 + 2 cos(2 m pi / 3) + 2 cos(5 m pi / 6)`.

For the finite list `m = 0,1,...,11`, these values are exactly

`6, 1 - sqrt(3), 2, 4, 0, 1 + sqrt(3), 2, 1 + sqrt(3), 0, 4, 2, 1 - sqrt(3)`.

Hence the only zero eigenvalues occur for `m = 4` and `m = 8`, i.e. for `k = 8` and `k = 16`.

So every real solution of `Bx = 0` lies in the real span of `phi_8` and `phi_16`. But these are the two primitive cube-root modes:

`phi_8(j) = exp(2 pi i j / 3)`, `phi_16(j) = exp(4 pi i j / 3)`.

For either mode `z^j` with `z^3 = 1` and `z != 1`, we have

`z^i + z^(i+1) + z^(i+2) = z^i (1 + z + z^2) = 0`.

Therefore every real solution of `Bx = 0` satisfies

`x_i + x_{i+1} + x_{i+2} = 0`

for every `i`.

Now compare the equations for `i` and `i+1`:

`x_i + x_{i+1} + x_{i+2} = 0`,
`x_{i+1} + x_{i+2} + x_{i+3} = 0`.

Subtracting gives `x_{i+3} = x_i`. So any real solution is `3`-periodic. Writing its three residue-class values as `a,b,c`, the recurrence gives

`a + b + c = 0`.

But a coloring requires `a,b,c in {+1,-1}`, and no three signs sum to `0`.

This contradiction shows that no red/blue coloring can satisfy the CNB condition on every closed neighborhood. Therefore `C_24(4,5,12)` is not a CNBC graph.

Practical solve-stage classification: this is a strong exact disproof candidate, so the artifact should be treated as `COUNTEREXAMPLE` pending skeptical verification and any later Lean formalization.

## likely_failure_points

- A sign or indexing error in the exact neighborhood mask would change the Fourier symbol.
- The verification pass should independently recheck the odd-frequency factorization and the even-frequency zero set.
- The step from kernel support `{8,16}` to the recurrence `x_i + x_{i+1} + x_{i+2} = 0` should be recomputed independently.
- The final contradiction uses the fact that every solution is `3`-periodic and then compares only the three residue-class values; verification should confirm that no hidden convention weakens that reduction.

## what_verify_should_check

- Re-derive the `+/-1` CNB equations from the exact graph definition in `selected_problem.md`.
- Recompute the eigenvalues `lambda_k = 1 + 2 cos(k pi / 3) + 2 cos(5 k pi / 12) + (-1)^k` independently and confirm that only `k = 8,16` give zero.
- Recheck that the `k = 8,16` Fourier modes are exactly the primitive cube-root modes and force `x_i + x_{i+1} + x_{i+2} = 0`.
- Confirm that `x_i + x_{i+1} + x_{i+2} = 0` implies `x_{i+3} = x_i`, so only `3`-periodic candidates remain.
- As an adversarial sanity check only, either compute the exact matrix rank or check the `8` possible `3`-periodic sign patterns directly.
- If the proof survives skeptical review, consider Lean formalizing the finite kernel-structure argument rather than any search.

## verify_rediscovery

- PASS 1 used a bounded live web audit focused on the exact instance notation, alternate notation, the canonical 2025 source, and same-source theorem checks.
- No rediscovery was established within budget. The exact tuple `C_24(4,5,12)` still points back to the canonical paper rather than to a later exact-instance settlement, and the paper still appears to leave this `n == 0 (mod 8)` mixed-parity case in its open-question regime rather than resolving it by Theorem 16, 17, or 19.
- I did not find a theorem, proposition, example, observation, or corollary in the same source or a later exact-instance citation that already settles the exact statement "`C_24(4,5,12)` is or is not a CNBC graph."
- Rediscovery verdict for PASS 1: not established.

## verify_faithfulness

- The solve artifact stayed locked to the exact intended statement. The target in `selected_problem.md` is the yes/no CNBC status of the single graph `C_24(4,5,12)`, and the proof attacks exactly that statement by deriving nonexistence of a red/blue coloring with balanced closed neighborhoods.
- The signed equation
  `x_i + x_{i-4} + x_{i+4} + x_{i-5} + x_{i+5} + x_{i+12} = 0`
  matches the exact graph definition. A local recheck gives `N[0] = {0,4,5,12,19,20}`, so the graph is indeed quintic and each closed neighborhood has size `6`.
- There is no theorem drift, quantifier drift, or definition change. The artifact proves a disproof of the intended CNBC claim, not a weaker proxy statement.

## verify_proof

- I found no incorrect step.
- The Fourier symbol was recomputed independently from the exact mask and agrees with
  `lambda_k = 1 + 2 cos(k pi / 3) + 2 cos(5 k pi / 12) + (-1)^k`.
- A direct recomputation over all `24` frequencies shows that the only zero eigenvalues are at `k = 8` and `k = 16`. A separate exact rational row-reduction on the `24 x 24` CNB matrix gives rank `22`, so the real solution space has dimension `2`, exactly matching those two Fourier modes.
- The modes `k = 8,16` are the primitive cube-root modes, so every real kernel vector satisfies `x_i + x_{i+1} + x_{i+2} = 0`. Subtracting consecutive instances of that relation gives `x_{i+3} = x_i`, so every real solution is `3`-periodic.
- For a `{+1,-1}` coloring, `3`-periodicity leaves only residue-class values `a,b,c in {+1,-1}` with `a + b + c = 0`, which is impossible. This closes the disproof exactly.

## verify_adversarial

- I reran a local checker on the exact graph mask. Every closed neighborhood has size `6`, confirming the signed-balance translation.
- I checked all `8` possible `3`-periodic sign patterns directly; none satisfies the CNB equations.
- I also reran an independent matrix computation, which gave rank `22` and nullity `2`, consistent with the spectral argument and inconsistent with any hidden larger solution space.
- No candidate construction survives these checks.

## verify_verdict

- `VERIFIED`.
- Classification remains `COUNTEREXAMPLE`, not `EXACT`, because this is a non-Lean verified exact disproof candidate of the intended statement and no rediscovery was established.
- `lean_ready = true` because the exact instance appears frontier-novel within the bounded audit and the proof survived skeptical checking without needing substantive repair.

## minimal_repair_if_any

- None. No conservative proof patch was needed.
