# Working Packet: The Biplane of Order 14

- slug: `biplane-121-16-2`
- title: Does a biplane with parameters (121,16,2) exist?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `False`
- paper leverage score: `76`
- single-solve-to-paper fraction: `0.9`

## statement
Either construct a symmetric 2-(121,16,2) design or prove nonexistence.

## novelty_notes
- frontier basis: The 2020 automorphism-group paper explicitly states that the existence of a biplane with parameters (121,16,2) is open and pushes automorphism restrictions further.
- why still open: (not recorded)
- attempted conflict check: The current exclusion sweep found no prior mathematical attempt, slug conflict, or near-duplicate for the exact (121,16,2) biplane existence question.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The title and theorem are fixed in advance, and a certified design or certified obstruction would leave almost no packaging tax.
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
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Park: very strong paper leverage, but the live route appears too search-heavy and orbit-matrix-driven to qualify as a clean micro-paper target right now.

## likely_paper_shape
- note title: The Biplane of Order 14
- hypothetical title: The Biplane of Order 14
- paper shape: A single exact existence paper or exact nonexistence paper for one canonical design parameter set.
- publication if solved: An existence or nonexistence theorem for the order-14 biplane would immediately be a standalone design-theory paper.
- minimal artifact requirements: Either a complete incidence matrix for a symmetric 2-(121,16,2) design or a complete obstruction chain excluding all candidates.

## hypothetical_abstract
We resolve the existence question for a biplane with parameters (121,16,2), the classical order-14 case. Using structural restrictions on automorphisms and orbit matrices, we either construct a design or prove that no such design exists. The paper narrative is immediate, but the current likely route still appears too computational for the strict micro-paper lane.

## single_solve_explanation
If the existence status were settled, the paper would already be essentially written: one theorem, one certificate, and a short account of the structural restrictions used. The problem is downranked only because the anticipated route still looks computationally bulky, not because the publication packet is weak. The solve itself would provide almost all of the eventual note.

## broader_theorem_nonimplication
Current structural theorems restrict automorphism groups of a hypothetical design but do not imply existence or nonexistence of the full (121,16,2) biplane.

## literature_gap
The 2020 paper sharpens automorphism restrictions for a hypothetical biplane with parameters (121,16,2) and still states that existence remains open.

## transfer_kit
- lemma: A biplane with parameters (121,16,2) is a symmetric 2-design, so any positive certificate is a compact incidence structure with exact pair-count verification.
- lemma: The 2020 source proves that a hypothetical automorphism group has heavily restricted order and excludes automorphisms of orders 11 and 13.
- lemma: The same source analyzes possible actions of automorphisms of orders 5 and 7, giving ready-made orbit-structure constraints.
- toy example: The small known biplanes provide the model certificate format: an incidence matrix with exact pair counts and symmetry checks.
- known obstruction: Orbit-matrix case splits can explode, and a nonexistence proof may become a large computation rather than a short structural argument.
- prior-work stop sentence: The 2020 automorphism-group paper states that the existence of a biplane with parameters (121,16,2) is still open.
- recommended first attack: Push the restricted automorphism cases to exhaustion and then test whether the remaining automorphism-free or low-symmetry residue can be ruled out structurally.
- paper if solved: The paper would be a short exact-design note on the order-14 biplane, built around one construction or one obstruction theorem.

## bounded_source_list
- D. Crnković, D. Dumičić Danilović, and S. Rukavina, "On automorphism groups of a biplane (121,16,2)" (2020).
- The 2020 automorphism-group paper, standard biplane background, and bounded later-status checks.
- artifacts/biplane-121-16-2/record.md
- artifacts/biplane-121-16-2/status.json
