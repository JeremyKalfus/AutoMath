# Family Record: cnbc_quintic_nonexistence

## family_statement_lock

- Active family campaign: nonexistence of closed-neighborhood balanced colorings in selected quintic circulants.
- Current publication target: unify the verified exact counterexamples through a Fourier / periodicity theorem slice.

## existing_instance_inventory

- Verified exact counterexample candidates:
  - `c16-4-5-8-cnbc`
  - `c20-2-3-10-cnbc`
  - `c24-4-5-12-cnbc`
- All three currently sit at `classification = COUNTEREXAMPLE`, `verify_verdict = VERIFIED`, and `lean_ready = true`.

## shared_structure

- Every instance is translated to a `±1` circulant linear system on `Z/nZ`.
- Fourier diagonalization is the common engine.
- The current proofs split into:
  - invertible-symbol obstruction
  - small-kernel periodicity obstruction
  - opposite-pair reduction followed by periodicity contradiction

## parameter_sensitive_steps

- identifying which part of each proof is genuinely instance-specific
- deciding whether the common structural theorem should be phrased as:
  - an invertibility theorem,
  - a kernel-support theorem,
  - or a two-step antipodal reduction theorem

## candidate_theorem_slices

- Invertible-symbol theorem for quintic circulants.
- Kernel-supported-on-low-order-characters theorem.
- Opposite-pair reduction theorem for even-order antipodal quintic circulants.
- Unified Fourier / periodicity obstruction package with the three exact instances as applications.

## chosen_slice

- Chosen immediate slice: a Fourier / periodicity obstruction theorem that explains the current exact cluster without overclaiming an infinite family.

## proof_plan

1. Formalize the CNB-to-circulant-operator translation.
2. Package the invertible-symbol argument as a theorem.
3. Package the low-order-kernel periodicity argument as a theorem.
4. Recast `C_16`, `C_20`, and `C_24` as applications.

## fallback_counterexample_plan

- If the unified theorem still feels too broad, keep the exact instances and publish the shared method plus frontier applications.
- If one parameter line appears to continue cleanly, test one or two next exact instances before claiming any infinite family.

## next_best_feeder_instances

- `C_28(4,5,14)`
- `C_28(2,3,14)`

## publication_value

- The repo already has more than isolated examples. The current exact counterexamples visibly share a reusable operator-theoretic obstruction package.
