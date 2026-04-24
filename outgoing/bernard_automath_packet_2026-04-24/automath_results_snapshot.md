# AutoMath results snapshot

Prepared: 2026-04-24

## Definitions

`lean_queue.json` contains publication-significant packets for which:

- the solve is done;
- verification says `VERIFIED`;
- the publication audit says `PAPER_READY`;
- proof artifacts are preserved;
- Lean is the remaining gate.

`lean_complete.json` contains publication-significant proofs that AutoMath has definitively proved in Lean.

## Current counts

- Archived failed / unsuitable / rediscovered / non-ready attempts: `142`
- Publication-significant packets in `lean_queue.json`: `9`
- Publication-significant proofs in `lean_complete.json`: `0`
- Archived legacy Lean-complete instance-only snippets: `9`

The crude publication-packet success rate in the current repo snapshot is:

`9 / (142 + 9 + 0) = 9 / 151 = 5.96%`

This rate counts publication-significant Lean-pending packets, not Lean-complete theorem proofs. The Lean-complete publication-significant count is currently `0`.

## Other publication-significant packets

Besides `r-b8-b10-book-ramsey`, the current `lean_queue.json` contains these eight Lean-pending publication packets:

- `abelian-difference-set-64681-441-3`
- `cyclic-difference-set-963-222-51`
- `cyclic-difference-set-645-161-40`
- `cyclic-hadamard-difference-set-8835-4417-2208`
- `cyclic-hadamard-difference-set-9423-4711-2355`
- `cyclic-difference-set-1111-186-31`
- `cyclic-difference-set-2291-230-23`
- `cyclic-difference-set-1925-260-35`

All nine live publication-significant packets, including `R(B8,B10)`, are pending Lean.

## Legacy Lean code

There are nine old Lean-complete artifacts in the archive, but they are instance-only and not counted as publication-significant AutoMath successes. They were moved out of the live `lean_complete.json` so that "Lean-complete" means exactly "definitively proved in Lean and publication-significant."

