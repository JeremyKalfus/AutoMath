# Working Packet: The Exact Value of R(B27, B29)

- slug: `r-b27-b29-two-off-book-ramsey`
- title: Determine the exact value of R(B27, B29)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `52`
- single-solve-to-paper fraction: `0.55`

## statement
Determine the least N such that every graph on N vertices contains B27 or its complement contains B29.

## novelty_notes
- frontier basis: Current checked sources prove the lower pattern only through n <= 21, while the older exact upper surface gives R(B27, B29) <= 113 because 29 ≡ 2 (mod 3).
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A sharp closure at 113 would be meaningful as another beyond-range confirmation. But the note is not near-paper now because the lower side of the packet is pattern evidence rather than a theorem for this scale.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: unresolved
- theorem-slice stability: fragile
- search-heavy: True
- certificate compactness: low
- exact gap from source: moderate
- assessment: Not lane-eligible. This is a pattern-probing watchlist candidate, not a current one-shot publication candidate.

## likely_paper_shape
- note title: The Exact Value of R(B27, B29)
- hypothetical title: The Exact Value of R(B27, B29)
- paper shape: A speculative continuation note for the two-off book line beyond the proved range, provided the expected pattern survives intact.
- publication if solved: If solved sharply at 113, this could support a brief pattern-extension note, but it is too far from a near-paper packet for the strict micro-paper lane.
- minimal artifact requirements: Either an explicit 112-vertex Ramsey-(B27, B29) witness or a proof that every 113-vertex graph contains B27 or its complement contains B29.

## hypothetical_abstract
We determine the Ramsey number R(B27, B29). Current checked sources still prove the two-off lower pattern only in a smaller range, but the classical upper-bound surface fixes the natural target value 113 for this pair. Any exact closure would therefore speak to the persistence of the two-off book Ramsey pattern beyond the currently proved interval.

## single_solve_explanation
This is too speculative for the micro-paper lane because the honest paper would almost certainly be about pattern extension, not this single tuple by itself. A solve would still need heavy narrative work explaining why n = 29 matters and why the result should not be absorbed into a broader theorem. That keeps the single-solve-to-paper fraction low.

## broader_theorem_nonimplication
The 2025 theorem does not reach n = 29, and its discussion makes clear that extension beyond the proved range is open. The older upper-bound surface only pins a natural target; it does not imply the exact value.

## literature_gap
Checked sources establish the two-off lower theorem only through n <= 21 and the older upper theorem gives R(B27, B29) <= 113; no exact closure surfaced in the bounded audit.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe 2025 proves the two-off lower line 4n - 3 <= R(B_{n-2}, B_n) only for 4 <= n <= 21.
- lemma: The same paper cites the older upper-bound surface R(B_{n-2}, B_n) <= 4n - 3 when n ≡ 2 (mod 3).
- lemma: For n = 29, that upper-bound surface yields R(B27, B29) <= 113.
- lemma: Wesley 2026 contributes modern lower-bound infrastructure but no exact closure of this tuple in the checked sources.
- toy example: The proved two-off cases at n = 20 and n = 21 are the nearest theorem-level models for the expected pattern.
- known obstruction: There is no theorem-level lower bound for this exact scale in the checked literature, so the candidate would likely require heavy search or a new general argument.
- prior-work stop sentence: Current checked sources stop with the proved two-off lower theorem at n <= 21 and the natural upper target R(B27, B29) <= 113.
- recommended first attack: Do not prioritize this for live solve; if revisited, begin with a structured witness search at 112 vertices to see whether the expected pattern value is even plausible.
- paper if solved: If solved sharply, the paper would need to be framed as a cautious extension of the two-off book Ramsey pattern well beyond the current theorem range.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), especially Lemma 1 proving 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and explicitly treating extension further out as open; together with the same paper's citation of the older upper-bound surface R(B_{n-2}, B_n) <= 4n - 3 when n ≡ 2 (mod 3), which for n = 29 gives R(B27, B29) <= 113; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026) as a recent lower-bound infrastructure check; plus bounded 2026-04-14 exact-statement, canonical-source, and recent-status searches that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Lemma 1 and its beyond-range discussion; the cited older upper-bound surface for n ≡ 2 (mod 3); Wesley 2026 as a recent lower-bound status check; and bounded 2026-04-14 exact-term and recent-status searches.
- artifacts/r-b27-b29-two-off-book-ramsey/record.md
- artifacts/r-b27-b29-two-off-book-ramsey/status.json
