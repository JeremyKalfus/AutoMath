# Working Packet: The Cyclic (2574,249,24) Difference-Set Case

- slug: `cyclic-difference-set-2574-249-24`
- title: cyclic-difference-set-2574-249-24
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `77`
- single-solve-to-paper fraction: `0.75`

## statement
Determine whether the cyclic group C_2574 admits a (2574,249,24)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon Table 2 isolates (2574,249,24) as one of the remaining cyclic rows.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The theorem statement is already paper-shaped; the missing piece is only a stronger outside-source status confirmation.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Backup only. The theorem slice is attractive, but the capped novelty audit is too thin for the live lane.

## likely_paper_shape
- note title: The Cyclic (2574,249,24) Difference-Set Case
- hypothetical title: On the cyclic (2574,249,24) difference-set case
- paper shape: A short cyclic residual-case note with one exact Table 2 theorem.
- publication if solved: Settling the cyclic (2574,249,24) row would plausibly support a short residual-case note if the exact tuple is still frontier-open.
- minimal artifact requirements: A proof or disproof for C_2574, the decisive contracted-multiplier contradiction or construction, and a refreshed later-status note.

## hypothetical_abstract
We determine whether the cyclic group C_2574 admits a (2574,249,24)-difference set. Baumert and Gordon list this exact row in Table 2 among the residual cyclic cases with 150 <= k <= 300 and gcd(v,n) > 1. A direct solution would plausibly support a short note, but the present capped curation run did not obtain a sufficiently robust later-status audit for the tuple.

## single_solve_explanation
The source already isolates the exact row, so one clean solve would carry most of the mathematical payload of a short paper. Only a brief introduction, the polished main proof, and a concise status paragraph would remain after the solve. The current blocker is the thinness of the later-literature check, not the paper shape.

## broader_theorem_nonimplication
Baumert-Gordon already exhaust their standard necessary conditions before leaving (2574,249,24) in Table 2, so the row is not implied by the source itself. The bounded web audit did not surface a clean independent later-source status check.

## literature_gap
Baumert-Gordon stop at listing (2574,249,24) as a remaining possible cyclic case in Table 2; the capped 2026-04-16 audit left the later exact-tuple status unclear.

## transfer_kit
- lemma: Baumert-Gordon Table 2 isolates (2574,249,24) as an exact remaining cyclic row.
- lemma: Section 2 records the necessary conditions already used before the row reaches Table 2.
- lemma: Theorem 3.1 gives contracted coefficient equations for divisors of 2574.
- lemma: Theorem 3.2 gives multiplier-orbit equalities once a prime-power divisor of n = 225 yields a contracted multiplier.
- toy example: Contract a hypothetical 249-set modulo 11 or 13 and compare the coefficient vector with the orbit sizes forced by powers of 5 from n = 225.
- known obstruction: Any surviving configuration must satisfy rigid contracted equations simultaneously across the 2 * 3^2 * 11 * 13 factorization of v.
- prior-work stop sentence: Baumert and Gordon stop at listing (2574,249,24) as a remaining possible cyclic case in Table 2.
- recommended first attack: Choose a divisor of 2574 where the 5-part of n induces a useful multiplier and combine the resulting orbit structure with Theorem 3.1.
- paper if solved: If solved exactly, the paper would be a short note closing the cyclic Table 2 row (2574,249,24).

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 2 listing the exact cyclic row (2574,249,24) among the possible cases with 150 <= k <= 300 and gcd(v,n) > 1.
- Baumert-Gordon 2004 Table 2, bounded exact/alternate web probes on 2026-04-16, Gordon's current publication/database pages, and local attempt/search/paper/failed memory.
- artifacts/cyclic-difference-set-2574-249-24/record.md
- artifacts/cyclic-difference-set-2574-249-24/status.json
