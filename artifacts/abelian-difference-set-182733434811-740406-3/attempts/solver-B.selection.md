# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-182733434811-740406-3`
- worker_role: `solver-B`
- canonical_source: `Daniel M. Gordon, "On difference sets with small lambda" (Journal of Algebraic Combinatorics 55, 2022), especially Theorem 2, Theorems 3 and 4, and Table 4 listing the six remaining abelian (v,k,3)-difference-set cases for k <= 10^10.`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would remove one of the six residual abelian lambda = 3 cases isolated by Gordon's 2022 elimination up to k <= 10^10.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `76`
- single_solve_to_paper_fraction: `0.76`
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
- exact_gap_from_source: `small`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `False`
- pre_solve_gate: `pass`
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/abelian-difference-set-182733434811-740406-3/working_packet.md`
- paper_shape: `A one-theorem cleanup note removing one of the six residual abelian lambda = 3 parameter sets in Gordon's 2022 table.`

## question
Does any abelian group of order 182733434811 admit a (182733434811,740406,3)-difference set?

## canonical_statement
Determine whether there exists an abelian (182733434811,740406,3)-difference set.

## intended_statement
Determine whether any abelian group of order 182733434811 admits a (182733434811,740406,3)-difference set.

## pre_solve_gate_reason
The exact tuple is not present in local attempt memory, and bounded source-anchored web checking still finds it only as an open residual case in Gordon's Table 4 with no later resolution surfaced.

## micro_paper_assessment
This is lane-eligible, though less crisp than the selected [3,9,9] case: the frontier basis is strong, the exact gap is explicit, and one decisive solve would already look like the core of a short cleanup note.

## hypothetical_title
On an Open Abelian (182733434811,740406,3)-Difference Set Case

## hypothetical_abstract
We determine whether any abelian group of order 182733434811 admits a (182733434811,740406,3)-difference set. Gordon's 2022 analysis leaves this tuple as one of only six residual abelian lambda = 3 cases with k <= 10^10 after the standard elimination theorems are applied. The result therefore closes a named residual table entry with only light exposition beyond the decisive proof.

## single_solve_paper_explanation
Because the tuple already appears in an explicit residual table, an exact solve would immediately be the main theorem of a short note. The paper would not need a feeder ladder: the literature context is just the elimination pipeline and the fact that this tuple survived it. Remaining work after the solve is mostly a concise recap of the known filters and the final argument.

## broader_theorem_nonimplication_note
The canonical source explicitly says that Theorem 2, Theorems 3 and 4, Lander, and Mann do not settle this tuple, so no broader published elimination uncovered in the bounded audit already disposes of it.

## literature_gap
Prior work stops at listing (182733434811,740406,3) in Table 4 as one of the six remaining abelian lambda = 3 cases for k <= 10^10.

## publication_packet_title
A Residual Abelian Lambda = 3 Difference-Set Case

## publication_packet_frontier_basis
Gordon's Table 4 identifies (182733434811,740406,3) as one of the six remaining abelian lambda = 3 cases after Theorem 2, Theorems 3 and 4, Lander, and Mann eliminations.

## publication_packet_near_paper_reason
The source already supplies the cleanup narrative and the elimination framework, so an exact solve would only need the decisive existence or nonexistence argument for this one tuple plus a short recap of why it escaped the previous tests.

## publication_packet_literature_scope
Gordon 2022, especially the orbit-counting elimination Theorem 2, the cyclic and contracted multiplier bounds in Theorems 3 and 4, and Table 4.

## publication_packet_artifact_requirements
Either a compact nonexistence argument using multiplier or contracted-multiplier structure, or an explicit abelian difference-set certificate with a short verification packet.

## paper_shape
A one-theorem cleanup note removing one of the six residual abelian lambda = 3 parameter sets in Gordon's 2022 table.

## transfer_kit

### usable_lemmas
- Gordon's Lemma 1 gives the orbit structure of G under a multiplier after isolating a prime divisor p of v.
- Theorem 2 converts the orbit decomposition into the inequalities k = ao + b, b(b - 1) <= lambda(|H| - 1), and a o(o - 1) <= lambda(p - 1).
- Theorem 3 bounds the multiplier group size in cyclic groups by |M| <= k.
- Theorem 4 extends the same style of bound to contracted multipliers over quotient groups.

### toy_example
Use Gordon's smaller Table 4 entries (4761,120,3) or (64681,441,3) as the worked model for how a residual lambda = 3 case is packaged in the source literature.

### known_obstruction
This tuple already survives the standard fast eliminations, so any proof must use structure not captured by Gordon's existing Theorem 2, cyclic multiplier bounds, Lander, or Mann filters.

### prior_work_stop_sentence
Table 4 of Gordon (2022) still lists (182733434811,740406,3) as an open abelian lambda = 3 case.

### recommended_first_attack
Factor the ambient abelian group through a large prime divisor p of v, force multiplier or contracted-multiplier orbits, and try to contradict the orbit-count inequalities or quotient character data.

### paper_if_solved
If solved exactly, the paper would be a one-theorem note deleting one row from Gordon's residual abelian lambda = 3 table.
