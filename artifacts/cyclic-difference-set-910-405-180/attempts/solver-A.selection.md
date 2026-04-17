# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-910-405-180`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open cyclic row (910,405,180) in group [910], cross-checked against Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), slide 39, and Marco Buratti and Aleksandra Nakić, "On symmetric designs with additive automorphism groups" (Designs, Codes and Cryptography, online 2024), which still cites cyclic (910,405,180) existence as open.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle the exact cyclic row (910,405,180) in C_910.`
- publication_if_solved_score: `solve_is_basically_the_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `low`
- paper_leverage_score: `82`
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
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-910-405-180/working_packet.md`
- paper_shape: `A short exact cyclic residual-row note resolving one of the canonical open Table 2 cases.`

## question
Does the cyclic group C_910 admit a (910,405,180)-difference set?

## canonical_statement
Determine whether the cyclic group C_910 admits a (910,405,180)-difference set.

## intended_statement
Determine whether the cyclic group C_910 admits a (910,405,180)-difference set.

## pre_solve_gate_reason
The exact theorem slice stayed stable across the 2016 survey, the 2019 repository slides, and a 2024 primary-source mention that still treats the row as open, so one decisive solve would already be most of a paper.

## micro_paper_assessment
Lane-eligible exact residual case with a stable theorem slice, cheap novelty surface, and a solve that is basically the paper.

## hypothetical_title
On the Cyclic (910,405,180) Difference-Set Problem

## hypothetical_abstract
We determine whether the cyclic group C_910 admits a (910,405,180)-difference set. Gordon and Schmidt list this exact row as open in Table 2 of their multiplier-conjecture survey, Gordon still lists it in the 2019 La Jolla repository slides, and Buratti and Nakić still cite its existence as open in 2024. A proof or disproof would therefore resolve a crisp frontier residue and would already supply the title theorem of a short note.

## single_solve_paper_explanation
The exact theorem is already isolated in the literature, so the solve itself is the paper's mathematical core. What remains after the solve is only light exposition: restating the row's place in Table 2 and recording the decisive multiplier or contracted-count obstruction or construction. There is no feeder ladder hiding behind this packet.

## broader_theorem_nonimplication_note
A later broader theorem would be expected to remove the row from the open-case lists, but a 2024 primary-source paper still refers to cyclic (910,405,180) existence as open, so the bounded audit did not surface any ambient result that already settles it.

## literature_gap
Published sources surfaced in this curation stop at treating the exact cyclic row (910,405,180) as open: it appears in Gordon-Schmidt 2016 Table 2, Gordon 2019 still lists it among the smallest open cases, and Buratti-Nakić 2024 still cite the row as open.

## publication_packet_title
On the Cyclic (910,405,180) Difference-Set Problem

## publication_packet_frontier_basis
Gordon-Schmidt 2016 isolate the exact cyclic row [910] as open in Table 2, Gordon 2019 still lists it among the smallest open cases, and Buratti-Nakić 2024 still refer to a cyclic (910,405,180) difference set as open.

## publication_packet_near_paper_reason
The source literature already provides an exact title theorem with bounded context; after a solve, only a short comparison with the standard multiplier tables and the proof argument would remain.

## publication_packet_literature_scope
Gordon-Schmidt 2016 Table 2; Gordon 2019 ArasuFest slides; Buratti-Nakić 2024 on additive automorphism groups; local attempt-registry conflict check on 2026-04-15.

## publication_packet_artifact_requirements
A proof or disproof in C_910 together with the contracted quotient or multiplier argument and a short explanation of why the row survives the published eliminations.

## paper_shape
A short exact cyclic residual-row note resolving one of the canonical open Table 2 cases.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt 2016 isolate the exact cyclic row [910] in Table 2, so the target theorem is already source-stable.
- The survey's multiplier and quotient framework sharply constrains any hypothetical cyclic set in C_910.
- The factorization 910 = 2 · 5 · 7 · 13 gives immediate quotient tests at orders 70, 130, 182, and 455.

### toy_example
Contract to the quotient of order 70 and test whether any admissible coefficient multiset can sum to 405 while matching the required second-moment relation for λ = 180.

### known_obstruction
The row survives the standard multiplier eliminations already built into the survey tables, so any proof must sharpen the quotient bookkeeping beyond the existing open-case machinery.

### prior_work_stop_sentence
Gordon-Schmidt 2016 list (910,405,180) as open in Table 2, Gordon 2019 still lists it among the smallest open cases, and Buratti-Nakić 2024 still refer to a cyclic (910,405,180) difference set as open.

### recommended_first_attack
Use cyclic contracted multipliers on quotients by 5, 7, and 13 and compare the resulting coefficient patterns against the exact size and autocorrelation constraints.

### paper_if_solved
If solved exactly, the paper would be a short residual-row note settling the cyclic Table 2 case (910,405,180).
