# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-765-192-48-group-3-255`
- worker_role: `solver-B`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (765,192,48) in group [3,255].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle the exact Table 2 row (765,192,48) in C_3 x C_255.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `82`
- single_solve_to_paper_fraction: `0.8`
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
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/abelian-difference-set-765-192-48-group-3-255/working_packet.md`
- paper_shape: `A short exact-group residual-row note from the multiplier-conjecture survey.`

## question
Does the abelian group C_3 x C_255 admit a (765,192,48)-difference set?

## canonical_statement
Determine whether the abelian group C_3 x C_255 admits a (765,192,48)-difference set.

## intended_statement
Determine whether the abelian group C_3 x C_255 admits a (765,192,48)-difference set.

## pre_solve_gate_reason
The row is exact, locally fresh, and unique in the surveyed table neighborhood; bounded exact/alternate-notation web sweeps returned no direct later settlement.

## micro_paper_assessment
Lane-eligible. This is a unique exact-row residual case with low feeder risk and a clean short-note packet if solved.

## hypothetical_title
On the (765,192,48) Difference-Set Problem in C_3 x C_255

## hypothetical_abstract
We determine whether the abelian group C_3 x C_255 admits a (765,192,48)-difference set. Gordon and Schmidt list this exact group row as open in Table 2 of their multiplier-conjecture survey. Because the row is already isolated at source level and no direct later settlement surfaced in the bounded status sweep, one exact solve would already form the core of a short publishable note.

## single_solve_paper_explanation
This is already a paper-shaped exact theorem/result pair in a standard reference table. Solving it would supply the central theorem and most of the technical work. What remains would be a short introduction, notation setup, and proof cleanup.

## broader_theorem_nonimplication_note
The row remains explicitly listed after the survey's multiplier theorems and does not share the same parameters with another known exact group row in the final shortlist, so no broader result surfaced here that would make the honest title theorem substantially larger than this exact case.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing (765,192,48) in [3,255] as open; bounded exact and alternate-notation web sweeps on 2026-04-15 found no direct later settlement.

## publication_packet_title
On the (765,192,48) Difference-Set Problem in C_3 x C_255

## publication_packet_frontier_basis
Gordon-Schmidt 2016 Table 2 isolates the exact [3,255] row as open, and local attempt/source memory shows no conflicting prior run on this exact statement.

## publication_packet_near_paper_reason
The source already provides the title-theorem statement, so a decisive proof or disproof would leave only light contextual framing and exposition.

## publication_packet_literature_scope
Gordon-Schmidt 2015/2016 Table 2, bounded exact-statement and alternate-notation web sweeps on 2026-04-15, and local attempt/source registry checks.

## publication_packet_artifact_requirements
A proof or disproof in C_3 x C_255, the decisive multiplier-orbit or quotient contradiction or construction, and a short account of why the row survived the published multiplier criteria.

## paper_shape
A short exact-group residual-row note from the multiplier-conjecture survey.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt 2016 isolate the exact [3,255] row in Table 2, fixing the target theorem.
- For (765,192,48), the order is n = 144 = 2^4 x 3^2, so the nontrivial multiplier pressure comes first from the prime 2 recorded against the row.
- The group C_3 x C_255 decomposes as C_3^2 x C_5 x C_17, giving immediate quotient maps to the 5- and 17-parts for orbit-size bookkeeping.

### toy_example
Project a hypothetical difference set to the C_17 quotient and check whether a 2-multiplier-fixed orbit partition can realize total size 192.

### known_obstruction
The published multiplier criteria do not already remove the row, so any proof must sharpen the orbit or quotient analysis beyond the tabulated filters.

### prior_work_stop_sentence
Gordon-Schmidt 2016 list (765,192,48) in group [3,255] as open in Table 2.

### recommended_first_attack
Exploit the C_3^2 x C_5 x C_17 decomposition and test whether 2-multiplier orbit sizes on the odd quotients are compatible with k = 192 and lambda = 48.

### paper_if_solved
If solved exactly, the paper would be a short residual-row note on the Table 2 case (765,192,48) in C_3 x C_255.
