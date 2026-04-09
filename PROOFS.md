# AutoMath Proofs

This file is maintained by the LEAN stage of AutoMath.
When a candidate is upgraded to `EXACT`, the same Lean run should update or append that slug's section here before it finalizes `status.json`.

It records every AutoMath result that currently counts as a full success inside the harness:

- `classification = EXACT`
- `lean_complete = true`

Publication-mode note:

- this file remains the exact-instance inventory
- exact wins are preserved even when they are only feeder evidence
- `EXACT` alone is no longer a global stop condition
- each entry may still have `publication_status = INSTANCE_ONLY`

## Update Rule

- Keep exactly one section per solved slug using heading `## <slug>`.
- If a slug's section already exists, replace that section instead of duplicating it.
- Do not add rediscoveries, partials, variants, or non-Lean candidates.

## z3-z25-prime-zero-divisor-graph

- Title: `Is the zero-divisor graph Γ(Z_3 × Z_25) prime?`
- Exact statement: the zero-divisor graph `Γ(Z_3 × Z_25)` admits a prime labeling, meaning a bijection from its `34` vertices to `{1,2,...,34}` such that adjacent vertices receive coprime labels.
- Verify verdict: `VERIFIED`
- Publication status: `INSTANCE_ONLY`
- Lean completion date in repo state: `2026-04-08`
- Vertex count / label set size: `34`
- Completion note: Lean verified the exact instance in the AutoMath backend; the artifact is being preserved while external novelty review proceeds separately.
- Artifact directory: `artifacts/z3-z25-prime-zero-divisor-graph/`
- Record file: `artifacts/z3-z25-prime-zero-divisor-graph/record.md`
- Status file: `artifacts/z3-z25-prime-zero-divisor-graph/status.json`
- Lean backend file: `lean/AutoMath/Z3Z25.lean`
- Mirrored Lean file: `artifacts/z3-z25-prime-zero-divisor-graph/lean/Z3Z25.lean`
- Main Lean theorem: `AutoMath.Z3Z25.z3_z25_zeroDivisorGraph_prime`
- Explicit Lean theorem: `AutoMath.Z3Z25.z3_z25_zeroDivisorGraph_prime_explicit`
- Recorded axiom audit: only `[propext, Classical.choice, Quot.sound]`
- Extra Lean audit note: `lean4checker --fresh` was unavailable on this machine

## z5-z5-z3-prime-zero-divisor-graph

- Title: `Is the zero-divisor graph Γ(Z_5 × Z_5 × Z_3) prime?`
- Exact statement: the zero-divisor graph `Γ(Z_5 × Z_5 × Z_3)` admits a prime labeling, meaning a bijection from its `42` vertices to `{1,2,...,42}` such that adjacent vertices receive coprime labels.
- Verify verdict: `VERIFIED`
- Publication status: `INSTANCE_ONLY`
- Lean completion date in repo state: `2026-04-08`
- Vertex count / label set size: `42`
- Completion note: Lean verified the exact intended statement in the AutoMath backend; archived to avoid rerunning this solved instance.
- Artifact directory: `artifacts/z5-z5-z3-prime-zero-divisor-graph/`
- Record file: `artifacts/z5-z5-z3-prime-zero-divisor-graph/record.md`
- Status file: `artifacts/z5-z5-z3-prime-zero-divisor-graph/status.json`
- Lean backend file: `lean/AutoMath/Z5Z5Z3.lean`
- Mirrored Lean file: `artifacts/z5-z5-z3-prime-zero-divisor-graph/lean/AutoMath/Z5Z5Z3.lean`
- Axiom audit file: `artifacts/z5-z5-z3-prime-zero-divisor-graph/lean/AxiomAudit.lean`
- Main Lean theorem: `AutoMath.Z5Z5Z3.z5_z5_z3_zeroDivisorGraph_prime`
- Explicit Lean theorem: `AutoMath.Z5Z5Z3.z5_z5_z3_zeroDivisorGraph_prime_explicit`
- Recorded axiom audit: only `[propext, Classical.choice, Quot.sound]`
- Extra Lean audit note: `lean4checker --fresh` was unavailable on this machine

## z5-z25-prime-zero-divisor-graph

- Title: `Is the zero-divisor graph Γ(Z_5 × Z_25) prime?`
- Exact statement: the zero-divisor graph `Γ(Z_5 × Z_25)` admits a prime labeling, i.e. a bijection from its `44` vertices to `{1,2,...,44}` such that adjacent vertices receive coprime labels.
- Verify verdict: `VERIFIED`
- Publication status: `INSTANCE_ONLY`
- Lean completion date in repo state: `2026-04-08`
- Vertex count / label set size: `44`
- Completion note: Lean verified the exact intended statement in the AutoMath backend; archived to avoid rerunning this solved instance.
- Artifact directory: `artifacts/z5-z25-prime-zero-divisor-graph/`
- Record file: `artifacts/z5-z25-prime-zero-divisor-graph/record.md`
- Status file: `artifacts/z5-z25-prime-zero-divisor-graph/status.json`
- Lean backend file: `lean/AutoMath/Z5Z25.lean`
- Mirrored Lean file: `artifacts/z5-z25-prime-zero-divisor-graph/lean/Z5Z25.lean`
- Axiom audit file: `artifacts/z5-z25-prime-zero-divisor-graph/lean/Z5Z25AxiomAudit.lean`
- Main Lean theorem: `AutoMath.Z5Z25.z5_z25_zeroDivisorGraph_prime`
- Explicit Lean theorem: `AutoMath.Z5Z25.z5_z25_zeroDivisorGraph_prime_explicit`
- Recorded axiom audit: only `[propext, Classical.choice, Quot.sound]`
- Extra Lean audit note: `lean4checker --fresh` was unavailable on this machine

## z2-power-8-prime-zero-divisor-graph

- Title: `Is the zero-divisor graph Γ(Z_2^8) prime?`
- Exact statement: the zero-divisor graph `Γ(Z_2^8)` admits a prime labeling, i.e. a bijection from its `254` vertices to `{1,2,...,254}` such that adjacent vertices receive coprime labels.
- Verify verdict: `VERIFIED`
- Publication status: `INSTANCE_ONLY`
- Lean completion date in repo state: `2026-04-08`
- Vertex count / label set size: `254`
- Completion note: Lean verified the exact intended statement in the AutoMath backend; archived to avoid rerunning this solved instance.
- Artifact directory: `artifacts/z2-power-8-prime-zero-divisor-graph/`
- Record file: `artifacts/z2-power-8-prime-zero-divisor-graph/record.md`
- Status file: `artifacts/z2-power-8-prime-zero-divisor-graph/status.json`
- Lean backend file: `lean/AutoMath/Z2Power8.lean`
- Mirrored Lean file: `artifacts/z2-power-8-prime-zero-divisor-graph/lean/AutoMath/Z2Power8.lean`
- Axiom audit file: `artifacts/z2-power-8-prime-zero-divisor-graph/lean/AxiomAudit.lean`
- Main Lean theorem: `AutoMath.Z2Power8.z2_power_8_zeroDivisorGraph_prime`
- Explicit Lean theorem: `AutoMath.Z2Power8.z2_power_8_zeroDivisorGraph_prime_explicit`
- Recorded axiom audit: only `[propext, Classical.choice, Quot.sound]`

## z5-z5-z2-prime-zero-divisor-graph

- Title: `Is the zero-divisor graph Γ(Z_5 × Z_5 × Z_2) prime?`
- Exact statement: the zero-divisor graph `Γ(Z_5 × Z_5 × Z_2)` admits a prime labeling, i.e. a bijection from its `33` vertices to `{1,2,...,33}` such that adjacent vertices receive coprime labels.
- Verify verdict: `VERIFIED`
- Publication status: `INSTANCE_ONLY`
- Lean completion date in repo state: `2026-04-08`
- Vertex count / label set size: `33`
- Completion note: Lean verified the exact intended statement in the AutoMath backend; archived to avoid rerunning this solved instance.
- Artifact directory: `artifacts/z5-z5-z2-prime-zero-divisor-graph/`
- Record file: `artifacts/z5-z5-z2-prime-zero-divisor-graph/record.md`
- Status file: `artifacts/z5-z5-z2-prime-zero-divisor-graph/status.json`
- Lean backend file: `lean/AutoMath/Z5Z5Z2.lean`
- Mirrored Lean file: `artifacts/z5-z5-z2-prime-zero-divisor-graph/lean/AutoMath/Z5Z5Z2.lean`
- Axiom audit file: `artifacts/z5-z5-z2-prime-zero-divisor-graph/lean/AxiomAudit.lean`
- Main Lean theorem: `AutoMath.Z5Z5Z2.z5_z5_z2_zeroDivisorGraph_prime`
- Explicit Lean theorem: `AutoMath.Z5Z5Z2.z5_z5_z2_zeroDivisorGraph_prime_explicit`
- Recorded axiom audit: only `[propext, Classical.choice, Quot.sound]`
- Extra Lean audit note: `lean4checker --fresh` was unavailable on this machine

## z7-z25-prime-zero-divisor-graph

- Title: `Is the zero-divisor graph Γ(Z_7 × Z_25) prime?`
- Exact statement: the zero-divisor graph `Γ(Z_7 × Z_25)` admits a prime labeling, meaning a bijection from its `54` vertices to `{1,2,...,54}` such that adjacent vertices receive coprime labels.
- Verify verdict: `VERIFIED`
- Publication status: `INSTANCE_ONLY`
- Lean completion date in repo state: `2026-04-08`
- Vertex count / label set size: `54`
- Completion note: Lean verified the exact intended `Z_7 × Z_25` instance in the AutoMath backend with the explicit 54-label witness from verification.
- Artifact directory: `artifacts/z7-z25-prime-zero-divisor-graph/`
- Record file: `artifacts/z7-z25-prime-zero-divisor-graph/record.md`
- Status file: `artifacts/z7-z25-prime-zero-divisor-graph/status.json`
- Lean backend file: `lean/AutoMath/Z7Z25.lean`
- Mirrored Lean file: `artifacts/z7-z25-prime-zero-divisor-graph/lean/Z7Z25.lean`
- Axiom audit file: `artifacts/z7-z25-prime-zero-divisor-graph/lean/Z7Z25AxiomAudit.lean`
- Main Lean theorem: `AutoMath.Z7Z25.z7_z25_zeroDivisorGraph_prime`
- Explicit Lean theorem: `AutoMath.Z7Z25.z7_z25_zeroDivisorGraph_prime_explicit`
- Recorded axiom audit: only `[propext, Classical.choice, Quot.sound]`
- Extra Lean audit note: `lean4checker --fresh` was unavailable on this machine

## z7-z7-z2-prime-zero-divisor-graph

- Title: `Is the zero-divisor graph Γ(Z_7 × Z_7 × Z_2) prime?`
- Exact statement: the zero-divisor graph `Γ(Z_7 × Z_7 × Z_2)` admits a prime labeling, meaning a bijection from its `61` vertices to `{1,2,...,61}` such that adjacent vertices receive coprime labels.
- Verify verdict: `VERIFIED`
- Publication status: `INSTANCE_ONLY`
- Lean completion date in repo state: `2026-04-08`
- Vertex count / label set size: `61`
- Completion note: Lean verified the exact intended `Z_7 × Z_7 × Z_2` instance in the AutoMath backend using the explicit 61-label witness from verification.
- Artifact directory: `artifacts/z7-z7-z2-prime-zero-divisor-graph/`
- Record file: `artifacts/z7-z7-z2-prime-zero-divisor-graph/record.md`
- Status file: `artifacts/z7-z7-z2-prime-zero-divisor-graph/status.json`
- Lean backend file: `lean/AutoMath/Z7Z7Z2.lean`
- Mirrored Lean file(s): `artifacts/z7-z7-z2-prime-zero-divisor-graph/lean/AutoMath/Z7Z7Z2.lean`, `artifacts/z7-z7-z2-prime-zero-divisor-graph/lean/AxiomAudit.lean`
- Main Lean theorem: `AutoMath.Z7Z7Z2.z7_z7_z2_zeroDivisorGraph_prime`
- Explicit Lean theorem: `AutoMath.Z7Z7Z2.z7_z7_z2_zeroDivisorGraph_prime_explicit`
- Recorded axiom audit: only `[propext, Classical.choice, Quot.sound]`
- `lean4checker --fresh` note: unavailable on this machine
- Build note: `lake build AutoMath.Z7Z7Z2` succeeded; repo-wide `lake build` currently fails in unrelated existing file `lean/AutoMath/C16458CNBC.lean`

## p7-square-prime-labeling

- Title: `Does the square of the 7-vertex path P_7^2 admit a prime labeling?`
- Exact statement: the square of the seven-vertex path `P_7^2` admits a prime labeling, meaning a bijection from its `7` vertices to `{1,2,...,7}` such that adjacent vertices receive coprime labels.
- Verify verdict: `VERIFIED`
- Publication status: `INSTANCE_ONLY`
- Lean completion date in repo state: `2026-04-08`
- Completion note: Lean verified the exact intended `P_7^2` instance using the verified witness `(6,1,5,2,3,7,4)` in path order.
- Artifact directory: `artifacts/p7-square-prime-labeling/`
- Record file: `artifacts/p7-square-prime-labeling/record.md`
- Status file: `artifacts/p7-square-prime-labeling/status.json`
- Lean backend file: `lean/AutoMath/P7SquarePrimeLabeling.lean`
- Mirrored Lean file(s): `artifacts/p7-square-prime-labeling/lean/AutoMath/P7SquarePrimeLabeling.lean`, `artifacts/p7-square-prime-labeling/lean/AxiomAudit.lean`
- Main Lean theorem: `AutoMath.P7SquarePrimeLabeling.p7_square_prime`
- Explicit Lean theorem: `AutoMath.P7SquarePrimeLabeling.p7_square_prime_explicit`
- Axiom audit note: `lake env lean ../artifacts/p7-square-prime-labeling/lean/AxiomAudit.lean` reported only `[propext, Classical.choice, Quot.sound]` for the main theorem
- `lean4checker --fresh` note: unavailable on this machine
- Build note: `lake build AutoMath.P7SquarePrimeLabeling` succeeded; repo-wide `lake build` currently fails in unrelated existing files `lean/AutoMath/C16458CNBC.lean` and `lean/AutoMath/C244512CNBC.lean`

## p4x-p4-grid-prime-labeling

- Title: `Does the 4x4 grid P_4 x P_4 admit a prime labeling?`
- Exact statement: the Cartesian grid graph `P_4 x P_4` admits a prime labeling, meaning a bijection from its `16` vertices to `{1,2,...,16}` such that every horizontal or vertical edge joins coprime labels.
- Verify verdict: `VERIFIED`
- Publication status: `INSTANCE_ONLY`
- Lean completion date in repo state: `2026-04-08`
- Completion note: Lean verified the exact intended `P_4 x P_4` instance using the explicit `4 x 4` witness matrix from verification.
- Artifact directory: `artifacts/p4x-p4-grid-prime-labeling/`
- Record file: `artifacts/p4x-p4-grid-prime-labeling/record.md`
- Status file: `artifacts/p4x-p4-grid-prime-labeling/status.json`
- Lean backend file: `lean/AutoMath/P4xP4GridPrimeLabeling.lean`
- Mirrored Lean file(s): `artifacts/p4x-p4-grid-prime-labeling/lean/AutoMath/P4xP4GridPrimeLabeling.lean`, `artifacts/p4x-p4-grid-prime-labeling/lean/AxiomAudit.lean`
- Main Lean theorem: `AutoMath.P4xP4GridPrimeLabeling.p4x_p4_grid_prime`
- Explicit Lean theorem: `AutoMath.P4xP4GridPrimeLabeling.p4x_p4_grid_prime_explicit`
- Axiom audit note: `lake env lean ../artifacts/p4x-p4-grid-prime-labeling/lean/AxiomAudit.lean` reported only `[propext, Classical.choice, Quot.sound]` for the main, checked, and explicit theorems, with no `sorryAx` in the audit output
- `lean4checker --fresh` note: unavailable on this machine
- Build note: `lake build AutoMath.P4xP4GridPrimeLabeling` succeeded; repo-wide `lake build` currently fails in unrelated existing modules `lean/AutoMath/C16458CNBC.lean` and `lean/AutoMath/C244512CNBC.lean`
