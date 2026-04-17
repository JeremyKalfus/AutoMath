# Untitled Entry

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-729-273-102-group-3-3-3-3-3-3`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon, "The La Jolla Difference Set Repository" (ArasuFest talk slides, August 3, 2019), especially slide 46 listing the smallest open elementary-abelian case 729 273 102 [3,3,3,3,3,3].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A proof of existence or nonexistence would settle Gordon's named smallest open elementary-abelian case at parameters (729,273,102) in C_3^6.`
- publication_if_solved_score: `solve_is_basically_the_paper`
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
- working_packet_path: `artifacts/abelian-difference-set-729-273-102-group-3-3-3-3-3-3/working_packet.md`
- paper_shape: `A short note settling the smallest open elementary-abelian difference-set case.`

## question
Does the elementary abelian group C_3 x C_3 x C_3 x C_3 x C_3 x C_3 admit a (729,273,102)-difference set?

## canonical_statement
Determine whether the elementary abelian group C_3^6 admits a (729,273,102)-difference set.

## intended_statement
Determine whether the elementary abelian group C_3^6 admits a (729,273,102)-difference set.

## pre_solve_gate_reason
The exact group is source-anchored as the smallest open case in a named family question, no local attempt-registry conflict was found, and the bounded exact/alternate-notation web sweep surfaced no direct post-source settlement.

## micro_paper_assessment
Lane-eligible. The candidate is an exact smallest-open-case theorem with a clean family anchor, low feeder risk, and a paper packet that is already close to title-and-abstract form.

## hypothetical_title
The Elementary Abelian (729,273,102)-Difference-Set Problem

## hypothetical_abstract
We determine whether the elementary abelian group C_3^6 admits a (729,273,102)-difference set. Gordon's La Jolla Difference Set Repository slides identify this exact group as the smallest open elementary-abelian case outside the settled Hadamard and Paley families. Our result therefore closes a named residual case and yields a short self-contained note with only light family framing beyond the core proof.

## single_solve_paper_explanation
The source already supplies both the exact statement and the publication narrative: this is the smallest open elementary-abelian case. A single exact solve would therefore provide almost all of the paper's mathematical content. What remains after the solve is mostly expository packaging, not additional theorem development.

## broader_theorem_nonimplication_note
The later source does not claim a general classification of elementary-abelian difference sets beyond the settled Hadamard and Paley families; instead it isolates C_3^6 at (729,273,102) as an unresolved residue, so no broader published theorem surfaced here that already forces the answer.

## literature_gap
Prior work surfaced in this curation stops at Gordon 2019 identifying (729,273,102) in C_3^6 as the smallest open elementary-abelian case; the bounded exact and alternate-notation web sweeps on 2026-04-15 found no direct later settlement.

## publication_packet_title
The Elementary Abelian (729,273,102)-Difference-Set Problem

## publication_packet_frontier_basis
Gordon's 2019 LJDSR slides single out 729 273 102 in [3,3,3,3,3,3] as the smallest open elementary-abelian case, while local attempt and source memory show no cooled-down or duplicate run on this exact group statement.

## publication_packet_near_paper_reason
One exact solve would already answer the stated smallest-open-case question, so the remaining work would be limited to short family context and clean proof exposition.

## publication_packet_literature_scope
Gordon 2019 slide 46, Gordon-Schmidt 2015/2016 multiplier-survey table context, bounded exact-statement and alternate-notation web sweeps on 2026-04-15, and local attempt/source registry checks.

## publication_packet_artifact_requirements
A source-faithful proof or disproof in C_3^6, the decisive character-orbit or quotient argument, and a brief explanation of how this resolves the smallest open elementary-abelian case.

## paper_shape
A short note settling the smallest open elementary-abelian difference-set case.

## transfer_kit

### usable_lemmas
- Gordon 2019 explicitly labels (729,273,102) in [3,3,3,3,3,3] as the smallest open elementary-abelian case, fixing the theorem slice.
- For any abelian difference set D, the group-ring equation D D^(-1) = n + lambda G and its character form constrain all nontrivial character values to modulus sqrt(n); here n = 171.
- The source discussion on known gcd(v,n) > 1 cases highlights the character-divisibility viewpoint as a natural obstruction framework for noncyclic abelian groups.

### toy_example
Work in F_3^2 first: inspect how character values and multiplier-fixed orbit unions behave in a small elementary-abelian model before lifting the bookkeeping pattern to F_3^6.

### known_obstruction
The family is already settled in the obvious Hadamard and Paley directions, so any proof must address the genuinely residual elementary-abelian case rather than inherit an infinite-family construction.

### prior_work_stop_sentence
Gordon 2019 lists 729 273 102 in [3,3,3,3,3,3] as the smallest open elementary-abelian case.

### recommended_first_attack
Translate the problem into character-value constraints on F_3^6 and test whether the 19-part of n = 171 forces an impossible orbit or divisibility pattern for a putative difference set.

### paper_if_solved
If solved exactly, the paper would be a short note settling the smallest open elementary-abelian difference-set case.
