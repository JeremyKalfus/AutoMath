# AutoMath Proofs

This file is maintained by the LEAN stage of AutoMath.
When a candidate is upgraded to `EXACT`, the same Lean run should update or append that slug's section here before it finalizes `status.json`.

It records every AutoMath result that currently counts as a full success inside the harness:

- `classification = EXACT`
- `lean_complete = true`

## Update Rule

- Keep exactly one section per solved slug using heading `## <slug>`.
- If a slug's section already exists, replace that section instead of duplicating it.
- Do not add rediscoveries, partials, variants, or non-Lean candidates.

## z3-z25-prime-zero-divisor-graph

- Title: `Is the zero-divisor graph Γ(Z_3 × Z_25) prime?`
- Exact statement: the zero-divisor graph `Γ(Z_3 × Z_25)` admits a prime labeling, meaning a bijection from its `34` vertices to `{1,2,...,34}` such that adjacent vertices receive coprime labels.
- Verify verdict: `VERIFIED`
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
