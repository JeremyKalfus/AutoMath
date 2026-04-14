# Determine the exact value of R(B11, B11)

- entry_type: `paper_candidate`
- slug: `r-b11-diagonal-book-ramsey`
- worker_role: `solver-A`
- canonical_source: `Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.18, revision dated January 6, 2026), Section 5.3, together with Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), and bounded exact-term, alternate-notation, and recent-status web checks performed on 2026-04-13.`
- open_status_checked_on: `2026-04-13`
- publication_if_solved: `Settling the first unresolved diagonal book case not handled by the existing number-theoretic criteria would already support a genuine short note.`
- publication_if_solved_score: `standalone_short_paper`
- solve_to_publication_distance: `short`
- single_pass_proof_plausibility: `low`
- paper_leverage_score: `80`
- single_solve_to_paper_fraction: `0.78`
- title_theorem_strength: `strong`
- family_anchor_strength: `strong`
- publication_narrative_strength: `strong`
- editorial_overhead: `low`
- immediate_corollary_headroom: `moderate`
- isolated_exact_case_risk: `low`
- broader_theorem_implication_risk: `low`
- theorem_slice_stability: `stable`
- search_heavy: `False`
- certificate_compactness: `moderate`
- transfer_kit_present: `True`
- exact_gap_from_source: `tiny`
- micro_paper_lane_eligible: `True`
- novelty_check_cost: `low`
- formalization_overhead: `high`
- packaging_risk: `low`
- needs_feeder_ladder: `no`
- pre_solve_gate: `pass`
- publication_packet_quality: `strong`
- working_packet_path: `artifacts/r-b11-diagonal-book-ramsey/working_packet.md`
- paper_shape: `A one-theorem exact-value note on a diagonal book Ramsey number.`

## question
Is R(B11, B11) = 45 or 46?

## canonical_statement
Determine the exact value of R(B11, B11).

## intended_statement
Either prove that every graph on 45 vertices contains B11 or has a complement containing B11 and thus show R(B11, B11) = 45, or construct a 45-vertex graph with no B11 and no complement B11 and thus show R(B11, B11) = 46.

## pre_solve_gate_reason
DS1.18 leaves only 45 <= R(B11, B11) <= 46 after giving the general diagonal book framework, and the more recent 2025-2026 book papers did not close this specific case.

## micro_paper_assessment
Pass. This is a stable one-gap diagonal residue in a named family with a ready-made narrative explaining exactly why the case remains open.

## hypothetical_title
The Exact Value of R(B11, B11)

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B11, B11). Existing work places this value in the one-gap window 45 <= R(B11, B11) <= 46, but the standard exact criteria for diagonal books do not decide n = 11. Our theorem closes the smallest diagonal book case remaining outside those criteria and upgrades the current diagonal table by an exact entry.

## single_solve_paper_explanation
The exact n = 11 diagonal value is already the honest title theorem. The surrounding family theory, including the general one-gap framework and the prime-power and sum-of-two-squares criteria, is already available in the literature, so a successful solve leaves only light exposition and comparison with the existing exact diagonal cases. That places the candidate inside the desired 70-90 percent paper window.

## broader_theorem_nonimplication_note
The known exact diagonal criteria do not apply at n = 11 because 4n + 1 = 45 is a sum of two squares and is not a prime power, so the published family theorems do not already decide R(B11, B11).

## literature_gap
DS1.18 leaves R(B11, B11) unresolved between 45 and 46, and no later exact resolution surfaced in the bounded 2026-04-13 audit.

## publication_packet_title
The Exact Value of R(B11, B11)

## publication_packet_frontier_basis
DS1.18 states 4n + 1 <= R(Bn, Bn) <= 4n + 2 for n <= 21, records exact diagonal criteria when 4n + 1 is a prime power or not a sum of two squares, and still leaves n = 11 unresolved between 45 and 46; the 2025 and 2026 book papers do not report an exact solution for this diagonal case; bounded exact-term and recent-status searches on 2026-04-13 did not surface a later exact-resolution paper.

## publication_packet_near_paper_reason
The family theorem, two exact diagonal criteria, and neighboring exact diagonal entries are already in place. Once the n = 11 residue is settled, the rest of the note is mainly a short explanation of why this case escapes the existing criteria and how the forcing or witness construction resolves it.

## publication_packet_literature_scope
DS1.18 Section 5.3, Lidicky-McKinley-Pfender-Van Overberghe 2025, Wesley 2026, and bounded 2026-04-13 exact-statement, alternate-notation, and recent-status searches for R(B11, B11).

## publication_packet_artifact_requirements
Either a proof that every 45-vertex graph contains B11 or has complement containing B11, or one explicit 45-vertex graph avoiding both.

## paper_shape
A one-theorem exact-value note on a diagonal book Ramsey number.

## transfer_kit

### usable_lemmas
- DS1.18 records the diagonal framework 4n + 1 <= R(Bn, Bn) <= 4n + 2 for all n <= 21.
- The same survey records the exact criterion R(Bn, Bn) = 4n + 2 whenever 4n + 1 is a prime power.
- The survey also records that if 4n + 1 is not the sum of two integer squares, then R(Bn, Bn) <= 4n + 1, which gives exactness in many cases but not at n = 11.

### toy_example
The diagonal family already contains exact cases forced by number-theoretic criteria, while n = 11 is the first small residue where those criteria do not decide between 45 and 46.

### known_obstruction
Any proof of R(B11, B11) = 45 must rule out every 45-vertex self-complementary obstruction pattern, while a proof of R(B11, B11) = 46 requires one explicit 45-vertex graph avoiding B11 in both a graph and its complement.

### prior_work_stop_sentence
Current sources leave the diagonal book number R(B11, B11) in the one-gap window 45 <= R(B11, B11) <= 46.

### recommended_first_attack
Exploit the published diagonal one-gap framework and attack the n = 11 residue by proving that any 45-vertex extremal graph would have to realize an impossible refinement of the known lower-bound templates.

### paper_if_solved
The paper would be a short exact-value note on the first diagonal book residue not resolved by the standard number-theoretic criteria.
