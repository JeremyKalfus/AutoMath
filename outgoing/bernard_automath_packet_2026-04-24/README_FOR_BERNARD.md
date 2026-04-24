# AutoMath packet for Bernard Lidicky

Prepared: 2026-04-24

This packet is meant to answer the process/status questions around the AutoMath run that produced the candidate proof of `R(B8, B10) = 37`.

## Files

- `rb8_b10_clean_transcript.md`: concise run transcript and proof spine for the `R(B8, B10)` packet.
- `automath_results_snapshot.md`: current repo-level results snapshot, including success-rate accounting and the distinction between Lean-pending and Lean-complete results.
- `current_state/lean_queue_publication_ready_pending_lean.json`: the current publication-significant packets whose solve, verification, significance check, and proof preservation are done, but whose Lean formalization is not complete.
- `current_state/lean_complete_publication_significant.json`: the current list of publication-significant results definitively proved in Lean. This is currently empty.
- `stage_summaries/`: short normalized stage summaries for solve, verify, and Lean.
- `lean/RB8B10BookRamsey.lean`: current Lean skeleton for the `R(B8, B10)` obstruction. It checks supporting pieces but does not complete the spectral/minpoly bridge, so it is not a Lean proof of the theorem.
- `email_draft_to_bernard.md`: the replacement email body.

## Current vocabulary

- `lean_queue.json` means: the result is solved, verified, publication-significant, and preserved well enough for a paper packet; Lean is the remaining gate.
- `lean_complete.json` means: AutoMath has definitively proved the publication-significant result in Lean.

The old names `human_ready.json` and `proofs.json` were removed because they were causing exactly the wrong inference: Lean-complete instance-only snippets were being visually mixed with publication-significant packets. The current live `lean_complete.json` has `proof_count = 0`.

The corrected current state is: `R(B8,B10)` is in `lean_queue.json`, not `lean_complete.json`.

## Source checks used in the email

- Radziszowski, "Small Ramsey Numbers", DS1.17, Section 5.3(g): records the book Ramsey upper-bound mechanism. For `(m,n) = (8,10)`, the condition for `R(B_m,B_n) <= 2(m+n+1)` is satisfied, giving `R(B8,B10) <= 38`. URL: https://cs.rit.edu/~spr/ElJC/ejcram17.pdf
- Lidicky, McKinley, Pfender, Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations", EJC 32(4), #P4.64, Theorem 1: gives `4n-3 <= R(B_{n-2},B_n)` for `4 <= n <= 21`, so for `n = 10` it gives `37 <= R(B8,B10)`. DOI: https://doi.org/10.37236/13577
- AutoMath provenance: local repo snapshot at commit `9fecfaa`; Git remote is `git@github.com:JeremyKalfus/AutoMath.git`.
