# dsrg-96-10-5-1-1

## statement_lock
- Active slug: `dsrg-96-10-5-1-1`
- Title: `Does a directed strongly regular graph dsrg(96,10,5,1,1) exist?`
- Locked intended statement: there exists a directed strongly regular graph with parameters `(v,k,t,lambda,mu) = (96,10,5,1,1)`.
- Exact matrix reformulation used here: there exists a `96 x 96` `0/1` matrix `A` such that
  - `A_ii = 0` for all `i`,
  - every row sum and every column sum is `10`,
  - `A^2 = tI + lambda A + mu(J - I - A) = 5I + A + (J - I - A) = J + 4I`.
- So for every ordered pair of distinct vertices `(x,y)` there is exactly one directed `2`-path `x -> z -> y`, and for each vertex `x` there are exactly `5` directed `2`-paths from `x` back to itself.

Self-check:
- The existential target has been locked exactly, not weakened to a nearby parameter tuple.
- Because `lambda = mu = 1`, the adjacency distinction disappears from the quadratic identity; the solve stage can work with `A^2 = J + 4I` directly.

## definitions
- `J` is the all-ones matrix.
- For a vertex `x`, write `N^+(x)` for its outneighbors and `N^-(x)` for its inneighbors.
- Since `t = 5`, each vertex has exactly `5` mutual neighbors:
  `|N^+(x) cap N^-(x)| = 5`.
- Relative to a fixed vertex `x`, partition `V \\ {x}` into:
  - `M(x) = N^+(x) cap N^-(x)` with size `5`,
  - `O(x) = N^+(x) \\ N^-(x)` with size `5`,
  - `I(x) = N^-(x) \\ N^+(x)` with size `5`,
  - `N(x) = V \\ ({x} union N^+(x) union N^-(x))` with size `80`.
- For each `z in N^+(x)`, define the block `C_x(z) = N^+(z) \\ {x}`.

Ambiguities / conventions:
- I am using the standard adjacency-matrix definition from the dossier: constant indegree and outdegree `k`, zero diagonal, and the exact `2`-path identity.
- I am not assuming symmetry, normality, vertex-transitivity, or a Cayley model unless stated explicitly.

Self-check:
- The only nontrivial reformulation is replacing the full dsrg identity by `A^2 = J + 4I`; that step is exact here.
- The four local classes `M, O, I, N` are forced by the parameter tuple and will be used only as necessary-condition bookkeeping.

## approach_A
- Structural / invariant route: exploit the collapsed quadratic identity `A^2 = J + 4I`.

Major step 1: spectral package.
- From `A^2 = J + 4I`, multiplying by the all-ones vector `j` gives
  `A^2 j = (96 + 4) j = 100 j`.
- In a dsrg, `Aj = 10j` and `j^T A = 10 j^T`, so on the codimension-one subspace
  `U = {x : j^T x = 0}` we have `Jx = 0` and therefore
  `A^2 x = 4x`.
- Hence every eigenvalue of `A` is in `{10, 2, -2}`.
- Using `trace(A) = 0` and `dim U = 95`, the multiplicities are forced:
  - `10` with multiplicity `1`,
  - `2` with multiplicity `45`,
  - `-2` with multiplicity `50`.
- In particular `A` is invertible, with
  `A^-1 = A / 4 - J / 40`.

Self-check:
- The multiplicity equations are
  `m_+ + m_- = 95` and `10 + 2m_+ - 2m_- = 0`, giving `(m_+, m_-) = (45, 50)`.
- No normality assumption was used; this is only right-spectrum data forced by the polynomial identity.

Major step 2: every arc lies in a unique directed triangle.
- Fix an arc `x -> y`.
- The pair `(y,x)` is distinct, so `(A^2)_{yx} = 1`.
- Hence there is a unique vertex `z` with `y -> z -> x`, and therefore the arc `x -> y` lies in the unique directed triangle
  `x -> y -> z -> x`.
- Since every arc has this property, the full arc set partitions into directed `3`-cycles.
- With `96 * 10 = 960` total arcs, this gives exactly `960 / 3 = 320` directed triangles.
- For a fixed vertex `x`, its `10` outgoing arcs lie in `10` distinct directed triangles, so every vertex lies in exactly `10` directed triangles.

Self-check:
- The argument uses only the off-diagonal identity `(A^2)_{yx} = 1`.
- Distinct outgoing arcs from `x` cannot belong to the same directed triangle, because a directed triangle through `x` contains exactly one outgoing arc from `x`.

Major step 3: exact partition identity around one vertex.
- Fix a vertex `x`.
- The `x`-th row of `A^2 = J + 4I` says that
  `sum_{z in N^+(x)} row_z(A)` is the row vector with entry `5` at `x` and entry `1` at every other vertex.
- Equivalently:
  - every vertex `y != x` lies in exactly one outneighborhood `N^+(z)` with `z in N^+(x)`,
  - the vertex `x` itself lies in exactly `5` of those outneighborhoods.
- Therefore the ten blocks `C_x(z) = N^+(z) \\ {x}` for `z in N^+(x)` form a partition of `V \\ {x}`.
- If `z in M(x)`, then `x in N^+(z)` and `|C_x(z)| = 9`.
- If `z in O(x)`, then `x notin N^+(z)` and `|C_x(z)| = 10`.
- So each vertex produces a partition of the other `95` vertices into five `9`-blocks and five `10`-blocks.

Self-check:
- The block sizes add up correctly:
  `5 * 9 + 5 * 10 = 95`.
- This is an exact consequence of the row equation and is stronger than the raw degree facts.

Major step 4: nonnormality is forced.
- Any `0/1` adjacency matrix with zero diagonal and row sum `10` satisfies
  `trace(AA^T) = 96 * 10 = 960`.
- The eigenvalues forced above have squared moduli
  `10^2 + 45 * 2^2 + 50 * 2^2 = 100 + 380 = 480`.
- If `A` were normal, the sum of squared singular values `trace(AA^T)` would equal the sum of squared eigenvalue moduli.
- But `960 != 480`, so any solution must be nonnormal.

Self-check:
- This is a scope-tight obstruction: it does not prove nonexistence, but it does rule out the entire normal-matrix regime.
- In particular, spectral arguments that silently assume orthogonal diagonalization are invalid here.

Major step 5: limits of the invariant route.
- The spectral package is clean but does not by itself force contradiction.
- The triangle decomposition and the fixed-vertex partition are both exact, but in this pass I still did not close a global impossibility from them alone.

Self-check:
- The route yields strong structure, not a full disproof.
- At this point the problem still admits the possibility of a highly non-Cayley, non-normal realization.

## approach_B
- Construction / extremal / contradiction route: test the most algebraic realizations first, then push the fixed-vertex block structure.

Major step 1: local block consequences and the `x`-triangle matching.
- Keep a fixed vertex `x`.
- For each `z in N^+(x)`, the pair `(z,x)` has exactly one directed `2`-path from `z` to `x`.
- Therefore each block `C_x(z)` contains exactly one vertex from `N^-(x) = M(x) union I(x)`.
- Since the ten blocks partition `V \\ {x}` and `|M(x) union I(x)| = 10`, it follows that every block contains exactly one vertex of `M(x) union I(x)`.
- So the five `9`-blocks and five `10`-blocks are not arbitrary: each contains exactly one vertex from the `10`-set `M(x) union I(x)` and the remaining `8` or `9` vertices lie in `O(x) union N(x)`.
- Equivalently, each outneighbor `z in N^+(x)` has a unique matched vertex `phi_x(z) in N^-(x)` such that
  `x -> z -> phi_x(z) -> x` is a directed triangle.
- Because the ten blocks are disjoint and contain the ten vertices of `N^-(x)` exactly once, `phi_x` is a bijection
  `N^+(x) -> N^-(x)`.

Self-check:
- This refinement is exact: the unique middle vertex for `(z,x)` must lie in `N^-(x)`.
- The count matches globally because there are `10` blocks and exactly `10` vertices in `M(x) union I(x)`.

Major step 2: the mutual-neighbor graph is sparse.
- Let `H` be the undirected graph on the same vertex set where `x` and `y` are adjacent exactly when `x <-> y` is a mutual pair.
- Since each vertex has exactly `t = 5` mutual neighbors, `H` is `5`-regular on `96` vertices.
- For any distinct vertices `x,y`, a common neighbor `z` of `x` and `y` in `H` must satisfy
  `x -> z -> y`, so `z` lies in `N^+(x) cap N^-(y)`.
- But `|N^+(x) cap N^-(y)| = (A^2)_{xy} = 1` for `x != y`.
- Therefore any pair of vertices has at most one common neighbor in `H`.

Self-check:
- The conclusion is exact and uses only the dsrg `2`-path identity.
- This does not collapse `H` completely, but it sharply limits how mutual pairs can cluster.

Major step 3: abelian Cayley obstruction.
- Suppose, as a candidate construction, that the digraph were a Cayley digraph on an abelian group `G` of order `96`, with connection set `D subset G`, `|D| = 10`, and identity `e notin D`.
- Then the adjacency condition `A^2 = J + 4I` translates in the group ring to
  `D^2 = G + 4e`,
  meaning:
  - every nonidentity group element has exactly one ordered representation `d1 d2`,
  - the identity has exactly five such ordered representations.
- For any nonprincipal character `chi`, applying `chi` gives
  `chi(D)^2 = chi(G) + 4 chi(e) = 4`,
  so `|chi(D)|^2 = 4`.
- For the principal character, `|chi_0(D)|^2 = 10^2 = 100`.
- Summing over all `96` characters yields total character energy
  `100 + 95 * 4 = 480`.
- But Parseval for the indicator of a subset of size `10` in an abelian group of order `96` gives
  `sum_chi |chi(D)|^2 = 96 * 10 = 960`.
- Contradiction.

Conclusion of Approach B:
- There is no abelian Cayley realization of the target parameters.
- This does not rule out arbitrary dsrgs, but it eliminates the most obvious algebraic-construction family.

Self-check:
- The contradiction is exact for abelian Cayley models.
- The main scope risk is only theorem scope: this rules out one construction class, not all possible digraphs.

## lemma_graph
1. Lock the problem as a `96 x 96` zero-diagonal `0/1` matrix with row/column sums `10` and `A^2 = J + 4I`.
2. Pass to `U = {x : j^T x = 0}` to get `A^2 = 4I` on `U`.
3. Deduce the forced spectrum `10^1, 2^45, (-2)^50` and the inverse formula `A^-1 = A/4 - J/40`.
4. Use the off-diagonal identity `(A^2)_{yx} = 1` to show that every arc `x -> y` lies in a unique directed triangle `x -> y -> z -> x`; hence the `960` arcs partition into exactly `320` directed triangles.
5. Fix a vertex `x` and use the `x`-th row of `A^2` to show that the ten outneighborhoods of vertices in `N^+(x)` partition `V \\ {x}` into five `9`-blocks and five `10`-blocks.
6. Refine those blocks by the `(z,x)` path count: each block contains exactly one vertex of `M(x) union I(x)`, giving a bijection `phi_x : N^+(x) -> N^-(x)` via the triangles through `x`.
7. Record the auxiliary obstruction that any solution must be nonnormal, since `trace(AA^T) = 960` but the squared eigenvalue moduli sum to `480`.
8. Separately form the mutual-neighbor graph `H`, note that it is `5`-regular, and show that every pair of vertices has at most one common neighbor in `H`.
9. Test the abelian Cayley construction route and rule it out exactly via character sums.

## chosen_plan
- The best path is still the invariant route: the identity `A^2 = J + 4I` is too rigid to ignore.
- I pushed that route first because it gives exact spectral data, a global triangle decomposition, an explicit inverse, and a strong fixed-vertex partition picture without any search.
- I then used the construction route only in the most targeted way: rather than generic brute force, I checked whether the tuple could come from an abelian Cayley model and ruled that out exactly.

Attempted rigorous closure:
- I tried to convert the block partition around a fixed vertex into a full contradiction by tracking how the classes `M(x), O(x), I(x), N(x)` feed one another.
- I also checked whether the new triangle decomposition and the sparse mutual-neighbor graph force a short contradiction. They do not, at least not from the identities I could close cleanly in this pass.
- That bookkeeping produces many necessary equalities, but it still leaves room for a hypothetical highly asymmetric non-Cayley and nonnormal digraph.
- So the strongest rigorous output of this solve stage is:
  - the exact reduction to `A^2 = J + 4I`,
  - the forced spectrum and inverse,
  - the exact partition of all arcs into `320` directed triangles,
  - the per-vertex five-`9` plus five-`10` partition together with the bijection `phi_x : N^+(x) -> N^-(x)`,
  - the fact that any solution must be nonnormal,
  - the `5`-regular mutual-neighbor graph with pairwise common-neighbor number at most `1`,
  - and the exact nonexistence of abelian Cayley realizations.

Self-check:
- I am stopping for mathematical reasons, not because code failed.
- No full proof or disproof of the intended statement has been obtained yet.

## self_checks
- Statement fidelity: locked and maintained exactly.
- Structural algebra:
  - `A^2 = J + 4I` is correct.
  - The spectrum `10^1, 2^45, (-2)^50` is correct.
  - `A^-1 = A/4 - J/40` is correct.
- Triangle structure:
  - every arc lies in a unique directed triangle;
  - therefore there are exactly `320` directed triangles;
  - each vertex lies in exactly `10` directed triangles.
- Local partition:
  - the ten blocks around a vertex really do partition the other `95` vertices;
  - the size pattern is exactly `5` blocks of size `9` and `5` blocks of size `10`;
  - each block contains exactly one vertex of `M(x) union I(x)`;
  - hence the triangles through `x` induce a bijection `phi_x : N^+(x) -> N^-(x)`.
- Obstruction package:
  - any solution must be nonnormal;
  - the mutual-neighbor graph is `5`-regular and any pair of vertices has at most one common mutual neighbor;
- Construction obstruction:
  - the abelian Cayley contradiction is exact but narrower than the full problem.
- Final honesty check:
  - I did not prove global nonexistence;
  - I did not construct a witness;
  - therefore the conservative solve classification must stay below `CANDIDATE` and below `COUNTEREXAMPLE`.

## code_used
- No code used.
- Reason: the handwritten matrix reduction and the abelian-Cayley contradiction were already stronger than any justified bounded experiment, and I did not reach the point where generic search would be warranted under the harness rules.

## result
- Solve-stage verdict: `PARTIAL`
- Confidence: `medium`
- Strongest exact output from this pass:
  - any solution must satisfy the collapsed identity `A^2 = J + 4I`;
  - the right-spectrum is forced to be `10^1, 2^45, (-2)^50`;
  - every arc lies in a unique directed triangle, so the `960` arcs partition into exactly `320` directed `3`-cycles;
  - every vertex induces a partition of the remaining `95` vertices into five `9`-blocks and five `10`-blocks, each block containing exactly one vertex from `M(x) union I(x)`;
  - any solution must be nonnormal;
  - the mutual-neighbor graph is a `5`-regular graph on `96` vertices with pairwise common-neighbor number at most `1`;
  - no abelian Cayley realization exists.
- I did not prove that no dsrg with these parameters exists, and I did not produce a construction.
- Lean was not used and should stay off.

## likely_failure_points
- The main gap is global: the fixed-vertex partition constraints are strong, but I did not turn them into a full contradiction.
- The graph could still be a genuinely asymmetric non-Cayley object; the abelian obstruction does not touch that case.
- I did not prove that the local four-class structure around one vertex extends to a full association scheme or equitable partition; assuming that would overclaim.
- Because the dossier already marked curation confidence as low, there is also the meta-risk that the tuple has a published resolution I am not allowed to check here.

## what_verify_should_check
- First confirm the exact dsrg reduction:
  - zero diagonal,
  - indegree/outdegree `10`,
  - `A^2 = J + 4I`.
- Then check the invariant package carefully:
  - `A^2 = 4I` on the sum-zero subspace,
  - spectrum `10^1, 2^45, (-2)^50`,
  - inverse formula `A^-1 = A/4 - J/40`,
  - nonnormality from `trace(AA^T) = 960` versus squared eigenvalue-modulus sum `480`.
- Then check the triangle package:
  - every arc `x -> y` lies in a unique directed triangle `x -> y -> z -> x`;
  - hence the arc set partitions into exactly `320` directed triangles;
  - each fixed vertex lies in exactly `10` such triangles.
- Then check the local partition claim:
  - for fixed `x`, the blocks `C_x(z) = N^+(z) \\ {x}` with `z in N^+(x)` partition `V \\ {x}`;
  - five blocks have size `9`, five have size `10`;
  - each block contains exactly one vertex of `M(x) union I(x)`;
  - the induced triangle matching gives a bijection `phi_x : N^+(x) -> N^-(x)`.
- Then check the mutual-neighbor graph claim:
  - the mutual-neighbor graph is `5`-regular;
  - any two vertices have at most one common mutual neighbor.
- Then check the abelian Cayley obstruction:
  - group-ring identity `D^2 = G + 4e`,
  - nonprincipal character values satisfy `chi(D)^2 = 4`,
  - Parseval gives the contradiction `480 != 960`.
- Because solve ran with web disabled and the dossier flagged moderate rediscovery risk, verification should do the bounded prior-art audit first before treating any nonexistence argument as frontier-novel.

## verify_rediscovery
- PASS 1 used a bounded web audit against the canonical Hobart-Brouwer dsrg pages only.
- The exact tuple `(96,10,5,1,1)` still appears in Table 91-100 with comment `?`, not with a construction tag `T*` or nonexistence tag `N*`.
- In the same source, section `1.5` already states the general theorem that a directed strongly regular graph cannot be a Cayley graph of an Abelian group. So the solve-stage abelian-Cayley obstruction is mathematically correct but not novel.
- Within the remaining audit budget I did not find a source establishing that the exact intended statement is already solved, directly implied, or explicitly exhibited.
- Rediscovery verdict for the intended statement: not established. Rediscovery is present only for the narrower abelian-Cayley subclaim, not for the exact instance-level existence question.

## verify_faithfulness
- The solve artifact does not prove the intended statement either way.
- Its actual content is a package of necessary conditions and subclass obstructions:
  - the exact reduction to `A^2 = J + 4I`;
  - the forced eigenvalue set and multiplicities;
  - the unique directed-triangle decomposition of arcs;
  - the fixed-vertex `5`-by-`9` and `5`-by-`10` partition with the bijection `phi_x : N^+(x) -> N^-(x)`;
  - the nonnormality requirement;
  - the sparse mutual-neighbor graph constraint;
  - the nonexistence of abelian Cayley realizations.
- That is faithful to a `PARTIAL` obstruction analysis. It is not faithful to a full proof of existence or nonexistence of dsrg `(96,10,5,1,1)`.

## verify_proof
- I did not find a fatal incorrect step in the explicit structural claims.
- The only point needing repair is the multiplicity argument in the spectral package. From `A^2 = J + 4I` and `AJ = JA = 10J`, one should explicitly derive the annihilating polynomial
  `(A-10I)(A-2I)(A+2I) = 0`.
  Because the roots `10,2,-2` are distinct, `A` is diagonalizable, so the claimed algebraic multiplicities `1,45,50` do follow from trace and dimension counting.
- After that repair, the remaining steps check out:
  - for `x != y`, `(A^2)_{xy} = 1` gives exactly one directed `2`-path from `x` to `y`, which yields the unique-triangle decomposition of arcs;
  - the row equation for `A^2` gives the partition of `V \\ {x}` into five `9`-blocks and five `10`-blocks;
  - the `(z,x)` path count gives exactly one vertex of `N^-(x)` in each block, hence the bijection `phi_x`;
  - the mutual-neighbor graph argument and the nonnormality argument are both correct;
  - the abelian Cayley contradiction is valid, though already known from the canonical source.
- So the proof package is sound after one tiny justification repair, but it still stops far short of a proof or disproof of the intended statement.

## verify_adversarial
- No witness matrix, checker, or search code exists for this slug, so PASS 4 was a mathematical adversarial audit rather than a code rerun.
- I independently rechecked the core arithmetic:
  - the multiplicity equations force `(45,50)`;
  - `trace(AA^T) = 96 * 10 = 960`;
  - the squared eigenvalue-modulus sum is `10^2 + 45 * 2^2 + 50 * 2^2 = 480`, so any witness would indeed have to be nonnormal.
- I also tried to break the triangle and block claims by looking for double-counting errors around a fixed vertex `x`; none appeared once the row interpretation of `A^2` was kept explicit.
- This adversarial pass therefore supports the partial obstruction package, but it does not produce a witness, a contradiction, or any computation that closes the exact instance.

## verify_verdict
- `MINOR_FIX`
- Classification remains `PARTIAL`.
- Reason: the artifact contains a correct-looking and now repaired partial analysis, but it still does not prove or disprove the exact intended dsrg existence statement.
- `lean_ready = false` because there is nothing exact to formalize yet, and PASS 1 did not establish rediscovery of the exact tuple either.

## minimal_repair_if_any
- Minimal repair applied in verification: make the spectral package explicit by inserting the annihilating polynomial
  `(A-10I)(A-2I)(A+2I) = 0`
  before concluding algebraic multiplicities.
- No stronger repair is available without a genuinely new global argument. The run must stay below `CANDIDATE`, below `COUNTEREXAMPLE`, and far below `EXACT`.
