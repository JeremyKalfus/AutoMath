# Working Packet: The First Open s = 5 Case for BSHM(4rs,4s-1,4s-1,-1) with r == 2 (mod 4)

- slug: `bshm-120-19-19-neg1`
- title: bshm-120-19-19-neg1
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.75`

## statement
Determine whether an order-120 Hadamard matrix exists that is balanced splittable with parameters (120,19,19,-1).

## novelty_notes
- frontier basis: Corollary 74 leaves the odd-s portion of the r == 2 (mod 4) branch open, and Table 6 records (120,19,19,-1) as the first s = 5 tuple in that residual list.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the order-120, s = 5 case is settled, the note already has a clean frontier hook: it closes the first s = 5 residue in an explicitly isolated branch. What remains is mainly a short recap of Corollary 74 and the exact certificate.
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
- assessment: Lane-eligible. The first-s = 5 framing gives this exact tuple a credible title theorem, low editorial overhead, and a stable note shape.

## likely_paper_shape
- note title: The First Open s = 5 Case for BSHM(4rs,4s-1,4s-1,-1) with r == 2 (mod 4)
- hypothetical title: The First Open s = 5 Case for Balanced Splittable Hadamard Matrices in the r == 2 (mod 4) Branch
- paper shape: A single-theorem note on the first unresolved s = 5 Type 1 BSHM case in the even-r odd-s branch.
- publication if solved: A construction or obstruction for BSHM(120,19,19,-1) would plausibly be publishable as a short note settling the first open s = 5 residue in the r == 2 (mod 4) branch of a named BSHM family.
- minimal artifact requirements: Either an explicit order-120 Hadamard matrix with a certified 19-row balanced split yielding inner products 19 and -1, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (120,19,19,-1). In the Type 1 family BSHM(4rs,4s-1,4s-1,-1), Jedwab, Li, and Simon proved that the branch r == 2 (mod 4), r > 2 is settled when s = 1 or s is even and otherwise open; Table 6 shows that (120,19,19,-1) is the first s = 5 tuple left unresolved. Resolving this parameter yields a compact note because the surrounding framework, neighboring solved cases, and exact frontier location are already available.

## single_solve_explanation
This tuple is already paper-shaped because it is the first unresolved s = 5 representative in a named open branch, not just an arbitrary larger instance. Once the exact proof is known, the paper mainly needs to recall Corollary 74, explain the new s = 5 residue, and present the certificate. The solve therefore supplies most of the final note.

## broader_theorem_nonimplication
Corollary 74 covers r == 2 (mod 4) only for s = 1 or even s and explicitly leaves odd s > 1 open. The tuple (120,19,19,-1) has r = 6 and s = 5, so it sits exactly in the published open regime and is not implied by the broader theorem.

## literature_gap
Current checked source literature leaves BSHM(120,19,19,-1) unresolved as the first s = 5 entry in Table 6 of the Type 1 family.

## transfer_kit
- lemma: Proposition 69 converts the b = 0 case BSHM(4rs,4s,4s,0) into the b = -1 case BSHM(4rs,4s-1,4s-1,-1) when the all-ones row is present.
- lemma: Corollary 70 gives general existence mechanisms from Hadamard matrices of orders r and 4s or of orders 2r and 2s.
- lemma: Corollary 74 identifies the unresolved even-r odd-s branch and leaves s = 5 uncovered.
- lemma: Table 6 lists (120,19,19,-1) as the first open s = 5 case.
- toy example: The solved benchmark BSHM(40,19,19,-1) lies in the r = 2 slice of Corollary 74 and shows that the s = 5 parameter itself is compatible with the family outside the unresolved branch.
- known obstruction: The known constructions in the r == 2 (mod 4) branch do not extend from even s to odd s > 1, so the obstruction is precisely the odd-s residue rather than the ambient parameter formulas.
- prior-work stop sentence: The current source settles the r == 2 (mod 4) branch when s = 1 or s is even, but Table 6 still leaves BSHM(120,19,19,-1) open as the first s = 5 case.
- recommended first attack: Use Proposition 69 to reduce the question to a 20-row split and test whether the repeated-block structure for r = 6, s = 5 forces an order-specific obstruction or a constrained construction.
- paper if solved: If solved exactly, the paper would be a short note closing the first s = 5 residue in the r == 2 (mod 4) branch of the Type 1 balancedly splittable Hadamard family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 69, Corollary 70, Table 6 on page 36, and Corollary 74 on page 37: the paper leaves (120,19,19,-1) as the first open s = 5 case in the r == 2 (mod 4) branch of the Type 1 family BSHM(4rs,4s-1,4s-1,-1).
- Jedwab-Li-Simon (2023), especially Proposition 69, Corollary 70, Table 6, and Corollary 74, together with Kharaghani-Suda (2019) for the original BSHM formulation.
- artifacts/bshm-120-19-19-neg1/record.md
- artifacts/bshm-120-19-19-neg1/status.json
