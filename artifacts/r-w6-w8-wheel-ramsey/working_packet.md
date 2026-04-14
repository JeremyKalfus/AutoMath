# Working Packet: The Exact Value of R(W6, W8)

- slug: `r-w6-w8-wheel-ramsey`
- title: Determine the exact value of R(W6, W8)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `31`
- single-solve-to-paper fraction: `0.41`

## statement
Determine the smallest n such that every graph on n vertices contains W6 or its complement contains W8.

## novelty_notes
- frontier basis: DS1.17 still records the pair as unresolved in the small-wheel table, while the 2025 paper improved other wheel entries without closing this one. Under the bounded audit, however, the exact gap remained too diffuse to support a near-paper packet.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If someone solved the pair cleanly, there would be a note. The issue is that curation could not reduce the current public status to a tight, crisp frontier packet with a cheap novelty check and compact certificate burden.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: weak
- family anchor strength: moderate
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: none
- isolated exact-case risk: high
- broader-theorem implication risk: unresolved
- theorem-slice stability: unclear
- search-heavy: True
- certificate compactness: low
- exact gap from source: broad
- assessment: Fail. This dossier does not currently clear the repo's threshold for closability, certificate compactness, or theorem-slice stability.

## likely_paper_shape
- note title: The Exact Value of R(W6, W8)
- hypothetical title: The Exact Value of R(W6, W8)
- paper shape: At best a search-heavy exact-value note with unclear certificate scope.
- publication if solved: An exact value could still be publishable, but the bounded audit does not make it look like a micro-paper candidate.
- minimal artifact requirements: A substantial critical-graph search, independently checkable certificates, and a refreshed literature audit that first secures a tight finite gap from current sources.

## hypothetical_abstract
We determine the wheel Ramsey number R(W6, W8). Existing survey sources still leave this small-wheel pair unresolved. Any exact result would close a remaining entry in the low-order wheel table.

## single_solve_explanation
A solve would produce the headline theorem, but the current packet is too under-specified for the repo's one-shot standard. Before the actual solve, curation would still need a cleaner finite gap, a clearer certificate plan, and a better handle on whether the theorem slice would stay pair-specific. That is too much pre-solve overhead for this lane.

## broader_theorem_nonimplication
The bounded audit did not recover a broader theorem settling R(W6, W8), but it also did not recover a tight pair-specific frontier packet. That unresolved source picture is itself enough to fail the lane conservatively.

## literature_gap
The bounded 2026-04-13 audit confirmed that R(W6, W8) remains unresolved in the survey literature, but did not secure a tight modern finite gap suitable for a micro-paper packet.

## transfer_kit
- lemma: DS1.17 Table VIII keeps R(W6, W8) unresolved in the small-wheel table.
- lemma: The 2025 wheel paper demonstrates that the surrounding family is still active, though not this pair.
- lemma: Classical small-wheel exact results around W6 provide baseline constructions and computational methods, but not a closure here.
- toy example: The exact diagonal value R(W6, W6) = 17 is the nearest solved baseline involving W6.
- known obstruction: The current public packet does not yet expose a tight finite gap, so any solve attempt risks turning into an unfocused search campaign before it even becomes paper-shaped.
- prior-work stop sentence: Current bounded curation confirms only that the pair remains unresolved in the survey literature, not a tight finite gap.
- recommended first attack: Do not prioritize this until a refreshed literature pass produces a tight finite interval and a tractable critical-graph plan.
- paper if solved: The paper would be an exact-value note only after substantial additional curation and certificate planning.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.2 and Table VIII; Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Section 2 and Table 1; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-13.
- DS1.17 Section 5.2 and Table VIII, Lidicky-McKinley-Pfender-Van Overberghe 2025, and bounded 2026-04-13 exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches for R(W6, W8).
- artifacts/r-w6-w8-wheel-ramsey/record.md
- artifacts/r-w6-w8-wheel-ramsey/status.json
