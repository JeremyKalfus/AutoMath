# Working Packet: On the Abelian (4797048929975,3793567,3) Difference-Set Problem

- slug: `abelian-difference-set-4797048929975-3793567-3`
- title: abelian-difference-set-4797048929975-3793567-3
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `63`
- single-solve-to-paper fraction: `0.71`

## statement
Determine whether any abelian group of order 4797048929975 admits a (4797048929975,3793567,3)-difference set.

## novelty_notes
- frontier basis: Gordon 2022 Table 4 leaves the exact parameter set (4797048929975,3793567,3) among the six surviving abelian lambda = 3 cases, and the local attempt registry shows no prior run on this tuple.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A clean exact solve would still remove one of Gordon's named residual Table 4 cases, but the parameter size raises novelty-check and packaging caution compared with the smaller Table 2 exact-group rows.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: moderate
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: moderate
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: moderate
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: low
- exact gap from source: small
- assessment: A legitimate residual-case packet, but clearly weaker than the smaller exact-group rows for the strict micro-paper lane.

## likely_paper_shape
- note title: On the Abelian (4797048929975,3793567,3) Difference-Set Problem
- hypothetical title: On the Abelian (4797048929975,3793567,3) Difference-Set Problem
- paper shape: A residual abelian lambda = 3 note from Gordon's six surviving Table 4 cases.
- publication if solved: A proof of existence or nonexistence would settle one of the six remaining abelian (v,k,3) parameter sets in Gordon 2022 Table 4.
- minimal artifact requirements: A proof or disproof for the abelian order 4797048929975 case together with the prime-quotient or multiplier constraints used and a short explanation of how the argument goes beyond Gordon's eliminations.

## hypothetical_abstract
We determine whether any abelian group of order 4797048929975 admits a (4797048929975,3793567,3)-difference set. Gordon isolates this exact tuple among the six surviving abelian lambda = 3 cases in Table 4 of his 2022 paper. A decisive proof would still support a short note, but the present packet remains below the strict micro-paper lane because the bounded 2026-04-15 later-source audit stayed too thin for a tuple of this scale.

## single_solve_explanation
Solving this exact tuple would still remove one of Gordon's named residual Table 4 cases and would therefore provide the core theorem of a short note. What would remain is light framing around the residual lambda = 3 list and exposition of the decisive elimination or construction. The packet is weaker than the smaller exact-group rows because the parameter size increases citation and packaging risk, not because it needs a feeder ladder.

## broader_theorem_nonimplication
Gordon's 2022 elimination machinery leaves this exact tuple among the surviving Table 4 cases, and the bounded tuple search did not surface a later theorem directly settling it. The conservative holdback comes from the thin later-source surface rather than any visible broader theorem that already forces the answer.

## literature_gap
Prior work surfaced in this curation stops at Gordon 2022 Table 4 leaving (4797048929975,3793567,3) among the surviving abelian lambda = 3 cases; the bounded 2026-04-15 web sweep did not surface a later direct settlement.

## transfer_kit
- lemma: Gordon 2022 Table 4 isolates (4797048929975,3793567,3) as one of the surviving abelian lambda = 3 parameter sets.
- lemma: Gordon's Theorems 2, 3, and 4 provide the elimination machinery that any future proof must sharpen or bypass.
- lemma: The order factorization v = 5^2 * 251 * 397 * 463 * 4159 and n = k - lambda = 3793564 = 2^2 * 948391 give immediate Sylow and quotient directions for contracted-count tests.
- toy example: Contract along a prime-order quotient such as 251 or 397 and test whether the surviving coefficient pattern can still realize total size 3793567 with lambda = 3.
- known obstruction: The tuple already survives Gordon's published elimination machinery, so any proof must add a genuinely sharper multiplier, quotient, or character argument.
- prior-work stop sentence: Gordon 2022 leave (4797048929975,3793567,3) among the surviving abelian lambda = 3 cases in Table 4.
- recommended first attack: Re-run Gordon's lambda = 3 machinery prime by prime on the factorization 5^2 * 251 * 397 * 463 * 4159 and look for a quotient-count contradiction that is invisible at the published Table 4 level.
- paper if solved: If solved exactly, the paper would be a short note removing one of Gordon's surviving abelian lambda = 3 Table 4 cases.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda" (Journal of Algebraic Combinatorics 55, 2022), especially Table 4 and the elimination machinery in Theorems 2, 3, and 4, which leave the exact abelian parameter set (4797048929975,3793567,3) unresolved.
- Gordon 2022 Table 4 and Theorems 2, 3, and 4, bounded exact-tuple web checks on 2026-04-15, and local attempt-registry memory.
- artifacts/abelian-difference-set-4797048929975-3793567-3/record.md
- artifacts/abelian-difference-set-4797048929975-3793567-3/status.json
