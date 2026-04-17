# Working Packet: On the Cyclic (645,161,40) Difference-Set Problem

- slug: `cyclic-difference-set-645-161-40`
- title: Does the cyclic group C_645 admit a (645,161,40)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `81`
- single-solve-to-paper fraction: `0.78`

## statement
Determine whether the cyclic group C_645 admits a (645,161,40)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 Table 3 isolates the exact cyclic row (645,161,40) as one of the remaining possible cases with 150 <= k <= 300 and gcd(v,n)=1, and the bounded 2026-04-15 status sweep did not expose a later settlement.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The source already fixes the exact title theorem, the family anchor, and the stop line in the literature. After one decisive proof or disproof, the remaining work is mostly brief context and a comparison with the few sibling Table 3 rows.
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
- assessment: Best current lane survivor: exact row, stable theorem slice, strong family anchor, and a quiet enough novelty surface that one decisive solve would already supply most of a short note.

## likely_paper_shape
- note title: On the Cyclic (645,161,40) Difference-Set Problem
- hypothetical title: On the cyclic (645,161,40) difference-set problem
- paper shape: A short residual-case note closing one open Table 3 cyclic parameter row.
- publication if solved: Settling the exact cyclic row (645,161,40) would close one of the residual Table 3 cases and would already read like the title theorem of a short cleanup note in the cyclic difference-set lane.
- minimal artifact requirements: A proof or disproof for the cyclic group C_645, the decisive multiplier or contracted-residue argument, and a short explanation of why the standard Table 3 filters stop here.

## hypothetical_abstract
We determine whether the cyclic group C_645 admits a (645,161,40)-difference set. Baumert and Gordon list this exact tuple as one of the surviving Table 3 cyclic cases with 150 <= k <= 300 and gcd(v,n)=1 after their standard eliminations. A definitive existence or nonexistence proof would therefore close a precise residual case rather than contribute only an isolated curiosity.

## single_solve_explanation
This row is already source-anchored as a residual exact case, so the main theorem of the note is predetermined before any new work starts. One clean proof or disproof would do most of the mathematical work and most of the paper-shaping work at once. What remains after the solve is mainly a short literature recap and a comparison with neighboring Table 3 survivors.

## broader_theorem_nonimplication
The later multiplier-theorem surface explicitly advertises eliminations for some Table 3 rows, including (419,133,42) and (1123,154,21), but no surfaced broader theorem discharged (645,161,40); the tuple still behaves like an exact residual row rather than an already-implied corollary.

## literature_gap
Baumert-Gordon 2004 Table 3 lists the cyclic parameter row (645,161,40) as possible, and the bounded 2026-04-15 exact-tuple, alternate-notation, and Gordon-site searches surfaced no later direct settlement of that exact row.

## transfer_kit
- lemma: Baumert-Gordon 2004 Table 3 isolates (645,161,40) as a surviving cyclic case, so the target theorem is source-anchored and exact.
- lemma: Section 2 of Baumert-Gordon records the standard necessary conditions already used to cull nearby tuples, including the Mann and Arasu-style filters, so any new proof can start from a sharply reduced residual case.
- lemma: Theorem 3.1 in Baumert-Gordon gives contracted coefficient equations for each divisor w of v, and Theorem 3.2 supplies multiplier-orbit constraints that can force contradictions once a candidate multiplier is fixed.
- toy example: Contract a hypothetical set modulo 43 and modulo 15 and test whether the resulting coefficient vectors can satisfy the Table 3.1 equations with k = 161 and n = 121.
- known obstruction: The routine arithmetic filters already leave this tuple alive, so any proof must go beyond the stock Table 3 eliminations and use sharper multiplier or contraction bookkeeping.
- prior-work stop sentence: Baumert-Gordon 2004 Table 3 lists (645,161,40) as a remaining possible cyclic case, and the bounded 2026-04-15 search surfaced no later direct settlement.
- recommended first attack: Exploit the prime square order n = 121 to force an 11-multiplier orbit structure, then compare the induced orbit sizes with contracted residue counts modulo 43 and modulo 15.
- paper if solved: If solved exactly, the paper would be a short residual-case note closing the cyclic Table 3 row (645,161,40).

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the open cyclic row (645,161,40) among the possible cases with 150 <= k <= 300 and gcd(v,n)=1.
- Baumert-Gordon 2004 Table 3 and Sections 2-3, the later multiplier-theorem surface that explicitly eliminates some sibling rows, the Gordon web surface, and the local attempt and search registries.
- artifacts/cyclic-difference-set-645-161-40/record.md
- artifacts/cyclic-difference-set-645-161-40/status.json
