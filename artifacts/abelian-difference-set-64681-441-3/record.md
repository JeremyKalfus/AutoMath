# Solve Record: An Abelian (64681,441,3)-Difference Set

## statement_lock
Active slug: `abelian-difference-set-64681-441-3`.

Active title theorem target: **No abelian group of order 64681 admits a (64681,441,3)-difference set.**

Locked intended statement:
Determine whether any abelian group of order `64681 = 71 · 911` admits a `(64681,441,3)`-difference set.

Solve-stage position:
- A successful exact solve here would already be about `0.8` of a micro-paper.
- The exact title theorem, if the present argument survives verification, is: `No abelian (64681,441,3)-difference set exists.`
- Minimal remaining packaging work would be: cite the multiplier theorem used below in the precise form needed, note Gordon's Table 4 frontier context, and compress the orbit-count proof into short-note form.

## definitions
- A `(v,k,lambda)`-difference set in a finite group `G` is a `k`-subset `D` such that every nonidentity element of `G` occurs exactly `lambda` times as `d1 d2^{-1}` with `d1,d2 in D`.
- For an abelian difference set, the order is `n = k - lambda`. Here `n = 441 - 3 = 438 = 2 · 3 · 73`.
- Since `64681 = 71 · 911` is squarefree and the group is assumed abelian, every abelian group of order `64681` is cyclic. So the problem reduces to a cyclic difference set in `C_64681`.
- Standard multiplier fact used below: for a cyclic `(v,k,lambda)`-difference set, any prime `r` dividing `n` with `gcd(r,v)=1` is a numerical multiplier.
- Standard translation-normalization fact used below: if `rD = D + s` and `gcd(r-1,v)=1`, then after translating by a suitable group element one may assume `rD = D`.

## approach_A
Structural / invariant route: force invariance under the multiplier `r = 3` and count its orbits.

Reason:
- `3 | n = 438` and `gcd(3,64681)=1`, so `3` is a multiplier in the cyclic case.
- Also `gcd(3-1,64681)=gcd(2,64681)=1`, so some translate of any putative difference set is fixed setwise by multiplication by `3`.
- Therefore any putative difference set has size equal to a sum of orbit sizes of the map `x -> 3x` on `C_64681`.

Orbit structure:
- `0` is a fixed point, contributing one orbit of size `1`.
- On nonzero multiples of `911`, orbit size is `ord_71(3) = 35`.
- On nonzero multiples of `71`, orbit size is `ord_911(3) = 455`.
- On units, orbit size is `ord_64681(3) = lcm(35,455) = 455`.

So every `3`-invariant subset of `C_64681` has size
`delta + 35a + 455b`
with `delta in {0,1}` and `a,b >= 0`.

But `441` is neither of the form `35a + 455b` nor `1 + 35a + 455b`:
- `441` is not divisible by `35`;
- `440` is not divisible by `35`;
- `455 > 441`, so `b = 0`.

This gives an immediate contradiction if the multiplier and normalization steps are valid as stated.

## approach_B
Construction / extremal / contradiction route: quotient-fiber intersection numbers over the subgroup of order `911` or `71`.

Setup:
- View a putative difference set `D` in `C_64681`.
- Push `D` to the quotient `C_64681 / C_911`, which has order `71`, and let the fiber sizes be `a_0,...,a_70`.
- Then `sum a_i = 441`.
- Group-ring contraction gives `sum a_i^2 = n + lambda · 911 = 438 + 3·911 = 3171`.

This route asks whether a `71`-tuple of integers in `[0,911]` with those first two moments can also satisfy the quotient-difference constraints and multiplier symmetries. It may yield a contradiction, but it is less direct here than the multiplier-orbit route and likely requires extra bookkeeping.

Why not chosen:
- It does not close the instance as cleanly as the `3`-orbit semigroup obstruction.
- It is better used as a secondary check or a route for neighboring parameters if the multiplier argument fails.

## lemma_graph
1. `64681 = 71 · 911`, so any abelian group of order `64681` is cyclic.
2. For a cyclic difference set with parameters `(64681,441,3)`, the order is `n = 438`, so `3 | n` and `gcd(3,64681)=1`.
3. By the cyclic multiplier theorem, `3` is a numerical multiplier.
4. By translation normalization, because `gcd(3-1,64681)=1`, some translate of a putative difference set is fixed by multiplication by `3`.
5. The `3`-orbits on `C_64681` have sizes only `1`, `35`, and `455`.
6. `441` cannot be expressed as a sum of orbit sizes from `{1,35,455}`.
7. Contradiction. Therefore no abelian `(64681,441,3)`-difference set exists.

## chosen_plan
Choose Approach A.

Reason:
- It uses the smallest amount of additional structure beyond the packet.
- It targets a full theorem, not a partial slice.
- If correct, it closes the exact intended statement with a short proof that already looks like the body of a one-theorem note.

What extra structure would make this paper-shaped if the main claim closes?
- An explicit citation of the multiplier theorem in the exact cyclic form used.
- A compact orbit table for multiplication by `3` modulo `71`, `911`, and `64681`.
- One short contextual paragraph tying the argument back to Gordon's residual Table 4 list.
- One brief remark explaining that the method is reusable for other residual squarefree-order cases when a multiplier gives a size-semigroup obstruction.

## self_checks
- After statement lock: the target is still the exact intended theorem, not a weaker witness-only claim.
- After group-structure reduction: no abelian noncyclic case survives because `71` and `911` are distinct primes.
- After choosing the multiplier route: the only real load-bearing input is the standard cyclic multiplier theorem.
- After orbit counting: the size obstruction is exact and does not rely on probabilistic or search-heavy evidence.
- After the final contradiction: this is theorem-shaped, but verification must still check the literature citation and the precise multiplier theorem hypotheses.

## code_used
Minimal code only.

Used one-off Python checks to verify the arithmetic facts supporting the chosen proof:
- `ord_71(3) = 35`
- `ord_911(3) = 455`
- `ord_64681(3) = 455`
- the orbit multiset for `x -> 3x` on `C_64681` is exactly `[(1,1), (35,2), (455,142)]`
- there is no representation of `441` as a sum of these orbit sizes

No search, SAT, ILP, CP-SAT, brute force construction, or broad computation was used.

## result
Claim:
There is no abelian `(64681,441,3)`-difference set.

Proof attempt:

Let `G` be an abelian group of order `64681 = 71 · 911`. Since the order is squarefree, `G` is cyclic, so it is enough to rule out a cyclic difference set in `C_64681`.

Assume for contradiction that `D` is a subset of `C_64681` forming a `(64681,441,3)`-difference set. Its order is
`n = k - lambda = 441 - 3 = 438 = 2 · 3 · 73`.

Because `3 | n` and `gcd(3,64681)=1`, the standard cyclic multiplier theorem makes `3` a numerical multiplier of `D`. Hence there exists some `s in C_64681` such that
`3D = D + s`.

Since `gcd(3-1,64681)=gcd(2,64681)=1`, choose `g in C_64681` satisfying
`(3-1)g = -s`.
Then for `D' = D + g` we have
`3D' = 3D + 3g = D + s + 3g = D + g = D'`.
So after translation we may assume from the start that `3D = D`.

Therefore `D` is a union of orbits of the permutation `x -> 3x` on `C_64681`.

Now compute orbit sizes.

For `x = 0`, the orbit has size `1`.

For nonzero elements divisible by `911`, write `x = 911y` with `y not congruent 0 mod 71`. Then orbit size is the order of `3` modulo `71`, namely `35`.

For nonzero elements divisible by `71`, write `x = 71z` with `z not congruent 0 mod 911`. Then orbit size is the order of `3` modulo `911`, namely `455`.

For units, orbit size is the order of `3` modulo `64681`, which is
`lcm(ord_71(3), ord_911(3)) = lcm(35,455) = 455`.

Hence every `3`-invariant subset of `C_64681` has cardinality
`delta + 35a + 455b`
for some `delta in {0,1}` and integers `a,b >= 0`.

But `|D| = 441`, and this is impossible:
- if `b >= 1`, then `delta + 35a + 455b >= 455 > 441`;
- if `b = 0` and `delta = 0`, then `441` must be divisible by `35`, which it is not;
- if `b = 0` and `delta = 1`, then `440` must be divisible by `35`, which it is not.

This contradiction proves that no cyclic, hence no abelian, `(64681,441,3)`-difference set exists.

Self-check on the proof:
- The contradiction is exact and short.
- The only external theorem needed is the standard multiplier theorem for cyclic difference sets.
- The rest is elementary orbit counting.

Smallest supporting theorem slice:
For this parameter, the multiplier `3` alone forces a forbidden orbit-size semigroup, so no appeal to deeper search or to Gordon's sharper elimination machinery is needed beyond the frontier context.

Immediate corollary / natural remark:
Any cyclic residual case with squarefree `v` and a multiplier `r | n` such that `k` is not a sum of the resulting `r`-orbit sizes is ruled out by the same template.

Why this instance matters:
It would remove one of Gordon's six residual abelian `lambda = 3` parameter sets by a very short group-uniform obstruction.

What part of the argument scales:
- cyclic reduction for squarefree abelian orders;
- multiplier normalization when `gcd(r-1,v)=1`;
- orbit-size semigroup obstruction once the relevant multiplicative orders are sparse.

What part does not automatically scale:
- the final contradiction depends on the specific incompatibility between `k = 441` and the orbit sizes `1,35,455`;
- cases with denser orbit spectra or non-squarefree `v` may need fiber-count or character arguments instead.

What theorem slice is suggested:
- a short lemma excluding cyclic `(v,k,lambda)` difference sets whenever a forced multiplier yields orbit sizes whose additive semigroup misses `k`.

What next parameter shifts would help most:
- check whether Gordon's other residual squarefree-order tuples admit the same forced-multiplier orbit contradiction;
- for this exact tuple, verify whether multipliers `2` or `73` give an equally short redundant obstruction that could strengthen the writeup.

Is this still just an instance or already closer to a paper-shaped claim?
- Closer to a paper-shaped claim. It is still a single residual instance, but it closes the exact title theorem with a short, reusable obstruction template.

## family_affinity
Strong affinity with the cyclic / abelian `lambda = 3` residual family isolated by Gordon, especially squarefree-order cases where multiplier orbits are easy to enumerate.

## generalization_signal
Moderate.

The proof pattern plausibly extends to any residual case with:
- squarefree abelian order forcing cyclicity,
- a prime divisor `r` of `n = k - lambda` with `gcd(r,v)=1`,
- `gcd(r-1,v)=1`,
- and orbit sizes under `x -> rx` whose additive semigroup misses `k`.

That is a real theorem-facing signal, but the present writeup only certifies the current tuple.

## proof_template_reuse
High for nearby cyclic `pq`-order cases; moderate outside that lane.

Reusable template:
1. reduce abelian squarefree order to the cyclic case;
2. pick a forced multiplier `r | n`;
3. normalize to an `r`-invariant translate;
4. classify orbit sizes on `0`, each prime-divisor layer, and units;
5. show `k` is not in the orbit-size semigroup.

## candidate_theorem_slice
Candidate slice:

Let `v = pq` with distinct primes `p,q`, and let `D` be a cyclic `(v,k,lambda)`-difference set of order `n = k - lambda`. Suppose a prime `r | n` satisfies `gcd(r,v)=1` and `gcd(r-1,v)=1`. If `k` is not representable as a sum of orbit sizes of `x -> rx` on `C_v`, equivalently not of the form
`delta + a·ord_p(r) + b·ord_q(r) + c·lcm(ord_p(r),ord_q(r))`
with `delta in {0,1}` and `a,b,c >= 0`,
then no such difference set exists.

For the current tuple, `p=71`, `q=911`, `r=3`, and the orbit-size set is `{1,35,455}`.

## smallest_param_shift_to_test
- First shift: test Gordon's other residual `lambda = 3` cases with squarefree `v` for the same multiplier-orbit semigroup obstruction.
- Second shift: on this tuple, test whether `r = 2` or `r = 73` yields a second independent orbit-size contradiction suitable for a cleaner note.

## why_this_is_or_is_not_publishable
If the multiplier citation and novelty check survive verification, this is close to publishable as a short note.

Why it is paper-shaped:
- It settles an exact residual frontier case.
- The proof is short, self-contained after one standard theorem citation, and group-uniform.
- The note would have a clear title theorem and a natural literature anchor.

Why I am still conservative at solve stage:
- the proof leans on a standard multiplier theorem that should be cited carefully in `verify`;
- novelty / rediscovery checking is still outstanding by stage design;
- no broader slice has yet been proved beyond the current parameter.

Current judgment:
- not too thin for the micro-paper lane if verified cleanly;
- still not ready to call `PAPER_READY` from solve alone.

## paper_shape_support
The result needs only a small support package to become a note:
- a one-paragraph recap of Gordon's residual Table 4 frontier;
- a cited multiplier theorem statement;
- the orbit-count lemma as the proof core;
- one short remark on reuse for other squarefree residual cases.

This is exactly the kind of solve where the mathematics itself is already 70-90% of the paper.

## boundary_remark
Boundary remark:
This argument is strong because the multiplier `3` has only three orbit sizes on `C_64681`: `1`, `35`, and `455`. The obstruction would disappear immediately if `k` landed in the corresponding additive semigroup, so the present proof is structurally sharp for this exact parameter but not automatically universal across the whole `lambda = 3` frontier.

## likely_failure_points
- The exact statement of the multiplier theorem must match the cyclic setting used here.
- Verification should check that no extra hypothesis beyond `r | n` and `gcd(r,v)=1` is needed.
- The normalization step must be stated on the correct additive / multiplicative notation convention for `C_64681`.
- The orbit-size computation should be rechecked directly from the orders of `3 mod 71` and `3 mod 911`.
- Prior art may already contain this exact short obstruction even if the packet currently treats the case as open.

## what_verify_should_check
- Confirm the precise literature citation and hypotheses for the cyclic first multiplier theorem used here.
- Recompute `ord_71(3)=35`, `ord_911(3)=455`, and the orbit decomposition under `x -> 3x`.
- Check whether Gordon or earlier sources already effectively imply this exact obstruction.

## verify_rediscovery
PASS 1 bounded prior-art audit completed within budget.

Search patterns used:
- exact tuple search for `(64681,441,3)` and nearby exact notation;
- alternate family phrasing for abelian `lambda = 3` difference sets;
- the canonical Gordon source itself;
- same-source checks around Table 4 / theorem references;
- one bounded recent-status search for any later explicit resolution.

Findings:
- Gordon's 2022 paper still lists `(64681,441,3)` in Table 4 as one of the six remaining open abelian `(v,k,3)` cases after the source's eliminations.
- The bounded search did not uncover any later paper, note, repository entry, or discussion explicitly resolving the exact tuple.
- Within the audit budget, rediscovery was not established.

Verdict for PASS 1:
- `verify_verdict != REDISCOVERY`
- the exact intended statement still looks frontier-novel on the bounded audit, but publication audit should still do one final conservative literature pass later.

## verify_faithfulness
The claimed result matches the intended statement after one standard reduction:
- intended statement: determine whether any abelian group of order `64681` admits a `(64681,441,3)`-difference set;
- since `64681 = 71 * 911` is squarefree, every abelian group of that order is cyclic;
- a cyclic nonexistence proof therefore settles the exact intended abelian statement.

No wrong-theorem drift, quantifier drift, or proxy-statement substitution was found. The solver aimed at the exact nonexistence theorem for the selected tuple.

## verify_proof
First incorrect step found in the solve proof as written:
- the record states as a "standard" fact that any prime `r` dividing `n = k - lambda` with `gcd(r,v)=1` is a multiplier in the cyclic case, then applies this with `r = 3`;
- that is too strong for the cited Gordon framework. The classical first multiplier theorem used in this lane requires a prime multiplier `p > lambda`. Here `3 = lambda`, so the argument does not justify that `3` is a multiplier.

Tiny conservative repair:
- replace `r = 3` by `r = 73`;
- here `73 | n = 438`, `73 > lambda = 3`, and `gcd(73,64681)=1`, so the standard first multiplier theorem applies;
- also `gcd(73 - 1, 64681) = gcd(72,64681) = 1`, so after translation one may assume `73D = D`.

With that repair, the orbit argument closes cleanly:
- `ord_71(73) = 35`;
- `ord_911(73) = 35`;
- hence every nonzero orbit of `x -> 73x` on `C_64681` has size `35`, while `0` is fixed;
- any `73`-invariant subset therefore has size `delta + 35a` with `delta in {0,1}`;
- `441` is neither divisible by `35` nor of the form `1 + 35a`, since `440` is not divisible by `35`.

After this repair, no further incorrect step was found in the proof skeleton. The repaired proof is short, exact, and group-uniform.

## verify_adversarial
I reran the arithmetic checks directly.

For the original solve argument:
- the orbit arithmetic for `r = 3` is internally consistent, but the multiplier theorem hypothesis is not justified there, so that route cannot be accepted as written.

For the repaired argument:
- direct computation gave `ord_71(73) = 35`, `ord_911(73) = 35`, and `ord_64681(73) = 35`;
- direct orbit decomposition under `x -> 73x (mod 64681)` gave unique orbit sizes `[1,35]`, with one fixed point and `1848` nonzero `35`-cycles;
- a direct semigroup check found no representation of `441` as `delta + 35a` with `delta in {0,1}`.

No construction, checker, or counterexample artifact existed to rerun beyond these arithmetic checks. The repaired contradiction survived the adversarial pass.

## publication_prior_art_audit
Bounded publication audit run on `2026-04-15`.

Canonical-source check:
- Gordon, *On difference sets with small lambda* (J. Algebraic Combinatorics 55, 2022), still leaves `(64681,441,3)` in Table 4 as one of the six remaining open abelian `(v,k,3)` cases after the paper's eliminations.
- The source's same-paper elimination landmarks are Theorems 2, 3, and 4 together with the Lander and Mann tests; within that canonical source check, no theorem, proposition, example, corollary, observation, or sufficient-condition statement was found that already settles this exact tuple.

Exact-statement / alternate-notation search:
- Searched the exact tuple forms `(64681,441,3)`, `64681,441,3`, and the family phrasings `abelian difference set`, `cyclic difference set`, and `71·911`.
- The bounded web pass did not uncover any later paper, note, preprint, or repository page explicitly resolving the exact tuple.

Outside-source status pass:
- The La Jolla Difference Set Repository remains the active public status surface for difference-set parameters with `v < 100000`, and its frozen `v1.2` data release is mirrored on Zenodo.
- Within the bounded search budget, that outside-source pass did not surface any explicit post-2022 resolution of the current tuple.

Conservative verdict:
- `REDISCOVERY` was not established.
- On the bounded audit, the claim still behaves like a residual frontier case rather than a known old instance.

## publication_statement_faithfulness
The repaired proof remains faithful to the selected theorem target.

- Intended statement: determine whether any abelian group of order `64681` admits a `(64681,441,3)`-difference set.
- Strongest audited proof: no abelian group of order `64681` admits such a difference set.
- Faithfulness reason: `64681 = 71 * 911` is squarefree, so every abelian group of that order is cyclic. A cyclic nonexistence proof therefore settles the exact intended abelian statement, not a proxy theorem.

No quantifier drift, scope drift, or weaker substitute claim was introduced by the repaired `r = 73` multiplier route.

## publication_theorem_worthiness
Required judgment:
- Stronger than "here is an example": yes. This is an exact group-uniform nonexistence theorem for the selected frontier tuple.
- Real title theorem / theorem slice: yes. "No abelian `(64681,441,3)`-difference set exists" is a clean title theorem for a short note.
- Structural or merely instance-specific: structural-but-narrow. The statement is a single parameter slice, but the proof is not a hand-picked example check; it is a multiplier-orbit obstruction that applies uniformly to every abelian group of order `64681`.
- Would it survive "what is the theorem?": yes. The theorem is the exact residual-case nonexistence result.
- Too dependent on hand-picked small cases: no. The proof does not rest on enumerating small constructions or on ad hoc computation, though the final contradiction is tailored to this tuple.

Bottom line:
- theorem-worthiness passes;
- the packet is still narrow, but it is narrow in the right micro-paper way.

## publication_publishability
Required judgment:
- Would this result already constitute most of a publishable note if correct and verified in the current bounded sense: yes.
- Estimated solve-to-paper fraction: about `0.88`.
- Remaining gap size: genuinely small.

Why the remaining gap is small:
- the frontier anchor is already supplied by Gordon's Table 4 residual list;
- the repaired proof is short and theorem-shaped;
- the writeup burden is mostly citation polish, a one-paragraph source recap, and compression of the orbit-count proof into paper prose.

Referee-facing judgment:
- A referee asking "what is the theorem?" receives a precise residual-case theorem, not a computation dump.
- A referee asking "why is this publishable?" receives a clean removal of one of six explicitly isolated abelian `lambda = 3` residual cases.

Lean judgment:
- Lean would be a later archival seal, not a prerequisite for publication status here.
- In human publication terms, the current packet is already ahead of the Lean bottleneck.

## publication_packet_audit
Packet quality judgment: high.

Reasons:
- exact frontier claim;
- short repaired proof with a single standard multiplier input;
- bounded prior-art pass did not find rediscovery;
- proof artifacts are preserved well enough for manuscript assembly and later Lean queue handoff.

Notable risk that remains:
- the bounded web audit is still bounded, so the publication confidence should remain `medium-high` rather than maximal.

Decision:
- promote from `SLICE_CANDIDATE` to `PAPER_READY`.
- do not expand this into a broader theorem program before moving the packet forward.

## micro_paper_audit
Micro-paper verdict: pass.

Required judgment:
- Is there a real title theorem here: yes.
- Is the claim still too dependent on small cases: no.
- If not paper-ready, should it be moved aside rather than expanded: not applicable, because it is paper-ready on the bounded audit.
- Would Lean directly seal the packet, or only provide later polish: later seal / secondary lane.

Why this passes the lane:
- one solve removes one of Gordon's six residual abelian `lambda = 3` cases;
- the note does not need a feeder ladder;
- the proof is compact enough that the mathematics itself already supplies most of the final paper;
- the family anchor is strong enough that exact-case narrowness does not collapse into "mere example" status.

Net assessment:
- this candidate did not merely look attractive before audit;
- it remains a genuine one-shot micro-paper packet after audit.

## strongest_honest_claim
After the repaired `r = 73` multiplier argument and the bounded prior-art audit, the strongest honest claim is:

**No abelian group of order `64681` admits a `(64681,441,3)`-difference set.**

On the current bounded audit, that theorem is still a frontier residual-case result rather than a rediscovery, and it is strong enough to count as a human-ready micro-paper packet.

## paper_title_hint
**No Abelian `(64681,441,3)`-Difference Set Exists**

## next_action
Promote this artifact to `PAPER_READY` / `human_ready`, preserve the repaired `r = 73` proof as the canonical packet, and hand it off for short manuscript assembly plus non-blocking Lean formalization. Do not broaden the claim into a larger theorem program before the exact residual-case note is captured.

## verify_theorem_worthiness
Exactness:
- yes, after the `73` repair the argument addresses the exact selected theorem.

Novelty:
- bounded PASS 1 did not establish rediscovery;
- because the prior-art search was deliberately narrow, novelty is plausible but should still be carried conservatively into publication audit.

Reproducibility:
- high; the proof depends on one standard multiplier theorem citation plus very small orbit-order computations.

Lean readiness:
- the mathematics is strong enough to formalize eventually, but Lean is not the shortest remaining path right now;
- the immediate remaining work is publication-facing: tighten the citation, state the repaired theorem cleanly, and audit novelty/publication scope.

Paper leverage:
- if correct and later Lean-sealed, this would already constitute most of a publishable note;
- estimated single-solve-to-paper contribution: about `0.78`;
- visible title theorem: `No abelian (64681,441,3)-difference set exists.`

What scales:
- squarefree abelian-order reduction to the cyclic case;
- multiplier normalization when `gcd(r-1,v)=1`;
- orbit-semigroup obstructions when a valid multiplier has sparse orbit spectrum.

What does not clearly scale:
- the final obstruction here is instance-sensitive and depends on the very sparse `73`-orbit spectrum;
- cases with denser orbit sizes or non-squarefree `v` would need different arguments.

Best honest publication status at verify:
- better than `INSTANCE_ONLY`, because this is an anchored residual Gordon Table 4 case with a one-theorem note shape and a small remaining packaging gap;
- still short of `PAPER_READY` until publication audit finishes and the citation / novelty framing is tightened.

## verify_verdict
`VERIFIED`, but only after a tiny conservative repair.

More precisely:
- not a rediscovery on the bounded verify audit;
- not a wrong statement;
- the original proof as written had a real gap at the multiplier step;
- replacing multiplier `3` with valid multiplier `73` repairs the proof without changing the theorem.

Current strongest honest mathematical claim:
- no abelian group of order `64681` admits a `(64681,441,3)`-difference set.

## minimal_repair_if_any
Minimal repair accepted:
- replace every load-bearing use of multiplier `3` by multiplier `73`;
- cite the first multiplier theorem in the form "prime `p > lambda`, `p | n`, `gcd(p,v)=1` implies multiplier";
- recompute the orbit paragraph accordingly: all nonzero `73`-orbits on `C_64681` have size `35`;
- conclude from `441 != delta + 35a`.

This preserves the exact theorem, keeps the proof short, and does not introduce a conceptually different solve path.
