# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-990-345-120`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the Ryser-conjecture slide listing (990,345,120,225) among the small open cyclic cases and the Lander-conjecture slide listing the exact 990 row [2,G9,5,11].`
- open_status_checked_on: `2026-04-16`
- publication_status: `NONE`
- publication_if_solved: `A decisive existence or nonexistence result for the cyclic (990,345,120) case would read like the title theorem of a short residual-case note tied to Gordon's small open cyclic list.`
- publication_if_solved_score: `solve_is_basically_the_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `86`
- single_solve_to_paper_fraction: `0.82`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `moderate`
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
- working_packet_path: `artifacts/cyclic-difference-set-990-345-120/working_packet.md`
- paper_shape: `A short note closing one named small open cyclic difference-set row.`

## question
Does the cyclic group C_990 admit a (990,345,120)-difference set?

## canonical_statement
Determine whether the cyclic group C_990 admits a (990,345,120)-difference set.

## intended_statement
Determine whether the cyclic group C_990 admits a (990,345,120)-difference set.

## pre_solve_gate_reason
The cyclic 990 row is source-anchored, a later 2019 status surface still names it as open, no exact local attempt conflict exists, and one exact solve would already supply essentially the whole note.

## micro_paper_assessment
Lane-eligible. The row is explicit, the paper story is immediate, and the later-status picture is strong enough for a live micro-paper solve attempt.

## hypothetical_title
On the cyclic (990,345,120) difference-set case

## hypothetical_abstract
We determine whether the cyclic group C_990 admits a (990,345,120)-difference set. Gordon's 2019 ArasuFest/LJDSR status slides still isolate this parameter row among the small open cyclic cases, with the same parameter set also appearing as a separate noncyclic residual row. A direct solution would close one named cell in the residual table and would leave only light contextual writeup around the main proof.

## single_solve_paper_explanation
The source packet already isolates the exact cyclic row, so one clean proof or disproof would provide the honest title theorem and nearly all of the paper's mathematics. What remains after the solve is mainly a short introduction, the polished proof, and a brief status discussion about the neighboring noncyclic 990 row. This is not a feeder instance: the solve itself is the paper-shaped contribution.

## broader_theorem_nonimplication_note
The 2019 status slides still separate the cyclic 990 row from the exact noncyclic [2,G9,5,11] row, so the honest theorem does not automatically collapse into a broader ambient classification result. A stronger all-group obstruction may exist, but the bounded audit did not surface one, and the cyclic slice remains explicitly named as a frontier residue.

## literature_gap
The surfaced 2019 status packet stops at listing the cyclic (990,345,120) row as open, and the capped 2026-04-16 exact/alternate search did not surface a later exact-tuple closure.

## publication_packet_title
The Cyclic (990,345,120) Difference-Set Case

## publication_packet_frontier_basis
Gordon's 2019 ArasuFest/LJDSR status slides still list (990,345,120,225) among the small open cyclic cases while separately naming an exact noncyclic 990 row.

## publication_packet_near_paper_reason
If the cyclic row is settled exactly, the theorem statement, frontier hook, and most of the mathematics are already determined by the residual-case packet.

## publication_packet_literature_scope
Gordon's 2019 ArasuFest/LJDSR slide packet, bounded exact-statement searches for "990,345,120" difference set and cyclic difference set 990 345 120 on 2026-04-16, and local attempt/source/paper/search memory.

## publication_packet_artifact_requirements
A cyclic proof or disproof, a clean multiplier-orbit or contracted-coefficient argument, and a compact status paragraph tying the 2019 residual table to the new theorem.

## paper_shape
A short note closing one named small open cyclic difference-set row.

## transfer_kit

### usable_lemmas
- The ArasuFest Ryser-conjecture slide explicitly lists (990,345,120,225) among the small open cyclic cases.
- The same slide packet separately lists the exact 990 noncyclic row [2,G9,5,11], so parameter-level arithmetic alone does not settle the cyclic slice.
- The same source family uses multiplier and character criteria as the first-line elimination tools for residual difference-set rows.
- The parameter arithmetic n = k - lambda = 225 supplies immediate 3-part and 5-part multiplier pressure on quotient contractions of C_990.

### toy_example
Contract a hypothetical cyclic set modulo 45 or 90 and test whether the 3- and 5-orbit counts can satisfy the group-ring equations with k = 345 and lambda = 120.

### known_obstruction
Any cyclic solution must reconcile simultaneous 3-part and 5-part multiplier structure with the 2 and 11 factors of C_990.

### prior_work_stop_sentence
Gordon's 2019 status slides still list the cyclic (990,345,120) row as open among the small Ryser-conjecture cases.

### recommended_first_attack
Normalize by a 3- or 5-multiplier, contract to a quotient on the 45- or 90-part, and force the orbit counts against the difference-set equations.

### paper_if_solved
If solved exactly, the paper would be a short note closing the cyclic 990 residual row in Gordon's small open table.
