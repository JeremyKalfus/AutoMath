# Working Packet: The Parameter Set (36,3,3,-1) for Balancedly Splittable Hadamard Matrices

- slug: `bshm-36-3-3-neg1`
- title: bshm-36-3-3-neg1
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `49`
- single-solve-to-paper fraction: `0.58`

## statement
Determine whether an order-36 Hadamard matrix exists that is balancedly splittable with parameters (36,3,3,-1).

## novelty_notes
- frontier basis: Table 6 lists (36,3,3,-1) among the remaining odd-r, s = 1 cases left open by the source's structural restrictions.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The canonical source still supplies a short residual-table narrative, but the recent broader-order status signal means a clean packet now requires reconciling that ambient claim before the exact tuple can honestly serve as the title theorem.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: weak
- family anchor strength: moderate
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: low
- isolated exact-case risk: high
- broader-theorem implication risk: unresolved
- theorem-slice stability: unclear
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Not lane-eligible under the present audit. The exact tuple is still structurally interesting, but the theorem slice is not stable enough for a clean one-shot micro-paper target until the broader order-36 status signal is reconciled.

## likely_paper_shape
- note title: The Parameter Set (36,3,3,-1) for Balancedly Splittable Hadamard Matrices
- hypothetical title: The Parameter Set (36,3,3,-1) in the Type 1 BSHM Family
- paper shape: A short note settling a small unresolved Type 1 BSHM parameter.
- publication if solved: A construction or obstruction for BSHM(36,3,3,-1) could still matter, but the bounded curation audit did not certify a clean micro-paper packet because a recent broader-order status signal may already force the order-36 case.
- minimal artifact requirements: Either an explicit order-36 Hadamard matrix with a certified 3-row balanced split yielding inner products 3 and -1, or a concise impossibility proof.

## hypothetical_abstract
We determine the existence status of a balancedly splittable Hadamard matrix with parameters (36,3,3,-1). The 2023 structural classification of Type 1 balanced splittable Hadamard matrices leaves this tuple in a short residual table after the generic existence and nonexistence arguments are exhausted. Resolving the order-36 case yields a compact stand-alone note because the surrounding framework and motivation are already in place.

## single_solve_explanation
The canonical source alone would make this tuple look close to paper-shaped, but the recent seminar claim about general order-36 nonexistence means one exact solve may collapse into a broader ambient observation. That uncertainty pushes substantial publication work back into novelty and scope reconciliation, so the solve no longer accounts for the target 70-90% of the note.

## broader_theorem_nonimplication
The 2023 canonical source does not settle (36,3,3,-1), but a January 24, 2024 seminar slide by Hadi Kharaghani states that no balancedly splittable Hadamard matrix of order 36 exists as part of a broader order-4n^2 claim for odd n. Under the bounded curation audit, that broader-status signal was enough to make nonimplication unresolved.

## literature_gap
The canonical 2023 source leaves BSHM(36,3,3,-1) open in Table 6, but the bounded recent-status audit no longer supports a clean exact literature gap because of the 2024 broader-order nonexistence claim.

## transfer_kit
- lemma: Proposition 68 gives the repeated-block structure for Type 1 BSHM(4rs,4s-1,4s-1,-1).
- lemma: Proposition 72 yields the odd-r lower bound r >= 4s - 1 and the sum-of-odd-squares obstruction.
- lemma: Result 8(vi) constructs the boundary case r = 4s - 1 under a skew-type Hadamard condition.
- lemma: Table 6 lists (36,3,3,-1) as unresolved.
- toy example: The nearest solved boundary benchmark is again BSHM(12,3,3,-1), obtained from Result 8(vi) with s = 1.
- known obstruction: A January 24, 2024 seminar slide claims a broader nonexistence statement for balancedly splittable Hadamard matrices of order 36, so any order-36 packet must first reconcile whether the exact tuple is already subsumed.
- prior-work stop sentence: The 2023 canonical source leaves BSHM(36,3,3,-1) open in Table 6, but the bounded recent-status audit surfaced a later broader-order nonexistence claim that was not fully resolved within curation.
- recommended first attack: Before any tuple-specific proof attempt, verify whether the reported broader order-36 nonexistence statement is published and exact enough to settle this case; only then decide whether a family-specific obstruction note still survives.
- paper if solved: If the broader-order status check clears and the exact tuple still remains open, the paper would revert to a short note on a small unresolved Type 1 balancedly splittable Hadamard parameter.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 72, Table 6 on p. 36, and Corollary 74 on p. 37: the paper leaves (36,3,3,-1) as the next unresolved odd-r, s = 1 Type 1 parameter after (28,3,3,-1).
- Jedwab-Li-Simon (2023), especially Proposition 68, Proposition 72, Table 6, and Corollary 74.
- artifacts/bshm-36-3-3-neg1/record.md
- artifacts/bshm-36-3-3-neg1/status.json
