# Does the abelian group C_3 x C_159 admit a (477,204,87)-difference set?

- entry_type: `paper_candidate`
- slug: `abelian-difference-set-477-204-87-group-3-159`
- worker_role: `solver-A`
- canonical_source: `Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row 477 204 87 [3,159].`
- open_status_checked_on: `2026-04-15`
- publication_status: `NONE`
- publication_if_solved: `A construction or nonexistence proof for the exact [3,159] row would support a short note removing one tabled open case from the Gordon-Schmidt multiplier-survey frontier.`
- publication_if_solved_score: `solve_plus_light_writeup`
- solve_to_publication_distance: `short-medium`
- single_pass_proof_plausibility: `moderate`
- paper_leverage_score: `72`
- single_solve_to_paper_fraction: `0.72`
- title_theorem_strength: `moderate`
- family_anchor_strength: `strong`
- publication_narrative_strength: `moderate`
- editorial_overhead: `low`
- immediate_corollary_headroom: `low`
- isolated_exact_case_risk: `moderate`
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
- publication_packet_quality: `moderate`
- working_packet_path: `artifacts/abelian-difference-set-477-204-87-group-3-159/working_packet.md`
- paper_shape: `A one-theorem note resolving one exact group-specific open row from the multiplier-survey table.`

## question
Does the abelian group C_3 x C_159 admit a (477,204,87)-difference set?

## canonical_statement
Determine whether the abelian group C_3 x C_159 admits a (477,204,87)-difference set.

## intended_statement
Determine whether the abelian group C_3 x C_159 admits a (477,204,87)-difference set.

## pre_solve_gate_reason
The authoritative attempt registry shows no exact match for the [3,159] row. In the bounded 2026-04-15 audit, the exact tuple search and the alternate-notation search only surfaced Gordon-Schmidt's Table 2, while Gordon's current repository and publications pages did not expose a later direct settlement. Because the source already frames [3,159] as an exact open table row, a successful proof would keep the theorem slice stable instead of needing a feeder ladder.

## micro_paper_assessment
Lane-eligible, though slightly weaker than the top Lander rows because the paper narrative is table-driven rather than conjecture-branded. Still, one exact proof would already do most of the publication work and the theorem slice looks stable.

## hypothetical_title
On (477,204,87)-Difference Sets in C_3 x C_159

## hypothetical_abstract
We determine whether the abelian group C_3 x C_159 admits a (477,204,87)-difference set. Gordon and Schmidt list this exact row in Table 2 of their multiplier-survey paper as one of the smallest remaining open group-specific cases. Resolving it would therefore convert an already-canonical table entry into a concise stand-alone theorem note.

## single_solve_paper_explanation
This row is not just a tiny curiosity because it comes prepackaged as an exact frontier item in a canonical survey table. A clean proof would already supply the theorem, the novelty statement, and most of the paper's introduction. Beyond that, only light exposition and certificate validation remain.

## broader_theorem_nonimplication_note
Table 2 of the Gordon-Schmidt survey explicitly records [3,159] as open after the paper's multiplier-conjecture analysis and computational checks. In the bounded 2026-04-15 search, no later direct source surfaced that settles the exact [3,159] row.

## literature_gap
Gordon-Schmidt Table 2 still lists 477 204 87 [3,159] among the exact open difference-set rows.

## publication_packet_title
The (477,204,87) Difference-Set Case in C_3 x C_159

## publication_packet_frontier_basis
Table 2 of Gordon-Schmidt's multiplier survey isolates 477 204 87 [3,159] as an exact open group row.

## publication_packet_near_paper_reason
The survey already provides the frontier statement and the relevant multiplier-conjecture context. If the exact row is settled, the remaining paper is mostly a short table-to-theorem conversion plus the final certificate.

## publication_packet_literature_scope
Gordon-Schmidt (2016), especially Table 2, together with Gordon's current difference-set repository page and publications page for bounded freshness checking.

## publication_packet_artifact_requirements
Either an explicit (477,204,87)-difference set in C_3 x C_159, or a compact nonexistence proof for that exact group.

## paper_shape
A one-theorem note resolving one exact group-specific open row from the multiplier-survey table.

## transfer_kit

### usable_lemmas
- Table 2 of Gordon-Schmidt records 477 204 87 [3,159] as an exact open row.
- A translate fixed by all multipliers reduces any proof attempt to orbit unions once a usable multiplier is identified.
- The group-ring identity D D^(-1) = n + lambda G gives exact quotient-count constraints.
- The character criterion |chi(D)|^2 = n for nontrivial chi gives a rigid target for obstruction arguments.

### toy_example
Gordon's 2022 short proof that no (352,27,2)-difference set exists is a model of the multiplier-orbit obstruction style that could still settle an exact small row like [3,159].

### known_obstruction
The survey leaves the row open despite standard multiplier-conjecture reasoning, so a successful proof probably needs a sharper orbit or character obstruction than the published table already records.

### prior_work_stop_sentence
Gordon-Schmidt Table 2 stops at listing 477 204 87 [3,159] as an open difference-set row.

### recommended_first_attack
Assume the most useful available multiplier normalization and analyze orbit unions in C_3 x C_159 until the quotient coefficients or character sums force a contradiction.

### paper_if_solved
If solved exactly, the paper would be a short note removing one exact row from the Gordon-Schmidt multiplier-survey table.
