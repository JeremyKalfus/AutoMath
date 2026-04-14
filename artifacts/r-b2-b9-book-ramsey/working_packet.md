# Working Packet: The Exact Value of R(B2, B9)

- slug: `r-b2-b9-book-ramsey`
- title: Determine the exact value of R(B2, B9)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `67`
- single-solve-to-paper fraction: `0.66`

## statement
Determine the least n such that every graph on n vertices contains a copy of B2 or its complement contains a copy of B9.

## novelty_notes
- frontier basis: Current public sources support only 22 <= R(B2, B9) <= 24.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved, the result would still serve as the note's title theorem inside a standard family. The target misses the strongest lane only because the corridor is slightly wider and the forcing/witness packet is therefore less sharply constrained than for the one-gap cases.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Borderline but not lane-eligible. The story is real, yet the remaining three-value corridor keeps the solve-to-paper fraction just below the 0.70 target.

## likely_paper_shape
- note title: The Exact Value of R(B2, B9)
- hypothetical title: The Exact Value of R(B2, B9)
- paper shape: A one-theorem exact-value note on the B2 versus Bn book line.
- publication if solved: An exact closure of R(B2, B9) would still support a short note, but the three-value corridor leaves a bit more residue than the strict lane prefers.
- minimal artifact requirements: A 21-, 22-, or 23-vertex critical graph analysis together with either a sharp witness or a complete forcing proof.

## hypothetical_abstract
We determine the two-color Ramsey number R(B2, B9). Existing public sources place this parameter in the interval 22 <= R(B2, B9) <= 24. Our result closes another small case on the B2-versus-book line.

## single_solve_explanation
A clean exact solve would still give a real title theorem and most of the final note. The family context is already standard, and the note would mostly need the sharp certificate and a short comparison with nearby B2 cases. It falls just short of the strict micro-paper lane because the current interval is not yet a one-gap residue.

## broader_theorem_nonimplication
The checked survey and 2025 update improve only the lower side and generic upper side; no bounded search result or source theorem collapses the corridor 22-24 to a single value.

## literature_gap
Publicly checked sources stop at 22 <= R(B2, B9) <= 24.

## transfer_kit
- lemma: DS1.17 records the survey corridor 22 <= R(B2, B9) <= 24.
- lemma: Table 1 of the 2025 paper improves the lower bound to 22.
- lemma: The survey lists exact nearby B2-line values such as R(B2, B8) = 21 and R(B2, B6) = 17.
- toy example: The exact case R(B2, B8) = 21 is the nearest solved benchmark below the target.
- known obstruction: The extra middle value means a proof may need both a lower-end witness analysis and an upper-end forcing argument rather than a single rigid one-gap contradiction.
- prior-work stop sentence: Current checked sources stop at 22 <= R(B2, B9) <= 24.
- recommended first attack: Start by attempting to rule out a 23-vertex witness through common-neighbor constraints before investing in broader generation.
- paper if solved: The paper would be a short exact-value note on the B2-versus-book family.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Table 1, which improves the lower bound to 22; Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, June 7, 2024), Section 5.3 and Table IXa, which record the corridor 22-24; and bounded exact-statement, alternate-notation, canonical-source, and recent-status web checks on 2026-04-14 that did not surface a later exact determination.
- Radziszowski DS1.17 Section 5.3 and Table IXa, Lidicky-McKinley-Pfender-Van Overberghe 2025 Table 1, and bounded 2026-04-14 exact-term, alternate-notation, outside-source, and recent-status web checks.
- artifacts/r-b2-b9-book-ramsey/record.md
- artifacts/r-b2-b9-book-ramsey/status.json
