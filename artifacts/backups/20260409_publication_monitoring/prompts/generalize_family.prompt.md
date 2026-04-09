Read `AGENTS.md` and `selected_problem.md` first.

This is the GENERALIZE stage.
Default: do NOT browse the internet.
Limited web is allowed only if the campaign dossier does not cleanly preserve the exact family statement you need.

Purpose:
Take one active family campaign plus the relevant exact proofs / partials / counterexamples and try to turn them into:

- a theorem slice
- a family theorem
- or a publishable counterexample theorem

Before doing anything substantial:

1. Detect the active `family_slug`, dossier path, and family artifact path from `selected_problem.md`.
2. Read the campaign dossier first.
3. Read the relevant exact-instance or partial artifacts named there.
4. Read `PROOFS.md` if the dossier uses Lean-backed exact seeds.

Bounded-read policy:

- Stay local unless the dossier itself is insufficient to reconstruct the family statement.
- Read the dossier, the current family record/status, `PROOFS.md`, and only the most relevant seed artifacts.
- Target 4 to 6 seed artifacts; hard cap 10 opened artifacts unless you are forced to inspect one more discriminator.
- Use `rg` or equivalent local search to jump to exact sections instead of roaming through whole files.
- Once you can fill the required sections honestly, stop exploring and write the family outputs immediately.
- Write `record.md` and `status.json` before any closing message.

Work in this order:

1. Lock the family statement and the current theorem target.
2. Build the exact instance inventory from the dossier and seed artifacts.
3. Extract the shared proof template.
4. Separate genuinely scalable steps from instance-specific tricks.
5. Propose several theorem slices or counterexample-slice claims.
6. Choose the strongest honest slice.
7. Give one main proof path and one fallback path.
8. If the slice still does not close, choose the smallest next feeder instances that would maximally discriminate between competing templates.

You must explicitly identify:

- the common decomposition / invariant / construction
- which steps genuinely scale in the parameters
- which steps are instance-specific
- the strongest plausible theorem slice
- the smallest likely counterexample or obstruction

Write durable outputs under:

- `artifacts/families/<family_slug>/record.md`
- `artifacts/families/<family_slug>/status.json`

Required sections in `record.md`:

- `family_statement_lock`
- `existing_instance_inventory`
- `shared_structure`
- `parameter_sensitive_steps`
- `candidate_theorem_slices`
- `chosen_slice`
- `proof_plan`
- `fallback_counterexample_plan`
- `next_best_feeder_instances`
- `publication_value`

Required output content:

- a proposed theorem slice
- a proof plan
- reusable lemmas
- one strongest path forward
- one fallback path

If you cannot prove a theorem slice, you must still output:

- the best generalized conjecture/template
- the smallest next feeder instance or two that would maximally discriminate between competing templates

Status policy for `status.json`:

- `entry_type`
- `family_slug`
- `family_name`
- `stage = "generalize"`
- `classification`
- `publication_status`
- `publication_confidence`
- `strongest_honest_claim`
- `paper_title_hint`
- `lean_ready`
- `lean_complete`
- `next_action`
- `proof_artifacts_preserved`

Publication-status guidance:

- isolated theorem-template observations only: `INSTANCE_ONLY` or `NONE`
- clean but not fully closed theorem slice: `SLICE_CANDIDATE`
- strong family-level conjectural path with evidence but no closure: `FAMILY_CANDIDATE`
- fully closed nontrivial slice with honest proof support: `SLICE_EXACT`
- use `PAPER_READY` only if the strongest honest claim now looks genuinely publishable

Do not overclaim.
Generalization is the default next step once a family campaign is active.
