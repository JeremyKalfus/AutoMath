# Working Packet: The Smallest Unattempted Open Abelian Biplane Row

- slug: `abelian-biplane-difference-set-1124921029-47433-2`
- title: abelian-biplane-difference-set-1124921029-47433-2
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `67`
- single-solve-to-paper fraction: `0.69`

## statement
Determine whether any abelian group of order 1124921029 admits a (1124921029,47433,2)-difference set.

## novelty_notes
- frontier basis: Gordon's Table 3 lists (1124921029,47433,2) among the surviving open abelian biplane parameters after Theorem 2, Theorem 4, and further Lander-based eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A direct solve would already remove a named residual biplane case and would need only bounded framing around the multiplier machinery, but the final note would still read as table cleanup rather than a naturally sharp micro-paper title theorem.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Credible and fresh, but not lane-eligible: it is an honest frontier residue with a compact literature gap, yet the branded result is still more residual-table cleanup than a self-standing title theorem.

## likely_paper_shape
- note title: The Smallest Unattempted Open Abelian Biplane Row
- hypothetical title: On the Abelian (1124921029,47433,2)-Difference Set Problem
- paper shape: A residual-case biplane note centered on the smallest currently unattempted Table 3 row, but still more cleanup-shaped than title-theorem-shaped.
- publication if solved: A proof of existence or nonexistence would delete the smallest unattempted row from Gordon's Table 3 of residual open abelian biplane cases.
- minimal artifact requirements: Either a compact arithmetic obstruction proving nonexistence in all abelian groups of order 1124921029 or a human-checkable existence certificate together with the multiplier-orbit explanation of why the case survived the standard filters.

## hypothetical_abstract
We determine whether any abelian group of order 1124921029 admits a (1124921029,47433,2)-difference set. Gordon's 2022 analysis leaves this tuple among the residual open abelian biplane cases after the standard multiplier and Lander-style eliminations. The result would remove the smallest currently unattempted Table 3 row, although the note would still need modest framing to explain the residual-case context.

## single_solve_explanation
A complete existence or nonexistence proof would carry essentially all of the mathematics for the eventual note, because the source already isolates the tuple as one of the residual open cases. What remains after the solve is bounded exposition: explain the Table 3 context, state why the published elimination machinery stops here, and present the decisive new obstruction or construction. That is close to paper-shaped, but still slightly too cleanup-driven for the strict micro-paper lane.

## broader_theorem_nonimplication
Gordon explicitly leaves this tuple in Table 3 after applying Theorem 2 and then using Lander's stronger design-theoretic tests on most survivors, so the standard broader abelian-biplane machinery cited in the source does not already settle it.

## literature_gap
Prior work stops at listing (1124921029,47433,2) as one of the remaining open abelian biplane cases in Table 3 of Gordon (2022).

## transfer_kit
- lemma: For lambda = 2, the biplane parameter relation gives v = k(k - 1)/2 + 1 and n = k - 2, fixing the exact tuple once k = 47433 is chosen.
- lemma: Gordon's Theorem 2 gives the basic multiplier-orbit contradiction framework over G = Z_p x H by forcing orbit counts a and b to satisfy three inequalities.
- lemma: Gordon's Theorem 4 promotes contracted multipliers on quotients G/H and was used as a key elimination tool for Table 3.
- lemma: Gordon states that most remaining Table 3 survivors were then attacked using Lander's Theorems 4.19 and 4.38, so any final proof must go beyond the standard fast filters.
- toy example: Use the classical abelian biplane parameter set (16,6,2) as the smallest nontrivial worked example of a lambda = 2 difference-set family member.
- known obstruction: The tuple already survives Gordon's published multiplier screen and the follow-up Lander-style eliminations, so any final contradiction must exploit finer orbit or quotient structure.
- prior-work stop sentence: Gordon (2022) still lists (1124921029,47433,2) as open in Table 3.
- recommended first attack: Factor v = 13693 x 82153, pick a prime divisor p of v, and try to force a Theorem 2 orbit-count contradiction from a multiplier coming from a prime divisor of n = 47431.
- paper if solved: If solved exactly, the paper would be a short residual-case note deleting the smallest currently unattempted row of Gordon's abelian biplane table.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda" (Journal of Algebraic Combinatorics 55, 2022), especially Table 3 and the elimination machinery in Theorems 2 and 4.
- Gordon 2022 for Table 3 and the multiplier pipeline, Hughes-Dickey as summarized there for earlier abelian biplane computations, and Lander's symmetric-design tests for surrounding eliminations.
- artifacts/abelian-biplane-difference-set-1124921029-47433-2/record.md
- artifacts/abelian-biplane-difference-set-1124921029-47433-2/status.json
