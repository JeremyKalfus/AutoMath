# Working Packet: The Exact Value of R(W4, W8)

- slug: `r-w4-w8-wheel-ramsey`
- title: Determine the exact value of R(W4, W8)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `43`
- single-solve-to-paper fraction: `0.52`

## statement
Determine the smallest n such that every graph on n vertices contains W4 or its complement contains W8.

## novelty_notes
- frontier basis: The current survey still lists the pair as unresolved, while the 2025 paper tightened or closed other wheel entries without resolving this one. Because W4 is K4, the statement also sits close to better studied clique-versus-wheel territory.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A successful exact closure would still be publishable as a concise table update. But the likely argument would either be computationally heavy or get reframed through broader K4-versus-wheel considerations, which weakens the strict micro-paper fit.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: low
- isolated exact-case risk: high
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: moderate
- assessment: Fail. This is a legitimate unresolved table entry, but it is too wide and too prone to broader reframing for the current one-shot lane.

## likely_paper_shape
- note title: The Exact Value of R(W4, W8)
- hypothetical title: The Exact Value of R(W4, W8)
- paper shape: A small wheel exact-value note with a mixed clique-wheel flavor and substantial computational packaging.
- publication if solved: An exact value for R(W4, W8) could still support a table-closing note, but it does not clear the strict micro-paper lane.
- minimal artifact requirements: Either a complete elimination of critical graphs near the threshold or one explicit extremal witness plus a verified upper-bound classification.

## hypothetical_abstract
We determine the wheel Ramsey number R(W4, W8). Existing survey data leaves this pair in the range 22 <= R(W4, W8) <= 26. Our result would close a small unresolved entry at the interface of clique-wheel and wheel-wheel Ramsey theory.

## single_solve_explanation
The exact value would be the title theorem. The problem is that the solve likely carries extra baggage: either a substantial computational appendix or a reframing through more general K4-versus-wheel behavior. That leaves too much post-solve packaging for the micro-paper lane.

## broader_theorem_nonimplication
Exact results for smaller wheels and general clique Ramsey facts do not by themselves settle R(W4, W8). The current survey still records a nontrivial interval.

## literature_gap
Current public sources leave R(W4, W8) in the range 22 <= R(W4, W8) <= 26, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: DS1.17 Table VIII records the unresolved range 22 <= R(W4, W8) <= 26.
- lemma: W4 is isomorphic to K4, which gives immediate access to the surrounding clique-versus-wheel literature cited in the survey.
- lemma: The 2025 paper shows that exact small-wheel closures remain achievable, but it does not close this mixed pair.
- toy example: The exact neighboring baseline R(W4, W6) = 19 appears in the classical small-wheel literature.
- known obstruction: Because W4 = K4, a short proof might drift into a broader clique-versus-wheel observation rather than staying a crisp exact-pair note.
- prior-work stop sentence: Current sources stop at 22 <= R(W4, W8) <= 26.
- recommended first attack: Only revisit this if a pair-specific structural reduction is found that avoids a broad K4-versus-wheel detour.
- paper if solved: The paper would be a short exact-value note, but it would likely need broader clique-wheel framing than the repo currently wants.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.2 and Table VIII; Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Section 2 and Table 1; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-13.
- DS1.17 Section 5.2 and Table VIII, Lidicky-McKinley-Pfender-Van Overberghe 2025, and bounded 2026-04-13 exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches for R(W4, W8).
- artifacts/r-w4-w8-wheel-ramsey/record.md
- artifacts/r-w4-w8-wheel-ramsey/status.json
