# Working Packet: On the (729,273,102) Difference-Set Problem for Exponent at Most 27

- slug: `abelian-difference-set-729-273-102-exp-le-27`
- title: abelian-difference-set-729-273-102-exp-le-27
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `70`
- single-solve-to-paper fraction: `0.71`

## statement
Determine whether any abelian group with exponent at most 27 admits a (729,273,102)-difference set.

## novelty_notes
- frontier basis: Gordon-Schmidt 2016 Table 2 isolates the exact exponent-bounded row, and local attempt memory shows no prior run on this canonical problem key.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A decisive solve would still be close to paper-shaped, but some framing work would be needed to explain the exponent-bounded slice rather than an exact group row.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: unclear
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Reasonable backup packet with a strong source anchor, but theorem-slice stability is too unclear for the strict micro-paper lane.

## likely_paper_shape
- note title: On the (729,273,102) Difference-Set Problem for Exponent at Most 27
- hypothetical title: On the (729,273,102) Difference-Set Problem for Exponent at Most 27
- paper shape: A short exponent-bounded residual-row note from the multiplier-conjecture survey.
- publication if solved: A proof of existence or nonexistence would settle the exact Table 2 exponent-bounded row (729,273,102) with exp(G) <= 27.
- minimal artifact requirements: A proof or disproof for all abelian groups with exponent at most 27, together with the decisive structural reduction and explanation of why the row remains in Table 2.

## hypothetical_abstract
We determine whether any abelian group of exponent at most 27 admits a (729,273,102)-difference set. Gordon and Schmidt isolate this exact exponent-bounded row in Table 2 of their multiplier-conjecture survey. A decisive proof would likely support a short note, but the slice is less stable than an exact-group row because the honest theorem could broaden during the proof.

## single_solve_explanation
One exact solve would still do much of the mathematical work of a short paper because the source isolates a small residual slice. What remains after the solve would be a bit more framing than for an exact group row, since the theorem is stated over an exponent-bounded family rather than one group. That instability is why the packet fails the strict lane despite being source-anchored and plausibly publishable.

## broader_theorem_nonimplication
The survey itself lists the exponent-bounded slice as open, but a shortest proof could plausibly widen into a broader statement about abelian 3-groups, so the theorem slice is not stable enough for the strict lane.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing the row (729,273,102) with exp(G) <= 27 as open.

## transfer_kit
- lemma: Gordon-Schmidt 2016 isolate the exact exponent-bounded row (729,273,102) with exp(G) <= 27 in Table 2.
- lemma: For (729,273,102), the order n = 171 = 3^2 * 19, and Table 2 records the multiplier-conjecture prime data attached to the row.
- lemma: Any abelian group of order 729 and exponent at most 27 is a 3-group with limited invariant-factor types, giving a bounded structural case split.
- toy example: Start with the maximal-exponent candidate C_27 x C_27 and test whether the recorded multiplier information can be made compatible with k = 273 and lambda = 102.
- known obstruction: The survey's general multiplier results do not already eliminate the row, so any proof must use sharper structural or quotient bookkeeping inside the exponent-bounded family.
- prior-work stop sentence: Gordon-Schmidt 2016 list (729,273,102) with exp(G) <= 27 as open in Table 2.
- recommended first attack: Enumerate the invariant-factor types of abelian groups of order 729 and exponent at most 27 and try to exclude each type by a common orbit-count or quotient argument.
- paper if solved: If solved exactly, the paper would be a short note closing the Table 2 exponent-bounded row (729,273,102), provided the proof does not widen the honest theorem too much.

## bounded_source_list
- Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the open row (729,273,102) with exp(G) <= 27.
- Gordon-Schmidt 2016 Table 2 and local attempt-registry memory.
- artifacts/abelian-difference-set-729-273-102-exp-le-27/record.md
- artifacts/abelian-difference-set-729-273-102-exp-le-27/status.json
