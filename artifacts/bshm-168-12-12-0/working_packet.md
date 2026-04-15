# Working Packet: The Parameter Set (168,12,12,0) for Balanced Splittable Hadamard Matrices

- slug: `bshm-168-12-12-0`
- title: bshm-168-12-12-0
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.74`

## statement
Determine whether an order-168 Hadamard matrix exists that is balanced splittable with parameters (168,12,12,0).

## novelty_notes
- frontier basis: Theorem 65 and Remark 66 isolate the known Type 2 constructions, Corollary 67 leaves the odd-odd residue unresolved, and Table 5 records (168,12,12,0) as the first r = 7, s = 3 case in that residual list.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the order-168, s = 3 case is settled, the note already has a named-family anchor and a compact exact certificate. Only a short recap of the Type 2 framework is needed beyond the proof itself.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible, but weaker than the first-open residues. The family anchor is still strong enough that one exact solve could plausibly stand as the title theorem of a short note.

## likely_paper_shape
- note title: The Parameter Set (168,12,12,0) for Balanced Splittable Hadamard Matrices
- hypothetical title: The Parameter Set (168,12,12,0) for Balanced Splittable Hadamard Matrices
- paper shape: A single-theorem note on the first r = 7, s = 3 unresolved parameter in the Type 2 BSHM(8rs,4s,4s,0) family.
- publication if solved: A construction or obstruction for BSHM(168,12,12,0) would plausibly be publishable as a short note settling the first r = 7, s = 3 open case in the Type 2 BSHM(8rs,4s,4s,0) family.
- minimal artifact requirements: Either an explicit order-168 Hadamard matrix with a certified 12-row balanced split yielding inner products 12 and 0, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (168,12,12,0). The current Type 2 classification for BSHM(8rs,4s,4s,0) resolves all cases outside the odd-odd regime and lists (168,12,12,0) among the remaining open parameters in Table 5. Resolving this tuple would yield a concise note because the family theory and the exact literature frontier are already explicit.

## single_solve_explanation
This candidate is weaker than the first-open Table 5 entries, but it still has a credible short-note shape because the exact tuple is explicitly isolated in a named residual list. Once the proof is known, the remaining paper work is mostly expository and certificate-focused. That keeps the solve within the target publication fraction.

## broader_theorem_nonimplication
Corollary 67 settles the Type 2 family only outside the odd-odd regime. Since (168,12,12,0) has r = 7 and s = 3, it remains in the unresolved odd-odd branch and is not implied by the broader theorem.

## literature_gap
Current checked source literature leaves BSHM(168,12,12,0) unresolved in Table 5 of the Type 2 family.

## transfer_kit
- lemma: Theorem 65(i) gives one existence route for the Type 2 family from Hadamard matrices of orders 2r and 4s.
- lemma: Theorem 65(ii) gives a second route from Hadamard matrices of orders 4r and 2s.
- lemma: Remark 66 states that these two routes account for all known existence results in the Type 2 family.
- lemma: Corollary 67 and Table 5 isolate (168,12,12,0) in the unresolved odd-odd residue.
- toy example: The solved benchmark BSHM(48,12,12,0) shows that the s = 3 parameter is realizable outside the odd-odd residue, so the unresolved part is the odd r = 7 factor rather than s itself.
- known obstruction: The published constructions do not cross into the odd-odd regime, so the r = 7, s = 3 case cannot be obtained by direct application of Theorem 65.
- prior-work stop sentence: The current source resolves the Type 2 family outside the odd-odd regime and still lists BSHM(168,12,12,0) in Table 5.
- recommended first attack: Analyze whether the r = 7, s = 3 case can satisfy the block-product constraints implicit in Theorem 65, or whether those constraints force an obstruction in the corresponding strongly regular graph parameters.
- paper if solved: If solved exactly, the paper would be a short note settling the parameter set (168,12,12,0) inside the residual odd-odd branch of the Type 2 family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Theorem 65, Remark 66, Table 5 on page 33, and Corollary 67 on page 34: the paper leaves (168,12,12,0) as the first open r = 7, s = 3 case in the Type 2 family BSHM(8rs,4s,4s,0).
- Jedwab-Li-Simon (2023), especially Theorem 65, Remark 66, Table 5, and Corollary 67, together with Kharaghani-Suda (2019) for the original balancedly splittable Hadamard-matrix setup.
- artifacts/bshm-168-12-12-0/record.md
- artifacts/bshm-168-12-12-0/status.json
