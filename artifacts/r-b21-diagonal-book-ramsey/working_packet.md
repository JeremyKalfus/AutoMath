# Working Packet: The Exact Value of R(B21, B21)

- slug: `r-b21-diagonal-book-ramsey`
- title: r-b21-diagonal-book-ramsey
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `79`
- single-solve-to-paper fraction: `0.78`

## statement
Either prove that every graph on 85 vertices contains B21 or has a complement containing B21 and thus show R(B21, B21) = 85, or construct an 85-vertex graph with no B21 and no complement B21 and thus show R(B21, B21) = 86.

## novelty_notes
- frontier basis: DS1.17 records the exact diagonal criteria tied to prime powers and sums of two squares. The 2025 paper proves 4n + 1 <= R(Bn, Bn) <= 4n + 2 for 4 <= n <= 21 and covers n = 21 in that one-gap framework, while Wesley 2026 improves lower bounds for books but does not report an exact diagonal closure at n = 21.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: This is a mature one-gap diagonal packet rather than a campaign target. Once n = 21 is settled, the note mainly needs a short explanation of why 85 lies outside the standard exact criteria and the argument that closes the two-point window.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Pass. The gap is tiny, the theorem slice is stable, and one exact solve would already constitute most of a publishable note.

## likely_paper_shape
- note title: The Exact Value of R(B21, B21)
- hypothetical title: The Exact Value of R(B21, B21)
- paper shape: A one-theorem exact-value note on a diagonal book Ramsey number outside the standard exact criteria.
- publication if solved: Settling this final small-range diagonal residue would already support a standalone short note in the book Ramsey program.
- minimal artifact requirements: Either a proof that every 85-vertex graph contains B21 or has complement containing B21, or one explicit 85-vertex graph avoiding B21 in both colors.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B21, B21). Current diagonal criteria leave only the one-gap window 85 <= R(B21, B21) <= 86 because 4n + 1 = 85 is a sum of two squares and not a prime power. Our result closes one of the clean remaining diagonal residues in the exact theory of book Ramsey numbers.

## single_solve_explanation
The exact diagonal value at n = 21 would itself be the title theorem. The family scaffolding, comparison cases, and reason the standard number-theoretic machinery fails are already available in the literature, so the remaining paper work after a solve is mostly contextual exposition and a compact extremal discussion.

## broader_theorem_nonimplication
The known diagonal exact criteria do not settle n = 21 because 85 = 2^2 + 9^2 and is not a prime power. A successful proof would still naturally center on this exact diagonal case rather than collapsing into a broader already-known theorem.

## literature_gap
Current public sources support only the one-gap diagonal window 85 <= R(B21, B21) <= 86, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: Lidický-McKinley-Pfender-Van Overberghe 2025 proves 4n + 1 <= R(Bn, Bn) <= 4n + 2 for all 4 <= n <= 21, hence 85 <= R(B21, B21) <= 86.
- lemma: DS1.17 item 5.3(f) gives the exact diagonal criterion R(Bn, Bn) = 4n + 2 when 4n + 1 is a prime power.
- lemma: The same item gives the upper criterion R(Bn, Bn) <= 4n + 1 when 4n + 1 is not a sum of two squares, which does not apply here because 85 is representable as a sum of two squares.
- toy example: The diagonal family already resolves n = 20 exactly because 81 is a prime power, while n = 21 remains open because 85 escapes both standard exact criteria.
- known obstruction: Any proof of R(B21, B21) = 85 must exclude every 85-vertex extremal template compatible with the known lower-bound machinery, while a proof of R(B21, B21) = 86 requires one explicit 85-vertex witness avoiding B21 in both a graph and its complement.
- prior-work stop sentence: Current sources stop at the one-gap diagonal window 85 <= R(B21, B21) <= 86.
- recommended first attack: Push the published diagonal lower-bound templates against degree-common-neighborhood constraints on 85 vertices and force a 21-page book in one color.
- paper if solved: The paper would be a short exact-value note closing another diagonal book Ramsey residue outside the standard criteria.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), item 5.3(f), together with Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1 and Appendix A, and William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026).
- DS1.17 item 5.3(f), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1 and Appendix A, Wesley 2026, and bounded exact-term, alternate-notation, canonical-source, source-internal, outside-source, and recent-status web checks performed on 2026-04-13, plus local 2026-04-15 attempt-registry conflict checks.
- artifacts/r-b21-diagonal-book-ramsey/record.md
- artifacts/r-b21-diagonal-book-ramsey/status.json
