# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-781-300-115`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the exact cyclic row (781,300,115); status rechecked against Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), Table 2, and Daniel M. Gordon, "The La Jolla Difference Set Repository" talk slides (ArasuFest, 2019).`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle one of the explicit surviving cyclic difference-set rows with k <= 300, namely the exact cyclic case (781,300,115).`
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
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-781-300-115/working_packet.md`
- paper_shape: `A short note closing an exact cyclic residual row that has persisted across the small-parameter table, the multiplier survey, and the LJDSR status slides.`

## question
Does the cyclic group C_781 admit a (781,300,115)-difference set?

## canonical_statement
Determine whether the cyclic group C_781 admits a (781,300,115)-difference set.

## intended_statement
Determine whether the cyclic group C_781 admits a (781,300,115)-difference set.

## pre_solve_gate_reason
The statement is exact, cyclic, source-anchored across a clean citation chain, and a direct solution would already read like the title theorem of a short note with only light exposition left.

## micro_paper_assessment
Lane-eligible. The row is exact, stable, and strongly anchored to a recognizable cyclic-difference-set family, and one clean solve would already look like the title theorem of a short note.

## hypothetical_title
On the Cyclic (781,300,115) Difference-Set Problem

## hypothetical_abstract
We determine whether the cyclic group C_781 admits a (781,300,115)-difference set. Baumert and Gordon listed this exact row among the surviving cyclic cases with 150 <= k <= 300, and Gordon-Schmidt's multiplier-conjecture survey and Gordon's 2019 LJDSR slides still display the same case as open. A proof or disproof therefore closes a crisp residual problem with a ready-made short-note narrative.

## single_solve_paper_explanation
The exact theorem statement is already source-isolated and has a clean later status chain, so the mathematical solve itself would be the paper's core contribution. What remains after the solve is light: explain the small-parameter table context, record the cyclic multiplier bookkeeping, and package the proof certificate. This is the right 70-90% closure profile for the micro-paper lane.

## broader_theorem_nonimplication_note
In the surfaced literature, Baumert-Gordon's detailed eliminations in Sections 3.2-3.4 clear many neighboring cyclic rows but leave (781,300,115) only as a table survivor, and the later 2015 survey plus 2019 slides still list [781] as open; no boundedly surfaced broader theorem already settles this exact slice.

## literature_gap
Prior work surfaced in this audit stops at listing the exact cyclic row (781,300,115) as open in Table 3 of Baumert-Gordon 2004, then again in Table 2 of Gordon-Schmidt 2015 and in Gordon's 2019 LJDSR open-case slides.

## publication_packet_title
On the Cyclic (781,300,115) Difference-Set Problem

## publication_packet_frontier_basis
Baumert-Gordon 2004 Table 3 lists (781,300,115) as an open cyclic case with 150 <= k <= 300 and gcd(v,n)=1; Gordon-Schmidt 2015 Table 2 and Gordon's 2019 LJDSR slides still surface [781] as open.

## publication_packet_near_paper_reason
A direct proof or disproof would itself close a named long-lived cyclic row, so the solve supplies the theorem, novelty hook, and main technical body at once.

## publication_packet_literature_scope
Baumert-Gordon 2004 Table 3 and Sections 3.2-3.4, Gordon-Schmidt 2015 Table 2, and Gordon's 2019 LJDSR slides listing open cases.

## publication_packet_artifact_requirements
A proof or disproof in C_781, together with the contracted-multiplier or group-ring certificate used and a short status-chain discussion showing that the exact row remained open in the surfaced literature.

## paper_shape
A short note closing an exact cyclic residual row that has persisted across the small-parameter table, the multiplier survey, and the LJDSR status slides.

## transfer_kit

### usable_lemmas
- Baumert-Gordon Theorem 3.1 gives the contracted residue-count equations for cyclic difference sets at each divisor w of v.
- Baumert-Gordon Theorem 3.2 turns suitable powers of the prime divisors of n = 185 into w-multipliers, forcing equal coefficient patterns on residue classes modulo w.
- Gordon-Schmidt's Table 2 records the multiplier-conjecture prime data for [781], namely the n-factors 5 and 37 as the active multiplier primes still attached to the open row.

### toy_example
Baumert-Gordon's Section 3.3 elimination of the cyclic case (303,151,75) is the model toy instance: a forced multiplier collapses the search to orbit unions and a short contradiction.

### known_obstruction
The standard small-parameter, Schmidt, and contracted-multiplier filters clear many nearby cyclic rows but leave (781,300,115) standing, so any proof must sharpen the orbit or congruence bookkeeping rather than replay the existing tables.

### prior_work_stop_sentence
Baumert and Gordon list (781,300,115) in Table 3 as a possible cyclic difference set with 150 <= k <= 300 and gcd(v,n)=1, and later surfaced status sources still show [781] as open.

### recommended_first_attack
Use Theorem 3.2 on divisors w of 781 to force a common contracted multiplier from n = 5 * 37, impose the orbit-equality pattern in Theorem 3.1, and try to eliminate the resulting residue-count system without broad search.

### paper_if_solved
If solved exactly, the paper would be a short note closing the cyclic (781,300,115) row that persists across the small-parameter tables and later multiplier-survey status lists.
