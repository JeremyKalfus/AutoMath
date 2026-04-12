# Phase 8 Validation

Validation date: `2026-04-12`

This note validates the one-shot publication redesign against the Phase 8 checks in
`ONE_SHOT_PUBLICATION_REDESIGN_PLAN.md`.

It is intentionally conservative. The goal is to record what the repo state already
supports, not to claim that the redesign is fully vindicated before a real one-shot
paper win exists.

## Baseline

- Verified checkpoint before continuation:
  - `HEAD == origin/main == 227b517`
  - the repo was clean before the continuation run
  - the redesign landing already included the Phase 7 context-hygiene work
- Actual redesigned dry run now executed:
  - `scripts/automath_cycle.py --mode publication`
  - selected candidate: `cocktail-party-two-monochromatic-diameter-2-cover`
  - end state: candidate archived honestly as `VARIANT` with candidate-local `publication_status = SLICE_EXACT`
- Current queue shape after that dry run:
  - 4 of 4 remaining entries are `paper_candidate`
  - next queued candidate is `ladder-4-rungs-edge-erdos-posa`
- Current strongest publication status in the repo summary:
  - `SLICE_EXACT`
  - this still comes from the legacy warm family campaign `zero_divisor_prime_labelings`, not from a new redesigned one-shot `PAPER_READY` win

## Check 27: A/B Calibration On Existing Repo History

Status: `PASS`

Question:
- does the redesigned policy prefer easy-to-publish targets over the older stock of easy-to-extend campaign work?

Evidence from repo history:
- `failed_problems.json` currently has 88 archived items.
- Its broad historical mix is dominated by campaign-style and feeder-style work:
  - `zero_divisor`: 34 archived slugs
  - `dsrg`: 17 archived slugs
  - `cnbc`: 4 archived slugs
  - `prime_labeling`: 3 archived slugs
- Reason distribution in `failed_problems.json`:
  - `LEGACY_STRING`: 47
  - `CANDIDATE`: 26
  - `EXACT`: 9
  - `REDISCOVERY`: 6

Calibration conclusion:
- under the old regime, a large amount of repo energy accumulated in feeder-heavy families, archived campaign attempts, and exact instances that were not already paper-shaped
- under the redesigned regime, those objects now live mainly in `failed_problems.json` and `memory/search_memory.json`, not in the active queue
- the current queue is instead populated by smallest-open-case and near-paper finite-slice targets

Which old targets would now be downranked:
- repeated zero-divisor feeder instances whose solve does not itself yield a paper
- dsrg existence/nonexistence one-offs that still require broader packaging after the solve
- exact prime-labeling instances that are mathematically closed but not obviously paper-shaped on their own

Which old exacts look non-near-paper under the new rubric:
- all current `EXACT` entries archived in `failed_problems.json` have `publication_status = null`
- that matches the redesign rule that an exact instance alone is not automatically a one-shot publication packet

What the redesign now prefers instead:
- `cocktail-party-two-monochromatic-diameter-2-cover`
- `ladder-4-rungs-edge-erdos-posa`
- `order-12-9-regular-one-factorization`
- `eight-regular-forbidden-outdegree-three-set`
- `all-9-vertex-graphs-1-11-representable`

These are all narrow theorem/result targets where the queue already records short publication distance and an explicit paper shape.

## Check 28: Queue Contents Change In The Expected Direction

Status: `PASS`

Evidence:
- `queue.json` currently contains:
  - 4 `paper_candidate`
  - 0 `family_campaign`
  - 0 `feeder_instance`

Current queued scores:
- `ladder-4-rungs-edge-erdos-posa`
  - `publication_if_solved_score = standalone_short_paper`
  - `solve_to_publication_distance = tiny`
  - `publication_packet_quality = excellent`
- `order-12-9-regular-one-factorization`
  - `publication_if_solved_score = standalone_short_paper`
  - `solve_to_publication_distance = tiny`
  - `publication_packet_quality = strong`
- `eight-regular-forbidden-outdegree-three-set`
  - `publication_if_solved_score = paper_with_light_packaging`
  - `solve_to_publication_distance = short`
  - `publication_packet_quality = strong`
- `all-9-vertex-graphs-1-11-representable`
  - `publication_if_solved_score = paper_with_light_packaging`
  - `solve_to_publication_distance = short-medium`
  - `publication_packet_quality = strong`

Validation conclusion:
- the queue is now dominated by one-shot publication candidates exactly as intended
- feeder ladders and warm campaigns are not occupying the top slots by default
- the first queued cocktail-party packet was consumed by a real redesigned run and then removed honestly instead of lingering as fake active progress

## Check 29: Runtime Behavior Changes In The Expected Direction

Status: `PASS`

Evidence from `ledger.md`:
- the redesigned runtime explicitly recorded:
  - `Queue had no usable paper_candidate, so one-shot publication curation started.`
  - `Publication mode selected one-shot paper candidate forbidden-outdegree-orientation-d7 instead of silently preferring a warm family campaign.`
  - `Publication mode selected one-shot paper candidate cocktail-party-two-monochromatic-diameter-2-cover instead of silently preferring a warm family campaign.`
  - the cocktail-party candidate then ran through solve, verify, and publication audit before being moved aside as `VARIANT`

What this shows:
- the manager now prefers the one-shot lane when usable paper candidates are available
- it does not silently default back to the old warm-campaign behavior
- when the first redesigned paper candidate failed verification, it was honestly reclassified as `REDISCOVERY` rather than being padded into a fake publication win
- when the second redesigned paper candidate failed to close the full theorem, the system still preserved the strongest honest publication packet it actually earned instead of overstating the result

Important limitation:
- the repo still contains strong legacy family infrastructure and family summaries
- the strongest current publication status in `artifacts/families/summary.md` still comes from the old zero-divisor campaign
- so the redesign has changed queueing and selection behavior more strongly than it has changed the top-line “strongest claim in repo” headline

Runtime coherence fix applied during validation:
- the cocktail-party dry run exposed that archiving or rotating a queue entry could leave `selected_problem.md` pointing at the retired packet even after `queue.json` moved on
- it also exposed that `failed_problems.json` could preserve the pre-audit publication status instead of the final audited publication status
- `scripts/automath_cycle.py` is now patched so queue rotations/removals resync `selected_problem.md`, and post-audit archival records the final audited `publication_status`

## Check 30: Before Solving, The Top Candidate Already Looks Like Most Of A Paper

Status: `PASS`

Evidence from the first redesigned dry run:
- before solving, `selected_problem.md` for `cocktail-party-two-monochromatic-diameter-2-cover` already recorded:
  - `publication_if_solved`
  - `solve_to_publication_distance`
  - `pre_solve_gate = pass`
  - `publication_packet_quality = excellent`
  - `paper_shape`
- the candidate-local working packet at
  `artifacts/cocktail-party-two-monochromatic-diameter-2-cover/working_packet.md`
  already contains:
  - statement
  - novelty notes
  - proof sketch
  - likely paper shape
  - bounded source list

Validation conclusion:
- the current top candidate can already explain, before solving, why a solve would be most of a paper
- that is exactly the behavior Phase 8 wanted from the redesigned front end
- the next queued candidate, `ladder-4-rungs-edge-erdos-posa`, is now selected with the same packetized structure rather than reverting to campaign prose

## Check 31: First End-To-End Win Really Looks Like A Paper Packet

Status: `OPEN`

Honest state:
- there is not yet a new end-to-end one-shot win under the redesign that reaches `publication_status = PAPER_READY`
- the first redesigned one-shot attempt visible in the ledger, `forbidden-outdegree-orientation-d7`, did not become such a win
- instead it was honestly downgraded during verify:
  - the bipartite slice was already known
  - the claimed nonbipartite slice failed on a false bridge argument
  - final artifact status became `REDISCOVERY`
- the next redesigned dry run, `cocktail-party-two-monochromatic-diameter-2-cover`, also did not close the full conjecture
- however, unlike the `d = 7` case, it did leave a real publication-shaped fallback packet:
  - `stage = publication_audit`
  - `classification = VARIANT`
  - `publication_status = SLICE_EXACT`
  - `proof_artifacts_preserved = true`
  - strongest honest claim = exact empty-signature-class slice plus exact 6-vertex verification under the source-faithful reading

Why this is still useful:
- this is evidence that the redesigned harness can reject an attractive-looking candidate honestly
- it is also evidence that the redesigned harness can preserve a small exact publication slice produced during a failed one-shot attack, rather than collapsing everything into “attempt failed”
- but it is not yet evidence that the redesign has produced its first true paper packet

What remains to validate Check 31:
- one redesigned `paper_candidate` must complete solve, verify, and publication audit in a way that leaves only writeup or direct packet sealing
- the cocktail-party result still leaves major new mathematics on the locally saturated critical-pair case, so it is not yet close enough to count as that closing example

## Overall Judgment

Current Phase 8 outcome: `PASS_WITH_ONE_OPEN_SUCCESS_CRITERION`

What is validated:
- the queue now strongly prefers one-shot paper candidates
- the runtime has demonstrated one-shot selection behavior
- the new packet surfaces explain the publication case before solving
- the first redesigned full dry run produced an honest exact slice rather than an inflated theorem claim
- runtime coherence bugs surfaced by the dry run were small, concrete, and patched locally
- exact instances and feeder-heavy history are no longer dominating active selection

What is not yet validated:
- a full redesigned end-to-end one-shot paper win

## Minimal Continuation Point

The smallest honest next move after this validation is:

1. keep the redesigned one-shot queue active
2. continue solving from the current top packetized candidate `ladder-4-rungs-edge-erdos-posa`
3. treat the first genuine one-shot `PAPER_READY` result as the closing evidence for Check 31
