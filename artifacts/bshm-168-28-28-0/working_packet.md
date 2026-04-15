# Working Packet: The First Open s = 7 Case for BSHM(8rs,4s,4s,0)

- slug: `bshm-168-28-28-0`
- title: bshm-168-28-28-0
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `68`
- single-solve-to-paper fraction: `0.66`

## statement
Determine whether an order-168 Hadamard matrix exists that is balanced splittable with parameters (168,28,28,0).

## novelty_notes
- frontier basis: Corollary 67 leaves the odd-odd residue unresolved, and Table 5 records (168,28,28,0) as the first s = 7 parameter in that residual list.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The family anchor is real and the exact tuple is tabulated, but compared with the first four queue entries more narrative work would remain after the solve. The note would need heavier framing to justify why this later residue, rather than the smallest odd-odd frontier, is the right title theorem.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Not lane-eligible this cycle. The family anchor is real and the bounded audit did not find a settlement source, but the honest paper fraction stays below the 0.70 gate and the title theorem is weaker than the first four entries.

## likely_paper_shape
- note title: The First Open s = 7 Case for BSHM(8rs,4s,4s,0)
- hypothetical title: The First Open s = 7 Case for Balanced Splittable Hadamard Matrices in the Type 2 Family
- paper shape: A possible exact-parameter note on the first open s = 7 case in the Type 2 BSHM(8rs,4s,4s,0) family.
- publication if solved: A construction or obstruction for BSHM(168,28,28,0) might be publishable as a short note settling the first s = 7 open case in the Type 2 BSHM(8rs,4s,4s,0) family.
- minimal artifact requirements: Either an explicit order-168 Hadamard matrix with a certified 28-row balanced split yielding inner products 28 and 0, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (168,28,28,0). In the Type 2 family BSHM(8rs,4s,4s,0), the current source leaves only the odd-odd residue unresolved and lists (168,28,28,0) as the first s = 7 entry in Table 5. A solution would likely support a short note, but it would leave more packaging work than the stronger first-open residues in the same family.

## single_solve_explanation
This exact tuple still has a plausible paper story because it is the first s = 7 point in an explicitly tabulated open list. But after one solve, the note would still need more framing than the first-open odd-odd or s = 5 residues, since the family hook is a step further from the smallest frontier edge. That keeps the single-solve fraction below the lane target for this cycle.

## broader_theorem_nonimplication
Corollary 67 does not settle odd r,s > 1, and (168,28,28,0) has r = 3 and s = 7. So the broader theorem does not already determine this tuple; the reason it fails the lane is packaging strength, not broader-theorem implication.

## literature_gap
Current checked source literature leaves BSHM(168,28,28,0) unresolved as the first s = 7 entry in Table 5 of the Type 2 family.

## transfer_kit
- lemma: Theorem 65(i) gives one standard construction route for BSHM(8rs,4s,4s,0).
- lemma: Theorem 65(ii) gives a second construction route for the same family.
- lemma: Remark 66 states that all known Type 2 existence results come from Theorem 65.
- lemma: Corollary 67 and Table 5 isolate (168,28,28,0) inside the unresolved odd-odd residue.
- toy example: The solved benchmark BSHM(112,28,28,0) lies in the r = 2 slice of Corollary 67 and shows that the s = 7 parameter is compatible with the family outside the odd-odd residue.
- known obstruction: The published construction routes do not cover odd-odd cases, so any solution for order 168 must confront the genuine odd-odd barrier rather than inherit an even-factor construction.
- prior-work stop sentence: The current source resolves the Type 2 family outside the odd-odd regime and still lists BSHM(168,28,28,0) in Table 5 as the first s = 7 case.
- recommended first attack: Reuse the Type 2 product framework at r = 3, s = 7 to test whether the odd-odd barrier can be broken by an order-specific lift or sharpened into an obstruction for the associated strongly regular graph parameters.
- paper if solved: If solved exactly, the paper would likely be a short note on the first s = 7 residue in the Type 2 balanced splittable Hadamard-matrix family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Theorem 65, Remark 66, Table 5 on page 33, and Corollary 67 on page 34: the paper leaves (168,28,28,0) as the first open s = 7 case in the Type 2 family BSHM(8rs,4s,4s,0).
- Jedwab-Li-Simon (2023), especially Theorem 65, Remark 66, Table 5, and Corollary 67, together with Kharaghani-Suda (2019) for the original balancedly splittable Hadamard-matrix setup.
- artifacts/bshm-168-28-28-0/record.md
- artifacts/bshm-168-28-28-0/status.json
