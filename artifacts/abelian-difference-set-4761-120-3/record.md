# abelian-difference-set-4761-120-3

## statement_lock
- Active slug: `abelian-difference-set-4761-120-3`
- Active title: `Does there exist an abelian (4761,120,3)-difference set?`
- Exact intended statement locked for solve: `There exists an abelian (4761,120,3)-difference set.`
- Exact negation targeted for disproof: for every finite abelian group `G` of order `4761`, there is no subset `D ⊆ G` with `|D| = 120` such that every nonzero element of `G` occurs exactly `3` times as an ordered difference `d1 - d2` with `d1,d2 ∈ D`.

## definitions
- Parameter check: `k(k-1) = 120*119 = 14280 = 3*(4761-1)`, so the basic counting identity is consistent.
- Difference-set order: `n = k - lambda = 117 = 3^2 * 13`.
- Any abelian group of order `4761 = 3^2 * 23^2` splits as `G = P3 × P23` with `|P3| = 9` and `|P23| = 529`.
- Ambiguity in group type remains: `P3` may be `C9` or `C3 × C3`, and `P23` may be `C529` or `C23 × C23`.
- I use `H := P3` and `K := G/H`, so `|H| = 9` and `|K| = 529`.
- For quotient counting, write `a_x := |D ∩ pi^{-1}(x)|` for `x ∈ K`, where `pi : G -> K`.
- Missing imported ingredient: the argument below uses the standard abelian prime-multiplier theorem at the prime `13`. The solve-stage attempt is only as strong as that theorem application.

## approach_A
Structural / invariant approach: compress the putative difference set by the `3`-Sylow subgroup and study the quotient profile on `K`.

If `D` exists, then the coset counts `a_x` satisfy:
- `0 <= a_x <= 9`
- `sum_x a_x = 120`
- `sum_x a_x^2 = k + lambda(|H|-1) = 120 + 3*8 = 144`
- for every nonzero `t ∈ K`, `sum_x a_x a_{x+t} = lambda |H| = 27`

Hence
- `sum_x a_x(a_x - 1) = 24`

Interpretation:
- a pure `0/1` profile would have `sum_x a_x(a_x-1)=0`
- here the total repeated occupancy above `0/1` is only `24`
- so the quotient profile is extremely sparse and should be vulnerable to orbit or congruence constraints

Brief self-check:
- These identities come directly from summing ordered differences by fibers of `pi`.
- By itself this does not yet force a contradiction, but it strongly suggests a rigid quotient pattern.

## approach_B
Construction / extremal / contradiction approach: use a multiplier to force quotient counts to be constant on large scalar-multiplication orbits.

Heuristic route:
- `13 | n = 117`
- `gcd(13,4761) = 1`
- `13 > lambda = 3`

Under the standard abelian prime-multiplier theorem, this should imply that `13` is a multiplier. So if `D` exists, then for some `g ∈ G`,
- `13D = D + g`

Passing to `K = G/H`, this should force
- `a_x = a_{13x - c}` for a suitable `c ∈ K`

Since `12` is invertible on the `23`-group `K`, the affine action `x -> 13x - c` can be conjugated to the linear action `x -> 13x`. Then the quotient count profile becomes constant on multiplication-by-`13` orbits.

Brief self-check:
- This route is much sharper than Approach A because it reduces existence to an orbit-count problem on a group of order `23^2`.
- The only serious non-elementary dependency is the multiplier theorem.

## lemma_graph
1. Assume an abelian `(4761,120,3)` difference set `D` exists in a finite abelian group `G`.
2. Let `H := P3` and `K := G/H`, so `|H| = 9` and `|K| = 529`.
3. Invoke the standard prime-multiplier theorem at `13` to obtain `13D = D + g` for some `g ∈ G`.
4. Define quotient counts `a_x := |D ∩ pi^{-1}(x)|`.
5. Deduce `a_x = a_{13x-c}`, where `c := pi(g)`.
6. Choose the unique `x0 ∈ K` with `12x0 = c`, and define `b_x := a_{x+x0}`.
7. Then `b_{13x} = b_x`, so `b` is constant on multiplication-by-`13` orbits in `K`.
8. Compute the possible orbit sizes for `x -> 13x` on `C23 × C23` and on `C529`.
9. Use `0 <= b_x <= 9` and `sum_x b_x = 120` to get a congruence contradiction.

## chosen_plan
I choose Approach B. It gives a clean exact obstruction once the multiplier step is accepted.

Step 1. Fix the quotient.

Let `H := P3`, so `|H| = 9`, and let `K := G/H`, so `|K| = 529 = 23^2`.

Self-check:
- This is canonical for abelian `G`, because the `3`-primary subgroup is characteristic.

Step 2. Apply the multiplier theorem.

Assume the standard abelian prime-multiplier theorem in the usual form: if a prime `p` satisfies `p | n`, `gcd(p,v)=1`, and `p > lambda`, then `p` is a numerical multiplier. With `p=13`, `n=117`, `v=4761`, `lambda=3`, this yields some `g ∈ G` such that
- `13D = D + g`

Self-check:
- This is the only imported theorem in the solve attempt.
- If the theorem does not apply exactly as stated, the disproof drops from a completed argument to a promising conditional route.

Step 3. Derive quotient-count invariance.

Let `pi : G -> K` be the quotient map and set `c := pi(g)`. For each `x ∈ K`, let
- `a_x := |D ∩ pi^{-1}(x)|`

Because multiplication by `13` is an automorphism of `G` and preserves `H`, counting elements of `13D` and `D+g` in the fiber over `x` gives
- `a_x = a_{13x - c}`

Self-check:
- The indexing is consistent: the fiber over `x` on the translated side comes from the fiber over `x-c`, and on the multiplied side it comes from the fiber over `13^{-1}x`; these are equivalent after reindexing.

Step 4. Conjugate the affine action to a linear one.

Since `K` is a `23`-group, multiplication by `12` is bijective. So there is a unique `x0 ∈ K` with
- `12x0 = c`

Define
- `b_x := a_{x+x0}`

Then
- `b_{13x} = a_{13x+x0} = a_{13(x+x0)-c} = a_{x+x0} = b_x`

Thus `b` is constant on each orbit of `T(x) := 13x`.

Self-check:
- This conjugation is exact because `13x0 - c = x0`.

Step 5. Compute orbit sizes.

There are two possibilities for `K`.

Case 1: `K ≅ C23 × C23`.
- Every nonzero element has order `23`.
- The scalar `13 mod 23` has multiplicative order `11`.
- So every nonzero orbit of `x -> 13x` has size `11`.

Case 2: `K ≅ C529`.
- The subgroup of elements of order dividing `23` has `23` elements, so its `22` nonzero elements split into two orbits of size `11`.
- For elements of order `529`, the orbit size is the multiplicative order of `13 mod 529`.
- A tiny bounded arithmetic check gives `ord_529(13) = 253`, with `13^11 ≡ 438 (mod 529)` and `13^11 ≡ 1 (mod 23)`.
- So the `506` elements of order `529` split into two orbits of size `253`.

Therefore, in either quotient type, every nonzero orbit has size `11` or `253`.

Self-check:
- The `C23 × C23` case is immediate from the scalar order modulo `23`.
- The `C529` case is the only place where I used a tiny computation.

Step 6. Force the congruence contradiction.

Each `b_x` is a coset count, so
- `0 <= b_x <= 9`
- `sum_x b_x = |D| = 120`

Because `b` is constant on each `13`-orbit:
- every size-`253` orbit contributes `253r` for some integer `r` with `0 <= r <= 9`
- but `253 > 120`, so every size-`253` orbit must contribute `0`

Hence the total sum has the form
- `120 = b_0 + 11m`

for some integer `m`, with `0 <= b_0 <= 9`.

But `120 ≡ 10 (mod 11)`, so this forces `b_0 ≡ 10 (mod 11)`, impossible because `b_0` lies in `0..9`.

Therefore, conditional on the multiplier theorem application in Step 2, no abelian `(4761,120,3)` difference set exists.

Self-check:
- Once the orbit sizes are correct, the contradiction is immediate and elementary.
- No search, SAT, ILP, or brute-force witness enumeration is needed.

## self_checks
- Exactness check: the argument targets the exact negation of the selected existence statement, not a relaxed proxy.
- Ambiguity check: the proof handles both possible quotient types `C23 × C23` and `C529`.
- Imported-theorem check: the whole disproof depends on the precise scope of the multiplier theorem at `p=13`.
- Arithmetic check: the only local computation needed was confirming `ord_529(13)=253` and the orbit decomposition.
- Conservatism check: solve should not call this `EXACT`; at most it supports a provisional exact-looking disproof candidate.

## code_used
- Minimal code was used only after the reasoning path was already clear.
- Tiny bounded arithmetic experiment:
  - checked `ord_529(13) = 253`
  - checked `13^11 ≡ 438 (mod 529)` and `13^11 ≡ 1 (mod 23)`
  - enumerated `x -> 13x` orbit sizes on `C529` as `[1, 11, 11, 253, 253]`
  - enumerated orbit sizes on `C23 × C23` as one orbit of size `1` and `48` orbits of size `11`
- No constructive search, SAT, ILP, CP-SAT, brute force, or generic optimization was used.

## result
- Provisional classification: `COUNTEREXAMPLE`
- Confidence: `medium`
- Best current claim: assuming the standard abelian prime-multiplier theorem applies exactly as used at `p=13`, the intended statement is false.
- Why confidence is only medium: the orbit-count contradiction is clean, but the solve-stage proof still hinges on one recalled theorem rather than a first-principles derivation inside this pass.

## likely_failure_points
- The exact statement of the prime-multiplier theorem may have a hypothesis or nuance not captured here.
- The quotient recurrence `a_x = a_{13x-c}` should be re-derived skeptically rather than trusted from memory.
- If the multiplier theorem applies only after a normalization or only to a translate of `D`, that normalization needs to be made explicit.

## what_verify_should_check
- Check the exact multiplier theorem statement and whether `p=13` satisfies all hypotheses for an abelian `(4761,120,3)` difference set.
- Re-derive the quotient recurrence from `13D = D + g` carefully, including any indexing or translation conventions.
- Recompute the orbit decomposition of `x -> 13x` on both `C23 × C23` and `C529`.
- Confirm that the final contradiction really reduces to `120 = b_0 + 11m` with `0 <= b_0 <= 9`.
- If the multiplier theorem is valid as used, promote this to a strong exact disproof candidate for later Lean work.

## verify_rediscovery
- PASS 1 used a bounded web audit focused on the exact tuple `(4761,120,3)`, reordered tuple searches, the canonical 2022 Gordon paper, and repository/status checks tied to Gordon's difference-set pages.
- I found the canonical source and repository material consistent with the dossier's claim that abelian `(4761,120,3)` remained one of the open `lambda = 3` cases in Gordon's 2022 table.
- I did not find a later paper, repository update, theorem, proposition, example, observation, or corollary explicitly settling this exact tuple.
- Rediscovery is therefore **not established** in this pass.

## verify_faithfulness
- The solve-stage argument is aimed at the exact negation of the intended statement: nonexistence of an abelian `(4761,120,3)` difference set.
- There is no evident theorem drift in the arithmetic part: the quotient is always of order `23^2`, both abelian quotient types are handled, and the final congruence obstruction concerns the exact tuple.
- The only faithfulness-sensitive dependency is the imported multiplier claim. If that theorem applies exactly as stated to every abelian `(4761,120,3)` difference set, then the proof targets the intended statement itself rather than a proxy or nearby variant.

## verify_proof
- The first unsupported step is Step 2 of `chosen_plan`: invoking the abelian prime-multiplier theorem at `p = 13` in the form "if `p | n`, `gcd(p,v)=1`, and `p > lambda`, then `p` is a multiplier".
- The record presents this as recalled background, not as a cited theorem with checked hypotheses, and the local Lean development explicitly leaves that reduction as the blocker.
- Conditional on that step, the rest of the proof checks out cleanly:
- From `13D = D + g`, the quotient recurrence `a_x = a_{13x-c}` is correct after reindexing.
- The affine-to-linear conjugation via `12x0 = c` is correct because `12` is invertible on the `23`-group quotient.
- The orbit arithmetic is correct: on `C23 × C23` the nonzero orbits have size `11`, and on `C529` the orbit sizes are `1,11,11,253,253`.
- The residue contradiction `120 = b_0 + 11m` with `0 <= b_0 <= 9` is valid, and any coefficient on a size-`253` orbit must be zero since `253 > 120`.
- Verdict for this pass: the proof is a strong conditional disproof, but the actual disproof remains incomplete until the multiplier theorem invocation is pinned down exactly.

## verify_adversarial
- I reran the local arithmetic checks in a fresh script.
- Confirmed `ord_529(13) = 253`.
- Confirmed `13^11 ≡ 438 mod 529` and `13^11 ≡ 1 mod 23`.
- Confirmed orbit sizes for multiplication by `13` are `[1, 11, 11, 253, 253]` on `C529` and `{1: 1, 11: 48}` on `C23 × C23`.
- I also inspected the Lean files. They only formalize the final residue obstruction and explicitly state that the multiplier reduction is missing.
- Attempting to run the local Lean audit failed because `lake` tried to fetch dependencies from GitHub and network access is unavailable in this environment, so there is no full formal recheck here.

## verify_verdict
- `UNVERIFIED`
- Reason: no rediscovery was found, and the internal orbit-count argument looks correct, but the first substantive step still depends on an uncited and unverified multiplier theorem application. That is too large a gap to mark the run `VERIFIED` or `lean_ready`.

## minimal_repair_if_any
- Minimal repair: replace the recalled multiplier step with an exact cited theorem statement covering abelian difference sets, then explicitly verify its hypotheses for `(v,k,lambda,n) = (4761,120,3,117)` and record the resulting conclusion `13D = D + g` (or the equivalent multiplier formulation after translation).
- If that repair is supplied cleanly, the rest of the current argument appears strong enough to revisit as a `COUNTEREXAMPLE` candidate for Lean preparation.
