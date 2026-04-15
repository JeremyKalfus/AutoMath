# Untitled Entry

- entry_type: `paper_candidate`
- slug: `bshm-72-12-12-0`
- worker_role: `solver-A`
- canonical_source: `Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Theorem 65, Remark 66, Table 5 on page 33, and Corollary 67 on page 34: the paper leaves (72,12,12,0) as the first open odd-odd case in the Type 2 family BSHM(8rs,4s,4s,0).`
- open_status_checked_on: `2026-04-14`
- publication_status: `NONE`
- publication_if_solved: `A construction or obstruction for BSHM(72,12,12,0) would plausibly be publishable as a short note settling the first odd-odd open case in the Type 2 BSHM(8rs,4s,4s,0) family.`
- publication_if_solved_score: `solve_plus_light_packaging`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `86`
- single_solve_to_paper_fraction: `0.84`
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
- working_packet_path: `artifacts/bshm-72-12-12-0/working_packet.md`
- paper_shape: `A single-theorem note on the first unresolved odd-odd parameter in the Type 2 BSHM(8rs,4s,4s,0) family.`

## question
Does there exist a balanced splittable Hadamard matrix BSHM(72,12,12,0)?

## canonical_statement
Determine whether there exists a BSHM(72,12,12,0).

## intended_statement
Determine whether an order-72 Hadamard matrix exists that is balanced splittable with parameters (72,12,12,0).

## pre_solve_gate_reason
Thin repo memory and slug scans show no prior mathematical attempt for this exact tuple. In the canonical 2023 source, the PDF audit confirmed that Theorem 65 is followed by Remark 66 and Table 5 on page 33, where Table 5 begins with (72,12,12,0), and Corollary 67 on page 34 leaves only odd r,s > 1 unresolved. A bounded 2026-04-14 web audit combined exact quoted tuple searches, acronym-form and balanced-versus-balancedly wording searches, direct source-title checks, and recent-status checks; the tuple-specific searches produced no settlement hit and the positive hits were only the canonical EJC paper plus citation and bibliography mirrors such as DBLP and Emergent Mind, with no later source settling this parameter.

## micro_paper_assessment
Lane-eligible. This is the smallest odd-odd open case in a named family, with a stable theorem slice, cheap packaging, and no obvious broader result already settling it.

## hypothetical_title
The First Odd-Odd Open Case for Balanced Splittable Hadamard Matrices with Parameters (8rs,4s,4s,0)

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (72,12,12,0). Jedwab, Li, and Simon showed that all known existence results for the Type 2 family BSHM(8rs,4s,4s,0) arise from Theorem 65 and that, assuming the Hadamard matrix conjecture, only odd r,s > 1 remain unresolved; Table 5 begins that residual list with (72,12,12,0). Resolving this parameter closes the smallest odd-odd residue in the family and yields a compact stand-alone note.

## single_solve_paper_explanation
This tuple already reads like a title theorem because the source isolates it as the first open odd-odd parameter in a named BSHM family. Once the existence or nonexistence proof is in hand, the rest of the note is short: summarize Theorem 65 and Corollary 67, explain the odd-odd residue, and present the certificate. That keeps the solve squarely in the 70-90% range of the final paper.

## broader_theorem_nonimplication_note
Corollary 67 leaves the Type 2 family unresolved exactly when both r and s are odd and greater than 1. The tuple (72,12,12,0) has r = 3 and s = 3, so it lies precisely in the published open regime and is not implied by the broader theorem.

## literature_gap
Current checked source literature determines the Type 2 family BSHM(8rs,4s,4s,0) outside the odd-odd residue, where Table 5 begins with BSHM(72,12,12,0).

## publication_packet_title
The First Odd-Odd Open Case for BSHM(8rs,4s,4s,0)

## publication_packet_frontier_basis
Theorem 65 determines all currently known existence cases, Remark 66 states that no other existence results are known, Corollary 67 leaves only odd r,s > 1 unresolved, and Table 5 starts that residue with (72,12,12,0).

## publication_packet_near_paper_reason
If the order-72 case is settled, the paper is nearly complete: recall Theorem 65 and Corollary 67, explain why this is the first odd-odd residue, and present the exact witness or obstruction. Very little remains beyond framing and verification.

## publication_packet_literature_scope
Jedwab-Li-Simon (2023), especially Theorem 65, Remark 66, Table 5, and Corollary 67, together with Kharaghani-Suda (2019) for the original balancedly splittable Hadamard-matrix setup.

## publication_packet_artifact_requirements
Either an explicit order-72 Hadamard matrix with a certified 12-row balanced split yielding inner products 12 and 0, or a compact impossibility proof.

## paper_shape
A single-theorem note on the first unresolved odd-odd parameter in the Type 2 BSHM(8rs,4s,4s,0) family.

## transfer_kit

### usable_lemmas
- Theorem 65(i) gives existence for BSHM(8rs,4s,4s,0) when Hadamard matrices of orders 2r and 4s exist.
- Theorem 65(ii) gives existence for BSHM(8rs,4s,4s,0) when Hadamard matrices of orders 4r and 2s exist.
- Remark 66 states that all currently known existence results for BSHM(8rs,4s,4s,0) come from Theorem 65.
- Corollary 67 leaves only the odd-odd residue unresolved, and Table 5 lists (72,12,12,0) first.

### toy_example
The nearby positive benchmark BSHM(48,12,12,0) lies in the solved r = 2 slice of Corollary 67 and shows that the s = 3 parameter itself is compatible with the family outside the odd-odd residue.

### known_obstruction
The known constructions stop exactly when both r and s are odd and greater than 1, so any proof for order 72 must address the genuine odd-odd residue rather than repackage an even-factor construction.

### prior_work_stop_sentence
The current source determines BSHM(8rs,4s,4s,0) whenever at least one of r,s is not an odd integer greater than 1, and Table 5 starts the remaining odd-odd cases with BSHM(72,12,12,0).

### recommended_first_attack
Exploit the product structure behind Theorem 65 and Proposition 64 to test whether the odd-odd obstruction at r = s = 3 can be converted into an order-specific construction or a contradiction in the associated strongly regular graph parameters.

### paper_if_solved
If solved exactly, the paper would be a short note closing the smallest odd-odd residue in the Type 2 balanced splittable Hadamard-matrix family.
