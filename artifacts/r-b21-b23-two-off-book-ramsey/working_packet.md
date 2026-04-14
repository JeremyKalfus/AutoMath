# Working Packet: The Exact Value of R(B21, B23)

- slug: `r-b21-b23-two-off-book-ramsey`
- title: Determine the exact value of R(B21, B23)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `58`
- single-solve-to-paper fraction: `0.63`

## statement
Determine the least N such that every graph on N vertices contains a red copy of B21 or its complement contains a blue copy of B23.

## novelty_notes
- frontier basis: The 2025 source gives the exact two-off pattern up to n <= 21 and points to extension beyond that range as open terrain, while earlier work supplies the upper bound R(B21, B23) <= 89 because 23 ≡ 2 (mod 3).
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If an exact lower bound of 89 were proved, the resulting note could be framed as the first beyond-range extension of the two-off book pattern at a specific parameter. But the curation pass could not certify that the honest theorem slice would stay instance-level rather than shifting to a broader extension theorem.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: unresolved
- theorem-slice stability: unclear
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: moderate
- assessment: Not lane-eligible. The family anchor is real, but the theorem slice is unclear, the search and novelty costs are high, and the post-solve packaging risk is too large for the one-shot micro-paper objective.

## likely_paper_shape
- note title: The Exact Value of R(B21, B23)
- hypothetical title: The Exact Value of R(B21, B23)
- paper shape: A pattern-extension note beyond the proved 2025 range, provided the exact value lands on the expected two-off book line and the proof does not collapse into a broader theorem.
- publication if solved: If this exact pair were settled at the natural 4n-3 frontier, it could support a short note on extending the book-Ramsey two-off pattern beyond the 2025 range.
- minimal artifact requirements: An 88-vertex Ramsey-(B21,B23) witness or a proof that every 89-vertex graph contains B21 or its complement contains B23.

## hypothetical_abstract
We determine the Ramsey number R(B21, B23). Current checked sources give strong pattern evidence from the 2025 small-book Ramsey paper and an earlier upper-bound surface at 89, but do not cheaply certify an exact value for this specific pair. If closed sharply, the result would sit as a first beyond-range data point for the two-off book pattern.

## single_solve_explanation
This target does not pass the micro-paper lane because one exact solve may still need substantial packaging to justify why the isolated pair matters. The note only becomes paper-shaped if the result lands on the expected pattern value and can be framed cleanly against the 2025 theorem. There is also real risk that the proof, if it works, naturally wants to prove a broader family statement instead.

## broader_theorem_nonimplication
The 2025 theorem proves the two-off lower pattern only through n <= 21, and its own open-question section explicitly asks whether that pattern extends further. That makes direct implication by published broader theorems unresolved rather than low-risk.

## literature_gap
Checked sources establish the relevant pattern only up to n <= 21 and do not certify an exact value for R(B21, B23).

## transfer_kit
- lemma: EJC 2025 Theorem 1 proves 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21.
- lemma: The same paper records that earlier work already gave R(B_{n-2}, B_n) <= 4n - 3 when n ≡ 2 (mod 3), which for n = 23 gives the upper bound R(B21, B23) <= 89.
- lemma: Section 4.2.1 states that extending the pattern beyond the proved range remains open and plausible from the construction side.
- lemma: The 2026 lower-bound paper provides modern block-circulant and SAT-oriented infrastructure around book Ramsey lower bounds.
- toy example: The exact behavior at n = 20 or 21 in the 2025 theorem is the nearest structural model for the pair (21,23).
- known obstruction: The available lower-bound constructions are highly search-driven and do not yet exhibit a clean family pattern beyond the proved range.
- prior-work stop sentence: Current checked sources prove the two-off book pattern only through n <= 21 and do not certify the exact pair (21,23).
- recommended first attack: Try to build an 88-vertex 2-polycirculant Ramsey-(B21,B23) witness first, because the older upper-bound surface already pins the natural target value at 89.
- paper if solved: If solved sharply at 89, the paper would be a short pattern-extension note for two-off book Ramsey numbers just beyond the 2025 theorem range.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), especially Theorem 1 and the open-question discussion in Section 4.2.1; together with the note in that paper that earlier work already gave R(B_{n-2}, B_n) <= 4n - 3 when n ≡ 2 (mod 3), and the 2026 paper "Lower bounds for book Ramsey numbers" cited there as [39] for additional lower-bound infrastructure. The bounded 2026-04-14 curation pass did not find a later exact closure for the specific pair (21,23), but also did not secure a cheap theorem-level status audit strong enough to pass the micro-paper lane.
- EJC 2025 Table 1, Theorem 1, and Section 4.2.1; the cited earlier upper-bound surface for R(B_{n-2}, B_n) when n ≡ 2 (mod 3); and the 2026 lower-bound paper for book Ramsey numbers.
- artifacts/r-b21-b23-two-off-book-ramsey/record.md
- artifacts/r-b21-b23-two-off-book-ramsey/status.json
