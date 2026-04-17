# Untitled Entry

- entry_type: `paper_candidate`
- slug: `cyclic-difference-set-639-232-84`
- worker_role: `solver-A`
- canonical_source: `Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing possible cyclic cases with 150 <= k <= 300 and gcd(v,n)=1; status rechecked against Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), Table 2.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle another small cyclic survivor that persisted from Baumert-Gordon's k <= 300 table into the 2015 multiplier-status survey.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short-medium`
- single_pass_proof_plausibility: `low`
- paper_leverage_score: `76`
- single_solve_to_paper_fraction: `0.73`
- title_theorem_strength: `moderate`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
- broader_theorem_implication_risk: `moderate`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `moderate`
- packaging_risk: `moderate`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/cyclic-difference-set-639-232-84/working_packet.md`
- paper_shape: `A compact exact-case note on the cyclic (639,232,84) problem.`

## question
Does the cyclic group of order 639 admit a (639,232,84)-difference set?

## canonical_statement
Determine whether the cyclic group C_639 admits a (639,232,84)-difference set.

## intended_statement
Determine whether the cyclic group C_639 admits a (639,232,84)-difference set.

## pre_solve_gate_reason
The candidate is still source-anchored and stable enough to count as a plausible title theorem, although the narrative is slightly weaker than for the two smallest cases.

## micro_paper_assessment
Lane-eligible, but weaker than the first two choices. The family anchor is strong, yet the exact theorem is a little more table-row-shaped.

## hypothetical_title
On Cyclic (639,232,84) Difference Sets

## hypothetical_abstract
We determine whether the cyclic group of order 639 admits a (639,232,84)-difference set. This parameter survives Baumert-Gordon's k <= 300 cyclic search and remains present in Gordon-Schmidt's 2015 list of open difference-set parameters. The result would close a clearly documented residual case with a short, exact-case paper.

## single_solve_paper_explanation
The tuple is already isolated in the literature, so an exact proof would contribute the core mathematics and most of the novelty of the final note. Remaining work would consist of comparing the cyclic [639] case with the distinct noncyclic [3,213] row and explaining why existing multiplier tools stop short. That is still inside the micro-paper band, though less crisp than the smaller 465 and 469 cases.

## broader_theorem_nonimplication_note
The later survey explicitly continues to list both the cyclic and noncyclic group types for this parameter, showing that the published multiplier machinery does not collapse the exact cyclic theorem into an already-known ambient statement.

## literature_gap
Prior work stops at listing the cyclic [639] realization of (639,232,84) as open in Baumert-Gordon 2004 and Gordon-Schmidt 2015.

## publication_packet_title
The Cyclic (639,232,84) Difference-Set Problem

## publication_packet_frontier_basis
Baumert-Gordon 2004 retain (639,232,84) in Table 3, and Gordon-Schmidt 2015 still list both [639] and the noncyclic variant [3,213] as open.

## publication_packet_near_paper_reason
An exact cyclic resolution would already remove one residual row from a canonical open table and would need only bounded contextualization around the older elimination program.

## publication_packet_literature_scope
Baumert-Gordon 2004 for the original cyclic table; Gordon-Schmidt 2015 for later open-status confirmation and multiplier-theorem context.

## publication_packet_artifact_requirements
A concise proof in C_639, ideally multiplier-driven or cyclotomic, together with a literature audit that distinguishes the cyclic [639] case from the separate abelian [3,213] variant.

## paper_shape
A compact exact-case note on the cyclic (639,232,84) problem.

## transfer_kit

### usable_lemmas
- Baumert-Gordon's contracted coefficient equations apply to every divisor w of 639 and convert a putative cyclic difference set into a short integer correlation system.
- Their search pipeline already absorbs the standard Schutzenberger, BRC, Mann, Lander, and Yamamoto tests before declaring the case open.
- Gordon-Schmidt 2015 record both [639] and [3,213] as unresolved, clarifying that group type matters and that a cyclic proof is not automatically inherited from a broader abelian theorem.

### toy_example
Use a small cyclic difference set to show how one compares the coefficient vector for [v] with that of a noncyclic group of the same order; this matters here because [639] and [3,213] must be separated.

### known_obstruction
The cyclic case coexists in the survey with a distinct noncyclic open row, so a final proof has to use structure special to C_639 rather than only parameter arithmetic.

### prior_work_stop_sentence
Baumert-Gordon keep (639,232,84) in Table 3, and Gordon-Schmidt still list [639] as open in Table 2.

### recommended_first_attack
Use the prime factors of n = 148 to force or obstruct candidate multipliers in C_639, then apply the contracted coefficient equations at divisors 3, 9, and 71.

### paper_if_solved
If solved exactly, the paper would be a short exact-case note separating the cyclic group of order 639 from the remaining open abelian variants.
