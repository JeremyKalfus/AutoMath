# AutoMath 50-Cycle Observer Log

Historical note:
This file records a pre-one-shot-redesign observer run. Keep it for harness debugging history, but do not treat it as the current AutoMath operating plan or queue policy.

Date: 2026-04-08
Observer: Codex

## Scope

- Requested run: `./run_n_cycles.sh 50`
- Inter-cycle sleep override: `AUTOMATH_SLEEP_SECONDS=0`
- Goal: observe the bounded run, keep notes compact per cycle, record only confirmed issues/smells, and document any minimal fixes made to keep the harness running smoothly.

## Repo Understanding Snapshot

- `run_n_cycles.sh` wraps `run_once.sh` for a fixed cycle count and deliberately defers `.stop_harness` markers until the requested count completes.
- `run_once.sh` curates when the queue is unusable, renders the next problem into `selected_problem.md`, runs solve, then verify, and only runs Lean when verification marks the result `lean_ready = true`.
- Solve and Lean run with web disabled; verify starts with a bounded rediscovery pass.
- In the current naming scheme, publication-significant Lean-complete successes go to `lean_complete.json`; this historical run predated the `PROOFS.md` archival split. Bounded runs temporarily defer stop markers such as `.stop_harness`.

## Confirmed Issues / Smells

- Cycle 2/50: `conway-99-graph` solve worker timed out without producing `record.md` or `status.json`. The harness recovered correctly by logging a solve infrastructure failure and rotating the slug to the queue tail. Watching for repetition before changing anything.
- Cycle 10/50: `c16-4-5-8-cnbc` reached a verified `COUNTEREXAMPLE` with `lean_ready = true`, but the Lean worker timed out before completing formalization. The harness recovered by moving the slug aside with `LEAN_INCOMPLETE`, but this is a real loss of throughput on a strong candidate.
- Cycle 11/50: `c20-2-3-10-cnbc` repeated the same pattern as cycle 10: verified `COUNTEREXAMPLE`, Lean started, then Lean timed out. After this second occurrence, the Lean timeout was increased for future cycles.
- Cycle 20/50: `srg-100-33-8-12` exposed a reporting mismatch. The cycle report said `CANDIDATE (lean incomplete)` even though `status.json` had already been downgraded to `classification = FAILED` during the Lean audit. This was fixed as a reporting-only patch for future cycles.

## Changes Made

- Created this observer log.
- Raised `LEAN_TIMEOUT` in `run_once.sh` from `600` seconds to `1200` seconds after two separate verified CNBC counterexample candidates timed out during Lean formalization.
- Fixed a misleading cycle-report string in `run_once.sh` so post-Lean incomplete results now report their actual classification instead of always saying `CANDIDATE (lean incomplete)`.

## Cycle Notes

- Cycle 1/50
  - Problem: `symmetric-conference-matrix-66` — “Does a symmetric conference matrix of order 66 exist?”
  - Solve summary: handwritten no-code pass; translated the instance to `srg(65,32,15,16)` / `ETF(33,66)` and proved only a variant obstruction ruling out any Cayley or abelian-regular realization via character-field incompatibility.
  - Verify outcome: `REDISCOVERY`.
  - Harness behavior: good. The verifier moved the problem aside conservatively instead of letting a known variant obstruction count as frontier progress.

- Cycle 2/50
  - Started on `conway-99-graph`.
  - Result: solve-stage infrastructure timeout after a long idle spell with no artifact write.
  - Harness behavior: acceptable recovery. No manual intervention needed.

- Cycle 3/50
  - Started on `szymanski-q5`.

- Cycle 2/50 auto-summary
  - Title: `Does Conway's 99-graph exist?`
  - Slug: `conway-99-graph`
  - Outcome: `solve infrastructure timeout`
  - Classification: `(none)`
  - Verify verdict: `(none)`
  - Lean ran: `no`; lean ready `(none)`, lean complete `(none)`

- Cycle 3/50 auto-summary
  - Title: `Does Szymanski's routing conjecture hold for Q_5?`
  - Slug: `szymanski-q5`
  - Outcome: `PARTIAL/VERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 4/50 auto-summary
  - Title: `Does Conway's 99-graph exist?`
  - Slug: `conway-99-graph`
  - Outcome: `PARTIAL/VERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 5/50 auto-summary
  - Title: `Does Baron Munchhausen's omni-sequence satisfy B(22)=3?`
  - Slug: `b22-munchhausen-matrix`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 6/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (60,16,9,2,5) exist?`
  - Slug: `dsrg-60-16-9-2-5`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 7/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (60,18,11,6,5) exist?`
  - Slug: `dsrg-60-18-11-6-5`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 8/50 auto-summary
  - Title: `Does a strongly regular graph with parameters (69,20,7,5) exist?`
  - Slug: `srg-69-20-7-5`
  - Outcome: `PARTIAL/VERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 9/50 auto-summary
  - Title: `Does Baron Munchhausen's omni-sequence satisfy B(23)=3?`
  - Slug: `b23-munchhausen-matrix`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 10/50 auto-summary
  - Title: `Is the quintic circulant C_16(4,5,8) a CNBC graph?`
  - Slug: `c16-4-5-8-cnbc`
  - Outcome: `lean infrastructure timeout`
  - Classification: `COUNTEREXAMPLE`
  - Verify verdict: `VERIFIED`
  - Lean ran: `yes`; lean ready `true`, lean complete `false`

- Cycle 11/50 auto-summary
  - Title: `Is the quintic circulant C_20(2,3,10) a CNBC graph?`
  - Slug: `c20-2-3-10-cnbc`
  - Outcome: `lean infrastructure timeout`
  - Classification: `COUNTEREXAMPLE`
  - Verify verdict: `VERIFIED`
  - Lean ran: `yes`; lean ready `true`, lean complete `false`

- Cycle 12/50 auto-summary
  - Title: `Is the quintic circulant C_24(4,5,12) a CNBC graph?`
  - Slug: `c24-4-5-12-cnbc`
  - Outcome: `lean infrastructure timeout`
  - Classification: `COUNTEREXAMPLE`
  - Verify verdict: `VERIFIED`
  - Lean ran: `yes`; lean ready `true`, lean complete `false`

- Cycle 13/50 auto-summary
  - Title: `Is the zero-divisor graph Gamma(Z_7 x Z_7 x Z_2) prime?`
  - Slug: `z7-z7-z2-prime-zero-divisor-graph`
  - Outcome: `EXACT`
  - Classification: `EXACT`
  - Verify verdict: `VERIFIED`
  - Lean ran: `yes`; lean ready `true`, lean complete `true`

- Cycle 14/50 auto-summary
  - Title: `Does Baron Munchhausen's omni-sequence satisfy B(24)=3?`
  - Slug: `b24-munchhausen-matrix`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 15/50 auto-summary
  - Title: `Does the square of the 7-vertex path P_7^2 admit a prime labeling?`
  - Slug: `p7-square-prime-labeling`
  - Outcome: `EXACT`
  - Classification: `EXACT`
  - Verify verdict: `VERIFIED`
  - Lean ran: `yes`; lean ready `true`, lean complete `true`

- Cycle 16/50 auto-summary
  - Title: `Does the 4x4 grid P_4 × P_4 admit a prime labeling?`
  - Slug: `p4x-p4-grid-prime-labeling`
  - Outcome: `EXACT`
  - Classification: `EXACT`
  - Verify verdict: `VERIFIED`
  - Lean ran: `yes`; lean ready `true`, lean complete `true`

- Cycle 17/50 auto-summary
  - Title: `Does the Möbius ladder M_5 admit a prime labeling?`
  - Slug: `m5-mobius-ladder-prime-labeling`
  - Outcome: `REDISCOVERY`
  - Classification: `REDISCOVERY`
  - Verify verdict: `REDISCOVERY`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 18/50 auto-summary
  - Title: `Does a strongly regular graph with parameters (85,30,11,10) exist?`
  - Slug: `srg-85-30-11-10`
  - Outcome: `PARTIAL/VERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 19/50 auto-summary
  - Title: `Does a strongly regular graph with parameters (88,27,6,9) exist?`
  - Slug: `srg-88-27-6-9`
  - Outcome: `FAILED/CRITICAL_FLAW`
  - Classification: `FAILED`
  - Verify verdict: `CRITICAL_FLAW`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 20/50 auto-summary
  - Title: `Does a strongly regular graph with parameters (100,33,8,12) exist?`
  - Slug: `srg-100-33-8-12`
  - Outcome: `CANDIDATE (lean incomplete)`
  - Classification: `FAILED`
  - Verify verdict: `MINOR_FIX`
  - Lean ran: `yes`; lean ready `false`, lean complete `false`

- Cycle 21/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (54,10,4,1,2) exist?`
  - Slug: `dsrg-54-10-4-1-2`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 22/50 auto-summary
  - Title: `Does a strongly regular graph with parameters (96,35,10,14) exist?`
  - Slug: `srg-96-35-10-14`
  - Outcome: `PARTIAL/VERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 23/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (64,13,6,1,3) exist?`
  - Slug: `dsrg-64-13-6-1-3`
  - Outcome: `verify infrastructure timeout`
  - Classification: `PARTIAL`
  - Verify verdict: `(none)`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 24/50 auto-summary
  - Title: `Does a strongly regular graph with parameters (99,42,21,15) exist?`
  - Slug: `srg-99-42-21-15`
  - Outcome: `PARTIAL/VERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 25/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (64,13,6,1,3) exist?`
  - Slug: `dsrg-64-13-6-1-3`
  - Outcome: `VARIANT/VERIFIED`
  - Classification: `VARIANT`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 26/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (36,14,7,6,5) exist?`
  - Slug: `dsrg-36-14-7-6-5`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 27/50 auto-summary
  - Title: `Does Baron Munchhausen's omni-sequence satisfy B(25)=3?`
  - Slug: `b25-munchhausen-matrix`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 28/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (54,11,4,3,2) exist?`
  - Slug: `dsrg-54-11-4-3-2`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 29/50 auto-summary
  - Title: `Does Baron Munchhausen's omni-sequence satisfy B(26)=3?`
  - Slug: `b26-munchhausen-matrix`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 30/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (51,15,10,5,4) exist?`
  - Slug: `dsrg-51-15-10-5-4`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 31/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (28,6,3,2,1) exist?`
  - Slug: `dsrg-28-6-3-2-1`
  - Outcome: `PARTIAL/VERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 32/50 auto-summary
  - Title: `What is the exact value of A352178(23)?`
  - Slug: `powers-of-two-pairs-23`
  - Outcome: `VARIANT/VERIFIED`
  - Classification: `VARIANT`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 33/50 auto-summary
  - Title: `Does a 5-balanced equi-30-square exist?`
  - Slug: `d5-balanced-equi-30-square`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 34/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (24,10,5,3,5) exist?`
  - Slug: `dsrg-24-10-5-3-5`
  - Outcome: `PARTIAL/UNVERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `UNVERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 35/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (27,7,4,1,2) exist?`
  - Slug: `dsrg-27-7-4-1-2`
  - Outcome: `PARTIAL/VERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 36/50 auto-summary
  - Title: `(none)`
  - Slug: `(none)`
  - Outcome: `curation timed out without a usable queue`
  - Classification: `(none)`
  - Verify verdict: `(none)`
  - Lean ran: `no`; lean ready `(none)`, lean complete `(none)`

- Cycle 37/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (40,18,9,7,9) exist?`
  - Slug: `dsrg-40-18-9-7-9`
  - Outcome: `PARTIAL/VERIFIED`
  - Classification: `PARTIAL`
  - Verify verdict: `VERIFIED`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 38/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (48,22,11,9,11) exist?`
  - Slug: `dsrg-48-22-11-9-11`
  - Outcome: `PARTIAL/MINOR_FIX`
  - Classification: `PARTIAL`
  - Verify verdict: `MINOR_FIX`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 39/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (56,12,3,1,3) exist?`
  - Slug: `dsrg-56-12-3-1-3`
  - Outcome: `PARTIAL/CRITICAL_FLAW`
  - Classification: `PARTIAL`
  - Verify verdict: `CRITICAL_FLAW`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 40/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (48,9,5,0,2) exist?`
  - Slug: `dsrg-48-9-5-0-2`
  - Outcome: `PARTIAL/CRITICAL_FLAW`
  - Classification: `PARTIAL`
  - Verify verdict: `CRITICAL_FLAW`
  - Lean ran: `no`; lean ready `false`, lean complete `false`

- Cycle 41/50 auto-summary
  - Title: `Does a directed strongly regular graph with parameters (30,11,9,2,5) exist?`
  - Slug: `dsrg-30-11-9-2-5`
  - Outcome: `PARTIAL (lean incomplete)`
  - Classification: `PARTIAL`
  - Verify verdict: `CRITICAL_FLAW`
  - Lean ran: `yes`; lean ready `false`, lean complete `false`

- Cycle 42/50 auto-summary
  - Title: `(none)`
  - Slug: `(none)`
  - Outcome: `curation timed out without a usable queue`
  - Classification: `(none)`
  - Verify verdict: `(none)`
  - Lean ran: `no`; lean ready `(none)`, lean complete `(none)`

- Cycle 43/50 auto-summary
  - Title: `(none)`
  - Slug: `(none)`
  - Outcome: `curation timed out without a usable queue`
  - Classification: `(none)`
  - Verify verdict: `(none)`
  - Lean ran: `no`; lean ready `(none)`, lean complete `(none)`

- Cycle 44/50 auto-summary
  - Title: `(none)`
  - Slug: `(none)`
  - Outcome: `curation timed out without a usable queue`
  - Classification: `(none)`
  - Verify verdict: `(none)`
  - Lean ran: `no`; lean ready `(none)`, lean complete `(none)`
