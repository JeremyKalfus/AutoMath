# Determine the exact value of R(C9, C9, C9)

- entry_type: `paper_candidate`
- slug: `r3-c9-odd-cycle-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, revision dated June 7, 2024), Section 6.3.1, together with the Bondy-Erdős odd-cycle line recorded there and bounded 2026-04-13 web checks.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Settling the first publicly recorded open three-color odd-cycle diagonal case would read immediately as the title theorem of a short Ramsey note rather than as feeder evidence.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `87`
- single_solve_to_paper_fraction: `0.83`
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
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r3-c9-odd-cycle-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on the first open three-color odd-cycle diagonal Ramsey number.`

## question
Is R(C9, C9, C9) = 33?

## canonical_statement
Determine the exact value of R(C9, C9, C9).

## intended_statement
Either prove that every 3-coloring of K33 contains a monochromatic C9, or construct a 3-coloring of K33 with no monochromatic C9 and thus show R(C9, C9, C9) >= 34.

## pre_solve_gate_reason
The web-accessible survey still identifies C9 as the first open three-color odd-cycle case, the conjectural value is already fixed, and one sharp resolution would essentially determine the paper.

## micro_paper_assessment
Pass. This is a named first-open-case slice in a flagship exact-value family, and one clean solve would already look like the full short paper rather than a remark or a campaign stepping stone.

## hypothetical_title
The Exact Value of R(C9, C9, C9)

## hypothetical_abstract
We determine the exact three-color Ramsey number R(C9, C9, C9). The publicly accessible Ramsey survey revision of June 7, 2024 records C9 as the first open odd-cycle diagonal case and gives only the lower bound 33 together with sufficiently-large odd-cycle results. Our theorem fixes the first unresolved bounded odd-cycle entry in the three-color table and tests the Bondy-Erdős 4n-3 prediction at its smallest open parameter.

## single_solve_paper_explanation
If the exact C9 value is determined, the resulting theorem is already the title and the core contribution of the note. The conjectural target, the nearest solved benchmark C7, and the large-n odd-cycle context are standard, so the post-solve work is mostly exposition and critical-coloring discussion. This is squarely inside the 70-90% paper window because the mathematical burden is concentrated in one bounded diagonal theorem.

## broader_theorem_nonimplication_note
The sufficiently-large odd-cycle theorem recorded in the survey only applies for large odd n and does not settle the bounded C9 slice, while the classical Bondy-Erdős conjectural formula supplies only the target value 33, not an exact proof.

## literature_gap
The June 7, 2024 Ramsey survey states that the first open three-color odd-cycle diagonal case is R(C9, C9, C9), known only to satisfy R(C9, C9, C9) >= 33.

## publication_packet_title
The Exact Value of R(C9, C9, C9)

## publication_packet_frontier_basis
The June 7, 2024 Ramsey survey says the first open three-color odd-cycle diagonal case is R3(C9), with lower bound 33 and only sufficiently-large odd-cycle theorems beyond that; bounded 2026-04-13 web checks found no later exact-resolution paper for C9.

## publication_packet_near_paper_reason
The conjectural target 33, the lower-bound construction template, and the large-n odd-cycle backdrop are already in place. Once the exact C9 value is settled, what remains is a short extremal discussion and comparison with the solved C7 case.

## publication_packet_literature_scope
Radziszowski DS1.17 Section 6.3.1; the Bondy-Erdős odd-cycle conjecture record; the UCSD Erdős problem page on three-color cycle Ramsey numbers; and bounded 2026-04-13 searches for exact and alternate notation of the C9 diagonal case.

## publication_packet_artifact_requirements
Either a proof that every 3-coloring of K33 contains a monochromatic C9, or one explicit 33-vertex coloring with no monochromatic C9.

## paper_shape
A one-theorem exact-value note on the first open three-color odd-cycle diagonal Ramsey number.

## transfer_kit

### usable_lemmas
- Radziszowski DS1.17 states that if the Bondy-Erdős odd-cycle prediction holds, then R(Cn, Cn, Cn) = 4n - 3 for odd n, and it identifies C9 as the first open diagonal case.
- The same survey records the exact solved predecessor R(C7, C7, C7) = 25.
- The survey records that R(Cn, Cn, Cn) = 4n - 3 for sufficiently large odd n, so the only remaining difficulty is the bounded small-parameter residue.

### toy_example
The nearest solved odd-cycle benchmark is R(C7, C7, C7) = 25, while the conjectural C9 target is 33.

### known_obstruction
Any upper-bound proof must rule out 33-vertex colorings built from the standard odd-cycle blowup templates, while a disproof must exhibit one explicit 33-vertex witness with no monochromatic C9.

### prior_work_stop_sentence
The June 7, 2024 Ramsey survey states that the first open three-color odd-cycle diagonal case is R(C9, C9, C9), known only to satisfy R(C9, C9, C9) >= 33.

### recommended_first_attack
Start from the 32-vertex lower-bound blowup pattern behind the 4n - 3 conjecture and run a stability argument showing that every 33-vertex extension already forces a monochromatic 9-cycle.

### paper_if_solved
The paper would be a short exact-value note closing the first open three-color odd-cycle diagonal Ramsey number.
