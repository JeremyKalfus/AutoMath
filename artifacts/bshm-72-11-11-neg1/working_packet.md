# Working Packet: The First Open Odd-s Case for BSHM(4rs,4s-1,4s-1,-1) with r == 2 (mod 4)

- slug: `bshm-72-11-11-neg1`
- title: bshm-72-11-11-neg1
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `83`
- single-solve-to-paper fraction: `0.82`

## statement
Determine whether an order-72 Hadamard matrix exists that is balanced splittable with parameters (72,11,11,-1).

## novelty_notes
- frontier basis: Corollary 74 isolates the branch r == 2 (mod 4), r > 2 as solved when s = 1 or s is even and otherwise open, and Table 6 records (72,11,11,-1) as the first remaining odd-s tuple in that branch.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the order-72 case is settled, the paper is nearly complete: recall Corollary 74, explain why this is the first unresolved odd-s residue, and present the exact witness or obstruction. Very little remains beyond framing and verification.
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
- assessment: Lane-eligible. This is a stable, regime-first exact case with strong family anchoring, cheap packaging, and no obvious broader theorem already implying the answer.

## likely_paper_shape
- note title: The First Open Odd-s Case for BSHM(4rs,4s-1,4s-1,-1) with r == 2 (mod 4)
- hypothetical title: The Parameter Set (72,11,11,-1) for Balanced Splittable Hadamard Matrices
- paper shape: A single-theorem design-theory note on the first unresolved odd-s case in the r == 2 (mod 4) branch of BSHM(4rs,4s-1,4s-1,-1).
- publication if solved: A construction or obstruction for BSHM(72,11,11,-1) would plausibly be publishable as a short note settling the first open odd-s residue in the r == 2 (mod 4) branch of a named BSHM family.
- minimal artifact requirements: Either an explicit order-72 Hadamard matrix with a certified 11-row balanced split yielding inner products 11 and -1, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (72,11,11,-1). Jedwab, Li, and Simon reduced the Type 1 family BSHM(4rs,4s-1,4s-1,-1) to explicit existence and nonexistence regions and left the branch r == 2 (mod 4), r > 2, odd s unresolved, with (72,11,11,-1) first in Table 6. Resolving this parameter closes the first open odd-s even-r residue in the family and yields a compact stand-alone note.

## single_solve_explanation
The exact order-72 statement already reads like a title theorem because the source isolates it as the first unresolved case in a named open branch. Once the existence or nonexistence proof is in hand, the rest of the note is short: recall the family classification, explain why this is the first remaining odd-s even-r case, and present the certificate. That keeps the solve squarely in the 70-90% range of the final paper.

## broader_theorem_nonimplication
Corollary 74 settles the r == 2 (mod 4) branch only when s = 1 or s is even, and explicitly leaves odd s > 1 open. The tuple (72,11,11,-1) has r = 6 and s = 3, so no broader published theorem in the canonical source already determines it.

## literature_gap
Current checked source literature determines the family BSHM(4rs,4s-1,4s-1,-1) in all r == 2 (mod 4) cases except the odd-s branch, where Table 6 begins with BSHM(72,11,11,-1).

## transfer_kit
- lemma: Proposition 69 relates BSHM(4rs,4s,4s,0) to BSHM(4rs,4s-1,4s-1,-1) when the all-ones row is present.
- lemma: Corollary 70 gives broad existence results for BSHM(4rs,4s-1,4s-1,-1) from Hadamard matrices of orders r and 4s or of orders 2r and 2s.
- lemma: Corollary 74 proves that for r == 2 (mod 4) and r > 2, existence is known when s = 1 or s is even, and otherwise open.
- lemma: Table 6 lists (72,11,11,-1) as the smallest open odd-s case in that branch.
- toy example: The neighboring positive benchmark is BSHM(24,11,11,-1), which falls under the solved r = 2 case in Corollary 74.
- known obstruction: The source's even-r constructions already handle s = 1 and all even s, so any proof for the order-72 case must confront the genuinely new odd-s residue rather than repackage the known constructions.
- prior-work stop sentence: The current source settles the r == 2 (mod 4) branch of BSHM(4rs,4s-1,4s-1,-1) except for odd s > 1, where Table 6 starts with BSHM(72,11,11,-1).
- recommended first attack: Exploit Proposition 69 and the repeated-block structure behind Type 1 parameters to test whether an underlying 12-row split can exist at order 72 or to force an order-specific obstruction.
- paper if solved: If solved exactly, the paper would be a short note closing the first open odd-s residue in the r == 2 (mod 4) branch of the BSHM(4rs,4s-1,4s-1,-1) family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Table 6 on page 36 and Corollary 74 on page 37: the paper leaves (72,11,11,-1) as the first unresolved odd-s case in the Type 1 family BSHM(4rs,4s-1,4s-1,-1) with r == 2 (mod 4), r > 2.
- Jedwab-Li-Simon (2023), especially Proposition 69, Corollary 70, Table 6, and Corollary 74, together with Kharaghani-Suda (2019) for the original BSHM setup.
- artifacts/bshm-72-11-11-neg1/record.md
- artifacts/bshm-72-11-11-neg1/status.json
