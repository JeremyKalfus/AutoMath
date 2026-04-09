## statement_lock

The active problem is:

> Does there exist a loopless directed strongly regular graph with parameters `(v,k,t,lambda,mu) = (54,11,4,3,2)`?

For this solve pass I lock the intended exact statement as:

> **Intended statement.** No directed strongly regular graph with parameters `(54,11,4,3,2)` exists.

For any candidate adjacency matrix `A`, the dsrg condition is exactly

`A^2 = t I + lambda A + mu (J - I - A) = 4I + 3A + 2(J - I - A) = A + 2I + 2J`.

So every rigorous argument can be framed as a consequence of

`A^2 = A + 2I + 2J`, `AJ = JA = 11J`, `diag(A) = 0`.

## definitions

- `A` is the `54 x 54` `0/1` adjacency matrix of the digraph.
- `J` is the all-ones matrix and `I` is the identity matrix.
- For a fixed vertex `x`, write:
  - `M = {y : x -> y and y -> x}` with `|M| = t = 4`,
  - `O = {y : x -> y and y !-> x}` with `|O| = 7`,
  - `I_x = {y : y -> x and x !-> y}` with `|I_x| = 7`,
  - `N = {y : x !-> y and y !-> x}` with `|N| = 35`.
- Also write `S = N^+(x) = M ∪ O` and `T = N^-(x) = M ∪ I_x`, so `|S| = |T| = 11` and `|S ∩ T| = 4`.

Potential ambiguity check:

- I use `I_x` for the in-only cell to avoid colliding with the identity matrix `I`.
- "Loopless" means `A_xx = 0` for every vertex `x`.
- The dsrg definition already forces constant in-degree and out-degree `11`.

## approach_A

### Structural / invariant route

Start from

`A^2 = A + 2I + 2J`.

On the all-ones line, `A` has eigenvalue `11`. On the orthogonal complement of `1`, the matrix satisfies

`x^2 - x - 2 = 0 = (x-2)(x+1)`,

so the only nontrivial eigenvalues are `2` and `-1`.

Let their multiplicities be `m_2` and `m_{-1}`. Then

- `m_2 + m_{-1} = 53`,
- `11 + 2 m_2 - m_{-1} = tr(A) = 0`.

Solving gives

- `m_2 = 14`,
- `m_{-1} = 39`.

So the forced spectrum is

`11^1, 2^14, (-1)^39`.

Because none of these eigenvalues is `0`, `A` is invertible. Interpolating on the three eigenspaces gives the exact inverse

`A^(-1) = (1/2) A - (1/2) I - (1/11) J`.

This route gives strong necessary algebra, but no contradiction by itself. The spectrum is perfectly integral and the inverse has no immediate sign or divisibility obstruction.

I also checked the tempting mod-`2` reduction:

`A^2 ≡ A (mod 2)`.

So `A mod 2` is a zero-diagonal idempotent. I briefly hoped that high rank over `F_2` might be impossible for such matrices. The small bounded experiment recorded below shows that this hoped-for obstruction is false in general, so I do not claim anything from the mod-`2` route beyond the idempotence itself.

## approach_B

### Construction / extremal / contradiction route

Fix a vertex `x` and use the four-cell partition `M, O, I_x, N`.

The dsrg axiom can be read locally as:

- if `y -> x`, then `|N^+(y) ∩ T| = 3`,
- if `y !-> x`, then `|N^+(y) ∩ T| = 2`,
- if `x -> y`, then `|S ∩ N^-(y)| = 3`,
- if `x !-> y`, then `|S ∩ N^-(y)| = 2`.

Applying this to each cell gives exact row-side totals:

- each vertex of `M` sends `3` arcs into `T`, hence
  `e(M,M) + e(M,I_x) = 4 * 3 = 12`,
- each vertex of `O` sends `2` arcs into `T`, hence
  `e(O,M) + e(O,I_x) = 7 * 2 = 14`,
- therefore `M -> (O ∪ N)` contributes `4 * 7 = 28`,
- and `O -> (O ∪ N)` contributes `7 * 9 = 63`.

Applying the same axiom column-wise to targets of the form `y` gives exact `S`-to-cell totals:

- every vertex of `M` receives `3` arcs from `S`, so
  `e(M,M) + e(O,M) = 4 * 3 = 12`,
- every vertex of `O` receives `3` arcs from `S`, so
  `e(M,O) + e(O,O) = 7 * 3 = 21`,
- every vertex of `I_x` receives `2` arcs from `S`, so
  `e(M,I_x) + e(O,I_x) = 7 * 2 = 14`,
- every vertex of `N` receives `2` arcs from `S`, so
  `e(M,N) + e(O,N) = 35 * 2 = 70`.

Write

- `a = e(M,M)`,
- `g = e(O,O)`.

Then the whole unconditional block-total system collapses to

- `e(M,I_x) = 12 - a`,
- `e(O,M) = 12 - a`,
- `e(O,I_x) = 2 + a`,
- `e(M,O) = 21 - g`,
- `e(M,N) = 7 + g`,
- `e(O,N) = 63 - g`.

The only immediate restrictions are

- `0 <= a <= 12`,
- `0 <= g <= 21`.

So this first local counting attack does **not** force a contradiction. It does show that any contradiction has to use finer information than one-vertex block totals.

## lemma_graph

1. `A` must satisfy the exact matrix identity `A^2 = A + 2I + 2J`.
2. Therefore the nontrivial eigenvalues are forced to be `2` and `-1`.
3. Trace and dimension force multiplicities `14` and `39`.
4. Hence `A` is invertible with explicit inverse `A^(-1) = (1/2)A - (1/2)I - (1/11)J`.
5. For any fixed vertex `x`, the partition sizes are forced to be `|M|=4`, `|O|=7`, `|I_x|=7`, `|N|=35`.
6. The dsrg axiom gives exact unconditional block totals from `S = N^+(x)` into the four cells: `(12,21,14,70)`.
7. Those totals remain parametrically consistent, so a contradiction must come from a finer two-vertex or pair-coherent analysis, not from this coarse partition alone.

## chosen_plan

The best path was the fixed-vertex contradiction route, not the pure spectral route.

Reason:

- the spectral data is clean but feasible,
- the local partition is small enough to attack by hand,
- the problem dossier explicitly suggested neighborhood partitions and sparse overlap counting.

I therefore pushed the one-vertex partition as far as possible without introducing unjustified search. When that failed to contradict itself, I only used one tiny bounded computation to test whether the mod-`2` idempotent idea had any chance of becoming a real obstruction. It did not.

## self_checks

- Statement lock check: substituting `(t,lambda,mu) = (4,3,2)` into the standard dsrg identity really does give `A^2 = A + 2I + 2J`.
- Spectral check: `11 + 14*2 + 39*(-1) = 0`, so the trace condition is consistent.
- Dimension check: `1 + 14 + 39 = 54`.
- Inverse check: on eigenvalues `11,2,-1`, the formula `(1/2)A - (1/2)I - (1/11)J` acts as `1/11, 1/2, -1`, respectively.
- Local partition check: `4 + 7 + 7 + 35 = 53`, so the non-base vertices are fully partitioned.
- `S`-to-cell total check: `12 + 21 + 14 + 70 = 117`; adding the `4` arcs from `S` back to `x` gives `121 = 11 * 11`, exactly the total number of arcs leaving `S`.
- Row-total check: the `M` rows contribute `12 + 28 + 4 = 44 = 4 * 11`, and the `O` rows contribute `14 + 63 = 77 = 7 * 11`.
- Route-failure check: the mod-`2` idea was explicitly tested on small cases before discarding it; I am not suppressing a hidden contradiction there.

## code_used

Yes, but only minimally and only after the handwritten reasoning routes were fixed.

Purpose:

- test whether the mod-`2` structural route could be closed by a general rank obstruction for zero-diagonal idempotent matrices over `F_2`.

What was checked:

- exhaustive search for small sizes `n <= 5` showed maximum ranks
  `0, 0, 2, 2, 4`
  for zero-diagonal idempotents over `F_2`.

Interpretation:

- high rank is possible in that toy setting, so the raw fact `A^2 ≡ A (mod 2)` is not enough by itself to obstruct the `(54,11,4,3,2)` instance.

No search was run on the actual `54`-vertex instance, and I did not use SAT, ILP, CP-SAT, brute force over candidate digraphs, or generic optimization.

## result

I did **not** find a rigorous proof or disproof.

What I did get rigorously:

- the exact matrix identity `A^2 = A + 2I + 2J`,
- the forced spectrum `11^1, 2^14, (-1)^39`,
- the explicit inverse of `A`,
- the full one-vertex `M/O/I_x/N` block-total system around a fixed vertex.

The strongest honest classification for this solve pass is therefore:

`PARTIAL`

The main mathematical content is negative information about what will **not** work quickly:

- pure spectral feasibility does not obstruct the tuple,
- the first one-vertex local counting layer is still consistent,
- the naive mod-`2` projection idea is not sharp enough.

## likely_failure_points

- The one-vertex partition may simply be too coarse. A real contradiction, if it exists, probably has to involve a fixed ordered pair `(x,y)` and a finer partition by joint relation to both vertices.
- I did not derive any unconditional relation for `AA^T` or `A^T A`, so common out-neighbor and common in-neighbor counts remain uncontrolled.
- A five-cell equitable-quotient ansatz around one vertex might still be tempting, but I have not justified that ansatz, so it would only be heuristic at this stage.
- The explicit inverse and mod-`2` idempotence may still matter later, but I do not currently see a rigorous bridge from them to nonexistence.

## what_verify_should_check

- Recheck the normalization `A^2 = A + 2I + 2J`.
- Recheck the spectrum calculation and the explicit inverse formula.
- Recheck the fixed-vertex partition sizes `4,7,7,35`.
- Recheck every one of the eight block-total equations for `e(M,*)` and `e(O,*)`.
- Recheck that the totals are genuinely consistent and that no hidden subtraction of `x` was mishandled.
- Recheck the tiny `F_2` experiment only as a reason for discarding that route, not as evidence for or against existence of the target dsrg.
- Decide whether the next serious attack should be:
  - a two-vertex local feasibility analysis around an arc or mutual pair, or
  - a construction-oriented attempt that studies whether the algebra `A^2 = A + 2I + 2J` can arise from a known finite configuration.

## verify_rediscovery

- PASS 1 used a bounded live web audit on the exact tuple `(54,11,4,3,2)`, the complement tuple `(54,42,35,32,35)`, the canonical Brouwer-Hobart dsrg table, same-source row comments around the `54`-vertex page, and one recent dsrg status paper.
- The canonical source still lists `(54,11,4,3,2)` with comment `?`, while nearby `54`-vertex rows that are settled are explicitly tagged by constructions such as `M10` or nonexistence tags such as `N3`, `N4`, `N6`, `N10`, `N11`, `N12`.
- The bounded recent-paper check did not produce a theorem, proposition, example, observation, or corollary settling this exact tuple. A 2025 paper on dsrgs from linear groups cites the Brouwer-Hobart catalog as the status reference and does not identify `(54,11,4,3,2)` as a solved instance.
- Conclusion for PASS 1: rediscovery was not established within budget, so this run should not be classified as `REDISCOVERY`.

## verify_faithfulness

- The solve artifact is faithful about scope. It locks the intended statement to nonexistence for the exact tuple `(54,11,4,3,2)`, but it does not pretend to prove that statement.
- The actual mathematical content is a `PARTIAL` package consisting of the normalized matrix identity, the forced spectrum and inverse, and the one-vertex `M/O/I_x/N` block-total system.
- I did not find wrong-theorem drift, quantifier drift, changed definitions, or a swap to a nearby proxy problem. The natural-language summary matches the mathematics actually carried out.
- Because the intended statement is still unresolved in the artifact, the classification must remain `PARTIAL`, not `CANDIDATE`, `COUNTEREXAMPLE`, or `EXACT`.

## verify_proof

- First incorrect step found: none in the claims actually made.
- I rechecked the normalization
  `A^2 = 4I + 3A + 2(J-I-A) = A + 2I + 2J`.
- On the `J`-orthogonal subspace this gives the restricted polynomial `u^2 - u - 2 = (u-2)(u+1)`, so the nontrivial eigenvalues are `2` and `-1`. Using `m_2 + m_{-1} = 53` and `11 + 2m_2 - m_{-1} = 0` indeed forces `(m_2,m_{-1}) = (14,39)`.
- The inverse formula `A^(-1) = (1/2)A - (1/2)I - (1/11)J` is correct: it acts by `1/11`, `1/2`, and `-1` on the eigenspaces for eigenvalues `11`, `2`, and `-1`, respectively.
- For a fixed vertex `x`, the partition sizes `|M|=4`, `|O|=7`, `|I_x|=7`, `|N|=35` are correct, and the local dsrg counts around `x` do force the displayed eight block-total equations.
- The derived parametrization
  `e(M,I_x)=12-a`, `e(O,M)=12-a`, `e(O,I_x)=2+a`, `e(M,O)=21-g`, `e(M,N)=7+g`, `e(O,N)=63-g`
  is consistent with the row and column totals, so the solver is correct that this coarse partition does not itself yield a contradiction.
- The substantive gap is not an incorrect step but an absent step: none of these verified identities proves the intended nonexistence statement.

## verify_adversarial

- There is no local checker, witness digraph, adjacency matrix, or search script in this artifact directory, so there was nothing executable to rerun beyond arithmetic verification.
- I reran fresh shell checks for the key algebra:
  - the dsrg normalization simplifies to `A^2 = A + 2I + 2J`,
  - the trace equations force multiplicities `14` and `39`,
  - the inverse formula multiplies back to the identity on the three forced eigenspaces.
- I also adversarially checked the one-vertex counts for hidden omissions of the base vertex `x`. The totals in the record are internally consistent: `12 + 21 + 14 + 70 = 117`, and adding the `4` arcs from `S` to `x` recovers `121 = 11^2`.
- Adversarial conclusion: the artifact survives as a sound partial obstruction package, but it still does not support an exact proof or exact disproof of the tuple.

## verify_verdict

- `UNVERIFIED`
- Classification remains `PARTIAL`.
- Reason: PASS 1 did not establish rediscovery, and I did not find an incorrect step in the partial algebraic/counting package, but the artifact still falls well short of proving the intended exact statement that no dsrg with parameters `(54,11,4,3,2)` exists.
- `lean_ready` must remain `false` because there is no frontier-novel exact theorem or exact counterexample to formalize.

## minimal_repair_if_any

- No mathematical repair was applied.
- The only conservative repair is classificatory: keep the slug explicitly at `PARTIAL` with `verify_verdict = UNVERIFIED`, and do not run Lean on the current artifact.
