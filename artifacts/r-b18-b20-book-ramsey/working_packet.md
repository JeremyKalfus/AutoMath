# Working Packet: The Exact Value of R(B18, B20)

- slug: `r-b18-b20-book-ramsey`
- title: Determine the exact value of R(B18, B20)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `65`
- single-solve-to-paper fraction: `0.7`

## statement
Either prove that every graph on 77 vertices contains B18 or its complement contains B20 and thus show R(B18, B20) = 77, or construct a 77-vertex graph avoiding B18 whose complement avoids B20 and thus show R(B18, B20) = 78.

## novelty_notes
- frontier basis: Current public sources leave this pair in the one-gap window 77 <= R(B18, B20) <= 78. The same family has seen substantial recent movement, but no public source found in the bounded audit closes this exact pair.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: This candidate is farther out than the smaller almost-diagonal pairs, but it remains paper-shaped because the gap is still one and the family scaffold is already in place. After the solve, the paper mostly writes itself from the exact proof or witness and the adjacent solved benchmark.
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
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Pass, but at the floor of the strict lane. The family anchor remains strong and the gap is still one, yet the larger threshold modestly increases certificate and proof-management risk.

## likely_paper_shape
- note title: The Exact Value of R(B18, B20)
- hypothetical title: The Exact Value of R(B18, B20)
- paper shape: A one-theorem exact-value note on the almost-diagonal book Ramsey line.
- publication if solved: Closing R(B18, B20) would still support a concise exact-value note on the unresolved almost-diagonal book Ramsey line inside the current source-backed range.
- minimal artifact requirements: Either a proof that every 77-vertex graph forces B18 or a complement B20, or one explicit 77-vertex witness graph avoiding B18 whose complement avoids B20.

## hypothetical_abstract
We determine the book Ramsey number R(B18, B20). Existing public sources leave this almost-diagonal case in the one-gap window 77 <= R(B18, B20) <= 78. Our result closes a clean unresolved point on the current book Ramsey frontier.

## single_solve_explanation
The exact determination would be the honest main theorem of the note. The solve-to-paper fraction is lower than for the smaller candidates only because the threshold is larger and any witness may be somewhat less transparent, but the result still remains inside the micro-paper band. No feeder ladder is needed once the exact value is established.

## broader_theorem_nonimplication
Recent exact results on the line R(B_{n-1}, B_n) do not imply an exact value for R(B_{n-2}, B_n). For n = 20, public sources still give only 77 <= R(B18, B20) <= 78.

## literature_gap
Current public sources support only 77 <= R(B18, B20) <= 78, and the bounded 2026-04-14 exact-term and alternate-notation audit did not uncover a later exact determination.

## transfer_kit
- lemma: Lidický-McKinley-Pfender-Van Overberghe 2025, Theorem 1, gives 77 <= R(B18, B20).
- lemma: DS1.17 Section 5.3(g) gives R(B18, B20) <= 2(18 + 20 + 1) = 78.
- lemma: Wesley 2026 gives the adjacent exact benchmark R(B19, B20) = 79.
- toy example: The neighboring exact case R(B19, B20) = 79 is the nearest solved comparison above the target.
- known obstruction: The main risk is that a 78-proof may require a less transparent 77-vertex witness than the smaller candidates, so any exact closure must still keep the certificate compact enough for a short note.
- prior-work stop sentence: Current sources stop at the one-gap window 77 <= R(B18, B20) <= 78.
- recommended first attack: Use the 2025 construction family as a constrained extension problem first and insist on a human-readable witness or a short nonextension proof before allowing any heavier search.
- paper if solved: The paper would be a concise exact-value note on a one-gap book Ramsey frontier case.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.3(g); Bernard Lidický, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1; William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026), Theorem 2 and appendix benchmarks; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-14.
- DS1.17 Section 5.3(g), Lidický-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Wesley 2026 Theorem 2 and appendix benchmarks, plus bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches on 2026-04-14.
- artifacts/r-b18-b20-book-ramsey/record.md
- artifacts/r-b18-b20-book-ramsey/status.json
