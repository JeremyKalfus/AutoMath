# Solve Record: The edge-Erdos-Posa property for the 4-rung ladder

## statement_lock
- Active slug: `ladder-4-rungs-edge-erdos-posa`
- Active title: `Does the ladder with 4 rungs have the edge-Erdos-Posa property?`
- Entry type: `paper_candidate`
- Intended statement locked for this run: determine whether the 4-rung ladder `L4` has the edge-Erdos-Posa property.
- Concrete model used in this solve attempt: `L4` has vertices `a1,a2,a3,a4,b1,b2,b3,b4`, rail edges `a_i a_{i+1}` and `b_i b_{i+1}` for `i=1,2,3`, and rungs `a_i b_i` for `i=1,2,3,4`.
- Solve target for this run: either produce a rigorous positive reduction that genuinely closes `L4`, or produce a rigorous obstruction/counterexample mechanism. No such closure was reached in this run; the strongest honest output is a structural reduction around extendable 3-rung cores.

## definitions
- Ambiguity noted: the packet states the edge-Erdos-Posa property in standard graph-theoretic language but does not explicitly say whether graphs are simple or may have parallel edges. This attempt assumes finite simple graphs, since the ladder source is framed that way in ordinary usage.
- A subdivision of `L4` is a topological minor model in which each edge of `L4` is replaced by a path and the replacement paths are internally vertex-disjoint.
- For an `L4`-subdivision `S`, the `left 3-rung core` means the subgraph obtained by deleting the rightmost cell, equivalently keeping rungs `1,2,3`; the `right 3-rung core` is defined symmetrically.
- A `terminal rung` of a 3-rung ladder subdivision is one of its two end rungs.
- An `extendable 3-rung core` is a 3-rung ladder subdivision `K` together with a terminal rung having endpoints `x,y` such that `G - E(K)` contains an `x-y` path `Q` whose internal vertices avoid `K` and whose length is at least `3`.
- Observation: if `K` is extendable in this sense, then `K ∪ Q` contains an `L4`-subdivision. One uses an internal edge of `Q` as the new rung and the two nonempty subpaths from `x` and `y` to that edge as the new rail segments.

## approach_A
- Structural / invariant approach: reduce `L4` to `L3` plus one terminal extension.
- Every `L4` contains a left 3-rung core and a right 3-rung core. For either end core, the deleted fourth cell becomes an extra path between the endpoints of the terminal rung.
- This yields the key reduction:
  - `L4`-subdivision `=>` an extendable `L3`-subdivision.
  - Conversely, an extendable `L3`-subdivision `=>` an `L4`-subdivision.
- Since the 3-rung ladder already has the edge-Erdos-Posa property, the hope is that one can lift the known `L3` hitting/packing control to the strictly smaller family of extendable `L3` cores.
- Local control does work in the hitting direction. Fix one 3-rung core `K` and one terminal rung with endpoints `x,y`. All ways to extend `K` at that side are exactly the `x-y` paths in `G-E(K)` of length at least `3` that avoid `K` internally. Any edge cut separating `x` from `y` in `G-E(K)` hits all such extension paths.
- The obstruction is global, not local. Even if there are many `x-y` paths around one fixed core, that does not by itself produce many edge-disjoint `L4` subdivisions because all those copies reuse the core edges, and plain edge-Menger does not directly certify many sufficiently long extension paths.
- Self-check after approach A: the reduction is mathematically coherent and isolates the right missing lemma, but it does not yet convert many extendable cores into many edge-disjoint `L4` subdivisions or one bounded global hitting set.

## approach_B
- Construction / extremal / contradiction approach: look for the first counterexample mechanism beyond the 14-rung condensed-wall barrier.
- A naive negative family would try to force every `L4` through one narrow central strip while still allowing arbitrarily many distinct `L4` subdivisions. This is weaker than the 14-rung mechanism because `L4` needs only one extra cell beyond `L3`, so any fixed-core construction is vulnerable to a local terminal cut.
- More concretely, if all `L4` subdivisions in a host family arise by extending a bounded number of `L3` cores, then each core-end is controlled by a finite `x-y` cut argument, so a bounded union of local cuts destroys all `L4` subdivisions. Therefore a genuine negative family would need many essentially different cores, not just many alternate end paths around one core.
- This suggests why the published 14-rung negative mechanism may not compress directly to `L4`: the large-rung obstruction can distribute complexity over many cells, while `L4` exposes a terminal-rung interface that is much easier to separate.
- Self-check after approach B: this argues against the most naive condensed-wall transplant, but it is not a proof that no more sophisticated non-condensed-wall counterexample exists.

## lemma_graph
- Lemma 1: Every `L4`-subdivision contains an extendable `L3`-subdivision.
- Lemma 2: Every extendable `L3`-subdivision contains an `L4`-subdivision.
- Lemma 3: For a fixed `L3` core `K` and fixed terminal rung endpoints `x,y`, all `L4` subdivisions obtained by extending that end of `K` are hit by any edge cut separating `x` from `y` in `G-E(K)`.
- Lemma 4 candidate: If a graph contains many pairwise edge-disjoint extendable `L3` cores whose extension interfaces are sufficiently separated, then it contains many edge-disjoint `L4` subdivisions.
- Missing bridge: a compact global theorem saying that every family of extendable `L3` cores either concentrates on boundedly many terminal interfaces or yields `k` edge-disjoint `L4` subdivisions.

## chosen_plan
- Chosen path: pursue the positive side through the `extendable L3 core` reduction.
- Reason for choosing it: it is the cleanest local structure available from the packet, it directly exploits the known `L3` positive case, and it explains why `L4` may still be positive even though large ladders are negative.
- Immediate objective in this run: prove the reduction rigorously enough to support a future theorem slice, then identify the exact unsolved globalization step rather than pretending a full proof.

## self_checks
- Step 1, statement lock: the intended statement stayed fixed on the single yes/no theorem for `L4`; no drift into broader ladder campaigns.
- Step 2, decomposition check: deleting one end cell of an `L4` subdivision really does leave a 3-rung ladder subdivision; conversely any terminal extension path of length at least `3` around a 3-rung core rebuilds a fourth rung.
- Step 3, local-cut check: for a fixed core the right language is an `x-y` path problem in `G-E(K)`, and any `x-y` cut there destroys all terminal extensions.
- Step 4, packing check: the Menger packing side fails to solve the whole problem because parallel extensions of one core share the core edges; this is the genuine bottleneck and not a bookkeeping issue.
- Step 5, counterexample check: no explicit host graph family was produced, so this run does not justify `COUNTEREXAMPLE`.
- Step 6, proof check: no complete edge-Erdos-Posa theorem or disproof was obtained, so this run must remain `PARTIAL`.

## code_used
- No code used in this run.
- Reason: the current bottleneck is conceptual, not computational. A brute-force or SAT-style search would violate the prompt’s default policy and would not address the missing global lemma.

## result
- Strongest honest result of this run:
  - `L4` can be reformulated exactly as the family of extendable 3-rung ladder subdivisions.
  - For a fixed 3-rung core, extensions are controlled by a terminal `x-y` path problem, hence by local edge cuts.
  - Therefore any negative construction for `L4` must evade bounded unions of such local terminal cuts by using many essentially distinct cores or interfaces.
- Rigorous proof skeleton for the core equivalence:
  - Let `S` be an `L4`-subdivision with branch vertices corresponding to `a1,...,a4,b1,...,b4`.
  - Remove the rightmost cell, meaning the top and bottom rail segments from rung `3` to rung `4` together with the fourth rung. The remaining subgraph is an `L3`-subdivision `K`.
  - The deleted cell is a path `Q` from the endpoints `x,y` of the third rung: go from `x` along the top segment to the fourth top branch vertex, cross the fourth rung, then return along the bottom segment to `y`. This `Q` is internally disjoint from `K` and has length at least `3`.
  - Hence `S` contains an extendable `L3` core.
  - Conversely, suppose `K` is an `L3`-subdivision and `Q` is an `x-y` path in `G-E(K)` internally disjoint from `K`, where `x,y` are the endpoints of a terminal rung of `K` and `|E(Q)| >= 3`.
  - Choose an internal edge `uv` of `Q`. Then the subpath of `Q` from `x` to `u`, the edge `uv`, and the subpath from `v` to `y` serve as the two new rail segments and the new rung of a fourth cell attached at the terminal rung `xy`.
  - The union with `K` is a subdivision of `L4`.
- This does not settle the main question because the global edge-packing/hitting interaction between many extendable cores remains open in the current attempt.
- What part of the argument scales:
  - The decomposition `Lt = extendable L_{t-1}` scales formally to every ladder length `t >= 2`.
  - The fixed-core terminal-cut analysis also scales to every end-extension step.
- What part does not scale:
  - The missing globalization step already appears at `t=4`; iterating the local reduction alone does not produce a packing theorem.
  - The argument does not distinguish whether `t=4` is the last positive case or whether a broader range `4,...,13` is positive.
- Suggested theorem slice from this run:
  - prove a bounded-interface theorem for extendable `L3` cores, or
  - prove that any family of pairwise edge-disjoint extendable `L3` cores can be pruned to edge-disjoint `L4` subdivisions once the cores are sufficiently separated.
- Next feeder instances that would help most:
  - a one-ended slice where all `L4` subdivisions must use the same terminal side of an `L3` core,
  - a two-core interaction lemma describing when two extendable `L3` cores can be uncrossed into edge-disjoint `L4` subdivisions.
- Current package status: still not an instance-only exact result and not yet a theorem; it is closer to a paper-shaped claim than a random failed attempt because it identifies a sharp structural reduction, but it is not yet publishable.

## family_affinity
- Affinity: high with the ladder family, but the useful signal is narrow.
- The reduction `Lt = extendable L_{t-1}` suggests a recursive ladder viewpoint.
- For the publication objective, the relevant family signal is not “all ladders” but “small ladders may be positive until the extension interfaces become globally uncontrollable.”

## generalization_signal
- Real signal: the open difficulty may be reframed as a controlled extension problem over the already-positive `L3` case.
- If one can prove a bounded-interface theorem for extendable `L3` cores, that would likely give `L4` directly and may illuminate some later rung counts.
- If instead one can build a counterexample family requiring many incomparable extendable cores, that would show the first failure mechanism already appears at `t=4`.

## proof_template_reuse
- Reusable template:
  - represent `Lt` as an end-extension of `L_{t-1}`,
  - isolate a local terminal interface at one end rung,
  - apply an edge-cut/path dichotomy locally,
  - then seek a global uncrossing or representative-interface lemma.
- This template should reuse for `L5` and higher only if the `L4` globalization step is first understood; otherwise the same obstruction simply propagates upward.

## candidate_theorem_slice
- Candidate theorem slice:
  - Every `L4`-subdivision is equivalent to an extendable `L3`-subdivision.
  - Therefore the `L4` edge-Erdos-Posa problem reduces to proving a global packing/hitting theorem for extendable `L3` cores.
- This is not yet a standalone theorem note, but it is the most concrete honest slice extracted in this run.

## smallest_param_shift_to_test
- Smallest shift to test next: a one-sided version in which only right-end extensions of `L3` cores are allowed.
- Reason: it removes the left/right symmetry and may make the global interface lemma significantly cleaner without changing the essential `L3 + one extra cell` structure.

## why_this_is_or_is_not_publishable
- If the main `L4` problem were solved cleanly, it would already be about `70-90%` of a paper, exactly as the packet claims.
- The exact paper claim would be either:
  - `The 4-rung ladder has the edge-Erdos-Posa property`, or
  - `The 4-rung ladder does not have the edge-Erdos-Posa property`.
- Minimal remaining packaging work after a successful solve would be:
  - align notation with the 2024 ladder paper,
  - add one short context section comparing `L3` positive and `L14` negative,
  - include a compact consequence/corollary section and, if positive, the explicit hitting-function dependence.
- This run is not publishable because it does not prove the target theorem or give a counterexample family.
- It is still publication-aware because it isolates a narrow, potentially paper-relevant theorem slice rather than generating unrelated feeder computations.

## likely_failure_points
- The main failure point is the global step from many extendable `L3` cores to either bounded hitting or `k` edge-disjoint `L4` subdivisions.
- A second failure point is hidden overlap: two different extendable cores may intersect in ways that defeat naive pruning and uncrossing.
- A third failure point is definitional: if the source paper uses a refined notion of condensed walls or special decompositions, this local reduction may be necessary but too weak compared with their machinery.
- A fourth failure point is false optimism: the reduction could be compatible with a sophisticated negative example, so it should not be overread as evidence for positivity.

## what_verify_should_check
- Verify that the decomposition lemma is stated with the correct subdivision conventions and does not accidentally use non-simple-graph behavior.
- Check whether the 2024 paper already contains a formulation equivalent to `L4 = extendable L3`; if so, this run should be downgraded as routine rather than novel.
- Check whether the one-sided extension slice already appears implicitly in the `L3` proof machinery.
- If a later solve run claims a positive theorem, verify the missing globalization step very carefully because that is the only serious gap left by this attempt.

## verify_rediscovery
- PASS 1 used a bounded web audit on 2026-04-12 with the required patterns: the exact 4-rung instance, alternate ladder notation, the canonical Steck-Ulmer source, same-source theorem / proposition / example / observation / corollary checks, and one later-status sweep.
- Within the search budget, I did not find a later paper, preprint, or status note settling the exact 4-rung ladder case.
- The canonical 2024 source still appears to be the controlling reference and is consistent with the packet claim that ladders with `4` through `13` rungs remain open there.
- I also did not find a same-source theorem, proposition, example, observation, or corollary already implying the exact 4-rung answer.
- Rediscovery verdict: not established.

## verify_faithfulness
- The solve record is faithful in one important respect: it does not pretend to settle whether `L4` has the edge-Erdos-Posa property.
- The strongest actual claim is only a structural reduction from `L4`-subdivisions to extendable `L3` cores plus a local cut observation for a fixed core.
- The original writeup did contain a small definitional mismatch inside that reduction: the extension path was said to need length at least `2`, but the converse construction needs an internal edge and therefore requires length at least `3`.
- After that repair, the artifact remains on the exact selected problem rather than drifting to a different theorem; it is just a corrected partial setup rather than a solution.

## verify_proof
- First incorrect step in the original text: the converse direction of the reduction was stated with an extension path of length at least `2`.
- For a 2-edge `x-y` path there is no internal edge available to serve as the fourth rung, so the converse implication as written was too strong.
- That issue is repairable by requiring `|E(Q)| >= 3` and choosing an internal edge of `Q`.
- A second overstatement also needed trimming: plain edge-Menger gives a small `x-y` cut or many edge-disjoint `x-y` paths, but it does not by itself guarantee many sufficiently long extension paths. The cut-side statement survives; the local packing-side slogan does not.
- After those conservative repairs, I do not see a further internal contradiction because the artifact already stops short of claiming the target theorem. The remaining gap is the intended one: no globalization lemma and no counterexample family.

## verify_adversarial
- There is no checker, code, or witness file in this artifact to rerun.
- I adversarially tested the converse construction on the shortest possible extension paths. A path of length `2` fails, exactly because it has no internal edge; a path of length `3` is the first case that works.
- I also stress-tested the local Menger language: a graph can have many edge-disjoint `x-y` paths of length `2`, so raw Menger packing does not certify many valid `L4` extensions around one fixed core.
- Those adversarial checks support the repaired record: the corrected reduction survives, but the writeup has no verified local packing theorem and no full edge-Erdos-Posa proof.

## verify_theorem_worthiness
- The corrected reduction to extendable `L3` cores is a useful structural lemma, but it is not yet `70-90%` of a paper for this `paper_candidate`.
- What looks real is a theorem slice one step later: a bounded-interface, uncrossing, or representative-core theorem for extendable `L3` subdivisions could plausibly close `L4`.
- What scales from the current artifact is the end-extension viewpoint and the fixed-core cut language.
- What clearly does not scale from the current artifact is any packing conclusion. The entire publication-critical difficulty is still the globalization step.
- The best honest publication status for the present artifact is therefore `NONE`, not `SLICE_CANDIDATE`: the current writeup exposes a plausible slice but does not yet prove one.
- The smallest adjacent test that most probes the claimed template is a one-sided version where only one terminal side of an `L3` core may be extended and one seeks a bounded-interface theorem there first.

## verify_verdict
- `MINOR_FIX`
- PASS 1 did not establish rediscovery.
- PASS 2 found a small but real definitional mismatch inside the reduction, now repaired conservatively.
- PASS 3 and PASS 4 also required softening the local Menger language to the cut-side statement that is actually justified.
- The surviving artifact is still only `PARTIAL`: a corrected structural reduction and fixed-core cut observation, not a solution of the `L4` edge-Erdos-Posa question.
- `lean_ready = false` and `lean_packet_seal = false` because formalizing this local reduction would not be the shortest remaining path to a sealed publication packet.

## minimal_repair_if_any
- Repaired the definition of an extendable `L3` core so that the terminal extension path must have at least `3` edges.
- Repaired the converse construction to choose an internal edge of the extension path.
- Softened the local-control paragraph so it records only the justified cut-side statement and no longer treats plain Menger packing as evidence for many valid extensions.
- No tiny repair yields the target theorem. Any next step still needs either a genuine globalization lemma or an explicit counterexample mechanism.

## publication_prior_art_audit
- Bounded live-web audit run on `2026-04-12` with the required narrow scope: exact-statement search (`4-rung ladder` plus `edge-Erdos-Posa`), alternate-notation search (`2 x 4 grid` / `2x4 grid` plus `edge-Erdos-Posa`), canonical-source check, same-source theorem / proposition / example / corollary / observation scan, and one outside-source status pass.
- Canonical source check: the Springer page for Steck and Ulmer, `On the Edge-Erdos-Posa Property of Ladders` (Graphs and Combinatorics 40, 2024), still frames the positive result at `3` rungs and the negative barrier at `14+` rungs, and its discussion explicitly asks whether the property holds for ladders with `4` to `13` rungs.
- Same-source implication check: within that canonical source, I did not find a theorem, proposition, example, corollary, observation, or sufficient-condition statement that already settles the exact `4`-rung case. The paper's `14+` obstruction language is tied to condensed walls and does not itself answer `L4`.
- Alternate-notation check: the `2 x 4 grid` / `2x4 grid` search did not surface an independent follow-up settling the edge-Erdos-Posa status of that graph; it mainly produced unrelated grid-material noise rather than a theorem closing the selected case.
- Outside-source status pass: Jean-Florent Raymond's dynamic Erdős-Pósa listing, last updated `2025-06-16`, still records the ladder-related edge-side entry at the `2 x 3` grid / house level and does not advertise a separate `4`-rung or `2 x 4` ladder closure. This is supportive but not dispositive because the listing is a status aid, not a formal proof of openness.
- Prior-art verdict: rediscovery was not established within the bounded audit. The canonical `2024` ladder paper remains the controlling source anchor, and the selected `L4` case still honestly appears open on this evidence.

## publication_statement_faithfulness
- The strongest honest current claim is not a solution of the selected yes-or-no theorem.
- What the artifact actually supports is narrower: a corrected equivalence between `L4`-subdivisions and extendable `L3` cores, together with a fixed-core terminal-cut observation.
- This is stronger than "here is an example" because it is a structural statement about every `L4`-subdivision, not a hand-picked host graph.
- The proof is structural rather than small-case enumeration, but it remains a setup lemma. It does not yet imply bounded hitting, `k` edge-disjoint `L4` subdivisions, or a counterexample family.
- Faithfulness verdict: the current packet stays on the exact selected problem, but its honest output is still a preparatory lemma package rather than the target theorem.

## publication_theorem_worthiness
- If the selected `paper_candidate` were fully solved, it would still be about `70-90%` of a short paper: the note would have a clean headline theorem, immediate context from `L3` positive and `L14+` negative, and low packaging overhead.
- The current artifact is not there. There is not yet a referee-facing theorem slice answering "what is the theorem?" in a way that would justify a standalone note.
- A real slice target does exist: a bounded-interface / uncrossing / representative-core theorem for extendable `L3` cores would be a publishable theorem slice because it would directly attack the publication-critical globalization step.
- The presently proved reduction is too local to count as that slice. It is close to an organizing rephrasing of "`L4` is `L3` plus one extra cell" plus a local cut fact, not yet a theorem that materially shortens the path to publication on its own.
- The claim is not overly dependent on hand-picked small cases; the weakness is not instance-chasing but the absence of the global packing/hitting theorem.
- Theorem-worthiness verdict: the strongest honest claim is a useful structural lemma, but not yet a paper-grade theorem slice. Conservative publication status therefore stays below `SLICE_CANDIDATE`.

## publication_publishability
- The selected target itself still looks publication-worthy if solved cleanly; the audit did not discover a rediscovery or a hidden feeder ladder requirement.
- The remaining gap is not merely polish. The missing globalization step is still the actual theorem, so the candidate looked closer before audit than it does after audit.
- A referee would still ask "what is the theorem?" and the present packet would have to answer with the unresolved bounded-interface theorem, not with the corrected reduction already on disk.
- There is no parameterized theorem or counterexample theorem closed yet. The packet therefore is not `PAPER_READY`, not `SLICE_EXACT`, and not even honestly `SLICE_CANDIDATE` on current evidence.
- Lean would not directly seal the publication packet here. Formalizing the corrected reduction would only archive a local lemma; the shortest remaining route is still combinatorial, either through a genuine globalization theorem or through an explicit non-condensed-wall counterexample family.

## publication_packet_audit
- Packet quality after audit: the target remains strong, but the current proof packet is weak.
- Strongest honest packet content:
  - exact prior-art anchor at the `2024` Steck-Ulmer paper with no bounded-audit rediscovery found,
  - corrected `L4 <=>` extendable `L3` reduction,
  - fixed-core terminal-cut observation,
  - explicit identification of the missing globalization step.
- What is missing for a referee-facing packet:
  - either a theorem giving bounded hitting or packing from many extendable `L3` cores,
  - or an explicit counterexample family showing that such globalization fails already at `L4`.
- Publication packet verdict: promising target, but current packet is still scaffolding rather than a near-sealed theorem note.

## strongest_honest_claim
- After skeptical repair and bounded prior-art audit, the strongest honest claim is: every `L4`-subdivision is equivalent to an extendable `L3` core with a terminal extension path of length at least `3`, and for any fixed such core, any edge cut separating the terminal rung endpoints in `G - E(K)` hits all extensions through that interface.
- This is a real structural claim and stronger than an example, but it does not yet settle the edge-Erdos-Posa property for `L4` and does not yet produce a referee-facing theorem slice.

## paper_title_hint
- `Extendable 3-rung cores and the 4-rung ladder edge-Erdos-Posa problem`

## next_action
- Return to `solve` / `generalize` with the publication claim locked conservatively.
- Primary target: prove a one-sided bounded-interface or uncrossing theorem for extendable `L3` cores that genuinely yields bounded hitting or `k` edge-disjoint `L4` subdivisions.
- Fallback target if the positive route stalls: construct an explicit non-condensed-wall counterexample family whose `L4` models necessarily use many incomparable extendable cores, so the failure mechanism itself becomes the theorem.
