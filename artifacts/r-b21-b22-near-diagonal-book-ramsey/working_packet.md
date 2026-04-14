# Working Packet: The Exact Value of R(B21, B22)

- slug: `r-b21-b22-near-diagonal-book-ramsey`
- title: Determine the exact value of R(B21, B22)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `54`
- single-solve-to-paper fraction: `0.59`

## statement
Determine the least N such that every graph on N vertices contains a red copy of B21 or its complement contains a blue copy of B22.

## novelty_notes
- frontier basis: The 2025 source proves the exact near-diagonal formula R(B_{n-1}, B_n) = 4n - 1 only up to n = 21 and explicitly raises extension beyond that range as open territory.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A sharp closure at the expected value 87 would be inherently paper-shaped. But the curation pass could not cheaply verify whether that exact pair is still frontier-open in the narrow theorem-level sense required for a micro-paper queue leader.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: unresolved
- theorem-slice stability: unclear
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: broad
- assessment: Not lane-eligible. The family is good, but the theorem slice is unstable, the gap from source is too broad, and a successful proof would likely want broader packaging before it becomes paper-ready.

## likely_paper_shape
- note title: The Exact Value of R(B21, B22)
- hypothetical title: The Exact Value of R(B21, B22)
- paper shape: A beyond-range extension note for the near-diagonal book formula, but only if the exact pair lands cleanly on the expected pattern value and the proof remains instance-shaped.
- publication if solved: If the 4n - 1 near-diagonal book pattern extends to n = 22, that exact closure could support a compact pattern-extension note.
- minimal artifact requirements: An 86-vertex Ramsey-(B21,B22) witness or a proof that every 87-vertex graph contains B21 or its complement contains B22.

## hypothetical_abstract
We determine the Ramsey number R(B21, B22). The 2025 small-book Ramsey paper proves the near-diagonal formula R(B_{n-1}, B_n) = 4n - 1 only through n = 21, leaving the next exact pair beyond that range unresolved in the bounded curation pass. A sharp closure would create a natural first extension point for that exact formula.

## single_solve_explanation
This target misses the micro-paper lane because the solve alone is unlikely to finish the narrative. The honest paper would need substantial argument that the pair is the right theorem slice and not merely the first corollary of a broader new near-diagonal extension. That broader-theorem drift risk is exactly why the lane fails here.

## broader_theorem_nonimplication
No checked source extends the exact near-diagonal book formula beyond n = 21, and the 2025 paper explicitly treats such extension as open. But that same setup makes broader-theorem implication risk unresolved rather than low.

## literature_gap
Checked sources prove R(B_{n-1}, B_n) = 4n - 1 only for 4 <= n <= 21 and do not certify the exact pair (21,22).

## transfer_kit
- lemma: EJC 2025 Theorem 1 proves R(B_{n-1}, B_n) = 4n - 1 for 4 <= n <= 21.
- lemma: Section 4.2.1 states that the construction pattern seemed plausibly extendable beyond the proved range, but became computationally expensive.
- lemma: The paper notes that Wesley's later work extends related lower bounds on an infinite subfamily, giving some transfer infrastructure but not this exact parameter.
- lemma: The 2026 lower-bound paper adds modern search-based construction techniques around books.
- toy example: The exact case R(B20, B21) = 83 from the 2025 theorem is the nearest concrete model below the target.
- known obstruction: The known constructions beyond the proved range are computationally heavy and do not isolate a clean symbolic pattern at this specific parameter.
- prior-work stop sentence: Current checked sources prove the near-diagonal exact formula only through n <= 21 and do not certify the pair (21,22).
- recommended first attack: Look first for an 86-vertex 2-polycirculant Ramsey-(B21,B22) witness matching the 4n - 1 pattern before investing in broader flag-algebra upper machinery.
- paper if solved: If solved sharply at 87, the paper would be a one-case extension note for the near-diagonal book Ramsey formula beyond the 2025 range.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), especially Theorem 1 proving R(B_{n-1}, B_n) = 4n - 1 for 4 <= n <= 21 and the open-question discussion in Section 4.2.1 about extending that pattern beyond the proved range; together with the 2026 paper "Lower bounds for book Ramsey numbers" for surrounding lower-bound infrastructure. The bounded 2026-04-14 curation pass did not find a later exact closure for (21,22), but it also did not find a cheap parameter-specific upper/lower corridor strong enough for the micro-paper lane.
- EJC 2025 Table 1, Theorem 1, and Section 4.2.1, together with the 2026 lower-bound paper on book Ramsey numbers.
- artifacts/r-b21-b22-near-diagonal-book-ramsey/record.md
- artifacts/r-b21-b22-near-diagonal-book-ramsey/status.json
