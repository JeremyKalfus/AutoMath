# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-469-208-92`
- worker_role: `solver-B`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing possible cyclic cases with 150 <= k <= 300 and gcd(v,n)=1; status rechecked against Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), Table 2.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would remove one of the smallest cyclic gcd(v,n)=1 survivors from Baumert-Gordon's k <= 300 table that still appears as open in the 2015 multiplier survey.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `84`
- single_solve_to_paper_fraction: `0.79`
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
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/cyclic-difference-set-469-208-92/working_packet.md`
- paper_shape: `A short residual cyclic-difference-set paper anchored on the exact (469,208,92) theorem.`

## question
Does the cyclic group of order 469 admit a (469,208,92)-difference set?

## canonical_statement
Determine whether the cyclic group C_469 admits a (469,208,92)-difference set.

## intended_statement
Determine whether the cyclic group C_469 admits a (469,208,92)-difference set.

## pre_solve_gate_reason
The theorem slice is exact and stable, the family anchor is strong, and the current literature already identifies the tuple as a crisp unresolved survivor.

## micro_paper_assessment
Lane-eligible. The candidate is exact, source-anchored, and close enough to paper-shaped that one solve would carry the note.

## hypothetical_title
On the Cyclic (469,208,92) Difference-Set Problem

## hypothetical_abstract
We determine whether the cyclic group of order 469 admits a (469,208,92)-difference set. This parameter appears in Baumert-Gordon's list of unresolved cyclic cases with 150 <= k <= 300 and remains open in Gordon-Schmidt's 2015 multiplier-status table. The result therefore closes a canonical small-parameter cyclic residue and yields a naturally paper-shaped note.

## single_solve_paper_explanation
The canonical source already packages the problem as a residual exact case, and the later survey confirms that it remained unsolved after additional multiplier-theorem progress. A complete proof would therefore provide the central mathematics and most of the novelty burden of the final note. The post-solve work is light framing rather than a further theorem campaign.

## broader_theorem_nonimplication_note
Baumert-Gordon's entire table-construction pipeline and the later multiplier-survey machinery both leave [469] unresolved, so the exact cyclic case is not already forced by the broader published theorems surfaced in this audit.

## literature_gap
Prior work stops at recording the cyclic parameter (469,208,92) as open in Baumert-Gordon 2004 and Gordon-Schmidt 2015.

## publication_packet_title
The Cyclic (469,208,92) Difference-Set Case

## publication_packet_frontier_basis
Baumert-Gordon 2004 list (469,208,92) in Table 3, and Gordon-Schmidt 2015 still list [469] among the smallest open difference-set parameters.

## publication_packet_near_paper_reason
An exact resolution would already be a clean title theorem with bounded follow-up exposition because the ambient family and residual status are fully source-anchored.

## publication_packet_literature_scope
Baumert-Gordon 2004 for the original small-parameter cyclic table and proof toolkit; Gordon-Schmidt 2015 for later open-status confirmation and multiplier framing.

## publication_packet_artifact_requirements
Either a compact nonexistence proof in C_469 or an explicit cyclic construction, plus a brief source-faithful audit showing that previously published filters leave the case unresolved.

## paper_shape
A short residual cyclic-difference-set paper anchored on the exact (469,208,92) theorem.

## transfer_kit

### usable_lemmas
- Baumert-Gordon's table-building starts from the standard parameter identity and the classical necessary conditions for cyclic difference sets.
- Their Section 3 gives the coefficient-vector equations for contracted polynomials theta[w](x), which are often enough to force contradictions for specific divisors w of v.
- Gordon-Schmidt 2015 identify the relevant prime divisors of n = 116 and frame the residual obstruction in multiplier language.
- The Xiang-Chen bound on cyclic multiplier groups, cited in later difference-set work, constrains any successful multiplier configuration once a candidate multiplier is forced.

### toy_example
Work out the coefficient equations for a small cyclic difference set modulo a divisor w to illustrate how a polynomial reduction translates existence into a short integer-feasibility problem.

### known_obstruction
Neither the standard small-parameter filters nor the later multiplier-survey machinery eliminates the case, so the final argument must extract a sharper orbit or cyclotomic obstruction.

### prior_work_stop_sentence
Baumert-Gordon list (469,208,92) as open in Table 3, and Gordon-Schmidt still list [469] as open in Table 2.

### recommended_first_attack
Exploit the factorization n = 4 * 29 and v = 7 * 67 to force a new multiplier or contracted multiplier, then test the resulting orbit counts against the contracted coefficient equations.

### paper_if_solved
If solved exactly, the paper would be a short note closing one of the smallest unresolved cyclic k <= 300 cases.
