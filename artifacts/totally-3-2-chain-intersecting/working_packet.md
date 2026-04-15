# Working Packet: Totally (3,2)-Chain Intersecting Families

- slug: `totally-3-2-chain-intersecting`
- title: totally-3-2-chain-intersecting
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `67`
- single-solve-to-paper fraction: `0.68`

## statement
For each n, determine the maximum cardinality of a family F of subsets of [n] that contains no 3-chain A1 subset A2 subset A3 and 2-chain B1 subset B2 with A1 intersection B1 empty.

## novelty_notes
- frontier basis: The 2025 paper resolves the first open totally chain-intersecting case (2,2) and then states a general conjecture for p >= q, making (3,2) a natural next slice.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If the slice really stays at (3,2), the note would already have a clear title theorem and immediate context from the 2025 paper. The risk is that any successful proof may naturally widen to a broader q=2 or even general p >= q statement, making the curated slice unstable.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: unclear
- search-heavy: False
- certificate compactness: high
- exact gap from source: small
- assessment: Interesting but not lane-eligible. The slice is mathematically natural, yet theorem-slice stability is unclear and the final paper may want a broader statement than the curated target.

## likely_paper_shape
- note title: Totally (3,2)-Chain Intersecting Families
- hypothetical title: Totally (3,2)-Chain Intersecting Families
- paper shape: A short extremal-set-theory note proving the next concrete totally chain-intersecting case after (2,2).
- publication if solved: An exact all-n formula for the totally (3,2) case would plausibly yield a short extremal-set-theory note.
- minimal artifact requirements: A proof of the exact extremal formula for all n, together with the sharp construction and a brief stability discussion if needed.

## hypothetical_abstract
We determine the maximum size of a totally (3,2)-chain intersecting family of subsets of [n]. Gerbner's 2025 paper solves the first open totally chain-intersecting case (2,2) and formulates a general conjecture for p >= q, but does not close this next slice. An exact all-n formula would give a compact continuation note, provided the theorem does not immediately collapse into a broader general statement.

## single_solve_explanation
A clean all-n extremal formula would likely supply the main theorem, proof, and sharp construction in one shot. Some write-up would still be needed to justify why the (3,2) slice deserves separate emphasis rather than being subsumed by a stronger theorem. That instability pushes the packet slightly below the desired 70-90% range.

## broader_theorem_nonimplication
The 2025 paper proves only the totally (2,2) case and states a conjecture for the broader family; it does not already imply the (3,2) formula. The issue is not implication from known theorems but the risk that a successful proof would immediately broaden the honest claim.

## literature_gap
After the exact (2,2) theorem, the current checked source leaves the general totally (p,q) conjecture open and does not settle the specialized totally (3,2) case.

## transfer_kit
- lemma: The 2025 paper proves that the largest totally (2,2)-chain intersecting family has cardinality 2^(n-1).
- lemma: The same paper states Conjecture 6 giving the proposed extremal formula for totally (p,q)-chain intersecting families when p >= q.
- lemma: The candidate extremal construction F_q(i) is explicitly described in the source.
- lemma: The paper's proof toolkit includes the permutation method and circle-method style canonical-chain arguments.
- toy example: The neighboring solved benchmark is the exact totally (2,2) theorem with optimum size 2^(n-1).
- known obstruction: A proof route based on the source's general machinery may immediately extend beyond (3,2), making the branded slice unstable as a stand-alone micro-paper target.
- prior-work stop sentence: Current checked sources solve the totally (2,2) case and propose the general conjecture, but do not settle the totally (3,2) slice.
- recommended first attack: Test whether the paper's permutation-method inequalities specialize cleanly to q=2 and p=3 before attempting any wider generalization.
- paper if solved: If the slice remains isolated, the paper would be a short extremal-set-theory note proving the next concrete totally chain-intersecting case after (2,2).

## bounded_source_list
- Daniel Gerbner, "A note on strongly and totally chain intersecting families," Graphs and Combinatorics 41 (2025), especially Theorem 5 and Conjecture 6; bounded 2026 searches in this run surfaced the 2025 paper but no later exact all-n solution for the specialized totally (3,2) slice.
- The 2025 Graphs and Combinatorics article and bounded 2026 exact-statement search in this run.
- artifacts/totally-3-2-chain-intersecting/record.md
- artifacts/totally-3-2-chain-intersecting/status.json
