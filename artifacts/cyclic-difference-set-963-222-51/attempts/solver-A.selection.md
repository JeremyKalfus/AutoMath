# Does the cyclic group C_963 admit a (963,222,51)-difference set?

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-963-222-51`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially the Ryser-conjecture slide listing the cyclic row (963,222,51,171) among the small open cases and the Lander-conjecture slide listing the exact group [9,107] as a smallest open case with p = 3.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Closing the exact cyclic (963,222,51) / [9,107] row would already yield a paper-shaped note because the case is explicitly isolated in the La Jolla open-case slides and bounded 2026-04-15 status checks surfaced no later exact closure.`
- publication_if_solved_score: `solve_is_basically_the_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium-high`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.78`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
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
- working_packet_path: `artifacts/cyclic-difference-set-963-222-51/working_packet.md`
- paper_shape: `Exact one-row closure note for a named small cyclic Ryser/Lander residue.`

## question
Does the cyclic group C_963 admit a (963,222,51)-difference set?

## canonical_statement
Determine whether the cyclic group C_963 admits a (963,222,51)-difference set.

## intended_statement
Determine whether the cyclic group C_963 admits a (963,222,51)-difference set.

## pre_solve_gate_reason
Thin local memory across memory/attempt_registry.json, memory/source_registry.json, memory/search_memory.json, memory/paper_memory.json, failed_problems.json, and the current artifact slug list shows no exact or near-duplicate attempted problem for the cyclic (963,222,51) / [9,107] row. Gordon's 2019 La Jolla slides still isolate the row as open, and the bounded 2026-04-15 exact-tuple, alternate-notation, and recent-status web sweeps surfaced no later exact closure. Because this queue was empty at the start of the run, this packet is restored as the top slot and is the sole strict lane survivor in the current audited shortlist.

## micro_paper_assessment
This is the only strict lane survivor in the current five-slot shortlist. The theorem slice is stable, the family anchor is strong, the solve-to-publication distance is short, and the bounded status audit did not surface either a local attempt conflict or a later exact closure. If solved exactly, this would honestly read like the title theorem of a short note rather than a feeder instance.

## hypothetical_title
The cyclic (963,222,51) difference-set case

## hypothetical_abstract
We study the exact cyclic difference-set case (963,222,51), listed by Gordon among the small open residues for Ryser-type and Lander-type cyclic difference-set questions. We determine the existence question by combining multiplier restrictions with contraction data forced on the 9- and 107-quotients. This closes one of the smallest named cyclic residues in the La Jolla open-case tables.

## single_solve_paper_explanation
The row is already isolated by a canonical source and already carries a recognizable family anchor. If the exact cyclic case is settled, most of the paper is present immediately: statement, motivation, literature stop line, and main theorem. What remains is mainly exposition and the bounded novelty-audit record.

## broader_theorem_nonimplication_note
The surfaced literature did not reveal a broader theorem eliminating all remaining small cyclic Ryser/Lander residues, and the exact order-963 row is still singled out rather than absorbed by a generic closed family.

## literature_gap
Prior work surfaced in this curation run stops at listing the exact cyclic row (963,222,51) / [9,107] as open; the bounded 2026-04-15 search did not surface a later exact resolution.

## publication_packet_title
The cyclic (963,222,51) difference-set case

## publication_packet_frontier_basis
Gordon's 2019 La Jolla slides still isolate (963,222,51) as a small open cyclic case and as the exact [9,107] residue, and bounded 2026-04-15 status checks surfaced no later exact closure.

## publication_packet_near_paper_reason
If the exact cyclic row is settled, the title theorem, literature gap, and family anchor are already fixed by the source. What remains is mainly exposition and the bounded novelty-audit record, not a feeder ladder or a second mathematical campaign.

## publication_packet_literature_scope
Gordon's 2019 La Jolla repository slides for the exact frontier statement, together with bounded 2026-04-15 exact-tuple and status searches to confirm that no later exact closure surfaced.

## publication_packet_artifact_requirements
Either a cyclic construction in C_963 or a compact nonexistence proof using multiplier, quotient, or character constraints, together with a short note recording the bounded no-closure status audit.

## paper_shape
Exact one-row closure note for a named small cyclic Ryser/Lander residue.

## transfer_kit

### usable_lemmas
- Counting gives n = k - lambda = 171 and the group-ring identity D D^(-1) = n + lambda G.
- Cyclic difference sets admit strong numerical multiplier restrictions, as emphasized in the La Jolla repository sources and the multiplier literature cited there.
- Contractions to quotients such as C_9 and C_107 preserve rigid character-value constraints that can be checked without a broad search campaign.
- The row has already survived the standard easy filters in the canonical open-case tables, so any proof starts beyond the basic BRC and Schutzenberger tests.

### toy_example
The order factorization 963 = 9 * 107 gives the smallest nontrivial quotient pattern to test first; a hypothetical cyclic set would have tightly constrained images in C_9 and C_107.

### known_obstruction
Multiplier and quotient-profile constraints appear rigid enough that one bad contraction profile could force immediate nonexistence.

### prior_work_stop_sentence
Gordon's 2019 La Jolla slides still list (963,222,51) / [9,107] as an exact open cyclic residue, and bounded 2026-04-15 status searches surfaced no later exact closure.

### recommended_first_attack
Push the multiplier group and quotient contractions to C_9 and C_107 far enough to force an impossible orbit or coefficient profile.

### paper_if_solved
If solved, the paper is a short exact closure note for one of the named small cyclic residues in the La Jolla open-case tables.
