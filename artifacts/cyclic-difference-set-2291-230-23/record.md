# Solve Record: The Cyclic (2291,230,23) Difference-Set Case

- slug: `cyclic-difference-set-2291-230-23`
- working_packet: `artifacts/cyclic-difference-set-2291-230-23/working_packet.md`

## statement_lock
Determine whether the cyclic group C_2291 admits a (2291,230,23)-difference set.

## definitions
Let `D ⊂ Z/2291Z` be a putative cyclic difference set with parameters `(v,k,λ) = (2291,230,23)`. Then every nonzero residue of `Z/2291Z` must occur exactly `23` times among ordered differences `d_1 - d_2` with `d_i ∈ D`, and
`n := k - λ = 207 = 3^2 * 23`.

For each divisor `w | 2291`, let `π_w : Z/2291Z -> Z/wZ` be the quotient map and let
`b_j := |D ∩ π_w^{-1}(j)|`.
If `m = 2291 / w`, then the contracted vector `b = (b_j)_{j ∈ Z/wZ}` satisfies:

- `sum_j b_j = 230`
- `sum_j b_j^2 = n + λ m`
- for every nonzero `s ∈ Z/wZ`, `sum_j b_j b_{j-s} = λ m`

The identity-coefficient formula `sum_j b_j^2 = n + λ m` will be used at `w = 29`, where `m = 79`, so
`sum_j b_j^2 = 207 + 23 * 79 = 2024`.

## approach_A
Structural / invariant route: work modulo `29`.

Because `2291 = 29 * 79`, the quotient `Z/2291Z -> Z/29Z` has kernel size `79`. The packet's intended source lane is Baumert-Gordon Theorem 3.2: if the prime-power factors of `n = 3^2 * 23` share a common residue modulo `29`, then that residue acts as a `29`-multiplier on the contracted coefficients.

Here `3^4 ≡ 23 (mod 29)` and `23^1 ≡ 23 (mod 29)`, so `t = 23` is the common residue. Since `23` has order `7` modulo `29`, the nonzero residues of `Z/29Z` split into four `23`-orbits of size `7`, plus the fixed residue `0`. Thus the contracted vector must have the shape
`(x_0; a,a,a,a,a,a,a; b,...,b; c,...,c; d,...,d)`
across `0` and the four nonzero orbits.

This immediately yields

- `x_0 + 7(a+b+c+d) = 230`
- `x_0^2 + 7(a^2+b^2+c^2+d^2) = 2024`

Reducing these modulo `7` forces `x_0 ≡ 6 (mod 7)` and `x_0^2 ≡ 1 (mod 7)`, hence `x_0 ≡ 6 (mod 7)` as expected. A Cauchy bound on the four orbit values then gives `x_0 <= 20`, so only `x_0 ∈ {6,13,20}` can occur. This is already a very small search surface.

## approach_B
Construction / extremal contradiction route: treat the `29`-quotient as a five-variable exact autocorrelation problem.

Once the `23`-orbit symmetry is imposed, each nonzero shift in `Z/29Z` lies in one of the same four `23`-orbits. Therefore the exact equations
`sum_j b_j b_{j-s} = 1817` for `s != 0`
collapse to four orbit-level correlation equations in the five unknowns `x_0,a,b,c,d`.

This means the full cyclic existence question can be attacked by a bounded exact elimination:

1. enumerate the small list of integer quintuples compatible with the sum and square-sum equations,
2. test the four nontrivial contracted correlation equations,
3. conclude impossibility if no orbit-constant `29`-contraction exists.

This is still reasoning-first because the finite search only begins after the multiplier reduction and the `x_0 ∈ {6,13,20}` squeeze have been proved on paper.

## lemma_graph
`L1.` For a cyclic `(2291,230,23)` difference set, every quotient contraction to order `w` satisfies the exact sum / square-sum / nonzero-correlation identities.

`L2.` For `w = 29`, the common residue `23` coming from `3^4 ≡ 23` and `23^1 ≡ 23 (mod 29)` makes multiplication by `23` a valid quotient multiplier.

`L3.` The `23`-action on `Z/29Z^×` has four orbits of size `7`, so the mod-`29` contraction is determined by `x_0,a,b,c,d`.

`L4.` The sum and square-sum identities imply `x_0 ∈ {6,13,20}`.

`L5.` If no such quintuple satisfies all contracted correlation equations, then no cyclic `(2291,230,23)` difference set exists.

## chosen_plan
Use `L1-L4` to reduce the problem to a bounded exact quotient calculation at `w = 29`. If the orbit-constant contracted systems are empty, that gives a genuine theorem candidate:

`There is no cyclic (2291,230,23)-difference set.`

If the `29`-lane unexpectedly survives, stop and record the surviving profiles rather than drifting to a different campaign. The next bounded lane would then be the `79`-quotient, but only after preserving the `29` output.

## self_checks
`SC1.` Parameter sanity: `230 * 229 = 23 * 2290`, so the basic difference-set count is consistent.

`SC2.` The contraction identities at `w = 29` and `w = 79` are exact and use only the definition of a difference set.

`SC3.` The load-bearing multiplier step is now full-group: `23` is used as a `2291`-multiplier, then the standard translation normalization with `gcd(23-1,2291) = 1` is invoked to replace `D` by an equivalent `23`-invariant difference set.

`SC4.` A bounded exact check of the five-variable mod-`29` orbit-constant system found exactly four ordered solutions, all cyclic reorderings of the same profile `(13,4,7,10,10)`.

`SC5.` The surviving mod-`29` profile forces `0 ∈ D`, forces all four size-`7` orbits on the `79`-torsion line to be selected, and hence forces the mod-`79` zero fiber to equal `29`.

`SC6.` Once the mod-`79` zero fiber is `29`, the mod-`79` second moment is impossible because the remaining `78` coefficients still sum to `201`, so the total square sum is at least `29^2 + 201 = 1042 > 874`.

## code_used
Yes, minimally.

A short inline `python3` checker was used for exactly one bounded task: enumerate all integer quintuples `(x_0,a,b,c,d)` compatible with the `23`-orbit-constant mod-`29` contraction equations

- `x_0 + 7(a+b+c+d) = 230`
- `x_0^2 + 7(a^2+b^2+c^2+d^2) = 2024`
- the four orbit-level nonzero-correlation equations `sum_j b_j b_{j-s} = 1817`

The checker returned exactly the four ordered solutions

- `(13,4,10,10,7)`
- `(13,7,4,10,10)`
- `(13,10,7,4,10)`
- `(13,10,10,7,4)`

so, up to cyclic relabeling of the four nonzero `23`-orbits of `Z/29Z`, the unique surviving profile is `(13;4,7,10,10)`.

## result
Strong theorem candidate:

`The cyclic group C_2291 admits no (2291,230,23)-difference set.`

Argument skeleton:

1. Because `3^1040 ≡ 23 (mod 2291)` and `23^1 ≡ 23 (mod 2291)`, the prime-power factors of `n = 3^2 * 23` share the residue `23` modulo `2291`. Under the Baumert-Gordon multiplier theorem, `23` is therefore a numerical multiplier for any cyclic `(2291,230,23)` difference set.
2. Since `gcd(23-1,2291) = gcd(22,2291) = 1`, translate the putative difference set so that it is actually invariant under multiplication by `23`.
3. Reduce this `23`-invariant set modulo `29`. The nonzero residues split into four size-`7` orbits, so the contracted vector has the form `(x_0;a,b,c,d)` on those orbit blocks.
4. The exact mod-`29` contraction equations leave only the profile `(13;4,7,10,10)` up to cyclic relabeling.
5. Interpret that profile using the full `23`-orbit decomposition in `Z/2291Z ≅ Z/29Z × Z/79Z`:
   - `x_0 = 13` implies the mod-`29` zero fiber consists of `0` plus exactly four selected size-`3` orbits on the `29`-torsion line;
   - each nonzero orbit value is `1 (mod 3)`, so each of the four size-`7` orbits on the `79`-torsion line must also be selected.
6. Therefore the mod-`79` zero fiber has size
   `y_0 = 1 + 4 * 7 = 29`.
7. But for the mod-`79` contraction we must have
   `sum_j y_j = 230`
   and
   `sum_j y_j^2 = 207 + 23 * 29 = 874`.
   Since `y_0 = 29`, the remaining `78` coefficients sum to `201`, so their squared sum is at least `201`. Hence
   `sum_j y_j^2 >= 29^2 + 201 = 1042`,
   contradiction.

So the invariant-set assumption, and hence the original cyclic difference set, cannot exist.

## family_affinity
High. The contradiction is exactly of the residual-row type suggested by Baumert-Gordon: one multiplier, one small quotient elimination, and one complementary quotient moment clash.

## generalization_signal
Moderate positive signal. What scales is the template
`full multiplier -> normalize to invariance -> solve one quotient orbit system -> push the forced residue pattern into the complementary quotient`.
What does not obviously scale is the very sharp final contradiction `29^2 + 201 > 874`, which is specific to this tuple's small `n`.

## proof_template_reuse
Reusable template:

1. choose a divisor `w | v`,
2. first check whether the same residue gives a multiplier on the full cyclic group,
3. normalize by translation to a genuinely invariant set when `gcd(t-1,v)=1`,
4. compress one quotient by multiplier orbits,
5. solve the exact contracted system,
6. reinterpret the surviving pattern in a second quotient to force a moment contradiction.

## candidate_theorem_slice
Concrete theorem slice now visible:

`If a 23-invariant subset D ⊂ Z/2291Z has the contracted data of a cyclic (2291,230,23) difference set, then its mod-29 contraction is uniquely forced to be (13;4,7,10,10) up to orbit relabeling, and this in turn forces the mod-79 zero fiber to be 29, impossible.`

## smallest_param_shift_to_test
If this proof needs repair, the two most useful bounded shifts are:

1. re-run the same multiplier-normalization lane for another Baumert-Gordon squarefree row where one quotient has orbit size `7` and the complementary quotient has a very small second moment;
2. on this same tuple, verify whether the mod-`79` contradiction can be derived without the finite mod-`29` search, which would make the note cleaner.

## why_this_is_or_is_not_publishable
If the multiplier theorem and translation normalization check out exactly as used, then the title theorem is:

`The cyclic group C_2291 admits no (2291,230,23)-difference set.`

This would already be about `80-85%` of a short micro-paper. Minimal remaining packaging:

- cite the exact Baumert-Gordon multiplier statement used,
- present the five-variable mod-`29` elimination cleanly, preferably as a tiny table or appendix certificate,
- add one paragraph locating the row inside Table 3 and one paragraph stating the complementary-quotient contradiction.

This is no longer too thin for the micro-paper lane if verification passes; right now it is a strong candidate rather than a finished packet.

## paper_shape_support
If the main claim closes, the smallest paper-shaping support is already visible:

- one multiplier-normalization lemma for `t = 23`,
- one exact mod-`29` elimination lemma producing the unique profile `(13;4,7,10,10)`,
- one final mod-`79` second-moment contradiction.

The immediate corollary / remark is:

`Any proof of nonexistence for this tuple can be organized entirely inside the multiplier-contraction framework already present in Baumert-Gordon, without invoking heavy search or generic optimization.`

## boundary_remark
The part that scales is the multiplier-orbit compression and cross-quotient bookkeeping. The part that does not obviously scale is the last numerical inequality after `y_0 = 29`, which is highly instance-specific. So the current package is closer to a paper-shaped exact row than to a broad family theorem.

## likely_failure_points
The load-bearing points are:

1. The exact source hypothesis-to-conclusion form that makes `23` a full `2291`-multiplier from the residue condition on `n = 3^2 * 23`.
2. The standard translation-normalization step turning `23D = D + s` into literal `23D = D` using `gcd(22,2291) = 1`.
3. The bounded finite elimination certificate for the mod-`29` orbit-constant system.

If point `1` only gives a quotient multiplier and not a full-group multiplier, the current cross-quotient contradiction would need to be weakened back to a slice result.

## what_verify_should_check
Verify should check:

1. the full-group arithmetic `3^1040 ≡ 23 (mod 2291)` and `ord_2291(23) = 21`,
2. the exact source statement ensuring that this common residue makes `23` a valid multiplier for the cyclic difference set,
3. the translation-normalization step from `23D = D + s` to an equivalent `23`-invariant set,
4. the contraction identities at `w = 29` and `w = 79`,
5. the finite elimination result that the only mod-`29` orbit-constant contracted profile is `(13;4,7,10,10)` up to orbit relabeling,
6. the orbit bookkeeping turning that profile into the mod-`79` zero-fiber value `29`,
7. the final square-sum contradiction `29^2 + 201 > 874`.

## verify_rediscovery
Bounded PASS 1 audit did not establish rediscovery.

- The canonical source still lists `(2291,230,23)` as a surviving cyclic row in the Baumert-Gordon table of possible cases.
- A bounded exact-tuple and alternate-notation web sweep did not surface a later paper, note, repository entry, theorem, proposition, example, or corollary explicitly settling this exact cyclic instance.
- I also checked the same source surface for an internal already-published discharge of this row and did not find one.

Verdict for PASS 1: no rediscovery found within budget, so the run cannot be downgraded to `REDISCOVERY` on the present evidence.

## verify_faithfulness
The solve artifact is faithful to the intended statement.

- The intended statement is the exact existence question for a cyclic `(2291,230,23)` difference set, and the solve artifact addresses that exact question by a nonexistence proof.
- There is no quantifier drift, family drift, or replacement by a weaker proxy claim.
- The source use is faithful at the load-bearing multiplier step: Baumert-Gordon Theorem `3.2` is being used with `w = v = 2291`, so the conclusion is a full-group multiplier statement rather than only a quotient multiplier statement.
- The normalization step from `23D = D + s` to an equivalent literal `23`-invariant translate is valid because for `D' = D + a` one has `23D' = D' + s + 22a`, and `22` is invertible modulo `2291`.

Conservative classification outcome from PASS 2: the claimed theorem slice matches the intended statement, but absent Lean this must remain below `EXACT`.

## verify_proof
No incorrect step was found in the current argument.

Checks:

1. The multiplier arithmetic checks out: `3^1040 ≡ 23 (mod 2291)`, `23^1 ≡ 23 (mod 2291)`, and `ord_2291(23) = 21`.
2. The mod-`29` orbit reduction is correct: multiplication by `23` has one fixed residue and four nonzero orbits of size `7`.
3. The contracted identities at `w = 29` give
   - `x_0 + 7(a+b+c+d) = 230`
   - `x_0^2 + 7(a^2+b^2+c^2+d^2) = 2024`
   - nonzero-shift correlation `1817`
4. Independent re-enumeration of the exact orbit-constant mod-`29` system again produced exactly four ordered solutions, all cyclic reorderings of `(13,4,7,10,10)`.
5. The transfer from the mod-`29` profile to the mod-`79` zero fiber is correct once the full `23`-orbit types in `Z/2291Z` are stated explicitly:
   - one fixed orbit `{0}`,
   - twenty-six size-`3` orbits in the mod-`29` zero fiber,
   - four size-`7` orbits in the mod-`79` zero fiber,
   - one hundred four generic size-`21` orbits.
6. Because a generic size-`21` orbit contributes `3` points to each residue in a nonzero mod-`29` orbit, while a size-`7` orbit in the mod-`79` zero fiber contributes `1`, each nonzero mod-`29` orbit value is congruent mod `3` to the indicator of the corresponding size-`7` orbit. Since `(4,7,10,10) ≡ (1,1,1,1) (mod 3)`, all four such size-`7` orbits must be present.
7. Likewise `x_0 = 13 = 1 + 4·3` means the mod-`29` zero fiber consists of `0` plus four size-`3` orbits.
8. Therefore the mod-`79` zero fiber has size `y_0 = 1 + 4·7 = 29`. The mod-`79` square-sum identity requires total square sum `207 + 23·29 = 874`, but the remaining `78` coefficients still sum to `201`, so the square sum is at least `29^2 + 201 = 1042`, contradiction.

The only issue I found is wording ambiguity, not a mathematical defect: the phrases “29-torsion line” and “79-torsion line” are easy to misread in the current prose. The bookkeeping itself is correct.

## verify_adversarial
Adversarial reruns supported the disproof.

- Recomputed the arithmetic checks used in the solve artifact: `3^1040 ≡ 23 (mod 2291)`, `ord_2291(23) = 21`, `ord_29(23) = 7`, and `ord_79(23) = 3`.
- Re-ran the bounded exact mod-`29` enumeration from scratch and recovered exactly the four ordered solutions claimed in the record.
- Recomputed the full `23`-orbit decomposition on `Z/2291Z`; the orbit census is exactly:
  - `1` orbit of size `1`,
  - `26` orbits of size `3` in the mod-`29` zero fiber,
  - `4` orbits of size `7` in the mod-`79` zero fiber,
  - `104` orbits of size `21` off both zero fibers.
- Tried to break the cross-quotient step by checking whether generic size-`21` orbits could alter the mod `3` residue class of a nonzero mod-`29` orbit value. They cannot: they contribute in multiples of `3` per residue, so the congruence argument survives intact.

PASS 4 outcome: the finite certificate and the orbit-transfer argument both survived adversarial rechecking.

## publication_prior_art_audit
Bounded audit date: `2026-04-15`.

- Exact-statement search: direct exact-tuple searches for `(2291,230,23)` plus `difference set` did not surface a later paper, note, preprint, theorem page, repository entry, proposition, example, or corollary settling this exact cyclic row.
- Alternate-notation search: bounded searches using spaced tuple notation, `C_2291`, and the order parameter `n = 207` likewise produced no relevant later settlement beyond the Baumert-Gordon source surface.
- Canonical source check: Baumert-Gordon 2004 Table 3 explicitly lists `(2291,230,23)` among the possible cyclic cases with `150 <= k <= 300` and `gcd(v,n) = 1`. Section `3.2` gives the contracted-multiplier tool used here, but the paper does not itself discharge this row. Table `4` lists cases eliminated there and does not include `2291,230,23`.
- Internal theorem / proposition / example / corollary / observation / sufficient-condition check inside the canonical source: none of the explicitly stated eliminations in the paper settle this tuple; the tuple remains a survivor rather than a hidden already-resolved example.
- Outside-source status pass: Gordon's public Difference Sets repository describes itself as an attempt to include all known difference sets and nonexistence results for `v < 100000`, with an explicit `open` status surface. A bounded status search across that surface and the general web did not produce a conflicting existing record or a later direct settlement for this tuple.
- Recent follow-up spot-check: Gordon's 2022 paper on small `lambda` points readers to the live repository and reports further eliminations in related parameter ranges, but it does not report a settlement of `(2291,230,23)`.

Audit verdict: within the required bounded prior-art budget, I did not find rediscovery evidence. This supports treating the packet as frontier-novel at bounded-search confidence, not as a fully survey-complete novelty claim.

## publication_statement_faithfulness
The packet is faithful to the intended statement.

- The strongest claim is still the exact intended existence question for cyclic `(2291,230,23)`, answered by a nonexistence theorem.
- There is no family drift, proxy drift, or downgrade to a weaker quotient-only statement.
- The source use remains faithful: Theorem `3.2` is used as a multiplier theorem, and Theorem `3.1` supplies the contracted equations at `w = 29` and `w = 79`.
- The proof packet stays on the exact one-shot lane: full multiplier, exact quotient elimination, then complementary-quotient contradiction.

## publication_theorem_worthiness
This is materially stronger than “here is an example.”

- The strongest honest claim is a genuine theorem: `The cyclic group C_2291 admits no (2291,230,23)-difference set.`
- There is a real title theorem, not merely a worked instance or supportive lemma.
- The proof is structural in method even though the scope is instance-locked: multiplier normalization, orbit-compressed contraction, and a forced second-moment contradiction.
- The packet would survive a referee asking “what is the theorem?” because the answer is immediate and exact.
- The finite mod-`29` elimination is a bounded certificate, not a hand-picked menagerie of small cases. It is still instance-specific, but not in a way that collapses the result into “just an example.”
- The honest limitation is scope, not theoremhood: this is a single residual row, not a family theorem.

## publication_publishability
If the current verified argument is correct in the bounded sense already established, then this is most of a publishable micro-note.

- Estimated single-solve-to-paper fraction: about `0.89`.
- The paper core is already present: one exact residual-case theorem anchored to Baumert-Gordon Table `3`, one compact multiplier lemma, one short elimination certificate, and one final contradiction.
- The remaining gap is editorial rather than mathematical:
  - write the mod-`29` elimination certificate in appendix-grade form,
  - phrase the orbit bookkeeping cleanly,
  - cite the source row and bounded no-rediscovery audit carefully.
- This is not a feeder ladder target and should not be expanded into a broader theorem program before archiving the exact-row result.

Publication verdict: `PAPER_READY`.

## publication_packet_audit
Packet judgment: human-ready.

- The theorem statement is clear and title-sized.
- The proof artifacts are preserved well enough to support a short note.
- The family anchor is real: this closes one named Baumert-Gordon survivor rather than reporting an isolated curiosity with no literature foothold.
- The bounded literature positioning is good enough for a conservative human-ready packet.
- Lean would not be the reason the packet becomes publishable; it is optional later sealing and archival polish.

## micro_paper_audit
This passes the strict micro-paper lane after audit.

- Stronger than example-only: yes.
- Most of a publishable note already present: yes.
- Real theorem slice: yes, an exact nonexistence theorem for one named cyclic survivor.
- Structural versus instance-only: structural method, instance-locked conclusion.
- Too dependent on hand-picked small cases: no, though one bounded finite certificate remains load-bearing.
- Remaining gap if not paper-ready: not applicable; the remaining work is writeup polish, not theorem growth.

Assessment: the candidate looked only marginally lane-eligible before solve, but after verification and bounded prior-art checking it now clears the micro-paper bar comfortably.

## strongest_honest_claim
Within the bounded prior-art audit completed on `2026-04-15`, the cyclic group `C_2291` admits no `(2291,230,23)`-difference set. The proof packet uses a full `23`-multiplier, translation normalization, a unique orbit-compressed mod-`29` contraction profile, and the forced mod-`79` second-moment contradiction. No earlier direct settlement of this exact row surfaced in the bounded audit.

## paper_title_hint
No cyclic `(2291,230,23)`-difference set exists

## next_action
Treat this packet as `HUMAN_READY`: move it off the main discovery queue, preserve the compact mod-`29` elimination certificate as appendix-grade evidence, and place it on the non-blocking Lean queue for optional later formal sealing rather than expanding the theorem scope.

## verify_theorem_worthiness
Assessment:

- Exactness: yes, the visible theorem is the exact nonexistence statement for the named cyclic row.
- Novelty: bounded audit did not expose rediscovery, but novelty is still only bounded-audit confidence until publication audit finishes.
- Reproducibility: strong. The proof reduces to source-cited multiplier facts, two exact contraction identities, a tiny finite mod-`29` certificate, and one explicit complementary-quotient contradiction.
- Lean readiness: yes in principle. The theorem slice is rigid enough to formalize.
- Lean packet seal: no. Lean is not the shortest remaining path to a sealed packet; the shorter next step is publication audit plus a clean preserved certificate for the mod-`29` elimination.
- Paper leverage: real. If correct and Lean-sealed, this already looks like most of a short residual-case note rather than a mere isolated computational curiosity.

Explicit answers:

- Would this result, if correct and Lean-sealed, already constitute most of a publishable note? Yes.
- What percentage of the paper would one solve already provide? About `80-85%`.
- What title theorem is actually visible? `The cyclic group C_2291 admits no (2291,230,23)-difference set.`
- What part of the argument scales? The multiplier -> normalize -> quotient-orbit compression -> complementary quotient transfer template.
- What part clearly does not? The final second-moment contradiction and the specific surviving profile `(13;4,7,10,10)` are highly tuple-specific.
- Is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? No. The best honest status at verify is `SLICE_CANDIDATE`.

So the verified theorem slice is stronger than `INSTANCE_ONLY`, but it is not yet a publication-complete packet and should not be promoted beyond `SLICE_CANDIDATE` before publication audit.

## verify_verdict
`VERIFIED`

The current record supports the conservative verify-stage conclusion:

- `verify_verdict = VERIFIED`
- `classification = COUNTEREXAMPLE`
- `publication_status = SLICE_CANDIDATE`

This remains below `EXACT` because Lean has not been completed.

## minimal_repair_if_any
Tiny conservative repair only:

- keep the mathematics unchanged,
- clarify in the writeup that the size-`3` orbits lie in the mod-`29` zero fiber and the size-`7` orbits lie in the mod-`79` zero fiber,
- preserve the mod-`29` elimination output as an explicit compact certificate so publication audit does not have to trust prose alone.
