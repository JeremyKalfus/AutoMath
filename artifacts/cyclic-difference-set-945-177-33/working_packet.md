# Working Packet: The Cyclic (945,177,33) Difference-Set Case

- slug: `cyclic-difference-set-945-177-33`
- title: cyclic-difference-set-945-177-33
- publication status: `REDISCOVERY`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `18`
- single-solve-to-paper fraction: `0.15`

## statement
Determine whether the cyclic group C_945 admits a (945,177,33)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon Table 2 originally isolated (945,177,33) as a residual cyclic row.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: Historically the row was paper-shaped, but it is no longer frontier-open.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: weak
- family anchor strength: strong
- publication narrative strength: weak
- editorial overhead: high
- immediate corollary headroom: none
- isolated exact-case risk: high
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Fails the lane as a rediscovery. Keep only as an audited negative control.

## likely_paper_shape
- note title: The Cyclic (945,177,33) Difference-Set Case
- hypothetical title: On the cyclic (945,177,33) difference-set case
- paper shape: Would have been a short residual-case note, but the row is now a rediscovery.
- publication if solved: A direct solution would have been paper-shaped when Baumert-Gordon listed the row, but later literature has already closed it.
- minimal artifact requirements: None for live solve; the useful artifact is only the rediscovery note preventing reruns.

## hypothetical_abstract
Baumert and Gordon list the cyclic parameter row (945,177,33) as a residual Table 2 case. However, a bounded 2026-04-16 outside-source exact-tuple search surfaced Tao Feng's paper 'Nonexistence of Some (945,177,33)-difference Sets' in Ars Combinatoria 94 (2010). This row is therefore unsuitable for the live micro-paper lane because the exact claim is already settled.

## single_solve_explanation
When first isolated in Table 2, one clean solve would have been most of a short note. That is no longer relevant because the exact statement has already been handled in later literature. The only value now is as a do-not-recur memory entry.

## broader_theorem_nonimplication
Baumert-Gordon did not settle the row, but Tao Feng later did so directly in a dedicated nonexistence paper.

## literature_gap
There is no remaining literature gap for the exact tuple: Feng 2010 appears to close the case after Baumert-Gordon.

## transfer_kit
- lemma: Baumert-Gordon Table 2 isolates (945,177,33) as a residual cyclic row in the 2004 source.
- lemma: Section 2 records the standard necessary conditions already exhausted before the row survives to Table 2.
- lemma: Theorem 3.1 gives the contracted coefficient equations that would have underpinned a short proof or disproof.
- lemma: Theorem 3.2 gives the contracted multiplier equalities relevant to the 945 case.
- toy example: Contract a hypothetical 177-set modulo 35 or 45 and compare the resulting coefficient vector with the orbit sizes forced by powers of 2 and 3 from n = 144.
- known obstruction: The easy arithmetic tests were already exhausted in the source, and later literature appears to finish the row entirely.
- prior-work stop sentence: Baumert and Gordon stop at listing (945,177,33) as a remaining possible cyclic case in Table 2, but Tao Feng later appears to prove nonexistence.
- recommended first attack: No live attack recommended; archive the row as a rediscovery instead.
- paper if solved: Historically this would have been a short note closing one Table 2 row, but it is no longer a frontier target.

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 2 listing the exact cyclic row (945,177,33) among the possible cases with 150 <= k <= 300 and gcd(v,n) > 1.
- Baumert-Gordon 2004 Table 2, bounded exact-tuple web probes on 2026-04-16, and the surfaced later paper by Tao Feng listed in Ars Combinatoria volume 94 (2010).
- artifacts/cyclic-difference-set-945-177-33/record.md
- artifacts/cyclic-difference-set-945-177-33/status.json
