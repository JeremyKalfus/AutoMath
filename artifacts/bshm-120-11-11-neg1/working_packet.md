# Working Packet: The Parameter Set (120,11,11,-1) for Balanced Splittable Hadamard Matrices

- slug: `bshm-120-11-11-neg1`
- title: bshm-120-11-11-neg1
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `79`
- single-solve-to-paper fraction: `0.78`

## statement
Determine whether an order-120 Hadamard matrix exists that is balanced splittable with parameters (120,11,11,-1).

## novelty_notes
- frontier basis: Corollary 74 leaves the branch r == 2 (mod 4), r > 2, odd s > 1 explicitly open, and Table 6 records (120,11,11,-1) as the next unresolved s = 3 case after the order-72 tuple.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: Once the exact 120-case is settled, the note is already shaped: recall Corollary 74, explain the odd-s residue at s = 3, and present the certificate. The surrounding exposition is short because the family classification is already in the literature.
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
- assessment: Lane-eligible. This is a stable exact slice with strong family anchoring and a crisp frontier narrative tied to the next unresolved odd-s residue after the order-72 case.

## likely_paper_shape
- note title: The Parameter Set (120,11,11,-1) for Balanced Splittable Hadamard Matrices
- hypothetical title: The Parameter Set (120,11,11,-1) for Balanced Splittable Hadamard Matrices
- paper shape: A single-theorem note on the next unresolved even-r, odd-s Type 1 BSHM parameter after the order-72 case.
- publication if solved: A construction or obstruction for BSHM(120,11,11,-1) would plausibly be publishable as a short note on the next unresolved odd-s residue in the r == 2 (mod 4) branch of a named BSHM family.
- minimal artifact requirements: Either an explicit order-120 Hadamard matrix with a certified 11-row balanced split yielding inner products 11 and -1, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (120,11,11,-1). Jedwab, Li, and Simon proved that in the Type 1 family BSHM(4rs,4s-1,4s-1,-1), the branch r == 2 (mod 4), r > 2 is settled when s = 1 or s is even and otherwise remains open; Table 6 records (120,11,11,-1) as the next unresolved s = 3 case after the order-72 tuple. Resolving this parameter yields a concise stand-alone note because the family framework and the neighboring solved cases are already available.

## single_solve_explanation
This exact tuple is already close to a title theorem because it sits in an explicitly isolated open branch of Corollary 74. Once the existence or nonexistence proof is known, the remaining work is mostly to recap the branch structure, explain why the s = 3 residue persists at r = 10, and state the witness or obstruction. That places the solve itself in the target 70-90% band of the eventual paper.

## broader_theorem_nonimplication
Corollary 74 settles the r == 2 (mod 4) branch only when s = 1 or s is even; it explicitly leaves odd s > 1 open. The tuple (120,11,11,-1) has r = 10 and s = 3, so no broader published theorem in the canonical source already determines it.

## literature_gap
Current checked source literature leaves BSHM(120,11,11,-1) unresolved in Table 6 as the next even-r, odd-s case with s = 3.

## transfer_kit
- lemma: Proposition 69 converts a BSHM(4rs,4s,4s,0) containing the all-ones row into a BSHM(4rs,4s-1,4s-1,-1).
- lemma: Corollary 70 gives broad existence for BSHM(4rs,4s-1,4s-1,-1) when Hadamard matrices of orders r and 4s or of orders 2r and 2s are available.
- lemma: Corollary 74 identifies the unresolved branch r == 2 (mod 4), r > 2, odd s > 1.
- lemma: Table 6 lists (120,11,11,-1) among the residual open tuples in that branch.
- toy example: The solved benchmark BSHM(24,11,11,-1) lies in the r = 2 slice of Corollary 74 and shows that the s = 3 parameter itself is not the obstruction.
- known obstruction: The published even-r constructions cover s = 1 and all even s, so any proof for (120,11,11,-1) must confront the genuinely new odd-s residue rather than repackage the known constructions.
- prior-work stop sentence: The current source settles the r == 2 (mod 4) branch of BSHM(4rs,4s-1,4s-1,-1) when s = 1 or s is even, but Table 6 still leaves BSHM(120,11,11,-1) open.
- recommended first attack: Use Proposition 69 to analyze the underlying 12-row split BSHM(120,12,12,0) candidate and force an order-specific obstruction or construction in the s = 3 residue.
- paper if solved: If solved exactly, the paper would be a short note settling the next unresolved s = 3 case in the r == 2 (mod 4) branch of the Type 1 balancedly splittable Hadamard family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 69, Corollary 70, Table 6 on page 36, and Corollary 74 on page 37: the paper leaves (120,11,11,-1) as the next unresolved even-r, odd-s case after (72,11,11,-1) in the Type 1 family BSHM(4rs,4s-1,4s-1,-1).
- Jedwab-Li-Simon (2023), especially Proposition 69, Corollary 70, Table 6, and Corollary 74, together with Kharaghani-Suda (2019) for the original BSHM setup.
- artifacts/bshm-120-11-11-neg1/record.md
- artifacts/bshm-120-11-11-neg1/status.json
