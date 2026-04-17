# Working Packet: On the Cyclic (1093,169,26) Difference-Set Problem

- slug: `cyclic-difference-set-1093-169-26`
- title: Does the cyclic group C_1093 admit a (1093,169,26)-difference set?
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `77`
- single-solve-to-paper fraction: `0.74`

## statement
Determine whether the cyclic group C_1093 admits a (1093,169,26)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 Table 3 lists the exact cyclic row (1093,169,26) as open, and the bounded 2026-04-15 later-source sweep did not reveal a direct discharge.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The exact statement is already fixed by the source table and already reads like the title theorem of a short note. After a solve, only concise framing and comparison to the remaining Table 3 survivors would be left.
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
- assessment: Clean second lane candidate: exact row, quiet novelty surface, and a prime-order ambient group that keeps the paper packet tight.

## likely_paper_shape
- note title: On the Cyclic (1093,169,26) Difference-Set Problem
- hypothetical title: On the cyclic (1093,169,26) difference-set problem
- paper shape: A short residual-case note closing one open Table 3 cyclic parameter row.
- publication if solved: Settling the exact cyclic row (1093,169,26) would likely yield a short residual-case note because the source already isolates the title theorem and the family anchor.
- minimal artifact requirements: A proof or disproof for C_1093, the decisive multiplier or cyclotomic argument, and a short explanation of why the standard Table 3 eliminations stop short of this row.

## hypothetical_abstract
We determine whether the cyclic group C_1093 admits a (1093,169,26)-difference set. Baumert and Gordon isolate this tuple in Table 3 as one of the remaining cyclic possibilities with 150 <= k <= 300 and gcd(v,n)=1. A decisive proof would close an exact residual case with only light post-solve exposition remaining.

## single_solve_explanation
The statement is already paper-shaped before any new mathematics begins because the source table singles it out as an exact survivor. A one-pass proof would contribute both the central theorem and most of the eventual narrative. What would remain after the solve is only a compact explanation of how this row sits among the few surviving cyclic tuples.

## broader_theorem_nonimplication
No surfaced later theorem settled (1093,169,26) as a corollary of a broader cyclic classification result; the later multiplier-theorem surface that explicitly advertises sibling eliminations did not expose this tuple as already resolved.

## literature_gap
Baumert-Gordon 2004 Table 3 lists the cyclic parameter row (1093,169,26) as possible, and the bounded 2026-04-15 exact-tuple, alternate-notation, and Gordon-site searches surfaced no later direct settlement of that exact row.

## transfer_kit
- lemma: Baumert-Gordon 2004 Table 3 isolates (1093,169,26) as a surviving cyclic case.
- lemma: Section 2 of Baumert-Gordon records the standard necessary conditions already exhausted on neighboring tuples, so the remaining task is inherently a residual-case argument rather than a full fresh census.
- lemma: Theorem 3.1 and Theorem 3.2 in Baumert-Gordon provide contracted coefficient identities and multiplier-orbit constraints that are directly reusable in a row-specific proof.
- toy example: Because 1093 is prime, model a putative set by the orbit partition of nonzero residues under a candidate multiplier coming from n = 143 = 11 * 13 and test whether the orbit sizes can sum to k = 169.
- known obstruction: The stock arithmetic tests already fail to eliminate this tuple, so any proof must sharpen the multiplier or cyclotomic residue analysis beyond the published table construction.
- prior-work stop sentence: Baumert-Gordon 2004 Table 3 lists (1093,169,26) as a remaining possible cyclic case, and the bounded 2026-04-15 search surfaced no later direct settlement.
- recommended first attack: Exploit the prime-order ambient group and force 11- and 13-multiplier orbit structures on F_1093^x, then compare the allowed orbit partitions with k = 169 and lambda = 26.
- paper if solved: If solved exactly, the paper would be a short note closing the Table 3 cyclic row (1093,169,26).

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the open cyclic row (1093,169,26) among the possible cases with 150 <= k <= 300 and gcd(v,n)=1.
- Baumert-Gordon 2004 Table 3 and Sections 2-3, the later multiplier-theorem surface on sibling rows, the Gordon web surface, and the local attempt and search registries.
- artifacts/cyclic-difference-set-1093-169-26/record.md
- artifacts/cyclic-difference-set-1093-169-26/status.json
