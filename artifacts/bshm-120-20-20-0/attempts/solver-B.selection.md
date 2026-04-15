# Untitled Entry

- entry_type: `paper_candidate`
- slug: `bshm-120-20-20-0`
- worker_role: `solver-B`
- canonical_source: `Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Theorem 65, Remark 66, Table 5 on page 33, and Corollary 67 on page 34: the paper leaves (120,20,20,0) as the first open s = 5 case in the Type 2 family BSHM(8rs,4s,4s,0).`
- open_status_checked_on: `2026-04-14`
- publication_status: `NONE`
- publication_if_solved: `A construction or obstruction for BSHM(120,20,20,0) would plausibly be publishable as a short note settling the first s = 5 open case in the Type 2 BSHM(8rs,4s,4s,0) family.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `83`
- single_solve_to_paper_fraction: `0.81`
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
- novelty_check_cost: `moderate`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/bshm-120-20-20-0/working_packet.md`
- paper_shape: `A single-theorem note on the first unresolved s = 5 parameter in the Type 2 BSHM(8rs,4s,4s,0) family.`

## question
Does there exist a balanced splittable Hadamard matrix BSHM(120,20,20,0)?

## canonical_statement
Determine whether there exists a BSHM(120,20,20,0).

## intended_statement
Determine whether an order-120 Hadamard matrix exists that is balanced splittable with parameters (120,20,20,0).

## pre_solve_gate_reason
Thin repo memory and slug scans show no prior mathematical attempt for this exact tuple. In the canonical 2023 source, the PDF audit confirmed that Theorem 65 and Remark 66 cover the known Type 2 existence mechanisms, while Table 5 on page 33 lists (120,20,20,0) as the first s = 5 entry and Corollary 67 leaves only odd r,s > 1 unresolved. A bounded 2026-04-14 web audit over exact-tuple and acronym-form searches for this tuple, together with family-level balanced-versus-balancedly wording, source-title, and citation-mirror searches, surfaced only the canonical EJC paper, generic bibliographic mirrors, or no parameter-specific settlement hit.

## micro_paper_assessment
Lane-eligible. The first-s = 5 framing gives this exact tuple a credible title theorem, low editorial overhead, and a stable note shape.

## hypothetical_title
The First Open s = 5 Case for Balanced Splittable Hadamard Matrices in the Type 2 Family

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (120,20,20,0). In the Type 2 family BSHM(8rs,4s,4s,0), Jedwab, Li, and Simon proved that all known constructions come from Theorem 65 and that, assuming the Hadamard matrix conjecture, only odd r,s > 1 remain unresolved; Table 5 shows that (120,20,20,0) is the first s = 5 case left open. Resolving this parameter yields a compact note because the surrounding framework, neighboring solved cases, and exact frontier location are already available.

## single_solve_paper_explanation
This tuple is already paper-shaped because it is the first s = 5 representative in a named open residue, not just an arbitrary larger instance. Once the exact proof is known, the paper mainly needs to recall Theorem 65 and Corollary 67, explain the new s = 5 residue, and present the certificate. The solve therefore supplies most of the final note.

## broader_theorem_nonimplication_note
Corollary 67 determines the Type 2 family outside the odd-odd regime and does not settle cases with odd r,s > 1. The tuple (120,20,20,0) has r = 3 and s = 5, so it sits exactly in the published open branch and is not implied by the broader theorem.

## literature_gap
Current checked source literature leaves BSHM(120,20,20,0) unresolved as the first s = 5 entry in Table 5 of the Type 2 family.

## publication_packet_title
The First Open s = 5 Case for BSHM(8rs,4s,4s,0)

## publication_packet_frontier_basis
Corollary 67 leaves the Type 2 odd-odd residue unresolved, and Table 5 records (120,20,20,0) as the first s = 5 parameter in that residual list.

## publication_packet_near_paper_reason
If the order-120, s = 5 case is settled, the paper already has a clean frontier hook: it closes the first s = 5 residue in an explicitly isolated family branch. What remains is mainly a short recap of Theorem 65 and the exact certificate.

## publication_packet_literature_scope
Jedwab-Li-Simon (2023), especially Theorem 65, Remark 66, Table 5, and Corollary 67, together with Kharaghani-Suda (2019) for the original balancedly splittable Hadamard-matrix formulation.

## publication_packet_artifact_requirements
Either an explicit order-120 Hadamard matrix with a certified 20-row balanced split yielding inner products 20 and 0, or a compact impossibility proof.

## paper_shape
A single-theorem note on the first unresolved s = 5 parameter in the Type 2 BSHM(8rs,4s,4s,0) family.

## transfer_kit

### usable_lemmas
- Theorem 65(i) gives existence for BSHM(8rs,4s,4s,0) when Hadamard matrices of orders 2r and 4s exist.
- Theorem 65(ii) gives a second construction route using Hadamard matrices of orders 4r and 2s.
- Remark 66 states that all known existence results for this family arise from Theorem 65.
- Table 5 lists (120,20,20,0) as the first open s = 5 case inside the odd-odd residue left by Corollary 67.

### toy_example
The solved benchmark BSHM(80,20,20,0) lies in the r = 2 slice of Corollary 67 and shows that the s = 5 parameter is compatible with the family outside the odd-odd residue.

### known_obstruction
The known product constructions stop exactly when both factors are odd and greater than 1, so any order-120 proof must engage the genuine odd-odd barrier rather than reuse an even-factor decomposition.

### prior_work_stop_sentence
The current source determines the Type 2 family outside the odd-odd regime, and Table 5 still lists BSHM(120,20,20,0) as the first s = 5 case left open.

### recommended_first_attack
Use the product templates behind Theorem 65 to test whether the r = 3, s = 5 case can be forced into a constrained strongly regular graph profile or lifted from a smaller decomposition that survives the odd-odd obstruction.

### paper_if_solved
If solved exactly, the paper would be a short note settling the first s = 5 residue in the Type 2 balanced splittable Hadamard-matrix family.
