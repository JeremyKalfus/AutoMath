# Does every Paley graph have an internal partition?

- entry_type: `paper_candidate`
- slug: `paley-graph-internal-partition`
- worker_role: `solver-A`
- canonical_source: `Pál Bärnkopf, Zoltán Lóránt Nagy, and Zoltán Paulovics, "A Note on Internal Partitions: The 5-Regular Case and Beyond" (Graphs and Combinatorics, 2024), Problem 7.`
- open_status_checked_on: `2026-04-12`
- attack_style: `quadratic-residue symmetry plus cohesive-set and near-bisection arguments specialized to Paley graphs`
- curation_confidence: `high`
- publication_status: `SLICE_CANDIDATE`
- publication_if_solved: `A complete Paley-family theorem is immediately paper-ready because the family is classical and the statement is already singled out as a named open problem.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short-medium`
- single_pass_proof_plausibility: `medium`
- paper_leverage_score: `74`
- single_solve_to_paper_fraction: `0.78`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `moderate`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- search_heavy: `False`
- certificate_compactness: `high`
- transfer_kit_present: `True`
- exact_gap_from_source: `broad`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `medium`
- packaging_risk: `medium`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/paley-graph-internal-partition/working_packet.md`
- paper_shape: `A family theorem on a canonical pseudorandom graph class, with either a universal construction or a first counterexample and structural explanation.`

## question
For each finite field order q ≡ 1 (mod 4), does the Paley graph P(q) admit an internal partition?

## canonical_statement
Prove that every Paley graph has an internal partition.

## intended_statement
Settle the Paley-family problem outright, either by proving all Paley graphs admit internal partitions or by finding a minimal counterexample within the residue-graph family.

## why_reasoning_friendly
The family has strong algebraic symmetry, so progress can come from a direct structural argument rather than a sprawling exact-instance campaign.

## why_low_token
The target is one family theorem with a standard explicit graph definition and a yes/no verifier based on degree counts across a partition.

## verifier_hint
A positive witness is a partition with local neighbour-count checks; a negative solution needs a rigorous structural obstruction, not a heuristic search trace.

## lean_hint
Formalization is feasible after the core argument is known, but finite-field graph preliminaries make it slightly heavier than the smaller exact-slice packets.

## rediscovery_risk
low

## why_still_appears_open
The 2024 paper lists the Paley statement explicitly as Problem 7, and the bounded outside-status search did not turn up any later resolution.

## why_this_could_be_publishable
It is already phrased as a standalone open theorem on a famous graph family, so one strong solve is essentially the paper.

## pre_solve_gate_reason
The statement is already a named standalone family theorem, so one clean solve would largely determine the paper even though the family scope is broader than the first two queue entries.

## micro_paper_assessment
Pass, but lower priority: the paper shape is excellent, yet the target is a full family theorem rather than a tiny exact residue.

## hypothetical_title
Internal Partitions in Paley Graphs

## hypothetical_abstract
We settle the Paley internal-partition problem posed in the 2024 internal-partitions note. Using the additive and multiplicative symmetries of Paley graphs, we either construct internal partitions uniformly across the family or isolate a first counterexample together with the structural obstruction that forces it. Because the family is classical and the theorem statement is already singled out in the literature, the solve itself supplies most of a finished note.

## single_solve_paper_explanation
The source already frames this as a standalone open problem on a famous graph family, so a full solve immediately gives the paper title, statement, and motivation. After the solve, the remaining work is mainly a brief background paragraph on internal partitions, a polished proof, and one or two remarks comparing Paley graphs with the general regular-graph setting. The main caution is breadth, not packaging.

## broader_theorem_nonimplication_note
The 2024 paper poses the Paley-family statement as an open problem rather than deducing it from a broader theorem, and bounded status checks found no later family-wide implication closing it.

## literature_gap
The recent internal-partitions paper records the Paley-family statement as an explicit open problem and does not advance beyond posing it.

## publication_packet_title
Internal Partitions in Paley Graphs

## publication_packet_frontier_basis
The 2024 internal-partitions paper lists the Paley-family problem explicitly as Problem 7.

## publication_packet_near_paper_reason
Any family-wide solution or first counterexample would already be a referee-facing theorem on a famous graph class.

## publication_packet_literature_scope
The 2024 internal-partitions note, standard Paley graph background, and one bounded later-status search.

## publication_packet_artifact_requirements
Either a constructive partition rule across the family or a rigorous first counterexample with local neighbour-count verification.

## paper_shape
A family theorem on a canonical pseudorandom graph class, with either a universal construction or a first counterexample and structural explanation.

## transfer_kit

### usable_lemmas
- Paley graphs are regular self-complementary Cayley graphs on F_q, so additive and multiplicative symmetries are available from the start.
- Internal partitions are verified purely by local neighbour counts across the chosen bipartition, giving a tiny checker once a candidate partition is proposed.
- The 2024 paper already isolates the Paley-family statement as a named open problem, so any structural Paley-specific lemma feeds directly into the final theorem narrative.

### toy_example
P(5) = C_5 is the smallest sanity-check model for the partition condition and keeps the neighbour-count verification completely explicit.

### known_obstruction
Paley graphs are pseudo-random enough that naive bisection or switching heuristics may not preserve the internal condition.

### prior_work_stop_sentence
The recent internal-partitions paper states the Paley-family theorem as an explicit open problem and stops there.

### recommended_first_attack
Search for a residue-class based partition or a canonical near-bisection stabilized by the Paley automorphism group.

### paper_if_solved
The paper would be a single family-theorem note on a classical algebraic graph family, with one proof section and a short comparison to the general internal-partition literature.

## definitions
- An internal partition is a nontrivial vertex partition in which each vertex has at least as many neighbours in its own class as across.
- A Paley graph P(q) has vertex set F_q with x adjacent to y when x-y is a nonzero quadratic residue, for q ≡ 1 mod 4.
- Paley graphs are highly structured regular graphs and canonical test cases for partition problems.

## publication_red_flags
- Paley graphs are pseudo-random enough that naive switching arguments may fail.
- If false, the first counterexample may occur at a larger q and need nontrivial computation.
