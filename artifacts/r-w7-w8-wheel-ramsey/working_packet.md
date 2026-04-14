# Working Packet: The Exact Value of R(W7, W8)

- slug: `r-w7-w8-wheel-ramsey`
- title: Determine the exact value of R(W7, W8)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `58`
- single-solve-to-paper fraction: `0.61`

## statement
Determine the least n such that every red-blue coloring of Kn contains a red W7 or a blue W8, equivalently close the current window 19 <= R(W7, W8) <= 21.

## novelty_notes
- frontier basis: DS1.17 Table VIII records the current wheel bounds 19 <= R(W7, W8) <= 21, while the bounded 2026-04-13 exact-term and recent-status audit did not surface a later exact-resolution paper.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact value were pinned down, there would be a plausible short note because wheel Ramsey numbers are a standard family. But more of the note would still have to be spent on family framing and case analysis than in the cleaner one-gap book residues.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail for the strict lane. The family anchor is classical, but the current packet is still too wide and editorially heavier than the best micro-paper options.

## likely_paper_shape
- note title: The Exact Value of R(W7, W8)
- hypothetical title: The Exact Value of R(W7, W8)
- paper shape: A small exact-value note on a classical wheel Ramsey number.
- publication if solved: An exact value could support a short wheel-Ramsey note, but the current packet is weaker and less paper-ready than the best book candidates.
- minimal artifact requirements: Either a forcing proof at 19, 20, or 21 vertices, or explicit critical colorings showing which smaller orders remain avoidable.

## hypothetical_abstract
We determine the wheel Ramsey number R(W7, W8). Current tables leave this classical case in the interval 19 <= R(W7, W8) <= 21. Our result closes one of the small unresolved wheel entries and sharpens the exact boundary for two-color Ramsey numbers involving wheels.

## single_solve_explanation
A successful solve would be publishable, but the candidate is not as near-paper as a one-gap book residue. The remaining window has three values, and the surrounding paper would need more census-style discussion of critical colorings and comparisons with adjacent wheel cases. That lowers the solve-to-paper fraction below the desired band.

## broader_theorem_nonimplication
The available wheel results in DS1.17 provide only general lower and upper mechanisms and do not imply the exact mixed case R(W7, W8). The honest theorem slice would remain this exact small wheel number rather than collapsing into a broader known principle.

## literature_gap
Current public sources leave R(W7, W8) unresolved in the interval 19 <= R(W7, W8) <= 21, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: DS1.17 item 5.2(b) gives the generic lower-bound templates 3m - 2 for even n and 2m - 1 in general, which support the small wheel lower-bound landscape.
- lemma: DS1.17 Table VIII records the current bounds 19 <= R(W7, W8) <= 21.
- lemma: The same survey records several nearby exact wheel values such as R(W5, W5) = 15 and the exact low-order diagonal and near-diagonal wheel entries around this range.
- toy example: The small wheel table already contains exact nearby cases, while R(W7, W8) remains one of the unresolved low-order mixed entries.
- known obstruction: Any exact proof must control 19- and 20-vertex critical colorings where one color avoids a 6-cycle-with-hub and the complement simultaneously avoids a 7-cycle-with-hub.
- prior-work stop sentence: Current sources stop at the interval 19 <= R(W7, W8) <= 21.
- recommended first attack: Exploit degree constraints around a potential wheel hub and classify whether any 20-vertex critical coloring can simultaneously avoid both wheel configurations.
- paper if solved: The paper would be a short exact-value note on a remaining small wheel Ramsey number.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Table VIII and items 5.2(b)-(c), together with bounded exact-term, alternate-notation, canonical-source, and recent-status web checks performed on 2026-04-13.
- DS1.17 Table VIII and items 5.2(b)-(c), together with bounded 2026-04-13 exact-statement, alternate-notation, source-internal, and recent-status searches for R(W7, W8).
- artifacts/r-w7-w8-wheel-ramsey/record.md
- artifacts/r-w7-w8-wheel-ramsey/status.json
