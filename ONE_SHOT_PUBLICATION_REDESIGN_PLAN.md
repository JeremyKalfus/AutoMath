# One-Shot Publication Redesign Plan

## Objective

Redesign AutoMath so it optimizes for:

`the smallest frontier claim where a single strong solve is already 70-90% of a paper`

This is not the same as:

- finding mathematically interesting families,
- building long feeder ladders,
- or accumulating many exact instances that still require substantial packaging work.

The new default target is:

- as small as possible without becoming trivia-shaped,
- frontier enough to matter,
- exact enough to verify and Lean-seal honestly,
- and immediately paper-shaped if solved.

Call this the MICRO-PAPER objective:

- one clean solve should already look like the title theorem of a short note
- the remaining work should mostly be framing, writeup polish, Lean sealing, and maybe one or two immediate corollaries
- the system should reject tiny exact curiosities that still need a second research program before they become paper-worthy

## Hard Guardrails

These are explicit constraints, not suggestions.

### No Silent Fallbacks

If something does not work, AutoMath must not silently fall back to:

- broad curation,
- family-campaign mode,
- feeder-ladder mode,
- alternate publication criteria,
- or any other substitute objective.

If the intended approach fails, the system should:

1. stop that path,
2. record the blocker clearly,
3. preserve any useful artifacts,
4. and wait for the manager or user to choose the next move.

There should be no automatic "well, this did not work, so now we will do something conceptually different instead."

### No Unapproved Concept Drift

AutoMath must not make big concept-altering decisions that were not explicitly specified by the user without first informing the user.

Examples of forbidden silent concept drift:

- changing the top-level objective,
- redefining what counts as publication success,
- changing the stop condition,
- switching from one-shot publication hunting back to campaign-first behavior,
- introducing a new problem class that changes the mission,
- deciding on a different notion of novelty or publishability,
- broadening or narrowing the theorem target in a way that changes the paper shape.

Small tactical decisions are allowed.
Big conceptual decisions require an explicit pause and user-facing notice.

## Working Definition Of Success

The main optimization target is no longer "easy to solve mathematically."
It is:

`easy to publish once solved`

That means the best candidates are things where a single solve would already yield one of:

- an exact theorem/result pair,
- a sharp obstruction theorem,
- a minimal counterexample,
- a tiny structural theorem with immediate application,
- a method note with a tiny theorem core and one or two direct applications.

Anything that requires a long feeder ladder before becoming paper-shaped should be downranked heavily.

## Core Redesign Principles

1. Curation should optimize for `solve -> publication distance`, not just solve difficulty.
2. Any problem that needs a feeder ladder before it becomes paper-shaped should be downranked hard.
3. Any campaign that keeps producing solved feeders without shrinking the final publication gap should be deprioritized.
4. "Family theorem potential" should stop dominating unless the family theorem is already very close.
5. The best targets should be exact theorem/result pairs, sharp obstructions, minimal counterexamples, or tiny structural lemmas with immediate applications.
6. If solving a problem does not already put the project most of the way to a paper, that problem is probably not a top-priority target.

## Plan

### Phase 0: Safe Pause And Preservation

1. Pause the live manager and preserve the current repo state.
   Success check: the background run is stopped cleanly, active worktrees are accounted for, and there is one preserved checkpoint before redesign work starts.

2. Snapshot the current operating assumptions.
   Success check: there is a short written baseline of what the old system optimized for, what it did well, and why it no longer matches the updated objective.

### Phase 1: Objective Rewrite

3. Rewrite the source-of-truth objective in [AGENTS.md](/Users/jeremykalfus/CodingProjects/AutoMath/AGENTS.md).
   Success check: the written default is one-shot publication distance, not campaign-first family growth.

4. Rewrite the curation prompt and scheduler comments so the new objective appears everywhere the system makes selection decisions.
   Files likely touched:
   - [prompts/curate_batch.prompt.md](/Users/jeremykalfus/CodingProjects/AutoMath/prompts/curate_batch.prompt.md)
   - [scripts/automath_cycle.py](/Users/jeremykalfus/CodingProjects/AutoMath/scripts/automath_cycle.py)
   Success check: no prompt still implies that feeder-rich family programs are the default best targets.

5. Add the hard guardrails above to the operational instructions.
   Success check: no silent fallback behavior and no unapproved concept drift are documented as explicit policy.

### Phase 2: Curation Rubric Replacement

6. Replace the current selection rubric with a publication-distance rubric.
   Every candidate should expose:
   - `publication_if_solved`
   - `solve_to_publication_distance`
   - `single_pass_proof_plausibility`
   - `novelty_check_cost`
   - `formalization_overhead`
   - `paper_shape`
   - `needs_feeder_ladder`
   - `packaging_risk`
   - `paper_leverage_score`
   - `single_solve_to_paper_fraction`
   - `title_theorem_strength`
   - `family_anchor_strength`
   - `publication_narrative_strength`
   - `editorial_overhead`
   - `immediate_corollary_headroom`
   - `isolated_exact_case_risk`
   - `broader_theorem_implication_risk`
   - `search_heavy`
   - `certificate_compactness`
   - `transfer_kit_present`
   - `exact_gap_from_source`
   - `micro_paper_lane_eligible`
   Success check: the top-ranked queue entries are obviously "paper if solved" rather than "interesting if extended."

7. Introduce a new top-level candidate type: `paper_candidate`.
   Meaning:
   - exact theorem/result pair,
   - sharp obstruction,
   - minimal counterexample,
   - or tiny structural theorem with immediate application.
   Success check: the system can choose a publishable one-shot target without forcing it through campaign machinery.

8. Add a strict pre-solve gate:
   "If solved, would this already be 70-90% of a paper?"
   Success check: candidates that fail this gate are rejected or heavily downranked before solve starts.

9. Add a transfer-kit requirement for every micro-paper candidate.
   Each packet must already contain:
   - 2 to 4 usable lemmas / proof ingredients
   - 1 toy worked example
   - 1 known obstruction or failure mode
   - 1 exact sentence saying where prior work stops
   - 1 recommended first attack
   - 1 sentence saying what the paper would look like if solved
   Success check: the solver starts with a paper-shaped packet, not just a bare statement.

### Phase 3: Scheduler Redesign

9. Split the pipeline into two modes, with one-shot publication mode as the default.
   Default mode:
   - curate
   - bounded novelty check
   - solve
   - verify
   - publication audit
   - Lean only if it directly seals the packet
   Secondary mode:
   - campaign mode, only when a family theorem is already visibly near closure
   Success check: most fresh runs enter the one-shot lane, not the campaign lane.

10. Add hard time caps per candidate.
   Policy:
   - one bounded solve pass,
   - one verify pass,
   - one publication audit pass,
   - optional Lean pass only if it directly closes the packet.
   Success check: no single candidate consumes long wall-clock time unless publication distance is clearly collapsing.

11. Penalize repeated solved feeders that do not reduce paper distance.
   Success check: the scheduler stops treating "more feeder evidence" as progress when the paper gap is unchanged.

12. Remove automatic preference for long-horizon family generalization unless the family theorem is one or two explicit lemmas from closure.
   Success check: warm campaigns no longer dominate simply because they already have momentum.

### Phase 4: Publication Packet First

13. Create a "publication packet" requirement before major effort is spent.
   Each serious candidate should have:
   - exact statement,
   - why it is frontier,
   - why solving it is near-publication,
   - likely title,
   - minimal literature surface,
   - minimal artifact requirements.
   Success check: the system can justify the candidate as a near-paper before solving it.

14. Make publication packet quality a first-class score.
   Success check: a small crisp result with a short referee path outranks a richer but slower family program.

15. Add a narrow one-shot publication audit.
   Required checks:
   - exact statement search,
   - alternate notation search,
   - canonical source check,
   - one outside-source status pass.
   Success check: novelty validation is cheap enough that it does not dominate runtime.

### Phase 5: Lean Repositioning

16. Reposition Lean as a packet-sealing tool, not an exploration driver.
   Success check: candidates are not selected because they are Lean-friendly unless Lean would directly finish publication.

17. For one-shot candidates, Lean should only be used if it is the shortest path from "solved" to "paper-ready artifact."
   Success check: the system does not sink time into formalization for candidates that are not already almost publishable.

### Phase 6: Subagents

18. Use subagents only in narrow, role-locked ways.
   Roles:
   - `curation-scout`: find a few one-shot paper candidates
   - `novelty-scout`: bounded rediscovery check on one candidate
   - `solver-A`: direct solve attempt
   - `solver-B`: alternate solve attempt
   - `packet-auditor`: theorem/result/title/claim language for the winning candidate
   Success check: no subagent is asked to absorb the whole repo or wander across unrelated campaigns.

19. Enforce one write-owner per artifact.
   Rules:
   - manager owns canonical queue and status files,
   - solver subagents write only candidate-local sidecar artifacts,
   - packet-auditor writes only publication-packet files.
   Success check: no merge conflicts and no accidental mutation of canonical state.

20. Require short handoff memos instead of full context cloning whenever possible.
   Each memo should include:
   - exact statement,
   - why publishable if solved,
   - allowed files,
   - stop condition,
   - output path.
   Success check: subagent context stays small and precise.

21. Cap subagent context aggressively.
   Default budget:
   - 1 candidate,
   - 1 dossier,
   - 3-6 source files,
   - 1 explicit output file.
   Success check: subagents do not burn tokens rereading broad campaign history.

22. Discard subagent outputs that do not shorten solve-to-publication distance.
   Success check: "interesting but not paper-near" ideas do not metastasize into new campaigns.

### Phase 7: Context Hygiene

23. Create candidate-local working packets.
   Each top candidate gets a tiny packet containing:
   - statement,
   - novelty notes,
   - proof sketch,
   - likely paper shape,
   - bounded source list.
   Success check: most work can proceed without reopening broad repo context.

24. Keep canonical repo memory thin.
   Canonical memory should store:
   - wins,
   - losses,
   - publication packets,
   - short reasons.
   Success check: future runs can orient fast without replaying huge ledgers.

25. Separate search memory from paper memory.
   Search memory:
   - what was tried,
   - why it was rejected.
   Paper memory:
   - what is already nearly publishable.
   Success check: promising one-shot candidates are not buried under campaign bookkeeping.

26. Add strict read budgets to prompts.
   Success check: solve and audit passes do not drift into broad repo absorption.

### Phase 8: Validation

27. Run an A/B calibration on existing repo history.
   Test:
   - which old targets would have been selected under the new rubric,
   - which current campaigns would have been downranked,
   - which existing exacts were actually near-paper candidates.
   Success check: the new policy clearly prefers "easy to publish" over "easy to extend."

28. Verify that queue contents change in the expected direction.
   Success check: top queue slots are dominated by `paper_candidate` items, not feeder ladders.

29. Verify that runtime behavior changes in the expected direction.
   Success check: the system spends more time on distinct small paper-near targets and less time on repeated packaging loops.

30. Verify that the first redesigned dry run can explain, before solving, why the top candidate is already most of a paper if solved.
   Success check: AutoMath can articulate the exact publication case upfront.

31. Verify that the first end-to-end win under the redesign really looks like a paper packet.
   Success check: after solving, the remaining work is mostly writeup and sealing, not major new mathematics.

## Anti-Goals

AutoMath should reject or heavily penalize:

- problems that need many feeders before becoming paper-shaped,
- broad family campaigns with expensive packaging,
- exact instances that are easy to solve but expensive to publish,
- results with fuzzy novelty surfaces,
- family programs where the theorem still depends on multiple unresolved structural steps.

## Immediate Execution Order

When implementation starts, the recommended order is:

1. pause and preserve the current manager state,
2. rewrite objective and guardrails,
3. replace the curation rubric,
4. redesign the scheduler gates,
5. create the `paper_candidate` fast path,
6. tighten subagent roles and context budgets,
7. validate on old repo history,
8. only then relaunch AutoMath under the new policy.

## Success Criterion

The redesign is successful when AutoMath systematically prefers:

`small, frontier, low-literature-surface problems where one strong solve is already most of a paper`

and systematically rejects:

`mathematically tractable problems whose publication path still requires long campaign growth after the solve`
