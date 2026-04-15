# Working Packet: The First Open s = 2 Odd-r Case for BSHM(4rs,4s-1,4s-1,-1)

- slug: `bshm-72-7-7-neg1`
- title: bshm-72-7-7-neg1
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `71`
- single-solve-to-paper fraction: `0.73`

## statement
Determine whether an order-72 Hadamard matrix exists that is balanced splittable with parameters (72,7,7,-1).

## novelty_notes
- frontier basis: Table 6 leaves (72,7,7,-1) as the smallest unresolved odd-r parameter with s = 2 after the source's generic Type 1 restrictions are applied.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the order-72, s = 2 case is settled, the note already has a clear first-open-case narrative inside a named family. Beyond the solve, the paper mostly needs a brief summary of the odd-r restrictions and the exact certificate.
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
- assessment: Lane-eligible, though weaker than the top four entries because its publication story is still a table-residue note rather than a regime-first theorem.

## likely_paper_shape
- note title: The First Open s = 2 Odd-r Case for BSHM(4rs,4s-1,4s-1,-1)
- hypothetical title: The Parameter Set (72,7,7,-1) for Balanced Splittable Hadamard Matrices
- paper shape: A short note settling the first unresolved s = 2 odd-r Type 1 BSHM parameter.
- publication if solved: A construction or obstruction for BSHM(72,7,7,-1) would plausibly be publishable as a short note settling the first open s = 2 odd-r Type 1 case.
- minimal artifact requirements: Either an explicit order-72 Hadamard matrix with a certified 7-row balanced split yielding inner products 7 and -1, or a concise impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (72,7,7,-1). The 2023 Type 1 classification leaves this tuple as the first unresolved odd-r case with s = 2 after the broad structural restrictions are imposed. Resolving the case yields a compact stand-alone note because the surrounding family theory is already developed in the source.

## single_solve_explanation
The order-72 tuple already comes with a natural first-open-case narrative inside the s = 2 branch. Once the answer is known, most of the remaining work is expository rather than mathematical. That keeps the single solve comfortably within the target publication fraction.

## broader_theorem_nonimplication
The source only proves odd-r nonexistence below the threshold r < 4s - 1 and gives the boundary construction at r = 4s - 1. For (72,7,7,-1), we have r = 9 and s = 2, so the case lies just beyond the boundary and remains explicitly open in Table 6.

## literature_gap
Current checked source literature leaves BSHM(72,7,7,-1) unresolved as the first s = 2 odd-r entry in Table 6.

## transfer_kit
- lemma: Proposition 68 gives the repeated-block Type 1 structure.
- lemma: Proposition 72 proves the odd-r threshold r >= 4s - 1 and gives a parity-based arithmetic obstruction.
- lemma: Result 8(vi) gives the boundary construction at r = 4s - 1, which for s = 2 yields a solved benchmark at (56,7,7,-1).
- lemma: Table 6 lists (72,7,7,-1) as open.
- toy example: The nearest positive benchmark is BSHM(56,7,7,-1), the boundary case r = 4s - 1 with s = 2.
- known obstruction: The odd-r theory already proves that no case with r < 4s - 1 can exist, so the order-72 tuple sits immediately above a sharp structural threshold.
- prior-work stop sentence: The current source leaves BSHM(72,7,7,-1) as the first unresolved s = 2 odd-r parameter in Table 6.
- recommended first attack: Use the Proposition 68 repeated-block form and the Proposition 72 odd-square constraint to test whether the first post-threshold s = 2 case admits any order-72 realization at all.
- paper if solved: If solved exactly, the paper would be a short note on the first unresolved s = 2 odd-r case in the Type 1 balancedly splittable Hadamard-matrix family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 68, Proposition 72, Table 6 on page 36, and Corollary 74 on page 37: the paper leaves (72,7,7,-1) as the first unresolved odd-r case with s = 2 in the Type 1 family BSHM(4rs,4s-1,4s-1,-1).
- Jedwab-Li-Simon (2023), especially Proposition 68, Proposition 72, Table 6, and Corollary 74, together with Kharaghani-Suda (2019) for the original BSHM framework.
- artifacts/bshm-72-7-7-neg1/record.md
- artifacts/bshm-72-7-7-neg1/status.json
