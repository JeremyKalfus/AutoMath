# Does the cyclic group C_616 admit a (616,165,44)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-616-165-44`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the Ryser-conjecture slide listing (616,165,44,121) among the six small open cyclic cases.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `A proof or disproof for the cyclic (616,165,44) case would likely stand as a short Ryser-conjecture note because the source already isolates it as one of the six small open cyclic cases.`
- publication_if_solved_score: `solve_is_basically_the_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.78`
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
- novelty_check_cost: `medium`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-616-165-44/working_packet.md`
- paper_shape: `A short exact-case Ryser-conjecture note.`

## question
Does the cyclic group C_616 admit a (616,165,44)-difference set?

## canonical_statement
Determine whether the cyclic group C_616 admits a (616,165,44)-difference set.

## intended_statement
Determine whether the cyclic group C_616 admits a (616,165,44)-difference set.

## pre_solve_gate_reason
The authoritative local attempt registry shows no duplicate slug or identity-key collision, the 2019 canonical source still isolates the exact cyclic row, and the bounded 2026-04-15 exact-tuple, synonym, and recent-publications sweep surfaced no later candidate-specific settlement.

## micro_paper_assessment
This is the cleanest audited survivor in the current run. The theorem slice is stable, the family anchor is strong, and one exact solve would already look like the title theorem of a short note.

## hypothetical_title
On the cyclic (616,165,44) difference-set problem

## hypothetical_abstract
We determine whether the cyclic group C_616 admits a (616,165,44)-difference set. Gordon's La Jolla repository slides isolate this parameter set as one of the six small open cyclic cases attached to Ryser's conjecture. A decisive proof would close an exact residual row rather than contribute only feeder evidence, so the mathematical core of the note is concentrated in the single solve itself.

## single_solve_paper_explanation
This target already comes with a crisp title theorem, a named family anchor, and a tiny literature gap. If the row is settled exactly, the remaining work is mostly to write the proof cleanly and place it against Ryser's conjecture and the standard cyclic tools. No extra campaign of feeder lemmas is needed to make the note paper-shaped.

## broader_theorem_nonimplication_note
The source still lists the exact cyclic row as open, and the bounded later-status sweep surfaced no theorem expressly removing cyclic n=121 cases with v = 616. The likely proof tools are standard cyclic-contraction methods, but they do not already imply nonexistence on the surfaced record.

## literature_gap
Prior work surfaced in this curation stops at Gordon's 2019 La Jolla slides listing (616,165,44,121) among the six small open cyclic Ryser cases; the bounded 2026-04-15 exact-tuple, synonym, and recent-publications sweep surfaced no later targeted settlement.

## publication_packet_title
The cyclic (616,165,44) difference-set problem

## publication_packet_frontier_basis
Gordon's 2019 La Jolla slides list (616,165,44,121) among the six small open cyclic Ryser-conjecture cases.

## publication_packet_near_paper_reason
The canonical source already supplies the exact theorem slice, the conjectural family anchor, and the literature stop line. A clean existence or nonexistence proof would therefore do almost all of the mathematical work of the note.

## publication_packet_literature_scope
Gordon 2019 La Jolla slides for the open-case listing, Baumert-Gordon 2003 for cyclic contracted-multiplier tools, and the bounded 2026-04-15 exact-tuple/synonym sweep plus Gordon's publications page through 2025 for later-status checking.

## publication_packet_artifact_requirements
A cyclic existence or nonexistence proof, the decisive contracted-count or multiplier argument, and a brief explanation of how the result closes this Ryser-case row.

## paper_shape
A short exact-case Ryser-conjecture note.

## transfer_kit

### usable_lemmas
- Gordon 2019 isolates (616,165,44,121) as an exact small open cyclic case on the Ryser-conjecture slide.
- Baumert-Gordon 2003 state that cyclic cases with gcd(v,n) > 1 sit in the Ryser-conjecture lane and develop divisor-contraction equations for cyclic difference sets via Theorem 3.1.
- Baumert-Gordon 2003 Theorem 3.2 provides multiplier-fixed congruence constraints that can sharpen the contracted-count equations.

### toy_example
Contract modulo w = 56 so that v/w = 11 and check whether 56 integer counts in [0,11] can satisfy sum 165 and energy n + lambda*(v/w) = 121 + 44*11 = 605.

### known_obstruction
Ryser's conjecture predicts nonexistence because gcd(616,121) = 11 > 1, but the surfaced literature still leaves this exact cyclic row open.

### prior_work_stop_sentence
Gordon 2019 lists (616,165,44,121) among the six small open cyclic Ryser-conjecture cases.

### recommended_first_attack
Use divisor-contraction equations at a quotient of size 11 together with multiplier-fixed orbit constraints coming from n = 11^2.

### paper_if_solved
If solved exactly, the paper would be a short note settling one of the six small open cyclic Ryser cases.
