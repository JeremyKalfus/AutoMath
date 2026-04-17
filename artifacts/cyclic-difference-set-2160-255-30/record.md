# Solve Record: Does the cyclic group C_2160 admit a (2160,255,30)-difference set?

- slug: `cyclic-difference-set-2160-255-30`
- working_packet: `artifacts/cyclic-difference-set-2160-255-30/working_packet.md`

## statement_lock
Determine whether the cyclic group C_2160 admits a (2160,255,30)-difference set.

Exact intended theorem for this solve pass: either prove that no cyclic difference set with parameters `(2160,255,30)` exists, or produce a theorem-facing obstruction package narrow enough that one bounded quotient check remains. If the nonexistence proof closes, the title theorem is:

`The cyclic group C_2160 does not admit a (2160,255,30)-difference set.`

If it closes honestly, this should already be about `75%` to `85%` of a short micro-paper because Baumert-Gordon already isolate this exact row and the remaining work is mainly exposition plus verify-stage novelty checking.

## definitions
Work additively in `G = Z/2160Z`. A `(2160,255,30)` difference set is a subset `D ⊂ G` of size `255` such that every nonzero element of `G` has exactly `30` ordered representations as `d1 - d2` with `d1,d2 ∈ D`.

Set `n = k - λ = 225 = 15^2`.

For any quotient of order `w | 2160`, with kernel size `m = 2160 / w`, if the contracted coefficients are `b_0, ..., b_{w-1}`, then the standard group-ring contraction identities give

- `sum b_i = 255`
- `sum b_i^2 = n + λ m = 225 + 30m`
- for every nonzero shift `j mod w`, `sum_i b_i b_{i-j} = 30m`

Equivalently, every nonprincipal character on the quotient has squared character sum `225`.

Baumert-Gordon's multiplier transfer kit indicates that because the prime powers dividing `n` are `9` and `25`, any quotient `C_w` with `9 ≡ 25 (mod w)` should inherit a `w`-multiplier orbit constraint. The only nontrivial divisors of `2160` of that form are divisors of `16`, so the clean multiplier quotient here is `w = 16`, with multiplier `9`.

Ambiguities and conventions:

- I am treating the contracted sum/square/correlation equations as rederived from the difference-set group-ring identity, not as a new theorem claim.
- The precise Baumert-Gordon multiplier citation still needs verify-stage auditing, but the transfer kit already points to the exact `w = 16` lane.
- Solve runs with web disabled, so I am not making any rediscovery claim here.

## approach_A
Structural / invariant route.

1. Use the `w = 16` multiplier coming from `9 ≡ 25 (mod 16)` to force the mod-`16` contracted coefficients constant on multiplication-by-`9` orbits.
2. Exploit the orbit structure on `C_16`:
   - all even residues are fixed,
   - odd residues come in four pairs `{1,9}`, `{3,11}`, `{5,13}`, `{7,15}`.
3. Combine the quotient equations with the order-`2` character on `C_16` to force the even/odd totals.
4. Try to drive a contradiction either directly on `C_16`, or by combining the mod-`16` orbit data with a small odd-part quotient such as `C_3`, `C_5`, or `C_15`.

Self-check after approach A: this is the exact source-recommended lane and it keeps the argument theorem-shaped if it closes, but it is not obvious a priori that `C_16` alone is rigid enough.

## approach_B
Construction / extremal / contradiction route.

1. Ignore the multiplier at first and solve the tiny quotient contractions on the odd part.
2. Mod `2` contraction is forced by the order-`2` character, and mod `3` contraction can be solved exactly from the sum and square-sum equations.
3. Refine to `C_6` and then `C_15 ≅ C_3 × C_5`, searching only quotient coefficient profiles rather than subsets of `C_2160`.
4. If no mod-`15` contracted coefficient vector exists at all, the row is dead without ever touching the full group.

Self-check after approach B: this is a bounded exact obstruction lane, not a brute-force search on `C_2160`, but it may fail if `C_15` still has viable quotient profiles and the `16`-multiplier really is needed.

## lemma_graph
Current lemma skeleton:

1. Any quotient contraction to `C_w` satisfies the exact sum, square-sum, and nonzero-correlation equations with target `30 * (2160 / w)`.
2. On `C_2`, if the two contracted coefficients are `(u,v)`, then
   - `u + v = 255`
   - `u - v = ±15`
   forcing `(u,v) = (135,120)` up to order.
3. On `C_3`, if the three coefficients are `(a,b,c)`, then
   - `a + b + c = 255`
   - `a^2 + b^2 + c^2 = 225 + 30 * 720 = 21825`
   Writing `a = 85 + x`, `b = 85 + y`, `c = 85 - x - y`, one gets `x^2 + y^2 + xy = 75`, whose integer solutions force `(a,b,c)` to be a permutation of `(90,90,75)`.
4. Combining the mod-`2` and mod-`3` data, the mod-`6` contraction has only two row-split types up to cyclic translation:
   - even-row counts `(45,45,45)` and odd-row counts `(30,45,45)`, or
   - even-row counts `(35,50,50)` and odd-row counts `(40,40,40)`,
   where the column totals are `(75,90,90)`.
5. On `C_16`, the `9`-multiplier forces odd residues paired across distance `8`, so if the mod-`16` coefficients are `e_0,...,e_7` on even classes and `o_0,...,o_3` on the odd pairs, then
   - `sum e_r + 2 sum o_r = 255`
   - the order-`2` character gives `sum e_r - 2 sum o_r = 15`
   hence `sum e_r = 135` and `sum o_r = 60`.
6. The natural next exact slice is therefore quotient-only: determine whether any mod-`15` coefficient vector exists, and if so whether it is compatible with the mod-`16` orbit constraints.

Self-check after lemma graph: the currently honest theorem slice is real and narrow, but not yet a disproof.

## chosen_plan
Choose approach B first, with approach A held in reserve.

Reason:

- the mod-`2` and mod-`3` contractions already collapse to exact small profiles;
- a contradiction on `C_15` would be stronger than a merely suggestive mod-`16` slice and would already look like the core of a short note;
- if mod-`15` survives, then the remaining obstruction lane is clear: combine the surviving odd-part contractions with the source-anchored `w = 16` multiplier data.

Extra structure that would make the row paper-shaped if the main claim closes:

- an exact proposition classifying the mod-`3` contraction as `(90,90,75)`,
- either a no-go theorem for the mod-`15` contraction or a no-go refinement of those mod-`15` profiles against the `w = 16` orbit pattern,
- one boundary remark explaining why the arithmetic coincidence `9 ≡ 25 (mod 16)` is the special feature of this exact row.

Update after the bounded quotient search:

- the odd-part route alone does **not** kill the row;
- the mod-`5` contraction has exactly two profiles up to cyclic rotation:
  - `(39,54,54,54,54)`,
  - `(63,48,48,48,48)`;
- each of those lifts to an explicit valid mod-`15` contraction with mod-`3` row sums `(75,90,90)`:
  - type A: one column `(3,18,18)` and four columns `(18,18,18)`,
  - type B: one column `(27,18,18)` and four columns `(12,18,18)`;
- both surviving mod-`15` contractions admit valid mod-`30` parity refinements, so the next real obstruction must use the `16`-multiplier data rather than smaller odd-part quotients.

## self_checks
- The contraction sum/square formulas were rederived locally from the quotient group-ring identity, not copied without reconstruction.
- The mod-`2` contraction really is forced to `(135,120)` because the negative sign would make the parity total nonintegral.
- The mod-`3` quadratic reduction is exact and leaves only permutations of `(90,90,75)`.
- The bounded experiment stayed at quotient level only: first `C_5`, then `C_15`, then a parity-difference refinement on `C_30`.
- The current artifact is still solve-stage only. I do not yet have a proof or a counterexample, but I now know that the low odd-part quotient route survives in only a tiny explicit way.

## code_used
Minimal code was used, but only after the reasoning package above was written.

Exact bounded computations performed:

1. `C_5` contraction search:
   - exact profiles are only the two cyclic types
     - `(39,54,54,54,54)`
     - `(63,48,48,48,48)`.
2. `C_15 ≅ C_3 × C_5` refinement:
   - both mod-`5` types survive;
   - explicit valid contractions are
     - type A: one column `(3,18,18)` and four columns `(18,18,18)`,
     - type B: one column `(27,18,18)` and four columns `(12,18,18)`.
3. `C_30` parity-difference refinement:
   - writing `d = e - o` for the even-minus-odd split of the mod-`15` cells, the exact perfect-sequence condition on `d` also survives;
   - a valid nontrivial refinement for both type A and type B is
     - one column `(-1,8,8)` and four columns `(4,-2,-2)`;
   - type B also admits the trivial concentrated refinement
     - one column `(15,0,0)` and four zero columns.

No SAT, ILP, CP-SAT, or full-group brute force was used.

## result
Current result: partial structural package only.

Supported so far:

- the exact intended statement is locked;
- mod `2` contraction is forced to `(135,120)`;
- mod `3` contraction is forced to a permutation of `(90,90,75)`;
- mod `6` contraction has only two split types up to translation;
- mod `16` contraction must respect the `9`-multiplier orbit partition, with total mass `135` on even residues and `120` on odd residues;
- mod `5` contraction has only two profiles up to rotation: `(39,54,54,54,54)` and `(63,48,48,48,48)`;
- mod `15` contraction survives only in two tiny explicit families:
  - one column `(3,18,18)` with four `(18,18,18)`,
  - one column `(27,18,18)` with four `(12,18,18)`;
- both mod-`15` families admit exact mod-`30` parity refinements.

Not yet supported:

- nonexistence of the cyclic `(2160,255,30)` difference set;
- existence of such a difference set;
- a contradiction linking the surviving `C_15` / `C_30` profiles to the `w = 16` multiplier data.

Best current theorem-facing statement:

`Any cyclic (2160,255,30) difference set would have one of two explicit mod-15 contractions, and both of those already admit compatible mod-30 parity refinements; therefore any eventual disproof must use finer 2-primary structure than the odd-part quotient equations alone.`

## family_affinity
Strong. This is exactly the Baumert-Gordon residual-case lane: a single cyclic source row, a square `n`, and a contraction-plus-multiplier obstruction strategy rather than a broad campaign.

## generalization_signal
Moderate positive signal.

What looks reusable:

- solve the smallest odd-part quotients exactly first;
- isolate a mod-`2` or mod-`p` split from the order-`2` or low-order characters;
- use the special congruence between prime powers dividing `n` to obtain a source-anchored multiplier quotient on a small divisor of `v`.

What does not yet look reusable:

- the precise mod-`6` split types,
- the explicit surviving mod-`15` / `C_30` profiles,
- any eventual contradiction that depends specifically on `9 ≡ 25 (mod 16)`.

What part of the argument scales:

- solve the smallest quotient contractions exactly,
- classify surviving quotient profiles before escalating,
- use those survivors to prove that any future contradiction must come from a specific remaining source-supported lane.

What part does not scale well:

- the explicit `C_15` and `C_30` profile search is row-specific and mainly useful as elimination of false easy lanes.

## proof_template_reuse
Current reusable template:

1. rederive quotient contraction equations from the difference-set identity,
2. solve the smallest quotient profiles exactly,
3. isolate one special source-supported multiplier quotient,
4. intersect the quotient data rather than search the full cyclic group.

This is a real template for other residual cyclic rows, but the exact arithmetic obstruction is still row-specific here. The present run also shows a negative lesson worth reusing: if the odd-part quotient survives in a tiny explicit family, stop spending budget there and push immediately to the special multiplier quotient.

## candidate_theorem_slice
Candidate theorem slice.

If `D ⊂ C_2160` is a cyclic `(2160,255,30)` difference set, then:

- its mod-`2` contraction is exactly `(135,120)`,
- its mod-`3` contraction is a permutation of `(90,90,75)`,
- hence its mod-`6` contraction has only two split types up to translation,
- its mod-`5` contraction is, up to cyclic rotation, either `(39,54,54,54,54)` or `(63,48,48,48,48)`,
- its mod-`15` contraction is, up to cyclic translation, one of exactly two explicit families:
  - one column `(3,18,18)` and four columns `(18,18,18)`,
  - one column `(27,18,18)` and four columns `(12,18,18)`,
- both of those families admit compatible parity refinements on `C_30`,
- and its mod-`16` contraction is constant on the `9`-multiplier orbits, with total mass `135` on even residues and `120` on odd residues.

The smallest visible theorem slice is now a stronger quotient-classification proposition: the entire low odd-part lane is classified and survives, so the unresolved mathematics is specifically the interaction with the `16`-adic multiplier structure.

## smallest_param_shift_to_test
If this row survives the current attempt, the most informative nearby shifts are:

- other cyclic rows where the prime powers dividing `n` become congruent modulo a small divisor of `v`,
- or sibling rows where the odd-part quotient is as small as `C_3 × C_5`.

Those are the cases most likely to admit the same quotient-first then multiplier-refinement workflow.

For this exact row, the next parameter shift that would help most is not a nearby `(v,k,λ)` tuple but a nearby quotient choice: a mixed quotient that still carries the `16`-multiplier signal, such as `C_48`, `C_80`, or `C_240`, if the Baumert-Gordon theorem supports pushing the `16`-orbit information into a compatible odd-part refinement.

## why_this_is_or_is_not_publishable
Not publishable yet.

- A successful exact disproof here would likely already be `70%` to `90%` of a paper, because the title theorem is fixed and the surrounding note is short.
- The exact title theorem would be `The cyclic group C_2160 does not admit a (2160,255,30)-difference set.`
- Minimal remaining packaging work, if the solve closes, would be:
  - state the Baumert-Gordon Table 2 anchor,
  - write the quotient identities cleanly,
  - present the decisive contradiction,
  - add one short boundary remark about why this row needs the `16`-adic coincidence.
- The current package is still too thin for the micro-paper lane because it stops at a classified survival slice rather than theorem closure.

## paper_shape_support
Paper-shape support if the main claim closes:

- the source already isolates the exact row;
- the theorem is narrow and exact rather than feeder work;
- the natural supporting structure is cheap: one quotient-classification lemma, one decisive contradiction, and one immediate remark removing a residual Ryser-table row.

At present, the missing ingredient is the decisive contradiction itself. The current slice helps by showing exactly what the contradiction cannot be: it will not come from naive `C_5`, `C_15`, or `C_30` quotient elimination alone.

## boundary_remark
Boundary remark already visible:

The standard easy arithmetic filters are spent before this row appears in Baumert-Gordon's table, so any real proof must use sharper quotient structure. The special arithmetic feature of this row is that the prime powers in `n = 225` coincide modulo `16`, making the `2`-primary quotient the only obvious multiplier-controlled quotient.

Concrete boundary remark after the experiment:

The entire odd-part quotient lane survives in explicit tiny families, so the row is not going to fall to a cheap `3`- and `5`-part contraction alone. Any true disproof now has to detect incompatibility between those surviving low quotients and the `16`-adic multiplier symmetry.

## likely_failure_points
- The mod-`15` quotient may still admit viable profiles, in which case the odd-part contraction alone does not settle the row.
- The current verified packet no longer supports the stronger claim that the `(75,90,90)` mod-`3` branch exhausts the odd-part lane, so any publication-facing theorem must be stated strictly below that failed exhaustiveness line.
- The `w = 16` multiplier slice may be too weak unless it is combined with a more refined mixed quotient.
- The surviving explicit `C_30` refinements show that even parity information alone is not enough.
- Verify may later require a more precise statement of the Baumert-Gordon multiplier theorem than the current solve-stage paraphrase.

## what_verify_should_check
- Audit the exact Baumert-Gordon Theorem `3.1` / `3.2` wording used for the `w = 16` multiplier-orbit claim.
- Recheck the mod-`2` and mod-`3` contraction derivations line by line.
- Recheck the exact bounded searches:
  - the two `C_5` profiles,
  - the two explicit `C_15` contractions,
  - the `C_30` parity refinements.
- Verify that all code stayed at the quotient-profile level and encoded the exact correlation targets correctly.
- If the row remains partial, verify whether the stronger explicit quotient-classification slice is strong enough to merit `SLICE_CANDIDATE` or should fall back to `NONE`.

## verify_rediscovery
Bounded prior-art audit run on `2026-04-15`.

- Query patterns used within budget: the exact tuple `(2160,255,30)`, alternate notation with `C_2160`, the canonical Baumert-Gordon 2004 source, same-source theorem / proposition coverage, and a bounded Dan Gordon / residual-status surface check.
- The canonical source still lists `(2160,255,30)` as a surviving cyclic case; the bounded exact-tuple searches did not surface a later paper or database page explicitly settling this exact row.
- PASS 1 therefore did not establish rediscovery.

Conclusion: `REDISCOVERY` is not supported within the bounded audit budget.

## verify_faithfulness
The artifact is not faithful to the intended statement.

- Intended statement: determine whether the cyclic group `C_2160` admits a `(2160,255,30)` difference set.
- Actual supported content after skeptical checking is narrower: several low-quotient necessary conditions, plus two explicit `C_15` / `C_30` witnesses inside one mod-`3` branch.
- The load-bearing mismatch is that the record presents the mod-`3` contraction as uniquely forcing a permutation of `(90,90,75)`, and then treats the resulting `C_15` / `C_30` classification as exhaustive. That is false.

Faithfulness verdict: `VARIANT`.

## verify_proof
First incorrect step found:

> In `lemma_graph`, item 3, the record claims that `x^2 + y^2 + xy = 75` forces `(a,b,c)` to be a permutation of `(90,90,75)`.

Why this fails:

- Writing `(a,b,c) = (85+x,85+y,85-x-y)`, the equation `x^2 + y^2 + xy = 75` also has the integer solution `(x,y) = (10,-5)`.
- That gives the additional mod-`3` contraction family `(95,80,80)` up to permutation.
- A direct rerun of the exact mod-`3` contraction equations confirms six solutions:
  - permutations of `(90,90,75)`,
  - permutations of `(95,80,80)`.

Downstream consequence:

- The stated mod-`6` split types are not exhaustive.
- The record's row-target choice `(75,90,90)` is only one branch.
- The claimed exhaustive mod-`15` and mod-`30` classifications are therefore not proved.

Supported subclaims that do survive skeptical checking:

- mod-`2` contraction is exactly `(135,120)` up to order;
- mod-`5` contraction has exactly two cyclic classes, namely `(39,54,54,54,54)` and `(63,48,48,48,48)`;
- the two displayed `C_15` contractions are valid exact contractions;
- the displayed parity-difference refinement `(-1,8,8)` with four columns `(4,-2,-2)` is a valid witness for both displayed `C_15` families.

## verify_adversarial
Adversarial reruns were arithmetic and bounded.

- Recomputed the exact mod-`3` contraction system: besides permutations of `(90,90,75)`, permutations of `(95,80,80)` also satisfy the equations.
- Recomputed the reduced mod-`5` search: there are `10` solutions total, forming exactly two rotation classes:
  - `(39,54,54,54,54)`,
  - `(48,48,48,48,63)`, i.e. the same class as `(63,48,48,48,48)`.
- Rechecked the two displayed `C_15` matrices directly on `C_3 x C_5`; both satisfy the exact autocorrelation targets.
- Rechecked the displayed parity-difference witness and confirmed it is entrywise admissible and has zero nontrivial autocorrelation for both displayed `C_15` families.
- No preserved checker file exists in the candidate artifact. The computational claims were reproducible only by rerunning the worker-log snippets.

Adversarial conclusion: some local witnesses are real, but the advertised exhaustive classification breaks at the missed mod-`3` branch.

## verify_theorem_worthiness
Assessment after skeptical checking:

- Exactness: fails for the intended statement.
- Novelty: bounded PASS 1 found no rediscovery, but the current verified packet is only a helper-lemma variant.
- Reproducibility: partial. The arithmetic can be rerun, but the candidate did not preserve a durable checker.
- Lean readiness: no. Lean would only formalize helper quotient lemmas while the theorem-sized gap remains unresolved.
- Paper leverage: low in current form.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? The currently verified packet is only about `20%` to `30%` of a note.
- What title theorem is actually visible? At best: low-quotient necessary conditions for hypothetical cyclic `(2160,255,30)` difference sets.
- What part of the argument scales? Exact contraction classification on very small quotients, and branch-specific witness verification.
- What part clearly does not? The claimed exhaustive `C_15` / `C_30` classification until the missed `(95,80,80)` mod-`3` branch is checked, and the still-unresolved interaction with the `16`-adic multiplier lane.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? `NONE`.

The honest packet no longer meets the micro-paper lane: it is a collection of verified helper constraints, not a theorem-shaped exact-case result.

## verify_verdict
- `verify_verdict = "VARIANT"`
- `classification = "VARIANT"`
- `confidence = "high"`
- strongest honest claim: any cyclic `(2160,255,30)` difference set must satisfy the verified mod-`2`, mod-`3`, and mod-`5` contraction constraints above, and the displayed `C_15` / `C_30` objects are valid branch witnesses only, not an exhaustive classification.
- `publication_status = "NONE"`
- `next_action = "preserve the verified low-quotient lemmas, rerun the mod-15 branch analysis with both mod-3 families, and only then revisit the mixed-quotient / mod-16 multiplier lane"`

## minimal_repair_if_any
Tiny conservative repair available:

- replace the mod-`3` sentence by: "the mod-`3` contraction is a permutation of either `(90,90,75)` or `(95,80,80)`";
- downgrade every downstream `C_15` / `C_30` statement from "only" / "exactly" to "displayed valid witnesses in the `(75,90,90)` branch";
- do not advertise any exhaustive low odd-part classification until the `(95,80,80)` branch has been checked.

## publication_prior_art_audit
Bounded web audit performed on `2026-04-15`.

- Exact-statement searches for the tuple `(2160,255,30)` and the phrasing `cyclic difference set` surfaced Baumert-Gordon 2004 as the only exact-row hit.
- Alternate-notation searches using `C_2160`, `v=2160, k=255, lambda=30`, and the residual-data phrasing `n=225`, `gcd(v,n)=45` did not surface a later theorem, proposition, example, corollary, or observation settling this exact row.
- Canonical-source check: Baumert-Gordon 2004 Table 2 explicitly lists `2160 255 30 225 45` among the possible cyclic cases with `150 <= k <= 300` and `gcd(v,n) > 1`. Section `3.2` gives the contracted-coefficient equations (Theorem `3.1`) and contracted-multiplier criterion (Theorem `3.2`) used by the local solve attempt. The paper does not later give a dedicated elimination or construction for `(2160,255,30)`; its worked elimination in Section `3.3` is the different row `(429,108,27)`.
- Outside-status pass: the current Dan Gordon / La Jolla difference-set repository remains the intended status surface for small and medium parameter searches, but the bounded web pass did not expose a tuple-specific page for `(2160,255,30)`. The honest inference is therefore negative-only: no later direct settlement surfaced, but I do not have a database-export line proving the row is still marked open there.
- One recent follow-up check was sufficient: Gordon's `On difference sets with small lambda` (published `2020-11-21`, issue `2022`) cites both Baumert-Gordon 2004 and the current repository, but the surfaced text does not mention `(2160,255,30)` and does not change the exact-row status.

Conservative verdict: not a rediscovery in the bounded sources reviewed, but also not frontier-certified beyond `no surfaced later exact settlement`.

## publication_statement_faithfulness
The publication-facing statement must be cut back below the stronger solve-stage narrative.

- The canonical source only isolates the row and supplies the contraction / multiplier toolkit. It does **not** claim that the low odd-part lane is exhausted for `(2160,255,30)`.
- Verify-stage checking already showed that the stronger local statement about exhaustive mod-`15` / mod-`30` classification was not faithful: the packet only verifies exact mod-`2`, mod-`3`, and mod-`5` contraction constraints, plus explicit `C_15` / `C_30` witnesses inside one mod-`3` branch.
- The faithful theorem-facing residue is therefore a helper-lemma package about forced low-quotient profiles, not a nonexistence theorem and not an exhaustive low-quotient classification.

## publication_theorem_worthiness
The strongest honest claim is stronger than `here is an example`, but not strong enough to be the theorem of a note.

- Stronger than an example: yes. The packet contains exact necessary constraints on quotient contractions, not just one constructed witness.
- Real title theorem or theorem slice: only in the weak auxiliary sense. The current slice is a row-specific helper proposition, not the title theorem one would put on page 1.
- Structural versus instance-specific: mixed. The method is structural because it uses contracted-coefficient identities and multiplier structure, but the surviving content is still heavily row-specific and does not close the row.
- Referee test `what is the theorem?`: as a standalone note, this currently fails. A referee could reasonably say that the packet identifies some failed easy lanes but does not yet settle the advertised problem.

## publication_publishability
Current verdict: not publishable as a micro-paper packet.

- Would the current bounded result already constitute most of a publishable note? No.
- Best current percentage estimate: about `25%` of a publishable note. The family anchor and helper lemmas are real, but the decisive mathematics is still missing.
- Is the remaining gap genuinely small? No. After verify removed the claimed exhaustiveness of the odd-part lane, the missing step is again the main theorem-sized contradiction, not light packaging.
- Is the claim still too dependent on hand-picked small cases? Yes. The concrete `C_15` / `C_30` witnesses live in one branch and mainly show that several cheap quotient routes do **not** work.
- Should this be moved aside rather than expanded into a larger theorem program? Yes. Preserve the verified helper lemmas and cool the slug unless a concrete `16`-adic / mixed-quotient attack is ready. Do not turn this into a broader exploratory campaign.
- Would Lean directly seal the packet? No. Lean could archive helper lemmas, but formalization would be optional polish and would not convert the packet into a theorem-ready note.

## publication_packet_audit
- Publication-status call: `NONE`.
- Reason: the packet is not a rediscovery, but it also does not clear the `SLICE_CANDIDATE` bar because the remaining gap is still theorem-sized rather than editorial.
- Publication-packet quality: thin helper packet only.
- Proof artifacts preserved: yes. The verified quotient constraints and branch witnesses are worth keeping as bounded local memory.
- Human-ready: no.

## micro_paper_audit
Micro-paper verdict: fail in the current audited state.

- The candidate looked strong pre-audit because the exact row is source-anchored and would be paper-shaped **if solved**.
- After verify and bounded publication audit, the honest packet is no longer close to that solve. What remains is a helper-slice package explaining that the easy odd-part quotient lane does not close the case.
- Single-solve-to-paper fraction for the current packet should therefore stay low, around `0.25`, not in the original `0.76` lane.
- Title-theorem strength is weak in publication terms, because the current packet does not yet give a theorem a referee would recognize as the note's main contribution.
- Publication narrative strength is weak: the current story is `these easy quotient eliminations do not suffice`, which is useful internal knowledge but not yet a publishable theorem note.

## strongest_honest_claim
Any cyclic `(2160,255,30)` difference set must satisfy the exact mod-`2`, mod-`3`, and mod-`5` contraction constraints established in verify, and the displayed `C_15` / `C_30` objects are valid witnesses only inside one mod-`3` branch. The current packet therefore preserves helper quotient structure for the row, but it does **not** yet supply an exhaustive low-quotient classification, a final obstruction, or an existence construction.

## paper_title_hint
Low-Quotient Constraints for the Cyclic `(2160,255,30)` Difference-Set Problem

## next_action
Move the row aside as `not paper-ready` in its current state while preserving the verified helper lemmas. Reopen only with a concrete `16`-adic / mixed-quotient plan that directly targets the remaining theorem-sized gap; Lean, if used now, should be limited to archival sealing of helper lemmas rather than treated as publication progress.
