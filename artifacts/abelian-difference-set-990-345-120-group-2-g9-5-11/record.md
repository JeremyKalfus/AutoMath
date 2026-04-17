# Solve Record: Does an abelian group of type [2,G9,5,11] admit a (990,345,120)-difference set?

- slug: `abelian-difference-set-990-345-120-group-2-g9-5-11`
- working_packet: `artifacts/abelian-difference-set-990-345-120-group-2-g9-5-11/working_packet.md`

## statement_lock
Determine whether any abelian group with Gordon's Lander-conjecture row [2,G9,5,11] admits a (990,345,120)-difference set.

## definitions
- Parameters are fixed at `v = 990`, `k = 345`, `lambda = 120`, so `n = k - lambda = 225 = 15^2`.
- Write `G` for a putative abelian group of order `990` with Gordon type `[2,G9,5,11]`.
- The notation `G9` is the only local ambiguity. I will treat it conservatively as "the abelian 3-part of order `9` named by Gordon's row"; the arguments below only use Hall quotients by the `2`, `5`, and `11` factors, so they are uniform in either abelian order-9 type.
- For a subgroup `N <= G`, if `pi : G -> G/N = Q` is the quotient map and `D` is a difference set, write `X = pi(D) = sum_{q in Q} x_q q` where `x_q = |D cap pi^{-1}(q)|`.
- The basic group-ring identity is `D D^(-1) = 225 + 120 G`, hence after quotienting,
  `X X^(-1) = 225 + 120 |N| Q`.
- Intended title theorem if the row closes negatively:
  `No abelian group of Gordon type [2,G9,5,11] admits a (990,345,120)-difference set.`
- A successful solve here would still be about `0.76` of a paper because the frontier statement is already source-anchored and the remaining packaging would just be a short setup plus the final obstruction proof.

## approach_A
Structural / invariant route via Hall-quotient rigidity.

Take quotient orders `|Q|` for which the centered image `Y = X - s Q` can be chosen with `Y Y^(-1) = 225` and augmentation `15`. The useful choice is
`s = (k - sqrt(n)) / |Q| = (345 - 15) / |Q| = 330 / |Q|`,
whenever this is integral. For `|Q| = 11` and `|Q| = 22`, this gives `s = 30` and `s = 15`.

Then:
1. `Y Y^(-1) = 225`.
2. Since `3,5` divide `225` but do not divide `|Q|`, reduction modulo `3` and modulo `5` lands in semisimple group algebras of the abelian quotient `Q`.
3. In those semisimple quotients, `Y Y^(-1) = 0` forces `Y = 0`, so every coefficient of `Y` is divisible by both `3` and `5`.
4. Therefore `Y = 15 Z` with `Z Z^(-1) = 1` and augmentation `1`.
5. The identity coefficient of `Z Z^(-1)` is `sum z_q^2 = 1`, so `Z` is a single group element.

This would force the quotient image to be a uniform baseline plus one exceptional coset. That is a real theorem slice, not just heuristic structure.

## approach_B
Construction / contradiction route through compatible fiber profiles.

The quotient-rigidity slice suggests that any putative difference set must look like a nearly uniform `15`-point baseline on the `22` cosets of the Hall `45`-subgroup, with exactly one coset raised to `30`. Pushing the same idea to the `11`-quotient gives a `30`-baseline with one coset raised to `45`, and the `2`-quotient gives the forced split `180/165`.

The contradiction strategy is then:
1. push one level deeper to the `5`-quotient or `55`-quotient,
2. show the same centered element has only a delta-type solution there as well, and
3. combine the `11`- and `5`-profiles on a `11 x 5` grid of `18`-element cells to force an impossible local distribution.

This route is attractive because it stays theorem-facing and uses only exact quotient arithmetic, but the missing step is a clean classification of the centered norm-`25` element in a `5`-primary quotient. That is the first genuine blocker.

## lemma_graph
1. Quotient transfer:
   If `X = pi(D)` in `Z[Q]`, then `X X^(-1) = 225 + 120 |N| Q`.
2. Centering lemma:
   If `s = 330 / |Q|` is integral and `Y = X - s Q`, then `Y Y^(-1) = 225` and `epsilon(Y) = 15`.
3. Semisimple divisibility lemma:
   If `p in {3,5}` and `p does not divide |Q|`, then reducing `Y Y^(-1) = 225` modulo `p` gives `Y = 0` in `F_p[Q]`, hence every coefficient of `Y` is divisible by `p`.
4. Norm-one collapse:
   Writing `Y = 15 Z`, we get `Z Z^(-1) = 1` and `epsilon(Z) = 1`; therefore `Z` is a single basis element.
5. Consequence for `|Q| = 11`:
   the `11` coset counts are exactly one `45` and ten `30`.
6. Consequence for `|Q| = 22`:
   the `22` coset counts are exactly one `30` and twenty-one `15`.
7. Boundary push:
   the same template suggests checking `|Q| = 5` and `|Q| = 55`, but there the `5`-primary part breaks the clean semisimple divisibility argument.

## chosen_plan
Use approach A as the main line.

Concrete plan:
1. Lock the exact quotient-rigidity lemmas for quotient orders `11` and `22`.
2. Record the forced `2`-quotient split `180/165` as a consistency check.
3. Try one bounded experiment on the `5`-quotient to determine whether the centered norm-`25` element is also forced to a single exceptional coset.
4. If the `5`-quotient also rigidifies, try to fuse the `11`- and `5`-profiles; otherwise stop and report the exact obstruction slice honestly instead of pretending the full negative result is closed.

## self_checks
- Self-check after statement lock:
  the target is still the exact Gordon row, not a broader family claim.
- Self-check after approach selection:
  the proof attempts stay inside quotient/group-ring reasoning; no search-first drift.
- Self-check after lemma graph:
  the index-`11` and index-`22` conclusions are exact and uniform in the unresolved `G9` notation.
- Self-check before code:
  a real theorem slice is already preserved in this record, so a timeout now would still leave usable mathematical content.
- Self-check after the bounded `5`-quotient experiment:
  the code did not magically finish the obstruction; it exposed the exact place where the current method stops.

## code_used
One tiny exact enumeration was used after the reasoning sections were written.

Task:
- classify integer `5`-tuples `z = (z_0,...,z_4)` with
  `sum z_i = 5`,
  `sum z_i^2 = 25`,
  and cyclic autocorrelation `sum_i z_i z_{i+t} = 0` for `t = 1,2,3,4`.

Reason:
- for an order-`5` quotient, if `X = sum x_i g^i` and `Y = X - 66 Q`, then `Y = 3 Z` and `Z` must satisfy exactly the conditions above.

Exact output:
- ten solutions, forming two translation orbits:
  `5 e_j`,
  and `(2,2,2,2,-3)` up to cyclic shift.

So the order-`5` quotient profiles are exactly:
- one coset with `81` points and four with `66`, or
- one coset with `57` points and four with `72`.

## result
Current strongest honest result:

Let `D` be a putative `(990,345,120)` difference set in an abelian group of type `[2,G9,5,11]`.

- For any quotient `Q` of order `11`, the quotient fiber profile of `D` is forced to be:
  one coset with `45` points and ten cosets with `30` points.
- For any quotient `Q` of order `22`, the quotient fiber profile of `D` is forced to be:
  one coset with `30` points and twenty-one cosets with `15` points.
- For the quotient of order `2`, the two fiber counts are forced to be `180` and `165`.
- For the quotient of order `5`, a bounded exact classification of the centered norm-`25` equation shows two and only two profile types:
  `{81,66,66,66,66}` and `{57,72,72,72,72}`.

Proof of the `11`- and `22`-quotient claim:

Let `|Q| = q` with `q in {11,22}` and let `X = sum x_t t` be the quotient image. Set `s = 330/q` and `Y = X - s Q`. Then
`epsilon(Y) = 345 - sq = 15`.
Using `X X^(-1) = 225 + 120 (990/q) Q` and `Q^2 = q Q`, a direct expansion gives
`Y Y^(-1) = 225`.
Now reduce modulo `3`. Since `3` does not divide `q`, the group algebra over `F_3` is semisimple and characters separate points, so from `Y Y^(-1) = 0` we get `Y = 0 mod 3`. The same argument modulo `5` gives `Y = 0 mod 5`. Hence `Y = 15 Z` with `Z in Z[Q]`, `epsilon(Z)=1`, and `Z Z^(-1)=1`.
Looking at the identity coefficient yields `sum z_t^2 = 1`, so exactly one `z_t` is `1` and all others are `0`. Thus `Z` is a group element, so `Y = 15 g` for some `g in Q`. Therefore
`X = s Q + 15 g`.
This is exactly the stated quotient profile.

Interpretation of the order-`5` experiment:

Let `Q` have order `5` and write `X = sum x_i g^i`. Setting `Y = X - 66 Q` gives `Y Y^(-1) = 225` and `epsilon(Y)=15`. Modulo `3`, the quotient group algebra is semisimple, so `Y = 3 Z` and `Z Z^(-1)=25`, `epsilon(Z)=5`. The bounded enumeration above classifies all such `Z`, producing exactly the two profile types stated.

This is useful but also shows the current proof path does not yet close the row: the `5`-primary quotient still allows nontrivial centered solutions.

## family_affinity
High. The argument is a standard difference-set quotient/character skeleton, but the exceptional-coset conclusion is unusually sharp for this exact row and would transfer to nearby abelian Hall-split Lander residues with square `n`.

## generalization_signal
Moderate. The centered-element lemma applies whenever a quotient order `q` divides `k - sqrt(n)` and the primes dividing `sqrt(n)` are disjoint from `q`. Here that cleanly hits the `11`- and `22`-quotients. The exact experiment shows the `5`-primary step is qualitatively different: rigidity weakens to two orbit types instead of one.

## proof_template_reuse
Reusable template:
1. pass to a Hall quotient,
2. subtract the baseline `s Q` with `s = (k - sqrt(n))/|Q|`,
3. reduce the centered norm equation modulo primes dividing `sqrt(n)` but not the quotient order,
4. conclude coefficientwise divisibility,
5. collapse to a single exceptional coset.

That template is compact and paper-usable.

## candidate_theorem_slice
Candidate theorem slice:

`If an abelian group of type [2,G9,5,11] admits a (990,345,120)-difference set, then relative to any quotient of order 11 the fiber counts are {45,30,...,30}, relative to any quotient of order 22 the fiber counts are {30,15,...,15}, and relative to any quotient of order 5 the fiber counts are either {81,66,66,66,66} or {57,72,72,72,72}.`

This is theorem-shaped and could plausibly survive into a final note as a main structural proposition even if the full nonexistence proof needs one more lemma.

## smallest_param_shift_to_test
Best next parameter shifts:

- First: test the quotient of order `55`, because it is the first place where the forced `11`- and `5`-profiles can interact on a common `11 x 5` grid.
- Second: test whether either order-`5` profile is compatible with the order-`22` baseline `{30,15,...,15}` under the shared `2 x 11 x 5` Hall decomposition.

## why_this_is_or_is_not_publishable
Not publishable yet by itself.

What is already real:
- a clean exact structural proposition,
- an exact code-backed classification of the order-`5` quotient profiles,
- a natural paper title theorem if the final obstruction closes, and
- a proof template that clearly scales within this arithmetic family.

What is still missing:
- the final contradiction or explicit nonexistence theorem in the original group type.

So the current package is still too thin for the micro-paper lane on its own, but it is close enough to justify `SLICE_CANDIDATE` as a publication-facing intermediate state.

## paper_shape_support
If the main claim closes negatively, the paper shape is already clear:

- exact title theorem:
  `No abelian group of type [2,G9,5,11] admits a (990,345,120)-difference set.`
- what the present slice contributes:
  it gives a short structural proposition forcing a unique exceptional coset in the `11`- and `22`-quotients, together with an exact two-orbit classification on the `5`-quotient.
- minimal remaining packaging work:
  one final compatibility lemma closing the obstruction, plus a concise literature/setup section around Gordon's open row.
- immediate corollary / remark:
  any putative example would have to be extraordinarily rigid at the Hall-quotient level; in particular, the `22`-coset profile is baseline `15` everywhere except one `30`-coset.

## boundary_remark
The part of the argument that scales is the Hall-quotient centering trick and the semisimple divisibility collapse. The part that does not yet scale is the `5`-primary quotient, where the clean mod-`5` semisimple step breaks and two centered norm-`25` orbits survive. That is exactly why the present result is a structural slice rather than a complete paper-ready obstruction.

## likely_failure_points
- The only notation ambiguity is the exact meaning of `G9`, but the current quotient arguments avoid dependence on that choice.
- The full negative result still needs a genuine local contradiction beyond the `11`-, `22`-, and `5`-quotient rigidity.
- The bounded experiment confirms that the `5`-quotient admits several centered norm-`25` patterns, so this line may stop at the slice level unless the `55`-quotient interaction supplies the missing obstruction.

## what_verify_should_check
- Verify the group-ring expansion `Y Y^(-1) = 225` for the centered quotient elements with `q = 11` and `q = 22`.
- Verify the semisimple reduction step carefully: for abelian `Q` with `p not dividing |Q|`, `Y Y^(-1)=0` in `F_p[Q]` implies `Y=0`.
- Verify that the quotient-order arguments are uniform in both possible abelian order-`9` types behind `G9`.
- Re-run the tiny order-`5` enumeration independently and confirm the two-orbit classification `{81,66,66,66,66}` / `{57,72,72,72,72}`.
- Check whether the quotient-rigidity proposition is already known in the literature for this exact row or for a slightly broader class.

## verify_rediscovery
- PASS 1 used a bounded web audit on the exact tuple `990 345 120 [2,G9,5,11]`, alternate notation for the same row, Gordon's canonical La Jolla / ArasuFest source, and one freshness check against Gordon-facing repository/publication surfaces.
- The canonical source still points back to Gordon's 2019 slide deck listing `990 345 120 225 [2,G9,5,11]` as open.
- Within the bounded search budget, I did not find a paper, repository update, or discussion page explicitly settling this exact group-type row.
- Verdict for PASS 1: no rediscovery established inside budget. This is only a bounded negative search result, not a proof of novelty.

## verify_faithfulness
- The intended statement is the exact existence/nonexistence question for the Gordon row `[2,G9,5,11]`.
- The solver's strongest written claim is not that exact statement. It is a conditional structural slice about quotient profiles for quotients of orders `11`, `22`, and `5`.
- That is theorem drift relative to the intended row-closing task, so the run cannot be classified as a verified settlement of the selected problem.
- Classification consequence: even if the slice were correct, it would be a `VARIANT` of the intended statement rather than a closure of the row.

## verify_proof
- The first incorrect step occurs in the proof of the claimed `11`- and `22`-quotient rigidity lemma.
- The record argues: in `F_p[Q]`, semisimplicity plus `Y Y^(-1) = 0` implies `Y = 0`. That implication is false in general.
- Direct finite-field checks produce explicit nonzero counterexamples already for `Q = C_11`:
  - over `F_3`: `(0,0,0,0,1,0,1,2,2,2,1)` has cyclic autocorrelation `0` at every shift,
  - over `F_5`: `(0,0,0,0,1,1,2,2,0,3,1)` has cyclic autocorrelation `0` at every shift.
- So the deduction "all coefficients of `Y` are divisible by both `3` and `5`, hence `Y = 15 Z`" is unsupported, and the downstream exceptional-coset conclusions for quotient orders `11` and `22` do not survive verification.
- The order-`5` computation can be conservatively repaired. Although the same semisimplicity slogan was invoked there, exhaustive search over `F_3[C_5]` found no nonzero solution to `Y Y^(-1)=0`, so `Y = 3 Z` is valid for `q = 5`. Combined with the rerun integer enumeration below, this salvages only the order-`5` profile classification.

## verify_adversarial
- I reran the exact integer enumeration for `5`-tuples `z` with `sum z_i = 5`, `sum z_i^2 = 25`, and cyclic autocorrelations `0` for shifts `1,2,3,4`.
- The rerun reproduced exactly `10` solutions, namely the two cyclic translation orbits of `5 e_j` and `(2,2,2,2,-3)`.
- Therefore the induced order-`5` quotient profiles `{81,66,66,66,66}` and `{57,72,72,72,72}` are reproducible.
- I also ran an adversarial finite-field check against the critical semisimple step. Nonzero null-product vectors exist in `F_3[C_11]` and `F_5[C_11]`, so the proof of the `11`/`22` quotient claims fails exactly where the record said verification should focus.

## verify_theorem_worthiness
- Exactness: the row itself is not settled. The verified residue is only an auxiliary order-`5` quotient-profile lemma.
- Novelty: bounded web search did not establish rediscovery of the exact row, but it also did not supply a literature anchor for the repaired auxiliary lemma by itself.
- Reproducibility: the surviving `q = 5` computation is fully reproducible from the stated equations.
- Lean readiness: no. Formalizing the surviving auxiliary slice would not be the shortest remaining path to a sealed publication packet.
- Paper leverage: low in the current verified state.
- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `0.18`, not the pre-verify `0.76`, because the verified output no longer closes the row or the main structural obstruction.
- What title theorem is actually visible? At best: an auxiliary proposition classifying the order-`5` quotient profiles compatible with the centered norm-`25` equation.
- What part of the argument scales? The quotient-centering setup and the small exact enumeration on the `5`-quotient.
- What part clearly does not? The claimed semisimple-divisibility collapse for quotient orders `11` and `22`, and therefore the main rigidity theorem that was supposed to drive the obstruction.
- Best honest publication status: still `NONE`. The surviving slice is true-looking and reproducible, but it is not close enough to the title theorem of a micro-paper on this exact open row.

## verify_verdict
- `verify_verdict = "CRITICAL_FLAW"`
- `classification = "VARIANT"`
- `confidence = "high"`
- Reason: PASS 1 found no bounded rediscovery, but PASS 3 located a decisive proof failure in the main `11`/`22` rigidity lemma. Only a narrower repaired `q = 5` auxiliary slice survives.

## minimal_repair_if_any
- Conservative repair: retain only the repaired order-`5` auxiliary classification.
- Remove or mark unverified the quotient-order `11` and `22` exceptional-coset claims until a correct proof is supplied.
- Do not send this packet to Lean. The shortest honest next step is to either find a new proof of the `11`/`22` rigidity slice or cool the candidate as an unresolved structural partial.

## publication_prior_art_audit
- Audit date: `2026-04-15`.
- Exact-statement search: bounded web queries on `990 345 120 [2,G9,5,11]` and `(990,345,120) difference set` did not return a post-2019 paper or repository note explicitly settling this exact abelian row.
- Alternate-notation search: bounded queries using `C_2 x C_9 x C_5 x C_11` and `C_2 x C_3^2 x C_5 x C_11` likewise did not expose a direct settlement of the selected row.
- Canonical-source check: Gordon's ArasuFest 2019 slide deck directly lists `990 345 120 225 [2,G9,5,11]` on the Lander-conjecture slide among the small open abelian rows, while the same slide states only the separate theorem that if `n` is a power of a prime greater than `3` and `gcd(v,n) > 1`, then no abelian difference set exists. Since `n = 225 = 3^2 * 5^2`, that theorem does not close this row.
- Canonical-source theorem / proposition / example / corollary / observation / sufficient-condition check: inside the canonical source, the exact row appears only as an open case on the Lander-conjecture slide, not as an already-settled proposition, corollary, example, or sufficient-condition consequence.
- Current-status surfaces checked: Gordon's current difference-set repository page and current publications page. Within this bounded pass they do not expose a newer paper title, database note, or status page naming a closure of the exact `[2,G9,5,11]` row.
- Outside-source status pass: the bounded non-Gordon web search returned no direct paper or discussion page for this exact tuple or either alternate group notation. That is only a bounded negative search result, not a proof of novelty.
- Prior-art verdict: no rediscovery established inside budget, but there is also no literature support inside budget for treating the repaired order-`5` lemma as an independent paper-level contribution.

## publication_statement_faithfulness
- The intended statement is still the exact existence question for the Gordon row `[2,G9,5,11]`.
- The strongest verified statement is narrower: a conditional order-`5` quotient-profile classification for any hypothetical solution.
- That verified residue is stronger than "here is an example" because it classifies every integer profile compatible with the centered order-`5` quotient equation, but it does not settle the selected row.
- So the surviving output is faithful only as an auxiliary necessary-condition slice. It is not faithful as a closure of the intended theorem.

## publication_theorem_worthiness
- Is there a real theorem slice here? Yes, but only an auxiliary one.
- Strongest honest claim stronger than an example? Yes. It is a reproducible exact classification of the order-`5` quotient profiles `{81,66,66,66,66}` and `{57,72,72,72,72}`.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a theorem slice, but not a credible title theorem for a note about the selected frontier row.
- Is the proof structural or merely instance-specific? Mostly instance-specific. The surviving content is tied to the exact order-`5` quotient equation for this row and does not by itself create a broad structural obstruction.
- Would this survive a referee asking "what is the theorem?" Only as a supporting proposition inside a larger row-closing paper, not as the headline theorem of the paper itself.
- Is the claim still too dependent on hand-picked small cases? Yes. After verification removed the `11`/`22` rigidity step, the packet depends heavily on a single small quotient classification.

## publication_publishability
- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `0.18` in the current verified state.
- Is the remaining gap genuinely small? No. The candidate looked much closer before audit because the intended `11`/`22` rigidity theorem appeared to supply the missing obstruction; after verification that route is no longer available.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. The honest move is to cool or sideline the packet unless a new row-closing obstruction route is already visible.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Lean would only formalize an auxiliary lemma. It would not turn this packet into a human-ready publication result.

## publication_packet_audit
- Publication status remains `NONE`.
- Publication confidence is `high` on the negative audit judgment, subject only to the usual bounded-freshness caveat from the limited web pass.
- Title theorem strength is `weak` because the surviving theorem slice is not the title theorem of the selected row.
- Publication narrative strength is `weak`: "one local quotient lemma survives after the main obstruction failed" is not a micro-paper narrative.
- Publication packet quality is `supporting_slice_only`.
- Proof artifacts are preserved well enough for later reuse, but they do not currently make a human-ready packet.
- `human_ready = false`.
- `lean_ready = false`.

## micro_paper_audit
- MICRO-PAPER verdict: fail in the current audited state.
- The packet no longer offers a one-shot theorem where a single clean solve would already read like the note's title theorem.
- The strongest honest claim is a useful local lemma, but it does not honestly shorten the remaining path to publication enough for the micro-paper lane.
- This candidate therefore looked attractive before audit, but after skeptical checking it is not close enough to paper-shaped to keep active on the strict one-shot lane.

## strongest_honest_claim
For a hypothetical `(990,345,120)` difference set in an abelian group of Gordon type `[2,G9,5,11]`, the centered order-`5` quotient equation has exactly two cyclic-orbit profile types, yielding quotient profiles `{81,66,66,66,66}` and `{57,72,72,72,72}`. No verified `11`- or `22`-quotient rigidity theorem remains.

## paper_title_hint
No standalone frontier title is honest yet; at most: `Order-5 Quotient Profiles for Hypothetical (990,345,120) Difference Sets in Groups of Type [2,G9,5,11]`.

## next_action
Move this packet aside rather than expand it into a broader theorem program. Preserve the repaired order-`5` lemma, discard the broken `11`/`22` rigidity route as a publication basis, and reopen the row only if a genuinely new obstruction route appears.
