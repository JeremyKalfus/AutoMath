# Solve Record: c16-4-5-8-cnbc

## statement_lock

- Active title: `Is the quintic circulant C_16(4,5,8) a CNBC graph?`
- Locked target statement: let `G = C_16(4,5,8)` be the simple undirected graph on `Z/16Z` with edges from `i` to `i ± 4`, `i ± 5`, and `i + 8` modulo `16`. The exact claim to prove or disprove is:
  `G` admits a red/blue coloring such that every closed neighborhood `N[i] = {i, i ± 4, i ± 5, i + 8}` contains exactly three red and three blue vertices.
- Equivalent `±1` formulation: write `x_i = 1` for red and `x_i = -1` for blue. Then the CNB condition is
  `x_i + x_{i-4} + x_{i+4} + x_{i-5} + x_{i+5} + x_{i+8} = 0`
  for every `i mod 16`.
- Self-check: `8` is the antipodal generator, so it contributes one undirected edge, not two; the closed neighborhood size is `6`, and signed sum `0` is exactly the `3` red / `3` blue condition.

## definitions

- Graph convention: simple undirected graph; no loops and no multiple edges.
- Because `8 ≡ -8 (mod 16)`, the generator `8` contributes a single antipodal edge. So the graph is quintic with neighbors `i ± 4`, `i ± 5`, and `i + 8`.
- Hence each closed neighborhood has size `6`: the vertex itself plus `5` distinct neighbors.
- CNB-coloring means each closed neighborhood has equally many red and blue vertices, i.e. exactly `3` red and `3` blue here.
- I am treating this as the exact `n = 16` instance only, not as a claim about the broader family from the source.
- The only meaningful conventions to keep fixed are the modular indexing and the fact that `±4` contributes two neighbors while `8` contributes one.
- Self-check: no family-level strengthening or alternate graph convention has been introduced.

## approach_A

Structural / invariant approach via the circulant neighborhood operator.

- Let `B` be the linear operator on real `16`-periodic sequences given by
  `(Bx)_i = x_i + x_{i-4} + x_{i+4} + x_{i-5} + x_{i+5} + x_{i+8}`.
  A CNB-coloring is exactly a `±1` vector in `ker(B)`.
- Since `B` is circulant, the Fourier characters diagonalize it. For `ω = e^{2πi/16}` and `φ_k(j) = ω^(kj)`, we have
  `Bφ_k = λ_k φ_k`, where
  `λ_k = 1 + ω^(4k) + ω^(-4k) + ω^(5k) + ω^(-5k) + ω^(8k)`.
- Simplifying,
  `λ_k = 1 + 2 cos(kπ/2) + 2 cos(5kπ/8) + (-1)^k`.
- For odd `k`, the first and last terms cancel, so
  `λ_k = 2 cos(5kπ/8)`.
  Since `5k` is odd, the angle `5kπ/8` is an odd multiple of `π/8`, never a zero of cosine. Hence `λ_k ≠ 0`.
- For even `k = 2m`,
  `λ_{2m} = 2 + 2(-1)^m + 2 cos(5mπ/4)`.
  If `m` is even, then `λ_{2m} = 4 + 2 cos(5mπ/4)` and `cos(5mπ/4) ∈ {1, 0, -1, 0}`, so `λ_{2m} ∈ {6, 4, 2}`.
  If `m` is odd, then `λ_{2m} = 2 cos(5mπ/4) = ±√2`.
  So again `λ_{2m} ≠ 0`.
- Therefore `λ_k ≠ 0` for every `k = 0, 1, ..., 15`, so `B` is invertible over `R`.
- Hence `Bx = 0` has only the zero solution. In particular there is no `±1` solution, so no CNB-coloring exists.
- Self-check: this route proves something stronger than mere nonexistence of a coloring; it proves the closed-neighborhood linear system has trivial real kernel.

## approach_B

Construction / contradiction approach by testing the two most natural balanced ansätze.

- First try a `4`-periodic quotient coloring `x_i = a_{i mod 4}`. Then the CNB equation at residue class `r` becomes
  `4a_r + a_{r+1} + a_{r-1} = 0`.
  But `a_r ∈ {±1}`, so the left-hand side is always in `{±2, ±6}`, never `0`. Thus no residue-class-constant coloring works.
- Next try the strongest antipodal balancing ansatz `x_{i+8} = -x_i`. Then
  `x_{i-4} = -x_{i+4}` and `x_{i-5} = -x_{i+3}`,
  so the CNB equation collapses to
  `x_{i+5} - x_{i+3} = 0`,
  i.e. `x_{i+2} = x_i` for every `i`.
- But `x_{i+2} = x_i` implies `x_{i+8} = x_i`, contradicting the antipodal condition `x_{i+8} = -x_i`.
- So the two most obvious balanced constructions both fail, which points toward nonexistence rather than existence.
- Self-check: Approach B is only an obstruction heuristic; it does not by itself rule out all colorings, so it should not be used as the final proof.

## lemma_graph

1. A CNB-coloring is equivalent to a `±1` solution of `Bx = 0` for the circulant operator with mask `{0, ±4, ±5, 8}`.
2. Fourier characters of `Z/16Z` diagonalize `B`.
3. The corresponding eigenvalues are `λ_k = 1 + 2 cos(kπ/2) + 2 cos(5kπ/8) + (-1)^k`.
4. Every eigenvalue `λ_k` is nonzero by the odd/even case split.
5. Therefore `ker(B) = {0}` over `R`.
6. Hence no `±1` coloring vector exists, so `C_16(4,5,8)` is not CNBC.

## chosen_plan

- Use Approach A as the main proof, because the graph is circulant and the signed closed-neighborhood equations are exactly a small circulant linear system.
- Keep Approach B only as a sanity check that the natural quotient and antipodal constructions do not produce a witness.
- Do not use code in solve: the nonexistence proof is closed-form and finite as written.
- Self-check: this respects the reasoning-first rule and the minimal-code rule.

## self_checks

- Statement lock check: the target remains the exact intended statement "`C_16(4,5,8)` is a CNBC graph", now attacked as a disproof attempt for that exact instance.
- Definition check: the neighborhood mask is `{0, ±4, ±5, 8}` and the closed-neighborhood size is `6`.
- Structural check: the Fourier eigenvalue formula matches the mask term-by-term.
- Nonvanishing check: the odd `k` and even `k = 2m` cases both leave no zero eigenvalue.
- Conservatism check: the classification below is `COUNTEREXAMPLE`, not `EXACT`, because Lean is still off in solve.
- Workflow check: no code was used.

## code_used

- Solve stage: none.
- No checker or search was needed because the handwritten invertibility argument already certifies nonexistence.

## result

Claim: the intended statement is false. `C_16(4,5,8)` is not a CNBC graph.

Candidate exact disproof:

Let `x_i ∈ {±1}` encode a red/blue coloring of the vertices `i ∈ Z/16Z`, with `1 = red` and `-1 = blue`. Because every closed neighborhood has size `6`, the CNB condition is equivalent to

`x_i + x_{i-4} + x_{i+4} + x_{i-5} + x_{i+5} + x_{i+8} = 0`

for every `i mod 16`.

Define the circulant linear operator `B` by the left-hand side. On the Fourier character `φ_k(j) = ω^(kj)` with `ω = e^(2πi/16)`, we have

`Bφ_k = λ_k φ_k`

with

`λ_k = 1 + ω^(4k) + ω^(-4k) + ω^(5k) + ω^(-5k) + ω^(8k)`
`    = 1 + 2 cos(kπ/2) + 2 cos(5kπ/8) + (-1)^k`.

Now check that `λ_k` never vanishes.

- If `k` is odd, then `1 + (-1)^k = 0`, so
  `λ_k = 2 cos(5kπ/8)`.
  Here `5k` is odd, so `5kπ/8` is an odd multiple of `π/8`, and cosine is nonzero at every odd multiple of `π/8`. Hence `λ_k ≠ 0`.
- If `k = 2m` is even, then
  `λ_{2m} = 2 + 2(-1)^m + 2 cos(5mπ/4)`.
  If `m` is even, this is `4 + 2 cos(5mπ/4)`, which belongs to `{6, 4, 2}`.
  If `m` is odd, this is `2 cos(5mπ/4) = ±√2`.
  So again `λ_{2m} ≠ 0`.

Therefore `λ_k ≠ 0` for all `k`, so the circulant operator `B` is invertible. Hence the linear system `Bx = 0` has only the zero real solution.

But a red/blue coloring vector has every coordinate in `{±1}`, so it is nonzero. This contradiction shows that no CNB-coloring exists.

Therefore `C_16(4,5,8)` does not admit a closed-neighborhood balanced coloring. Equivalently, it is not a CNBC graph.

Practical solve-stage classification: this is a strong exact disproof candidate, so the artifact should be treated as `COUNTEREXAMPLE` pending verification and any later Lean formalization.

## likely_failure_points

- A sign or indexing error in the circulant mask would change the eigenvalue formula.
- The verification pass should recheck carefully that the generator `8` contributes one antipodal edge, while `±4` and `±5` each contribute two distinct neighbors.
- The odd/even case split for the eigenvalues is simple but easy to miscopy; verification should recompute it independently.
- The proof shows impossibility over all real color vectors satisfying the linear equations, which is stronger than needed; verification should confirm that no hidden convention change weakens the translation from CNB-coloring to `Bx = 0`.

## what_verify_should_check

- Re-derive the `±1` CNB equations from the exact graph definition in `selected_problem.md`.
- Recompute the eigenvalues of the circulant operator independently and confirm that none is zero.
- Confirm that the argument proves nonexistence for the exact intended instance `C_16(4,5,8)`, not for a nearby variant.
- As an adversarial sanity check only, optionally enumerate all `2^16` colorings and confirm that none satisfies all `16` closed-neighborhood equations.
- If the proof survives skeptical checking, decide whether the direct linear-algebra nonexistence proof is simple enough to formalize in Lean.

## verify_rediscovery

- Pass 1 result: no rediscovery found within the bounded audit.
- Limited web checks covered the exact instance notation `C_16(4,5,8)`, alternate circulant wording, the canonical 2025 source, and theorem/question checks inside that same source.
- The canonical source still treats the `n ≡ 0 (mod 8)` quintic circulants with `d_1 ≡ 0 (mod 4)` and `d_2` odd as open, and the selected instance is presented as lying outside the stated sufficient-condition theorems.
- I did not find a later paper, theorem, proposition, example, observation, or explicit exact-instance exhibit settling `C_16(4,5,8)` during the bounded pass.
- So this run does not look like a `REDISCOVERY`.
- Short proof-status note: independently of novelty, the current nonexistence proof also appears mathematically sound after the later passes below.

## verify_faithfulness

- Pass 2 result: faithful.
- The intended statement in `selected_problem.md` is the exact existence claim that `C_16(4,5,8)` is a CNBC graph.
- The solve record attacks exactly that statement and does not drift to a different family-level theorem, a different notion of balanced coloring, or a different graph convention.
- The graph data remain consistent throughout: vertices in `Z/16Z`, neighbors `i ± 4`, `i ± 5`, and `i + 8`, with the antipodal generator `8` counted once, so each closed neighborhood has size `6`.
- The proof therefore establishes the negation of the exact intended statement for this exact instance, not a weaker proxy and not a nearby `VARIANT`.

## verify_proof

- Pass 3 result: no incorrect step found.
- Re-deriving the CNB equations gives the same signed system
  `x_i + x_{i-4} + x_{i+4} + x_{i-5} + x_{i+5} + x_{i+8} = 0`
  for every `i mod 16`, which is exactly the closed-neighborhood balance condition for a `6`-vertex neighborhood.
- The circulant/Fourier setup is correct for the mask `{0, ±4, ±5, 8}`.
- Independent recomputation gives
  `λ_k = 1 + 2 cos(kπ/2) + 2 cos(5kπ/8) + (-1)^k`.
- For odd `k`, this simplifies to `λ_k = 2 cos(5kπ/8)`, which is nonzero because `5k` is odd and cosine is nonzero at every odd multiple of `π/8`.
- For even `k = 2m`, this simplifies to
  `λ_{2m} = 2 + 2(-1)^m + 2 cos(5mπ/4)`;
  if `m` is even this is one of `{6, 4, 2}`, and if `m` is odd this is `±√2`.
- Numerical recomputation of all `16` eigenvalues gives minimum absolute value about `0.7653668647`, so none vanishes.
- Hence the closed-neighborhood operator has trivial real kernel. Since a red/blue coloring vector lies in `{±1}^{16}` and is therefore nonzero, no CNB-coloring can exist.
- I did not find a hidden assumption, missing case, or unjustified leap in the proof.

## verify_adversarial

- Pass 4 result: the claimed disproof resisted adversarial checks.
- I ran an independent local checker for the exact graph definition and confirmed that every closed neighborhood has size `6`, as required by the argument.
- I also exhaustively enumerated all `2^16 = 65536` red/blue colorings. None satisfies all `16` CNB equations.
- A separate exact Gaussian-elimination check on the `16 × 16` coefficient matrix gives full rank `16`, matching the Fourier invertibility claim.
- These computations do not replace the proof, but they are consistent with it and provide no counterexample to the claimed nonexistence result.

## verify_verdict

- `verify_verdict`: `VERIFIED`
- `classification`: `COUNTEREXAMPLE`
- `confidence`: `high`
- `lean_ready`: `true`
- Reason: the exact intended statement now looks correctly disproved for the frontier instance `C_16(4,5,8)`, no rediscovery was established in the bounded prior-art pass, and the remaining gate is Lean formalization rather than further mathematical repair.

## minimal_repair_if_any

- No repair was needed.
- Conservative Lean-facing simplification only: formalizing matrix invertibility or the finite linear system may be cleaner than formalizing the full Fourier discussion verbatim.
