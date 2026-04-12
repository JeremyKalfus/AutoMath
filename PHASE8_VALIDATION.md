# Phase 8 Validation

Validation date: `2026-04-12`

This note validates the one-shot publication redesign against the Phase 8 checks in
`ONE_SHOT_PUBLICATION_REDESIGN_PLAN.md`.

It is intentionally conservative. The goal is to record what the repo state already
supports, not to claim that the redesign is fully vindicated before a real one-shot
paper win exists.

## Baseline

- Verified repo state before validation:
  - `git status --short` clean
  - `HEAD == origin/main`
  - current redesign landing includes Phase 7 commit `dad1fc5`
- Active selected candidate:
  - `cocktail-party-two-monochromatic-diameter-2-cover`
- Current queue shape:
  - 5 of 5 entries are `paper_candidate`
- Current strongest publication status in the repo summary:
  - `SLICE_EXACT`
  - this still comes from the legacy warm family campaign `zero_divisor_prime_labelings`, not from a new one-shot paper win

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
  - 5 `paper_candidate`
  - 0 `family_campaign`
  - 0 `feeder_instance`

Current queued scores:
- `cocktail-party-two-monochromatic-diameter-2-cover`
  - `publication_if_solved_score = standalone_short_paper`
  - `solve_to_publication_distance = tiny`
  - `publication_packet_quality = excellent`
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

## Check 29: Runtime Behavior Changes In The Expected Direction

Status: `PASS`

Evidence from `ledger.md`:
- the redesigned runtime explicitly recorded:
  - `Queue had no usable paper_candidate, so one-shot publication curation started.`
  - `Publication mode selected one-shot paper candidate forbidden-outdegree-orientation-d7 instead of silently preferring a warm family campaign.`

What this shows:
- the manager now prefers the one-shot lane when usable paper candidates are available
- it does not silently default back to the old warm-campaign behavior
- when the first redesigned paper candidate failed verification, it was honestly reclassified as `REDISCOVERY` rather than being padded into a fake publication win

Important limitation:
- the repo still contains strong legacy family infrastructure and family summaries
- the strongest current publication status in `artifacts/families/summary.md` still comes from the old zero-divisor campaign
- so the redesign has changed queueing and selection behavior more strongly than it has changed the top-line “strongest claim in repo” headline

## Check 30: Before Solving, The Top Candidate Already Looks Like Most Of A Paper

Status: `PASS`

Evidence in the current selection surfaces:
- `selected_problem.md` for `cocktail-party-two-monochromatic-diameter-2-cover` already records:
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

## Check 31: First End-To-End Win Really Looks Like A Paper Packet

Status: `OPEN`

Honest state:
- there is not yet a new end-to-end one-shot win under the redesign that reaches `publication_status = PAPER_READY`
- the first redesigned one-shot attempt visible in the ledger, `forbidden-outdegree-orientation-d7`, did not become such a win
- instead it was honestly downgraded during verify:
  - the bipartite slice was already known
  - the claimed nonbipartite slice failed on a false bridge argument
  - final artifact status became `REDISCOVERY`

Why this is still useful:
- this is evidence that the redesigned harness can reject an attractive-looking candidate honestly
- but it is not yet evidence that the redesign has produced its first true paper packet

What remains to validate Check 31:
- one redesigned `paper_candidate` must complete solve, verify, and publication audit in a way that leaves only writeup or direct packet sealing
- until that happens, Phase 8 is only partially complete overall

## Overall Judgment

Current Phase 8 outcome: `PASS_WITH_ONE_OPEN_SUCCESS_CRITERION`

What is validated:
- the queue now strongly prefers one-shot paper candidates
- the runtime has demonstrated one-shot selection behavior
- the new packet surfaces explain the publication case before solving
- exact instances and feeder-heavy history are no longer dominating active selection

What is not yet validated:
- a full redesigned end-to-end one-shot paper win

## Minimal Continuation Point

The smallest honest next move after this validation is:

1. keep the redesigned one-shot queue active
2. continue solving from the current top packetized candidate
3. treat the first genuine one-shot `PAPER_READY` result as the closing evidence for Check 31
