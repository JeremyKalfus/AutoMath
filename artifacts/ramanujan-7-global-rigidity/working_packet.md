# Working Packet: Global Rigidity of 7-Regular Ramanujan Graphs

- slug: `ramanujan-7-global-rigidity`
- title: Is every 7-regular Ramanujan graph globally rigid in R^2?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `80`
- single-solve-to-paper fraction: `0.77`

## statement
Either prove that every 7-regular Ramanujan graph is globally rigid in R^2 or exhibit a 7-regular Ramanujan graph that is not globally rigid in R^2.

## novelty_notes
- frontier basis: Cioaba-Dewar-Grasegger-Gu prove all sufficiently large 7-regular Ramanujan graphs are globally rigid and record that the all-orders statement remains open only through finitely many small orders.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath slug, title, source anchor, or near-duplicate attempt for the exact k = 7 Ramanujan global-rigidity question.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The asymptotic theorem, motivation, and finite-reduction observation are already published; after the solve, the paper mostly needs the residue analysis or the counterexample.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Pass, though less clean than the top three entries: the theorem slice is stable and near-paper, but the residue likely needs certified computation rather than a purely conceptual proof.

## likely_paper_shape
- note title: Global Rigidity of 7-Regular Ramanujan Graphs
- hypothetical title: Global Rigidity of 7-Regular Ramanujan Graphs
- paper shape: A finite-residue completion note combining the 2023 asymptotic theorem with exact treatment of the unresolved 7-regular small orders.
- publication if solved: Closing the k = 7 case would settle one of the two remaining open degrees in the exact-all-orders Ramanujan global-rigidity question and would make a credible short note.
- minimal artifact requirements: Either a full argument or certified computation showing every 7-regular Ramanujan graph of orders 16, 18, and 20 is globally rigid, or one explicit non-globally-rigid 7-regular Ramanujan counterexample.

## hypothetical_abstract
We settle the remaining exact-degree question for planar global rigidity of 7-regular Ramanujan graphs. A 2023 theorem proved the statement for sufficiently large order and reduced the unresolved residue to finitely many small orders; we complete that residue analysis. This determines whether every 7-regular Ramanujan graph is globally rigid in R^2.

## single_solve_explanation
The current literature already contains the asymptotic theorem and the finite-reduction observation. If the small orders all work, the note is a finite-residue completion paper; if one fails, the note is a compact counterexample paper. In both cases, the one exact solve contributes most of the final paper.

## broader_theorem_nonimplication
The 2023 theorem proves the statement only for sufficiently large order and explicitly says the exact all-orders k = 7 case still requires checking the 16-, 18-, and 20-vertex residues.

## literature_gap
The literature proves all sufficiently large 7-regular Ramanujan graphs are globally rigid in R^2 but does not settle the all-orders statement because the small orders 16, 18, and 20 remain unresolved.

## transfer_kit
- lemma: The 2023 paper proves every 7-regular Ramanujan graph with more than 22 vertices is globally rigid in R^2.
- lemma: Its open-problems section records that any 7-regular counterexample must have more than 14 vertices and that only orders 16, 18, and 20 remain to be checked.
- lemma: The paper already supplies the spectral and connectivity machinery linking the Ramanujan bound to global rigidity.
- toy example: The already-checked orders up to 14 provide the smallest verified side of the finite residue and indicate how a certification argument is expected to look.
- known obstruction: The remaining burden may collapse into explicit finite enumeration of 7-regular Ramanujan graphs at three small orders rather than a new structural theorem.
- prior-work stop sentence: The 2023 Ramanujan rigidity paper stops with the exact k = 7 all-orders case unresolved and notes that only the 16-, 18-, and 20-vertex residues remain.
- recommended first attack: Exploit the paper's finite-reduction observation directly and certify the 16-, 18-, and 20-vertex cases one order at a time, using structural pruning before any exhaustive generation.
- paper if solved: The paper would be a short finite-residue completion note for the exact k = 7 Ramanujan global-rigidity problem.

## bounded_source_list
- Sebastian M. Cioaba, Sean Dewar, Georg Grasegger, and Xiaofeng Gu, "Graph Rigidity Properties of Ramanujan Graphs" (Electronic Journal of Combinatorics 30(3), 2023).
- The 2023 Ramanujan rigidity paper, 2026-04-13 exact-statement and alternate-notation searches for the k = 7 problem, the source's Section 6 open-problem discussion, and bounded 2024-2026 status searches that did not surface a completed k = 7 resolution.
- artifacts/ramanujan-7-global-rigidity/record.md
- artifacts/ramanujan-7-global-rigidity/status.json
