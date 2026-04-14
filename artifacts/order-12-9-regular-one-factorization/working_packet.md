# Working Packet: One-Factorizations of 9-Regular Graphs of Order 12

- slug: `order-12-9-regular-one-factorization`
- title: Is every 9-regular graph on 12 vertices one-factorizable?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `False`
- paper leverage score: `78`
- single-solve-to-paper fraction: `0.79`

## statement
Either prove that all 9-regular graphs on 12 vertices are one-factorizable or isolate an exact counterexample among the nine base graphs left by the canonical source.

## novelty_notes
- frontier basis: The canonical 2005 paper explicitly leaves degrees 7, 8, and 9 open for order 12 and records that the degree-9 slice is reduced to nine nonisomorphic base graphs.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath mathematical attempt, slug conflict, or near-duplicate for the exact order-12 degree-9 one-factorization slice.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved exactly, the title theorem, table format, and verifier are all predetermined, leaving mostly proof cleanup and a short explanation of the residue.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Borderline park: the residue is tiny and paper-shaped, but the current bounded audit leaves too much later-status ambiguity to grant a fully clean micro-paper pass.

## likely_paper_shape
- note title: One-Factorizations of 9-Regular Graphs of Order 12
- hypothetical title: One-Factorizations of 9-Regular Graphs of Order 12
- paper shape: A fixed-order exact classification note with a table of the remaining degree-9 graphs, factorization verdicts, and a short structural discussion.
- publication if solved: A complete degree-9 classification on order 12 would already be a short exact-classification paper because the source literature singles out this finite slice.
- minimal artifact requirements: An explicit factorization table for the remaining degree-9 graphs or a complete obstruction argument for a minimal exception, together with a small perfect-matching decomposition checker.

## hypothetical_abstract
We settle the smallest unresolved high-degree slice in the order-12 one-factorization classification by determining the 9-regular case. Using complement heuristics, perfect-matching structure, and bounded finite verification, we either prove that each remaining 9-regular graph on 12 vertices is one-factorizable or isolate a minimal exception. The paper shape is real, but the current bounded literature sweep still leaves enough rediscovery ambiguity to keep this slice just below the strict micro-paper lane.

## single_solve_explanation
If the finite degree-9 residue were settled, the note would already be nearly complete: the theorem statement is fixed, the finite table is small, and the verifier is straightforward. The reason it is not front-ranked is not paper shape but bounded novelty uncertainty after noisy later order-12 enumeration metadata. One more careful status refresh could move it back into the lane.

## broader_theorem_nonimplication
The canonical source isolates the order-12 degree-9 residue rather than deriving it from a stronger theorem, but later enumeration metadata around order-12 one-factorization is noisy enough that a stricter novelty check is still needed before treating the slice as fully clean.

## literature_gap
The canonical 2005 source classifies the order-12 cases r <= 6 and r = 10,11 and leaves the degree-9 slice unresolved after reducing it to nine nonisomorphic base graphs.

## transfer_kit
- lemma: The canonical 2005 classification leaves only nine nonisomorphic base graphs in the order-12 degree-9 residue.
- lemma: Complement and perfect-matching heuristics reduce the live work to a tiny finite list of exact factorization certificates.
- lemma: A positive certificate is explicit: a one-factorization is just a decomposition into perfect matchings that can be checked mechanically and read by hand.
- toy example: The resolved low-degree and very-high-degree order-12 cases in the 2005 paper give the exact model for the final classification-table format.
- known obstruction: Later order-12 census metadata is noisy enough that rediscovery risk is not yet fully extinguished without a stricter dedicated audit.
- prior-work stop sentence: The canonical 2005 paper leaves the degree-9 order-12 slice unresolved after reducing it to nine nonisomorphic base graphs.
- recommended first attack: Exploit complements and near-complete-graph structure first, and only then verify explicit perfect-matching decompositions on the remaining finite list.
- paper if solved: The paper would be a short finite-classification note built around one theorem, one nine-row verdict table, and a tiny checker.

## bounded_source_list
- Petteri Kaski and Patric R. J. Ostergard, "One-Factorizations of Regular Graphs of Order 12" (Electronic Journal of Combinatorics 12, 2005).
- Kaski-Ostergard 2005 together with bounded later-status checks against order-12 one-factorization and related census literature.
- artifacts/order-12-9-regular-one-factorization/record.md
- artifacts/order-12-9-regular-one-factorization/status.json
