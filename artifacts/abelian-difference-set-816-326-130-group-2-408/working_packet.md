# Working Packet: On the (816,326,130) Difference-Set Problem in C_2 x C_408

- slug: `abelian-difference-set-816-326-130-group-2-408`
- title: abelian-difference-set-816-326-130-group-2-408
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `78`
- single-solve-to-paper fraction: `0.76`

## statement
Determine whether the abelian group C_2 x C_408 admits a (816,326,130)-difference set.

## novelty_notes
- frontier basis: Gordon-Schmidt 2016 Table 2 isolates the exact [2,408] row as open, and local attempt/source memory shows no prior run on this exact statement.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: One exact solve would directly resolve the row named in the survey table, so the post-solve workload is only light exposition and context.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible, though slightly less crisp than the top rows because the likely proof path looks more technical on the 2-primary side.

## likely_paper_shape
- note title: On the (816,326,130) Difference-Set Problem in C_2 x C_408
- hypothetical title: On the (816,326,130) Difference-Set Problem in C_2 x C_408
- paper shape: A short exact-group residual-row note from the multiplier-conjecture survey.
- publication if solved: A proof of existence or nonexistence would settle the exact Table 2 row (816,326,130) in C_2 x C_408.
- minimal artifact requirements: A proof or disproof in C_2 x C_408, the decisive quotient or orbit argument, and a short explanation of the surviving multiplier obstruction.

## hypothetical_abstract
We determine whether the abelian group C_2 x C_408 admits a (816,326,130)-difference set. Gordon and Schmidt list this exact row as open in Table 2 of their multiplier-conjecture survey. Because the theorem slice is already exact and the bounded status sweep found no direct later settlement, the solve itself would form the core of a short note.

## single_solve_explanation
The source table already isolates the exact group row, so a proof or disproof would carry most of the mathematical weight of the paper. What remains would be brief framing and proof presentation. No feeder ladder is needed.

## broader_theorem_nonimplication
The row survives the survey's general multiplier machinery and appears as its own exact group entry; no broader published theorem surfaced in the bounded audit that automatically settles C_2 x C_408.

## literature_gap
Prior work surfaced in this curation stops at Gordon-Schmidt 2016 Table 2 listing (816,326,130) in [2,408] as open; bounded exact and alternate-notation web sweeps on 2026-04-15 found no direct later settlement.

## transfer_kit
- lemma: Gordon-Schmidt 2016 isolate the exact [2,408] row in Table 2, fixing the target theorem.
- lemma: For (816,326,130), the order is n = 196 = 2^2 x 7^2, so the main multiplier pressure on the odd side comes from the prime 7.
- lemma: The group C_2 x C_408 decomposes as C_2 x C_8 x C_3 x C_17, giving natural projections to the odd quotients and the 2-primary component.
- toy example: Project to the C_17 quotient and test whether a 7-multiplier-fixed orbit partition can realize total size 326.
- known obstruction: The standard multiplier filters do not already kill the row, so a successful proof must sharpen orbit or quotient bookkeeping beyond the published table.
- prior-work stop sentence: Gordon-Schmidt 2016 list (816,326,130) in group [2,408] as open in Table 2.
- recommended first attack: Exploit the C_2 x C_8 x C_3 x C_17 decomposition and compare 7-multiplier orbit sizes with the allowed odd-quotient occupancies.
- paper if solved: If solved exactly, the paper would be a short residual-row note on the Table 2 case (816,326,130) in C_2 x C_408.

## bounded_source_list
- Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (816,326,130) in group [2,408].
- Gordon-Schmidt 2015/2016 Table 2, bounded exact-statement and alternate-notation web sweeps on 2026-04-15, and local attempt/source registry checks.
- artifacts/abelian-difference-set-816-326-130-group-2-408/record.md
- artifacts/abelian-difference-set-816-326-130-group-2-408/status.json
