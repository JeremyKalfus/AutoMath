# Working Packet: The First Open Type 1 Case for BSHM(4rs,4s-1,4s-1,-1)

- slug: `bshm-20-3-3-neg1`
- title: bshm-20-3-3-neg1
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.72`

## statement
Determine whether an order-20 Hadamard matrix exists that is balanced splittable with parameters (20,3,3,-1).

## novelty_notes
- frontier basis: Table 6 begins with (20,3,3,-1), while Corollary 74 shows that the surrounding Type 1 family is otherwise decided by parity, the skew-type branch, and the odd-r restriction from Proposition 72.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the order-20 case is settled, the paper is already close to complete: recall the structural restrictions leading to Table 6, explain why this is the first remaining Type 1 parameter, and present the exact witness or obstruction. The surrounding theory is already packaged in the canonical source.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. The family anchor is strong, the theorem slice is stable, and solving the first remaining Type 1 parameter would already supply most of a short note.

## likely_paper_shape
- note title: The First Open Type 1 Case for BSHM(4rs,4s-1,4s-1,-1)
- hypothetical title: The First Open Type 1 Balanced Splittable Hadamard Matrix Parameter Set
- paper shape: A single-theorem note on the first open Type 1 BSHM(4rs,4s-1,4s-1,-1) parameter.
- publication if solved: A construction or obstruction for BSHM(20,3,3,-1) would plausibly be publishable as a short note settling the first open Type 1 BSHM(4rs,4s-1,4s-1,-1) case.
- minimal artifact requirements: Either an explicit order-20 Hadamard matrix with a certified 3-row balanced split yielding inner products 3 and -1, or a compact impossibility proof.

## hypothetical_abstract
We determine the existence status of a balanced splittable Hadamard matrix with parameters (20,3,3,-1). Jedwab, Li, and Simon reduced the Type 1 family BSHM(4rs,4s-1,4s-1,-1) to a short residual list and Table 6 begins that list with (20,3,3,-1). Resolving this smallest remaining Type 1 parameter would yield a compact note because the family structure, surrounding restrictions, and exact frontier placement are already explicit in the source literature.

## single_solve_explanation
This exact tuple is already paper-shaped because it is the first unresolved parameter in a named Type 1 family, not a one-off curiosity. Once the existence or nonexistence proof is known, the note mainly needs to summarize the structural reductions behind Table 6 and present the exact certificate. That keeps the solve in the target 70-90% range of the eventual paper.

## broader_theorem_nonimplication
Corollary 74 does not settle (20,3,3,-1): for odd r it gives nonexistence only when r < 4s-1, existence on the skew-type branch when r = 4s-1, and otherwise leaves the case open. Here r = 5 and s = 1, so the tuple lies exactly in the published residual list rather than being implied by the broader theorem.

## literature_gap
Current checked source literature reduces the Type 1 family to a residual list in Table 6 and begins that list with BSHM(20,3,3,-1).

## transfer_kit
- lemma: Proposition 68 shows that any Type 1 BSHM(4rs,4s-1,4s-1,-1) can be column-reordered so that the distinguished submatrix has repeated Hadamard-block structure.
- lemma: Proposition 69 links BSHM(4rs,4s,4s,0) and Type 1 BSHM(4rs,4s-1,4s-1,-1) containing the all-ones row.
- lemma: Corollary 70(ii) rules out the all-ones-row route when r is odd.
- lemma: Proposition 72 and Corollary 74 provide the odd-r restrictions that leave (20,3,3,-1) in Table 6.
- toy example: The nearby resolved benchmark BSHM(16,3,3,-1) lies in the even-r slice covered by Corollary 74 and shows that the s = 1 Type 1 parameter itself is viable outside the residual odd branch.
- known obstruction: For odd r, any Type 1 solution cannot come from the all-ones-row lift of Proposition 69, so the order-20 case must evade the standard route already blocked by Corollary 70(ii).
- prior-work stop sentence: The current source determines the Type 1 family outside the residual list in Table 6, which begins with BSHM(20,3,3,-1).
- recommended first attack: Exploit the repeated-block structure from Proposition 68 at s = 1 to classify the possible 3 x 20 distinguished submatrices and test whether any order-20 Hadamard completion can satisfy the Type 1 dot-product pattern without the all-ones-row route.
- paper if solved: If solved exactly, the paper would be a short note settling the first open Type 1 balanced splittable Hadamard-matrix parameter set.

## bounded_source_list
- Jonathan Jedwab, Shuxing Li, and Samuel Simon, "Constructions and restrictions for balanced splittable Hadamard matrices," The Electronic Journal of Combinatorics 30(1) (2023), especially Proposition 68, Proposition 69, Corollary 70, Proposition 72, Table 6 on page 36, and Corollary 74 on pages 36-37: the paper leaves (20,3,3,-1) as the first open Type 1 case in the family BSHM(4rs,4s-1,4s-1,-1).
- Jedwab-Li-Simon (2023), especially Proposition 68, Proposition 69, Corollary 70, Proposition 72, Table 6, and Corollary 74, together with Kharaghani-Suda (2019) for the original balancedly splittable Hadamard-matrix setup.
- artifacts/bshm-20-3-3-neg1/record.md
- artifacts/bshm-20-3-3-neg1/status.json
