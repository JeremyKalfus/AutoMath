# Working Packet: Another Residual Abelian Biplane Table 3 Case

- slug: `abelian-biplane-difference-set-3699075079-86013-2`
- title: abelian-biplane-difference-set-3699075079-86013-2
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `False`
- paper leverage score: `63`
- single-solve-to-paper fraction: `0.67`

## statement
Determine whether any abelian group of order 3699075079 admits a (3699075079,86013,2)-difference set.

## novelty_notes
- frontier basis: Gordon's Table 3 keeps (3699075079,86013,2) among the open abelian biplane parameter sets surviving the paper's elimination pipeline.
- why still open: (not recorded)
- attempted conflict check: (not recorded)
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: A direct solve would already give the mathematical core of a note, but the note would still depend heavily on the pre-existing Table 3 narrative rather than on a naturally sharp exact theorem.
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
- certificate compactness: moderate
- exact gap from source: small
- assessment: Honest frontier backup, but still outside the lane: the family anchor is good, while the title theorem remains too much a residual-table deletion and too little a self-standing short-note theorem.

## likely_paper_shape
- note title: Another Residual Abelian Biplane Table 3 Case
- hypothetical title: On the Abelian (3699075079,86013,2)-Difference Set Problem
- paper shape: A residual-case biplane note with a clean source anchor but still a cleanup-first title theorem.
- publication if solved: A proof of existence or nonexistence would remove another unattempted residual row from Gordon's Table 3 of open abelian biplane cases.
- minimal artifact requirements: A decisive nonexistence proof via multiplier-orbit contradictions or a verifiable construction in an abelian group of order 3699075079, plus a short account of why the tuple survives Gordon's filters.

## hypothetical_abstract
We determine whether any abelian group of order 3699075079 admits a (3699075079,86013,2)-difference set. This parameter set appears in Gordon's 2022 Table 3 of residual open abelian biplane cases after the standard multiplier-based eliminations. Solving it would remove a genuine frontier row, though the resulting note would still need moderate contextual packaging around the table of survivors.

## single_solve_explanation
If the tuple is settled, the main theorem of the note is immediately in hand because the source already isolates the problem as a residual frontier case. After the solve, only bounded exposition remains: explain the abelian biplane context, restate the failed published filters, and present the decisive new argument. The result is publishable in principle, but not crisp enough to count as a strict micro-paper target.

## broader_theorem_nonimplication
The published multiplier and contracted-multiplier theorems in Gordon's paper are expressly insufficient here, since the tuple remains in Table 3 after those filters and the follow-up Lander tests are applied to most survivors.

## literature_gap
Prior work stops at listing (3699075079,86013,2) among the remaining open abelian biplane cases in Table 3 of Gordon (2022).

## transfer_kit
- lemma: For lambda = 2, the parameter equations force n = k - 2 = 86011 and v = k(k - 1)/2 + 1 = 3699075079.
- lemma: Theorem 2 in Gordon gives an orbit-count obstruction whenever a multiplier yields a prime divisor p of v with sufficiently large orbit size.
- lemma: Theorem 4 gives quotient-level multiplier control in cyclic quotients and was an important elimination tool for Table 3.
- lemma: Gordon reports that Lander's Theorems 4.19 and 4.38 dispose of many other open biplane rows, isolating this tuple as a genuine residue.
- toy example: Use the classical lambda = 2 difference-set example (16,6,2) as the baseline biplane model before scaling to the residual abelian cases.
- known obstruction: The tuple has already resisted the standard Theorem 2 and Lander-based filters, so a final proof must exploit more delicate multiplier or quotient information.
- prior-work stop sentence: Gordon (2022) still lists (3699075079,86013,2) as open in Table 3.
- recommended first attack: Exploit the factorization v = 7 x 71 x 883 x 8429 and search for a prime-divisor choice that forces impossible orbit counts under Theorem 2 for a multiplier arising from n = 86011.
- paper if solved: If solved exactly, the paper would be a short note removing one more open row from Gordon's abelian biplane table.

## bounded_source_list
- Daniel M. Gordon, "On difference sets with small lambda" (Journal of Algebraic Combinatorics 55, 2022), especially Table 3 and the elimination machinery in Theorems 2 and 4.
- Gordon 2022, together with the Hughes-Dickey and Lander references cited there for the surrounding biplane elimination program.
- artifacts/abelian-biplane-difference-set-3699075079-86013-2/record.md
- artifacts/abelian-biplane-difference-set-3699075079-86013-2/status.json
