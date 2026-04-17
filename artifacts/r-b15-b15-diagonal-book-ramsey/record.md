# Solve Record: The Exact Value of R(B15, B15)

- slug: `r-b15-b15-diagonal-book-ramsey`
- working_packet: `artifacts/r-b15-b15-diagonal-book-ramsey/working_packet.md`

## statement_lock
Locked target: determine whether the one-step gap closes at `61` or `62`, i.e. prove either `R(B15,B15)=61` by forcing a monochromatic `B15` in every coloring of `K_61`, or `R(B15,B15)=62` by exhibiting a `61`-vertex coloring with no monochromatic `B15`.

Exact title-theorem candidate if the construction route succeeds: `R(B15,B15)=62`.

## definitions
- `B15` is the book graph consisting of `15` triangles sharing one common spine edge.
- For a color class graph `G` on `n` vertices, a monochromatic `B15` is equivalent to an edge of `G` lying in at least `15` triangles of `G`.
- Write `b(G)=max_{uv in E(G)} |N_G(u) cap N_G(v)|`. Then a red-blue coloring of `K_n` avoids monochromatic `B15` iff for one color class `G` we have `b(G) <= 14` and `b(\bar G) <= 14`.
- The packet supplies the literature bound `61 <= R(B15,B15) <= 62`, so a valid `61`-vertex witness would close the exact value.

Self-check: the solve target is genuinely exact-value, not merely a witness-hunt, because the cited upper bound already leaves a one-step gap.

## approach_A
Structural / invariant route via monochromatic triangle counts.

Let `G` be the red graph of a hypothetical coloring of `K_61` with no monochromatic `B15`. Then every red edge lies in at most `14` red triangles and every blue edge lies in at most `14` blue triangles. If `t(G)` and `t(\bar G)` denote the red and blue triangle counts, then

`3 t(G) <= 14 e(G)` and `3 t(\bar G) <= 14 e(\bar G)`.

Hence

`t(G) + t(\bar G) <= 14 * C(61,2) / 3 = 14 * 1830 / 3 = 8540`.

Goodman's identity gives

`t(G) + t(\bar G) = C(61,3) - (1/2) sum_v d(v)(60-d(v))`.

Since `d(60-d) <= 30*30 = 900` for every integer `d`,

`t(G) + t(\bar G) >= 35990 - (1/2) * 61 * 900 = 8540`.

So equality must hold throughout. Therefore every vertex has degree exactly `30`, every red edge lies in exactly `14` red triangles, and every blue edge lies in exactly `14` blue triangles.

Consequences:
- Any extremal `61`-vertex coloring must be perfectly balanced.
- In the red graph, adjacent pairs have exactly `lambda = 14` common red neighbors.
- For a nonedge `uv`, the blue edge `uv` has exactly `14` common blue neighbors; since `d(u)=d(v)=30`, this forces `|N_G(u) cap N_G(v)| = 15`.
- Thus any extremal witness on `61` vertices must be a strongly regular graph with parameters `(61,30,14,15)`.

Self-check: this route does not itself settle the problem, but it sharply narrows the target to a very rigid object and explains why order `61` is the critical threshold.

## approach_B
Construction / extremal route via the Paley graph on `F_61`.

Let `Q` be the set of nonzero quadratic residues modulo `61`. Color `{x,y}` red when `x-y in Q`, and blue otherwise. Because `61 equiv 1 mod 4`, we have `-1 in Q`, so the coloring is undirected.

This is the natural candidate for the `(61,30,14,15)` structure suggested by Approach A:
- each vertex has `30` red neighbors because exactly half of the nonzero residues are squares;
- the coloring is self-complementary up to multiplication by a nonsquare;
- common-neighbor counts reduce to counting pairs of consecutive residues / nonresidues.

For `a != 0`, common red neighbors of `0` and `a` are the `z` with `z in Q` and `z-a in Q`.

If `a in Q`, scaling by `a^{-1} in Q` reduces this to counting `t` with `t in Q` and `t-1 in Q`.

If `a notin Q`, scaling by the nonsquare `a^{-1}` reduces this to counting `t` with `t` and `t-1` both nonsquares.

Let
- `A = #{t : chi(t)=1, chi(t-1)=1}`,
- `B = #{t : chi(t)=1, chi(t-1)=-1}`,
- `C = #{t : chi(t)=-1, chi(t-1)=1}`,
- `D = #{t : chi(t)=-1, chi(t-1)=-1}`,
where `t` ranges over `F_61 \\ {0,1}` and `chi` is the quadratic character.

Then:
- `A+B = 29` because among `F_61 \\ {0,1}`, there are `29` residues and `30` nonsquares.
- `A+C = 29` by the same count shifted by `1`.
- Since `-1` is a square, the involution `t -> 1-t` swaps the `(+,-)` and `(-,+)` cases, so `B=C`.
- The character sum `sum_t chi(t(t-1)) = -1` yields `A + D - B - C = -1`.

Solving gives `A=14`, `B=C=D=15`.

Therefore:
- if `a in Q` (red edge), the pair has exactly `14` common red neighbors;
- if `a notin Q` (blue edge), the pair has exactly `14` common blue neighbors by symmetry, equivalently exactly `15` common red neighbors.

So the Paley coloring on `61` vertices avoids monochromatic `B15`.

Self-check: if these counts are right, the construction gives the missing `61`-vertex witness and closes the exact value at `62`.

## lemma_graph
Proof skeleton.

1. Literature packet gives `R(B15,B15) <= 62`.
2. A `61`-vertex witness with monochromatic book number at most `14` in both colors would imply `R(B15,B15) >= 62`.
3. Goodman equality shows any such witness must have the rigid `(61,30,14,15)` conference-graph shape.
4. The Paley coloring on `F_61` is the canonical candidate for that shape.
5. Quadratic-character counting gives:
   - adjacent red pairs have `14` common red neighbors,
   - adjacent blue pairs have `14` common blue neighbors.
6. Therefore the Paley coloring of `K_61` has no monochromatic `B15`.
7. Combining steps `1` and `6` gives the candidate theorem `R(B15,B15)=62`.

Self-check: the only load-bearing step not yet externally checked in-repo is the residue-count arithmetic for the Paley witness.

## chosen_plan
Choose Approach B as the main solve path, with Approach A kept as the invariant explanation for why the Paley witness is the right object rather than an ad hoc search hit.

Immediate next step:
- run a tiny verification script for the explicit Paley(61) coloring;
- confirm degree `30` and monochromatic book number exactly `14` in both colors;
- if confirmed, record the exact-value candidate `R(B15,B15)=62`.

What extra structure would make this paper-shaped if the main claim closes?
- A clean statement that the Paley(61) coloring is a `(61,30,14,15)` conference witness.
- One short lemma extracting the exact common-neighbor counts from the quadratic-character partition.
- One boundary remark explaining that this is a family-anchored exact-value note, but the Paley mechanism does not automatically settle all neighboring diagonal book numbers.

## self_checks
- Statement lock check: the solve is aimed at the exact diagonal value, not only at a lower-bound artifact.
- Definitions check: `B15` has been converted into a precise edge-in-triangles condition, so both combinatorial counting and construction language match.
- Approach check: Approach A is genuinely structural/invariant; Approach B is genuinely construction/extremal.
- Risk check before code: the only serious remaining failure mode is an arithmetic slip in the Paley common-neighbor count.
- Post-code check: the explicit Paley(61) witness matched the predicted parameters exactly, so the remaining risk is no longer arithmetic but verification-stage novelty / citation scope.

## code_used
Yes, minimal witness-verification only.

Bounded Python check performed:
- built the Paley graph on `F_61` from the nonzero quadratic residues modulo `61`;
- verified every vertex has degree `30`;
- verified every red edge has exactly `14` red common neighbors;
- verified every nonedge has exactly `15` red common neighbors;
- verified the maximum monochromatic book size is `14` in both colors.

Explicit residue set used for the witness:
`{1,3,4,5,9,12,13,14,15,16,19,20,22,25,27,34,36,39,41,42,45,46,47,48,49,52,56,57,58,60}`.

## result
Main candidate result: `R(B15,B15)=62`.

Lower bound:
- The Paley coloring of `K_61` defined by quadratic residues modulo `61` has monochromatic book number exactly `14` in each color.
- Therefore `K_61` admits a red-blue coloring with no monochromatic `B15`, so `R(B15,B15) >= 62`.

Upper bound:
- The working packet cites Lemma 1 of Lidicky-McKinley-Pfender-Van Overberghe 2025 as giving `R(B15,B15) <= 62`.

Combined conclusion:
- assuming that cited upper bound is exactly as stated, the exact diagonal book Ramsey number is `R(B15,B15)=62`.

What part of the argument scales:
- the Goodman-equality reduction to a conference-style witness at the critical order;
- the Paley construction whenever a suitable field order `q equiv 1 mod 4` matches the target book parameter.

What part does not scale automatically:
- converting a family lower-bound template into an exact diagonal value still needs the matching sharp upper bound for the specific `n`;
- the residue-count proof gives one rigid witness, not a general forcing theorem for neighboring diagonal cases.

What theorem slice is suggested:
- a stand-alone lemma that the Paley coloring on `61` vertices has monochromatic book number exactly `14`.

What next parameter shifts would help most:
- test whether the same conference-graph logic gives the sharp lower-bound endpoint for the next diagonal case `B16`;
- compare against the solved near-diagonal `R(B14,B15)=59` corridor to see whether a common short proof package can be extracted.

Current package assessment:
- this is no longer just an isolated instance witness; it is a near-paper exact-value candidate because the witness closes the cited one-step gap directly.

## family_affinity
High. This sits directly inside the diagonal book Ramsey family at the `4n+1 / 4n+2` threshold, and the witness shape is the conference-graph / Paley mechanism already native to extremal Ramsey constructions.

## generalization_signal
Moderate. The conference-graph mechanism scales to prime powers `q equiv 1 mod 4`, where the Paley graph has parameters `(q,(q-1)/2,(q-5)/4,(q-1)/4)`. That suggests a reusable lower-bound template for `B_{(q-5)/4}`. What does not scale automatically is exactness: the upper endpoint still has to be closed separately for each `n`.

## proof_template_reuse
Reusable template:
1. turn monochromatic books into edge-codegree bounds;
2. apply Goodman to identify the equality case at the critical order;
3. search only for the forced strongly-regular / conference witness;
4. instantiate that witness with a Paley graph when a suitable field order exists.

## candidate_theorem_slice
Candidate lower-bound slice: the Paley coloring of `K_61` has monochromatic book number exactly `14` in each color. This is the smallest theorem slice that already carries the full exact-value conclusion once combined with the cited upper bound `R(B15,B15) <= 62`.

## smallest_param_shift_to_test
Two nearby shifts matter most:
- `B14`: compare whether the same conference-graph mechanism cleanly explains the already-solved neighboring almost-diagonal corridor.
- `B16`: test whether the next diagonal case admits an analogous critical-order construction or whether the Paley/conference template breaks immediately.

## why_this_is_or_is_not_publishable
If the Paley(61) witness is correct, this is close to the micro-paper sweet spot. A successful solve would already be about `75%` to `85%` of a paper because:
- the exact title theorem is `R(B15,B15)=62`;
- the family placement is immediate;
- the remaining packaging is light: write the explicit coloring, prove the common-neighbor counts, and cite the existing `<= 62` bound.

It would be too thin only if the construction turned out to be folklore already attached to the exact `B15` case. That is a verification-stage novelty question, not a solve-stage mathematical gap.

## paper_shape_support
Paper-shaped support if the main claim closes:
- main theorem: `R(B15,B15)=62`;
- supporting lemma: the Paley graph on `61` vertices is strongly regular with parameters `(61,30,14,15)`;
- immediate corollary / remark: the critical coloring is self-complementary and achieves monochromatic book number exactly `14` in both colors;
- minimal remaining packaging work: a compact residue-count proof, one figure or explicit residue set, and literature comparison against the known `61 <= R <= 62` gap.
- exact sentence for why the instance matters: this single `61`-vertex critical coloring closes a public one-step frontier gap, so the witness is already the title-theorem artifact of a short exact-value note.

## boundary_remark
Boundary remark: this solve would be stronger than a bare instance witness because it identifies the exact critical `61`-vertex mechanism, but it still does not by itself produce a broad new theorem for all diagonal book Ramsey numbers. The paper claim is exact-value, family-anchored, and micro-paper sized.

## likely_failure_points
- The packet's upper bound must really be the exact statement `R(B15,B15) <= 62`, not merely a nearby variant in different notation.
- Verification should check that this `61`-vertex witness is not already explicitly recorded as settling the case in the cited literature.
- If the Paley witness is already implicit in the cited sources, the mathematical result may still be correct but publication status would drop from frontier solve to rediscovery / repackaging.

## what_verify_should_check
- Confirm the literature bound used here is exactly `R(B15,B15) <= 62`.
- Novelty-check whether the Paley(61) witness or an equivalent conference-graph construction is already noted in the sources as settling `R(B15,B15)=62`.
- Verify the explicit residue set and the common-neighbor counts independently.
- Check whether the argument should be presented as a new exact determination or as a new short proof of a result already implicit elsewhere.

## verify_rediscovery
PASS 1 used a bounded web audit on `2026-04-15` with exact-statement, alternate-notation, canonical-source, and recent-status queries.

Findings:
- Lidicky-McKinley-Pfender-Van Overberghe 2025, Lemma 1, confirms only the interval `4n+1 <= R(B_n,B_n) <= 4n+2` for `n <= 21`, so for `n=15` the cited source gives `61 <= R(B15,B15) <= 62`.
- The same source attributes the lower bound side to existing construction machinery, but only at the `61 <= R(B15,B15)` level; this does not already supply a `61`-vertex witness and does not settle the exact value.
- Bounded checks around Wesley 2026 turned up recent diagonal and near-diagonal book-Ramsey updates, but no exact public statement `R(B15,B15)=62` and no explicit prior-art record of the Paley(61) witness closing the diagonal `B15` case.

Verdict for PASS 1:
- rediscovery not established within the bounded audit;
- no source located in PASS 1 already settles the exact intended statement.

## verify_faithfulness
The intended statement is the exact diagonal value `R(B15,B15)`.

Faithfulness check:
- the solver's new mathematical content is a `61`-vertex witness, which proves the lower-bound slice `R(B15,B15) >= 62`;
- the source-backed upper bound `R(B15,B15) <= 62` matches the same exact target and closes the same instance;
- there is no quantifier drift, no change of object, and no nearby-family substitution.

Conservative wording repair:
- the locally checked contribution is the witness and its consequences;
- the exact-value theorem should be described as a verified candidate exact theorem supported by the checked witness plus the cited upper bound, not as a self-contained in-repo upper-bound proof.

## verify_proof
No incorrect mathematical step was found in the lower-bound argument.

Checks:
- the Goodman bound arithmetic is consistent: `t(G)+t(\\bar G) <= 14 * \\binom{61}{2} / 3 = 8540`, while Goodman's identity gives the matching lower bound `8540`, so equality forces degree `30` at every vertex and the rigid `(61,30,14,15)` parameter pattern;
- for nonedges, the conversion from blue common-neighbor count `14` to red common-neighbor count `15` is correct once regularity and the `59` remaining vertices are accounted for;
- in the character-count proof, the equations `A+B=29`, `A+C=29`, `B=C`, and `A+D-B-C=-1` solve to `A=14` and `B=C=D=15`, exactly as claimed.

External dependency retained:
- the exact-value conclusion still depends on the cited literature upper bound `R(B15,B15) <= 62`, which was verified as a source claim in PASS 1 but not reproved locally.

## verify_adversarial
An independent bounded Python rerun checked the explicit Paley construction on `F_61`.

Observed outputs:
- degree set: `{30}`;
- red common-neighbor count on every red edge: `14`;
- red common-neighbor count on every blue edge: `15`;
- blue common-neighbor count on every blue edge: `14`;
- maximum red book size: `14`;
- maximum blue book size: `14`;
- triangle totals: `t(G)=4270`, `t(\\bar G)=4270`, so `t(G)+t(\\bar G)=8540`, matching the Goodman equality calculation.

The recorded quadratic-residue set modulo `61` was also rechecked and matches the explicit list in the solve record.

Adversarial verdict:
- the claimed `61`-vertex construction survives direct recomputation;
- no hidden monochromatic `B15` appeared under rerun.

## verify_theorem_worthiness
Exactness:
- if the cited upper bound is used exactly as stated, the visible title theorem is `R(B15,B15)=62`.

Novelty:
- bounded rediscovery checking did not find an earlier exact settlement, but that remains a publication-audit task rather than a finished novelty theorem.

Reproducibility:
- high; the witness is explicit, short, and independently rerunnable with a tiny checker.

Lean readiness:
- `lean_ready = false`;
- `lean_packet_seal = false`;
- reason: the shortest remaining path is not formalization. The remaining gap is publication-audit hardening of novelty and a compact human proof packet around the checked Paley witness plus the cited upper bound. Lean would currently be archival polish rather than the minimal route to a sealed paper packet.

Micro-paper assessment:
- if the result remains frontier-novel, one solve would already provide most of a publishable note;
- estimated single-solve-to-paper fraction remains about `0.75`;
- the visible title theorem is exactly `R(B15,B15)=62`;
- what scales is the lower-bound template: conference/Paley structure and the codegree computation;
- what does not scale automatically is exactness, since each neighboring diagonal case still needs its own sharp upper endpoint and its own novelty check.

Best honest publication status after verify:
- still `SLICE_CANDIDATE`, not `PAPER_READY`;
- this is stronger than `INSTANCE_ONLY` because the theorem slice already carries the full exact-value note once the literature positioning is hardened, but the packet is not yet publication-audited tightly enough to call finished.

## verify_verdict
`VERIFIED`

Meaning of this verdict here:
- the locally checkable mathematics supports the lower-bound slice and is consistent with the exact intended statement;
- no rediscovery was established in the bounded PASS 1 audit;
- classification should remain `CANDIDATE`, not `EXACT`, because Lean is not complete and the publication-status lane still needs its dedicated audit.

## minimal_repair_if_any
No mathematical repair was needed.

One conservative presentation repair is required:
- wherever the solve record sounds unconditional, restate the outcome as a verified candidate exact theorem supported by a checked `61`-vertex Paley witness together with the cited upper bound `R(B15,B15) <= 62`.

## publication_prior_art_audit
Bounded audit performed on `2026-04-15` with the required narrow passes.

Exact-statement search:
- direct searches for `R(B15,B15)` and `R(B_{15},B_{15})` did not immediately surface an exact-value hit;
- this means the case is easy to miss if the audit stays at the literal instance notation only.

Alternate-notation search:
- searching the family form `R(B_n,B_n)=4n+2` with the prime-power condition produced the decisive prior art;
- Wesley 2026 states in its introduction / Theorem 1 that if `q=4n+1` is a prime power, then `R(B_n,B_n)=4n+2`;
- substituting `n=15` gives `q=61`, and `61` is prime, so the theorem already yields `R(B15,B15)=62`.

Canonical-source check:
- `Lidicky-McKinley-Pfender-Van Overberghe 2025`, Lemma 1, still supports the coarse corridor `61 <= R(B15,B15) <= 62`;
- inside that canonical source, the cited note on Lemma 1 attributes the upper bounds to `RS78` and only records a lower-bound witness family, so reading Lemma 1 alone makes the case look like a one-step gap;
- `Wesley 2026`, however, explicitly records the stronger theorem-level sufficient condition that settles the diagonal case whenever `4n+1` is a prime power.

Theorem / proposition / example / corollary / observation / sufficient-condition check:
- the decisive prior art is theorem-level, not merely an example or observation;
- the relevant sufficient condition is exactly the prime-power condition `4n+1 = q`, which applies here with `q=61`.

Outside-source status pass:
- the exact-statement and alternate-notation web checks found no evidence that `R(B15,B15)=62` is being treated as a fresh frontier result;
- the consistent status is instead that this is a classical family consequence that the selected packet failed to surface.

Recent follow-up check:
- not needed, because the theorem-level prior art already resolves novelty decisively.

Audit verdict:
- `REDISCOVERY`.

## publication_statement_faithfulness
The local solve remains mathematically faithful only as a lower-bound artifact:
- the checked Paley coloring of `K_61` really does prove the slice `R(B15,B15) >= 62`;
- combining that slice with a literature upper bound still targets the right exact instance;
- the publication packet was not faithful to the prior-art situation, because it framed this instance as open even though the prime-power diagonal theorem already covers it.

Conservative repair:
- the strongest honest statement is no longer "we determined `R(B15,B15)`";
- it is "we reconstructed a correct Paley(61) witness for a known exact diagonal book Ramsey value."

## publication_theorem_worthiness
Is the strongest honest claim stronger than "here is an example"?
- No as a new-paper claim. The witness is structured and correct, but publication-wise it only rederives a known theorem instance.

Is there a real title theorem, theorem slice, or counterexample theorem here?
- There is a real theorem, namely the already-known exact value `R(B15,B15)=62`, but this packet does not create a new theorem.

Is the proof structural or merely instance-specific?
- The witness is structural, since it sits inside the classical prime-power / Paley mechanism;
- the contribution of this packet is still only an instance-level reconstruction of that known mechanism.

Would this survive a referee asking "what is the theorem?"
- No as a novelty claim. A referee would immediately point to the existing prime-power theorem and ask what is new beyond rechecking one witness.

Is the claim still too dependent on hand-picked small cases?
- Yes for publication purposes. Once novelty collapses, the packet is just one explicit `n=15` realization of a known family theorem.

## publication_publishability
Would this result, if correct and verified in the current bounded sense, already constitute most of a publishable note?
- No for the MICRO-PAPER frontier lane.

What percentage of the paper would one solve already provide?
- About `0.10` at best, because the solve reproduces known mathematics rather than supplying a frontier title theorem.

If this is not yet paper-ready, is the remaining gap genuinely small or did the candidate only look attractive before audit?
- It only looked attractive before audit;
- the blocker is not light packaging, but a failed novelty premise.

If this is not yet paper-ready, should it be moved aside rather than expanded into a larger theorem program?
- Yes. It should be moved aside as `REDISCOVERY`, not expanded.

Would Lean directly seal the packet, or would it only be optional polish / later archival formalization?
- Lean would be optional archival formalization only;
- it would not convert this rediscovery into a publishable frontier packet.

## publication_packet_audit
Publication verdict:
- `publication_status = REDISCOVERY`.

Reason:
- the Paley(61) witness is correct and preserved;
- the exact value it supports was already settled by the prime-power diagonal book theorem cited in `Wesley 2026`.

Packet quality:
- mathematically clean as an internal witness packet;
- low as a publication packet, because the novelty lane is closed.

Human-ready / stop-tier consequences:
- not `PAPER_READY`;
- `human_ready = false`;
- keep the proof artifacts, but move the slug aside rather than forwarding it to the human-ready or Lean queues.

## micro_paper_audit
MICRO-PAPER verdict:
- fail the micro-paper lane.

Reasoning:
- before audit, the packet appeared to be a one-step frontier gap with high title-theorem leverage;
- after audit, the exact case is already covered by a classical family theorem, so the leverage collapses;
- the checked witness is still useful as preserved support, but it no longer shortens solve-to-publication distance in the frontier sense.

Would this result already read like most of a publishable note?
- No.

Would this be more than an instance note?
- No. In frontier terms it drops below even `INSTANCE_ONLY`, because the instance itself is already known.

## strongest_honest_claim
The Paley coloring of `K_61` is a correct witness with monochromatic book number `14` in each color, but this only reproduces the already-known exact value `R(B15,B15)=62` covered by the classical prime-power diagonal book theorem recorded in `Wesley 2026`.

## paper_title_hint
No new-paper title is recommended.

Internal reference title only:
- `Paley(61) Witness for the Known Value R(B15,B15)=62`.

## next_action
Reclassify the slug as `REDISCOVERY`, preserve the explicit Paley witness and verification notes as internal reference artifacts, and move the candidate aside instead of expanding it or sending it to Lean.
