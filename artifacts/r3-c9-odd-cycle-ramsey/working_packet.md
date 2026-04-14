# Working Packet: The Exact Value of R(C9, C9, C9)

- slug: `r3-c9-odd-cycle-ramsey`
- title: Determine the exact value of R(C9, C9, C9)
- publication status: `NONE`
- packet quality: `strong`
- micro-paper eligible: `True`
- paper leverage score: `87`
- single-solve-to-paper fraction: `0.83`

## statement
Either prove that every 3-coloring of K33 contains a monochromatic C9, or construct a 3-coloring of K33 with no monochromatic C9 and thus show R(C9, C9, C9) >= 34.

## novelty_notes
- frontier basis: The June 7, 2024 Ramsey survey says the first open three-color odd-cycle diagonal case is R3(C9), with lower bound 33 and only sufficiently-large odd-cycle theorems beyond that; the current Electronic Journal of Combinatorics survey landing page and RIT survey publication list checked on 2026-04-13 still expose DS1.17 as the live survey record; the UCSD Erdős problem page still tracks the three-color odd-cycle question at the family level; and bounded 2026-04-13 exact-term and alternate-notation checks found no later exact-resolution paper for C9.
- why still open: (not recorded)
- attempted conflict check: The exclusion sweep found no archived conflicting AutoMath mathematical status for the exact C9 three-color odd-cycle problem; the matching slug and artifact directory belong to the current live dossier rather than to a retired attempt.
- rediscovery risk: (not recorded)

## proof_sketch
- attack style: (not recorded)
- likely route: The conjectural target 33, the lower-bound construction template, and the large-n odd-cycle backdrop are already in place. Once the exact C9 value is settled, what remains is a short extremal discussion and comparison with the solved C7 case.
- verifier focus: (not recorded)

## micro_paper_test
- title theorem strength: strong
- family anchor strength: strong
- publication narrative strength: strong
- editorial overhead: low
- immediate corollary headroom: moderate
- isolated exact-case risk: low
- broader-theorem implication risk: low
- theorem-slice stability: stable
- search-heavy: False
- certificate compactness: high
- exact gap from source: tiny
- assessment: Pass. This is a named first-open-case slice in a flagship exact-value family, and one clean solve would already look like the full short paper rather than a remark or a campaign stepping stone.

## likely_paper_shape
- note title: The Exact Value of R(C9, C9, C9)
- hypothetical title: The Exact Value of R(C9, C9, C9)
- paper shape: A one-theorem exact-value note on the first open three-color odd-cycle diagonal Ramsey number.
- publication if solved: Settling the first publicly recorded open three-color odd-cycle diagonal case would read immediately as the title theorem of a short Ramsey note rather than as feeder evidence.
- minimal artifact requirements: Either a proof that every 3-coloring of K33 contains a monochromatic C9, or one explicit 33-vertex coloring with no monochromatic C9.

## hypothetical_abstract
We determine the exact three-color Ramsey number R(C9, C9, C9). The publicly accessible Ramsey survey revision of June 7, 2024 records C9 as the first open odd-cycle diagonal case and gives only the lower bound 33 together with sufficiently-large odd-cycle results. Our theorem fixes the first unresolved bounded odd-cycle entry in the three-color table and tests the Bondy-Erdős 4n-3 prediction at its smallest open parameter.

## single_solve_explanation
If the exact C9 value is determined, the resulting theorem is already the title and the core contribution of the note. The conjectural target, the nearest solved benchmark C7, and the large-n odd-cycle context are standard, so the post-solve work is mostly exposition and critical-coloring discussion. This is squarely inside the 70-90% paper window because the mathematical burden is concentrated in one bounded diagonal theorem.

## broader_theorem_nonimplication
The sufficiently-large odd-cycle theorem recorded in the survey only applies for large odd n and does not settle the bounded C9 slice, while the classical Bondy-Erdős conjectural formula supplies only the target value 33, not an exact proof.

## literature_gap
The June 7, 2024 Ramsey survey states that the first open three-color odd-cycle diagonal case is R(C9, C9, C9), known only to satisfy R(C9, C9, C9) >= 33.

## transfer_kit
- lemma: Radziszowski DS1.17 states that if the Bondy-Erdős odd-cycle prediction holds, then R(Cn, Cn, Cn) = 4n - 3 for odd n, and it identifies C9 as the first open diagonal case.
- lemma: The same survey records the exact solved predecessor R(C7, C7, C7) = 25.
- lemma: The survey records that R(Cn, Cn, Cn) = 4n - 3 for sufficiently large odd n, so the only remaining difficulty is the bounded small-parameter residue.
- toy example: The nearest solved odd-cycle benchmark is R(C7, C7, C7) = 25, while the conjectural C9 target is 33.
- known obstruction: Any upper-bound proof must rule out 33-vertex colorings built from the standard odd-cycle blowup templates, while a disproof must exhibit one explicit 33-vertex witness with no monochromatic C9.
- prior-work stop sentence: The June 7, 2024 Ramsey survey states that the first open three-color odd-cycle diagonal case is R(C9, C9, C9), known only to satisfy R(C9, C9, C9) >= 33.
- recommended first attack: Start from the 32-vertex lower-bound blowup pattern behind the 4n - 3 conjecture and run a stability argument showing that every 33-vertex extension already forces a monochromatic 9-cycle.
- paper if solved: The paper would be a short exact-value note closing the first open three-color odd-cycle diagonal Ramsey number.

## bounded_source_list
- Stanisław P. Radziszowski, "Small Ramsey Numbers" (Electronic Journal of Combinatorics, Dynamic Survey DS1.17, revision dated June 7, 2024), Section 6.3.1, together with the current Electronic Journal of Combinatorics survey landing page and RIT survey publication list checked on 2026-04-13, the Bondy-Erdős odd-cycle line recorded there, the UCSD Erdős Ramsey problem page, and bounded 2026-04-13 exact-term and alternate-notation web checks.
- Radziszowski DS1.17 Section 6.3.1; the Bondy-Erdős odd-cycle conjecture record; the UCSD Erdős problem page on three-color cycle Ramsey numbers; and bounded 2026-04-13 exact-statement, alternate-notation, and status searches for the C9 diagonal case.
- artifacts/r3-c9-odd-cycle-ramsey/record.md
- artifacts/r3-c9-odd-cycle-ramsey/status.json
