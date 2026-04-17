# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-1925-260-35`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 2 listing the exact cyclic row (1925,260,35) among the possible cases with 150 <= k <= 300 and gcd(v,n) > 1.`
- open_status_checked_on: `2026-04-16`
- publication_status: `NONE`
- publication_if_solved: `Settling the cyclic (1925,260,35) row would plausibly yield a short residual-case note whose title theorem is exactly this Baumert-Gordon Table 2 survivor.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `81`
- single_solve_to_paper_fraction: `0.79`
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
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/cyclic-difference-set-1925-260-35/working_packet.md`
- paper_shape: `A short residual-case note closing one exact cyclic Table 2 survivor by proof or disproof.`

## question
Does the cyclic group C_1925 admit a (1925,260,35)-difference set?

## canonical_statement
Determine whether the cyclic group C_1925 admits a (1925,260,35)-difference set.

## intended_statement
Determine whether the cyclic group C_1925 admits a (1925,260,35)-difference set.

## pre_solve_gate_reason
The local attempt registry is clean, the exact theorem slice is stable, and the bounded 2026-04-16 web audit surfaced the canonical source but no later exact-tuple settlement; under the search cap this is the best currently usable micro-paper packet.

## micro_paper_assessment
Lane-eligible. The theorem slice is exact, source-anchored, and paper-shaped, and one solve would plausibly account for most of the note.

## hypothetical_title
On the cyclic (1925,260,35) difference-set case

## hypothetical_abstract
We determine whether the cyclic group C_1925 admits a (1925,260,35)-difference set. Baumert and Gordon isolate this exact parameter row in Table 2 as one of the residual cyclic cases with 150 <= k <= 300 and gcd(v,n) > 1. A direct solution closes a named survivor in a standard source and would support a short note with only light framing left after the proof.

## single_solve_paper_explanation
The source already supplies a crisp theorem statement, a canonical table entry, and the standard necessary conditions that failed to eliminate the case. That means a single proof or disproof would already provide most of the eventual note, with only a brief introduction, the cleaned main argument, and a short literature-status paragraph left to write. This is not just a tiny curiosity because it closes one exact residual row in a recognized cyclic-difference-set classification table.

## broader_theorem_nonimplication_note
Baumert-Gordon explicitly leave (1925,260,35) in Table 2 after their standard eliminations, so the row is not already dispatched inside the canonical source. The bounded 2026-04-16 web audit did not surface a later exact-tuple theorem settling this parameter set.

## literature_gap
Baumert-Gordon stop at listing (1925,260,35) as a remaining possible cyclic case in Table 2; the capped 2026-04-16 audit found no later exact-tuple settlement.

## publication_packet_title
The Cyclic (1925,260,35) Difference-Set Case

## publication_packet_frontier_basis
Baumert-Gordon Table 2 isolates (1925,260,35) as an exact remaining cyclic row after the source's standard eliminations.

## publication_packet_near_paper_reason
If the row is still open, one decisive proof or disproof already supplies the title theorem, the canonical literature anchor, and nearly all of the note's mathematical payload.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 2 and its Section 2-3 machinery, bounded exact/alternate tuple web probes on 2026-04-16, Dan Gordon's publications/database surfaces, and local attempt/search/paper/failed memory.

## publication_packet_artifact_requirements
A proof or disproof for C_1925, the decisive multiplier-orbit or contraction argument, and a short status note recording the bounded 2026-04-16 outside-source audit.

## paper_shape
A short residual-case note closing one exact cyclic Table 2 survivor by proof or disproof.

## transfer_kit

### usable_lemmas
- Baumert-Gordon Table 2 isolates (1925,260,35) as an exact remaining cyclic row with gcd(v,n) > 1.
- Section 2 records the standard arithmetic and multiplier filters already exhausted before the tuple reaches Table 2.
- Theorem 3.1 gives contracted coefficient equations for every divisor w of v.
- Theorem 3.2 gives multiplier-orbit equalities once a suitable prime-power divisor of n yields a contracted multiplier modulo a divisor of v.

### toy_example
Contract a hypothetical 260-set modulo 25 or 35 and compare the resulting coefficient vector with the orbit sizes forced by powers of 3 acting on the quotient.

### known_obstruction
Any surviving configuration must satisfy both the Table 2 residual arithmetic and a rigid contracted-multiplier pattern across the 5^2 * 7 * 11 factorization of v.

### prior_work_stop_sentence
Baumert and Gordon stop at listing (1925,260,35) as a remaining possible cyclic case in Table 2.

### recommended_first_attack
Choose a divisor of 1925 on which a prime divisor of n induces a useful contracted multiplier, then intersect the forced orbit decomposition with the Theorem 3.1 coefficient equations.

### paper_if_solved
If solved exactly, the paper would be a short note closing the cyclic Table 2 row (1925,260,35).
