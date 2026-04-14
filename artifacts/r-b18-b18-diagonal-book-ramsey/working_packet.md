# Working Packet: The Exact Value of R(B18, B18)

- slug: `r-b18-b18-diagonal-book-ramsey`
- title: Determine the exact value of R(B18, B18)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `67`
- single-solve-to-paper fraction: `0.68`

## statement
Determine the least n such that every red-blue coloring of K_n contains a monochromatic book B18.

## novelty_notes
- frontier basis: Current public sources leave the diagonal book Ramsey number at 73 <= R(B18, B18) <= 74. The frontier is still one step wide, but the resulting packet is less clearly in the 70-90% finished-paper zone than the higher-ranked diagonal cases.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the endpoint 73 versus 74 is settled, the note would still have a clean title theorem and literature slot. The conservative downgrade is that the proof artifact is more likely to be bulky enough that the solve alone no longer guarantees a nearly complete paper packet.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Borderline fail for the strict lane. The statement is still legitimate and likely open, but the solve-to-publication distance is no longer comfortably inside the required 70-90% paper zone.

## likely_paper_shape
- note title: The Exact Value of R(B18, B18)
- hypothetical title: The Exact Value of R(B18, B18)
- paper shape: A one-theorem exact-value note for a larger diagonal book Ramsey number, but with a weaker near-paper margin than the four higher-ranked slots.
- publication if solved: An exact determination of R(B18, B18) could still support a short note, but the solve no longer looks as close to a nearly finished paper packet as the stronger queue slots above.
- minimal artifact requirements: Either an explicit 73-vertex coloring avoiding monochromatic B18 or a compact proof that every 74-vertex coloring forces B18.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B18, B18). Previous work placed this number in the interval 73 <= R(B18, B18) <= 74. Our result closes the remaining one-step gap for a larger diagonal book pair.

## single_solve_explanation
This statement still has the right family anchor and a clean exact gap, so a successful solve could plausibly support a short note. The problem is not novelty or theorem-slice drift; it is that the proof packet may be large enough that the solve itself no longer supplies the desired 70-90% of the paper without additional compression or secondary cleanup. That pushes it just outside the strict micro-paper lane.

## broader_theorem_nonimplication
Known diagonal-book theorems still stop at the generic interval 4n + 1 <= R(B_n, B_n) <= 4n + 2, so no broader published theorem currently settles n = 18. The conservative concern is closability, not hidden implication by a stronger ambient theorem.

## literature_gap
Current public sources stop at 73 <= R(B18, B18) <= 74.

## transfer_kit
- lemma: Lidicky-McKinley-Pfender-Van Overberghe (2025), Lemma 1, gives 73 <= R(B18, B18) <= 74.
- lemma: The same lemma gives the exact neighboring almost-diagonal value R(B17, B18) = 71.
- lemma: Wesley (2026) confirms continuing lower-bound progress in the book family without reporting an exact closure for B18.
- lemma: The same 2025 paper records exact smaller diagonal benchmarks such as R(B8, B8) = 33.
- toy example: The exact neighboring almost-diagonal case R(B17, B18) = 71 is the nearest solved benchmark for the intended theorem shape.
- known obstruction: By this size, structured near-extremal constructions may generate a larger proof residue, so the main risk is not theorem drift but a certificate that is too bulky for a clean micro-paper packet.
- prior-work stop sentence: Current sources stop at 73 <= R(B18, B18) <= 74.
- recommended first attack: Use the exact almost-diagonal case R(B17, B18) = 71 as the local forcing template and test whether any 73-vertex near-extremal construction can survive a one-vertex extension without creating too many common neighbors on a spine edge.
- paper if solved: The paper would be a short exact-value note only if the decisive proof artifact stays compact enough to avoid a second clean-up campaign.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey numbers for books, wheels, and generalizations" (Electronic Journal of Combinatorics 32(4) (2025)), Lemma 1 giving 73 <= R(B18, B18) <= 74; together with William J. Wesley, "Lower bounds for book Ramsey numbers" (Discrete Mathematics 349(5) (2026)), used as a bounded recent-status and citation check that did not report an exact closure for B18; and bounded 2026-04-14 exact-statement and alternate-notation web checks that did not reveal a relevant later exact determination.
- 2025 EJC Lemma 1 for the one-step interval and family context, 2026 Wesley paper as a recent-status check, and bounded 2026-04-14 exact-statement, synonym, and status searches.
- artifacts/r-b18-b18-diagonal-book-ramsey/record.md
- artifacts/r-b18-b18-diagonal-book-ramsey/status.json
