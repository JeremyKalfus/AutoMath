# Working Packet: The Parameter Set (120,12,12,0) for Balanced Splittable Hadamard Matrices

- slug: `bshm-120-12-12-0`
- title: bshm-120-12-12-0
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `80`
- single-solve-to-paper fraction: `0.79`

## statement
Determine whether an order-120 Hadamard matrix exists that is balanced splittable with parameters (120,12,12,0).

## novelty_notes
- frontier basis: Theorem 65 and Remark 66 isolate the known Type 2 constructions, Corollary 67 leaves the odd-odd residue unresolved, and Table 5 records (120,12,12,0) as the first r = 5, s = 3 point in that residual list.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the order-120, s = 3 case is settled, the note already has a clean family hook and needs very little beyond the exact certificate. The surrounding Type 2 framework is already organized in Theorem 65, Remark 66, and Corollary 67.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. This exact tuple has a stable family anchor, low packaging cost, and enough narrative support to function as the title theorem of a short note.

## likely_paper_shape
- note title: The Parameter Set (120,12,12,0) for Balanced Splittable Hadamard Matrices
- hypothetical title: The Parameter Set (120,12,12,0) for Balanced Splittable Hadamard Matrices
- paper shape: A single-theorem note on the first r = 5, s = 3 unresolved parameter in the Type 2 BSHM(8rs,4s,4s,0) family.
- publication if solved: A construction or obstruction for BSHM(120,12,12,0) would plausibly be publishable as a short note settling the first r = 5, s = 3 open case in the Type 2 BSHM(8rs,4s,4s,0) family.
- minimal artifact requirements: Either an explicit order-120 Hadamard matrix with a certified 12-row balanced split yielding inner products 12 and 0, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (120,12,12,0). Jedwab, Li, and Simon showed that the Type 2 family BSHM(8rs,4s,4s,0) is resolved outside the odd-odd regime, and Table 5 lists (120,12,12,0) among the remaining unresolved parameters. Resolving this exact tuple would produce a short note because the family classification, neighboring positive cases, and exact frontier placement are already available in the source literature.

## single_solve_explanation
The exact order-120 statement is already close to paper-shaped because it lies in an explicitly tabulated residual list rather than an amorphous broader program. Once the existence or nonexistence proof is known, the note mainly needs to summarize the Type 2 classification and present the certificate. That keeps the single solve well within the target publication fraction.

## broader_theorem_nonimplication
Corollary 67 settles the Type 2 family only outside the odd-odd regime. The tuple (120,12,12,0) has r = 5 and s = 3, so it lies inside the residual odd-odd branch and is not implied by the broader theorem.

## literature_gap
Current checked source literature leaves BSHM(120,12,12,0) unresolved as the first r = 5, s = 3 entry in Table 5 of the Type 2 family.

## transfer_kit
- lemma: Theorem 65(i) gives the standard construction route from Hadamard matrices of orders 2r and 4s.
- lemma: Theorem 65(ii) gives the alternative construction route from Hadamard matrices of orders 4r and 2s.
- lemma: Remark 66 states that all known existence results for the Type 2 family are already accounted for by Theorem 65.
- lemma: Corollary 67 and Table 5 isolate (120,12,12,0) inside the remaining odd-odd residue.
- toy example: The solved benchmark BSHM(48,12,12,0) lies in the r = 2 slice and shows that the s = 3 parameter is compatible with the family outside the odd-odd residue.
- known obstruction: The known existence mechanisms all require escaping the odd-odd regime, so the r = 5, s = 3 case cannot be obtained by a direct application of the published product theorems.
- prior-work stop sentence: The current source resolves the Type 2 family outside the odd-odd regime and still lists BSHM(120,12,12,0) in Table 5.
- recommended first attack: Push the Type 2 product decomposition for r = 5, s = 3 until it either yields a constrained block model for a construction or forces an incompatibility in the associated strongly regular graph parameters.
- paper if solved: If solved exactly, the paper would be a short note settling the parameter set (120,12,12,0) inside the residual odd-odd branch of the Type 2 family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Theorem 65, Remark 66, Table 5 on page 33, and Corollary 67 on page 34: the paper leaves (120,12,12,0) as the first open r = 5, s = 3 case in the Type 2 family BSHM(8rs,4s,4s,0).
- Jedwab-Li-Simon (2023), especially Theorem 65, Remark 66, Table 5, and Corollary 67, together with Kharaghani-Suda (2019) for the original balancedly splittable Hadamard-matrix setup.
- artifacts/bshm-120-12-12-0/record.md
- artifacts/bshm-120-12-12-0/status.json
