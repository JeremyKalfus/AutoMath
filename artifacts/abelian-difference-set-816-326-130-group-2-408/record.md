# Solve Record: On the (816,326,130) Difference-Set Problem in C_2 x C_408

- slug: `abelian-difference-set-816-326-130-group-2-408`
- working_packet: `artifacts/abelian-difference-set-816-326-130-group-2-408/working_packet.md`

## statement_lock
Locked target: determine whether the abelian group `G = C_2 x C_408 ~= C_2 x C_8 x C_3 x C_17` admits a `(v,k,lambda) = (816,326,130)` difference set.

Equivalent title-theorem form:
No `(816,326,130)`-difference set exists in `C_2 x C_408`.

## definitions
Write the group additively. Let `D subseteq G` be a difference set, so in `Z[G]`
`D D^(-1) = n * 1_G + lambda * G` with `n = k-lambda = 196 = 2^2 * 7^2`.

For a quotient `pi : G -> H` with kernel size `w`, if
`pi(D) = sum_{h in H} s_h h` as a multiset-count element of `Z[H]`, then
`pi(D) pi(D)^(-1) = 196 * 1_H + 130 w H`.
In particular:
- `sum_h s_h = 326`
- `sum_h s_h^2 = 196 + 130 w`

Conventions used below:
- `pi_3 : G -> C_3` has kernel size `272`
- `pi_51 : G -> C_3 x C_17` has kernel size `16`
- for `pi_51`, write counts as `c_{r,j}` with `r in C_3`, `j in C_17`

Ambiguities / load-bearing inputs:
- I am using the standard abelian multiplier theorem in the form: because `7 | n` and `gcd(7,816)=1`, multiplication by `7` is a numerical multiplier, so `D^(7) = D + g` for some `g in G`.
- The proof also uses the routine normalization that after translating `D`, the induced affine action on `C_3 x C_17` may be taken to be `(r,j) -> (r+t, 7j)` with `t in C_3`, because the `C_17` part of the translation can be absorbed since `7-1 = 6` is invertible mod `17`.
- `0 <= c_{r,j} <= 16` because each fiber of `pi_51` has size `16`.

## approach_A
Structural / invariant route.

1. Push `D` to the `C_3` quotient and solve the integer moment equations exactly.
2. Use the `7`-multiplier on the `C_3 x C_17` quotient to force the `c_{r,j}` counts to be constant on affine `7`-orbits.
3. Split by the residual `C_3`-translation parameter `t in {0,1,2}`.
4. Show each affine-orbit pattern is incompatible with the forced `C_3` quotient data or with the `C_3 x C_17` second-moment equation.

Why this is attractive:
- it uses only quotient bookkeeping and the one multiplier already highlighted in the packet
- it aims directly at a paper-shaped nonexistence theorem, not just a computational witness
- it avoids search-heavy machinery

## approach_B
Construction / contradiction route.

Try to realize `D` on the odd quotient first. The `C_17` quotient counts would have to satisfy
`sum s_j = 326`, `sum s_j^2 = 6436`, and, after `7`-normalization, two-level orbit structure
`s_0 = a`, `s_j = b` for `j != 0`, hence `(a,b) = (6,20)`.

Then try to lift this through the `C_3` quotient and the `16`-element fibers of `pi_51`.
This looks weaker than Approach A because the `C_17` quotient alone is not contradictory.
It does, however, suggest a useful self-check: any full proof should still be compatible with the forced `C_17` two-level pattern after normalization.

## lemma_graph
Lemma skeleton.

1. Quotient moment lemma:
For any quotient `pi : G -> H` with kernel size `w`, the projected multiplicities satisfy
`sum s_h = 326` and `sum s_h^2 = 196 + 130 w`.

2. `C_3` quotient lemma:
If `m_r = |D cap pi_3^(-1)(r)|`, then `{m_r}` is exactly `{116,110,100}`.

3. Multiplier normalization lemma:
Using the `7`-multiplier, after translation of `D` the induced action on `C_3 x C_17` is
`T_t(r,j) = (r+t,7j)` for some `t in C_3`.

4. Orbit-shape lemma for `t != 0`:
`T_t` has one orbit of size `3` on the zero column and one orbit of size `48` on the nonzero columns, forcing
`3a + 48b = 326`, impossible mod `3`.

5. Orbit-shape lemma for `t = 0`:
Each `C_3` row is `7`-invariant, so row `r` has the form `(a_r, b_r, ..., b_r)` with
`a_r + 16 b_r = m_r`.
For `m_r in {116,110,100}`, the only possibilities in `[0,16]` are
`116 -> (4,7)`, `110 -> (14,6)`, `100 -> (4,6)`.
Their total square sum is
`(4^2 + 16*7^2) + (14^2 + 16*6^2) + (4^2 + 16*6^2) = 2164`,
but the `C_3 x C_17` quotient requires
`sum c_{r,j}^2 = 196 + 130*16 = 2276`.

6. Contradiction:
Both `t != 0` and `t = 0` fail, so `D` cannot exist.

## chosen_plan
Use Approach A.

It gives the cleanest theorem-facing route:
- first lock the `C_3` quotient exactly
- then run the `7`-multiplier on `C_3 x C_17`
- finish by a short two-case contradiction

If this holds under verification of the multiplier theorem phrasing, the solve itself is already about `80-90%` of a short note. The remaining packaging is only:
- one careful statement of the multiplier input
- a polished quotient lemma
- a short explanatory paragraph on why the `C_3 x C_17` affine action is the decisive obstruction

## self_checks
Self-check after statement lock:
- parameters are internally consistent: `326 * 325 = 130 * 815`, `n = 196`
- the target group decomposition `C_2 x C_408 ~= C_2 x C_8 x C_3 x C_17` is correct

Self-check after the `C_3` quotient:
- with `m_r = 108 + u_r`, we need `sum u_r = 2`, `sum u_r^2 = 132`
- solving this integer system gives, up to permutation, `(u_0,u_1,u_2) = (8,2,-8)`, hence `{m_r} = {116,110,100}`
- check: `116 + 110 + 100 = 326` and `116^2 + 110^2 + 100^2 = 35556 = 196 + 130*272`

Self-check after multiplier normalization:
- the only residual affine parameter on `C_3 x C_17` is the `C_3` shift `t`
- the orbit descriptions for `t = 0` and `t != 0` match the facts that `7` is trivial on `C_3` and has order `16` on `C_17^times`

Self-check after contradiction:
- `t != 0` fails because `3a + 48b` is divisible by `3`, while `326` is not
- `t = 0` fails because the forced row patterns produce square sum `2164`, not `2276`
- both contradictions are arithmetic, not heuristic

## code_used
No code used.

The argument stayed in quotient arithmetic and affine-orbit bookkeeping, so a bounded experiment was unnecessary.

## result
Provisional nonexistence proof.

Assume `D subseteq G` is a `(816,326,130)`-difference set.

Step 1: force the `C_3` quotient.
Let `m_r = |D cap pi_3^(-1)(r)|` for `r in C_3`.
Since `|ker pi_3| = 272`, the quotient-moment lemma gives
`sum_r m_r = 326` and `sum_r m_r^2 = 196 + 130*272 = 35556`.
Write `m_r = 108 + u_r`. Then
`sum_r u_r = 2`, `sum_r u_r^2 = 132`.
Up to permutation, the unique integer solution is `(u_0,u_1,u_2) = (8,2,-8)`, so
`{m_r} = {116,110,100}`.

Step 2: push to `C_3 x C_17`.
Let `c_{r,j}` be the multiplicity on `(r,j) in C_3 x C_17`.
Because `|ker pi_51| = 16`, we have
`sum_{r,j} c_{r,j} = 326`,
`sum_{r,j} c_{r,j}^2 = 196 + 130*16 = 2276`,
and each `c_{r,j}` lies in `[0,16]`.

Step 3: apply the `7`-multiplier.
Using the standard multiplier theorem, `D^(7) = D + g` for some `g in G`.
After translating `D`, the induced action on `C_3 x C_17` is
`T_t(r,j) = (r+t, 7j)` for some `t in C_3`.

Case 1: `t != 0`.
Then `T_t` has one orbit of size `3` on the zero column and one orbit of size `48` on the nonzero columns.
So `c_{r,0} = a` for all `r`, and `c_{r,j} = b` for all `j != 0`.
Hence
`3a + 48b = 326`,
impossible because the left side is divisible by `3` and the right side is not.

Case 2: `t = 0`.
Then each row is individually `7`-invariant, so row `r` has one value `a_r` at `j=0` and one value `b_r` on all `16` nonzero `j`.
Its row sum is `a_r + 16 b_r = m_r`.
Since `0 <= a_r,b_r <= 16` and `{m_r} = {116,110,100}`, the only possibilities are
- `116 -> (a_r,b_r) = (4,7)`
- `110 -> (14,6)`
- `100 -> (4,6)`

Therefore the total square sum is forced to be
`(4^2 + 16*7^2) + (14^2 + 16*6^2) + (4^2 + 16*6^2) = 2164`,
contradicting the required value `2276`.

Both cases fail. Therefore no `(816,326,130)`-difference set exists in `C_2 x C_408`.

What scales:
- the `C_3` quotient moment lock
- the affine-orbit split on `C_3 x C_p` when a prime multiplier acts transitively on `C_p^times`

What does not automatically scale:
- the exact row-sum decompositions depend on the fiber size `16`
- the contradiction uses the specific totals `326`, `2276`, and the exact `C_3` row multiset

Suggested theorem slice:
If a putative abelian difference set on a group with odd quotient `C_3 x C_17` has kernel size `16`, order `n = 196`, and `7` acts as a multiplier, then the induced affine-orbit patterns on the quotient already obstruct existence when the `C_3` row sums are `{116,110,100}`.

Most useful next parameter shifts:
- test other residual rows with the same `17`-primary multiplier geometry
- test nearby groups where the `C_3 x C_17` quotient survives but the kernel size changes from `16`

Package assessment:
This is no longer just a raw instance witness. If the multiplier input and the normalization step verify cleanly, it is close to a paper-shaped exact nonexistence note.

## family_affinity
Moderate-to-strong.

The obstruction is not a one-off parity trick. It uses a reusable pattern:
- lock a small odd quotient by moment equations
- use a prime multiplier that is transitive on the nonzero part of a prime quotient
- compare the resulting affine orbit counts against the fiber-size bounds and second moments

That template should be relevant to other survey-table residual rows with a visible `C_17` or similar odd prime quotient.

## generalization_signal
Real but local.

The part that generalizes is the affine-orbit obstruction on `C_3 x C_p` when a prime multiplier acts trivially on the `C_3` factor and transitively on `C_p^times`.
The part that is instance-specific is the exact row-sum triple `{116,110,100}` and the forced decompositions through a `16`-element kernel.

So the immediate signal is "small theorem slice with family reuse", not "broad new classification theorem".

## proof_template_reuse
Reusable proof template.

1. Push to the smallest informative odd quotient.
2. Solve the quotient moment equations exactly.
3. Normalize the multiplier action to a short affine form.
4. Enumerate the orbit-size cases.
5. Use fiber-size bounds plus one second-moment identity to kill each case.

This is a credible template for other exact Table 2 rows where the odd quotient and multiplier geometry are comparably small.

## candidate_theorem_slice
Primary slice:
No `(816,326,130)`-difference set exists in `C_2 x C_408`.

Secondary slice:
For this parameter set, any putative difference set would induce `C_3` quotient row sums `{116,110,100}`; combined with the `7`-multiplier on the `C_3 x C_17` quotient, those row sums are incompatible with the only possible affine-orbit structures.

## smallest_param_shift_to_test
Best next local tests if this exact argument needs family support:
- same odd quotient `C_3 x C_17`, different `2`-primary kernel size
- same total parameters but nearby abelian group structure where the `7`-multiplier still survives

Best immediate check inside this case:
- verify whether the `C_17` quotient after normalization indeed forces the two-level count pattern `(6,20,...,20)`; it is not needed for the contradiction above, but it is a useful consistency cross-check for the final packet.

## why_this_is_or_is_not_publishable
If the multiplier step verifies cleanly, this is plausibly publishable in the micro-paper lane.

Why:
- the theorem is the exact open survey row
- the proof is short and theorem-shaped
- the post-solve packaging is light: state the multiplier input carefully, present the quotient lemmas cleanly, and add one paragraph situating the row inside the Gordon-Schmidt table

Would a successful solve already be `70-90%` of a paper?
- Yes. This attempt is around `0.8-0.85` of a short paper packet if verification accepts the multiplier normalization exactly as used here.

Minimal remaining packaging work:
- polish the `C_3` quotient lemma into a self-contained proposition
- cite the exact multiplier theorem statement used for `7`
- add one brief boundary remark explaining why the method is local rather than a broad family theorem

Current risk:
- until verification checks the multiplier theorem hypothesis and the affine normalization carefully, the package should still be treated conservatively

## paper_shape_support
Exact title theorem:
On the Nonexistence of a `(816,326,130)` Difference Set in `C_2 x C_408`.

Immediate corollary / remark:
The open `[2,408]` row in the Gordon-Schmidt Table 2 residual list is obstructed already on the `C_3 x C_17` quotient; no heavy search or deeper `2`-primary analysis is needed once the `7`-multiplier is used correctly.

Why this is paper-shaped if correct:
- the result settles one exact residual row
- the core argument fits into a compact note
- the method is slightly more than a naked instance because it isolates a reusable affine-orbit obstruction

This is not too thin for the micro-paper lane if the argument verifies. Without multiplier verification, it remains an unusually strong but still provisional solve artifact.

## boundary_remark
Boundary remark.

The proof does not claim a general no-go theorem for all groups of order `816` or all `(816,326,130)` rows. It uses the specific odd quotient geometry of `C_3 x C_17` and the fact that `7` acts as a multiplier with order `16` on the `17`-part.

Natural boundary corollary:
once a residual row has the same odd quotient and multiplier pattern, the first thing to test is whether its quotient row sums force the same kind of affine-orbit contradiction.

## likely_failure_points
Main verification risks:
- confirm the exact multiplier theorem statement used to promote `7` to a multiplier in this abelian setting
- check the translation-normalization step on `C_3 x C_17` carefully: the `C_17` part can be absorbed, but the residual `C_3` shift really is only `t in {0,1,2}`
- confirm that no hidden convention issue changes the quotient identity from `196 * 1_H + 130 w H`
- polish the uniqueness of `{116,110,100}` from the `C_3` quotient into a short explicit integer lemma

## verify_rediscovery
PASS 1: bounded rediscovery audit.

Bounded web sweep used the exact tuple, alternate notation, the canonical source title, and recent-status phrasing. The sweep kept returning Gordon-Schmidt's multiplier-conjecture survey and generic difference-set listings; it did not surface a later paper, preprint, theorem, proposition, example, or repository entry explicitly settling the exact row `(816,326,130)` in `C_2 x C_408` / `[2,408]`.

Canonical-source check:
- Gordon-Schmidt's survey still lists the `[2,408]` row `(816,326,130)` in Table 2 as open.
- The same source separates proved multiplier theorems from the multiplier conjecture. In particular, the survey's First Multiplier Theorem requires `p > lambda`, so it does not by itself certify `7` as a multiplier here because `7 < 130`.

Rediscovery verdict:
- no bounded-evidence rediscovery found
- no direct later settlement found within the allotted sweep
- however, the canonical source does not support the solve record's use of `7` as an already-proved multiplier

## verify_faithfulness
PASS 2: faithfulness to the intended statement.

Top-level target faithfulness is good: the packet aims at the exact intended disproof of the exact selected statement, not a broader or weaker family statement.

The proof body is not fully faithful to that target, because it silently narrows to a conditional subcase that is not derived from the hypotheses:
- it claims the `C_3` quotient multiplicities are uniquely forced to `{116,110,100}`
- it then treats `7` as a proved multiplier and builds the `C_3 x C_17` affine-orbit split on that basis

The first narrowing is false as stated, and the second is unsupported by the cited source material. So the packet does not currently verify the exact intended theorem; at best it sketches a nearby conditional obstruction.

## verify_proof
PASS 3: proof-correctness check.

First incorrect step:
- Step 1 claims that `sum u_r = 2` and `sum u_r^2 = 132` have, up to permutation, the unique integer solution `(8,2,-8)`.
- This is false. There is a second solution `(10,-4,-4)`, giving a second admissible `C_3` row multiset `{118,104,104}` in addition to `{116,110,100}`.

So the proof already fails before the multiplier step. The advertised `C_3` quotient lemma is not established.

Downstream status after that correction:
- the `t = 0` square-sum contradiction can be repaired for both admissible row multisets:
  - `{116,110,100}` gives row-shape square total `2164`
  - `{118,104,104}` gives row-shape square total `2100`
  - both contradict the required `2276`
- but the proof still cannot conclude nonexistence, because the move from a putative difference set to a `7`-multiplier affine action on `C_3 x C_17` remains unsupported

Load-bearing unresolved gap:
- the solve record uses `7 | n` and `gcd(7,816)=1` as if that automatically made `7` a numerical multiplier
- the canonical source does not justify that implication for this row; the cited proved theorem requires `p > lambda`, which fails here

Conclusion for proof correctness:
- first incorrect step: false uniqueness claim in the `C_3` quotient lock
- surviving critical gap after tiny arithmetic repair: unjustified use of `7` as a proved multiplier

## verify_adversarial
PASS 4: adversarial checks.

No checker or search code exists in the artifact directory, so the adversarial pass was a direct rerun of the packet's arithmetic constraints.

Local arithmetic checks performed:
- enumerated integer solutions to `u_0 + u_1 + u_2 = 2`, `u_0^2 + u_1^2 + u_2^2 = 132`
- found two solution types, not one: `(-8,2,8)` and `(-4,-4,10)`
- verified the corresponding `C_3` row multisets are `{116,110,100}` and `{118,104,104}`
- verified the only `t = 0` row decompositions with `0 <= a_r,b_r <= 16` are:
  - `116 -> (4,7)`
  - `110 -> (14,6)`
  - `100 -> (4,6)`
  - `118 -> (6,7)`
  - `104 -> (8,6)`
- verified the resulting square totals are `2164` and `2100`, both below the required `2276`

Adversarial conclusion:
- the quotient arithmetic does contain a real obstruction pattern
- but the packet's theorem claim still breaks, because the bridge into the affine-orbit framework depends on an unproved multiplier input

## verify_theorem_worthiness
PASS 5: theorem-worthiness assessment.

Exactness:
- the intended theorem slice is exact and still attractive
- the current artifact is not exact: it does not prove the selected statement

Novelty:
- bounded audit found no rediscovery of the exact row
- novelty therefore remains plausible, but only for the target problem, not for the current unfinished proof

Reproducibility:
- the local arithmetic is reproducible and easy to check
- the proof as a theorem packet is not reproducible end-to-end because the multiplier premise is not justified from the packet's cited inputs

Lean readiness:
- not Lean-ready
- Lean would only formalize a broken route, not seal a near-complete theorem packet

Paper leverage:
- if the exact nonexistence theorem were proved, it would still look like most of a short publishable note
- best estimate for the target remains roughly `0.76` of a paper from one clean solve

Required explicit answers:
- would this result, if correct and Lean-sealed, already constitute most of a publishable note?
  - yes; the exact survey row is a paper-shaped title theorem
- what percentage of the paper would one solve already provide?
  - about `75-80%`
- what title theorem is actually visible?
  - intended: nonexistence of an `(816,326,130)` difference set in `C_2 x C_408`
  - current honest theorem visibility: only a conditional quotient-orbit obstruction, not the intended theorem
- what part of the argument scales?
  - the quotient-moment bookkeeping and the affine-orbit contradiction template once a valid multiplier input is available
- what part clearly does not?
  - the exact `C_3` row lock as written; it needs a two-pattern split, and the specific multiplier step is not presently available from the cited theorem base
- is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`?
  - `NONE`, because there is not yet a verified theorem packet

Overall worthiness assessment:
- the target remains a legitimate micro-paper candidate
- this verification run does not produce a paper-ready or Lean-ready packet
- the current artifact is best viewed as a partial conditional route with one tiny arithmetic repair available and one non-tiny theorem gap still open

## verify_verdict
`CRITICAL_FLAW`

Reason:
- no rediscovery was found, so the target itself remains live
- the proof fails first at the false uniqueness claim for the `C_3` quotient
- after that tiny repair, the packet still depends on an unsupported claim that `7` is a proved multiplier for this row
- the run must not be labeled `EXACT`; the strongest honest state is an unresolved nearby conditional route

## minimal_repair_if_any
Tiny conservative repair available:
- replace the false "unique `C_3` row multiset" claim by the two admissible multisets `{116,110,100}` and `{118,104,104}`
- note that the `t = 0` square-sum contradiction survives for both patterns

Non-tiny unresolved blocker:
- do not claim a theorem until the packet either justifies the `7`-multiplier input from a valid published theorem or finds a different route that avoids that input entirely

## publication_prior_art_audit
Bounded publication-facing prior-art audit on `2026-04-15`.

Exact-statement search:
- searched the exact tuple `(816,326,130)` together with `C_2 x C_408`
- searched the exact tuple together with the survey-table notation `[2,408]`
- searched the exact tuple together with plain-text variants `C2 x C408` and `Z_2 x Z_408`
- within this narrow sweep, the only direct exact-row hit was the canonical Gordon-Schmidt survey and search-engine echoes of its Table 2 row

Alternate-notation search:
- no later exact hit surfaced for `C_2 x C_408`, `C2 x C408`, `Z_2 x Z_408`, or `[2,408]`
- I did not find a later theorem page, proposition, example, corollary, observation, sufficient-condition statement, or repository entry that already settles the exact row

Canonical-source check:
- Gordon-Schmidt state that Table 2 gives open difference-set parameters
- the table contains the exact row `816 326 130 [2,408]`
- the row is presented there as open, not as a settled existence or nonexistence theorem

Theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source:
- the bounded source check did not locate any named result in the survey that already closes the exact `[2,408]` row
- the surrounding source material instead records multiplier theorems, the multiplier conjecture, and then leaves this row in the open table

One outside-source status pass:
- the Dan Gordon difference-set repository homepage is live and still presents itself as a maintained database of abelian difference-set parameters and known results
- the 2022 follow-up paper `On difference sets with small lambda` is a natural later status source, but the bounded pass found no occurrence of `816`, `326`, or `[2,408]` there

Conservative prior-art verdict:
- rediscovery is not established within budget
- frontier status remains plausible but only in the bounded sense required for this audit
- the target still looks locally fresh, but this is not a full literature certification

## publication_statement_faithfulness
The packet stays attached to the exact selected statement. There is no drift in group, parameter tuple, or claim type.

Faithfulness after verification:
- the selected theorem slice is still `No (816,326,130)-difference set exists in C_2 x C_408`
- the current artifact does **not** prove that statement
- the strongest honest claim is only conditional: if a valid theorem really forces `7` to be a multiplier here, then the quotient-moment and affine-orbit bookkeeping would contradict existence

So the statement target remains faithful, but the artifact is weaker than its headline theorem.

## publication_theorem_worthiness
There is a real title-theorem slice here:
- existence or nonexistence of a `(816,326,130)` difference set in `C_2 x C_408`

Explicit answers:
- is the strongest honest claim stronger than "here is an example"? `Yes`, but only slightly in publication terms: it is a conditional structural obstruction, not a mere example, yet still not an unconditional theorem
- is there a real title theorem or theorem slice? `Yes`
- is the proof structural or merely instance-specific? `Structural in route, local in scope, and tied to this exact row`
- would this survive a referee asking "what is the theorem?" `No`
- is the claim still too dependent on hand-picked small cases? `No` in the search-heavy sense, but `yes` in the theorem-grade sense because one unsupported multiplier input still carries the proof

The route is not just a hand-picked small-case anecdote. It has a genuine structural spine:
- exact quotient moments on `C_3`
- affine-orbit analysis on `C_3 x C_17`
- contradiction from orbit sizes and second moments

But theorem-worthiness depends on the missing multiplier basis. Without that input, the packet is not referee-ready.

## publication_publishability
Explicit answers:
- would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? `Yes` for the target theorem slice
- what percentage of the paper would one solve already provide? about `0.76`
- is there a real title theorem, theorem slice, or counterexample theorem here? `Yes`, the exact nonexistence or existence question for the Table 2 row
- is this packet paper-ready now? `No`
- if not paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? the target is still attractive, but the remaining gap is **not** small because it is theorem-producing work
- if this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? `Yes`

Current publishability:
- not paper-ready
- not close enough to paper-ready to deserve `SLICE_CANDIDATE` on the current artifact
- the packet still needs either a valid literature-backed multiplier theorem for `7` in this setting or a different proof route that avoids that step

Managerial consequence:
- preserve the artifact
- cool the packet in the main lane
- do not inflate the failure into a broader theorem campaign

## publication_packet_audit
Packet quality split:
- target quality: strong exact micro-paper target
- current proof packet quality: low
- proof artifacts preserved: yes
- artifact preservation quality: good enough to retain as a failed-but-useful structural attempt

Human-ready / theorem packet decision:
- `publication_status = NONE`
- `human_ready = false`
- the packet is not ready to leave the discovery queue as a HUMAN_READY result

Lean-seal decision:
- would Lean directly seal the packet, or would it only be optional polish / later archival formalization? `Only later archival formalization`
- at present, Lean would formalize a conditional route with a live theorem gap, not seal a publication packet
- Lean remains secondary polish after a verified proof exists; it cannot rescue the present publication audit

## micro_paper_audit
Micro-paper lane verdict:
- the **target** remains micro-paper eligible
- the **current packet** does not meet the lane's HUMAN_READY threshold

Why the target still fits the lane:
- exact residual survey row
- real title theorem if solved
- no feeder ladder required
- one clean solve would still supply most of a short note

Why the current packet fails:
- the bounded verify state remains `CRITICAL_FLAW`
- the strongest honest claim is still conditional on an unsupported multiplier input
- the remaining work is theorem-producing work, not light post-solve packaging

Net assessment:
- good target
- not a publishable packet
- move it aside rather than enlarge it

## strongest_honest_claim
The current artifact supports only a conditional structural obstruction: if one can justify that `7` is a valid multiplier for a putative `(816,326,130)` difference set in `C_2 x C_408`, then the `C_3` and `C_3 x C_17` quotient bookkeeping yields a contradiction. This is stronger than a mere worked example, but it does not prove nonexistence in `C_2 x C_408`.

## paper_title_hint
On the `(816,326,130)` Difference-Set Problem in `C_2 x C_408`

## next_action
Move this packet aside in the main micro-paper lane. Reopen it only if one of the following happens:
- a valid literature-backed theorem really does force `7` to be a multiplier here
- a different proof route is found that avoids the multiplier step entirely

Until then, preserve the quotient-orbit template as a reusable failed attempt and do not inflate it into a broader theorem program.
