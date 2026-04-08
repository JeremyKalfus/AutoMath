# Solve Record: c12-1-3-6-cnbc

## statement_lock

- Active title: `Is the quintic circulant C_12(1,3,6) a CNBC graph?`
- Locked target statement: let `G = C_12(1,3,6)` be the simple undirected graph on `Z/12Z` with edges from `i` to `i ± 1`, `i ± 3`, and `i + 6` modulo `12`. The exact claim to prove or disprove is:
  `G` admits a red/blue coloring such that every closed neighborhood `N[i] = {i, i ± 1, i ± 3, i + 6}` contains exactly three red and three blue vertices.
- I am treating this as an existence question for this exact `n = 12` instance only, not for the whole family mentioned in the source.
- Equivalent `±1` formulation: write `x_i = 1` for red and `x_i = -1` for blue. Then the CNB condition is
  `x_{i-3} + x_{i-1} + x_i + x_{i+1} + x_{i+3} + x_{i+6} = 0`
  for every `i mod 12`.

## definitions

- Graph convention: simple undirected graph; no loops and no multiple edges.
- Because `6 ≡ -6 (mod 12)`, the `n/2` generator contributes one antipodal edge, not two distinct edges. So the graph is indeed quintic: neighbors of `i` are `i ± 1`, `i ± 3`, and `i + 6`.
- Hence each closed neighborhood has size `6`: the vertex itself plus `5` distinct neighbors.
- CNB-coloring means exactly half of each closed neighborhood is red and half is blue. Since `|N[i]| = 6`, this means exactly `3` red and `3` blue.
- Ambiguity to keep in mind for verification: the source appears to leave open a family-level regime, and this exact instance is extracted from that regime rather than named verbatim.

## approach_A

Structural / invariant approach via the circulant neighborhood operator.

- Let `B` be the linear operator on real `12`-periodic sequences given by
  `(Bx)_i = x_{i-3} + x_{i-1} + x_i + x_{i+1} + x_{i+3} + x_{i+6}`.
  A CNB-coloring is exactly a `±1` vector in `ker(B)`.
- Since `B` is circulant, the Fourier basis diagonalizes it. For `ω = e^(2πi/12)` and `φ_k(j) = ω^(kj)`, we have
  `Bφ_k = λ_k φ_k`, where
  `λ_k = 1 + ω^k + ω^(-k) + ω^(3k) + ω^(-3k) + ω^(6k)`.
- Using `ω^k + ω^(-k) = 2 cos(kπ/6)`, `ω^(3k) + ω^(-3k) = 2 cos(kπ/2)`, and `ω^(6k) = (-1)^k`,
  `λ_k = 1 + 2 cos(kπ/6) + 2 cos(kπ/2) + (-1)^k`.
- For `k = 0,1,2,3,4,5,6`, this gives
  `6, sqrt(3), 1, 0, 3, -sqrt(3), -2`,
  and `λ_{12-k} = λ_k`, so the only zeros are `k = 3` and `k = 9`.
- Therefore `ker(B)` is exactly the real span of the `k = 3, 9` modes, namely
  `u_j = cos(jπ/2) = (1,0,-1,0,...)`
  and
  `v_j = sin(jπ/2) = (0,1,0,-1,...)`.
- So every real solution of the CNB equations has the form
  `x_j = a cos(jπ/2) + b sin(jπ/2)`,
  i.e.
  `(x_0,...,x_11) = (a,b,-a,-b,a,b,-a,-b,a,b,-a,-b)`.
- If the solution is a genuine coloring, every coordinate must be `±1`, so necessarily `a,b ∈ {±1}`.
- This not only suggests existence; it classifies all possible CNB-colorings up to rotation / color swap.

## approach_B

Construction / extremal / contradiction approach by forcing a short periodic pattern.

- Try a `4`-periodic ansatz with `x_{i+2} = -x_i`. Then automatically `x_{i+4} = x_i`.
- Under this ansatz:
  `x_{i+6} = x_{i+2} = -x_i`,
  `x_{i+1} = -x_{i-1}`,
  and, because of period `4`,
  `x_{i-3} = x_{i+1}` and `x_{i+3} = x_{i-1}`.
- Hence for every `i`,
  `x_i + x_{i+6} = 0`,
  `x_{i-1} + x_{i+1} = 0`,
  and
  `x_{i-3} + x_{i+3} = x_{i+1} + x_{i-1} = 0`.
  So the whole closed-neighborhood sum is `0`.
- Therefore any repeated pattern `(a,b,-a,-b)` with `a,b ∈ {±1}` is automatically a CNB-coloring.
- This gives an explicit witness immediately, while Approach A explains why this pattern is not a lucky guess but the entire solution space.

## lemma_graph

1. CNB-colorings are exactly `±1` solutions to the closed-neighborhood equations.
2. Those equations are given by a circulant operator `B`.
3. Fourier modes diagonalize `B`, and the only zero eigenvalues occur at frequencies `3` and `9`.
4. Therefore every real solution is `4`-periodic of the form `(a,b,-a,-b)` repeated three times.
5. Choosing `a,b ∈ {±1}` yields actual red/blue colorings.
6. In particular `(1,1,-1,-1)` repeated is a witness, so `C_12(1,3,6)` is CNBC.

## chosen_plan

- Use Approach A as the main proof because it gives a clean necessity statement, avoids search, and matches the circulant symmetry of the problem.
- Use Approach B to make the existence part concrete and easy to verify locally.
- Do not use code unless the Fourier computation or the witness check develops a gap. At the moment the argument is closed-form and finite.

## self_checks

- Statement lock check: `+6` was counted once, not twice; degree `5` and closed-neighborhood size `6` are consistent.
- Definition check: the solve target is the exact `n = 12` instance, not an unproved family-level generalization.
- Approach A check: the eigenvalue formula was derived directly from the neighborhood mask and simplified to a cosine expression; the only zeros are at `k = 3, 9`.
- Approach B check: the local cancellation identities were rechecked carefully with the `4`-periodic rule `x_{i+2} = -x_i`.
- Final check: the proof establishes actual existence of a CNB-coloring, not merely a promising heuristic.
- Workflow check: no code was needed after the reasoning stage.

## code_used

- Solve stage: none.
- Verify stage: a tiny one-off local checker was used to confirm the explicit witness on all `12` closed neighborhoods and to enumerate all `2^12` colorings as an adversarial sanity check.

## result

Claim: the intended statement is true. `C_12(1,3,6)` is a CNBC graph.

Candidate exact proof:

Let `x_i ∈ {±1}` encode a red/blue coloring of the vertices `i ∈ Z/12Z`, with `1 = red` and `-1 = blue`. The CNB condition is exactly

`x_{i-3} + x_{i-1} + x_i + x_{i+1} + x_{i+3} + x_{i+6} = 0`

for every `i`.

Consider the circulant operator `B` defined by the left-hand side. On the Fourier basis `φ_k(j) = ω^(kj)` with `ω = e^(2πi/12)`, its eigenvalues are

`λ_k = 1 + ω^k + ω^(-k) + ω^(3k) + ω^(-3k) + ω^(6k)`
`    = 1 + 2 cos(kπ/6) + 2 cos(kπ/2) + (-1)^k`.

Direct evaluation shows

- `λ_0 = 6`
- `λ_1 = sqrt(3)`
- `λ_2 = 1`
- `λ_3 = 0`
- `λ_4 = 3`
- `λ_5 = -sqrt(3)`
- `λ_6 = -2`

and by symmetry `λ_{12-k} = λ_k`. So `ker(B)` is exactly the real span of the `k = 3` and `k = 9` modes. Equivalently, every real solution has the form

`(x_0,...,x_11) = (a,b,-a,-b,a,b,-a,-b,a,b,-a,-b)`.

To get an actual red/blue coloring, each coordinate must be `±1`, so choose `a = b = 1`. This gives the explicit coloring

`(x_0,...,x_11) = (1,1,-1,-1,1,1,-1,-1,1,1,-1,-1)`,

so the red vertices are `{0,1,4,5,8,9}` and the blue vertices are `{2,3,6,7,10,11}`.

For this pattern we have, for every `i`,

- `x_{i+6} = x_{i+2} = -x_i`
- `x_{i+1} = -x_{i-1}`
- `x_{i-3} = x_{i+1}` and `x_{i+3} = x_{i-1}`

therefore

`(x_i + x_{i+6}) + (x_{i-1} + x_{i+1}) + (x_{i-3} + x_{i+3}) = 0`.

So the closed-neighborhood sum is `0` at every vertex, which means each closed neighborhood contains exactly three red and three blue vertices.

Therefore `C_12(1,3,6)` admits a CNB-coloring. So the graph is CNBC.

## likely_failure_points

- A sign/indexing mistake in the Fourier convention could invalidate the kernel computation, so verification should recompute the eigenvalues independently.
- The graph definition must continue to treat the `6`-step edge as a single undirected edge, not as two distinct generators.
- The instance-to-family extraction in the source should be checked so that the intended statement matches the selected problem exactly.
- If formalization is attempted later, the cleanest route may be direct verification of the explicit witness rather than a full Fourier-development in Lean.

## what_verify_should_check

- Re-derive the CNB equation in `±1` form from the closed-neighborhood definition.
- Recompute the circulant eigenvalues `λ_k` and confirm that only `k = 3, 9` give zero.
- Confirm that the explicit coloring `(1,1,-1,-1)` repeated three times really satisfies every neighborhood equation.
- Check whether all CNB-colorings are indeed exhausted by the `4`-periodic family `(a,b,-a,-b)`.
- Check that the solver has proved the exact intended statement and not a nearby variant.

## verify_faithfulness

- Pass 2 result: faithful.
- The intended statement in [selected_problem.md] is the exact existence claim "`C_12(1,3,6)` is a CNBC graph."
- The solve record keeps that statement locked as the `n = 12` instance only and does not drift to the broader family-level open regime from the source.
- The graph definition is unchanged: vertices in `Z/12Z`, neighbors `i ± 1`, `i ± 3`, and `i + 6`, with the antipodal `+6` edge counted once. That matches the selected problem exactly.
- The solver proves existence of a CNB-coloring for this exact graph, not a weaker proxy such as a balanced open-neighborhood coloring or a coloring of a different circulant.
- On faithfulness grounds, this is the exact intended statement rather than a nearby `VARIANT`.

## verify_proof

- Pass 3 result: no incorrect step found.
- Re-derivation of the `±1` formulation is correct: for a closed neighborhood of size `6`, having exactly three red and three blue vertices is equivalent to the signed sum over that neighborhood being `0`.
- The circulant operator is set up correctly with mask `{0, ±1, ±3, 6}`.
- The Fourier eigenvalue formula
  `λ_k = 1 + ω^k + ω^(-k) + ω^(3k) + ω^(-3k) + ω^(6k)`
  and simplification
  `λ_k = 1 + 2 cos(kπ/6) + 2 cos(kπ/2) + (-1)^k`
  are correct.
- Independent recomputation gives `λ_0 = 6`, `λ_1 = sqrt(3)`, `λ_2 = 1`, `λ_3 = 0`, `λ_4 = 3`, `λ_5 = -sqrt(3)`, `λ_6 = -2`, and hence zeros only at `k = 3, 9`.
- Therefore `ker(B)` is the real span of the `4`-periodic modes `(1,0,-1,0,...)` and `(0,1,0,-1,...)`, so every real solution has the form `(a,b,-a,-b)` repeated.
- For an actual coloring, the coordinates themselves are `x_0 = a`, `x_1 = b`, `x_2 = -a`, `x_3 = -b`, so requiring every coordinate to lie in `{±1}` indeed forces `a,b ∈ {±1}`.
- The explicit witness `(1,1,-1,-1)` repeated then proves the intended existence claim.
- The proof is stronger than necessary because the witness alone suffices, but the extra classification argument is correct as written.

## verify_adversarial

- Pass 4 result: the candidate construction resisted adversarial checks.
- There was no existing checker file in the artifact directory, so I ran an independent one-off local computation as a verifier check only.
- The explicit witness `(1,1,-1,-1,1,1,-1,-1,1,1,-1,-1)` was checked against all `12` closed neighborhoods, and every neighborhood sum was `0`.
- I also exhaustively enumerated all `2^12 = 4096` red/blue colorings. Exactly `4` satisfy the CNB equations, namely the four choices of `(a,b,-a,-b)` with `a,b ∈ {±1}`.
- This computation does not replace the proof, but it confirms that the witness is genuine and that the claimed `4`-periodic family is complete.
- No counterexample to the claimed theorem or to the proposed witness was found.

## verify_verdict

- `verify_verdict`: `REDISCOVERY`
- `classification`: `REDISCOVERY`
- `confidence`: `high`
- `lean_ready`: `false`
- Reason: the solver appears to have proved the exact intended statement, but a targeted prior-art audit shows that this exact instance is already covered in the literature, so the correct practical outcome is rediscovery rather than frontier novelty.

## minimal_repair_if_any

- No repair is required.
- Conservative recommendation only: when moving to Lean, formalize the explicit witness proof first. The Fourier classification is correct, but it is unnecessary for certifying the exact existential statement.

## verify_rediscovery

- Pass 1 result: `REDISCOVERY`.
- Bounded web audit checked the exact instance notation, alternate notation, the canonical source, and theorem-level statements inside the same source.
- In Collins et al., *Closed Neighborhood Balanced Coloring of Graphs* (2025), the circulant sufficient-condition theorem identified as Theorem 17 in the arXiv numbering states that `C_n(S ∪ {n/2})` is CNBC when `n ≡ 4 (mod 8)` and `s2 = s1`, where `s1` counts elements of `S` congruent to `0 mod 4` and `s2` counts elements of `S` congruent to `2 mod 4`.
- For the present instance, `n = 12 ≡ 4 (mod 8)` and `S = {1,3}`, so `s1 = 0` and `s2 = 0`. Therefore the theorem directly implies that `C_12(1,3,6)` is CNBC.
- The later family-level open discussion in the same source does not make this exact instance frontier-open; it sits inside an earlier sufficient-condition theorem.
- The current proof still appears mathematically correct and useful as an independent proof artifact, but it is not a novel solve of an open problem.

## rediscovery_audit

- Exact instance search and source audit both point to the same conclusion: the exact intended statement is already settled in the literature.
- The strongest support is not a vague concluding question or citation rumor; it is a theorem in the canonical source itself whose hypotheses match the current instance.
- Practical outcome: archive this run as a rediscovery and move the slug aside so the harness does not re-curate it.

## final_reclassification

- Final practical classification: `REDISCOVERY`.
- Proof status: appears correct.
- Novelty status: not frontier-novel.
- Lean status: should not be used as a stop condition here.
