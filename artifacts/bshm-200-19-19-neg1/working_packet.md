# Working Packet: The Parameter Set (200,19,19,-1) for Balancedly Splittable Hadamard Matrices

- slug: `bshm-200-19-19-neg1`
- title: bshm-200-19-19-neg1
- publication status: `NONE`
- packet quality: `weak`
- micro-paper eligible: `False`
- paper leverage score: `58`
- single-solve-to-paper fraction: `0.66`

## statement
Determine whether an order-200 Hadamard matrix exists that is balancedly splittable with parameters (200,19,19,-1).

## novelty_notes
- frontier basis: Table 6 leaves (200,19,19,-1) open in the same s = 5 branch as the smaller order-120 tuple.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The source still supplies a compact residual-table narrative, but the smaller order-120 s = 5 case is the cleaner title theorem. That means additional scope justification would remain even after solving the order-200 case.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: weak
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: unclear
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Not lane-eligible under the present audit. The tuple still looks open, but theorem-slice stability is too weak because the smaller unresolved s = 5 case dominates the paper narrative.

## likely_paper_shape
- note title: The Parameter Set (200,19,19,-1) for Balancedly Splittable Hadamard Matrices
- hypothetical title: The Parameter Set (200,19,19,-1) in the Type 1 BSHM Family
- paper shape: A short note on another unresolved s = 5 Type 1 BSHM parameter.
- publication if solved: A construction or obstruction for BSHM(200,19,19,-1) could still matter, but bounded curation did not certify it as a clean micro-paper target because a smaller unresolved s = 5 case already supplies the stronger title theorem.
- minimal artifact requirements: Either an explicit order-200 Hadamard matrix with a certified 19-row balanced split yielding inner products 19 and -1, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balancedly splittable Hadamard matrix with parameters (200,19,19,-1). The 2023 classification of the Type 1 family BSHM(4rs,4s-1,4s-1,-1) leaves this tuple in the residual open list for the branch r == 2 (mod 4), odd s > 1. Resolving the case would still be mathematically relevant, but the publication packet is weaker than for the smaller order-120 s = 5 tuple because the exact title theorem is less frontier-efficient.

## single_solve_explanation
An exact proof would provide a real result, but it would not obviously deliver 70-90% of the best possible paper packet. The remaining work would include explaining why order 200 deserves a standalone note instead of being overshadowed by the smaller unresolved s = 5 case or by a broader branch statement. That extra scope work keeps this candidate outside the preferred micro-paper lane.

## broader_theorem_nonimplication
Published results still leave odd s > 1 open in the r == 2 (mod 4) branch, so no current theorem settles (200,19,19,-1). However, because (120,19,19,-1) is a smaller unresolved tuple in the same s = 5 branch, the most honest theorem after a successful proof may not remain the exact 200-case.

## literature_gap
Current checked source literature still leaves BSHM(200,19,19,-1) unresolved in Table 6, but the cleaner s = 5 literature gap is already supplied by the smaller order-120 tuple.

## transfer_kit
- lemma: Proposition 69 links the b = 0 and b = -1 Type 1 families when the all-ones row is present.
- lemma: Corollary 70 gives the standard existence mechanisms for BSHM(4rs,4s-1,4s-1,-1).
- lemma: Corollary 74 leaves the r == 2 (mod 4), odd-s branch open.
- lemma: Table 6 lists both (120,19,19,-1) and (200,19,19,-1) in the s = 5 branch.
- toy example: The solved benchmark BSHM(40,19,19,-1) lies in the r = 2 slice and shows that s = 5 itself is compatible with the family outside the unresolved branch.
- known obstruction: The smaller unresolved s = 5 tuple (120,19,19,-1) threatens title-theorem stability, because any generic method for the branch would likely make the order-200 case a corollary or a secondary instance.
- prior-work stop sentence: The current source leaves BSHM(200,19,19,-1) open in Table 6, but the cleaner publication gap for s = 5 is already represented by the smaller tuple BSHM(120,19,19,-1).
- recommended first attack: Only pursue this tuple if the order-120 s = 5 case is blocked for non-mathematical reasons; otherwise the stronger first attack is to target the smaller s = 5 representative.
- paper if solved: If solved exactly, the paper would still be a short note on an unresolved s = 5 parameter, but it would need extra justification to avoid being overshadowed by the smaller order-120 case.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 69, Corollary 70, Table 6 on page 36, and Corollary 74 on page 37: the paper leaves (200,19,19,-1) open in the same s = 5, r == 2 (mod 4) branch as (120,19,19,-1).
- Jedwab-Li-Simon (2023), especially Proposition 69, Corollary 70, Table 6, and Corollary 74, together with Kharaghani-Suda (2019).
- artifacts/bshm-200-19-19-neg1/record.md
- artifacts/bshm-200-19-19-neg1/status.json
