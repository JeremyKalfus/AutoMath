# Working Packet: The Exact Value of R(B21, B21)

- slug: `r-b21-b21-book-ramsey`
- title: Determine the exact value of R(B21, B21)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `44`
- single-solve-to-paper fraction: `0.56`

## statement
Determine the least n such that every graph on n vertices contains a copy of B21 or its complement contains a copy of B21.

## novelty_notes
- frontier basis: Current checked public sources support only 85 <= R(B21, B21) <= 86.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved, the result would still head a real note in the diagonal book family. It misses the lane because the larger extremal object makes a compact single-pass packet unlikely and raises the chance of long certificate management after the core solve.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: low
- exact gap from source: tiny
- assessment: Not lane-eligible. The family anchor is legitimate, but the likely certificate is too large and the solve-to-paper fraction is too low for strict one-shot publication mode.

## likely_paper_shape
- note title: The Exact Value of R(B21, B21)
- hypothetical title: The Exact Value of R(B21, B21)
- paper shape: A diagonal book Ramsey exact-value note whose certificate is likely too large for the strict lane.
- publication if solved: An exact closure of R(B21, B21) would still be paper-shaped, but it is too large and technically exposed for the strict micro-paper lane.
- minimal artifact requirements: A compact 85-vertex witness or a forcing proof at 85 vertices, plus enough verification detail to keep the certificate human-readable.

## hypothetical_abstract
We determine the diagonal book Ramsey number R(B21, B21). Current checked literature leaves the case in the interval 85 <= R(B21, B21) <= 86, while the available prime-power exactness theorem does not apply to n = 21. Our result closes a remaining finite diagonal case outside the presently settled infinite family.

## single_solve_explanation
A solve would still produce a clear title theorem in a named family, so the problem is genuinely paper-shaped. The note would mostly need the critical certificate and a brief comparison with solved diagonal cases. It fails the strict micro-paper lane because the certificate size and proof-management risk are too high relative to the smallest one-gap targets.

## broader_theorem_nonimplication
The checked infinite exact family covers prime-power values of 4n + 1, and 85 is not one of them. The checked 2025 theorem gives only the one-gap corridor 85-86 and no broader statement in the audited sources collapses the exact value.

## literature_gap
Publicly checked sources stop at 85 <= R(B21, B21) <= 86.

## transfer_kit
- lemma: Theorem 1 of the 2025 source gives 85 <= R(B21, B21) <= 86.
- lemma: The 2022 source explains the prime-power exactness mechanism for diagonal book numbers and therefore clarifies why n = 21 remains outside the solved family.
- lemma: The checked diagonal-book literature supplies neighboring exact and one-gap cases for short comparison once an exact value is known.
- toy example: The prime-power diagonal case n = 18 gives a nearby solved benchmark R(B18, B18) = 74 in the checked family literature.
- known obstruction: At this size, even a one-gap residue may hide a large and less transparent extremal witness, which weakens certificate compactness.
- prior-work stop sentence: Current checked sources stop at the one-gap window 85 <= R(B21, B21) <= 86.
- recommended first attack: Treat the case as a structured diagonal extremal-graph problem first and test whether known prime-power constructions suggest a near-extremal 85-vertex template.
- paper if solved: The paper would be an exact-value note on a larger unresolved diagonal book Ramsey case.

## bounded_source_list
- Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Theorem 1, which gives 85 <= R(B21, B21) <= 86; and Shyam Narayanan and Tian Zhang, "Ramsey numbers of fans and large books" (Electronic Journal of Combinatorics 29(1), 2022), whose prime-power diagonal exactness result does not settle n = 21 because 4n + 1 = 85 is not a prime power; together with bounded exact-statement, alternate-notation, source-internal, outside-source, and recent-status web checks on 2026-04-14 that did not reveal a later exact closure.
- Lidicky-McKinley-Pfender-Van Overberghe 2025 Theorem 1, Narayanan-Zhang 2022 for the prime-power diagonal exactness mechanism, and bounded 2026-04-14 exact-term, alternate-notation, source-internal, outside-source, and recent-status web checks.
- artifacts/r-b21-b21-book-ramsey/record.md
- artifacts/r-b21-b21-book-ramsey/status.json
