# Working Packet: The Cyclic (2869,240,20) Difference-Set Case

- slug: `cyclic-difference-set-2869-240-20`
- title: cyclic-difference-set-2869-240-20
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `79`
- single-solve-to-paper fraction: `0.75`

## statement
Determine whether the cyclic group C_2869 admits a (2869,240,20)-difference set.

## novelty_notes
- frontier basis: Baumert-Gordon 2004 Table 3 isolates (2869,240,20) as an exact surviving cyclic row with gcd(v,n) = 1, and bounded 2026-04-15 exact-row and alternate-notation searches surfaced no direct later settlement.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A direct solution would already settle the advertised row and leave only short source placement and proof exposition.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Usable lane survivor. The case is exact and source-anchored, with a plausible one-shot route to a short residual-case paper.

## likely_paper_shape
- note title: The Cyclic (2869,240,20) Difference-Set Case
- hypothetical title: On the cyclic (2869,240,20) difference-set problem
- paper shape: An exact Table 3 residual-case note driven by a compact multiplier-orbit or contraction obstruction.
- publication if solved: Settling the cyclic (2869,240,20) row would plausibly support a short exact-case note closing one of the Baumert-Gordon Table 3 survivors.
- minimal artifact requirements: A proof or disproof for C_2869, the decisive contracted-coefficient or multiplier-orbit contradiction, and a short note positioning the row among the surviving Table 3 cases.

## hypothetical_abstract
We determine whether the cyclic group C_2869 admits a (2869,240,20)-difference set. Baumert and Gordon isolate this tuple in Table 3 among the remaining cyclic cases with 150 <= k <= 300 and gcd(v,n) = 1. A direct solution would settle an exact residual row and supply the main contribution of a short note.

## single_solve_explanation
The literature already packages the row as an exact survivor, so a clean proof or disproof is most of the publishable object. What remains after the solve is mainly concise framing inside Table 3 and a short explanation of the method. That keeps the solve-to-paper distance inside the intended micro-paper band.

## broader_theorem_nonimplication
The source row survives the standard small-parameter screens, and the bounded exact-row plus alternate-notation searches on 2026-04-15 did not surface a later theorem explicitly settling (2869,240,20).

## literature_gap
Baumert-Gordon 2004 stops at listing (2869,240,20) as a remaining cyclic Table 3 case, and the bounded 2026-04-15 follow-up surfaced no direct later settlement of the exact tuple.

## transfer_kit
- lemma: Baumert-Gordon 2004 Table 3 isolates (2869,240,20) as an exact surviving cyclic row with gcd(v,n) = 1.
- lemma: Section 2 records the necessary conditions already exhausted before the tuple reaches Table 3.
- lemma: Theorem 3.1 gives the contracted coefficient equations for every divisor w of v.
- lemma: Theorem 3.2 gives multiplier-orbit equalities whenever the prime powers of n = 220 generate a common residue modulo a divisor of v.
- toy example: Try contraction modulo w = 41 or w = 69 and test whether the Theorem 3.1 count equations are compatible with orbits forced by 2-, 5-, or 11-power multipliers from n = 220.
- known obstruction: The easy cyclic filters are already exhausted in the source table, so any nonexistence proof has to exploit a sharper contraction or multiplier orbit pattern.
- prior-work stop sentence: Baumert-Gordon 2004 stops at listing (2869,240,20) as a remaining possible cyclic case in Table 3.
- recommended first attack: Search for a divisor of 2869 where powers of 2, 5, or 11 induce a useful w-multiplier, then intersect the orbit equalities with the contracted-count equations from Theorem 3.1.
- paper if solved: If solved exactly, the paper would be a short residual-case note on the cyclic Table 3 row (2869,240,20).

## bounded_source_list
- Leonard D. Baumert and Daniel M. Gordon, "On the existence of cyclic difference sets with small parameters" (Fields Institute Communications 41, 2004), especially Table 3 listing the exact cyclic row (2869,240,20) among the possible cases with 150 <= k <= 300 and gcd(v,n) = 1.
- Baumert-Gordon 2004 Table 3 and Sections 2-3, bounded exact-row and alternate-notation web searches on 2026-04-15, family-level status checks against the Baumert-Gordon citation surface and Gordon's difference-set web presence, and the local attempt registry.
- artifacts/cyclic-difference-set-2869-240-20/record.md
- artifacts/cyclic-difference-set-2869-240-20/status.json
