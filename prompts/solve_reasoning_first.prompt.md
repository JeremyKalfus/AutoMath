Read `AGENTS.md` and `selected_problem.md` first.

This is the SOLVE stage.
Do NOT browse the internet.
Treat this like a hard competition-style math problem. Solve or disprove it if you can. Do not search the internet.

Goal:
Produce the best reasoning-first attempt on the active problem, with minimal code.

First determine the active slug and title from `selected_problem.md`.
Create `artifacts/<slug>/` if missing.

Use these files:
- `artifacts/<slug>/record.md`
- `artifacts/<slug>/status.json`
- `artifacts/<slug>/lean/` (only if needed later)

Work in this order:

1. Lock the exact intended statement.
2. List any ambiguities, conventions, or missing definitions.
3. Write at least 2 reasoning approaches:
   - one structural / invariant approach
   - one construction / extremal / contradiction approach
4. Write a small lemma graph or proof skeleton.
5. Choose the best path and attempt a rigorous solution or disproof.
6. After each major step, add a brief self-check.
7. Only then decide whether minimal code is actually needed.

Code policy:
- default: no code
- allowed code only for:
  - checker
  - falsifier / counterexample search
  - tiny bounded experiment
  - witness verification
  - later exact search IF the reasoning stage already justified it
- keep code short and directly tied to a specific hypothesis
- do not start with generic optimization / SAT / ILP / CP-SAT / brute force unless:
  - the dossier explicitly marks the problem `search-heavy`, OR
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
- `likely_failure_points`
- `what_verify_should_check`

In `status.json`, keep at least these keys:
- `slug`
- `title`
- `stage`
- `classification`
- `confidence`
- `code_used`
- `lean_ready`
- `lean_complete`
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

Lean should stay OFF here unless you already have a strong exact candidate or exact disproof.
In this stage, the strongest positive proof classification is `CANDIDATE`; do not use `EXACT` before Lean completes.
Solve itself should almost never assign `REDISCOVERY`, because solve runs with web disabled.
If the dossier already carries strong prior-art risk, be conservative and avoid claiming `EXACT`.

Be conservative.
If you are not confident, use `PARTIAL`, `FAILED`, or `VARIANT`.
