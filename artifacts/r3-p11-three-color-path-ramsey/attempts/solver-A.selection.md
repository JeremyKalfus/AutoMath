# Determine the exact value of R(P11, P11, P11)

- entry_type: `paper_candidate`
- slug: `r3-p11-three-color-path-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 6.4.1.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Settling the next exact three-color path value after the already-audited P10 residue would still read like the title theorem of a short Ramsey note rather than a feeder computation.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `81`
- single_solve_to_paper_fraction: `0.74`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `small`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r3-p11-three-color-path-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note for the next unsolved three-color path parameter beyond the preserved P10 attempt.`

## question
Is R(P11, P11, P11) = 21?

## canonical_statement
Determine the exact value of R(P11, P11, P11).

## intended_statement
Either prove that every 3-coloring of K21 contains a monochromatic P11, or construct a 3-coloring of K21 with no monochromatic P11 and thus show R(P11, P11, P11) >= 22.

## pre_solve_gate_reason
The latest Ramsey survey still treats the exact three-color path formula as open beyond the verified small range, and the P11 slice remains a single bounded theorem rather than a campaign prerequisite.

## micro_paper_assessment
Pass. The claim is still bounded, still title-theorem-sized, and still anchored to a named exact-value family; unlike a raw census target, the surrounding paper narrative is already essentially written once the exact proof lands.

## hypothetical_title
The Exact Value of R(P11, P11, P11)

## hypothetical_abstract
We determine the exact three-color Ramsey number R(P11, P11, P11). The current Ramsey survey dated January 6, 2026 records the Faudree-Schelp path formula as unresolved beyond the previously verified small cases and does not list a later exact value for P11. Our result fixes the next bounded residue in the three-color path table and sharpens the exact small-parameter record by one step.

## single_solve_paper_explanation
A successful exact determination would already be the title theorem, because the conjectural value, neighboring solved cases, and standard constructions are all part of the existing narrative. What remains after the solve is mostly exposition, comparison with smaller cases, and either the extremal coloring or the final forcing argument. This is close to the 70-90% paper target because the mathematical content concentrates in the one exact theorem.

## broader_theorem_nonimplication_note
The available asymptotic three-color path theorem does not settle n = 11, and the survey's cycle-to-path transfer only addresses special odd-path implications rather than a full exact P11 theorem.

## literature_gap
Radziszowski's January 6, 2026 survey records exact small three-color path results only for the previously verified initial range and does not list an exact value for R(P11, P11, P11).

## publication_packet_title
The Exact Value of R(P11, P11, P11)

## publication_packet_frontier_basis
Radziszowski's January 6, 2026 survey records the Faudree-Schelp three-color path formula as verified only through smaller n and does not report an exact resolution of the P11 case.

## publication_packet_near_paper_reason
The surrounding formula, construction heuristics, and neighboring small cases are already in place. Once the exact P11 value is fixed, the note mostly needs the sharp proof or one extremal witness plus a short comparison with the solved lower parameters.

## publication_packet_literature_scope
Radziszowski DS1.18 Section 6.4.1, the survey's cited Faudree-Schelp and Gyarfas-Ruszinko-Sarkozy-Szemeredi path results, and bounded 2026-04-13 web searches for exact notation R(P11,P11,P11), alias notation R_3(P11), and recent status signals.

## publication_packet_artifact_requirements
Either a proof that every 3-coloring of K21 contains a monochromatic P11, or one explicit 21-vertex three-coloring with no monochromatic P11.

## paper_shape
A one-theorem exact-value note for the next unsolved three-color path parameter beyond the preserved P10 attempt.

## transfer_kit

### usable_lemmas
- Radziszowski's January 6, 2026 survey records the conjectural three-color path formula R(Pn, Pn, Pn) = 2n - 2 + (n mod 2) for all sufficiently large n.
- The same survey records that the small exact cases were settled only through the earlier verified range and does not report an exact value for P11.
- The survey notes only a restricted cycle-to-path implication for odd paths, which prevents the P11 case from collapsing automatically to a previously solved cycle theorem.

### toy_example
The neighboring conjectural value for P10 is 18 and for P11 is 21, so the first nontrivial benchmark is to compare any proposed P11 argument with the already-studied small path residues at 18-21 vertices.

### known_obstruction
Any proof must control near-extremal three-colorings of K21 that mimic the standard path-avoiding templates, while any disproof must produce a tight 21-vertex coloring with no monochromatic P11.

### prior_work_stop_sentence
Radziszowski's January 6, 2026 survey does not list an exact value for R(P11, P11, P11) after summarizing only the previously verified initial three-color path cases.

### recommended_first_attack
Start from the lower-bound coloring pattern behind the Faudree-Schelp formula and perform a stability analysis on how one extra vertex or one extra block interaction forces a monochromatic P11.

### paper_if_solved
The paper would be a short exact-value Ramsey note fixing the next unresolved three-color path parameter.
