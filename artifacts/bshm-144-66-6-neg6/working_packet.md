# Working Packet: The First u ≡ 2 (mod 4) Case for Balancedly Splittable Hadamard Matrices

- slug: `bshm-144-66-6-neg6`
- title: bshm-144-66-6-neg6
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.84`

## statement
Determine whether an order-144 Hadamard matrix exists that is balancedly splittable with parameters (144,66,6,-6).

## novelty_notes
- frontier basis: The source proves the family for Hadamard-order u, rules out odd u, and then singles out u = 6 as the smallest unresolved case in the remaining congruence class.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the 144-case is settled, the note already has a crisp family anchor, a smallest-open-case framing, and a compact target certificate. What remains after the solve is mostly a clean presentation of the construction or obstruction and a short placement relative to the known positive and negative results.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. This is a stable smallest-residue packet with strong family anchoring and low post-solve editorial drag.

## likely_paper_shape
- note title: The First u ≡ 2 (mod 4) Case for Balancedly Splittable Hadamard Matrices
- hypothetical title: A Balancedly Splittable Hadamard Matrix with Parameters (144,66,6,-6)
- paper shape: A single-theorem design-theory note closing the first unresolved u ≡ 2 (mod 4) BSHM(4u^2,2u^2-u,u,-u) case.
- publication if solved: A construction or obstruction for BSHM(144,66,6,-6) would plausibly be publishable as a short note closing the first unresolved u ≡ 2 (mod 4) case in a named BSHM family.
- minimal artifact requirements: Either an explicit order-144 Hadamard matrix with a certified 66-row balanced split giving inner products 6 and -6, or a compact obstruction ruling out that parameter set.

## hypothetical_abstract
We determine the existence status of a balancedly splittable Hadamard matrix with parameters (144,66,6,-6). Daniel and Praeger proved the natural positive family BSHM(4u^2,2u^2-u,u,-u) when u is a Hadamard order, excluded all odd u, and identified u = 6 as the first unresolved case with u ≡ 2 (mod 4). Resolving this parameter closes the first explicit residue in that family and yields a compact stand-alone note.

## single_solve_explanation
The exact 144-parameter statement is already a natural title theorem because the source isolates it as the first unresolved congruence-class residue. Once the existence or nonexistence proof is in hand, the rest of the paper is short: recall the family theorem, explain why u = 6 is the first remaining case, and present the witness or obstruction. That puts the solve comfortably in the 70-90% range of the finished note.

## broader_theorem_nonimplication
The 2023 paper proves the family only when u is itself a Hadamard order and explicitly leaves the u ≡ 2 (mod 4), u > 2 regime open. Its odd-u nonexistence theorem does not touch u = 6, so no broader published theorem already settles the 144-case.

## literature_gap
Current checked source literature proves BSHM(4u^2,2u^2-u,u,-u) for Hadamard-order u and proves nonexistence for odd u, but does not determine the first remaining case u = 6, i.e. BSHM(144,66,6,-6).

## transfer_kit
- lemma: Result 14 in the source gives existence of BSHM(4u^2,2u^2-u,u,-u) whenever u is the order of a Hadamard matrix.
- lemma: Result 7(i) in the source proves that BSHM(4u^2,2u^2-u,u,-u) does not exist when u is odd.
- lemma: Open Question (iii) on page 37 states that the remaining unresolved regime is u ≡ 2 (mod 4), u > 2, and identifies u = 6 as the smallest open case.
- lemma: The same passage notes that a real flat 66 x 144 equiangular tight frame already exists, so the missing issue is the Hadamard-submatrix realization.
- toy example: The neighboring positive benchmark is the u = 2 case BSHM(16,6,2,-2), which lies in the proved family.
- known obstruction: The odd-u nonexistence theorem blocks any attempt to extrapolate from nearby odd parameters, so the u = 6 case must use genuinely different structure.
- prior-work stop sentence: The current source proves the family for Hadamard-order u, rules out odd u, and then stops at the explicit open case BSHM(144,66,6,-6).
- recommended first attack: Exploit the known 66 x 144 real flat ETF and test whether it can be embedded as the designated split inside an order-144 Hadamard matrix, while using the strongly regular graph constraints from the source to prune impossible signatures.
- paper if solved: If solved exactly, the paper would be a short note closing the first unresolved u ≡ 2 (mod 4) case in the balancedly splittable Hadamard-matrix family.

## bounded_source_list
- Leah H. K. Daniel and Cheryl E. Praeger, "Balancedly splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Open Question (iii) on page 37: the paper proves existence of BSHM(4u^2,2u^2-u,u,-u) when u is the order of a Hadamard matrix, proves nonexistence for odd u, and identifies u = 6, i.e. BSHM(144,66,6,-6), as the smallest open case with u ≡ 2 (mod 4).
- Daniel-Praeger (2023), especially Open Question (iii) on page 37 and the surrounding family results, together with Kharaghani-Suda (2019) for the foundational balancedly splittable Hadamard-matrix setup.
- artifacts/bshm-144-66-6-neg6/record.md
- artifacts/bshm-144-66-6-neg6/status.json
