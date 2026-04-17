# Working Packet: The Cyclic (1785,224,28) Difference-Set Case

- slug: `cyclic-difference-set-1785-224-28`
- title: cyclic-difference-set-1785-224-28
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `84`
- single-solve-to-paper fraction: `0.8`

## statement
Determine whether the cyclic group C_1785 admits a (1785,224,28)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 Table 2 isolates (1785,224,28) as an exact surviving cyclic case with gcd(v,n) > 1, and bounded 2026-04-15 exact-row and alternate-notation searches surfaced no direct later settlement.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A solution would already close the exact row, supply the title theorem, and leave only short framing around Ryser's conjecture and the Baumert-Gordon elimination pipeline.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Best current slot. The case is exact, source-anchored, unattempted locally, and a clean solve would already read like the title theorem of a short residual-case note.

## likely_paper_shape
- note title: The Cyclic (1785,224,28) Difference-Set Case
- hypothetical title: On the cyclic (1785,224,28) difference-set problem
- paper shape: An exact residual-case note closing a named Table 2 Ryser-conjecture row by a contracted-multiplier or contraction contradiction.
- publication if solved: Settling the cyclic (1785,224,28) row would plausibly yield a short note closing one exact Ryser-conjecture survivor from the Baumert-Gordon table.
- minimal artifact requirements: A proof or disproof for C_1785, the decisive contracted-count or multiplier-orbit contradiction, and a short writeup placing the row inside Table 2 as a Ryser-conjecture survivor.

## hypothetical_abstract
We determine whether the cyclic group C_1785 admits a (1785,224,28)-difference set. Baumert and Gordon isolate this tuple in Table 2 as one of the remaining cyclic cases with 150 <= k <= 300 and gcd(v,n) > 1. A direct proof of existence or nonexistence would settle an exact Ryser-conjecture survivor and already furnish the main theorem of a short note.

## single_solve_explanation
This target is already paper-shaped because the exact row is source-exposed and has a built-in family anchor through Ryser's conjecture. If the case is settled cleanly, the note mainly needs a brief literature setup, the decisive argument, and a short discussion of why this row survived earlier screens. No feeder ladder or secondary theorem program is needed for the paper to exist.

## broader_theorem_nonimplication
The source table is explicitly the post-screen residue after standard necessary conditions, and bounded exact-row plus alternate-notation searches on 2026-04-15 did not surface any later theorem explicitly disposing of (1785,224,28).

## literature_gap
Baumert-Gordon 2004 stops at listing (1785,224,28) as a remaining cyclic Table 2 case, and the bounded 2026-04-15 follow-up surfaced no direct later settlement of that exact tuple.

## transfer_kit
- lemma: Baumert-Gordon 2004 Table 2 isolates (1785,224,28) as an exact surviving cyclic row with gcd(v,n) > 1.
- lemma: Section 2 records the standard necessary conditions already exhausted before the tuple reaches Table 2.
- lemma: Theorem 3.1 gives the contracted coefficient equations for every divisor w of v.
- lemma: Theorem 3.2 gives multiplier-orbit equalities whenever the prime powers of n = 196 generate a common residue modulo a divisor of v.
- toy example: Work modulo w = 255 or w = 357 and test whether the Theorem 3.1 contracted counts can coexist with orbit equalities forced by a 2- or 7-power multiplier from n = 196.
- known obstruction: The standard cyclic necessary conditions have already been spent in the source table, so only sharper contraction or multiplier structure can still kill the row.
- prior-work stop sentence: Baumert-Gordon 2004 stops at listing (1785,224,28) as a remaining possible cyclic case in Table 2.
- recommended first attack: Choose a divisor w of 1785 where powers of 2 or 7 collapse to a useful w-multiplier, then combine orbit equalities with the contracted-count equations from Theorem 3.1.
- paper if solved: If solved exactly, the paper would be a short residual-case note on the cyclic Table 2 row (1785,224,28).

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 2 listing the exact cyclic row (1785,224,28) among the possible cases with 150 <= k <= 300 and gcd(v,n) > 1.
- Baumert-Gordon 2004 Table 2 and Sections 2-3, bounded exact-row and alternate-notation web searches on 2026-04-15, family-level status checks against the Baumert-Gordon citation surface and Gordon's difference-set web presence, and the local attempt registry.
- artifacts/cyclic-difference-set-1785-224-28/record.md
- artifacts/cyclic-difference-set-1785-224-28/status.json
