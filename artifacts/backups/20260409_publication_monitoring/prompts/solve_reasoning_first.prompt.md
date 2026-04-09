Read `AGENTS.md` and `selected_problem.md` first.

This is the SOLVE stage.
Do NOT browse the internet.

Goal:
Produce the best reasoning-first attempt on the active feeder instance, with minimal code, while also extracting reusable structure for publication-mode generalization.

First determine the active slug and title from `selected_problem.md`.
Create `artifacts/<slug>/` if missing.

Use these files:

- `artifacts/<slug>/record.md`
- `artifacts/<slug>/status.json`
- `artifacts/<slug>/lean/` only if needed later

Work in this order:

1. Lock the exact intended statement.
2. List ambiguities, conventions, or missing definitions.
3. Write at least 2 reasoning approaches:
   - one structural / invariant approach
   - one construction / extremal / contradiction approach
4. Write a small lemma graph or proof skeleton.
5. Choose the best path and attempt a rigorous solution or disproof.
6. After each major step, add a brief self-check.
7. Only then decide whether minimal code is actually needed.
8. After any strong result, extract what part of the argument scales.

Code policy:

- default: no code
- allowed code only for:
  - checker
  - falsifier / counterexample search
  - tiny bounded experiment
  - witness verification
  - later exact search if the reasoning stage already justified it
- do not start with generic optimization / SAT / ILP / CP-SAT / brute force unless:
  - the dossier explicitly marks the problem `search-heavy`, or
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
- `likely_failure_points`
- `what_verify_should_check`

Mandatory publication-aware outputs:

- `family_affinity`
- `generalization_signal`
- `proof_template_reuse`
- `candidate_theorem_slice`
- `smallest_param_shift_to_test`

After any strong exact or counterexample result, you must say:

- what part of the argument scales
- what part does not
- what theorem slice is suggested
- what one or two next feeder instances would help most

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
- partial but obviously campaign-relevant structural package: `SLICE_CANDIDATE` only if a real theorem slice is visible
- otherwise use `NONE`

Lean should stay off here unless you already have a strong exact candidate or exact disproof.
In this stage, the strongest positive proof classification is `CANDIDATE`; do not use `EXACT` before Lean completes.
Solve itself should almost never assign `REDISCOVERY`, because solve runs with web disabled.

Be conservative.
