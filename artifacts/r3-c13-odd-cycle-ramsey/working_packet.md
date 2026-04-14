# Working Packet: The Exact Value of R(C13, C13, C13)

- slug: `r3-c13-odd-cycle-ramsey`
- title: Determine the exact value of R(C13, C13, C13)
- publication status: `NONE`
- packet quality: `moderate`
- micro-paper eligible: `True`
- paper leverage score: `72`
- single-solve-to-paper fraction: `0.7`

## statement
Either prove that every 3-coloring of K49 contains a monochromatic C13, or construct a 3-coloring of K49 with no monochromatic C13 and thus show R(C13, C13, C13) >= 50.

## novelty_notes
- frontier basis: Radziszowski DS1.17 records only sufficiently-large odd-cycle exactness and identifies C9 as the first open case; bounded 2026-04-13 primary-source web checks found no exact-resolution paper for the diagonal C13 value.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no archived conflicting AutoMath mathematical status for the exact C13 three-color odd-cycle problem; the matching slug and artifact directory belong to the current live dossier rather than to a retired attempt.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The conjectural target 49, the solved C7 benchmark, and the large-n odd-cycle theorem already give the note its framing. After the main solve, only a short account of the critical construction or forcing mechanism remains.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: moderate
- editorial overhead: low
- immediate corollary headroom: low
- isolated exact-case risk: moderate
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: moderate
- assessment: Pass narrowly. The family anchor is still strong and the theorem statement is stable, but the bounded slice is farther from the first-open case and therefore slightly less leveraged than the three entries above.

## likely_paper_shape
- note title: The Exact Value of R(C13, C13, C13)
- hypothetical title: The Exact Value of R(C13, C13, C13)
- paper shape: A one-theorem exact-value note for a bounded diagonal odd-cycle Ramsey number beyond the smallest open residue.
- publication if solved: A sharp exact C13 resolution would still support a short odd-cycle Ramsey note because the conjectural 4n-3 target and large-n theory are already fixed in the literature.
- minimal artifact requirements: Either a proof that every 3-coloring of K49 contains a monochromatic C13, or one explicit 49-vertex coloring with no monochromatic C13.

## hypothetical_abstract
We determine the exact three-color Ramsey number R(C13, C13, C13). The publicly accessible Ramsey survey revision of June 7, 2024 records the odd-cycle diagonal formula only for sufficiently large lengths and does not list an exact value for C13. Our theorem adds a bounded odd-cycle exact entry to the three-color table and tests the Bondy-Erdős 4n-3 prediction at n = 13.

## single_solve_explanation
If the exact C13 value is determined, the theorem itself is already the publishable core and the rest is packaging around a known conjectural target. The remaining exposition is short because the family context and expected value 49 are already standard. This sits on the lower edge of the target band because it is farther from the first-open residue than C9.

## broader_theorem_nonimplication
The large-odd-cycle theorem in the survey applies only for sufficiently large n and does not settle the bounded diagonal C13 case, while the Bondy-Erdős line supplies only the conjectural target 49.

## literature_gap
The June 7, 2024 Ramsey survey does not report an exact value for R(C13, C13, C13).

## transfer_kit
- lemma: Radziszowski DS1.17 records that for sufficiently large odd n we have R(Cn, Cn, Cn) = 4n - 3.
- lemma: The same survey records the exact solved predecessor R(C7, C7, C7) = 25.
- lemma: The survey identifies C9 as the first open odd-cycle diagonal case, so later odd slices such as C13 remain genuinely unresolved without a general exact theorem.
- toy example: The nearest publicly solved odd-cycle diagonal case is R(C7, C7, C7) = 25, while the conjectural C13 target is 49.
- known obstruction: Any upper-bound proof must control 49-vertex colorings modeled on the standard odd-cycle blowup templates, while a disproof must produce one explicit 49-vertex witness.
- prior-work stop sentence: The June 7, 2024 Ramsey survey does not report an exact value for R(C13, C13, C13).
- recommended first attack: Use the 48-vertex conjectural lower-bound template as the starting point and show that every 49-vertex local perturbation forces a monochromatic 13-cycle.
- paper if solved: The paper would be a short exact-value contribution to the three-color odd-cycle Ramsey program.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, revision dated June 7, 2024), Section 6.3.1, together with the large-odd-cycle theorem cited there and bounded 2026-04-13 primary-source web checks.
- Radziszowski DS1.17 Section 6.3.1, the large-odd-cycle theorem cited there, the UCSD Erdős problem page for the three-color odd-cycle conjecture, and bounded 2026-04-13 searches for R(C13,C13,C13), R3(C13), and recent status signals.
- artifacts/r3-c13-odd-cycle-ramsey/record.md
- artifacts/r3-c13-odd-cycle-ramsey/status.json
