# Working Packet: The Three-Color Ramsey Number of C9

- slug: `r3-c9-triple-cycle`
- title: Determine the exact value of R(C9, C9, C9)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `73`
- single-solve-to-paper fraction: `0.72`

## statement
Determine the least N such that every 3-coloring of the edges of K_N contains a monochromatic 9-cycle.

## novelty_notes
- frontier basis: The 2026 survey identifies R(C9, C9, C9) as the first open odd-cycle case under the Bondy-Erdős 4n-3 conjecture and records the lower bound 33.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the exact value 33 is proved, the note would have an excellent family narrative. But the current literature packet is looser than for the even-cycle C10 case, so some additional context-building might still be needed.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: moderate
- assessment: Not lane-eligible on the current packet. The paper story is good, but the source-backed corridor is still looser than desired for one-shot publication mode.

## likely_paper_shape
- note title: The Three-Color Ramsey Number of C9
- hypothetical title: The Three-Color Ramsey Number of C9
- paper shape: A first-open-case odd-cycle exact note if the classical 4n-3 prediction can be sealed at n = 9.
- publication if solved: An exact determination of R(C9, C9, C9) would plausibly support a short note on the first unresolved odd-cycle case in the diagonal three-color cycle program.
- minimal artifact requirements: Either a proof that every 3-coloring of K33 contains a monochromatic C9, or a 32-vertex coloring avoiding monochromatic C9.

## hypothetical_abstract
We determine the three-color Ramsey number R(C9, C9, C9). The current checked survey places C9 as the first unresolved odd-cycle case in the Bondy-Erdős diagonal conjecture and records the lower bound 33. An exact closure would therefore create a short note with a clear conjectural and historical anchor.

## single_solve_explanation
A successful exact solve would supply the title theorem and most of the paper's motivation. However, the currently checked packet is not as tight as for C10, so the solve would still need some extra positioning and perhaps a stronger upper-bound narrative. That keeps it just outside the strict lane.

## broader_theorem_nonimplication
The checked sources describe large-n odd-cycle results and a standing 4n-3 conjecture, but they still explicitly name C9 as the first unresolved case. So no broader published theorem currently settles the exact value.

## literature_gap
Current checked sources identify R(C9, C9, C9) as the first open odd-cycle case and record the lower bound 33, but no exact closure surfaced in the bounded audit.

## transfer_kit
- lemma: Radziszowski's 2026 survey records the Bondy-Erdős conjecture R(C_n, C_n, C_n) = 4n - 3 for odd n >= 5.
- lemma: The same survey identifies R(C9, C9, C9) as the first open odd-cycle case.
- lemma: The same table records the exact solved benchmark R(C7, C7, C7) = 25.
- lemma: The survey cites later large-n odd-cycle results showing that the ambient family is already well developed.
- toy example: The exact neighboring benchmark R(C7, C7, C7) = 25 is already recorded in the checked survey.
- known obstruction: The current packet exposes a natural conjectural value 33 but not a comparably sharp checked upper-bound corridor, so an exact solve likely needs more than a quick local adaptation.
- prior-work stop sentence: Current checked sources still leave R(C9, C9, C9) as the first open odd-cycle case, with lower bound 33.
- recommended first attack: Try to prove the conjectured threshold 33 by pushing odd-cycle forcing from the exact C7 case and the large-n odd-cycle templates into the first unresolved small instance.
- paper if solved: If solved exactly, the paper would be a short note closing the first unresolved odd-cycle case in the diagonal three-color cycle program.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics Dynamic Survey DS1 revision 18, 2026), Section 6.3.1(c), citing the Bondy-Erdős odd-cycle conjecture R(C_n, C_n, C_n) = 4n - 3 for odd n >= 5, the exact small table through C7, and later large-n odd-cycle progress; bounded 2026 exact-statement, alternate-notation, and recent-status searches in this run did not surface a later exact closure of R(C9, C9, C9).
- Radziszowski 2026 survey Section 6.3.1(c), the Bondy-Erdős conjectural 4n-3 formula, the exact small-cycle table through C7, large-n odd-cycle references cited there, and bounded 2026 status searches run here.
- artifacts/r3-c9-triple-cycle/record.md
- artifacts/r3-c9-triple-cycle/status.json
