# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-847-423-211-group-11-77`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), especially Table 2 listing the exact open row (847,423,211) in group [11,77].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle the exact Table 2 row (847,423,211) in the noncyclic group C_11 x C_77.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `low`
- paper_leverage_score: `74`
- single_solve_to_paper_fraction: `0.74`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `moderate`
- formalization_overhead: `moderate`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/abelian-difference-set-847-423-211-group-11-77/working_packet.md`
- paper_shape: `A short exact-group obstruction/existence note for one named Table 2 survivor.`

## question
Does the abelian group C_11 x C_77 admit a (847,423,211)-difference set?

## canonical_statement
Determine whether the abelian group C_11 x C_77 admits a (847,423,211)-difference set.

## intended_statement
Determine whether the abelian group C_11 x C_77 admits a (847,423,211)-difference set.

## pre_solve_gate_reason
The theorem slice is exact, source-anchored, group-specific, and already reads like the title theorem of a short note; after a solve, only light survey framing would remain.

## micro_paper_assessment
Lane-eligible. The solve would close an exact survey row in a specific group, and that one theorem already looks like the body of a short note.

## hypothetical_title
On the (847,423,211) Difference-Set Problem in C_11 x C_77

## hypothetical_abstract
We determine whether the abelian group C_11 x C_77 admits a (847,423,211)-difference set. Gordon and Schmidt list this exact group-specific row as open in Table 2 of their multiplier-conjecture survey. A proof would close one named survivor in a canonical residual table and would leave only light contextual exposition after the mathematics is done.

## single_solve_paper_explanation
This target is already a one-row theorem packet rather than a feeder instance. If solved, the exact theorem would naturally become the title theorem, with the remaining writing limited to source context, notation, and a short comparison with the survey table. The family anchor is strong enough that the result would read as more than an isolated curiosity.

## broader_theorem_nonimplication_note
The bounded audit surfaced the exact row as still open in Gordon-Schmidt's Table 2, and the theorem slice is tied to the noncyclic group [11,77] rather than a broader ambient class already shown settled in the surfaced literature.

## literature_gap
Prior work surfaced in this audit stops at listing the exact group-specific row (847,423,211) in [11,77] as open in Table 2 of Gordon-Schmidt 2015; the bounded exact-tuple search on 2026-04-15 surfaced no later direct settlement.

## publication_packet_title
On the (847,423,211) Difference-Set Problem in C_11 x C_77

## publication_packet_frontier_basis
Gordon-Schmidt 2015 Table 2 lists the row (847,423,211) in group [11,77] as open, and the bounded exact-tuple web sweep on 2026-04-15 surfaced no later direct settlement.

## publication_packet_near_paper_reason
The source already isolates one exact group row, so a clean existence or nonexistence proof would itself supply the central theorem and most of the note.

## publication_packet_literature_scope
Gordon-Schmidt 2015 Table 2, the Dan Gordon difference-set repository landing page, and the bounded exact-tuple web sweep on 2026-04-15.

## publication_packet_artifact_requirements
A compact proof in C_11 x C_77, the relevant orbit or quotient bookkeeping, and a short explanation of why the survey row remained open.

## paper_shape
A short exact-group obstruction/existence note for one named Table 2 survivor.

## transfer_kit

### usable_lemmas
- Gordon-Schmidt's multiplier-survey toolkit reduces exact open rows by forcing numerical multipliers and then analyzing orbit structure in the ambient group.
- Any translate fixed by a multiplier subgroup can be written as a union of its orbits, so orbit lengths in C_11 x C_77 become immediate size constraints on a putative difference set.
- The Table 2 row exposes the group type [11,77], so quotienting to the 11-part and 7-part factors gives a small number of structurally distinguished projections.

### toy_example
Work first with orbit counts for a smaller multiplier action on C_11 x C_7 to see how a union-of-orbits obstruction can force the wrong total size.

### known_obstruction
The row already survives the survey's existing multiplier and standard necessary-condition filters, so any proof must exploit sharper orbit bookkeeping than the generic table machinery alone.

### prior_work_stop_sentence
Gordon-Schmidt list (847,423,211) in group [11,77] as open in Table 2.

### recommended_first_attack
Translate a putative set so that a maximal surfaced multiplier subgroup fixes it, then test whether the resulting orbit partition on C_11 x C_77 can realize size 423 and the required difference multiplicities.

### paper_if_solved
If solved exactly, the paper would be a short note closing the Table 2 row (847,423,211) in C_11 x C_77.
