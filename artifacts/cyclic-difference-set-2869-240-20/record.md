# Solve Record: The Cyclic (2869,240,20) Difference-Set Case

- slug: `cyclic-difference-set-2869-240-20`
- working_packet: `artifacts/cyclic-difference-set-2869-240-20/working_packet.md`

## statement_lock
Determine whether the cyclic group C_2869 admits a (2869,240,20)-difference set.

## definitions
Write the ambient group additively as `G = Z/2869Z`, with `v = 2869 = 19 * 151`, `k = 240`, `lambda = 20`, and `n = k - lambda = 220`.

For a divisor `w | v`, let `u = v / w`, and let `pi_w : G -> Z/wZ` be reduction modulo `w`. If `D subset G` is a hypothetical difference set, define the contracted counts
`b_j = |D ∩ pi_w^{-1}(j)|` for `j in Z/wZ`.

Then the standard contraction identity from the source transfer kit is:
- `sum_j b_j = k = 240`;
- `sum_j b_j^2 = n + lambda u`;
- for each nonzero `t in Z/wZ`, `sum_j b_j b_{j-t} = lambda u`.

For `w = 19`, one has `u = 151`, so the numerical constraints become
- `sum_j b_j = 240`;
- `sum_j b_j^2 = 220 + 20 * 151 = 3240`;
- every nonzero periodic autocorrelation equals `20 * 151 = 3020`.

Conventions: when using a multiplier, I translate `D` first so the contracted coefficient vector is fixed by that multiplier action; this is the intended normalization from the working packet.

## approach_A
Structural / invariant route: work modulo `19`.

Reasoning:
- `2^12 ≡ 11 (mod 19)`;
- `5^3 ≡ 11 (mod 19)`;
- `11^1 ≡ 11 (mod 19)`.

So the prime divisors of `n = 220` admit powers with common residue `11 mod 19`. By the source multiplier input, the mod-`19` contraction can be normalized to satisfy `b_j = b_{11j}`. Since `11` has order `3 mod 19`, the nonzero residues split into six 3-cycles, so the entire contraction is determined by seven integers:
- `a = b_0`;
- `x_1, ..., x_6` on the six nonzero `11`-orbits.

This reduces the exact-row problem to a finite integer feasibility problem constrained simultaneously by:
- the size equation `a + 3(x_1 + ... + x_6) = 240`;
- the energy equation `a^2 + 3(x_1^2 + ... + x_6^2) = 3240`;
- the orbit-compressed autocorrelation equations for nonzero residues.

If this 7-variable system is inconsistent, the row is ruled out by a compact multiplier-plus-contraction obstruction, which is exactly the desired paper shape.

## approach_B
Construction / extremal / contradiction route: if the mod-`19` system survives, move to a second quotient and ask whether the surviving mod-`19` profiles can lift.

The natural fallback inside the same lane is `w = 151`, because `2869` has only the two prime factors `19` and `151`. The hope is that a second multiplier action modulo `151`, or even just the exact quotient equations there, forces an incompatible fiber-size distribution. Even before a full second multiplier analysis, one can use extremal inequalities:
- fixed total mass `240`,
- fixed quadratic energy `sum b_j^2 = 220 + 20 * 19 = 600` modulo `151`,
- bounded fiber sizes `0 <= b_j <= 19`.

This route is weaker structurally but useful as a contradiction filter: a valid difference set must survive both quotient geometries, not just the first.

## lemma_graph
`L1`. Any cyclic `(2869,240,20)` difference set yields, for each divisor `w | 2869`, a contracted count vector on `Z/wZ` with exact size, energy, and periodic-autocorrelation identities.

`L2`. For `w = 19`, the common residue calculation
`2^12 ≡ 5^3 ≡ 11 (mod 19)` activates the source multiplier theorem with multiplier `11`.

`L3`. The normalized mod-`19` contraction is therefore constant on the six nonzero `11`-orbits, hence depends on seven integers.

`L4`. Substituting that orbit form into the contraction identities gives a finite Diophantine system.

`L5`. If the system has no integral solution with `0 <= b_j <= 151`, then no cyclic `(2869,240,20)` difference set exists.

`L6`. If the mod-`19` system has survivors, test them against either the full nonzero autocorrelation equations or the mod-`151` contraction.

## chosen_plan
Best path: start with `w = 19` and push the multiplier normalization as far as possible before touching any code.

Why this is the best path:
- it uses the exact transfer-kit recommendation;
- it keeps the argument theorem-shaped rather than witness-shaped;
- it produces a compact finite obstruction problem in only seven variables;
- if it closes, the title theorem is already visible:
  `No cyclic (2869,240,20) difference set exists.`

If this closes cleanly, that solve would already be about 75% to 85% of a micro-paper. The minimal remaining packaging would be:
- place the row back into Baumert-Gordon Table 3,
- state the mod-`19` multiplier lemma cleanly,
- present the finite contradiction and one short boundary remark.

## self_checks
- Statement check: the intended theorem remains the exact cyclic row, not a softened surrogate.
- Definition check: the quotient equations are stated at the correct divisor level `u = v / w`.
- Approach check: both routes stay inside multiplier/contraction methods already licensed by the packet.
- Publication check: the main hoped-for output is a direct nonexistence theorem, not a loose computational curiosity.
- Step-5 check: the mod-`19` multiplier premise is explicit and arithmetic, namely `2^12 ≡ 5^3 ≡ 11 (mod 19)`.
- Step-6 check: the bounded mod-`19` experiment used the full nonzero autocorrelation equations, not only sum and square constraints.
- Step-7 check: the mod-`19` route does not close; the artifact records that failure honestly instead of inflating it into a theorem.
- Step-8 check: the mod-`151` multiplier premise is stronger, since `2` itself lies in the common power-intersection of `2`, `5`, and `11` modulo `151`.
- Step-9 check: the mod-`151` route yields a genuine rigid theorem slice, but still not the exact row theorem.

## code_used
Yes. I used two tiny bounded Python checks, both justified by the reasoning stage and both operating only on the quotient-contraction systems:

1. Mod `19`: enumerate the seven-variable `11`-orbit-constant contractions and test all exact nonzero autocorrelation equations.
2. Mod `151`: enumerate the eleven-variable `2`-orbit-constant contractions and test all exact nonzero autocorrelation equations.

No SAT / ILP / brute-force over subsets of `C_2869` was used. The computation stayed at the level of quotient fibers.

## result
No exact proof or disproof was obtained in this solve attempt.

What did close:
- The mod-`19` quotient does **not** by itself obstruct existence. The `11`-orbit-constrained contraction system has feasible solutions; an exact bounded enumeration found `16` such contractions.
- The mod-`151` quotient is much more rigid. Because `2` itself is a common residue-power of the prime divisors of `220` modulo `151`, any contracted vector can be normalized to be constant on the ten nonzero `2`-orbits of size `15`.
- For `w = 151`, the exact quotient equations admit exactly `2` such orbit-constant contractions. Up to swapping quadratic residues with quadratic nonresidues, they are:
  - `c_0 = 15`,
  - `c_x = 2` for every nonzero quadratic residue `x mod 151`,
  - `c_x = 1` for every quadratic nonresidue `x mod 151`.

Equivalently, the set of nonzero residue classes with doubled fiber size is forced to be the Paley `(151,75,37)` difference set in `C_151`, up to complement.

Immediate corollary / boundary remark:
- every nonzero mod-`151` fiber has size exactly `1` or `2`;
- exactly `75` of those fibers have size `2`, and they are the quadratic residues (or, symmetrically, the nonresidues);
- the zero fiber has size exactly `15`.

This is a real structural theorem slice, but it is still not enough to settle the existence question for `C_2869`.

## family_affinity
This sits squarely in the family of cyclic prime-product residual rows where a nontrivial multiplier on one prime quotient can collapse the case to a tiny orbit system. The mod-`151` outcome is especially characteristic of rows whose quotient contraction locks onto a Paley-type prime-field difference set.

## generalization_signal
Moderate to strong. The exact template that produced the mod-`151` rigidity should transfer to other Baumert-Gordon survivors with:
- `v = pq`,
- `gcd(v,n) = 1`,
- one prime quotient admitting a nontrivial common residue of the prime divisors of `n`,
- small orbit count after multiplier collapse.

What scales:
- quotient contraction identities,
- multiplier-orbit collapse,
- exact orbit-feasibility enumeration,
- recognition of a Paley-type forced quotient profile.

What does not obviously scale:
- the especially sharp uniqueness here depends on `ord_151(2) = 15` and the very small energy `sum c_j^2 = 600`, which drives the nonzero fiber sizes down to `1` and `2`.

## proof_template_reuse
Reusable template:
1. choose a prime divisor `w` of `v`;
2. find a nontrivial common residue of prime divisors of `n` modulo `w`;
3. normalize the contraction to be multiplier-invariant;
4. solve the resulting orbit-compressed quadratic/autocorrelation system;
5. identify whether the surviving heavy-fiber support is itself a known prime-field difference set, as happened here with the Paley `(151,75,37)` set.

## candidate_theorem_slice
Strongest exact slice from this run:

If a cyclic `(2869,240,20)` difference set exists, then after multiplier normalization its contraction modulo `151` is uniquely forced, up to exchanging quadratic residues and nonresidues, to the Paley-type profile
- `c_0 = 15`,
- `c_x = 2` on quadratic residues modulo `151`,
- `c_x = 1` on quadratic nonresidues modulo `151`.

Secondary slice:

The analogous mod-`19` contraction is `11`-orbit-constant and lies in a finite list of `16` exact feasible profiles, so the `19`-quotient alone is not decisive.

## smallest_param_shift_to_test
For this exact row, the next useful shift is not another family but a coupled argument:
- combine the rigid Paley-type mod-`151` contraction with the finite mod-`19` profile list;
- or attack mixed `19 x 151` character data rather than separate prime quotients.

If a neighboring parameter shift is needed later, the best candidates are other cyclic Table 3 survivors with `v = pq` and a prime quotient on which one prime divisor of `n` already generates a large multiplier orbit.

## why_this_is_or_is_not_publishable
At this stage the package is still too thin for the micro-paper lane.

Why it is not yet publishable:
- it does not settle the exact existence question;
- the strongest result is a quotient-classification proposition, not the title theorem;
- the main row still needs a coupling argument between the two prime quotients or an exact lift obstruction.

What would make it paper-shaped if the main claim closes:
- the mod-`151` Paley-type quotient classification would become an immediate supporting proposition;
- the mod-`19` finite profile list would become a short companion lemma;
- only light packaging would remain, because the source already isolates the row.

Assessment against the micro-paper target:
- a full solve here would still be about `0.75` of a paper;
- the current result alone is not enough and should remain below `PAPER_READY`.

## paper_shape_support
The exact title theorem is still clear: `On the nonexistence of a cyclic (2869,240,20) difference set`, if the obstruction closes. The current solve attempt now supplies the smallest honest support packet that would matter if that theorem is later proved:
- the explicit mod-`19` multiplier lemma,
- the finite mod-`19` feasible-profile list,
- the rigid mod-`151` Paley-type contraction theorem slice,
- one boundary remark explaining that quotient-wise obstructions alone appear exhausted.

Minimal remaining packaging work after a future full solve:
- present the decisive coupled contradiction,
- attach these two quotient propositions as setup,
- add short source placement inside Baumert-Gordon Table 3.

## boundary_remark
The mod-`151` slice is mathematically real, but on its own it still looks like an instance-level quotient classification rather than a paper. The current packet is closer to a paper-shaped claim than a bare witness search, yet still not enough for the micro-paper lane until the two-prime interaction is resolved.

## likely_failure_points
- The multiplier normalization may be weaker than expected if the source theorem requires a hypothesis I have not yet instantiated explicitly in the artifact.
- The mod-`19` orbit equations do admit a small feasible family, so that quotient is already exhausted as a stand-alone obstruction.
- The mod-`151` quotient is rigid but compatible, so a proof will likely need a genuinely coupled `19 x 151` argument rather than separate prime-quotient analyses.
- A next step that only repeats quotient-wise feasibility checks would likely add little.

## what_verify_should_check
Verify should check:
- that the multiplier theorem is being invoked with the exact hypothesis satisfied by `2^12 ≡ 5^3 ≡ 11 (mod 19)`;
- that the orbit partition under multiplication by `11 mod 19` has one fixed point and six 3-cycles on nonzero residues;
- that the mod-`19` bounded search really used the full contracted-coefficient identities, not only size and energy;
- that `2`, `5`, and `11` do indeed have a common residue-power equal to `2 mod 151`;
- that the mod-`151` exact search has only the two Paley-type surviving contractions and that their heavy support is exactly the quadratic residues / nonresidues;
- that the publication claim stays at `SLICE_CANDIDATE` rather than overclaiming a full solve.

## verify_rediscovery
Bounded rediscovery audit run on `2026-04-15` with limited web.

Searches covered:
- the exact tuple `(2869,240,20)`;
- alternate notation such as `C_2869`, `v = 2869, k = 240, lambda = 20`, and cyclic-difference-set phrasing;
- the canonical source itself;
- same-source theorem / proposition / example / observation / corollary coverage inside Baumert-Gordon 2004;
- one later Gordon citation / status-style surface.

Result:
- Baumert-Gordon 2004 still lists `(2869,240,20)` in Table 3 among the possible cyclic cases with `150 <= k <= 300` and `gcd(v,n) = 1`.
- The source theorem surface checked in the same paper is methodological: Theorem 3.1 gives the contracted count identities and Theorem 3.2 gives the multiplier criterion, but no same-source theorem, proposition, example, observation, or corollary settles the exact row `(2869,240,20)`.
- Within the capped web pass, no later paper, database page, or status note explicitly settling the exact tuple surfaced.

Verdict for PASS 1:
- rediscovery not established within budget;
- this is only bounded negative evidence, not a proof of novelty.

## verify_faithfulness
The artifact is faithful about one key point and unfaithful if read as a solve of the selected problem.

What matches:
- the record explicitly says no exact proof or disproof was obtained;
- the strongest stated result is a conditional quotient-classification slice, not the exact intended theorem.

What must be classified conservatively:
- the intended statement is still `Determine whether the cyclic group C_2869 admits a (2869,240,20)-difference set.`
- the checked claim is weaker and different:
  `If such a difference set exists, then its multiplier-normalized contraction modulo 151 is forced to the Paley-type profile.`

So the honest harness outcome is `classification = VARIANT`, not `EXACT`, and not a verified solve of the selected row.

## verify_proof
I checked the proof envelope against the canonical source method and reran the arithmetic independently.

Multiplier hypotheses:
- For `w = 19`, `n = 220 = 2^2 * 5 * 11` and
  `2^12 ≡ 5^3 ≡ 11 (mod 19)`,
  so Theorem 3.2 applies with `t = 11`.
- For `w = 151`,
  `2^1 ≡ 5^10 ≡ 11^55 ≡ 2 (mod 151)`,
  so Theorem 3.2 applies with `t = 2`.

Orbit structure:
- modulo `19`: one fixed point `0` and six nonzero `11`-orbits of size `3`;
- modulo `151`: one fixed point `0` and ten nonzero `2`-orbits of size `15`.

Independent reruns of the full Theorem 3.1 system reproduced the solver's claims:
- modulo `19`, there are exactly `16` orbit-constant contractions satisfying all nonzero autocorrelation equations;
- modulo `151`, there are exactly `2` orbit-constant contractions satisfying all nonzero autocorrelation equations;
- in those two `151`-quotient solutions, `c_0 = 15`, every nonzero coefficient is `1` or `2`, and the `75` heavy fibers are exactly the quadratic residues or exactly the quadratic nonresidues modulo `151`.

First incorrect step:
- none found inside the actual claim envelope that was checked.

Limitation:
- the verified argument does not couple the `19`- and `151`-quotients, so it does not reach an existence or nonexistence theorem for `C_2869`.

## verify_adversarial
No stored checker file existed in the artifact, so I reran independent plain-Python reconstructions of the compressed quotient systems as the adversarial check.

What survived adversarial rerun:
- the mod-`19` count `16` is correct, and the rerun used the full nonzero autocorrelation equations rather than only the size and square-sum equations;
- the mod-`151` count `2` is correct;
- the two mod-`151` survivors are complementary and their heavy support is exactly the quadratic-residue class split claimed in the record.

What did not survive as a theorem:
- no adversarial rerun turned the verified slice into an exact contradiction or construction;
- the exact existence question remains open after skeptical checking.

## verify_theorem_worthiness
- exactness: the selected theorem is still open; the verified deliverable is a conditional quotient-classification slice.
- novelty: bounded audit did not establish rediscovery of the exact row or of this exact slice, but novelty is not closed by the capped search.
- reproducibility: high. Independent reruns reproduced the orbit structure and the exact survivor counts `16` and `2`.
- Lean readiness: no. Lean would formalize a supporting proposition, not close the shortest remaining gap to a sealed publication packet.
- paper leverage: moderate as a support result, but insufficient by itself for the micro-paper lane.
- would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- what percentage of the paper would one full solve already provide? About `0.75`, as the selected packet says, but this artifact is materially short of that full solve.
- what title theorem is actually visible? `Any cyclic (2869,240,20) difference set has a unique multiplier-normalized mod-151 contraction, up to swapping quadratic residues and nonresidues.`
- what part of the argument scales? The multiplier-plus-contraction method on prime quotients, orbit compression, and exact feasibility reruns.
- what part clearly does not? Any jump from separate prime-quotient control to a full contradiction or construction for the exact row.
- best honest publication status: still only `SLICE_CANDIDATE`; the slice is theorem-shaped and reproducible, but it is publication-distant and not the title theorem of the target note.

Bottom line:
- this is a real verified variant;
- it is not a verified solution to the selected problem;
- it does not yet pass the micro-paper test on its own.

## verify_verdict
`VERIFIED`

Reason:
- bounded prior-art audit did not establish rediscovery;
- no incorrect step was found in the actual checked slice;
- the main correction is classification, not mathematics: this run verifies a nearby conditional theorem slice, so it should be preserved as `VARIANT`.

## minimal_repair_if_any
No mathematical repair is needed inside the checked slice.

The conservative repair is artifact-level:
- reclassify the run from `PARTIAL` to `VARIANT`;
- keep the strongest honest claim at the mod-`151` Paley-type contraction slice;
- do not mark Lean as the next lane, because formalizing this slice would not close the real publication gap.

## publication_prior_art_audit
Audit date: `2026-04-15`.

- Exact statement search: bounded web searches for `(2869,240,20)` and `cyclic difference set` surfaced Baumert-Gordon 2004 as the tuple-specific indexed source, with no explicit later settlement in view.
- Alternate notation search: `C_2869`, `v = 2869, k = 240, lambda = 20`, and cyclic-difference-set wording again surfaced the same source and no later tuple-specific theorem.
- Canonical source check: the tuple appears in Baumert-Gordon 2004 Table 3 as a surviving possible cyclic case. Within the same paper, Theorems 3.1 and 3.2 are method theorems, and the eliminated-case table does not contain `(2869,240,20)`, so no same-source theorem, proposition, example, observation, corollary, or sufficient-condition statement settles the row.
- Outside-source status pass: Gordon's Difference Set Repository is the natural later status surface. The bounded exact-tuple queries surfaced the repository itself but no indexed page announcing existence or nonexistence for `(2869,240,20)`.
- Recent follow-up check: not triggered. The narrow search created no concrete ambiguity requiring a broader literature pass.

Verdict:
- bounded negative evidence against rediscovery only;
- no later settlement surfaced within budget;
- novelty of the exact row or of the verified slice is not closed absolutely.

## publication_statement_faithfulness
- The selected statement is still `Determine whether the cyclic group C_2869 admits a (2869,240,20)-difference set.`
- The strongest audited claim is weaker: a verified conditional quotient-classification theorem slice modulo `151`.
- So any publication claim beyond slice level would be unfaithful to the artifact.
- The packet is faithful only if read as a preserved `VARIANT` support result, not as a solution of the selected row.

## publication_theorem_worthiness
- Is the strongest honest claim stronger than `here is an example`? Yes. It is a structural if-exists theorem slice with a unique multiplier-normalized mod-`151` profile.
- Is there a real theorem slice here? Yes. The slice is precise, reproducible, and referee-legible as a proposition.
- Is the proof structural or merely instance-specific? Structural inside one exact instance: it uses multiplier orbits, contraction identities, and a forced Paley-type quotient profile rather than a hand-picked witness.
- Would this survive a referee asking `what is the theorem?` Only partially. There is a real theorem, but it reads like a supporting proposition rather than the title theorem of a short note.
- Is the claim still too dependent on hand-picked small cases? Not mathematically, but yes in publication leverage: the theorem is pinned to one exact row and one prime quotient.

## publication_publishability
- Publication verdict: not paper-ready.
- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a real theorem slice, but not the title theorem the note needs.
- Is the remaining gap genuinely small? No. The unresolved step is still the main existence/nonexistence theorem for the row, and the next move appears to require a substantive coupled `19 x 151` obstruction or exact lift argument.
- Did the candidate only look attractive before audit? The candidate still looks attractive if fully solved, but the current packet only looked close before audit. At publication stage it is still materially short of the one-shot stop tier.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Preserve the slice and move the slug aside unless a concrete coupled obstruction is already available; do not widen this into a feeder-ladder program.
- Would Lean directly seal the packet, or would it only be optional polish? Only optional polish. Lean would formalize a support proposition but would not change the publication verdict.

## publication_packet_audit
- publication_status: `SLICE_EXACT`
- publication_confidence: `medium`
- publication_packet_quality: `supporting_slice_only`
- proof_artifacts_preserved: `true`
- lean_ready: `false`
- human_ready: `false`

## micro_paper_audit
- What percentage of the paper would one solve already provide? About `0.75`; a genuine proof or disproof of the selected row would still be most of a short note.
- What percentage of the paper does the current packet already provide? Roughly `0.35` to `0.45`; the title theorem is still absent.
- Micro-paper verdict: fail the stop rule. The verified slice is stronger than a curiosity and useful as setup, but it is not most of a publishable note.
- Lane decision: preserve as a support packet and reopen only for a decisive coupled obstruction or exact disproof/proof.

## strongest_honest_claim
If a cyclic `(2869,240,20)` difference set exists, then after multiplier normalization its contraction modulo `151` is uniquely forced, up to exchanging quadratic residues and nonresidues, to satisfy `c_0 = 15`, `c_x = 2` on one square class, and `c_x = 1` on the other.

## paper_title_hint
A forced mod-`151` Paley-type quotient profile in the cyclic `(2869,240,20)` difference-set problem

## next_action
Preserve this as a verified variant-side support packet and move the slug aside. Reopen only if there is a concrete coupled `19 x 151` obstruction or exact lift contradiction; do not expand into a broader theorem program.
