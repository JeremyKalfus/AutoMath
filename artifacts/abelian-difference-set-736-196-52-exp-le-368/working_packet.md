# Working Packet: The (736,196,52) difference-set problem for exponent at most 368

- slug: `abelian-difference-set-736-196-52-exp-le-368`
- title: Does any abelian group with exponent at most 368 admit a (736,196,52)-difference set?
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `68`
- single-solve-to-paper fraction: `0.7`

## statement
Determine whether any abelian group with exponent at most 368 admits a (736,196,52)-difference set.

## novelty_notes
- frontier basis: Gordon-Schmidt 2016 Table 2 isolates the exact exponent-bounded row (736,196,52) with exp(G) <= 368 among the small open multiplier-survey cases.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The source already isolates a bounded residual row, so a decisive solve would still leave a plausible short note. The main weakness is theorem-slice instability: the honest theorem may widen to a broader family statement rather than staying on the branded exp(G) <= 368 row.
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
- assessment: This is a source-anchored backup packet, not a strict lane survivor. The bounded family is still small and paper-shaped, but the honest theorem slice is too unclear to prioritize ahead of sharper exact-row packets.

## likely_paper_shape
- note title: The (736,196,52) difference-set problem for exponent at most 368
- hypothetical title: On the (736,196,52) difference-set problem for exponent at most 368
- paper shape: A short exponent-bounded residual-row note from the multiplier-conjecture survey.
- publication if solved: Closing the exponent-bounded row (736,196,52) with exp(G) <= 368 would likely support a short note, but more framing is needed than for a single exact-group row because the theorem is phrased over a bounded family.
- minimal artifact requirements: A proof or disproof for all abelian groups with exponent at most 368, together with the decisive structural reduction and a short explanation of why the row persists in Table 2.

## hypothetical_abstract
We determine whether any abelian group of exponent at most 368 admits a (736,196,52)-difference set. Gordon and Schmidt list this exact exponent-bounded row in Table 2 of their multiplier-conjecture survey among the smallest open cases. A decisive proof would likely support a short note, but the branded theorem slice is less stable than an exact-group row and therefore misses the strict lane.

## single_solve_explanation
Solving the row would likely provide the mathematical core of a short note because the source already isolates the residual exponent-bounded case. What remains after the solve is a bit more packaging than for a single-group row, since the theorem is phrased over a bounded family. That theorem-slice instability, rather than lack of paper shape, is why this packet is only a backup.

## broader_theorem_nonimplication
The canonical survey source still lists the exponent-bounded row as open, but the shortest honest proof may well broaden to a family statement, so the exact branded slice is not stable enough for the lane.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing the row (736,196,52) with exp(G) <= 368 as open.

## transfer_kit
- lemma: Gordon-Schmidt 2016 isolate the exact exponent-bounded row (736,196,52) with exp(G) <= 368 in Table 2.
- lemma: For (736,196,52), the order n = 144 = 2^4 * 3^2, so the 3-part multiplier information is the main first filter recorded against the row.
- lemma: Any abelian group of order 736 has the form 2-power part times C_23, and the exponent bound sharply limits the possible 2-primary structures.
- toy example: Begin with the maximal-exponent case C_16 x C_2 x C_23 and test whether multiplier-fixed orbit counts can realize k = 196 with lambda = 52.
- known obstruction: The survey machinery does not already remove the row, so any proof must exploit finer structural information inside the exponent-bounded family.
- prior-work stop sentence: Gordon-Schmidt 2016 list (736,196,52) with exp(G) <= 368 as open in Table 2.
- recommended first attack: Classify the allowed 2-primary group types under the exponent cap and try to rule them out uniformly using orbit counts on the 23-quotient.
- paper if solved: If solved exactly, the paper would be a short note closing the Table 2 exponent-bounded row (736,196,52), provided the proof does not honestly widen the theorem beyond the listed slice.

## bounded_source_list
- Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the open row (736,196,52) with exp(G) <= 368.
- Gordon-Schmidt 2016 Table 2 and the bounded 2026-04-15 shortlist audit that preserved this exponent-bounded row as a backup packet.
- artifacts/abelian-difference-set-736-196-52-exp-le-368/record.md
- artifacts/abelian-difference-set-736-196-52-exp-le-368/status.json
