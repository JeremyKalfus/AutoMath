# CNBC Quintic Nonexistence

Priority: second active campaign

Working objective:
Turn the verified exact nonexistence results on quintic circulants into a publishable Fourier / periodicity theorem slice, not merely a list of isolated counterexamples.

## Seed Cluster

Verified exact counterexample candidates in the ledger and artifacts:

- [artifacts/c16-4-5-8-cnbc/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/c16-4-5-8-cnbc/record.md)
- [artifacts/c20-2-3-10-cnbc/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/c20-2-3-10-cnbc/record.md)
- [artifacts/c24-4-5-12-cnbc/record.md](/Users/jeremykalfus/CodingProjects/AutoMath/artifacts/c24-4-5-12-cnbc/record.md)

Each currently sits at:

- `classification = COUNTEREXAMPLE`
- `verify_verdict = VERIFIED`
- `lean_ready = true`

## Shared Structural Backbone

All three arguments use the same translation:

- a red/blue coloring becomes a `±1` vector on `Z/nZ`
- closed-neighborhood balance becomes a circulant linear equation
- the relevant operator is diagonalized by Fourier modes
- nonexistence follows from one of two structural outcomes:
  - the operator is invertible, so no nonzero signed vector exists
  - the kernel is very small and forces a periodicity incompatible with `±1` signs

This is already a family theorem skeleton.

## Instance-Level Patterns

### `C_16(4,5,8)`

Ledger summary:

- the closed-neighborhood operator with mask `{0, ±4, ±5, 8}` has no zero Fourier mode
- the operator is invertible
- therefore there is no nonzero signed solution and hence no CNBC coloring

Publication take:

- clean “invertible circulant operator implies nonexistence” slice

### `C_20(2,3,10)`

Ledger summary:

- opposite-pair sums satisfy a length-10 circulant system
- that reduced operator is invertible
- hence `x_{i+10} = -x_i`
- the reduced half-length recurrence then forces a contradiction with period 10

Publication take:

- not pure invertibility on the original operator
- still a structural Fourier-plus-periodicity theorem

### `C_24(4,5,12)`

Ledger summary:

- the mask `{0, ±4, ±5, 12}` has a two-dimensional kernel supported only at frequencies `8` and `16`
- this forces every real solution into the primitive cube-root subspace
- therefore any solution is `3`-periodic
- no `±1`-valued 3-periodic pattern can satisfy the zero-sum condition

Publication take:

- strong periodicity theorem slice
- exact example of “small kernel implies impossible period”

## Strongest Current Publication Targets

1. A Fourier criterion theorem for quintic circulants:
   - if the closed-neighborhood circulant symbol has no zero among the relevant `n`th roots of unity, then the graph is not CNBC
2. A periodicity theorem:
   - if the kernel is supported only on low-order Fourier modes forcing a period incompatible with `±1` balance, then the graph is not CNBC
3. A hybrid slice theorem unifying the two outcomes above
4. Only after a clean theorem slice exists, an infinite-family nonexistence result along one parameter line

## Candidate Theorem Slices

### Slice A: invertible-symbol theorem

Strongest honest claim already visible:

- for a quintic circulant with the CNB mask used by the instance, if the Fourier symbol is nonzero at every discrete frequency, then the graph is not CNBC

Why publishable:

- this is not just an example
- it is a reusable structural theorem
- it explains the entire `C_16(4,5,8)` proof and future instances of the same type

### Slice B: kernel-forced periodicity theorem

Strongest honest claim already visible:

- if the CNB operator kernel is supported only on characters of order `d`, then any signed solution is `d`-periodic; if no `±1` `d`-periodic sequence satisfies the induced relation, then the graph is not CNBC

Why publishable:

- it subsumes the `C_24(4,5,12)` proof cleanly
- it also captures the second stage of the `C_20(2,3,10)` argument

### Slice C: exact opposite-pair reduction theorem

Strongest honest claim:

- in even-order quintic circulants with antipodal generator `n/2`, opposite-pair summation can reduce the CNB system to a half-length circulant obstruction

Why useful:

- it is the cleanest route from the exact `C_20(2,3,10)` proof to a theorem slice

## Chosen Campaign Target

Primary target:

- a publication-grade theorem slice unifying the three verified exact nonexistence proofs into a Fourier / periodicity criterion for quintic circulants

Secondary target:

- a clean paper framing around “spectral and periodic obstructions to closed-neighborhood balanced colorings in quintic circulants”

## Primary Theorem-Slice Target

- Prove a two-route obstruction theorem for selected quintic circulants:
  - invertible closed-neighborhood circulant operator implies nonexistence of a CNBC coloring
  - low-order-kernel support forcing an incompatible periodicity also implies nonexistence

## Fallback Target

- If the two-route theorem does not yet package cleanly, preserve the strongest honest criterion theorem plus the three exact frontier applications `C_16(4,5,8)`, `C_20(2,3,10)`, and `C_24(4,5,12)`.

## Strongest Path Forward

1. Formalize the exact CNB-to-circulant-operator translation.
2. Package the invertible-symbol criterion as a theorem.
3. Package the kernel-supported-on-low-order-characters criterion as a theorem.
4. Reprove `C_16`, `C_20`, and `C_24` as applications of those structural lemmas.
5. Only then evaluate whether an infinite family along one parameter line is honestly supported.

## Fallback Path

If the unified theorem slice stalls:

- keep the exact instances but explicitly publish the shared criterion as a “method plus three frontier applications” paper shape
- or run one or two discriminating feeder instances that tell us whether the current spectral pattern extends cleanly

## Next Best Feeders

Most informative next instances:

- `C_28(4,5,14)`
- `C_28(2,3,14)`

Why these:

- they extend the two strongest current parameter lines
- they test whether the same Fourier and periodicity mechanisms recur or fragment

## Blockers

- The exact proofs still use three slightly different narrations of the same mechanism rather than one clean statement-faithful criterion theorem.
- The opposite-pair reduction in the `C_20` line still needs to be expressed as a reusable structural lemma instead of an instance-specific maneuver.
- The campaign has not yet been Lean-packaged as a family criterion, only as exact-supporting linear algebra.

## Publication Value

The repo already contains three verified exact nonexistence arguments that are clearly not random. Their common backbone is strong enough to justify a publication campaign even before Lean closes every instance. The likely publishable product is a structural Fourier / periodicity theorem with exact frontier applications.
