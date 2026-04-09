# statement_lock

Active slug: `binary-legendre-pair-115`

Active title: `Does there exist a binary Legendre pair of length 115?`

Locked solve-stage statement:

Find binary sequences `A, B : Z/115Z -> {+1, -1}` such that for every nonzero shift
`s in Z/115Z`,

`PAF_A(s) + PAF_B(s) = -2`,

where

`PAF_A(s) = sum_j A(j) A(j+s)`,

and similarly for `B`.

This is the standard odd-length binary Legendre-pair normalization used in this solve
attempt. If verification finds that the canonical source uses a different normalization,
all deductions below must be re-audited from the statement lock onward.

Equivalent subset formulation used below:

- Let `X = {j : A(j) = -1}` and `Y = {j : B(j) = -1}`.
- Write `k_X = |X|`, `k_Y = |Y|`.
- Then the Legendre condition is equivalent to
  `nu_X(s) + nu_Y(s) = lambda` for every nonzero `s`,
  where `nu_X(s) = |X ∩ (X - s)|`.

# definitions

- `v = 115 = 5 * 23`.
- `PAF_A(0) = 115` for any binary sequence `A`.
- `S_A = sum_j A(j)` and `S_B = sum_j B(j)`.
- `PSD_A(t) = |sum_j A(j) zeta^(jt)|^2` for `zeta = exp(2 pi i / 115)`.
- `m`-compression means summing entries on residue classes modulo `115 / m`.
  Two useful compressions are:
  - `23`-compression to length `5`, with entries in odd integers in `[-23, 23]`.
  - `5`-compression to length `23`, with entries in `{-5, -3, -1, 1, 3, 5}`.

Ambiguities / conventions / missing definitions that matter:

- The exact odd-length binary Legendre-pair normalization is not written explicitly in
  `selected_problem.md`; this record assumes the standard nonzero-shift constant `-2`.
- Indexing is cyclic in `Z/115Z`.
- Because solve runs with web disabled, I am not asserting any source-specific
  normalization beyond this standard convention.

# approach_A

Structural / invariant route.

1. Use the Fourier transform of the combined autocorrelation sequence
   `C(s) = PAF_A(s) + PAF_B(s)`.
2. Since `C(0) = 230` and `C(s) = -2` for `s != 0`, deduce:
   - `PSD_A(0) + PSD_B(0) = 2`,
   - `PSD_A(t) + PSD_B(t) = 232` for every `t != 0`.
3. Therefore `S_A^2 + S_B^2 = 2`, so each total sum is `+1` or `-1`, and exactly one of
   them is `+1` while the other is `-1`.
4. Translating to subsets `X, Y`, conclude
   `k_X = 57`, `k_Y = 58` up to swapping, and then
   `nu_X(s) + nu_Y(s) = 57` for every nonzero `s`.
5. Carry these identities through compression by `23` and by `5` to force small integer
   block-sum constraints.

Why this could work:

- The zero-frequency identity is extremely rigid.
- The factorization `115 = 5 * 23` gives two nontrivial compression pictures.
- Small block-sum squares may leave only a tiny number of compressed states.

Self-check for approach A:

- The deduction `S_A^2 + S_B^2 = 2` is exact and independent of any search.
- The step from total sums to `(k_X, k_Y) = (57, 58)` uses only
  `k = (115 - S) / 2` for a binary sequence.
- The SDS parameter `lambda = 57` matches both formulas
  `lambda = k_X + k_Y - (v+1)/2` and
  `lambda(v-1) = k_X(k_X-1) + k_Y(k_Y-1)`.

# approach_B

Construction / extremal / contradiction route.

1. Compress by `23` to length `5`. Let the compressed sequences be
   `x = (x_0, ..., x_4)` and `y = (y_0, ..., y_4)`.
2. Then each `x_i, y_i` is an odd integer in `[-23, 23]`, the total sums are
   `sum x_i = 1`, `sum y_i = -1` after a harmless swap/sign normalization, and
   for every nonzero shift modulo `5`,
   `PAF_x(s) + PAF_y(s) = -46`.
3. At shift `0`, compression plus Fourier gives
   `sum_i x_i^2 + sum_i y_i^2 = 186`.
4. Because each odd square is `1 mod 8`, the excess above the baseline `10` is
   `176 = 8 * 22`, so the compressed entries have very limited magnitudes.
   In particular, `|x_i|, |y_i| <= 13`.
5. Enumerate only these compressed length-`5` states. If no state exists, that is a
   rigorous disproof of the original problem. If some states survive, the solve stage
   remains partial but with a sharply reduced search frontier.

Why this could work:

- This is not a blind search over full sequences of length `115`.
- The compressed problem is a necessary condition with only `5` coordinates.
- A contradiction at the compressed level would be exact.

Self-check for approach B:

- Compression preserves the relevant Fourier values at frequencies divisible by the
  compression factor.
- The nonzero-shift constant scales by the compression factor: `23 * (-2) = -46`.
- The zero-shift total `186` is consistent with the nonzero-frequency PSD total `232`
  for length `5`, since `186 + 46 = 232`.

# lemma_graph

- Lemma 1: `C(0) = 230` and `C(s) = -2` for `s != 0`.
- Lemma 2: Fourier transform of `C` gives
  `PSD_A(0) + PSD_B(0) = 2` and `PSD_A(t) + PSD_B(t) = 232` for `t != 0`.
- Lemma 3: `S_A, S_B in {+1, -1}` and, after normalization, `(S_A, S_B) = (1, -1)`.
- Lemma 4: Hence `(k_X, k_Y, lambda) = (57, 58, 57)` up to swapping `A, B`.
- Lemma 5: `23`-compression gives odd length-`5` sequences `(x, y)` with:
  - `sum x_i = 1`,
  - `sum y_i = -1`,
  - `sum x_i^2 + sum y_i^2 = 186`,
  - `PAF_x(s) + PAF_y(s) = -46` for `s = 1, 2`.
- Lemma 6: Any original Legendre pair must project to one of these compressed states.
- Target fork:
  - either show Lemma 5 has no solutions,
  - or classify all solutions and try to lift further.

# chosen_plan

Best current path: finish the invariant deductions exactly, then run a tiny bounded
enumeration of the `23`-compressed length-`5` states from Lemma 5. This stays within the
solve-stage code policy because:

- two reasoning routes have already been articulated,
- the code is tied to a specific necessary condition,
- and the search space is over compressed summaries, not over full length-`115` witnesses.

# self_checks

- Check 1: the only place where source dependence enters is the normalization
  `PAF_A(s) + PAF_B(s) = -2` for `s != 0`.
- Check 2: the arithmetic `(57, 58, 57)` is internally consistent.
- Check 3: the compression target is necessary but not sufficient; surviving compressed
  states would not by themselves prove existence.
- Check 4 after the bounded experiment: the code searched only compressed length-`5`
  tuples with the locked sums and autocorrelation targets. It did not search full
  length-`115` witnesses or invoke SAT / ILP / CP-SAT / Lean.

# code_used

Used one short script:

- `artifacts/binary-legendre-pair-115/compression23_feasibility.py`

What it checks:

- Enumerate all odd `5`-tuples `x` with entries in `[-23, 23]` and `sum x_i = 1`.
- Record each tuple's signature
  `(sum x_i^2, PAF_x(1), PAF_x(2))`.
- Match it against the required partner signature for a second compressed sequence `y`
  with `sum y_i = -1`, using the observation that `z -> -z` preserves PAF values and
  converts a sum-`1` tuple into a sum-`-1` tuple.

Observed output:

- `sum1_tuples = 198780`
- `signature_count = 15445`
- `matching_signature_pairs = 162`
- `actual_ordered_pairs = 22500`

Representative compatible compressed pair:

- `x = (-1, 1, -1, 1, 1)` with signature `(5, -3, 1)`
- `y = (7, 3, 1, -1, -11)` with signature `(181, -43, -47)`

These satisfy:

- `sum x_i = 1`
- `sum y_i = -1`
- `sum x_i^2 + sum y_i^2 = 186`
- `PAF_x(1) + PAF_y(1) = -46`
- `PAF_x(2) + PAF_y(2) = -46`

# result

Current solve-stage outcome:

- The invariant deductions are solid conditional on the normalization:
  `(k_X, k_Y, lambda) = (57, 58, 57)` up to swapping.
- The `23`-compression route does not force a contradiction by itself.
- The bounded compressed search found `162` compatible signature pairs and `22500`
  ordered compressed pairs at length `5`.
- The possible compressed square totals for the first sequence cover every
  `5 mod 8` value from `5` through `181`, so the compression leaves a wide energy split.

Therefore this solve attempt does not prove existence or nonexistence. The correct
classification remains `PARTIAL`, not `CANDIDATE` and not `COUNTEREXAMPLE`.

# likely_failure_points

- The assumed normalization could be wrong for this source family.
- The compressed length-`5` system may have many feasible states, in which case this
  route only gives a partial reduction.
- A surviving compressed state need not lift to a full length-`115` witness.
- The strongest remaining route may require mixing both factorizations `115 = 5 * 23`
  at once, rather than looking at a single compression in isolation.

# what_verify_should_check

- First confirm from the canonical source that the odd-length binary Legendre-pair
  condition is exactly `PAF_A(s) + PAF_B(s) = -2` for all nonzero `s`.
- Recheck the Fourier step yielding `PSD_A(0) + PSD_B(0) = 2` and
  `PSD_A(t) + PSD_B(t) = 232` for `t != 0`.
- Recheck the subset-parameter translation `(57, 58, 57)`.
- If code is later used, verify that it searches only the compressed feasibility system
  and does not silently assume a lifting theorem.
- Recompute the bounded output of
  `artifacts/binary-legendre-pair-115/compression23_feasibility.py`, especially the
  counts `162` and `22500` and the representative pair above.

# verify_rediscovery

PASS 1 used a bounded web audit and then stopped browsing.

- Canonical source check: Definition 1 in Kotsireas et al., *Special Matrices* 11
  (2023), doi:10.1515/spma-2023-0105, defines a binary Legendre pair by two
  conditions:
  - `PAF_a(j) + PAF_b(j) = -2` for all nonzero shifts `j`,
  - and `sum_i a_i = sum_i b_i`.
- The same source states immediately after the definition that these equal sums must be
  `1` or `-1`.
- Same-source status check: Section 4 reports partial searches for length `115` and says
  neither yielded an LP of length `115`.
- Same-source conclusion check: the remaining open lengths below `200` are listed as
  `115, 145, 159, 161, 169, 175, 177, 185, 187, 195`.
- Recent status check: the 2025 paper *A low-complexity algorithm to search for
  Legendre pairs* (Linear Algebra Appl. 721, published September 15, 2025) is a search
  algorithm paper and does not present a construction at length `115`.

Verdict of PASS 1:

- No rediscovery found.
- The exact instance still appears open.
- `verify_verdict` is therefore not `REDISCOVERY`.

# verify_faithfulness

The solve-stage statement lock is not faithful to the canonical source.

- The record locked only the nonzero-shift identity `PAF_A(s) + PAF_B(s) = -2`.
- The canonical source definition also requires `sum_j A(j) = sum_j B(j)`.
- This matters immediately: the record's normalization to opposite sums,
  `(S_A, S_B) = (1, -1)`, is not merely unstated in the source, it contradicts the
  source definition.
- Consequently the derived subset sizes `(57, 58)` and the compressed sum targets
  `sum x_i = 1`, `sum y_i = -1` belong to a different proxy problem, not the intended
  length-`115` binary Legendre-pair instance.

PASS 2 verdict:

- Wrong-theorem drift occurred at the statement lock.
- The solve attempt analyzed a nearby but different statement.

# verify_proof

First incorrect step found:

- In `approach_A`, Step 3 claims that `S_A^2 + S_B^2 = 2` implies each of `S_A, S_B`
  is `±1` and "exactly one of them is `+1` while the other is `-1`."
- The first clause is correct because odd binary sums are odd integers.
- The second clause does not follow. From `S_A^2 + S_B^2 = 2` one only gets
  `S_A, S_B ∈ {±1}`. All four sign pairs remain possible at that stage.
- The canonical source in fact requires `S_A = S_B`, so the admissible sign pairs are
  `(1, 1)` or `(-1, -1)`, not `(1, -1)`.

Consequences:

- Lemma 3 is false.
- Lemma 4's parameter claim `(k_X, k_Y, lambda) = (57, 58, 57)` is unsupported for the
  intended problem.
- Lemma 5 and the compressed feasibility system inherit the same drift.

PASS 3 verdict:

- The proof attempt has a critical mathematical break at the first sum-normalization
  step, after which the remaining deductions no longer target the intended statement.

# verify_adversarial

Reran the only checker-like script:

- `python3 artifacts/binary-legendre-pair-115/compression23_feasibility.py`

Observed output:

- `sum1_tuples=198780`
- `signature_count=15445`
- `matching_signature_pairs=162`
- `actual_ordered_pairs=22500`

Adversarial assessment:

- The script reproduces the counts recorded in the solve artifact.
- The script is internally consistent for the proxy system it encodes.
- However, it hardcodes the wrong compressed sum pattern:
  - it enumerates only `x` with `sum x_i = 1`,
  - and uses negation to force a partner `y` with `sum y_i = -1`.
- For the canonical LP definition, the compressed sums should agree, not oppose each
  other. So this computation does not test a necessary condition for the intended
  length-`115` problem.

PASS 4 verdict:

- The computation is reproducible, but it supports only the wrong proxy statement.

# verify_verdict

- `verify_verdict = "WRONG_STATEMENT"`
- `classification = "VARIANT"`
- `confidence = "high"`
- `lean_ready = false`
- `next_action = "return_to_solve_with_canonical_definition_and_rederive_invariants"`

Reason:

- No rediscovery was found, so this is not a literature issue.
- The blocker is faithfulness: the solve stage drifted from the canonical LP definition
  and then built its compression experiment on the drifted statement.
- Because the current artifact does not establish anything exact about the intended
  instance, Lean is not appropriate.

# minimal_repair_if_any

No tiny repair was applied.

- A conservative patch would require re-locking the statement to the canonical source
  definition with the equal-sums condition included.
- After that, the sum and subset-parameter deductions must be redone from scratch,
  along with any compression-based script.
- This exceeds the scope of a verification-stage "tiny conservative repair."
