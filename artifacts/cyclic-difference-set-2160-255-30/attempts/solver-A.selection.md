# Does the cyclic group C_2160 admit a (2160,255,30)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-2160-255-30`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 2 listing the exact cyclic row (2160,255,30) among the possible cases with 150 <= k <= 300 and gcd(v,n) > 1.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `Settling the exact cyclic Table 2 row (2160,255,30) would likely already yield a short Ryser-residual note, with only bounded context and exposition left.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `81`
- single_solve_to_paper_fraction: `0.76`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-2160-255-30/working_packet.md`
- paper_shape: `An exact Ryser-conjecture residual note centered on a single surviving cyclic Table 2 row.`

## question
Does the cyclic group C_2160 admit a (2160,255,30)-difference set?

## canonical_statement
Determine whether the cyclic group C_2160 admits a (2160,255,30)-difference set.

## intended_statement
Determine whether the cyclic group C_2160 admits a (2160,255,30)-difference set.

## pre_solve_gate_reason
The row is source-anchored, unattempted locally, the bounded exact-row web checks surfaced no later direct settlement, and a solve would still honestly remain the title theorem rather than collapsing into feeder work.

## micro_paper_assessment
Lane-eligible. This is the cleanest surviving one-shot packet found before the search cap: exact, source-anchored, family-anchored, and close to paper-complete if solved.

## hypothetical_title
On the cyclic (2160,255,30) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_2160 admits a (2160,255,30)-difference set. Baumert and Gordon isolate this tuple in Table 2 among the surviving cyclic cases with 150 <= k <= 300 and gcd(v,n) > 1 after the standard arithmetic and multiplier screens. Because the result would settle one exact Ryser-residual row without requiring a feeder ladder, it already looks like the title theorem of a short note.

## single_solve_paper_explanation
This target stays paper-shaped if solved: the honest theorem is exactly the Table 2 row itself, not a disposable feeder instance. The surrounding note would mostly explain the source residue, the decisive contracted-count or orbit argument, and the immediate consequence that one more Ryser-style cyclic case is removed. That is close to the 70 to 90 percent paper band.

## broader_theorem_nonimplication_note
The canonical source already isolates (2160,255,30) after its standard eliminations, and the bounded 2026-04-15 exact-row searches did not reveal a later theorem explicitly settling this tuple; unlike some smaller rows, no surfaced multiplier paper directly absorbed it during curation.

## literature_gap
Baumert-Gordon 2004 Table 2 lists the cyclic row (2160,255,30) as possible, and the bounded 2026-04-15 follow-up surfaced no direct later settlement for that exact tuple.

## publication_packet_title
The Cyclic (2160,255,30) Difference-Set Case

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 2 isolates (2160,255,30) as an exact surviving cyclic row with gcd(v,n) > 1; bounded 2026-04-15 exact-tuple searches for the row surfaced no direct later settlement beyond the canonical source and the current Dan Gordon difference-set database surface.

## publication_packet_near_paper_reason
A clean nonexistence or existence proof would already settle an exact Ryser-table residue with a clear family anchor, so the remaining work is mainly concise framing rather than additional mathematics.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 2 and Sections 2-3, the current Dan Gordon difference-set database surface accessed on 2026-04-15, bounded exact-row web searches for (2160,255,30), and the local attempt registry.

## publication_packet_artifact_requirements
A proof or disproof for C_2160, the decisive contracted-coefficient or multiplier-orbit contradiction, and a short note placing the row inside the Ryser gcd(v,n) > 1 residual table.

## paper_shape
An exact Ryser-conjecture residual note centered on a single surviving cyclic Table 2 row.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Table 2 isolates (2160,255,30) as an exact surviving cyclic row with gcd(v,n) > 1.
- Section 2 records the classical necessary conditions already exhausted before the tuple reaches Table 2.
- Theorem 3.1 gives contracted coefficient equations for every divisor w of v.
- Theorem 3.2 gives w-multiplier orbit equalities whenever the prime powers from n = 225 produce a common residue modulo w.

### toy_example
Start with a contraction modulo a divisor such as 45 and test whether the Theorem 3.1 equations can coexist with the 3- and 5-multiplier orbit equalities forced by n = 225.

### known_obstruction
The easy Ryser-style arithmetic eliminations are already spent in the source table, so any proof must exploit sharper contraction or multiplier structure.

### prior_work_stop_sentence
Baumert-Gordon 2004 stops at listing (2160,255,30) as a remaining possible cyclic case in Table 2.

### recommended_first_attack
Combine Theorem 3.1 on a divisor carrying the 3- and 5-adic symmetry with Theorem 3.2 orbit equalities and look for an impossible orbit-count profile.

### paper_if_solved
If solved exactly, the paper would be a short note eliminating or constructing the cyclic Table 2 row (2160,255,30) in the Ryser residual lane.
