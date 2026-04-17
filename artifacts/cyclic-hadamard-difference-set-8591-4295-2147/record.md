# Solve Record: Does the cyclic group C_8591 admit a (8591,4295,2147)-difference set?

- slug: `cyclic-hadamard-difference-set-8591-4295-2147`
- working_packet: `artifacts/cyclic-hadamard-difference-set-8591-4295-2147/working_packet.md`

## statement_lock
Determine whether the cyclic group `C_8591` admits a `(8591,4295,2147)`-difference set.

The exact title theorem, if the row closes, would be:
`The cyclic group C_8591 does not admit a (8591,4295,2147)-difference set.`
or
`The cyclic group C_8591 admits a (8591,4295,2147)-difference set.`

Because this tuple is already a named residual cyclic Hadamard survivor, a successful exact solve would still be about `70-90%` of a paper; the minimal remaining packaging work would be a short literature-placement paragraph, a clean writeup of the decisive arithmetic obstruction or construction, and one compact remark situating `8591` among the surviving sub-`10000` cases.

## definitions
Work additively in `G = C_8591`.

A `(v,k,lambda)`-difference set is a subset `D ⊂ G` with `|D| = k` such that every nonzero `g in G` has exactly `lambda` representations as `d1 - d2` with `d1,d2 in D`.

Here
- `v = 8591 = 11^2 * 71`,
- `k = 4295`,
- `lambda = 2147`,
- `n = k - lambda = 2148 = 2^2 * 3 * 179`.

For every nonprincipal character `chi` of `G`,
`|chi(D)|^2 = n = 2148`.

Ambiguities and conventions to keep explicit:
- existence is up to translation and inversion in the cyclic group;
- the current solve lane is non-Lean, so the strongest positive classification here can only be `CANDIDATE`;
- any multiplier input not already explicit in the active packet must be treated conservatively and flagged for `verify`.

## approach_A
Structural / invariant route.

Exploit quotient contraction and a contracted multiplier on a small quotient. The natural first quotient is `G/H ≅ C_11` where `|H| = 781`. If the repo-quoted Baumert-Gordon Theorem `3.2` is available in the needed form, then `t = 3` is a valid `11`-multiplier because
- `2^8 ≡ 3 (mod 11)`,
- `3 ≡ 3 (mod 11)`,
- `179 ≡ 3 (mod 11)`.

Since `gcd(3 - 1, 11) = 1`, a translate may be normalized so that the contracted `C_11` coefficient vector is `3`-invariant. Multiplication by `3` on `C_11^×` has two nonzero orbits of size `5`, so the quotient profile collapses to three integers:
- `a` on `0`,
- `b` on one `3`-orbit of nonzero residues,
- `c` on the other `3`-orbit.

The first-moment and second-moment equations on the quotient then become a three-variable diophantine system with a realistic chance of complete hand solution.

Self-check after approach setup:
- this route is mathematically sharp and very cheap if the `11`-multiplier is legitimate;
- the load-bearing risk is not downstream arithmetic but the exact theorem statement licensing the contracted multiplier.

## approach_B
Construction / extremal / contradiction route.

Ignore multipliers initially and compress to a quotient such as `C_121` or `C_71`. If `x_i` are the `71`-fiber counts on `C_121`, then
- `sum x_i = 4295`,
- `sum x_i^2 = 2148 + 71 * 2147 = 154585`,
- `sum x_i x_{i+s} = 71 * 2147 = 152437` for all nonzero `s`.

After centering with `z_i = 2x_i - 71`, this becomes a periodic autocorrelation system
- `sum z_i = -1`,
- `sum z_i^2 = 8521`,
- `sum z_i z_{i+s} = -71` for every nonzero `s`.

This route does not need a multiplier at the start and is honest as a fallback structural corridor. But by itself it still leaves a large search / lifting space. It looks better as a consistency check or as a second strike after a quotient-multiplier collapse has already reduced the profile.

Self-check after approach setup:
- this route uses only unconditional quotient equations;
- it is theorem-facing but not obviously decisive on its own for `8591`.

## lemma_graph
1. Contract a hypothetical difference set from `C_8591` to the quotient `C_11`.
2. Use the repo-quoted contracted multiplier theorem at `w = 11` with `t = 3`.
3. Normalize by translation to make the contracted vector `3`-invariant on `C_11`.
4. Replace the `11` coordinates by the three orbit variables `(a,b,c)`.
5. Solve the exact first-moment and second-moment equations.
6. If this gives a contradiction, close the row.
7. If not, extract the sharpest exact `C_11` theorem slice and test whether it is compatible with independent `71`- or `121`-quotient constraints.

## chosen_plan
Best path: push the `w = 11` quotient first.

Reason:
- it matches the packet's arithmetic hint that the decisive structure should come from quotient data tied to the factorization `8591 = 11^2 * 71` and `n = 2^2 * 3 * 179`;
- the nonzero `3`-orbits on `C_11` are only of size `5`, so the quotient profile is rigid enough to solve exactly by hand;
- even if the argument does not yet close the full theorem, it should at least produce a small exact theorem slice with real publication relevance.

Immediate goal of the chosen plan:
- classify the only possible `C_11` quotient count patterns of any hypothetical cyclic `(8591,4295,2147)` difference set.

## self_checks
- Statement lock check: the intended theorem remains the exact cyclic row `(8591,4295,2147)`, not a broader family claim.
- Scope check: no SAT / ILP / brute force has been introduced.
- Multiplier check: the decisive `w = 11` step currently relies on a theorem statement imported from a previously verified local artifact, not from a freshly reloaded source file in this run.
- Arithmetic check before solving the orbit system: the quotient totals are consistent with `sum c_i = 4295` and `sum c_i^2 = 2148 + 781 * 2147 = 1678955`.
- Bounded experiment check: a tiny exact residue-intersection script confirmed that the same contracted-multiplier congruence lane is nontrivial for `w = 71`, `121`, and even `8591`; so the current bottleneck is orbit complexity, not absence of a second multiplier.

## code_used
Minimal code used after the reasoning artifact was written.

One tiny `python3` arithmetic script was used only to intersect the power-residue sets of the prime divisors of `n = 2148` modulo `11`, `71`, `121`, and `8591`.

Outputs used:
- for `w = 11`, common nontrivial residues include `3,4,5,9`;
- for `w = 71`, common nontrivial residues include `20,30,32,37,45,48`, all of order `7`;
- for `w = 121`, common nontrivial residues include `3,9,27,81`, all of order `5`;
- for `w = 8591`, common nontrivial residues include `243,1937,5930,6293,6777,7503`, and each satisfies `gcd(t - 1, 8591) = 121`.

This confirms there is a genuine follow-up quotient lane at `71` and `121`, but no immediately normalizable full-group multiplier with `gcd(t - 1, 8591) = 1` surfaced in this pass.

## result
Using the `C_11` quotient and the `3`-orbit collapse, the contracted profile is forced into a two-pattern corridor.

Let the `C_11` quotient counts be `(a;b^5;c^5)` after `3`-invariant normalization. Then
- `a + 5b + 5c = 4295`,
- `a^2 + 5b^2 + 5c^2 = 1678955`.

Write `s = b + c = 781 + m`, `d = b - c`, and hence `a = 390 - 5m`. The moment equations reduce to
`11m^2 + 2m + d^2 = 781`.

Since `11m^2 <= 781`, one has `|m| <= 8`. Direct hand checking gives only two square hits:
- `m = 3`, `d = ±26`,
- `m = -7`, `d = ±16`.

Therefore the only admissible `C_11` quotient profiles are
- `(375;405^5;379^5)`, or
- `(425;395^5;379^5)`,
up to swapping the two nonzero `3`-orbits.

Equivalent order-`11` character values are therefore forced to one of the two conjugate pairs
- `-17 ± 13 sqrt(-11)`,
- `38 ± 8 sqrt(-11)`,
whose norms are both `2148`.

This is the strongest exact theorem slice I could close in the current pass. It is structural and sharp, but it does not yet determine existence or nonexistence of the full row.

Follow-up arithmetic from the bounded residue check:
- the same contracted-multiplier congruence mechanism also offers nontrivial residues on `C_71` and `C_121`, so a second quotient attack is genuinely available;
- on the full group `C_8591`, the common residues found all satisfy `t ≡ 1 (mod 121)`, equivalently `gcd(t - 1, 8591) = 121`, so they do not immediately give literal invariance on the whole group.

Self-check after the main derivation:
- the orbit arithmetic is exact and reproducible by hand;
- the only unresolved load-bearing issue is whether the `w = 11`, `t = 3` contracted multiplier normalization is fully licensed by the intended Baumert-Gordon theorem in exactly the form used here;
- even granting that step, the current output is still only a quotient-classification slice, not a contradiction;
- the residue experiment reduces one uncertainty: the next obstruction attempt should focus on the `71`-quotient, not on trying to force a full-group multiplier normalization.

## family_affinity
High affinity with the cyclic Hadamard survivor lane where a prime-power quotient and a small contracted multiplier force the surviving character values into a tiny algebraic corridor.

More specifically, this sits in the `v = 11^2 * q` subfamily with odd Hadamard parameters and a prime-power quotient `C_11` on which a nontrivial multiplier has exactly two nonzero orbits.

## generalization_signal
Moderate.

What looks reusable:
- contracting to a prime quotient `C_p`,
- normalizing by a valid `w`-multiplier,
- solving the three-variable orbit system exactly,
- translating the resulting profile into explicit algebraic character values.

What does not yet obviously scale:
- lifting that rigid prime-quotient corridor to a full contradiction in the ambient cyclic group.

## proof_template_reuse
Reusable template:
1. pick a prime quotient `w | v`;
2. find a genuine contracted multiplier `t` on `C_w`;
3. normalize to `t`-invariance;
4. collapse the quotient profile to multiplier orbits;
5. solve the moment equations exactly;
6. convert the profile into forced algebraic character values;
7. only then try to lift to another quotient or to a contradiction in the full group.

## candidate_theorem_slice
Assuming the `w = 11`, `t = 3` contracted multiplier normalization, any cyclic `(8591,4295,2147)` difference set has `C_11` quotient profile
`(375;405^5;379^5)` or `(425;395^5;379^5)`, up to swapping the two nonzero `3`-orbits.

## smallest_param_shift_to_test
The first useful shift is not a nearby `v`; it is the next quotient level for the same row.

Most useful next tests:
- use the now-confirmed nontrivial multiplier residues on `w = 71` or `w = 121` to derive the next quotient orbit system;
- intersect that second quotient pattern with the forced `C_11` corridor above;
- if not, test whether the two explicit order-`11` character values are compatible with the unconditional `C_71` or `C_121` compressed autocorrelation equations.

## why_this_is_or_is_not_publishable
This is not yet publishable in the micro-paper lane.

Why not:
- it does not settle existence or nonexistence;
- the current strongest claim is a quotient-profile theorem slice rather than the title theorem;
- one load-bearing multiplier statement still needs exact source reloading in `verify`.

If the main claim closed from here, the row would immediately become paper-shaped. Right now, though, the current package is still too thin for the micro-paper objective.

## paper_shape_support
If the full row closes, the paper shape is already obvious:
- title theorem: `On the cyclic Hadamard difference-set case (8591,4295,2147)`;
- solve-to-paper fraction: still about `0.84`;
- minimal remaining packaging: one concise source paragraph, the decisive arithmetic argument, and one short remark comparing `8591` with the other surviving cyclic Hadamard rows.

The current slice supports that eventual paper because it narrows any hypothetical solution to exactly two order-`11` character patterns. But it is not itself enough to carry the note.

## boundary_remark
The mod-`11` corridor is unexpectedly rigid but still instance-level.

Natural boundary remark:
- any hypothetical solution must already look very non-generic at order `11`, with the zero residue class count forced to either `375` or `425`;
- the remaining freedom is only the second quotient direction, not the order-`11` behavior.

One immediate corollary-like remark that falls out:
- every order-`11` character of a hypothetical difference set has value in the two-element set
  `{ -17 ± 13 sqrt(-11), 38 ± 8 sqrt(-11) }`
  up to conjugation.

## likely_failure_points
- The load-bearing risk is theorem scope: `verify` must confirm the exact contracted multiplier statement and its hypotheses at `w = 11`, `t = 3`.
- Even if that step is valid, the current slice may simply be compatible with actual solutions; no contradiction has yet emerged.
- A second quotient is definitely available, but the `71`- and `121`-orbit systems are much larger than the `11`-system and may not collapse without a second structural idea.
- The full-group common residues found in the bounded experiment all have `gcd(t - 1, 8591) = 121`, so they do not supply the simple whole-group translation-killing step that would make the proof immediate.

## what_verify_should_check
1. Reload the exact Baumert-Gordon Theorem `3.2` statement and verify that `t = 3` is a legitimate `11`-multiplier here from the prime divisors of `n = 2148`.
2. Check the translation-normalization step on `C_11`: because `gcd(3 - 1, 11) = 1`, the contracted vector should indeed be translatable to literal `3`-invariance.
3. Recompute the orbit structure of multiplication by `3` on `C_11^×`, namely two orbits of size `5`.
4. Recompute the diophantine reduction `11m^2 + 2m + d^2 = 781` and confirm that the only integer solutions are `(m,d) = (3,±26), (-7,±16)`.
5. Confirm the derived order-`11` character values `-17 ± 13 sqrt(-11)` and `38 ± 8 sqrt(-11)` and their norm `2148`.
6. Recompute the bounded residue-intersection outputs on `w = 71`, `121`, and `8591`, especially the facts that nontrivial common residues exist on both proper quotients and that every common full-group residue found in this pass satisfies `gcd(t - 1, 8591) = 121`.

## verify_rediscovery
PASS 1 used a bounded web audit only.

Search surface covered within budget:
- exact tuple search on `(8591,4295,2147)` and cyclic-Hadamard phrasing;
- alternate notation search on `C_8591` and `v = 8591`;
- the canonical Baumert-Gordon 2004 source;
- theorem / proposition / example checks around the same source surface;
- one recent-status pass aimed at 2019 and later repository / slide updates.

Outcome:
- Baumert-Gordon 2004 still lists `(8591,4295,2147)` among the open cyclic Hadamard cases up to `v = 10000`;
- the surfaced later status material used in the packet still repeats `8591` among the unresolved small cyclic Hadamard cases;
- within the bounded search budget, no later paper, note, repository entry, theorem, proposition, example, or observation was found that settles this exact cyclic row or directly implies its resolution.

Conclusion:
- rediscovery was not established within budget;
- `verify_verdict` is therefore not `REDISCOVERY`.

## verify_faithfulness
The selected problem asks for the exact existence question:
`Does the cyclic group C_8591 admit a (8591,4295,2147)-difference set?`

The current solve artifact does not answer that exact question. After checking the writeup closely, the strongest honest local claim is narrower:
- any hypothetical cyclic `(8591,4295,2147)` difference set has one of two forced `C_11` quotient profiles, equivalently one of two forced order-`11` character-value pairs.

So the artifact is faithful to a real theorem slice, but not to the intended title theorem. There is no quantifier drift inside the slice itself; the mismatch is that the solve stopped at a necessary-condition theorem and did not complete the existence / nonexistence decision for the full row.

Faithfulness conclusion:
- intended statement: not solved;
- strongest honest claim: a nearby exact structural slice;
- classification consequence: `VARIANT`, not a verified solve of the selected problem.

## verify_proof
I checked the load-bearing steps.

1. Multiplier premise:
   Baumert-Gordon Theorem `3.2` licenses `t = 3` as an `11`-multiplier here, because for each prime divisor of `n = 2148 = 2^2 * 3 * 179`, some power is congruent to `3 mod 11`:
   - `2^8 ≡ 3 mod 11`
   - `3^1 ≡ 3 mod 11`
   - `179 ≡ 3 mod 11`

2. Translation normalization:
   If the contracted polynomial satisfies `theta(x^t) ≡ x^s theta(x) mod (x^11 - 1)`, then translating by `x^h` changes the shift to `h(t-1)+s`. Since `gcd(t-1,11) = gcd(2,11) = 1`, one can choose `h` to kill the shift and obtain literal `3`-invariance on `C_11`.

3. Orbit structure:
   Multiplication by `3` on `C_11^×` has exactly two nonzero orbits:
   - `{1,3,9,5,4}`
   - `{2,6,7,10,8}`

4. Moment equations:
   Writing the quotient profile as `(a;b^5;c^5)`, the standard quotient equations give
   - `a + 5b + 5c = 4295`
   - `a^2 + 5b^2 + 5c^2 = 2148 + 781*2147 = 1678955`

   With `s = b+c = 781+m`, `d = b-c`, and `a = 390-5m`, these reduce correctly to
   `11m^2 + 2m + d^2 = 781`.

5. Integer solutions:
   Recomputing the diophantine equation gives exactly
   - `(m,d) = (3,±26)`
   - `(m,d) = (-7,±16)`

   Hence the only quotient profiles are
   - `(375;405^5;379^5)`, or
   - `(425;395^5;379^5)`,
   up to swapping the two nonzero `3`-orbits.

6. Character values:
   These profiles yield the order-`11` character values
   - `-17 ± 13 sqrt(-11)`
   - `38 ± 8 sqrt(-11)`
   and both have norm `2148`.

First incorrect step found:
- none inside the proved slice.

Proof conclusion:
- the local arithmetic argument for the `C_11` quotient slice is correct as written after discharging the multiplier-normalization premise;
- the proof fails only as a proof of the intended statement, because it never reaches a contradiction or construction for the full cyclic row.

## verify_adversarial
No construction witness exists to attack, so the adversarial pass focused on re-running the exact arithmetic support.

Reruns performed:
- checked the `11`-multiplier criterion for `t = 3` against the prime divisors `2,3,179` of `n`;
- recomputed the `x -> 3x` orbits on `C_11`;
- recomputed the diophantine reduction and exhaustively checked its integer solutions;
- recomputed the derived character values and their norms.

Observed outputs:
- multiplier exponents: `2^8`, `3^1`, and `179^1` all hit `3 mod 11`;
- orbit decomposition: `[0]`, `[1,3,9,5,4]`, `[2,6,7,10,8]`;
- only integer hits: `(-7,±16)` and `(3,±26)`;
- resulting profiles: `(425,395,379)` / swap and `(375,405,379)` / swap;
- resulting norms: all equal `2148`.

Adversarial conclusion:
- the computation supports the quotient-slice theorem;
- it does not support the stronger existence / nonexistence claim, because no second quotient obstruction or full contradiction is present.

## verify_theorem_worthiness
Exactness:
- the verified mathematics is an exact necessary-condition slice, not the exact intended theorem.

Novelty:
- bounded prior-art checking did not show that this exact `C_11` slice is already stated in the literature, but novelty confidence remains below the confidence for the full selected row because this is a derived intermediate statement rather than the named open case itself.

Reproducibility:
- high for the slice. The arithmetic is short, exact, and easily rerunnable.

Lean readiness:
- no. Formalizing this slice now would be archival polish on a side theorem, not the shortest path to a sealed publication packet for the selected problem.

Paper leverage:
- limited. The slice is structurally sharp and likely useful, but it is still publication-distant.

Explicit publication answers:
- would this result, if correct and Lean-sealed, already constitute most of a publishable note? No.
- what percentage of the paper would one solve already provide? About `0.35` to `0.40`, not the `0.84` attached to a full resolution of the row.
- what title theorem is actually visible? A necessary-condition theorem forcing the `C_11` quotient profile, equivalently the order-`11` character values, of any hypothetical cyclic `(8591,4295,2147)` difference set.
- what part of the argument scales? The quotient-plus-multiplier orbit collapse on prime quotients, and the conversion of the orbit profile into explicit algebraic character values.
- what part clearly does not? The lift from the rigid `C_11` slice to an actual contradiction or construction in `C_8591`.
- is the best honest publication status still only `INSTANCE_ONLY` or even `NONE`? `NONE` for the current artifact. This slice is too far from a standalone micro-paper packet.

The micro-paper target itself remains strong. What failed here is not the target but the distance still left after the current solve artifact.

## verify_verdict
- `verify_verdict = UNVERIFIED`
- `classification = VARIANT`
- `confidence = high`

Reason:
- bounded PASS 1 did not establish rediscovery;
- the structural `C_11` slice survives skeptical checking;
- the intended theorem is still unproved, so the selected row cannot be treated as verified.

## minimal_repair_if_any
Tiny conservative repair available:
- remove the conditional wording "`Assuming the w = 11, t = 3 contracted multiplier normalization`" when restating the quotient slice, because the multiplier criterion and the translation-normalization step both check out.

No mathematical patch closes the selected problem. The remaining gap is substantive:
- derive an independent `C_71` or `C_121` obstruction from the same row and intersect it with the forced `C_11` corridor, or
- produce an actual construction.

## publication_prior_art_audit
Bounded audit date: `2026-04-15`.

Exact-statement search:
- searches on the exact tuple `(8591,4295,2147)`, on `cyclic Hadamard 8591`, and on `C_8591` surfaced the same core frontier sources and did not surface a later case-specific construction or nonexistence paper.

Alternate-notation search:
- searches using `ideal autocorrelation`, `binary sequence`, and `circulant / cyclic Hadamard` wording also failed to produce a later exact settlement;
- the surfaced Song-lab slide material still treats `8591` as one of the surviving unresolved cyclic Hadamard values rather than as a closed case.

Canonical-source check:
- Baumert-Gordon 2004, Table 5, still lists `(8591,4295,2147)` as `Open`;
- the same paper's Theorem `3.2` is the multiplier theorem supporting the local `w = 11` slice;
- within that source, no theorem / proposition / example / corollary / observation / sufficient-condition entry was found that already settles `8591` beyond the open-table status.

Outside-source status pass:
- Dan Gordon's current difference-set repository page still presents itself as the maintained status surface for abelian difference-set parameters;
- the Zenodo snapshot `La Jolla Difference Sets Repository`, version `v1.2`, was published on `May 16, 2025`;
- Gordon's home page states that on `March 1, 2026` the website databases were frozen and converted to JSON archives;
- within the bounded exact-tuple search, no later repository note or paper was found that resolves the exact cyclic row `(8591,4295,2147)`.

Recent follow-up check:
- not escalated beyond the narrow search, because the canonical table, the repository surface, and the bounded exact / alternate-notation searches all aligned on the same unresolved frontier story.

Prior-art conclusion:
- rediscovery was not established within the bounded audit;
- novelty confidence for the full selected row remains materially better than novelty confidence for the local `C_11` slice, simply because the row itself is a named frontier survivor while the slice is an intermediate theorem that may or may not already be folklore.

## publication_statement_faithfulness
The selected problem asks for the exact existence decision for a cyclic `(8591,4295,2147)` difference set.

The strongest honest audited output is narrower:
- any hypothetical cyclic `(8591,4295,2147)` difference set has `C_11` quotient profile `(375;405^5;379^5)` or `(425;395^5;379^5)`, up to swapping the two nonzero `3`-orbits;
- equivalently, every order-`11` character value is forced to `-17 ± 13 sqrt(-11)` or `38 ± 8 sqrt(-11)`.

Faithfulness verdict:
- faithful as an exact theorem slice;
- not faithful as a resolution of the selected title theorem;
- no quantifier drift or scope drift was found inside the slice itself.

## publication_theorem_worthiness
Answers required by the audit:

- Is the strongest honest claim stronger than "here is an example"? Yes. It is an exact structural necessary-condition theorem, not a worked example.
- Is there a real theorem slice here? Yes. The `C_11` quotient and order-`11` character values are forced into a two-pattern corridor.
- Is the proof structural or merely instance-specific? Structural inside this exact row, but still instance-bound; it does not yet promote to a reusable family theorem with independent value.
- Would this survive a referee asking "what is the theorem?" Partly. There is a crisp theorem statement, but the honest answer is a supporting lemma for the row, not yet a note-carrying title theorem.
- Is the claim still too dependent on hand-picked small cases? It is not brute-force small-case dependent, but it is still too dependent on one small quotient direction and one exact parameter row.

Theorem-worthiness verdict:
- the slice is mathematically real and exact;
- it is strong enough to preserve as a named theorem slice;
- it is not strong enough to carry the micro-paper lane by itself.

## publication_publishability
Answers required by the audit:

- Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note? No.
- What percentage of the paper would one solve already provide? About `0.39`.
- Is there a real title theorem, theorem slice, or counterexample theorem here? There is a real theorem slice, not a real title-theorem resolution of the selected row.
- Is the proof structural or merely instance-specific? Structural but auxiliary.
- Would this survive a referee asking "what is the theorem?" Only as a lemma-level contribution inside a stronger paper.
- Is the claim still too dependent on hand-picked small cases? Yes, in the sense that only the `11`-quotient has been closed.
- If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit? The target itself remains attractive, but the current packet is not close; the remaining gap is still substantive.
- If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program? Yes. Preserve the slice and move aside unless a tightly bounded `71`- or `121`-quotient obstruction is immediately available.
- Would Lean directly seal the packet, or would it only be optional polish / later archival formalization? Only optional polish for the slice; Lean would not convert this packet into a human-ready publication packet.

Publishability verdict:
- not `PAPER_READY`;
- not a near-complete note;
- still publication-distant despite being mathematically nontrivial.

## publication_packet_audit
Packet verdict:
- strongest honest publication tier: `SLICE_EXACT`;
- publication confidence: `medium`;
- packet quality: exact slice preserved, but not note-shaped;
- proof artifacts are preserved well enough for future reuse;
- this is not a `HUMAN_READY` packet and should not leave the main discovery lane as a publication success.

Interpretation:
- the audited packet does contain a proved nontrivial theorem slice;
- however, it does not yet shorten the solve-to-publication distance enough to justify growing this row into a broader campaign from this packet alone.

## micro_paper_audit
Micro-paper verdict:
- the selected row remains a legitimate micro-paper target if the exact cyclic row is settled;
- the current audited packet does not meet the micro-paper lane as a deliverable;
- the present slice is useful scaffolding, not `70-90%` of a paper;
- the current audited fraction is about `0.39`, with `title_theorem_strength = medium` only because the theorem is auxiliary rather than the paper title theorem, and `publication_narrative_strength = low`.

Operational consequence:
- do not let this slice sprawl into a feeder-ladder program;
- keep it as a preserved exact obstruction slice and reopen only for one more narrow structural strike.

## strongest_honest_claim
Any hypothetical cyclic `(8591,4295,2147)` difference set has `C_11` quotient profile `(375;405^5;379^5)` or `(425;395^5;379^5)`, up to swapping the two nonzero `3`-orbits; equivalently, every order-`11` character value is forced to `-17 ± 13 sqrt(-11)` or `38 ± 8 sqrt(-11)`.

## paper_title_hint
Forced Order-`11` Quotient Profiles in the Cyclic Hadamard Case `(8591,4295,2147)`

## next_action
Preserve the exact `C_11` slice, cool the row, and do not expand into a broader theorem program from this packet. Reopen only if a tightly scoped `C_71` or `C_121` obstruction can be attacked within the same one-shot lane.
