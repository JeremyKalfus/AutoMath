# Working Packet: On the (847,423,211) Difference-Set Problem in C_11 x C_77

- slug: `abelian-difference-set-847-423-211-group-11-77`
- title: abelian-difference-set-847-423-211-group-11-77
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `74`
- single-solve-to-paper fraction: `0.74`

## statement
Determine whether the abelian group C_11 x C_77 admits a (847,423,211)-difference set.

## novelty_notes
- frontier basis: Gordon-Schmidt 2015 Table 2 lists the row (847,423,211) in group [11,77] as open, and the bounded exact-tuple web sweep on 2026-04-15 surfaced no later direct settlement.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The source already isolates one exact group row, so a clean existence or nonexistence proof would itself supply the central theorem and most of the note.
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
- assessment: Lane-eligible. The solve would close an exact survey row in a specific group, and that one theorem already looks like the body of a short note.

## likely_paper_shape
- note title: On the (847,423,211) Difference-Set Problem in C_11 x C_77
- hypothetical title: On the (847,423,211) Difference-Set Problem in C_11 x C_77
- paper shape: A short exact-group obstruction/existence note for one named Table 2 survivor.
- publication if solved: A proof of existence or nonexistence would settle the exact Table 2 row (847,423,211) in the noncyclic group C_11 x C_77.
- minimal artifact requirements: A compact proof in C_11 x C_77, the relevant orbit or quotient bookkeeping, and a short explanation of why the survey row remained open.

## hypothetical_abstract
We determine whether the abelian group C_11 x C_77 admits a (847,423,211)-difference set. Gordon and Schmidt list this exact group-specific row as open in Table 2 of their multiplier-conjecture survey. A proof would close one named survivor in a canonical residual table and would leave only light contextual exposition after the mathematics is done.

## single_solve_explanation
This target is already a one-row theorem packet rather than a feeder instance. If solved, the exact theorem would naturally become the title theorem, with the remaining writing limited to source context, notation, and a short comparison with the survey table. The family anchor is strong enough that the result would read as more than an isolated curiosity.

## broader_theorem_nonimplication
The bounded audit surfaced the exact row as still open in Gordon-Schmidt's Table 2, and the theorem slice is tied to the noncyclic group [11,77] rather than a broader ambient class already shown settled in the surfaced literature.

## literature_gap
Prior work surfaced in this audit stops at listing the exact group-specific row (847,423,211) in [11,77] as open in Table 2 of Gordon-Schmidt 2015; the bounded exact-tuple search on 2026-04-15 surfaced no later direct settlement.

## transfer_kit
- lemma: Gordon-Schmidt's multiplier-survey toolkit reduces exact open rows by forcing numerical multipliers and then analyzing orbit structure in the ambient group.
- lemma: Any translate fixed by a multiplier subgroup can be written as a union of its orbits, so orbit lengths in C_11 x C_77 become immediate size constraints on a putative difference set.
- lemma: The Table 2 row exposes the group type [11,77], so quotienting to the 11-part and 7-part factors gives a small number of structurally distinguished projections.
- toy example: Work first with orbit counts for a smaller multiplier action on C_11 x C_7 to see how a union-of-orbits obstruction can force the wrong total size.
- known obstruction: The row already survives the survey's existing multiplier and standard necessary-condition filters, so any proof must exploit sharper orbit bookkeeping than the generic table machinery alone.
- prior-work stop sentence: Gordon-Schmidt list (847,423,211) in group [11,77] as open in Table 2.
- recommended first attack: Translate a putative set so that a maximal surfaced multiplier subgroup fixes it, then test whether the resulting orbit partition on C_11 x C_77 can realize size 423 and the required difference multiplicities.
- paper if solved: If solved exactly, the paper would be a short note closing the Table 2 row (847,423,211) in C_11 x C_77.

## bounded_source_list
- Daniel M. Gordon and Bernhard Schmidt, "A Survey of the Multiplier Conjecture" (2015), especially Table 2 listing the exact open row (847,423,211) in group [11,77].
- Gordon-Schmidt 2015 Table 2, the Dan Gordon difference-set repository landing page, and the bounded exact-tuple web sweep on 2026-04-15.
- artifacts/abelian-difference-set-847-423-211-group-11-77/record.md
- artifacts/abelian-difference-set-847-423-211-group-11-77/status.json
