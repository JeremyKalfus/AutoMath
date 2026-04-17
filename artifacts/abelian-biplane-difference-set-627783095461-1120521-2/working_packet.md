# Working Packet: A Larger Residual Abelian Biplane Table 3 Case

- slug: `abelian-biplane-difference-set-627783095461-1120521-2`
- title: abelian-biplane-difference-set-627783095461-1120521-2
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `55`
- single-solve-to-paper fraction: `0.61`

## statement
Determine whether any abelian group of order 627783095461 admits a (627783095461,1120521,2)-difference set.

## novelty_notes
- frontier basis: Gordon's Table 3 lists (627783095461,1120521,2) among the surviving open abelian biplane rows after the paper's elimination pipeline.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The solve would be real mathematical progress, but the resulting note would need heavier contextual framing and a less compact argument than a strict one-shot micro-paper target should require.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: weak
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: high
- immediate corollary headroom: none
- isolated exact-case risk: high
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: low
- exact gap from source: small
- assessment: Genuine frontier residue, but not lane-eligible because the exact theorem is too bulky and too cleanup-driven to be the title theorem of a sharp short note.

## likely_paper_shape
- note title: A Larger Residual Abelian Biplane Table 3 Case
- hypothetical title: On the Abelian (627783095461,1120521,2)-Difference Set Problem
- paper shape: A table-cleanup biplane note whose exact theorem is too large to serve as a strong micro-paper title.
- publication if solved: A proof of existence or nonexistence would settle a larger residual open row in Gordon's abelian biplane table.
- minimal artifact requirements: Either a broad nonexistence proof covering all abelian groups of order 627783095461 or a large explicit construction, together with the explanation of why existing multiplier filters stop short here.

## hypothetical_abstract
We determine whether any abelian group of order 627783095461 admits a (627783095461,1120521,2)-difference set. Gordon's 2022 Table 3 identifies this tuple as a residual open abelian biplane case after the standard multiplier-based elimination methods are exhausted. Solving it would be publishable residual-case progress, but the packet is too bulky to count as a strict micro-paper target.

## single_solve_explanation
A solve would still provide the core theorem and would therefore dominate the eventual note mathematically. The difficulty is publication shape, not novelty: the exact case is large enough that the paper would need more explanation about the table context, more justification for why this row matters, and probably a less compact proof artifact. That pushes the packet outside the 70-90 percent micro-paper zone.

## broader_theorem_nonimplication
The source explicitly leaves this row unresolved after its multiplier and quotient-multiplier arguments, so there is no surfaced broader theorem in Gordon's elimination framework that already settles it.

## literature_gap
Prior work stops at listing (627783095461,1120521,2) as an open Table 3 case in Gordon (2022).

## transfer_kit
- lemma: For lambda = 2, the exact parameter relation yields n = 1120519 and v = 627783095461.
- lemma: Theorem 2 in Gordon gives the orbit-count obstruction inequalities for suitable multipliers over decompositions G = Z_p x H.
- lemma: Theorem 4 gives the contracted-multiplier bound in cyclic quotients, one of the key tools cited in the Table 3 cleanup pipeline.
- lemma: Gordon notes that Lander's Theorems 4.19 and 4.38 remove many other survivors, isolating this tuple as a true residual case.
- toy example: Use the small known biplane difference-set case (16,6,2) as the canonical toy model of the lambda = 2 family.
- known obstruction: This row already survived the published fast elimination tools, so a final proof must exploit a finer multiplier pattern than the standard screens expose.
- prior-work stop sentence: Gordon (2022) still lists (627783095461,1120521,2) as open in Table 3.
- recommended first attack: Use the factorization v = 83059 x 7558279 to search for a prime-divisor choice with strong order conditions for a multiplier coming from n = 1120519, then push Theorem 2 or Theorem 4 to a contradiction.
- paper if solved: If solved exactly, the paper would be a residual-case abelian biplane note with material but bounded packaging.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda" (Journal of Algebraic Combinatorics 55, 2022), especially Table 3 and the elimination machinery in Theorems 2 and 4.
- Gordon 2022 and the abelian biplane references used there to eliminate nearby cases.
- artifacts/abelian-biplane-difference-set-627783095461-1120521-2/record.md
- artifacts/abelian-biplane-difference-set-627783095461-1120521-2/status.json
