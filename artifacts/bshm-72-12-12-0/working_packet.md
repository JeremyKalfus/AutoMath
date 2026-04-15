# Working Packet: The First Odd-Odd Open Case for BSHM(8rs,4s,4s,0)

- slug: `bshm-72-12-12-0`
- title: bshm-72-12-12-0
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `86`
- single-solve-to-paper fraction: `0.84`

## statement
Determine whether an order-72 Hadamard matrix exists that is balanced splittable with parameters (72,12,12,0).

## novelty_notes
- frontier basis: Theorem 65 determines all currently known existence cases, Remark 66 states that no other existence results are known, Corollary 67 leaves only odd r,s > 1 unresolved, and Table 5 starts that residue with (72,12,12,0).
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the order-72 case is settled, the paper is nearly complete: recall Theorem 65 and Corollary 67, explain why this is the first odd-odd residue, and present the exact witness or obstruction. Very little remains beyond concise framing and certificate verification.
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
- assessment: Top-ranked usable micro-paper candidate in the current audited queue. This is the smallest odd-odd open case in a named family, with a stable theorem slice, a clear title-theorem narrative, cheap packaging, and no obvious broader published result already settling it. This curation run retained it as the active selection after the thin-memory exclusion sweep confirmed no local conflict, and it rewrote the five-slot queue from the existing audited shortlist without further browsing because the repository already contained a lane-eligible survivor.

## likely_paper_shape
- note title: The First Odd-Odd Open Case for BSHM(8rs,4s,4s,0)
- hypothetical title: The First Odd-Odd Open Case for Balanced Splittable Hadamard Matrices with Parameters (8rs,4s,4s,0)
- paper shape: A single-theorem note on the first unresolved odd-odd parameter in the Type 2 BSHM(8rs,4s,4s,0) family.
- publication if solved: A construction or obstruction for BSHM(72,12,12,0) would plausibly yield a short note settling the first odd-odd open case in the Type 2 BSHM(8rs,4s,4s,0) family.
- minimal artifact requirements: Either an explicit order-72 Hadamard matrix with a certified 12-row balanced split yielding inner products 12 and 0, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (72,12,12,0). Jedwab, Li, and Simon showed that all known existence results for the Type 2 family BSHM(8rs,4s,4s,0) arise from Theorem 65 and that, assuming the Hadamard matrix conjecture, only odd r,s > 1 remain unresolved; Table 5 begins that residual list with (72,12,12,0). Resolving this parameter closes the smallest odd-odd residue in the family and yields a compact stand-alone note.

## single_solve_explanation
This tuple already reads like a title theorem because the source isolates it as the first open odd-odd parameter in a named BSHM family. Once the existence or nonexistence proof is in hand, the rest of the note is short: summarize Theorem 65 and Corollary 67, explain the odd-odd residue, and present the certificate. That keeps the solve squarely in the 70-90% range of the final paper.

## broader_theorem_nonimplication
Corollary 67 leaves the Type 2 family unresolved exactly when both r and s are odd and greater than 1. The tuple (72,12,12,0) has r = 3 and s = 3, so it lies precisely in the published open regime and is not implied by the broader theorem.

## literature_gap
Current checked source literature determines the Type 2 family BSHM(8rs,4s,4s,0) outside the odd-odd residue, where Table 5 begins with BSHM(72,12,12,0).

## transfer_kit
- lemma: Theorem 65(i) gives existence for BSHM(8rs,4s,4s,0) when Hadamard matrices of orders 2r and 4s exist.
- lemma: Theorem 65(ii) gives existence for BSHM(8rs,4s,4s,0) when Hadamard matrices of orders 4r and 2s exist.
- lemma: Remark 66 states that all currently known existence results for BSHM(8rs,4s,4s,0) come from Theorem 65.
- lemma: Corollary 67 leaves only the odd-odd residue unresolved, and Table 5 lists (72,12,12,0) first.
- toy example: The nearby positive benchmark BSHM(48,12,12,0) lies in the solved r = 2 slice of Corollary 67 and shows that the s = 3 parameter itself is compatible with the family outside the odd-odd residue.
- known obstruction: The known constructions stop exactly when both r and s are odd and greater than 1, so any proof for order 72 must address the genuine odd-odd residue rather than repackage an even-factor construction.
- prior-work stop sentence: The current source determines BSHM(8rs,4s,4s,0) whenever at least one of r,s is not an odd integer greater than 1, and Table 5 starts the remaining odd-odd cases with BSHM(72,12,12,0).
- recommended first attack: Exploit the product structure behind Theorem 65 and Proposition 64 to test whether the odd-odd obstruction at r = s = 3 can be converted into an order-specific construction or a contradiction in the associated strongly regular graph parameters.
- paper if solved: If solved exactly, the paper would be a short note closing the smallest odd-odd residue in the Type 2 balanced splittable Hadamard-matrix family.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Theorem 65, Remark 66, Table 5 on page 33, and Corollary 67 on page 34: the paper leaves (72,12,12,0) as the first open odd-odd case in the Type 2 family BSHM(8rs,4s,4s,0).
- Jedwab-Li-Simon (2023), especially Theorem 65, Remark 66, Table 5, and Corollary 67, together with Kharaghani-Suda (2019) for the original balancedly splittable Hadamard-matrix setup.
- artifacts/bshm-72-12-12-0/record.md
- artifacts/bshm-72-12-12-0/status.json
