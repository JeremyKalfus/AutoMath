# Working Packet: The Exact Value of R(B16, B16)

- slug: `r-b16-diagonal-book-ramsey`
- title: Determine the exact value of R(B16, B16)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `85`
- single-solve-to-paper fraction: `0.82`

## statement
Either prove that every graph on 65 vertices contains B16 or has a complement containing B16 and thus show R(B16, B16) = 65, or construct a 65-vertex graph with no B16 and no complement B16 and thus show R(B16, B16) = 66.

## novelty_notes
- frontier basis: DS1.17 records the diagonal criteria R(Bn, Bn) = 4n + 2 when 4n + 1 is a prime power and R(Bn, Bn) <= 4n + 1 when 4n + 1 is not a sum of two squares. The 2025 paper proves 4n + 1 <= R(Bn, Bn) <= 4n + 2 for 4 <= n <= 21 and provides the lower-bound construction framework covering n = 16, while Wesley 2026 improves book lower bounds without reporting an exact closure of the n = 16 diagonal case.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The family theorem, the two standard exact criteria, and the narrow one-gap residue are already in place. If the exact value at n = 16 is settled, the remaining paper work is mostly a compact explanation of why 65 escapes the standard criteria and how the forcing or obstruction closes the gap.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Pass. This is a stable one-gap diagonal residue in a named family, with a clean story, low novelty-check cost, and very short solve-to-paper distance.

## likely_paper_shape
- note title: The Exact Value of R(B16, B16)
- hypothetical title: The Exact Value of R(B16, B16)
- paper shape: A one-theorem exact-value note on a diagonal book Ramsey number left outside the standard number-theoretic criteria.
- publication if solved: Closing this one-gap diagonal residue would already read as the title theorem of a genuine short note on book Ramsey numbers.
- minimal artifact requirements: Either a proof that every 65-vertex graph contains B16 or has complement containing B16, or one explicit 65-vertex graph avoiding B16 in both colors.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B16, B16). Existing diagonal criteria leave the case n = 16 in the one-gap window 65 <= R(B16, B16) <= 66 because 4n + 1 = 65 is a sum of two squares but not a prime power. Our result closes a clean residual diagonal case in the book Ramsey table and sharpens the current boundary of the exact theory.

## single_solve_explanation
The exact n = 16 diagonal value is already the honest title theorem. The surrounding paper infrastructure is unusually mature: the diagonal one-gap framework is published, the standard exact criteria are known, and the residue is a single named case with an immediate table update. After a solve, only light exposition and comparison with the existing exact diagonal cases remain.

## broader_theorem_nonimplication
The published diagonal exact criteria do not already settle n = 16 because 4n + 1 = 65 is neither a prime power nor excluded by the sum-of-two-squares obstruction. A shortest proof may use more structure than the published criteria, but the honest theorem would still remain this exact diagonal residue rather than a generic corollary of a known broader statement.

## literature_gap
Current public sources support only the one-gap window 65 <= R(B16, B16) <= 66, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: Lidický-McKinley-Pfender-Van Overberghe 2025 proves 4n + 1 <= R(Bn, Bn) <= 4n + 2 for all 4 <= n <= 21, hence 65 <= R(B16, B16) <= 66.
- lemma: DS1.17 item 5.3(f) records the exact criterion R(Bn, Bn) = 4n + 2 when 4n + 1 is a prime power.
- lemma: The same item records that if 4n + 1 is not a sum of two integer squares, then R(Bn, Bn) <= 4n + 1, explaining why many neighboring diagonal cases are exact while n = 16 is not covered.
- toy example: The nearby diagonal cases resolved by number-theoretic criteria provide the worked comparison: n = 17 is exact because 69 is not a sum of two squares, while n = 16 remains undecided because 65 = 1^2 + 8^2.
- known obstruction: Any proof of R(B16, B16) = 65 must eliminate every 65-vertex extremal template compatible with the published lower-bound constructions, while a proof of R(B16, B16) = 66 needs one explicit 65-vertex witness avoiding B16 in both a graph and its complement.
- prior-work stop sentence: Current sources stop at the one-gap diagonal window 65 <= R(B16, B16) <= 66.
- recommended first attack: Start from the published block-circulant and polycirculant lower-bound templates and prove that any 65-vertex extension necessarily creates a spine with at least 16 common neighbors in one color.
- paper if solved: The paper would be a short exact-value note closing a diagonal book Ramsey residue left open by the standard number-theoretic criteria.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), item 5.3(f); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1 and Appendix A; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026); and bounded exact-term, alternate-notation, canonical-source, source-internal, outside-source, and recent-status web checks performed on 2026-04-13.
- DS1.17 item 5.3(f), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1 and Appendix A, Wesley 2026, and bounded 2026-04-13 exact-statement, alternate-notation, source-internal, outside-source, and recent-status searches for R(B16, B16).
- artifacts/r-b16-diagonal-book-ramsey/record.md
- artifacts/r-b16-diagonal-book-ramsey/status.json
