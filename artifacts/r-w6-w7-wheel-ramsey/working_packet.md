# Working Packet: The Exact Value of R(W6, W7)

- slug: `r-w6-w7-wheel-ramsey`
- title: Determine the exact value of R(W6, W7)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `54`
- single-solve-to-paper fraction: `0.63`

## statement
Determine the smallest n such that every graph on n vertices contains W6 or its complement contains W7.

## novelty_notes
- frontier basis: DS1.17 Table VIII still lists the pair as unresolved with a three-value window, and the 2025 Lidicky-McKinley-Pfender-Van Overberghe paper improved other wheel pairs without reporting an exact closure here. The classic Faudree-McKay small-wheel paper settles the smaller baseline up to order 6 but does not reach this pair.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: If solved exactly, the statement could still headline a short note because small wheel Ramsey tables are standard reference objects. The problem is lane fit: the current gap is not one, and the most plausible route looks like heavier computation or exhaustive generation rather than a compact structural argument.
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
- search-heavy: True
- certificate compactness: moderate
- exact gap from source: small
- assessment: Fail for this run. The family anchor is real, but the gap is wider, the likely solve mode is search-heavy, and the post-solve packaging is heavier than the one-shot lane allows.

## likely_paper_shape
- note title: The Exact Value of R(W6, W7)
- hypothetical title: The Exact Value of R(W6, W7)
- paper shape: A one-theorem exact-value note on a small wheel Ramsey pair, likely with substantial search or classification content.
- publication if solved: An exact value for R(W6, W7) could plausibly support a short computational-exact note on a small unresolved wheel pair.
- minimal artifact requirements: Either a proof that every 19- or 20-vertex critical candidate collapses, or one explicit extremal witness at the correct threshold together with verification of wheel avoidance.

## hypothetical_abstract
We determine the wheel Ramsey number R(W6, W7). The current survey literature leaves this small wheel pair in the range 19 <= R(W6, W7) <= 21. Our result would close one of the compact unresolved entries in the low-order wheel table.

## single_solve_explanation
A successful exact solve would certainly provide the title theorem. The issue is that the solve itself would probably require a broader classification or heavy computation, and the final note would need more packaging around certificates and search methodology than the strict micro-paper lane wants. That keeps the solve-to-paper fraction below the target band.

## broader_theorem_nonimplication
Known exact results for W5 and W6, and the recent exact closures of R(W5, W7) and R(W5, W9), do not imply the value of R(W6, W7). The current public sources still leave a three-value window.

## literature_gap
Current public sources leave R(W6, W7) in the range 19 <= R(W6, W7) <= 21, and the bounded 2026-04-13 audit did not surface a later exact determination.

## transfer_kit
- lemma: DS1.17 Table VIII records the unresolved range 19 <= R(W6, W7) <= 21.
- lemma: Faudree-McKay 1993 gives the exact baseline r(W6) = 17 and records the small-wheel computational framework.
- lemma: The 2025 wheel paper closes R(W5, W7) = 15 and R(W5, W9) = 18, showing the surrounding small-wheel table remains active.
- toy example: The exact neighboring value R(W5, W7) = 15 is a solved reference point inside the same wheel family.
- known obstruction: Any exact closure is likely to require exhaustive handling of low-order critical graphs or a search-backed witness, which pushes the dossier toward heavier certificate management.
- prior-work stop sentence: Current sources stop at 19 <= R(W6, W7) <= 21.
- recommended first attack: Refresh the exact critical-graph counts around 18 to 20 vertices before committing, because the shortest plausible route appears to be computational classification rather than a clean hand proof.
- paper if solved: The paper would be a short exact-value note on a small wheel Ramsey number, but it would likely need visible computational certification.

## bounded_source_list
- Stanislaw P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, 2024), Section 5.2 and Table VIII; Bernard Lidicky, Gwen McKinley, Florian Pfender, and Steven Van Overberghe, "Small Ramsey Numbers for Books, Wheels, and Generalizations" (Electronic Journal of Combinatorics 32(4), 2025), Section 2 and Table 1; Ralph J. Faudree and Brendan D. McKay, "A Conjecture of Erdos on the Ramsey Number r(W6)" (JCMCC 13, 1993), Table 1 and surrounding discussion for the small-wheel baseline; and bounded exact-term, alternate-notation, canonical-source, outside-source, and recent-status web checks performed on 2026-04-13.
- DS1.17 Section 5.2 and Table VIII, Lidicky-McKinley-Pfender-Van Overberghe 2025, Faudree-McKay 1993, and bounded 2026-04-13 exact-term, alternate-notation, canonical-source, outside-source, and recent-status searches for R(W6, W7).
- artifacts/r-w6-w7-wheel-ramsey/record.md
- artifacts/r-w6-w7-wheel-ramsey/status.json
