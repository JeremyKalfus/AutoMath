# Working Packet: The Cyclic (465,145,45) Difference-Set Problem

- slug: `cyclic-difference-set-465-145-45`
- title: cyclic-difference-set-465-145-45
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `88`
- single-solve-to-paper fraction: `0.84`

## statement
Determine whether the cyclic group C_465 admits a (465,145,45)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 leaves (465,145,45) as one of only two open cyclic cases with k <= 150, and Gordon-Schmidt 2015 still lists [465] among the smallest open difference-set parameters.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: One exact solution would remove a canonical residual case with cheap rediscovery surface and would need only a short introduction explaining the prior necessary-condition pipeline.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Lane-eligible. This is a small, stable, source-anchored residual theorem whose exact resolution would itself be the paper.

## likely_paper_shape
- note title: The Cyclic (465,145,45) Difference-Set Problem
- hypothetical title: On Cyclic (465,145,45) Difference Sets
- paper shape: A short cyclic-difference-set note whose title theorem is exactly the resolution of the (465,145,45) case.
- publication if solved: A proof of existence or nonexistence would settle one of the two residual cyclic difference-set cases left open by Baumert-Gordon for k <= 150 and still listed as open in Gordon-Schmidt's 2015 status table.
- minimal artifact requirements: A human-checkable existence construction in C_465 or a compact nonexistence proof using multiplier, orbit, or cyclotomic congruence arguments, together with a brief audit that the standard published tests did not already exclude the case.

## hypothetical_abstract
We determine whether the cyclic group of order 465 admits a (465,145,45)-difference set. Baumert and Gordon left this parameter among the final two open cyclic cases with k <= 150, and Gordon and Schmidt still listed it as open in their 2015 multiplier survey. The result therefore closes a canonical residual case in the small-parameter cyclic difference-set literature with only light contextual packaging.

## single_solve_explanation
The literature already isolates this tuple as a named residual case, so an exact proof would supply essentially all of the mathematics of the paper. What remains after the solve is bounded exposition: restate the old elimination pipeline, explain why those tests stop at 465, and present the decisive new argument. That is comfortably inside the 70-90% micro-paper band.

## broader_theorem_nonimplication
The 2004 paper eliminates four of the six k <= 150 cyclic survivors using the standard Schutzenberger, BRC, Yamamoto, Lander, Mann, and cyclotomic filters, yet leaves (465,145,45) open; the 2015 survey still records [465] as open, so no broader published theorem surfaced in this audit that already settles the exact cyclic case.

## literature_gap
Prior work stops at listing C_465 with parameters (465,145,45) as an unresolved cyclic difference-set case in Baumert-Gordon 2004 and Gordon-Schmidt 2015.

## transfer_kit
- lemma: For any difference set, the parameter identity (v - 1)lambda = k(k - 1) fixes the tuple and prevents silent statement drift.
- lemma: Baumert-Gordon 2004 use the standard cyclic necessary-condition package: Schutzenberger, Bruck-Chowla-Ryser, Yamamoto, Mann, and Lander-style tests.
- lemma: Their Section 3 records the contracted-coefficient equations for theta[w](x), giving the sum, square-sum, and correlation constraints for any divisor w of v.
- lemma: Gordon-Schmidt 2015 organize multiplier-theorem tools for residual open cases and identify the relevant prime divisors of n that a successful proof would likely have to force as multipliers or obstruct as nonmultipliers.
- toy example: Use the classical cyclic (7,3,1)-difference set in C_7 to illustrate how a cyclic difference set is encoded by a short polynomial theta(x) and then reduced modulo divisors w of v.
- known obstruction: The standard published small-parameter filters already failed to eliminate (465,145,45), so any final proof must go beyond the stock table-building tests.
- prior-work stop sentence: Baumert and Gordon leave (465,145,45) open in Table 1, and Gordon-Schmidt still list [465] as open in Table 2 of their 2015 survey.
- recommended first attack: Try to force a new multiplier in C_465 from the prime divisors of n = 100, then run the contracted-multiplier orbit equations at a divisor w of 465 to show that no admissible coefficient vector can exist.
- paper if solved: If solved exactly, the paper would be a short note settling one of the last tiny cyclic small-parameter cases that survived the classical necessary-condition program.

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 1 listing the two remaining open cyclic cases with k <= 150; status rechecked against Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), Table 2.
- Baumert-Gordon 2004 for the residual source table and standard cyclic tests; Gordon-Schmidt 2015 for later open-status confirmation and multiplier-theorem context; the La Jolla Difference Set Repository only as a status cross-check surface.
- artifacts/cyclic-difference-set-465-145-45/record.md
- artifacts/cyclic-difference-set-465-145-45/status.json
