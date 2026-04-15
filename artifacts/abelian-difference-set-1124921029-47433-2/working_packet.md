# Working Packet: The First Residual Abelian Biplane Case in Gordon's Table 3

- slug: `abelian-difference-set-1124921029-47433-2`
- title: abelian-difference-set-1124921029-47433-2
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `66`
- single-solve-to-paper fraction: `0.71`

## statement
Determine whether any abelian group of order 1124921029 admits a (1124921029,47433,2)-difference set.

## novelty_notes
- frontier basis: Table 3 begins with (1124921029,47433,2) after the source's multiplier-based biplane eliminations and contracted-multiplier discussion.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If this case is settled, the source already supplies the finite residual frontier and the elimination background. The note would mainly explain why this first remaining biplane case finally falls.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: low
- exact gap from source: tiny
- assessment: Paper-shaped but not lane-eligible for the current micro-paper objective. The exact solve would likely make a note, yet the parameter size and low single-pass proof plausibility push closability below the preferred lane.

## likely_paper_shape
- note title: The First Residual Abelian Biplane Case in Gordon's Table 3
- hypothetical title: On Abelian (1124921029,47433,2)-Difference Sets
- paper shape: A one-theorem note on the first residual biplane parameter in Table 3, if the exact existence question is closed.
- publication if solved: A construction or nonexistence proof for an abelian (1124921029,47433,2)-difference set would plausibly support a short note settling the first listed residual biplane case from Gordon's Table 3.
- minimal artifact requirements: Either an explicit abelian group of order 1124921029 carrying a (1124921029,47433,2)-difference set, or a compact group-uniform nonexistence proof.

## hypothetical_abstract
We determine the existence status of abelian difference sets with parameters (1124921029,47433,2). Gordon's Table 3 isolates this tuple as the first remaining open biplane case after the source's orbit-count and multiplier-based eliminations. A resolution would therefore produce a clean residual-case note, although the parameter size makes the solve itself comparatively hard.

## single_solve_explanation
Because the source already isolates this tuple as the first surviving biplane parameter, an exact solve would immediately give a recognizable title theorem. The remaining paper work would be limited to restating the Table 3 frontier and presenting the decisive argument. The difficulty is closability, not paper shape.

## broader_theorem_nonimplication
The source explicitly retains this tuple in Table 3 after its biplane-specific eliminations. That means the current published theory does not already decide it.

## literature_gap
Gordon's Table 3 leaves (1124921029,47433,2) as the first remaining open abelian lambda = 2 case for k <= 10^10.

## transfer_kit
- lemma: Theorem 2 gives the core orbit-count obstruction template.
- lemma: Theorem 4 is highlighted in the source as an important tool for biplane eliminations via quotient multipliers.
- lemma: The biplane discussion explains that Table 3 records the remaining open lambda = 2 cases after the source's eliminations.
- lemma: The source notes that Hughes and Dickey had already ruled out all abelian lambda = 2 cases of order below 5000 except the classical known ones.
- toy example: The source's short proof of nonexistence for (352,27,2) is the template example for a compact biplane obstruction.
- known obstruction: This tuple survives the current multiplier-orbit and contracted-multiplier eliminations, so a successful proof needs a sharper structural or arithmetic obstruction than the source currently provides.
- prior-work stop sentence: Gordon's Table 3 still lists (1124921029,47433,2) as the first remaining open abelian lambda = 2 case.
- recommended first attack: Exploit the factorization v = 13693 x 82153 and n = 47431 to force a stronger multiplier-orbit decomposition than the source uses, with special attention to quotient multipliers in cyclic or near-cyclic group types.
- paper if solved: If solved exactly, the paper would be a note removing the first residual biplane parameter from Gordon's Table 3.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda," Journal of Algebraic Combinatorics 55 (2022), especially the biplane discussion on page 6 and Table 3 on page 6, which lists the remaining open abelian (v,k,2)-difference-set parameter sets for k <= 10^10.
- Gordon (2022), especially the biplane section and Table 3, together with the Hughes and Dickey computations cited there.
- artifacts/abelian-difference-set-1124921029-47433-2/record.md
- artifacts/abelian-difference-set-1124921029-47433-2/status.json
