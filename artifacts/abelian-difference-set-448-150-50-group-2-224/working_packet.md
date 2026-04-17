# Working Packet: The [2,224] (448,150,50) Difference-Set Case

- slug: `abelian-difference-set-448-150-50-group-2-224`
- title: abelian-difference-set-448-150-50-group-2-224
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `71`
- single-solve-to-paper fraction: `0.68`

## statement
Determine whether the abelian group C_2 x C_224 admits a (448,150,50)-difference set.

## novelty_notes
- frontier basis: Gordon and Schmidt's survey Table 2 isolates the exact row (448,150,50) in group [2,224] after the survey's multiplier-based eliminations.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A direct solve would be close to a paper, but the later-status audit is too weak and the packet still needs more narrative support than the lead candidate.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: moderate
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: small
- assessment: Conservative backup only. The exact row is attractive, but the current packet is too thin on later-status support to justify a live solve slot.

## likely_paper_shape
- note title: The [2,224] (448,150,50) Difference-Set Case
- hypothetical title: On the (448,150,50) difference-set case in C_2 x C_224
- paper shape: A short exact-group note if the row is still genuinely open and the multiplier packet stays local.
- publication if solved: An exact result for the [2,224] row could support a short note, but the present packet is still too thin on later-status support and falls below the target paper fraction.
- minimal artifact requirements: A proof or disproof in C_2 x C_224, a multiplier-orbit or quotient argument exploiting the 2-primary and 7-primary structure, and a stronger later-status note.

## hypothetical_abstract
We determine whether the abelian group C_2 x C_224 admits a (448,150,50)-difference set. Gordon and Schmidt's survey of the multiplier conjecture isolates this exact row in Table 2 after their eliminations. A direct solution could still support a short note, but the present capped audit did not recover a strong independent later-status source for the row.

## single_solve_explanation
The exact group row is already well isolated, so a clean proof or disproof would still carry most of the mathematics for a short note. The problem is that the later-status and framing packet is thinner here than for the lead cyclic 990 candidate. Under the current cap, this stays as a conservative backup.

## broader_theorem_nonimplication
The survey table keeps [2,224] as an exact open row after its multiplier-based eliminations, so the statement is not already implied by the survey's general machinery. The present issue is not logical collapse but weak later-status confirmation under the capped search budget.

## literature_gap
Gordon and Schmidt's survey stops at listing the exact open row (448,150,50) in group [2,224], and the capped 2026-04-16 exact/survey search did not surface a later closure.

## transfer_kit
- lemma: Gordon and Schmidt's survey Table 2 explicitly lists the exact open row (448,150,50) in group [2,224].
- lemma: The row survives the survey's multiplier-based eliminations, so any remaining proof has to use sharper local structure than the survey already spends.
- lemma: The group splits as a 2-primary part times a 7-part, giving natural quotient maps for contracted coefficient counts.
- lemma: The parameter arithmetic n = k - lambda = 100 puts immediate pressure on multiplier behavior from the 2- and 5-parts.
- toy example: Project to the order-7 quotient and inspect whether the resulting seven fiber sizes can be made compatible with the difference-set equations and any multiplier normalization.
- known obstruction: The survey has already spent the routine multiplier eliminations, so a successful proof must exploit a sharper local incompatibility than the standard toolkit alone.
- prior-work stop sentence: Gordon and Schmidt stop at listing (448,150,50) in group [2,224] as an exact open Table 2 row.
- recommended first attack: Use the 7-quotient and the 2-primary decomposition of C_2 x C_224 to derive fiber-size equations that survive the survey's multiplier reductions.
- paper if solved: If solved exactly, the paper would be a short note closing the [2,224] row from Gordon and Schmidt's multiplier-conjecture table.

## bounded_source_list
- Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (Designs, Codes and Cryptography 78, 2016), especially Table 2 listing the exact open row (448,150,50) in group [2,224].
- Gordon-Schmidt 2016 Table 2, bounded exact-statement search for "448,150,50" difference set "2,224" and survey-title search for "Survey of the Multiplier Conjecture" "448,150,50" on 2026-04-16, and local attempt/source/paper/search memory.
- artifacts/abelian-difference-set-448-150-50-group-2-224/record.md
- artifacts/abelian-difference-set-448-150-50-group-2-224/status.json
