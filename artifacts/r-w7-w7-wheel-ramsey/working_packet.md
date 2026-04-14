# Working Packet: The Exact Value of R(W7, W7)

- slug: `r-w7-w7-wheel-ramsey`
- title: Determine the exact value of R(W7, W7)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `47`
- single-solve-to-paper fraction: `0.56`

## statement
Determine the smallest n such that every graph on n vertices contains W7 or its complement contains W7.

## novelty_notes
- frontier basis: The current survey still lists the diagonal W7 case as unresolved, and the 2025 paper adds other wheel exact values without reporting a closure here. That leaves a legitimate frontier table entry, but not a one-gap residue.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved, the result would still be table-worthy. The issue is not whether a note exists, but whether a single solve is already 70-90 percent of that note; for this diagonal wheel case, the likely search and packaging burden is too large.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: low
- exact gap from source: small
- assessment: Fail. This is still a real open table entry, but it is too wide and too certificate-heavy for the repo's current one-shot micro-paper lane.

## likely_paper_shape
- note title: The Exact Value of R(W7, W7)
- hypothetical title: The Exact Value of R(W7, W7)
- paper shape: A diagonal wheel exact-value note with nontrivial certificate packaging.
- publication if solved: An exact diagonal wheel value could still support a note, but it would likely be classification-heavy rather than micro-paper clean.
- minimal artifact requirements: A full classification or a complete witness-elimination computation near the threshold, plus independently checkable certificates for all surviving critical graphs.

## hypothetical_abstract
We determine the diagonal wheel Ramsey number R(W7, W7). Current survey data leaves this case between 22 and 25. Our result would close a long-standing small-wheel table entry.

## single_solve_explanation
An exact solve would certainly be the central theorem. However, because the present gap is several integers wide and the likely route is computational classification, the paper would still need substantial infrastructure around witness management, critical-graph counts, and certificate presentation after the solve. That misses the strict micro-paper target.

## broader_theorem_nonimplication
Known diagonal and off-diagonal exact wheel values for smaller sizes do not determine R(W7, W7). The current public table still leaves a four-value window.

## literature_gap
Current public sources leave R(W7, W7) in the range 22 <= R(W7, W7) <= 25, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: DS1.17 Table VIII records the unresolved range 22 <= R(W7, W7) <= 25.
- lemma: The 2025 paper shows that small wheel Ramsey tables are still moving by closing other exact entries such as R(W5, W7) and R(W5, W9).
- lemma: Faudree-McKay 1993 provides the classical exact small-wheel baseline and search methodology for neighboring sizes.
- toy example: The exact diagonal value R(W6, W6) = 17 is the nearest smaller solved diagonal wheel benchmark.
- known obstruction: A diagonal wheel closure at this size likely requires broad critical-graph enumeration, so even a successful solve may come with bulky certificate management.
- prior-work stop sentence: Current sources stop at 22 <= R(W7, W7) <= 25.
- recommended first attack: Do not prioritize this unless a lightweight structural reduction sharply narrows the critical search space first.
- paper if solved: The paper would be a diagonal wheel exact-value note, but not a clean micro-paper by the repo's strict standard.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.2 and Table VIII; Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Section 2 and Table 1; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-13.
- DS1.17 Section 5.2 and Table VIII, Lidicky-McKinley-Pfender-Van Overberghe 2025, and bounded 2026-04-13 exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches for R(W7, W7).
- artifacts/r-w7-w7-wheel-ramsey/record.md
- artifacts/r-w7-w7-wheel-ramsey/status.json
