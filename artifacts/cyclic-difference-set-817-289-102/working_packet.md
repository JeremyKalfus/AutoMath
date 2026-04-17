# Working Packet: The Cyclic (817,289,102) Difference-Set Case

- slug: `cyclic-difference-set-817-289-102`
- title: cyclic-difference-set-817-289-102
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `73`
- single-solve-to-paper fraction: `0.72`

## statement
Determine whether the cyclic group C_817 admits a (817,289,102)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon Table 3 isolates (817,289,102) as an exact remaining cyclic row with gcd(v,n) = 1.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If genuinely open, one exact solve would still be most of the note, but the present audit did not reduce the later-status ambiguity enough.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: unresolved
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Interesting but not lane-eligible under the cap. The theorem slice is exact, yet the broader-status audit is too unclear.

## likely_paper_shape
- note title: The Cyclic (817,289,102) Difference-Set Case
- hypothetical title: On the cyclic (817,289,102) difference-set case
- paper shape: A short residual-case note if the exact Table 3 row remains frontier-open.
- publication if solved: If still genuinely open, the cyclic (817,289,102) row could support a short residual-case note.
- minimal artifact requirements: A proof or disproof for C_817, the decisive multiplier-orbit or contraction argument, and a stronger later-source status check before solve.

## hypothetical_abstract
We determine whether the cyclic group C_817 admits a (817,289,102)-difference set. Baumert and Gordon list this exact parameter row in Table 3 among the residual cyclic cases with 150 <= k <= 300 and gcd(v,n) = 1. A direct solution could still support a short note, but the present capped curation run left the later-status and broader-implication picture too unclear for a live green light.

## single_solve_explanation
The source already isolates one exact theorem candidate, so a clean solve would still provide most of the mathematical content for a short note. What remains after the solve would be a compact introduction and some framing. The current problem is that the bounded audit did not settle whether later multiplier results already subsume this row.

## broader_theorem_nonimplication
Baumert-Gordon leave (817,289,102) as a surviving Table 3 row, so the source itself does not settle it. The capped audit did not surface a clean later theorem one way or the other, so implication risk remains unresolved.

## literature_gap
Baumert-Gordon stop at listing (817,289,102) as a remaining possible cyclic case in Table 3; the capped 2026-04-16 audit did not resolve the later-status question.

## transfer_kit
- lemma: Baumert-Gordon Table 3 isolates (817,289,102) as an exact remaining cyclic row.
- lemma: Section 2 records the standard arithmetic filters already exhausted before the row reaches Table 3.
- lemma: Theorem 3.1 gives contracted coefficient equations for every divisor of 817.
- lemma: Theorem 3.2 gives multiplier-orbit equalities once a prime divisor of n = 187 acts as a contracted multiplier.
- toy example: Work modulo 19 or 43 and compare the resulting coefficient vector with orbit sizes forced by 11 or 17 acting on the quotient.
- known obstruction: Any surviving configuration must reconcile two independent multiplier sources from n = 11 * 17 with the sparse divisor structure 19 * 43 of v.
- prior-work stop sentence: Baumert and Gordon stop at listing (817,289,102) as a remaining possible cyclic case in Table 3.
- recommended first attack: Exploit the prime divisors 11 and 17 of n to force orbit decompositions modulo 19 or 43, then test them against Theorem 3.1.
- paper if solved: If solved exactly, the paper would be a short note closing the cyclic Table 3 row (817,289,102).

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the exact cyclic row (817,289,102) among the possible cases with 150 <= k <= 300 and gcd(v,n) = 1.
- Baumert-Gordon 2004 Table 3, bounded exact/alternate tuple web probes on 2026-04-16, the Gordon-Schmidt survey surface, and local attempt/search/paper/failed memory.
- artifacts/cyclic-difference-set-817-289-102/record.md
- artifacts/cyclic-difference-set-817-289-102/status.json
