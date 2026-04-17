# Working Packet: On the (765,192,48) Difference-Set Problem in C_3 x C_255

- slug: `abelian-difference-set-765-192-48-group-3-255`
- title: abelian-difference-set-765-192-48-group-3-255
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `82`
- single-solve-to-paper fraction: `0.8`

## statement
Determine whether the abelian group C_3 x C_255 admits a (765,192,48)-difference set.

## novelty_notes
- frontier basis: Gordon-Schmidt 2016 Table 2 isolates the exact [3,255] row as open, and local attempt/source memory shows no conflicting prior run on this exact statement.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The source already provides the title-theorem statement, so a decisive proof or disproof would leave only light contextual framing and exposition.
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
- assessment: Lane-eligible. This is a unique exact-row residual case with low feeder risk and a clean short-note packet if solved.

## likely_paper_shape
- note title: On the (765,192,48) Difference-Set Problem in C_3 x C_255
- hypothetical title: On the (765,192,48) Difference-Set Problem in C_3 x C_255
- paper shape: A short exact-group residual-row note from the multiplier-conjecture survey.
- publication if solved: A proof of existence or nonexistence would settle the exact Table 2 row (765,192,48) in C_3 x C_255.
- minimal artifact requirements: A proof or disproof in C_3 x C_255, the decisive multiplier-orbit or quotient contradiction or construction, and a short account of why the row survived the published multiplier criteria.

## hypothetical_abstract
We determine whether the abelian group C_3 x C_255 admits a (765,192,48)-difference set. Gordon and Schmidt list this exact group row as open in Table 2 of their multiplier-conjecture survey. Because the row is already isolated at source level and no direct later settlement surfaced in the bounded status sweep, one exact solve would already form the core of a short publishable note.

## single_solve_explanation
This is already a paper-shaped exact theorem/result pair in a standard reference table. Solving it would supply the central theorem and most of the technical work. What remains would be a short introduction, notation setup, and proof cleanup.

## broader_theorem_nonimplication
The row remains explicitly listed after the survey's multiplier theorems and does not share the same parameters with another known exact group row in the final shortlist, so no broader result surfaced here that would make the honest title theorem substantially larger than this exact case.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing (765,192,48) in [3,255] as open; bounded exact and alternate-notation web sweeps on 2026-04-15 found no direct later settlement.

## transfer_kit
- lemma: Gordon-Schmidt 2016 isolate the exact [3,255] row in Table 2, fixing the target theorem.
- lemma: For (765,192,48), the order is n = 144 = 2^4 x 3^2, so the nontrivial multiplier pressure comes first from the prime 2 recorded against the row.
- lemma: The group C_3 x C_255 decomposes as C_3^2 x C_5 x C_17, giving immediate quotient maps to the 5- and 17-parts for orbit-size bookkeeping.
- toy example: Project a hypothetical difference set to the C_17 quotient and check whether a 2-multiplier-fixed orbit partition can realize total size 192.
- known obstruction: The published multiplier criteria do not already remove the row, so any proof must sharpen the orbit or quotient analysis beyond the tabulated filters.
- prior-work stop sentence: Gordon-Schmidt 2016 list (765,192,48) in group [3,255] as open in Table 2.
- recommended first attack: Exploit the C_3^2 x C_5 x C_17 decomposition and test whether 2-multiplier orbit sizes on the odd quotients are compatible with k = 192 and lambda = 48.
- paper if solved: If solved exactly, the paper would be a short residual-row note on the Table 2 case (765,192,48) in C_3 x C_255.

## bounded_source_list
- Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (765,192,48) in group [3,255].
- Gordon-Schmidt 2015/2016 Table 2, bounded exact-statement and alternate-notation web sweeps on 2026-04-15, and local attempt/source registry checks.
- artifacts/abelian-difference-set-765-192-48-group-3-255/record.md
- artifacts/abelian-difference-set-765-192-48-group-3-255/status.json
