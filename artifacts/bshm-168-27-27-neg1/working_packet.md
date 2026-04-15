# Working Packet: The First Open s = 7 Case for BSHM(4rs,4s-1,4s-1,-1) with r == 2 (mod 4)

- slug: `bshm-168-27-27-neg1`
- title: bshm-168-27-27-neg1
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.73`

## statement
Determine whether an order-168 Hadamard matrix exists that is balancedly splittable with parameters (168,27,27,-1).

## novelty_notes
- frontier basis: Corollary 74 leaves the odd-s portion of the r == 2 (mod 4) branch open, and Table 6 records (168,27,27,-1) as the first s = 7 tuple in that residual list.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: Once the exact order-168 case is settled, the note has an immediate frontier narrative: it closes the first s = 7 residue in an explicit open branch. The rest is short contextual packaging around Corollary 74 and the certificate itself.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
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
- assessment: Lane-eligible, though slightly weaker than the smaller order-88 and order-120 packets. The first-s = 7 framing still gives the exact tuple a credible title theorem and compact paper packet.

## likely_paper_shape
- note title: The First Open s = 7 Case for BSHM(4rs,4s-1,4s-1,-1) with r == 2 (mod 4)
- hypothetical title: The First Open s = 7 Case for Balancedly Splittable Hadamard Matrices in the r == 2 (mod 4) Branch
- paper shape: A single-theorem note on the first unresolved s = 7 Type 1 BSHM case in the even-r odd-s branch.
- publication if solved: A construction or obstruction for BSHM(168,27,27,-1) would plausibly be publishable as a short note settling the first open s = 7 residue in the r == 2 (mod 4) branch of a named BSHM family.
- minimal artifact requirements: Either an explicit order-168 Hadamard matrix with a certified 27-row balanced split yielding inner products 27 and -1, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balancedly splittable Hadamard matrix with parameters (168,27,27,-1). In the Type 1 family BSHM(4rs,4s-1,4s-1,-1), Jedwab, Li, and Simon proved that the branch r == 2 (mod 4), r > 2 is settled when s = 1 or s is even and otherwise open; Table 6 shows that (168,27,27,-1) is the first s = 7 tuple left unresolved. Resolving this parameter yields a compact note because the literature already supplies the family classification and the neighboring solved r = 2 benchmark.

## single_solve_explanation
This target is still within the micro-paper lane because it is the first s = 7 representative of an explicitly open branch rather than a random larger case. Once the exact witness or obstruction is known, the remaining work is largely editorial: state Corollary 74, explain the first-s = 7 frontier, and present the certificate. That keeps the solve near three quarters of the final note.

## broader_theorem_nonimplication
Corollary 74 does not settle odd s > 1 in the r == 2 (mod 4) branch. Since (168,27,27,-1) has r = 6 and s = 7, it lies squarely in the published open regime and is not implied by the broader result.

## literature_gap
Current checked source literature leaves BSHM(168,27,27,-1) unresolved as the first s = 7 entry in Table 6 of the Type 1 family.

## transfer_kit
- lemma: Proposition 69 links the b = 0 and b = -1 Type 1 parameter families when the all-ones row is present.
- lemma: Corollary 70 gives broad existence for BSHM(4rs,4s-1,4s-1,-1) from lower-order Hadamard matrices.
- lemma: Corollary 74 leaves the r == 2 (mod 4), odd-s branch open.
- lemma: Table 6 lists (168,27,27,-1) as the first open s = 7 case.
- toy example: The solved benchmark BSHM(56,27,27,-1) lies in the r = 2 slice of Corollary 74 and shows that s = 7 itself is not incompatible with the family.
- known obstruction: The even-r constructions already cover s = 1 and all even s, so the remaining obstacle is the odd-s residue rather than the ambient order formula.
- prior-work stop sentence: The current source settles the r == 2 (mod 4) branch when s = 1 or s is even, but Table 6 still leaves BSHM(168,27,27,-1) open as the first s = 7 case.
- recommended first attack: Reduce via Proposition 69 to the 28-row split and test whether the r = 6, s = 7 repeated-block structure forces an order-specific obstruction or a narrowly constrained construction.
- paper if solved: If solved exactly, the paper would be a short note closing the first s = 7 residue in the r == 2 (mod 4) branch of the Type 1 balancedly splittable Hadamard family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 69, Corollary 70, Table 6 on page 36, and Corollary 74 on page 37: the paper leaves (168,27,27,-1) as the first open s = 7 case in the r == 2 (mod 4) branch of the Type 1 family BSHM(4rs,4s-1,4s-1,-1).
- Jedwab-Li-Simon (2023), especially Proposition 69, Corollary 70, Table 6, and Corollary 74, together with Kharaghani-Suda (2019) for the original BSHM framework.
- artifacts/bshm-168-27-27-neg1/record.md
- artifacts/bshm-168-27-27-neg1/status.json
