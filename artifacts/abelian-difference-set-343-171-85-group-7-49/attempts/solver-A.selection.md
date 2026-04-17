# Does the abelian group C_7 x C_49 admit a (343,171,85)-difference set?

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-343-171-85-group-7-49`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (343,171,85) in group [7,49].`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Settling the exact group row in C_7 x C_49 would likely produce a short note separating the open [7,49] case from the known Paley realization at the same parameters.`
- publication_if_solved_score: `solve_is_basically_the_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.82`
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
- working_packet_path: `artifacts/abelian-difference-set-343-171-85-group-7-49/working_packet.md`
- paper_shape: `A short exact-group note on the open [7,49] row at the Paley parameters (343,171,85).`

## question
Does the abelian group C_7 x C_49 admit a (343,171,85)-difference set?

## canonical_statement
Determine whether the abelian group C_7 x C_49 admits a (343,171,85)-difference set.

## intended_statement
Determine whether the abelian group C_7 x C_49 admits a (343,171,85)-difference set.

## pre_solve_gate_reason
The exact row is source-anchored in Survey Table 2, the local attempt registry is clean, and Gordon's 2019 La Jolla Repository slides still list the [7,49] group as open while distinguishing the existing [7,7,7] Paley case. That combination is enough to treat this as a stable lane-eligible micro-paper packet.

## micro_paper_assessment
Best current lane survivor: exact statement, stable theorem slice, cheap literature gap, and a clear short-note narrative if solved.

## hypothetical_title
On (343,171,85) difference sets in C_7 x C_49.

## hypothetical_abstract
We determine whether the abelian group C_7 x C_49 admits a (343,171,85)-difference set. Gordon and Schmidt isolate the exact group row [7,49] as open in Table 2 of their multiplier-conjecture survey, while Gordon's 2019 La Jolla Repository slides still list the same row among the open existence cases. Because the same parameters already occur in the Paley group [7,7,7], a solution for C_7 x C_49 is immediately a group-specific structural theorem rather than a broad census remark.

## single_solve_paper_explanation
This packet is already almost paper-shaped because the source literature has done the enumeration and narrowed the frontier to one exact group row. Solving that row settles the title theorem, and the remaining writing is mostly comparison with the known Paley realization and brief exposition of the decisive obstruction or construction. There is no feeder ladder hiding behind the solve.

## broader_theorem_nonimplication_note
A broader parameter-only theorem cannot already settle the case because (343,171,85)-difference sets exist in the Paley group [7,7,7]; the open point is the exact group C_7 x C_49. The survey and 2019 slides both continue to distinguish the [7,49] row as unresolved.

## literature_gap
Gordon-Schmidt 2016 Table 2 lists the exact row (343,171,85) in group [7,49] as open, and Gordon's 2019 La Jolla Difference Set Repository slides still record 343 171 85 [7,49] among the open existence cases.

## publication_packet_title
On (343,171,85) Difference Sets in C_7 x C_49

## publication_packet_frontier_basis
Survey Table 2 isolates the exact row [7,49], and Gordon's 2019 La Jolla Repository slides still list 343 171 85 [7,49] among the open existence cases.

## publication_packet_near_paper_reason
If the exact [7,49] case is solved, the proof itself is the title theorem; what remains is only a short comparison with the known Paley realization in [7,7,7] and a brief explanation of why the group-sensitive obstruction is new.

## publication_packet_literature_scope
Survey Table 2 and surrounding multiplier-conjecture discussion, Gordon's 2019 La Jolla Difference Set Repository slides, the local attempt registry, and the bounded exact-tuple search surface.

## publication_packet_artifact_requirements
A proof or disproof for C_7 x C_49, the decisive character or quotient contradiction, and a short literature note contrasting the open [7,49] row with the known [7,7,7] Paley example.

## paper_shape
A short exact-group note on the open [7,49] row at the Paley parameters (343,171,85).

## transfer_kit

### usable_lemmas
- Survey Table 2 isolates the exact open group row (343,171,85) in [7,49].
- The survey's multiplier-conjecture framing gives the standard admissible-prime and quotient constraints already exhausted before the row reaches Table 2.
- Gordon's 2019 slides record the group-ring identity D D^(-1) = n + lambda G and the character criterion |chi(D)|^2 = n as the basic exact-row proof infrastructure.
- The 2019 slides also distinguish the existing Paley case [7,7,7], so any proof for [7,49] must exploit group structure rather than parameter admissibility alone.

### toy_example
Push a hypothetical set in C_7 x C_49 down to the quotient C_7 x C_7 and compare the resulting fiber sizes against the known Paley configuration on [7,7,7].

### known_obstruction
Because the parameters already exist in another abelian group, any nonexistence proof for C_7 x C_49 must be genuinely group-specific and cannot just replay parameter-level admissibility filters.

### prior_work_stop_sentence
Gordon-Schmidt Table 2 and Gordon's 2019 La Jolla slides both stop at listing [7,49] as an open exact group row for the parameters (343,171,85).

### recommended_first_attack
Use character divisibility and the quotient map C_7 x C_49 -> C_7 x C_7 to force fiber counts incompatible with the Paley shadow on the quotient.

### paper_if_solved
If solved, the paper would be a short exact-group note on the (343,171,85) problem in C_7 x C_49.
