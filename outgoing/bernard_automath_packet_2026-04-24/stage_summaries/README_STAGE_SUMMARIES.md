# Stage summaries note

These are normalized summaries of the harness stages:

- `solve_stage_summary.md`
- `verify_stage_summary.md`
- `lean_stage_summary.md`

They are included to show how the program moved through solve, verify, and Lean without carrying forward stale internal labels. For full current status, use:

- `../rb8_b10_clean_transcript.md`
- `../automath_results_snapshot.md`
- `../current_state/lean_queue_publication_ready_pending_lean.json`
- `../current_state/lean_complete_publication_significant.json`

Current corrected status: the `R(B8,B10)` packet is publication-significant and Lean-pending, so it belongs in `lean_queue.json`; it is not Lean-complete, so it is not in `lean_complete.json`.
