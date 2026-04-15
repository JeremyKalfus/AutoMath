# Untitled Entry

- entry_type: `paper_candidate`
- slug: `bshm-120-12-12-0`
- worker_role: `solver-A`
- canonical_source: `Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Theorem 65, Remark 66, Table 5 on page 33, and Corollary 67 on page 34: the paper leaves (120,12,12,0) as the first open r = 5, s = 3 case in the Type 2 family BSHM(8rs,4s,4s,0).`
- open_status_checked_on: `2026-04-14`
- publication_status: `NONE`
- publication_if_solved: `A construction or obstruction for BSHM(120,12,12,0) would plausibly be publishable as a short note settling the first r = 5, s = 3 open case in the Type 2 BSHM(8rs,4s,4s,0) family.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `80`
- single_solve_to_paper_fraction: `0.79`
- title_theorem_strength: `moderate`
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
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/bshm-120-12-12-0/working_packet.md`
- paper_shape: `A single-theorem note on the first r = 5, s = 3 unresolved parameter in the Type 2 BSHM(8rs,4s,4s,0) family.`

## question
Does there exist a balanced splittable Hadamard matrix BSHM(120,12,12,0)?

## canonical_statement
Determine whether there exists a BSHM(120,12,12,0).

## intended_statement
Determine whether an order-120 Hadamard matrix exists that is balanced splittable with parameters (120,12,12,0).

## pre_solve_gate_reason
Thin repo memory and slug scans show no prior mathematical attempt for this exact tuple. In the canonical 2023 source, the PDF audit confirmed that Theorem 65 and Remark 66 account for the known Type 2 constructions, Corollary 67 leaves only odd r,s > 1 unresolved, and Table 5 on page 33 includes (120,12,12,0) as the next s = 3 odd-odd case after (72,12,12,0). A bounded 2026-04-14 web audit over exact-tuple and acronym-form searches for this tuple, together with family-level balanced-versus-balancedly wording, source-title, and citation-mirror searches, surfaced only the canonical EJC paper, generic bibliographic mirrors, or no parameter-specific settlement hit.

## micro_paper_assessment
Lane-eligible. This exact tuple has a stable family anchor, low packaging cost, and enough narrative support to function as the title theorem of a short note.

## hypothetical_title
The Parameter Set (120,12,12,0) for Balanced Splittable Hadamard Matrices

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (120,12,12,0). Jedwab, Li, and Simon showed that the Type 2 family BSHM(8rs,4s,4s,0) is resolved outside the odd-odd regime, and Table 5 lists (120,12,12,0) among the remaining unresolved parameters. Resolving this exact tuple would produce a short note because the family classification, neighboring positive cases, and exact frontier placement are already available in the source literature.

## single_solve_paper_explanation
The exact order-120 statement is already close to paper-shaped because it lies in an explicitly tabulated residual list rather than an amorphous broader program. Once the existence or nonexistence proof is known, the note mainly needs to summarize the Type 2 classification and present the certificate. That keeps the single solve well within the target publication fraction.

## broader_theorem_nonimplication_note
Corollary 67 settles the Type 2 family only outside the odd-odd regime. The tuple (120,12,12,0) has r = 5 and s = 3, so it lies inside the residual odd-odd branch and is not implied by the broader theorem.

## literature_gap
Current checked source literature leaves BSHM(120,12,12,0) unresolved as the first r = 5, s = 3 entry in Table 5 of the Type 2 family.

## publication_packet_title
The Parameter Set (120,12,12,0) for Balanced Splittable Hadamard Matrices

## publication_packet_frontier_basis
Theorem 65 and Remark 66 isolate the known Type 2 constructions, Corollary 67 leaves the odd-odd residue unresolved, and Table 5 records (120,12,12,0) as the first r = 5, s = 3 point in that residual list.

## publication_packet_near_paper_reason
If the order-120, s = 3 case is settled, the note already has a clean family hook and needs very little beyond the exact certificate. The surrounding Type 2 framework is already organized in Theorem 65, Remark 66, and Corollary 67.

## publication_packet_literature_scope
Jedwab-Li-Simon (2023), especially Theorem 65, Remark 66, Table 5, and Corollary 67, together with Kharaghani-Suda (2019) for the original balancedly splittable Hadamard-matrix setup.

## publication_packet_artifact_requirements
Either an explicit order-120 Hadamard matrix with a certified 12-row balanced split yielding inner products 12 and 0, or a compact impossibility proof.

## paper_shape
A single-theorem note on the first r = 5, s = 3 unresolved parameter in the Type 2 BSHM(8rs,4s,4s,0) family.

## transfer_kit

### usable_lemmas
- Theorem 65(i) gives the standard construction route from Hadamard matrices of orders 2r and 4s.
- Theorem 65(ii) gives the alternative construction route from Hadamard matrices of orders 4r and 2s.
- Remark 66 states that all known existence results for the Type 2 family are already accounted for by Theorem 65.
- Corollary 67 and Table 5 isolate (120,12,12,0) inside the remaining odd-odd residue.

### toy_example
The solved benchmark BSHM(48,12,12,0) lies in the r = 2 slice and shows that the s = 3 parameter is compatible with the family outside the odd-odd residue.

### known_obstruction
The known existence mechanisms all require escaping the odd-odd regime, so the r = 5, s = 3 case cannot be obtained by a direct application of the published product theorems.

### prior_work_stop_sentence
The current source resolves the Type 2 family outside the odd-odd regime and still lists BSHM(120,12,12,0) in Table 5.

### recommended_first_attack
Push the Type 2 product decomposition for r = 5, s = 3 until it either yields a constrained block model for a construction or forces an incompatibility in the associated strongly regular graph parameters.

### paper_if_solved
If solved exactly, the paper would be a short note settling the parameter set (120,12,12,0) inside the residual odd-odd branch of the Type 2 family.
