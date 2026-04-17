# Does the abelian group C_4 x C_112 admit a (448,150,50)-difference set?

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-448-150-50-group-4-112`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (448,150,50) in group [4,112] after the survey's multiplier-based eliminations.`
- open_status_checked_on: `2026-04-15`
- publication_if_solved: `Settling the exact group row (448,150,50) in C_4 x C_112 would already read like a short residual-case note in the multiplier-conjecture lane; after the proof, only a brief comparison with the sibling 448 rows and earlier eliminated 448-group types would remain.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `86`
- single_solve_to_paper_fraction: `0.79`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
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
- working_packet_path: `artifacts/abelian-difference-set-448-150-50-group-4-112/working_packet.md`
- paper_shape: `An exact residual-group difference-set note closing one Table 2 row from the multiplier-conjecture survey.`

## question
Does the abelian group C_4 x C_112 admit a (448,150,50)-difference set?

## canonical_statement
Determine whether the abelian group C_4 x C_112 admits a (448,150,50)-difference set.

## intended_statement
Determine whether the abelian group C_4 x C_112 admits a (448,150,50)-difference set.

## pre_solve_gate_reason
This is an exact source-anchored open row with a stable theorem slice, cheap novelty surface, and a paper story that mostly consists of the solve itself plus a short comparison paragraph about the other 448 groups.

## micro_paper_assessment
This is a clean lane-eligible packet: exact group-specific residue, stable theorem slice, low packaging burden, and a plausible short-note title that survives the proof-genericity stress test.

## hypothetical_title
On (448,150,50) difference sets in C_4 x C_112

## hypothetical_abstract
We determine whether the abelian group C_4 x C_112 admits a (448,150,50)-difference set. Gordon and Schmidt list this exact row as open in Table 2 of their multiplier-conjecture survey, while Arasu's earlier nonexistence results for several other groups of order 448 leave the [4,112] case unresolved. The result therefore closes a precise residual case in the order-448 difference-set classification rather than merely adding a tiny isolated example.

## single_solve_paper_explanation
The exact solve would already supply the title theorem, the core proof, and the main novelty claim of the paper. The remaining writeup is bounded to source-faithful positioning: one short introduction, one paragraph on the sibling 448 rows, and the proof itself. This is the right 70-90% lane because there is no feeder ladder and no need for a broader campaign to make the note publishable.

## broader_theorem_nonimplication_note
The canonical survey presents [4,112] as an explicit residual row after the available multiplier-based eliminations, and the outside-source Arasu paper only removes other 448-group decompositions such as C_4 x C_4 x C_4 x C_7 and C_8 x C_2 x C_2 x C_2 x C_7. The surfaced literature therefore does not already imply the [4,112] case, and the exact group structure is part of the honest theorem slice.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt Table 2 keeping the exact row (448,150,50) in group [4,112] open; the bounded 2026-04-15 exact-tuple, alternate-notation, and recent-status sweep surfaced no later targeted settlement, while Arasu 2000 only settles different 448-group types.

## publication_packet_title
The (448,150,50) difference-set problem in C_4 x C_112

## publication_packet_frontier_basis
Gordon-Schmidt Table 2 still lists the exact group row [4,112] at parameters (448,150,50) as open, while Arasu's 2000 nonexistence paper removes several other 448-group types without settling this one.

## publication_packet_near_paper_reason
One exact proof would already close a cited residual row from a canonical open table. What remains after the solve is light: explain how this row sits relative to the sibling 448 rows and cite the earlier eliminated 448 decompositions.

## publication_packet_literature_scope
Gordon-Schmidt 2016 Table 2, Arasu 2000 Proposition 4 on nonexistence for several other 448-group types, the La Jolla Difference Set Repository status pages, and the bounded 2026-04-15 exact-tuple and alternate-notation sweep plus Gordon's publications page through 2025.

## publication_packet_artifact_requirements
A proof or counterexample for C_4 x C_112, the decisive multiplier-or-quotient contradiction or explicit construction, and a short paragraph locating the result among the other order-448 group rows.

## paper_shape
An exact residual-group difference-set note closing one Table 2 row from the multiplier-conjecture survey.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt 2016 Table 2 lists the exact row (448,150,50) in group [4,112] as open after the survey's multiplier computations.
- The same survey is expressly a residual-status paper for the multiplier conjecture, so Table 2 functions as a canonical post-theorem open list rather than a raw parameter dump.
- Arasu 2000 Proposition 4 proves nonexistence for several other groups of order 448 with the same parameters, showing that the 2-primary decomposition matters and leaving [4,112] as a genuine exact residue.

### toy_example
Project C_4 x C_112 onto its quotient of order 7 by the Sylow-2 subgroup; the seven fiber counts lie in [0,64], sum to 150, and must satisfy the contracted second-moment identity n + lambda*(v/7) = 100 + 50*64 = 3300.

### known_obstruction
Arguments that depend only on the order 448 and n = 100 are too coarse, because earlier papers already separate the various 448-group types; the proof has to see the exact 2-primary structure of C_4 x C_112.

### prior_work_stop_sentence
After the survey's multiplier-based eliminations and Arasu's nonexistence results for other order-448 groups, the exact row (448,150,50) in group [4,112] still appears as open in Gordon-Schmidt Table 2.

### recommended_first_attack
Exploit the 5-multiplier pressure coming from n = 100 together with a quotient-by-Sylow-2 contraction to the order-7 factor, then test whether the resulting orbit-count equations can coexist with the group-ring identities in C_4 x C_112.

### paper_if_solved
If solved exactly, the paper would be a short residual-case note on (448,150,50) difference sets in C_4 x C_112 with a brief comparison to the sibling order-448 rows.
