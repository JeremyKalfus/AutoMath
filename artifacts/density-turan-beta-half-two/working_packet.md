# Working Packet: The Half-Set Density Threshold in Triangle-Free Graphs

- slug: `density-turan-beta-half-two`
- title: Is beta(1/2,2) equal to 1/50 in the density version of Turan's theorem?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.78`

## statement
Either prove that every triangle-free graph with all n/2-subsets inducing more than n^2/50 edges contains a triangle, or construct a sharper triangle-free extremal family showing that 1/50 is not the correct threshold.

## novelty_notes
- frontier basis: West's page records the exact conjecture beta(1/2,2) = 1/50 and notes the matching lower-bound construction via blowups of C_5 or the Petersen graph.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no prior AutoMath mathematical attempt, slug conflict, or near-duplicate for the exact constant beta(1/2,2) = 1/50.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The paper architecture is fixed in advance: define beta(alpha,2), recall the standard lower bound, and prove the exact upper bound or produce a sharper construction.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: moderate
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Pass, but less crisp than the K_9 decomposition exception: the target is exact and paper-shaped, though the proof could lean on heavier extremal machinery than the final note length suggests.

## likely_paper_shape
- note title: The Half-Set Density Threshold in Triangle-Free Graphs
- hypothetical title: The Half-Set Density Threshold in Triangle-Free Graphs
- paper shape: A single sharp threshold theorem for one named local-density extremal constant.
- publication if solved: Resolving the Erdos-Faudree-Rousseau-Schelp half-set threshold exactly would already be the title theorem of a short extremal graph note.
- minimal artifact requirements: Either a sharp upper-bound proof with a stability argument or a new triangle-free construction beating the 1/50 benchmark.

## hypothetical_abstract
We resolve the Erdos-Faudree-Rousseau-Schelp problem asking whether beta(1/2,2) equals 1/50. We either prove that 1/50 is the sharp half-set density threshold forcing a triangle or exhibit a triangle-free extremal construction with a strictly larger value. Since the lower-bound family and the exact conjectural constant are already fixed in the literature, the solve itself would provide the main theorem and most of the note.

## single_solve_explanation
This candidate already has a crisp title theorem and an obvious paper packet: one exact constant, one lower-bound construction, and one sharp upper bound or counterexample. The argument may use broader extremal tools, but the honest headline remains the half-set threshold because that exact constant is the published target. After the solve, what remains is mostly contextual framing and sharpening the extremal discussion.

## broader_theorem_nonimplication
The published background provides lower bounds and general inequalities for beta(alpha,r), but the exact half-set triangle-free constant beta(1/2,2) is explicitly posed as an open problem rather than a corollary of a broader theorem.

## literature_gap
The canonical source records the lower bound beta(1/2,2) >= 1/50 from blowups of C_5 or the Petersen graph and leaves the matching upper bound open.

## transfer_kit
- lemma: The lower bound beta(1/2,2) >= 1/50 comes from balanced blowups of C_5 and also from the Petersen graph construction highlighted on the canonical problem page.
- lemma: The problem is already isolated at one exact parameter pair alpha = 1/2, r = 2, so the theorem statement does not depend on resolving the whole beta(alpha,r) landscape.
- lemma: Any sharp result naturally packages with a stability discussion around the known lower-bound examples.
- toy example: Balanced blowups of C_5 provide the standard model example: they are triangle-free and witness the 1/50 lower bound on half-set induced density.
- known obstruction: The known lower-bound constructions are highly symmetric and locally dense on large subsets, so naive averaging arguments do not force triangles at the conjectured threshold.
- prior-work stop sentence: The published problem record gives the lower bound beta(1/2,2) >= 1/50 and stops before proving the matching upper bound.
- recommended first attack: Use a stability-first extremal approach centered on near blowups of C_5 or Petersen-type examples, then convert the structural control into a sharp half-set upper bound.
- paper if solved: The paper would be a short sharp-threshold extremal note built around one exact constant, one extremal family section, and one proof section.

## bounded_source_list
- Douglas West, "Density Version of Turan's Theorem" problem page, summarizing Erdos, Faudree, Rousseau, and Schelp's 1990 conjecture that beta(1/2,2) = 1/50.
- The 1990 EFRS problem as summarized by West, exact-statement and alternate-notation searches for beta(1/2,2), and bounded later-status checks for a settled sharp constant.
- artifacts/density-turan-beta-half-two/record.md
- artifacts/density-turan-beta-half-two/status.json
