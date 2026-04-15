# Working Packet: The Exact Value of R(B24, B26)

- slug: `r-b24-b26-two-off-book-ramsey`
- title: Determine the exact value of R(B24, B26)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `56`
- single-solve-to-paper fraction: `0.58`

## statement
Determine the least N such that every graph on N vertices contains B24 or its complement contains B26.

## novelty_notes
- frontier basis: Current checked sources prove the two-off lower pattern only through n <= 21, while the older exact upper surface gives R(B24, B26) <= 101 because 26 ≡ 2 (mod 3).
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A sharp closure at 101 would be mathematically meaningful as a first clean beyond-range confirmation of the two-off pattern. But the packet is not near-paper by current standards because the source-backed lower side has not caught up to the upper side.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: unresolved
- theorem-slice stability: unclear
- search-heavy: True
- certificate compactness: low
- exact gap from source: moderate
- assessment: Not lane-eligible. This is a plausible pattern-extension target, not a one-shot micro-paper target.

## likely_paper_shape
- note title: The Exact Value of R(B24, B26)
- hypothetical title: The Exact Value of R(B24, B26)
- paper shape: A beyond-range extension note for the two-off book Ramsey line, but only if the proof lands cleanly on the expected pattern value.
- publication if solved: If the pair were solved sharply at the natural pattern value 101, it could support a short pattern-extension note, but the present packet is too unstable for the strict micro-paper lane.
- minimal artifact requirements: Either an explicit 100-vertex Ramsey-(B24, B26) witness or a proof that every 101-vertex graph contains B24 or its complement contains B26.

## hypothetical_abstract
We determine the Ramsey number R(B24, B26). Current checked sources prove the two-off lower pattern only through n <= 21 but still give the natural upper target R(B24, B26) <= 101 from the classical n ≡ 2 (mod 3) surface. If the exact value is shown to equal 101, the result would supply a first explicit extension point beyond the proved 2025 range.

## single_solve_explanation
This fails the micro-paper lane because even a successful solve would still need substantial pattern-justification and beyond-range positioning. The honest paper would almost certainly be about extending the two-off line, not only about this one tuple. That makes the theorem slice unstable before solve.

## broader_theorem_nonimplication
The 2025 theorem only proves the two-off lower line through n = 21, and it explicitly treats extension beyond that range as open. The older upper-bound surface pins the natural target at 101 for n = 26, but it does not settle the exact value by itself.

## literature_gap
Checked sources establish the two-off lower theorem only up to n <= 21 and the older upper theorem gives R(B24, B26) <= 101; no exact closure surfaced in the bounded audit.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe 2025 proves 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21.
- lemma: The same paper cites the older upper-bound surface R(B_{n-2}, B_n) <= 4n - 3 when n ≡ 2 (mod 3).
- lemma: For n = 26, that older surface yields R(B24, B26) <= 101.
- lemma: Wesley 2026 provides recent lower-bound infrastructure around book Ramsey constructions without advertising an exact closure of this pair.
- toy example: The proved two-off pattern at n = 21 is the nearest source-backed benchmark immediately below the target range.
- known obstruction: The current lower-bound theorem stops at n = 21, so any exact progress at n = 26 likely needs a search-heavy witness or a new general lower-bound argument.
- prior-work stop sentence: Current checked sources stop with the proved two-off lower theorem at n <= 21 and the natural upper target R(B24, B26) <= 101.
- recommended first attack: Start with a highly symmetric 100-vertex witness search, because the classical upper surface already identifies 101 as the natural pattern endpoint.
- paper if solved: If solved at 101, the paper would need to be framed as a first beyond-range continuation of the two-off book Ramsey pattern.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), especially Lemma 1 proving 4n - 3 <= R(B_{n-2}, B_n) for 4 <= n <= 21 and explicitly highlighting extension beyond that range as open; together with the same paper's citation of the older exact upper-bound surface R(B_{n-2}, B_n) <= 4n - 3 when n ≡ 2 (mod 3), which for n = 26 gives R(B24, B26) <= 101; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5), 2026) as a recent lower-bound infrastructure check; plus bounded 2026-04-14 exact-statement, canonical-source, and recent-status searches that did not surface a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Lemma 1 and its discussion of extension beyond n = 21; the cited older upper-bound surface when n ≡ 2 (mod 3); Wesley 2026 as a recent lower-bound status check; and bounded 2026-04-14 exact-term and recent-status searches.
- artifacts/r-b24-b26-two-off-book-ramsey/record.md
- artifacts/r-b24-b26-two-off-book-ramsey/status.json
