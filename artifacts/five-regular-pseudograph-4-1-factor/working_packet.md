# Working Packet: The {4,1}-Factor Problem for 5-Regular Pseudographs

- slug: `five-regular-pseudograph-4-1-factor`
- title: Does every 5-regular pseudograph contain a {4,1}-factor?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `91`
- single-solve-to-paper fraction: `0.86`

## statement
Either prove that every 5-regular pseudograph contains a {4,1}-factor or construct a genuine counterexample.

## novelty_notes
- frontier basis: The 2015 source disproves the broader odd-degree conjecture for larger odd degrees and explicitly leaves the 5-regular pseudograph case open as the smallest surviving residue.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath mathematical attempt, slug conflict, or near-duplicate for the exact 5-regular pseudograph {4,1}-factor statement.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The introduction, theorem statement, and verifier are already forced by the literature; after the solve, little remains beyond exposition of the mod-3 reformulation and proof cleanup.
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
- exact gap from source: small
- assessment: Pass: exact residue, stable theorem surface, low editorial overhead, and a direct short-note narrative if solved.

## likely_paper_shape
- note title: The {4,1}-Factor Problem for 5-Regular Pseudographs
- hypothetical title: The {4,1}-Factor Problem for 5-Regular Pseudographs
- paper shape: One exact theorem or one exact counterexample package for the last low-degree odd residue of the {1,4}-factor problem on pseudographs.
- publication if solved: A full resolution of the exact 5-regular pseudograph residue would already be the title theorem of a short standalone note.
- minimal artifact requirements: Either a structural proof or a genuine counterexample, together with a tiny checker for the {4,1}-factor or the equivalent mod-3 edge-label certificate.

## hypothetical_abstract
We settle the 5-regular pseudograph case of the Akbari-Kano {1,4}-factor problem. Using the mod-3 edge-label reformulation and a minimal-counterexample analysis, we either prove that every 5-regular pseudograph admits a {4,1}-factor or isolate a genuine minimal obstruction. This closes the smallest surviving odd-degree residue after the known higher-odd-degree failures and leaves only routine framing and verification.

## single_solve_explanation
The source literature already fixes the frame: higher odd degrees fail, and the 5-regular pseudograph case is the exact low-degree residue. Once that residue is solved, the rest of the paper is basically forced: state the mod-3 reformulation, give the proof or counterexample, and position it against the 2015 boundary. No feeder ladder or campaign-building remains.

## broader_theorem_nonimplication
The broader odd-r conjecture is already false in larger odd degrees, so the remaining 5-regular pseudograph endpoint is not implied by a stronger general theorem; it survives precisely because the known counterexamples do not settle this smallest odd case.

## literature_gap
Prior work reaches the mod-3 reformulation, proves failures for larger odd degrees, and then stops with the exact 5-regular pseudograph {4,1}-factor case still open.

## transfer_kit
- lemma: Use the 2015 equivalence between a {4,1}-factor and an edge-labeling by {1,2} with every vertex-sum 0 modulo 3.
- lemma: The larger odd-degree conjecture already fails, so any proof can focus on the isolated 5-regular residue rather than a broad odd-degree program.
- lemma: Minimal-counterexample reductions stay local because the certificate is only degree bookkeeping on a spanning subgraph or its mod-3 label image.
- toy example: K_6 is the sanity-check model: deleting any perfect matching leaves a spanning 4-regular subgraph, so the positive certificate format is completely explicit on the smallest simple 5-regular graph.
- known obstruction: Naive induction on odd degree is false because larger odd-degree cases already admit counterexamples.
- prior-work stop sentence: After the broader odd-degree failures, prior work stops at the exact 5-regular pseudograph {4,1}-factor case.
- recommended first attack: Work in the mod-3 edge-label language and force a vertex-minimal counterexample to contain a reducible cut or parity configuration.
- paper if solved: The paper would be a one-theorem note closing the last low-degree odd residue, with the mod-3 reformulation as the short setup section.

## bounded_source_list
- Maria Axenovich and Jonathan Rollin, "Brooks type results for conflict-free colorings and {a,b}-factors in graphs" (Discrete Mathematics 338, 2015), together with Douglas West's regular-subgraph problem summary.
- Axenovich-Rollin 2015, the mod-3 reformulation used there, West's regular-subgraph summary, and bounded later-status checks.
- artifacts/five-regular-pseudograph-4-1-factor/record.md
- artifacts/five-regular-pseudograph-4-1-factor/status.json
