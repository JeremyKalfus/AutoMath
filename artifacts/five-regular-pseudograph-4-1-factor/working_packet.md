# Working Packet: The {4,1}-Factor Problem for 5-Regular Pseudographs

- slug: `five-regular-pseudograph-4-1-factor`
- title: Does every 5-regular pseudograph contain a {4,1}-factor?
- publication status: `SLICE_CANDIDATE`
- packet quality: `excellent`
- micro-paper eligible: `True`
- paper leverage score: `91`
- single-solve-to-paper fraction: `0.86`

## statement
Resolve the exact 5-regular pseudograph case, either by proving every such pseudograph has a {4,1}-factor or by exhibiting a genuine counterexample.

## novelty_notes
- frontier basis: The 2015 source narrows the odd-degree landscape to this last 5-regular pseudograph residue after larger odd-degree failures.
- why still open: The 2015 paper explicitly leaves the r = 5, t = 1 case open after disproving the broader odd-r conjecture, and the bounded status sweep surfaced only summary material still pointing to the same residue.
- attempted conflict check: Repo exclusion sweep found no matching slug, title, or near-duplicate exact statement in failed_problems.json, queue.json, selected_problem.md, campaigns/, PROOFS.md, or artifact statuses.
- rediscovery risk: low-medium

## proof_sketch
- attack style: minimal-counterexample plus cut/parity analysis through the mod-3 edge-label reformulation
- likely route: A proof or counterexample would directly close the named low-degree residue and would already determine the title theorem and core proof section of the paper.
- verifier focus: For a positive solve, verify the spanning subgraph degrees directly; for a negative solve, preserve the exact counterexample and the argument excluding every {4,1}-factor.

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- search-heavy: False
- certificate compactness: high
- exact gap from source: small
- assessment: Pass: this is a named-conjecture residue with a strong title theorem, low editorial overhead, and a direct note narrative once solved.

## likely_paper_shape
- note title: The {4,1}-Factor Problem for 5-Regular Pseudographs
- hypothetical title: The {4,1}-Factor Problem for 5-Regular Pseudographs
- paper shape: One exact theorem or counterexample package, with a brief structural section around the mod-3 reformulation and a short obstruction discussion.
- publication if solved: A full resolution of the smallest unresolved Akbari-Kano-type odd-degree case would already read like a short standalone paper.
- minimal artifact requirements: Either a structural proof or a minimal counterexample, together with a tiny checker for the {4,1}-factor or the equivalent edge-labeling certificate.

## hypothetical_abstract
We settle the 5-regular pseudograph case of the Akbari-Kano {1,4}-factor problem. Using the mod-3 edge-label reformulation and a minimal-counterexample analysis, we either prove that every 5-regular pseudograph admits a {4,1}-factor or isolate a genuine minimal obstruction. This closes the smallest surviving odd-degree residue after the 2015 counterexamples and leaves only routine framing and formal sealing.

## single_solve_explanation
The source already supplies the broader conjectural frame and the negative larger-odd-degree background, so the remaining narrative is almost forced. Once the 5-regular residue is solved, the paper mainly needs a short introduction, the exact proof or obstruction, and one brief discussion of how the 2015 reformulation pinpoints the last odd-degree gap. No feeder ladder or second theorem program is needed.

## broader_theorem_nonimplication
The 2015 paper disproves the broader odd-r conjecture for larger odd degrees but explicitly isolates the 5-regular pseudograph case as the remaining residue; those broader counterexamples do not settle this exact low-degree endpoint.

## literature_gap
Prior work reaches the reformulation, proves counterexamples for larger odd r, and then stops with the exact 5-regular pseudograph {4,1}-factor case still open.

## transfer_kit
- lemma: Use the 2015 equivalence between a {4,1}-factor and an edge-labeling by {1,2} with every vertex-sum 0 modulo 3.
- lemma: The 2015 counterexamples for larger odd degrees mean any proof can focus on the isolated 5-regular residue rather than a broad odd-degree program.
- lemma: Minimal-counterexample reductions can stay local because the certificate is only degree bookkeeping on a spanning subgraph or its mod-3 label image.
- toy example: K_6 is a sanity-check model: deleting any perfect matching leaves a spanning 4-regular subgraph, so the positive certificate format is completely explicit on the smallest simple 5-regular graph.
- known obstruction: Naive induction on odd degree is false because larger odd-degree cases already admit counterexamples.
- prior-work stop sentence: After the broader odd-degree failures, prior work stops at the exact 5-regular pseudograph {4,1}-factor case.
- recommended first attack: Work in the mod-3 edge-label language and force a vertex-minimal counterexample to contain a reducible cut or parity configuration.
- paper if solved: The paper would be a one-theorem note closing the last low-degree odd residue, with the mod-3 reformulation as the short setup section.

## bounded_source_list
- Maria Axenovich and Jonathan Rollin, "Brooks type results for conflict-free colorings and {a,b}-factors in graphs" (Discrete Mathematics 338, 2015), plus Douglas West's regular-subgraph problem summary.
- The 2015 source, the mod-3 reformulation it records, and one bounded later-status check.
- artifacts/five-regular-pseudograph-4-1-factor/record.md
- artifacts/five-regular-pseudograph-4-1-factor/status.json
