# Working Packet: On the (621,156,39) Difference-Set Problem in C_3 x C_207

- slug: `abelian-difference-set-621-156-39-group-3-207`
- title: Does the abelian group C_3 x C_207 admit a (621,156,39)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `79`
- single-solve-to-paper fraction: `0.77`

## statement
Determine whether the abelian group C_3 x C_207 admits a (621,156,39)-difference set.

## novelty_notes
- frontier basis: Gordon-Schmidt 2016 Table 2 still isolates the exact [3,207] row as open after the survey's multiplier-based eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The source already supplies the exact title theorem, the literature stop line, and the family anchor. After a solve, what remains is mostly concise exposition of the decisive orbit or quotient contradiction and brief placement against Table 2.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible. This is a stable exact theorem slice with a clear family anchor, low editorial overhead, and a solve-to-publication distance short enough for the strict micro-paper lane.

## likely_paper_shape
- note title: On the (621,156,39) Difference-Set Problem in C_3 x C_207
- hypothetical title: On the nonexistence of a (621,156,39) difference set in C_3 x C_207
- paper shape: A short exact-group residual-row note from the multiplier-conjecture survey.
- publication if solved: A proof of existence or nonexistence would settle the exact Table 2 row (621,156,39) in C_3 x C_207 and would already read like the title theorem of a short residual-row note.
- minimal artifact requirements: A proof or disproof in C_3 x C_207, the decisive quotient-orbit argument, and a short explanation of why the row survives the published Table 2 filters.

## hypothetical_abstract
We determine whether the abelian group C_3 x C_207 admits a (621,156,39)-difference set. Gordon and Schmidt isolate this exact row in Table 2 of their multiplier-conjecture survey. A decisive proof would remove a named residual case with only light post-solve framing left.

## single_solve_explanation
The exact row is already isolated in the source literature, so the theorem statement does not need to be invented after the solve. One clean existence or nonexistence argument would therefore carry most of the mathematics and most of the paper narrative. What would remain is a short introduction, the proof writeup, and a brief comparison with the survey filters.

## broader_theorem_nonimplication
The bounded audit surfaced no broader published theorem that already removes the exact [3,207] group row; Gordon-Schmidt still lists it separately in Table 2, and the later web surface did not expose a newer discharge.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing the exact row (621,156,39) in group [3,207] as open; the bounded 2026-04-15 exact-tuple and alternate-notation sweep surfaced no later direct settlement.

## transfer_kit
- lemma: Gordon-Schmidt 2016 isolate the exact group row [3,207] in Table 2, so the intended theorem is already source-anchored.
- lemma: For (621,156,39), the order is n = 117 = 3^2 * 13, and Table 2 records 13 as the natural multiplier-conjecture prime for the row.
- lemma: The decomposition C_3 x C_207 = C_3^3 x C_23 gives immediate 3-part and 23-part quotient tests for multiplier-fixed orbit counts.
- toy example: Project to the C_23 quotient and test whether a 13-multiplier-fixed orbit partition can sum to 156 while respecting the lambda = 39 difference counts.
- known obstruction: The row already survives the survey's standard multiplier machinery, so any proof must sharpen the quotient or orbit bookkeeping beyond Table 2.
- prior-work stop sentence: Gordon-Schmidt 2016 list (621,156,39) in group [3,207] as open in Table 2.
- recommended first attack: Exploit the C_3^3 x C_23 decomposition and test whether the recorded 13-multiplier information forces an orbit partition incompatible with total size 156 and lambda = 39.
- paper if solved: If solved exactly, the paper would be a short residual-row note on the Table 2 case (621,156,39) in C_3 x C_207.

## bounded_source_list
- Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (621,156,39) in group [3,207].
- Gordon-Schmidt 2016 Table 2, Gordon's current publications page, Gordon's current La Jolla repository page, the local attempt registry, and bounded exact-tuple plus alternate-notation searches on 2026-04-15.
- artifacts/abelian-difference-set-621-156-39-group-3-207/record.md
- artifacts/abelian-difference-set-621-156-39-group-3-207/status.json
