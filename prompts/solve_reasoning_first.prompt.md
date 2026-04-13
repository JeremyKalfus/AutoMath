Read `AGENTS.md` and `selected_problem.md` first.
If `selected_problem.md` includes `handoff_memo_path`, read that memo immediately after `selected_problem.md` and treat it as the binding scope authority for allowed files, stop condition, and output path.
If `selected_problem.md` includes `working_packet_path`, read that file immediately after `selected_problem.md`.

This is the SOLVE stage.
Do NOT browse the internet.

Goal:
Produce the best reasoning-first attempt on the active selected candidate, with minimal code, while keeping the MICRO-PAPER objective in view.

- If this is a `paper_candidate`, aim for the exact intended theorem or disproof plus the smallest amount of immediate supporting structure that makes the result paper-shaped.
- If this is a `feeder_instance`, extract only the family signal that materially shortens the path to publication.
- Do not settle for “some exact witness” if the result still lacks theorem shape.

First determine the active slug and title from `selected_problem.md`.
Create `artifacts/<slug>/` if missing.

Use these files:

- `artifacts/<slug>/record.md`
- `artifacts/<slug>/status.json`
- `artifacts/<slug>/lean/` only if needed later

Read budget:

- target 3 to 6 local files total after `selected_problem.md`
- hard cap 8 local files unless an exact blocker makes one more file unavoidable
- prefer the working packet, the local artifact record/status, and at most one or two supporting files
- do not reopen broad ledger history or unrelated artifact directories during solve

Sidecar attempt mode:

- if `selected_problem.md` includes `attempt_output_markdown` and `attempt_output_json`, treat this as a sidecar solver run
- read the canonical artifact `record.md` / `status.json` as inputs only
- if the sidecar output files already exist, continue from them instead of restarting from scratch
- write the durable solve record and solve status to those sidecar output paths instead of the canonical artifact files
- do not mutate canonical artifact files in this sidecar mode

Work in this order:

1. Lock the exact intended statement.
2. List ambiguities, conventions, or missing definitions.
3. Write at least 2 reasoning approaches:
   - one structural / invariant approach
   - one construction / extremal / contradiction approach
4. Write a small lemma graph or proof skeleton.
5. Explicitly ask: what extra structure would make this result paper-shaped if the main claim closes?
6. Choose the best path and attempt a rigorous solution or disproof.
7. After each major step, add a brief self-check.
8. Only then decide whether minimal code is actually needed.
9. After any strong result, extract the smallest supporting theorem slice, one natural corollary or boundary remark, and one exact sentence saying why the instance matters.

Code policy:

- default: no code
- allowed code only for:
  - checker
  - falsifier / counterexample search
  - tiny bounded experiment
  - witness verification
  - later exact search if the reasoning stage already justified it
- do not start with generic optimization / SAT / ILP / CP-SAT / brute force unless:
  - the dossier explicitly marks the problem `search_heavy`, or
  - two reasoning strategies have already failed

In `record.md`, use these sections:

- `statement_lock`
- `definitions`
- `approach_A`
- `approach_B`
- `lemma_graph`
- `chosen_plan`
- `self_checks`
- `code_used`
- `result`
- `family_affinity`
- `generalization_signal`
- `proof_template_reuse`
- `candidate_theorem_slice`
- `smallest_param_shift_to_test`
- `why_this_is_or_is_not_publishable`
- `paper_shape_support`
- `boundary_remark`
- `likely_failure_points`
- `what_verify_should_check`

Mandatory publication-aware outputs:

- `family_affinity`
- `generalization_signal`
- `proof_template_reuse`
- `candidate_theorem_slice`
- `smallest_param_shift_to_test`
- `why_this_is_or_is_not_publishable`
- `paper_shape_support`
- `boundary_remark`

If this is a `paper_candidate`, also make explicit:

- whether a successful solve would already be 70-90% of a paper
- what the exact title theorem would be
- what the minimal remaining packaging work would be
- what one immediate corollary or remark naturally falls out
- whether the current result is still too thin for the micro-paper lane

After any strong exact or counterexample result, you must say:

- what part of the argument scales
- what part does not
- what theorem slice is suggested
- what one or two next feeder instances would help most
- whether the current package is still just an instance or already closer to a paper-shaped claim

In `status.json`, keep at least these keys:

- `slug`
- `title`
- `stage`
- `classification`
- `confidence`
- `code_used`
- `lean_ready`
- `lean_complete`
- `publication_status`
- `publication_confidence`
- `single_solve_to_paper_fraction`
- `title_theorem_strength`
- `publication_narrative_strength`
- `micro_paper_assessment`
- `family_affinity`
- `generalization_signal`
- `candidate_theorem_slice`
- `next_action`

Allowed classifications:

- `NEW`
- `UNSUITED`
- `FAILED`
- `PARTIAL`
- `VARIANT`
- `CANDIDATE`
- `EXACT`
- `COUNTEREXAMPLE`
- `REDISCOVERY`

Publication-status guidance in solve:

- exact witness or disproof with no theorem closure yet: usually `INSTANCE_ONLY`
- partial but obviously theorem-facing structural package: `SLICE_CANDIDATE` only if a real theorem slice is visible
- otherwise use `NONE`

Lean should stay off here unless you already have a strong exact candidate or exact disproof.
In this stage, the strongest positive proof classification is `CANDIDATE`; do not use `EXACT` before Lean completes.
Solve itself should almost never assign `REDISCOVERY`, because solve runs with web disabled.

Be conservative.
