# Working Packet: The Cyclic (5859,203,7) Difference-Set Case

- slug: `cyclic-difference-set-5859-203-7`
- title: cyclic-difference-set-5859-203-7
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `78`
- single-solve-to-paper fraction: `0.76`

## statement
Determine whether the cyclic group C_5859 admits a (5859,203,7)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon Table 2 isolates (5859,203,7) as an exact remaining cyclic row after the source's eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If still open, one decisive solve would mostly be the paper; the blocker is only the underpowered later-status audit under the search cap.
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
- assessment: Strong backup only. The paper shape is real, but the later-status audit is too thin to mark the packet live.

## likely_paper_shape
- note title: The Cyclic (5859,203,7) Difference-Set Case
- hypothetical title: On the cyclic (5859,203,7) difference-set case
- paper shape: A short residual-case note centered on one exact cyclic Table 2 survivor.
- publication if solved: Settling the cyclic (5859,203,7) row would look like a short residual-case note if the row is still genuinely open.
- minimal artifact requirements: A proof or disproof for C_5859, the decisive contracted-multiplier argument, and a stronger later-status audit before solve.

## hypothetical_abstract
We determine whether the cyclic group C_5859 admits a (5859,203,7)-difference set. Baumert and Gordon list this exact parameter row in Table 2 among the remaining cyclic cases with 150 <= k <= 300 and gcd(v,n) > 1. A direct solution would plausibly support a short note, but the present capped curation run did not obtain a sufficiently independent later-status check to clear solve.

## single_solve_explanation
The canonical paper already isolates this tuple as a named residual row, so a single proof or disproof would provide the theorem statement and nearly all of the note's mathematics. What remains after the solve is mostly expository cleanup and a compact status paragraph. The problem is not paper-weak; the present issue is only that the bounded novelty audit stayed too source-adjacent.

## broader_theorem_nonimplication
Baumert-Gordon explicitly leave (5859,203,7) in Table 2, so the exact row is not already handled by the source's standard toolkit. The capped audit, however, did not obtain a satisfying independent later-source confirmation that the row remains unsettled.

## literature_gap
Baumert-Gordon stop at listing (5859,203,7) as a remaining possible cyclic case in Table 2; this capped run did not complete a robust outside-source recheck.

## transfer_kit
- lemma: Baumert-Gordon Table 2 isolates (5859,203,7) as an exact remaining cyclic row.
- lemma: Section 2 records the necessary conditions already spent before the row survives to Table 2.
- lemma: Theorem 3.1 gives contracted coefficient equations for every divisor of 5859.
- lemma: Theorem 3.2 converts suitable prime-power factors of n into contracted multiplier constraints.
- toy example: Contract a hypothetical 203-set modulo 31 or 63 and compare the coefficient vector with the orbit sizes forced by the 2-power part of n = 196.
- known obstruction: Any surviving configuration must reconcile a sparse lambda = 7 difference pattern with strong contracted-multiplier restrictions across 3^3 * 7 * 31.
- prior-work stop sentence: Baumert and Gordon stop at listing (5859,203,7) as a remaining possible cyclic case in Table 2.
- recommended first attack: Work modulo a divisor where 2 induces a useful contracted multiplier and force the orbit counts into the Theorem 3.1 coefficient equalities.
- paper if solved: If solved exactly, the paper would be a short note closing the cyclic Table 2 row (5859,203,7).

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 2 listing the exact cyclic row (5859,203,7) among the possible cases with 150 <= k <= 300 and gcd(v,n) > 1.
- Baumert-Gordon 2004 Table 2, bounded exact/alternate tuple web probes on 2026-04-16, Gordon's publications/database surfaces, and local attempt/search/paper/failed memory.
- artifacts/cyclic-difference-set-5859-203-7/record.md
- artifacts/cyclic-difference-set-5859-203-7/status.json
