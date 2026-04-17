# Working Packet: On the (783,391,195) Difference-Set Problem in C_3 x C_261

- slug: `abelian-difference-set-783-391-195-group-3-261`
- title: abelian-difference-set-783-391-195-group-3-261
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `83`
- single-solve-to-paper fraction: `0.82`

## statement
Determine whether the abelian group C_3 x C_261 admits a (783,391,195)-difference set.

## novelty_notes
- frontier basis: Gordon-Schmidt 2015 explicitly separate the known [3,3,87] row from the open [3,261] row at the same parameters, so solving the [3,261] case would settle an exact residual group-type question rather than a vague family fragment.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: One exact solve already yields the note: state the split status at v = 783, give the obstruction or construction for C_3 x C_261, and explain why the known [3,3,87] realization does not transfer.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: moderate
- exact gap from source: tiny
- assessment: Lane-eligible. The statement is exact, source-anchored, group-specific, and solving it would plausibly provide 80%+ of a short paper rather than a one-paragraph curiosity.

## likely_paper_shape
- note title: On the (783,391,195) Difference-Set Problem in C_3 x C_261
- hypothetical title: On the (783,391,195) Difference-Set Problem in C_3 x C_261
- paper shape: A short exact-group note separating the open [3,261] case from the known [3,3,87] case at the same parameters.
- publication if solved: A proof of existence or nonexistence would settle whether the exact abelian group C_3 x C_261 admits a (783,391,195)-difference set, despite the same parameters being realized in group type [3,3,87].
- minimal artifact requirements: A proof or disproof for C_3 x C_261, the orbit or quotient constraints used, and a short comparison with the known [3,3,87] realization.

## hypothetical_abstract
We determine whether the abelian group C_3 x C_261 admits a (783,391,195)-difference set. Gordon and Schmidt record the same parameters as known in group [3,3,87] but leave the exact group [3,261] open in Table 2 of their multiplier survey. A decisive construction or obstruction for C_3 x C_261 would therefore settle a clean residual group-type question and would already supply the main theorem of a short note.

## single_solve_explanation
This target is already paper-shaped before solving: the source supplies the exact open statement, the nearby known row gives the natural comparison theorem, and the theorem slice is stable under the likely proof routes. After the solve, little remains beyond packaging the argument, stating why [3,261] differs from [3,3,87], and writing a short literature-positioning paragraph.

## broader_theorem_nonimplication
The same parameters already occur in another abelian type, so a generic parameter-level existence or nonexistence theorem would not automatically settle the [3,261] row. The bounded later-source check did not surface any broader post-2015 theorem deciding the exact group C_3 x C_261.

## literature_gap
Prior work surfaced here stops at Gordon-Schmidt 2015, which lists (783,391,195) as known in group [3,3,87] but still open in group [3,261]; the bounded 2026-04-15 outside-source check found no later direct settlement of the [3,261] case.

## transfer_kit
- lemma: Gordon-Schmidt Table 2 isolates the exact open row (783,391,195) in group [3,261], so the honest theorem can stay group-specific.
- lemma: Gordon-Schmidt Table 1 records the same parameters in group [3,3,87] with comment TPP(27), showing that the issue is the precise abelian type rather than mere parameter feasibility.
- lemma: The survey's multiplier framework reduces any proof to orbit decompositions under the unresolved multiplier candidates listed for the row.
- lemma: The decomposition C_3 x C_261 is naturally compatible with 9-part and 29-part quotients, giving immediate contracted-count tests.
- toy example: Contract a hypothetical set to the 29-part quotient and compare the admissible orbit counts with the known [3,3,87] realization to see where the group-type obstruction first appears.
- known obstruction: Because the same parameters are already realized in a different abelian type, any proof for [3,261] must exploit exact group structure and cannot stop at parameter-level tests.
- prior-work stop sentence: Gordon-Schmidt list (783,391,195) as known in [3,3,87] but open in [3,261].
- recommended first attack: Exploit the C_3 x C_9 x C_29 decomposition and test whether the survey's multiplier-orbit constraints are compatible with any lift from the 29-part quotient to C_3 x C_261.
- paper if solved: If solved exactly, the paper would be a short note resolving the remaining v = 783 group-type split between the known [3,3,87] case and the open [3,261] case.

## bounded_source_list
- Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), especially Table 1 listing the known (783,391,195) row in group [3,3,87] and Table 2 listing the open row in group [3,261].
- Gordon-Schmidt 2015 Table 1 and Table 2, Gordon 2020 on small-lambda methods as a bounded later-source check, the current Dan Gordon difference-set index page, and local attempt-registry memory.
- artifacts/abelian-difference-set-783-391-195-group-3-261/record.md
- artifacts/abelian-difference-set-783-391-195-group-3-261/status.json
