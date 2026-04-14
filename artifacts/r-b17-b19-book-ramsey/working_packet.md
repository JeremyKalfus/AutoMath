# Working Packet: The Exact Value of R(B17, B19)

- slug: `r-b17-b19-book-ramsey`
- title: Determine the exact value of R(B17, B19)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `69`
- single-solve-to-paper fraction: `0.72`

## statement
Either prove that every graph on 73 vertices contains B17 or its complement contains B19 and thus show R(B17, B19) = 73, or construct a 73-vertex graph avoiding B17 whose complement avoids B19 and thus show R(B17, B19) = 74.

## novelty_notes
- frontier basis: The 2025 almost-diagonal book theorem yields the lower bound 73 <= R(B17, B19), while the older general upper-bound machinery in the survey still leaves only R(B17, B19) <= 74. The sampled 2026 Wesley paper reports continued progress on book lower bounds and the exact B_{n-1} versus B_n line, but no exact closure of this B_{n-2} versus B_n pair.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: This is a canonical one-gap residue in the same recent book-Ramsey lane as the stronger smaller instances. After one clean solve, the remaining paper would mostly be the forcing proof or critical witness, one nearby comparison, and a short paragraph explaining why the exact B_{n-1} versus B_n theorem does not subsume this case.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass. The family anchor is strong, the gap is one, and one exact solve would already look like the title theorem of a short note rather than a loose benchmark remark.

## likely_paper_shape
- note title: The Exact Value of R(B17, B19)
- hypothetical title: The Exact Value of R(B17, B19)
- paper shape: A one-theorem exact-value note on the B_{n-2} versus B_n book line.
- publication if solved: Closing R(B17, B19) would already support a compact note on the remaining one-gap almost-diagonal book Ramsey cases inside the currently source-backed range.
- minimal artifact requirements: Either a proof that every 73-vertex graph forces B17 or a complement B19, or one explicit 73-vertex witness graph avoiding B17 whose complement avoids B19.

## hypothetical_abstract
We determine the book Ramsey number R(B17, B19). Existing work leaves this almost-diagonal case in the one-gap window 73 <= R(B17, B19) <= 74. Our result closes one of the last clean one-gap residues in the currently source-backed B_{n-2} versus B_n range.

## single_solve_explanation
The exact value would already be the honest title theorem of the note. Because the family framework, notation, and neighboring solved cases are already standardized by the 2025 and 2026 book-Ramsey papers, the post-solve writing burden is small: proof or witness, one neighbor comparison, and a brief non-implication paragraph. That places the solve-to-paper fraction inside the target band.

## broader_theorem_nonimplication
The exact B_{n-1} versus B_n theorem settles R(B18, B19) but does not imply R(B17, B19). For this pair, the current public record supplies a lower bound from the 2025 almost-diagonal theorem and an upper bound from the survey inequality, but no exact closure.

## literature_gap
Current public sources support only the one-gap window 73 <= R(B17, B19) <= 74, and the bounded 2026-04-14 audit did not uncover a later exact determination.

## transfer_kit
- lemma: Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 73 <= R(B17, B19).
- lemma: DS1.17 Section 5.3(g) gives R(B17, B19) <= 2(17 + 19 + 1) = 74.
- lemma: The survey and Wesley 2026 give the adjacent exact benchmark R(B18, B19) = 75.
- toy example: The exact neighboring case R(B18, B19) = 75 is the closest solved off-diagonal benchmark above the target.
- known obstruction: A proof of 73 must eliminate every 73-vertex critical graph compatible with the current lower bound, while a proof of 74 needs one explicit 73-vertex witness graph avoiding B17 whose complement avoids B19.
- prior-work stop sentence: Current sources stop at the one-gap window 73 <= R(B17, B19) <= 74.
- recommended first attack: Start from the 2025 polycirculant lower-bound templates and test whether the extra two pages force a short rigidity argument before any bounded witness search is invoked.
- paper if solved: The paper would be a short exact-value note on a fresh almost-diagonal book Ramsey case.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1 and proof notes; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), Theorem 2 and appendix benchmarks; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14.
- DS1.17 Section 5.3(g), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1 and proof notes, Wesley 2026 Theorem 2 and appendix benchmarks, plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches on 2026-04-14.
- artifacts/r-b17-b19-book-ramsey/record.md
- artifacts/r-b17-b19-book-ramsey/status.json
