# Working Packet: The Parameter Set (88,7,7,-1) for Balanced Splittable Hadamard Matrices

- slug: `bshm-88-7-7-neg1`
- title: bshm-88-7-7-neg1
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `81`
- single-solve-to-paper fraction: `0.8`

## statement
Determine whether an order-88 Hadamard matrix exists that is balanced splittable with parameters (88,7,7,-1).

## novelty_notes
- frontier basis: Table 6 isolates (88,7,7,-1) as the next unresolved odd-r case with s = 2 after the order-72 case, while Proposition 72 and the boundary construction at r = 4s - 1 leave this exact tuple untouched.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the order-88 case is settled, the note is already nearly complete: recall the odd-r lower bound, explain the boundary benchmark at r = 7, and present the exact witness or obstruction. Very little remains beyond framing and verification.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. This is a stable exact slice with strong family anchoring, compact certification requirements, and a clear note shape centered on the next unresolved odd-r s = 2 case.

## likely_paper_shape
- note title: The Parameter Set (88,7,7,-1) for Balanced Splittable Hadamard Matrices
- hypothetical title: Balanced Splittable Hadamard Matrices with Parameters (88,7,7,-1)
- paper shape: A single-theorem design-theory note on the next unresolved odd-r, s = 2 Type 1 BSHM parameter.
- publication if solved: A construction or obstruction for BSHM(88,7,7,-1) would plausibly be publishable as a short note settling the next unresolved odd-r case with s = 2 in a named BSHM family.
- minimal artifact requirements: Either an explicit order-88 Hadamard matrix with a certified 7-row balanced split yielding inner products 7 and -1, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (88,7,7,-1). Jedwab, Li, and Simon reduced the Type 1 family BSHM(4rs,4s-1,4s-1,-1) to explicit existence, nonexistence, and a short residual table, in which (88,7,7,-1) is the next unresolved odd-r case with s = 2. Resolving this parameter yields a compact stand-alone note because the surrounding family theory and the neighboring boundary case are already in place.

## single_solve_explanation
The exact order-88 statement already reads like a title theorem because the source literature isolates it as a named residual case in a well-defined family. Once the existence or nonexistence proof is in hand, the rest of the note is short: cite Proposition 72, explain why r = 11 lies just beyond the solved boundary r = 7, and record the certificate. That keeps the single solve squarely in the target 70-90% range of the final paper.

## broader_theorem_nonimplication
For odd r, Proposition 72 only rules out r < 4s - 1 and Result 8(vi) covers the boundary r = 4s - 1 when a skew-type Hadamard matrix of order 4s exists. Here s = 2 and r = 11, so the exact case lies beyond the proved nonexistence range and beyond the boundary construction, and Table 6 explicitly leaves it open.

## literature_gap
Current checked source literature leaves BSHM(88,7,7,-1) unresolved as the next odd-r, s = 2 entry in Table 6 of the Type 1 family.

## transfer_kit
- lemma: Proposition 69 relates BSHM(4rs,4s,4s,0) to BSHM(4rs,4s-1,4s-1,-1) when the all-ones row is present.
- lemma: Corollary 70 supplies existence results for BSHM(4rs,4s-1,4s-1,-1) from Hadamard matrices of orders r and 4s or of orders 2r and 2s.
- lemma: Proposition 72 proves that odd-r cases satisfy r >= 4s - 1 by the sum-of-odd-squares argument on the complementary block.
- lemma: Table 6 lists (88,7,7,-1) as open after the previous constructions and restrictions are applied.
- toy example: The boundary benchmark BSHM(56,7,7,-1) is supplied by Result 8(vi) because r = 4s - 1 = 7 and a skew-type Hadamard matrix of order 8 exists.
- known obstruction: Odd-r cases below the boundary r = 4s - 1 are ruled out by Proposition 72, so any order-88 proof must exploit structure beyond the boundary mechanism rather than recycle the known obstruction.
- prior-work stop sentence: The current source settles the odd-r branch below the boundary and at the boundary, but Table 6 still leaves BSHM(88,7,7,-1) open.
- recommended first attack: Refine the Proposition 72 block-structure argument for the order-88 complementary block to force an order-specific obstruction or a highly constrained candidate split.
- paper if solved: If solved exactly, the paper would be a short note settling the next unresolved odd-r s = 2 case in the Type 1 balancedly splittable Hadamard family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 69, Corollary 70, Proposition 72, Table 6 on page 36, and Corollary 74 on page 37: the paper leaves (88,7,7,-1) as the next unresolved odd-r case with s = 2 in the Type 1 family BSHM(4rs,4s-1,4s-1,-1).
- Jedwab-Li-Simon (2023), especially Proposition 69, Corollary 70, Proposition 72, Table 6, and Corollary 74, together with Kharaghani-Suda (2019) for the original BSHM framework.
- artifacts/bshm-88-7-7-neg1/record.md
- artifacts/bshm-88-7-7-neg1/status.json
