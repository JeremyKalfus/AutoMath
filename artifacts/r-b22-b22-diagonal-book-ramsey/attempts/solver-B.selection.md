# Untitled Entry

- entry_type: `paper_candidate`
- slug: `r-b22-b22-diagonal-book-ramsey`
- worker_role: `solver-B`
- canonical_source: `William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), introduction and diagonal-family summary, together with Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4), 2025).`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `An exact determination of R(B22, B22) could still support a short note because the public frontier remains a one-step diagonal book Ramsey gap in a named family.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short-medium`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `66`
- single_solve_to_paper_fraction: `0.7`
- title_theorem_strength: `moderate`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
- editorial_overhead: `moderate`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `small`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `moderate`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/r-b22-b22-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for a larger diagonal book Ramsey number with a stable theorem slice but weaker compactness expectations.`

## question
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B22.

## canonical_statement
Determine the exact value of R(B22, B22).

## intended_statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B22.

## pre_solve_gate_reason
The theorem slice is still a stable one-gap exact endpoint in a named family, but the larger order and weaker compactness keep it at the bottom of the live queue.

## micro_paper_assessment
Pass, but only narrowly. The theorem slice remains stable and family-anchored, yet proof compactness is less secure than in the smaller diagonal cases.

## hypothetical_title
The Exact Value of R(B22, B22)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B22, B22). Previously available results left this number in the interval 89 <= R(B22, B22) <= 90. Our result closes the remaining one-step gap for this larger diagonal book pair.

## single_solve_paper_explanation
This target barely clears the 70% paper threshold because the public frontier is still a single endpoint in an established family. A successful solve would already provide the title theorem and nearly all of the final narrative. The main reason it is weaker than the smaller diagonal cases is the increased risk of a bulkier certificate.

## broader_theorem_nonimplication_note
The broad diagonal-book theory still stops at the one-step interval and does not decide the endpoint at n = 22. A proof of the exact endpoint would therefore remain the honest title theorem rather than a trivial corollary of an existing published statement.

## literature_gap
Current public sources stop at 89 <= R(B22, B22) <= 90.

## publication_packet_title
The Exact Value of R(B22, B22)

## publication_packet_frontier_basis
Current public sources leave the diagonal book Ramsey number at 89 <= R(B22, B22) <= 90. The theorem statement is still stable because the live frontier is an exact endpoint question, not a loose asymptotic campaign.

## publication_packet_near_paper_reason
If the endpoint 89 versus 90 is settled, the note still has a natural title theorem and an immediate placement in the diagonal book sequence. The main residue after the solve is just packaging the decisive witness or forcing proof, though the certificate may be less compact than for the smaller cases.

## publication_packet_literature_scope
Classical diagonal-book interval summarized in Wesley 2026, recent family context from the 2025 EJC paper, and bounded exact-statement, alternate-notation, canonical-source, and recent-status web checks performed on 2026-04-14, plus local 2026-04-15 attempt-registry conflict checks.

## publication_packet_artifact_requirements
Either an explicit 89-vertex coloring avoiding monochromatic B22 or a compact proof that every 90-vertex coloring forces B22.

## paper_shape
A one-theorem exact-value note for a larger diagonal book Ramsey number with a stable theorem slice but weaker compactness expectations.

## transfer_kit

### usable_lemmas
- The classical diagonal-book bounds summarized in Wesley 2026 leave R(B22, B22) in the one-step interval 89 <= R(B22, B22) <= 90.
- Wesley 2026 explains that diagonal lower bounds are built from Paley-type or block-circulant constructions, giving a concrete witness architecture to inspect.
- The 2025 paper reduces book counting to common-neighborhood counts along a spine edge, which is the natural forcing mechanism for any upper-bound proof.
- Recent smaller diagonal and almost-diagonal cases in the 2025 paper show that the family remains exact-value legible rather than purely asymptotic.

### toy_example
The exact almost-diagonal case R(B20, B21) = 83 is the nearest audited exact benchmark for how a small note in this family is packaged.

### known_obstruction
For larger diagonal books, the main risk is not theorem-slice drift but a longer list of structured critical colorings that weakens certificate compactness.

### prior_work_stop_sentence
Current public sources stop at 89 <= R(B22, B22) <= 90.

### recommended_first_attack
Start from the Paley-type lower-bound architecture described in the recent literature and test whether every one-vertex extension forces too many common neighbors on some spine edge.

### paper_if_solved
The paper would be a short exact-value note closing one more diagonal book Ramsey endpoint.
