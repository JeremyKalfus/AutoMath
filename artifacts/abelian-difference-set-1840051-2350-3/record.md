## statement_lock

Target statement: determine whether any abelian group of order `1840051` admits a `(1840051,2350,3)`-difference set.

Parameter check:

- `k(k-1) = 2350 * 2349 = 5520150`
- `lambda (v-1) = 3 * 1840050 = 5520150`
- `n = k - lambda = 2347`, which is prime.
- `v = 1840051` is also prime.

Because `v` is prime, every abelian group of order `1840051` is cyclic. So the active problem is exactly:

> Does the cyclic group `C_1840051` admit a `(1840051,2350,3)`-difference set?

Chosen title-theorem direction for this solve attempt:

> There is no abelian (equivalently cyclic) `(1840051,2350,3)`-difference set.

If that nonexistence statement closed cleanly, it would already be about `70%` of a short paper, because Gordon's Table 4 has already isolated this tuple as a residual frontier case.

## definitions

- A `(v,k,lambda)`-difference set in an abelian group `G` is a subset `D` of size `k` such that every nonzero `g in G` has exactly `lambda` ordered representations `g = x-y` with `x,y in D`.
- Here `G = C_p = F_p` additively with `p = 1840051`.
- Let `n = k-lambda = 2347`.
- Since `n` is a prime coprime to `p`, the standard prime-multiplier theorem makes `n` a numerical multiplier.
- Write `a = 2347 mod p` and let `H = <a> <= F_p^*`.

Exact arithmetic used later:

- `p-1 = 1840050 = 2 * 3^3 * 5^2 * 29 * 47`.
- Exhaustive modular-order computation gives `ord_p(2347) = 47`.
- Hence `H` has order `47`.

Conventions for the orbit reduction:

- If `aD = D+s` in additive notation, then translating by `t = (a-1)^(-1)s` replaces `D` by `D-t`, and `(a)(D-t) = D-t`.
- Since `a-1 = 2346` is invertible mod `p`, any candidate can be translated to an `H`-invariant candidate.

## approach_A

Structural / invariant route: force the problem into a quotient-orbit formulation.

1. Use `v` prime to reduce from "abelian" to "cyclic".
2. Use the prime multiplier `n = 2347` and the normalization above to translate any candidate difference set to one fixed by multiplication by `2347`.
3. Since every nonzero `H`-orbit has size `47` and `k = 2350 = 50 * 47`, a fixed candidate cannot contain `0`; it must be a disjoint union of exactly `50` nonzero `H`-orbits.
4. Push the difference-set condition down to the orbit quotient `Q = F_p^* / H`, which has size `(p-1)/47 = 39150`.

This route gives an exact compression of the whole problem to a sparse quotient-cover problem on `39150` orbit classes. It is the best theorem-facing reduction found in this run.

## approach_B

Construction / extremal / contradiction route: try to kill the candidate by local orbit-overproduction.

1. For one selected `H`-orbit `O`, compute the internal difference profile `O-O`.
2. For two selected `H`-orbits `O_x, O_y`, compute the cross-difference profile `O_x - O_y`.
3. If either one orbit alone or one ordered orbit pair already forces multiplicity `> lambda = 3` on some nonzero difference class, the global difference set is impossible.

This route does not close the problem, but it produces useful exact constraints:

- Internal orbit differences are as sparse as possible: each relevant difference orbit gets multiplicity `1`.
- Distinct orbit pairs are also locally mild: every difference orbit gets multiplicity at most `2`.

So a one-orbit or one-pair contradiction is not available here.

## lemma_graph

Proposed proof skeleton:

1. `v = 1840051` prime
   implies the ambient abelian group is uniquely `C_p`.
2. `n = 2347` prime and `gcd(n,p)=1`
   implies `2347` is a valid multiplier candidate.
3. `ord_p(2347)=47`
   implies the multiplier subgroup `H=<2347>` has size `47`.
4. Multiplier normalization
   implies any candidate difference set may be translated to an `H`-invariant set.
5. `k = 2350 = 50*47`
   implies the normalized set avoids `0` and is a union of exactly `50` nonzero `H`-orbits.
6. Orbit-difference calculation
   implies:
   - one selected orbit contributes `46` difference-orbits, each with multiplicity `1`;
   - one ordered pair of distinct selected orbits contributes one of four exact fiber shapes:
     - `47` singles,
     - `45` singles + `1` doubled orbit,
     - `43` singles + `2` doubled orbits,
     - in the special ratio class `-H`, `1` singleton + `23` doubled orbits.
7. Global existence problem
   becomes an exact quotient-cover problem on `Q = F_p^*/H` of size `39150`, with total orbit-level multiplicity exactly `3` on every quotient class.

## chosen_plan

I chose the nonexistence route through the multiplier-orbit compression because:

- `v` prime makes the group structure completely rigid.
- the packet already suggested exploiting the prime `n = 2347`;
- a successful orbit contradiction would be short, group-uniform, and paper-shaped;
- this route stays reasoning-first and uses only tiny exact computations.

Execution:

1. Lock the cyclic reduction.
2. Compute `ord_p(2347)`.
3. Normalize a hypothetical candidate to an `H`-fixed set.
4. Derive the exact `50`-orbit decomposition.
5. Test whether internal or pairwise orbit-difference counts already contradict `lambda = 3`.

The contradiction did not materialize at the one-orbit or one-pair level, so the honest output is a structural reduction, not a solve.

## self_checks

1. Parameter self-check:
   The parameter equation holds exactly, so there is no trivial arithmetic obstruction.

2. Group-type self-check:
   `1840051` was factored directly and is prime, so reducing to the cyclic case is rigorous.

3. Multiplier self-check:
   The modular-order computation gave `ord_p(2347)=47`, not something larger than `k`.
   So Gordon's cyclic bound `|M| <= k` does not by itself obstruct this tuple.

4. Orbit-size self-check:
   In a prime field, any nonzero `H`-orbit has size `47`, and `2350` is divisible by `47`.
   Therefore the normalized candidate must avoid `0`.

5. Local-contradiction self-check:
   Exhaustive quotient computations show max local multiplicity `1` for one orbit and `2` for one distinct orbit pair.
   So the current nonexistence attempt does not overclaim.

## code_used

Yes, but only tiny exact arithmetic / verification code.

Used code for:

- direct trial-division factoring of `v`, `k`, and `n`;
- exact factorization of `p-1`;
- exact computation of `ord_p(2347)=47`;
- exhaustive labeling of the `39150` cosets of `H` in `F_p^*`;
- exact histogramming of orbit-difference fibers for one orbit and one ordered pair of orbits.

No generic optimization, SAT, ILP, CP-SAT, or brute-force search over candidate difference sets was used.

## result

Main claim status: unresolved.

Strongest rigorous output from this solve run:

> If a `(1840051,2350,3)` abelian difference set exists, then after translation it is a subset `D subset F_1840051^*` fixed by multiplication by `2347`, and `D` is a union of exactly `50` orbits of the subgroup `H=<2347>` of order `47`.

More explicitly:

- `D = union_{s in S} sH` for some set `S` of `50` `H`-cosets.
- Let `Q = F_p^*/H`, so `|Q| = 39150`.
- The existence problem compresses to finding `|S|=50` in `Q` such that every quotient difference-orbit occurs with total multiplicity exactly `3`.

Exact local statistics found by exhaustive computation:

- One selected orbit contributes `46` quotient difference-classes, each with multiplicity `1`.
- For distinct selected orbits, the ordered pair contributes one of these exact shapes:
  - `38152` ratio classes: `47` singles;
  - `980` ratio classes: `45` singles and `1` doubled class;
  - `16` ratio classes: `43` singles and `2` doubled classes;
  - `1` special ratio class, namely `-H`: `1` singleton and `23` doubled classes.

This is a real theorem-facing reduction, but it is not yet a nonexistence proof and not a construction.

## family_affinity

Strong.

This tuple sits in the residual abelian `lambda = 3` family, but the prime-order feature makes it much more rigid than a generic residual case:

- prime `v` forces cyclicity;
- prime `n` gives a single clean multiplier subgroup;
- the whole problem compresses to a quotient of size `39150`.

That compression pattern is likely reusable for other residual prime-order cases, if such cases appear in the same frontier list.

## generalization_signal

Moderate.

What seems reusable:

- prime-order reduction `abelian -> cyclic`;
- prime-multiplier normalization;
- orbit compression to `F_p^*/<n>`;
- exact local fiber-shape analysis for orbit pairs.

What does not yet scale automatically:

- turning the compressed quotient formulation into a global obstruction;
- proving that the special doubled-ratio classes force an unavoidable overload.

## proof_template_reuse

Reusable template:

1. reduce to a cyclic prime-order ambient group;
2. fix a prime multiplier by translation;
3. decompose the candidate into multiplier orbits;
4. compress the difference equation to the quotient by the multiplier subgroup;
5. classify local orbit-pair fiber shapes exactly;
6. try to upgrade the local statistics to a global covering contradiction.

This is a legitimate proof template for prime-order residual difference-set cases, even though the last upgrade step failed here.

## candidate_theorem_slice

Most honest theorem slice currently visible:

> Any abelian `(1840051,2350,3)`-difference set is cyclic and, after translation, is the union of exactly `50` cosets of the order-`47` multiplier subgroup `H=<2347>` in `F_1840051^*`.

Supporting computational lemma:

> For any two selected `H`-orbits, the ordered cross-difference profile on `Q = F_p^*/H` has fiber multiplicities of one of the four exact shapes listed in `result`, and in particular no single ordered orbit pair contributes more than `2` representations to any quotient difference-class.

That is a genuine slice, but it is still a reduction theorem, not the title theorem of the micro-paper.

## smallest_param_shift_to_test

Within this exact tuple, the next smallest shift is not a new large search but a sharper local-to-global obstruction:

- test three-orbit configurations in the quotient, starting with one orbit, its negative orbit, and one generic third orbit;
- isolate the `16` ratio classes with two doubled fibers and the unique `-H` ratio class, and ask whether any `50`-set in `Q` can avoid forcing a quotient class above total multiplicity `3`.

If a nearby family case with prime `v` exists elsewhere in the residual list, this same compression should be tried there immediately.

## why_this_is_or_is_not_publishable

This run is not yet publishable.

Why not:

- there is no final existence or nonexistence theorem;
- the current output is a structural reduction plus exact local statistics;
- the last step from local orbit data to a global contradiction is still missing.

If the main nonexistence claim closed from this setup, the result would likely be `70%` to `90%` of a paper already.
At the current state, the package is still too thin for the micro-paper lane.

Minimal remaining packaging work if the main claim closes from this path:

- one decisive global obstruction on the `50` selected quotient classes;
- a short reminder of Gordon's residual frontier;
- the orbit-compression lemma and one boundary remark on the special `-H` ratio class.

## paper_shape_support

What extra structure would make this paper-shaped if the main claim closes?

- a global theorem on the quotient problem, not just pairwise diagnostics;
- ideally a compact proposition saying no `50`-subset of `Q = F_p^*/H` can realize the required exact `3`-cover of all `39150` quotient classes;
- alternatively, an explicit construction of such an `S`, which would convert the same compression into a construction note.

Immediate corollary / remark if the nonexistence path closes:

## verify_rediscovery

PASS 1 ran on 2026-04-15 with bounded live-web checks on the exact tuple `(1840051,2350,3)`, alternate family wording for abelian / cyclic `lambda = 3` difference sets, the canonical Gordon 2022 source, same-source theorem / table wording, and one status-style follow-up query. Within that budget, Gordon's paper remained the only precise source hit for this exact tuple, and no later construction, nonexistence theorem, or direct implication for `(1840051,2350,3)` surfaced.

Rediscovery was not established.

## verify_faithfulness

The selected problem is:

> Determine whether any abelian group of order `1840051` admits a `(1840051,2350,3)`-difference set.

Because `1840051` is prime, reducing "abelian" to the cyclic group `C_1840051` is faithful. The solve artifact is also faithful through the multiplier-normalization step: the strongest auditable claim is a reduction theorem saying that any such difference set, if it exists, can be translated to a union of exactly `50` cosets of the order-`47` subgroup `<2347>` in `F_p^*`.

However, the artifact does not resolve the intended existence question. It should therefore be treated as a theorem-facing partial reduction, not an exact solve. I applied one conservative narrowing in the verification reading: I did not retain the stronger claim that the exact orbit-pair fiber taxonomy has already been established, because the current artifact does not preserve the computation needed to audit that part.

## verify_proof

Independent exact checks reproduced the arithmetic backbone:

- `k(k-1) = lambda(v-1) = 5520150`;
- `p = 1840051` is prime;
- `n = k-lambda = 2347` is prime;
- `ord_p(2347) = 47`;
- `k = 2350 = 50 * 47`;
- `|F_p^* / <2347>| = (p-1)/47 = 39150`.

These checks support the cyclic reduction, the multiplier subgroup size, and the conclusion that any normalized candidate must be a union of exactly `50` nonzero multiplier orbits. No algebraic error was found in that core reduction.

The first step I could not fully audit is the sentence "Exhaustive quotient computations show ..." introducing the exact orbit-difference fiber-shape classification. No checker, script, or saved computation is preserved in this artifact, so that stronger computational slice is unsupported in the present packet. I did not find a contradiction there; it is simply not reproducible from the files currently attached to the run.

## verify_adversarial

No explicit candidate construction or counterexample was present to attack directly. No checker file exists under the slug artifact directory, so PASS 4 could only rerun independent arithmetic and modular-order computations. Those reruns matched the record:

- `1840051` and `2347` are prime;
- `ord_1840051(2347) = 47`;
- the quotient size is `39150`;
- `2350` is divisible by `47`.

The adversarial gap is the same as in PASS 3: the exact local orbit-pair histogram claim cannot be rerun from the preserved files, so the computation does not currently support that stronger taxonomy claim.

## verify_theorem_worthiness

Exactness:
The packet does not settle existence or nonexistence of an abelian `(1840051,2350,3)`-difference set.

Novelty:
Within the bounded rediscovery audit, I did not find a later settlement of the exact tuple. Gordon 2022 still appears to be the relevant frontier anchor.

Reproducibility:
Fair for the reduction theorem, weak for the stronger local fiber-shape classification because its underlying computation is not preserved.

Lean readiness:
No. Lean would currently formalize only a reduction lemma while the real remaining work is mathematical closure of the quotient problem, together with preservation of the missing computational support if that stronger slice is to be reused.

Paper leverage:
The verified content is a rigid multiplier-orbit reduction lemma that may be reusable for prime-order residual cases, but by itself it is not most of a publishable note.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? The hypothetical exact solve still looks like roughly `70%`, but the currently verified slice is closer to `20%` to `30%`.
- What title theorem is actually visible? "Any abelian `(1840051,2350,3)`-difference set is cyclic and, after translation, is a union of exactly `50` cosets of the order-`47` subgroup `<2347>` in `F_1840051^*`."
- What part of the argument scales? Prime-order reduction, multiplier normalization, and coset-union compression.
- What part clearly does not? The missing jump from the `50`-coset quotient model to a final existence / nonexistence theorem, and the unsupported exact orbit-pair taxonomy.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? `NONE` for the current verified packet.

## verify_verdict

`MINOR_FIX`

No rediscovery was established. The conservative repair is to narrow the strongest honest claim to the auditable reduction theorem and not treat the unpreserved exact orbit-pair histogram computation as verified.

## minimal_repair_if_any

- Keep the verified claim at the reduction-theorem level: cyclic prime-order ambient group, multiplier subgroup of order `47`, and a `50`-coset decomposition after translation.
- Before reasserting the exact orbit-pair fiber-shape taxonomy, preserve either the checker/script or durable saved output that reproduces those counts.

> Gordon's Table 4 would lose one of its six surviving abelian `lambda = 3` cases, and this tuple would be eliminated by a prime-order multiplier-orbit obstruction not captured by the currently published one-pair bounds.

## boundary_remark

Boundary remark:

- the multiplier route here is strong enough to force a rigid `50`-orbit model,
- but weak enough that one-orbit and one-pair counts stay below `lambda = 3`.

So the case sits exactly on the boundary where local multiplier data is informative but not yet decisive. The unique highly-colliding ratio class `-H` looks like the right place to push next.

## likely_failure_points

- I did not prove the final quotient-cover obstruction.
- The fiber-shape statistics were obtained by exact computation; a future proof should explain the `980 / 16 / 1` exceptional-ratio split conceptually.
- The current reduction assumes only standard multiplier facts and the translate-to-fixed normalization; verify should check the multiplier statement against the intended source wording.
- A construction route was not explored beyond the orbit compression, because the MICRO-PAPER objective strongly favors a short nonexistence proof if available.

## what_verify_should_check

- Check that the prime-multiplier theorem being used here is valid in the exact cyclic setting needed for `(v,k,lambda) = (1840051,2350,3)`.
- Check the normalization step `aD=D+s ->` translate to `aD=D` with `a=2347`.
- Re-run the exact arithmetic:
  - `1840051` prime;
  - `1840050 = 2 * 3^3 * 5^2 * 29 * 47`;
  - `ord_1840051(2347) = 47`.
- Re-run the quotient computation confirming:
  - `|Q| = 39150`;
  - one-orbit internal profile gives `46` singleton quotient classes;
  - distinct orbit-pair shapes split exactly as `38152`, `980`, `16`, `1`.
- Check whether the special class with shape `1 singleton + 23 doubles` is exactly the ratio class `-H`.

## publication_prior_art_audit

Bounded publication audit ran on `2026-04-15`.

Exact-statement search:

- Searches on the exact tuple `(1840051,2350,3)` and exact wording such as `abelian (1840051,2350,3) difference set` returned Gordon's 2022 paper as the only direct source hit.
- I did not find a later paper, note, or preprint explicitly settling this tuple within the bounded pass.

Alternate-notation search:

- Searches using cyclic wording and parameter notation such as `cyclic 1840051 2350 difference set` and `v=1840051, k=2350, lambda=3` likewise did not surface a later construction or nonexistence result.

Canonical-source check:

- Gordon's Table 4 lists `k = 2350`, `n = 2347`, `v = 1840,051` among the six open abelian `(v,k,3)` cases.
- In the same source passage, Gordon states that these are the cases left after applying Theorems 2 and 4 together with Theorems 3, the Lander tests, and the Mann test.
- I did not find a theorem, proposition, corollary, example, observation, or sufficient-condition statement inside the source that already settles the exact tuple beyond placing it in that residual list.

Outside-source status pass:

- Gordon's La Jolla Difference Set Repository page states that its listed parameters cover `v < 100000`, with additional recent computations only described for `v < 10^6`.
- Since `v = 1840051`, that repository is not itself a settlement source for this tuple, and an exact-tuple repository search surfaced no independent status entry.

Inference from the bounded sources:

- Within this narrow audit, rediscovery was not established.
- The honest frontier claim remains: Gordon 2022 appears to leave `(1840051,2350,3)` open, and I did not find a later direct settlement.

## publication_statement_faithfulness

The intended statement is:

> Determine whether any abelian group of order `1840051` admits a `(1840051,2350,3)`-difference set.

Because `1840051` is prime, reducing "abelian of order `1840051`" to the cyclic group `C_1840051` is faithful. The audited packet remains faithful through its strongest preserved step:

> Any such difference set, if it exists, can be translated to a union of exactly `50` cosets of the order-`47` subgroup `<2347>` in `F_1840051^*`.

That is a real structural consequence of the intended problem, not a change of target. But it is still only a reduction theorem. The packet does not resolve existence or nonexistence, and the unsupported orbit-pair taxonomy should not be treated as part of the strongest honest claim.

## publication_theorem_worthiness

Explicit answers:

- Is the strongest honest claim stronger than "here is an example"? Yes. It is a structural reduction theorem, not an isolated instance or witness.
- Is there a real theorem slice here? Yes, but it is a supporting proposition rather than a title theorem.
- Is the proof structural or merely instance-specific? Structural in method, but still heavily tied to this one parameter tuple and mostly obtained by specializing standard multiplier facts plus exact arithmetic.
- Would this survive a referee asking "what is the theorem?" Only at the level of a preparatory proposition: prime-order cyclic reduction plus a `50`-coset multiplier-orbit normalization.
- Is the claim too dependent on hand-picked small cases? No in the sense of small-case enumeration, but yes in the sense that it remains a narrow parameter-specific corollary and does not close the exact tuple.

The main downgrade in theorem-worthiness is novelty leverage. The visible slice is close to a routine exact-parameter corollary of known multiplier machinery rather than a new residual-case theorem. It is mathematically real, but not strong enough to carry a one-theorem note by itself.

## publication_publishability

Explicit answers:

- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? An actual exact solve of the tuple still looks like roughly `70%` of a short note, but the current audited packet is much less than that.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a theorem slice, but not a credible title theorem.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? The candidate still looks attractive if solved, but the current remaining gap is not small; the packet only looked close before audit because the preserved output is reduction-only.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Under the one-shot policy, this should be moved aside until there is a direct global obstruction or explicit construction.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Only optional later formalization of the reduction lemma. Lean would not turn this packet into a paper-ready result.

Conservative publication verdict:

- `publication_status = NONE`.
- The current packet is not instance-only, but it is also not close enough to a paper-shaped slice to justify promoting it as a publication-facing theorem packet.

## publication_packet_audit

Packet quality: thin reduction-only packet.

What is preserved well:

- the prime-order reduction to the cyclic case;
- the multiplier order computation `ord_1840051(2347) = 47`;
- the conclusion that any normalized candidate must be a union of exactly `50` nonzero multiplier orbits.

What is not preserved well enough:

- a reproducible checker or durable output for the stronger orbit-pair fiber taxonomy;
- any global obstruction or construction closing the quotient model;
- a note-level theorem statement that answers the actual existence question.

So the preserved packet is mathematically coherent, but publication-distant.

## micro_paper_audit

MICRO-PAPER verdict: fail for the current packet.

Why:

- the packet has a real structural slice, but not a title theorem;
- the strongest honest claim is likely too routine, as a specialization of known multiplier principles, to anchor a standalone note;
- the missing step is substantive new mathematics, not light editorial packaging;
- the one-shot lane should not expand this into a broader quotient-program campaign.

This slug remains a viable target only in the ex ante sense that an exact settlement of `(1840051,2350,3)` would still likely be paper-shaped. The current audited artifact is not itself close enough.

## strongest_honest_claim

The strongest honest claim preserved by the current packet is:

> If an abelian `(1840051,2350,3)`-difference set exists, then the ambient group is cyclic of prime order `1840051` and, after translation, the set is a union of exactly `50` cosets of the order-`47` subgroup `<2347>` in `F_1840051^*`.

## paper_title_hint

If this reduction slice ever needs a descriptive label, the honest non-paper-ready title is:

> Multiplier-Orbit Reduction for the Abelian `(1840051,2350,3)` Difference-Set Case

That is not a recommended publication title under the current packet quality.

## next_action

Move this slug aside as a reduction-only partial.

Reopen it only if one of these appears immediately:

- a direct global obstruction on the `50`-coset quotient model, or
- an explicit construction for the tuple.

Do not expand the current artifact into a larger theorem program or a broader search campaign.
