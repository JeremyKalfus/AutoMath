# Working Packet: The Parameter Set (44,3,3,-1) for Balancedly Splittable Hadamard Matrices

- slug: `bshm-44-3-3-neg1`
- title: bshm-44-3-3-neg1
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `72`
- single-solve-to-paper fraction: `0.73`

## statement
Determine whether an order-44 Hadamard matrix exists that is balancedly splittable with parameters (44,3,3,-1).

## novelty_notes
- frontier basis: Table 6 lists (44,3,3,-1) as one of the unresolved residual Type 1 parameters after the source's generic restrictions are applied.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The paper packet is compact: set the Type 1 family context, note the residual Table 6 status, and present the exact witness or obstruction. Very little feeder work remains once the answer is known.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible but weaker than the first three queue entries because its note framing is more residual-table than regime-first.

## likely_paper_shape
- note title: The Parameter Set (44,3,3,-1) for Balancedly Splittable Hadamard Matrices
- hypothetical title: Balancedly Splittable Hadamard Matrices at (44,3,3,-1)
- paper shape: A short note settling an unresolved Type 1 BSHM parameter in the odd-r, s = 1 branch.
- publication if solved: A construction or obstruction for BSHM(44,3,3,-1) would plausibly be publishable as a short note on an unresolved Type 1 BSHM parameter.
- minimal artifact requirements: Either an explicit order-44 Hadamard matrix with a certified 3-row balanced split yielding inner products 3 and -1, or a concise impossibility proof.

## hypothetical_abstract
We determine the existence status of a balancedly splittable Hadamard matrix with parameters (44,3,3,-1). In the 2023 classification of the Type 1 family BSHM(4rs,4s-1,4s-1,-1), this tuple remains in the short residual table left open after the general existence and nonexistence results. Settling it yields a concise note because the only substantial missing ingredient is the exact certificate for the order-44 case.

## single_solve_explanation
The order-44 question is already close to a finished note: the source contributes the family story and the residual open table. Once the exact answer is proved, the remaining work is largely presentational. That places the single solve in the target 70-90% publication range.

## broader_theorem_nonimplication
The published odd-r theory only rules out cases with r < 4s - 1 and handles the boundary construction r = 4s - 1. The tuple (44,3,3,-1) corresponds to r = 11 and s = 1, so it remains beyond the proved range and is explicitly left open.

## literature_gap
Current checked source literature leaves BSHM(44,3,3,-1) unresolved in Table 6 of the Type 1 family.

## transfer_kit
- lemma: Proposition 68 gives the repeated-block Type 1 structure.
- lemma: Proposition 72 imposes the odd-r lower bound and the sum-of-odd-squares condition.
- lemma: Result 8(vi) covers the boundary construction at r = 4s - 1.
- lemma: Table 6 lists (44,3,3,-1) as open.
- toy example: A nearby positive benchmark is BSHM(12,3,3,-1) from the boundary construction with s = 1.
- known obstruction: The source proves that odd-r cases below the threshold r = 4s - 1 cannot occur, so the open order-44 tuple lies in a narrow residual window rather than a diffuse unknown region.
- prior-work stop sentence: The current source narrows the Type 1 family to a short residual table and leaves BSHM(44,3,3,-1) among its open entries.
- recommended first attack: Run the Proposition 68 block repetition and Proposition 72 arithmetic obstruction directly at order 44, where the remaining configuration space should still be human-readable.
- paper if solved: If solved exactly, the paper would be a short note on a residual open parameter in the Type 1 balancedly splittable Hadamard-matrix family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 72, Table 6 on p. 36, and Corollary 74 on p. 37: the paper leaves (44,3,3,-1) open in the odd-r, s = 1 branch of the Type 1 family.
- Jedwab-Li-Simon (2023), especially Proposition 68, Proposition 72, Table 6, and Corollary 74.
- artifacts/bshm-44-3-3-neg1/record.md
- artifacts/bshm-44-3-3-neg1/status.json
