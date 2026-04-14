# Working Packet: The Exact Value of R(B4, B4)

- slug: `r-b4-b4-diagonal-book-ramsey`
- title: Determine the exact value of R(B4, B4)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `88`
- single-solve-to-paper fraction: `0.86`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic copy of the 4-page book graph B4.

## novelty_notes
- frontier basis: The 2025 EJC paper compresses the diagonal book case to the sharp interval 17 <= R(B4, B4) <= 18, and the usual sum-of-two-squares exactness shortcut does not resolve 17 because 17 = 1^2 + 4^2. This leaves a genuine one-step frontier rather than a case already collapsed by a broader criterion.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact value is found, the decisive proof or critical coloring is already almost the whole note. What remains is a short contextual paragraph about recent diagonal-book progress, a compact verification artifact, and a brief comparison with neighboring exact diagonal cases.
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
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass. This is a stable one-step exact gap in a named active family, and a clean solve would already look like a real short paper rather than a curiosity.

## likely_paper_shape
- note title: The Exact Value of R(B4, B4)
- hypothetical title: The Exact Value of R(B4, B4)
- paper shape: A one-theorem note settling the first unresolved small diagonal book Ramsey number left at a one-step interval.
- publication if solved: An exact determination of R(B4, B4) would already be the title theorem of a short note closing the first still-open diagonal book Ramsey case after the recent one-step family bounds.
- minimal artifact requirements: Either an explicit B4-free red-blue coloring of K17 or a proof that every coloring of K18 contains a monochromatic B4, together with a compact verification certificate.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B4, B4). Recent bounds leave this parameter in the sharp interval 17 <= R(B4, B4) <= 18, with neither the existing lower-bound constructions nor the standard sum-of-two-squares shortcut deciding the case. Our result closes the first unresolved small diagonal book case left by the recent family bounds.

## single_solve_explanation
One exact solve would already be the honest main theorem of the paper. The family anchor is strong because diagonal book Ramsey numbers are currently being tightened systematically, and this is the smallest unresolved one-step case in that recent line. After the solve, only short contextual packaging and the verification artifact remain.

## broader_theorem_nonimplication
The recent family theorem only gives 4n + 1 <= R(Bn, Bn) <= 4n + 2, and the known exactness shortcut applies only when 4n + 1 is not a sum of two squares. Here 17 is a sum of two squares, so no broader published criterion found in the bounded audit already settles the case.

## literature_gap
Current public sources stop at 17 <= R(B4, B4) <= 18.

## transfer_kit
- lemma: Pchelintsev, Rath, and Angeltveit (2025), Theorem 1, implies the lower bound R(B4, B4) >= 17.
- lemma: The same theorem gives the upper bound R(B4, B4) <= 18.
- lemma: The note after Theorem 1 states that R(Bn, Bn) = 4n + 1 when 4n + 1 is not a sum of two squares; this does not apply here because 17 = 1^2 + 4^2.
- lemma: The 2026 Wesley paper confirms that diagonal and near-diagonal book Ramsey numbers remain an active lower-bound frontier, so the family narrative is current.
- toy example: The exact solved neighbor R(B8, B8) = 33 shows how a single diagonal-book closure in this family already supports a compact standalone note.
- known obstruction: A lower-bound proof must exhibit a 2-coloring of K17 with no monochromatic B4, while an upper-bound proof must eliminate every such critical coloring at order 17.
- prior-work stop sentence: Current sources stop at 17 <= R(B4, B4) <= 18.
- recommended first attack: Start from the recent block-circulant and search-guided lower-bound constructions for book Ramsey numbers and analyze whether the K17 critical pattern can be completed or ruled out by a tight neighborhood case split.
- paper if solved: The paper would be a concise exact-value note closing the first unresolved small diagonal book Ramsey case left at a one-step interval.

## bounded_source_list
- Maksim V. Pchelintsev, Peter Rath, and Sebastian Angeltveit, "New lower and upper bounds on Ramsey numbers" (Electronic Journal of Combinatorics 32(4) (2025), #P4.64), Theorem 1 and the note immediately following it, which imply 17 <= R(B4, B4) <= 18; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026), 114913) as independent recent family context and bounded 2026-04-14 web checks that did not reveal a later exact closure.
- 2025 EJC P4.64 Theorem 1 and follow-up note, the 2026 Wesley Discrete Mathematics paper for recent family context, plus bounded 2026-04-14 exact-notation and status web checks.
- artifacts/r-b4-b4-diagonal-book-ramsey/record.md
- artifacts/r-b4-b4-diagonal-book-ramsey/status.json
