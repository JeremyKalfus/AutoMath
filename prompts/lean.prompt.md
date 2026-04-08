Read `AGENTS.md`, `selected_problem.md`, `artifacts/<slug>/record.md`, and `artifacts/<slug>/status.json` first.

This is the LEAN stage.
Do NOT browse the internet.

Only continue if the verified result is strong enough to formalize and the current classification is not `REDISCOVERY`.

Goal:
Formalize the EXACT intended statement, not a proxy.

Rules:
- use the existing `lean/` AutoMath project as the official Lean/Lake backend when it exists
- keep the problem-specific Lean source mirrored under `artifacts/<slug>/lean/`
- start with the exact theorem statement
- then write a proof skeleton
- then try a full proof only if feasible
- do not introduce new axioms
- do not use `sorry`, `admit`, or placeholders in the final claimed proof
- if Lean is available, run the build/check commands needed to confirm the file really checks, including `lake build`, a `#print axioms` audit for the target theorem, and `lean4checker --fresh` if it is available
- audit the theorem for faithfulness to the intended statement
- audit for hidden axioms / `sorryAx` if possible
- if blocked, leave the best exact statement and proof skeleton you can

Write under:
- `artifacts/<slug>/lean/`

Append to `artifacts/<slug>/record.md`:
- `lean_statement`
- `lean_skeleton`
- `lean_result`
- `lean_blockers`

Update `artifacts/<slug>/status.json` with:
- `stage = "lean"`
- `lean_ready`
- `lean_complete`
- `classification`
- `confidence`
- `next_action`

Stop condition:
- set `classification = "EXACT"` and `lean_complete = true` ONLY if the exact intended statement is fully formalized and checked
- otherwise keep the run at `CANDIDATE` if the mathematics still looks strong
- otherwise be conservative
