# Working Packet: The Parameter Set (28,3,3,-1) for Balancedly Splittable Hadamard Matrices

- slug: `bshm-28-3-3-neg1`
- title: bshm-28-3-3-neg1
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `78`
- single-solve-to-paper fraction: `0.77`

## statement
Determine whether an order-28 Hadamard matrix exists that is balancedly splittable with parameters (28,3,3,-1).

## novelty_notes
- frontier basis: Table 6 lists (28,3,3,-1) as an unresolved Type 1 parameter left open after Result 8(vi), Corollary 70, and Proposition 72.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The paper skeleton is already available from the source: state the Type 1 family, explain the known odd-r restrictions, and settle this exact tuple by construction or obstruction. Beyond the solve, only a short placement relative to Table 6 is needed.
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
- assessment: Lane-eligible. The note would be short and concrete, though the title theorem is a little less naturally branded than the regime-first 72-case.

## likely_paper_shape
- note title: The Parameter Set (28,3,3,-1) for Balancedly Splittable Hadamard Matrices
- hypothetical title: A Balancedly Splittable Hadamard Matrix with Parameters (28,3,3,-1)
- paper shape: A short note settling a very small unresolved Type 1 BSHM parameter.
- publication if solved: A construction or obstruction for BSHM(28,3,3,-1) would plausibly be publishable as a short note resolving one of the smallest remaining exact parameters in the Type 1 BSHM family.
- minimal artifact requirements: Either an explicit order-28 Hadamard matrix with a certified 3-row balanced split yielding inner products 3 and -1, or a concise impossibility proof.

## hypothetical_abstract
We determine the existence status of a balancedly splittable Hadamard matrix with parameters (28,3,3,-1). Jedwab, Li, and Simon reduced the Type 1 family BSHM(4rs,4s-1,4s-1,-1) to explicit existence, nonexistence, and a short residual table, in which (28,3,3,-1) appears among the smallest unresolved tuples. Resolving this parameter yields a compact note because the surrounding structural theory and residual classification are already in place.

## single_solve_explanation
This exact tuple is already close to paper-shaped because the source leaves only a short residual table and the parameter is tiny. Once the witness or obstruction is found, the remaining write-up is largely a short recap of the Type 1 classification and a presentation of the certificate. That makes the solve itself most of the eventual paper.

## broader_theorem_nonimplication
For odd r, Proposition 72 only rules out r < 4s - 1 and Result 8(vi) covers the boundary case r = 4s - 1 under a skew-type Hadamard hypothesis. The parameter (28,3,3,-1) has r = 7 and s = 1, so it lies beyond the proven nonexistence range and is not settled by the boundary construction.

## literature_gap
Current checked source literature leaves BSHM(28,3,3,-1) unresolved in Table 6 after applying Result 8(vi), Corollary 70, and Proposition 72.

## transfer_kit
- lemma: Proposition 68 gives the repeated-block structure H1 = 1^T tensor L for Type 1 BSHM(4rs,4s-1,4s-1,-1).
- lemma: Proposition 72 proves that when r is odd, one must have r >= 4s - 1 and obtain a sum-of-odd-squares constraint.
- lemma: Result 8(vi) gives the boundary construction at r = 4s - 1 from skew-type Hadamard matrices.
- lemma: Table 6 records (28,3,3,-1) as one of the remaining unresolved tuples.
- toy example: The nearest positive benchmark is BSHM(12,3,3,-1), arising from the boundary case r = 4s - 1 with s = 1.
- known obstruction: Proposition 72 rules out all odd-r cases with r < 4s - 1, so any argument for order 28 must work strictly beyond the known nonexistence threshold.
- prior-work stop sentence: The current source narrows the Type 1 family to a short residual table and leaves BSHM(28,3,3,-1) open there.
- recommended first attack: Exploit the repeated-block form from Proposition 68 together with the odd-square constraint in Proposition 72 to force a tiny-order obstruction or a very explicit order-28 construction.
- paper if solved: If solved exactly, the paper would be a short note resolving a very small residual parameter in the Type 1 balancedly splittable Hadamard-matrix family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 72, Table 6 on p. 36, and Corollary 74 on p. 37: the paper classifies the Type 1 family BSHM(4rs,4s-1,4s-1,-1) up to a short list of open cases and records (28,3,3,-1) as the next smallest unresolved entry after (20,3,3,-1).
- Jedwab-Li-Simon (2023), especially Proposition 68, Proposition 72, Table 6, and Corollary 74.
- artifacts/bshm-28-3-3-neg1/record.md
- artifacts/bshm-28-3-3-neg1/status.json
