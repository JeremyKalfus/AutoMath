# Working Packet: The Exact Value of R(B19, B21)

- slug: `r-b19-b21-book-ramsey`
- title: Determine the exact value of R(B19, B21)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `61`
- single-solve-to-paper fraction: `0.65`

## statement
Either prove that every graph on 81 vertices contains B19 or its complement contains B21 and thus show R(B19, B21) = 81, or construct a 81-vertex graph avoiding B19 whose complement avoids B21 and thus show R(B19, B21) = 82.

## novelty_notes
- frontier basis: The 2025 book-Ramsey theorem gives the lower bound 81 <= R(B19, B21), and the older upper-bound mechanism in DS1.17 gives R(B19, B21) <= 82. The sampled 2026 follow-up confirms the area is active but does not advertise an exact resolution of this larger pair.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved, the result would still yield a complete note. The problem is that the note would feel more like a single late-family exact instance than a crisp benchmark closure, so the editorial burden rises and the immediate narrative weakens.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: weak
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: high
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Fail for the strict lane. The exact gap is tiny and the novelty audit is cheap, but the larger parameter size pushes the target toward an isolated family-instance paper rather than a high-leverage micro-paper.

## likely_paper_shape
- note title: The Exact Value of R(B19, B21)
- hypothetical title: The Exact Value of R(B19, B21)
- paper shape: A larger one-theorem exact-value note on an almost-diagonal book pair.
- publication if solved: An exact value for R(B19, B21) would be publishable, but the story is weaker and more instance-heavy than the strict micro-paper lane should prefer.
- minimal artifact requirements: Either a proof that every 81-vertex graph forces B19 or a complement B21, or one explicit 81-vertex witness graph showing the threshold is 82.

## hypothetical_abstract
We determine the book Ramsey number R(B19, B21). Existing work leaves this almost-diagonal case in the one-gap window 81 <= R(B19, B21) <= 82. Our result sharpens the current frontier for exact values of book Ramsey numbers.

## single_solve_explanation
A solve would still produce a standalone paper, because the exact value itself is crisp and the literature shell is already in place. The issue is not publishability but leverage: for parameters this large, the note starts to look more like one more exact instance in an established family than the kind of especially sharp micro-paper target this lane wants.

## broader_theorem_nonimplication
Known exact theorems for diagonal books and for R(B_{n-1}, B_n) do not settle R(B19, B21), but the ambient family is now developed enough that a successful proof would risk reading as one more late-family add-on rather than a standout benchmark closure.

## literature_gap
Current public sources support only the one-gap window 81 <= R(B19, B21) <= 82, and the bounded 2026-04-13 audit did not uncover a later exact determination.

## transfer_kit
- lemma: Theorem 1 of the 2025 book-Ramsey paper gives the lower bound 81 <= R(B19, B21).
- lemma: DS1.17 Section 5.3(g) gives R(B19, B21) <= 2(19 + 21 + 1) = 82.
- lemma: The same 2025 paper proves the neighboring exact value R(B20, B21) = 83 on the B_{n-1} versus B_n line.
- toy example: The exact case R(B20, B21) = 83 is the nearest solved off-diagonal book benchmark above the target.
- known obstruction: A proof of 81 must eliminate every 81-vertex critical graph permitted by the known lower bound, while a proof of 82 needs a single 81-vertex witness graph avoiding B19 and complement-B21.
- prior-work stop sentence: Current sources stop at the one-gap window 81 <= R(B19, B21) <= 82.
- recommended first attack: Only pursue this after smaller fresh almost-diagonal cases, using the same structural templates but expecting a higher risk that the proof package becomes too instance-heavy.
- paper if solved: The paper would be a short exact-value note on a larger almost-diagonal book Ramsey number.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g); William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), abstract-level status check; and bounded exact-term, canonical-source, outside-source, and recent-status web checks performed on 2026-04-13.
- Lidicky-McKinley-Pfender-Van Overberghe 2025, DS1.17 Section 5.3(g), Wesley 2026 abstract-level status check, and bounded 2026-04-13 exact-term, canonical-source, outside-source, and recent-status searches for R(B19, B21).
- artifacts/r-b19-b21-book-ramsey/record.md
- artifacts/r-b19-b21-book-ramsey/status.json
