# Working Packet: The Exact Value of R(B22, B23)

- slug: `r-b22-b23-near-diagonal-book-ramsey`
- title: Determine the exact value of R(B22, B23)
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `52`
- single-solve-to-paper fraction: `0.58`

## statement
Determine the least N such that every graph on N vertices contains a red copy of B22 or its complement contains a blue copy of B23.

## novelty_notes
- frontier basis: The proved exact near-diagonal formula stops at n = 21, and the 2025 source itself treats extension further out as open.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved cleanly at the natural continuation value, the pair would be a respectable one-case extension note. But the curation pass could not reduce the theorem-shape risk enough to treat it as a live micro-paper candidate.
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
- assessment: Not lane-eligible. The family is respectable, but the theorem slice is unclear and the likely proof burden is too search-heavy for a one-shot micro-paper target.

## likely_paper_shape
- note title: The Exact Value of R(B22, B23)
- hypothetical title: The Exact Value of R(B22, B23)
- paper shape: Potentially a beyond-range formula-extension note, but only if the exact closure is sharp and the proof avoids collapsing into a wider near-diagonal theorem.
- publication if solved: A sharp closure could support a short note on extending the near-diagonal book formula one step beyond the 2025 range.
- minimal artifact requirements: A 90-vertex Ramsey-(B22,B23) witness or a proof that every 91-vertex graph contains B22 or its complement contains B23.

## hypothetical_abstract
We determine the Ramsey number R(B22, B23). The 2025 small-book Ramsey paper proves the exact near-diagonal formula only up to n = 21, leaving the next unchecked pair outside that theorem range unresolved in the present bounded curation pass. A sharp closure would be mathematically coherent but not yet close enough to paper-ready for the strict micro-paper lane.

## single_solve_explanation
This target fails the micro-paper lane because the solve would not obviously finish the story. The paper would likely need broader explanation, extra pattern analysis, and a careful novelty audit against any later extensions of the near-diagonal formula. That pushes it outside the one-shot publication objective.

## broader_theorem_nonimplication
No checked source extends the exact near-diagonal book formula to n = 23, but the 2025 paper's own extension discussion makes it plausible that any successful proof here might naturally generalize. That keeps broader-theorem implication risk unresolved.

## literature_gap
Checked sources prove the exact near-diagonal formula only through n <= 21 and do not certify the exact pair (22,23).

## transfer_kit
- lemma: EJC 2025 Theorem 1 proves R(B_{n-1}, B_n) = 4n - 1 for 4 <= n <= 21.
- lemma: Section 4.2.1 states there was no indication that the pattern stops immediately beyond the proved range, only that generation became expensive.
- lemma: The paper notes partial later progress on related lower-bound extensions, but not at this exact tuple.
- lemma: The 2026 lower-bound paper shows that high-symmetry and SAT-style constructions remain relevant tools in this family.
- toy example: The exact neighboring case R(B20, B21) = 83 is the nearest clean model below the target range.
- known obstruction: Beyond the 2025 range, the known search methods become expensive before yielding a clean symbolic construction pattern.
- prior-work stop sentence: Current checked sources stop the exact near-diagonal formula at n <= 21 and do not certify the pair (22,23).
- recommended first attack: Only revisit if the queue is empty; the natural first move is a high-symmetry witness search aimed at the continuation value 91.
- paper if solved: If solved sharply, the paper would be a short beyond-range extension note for the near-diagonal book Ramsey formula.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), especially Theorem 1 proving R(B_{n-1}, B_n) = 4n - 1 for 4 <= n <= 21 and the open-question discussion in Section 4.2.1; together with the 2026 paper "Lower bounds for book Ramsey numbers" for broader lower-bound infrastructure near the book family. The bounded 2026-04-14 curation pass did not surface a later exact closure for the exact pair (22,23), but also did not secure a cheap parameter-specific audit strong enough for the micro-paper lane.
- EJC 2025 Theorem 1 and Section 4.2.1, together with the surrounding 2026 lower-bound infrastructure for books.
- artifacts/r-b22-b23-near-diagonal-book-ramsey/record.md
- artifacts/r-b22-b23-near-diagonal-book-ramsey/status.json
