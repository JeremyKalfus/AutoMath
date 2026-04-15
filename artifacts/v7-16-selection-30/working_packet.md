# Working Packet: The Exact Value of V_7(16)

- slug: `v7-16-selection-30`
- title: v7-16-selection-30
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `52`
- single-solve-to-paper fraction: `0.63`

## statement
Determine whether the minimum worst-case number of comparisons needed to select the seventh smallest of sixteen elements is exactly 30.

## novelty_notes
- frontier basis: The open-problem list explicitly isolates V_7(16) = 30 as one of the unresolved exact comparison-selection parameters in Aigner's line of problems.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A definitive 30-or-not answer would already give the title theorem of a short note. The drag is that the likely proof is computer-assisted or decision-tree exhaustive, so the note risks reading as a small certificate dump rather than a crisp mathematical paper.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: high
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: small
- assessment: Not lane-eligible. The exact target is real and stable, but the expected proof mode is too search-heavy and the paper narrative is too parameter-table oriented.

## likely_paper_shape
- note title: The Exact Value of V_7(16)
- hypothetical title: The Exact Worst-Case Selection Complexity V_7(16)
- paper shape: A short exact-algorithms note fixing one small unresolved selection parameter, likely with a machine-assisted certificate.
- publication if solved: An exact determination of V_7(16) would plausibly support a short algorithmic note on a named unresolved selection-complexity parameter.
- minimal artifact requirements: Either an exact selection algorithm with worst-case bound 30 plus a matching lower bound, or a lower-bound certificate proving 30 impossible.

## hypothetical_abstract
We determine whether the minimum worst-case number of comparisons needed to select the seventh smallest of sixteen elements is 30. This parameter is explicitly listed in the current Aigner selection-problem compendium as an unresolved exact small case. A resolution would give a compact exact-algorithms note, though likely with a machine-assisted component.

## single_solve_explanation
If the exact value were settled, the main theorem, the algorithm or lower bound, and the certificate would all arrive together. The remaining paper work would be short, but the likely reliance on exhaustive search makes the result feel closer to a parameter-table update than to the strongest micro-paper lane targets. That keeps the packet below the preferred threshold.

## broader_theorem_nonimplication
The open-problem listing would not single out V_7(16) if a known monotonicity or generic selection theorem already implied the answer. The issue is not implication by broader published theory but the risk of a certificate-heavy one-off solve.

## literature_gap
The current exact-selection problem compendium still lists 'Prove or disprove that V_7(16) = 30' as an unresolved small parameter question.

## transfer_kit
- lemma: The source defines V_i(n) as the minimum worst-case number of comparisons needed to select the i-th smallest element from n elements.
- lemma: The same open-problem page frames these exact-value questions as part of Aigner's selection-complexity program.
- lemma: The page explicitly lists V_7(16) = 30 as an unresolved prove-or-disprove target.
- toy example: The broader line studies exact V_i(n) values for small parameters in the comparison model; V_7(16) is one of the highlighted unresolved cases.
- known obstruction: The most plausible route is an exhaustive comparison-tree analysis, which pushes the certificate toward machine-generated bulk.
- prior-work stop sentence: The current open-problem compendium still stops at the unresolved exact-value question 'Prove or disprove that V_7(16) = 30.'
- recommended first attack: Encode the lower-bound and decision-tree constraints tightly enough that any residual search certificate stays human-readable rather than drifting into a broad campaign on exact selection tables.
- paper if solved: If solved exactly, the paper would be a short exact-algorithms note fixing one named unresolved small selection parameter.

## bounded_source_list
- The algoresearch.org open-problems page, viewed on 2026-04-14, records this as an Aigner selection-complexity problem and points to the classical exact-selection literature; it lists 'Prove or disprove that V_7(16) = 30' among the exact small-parameter open cases for worst-case comparison selection.
- The algoresearch open-problem page and the classical exact-selection line it cites.
- artifacts/v7-16-selection-30/record.md
- artifacts/v7-16-selection-30/status.json
