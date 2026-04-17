# Solve Record: Does the cyclic group C_1111 admit a (1111,186,31)-difference set?

- slug: `cyclic-difference-set-1111-186-31`
- working_packet: `artifacts/cyclic-difference-set-1111-186-31/working_packet.md`

## statement_lock
Exact intended statement for this solve pass:

> The cyclic group `C_1111` does not admit a `(1111,186,31)` difference set.

Equivalent title-theorem form:

> There is no cyclic `(1111,186,31)` difference set.

If this argument is sound, it is already the title theorem of the intended short residual-case paper. Relative to the micro-paper target, a verified version of this proof would be roughly 80-85% of the finished note; the remaining work is bounded packaging, citation, and verification.

## definitions
Let `G = C_1111`, written additively. A `(1111,186,31)` difference set is a subset `D ⊂ G` of size `k = 186` such that every nonzero element of `G` has exactly `lambda = 31` representations as `d1 - d2` with `d1,d2 ∈ D`.

Set

- `v = 1111 = 11 * 101`
- `k = 186`
- `lambda = 31`
- `n = k - lambda = 155 = 5 * 31`

I use the standard multiplier fact for abelian difference sets: if a prime `p` divides `n` and `gcd(p,v)=1`, then `p` is a multiplier. Since `5 | 155` and `gcd(5,1111)=1`, the prime `5` is a multiplier. Because `gcd(5-1,1111)=gcd(4,1111)=1`, a translate of `D` may be chosen so that `5D = D`.

Under the Chinese remainder identification

`G ≅ Z_11 × Z_101`,

the map `x -> 5x` acts componentwise.

Useful subgroups:

- `H := Z_11 × {0}` of order `11`
- `K := {0} × Z_101` of order `101`

Conventions / ambiguity notes:

- I work only up to translation, which preserves the difference-set property.
- The argument uses standard contraction identities for quotient counts. Verification should confirm the coefficient formulas carefully.
- Solve runs with web disabled, so literature novelty is not checked here.

## approach_A
Structural invariant route: exploit the multiplier `5`.

1. Normalize by translation so that `D` is fixed by multiplication by `5`.
2. Compute the orbit lengths of `5` on `Z_11 × Z_101`.
3. Use `|D| = 186` to force the exact orbit inventory of any such `D`.
4. Contract modulo the subgroup `K` of order `101`, producing eleven fiber counts on `G/K ≅ Z_11`.
5. Compare:
   - the Diophantine possibilities forced by the contraction identities, and
   - the congruence forced by the orbit inventory.

Expected payoff: a direct contradiction without any search.

## approach_B
Construction / extremal contradiction route: describe the seven forced length-25 orbits explicitly.

Once `D` is normalized to be `5`-invariant, the size computation suggests:

- `D` contains all of `H`,
- the remaining `175` points are exactly seven length-25 orbits.

Projecting modulo `H` gives `101` quotient fibers. The `H`-coset has count `11`, and the nonzero quotient residues split into four `25`-cycles under multiplication by `5`. If `t_1,...,t_4` are the four nonzero fiber levels, then

- `11 + 25(t_1+t_2+t_3+t_4) = 186`, so `t_1+t_2+t_3+t_4 = 7`,
- `11^2 + 25(t_1^2+t_2^2+t_3^2+t_4^2) = 496`, so `t_1^2+t_2^2+t_3^2+t_4^2 = 15`.

Thus the only possible multiset is `{3,2,1,1}`.

This does not by itself kill the case, but it shows the candidate is extremely rigid and supports the quotient-by-`K` contradiction in Approach A.

## lemma_graph
1. `5 | n` and `gcd(5,v)=1`, so `5` is a multiplier.
2. Since `gcd(5-1,v)=1`, a translate of any cyclic difference set may be chosen `5`-invariant.
3. In `Z_11 × Z_101`, the `5`-orbits have lengths:
   - `1` at `(0,0)`,
   - `5` on `H \ {0}`,
   - `25` everywhere else.
4. Because `186 = 1 + 5*2 + 25*7`, any `5`-invariant candidate must contain all of `H` and exactly seven length-25 orbits.
5. Let `c_r = |D ∩ ({r} × Z_101)|` for `r ∈ Z_11`. By `5`-invariance,
   - `c_0 = x`,
   - `c_r = a` on one nonzero `5`-cycle,
   - `c_r = b` on the other nonzero `5`-cycle.
6. Contraction over `K` gives
   - `x + 5a + 5b = 186`,
   - `x^2 + 5a^2 + 5b^2 = 3286`.
7. These equations force `x ∈ {6,21}`.
8. Orbit structure forces `c_0 ≡ 1 (mod 25)`.
9. Since neither `6` nor `21` is `1 mod 25`, contradiction.

## chosen_plan
Use Approach A as the main proof path, and keep Approach B as a consistency check that the forced orbit profile really is narrow enough to support a short paper.

This is the better path because it closes the exact target without code, stays inside the multiplier / contraction framework already suggested by the packet, and yields a theorem-shaped nonexistence statement rather than only a witness-free obstruction.

## self_checks
1. Multiplier normalization:
   `5 | 155`, `gcd(5,1111)=1`, and `gcd(4,1111)=1`, so the standard normalization step is available.
2. Orbit lengths:
   `ord_11(5)=5` and `ord_101(5)=25` because `5^5 ≡ 95 != 1 (mod 101)` and `5^25 ≡ 1 (mod 101)`.
3. Size decomposition:
   there are only two length-5 orbits, namely the nonzero elements of `H`, and every other nonzero orbit has length `25`.
4. Quotient identity:
   for the subgroup `K` of order `101`, the identity coefficient is
   `k + lambda(|K|-1) = 186 + 31*100 = 3286`.
5. Diophantine step:
   solving the two equations for `(x,a,b)` really gives only the two profiles listed below.
6. Final contradiction:
   `c_0 = 1 + 25r` because `H` contributes one point to the zero fiber and each chosen length-25 orbit contributes either `0` or `25` points there.

## code_used
No code used. The current solve attempt is reasoning-only.

## result
Candidate disproof.

Assume for contradiction that `D ⊂ G ≅ Z_11 × Z_101` is a cyclic `(1111,186,31)` difference set.

Because `5 | n = 155` and `gcd(5,1111)=1`, the prime `5` is a multiplier. Since `gcd(5-1,1111)=1`, after translating `D` we may assume `5D = D`.

Now compute the orbit lengths of multiplication by `5`:

- on `Z_11^*`, the order is `5`,
- on `Z_101^*`, the order is `25`,
- hence on `Z_11 × Z_101` the only orbit lengths are:
  - `1` for `(0,0)`,
  - `5` for the ten nonzero elements of `H = Z_11 × {0}`,
  - `25` for every other nonzero element.

Since `|D| = 186 ≡ 1 (mod 5)`, the singleton orbit must be present. Writing

`186 = 1 + 5s + 25q`

with `s` the number of length-5 orbits used and `q` the number of length-25 orbits used, we get

`s + 5q = 37`.

There are only two length-5 orbits available, so `s <= 2`. Also `s ≡ 2 (mod 5)`, hence `s = 2` and `q = 7`. Therefore `D` contains all of `H`, together with exactly seven length-25 orbits.

Next contract modulo `K = {0} × Z_101`. For `r ∈ Z_11`, define

`c_r := |D ∩ ({r} × Z_101)|`.

Because `D` is `5`-invariant, the nonzero residues of `Z_11` split into two `5`-cycles, so the fiber counts have the form

- `c_0 = x`,
- `c_r = a` on one nonzero `5`-cycle,
- `c_r = b` on the other nonzero `5`-cycle.

Hence

`x + 5a + 5b = 186`.  (1)

The standard quotient-count identity gives

`sum_r c_r^2 = k + lambda(|K|-1) = 186 + 31*100 = 3286`,

so

`x^2 + 5a^2 + 5b^2 = 3286`.  (2)

Write `x = 1 + 5t`. Then from (1), `a+b = 37-t`. From (2),

`a^2 + b^2 = 657 - 2t - 5t^2`.

Therefore

`(a-b)^2 = 2(a^2+b^2) - (a+b)^2 = -11t^2 + 70t - 55`.

This must be a nonnegative square. Checking the integer range shows only:

- `t = 1`, giving `(a-b)^2 = 4`, hence `(x,a,b) = (6,19,17)` up to order;
- `t = 4`, giving `(a-b)^2 = 49`, hence `(x,a,b) = (21,20,13)` up to order.

So any candidate must satisfy

`c_0 ∈ {6,21}`.  (3)

But the orbit decomposition gives a different constraint on `c_0`. The subgroup `H` contributes exactly one point to the zero fiber `{0} × Z_101`, namely `(0,0)`. Each of the seven chosen length-25 orbits contributes either:

- `25` points to the zero fiber, if it lies inside `K \ {0}`, or
- `0` points to the zero fiber, if it is a unit orbit with nonzero first coordinate.

Thus

`c_0 = 1 + 25r`

for some integer `r`, so

`c_0 ≡ 1 (mod 25)`.  (4)

The values `6` and `21` from (3) are not congruent to `1 mod 25`, contradicting (4).

Therefore no cyclic `(1111,186,31)` difference set exists.

If the multiplier normalization and quotient identity are confirmed in verification, this is a full nonexistence proof for the exact selected row.

## family_affinity
This fits the classic cyclic-difference-set lane where a prime divisor of `n` yields a useful multiplier, a small prime factor of `v` creates a short exceptional orbit, and quotient contraction against the complementary prime factor turns the problem into a rigid Diophantine profile.

What scales:

- the multiplier-first setup,
- orbit counting on `pq`-order cyclic groups,
- quotient-count identities against one prime-factor subgroup.

What does not automatically scale:

- the final congruence `c_0 ≡ 1 (mod 25)` uses the very specific orbit profile forced by `v = 11 * 101` and `ord_101(5) = 25`,
- the contradiction depends on the exact parameter pair `(k,lambda) = (186,31)`.

## generalization_signal
There is a real reusable template here:

1. pick a prime `p | n` with `gcd(p,v)=1`,
2. normalize to a `p`-invariant translate,
3. classify orbit lengths on the CRT factors of `v`,
4. contract over one prime-factor subgroup,
5. compare the allowed quotient-count tuples with orbit-forced congruences.

The likely theorem slice suggested by this instance is not a broad classification theorem yet, but a local obstruction theorem for cyclic `pq` cases where one multiplier creates a single short-orbit subgroup and a uniform long-orbit complement.

## proof_template_reuse
Reusable proof template:

- first multiplier theorem for a prime dividing `n`,
- translate to fixed-point form when `gcd(p-1,v)=1`,
- use CRT to read off orbit lengths,
- derive a forced orbit inventory from `k`,
- pass to quotient fiber counts,
- solve a two-parameter Diophantine system,
- finish with an orbit congruence contradiction.

This template should transfer best to other residual cyclic rows with:

- `v = p_1 p_2`,
- a small multiplier prime dividing `n`,
- and nontrivial order separation on the two prime factors of `v`.

## candidate_theorem_slice
Exact slice visible from the current argument:

> Let `D` be a `5`-invariant subset of `Z_11 × Z_101` with `(1111,186,31)` difference-set quotient data. Then the fiber counts over the quotient by `{0} × Z_101` are simultaneously forced to satisfy `c_0 ∈ {6,21}` and `c_0 ≡ 1 (mod 25)`, which is impossible.

This slice is already theorem-shaped and is the core technical proposition behind the full nonexistence statement.

## smallest_param_shift_to_test
Most informative next shift if verification confirms the proof:

- another cyclic residual row with the same proof template features:
  `v = 11q`, `5 | n`, `gcd(4,v)=1`, and `ord_q(5) = 25` or another single long orbit length that makes one quotient fiber congruence visible.

The immediate point is not "nearby numerically" but "nearby structurally": the proof needs a short-orbit subgroup plus a long-orbit complement.

## why_this_is_or_is_not_publishable
If the present argument survives verification, it is not too thin for the micro-paper lane.

- The exact title theorem would be: `There is no cyclic (1111,186,31) difference set.`
- A successful solve here would already be within the target 70-90% paper band; my current estimate is about 0.8 to 0.85 of a short paper.
- Minimal remaining packaging work:
  - write the multiplier normalization as a formal lemma with citation,
  - present the orbit decomposition under `5`,
  - state the quotient identity cleanly,
  - include one paragraph locating the row inside Baumert-Gordon Table 3,
  - run bounded verification / prior-art checking.

At this point the package is much closer to a paper-shaped claim than to a bare instance. The main residual risk is verification, not theorem shape.

## paper_shape_support
Paper-shaped support now visible:

- title theorem: nonexistence of a cyclic `(1111,186,31)` difference set,
- core mechanism: a short multiplier-orbit argument plus one quotient-count contradiction,
- smallest supporting theorem slice: the impossible quotient-fiber profile under `5`-invariance,
- natural boundary remark: the obstruction uses the exact orbit arithmetic of `11 * 101` and does not yet classify all cyclic residual rows.

One immediate corollary / remark:

> Any cyclic `(1111,186,31)` difference set would force a `5`-invariant model with zero fiber count both congruent to `1 mod 25` and equal to `6` or `21`; hence the contradiction is intrinsic to the exact row, not to a failed search.

## boundary_remark
This is still an instance-level result, but it is a strong instance-level result with clear theorem shape.

The argument does not yet prove a broader family theorem. What scales is the multiplier-plus-contraction template; what does not automatically scale is the final modulus-25 contradiction. So the current packet is already closer to a paper-shaped claim than to a mere computational witness, but it remains centered on one exact Table 3 row.

## likely_failure_points
1. The multiplier normalization step should be checked against the exact version of the standard theorem being used.
2. The claim that all non-`H` nonzero elements have orbit length `25` should be rechecked carefully in CRT coordinates.
3. The quotient identity `sum c_r^2 = k + lambda(|K|-1)` should be verified explicitly.
4. The Diophantine reduction to `c_0 ∈ {6,21}` should be recomputed independently.
5. Verification should check whether an equivalent contradiction was already recorded in the literature, since solve runs with web disabled.

## what_verify_should_check
1. Confirm the exact multiplier citation and the translate-to-fixed-set normalization when `gcd(5-1,1111)=1`.
2. Recompute the orbit lengths of multiplication by `5` on `Z_11 × Z_101`.
3. Re-derive the contraction identities over the subgroup of order `101`.
4. Independently solve the quotient-count equations and confirm the only possibilities are `c_0 = 6` or `21`.
5. Check that the zero-fiber congruence `c_0 ≡ 1 (mod 25)` has no hidden exceptions.
6. Perform the bounded rediscovery search on the exact tuple `(1111,186,31)` and alternate cyclic notation.

## verify_rediscovery
- PASS 1 used a bounded web sweep on the exact tuple, alternate notation, the Baumert-Gordon source surface, and Daniel Gordon's difference-set pages.
- Queries included exact forms such as `(1111,186,31)` and reordered / alternate cyclic notation such as `1111 186 31 cyclic difference set`.
- The canonical source surface still points back to Baumert-Gordon's Table 3 survivor list; the bounded search did not surface a later paper, database entry, theorem, proposition, example, observation, or corollary explicitly settling this exact cyclic row.
- This is not a proof of novelty, but within the allotted verify budget I did not find rediscovery evidence.

## verify_faithfulness
- The solved claim matches the intended statement exactly: the packet asks whether `C_1111` admits a `(1111,186,31)` difference set, and the proof attempts the exact negation of that statement.
- I did not find wrong-theorem drift, weakened proxy substitution, parameter drift, or a switch from cyclic existence to a different ambient-group question.
- The technical core proposition in the record is genuinely in service of the exact title theorem rather than a nearby variant.

## verify_proof
- I did not find a first incorrect step.
- The multiplier step is standard: since `5 | n = 155` and `gcd(5,1111) = 1`, `5` is a multiplier for an abelian difference set; since `gcd(5-1,1111) = 1`, the usual translate-to-fixed-set normalization is available.
- The orbit analysis checks out in CRT coordinates `Z_11 x Z_101`:
  - `ord_11(5) = 5`,
  - `ord_101(5) = 25`,
  - so the only orbit lengths are `1` at `(0,0)`, `5` on `H \\ {0}`, and `25` on every other nonzero element.
- The size decomposition is then forced:
  - a `5`-invariant set of size `186` must contain the singleton orbit,
  - there are only two length-5 orbits,
  - hence the candidate contains all of `H` and exactly seven length-25 orbits.
- The quotient computation over `K = {0} x Z_101` is correct. Writing `c_r = |D ∩ ({r} x Z_101)|`, the contraction identity gives
  - `sum_r c_r = 186`,
  - `sum_r c_r^2 = n + lambda|K| = 155 + 31*101 = 3286 = k + lambda(|K|-1)`.
- Because `5` acts on `Z_11^*` with two length-5 cycles, the fiber profile has the form `(x,a,a,a,a,a,b,b,b,b,b)`, giving
  - `x + 5a + 5b = 186`,
  - `x^2 + 5a^2 + 5b^2 = 3286`.
- An independent arithmetic recomputation confirms the only integer solutions are `(x,a,b) = (6,19,17)` or `(21,20,13)` up to swapping `a,b`, so `c_0 ∈ {6,21}`.
- The orbit inventory separately forces `c_0 = 1 + 25r` because `(0,0)` contributes one point to the zero fiber and each chosen length-25 orbit contributes either `0` or `25` points there.
- Since `6` and `21` are not `1 mod 25`, the contradiction is genuine.

## verify_adversarial
- No checker file or search artifact exists for this slug; the proof is reasoning-only.
- I reran the key modular arithmetic locally:
  - `5^5 ≡ 1 (mod 11)`,
  - `5^5 ≡ 95 != 1 (mod 101)`,
  - `5^25 ≡ 1 (mod 101)`,
  confirming the stated orbit orders.
- I independently enumerated the contraction system and recovered only the two possible zero-fiber values `6` and `21`.
- I separately forced the orbit-side congruence `c_0 ∈ {1,26,51,76,101}` and checked that none of those values solve the contraction system.
- I did not find a hidden case or computational escape hatch.

## verify_theorem_worthiness
- Exactness: strong. The argument targets the exact selected row and yields the exact intended nonexistence statement.
- Novelty: bounded-positive. PASS 1 did not expose rediscovery, but novelty is still only as strong as the bounded search budget.
- Reproducibility: good. The proof uses a short multiplier citation, explicit orbit counts, and a two-equation integer check; nothing depends on opaque computation.
- Lean readiness: not yet the shortest path. The claim is theorem-shaped and formalizable in principle, but the immediate remaining work is publication audit and literature packaging rather than formal sealing.
- Paper leverage: good for the micro-paper lane. If this proof is correct and later Lean-sealed, it already supplies most of a short residual-case note anchored by Baumert-Gordon Table 3.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? Yes.
- What percentage of the paper would one solve already provide? About `0.84`.
- What title theorem is actually visible? `There is no cyclic (1111,186,31) difference set.`
- What part of the argument scales? The multiplier-normalization plus orbit-and-contraction template for cyclic `pq` cases.
- What part clearly does not? The final `c_0 ≡ 1 (mod 25)` contradiction is specific to the `11 * 101` orbit arithmetic and this exact parameter row.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? No. The best honest status is `SLICE_CANDIDATE`: the result is more than a bare isolated instance, but the publication packet is not yet audited as fully paper-ready.

## verify_verdict
- `verify_verdict = "VERIFIED"`
- `classification = "CANDIDATE"`
- `confidence = "high"`
- `publication_status = "SLICE_CANDIDATE"`
- `lean_ready = false`
- `lean_packet_seal = false`
- `next_action = "run_publication_audit"`

## minimal_repair_if_any
- No mathematical repair was needed.
- The only conservative cleanup is expository: in the final writeup, state the quotient identity both as `n + lambda|K|` and as `k + lambda(|K|-1)` so the coefficient calculation is transparent to a skeptical reader.

## publication_prior_art_audit
- Exact statement search on `"(1111,186,31)" cyclic difference set` and `"1111 186 31" difference set` surfaced the Baumert-Gordon 2004 source and did not surface a later theorem, proposition, corollary, example, observation, or database entry explicitly settling this exact cyclic row.
- Alternate-notation search on `v=1111, k=186, lambda=31`, `C_1111`, and reordered tuple forms likewise did not expose a later discharge.
- Canonical-source check: Baumert-Gordon 2004 still isolates `1111,186,31,155` among the open cyclic cases with `150 <= k <= 300`, and Section 3.2 gives the contracted-multiplier framework used here. The worked nonexistence example in Section 3.3 is `(429,108,27)`, not the selected row, so the paper does not already settle this case by theorem/example under another label.
- One outside-status pass on Daniel Gordon's current publications surface did not reveal a later paper devoted to `(1111,186,31)` or a follow-up title obviously implying it.
- Because that publications page listed the later paper `On Difference sets with small lambda` (2022), I ran one bounded follow-up check there; it did not surface `1111` or an exact settlement of the present tuple.
- Conservative audit conclusion: no rediscovery evidence appeared in the bounded pass, but the novelty claim is still bounded-search confidence rather than exhaustive-survey confidence.

## publication_statement_faithfulness
- The strongest honest claim remains exactly the selected theorem: `There is no cyclic (1111,186,31) difference set.`
- The proof packet does not drift to a different ambient group, a weaker obstruction, or a mere necessary condition. It addresses the exact cyclic existence question named in the working packet and selected problem file.
- The canonical source anchor and the local proof still talk about the same residual row, so there is no statement mismatch between source, solve record, and audit output.

## publication_theorem_worthiness
- Is the strongest honest claim stronger than `here is an example`? Yes. It is an exact nonexistence theorem for a named residual row.
- Is there a real title theorem, theorem slice, or counterexample theorem here? Yes: `No cyclic (1111,186,31) difference set exists.`
- Is the proof structural or merely instance-specific? It is structural enough for a note: the core uses a multiplier normalization, CRT orbit structure, and contracted fiber identities. The final contradiction is tuple-specific, so the result is a sharp slice theorem rather than a broad classification theorem.
- Would this survive a referee asking `what is the theorem?` Yes. The theorem is exact, short to state, and anchored to a published survivor list.
- Is the claim still too dependent on hand-picked small cases? No in the relevant sense. The proof is not a brute-force witness search or an anecdotal small example; it is a concise arithmetic obstruction tailored to one exact case.

## publication_publishability
- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? Yes.
- What percentage of the paper would one solve already provide? About `0.85`.
- Is the remaining gap genuinely small, or did the candidate only look attractive before audit? The remaining gap is genuinely small: clean exposition, precise citation of the multiplier normalization, and a compact literature paragraph are the main remaining tasks.
- If this were not paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes; but after audit I do not think expansion is needed. The right move is to package the exact note, not to inflate it into a broader campaign.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Lean is secondary seal work. It would strengthen archival exactness, but it is not the reason this packet is or is not publishable.

## publication_packet_audit
- `publication_status = PAPER_READY` is justified on the current bounded record.
- The packet already contains the title theorem, the proof spine, the source anchor, and preserved artifacts in `record.md` / `status.json`.
- The paper narrative is clean: Baumert-Gordon isolate the row; the local argument closes it by a short multiplier-orbit and contraction contradiction; the writeup burden is bounded.
- The main caution is still literature scope, not theorem shape. I did not find rediscovery, but the audit should be understood as a bounded publication check rather than a full survey.

## micro_paper_audit
- Pass. This is a genuine micro-paper packet rather than a feeder ladder.
- Single-solve-to-paper fraction remains above the lane threshold after skeptical checking because the solve is already the title theorem and not merely supporting evidence.
- Editorial overhead is still low, immediate corollary pressure is low, and the lack of brute-force search keeps the packet compact.
- The exact-row nature of the claim is acceptable here because the row is source-stable, theorem-shaped, and already reads like the main result of a short note.

## strongest_honest_claim
No cyclic `(1111,186,31)` difference set exists; a short `5`-multiplier orbit-and-contraction argument on `Z_11 x Z_101` gives the contradiction, and the bounded publication audit did not uncover a prior settlement of this exact row.

## paper_title_hint
On the Nonexistence of a Cyclic `(1111,186,31)` Difference Set

## next_action
Mark the packet `PAPER_READY`, move it to the HUMAN_READY lane with proof artifacts preserved, and treat Lean as a non-blocking secondary formal seal for later archival completion.
