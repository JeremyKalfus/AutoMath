# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-703-325-150`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), especially Table 2 listing the exact open cyclic row (703,325,150) in group [703].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle the exact cyclic Table 2 row (703,325,150) in C_703.`
- publication_if_solved_score: `solve_plus_light_writeup`
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
- working_packet_path: `artifacts/cyclic-difference-set-703-325-150/working_packet.md`
- paper_shape: `A short cyclic residual-row note anchored to the multiplier survey and contracted-multiplier toolkit.`

## question
Does the cyclic group C_703 admit a (703,325,150)-difference set?

## canonical_statement
Determine whether the cyclic group C_703 admits a (703,325,150)-difference set.

## intended_statement
Determine whether the cyclic group C_703 admits a (703,325,150)-difference set.

## pre_solve_gate_reason
This is an exact cyclic survey residue with stable theorem branding; the bounded exact-statement, alternate-notation, canonical-source, and recent-status sweep on 2026-04-15 surfaced no direct settlement, and one clean solve would already read like the title theorem of a short note.

## micro_paper_assessment
Lane-eligible. The packet is exact, source-anchored, theorem-stable, and close enough to paper-shaped that one clean solve would plausibly provide about eighty percent of the final note.

## hypothetical_title
On the (703,325,150) Cyclic Difference-Set Problem

## hypothetical_abstract
We determine whether the cyclic group C_703 admits a (703,325,150)-difference set. Gordon and Schmidt list this exact cyclic row as open in Table 2 of their multiplier-conjecture survey, and Baumert-Gordon supply a compact contracted-multiplier toolkit that is already tailored to short cyclic nonexistence notes. A definitive proof or obstruction would therefore close an exact residual case with only light exposition left after the mathematics.

## single_solve_paper_explanation
The source already isolates a single exact cyclic row, so the solve itself would supply the title theorem rather than merely feed a later campaign. What remains after the solve is mostly bounded exposition: quote the survey row, explain the residue-count or orbit argument, and compare the conclusion with the existing cyclic small-parameter tables. That is already close to the whole paper.

## broader_theorem_nonimplication_note
The surfaced literature still isolates the exact cyclic row [703] as open, and no boundedly surfaced broader theorem or database entry settles the case outright; even a proof using contracted multipliers would still honestly headline this exact row.

## literature_gap
Prior work surfaced in this curation stops at listing the exact cyclic row (703,325,150) in [703] as open in Gordon-Schmidt 2015 Table 2; the bounded exact-tuple and recent-status sweep on 2026-04-15 surfaced no later direct settlement.

## publication_packet_title
On the (703,325,150) Cyclic Difference-Set Problem

## publication_packet_frontier_basis
Gordon-Schmidt 2015 Table 2 lists the cyclic row (703,325,150) in [703] as open, and the bounded 2026-04-15 exact-tuple and recent-status sweep surfaced no later direct settlement.

## publication_packet_near_paper_reason
A direct existence or nonexistence proof would close a named cyclic survey residue and leave only light contextual writeup.

## publication_packet_literature_scope
Gordon-Schmidt 2015 Table 2, Baumert-Gordon 2004 on contracted multipliers for cyclic cases, the Dan Gordon difference-set repository landing page, and the bounded exact-tuple web sweep on 2026-04-15.

## publication_packet_artifact_requirements
A proof or disproof for C_703 together with the orbit-count or contracted-residue constraints used, plus a short comparison with the survey row and the older cyclic toolkit.

## paper_shape
A short cyclic residual-row note anchored to the multiplier survey and contracted-multiplier toolkit.

## transfer_kit

### usable_lemmas
- Baumert-Gordon 2004 Theorem 3.1 gives the contracted residue-count equations for every divisor w of v, providing compact integer constraints on the counts b_i.
- Baumert-Gordon 2004 Theorem 3.2 gives w-multiplier congruence constraints that can collapse the contracted counts into multiplier orbits.
- Gordon-Schmidt 2015 records the MC primes for this row as 5 and 7, so any proof can organize the candidate set into orbit patterns compatible with those multiplier pressures.
- The survey cites Xiang-Chen bounds on multiplier-group size, which can sharpen any orbit-based obstruction once a candidate multiplier subgroup is forced.

### toy_example
Start with the quotient counts modulo 19 or modulo 37 in C_703 and check whether any orbit partition compatible with a 5- or 7-multiplier can hit total size 325 and the required autocorrelation counts.

### known_obstruction
The row survives the standard multiplier-survey filters, so a successful proof must sharpen the existing cyclic orbit bookkeeping rather than merely replay the tabulated eliminations.

### prior_work_stop_sentence
Gordon-Schmidt list (703,325,150) in the cyclic group [703] as open in Table 2.

### recommended_first_attack
Combine contracted residue-count equations for w = 19 and w = 37 with the 5- and 7-multiplier orbit structure to rule out every feasible integer pattern for the contracted coefficients.

### paper_if_solved
If solved exactly, the paper would be a short cyclic residual-row note closing the Table 2 case (703,325,150).
