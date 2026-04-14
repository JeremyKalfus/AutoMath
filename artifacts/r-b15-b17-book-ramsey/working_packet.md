# Working Packet: The Exact Value of R(B15, B17)

- slug: `r-b15-b17-book-ramsey`
- title: Determine the exact value of R(B15, B17)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `75`
- single-solve-to-paper fraction: `0.76`

## statement
Either prove that every graph on 65 vertices contains B15 or its complement contains B17 and thus show R(B15, B17) = 65, or construct a 65-vertex graph avoiding B15 whose complement avoids B17 and thus show R(B15, B17) = 66.

## novelty_notes
- frontier basis: Public sources leave this pair in the one-gap window 65 <= R(B15, B17) <= 66. The 2025 theorem provides the lower bound, DS1.17 continues to provide only the general upper bound, and Wesley 2026 resolves the adjacent B16 versus B17 case rather than this one.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The write-up after a successful solve is short and standard: exact statement, forcing proof or extremal graph, one comparison with the solved R(B16, B17) benchmark, and a brief discussion of why the broader almost-diagonal line remains open. That is enough for a clean note.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass. This remains a one-gap exact target on a recent family frontier, and the solve would already carry most of the note's mathematical and editorial content.

## likely_paper_shape
- note title: The Exact Value of R(B15, B17)
- hypothetical title: The Exact Value of R(B15, B17)
- paper shape: A one-theorem exact-value note on the almost-diagonal book Ramsey line.
- publication if solved: Closing R(B15, B17) would already support a short exact-value note on the unresolved almost-diagonal book Ramsey strip.
- minimal artifact requirements: Either a proof that every 65-vertex graph forces B15 or a complement B17, or one explicit 65-vertex witness graph avoiding B15 whose complement avoids B17.

## hypothetical_abstract
We determine the book Ramsey number R(B15, B17). Existing public sources leave this almost-diagonal pair in the one-gap window 65 <= R(B15, B17) <= 66. Our result removes another clean frontier residue from the B_{n-2} versus B_n book Ramsey line.

## single_solve_explanation
The exact value would already be the central theorem of the note. Family framing, old upper-bound technology, and the recent lower-bound source are already available, so the solve does most of the real work. The remaining editorial load is small enough for the micro-paper lane.

## broader_theorem_nonimplication
The known exact theorem for R(B_{n-1}, B_n) gives R(B16, B17) = 67 but does not settle R(B15, B17). For n = 17, public sources still leave only the one-gap interval 65 <= R(B15, B17) <= 66.

## literature_gap
Current public sources support only 65 <= R(B15, B17) <= 66, and the bounded 2026-04-14 exact-term and alternate-notation audit did not uncover a later exact determination.

## transfer_kit
- lemma: Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 65 <= R(B15, B17).
- lemma: DS1.17 Section 5.3(g) gives R(B15, B17) <= 2(15 + 17 + 1) = 66.
- lemma: Wesley 2026 gives the adjacent exact benchmark R(B16, B17) = 67.
- toy example: The neighboring exact case R(B16, B17) = 67 is the nearest solved comparison immediately above the target.
- known obstruction: A 66-proof needs a 65-vertex avoiding graph, while a 65-proof must show that the structured lower-bound templates fail to extend one more vertex.
- prior-work stop sentence: Current sources stop at the one-gap window 65 <= R(B15, B17) <= 66.
- recommended first attack: Treat the 65-vertex witness question as the first branch, because a failed extension search would immediately sharpen the case for a forcing proof at 65.
- paper if solved: The paper would be a short exact-value note on an unresolved almost-diagonal book Ramsey pair.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), Theorem 2 and appendix benchmarks; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14.
- DS1.17 Section 5.3(g), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Wesley 2026 Theorem 2 and appendix benchmarks, plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches on 2026-04-14.
- artifacts/r-b15-b17-book-ramsey/record.md
- artifacts/r-b15-b17-book-ramsey/status.json
